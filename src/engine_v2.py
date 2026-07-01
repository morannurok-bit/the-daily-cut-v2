"""
The Daily Cut — Matching Engine (Layer 3) — reference implementation.

Implements the locked `intent_framework_v2` pipeline against the real V2 catalog.
This is the validated reference to port to Bolt/TS; the logic here is the spec.

Pipeline (per intent_framework_v2.md):
  diagnosis -> intent classifier -> candidate pull (intents + basics)
  -> body filter (best/ok/risky + override evaluation) -> context (lounge)
  -> height (scale) -> hard filters (cut/length/exposure) -> score -> group+rank

Notes on reconciliations (flagged to the team, not silent):
  * Runtime silhouette axis = the 9 intents (CSV `intents_served`, overrides
    `fired_intents`). The synthesis-layer strategy model (trace/anchor/sculpt/edge)
    was the lens for tagging body compatibility, now baked into the CSV
    body_type_*/body_modulators/override_patterns fields.
  * Body-type vocab normalized: pear<->triangle, apple<->oval.
  * Scoring (synthesis Section 4) is unwritten; the score() function below is the
    PROPOSED design built to the named factors + the style-multiplier numbers that
    ARE specified. Weights are tunable and marked.
  * Fabric tag-confidence gating: the CSV has no per-tag confidence field, so fabric
    discomforts are applied as downrank (not hard filter), per the doc's
    "uncertain => downrank" rule. Flagged as a data gap.
"""

import csv, re
from dataclasses import dataclass, field
from typing import Optional

# ----------------------------------------------------------------------------- #
# Vocab / mappings
# ----------------------------------------------------------------------------- #
BODY_ALIASES = {"pear": "triangle", "apple": "oval"}        # synthesis -> catalog
SIL_TO_CUT = {  # pants silhouette -> the 6 cut buckets the quiz lets her avoid
    "pants_skinny": "slim", "pants_slim": "slim", "pants_cigarette": "slim", "pants_tapered": "slim",
    "pants_straight": "straight", "pants_mom_fit": "straight", "pants_cargo": "straight", "pants_jogger": "straight",
    "pants_bootcut": "bootcut", "pants_flared": "flared",
    "pants_wide": "wide", "pants_culottes": "wide", "pants_paperbag": "wide",
    "pants_barrel": "barrel"}
EXPOSURE_TO_COVER = {"decollete": "neckline", "chest": "chest", "arms": "arms",
                     "shoulders": "shoulders", "legs": "legs"}
SHORT_NONPANTS = {"mid_thigh"}      # non-pants lengths that reveal legs / count "short"

def _split(s):
    return [x.strip() for x in (s or "").replace(";", ",").split(",") if x.strip()]

# ----------------------------------------------------------------------------- #
# Catalog
# ----------------------------------------------------------------------------- #
@dataclass
class Item:
    id: str; name: str; product_type: str; silhouette: str
    length_pants: str; length_nonpants: str; bottom_rise: str
    closeness_top: list; closeness_bottom: list
    color_family: str; exposure_location: list
    pattern: str; exposure_level: str
    featuring_zones: list; intents: list; strategy: list
    best: list; ok: list; risky: list
    modulators: list; fit_failures: list; scale: list; role: str
    core_style: str; adjacent_style: list; styling_flexibility: str
    fabric_behavior: str; fabric_risks: str; fabric_quality: str
    overrides: list  # list of dicts: {body_type, override_type, conditions:[str]}
    register: str = ""
    maturity: str = ""
    primary_fabric: str = ""

    @property
    def cut_family(self):
        return SIL_TO_CUT.get(self.silhouette.split(",")[0], None)

    @property
    def reveals_legs(self):
        return ("legs" in self.exposure_location
                or self.length_nonpants in SHORT_NONPANTS)


def parse_overrides(raw):
    blocks = []
    if not raw or "body_type" not in raw:
        return blocks
    for m in re.finditer(
        r"body_type:\s*([a-z_]+).*?override_type:\s*([a-z_]+).*?conditions:\s*\[(.*?)\]",
        raw, re.DOTALL):
        conds = re.findall(r'"([^"]+)"', m.group(3))
        blocks.append({"body_type": m.group(1).strip(),
                       "override_type": m.group(2).strip(),
                       "conditions": [c.strip() for c in conds]})
    return blocks


def load_catalog(path):
    items = []
    with open(path, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            items.append(Item(
                id=r["Item_ID"], name=" ".join(r["product_name"].split()),
                product_type=r["product_type"].strip(),
                silhouette=r["silhouette"].strip(),
                length_pants=r["length_pants"].strip(),
                length_nonpants=r["length_(non_pants)"].strip(),
                bottom_rise=r["bottom_rise"].strip(),
                closeness_top=_split(r["closeness_to_body_top"]),
                closeness_bottom=_split(r["closeness_to_body_bottom"]),
                color_family=r["color_family"].strip(),
                pattern=r.get("pattern", "").strip(),
                exposure_level=r.get("exposure_level", "").strip(),
                exposure_location=_split(r["exposure_location"]),
                featuring_zones=[z for z in _split(r["featuring_zones"]) if z != "none"],
                intents=_split(r["intents_served"]),
                strategy=_split(r["strategy"]),
                best=_split(r["body_type_best"]), ok=_split(r["body_type_ok"]),
                risky=_split(r["body_type_risky"]),
                modulators=_split(r["body_modulators"]),
                fit_failures=_split(r.get("fit_failures_addressed", "")),
                scale=_split(r["scale"]), role=r["item_role"].strip(),
                core_style=r["core_style"].strip(),
                adjacent_style=_split(r["adjacent_style"]),
                styling_flexibility=r.get("styling_flexibility", "").strip(),
                fabric_behavior=r.get("fabric_behavior", "").strip(),
                fabric_risks=r.get("fabric_risks", "").strip(),
                fabric_quality=r.get("fabric_quality", "").strip(),
                overrides=parse_overrides(r["override_patterns"]),
                register=r.get("register","").strip(),
                maturity=r.get("maturity_level","").strip(),
                primary_fabric=r.get("primary_fabric","").strip(),
            ))
    return items

# ----------------------------------------------------------------------------- #
# User profile (output of the holistic diagnosis)
# ----------------------------------------------------------------------------- #
@dataclass
class Profile:
    body_type: str                     # rectangle|inverted_triangle|hourglass|triangle|oval
    is_lean: bool = False
    height_tier: str = "mid"           # petite|mid|tall
    # intent-classifier raw answers
    q5a: str = "leave"                 # leave|tuck|both
    q5b: str = "no"                    # no|yes|both
    q6: str = "top_and_bottom_same"
    q6_followup: str = ""              # fitted_waist_seat|room_throughout|both
    q7_top: list = field(default_factory=list)     # close|tight|relaxed|oversized
    q7_bottom: list = field(default_factory=list)  # close|tight|relaxed
    featuring_zones: list = field(default_factory=list)
    q12_exposure: str = "comfortable" # comfortable|only_a_little|prefer_coverage
    exposure_covers: list = field(default_factory=list)
    # color & pattern (Part 4)
    go_to_colors: list = field(default_factory=list)
    print_opinion: str = "subtle_ok"         # solid|subtle_ok|likes_prints
    quality_sensitivity: str = "important"    # very|important|not  (Part2 Q1 fabric importance)
    style_range: str = "stay_close"    # stay_close|little_stretch|discovering
    # accepted sets (acceptance conditions)
    cut_accepted: list = field(default_factory=list)
    rise_accepted: list = field(default_factory=list)
    length_skirts_accepted: list = field(default_factory=list)
    # hard-filter prefs
    cut_avoid: list = field(default_factory=list)
    length_pants_avoid: list = field(default_factory=list)
    category_avoid: list = field(default_factory=list)   # {"pants","dress_skirt"} from "I don't wear..." opt-outs
    fabric_discomforts: list = field(default_factory=list)   # clingy|stiff|sheer|heavy|wrinkly
    # style — thumbnail verdicts: styles_yes='would wear', styles_no="wouldn't wear"
    styles_yes: list = field(default_factory=list)
    styles_no: list = field(default_factory=list)
    worlds_wear_some: list = field(default_factory=list)   # 'some pieces' thumbnails
    clicked_heroes: list = field(default_factory=list)      # [(world, category)] hero clicks in wear-some
    # style_range (above) is the adventurousness dial: stay_close|little_stretch|discovering
    # modulator-relevant variation signals
    modulator_signals: list = field(default_factory=list)
    # fit failures she wants solved (Q4): has_stretch (pulls at thighs/waist/hips) | long_inseam (pants too short)
    fit_failure_signals: list = field(default_factory=list)
    # context
    context: str = "default"           # default|lounge
    # derived
    fired_intents: list = field(default_factory=list)
    permissiveness: str = "medium"

    def norm_body(self):
        return BODY_ALIASES.get(self.body_type, self.body_type)

    @property
    def accepted_top(self):    return self.q7_top
    @property
    def accepted_bottom(self): return self.q7_bottom


# ----------------------------------------------------------------------------- #
# Intent classifier (the 9 patterns, per intent_framework_v2)
# ----------------------------------------------------------------------------- #
def classify_intents(p: Profile):
    t, b, f = set(p.q7_top), set(p.q7_bottom), set(p.featuring_zones)
    q6 = set(p.q6) if isinstance(p.q6, (list, set)) else {p.q6}   # Q6 is multi-select
    leaves  = p.q5a in ("leave", "both")    # 'both' = open to either
    tucks   = p.q5a in ("tuck", "both")
    nobuild = p.q5b in ("no", "both")
    builds  = p.q5b in ("yes", "both")
    fired = []

    # Intent 1 — vertical body line, no waist event
    if (leaves and nobuild and "top_and_bottom_same" in q6
            and (t & {"close", "tight"}) and t != {"oversized"}
            and (b & {"close", "tight"})):
        fired.append("intent_1")

    # Intent 2 — independent definer: structure on HER terms. She decides if/when/how a
    #            waist appears; the garment must AFFORD that (strategy=styling_anchor), never
    #            impose it (a wrap/built-in cinch is the garment deciding → Intent 3).
    # Tucking to define the waist is a TOP move — it works over any bottom (slim, balanced,
    # or wide). intent_2 must NOT gate on bottom proportion: a tucker who builds her own waist
    # (and lets the garment afford it, not impose it) is a definer regardless of leg width.
    # Lower-body volume is intent_4's job, not this one.
    if tucks and nobuild:
        fired.append("intent_2")

    # Intent 3 — garment builds the silhouette
    if builds:
        fired.append("intent_3")

    # Intent 4 — build/balance the lower body through proportion
    if (tucks and "slimmer_top_more_room_on_bottom" in q6
            and p.q6_followup in ("room_throughout", "fitted_waist_seat", "both")
            and ("relaxed" in b)):
        fired.append("intent_4")

    # Intent 5 — elongated lower body (room on top, slim bottom)
    if (leaves and nobuild and "more_room_on_top_slimmer_bottom" in q6
            and (t & {"relaxed", "oversized"}) and (b & {"close", "tight"})):
        fired.append("intent_5")

    # Intent 6 — step back from body
    if (leaves and nobuild and "top_and_bottom_same" in q6
            and (t & {"relaxed", "oversized"}) and ("relaxed" in b)):
        fired.append("intent_6")

    # Intent 7 — multi-modal / plays across modes (body/strategy read, not taste)
    if (p.q5a == "both" and p.q5b == "both" and p.q6_followup == "both"
            and len(t) >= 2 and len(b) >= 2):
        fired.append("intent_7")

    # Intent 8 — RETIRED. "Refined coverage" was not a distinct silhouette move: coverage
    #            is the exposure axis (Q12 + covered zones), composure is Intent 2, and polish
    #            is the style layer. Nothing it surfaced was otherwise unreachable.

    # Intent 9 — relaxed body, open to showing an opening (keyed to exposure, not featuring)
    if (leaves and nobuild
            and (q6 & {"top_and_bottom_same", "more_room_on_top_slimmer_bottom"})
            and (t & {"relaxed", "oversized"}) and ("relaxed" in b)
            and p.q12_exposure in ("comfortable", "only_a_little")):
        fired.append("intent_9")

    return fired


# ----------------------------------------------------------------------------- #
# Override condition evaluation
# ----------------------------------------------------------------------------- #
def _accepted_set(p: Profile, key):
    return {
        "pants_cuts_accepted": p.cut_accepted,
        "closeness_to_body_top_accepted": p.accepted_top,
        "closeness_to_body_bottom_accepted": p.accepted_bottom,
        "bottom_rise_accepted": p.rise_accepted,
        "length_skirts_dresses_accepted": p.length_skirts_accepted,
    }.get(key, [])

def eval_condition(cond: str, p: Profile) -> bool:
    cond = cond.strip()
    if " does NOT include " in cond:
        key, val = cond.split(" does NOT include ")
        opts = [v.strip() for v in val.split(" OR ")]
        target = p.exposure_covers if key.strip() == "exposure_covers" else _accepted_set(p, key.strip())
        return not any(o in target for o in opts)
    if cond.startswith("Q6 ="):
        return p.q6 == cond.split("=", 1)[1].strip()
    if " includes " in cond:
        key, val = cond.split(" includes ")
        key = key.strip()
        opts = [v.strip() for v in val.split(" OR ")]
        if key == "featuring_zones":   target = p.featuring_zones
        elif key == "fired_intents":   target = p.fired_intents
        elif key == "exposure_covers": target = p.exposure_covers
        else:                          target = _accepted_set(p, key)
        return any(o in target for o in opts)
    return False   # unknown condition form -> fail closed

def override_fires(item: Item, p: Profile):
    """Return the override block that fires for this user, or None."""
    body = p.norm_body()
    for blk in item.overrides:
        if blk["body_type"] != body:
            continue
        if all(eval_condition(c, p) for c in blk["conditions"]):
            return blk
    return None


# ----------------------------------------------------------------------------- #
# Body / context / height / hard filters
# ----------------------------------------------------------------------------- #
def _body_tokens(p: Profile):
    body = p.norm_body()
    toks = {body}
    if p.is_lean:
        toks.add(body + "_lean")
    return toks

def body_bucket(item: Item, p: Profile):
    toks = _body_tokens(p)
    # general tag matches general+lean; lean tag matches only lean (handled by toks)
    if toks & set(item.best):  return "best"
    if toks & set(item.risky): return "risky"
    if toks & set(item.ok):    return "ok"
    return "unlisted"

# --- Scale: band gate + asymmetric (downward-only) one-notch tolerance ---------
TIER_INDEX = {"petite": 0, "mid_short": 1, "mid_tall": 2, "tall": 3, "tall_plus": 3}
TAG_INDEX = {"petite_friendly": 0, "mid_short_friendly": 1, "mid_tall_friendly": 2,
             "tall_friendly": 3, "tall_required": 3}
HEMMABLE_CUTS = {"slim", "straight", "mom_fit", "wide"}   # straight-profile legs hem cleanly (cigarette->slim); shaped cuts (flared/bootcut/barrel) do not

def is_length_critical(it: Item):
    return it.length_pants == "full" or it.length_nonpants == "midi"

def garment_forgiving(it: Item):
    # has slack to absorb a touch of extra length/size
    if set(it.closeness_top + it.closeness_bottom) & {"relaxed", "oversized"}:
        return True
    if it.length_nonpants in {"hip", "mid_thigh"} or it.length_pants == "cropped":
        return True
    if not it.intents and it.role == "basic":   # a plain basic tee slides
        return True
    return False

def user_has_scale_slack(p: Profile):
    if p.q5a in ("tuck", "both"):                    return True   # can tuck length away
    if set(p.q7_top + p.q7_bottom) & {"relaxed", "oversized"}: return True
    if p.q6 != "not_much_extra_room":                return True   # accepts some room
    return False


# --- Permissiveness dial (fit-flexibility) ------------------------------------ #
# Spine = styling agency + closeness breadth; restriction load only deepens
# restrictive (few exclusions != flexibility). Returns restrictive|mixed|permissive.
def fit_permissiveness(p: Profile):
    agency = (1 if p.q5a in ("tuck", "both") else 0) + (1 if p.q5b in ("yes", "both") else 0)
    breadth = (1 if len(set(p.q7_top)) >= 3 else 0) + (1 if len(set(p.q7_bottom)) >= 3 else 0)
    spine = agency + breadth
    base = "restrictive" if spine <= 1 else "mixed" if spine == 2 else "permissive"
    load = 0
    if p.q12_exposure == "prefer_coverage" or len(p.exposure_covers) >= 3: load += 1
    if len(p.fabric_discomforts) >= 3:        load += 1
    if len(p.cut_avoid) >= 2:                 load += 1
    if len(set(p.rise_accepted)) == 1:        load += 1
    if 0 < len(set(p.length_skirts_accepted)) <= 1: load += 1
    if load >= 3:
        base = {"permissive": "mixed", "mixed": "restrictive",
                "restrictive": "restrictive"}[base]
    return base

def hemmable_pant(it: Item):
    return it.length_pants == "full" and it.cut_family in HEMMABLE_CUTS

def scale_match(item: Item, p: Profile):
    """Return (ok, factor, flags). Tolerance is downward-only: you can shorten/
    hem/tuck a too-long item, never lengthen a too-short one."""
    band = sorted({TAG_INDEX[t] for t in item.scale if t in TAG_INDEX})
    if not band:
        return True, 1.0, []                          # untagged -> neutral allow
    u = TIER_INDEX.get(p.height_tier, 1)
    if u in band:
        return True, 1.0, []                          # in-band, full match
    required = any(t.endswith("_required") for t in item.scale)
    if u > band[-1]:                                  # user taller than band -> too short
        return False, 0.0, []                         # cannot add length: no upward notch
    dist = band[0] - u                                # user shorter than band -> too long
    if required or dist >= 3:
        return False, 0.0, []
    # too long by 1-2 tiers (downward tolerance: shorten, never lengthen)
    if is_length_critical(item):
        if hemmable_pant(item):                        # hemming is baseline; bridges up to 2 tiers
            if dist == 2 and u == 0:                   # petite: hemming fixes hem, not a 2-tier-taller rise
                return False, 0.0, []
            return True, (0.85 if dist == 1 else 0.65), ["hem_to_length"]
        return False, 0.0, []                          # midi+ dress/skirt or shaped pant: strict
    if dist >= 2:
        return False, 0.0, []                          # non-pant garments: one tier of tolerance only
    if item.length_nonpants in {"hip", "waist"}:      # tops: extra length tucks or just sits longer
        return True, 0.9, ["top_length_lenient"]
    if garment_forgiving(item) and fit_permissiveness(p) != "restrictive":
        return True, 0.8, ["scale_notch"]
    return False, 0.0, []                             # restrictive user / firm garment: strict

EXPOSURE_LADDER = {"none": 0, "low": 1, "medium": 2, "medium_high": 3, "high": 4}
# Q5 comfort -> highest exposure_level she'll see (a GATE; covers handle zones separately).
EXPOSURE_CEILING = {"prefer_coverage": "low", "only_a_little": "medium", "comfortable": "high"}

# Category red-lines from the "I don't wear..." opt-outs (cut/length/dress-length questions).
# "pants" excludes full-length pants/jeans only — shorts are handled by the legs exposure-cover,
# not here (per the quiz's "if you don't wear shorts, we'll address that later" note).
CATEGORY_AVOID_TYPES = {
    "pants":       {"jeans", "trousers"},
    "dress_skirt": {"dress", "skirt"},
}
# A co-ord set can hide the avoided category in its silhouette (e.g. "top_standard,pants_wide").
CATEGORY_AVOID_COORD_FRAG = {
    "pants":       ("pants",),
    "dress_skirt": ("skirt",),
}

def hard_filter_reason(item: Item, p: Profile):
    # category red-lines ("I don't wear pants/jeans" / "I don't wear dresses/skirts")
    for cat in p.category_avoid:
        if item.product_type in CATEGORY_AVOID_TYPES.get(cat, set()):
            return f"product_type '{item.product_type}' in user category-avoid ({cat})"
        if item.product_type == "co-ord-sets":
            for frag in CATEGORY_AVOID_COORD_FRAG.get(cat, ()):
                if frag in item.silhouette.lower():
                    return f"co-ord contains '{frag}' but user avoids {cat}"
    # cut avoid (pants)
    if item.cut_family and item.cut_family in p.cut_avoid:
        return f"cut '{item.cut_family}' in user avoid"
    # pants length avoid
    if item.length_pants and item.length_pants in p.length_pants_avoid:
        return f"pant length '{item.length_pants}' in user avoid"
    # exposure covers (zone gate)
    for loc in item.exposure_location:
        cover = EXPOSURE_TO_COVER.get(loc)
        if cover and cover in p.exposure_covers:
            return f"exposes '{loc}' but user covers '{cover}'"
    if item.reveals_legs and "legs" in p.exposure_covers:
        return "reveals legs but user covers legs"
    # exposure level (degree gate) — above her comfort ceiling = out (hard line, no penalty band)
    ceil = EXPOSURE_CEILING.get(p.q12_exposure, "high")
    if item.exposure_level and EXPOSURE_LADDER.get(item.exposure_level, 0) > EXPOSURE_LADDER.get(ceil, 4):
        return f"exposure_level '{item.exposure_level}' exceeds '{p.q12_exposure}' ceiling ({ceil})"
    return None


# ----------------------------------------------------------------------------- #
# Strong-preference penalties (Bucket 2) — gradient, modulated by permissiveness
# ----------------------------------------------------------------------------- #
PENALTY_TABLE = {   # permissiveness -> {distance: score multiplier}  (tunable)
    "restrictive": {0: 1.0, 1: 0.25, 2: 0.05},
    "mixed":       {0: 1.0, 1: 0.60, 2: 0.30},
    "permissive":  {0: 1.0, 1: 0.85, 2: 0.60},
}
CLOSE_LADDER = {"tight": 0, "close": 1, "relaxed": 2, "oversized": 3}
EXTREMES = {0, 3}   # tight & oversized: deliberate looks — hard-gated if she didn't choose them; close/relaxed (the middle) is a penalty
RISE_LADDER  = {"low": 0, "mid": 1, "high": 2}
SKIRT_LEN_LADDER = {"mid_thigh": 0, "short": 0, "midi": 1, "long": 2}
FABRIC_SYNONYMS = {  # discomfort -> substrings sought in behavior + risks
    "clingy": ["cling", "shows_lines", "shows lines"],
    "stiff":  ["stiff"],
    "sheer":  ["sheer", "see_through", "see through", "transparent"],
    "heavy":  ["heavy"],
    "wrinkly": ["wrinkle"],
}

def _closeness_region(item_vals, user_vals, body_following=False, releasing=False):
    iv = sorted({CLOSE_LADDER[v] for v in item_vals if v in CLOSE_LADDER})
    uv = {CLOSE_LADDER[v] for v in user_vals if v in CLOSE_LADDER}
    if not iv or not uv:    return ("ok", 0)
    # a CLOSE grip-and-expand cut (A-line / fit-flare) releases over the body -> also serves relaxed
    if releasing and CLOSE_LADDER["close"] in iv:
        iv = sorted(set(iv) | {CLOSE_LADDER["relaxed"]})
    if set(iv) & uv:        return ("ok", 0)             # she chose this closeness (incl. released-relaxed)
    # a CLOSE item in a body-following fabric (skim/cling) reads body-conscious like tight:
    # rule it out for anyone who didn't choose close-or-tighter
    if (body_following and CLOSE_LADDER["close"] in iv
            and not (uv & {CLOSE_LADDER["tight"], CLOSE_LADDER["close"]})):
        return ("gate", 0)
    middles = [i for i in iv if i not in EXTREMES]       # close/relaxed values the item offers
    if not middles:         return ("gate", 0)           # item only sits at an unchosen extreme (tight/oversized)
    d = min(abs(i - u) for i in middles for u in uv)     # else: middle mismatch -> distance penalty
    return ("ok", min(2, d))

def closeness_eval(item: Item, p: Profile):
    follows = any(w in (item.fabric_behavior or "").lower() for w in ("skim", "cling"))
    releasing = any(w in (item.silhouette or "").lower() for w in ("a_line", "fit_flare"))
    top = _closeness_region(item.closeness_top, p.q7_top, follows)                 # bodice stays honest
    bot = _closeness_region(item.closeness_bottom, p.q7_bottom, follows, releasing) # skirt body releases
    if top[0] == "gate" or bot[0] == "gate":
        return ("gate", 0)
    return ("ok", max(top[1], bot[1]))                   # worst region drives it

def rise_distance(item: Item, p: Profile):
    if item.bottom_rise not in RISE_LADDER or not p.rise_accepted:
        return 0
    ii = RISE_LADDER[item.bottom_rise]
    d = [abs(ii - RISE_LADDER[r]) for r in p.rise_accepted if r in RISE_LADDER]
    return min(2, min(d)) if d else 0

def length_distance(item: Item, p: Profile):
    L = item.length_nonpants
    if L not in SKIRT_LEN_LADDER or not p.length_skirts_accepted:
        return 0
    if item.product_type and not any(k in item.product_type.lower()
                                     for k in ("skirt", "dress")):
        return 0                                         # only skirts/dresses
    ii = SKIRT_LEN_LADDER[L]
    d = [abs(ii - SKIRT_LEN_LADDER[a]) for a in p.length_skirts_accepted
         if a in SKIRT_LEN_LADDER]
    return min(2, min(d)) if d else 0

def fabric_distance(item: Item, p: Profile):
    if not p.fabric_discomforts:
        return 0
    hay = (item.fabric_behavior + " " + item.fabric_risks).lower()
    matches = 0
    for disc in p.fabric_discomforts:
        if any(syn in hay for syn in FABRIC_SYNONYMS.get(disc, [disc])):
            matches += 1
    return min(2, matches)

def preference_penalties(item: Item, p: Profile, perm: str):
    """Return (gate, factor, reasons). gate=True if closeness tighter-floor fires."""
    tbl = PENALTY_TABLE[perm]
    close = closeness_eval(item, p)
    if close[0] == "gate":
        return (True, 0.0, ["closeness tighter than chosen (floor)"])
    factor, reasons = 1.0, []
    for label, d in (("closeness", close[1]), ("rise", rise_distance(item, p)),
                     ("length", length_distance(item, p)), ("fabric", fabric_distance(item, p))):
        if d > 0:
            m = tbl[d]
            factor *= m
            reasons.append(f"{label} off {d} (×{m})")
    return (False, round(factor, 3), reasons)


# ----------------------------------------------------------------------------- #
# Scoring  ***PROPOSED Section-4 design — weights tunable***
# ----------------------------------------------------------------------------- #
# Coarse category for the hero category-restriction (clicked-hero unlock).
PRODUCT_CATEGORY = {
    "t-shirt": "top", "shirt": "top", "button_down": "top", "top": "top", "tank": "top",
    "jeans": "bottom", "shorts_or_bermudas": "bottom", "trousers": "bottom", "skirt": "bottom",
    "dress": "dress", "co-ord-sets": "set",
}
def item_category(item: Item):
    return PRODUCT_CATEGORY.get(item.product_type, "other")

STYLE_PERMISSION = {"stay_close": "low", "little_stretch": "medium", "discovering": "high"}

def _reg_base(r):
    for b in ("feminine_elegant","feminine_sexy","feminine_sweet","feminine_romantic","masculine","neutral"):
        if r.startswith(b): return b
    return r

_INTEN_RANK = {"subtle":0,"moderate":1,"pronounced":2}
_THUMB_WORLD = {"refined":"refined_casual","cool_casual":"cool_casual","cool_tlv":"cool_tlv",
                "formal":"formal_polished","sexy":"sexy","urban":"urban_ease","whimsical":"whimsical"}
# (look, slot, kind C/A, register, intensity, maturity)
_THUMB_PIECES = [
 ("refined","top","C","feminine_elegant","subtle","classic"),("refined","layer","C","masculine","moderate","classic"),
 ("refined","bottom","C","neutral","subtle","classic"),("refined","shoes","A","neutral","subtle","classic"),("refined","bag","A","neutral","subtle","classic"),
 ("cool_casual","top","C","neutral","moderate","young"),("cool_casual","bottom","C","neutral","subtle","classic"),
 ("cool_casual","shoes","A","neutral","subtle","young"),("cool_casual","bag","A","neutral","subtle","young"),
 ("cool_tlv","top","C","masculine","subtle","classic"),("cool_tlv","bottom","C","masculine","subtle","classic"),
 ("cool_tlv","shoes","A","neutral","subtle","young"),("cool_tlv","bag","A","feminine_sweet","moderate","young"),
 ("formal","top","C","masculine","subtle","mature"),("formal","bottom","C","masculine","moderate","mature"),
 ("formal","shoes","A","feminine_elegant","moderate","mature"),("formal","bag","A","feminine_elegant","subtle","mature"),
 ("sexy","top","C","feminine_sexy","pronounced","young"),("sexy","bottom","C","neutral","subtle","classic"),
 ("sexy","shoes","A","feminine_sexy","moderate","young"),("sexy","bag","A","feminine_sexy","moderate","young"),
 ("urban","top","C","neutral","pronounced","young"),("urban","bottom","C","neutral","subtle","classic"),
 ("urban","shoes","A","neutral","moderate","young"),("urban","bag","A","neutral","subtle","classic"),("urban","hat","A","neutral","subtle","young"),
 ("whimsical","top","C","feminine_romantic","moderate","classic"),("whimsical","bottom","C","feminine_sweet","pronounced","young"),
 ("whimsical","shoes","A","feminine_sweet","moderate","classic"),("whimsical","bag","A","feminine_romantic","moderate","young"),
]
_PALETTE_UNIVERSAL = {"gray","grey","navy","denim"}
_SOFT_NEUTRAL = {"neutral","neutrals","cream","beige","tan","camel"}

def build_axis(answers, go_to_colors):
    """L2: thumbnail answers {look:(verdict,{slots})} -> axis profile (fully profile-driven)."""
    taken, rejected = [], []
    for look,slot,kind,reg,inten,mat in _THUMB_PIECES:
        v,slots = answers.get(look,("no",set()))
        pc = dict(reg=reg,inten=inten,mat=mat,kind=kind)
        (taken if (v=="yes" or (v=="some" and slot in slots)) else rejected).append(pc)
    regs={p[3] for p in _THUMB_PIECES}
    liked={r for r in regs if any(p["reg"]==r for p in taken)}
    avoid={r for r in regs if r not in liked and any(p["reg"]==r for p in rejected)}
    # intensity ceiling = loudest she TOOK
    ceil = max((_INTEN_RANK[p["inten"]] for p in taken), default=1)
    # maturity avoid = maturities present ONLY in rejected clothing (never taken in clothing)
    taken_cloth_mat={p["mat"] for p in taken if p["kind"]=="C"}
    rej_cloth_mat={p["mat"] for p in rejected if p["kind"]=="C"}
    mat_avoid=rej_cloth_mat - taken_cloth_mat
    mod_plus=set()
    for look,(v,slots) in answers.items():
        if v=="no": continue
        looks=[p for p in _THUMB_PIECES if p[0]==look]
        tc=[p for p in looks if (v=="yes" or p[1] in slots) and p[2]=="C"]
        ta=[p for p in looks if (v=="yes" or p[1] in slots) and p[2]=="A"]
        if len(tc)>=2 or (len(tc)>=1 and len(ta)>=1): mod_plus.add(_THUMB_WORLD[look])
    palette={c.strip().lower() for c in go_to_colors} | _PALETTE_UNIVERSAL
    if palette & _SOFT_NEUTRAL: palette |= _SOFT_NEUTRAL   # picked "neutrals" -> accept the soft-neutral family
    return dict(liked_registers=liked, avoid_registers=avoid, mod_plus_worlds=mod_plus,
                palette=palette, intensity_ceiling=ceil, maturity_avoid=mat_avoid)

def style_eval(item: Item, p: Profile):
    """Option A: world-affinity primary; register/intensity/maturity refine (all from her axis); bounded leakage."""
    ax = getattr(p, "axis", None)
    if ax is None: return True, 1.0, "no-axis"
    reg=_reg_base(item.register); inten=item.register.split("_")[-1]
    col=item.color_family.split(",")[0].strip().lower()
    # denim's basic washes are category-basics, not statement colors: a jean is palette-exempt
    # for blue/indigo/denim even if she didn't pick blue (not picking blue != avoiding it).
    is_denim = item.product_type=="jeans" or "denim" in (item.primary_fabric or "").lower()
    denim_basic = col in ("blue","indigo","denim")
    if col and col not in ax["palette"] and not (is_denim and denim_basic):
        return False,0.0,f"palette {col} off"
    if reg in ax["avoid_registers"]:                            return False,0.0,f"{reg} avoid"
    if _INTEN_RANK.get(inten,0) > ax["intensity_ceiling"]:      return False,0.0,f"{inten}>ceiling"
    mat_f = 0.5 if item.maturity in ax["maturity_avoid"] else 1.0
    if not item.core_style:                                     return True, mat_f, f"basic·{reg}"
    if reg not in ax["liked_registers"]:                        return False,0.0,f"{reg} not liked"
    if item.core_style in ax["mod_plus_worlds"]:                return True, mat_f, f"{reg}·{item.core_style}"
    return False,0.0,f"{item.core_style} weak world"


def effective_intents(item: Item, p: Profile):
    """An item's intents as they apply to THIS woman. Two affordances are intents, not hand
       tags: a styling_anchor item can carry her self-defined waist (Intent 2), and an 'open'
       (multi-modal) item is hers to play with (Intent 7). Each counts only when she fires it."""
    eff = set(item.intents)
    if "intent_2" in p.fired_intents and "styling_anchor" in item.strategy:
        eff.add("intent_2")
    if "intent_7" in p.fired_intents and item.styling_flexibility == "open":
        eff.add("intent_7")
    return eff


# Color personality is INFERRED from her picks (go-to colors + print opinion), not self-reported.
BASIC_COLORS = {"black", "white", "gray", "grey", "brown", "blue", "neutral", "neutrals",
                "navy", "denim", "beige", "cream", "tan"}
PRINT_RANK = {"solid": 0, "subtle_ok": 1, "likes_prints": 2}

def item_color_level(item: Item):
    """0 basic+solid (universal backbone) · 1 statement color, solid · 2 tempered bold (statement
       softened by a neutral, e.g. red,neutral stripe) · 3 full bold (pure statement + bold)."""
    fams = {f.strip().lower() for f in item.color_family.replace(";", ",").split(",") if f.strip()}
    statement = fams - BASIC_COLORS
    color_rank = 0 if (not statement or (fams & BASIC_COLORS)) else 1  # basic/tempered 0, pure statement 1
    pattern_rank = 2 if item.pattern == "bold" else 0
    return color_rank + pattern_rank

def woman_color_level(p: Profile):
    """Inferred: did she pick any non-basic color (+1), plus how open she is to prints (0/1/2)."""
    has_statement = 1 if any(c.strip().lower() not in BASIC_COLORS for c in p.go_to_colors) else 0
    return min(3, has_statement + PRINT_RANK.get(p.print_opinion, 1))

def color_boost(item: Item, p: Profile):
    """Soft ladder, never gates. Basics (level 0) are universal. An item above her level is
       demoted so safer pieces lead; her specific go-to colors get a lift so they come first."""
    over = item_color_level(item) - woman_color_level(p)
    b = 1.0 if over <= 0 else (0.9 if over == 1 else 0.8)
    fams = {f.strip().lower() for f in item.color_family.replace(";", ",").split(",") if f.strip()}
    if (fams - BASIC_COLORS) & {c.strip().lower() for c in p.go_to_colors}:  # her chosen statement color
        b += 0.06
    return round(b, 3)


QUALITY_BOOST = {"very": 0.06, "important": 0.03, "not": 0.0}  # lift on 'high' items, by how much she cares

def quality_boost(item: Item, p: Profile):
    """Light, boost-only. Women who care about fabric quality get high-quality pieces lifted;
       'acceptable' pieces are never demoted (we don't gate quality, just reward it)."""
    if item.fabric_quality == "high":
        return round(1.0 + QUALITY_BOOST.get(p.quality_sensitivity, 0.0), 3)
    return 1.0


def score(item: Item, p: Profile, bucket: str):
    base = 1.0
    base += 0.5 if bucket == "best" else 0.0
    base += 0.1 * len(effective_intents(item, p) & set(p.fired_intents))     # intent depth
    base += 0.15 * len(set(item.featuring_zones) & set(p.featuring_zones))  # zone overlap
    base += 0.15 * len(set(item.modulators) & set(p.modulator_signals))     # modulator match
    base += 0.12 * len(set(item.fit_failures) & set(p.fit_failure_signals)) # fit-failure addressed (stretch / inseam)
    _, style_boost, _ = style_eval(item, p)
    return round(base * style_boost * color_boost(item, p) * quality_boost(item, p), 3)


# ----------------------------------------------------------------------------- #
# Pipeline
# ----------------------------------------------------------------------------- #
@dataclass
class Rec:
    item: Item; score: float; bucket: str; reasons: list

def run(catalog, p: Profile, verbose_trace=False):
    p.fired_intents = classify_intents(p)
    fired = set(p.fired_intents)
    perm = fit_permissiveness(p)
    trace = {"fired_intents": list(fired), "permissiveness": perm, "stages": []}

    # 1. candidate pull: intent match OR universal basic. Intent 2 pulls on the affordance
    #    (strategy=styling_anchor), so tuckable pieces reach her without a hand-applied tag.
    candidates = []
    for it in catalog:
        if (effective_intents(it, p) & fired) or (not it.intents and it.role == "basic"):
            candidates.append(it)
    trace["stages"].append(("candidate_pull", [c.id for c in candidates]))

    recs, dropped = [], []
    for it in candidates:
        reasons = []
        served = effective_intents(it, p) & fired
        if served:
            reasons.append("serves " + ",".join(sorted(served)))
        else:
            reasons.append("universal basic")

        # 2. body filter (+ override) — basics skip body filter (all-ok by convention)
        bucket = body_bucket(it, p)
        if it.intents:  # basics are body-neutral
            if bucket == "risky":
                if p.context == "lounge":
                    reasons.append("risky softened by lounge context")
                    bucket = "ok"
                else:
                    blk = override_fires(it, p)
                    if blk:
                        reasons.append(f"risky overridden via {blk['override_type']}")
                        bucket = "ok"
                    else:
                        dropped.append((it.id, "body-risky, no override")); continue
            elif bucket == "best":
                reasons.append("body_type best")

        # 3. scale (band gate + downward-only notch)
        ok, scale_factor, scale_flags = scale_match(it, p)
        if not ok:
            dropped.append((it.id, f"scale {it.scale} vs {p.height_tier}")); continue
        for fl in scale_flags:
            reasons.append(fl)

        # 4. hard filters
        hf = hard_filter_reason(it, p)
        if hf:
            dropped.append((it.id, hf)); continue

        # 5. strong-preference penalties (closeness floor gates; rest compound, dial-bent)
        pen_gate, pen_factor, pen_reasons = preference_penalties(it, p, perm)
        if pen_gate:
            dropped.append((it.id, pen_reasons[0])); continue
        reasons.extend(pen_reasons)

        # 6. style/taste — adventurousness gate (world × role × permission) + boost
        s_ok, _, s_reason = style_eval(it, p)
        if not s_ok:
            dropped.append((it.id, s_reason)); continue
        reasons.append(s_reason)
        sc = round(score(it, p, bucket) * scale_factor * pen_factor, 3)
        recs.append(Rec(it, sc, bucket, reasons))

    trace["dropped"] = dropped

    # 6. rank: SCORE-DOMINANT. Role is a gentle boost, not a grouping — so the best
    #    matches always lead, statement pieces edge ahead among comparable items, and a
    #    penalized item sinks no matter its role. (boost spread is tunable)
    ROLE_BOOST = {"hero": 1.08, "bridge": 1.0, "basic": 0.92}
    recs.sort(key=lambda r: -(r.score * ROLE_BOOST.get(r.item.role, 1.0)))
    return recs, trace


# ----------------------------------------------------------------------------- #
# Demo
# ----------------------------------------------------------------------------- #
def show(title, catalog, p):
    recs, trace = run(catalog, p)
    print("=" * 78)
    print(title)
    print(f"  body={p.norm_body()} lean={p.is_lean} height={p.height_tier} context={p.context}")
    print(f"  STYLE: would={p.styles_yes} wear_some={p.worlds_wear_some} "
          f"clicked={p.clicked_heroes} permission={STYLE_PERMISSION.get(p.style_range)}({p.style_range})")
    print(f"  FIRED INTENTS: {trace['fired_intents'] or '(none)'}")
    print("-" * 78)
    for r in recs:
        print(f"   {r.score:>5}  #{r.item.id:>2} [{r.item.role[:6]:>6}] "
              f"{r.item.name[:32]:32} ({r.bucket}) — {'; '.join(r.reasons)}")
    print(f"  …{len(recs)} surfaced, {len(trace['dropped'])} dropped")
    if trace["dropped"]:
        print("   dropped:", ", ".join(f"#{i}({why})" for i, why in trace["dropped"][:8])
              + (" …" if len(trace["dropped"]) > 8 else ""))


if __name__ == "__main__":
    catalog = load_catalog("/mnt/project/V2Grid_view_40.csv")
    print(f"Loaded {len(catalog)} items.\n")

    # Profile 1 — Mom-like: mid hourglass, refined_casual, waist-event tuck
    mom = Profile(
        body_type="hourglass", height_tier="mid",
        q5a="tuck", q5b="no", q6="top_and_bottom_same",
        q7_top=["close"], q7_bottom=["close", "tight"],
        featuring_zones=["waist"], q12_exposure="only_a_little", exposure_covers=[],
        cut_accepted=["straight", "slim", "wide"], rise_accepted=["high", "mid"],
        length_skirts_accepted=["midi"], styles_yes=["refined_casual"],
        modulator_signals=["full_bust_friendly"])
    show("PROFILE 1 — Mom-like (mid hourglass, refined_casual, waist tuck)", catalog, mom)
    print()

    # Profile 2 — Lora-like: petite rectangle, cool_casual, step-back, covers legs
    lora = Profile(
        body_type="rectangle", height_tier="petite",
        q5a="leave", q5b="no", q6="top_and_bottom_same",
        q7_top=["relaxed"], q7_bottom=["relaxed"], featuring_zones=[],
        q12_exposure="prefer_coverage", exposure_covers=["legs"],
        cut_accepted=["straight", "wide"], rise_accepted=["high", "mid"],
        length_skirts_accepted=[], styles_yes=["cool_casual"])
    show("PROFILE 2 — Lora-like (petite rectangle, cool_casual, step-back, covers legs)",
         catalog, lora)
    print()

    # Profile 3 — triangle, leg-feature Intent 5, to exercise overrides
    tri = Profile(
        body_type="triangle", height_tier="mid",
        q5a="leave", q5b="no", q6="more_room_on_top_slimmer_bottom",
        q7_top=["relaxed", "oversized"], q7_bottom=["close", "tight"],
        featuring_zones=["legs", "hips_and_curves"], q12_exposure="comfortable",
        cut_accepted=["slim", "straight"], rise_accepted=["high", "mid"],
        length_skirts_accepted=["short", "mid_thigh"], styles_yes=["cool_casual", "sexy"])
    show("PROFILE 3 — triangle, Intent-5 leg feature (exercises overrides)", catalog, tri)
