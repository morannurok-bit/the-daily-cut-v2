# Intent Classification Framework — The Daily Cut (v2.1)

The heart of the matching engine: the silhouette **intents** that drive recommendations, the
answer combinations that classify a user into them, and how body, items, and overrides
interact downstream.

**v2.1 reconciliation note.** This revision aligns the spec to the engine
(`engine_v2.py` → `classify_intents`), which is the source of truth. Changes from v2:

- **Intent 8 (“Refined coverage”) is retired.** It wasn’t a distinct silhouette move —
  coverage is the exposure axis (Q12 + covered zones), composure is Intent 2, and polish is
  the style layer. Nothing it surfaced was otherwise unreachable. Removed here, in the engine,
  and in the catalog (0 items). The framework now has **eight** intents: 1–7 and 9.
- **Intent 2 corrected to “independent definer.”** She defines the waist *herself* (tuck/belt);
  the garment must **afford** that, never **impose** it. A wrap/built-in cinch is the garment
  deciding → that’s **Intent 3**. Intent 2 no longer gates on proportion or leg width.
- **Firing rules now match the engine exactly.** **Featuring zones are not a firing signal** —
  they’re an item-side design-draw tag and a soft boost, not part of user classification.
  Several intents fire on fewer conditions than v2 claimed.

---

## Operating Principles

### 1. Intent is preference-based, not body-based
Intent = *what the woman is trying to achieve with an outfit* — not what flatters her body,
not her register, not her style world. Body type and height do **not** enter classification;
they enter at the item-matching layer.

### 2. Intent count scales with the latitude she gives
A woman who answers narrowly (one styling mode, one proportion, one closeness per region)
fires one or two intents — a tight feed. A woman who answers with maximal openness (“both” on
the waist questions, several closeness options) fires many — she has told us almost every
silhouette story is acceptable to her. This is correct: for a flexible woman the curation
happens at **taste** (style worlds + adventurousness), not at the intent layer. Intent count
is a direct readout of how much room she gave us.

### 3. Items earn an intent only where the wearing mode is a PRIMARY design intent
Item-level `intents_served` reflects what the garment is *designed to deliver*, not every
configuration mechanically possible with it. A relaxed tee that *can* be tucked doesn’t serve
Intent 2 just because tucking is possible — Intent 2 requires the waist to be the designed
visual story.

### 4. Style world does NOT gate intent
A cool_tlv architectural piece and a refined_casual soft piece can both fire Intent 2 or
Intent 4, through different aesthetic vocabularies. Intent is the silhouette story; world is
the aesthetic register. Independent dimensions.

### 5. Firing uses Q5/Q6/Q7 (and Q12 for one intent) — NOT featuring zones
The classifier reads Q5a, Q5b, Q6, the Q6 follow-up, Q7 top/bottom closeness, and — for
Intent 9 only — Q12 exposure. **Featuring zones are not read at firing time.** They are an
item-side “deliberate design draw” tag and a soft re-rank signal downstream. (This is the
single biggest source of v2→v2.1 drift: v2 listed featuring conditions in several intents’
“fires when” blocks; the engine never used them there.)

### 6. Afford vs impose — the Intent 2 / Intent 3 split
The dividing line between Intent 2 and Intent 3 is **who creates the waist**. Intent 2: *she*
does, through her own styling (tuck, belt); the garment merely affords it. Intent 3: the
*garment* does, through built-in construction (wrap, peplum, waist seam, belt-as-built-in).
A single piece can be tagged to serve both if it both affords self-styling and can build shape
on its own — but the user signals split cleanly on Q5b (see below).

---

## Signals Used for Classification

**Firing signals:**
1. **Q5a** — styling preference: `leave` / `tuck` (tuck or belt to define waist) / `both`
2. **Q5b** — garment-built waist: `no` (not my thing) / `yes` / `both`
3. **Q6** — proportion (single value, see “Q6” section): `top_and_bottom_same` /
   `slimmer_top_more_room_on_bottom` / `more_room_on_top_slimmer_bottom`
4. **Q6 follow-up** (when wider bottoms): `room_throughout` / `fitted_waist_seat` / `both`
5. **Q7 top closeness** — multi-select: `tight` / `close` / `relaxed` / `oversized`
6. **Q7 bottom closeness** — multi-select: `tight` / `close` / `relaxed`
7. **Q12 exposure comfort** — `comfortable` / `only_a_little` / `prefer_coverage`
   *(used at firing time by Intent 9 only)*

Derived booleans the engine uses:
`leaves = Q5a ∈ {leave, both}` · `tucks = Q5a ∈ {tuck, both}` ·
`nobuild = Q5b ∈ {no, both}` · `builds = Q5b ∈ {yes, both}`.
(“both” answers satisfy **both** sides — so a fully-flexible woman can fire leave-intents and
tuck-intents at once.)

**NOT used at firing time:** featuring zones (item-side + soft boost), body type, height,
style-world picks, color, fabric, cut/length avoids. These enter at item filtering / boost /
hard-filter layers.

---

## The Eight Intents

> Each “Fires when” below is the **exact** engine condition. `t` = Q7 top set, `b` = Q7 bottom
> set, `q6` = proportion.

### Intent 1 — Show the body line vertically
The long, uninterrupted vertical line. Body engaged throughout via close fit; **no waist
event.** The body’s own contour is the story (a close rib tee over close straight jeans).
Distinct from Intent 2: here nothing *styled* creates a waist moment — the waist is merely
traced, not headlined.

**Fires when:** `leaves` AND `nobuild` AND `top_and_bottom_same ∈ q6` AND
`t ∩ {close, tight} ≠ ∅` AND `t ≠ {oversized}` AND `b ∩ {close, tight} ≠ ∅`.

### Intent 2 — Independent definer: she defines the waist herself
The waist is the outfit’s headline, created by **her** styling commitment — tucking into a
high-rise, belting. The garment **affords** the move (`strategy = styling_anchor`); it does not
impose it. Works over **any bottom** — slim, straight, or wide — because tucking is a *top*
move (leg volume is Intent 4’s concern, not this one). A fitted knit tucked into high-rise
jeans is canonical; a drapey polo bloused over a waistband counts too (soft meeting point).

**Does NOT fire / tag when:** the waist is only *traced* by close fit (Intent 1), or the piece
*builds* the waist on its own — a wrap, a built-in cinch, a peplum (that’s Intent 3).

**Fires when:** `tucks` AND `nobuild`.
*(No proportion gate, no leg-width gate, no featuring gate — she tucks, and she isn’t asking
the garment to build the waist for her.)*

### Intent 3 — Let the garment build the silhouette
She wants one piece to deliver the shape: wrap dress, belted shirt dress, peplum, fit-and-flare,
A-line with a waist seam. The **construction** does the work — she doesn’t engineer it by
styling.

**Fires when:** `builds` (i.e. Q5b ∈ {yes, both}).
Fully determined by Q5b; other signals only decide which *additional* intents fire alongside.

### Intent 4 — Amplify curves through proportion
Fitted-through-the-waist top **tucked** into a volume bottom (wide-leg, full skirt) = small-
waist-to-fuller-bottom contrast, made louder. Fires regardless of style world (architectural
wide-leg or soft drapey wide-leg both qualify).

**Fires when:** `tucks` AND `slimmer_top_more_room_on_bottom ∈ q6` AND
`Q6-followup ∈ {room_throughout, fitted_waist_seat, both}` AND `relaxed ∈ b`.
*(Q5b does not gate. Top closeness and featuring zones are not read here — the volume bottom +
tuck + proportion carry it.)*

### Intent 5 — Elongated lower body / feature the legs
Slim, body-engaged bottom under a **relaxed or oversized** top: covered top + engaged leg =
legs as the visual redirect (slim/cigarette pants under a boxy shirt; close-hip mini). The leg
reveal is via **fabric tracing on a close-fit bottom**, not a loose hem (that’s Intent 9).

**Fires when:** `leaves` AND `nobuild` AND `more_room_on_top_slimmer_bottom ∈ q6` AND
`t ∩ {relaxed, oversized} ≠ ∅` AND `b ∩ {close, tight} ≠ ∅`.
*(Exposure and featuring were listed in v2 but are not read at firing; leg-exposure comfort is
enforced later as a hard filter, not here.)*

### Intent 6 — Step back from the body
Relaxed top + relaxed bottom, balanced proportion. Body isn’t the story — comfort, register, or
a refusal of the flattery frame (relaxed tee + relaxed jean; oversized shirt + relaxed wide-leg).

**Fires when:** `leaves` AND `nobuild` AND `top_and_bottom_same ∈ q6` AND
`t ∩ {relaxed, oversized} ≠ ∅` AND `relaxed ∈ b`.
*(No featuring gate. Differs from Intent 9 by proportion/exposure, not by featuring.)*

### Intent 7 — Multi-modal / plays across modes
She has no single silhouette — tucks some days, leaves it loose others, several closeness
options in play. A body/latitude read, not a taste. **Widens** the catalog on top of her
primary intents; never replaces them. At the item level, Intent 7 is for genuinely
multi-modal pieces (splitting co-ords, full-placket shirts worn many ways) — not every flexible
basic.

**Fires when:** `Q5a = both` AND `Q5b = both` AND `Q6-followup = both` AND
`|t| ≥ 2` AND `|b| ≥ 2`.

### Intent 9 — Covered body, feature an opening
Body covered by loose/relaxed fabric with a **deliberate opening** as the event: deep V, slit,
open back, or a **short hem on a loose bottom** (relaxed bermuda/short on an otherwise covered
body). Differs from Intent 5: the leg here is revealed by a loose hem, not by tracing a close-fit
bottom.

**Fires when:** `leaves` AND `nobuild` AND
`q6 ∩ {top_and_bottom_same, more_room_on_top_slimmer_bottom} ≠ ∅` AND
`t ∩ {relaxed, oversized} ≠ ∅` AND `relaxed ∈ b` AND
`Q12 exposure ∈ {comfortable, only_a_little}`.
*(Intent 9 is the one intent that reads Q12 at firing time — an opening-forward woman isn’t a
“prefer coverage” woman. Featuring zones are not read at firing; they steer which items best
execute the opening downstream.)*

---

## Q6 — Proportion only (three values)

Q6 asks purely about **proportion balance between top and bottom** — it carries no closeness
information. A user can want everything tight, close, or oversized; Q6 only says how she wants
top and bottom to relate.

> “When putting an outfit together, how do you like the proportions?”
> - More room on top, slimmer on the bottom → `more_room_on_top_slimmer_bottom`
> - Slimmer on top, more room on the bottom → `slimmer_top_more_room_on_bottom`
> - Top and bottom the same → `top_and_bottom_same`

(The old fourth option “not much extra room” was dropped as a duplicate of Q7 closeness; the
old “room on both” was reworded to “top and bottom the same” — the signal is *balance*, not
looseness.) Q6 combines with Q7 closeness to separate intents that share a proportion — e.g.
`more_room_on_top_slimmer_bottom` + engaged bottom → Intent 5, whereas the same proportion with
a relaxed bottom + covered opening → Intent 9.

---

## Catalog conventions (locked at tagging)

**Universal basics** (e.g. plain cotton tees): `intents_served` empty, `item_role = basic`,
`core_style` empty, `body_type_ok` = all. They surface via a basics path (fit + fabric + color),
available to all users regardless of fired intents.

**Blue denim is a category-basic:** a jean is palette-exempt for blue/indigo/denim even if the
user didn’t pick blue — not picking blue ≠ avoiding it. (Enforced in the engine’s palette gate.)

**featuring_zones (item-side)** captures *deliberate design draws* — `decollete`, `bust`,
`shoulders`, `arms`, `waist`, `hips_and_curves`, `seat`, `legs`, `back` — not every zone engaged
by closeness. It is a soft re-rank signal, **not** a firing input.

**`context = lounge`** softens body-risky tags for in-home wear (exposure prefs still enforced).

---

## Resolution logic

The engine runs all eight pattern checks independently; each returns fired / not-fired.

- **Single-intent user:** one pattern matches → surfaces items tagged with it.
- **Two-intent user:** e.g. Intent 1 + Intent 5 (“vertical line with a leg feature”), or
  Intent 2 + Intent 4 (“define the waist and amplify the bottom”).
- **Many-intent user:** broad, flexible — usually includes Intent 7; surface with variety.
- **No intent fires:** surface body- and world-matched **basics** with a low-confidence flag.

Conflict order when signals disagree: Q5a strongest, then Q5b, then Q6, with Q7 as tie-break.

---

## Engine pipeline

```
Questionnaire answers
   ↓ INTENT CLASSIFIER  (Q5a, Q5b, Q6, Q6-followup, Q7 top, Q7 bottom, Q12 for Intent 9)
Fired intents  e.g. [intent_2, intent_4]
   ↓ ITEM PULL          items whose intents_served ∩ fired  +  universal basics
   ↓ BODY-TYPE FILTER   best / ok / risky, with override patterns
   ↓ CONTEXT FILTER     lounge softens body-risky
   ↓ HEIGHT / SCALE
   ↓ HARD FILTERS       cuts, lengths, fabric, exposure covers, palette (denim-basic exempt)
   ↓ STYLE / AXIS LAYER register liked?  intensity ≤ ceiling?  maturity ok?  world reachable? (Option A)
   ↓ BOOST + RANK       world match, color, modulators, featured-zone overlap → heroes/bridges/basics
   ↓ Surface to user
```

---

## Body type & height (downstream, not in classification)

Intent firing is body- and height-agnostic; the *items that execute* an intent differ by body.
- `body_type_best` → boost · `body_type_ok` → neutral · `body_type_risky` → filtered unless an
  override fires (see `overrides_and_vocabulary.md`).
- `body_modulators` (e.g. `full_bust_friendly`, `midsection_friendly`) re-rank, don’t filter.
- Lean suffixes (`rectangle_lean`, etc.) match only lean users; general tags match both.

---

## What intent classification does NOT determine
Which items execute an intent (`intents_served` + body + height) · which body types succeed
(body rules + overrides) · ranking (boost layer) · hard filters (cuts, lengths, fabric,
exposure, palette). Intent classification produces only the fired-intent list.

---

## Tagging workflow per item
1. Identify the primary wearing modes the item is *designed* to deliver.
2. Tag `intents_served` for those primary modes only (not merely-possible ones). Remember the
   afford-vs-impose split: self-styled waist → Intent 2; garment-built waist → Intent 3.
3. Body-type compatibility + override patterns for risky types.
4. Note universal-basic / denim-basic conventions where applicable.

---
*End of intent framework specification v2.1. Reconciled to `engine_v2.py`; supersedes v2.*
