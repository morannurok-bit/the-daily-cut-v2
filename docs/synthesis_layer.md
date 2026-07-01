# Synthesis Layer: Questionnaire → Recommendation Policy

This document describes how the system turns a user's questionnaire answers into a structured recommendation policy. It sits between the questionnaire (input) and the body type rules (reference material), producing a resolved profile that the recommendation engine consumes.

The body type rules document describes geometric truth and strategy-specific success/failure modes. This document describes how those rules apply to a specific user given everything she told us. The recommendation engine then uses the resolved profile + body type rules to score items.

---

## Core Operating Principle

**The synthesis layer does not decide what is "flattering" in isolation. It resolves what the user gave permission to use. The recommendation engine should recommend the most body-compatible version of the user's chosen style, strategy, exposure, fit, and feature signals.**

This is the foundational principle that governs everything below. Body type rules describe geometric truth and strategy-specific success/failure modes — they are reference material, not filters. The user's signals (strategies selected, fits chosen, zones featured, exposure preferred, fabrics tolerated, cuts allowed) define what universe she wants to operate in. The system's job is to find the items within that universe that work best for her body. The body type rules inform *which version* of her chosen items will work; they don't override her choices.

Consequences of this principle:

- A pear user who selects celebrate mode gets bodycon hip-emphasis items — the body type rules inform which bodycon items work for pear curves (skim fabric, curvy-fit construction) rather than filtering bodycon out.
- A rectangle user who selects edge strategy gets items executing edge — the body type rules inform what good edge execution looks like for rectangle (multiple strategic features, asset-aligned redirects) rather than filtering items that lack anchor.
- An apple user who selects low-rise gets low-rise items — the body type rules inform which low-rise items work for apple (below-midsection rise, skim-fit hip, fluid fabric) rather than filtering low-rise out.

The system is anatomically intelligent, not anatomically prescriptive.

---

## Section 1: Profile Schema

The synthesis layer produces a structured profile per user. Schema below.

### Body identification

```
body_type: rectangle | inverted_triangle | hourglass | pear | apple
variation: object describing within-type variation, with confidence per signal
  - frame:
      value: lean | standard | soft | athletic
      confidence: low | medium | high
  - ribcage_signal:
      value: standard | wider
      confidence: low | medium | high
      (applies to rectangle, hourglass)
  - bust_signal:
      value: smaller | standard | fuller
      confidence: low | medium | high
  - midsection_signal:
      value: standard | prone
      confidence: low | medium | high
  - seat_signal:
      value: flat | projected | fuller
      confidence: low | medium | high
  - additional: free-form variation notes (athletic build, spoon hips, top/bottom hourglass, etc.)
height_tier: petite | mid | tall
  - petite: under 160
  - mid: 160-169
  - tall: 170+
```

**Confidence derivation:**

- *High:* multiple signals confirm (snug zone + fit issue + reported discomfort in same area; or two separate diagnostic signals point to the same variation)
- *Medium:* single strong signal (one snug zone + corresponding fit issue) OR consistent secondary signals
- *Low:* single weak signal (one snug zone with no fit issue; user reports "fits how it should" but selected one snug zone)

The confidence level affects how aggressively the variation modulator applies in scoring. High confidence: variation rules fire as documented. Medium confidence: variation rules apply but with reduced weight. Low confidence: variation noted but rules apply only as soft preference. Behavior data over time refines confidence — consistent engagement with variation-appropriate items raises confidence; rejection lowers it.

### Strategy weighting

```
strategies: array of strategy entries
  - strategy: trace | anchor | sculpt | edge
  - selected: boolean (did user pick this in Q5)
  - weight: float (relative emphasis, derived from secondary signals)
  - execution: object (populated based on follow-up answers per strategy)
    - if trace: {} (no follow-up; derived from fit + fabric)
    - if anchor:
        user_created: boolean (user-styled anchor through rise, tucking, belt)
        garment_created: boolean (wraps, belted dresses, shaped-waist pieces)
        unsure: boolean (user couldn't articulate)
    - if sculpt:
        waist_sculpt: boolean (corseted, princess-seamed, dramatic taper)
        lower_body_sculpt: boolean (peplum, dramatic flare, mermaid)
        shoulder_sculpt: boolean (structured shoulder, defined upper body)
        unsure: boolean
    - if edge:
        exposure_edge: boolean (open necklines, slits, bare shoulder, open back)
        proportion_edge: boolean (oversized + slim, short + wide combinations)
  - execution_gate: object describing quality requirements
    - quality_threshold: high | standard | none
    - notes: free-form
```

If user selected one strategy → that strategy weighted high, others available at neutral weight.
If user selected multiple → all selected weighted up; unselected at neutral.
Unselected strategies don't filter — items executing unselected strategies are evaluated on their own criteria.

**Execution sub-classifications apply within-strategy.** For each strategy the user selected, the execution selections determine which sub-patterns surface:

- Anchor + user_created only → meeting-point/tucking/belting patterns; FILTER garment-imposed waist construction
- Anchor + garment_created only → wraps, belted dresses, fitted-bodice; allow user-styled at neutral
- Anchor + both → both patterns surface; widest anchor catalog
- Sculpt + waist_sculpt only → corseted, princess-seamed; filter peplum-only and shoulder-only
- Sculpt + lower_body_sculpt only → peplum, dramatic flare; filter waist-only and shoulder-only
- Sculpt + shoulder_sculpt only → structured-shoulder; filter waist-construction and peplum
- Edge + exposure_edge only → open necklines, slits; downrank pure proportion-play
- Edge + proportion_edge only → oversized-and-slim combinations; downrank pure exposure pieces
- Edge + both → both patterns surface

See Q5 mapping in Section 2 for full execution rules and overlap zones.

### Featuring zones

```
featuring_zones: array of zone entries (one per named zone)
  - zone: décolletage | bust | shoulders | arms | waist | hips_curves | seat | legs | back
  - named: boolean (did user pick this in Q3 featuring question)
  - mode: reveal | sophisticated | coverage (per cross-body framework)
  - treatment: amplify | unlock | respect_over_default | fall_back
    (per cross-body framework — based on how the zone relates to body type defaults)
nothing_in_particular: boolean (if user picked "nothing in particular")
```

### Fit policy

```
fit_top:
  - selected: array (subset of [tight, close, relaxed, oversized])
  - shaping_gate: boolean (true if close fit available only when item provides shaping support — ribbed knit, structured construction, fitted with body)
fit_bottom:
  - selected: array (subset of [tight, close, relaxed, oversized])
```

### Volume policy

```
volume_preferences: array (subset of [mostly_top, mostly_bottom, balanced, minimal])
```

### Fabric policy

```
fabric:
  importance: very_important | important | low
  attention_to_detail: high | medium | low
  discomforts: array (subset of [clings, stiff, heavy, wrinkles])
    - filter behavior depends on tag confidence (see below)
```

**Tag-confidence-gated filtering:**

Fabric discomforts filter items only when the item's fabric tag has high confidence. When the tag is inferred or uncertain, treat as strong downrank rather than hard filter.

```
For each item with fabric property matching a user discomfort:
  - If item.fabric_tag.confidence = high → hard filter (remove from catalog)
  - If item.fabric_tag.confidence = medium → strong downrank (severely penalize ranking; surface only if no better alternatives exist)
  - If item.fabric_tag.confidence = low → moderate downrank (penalize but allow to surface if other signals are strong)
```

Tag confidence depends on data source:
- *High:* explicit product description states the property (product copy says "rigid denim", "structured", "non-stretch", "heavy wool"); or product imagery confirms; or trusted brand tagging
- *Medium:* category-level inference with reasonable reliability (e.g., "denim" defaults to medium-stiff but variation is significant; "ponte" defaults to structured stretch with good reliability)
- *Low:* category-level inference with high variation (e.g., "knit" — could be ribbed structured cotton or thin synthetic jersey; "shirt" — could be crisp poplin or fluid silk)

The principle: false-negatives from over-aggressive filtering on uncertain tags cost more than false-positives from surfacing borderline items. A user can dismiss a stiff-looking denim item; she can't see an item that was filtered out for being "stiff" when it was actually drapey stretch denim.

This applies to all fabric discomforts (clings, stiff, heavy, wrinkles). Same logic: filter only when we're confident; downrank when we're uncertain.

### Length policy

```
length_pants:
  avoid: array (subset of [full, cropped, capri]) — explicit user avoids; filter
  preferred: not currently captured (could add)
length_skirts_dresses:
  preferred: array (subset of [short, mid, long])
  not_preferred: derived (lengths not in preferred list are deprioritized but not filtered)
```

### Cut policy (pants/jeans)

```
cut_avoid: array (subset of [straight, wide, flared, bootcut, slim, barrel]) — filter
cut_preferred: not currently captured (could add)
rise: array (subset of [low, mid, high, flexible])
  - if flexible: all rises available
  - if specific rises selected: weight up selected, others available at neutral
```

### Exposure policy

```
exposure_overall: comfortable | depends | prefer_coverage
exposure_covers: array (subset of [arms, shoulders, back, chest, midriff, legs])
  - covered zones filter items revealing those zones
exposure_zones_available: derived (zones not in covers list, used for reveal/sophisticated mode access)
```

### Reveal modes (derived per zone)

```
reveal_modes: object mapping zones to modes
  - one entry per named featuring zone
  - mode: reveal | sophisticated | coverage
  - derived from: featuring zone named + exposure preferences + length preferences for that zone
```

### Style policy

Style archetype is the aesthetic register the user dresses in. It's separate from body type, strategy, and fit — two women with identical body/strategy/fit profiles can have completely different aesthetics (one wears jeans-and-tees casual classic, another wears wrap-dress romantic feminine, third wears architectural minimal, fourth wears edgy black).

Without style archetype captured, the system surfaces body-correct but style-wrong items: anatomically intelligent, stylistically broad. This is the highest-priority gap in the current system.

**Proposed schema:**

```
style_policy:
  archetypes_selected: array (subset of archetype vocabulary, multi-select with optional rank)
  intensity: quiet | clear | strong
  rejected_archetypes: array (explicit "definitely not this" filters)
  status: captured | inferred | not_yet_captured
```

**Archetype vocabulary (minimum viable):**

- *Casual:* jeans, t-shirts, button-downs, simple knits, comfort-first base register
- *Classic:* timeless basics, clean lines, simple silhouettes, neutral palette, often menswear-inflected
- *Polished:* tailored, put-together, structured pieces, refined detail
- *Romantic:* soft, feminine, flowing, decorative — wraps, ruffles, prints, feminine detail
- *Edgy:* sharp, dark, statement, often black, structured boots, leather
- *Sporty:* athletic-influenced, performance fabrics, casual-athletic crossover
- *Bohemian:* loose, layered, eclectic, textured, decorative without being polished
- *Minimal:* clean, architectural, undecorated, monochromatic, designed-restraint
- *Urban:* street-influenced, modern, often oversized, contemporary cuts

Archetypes are multi-select because most women combine 2-3. "Casual + classic" produces Lital's aesthetic (jeans + tees + button-downs + soft blazers). "Casual + classic + urban" produces a different one (jeans + tees + structured short jackets + modern silhouettes). "Polished + classic" produces a third (tailored pieces, structured construction).

**Intensity** captures how strongly the archetype expresses:
- *Quiet:* archetype is present but understated; user wears the basic version
- *Clear:* archetype is present and visible; user wears the recognizable expression
- *Strong:* archetype is the dominant statement; user wears the full expression

**Rejected archetypes** capture explicit "definitely not this" signals — different from "didn't pick." A user who explicitly rejects romantic/feminine should never see wrap dresses or ruffled blouses, even if body+strategy+fit signals would surface them.

**Application in synthesis layer:**

Style archetype affects scoring as a multiplier on item style-match:
- Items strongly matching selected archetypes: +1.0 multiplier
- Items moderately matching: 0.7 multiplier
- Items neutral on style: 0.5 multiplier
- Items matching unselected archetypes: 0.2 multiplier
- Items matching rejected archetypes: 0.0 multiplier (effective filter)

This sits alongside body-compatibility scoring. An item with strong body-compatibility but weak style match still ranks lower than an item with both strong body-compatibility and strong style match.

**Until the question is added:**

- Behavior data infers style archetype slowly (saves, dismisses, purchases reveal pattern)
- Quick-inference signals exist from current questionnaire: minimal detail preference + clean fabric preferences suggest minimal or classic; multiple strategy + multi-fit + broad signals suggest stylistically broad user without strong archetype lock; named featuring zones + specific styling signals suggest the archetype they imply
- The synthesis layer can flag inferred archetype as "inferred" status (low confidence) until the question captures it explicitly

The proposed questionnaire addition:

> *Q: Which describes your overall style? (Select up to 3, then rank top 2)*
> [casual, classic, polished, romantic, edgy, sporty, bohemian, minimal, urban]
>
> *Follow-up: Any aesthetics you definitely don't want? (Multi-select, optional)*
> [same list]

Two-question addition. Doesn't disrupt the existing questionnaire structure. Fills the biggest accuracy gap.

### Permissiveness

```
permissiveness:
  score: float (high | medium | low — derived)
  signals: object capturing which signals fired
    - multi_strategy: boolean (3+ strategies)
    - multi_fit: boolean (3+ fit options selected across top + bottom)
    - multi_volume: boolean (2+ volume options)
    - multi_featuring: boolean (2+ zones named)
    - broad_fabric: boolean (0-1 discomforts)
    - broad_exposure: boolean (comfortable + 0-2 covers)
    - flexible_cut_or_rise: boolean
```

### Hard constraints and filter categories

The synthesis layer distinguishes four filter categories with different override behavior:

```
true_hard_filters: items that filter for everyone, no override
  - user-explicit cut avoids (Q3 cuts marked "we won't show them")
  - user-explicit length avoids (Q3 lengths marked "we won't show them")
  - user-explicit exposure covers (Q4 zones marked covered)
  - fabric discomforts WHEN tag confidence is high (Q2 fabric properties flagged + item tagged with high confidence)
  
  These come from explicit user signals. The user told us no; we honor it.
  Fabric discomforts are tag-confidence-gated — see Fabric Policy section. High-confidence tag = filter; medium/low confidence = downrank instead.

body_type_structural_filters: items that fail across all strategies on the body type
  - items where the geometric failure doesn't depend on strategy (drop-waist on rectangle eliminates leg asset regardless of strategy; column dress with no features and no openings has nothing to redirect attention to)
  - filter by default
  - BUT: system checks for compensating features that change strategy frame before filtering
  - if item has strong edge features (strategic openings, slits, asset-aligned redirects), evaluate as edge item, not as anchor/trace failure
  
  Test: does the failure mode cross all strategy frames, or is it specific to one?

strategy_frame_filters: items that fail within a specific strategy
  - soft anchor (drawstring, self-tie) — fails when item executes anchor; doesn't apply to items executing edge or other strategies
  - poor-fabric trace — fails when item executes trace
  - fast-fashion sculpt — fails when item executes sculpt
  - single-feature edge with no compensation — fails when item executes edge
  
  These filter only when the corresponding strategy is the item's primary execution.

permissiveness_modulated_filters: items that filter for restrictive profiles, surface for permissive
  - items requiring sophisticated styling execution
  - items at the edge of body type tolerance (long heavy outerwear on borderline-petite rectangle)
  - items that work but require careful pairing
  - fabric discomforts WHEN tag confidence is medium or low (downrank for everyone; effective filter for restrictive users; surfacing more permitted for permissive users with strong other signals)
  
  For permissive users (multi-strategy, multi-fit, broad signals): surface; behavior data refines.
  For restrictive users (single strategy, narrow fit, multiple covers/discomforts): filter; only obvious heroes surface.
```

The four categories produce different filter behavior in scoring:

1. **True hard filters** — always filter; no override exists. User said no.
2. **Body-type structural filters** — filter by default, but verify item doesn't have compensating features that shift it into a different strategy frame before filtering.
3. **Strategy-frame filters** — filter only when item is executing that strategy.
4. **Permissiveness-modulated filters** — filter for restrictive users; surface for permissive users; behavior data refines over time.

### Restrictiveness output

```
restrictiveness: narrow | moderate | wide
catalog_width: small | medium | large
hero_weighting: high | standard | low
behavior_data_sensitivity: high | medium | low
```

---

## Section 2: Question-by-Question Mapping

For each questionnaire question, what it contributes to the profile and how.

### Q1: Height

| Answer | Contribution |
|---|---|
| Under 159 | height_tier = petite |
| 160-164 | height_tier = mid |
| 165-169 | height_tier = mid |
| 170-175 | height_tier = tall |
| 175+ | height_tier = tall |

**Modifier (not constraint).** Modifies length defaults, jacket length thresholds, midi-vs-maxi length perception. Doesn't filter directly.

### Q2: Body proportions

| Answer | Contribution |
|---|---|
| Shoulders, waist, hips about same width | body_type = rectangle |
| Shoulders and hips similar, smaller waist | body_type = hourglass |
| Shoulders broadest | body_type = inverted_triangle |
| Hips broadest | body_type = pear |
| Fullness around midsection | body_type = apple |

**Diagnostic.** Primary body type identifier. Confirmed by Q3, Q4.

### Q3: Distribution — snug zones

Each zone selected contributes to variation detection. Diagnostic, not preference.

| Selected zone | Contribution |
|---|---|
| Chest | If body_type = rectangle: variation.ribcage_signal might = wider. If body_type = hourglass: variation.bust_signal might = fuller. If body_type = apple: variation.bust_signal might = fuller. |
| Arms | Noisy signal across body types; flag for upper-arm bulk-aversion in featuring |
| Shoulders | If body_type = inverted_triangle: confirms identification. If body_type = apple: variation.top_heavy_signal |
| Waist/stomach | If body_type = rectangle: variation.midsection_signal might = prone. If body_type = apple: confirms identification. |
| Hips/thighs | If body_type = pear: confirms identification. If body_type = hourglass: variation.bottom_fuller |
| Seat | If body_type = pear or hourglass: confirms projected seat. If body_type = rectangle: variation.seat_signal = fuller |
| Nowhere specific | variation.frame = lean |

**Diagnostic.** Combined signals refine variation.

### Q3: Distribution — loose zones

| Selected zone | Contribution |
|---|---|
| Chest | If body_type = pear: confirms smaller bust. If body_type = rectangle: variation.frame leans lean |
| Arms | Lean signal; doesn't reclassify |
| Shoulders | If body_type = pear: confirms narrower shoulders |
| Waist | If body_type = rectangle: variation.frame leans lean (doesn't suggest hourglass — needs Q2 to indicate defined waist) |
| Hips/thighs | If body_type = inverted_triangle: confirms narrower hips. If body_type = rectangle: variation.frame leans lean |
| Seat | If body_type = rectangle: variation.seat_signal = flat (typical). If body_type = inverted_triangle or apple: confirms flat seat. |
| Nowhere specific | No specific contribution |

**Diagnostic.** Combined with snug zones to determine variation.

### Q3: What do you like most (featuring zones)

Each zone selected creates a featuring_zones entry.

| Selected zone | Contribution |
|---|---|
| Décolletage / collarbones | featuring_zones.décolletage.named = true |
| Bust | featuring_zones.bust.named = true |
| Shoulders | featuring_zones.shoulders.named = true |
| Arms | featuring_zones.arms.named = true |
| Waist | featuring_zones.waist.named = true |
| Hips/curves | featuring_zones.hips_curves.named = true |
| Seat | featuring_zones.seat.named = true |
| Legs | featuring_zones.legs.named = true |
| Back | featuring_zones.back.named = true |
| Nothing in particular | nothing_in_particular = true (lowers permissiveness; conservative defaults) |

For each named zone, **treatment** is derived from how the zone relates to body type defaults (amplify / unlock / respect over default / fall back — per cross-body framework). **Mode** is derived later from exposure and length signals.

**Preference.** Names what to amplify; doesn't lock other zones.

### Q4: Fit issues

| Answer | Contribution |
|---|---|
| Feels tight in chest | If body_type = rectangle: variation.ribcage_signal might = wider. Confirming signal. |
| Feels tight in arms | Flag bulk-aversion in featuring; might amplify slim-sleeve preferences |
| Feels tight in waist | If body_type = rectangle: variation.midsection_signal might = prone OR ribcage wider. If body_type = apple: confirms. |
| Pulls across thighs | If body_type = pear: confirms full thighs. |
| Too tight around hips/seat | If body_type = pear: confirms. If body_type = hourglass: confirms. |
| Too loose around hips/seat | If body_type = rectangle: confirms flat seat. If body_type = inverted_triangle: confirms narrower hips. |
| Gaps at waist | If body_type = hourglass or pear: confirms defined waist / waist-to-hip differential. |
| Everything usually sits how it should | No fit-issue flag; may indicate adapted buying patterns or natural good-fit |

**Diagnostic.** Refines variation.

### Q4: Length issues

| Answer | Contribution |
|---|---|
| Pants feel too short | If height_tier = tall: confirms (longer-leg proportions); modify length defaults |
| Pants feel too long | If height_tier = petite: confirms; modify length defaults |
| Tops feel too cropped | If height_tier = tall: signals need for longer tops |
| Tops feel too long | If height_tier = petite: signals need for shorter or cropped tops |
| Everything usually sits where it should | No length-issue flag |

**Diagnostic.** Modifies length-tier interpretation.

### Q5: How clothes should sit (strategy + execution)

Multi-select strategy with execution follow-ups. Each strategy that gets selected may trigger a follow-up question to capture how the user wants that strategy executed.

**Q5 (main question):** *How do you usually like clothes to sit on your body?* Multi-select.

| Answer | Contribution |
|---|---|
| Follow my natural shape | strategies[trace].selected = true |
| Defined around a certain area (like the waist) | strategies[anchor].selected = true |
| Create a more structured or shaped look | strategies[sculpt].selected = true |
| Sit away from the body / not focused on shape | strategies[edge].selected = true |

**Strategy weighting:**
- 1 strategy selected → that strategy weighted high, others available at neutral
- 2 strategies → both weighted up, others neutral
- 3+ strategies → all selected weighted up, plus multi-strategy permissiveness signal fires
- 0 strategies (fallback) → all strategies at neutral

**Execution follow-ups (only shown for selected strategies):**

---

**If trace is selected:**

No follow-up. The system uses fit and fabric preferences to understand the kind of trace appropriate for the user:

- Trace + close fit + soft fluid fabric + high fabric importance → refined skim-fit trace (sheath knits, fitted soft blouses, fitted button-downs in fluid fabric)
- Trace + close fit + structured fabric + high fabric importance → precise tailored trace (sheath dresses in ponte, structured fitted pieces)
- Trace + relaxed fit + soft fluid fabric → body-following drape without skin-fit (soft drape blouses that follow form, fitted-but-not-tight knits)
- Trace + any fit + standard fabric importance → standard trace items in user's fit range

---

**If anchor is selected:**

Follow-up: *When you like shape around the waist, what feels most like you? Select all that apply.*

| Answer | Internal label | Contribution |
|---|---|---|
| I like creating the shape myself — choosing the right rise, tucking, half-tucking, or adding a belt | user_created_anchor | strategies[anchor].execution.user_created = true |
| I like when the piece already creates the shape — like a wrap top, belted dress, or shaped-waist piece | garment_created_anchor | strategies[anchor].execution.garment_created = true |
| I'm not sure | unsure | strategies[anchor].execution.unsure = true |

---

**If sculpt is selected:**

Follow-up: *When you like a more shaped look, where do you like the shape to come from? Select all that apply.*

| Answer | Internal label | Contribution |
|---|---|---|
| A defined, sharper waist — like a corseted bodice, princess-seamed dress, or strong tailored taper | waist_sculpt | strategies[sculpt].execution.waist_sculpt = true |
| More curve through the lower body — like a peplum, fuller skirt, or shape that flares dramatically below the waist | lower_body_sculpt | strategies[sculpt].execution.lower_body_sculpt = true |
| A stronger shoulder line — like a structured blazer, defined shoulder, or jacket that builds the upper body | shoulder_sculpt | strategies[sculpt].execution.shoulder_sculpt = true |
| I'm not sure | unsure | strategies[sculpt].execution.unsure = true |

---

**If edge is selected:**

Follow-up: *When you like an outfit to feel more interesting, what kind of interest feels like you? Select all that apply.*

| Answer | Internal label | Contribution |
|---|---|---|
| Showing a little skin — like an open neckline, a slit, bare shoulders, or an open back | exposure_edge | strategies[edge].execution.exposure_edge = true |
| Playing with proportions — like an oversized shirt with slim jeans, or a short jacket with wide trousers | proportion_edge | strategies[edge].execution.proportion_edge = true |

---

**Application in synthesis layer:**

Items are tagged with strategy(s) they execute + execution sub-classification(s). User's execution selections filter accordingly:

- *Anchor + user_created only (no garment_created):* surface meeting-point patterns (high-rise + tuck, cropped + high-rise), surface tuck-friendly tops, surface belts; FILTER wraps, belted dresses, shaped-waist pieces, fitted bodice dresses that impose waist
- *Anchor + garment_created only (no user_created):* surface wraps, belted dresses, fitted-bodice pieces, shaped-waist construction; allow user-created patterns at neutral
- *Anchor + both:* surface both patterns; widest anchor catalog
- *Sculpt + waist_sculpt only:* surface corseted bodices, princess-seamed dresses, dramatic tapered construction; filter peplum-only and shoulder-only sculpt
- *Sculpt + lower_body_sculpt only:* surface peplum, dramatic flare, mermaid silhouettes; filter waist-only and shoulder-only sculpt
- *Sculpt + shoulder_sculpt only:* surface structured-shoulder blazers, defined shoulder pieces; filter waist-construction and peplum
- *Edge + exposure_edge only:* surface open necklines, slits, bare-shoulder, open-back; downrank pure proportion play without skin element
- *Edge + proportion_edge only:* surface oversized-with-fitted-bottom, fitted-with-volume-bottom combinations; downrank pure exposure-forward pieces

**Overlap zones to note:**

Some items execute multiple strategy/execution combinations and surface for users selecting any of the matching combinations:

- Wrap dress = anchor (garment_created) — surfaces for anchor garment_created users
- Fit-and-flare with structured bodice = anchor (garment_created) AND sculpt (waist + lower_body) — surfaces for any of these executions
- Peplum top = sculpt (lower_body) AND anchor (garment_created) — same
- Structured-shoulder blazer with strong waist suppression = sculpt (shoulder + waist) — surfaces for either execution

Items get classified by primary execution + secondary executions; user's selections produce union surfacing.

**Secondary-signal refinement (still relevant):**

When multiple strategies are selected, secondary signals help rank within selected strategies:

- Volume preference: "mostly bottom" or "balanced" + multi-strategy suggests edge proportion-play emphasis
- Fit preference: "close everywhere" + multi-strategy suggests trace emphasis
- "Defined around a certain area" with strong user emphasis vs. all options selected: anchor primary
- Featuring zones named: multiple zones suggest edge featuring; single zone suggests featuring-mode primary
- Style archetype: edgy/dramatic suggests edge; minimal/clean suggests trace; classic suggests anchor; sculptural/architectural suggests sculpt

**Execution gates from other signals:**

- Trace selected + fabric discomforts flagged (cling/stiff) → execution_gate.quality_threshold = high (trace requires good fabric for sensitivity-flagged users)
- Sculpt selected + attention to detail low → execution_gate.quality_threshold = standard
- Sculpt selected + fabric importance very_important → execution_gate.quality_threshold = high
- Any strategy + fabric importance very_important + attention to detail high → quality threshold elevated across all strategies

**Strategy-frame principle:** rules for selected strategies apply; rules for unselected don't filter items. Execution selections within strategies similarly: rules for selected executions apply; rules for unselected executions within the same strategy can downrank but don't filter.

**Preference.** Selected strategies and selected executions weighted up; unselected available at neutral or downrank. Items executing strategies the user didn't select aren't filtered solely on strategy basis; they get evaluated on the strategies they execute and the user's other signals.

### Q6: Volume preference

| Answer | Contribution |
|---|---|
| Mostly on top | volume_preferences includes "mostly_top" |
| Mostly on bottom | volume_preferences includes "mostly_bottom" |
| Balanced — same on top and bottom | volume_preferences includes "balanced" |
| Minimal / no volume | volume_preferences includes "minimal" |

**Preference.** Selected volume distributions weighted up; unselected available at neutral.

### Q7: Fit preference — tops

| Answer | Contribution |
|---|---|
| Tight | fit_top.selected includes "tight" |
| Close | fit_top.selected includes "close" |
| Relaxed | fit_top.selected includes "relaxed" |
| Oversized | fit_top.selected includes "oversized" |

**Shaping gate logic:** if user selected "close" but also flagged cling-averse fabric OR selected relaxed/oversized as primary preferences (with close as additional), set fit_top.shaping_gate = true. Close-fit items must provide shaping support (ribbed knit, structured construction, fitted with body) to surface.

**Preference.** Tight is a high-specificity preference. If not selected, tight/bodycon items are not filtered — but they require stronger support from strategy, style, exposure, and behavior signals to rank highly. A user may not pick tight as everyday fit but still like a fitted evening dress for a specific occasion, and the system should support this. Close, relaxed, oversized are standard preferences with no specificity-gate.

**Cross-garment fit propagation (critical):** fit_top selections apply to ALL garments engaging the upper torso, not just standalone tops. When fit_top is relaxed-only (close and tight not selected), the synthesis layer filters fitted-upper-body construction across categories: wrap tops, surplice tops, fitted button-downs, fitted polos, peplum tops, bodysuits, corset tops, wrap dresses, fit-and-flare with fitted bodice, sheath dresses, bodycon, fitted-closed blazers, and similar. See Section 3 "Cross-garment fit propagation" for complete rule.

### Q7: Fit preference — bottoms

Same structure as tops.

| Answer | Contribution |
|---|---|
| Tight | fit_bottom.selected includes "tight" |
| Close | fit_bottom.selected includes "close" |
| Relaxed | fit_bottom.selected includes "relaxed" |
| Oversized | fit_bottom.selected includes "oversized" |

**Preference.** Same cross-garment propagation: fit_bottom applies to all garments engaging hip/thigh/leg zone, including dress lower portions and jumpsuit legs.

### Fabric — Q1 importance

| Answer | Contribution |
|---|---|
| Very important | fabric.importance = very_important; raise quality threshold across all strategies |
| Important — I notice, but I can compromise | fabric.importance = important; standard quality threshold |
| Not a priority | fabric.importance = low; lower quality threshold |

**Modifier.** Modulates quality scoring; doesn't filter directly.

### Fabric — Q2 discomforts

| Answer | Contribution |
|---|---|
| Clings | fabric.discomforts includes "clings" → filter items with high-confidence cling tag; downrank items with medium/low confidence cling tag |
| Stiff | fabric.discomforts includes "stiff" → filter items with high-confidence stiff tag; downrank items with medium/low confidence stiff tag |
| Heavy | fabric.discomforts includes "heavy" → filter items with high-confidence heavy tag; downrank items with medium/low confidence heavy tag |
| Wrinkles | fabric.discomforts includes "wrinkles" → filter items with high-confidence wrinkle-prone tag; downrank items with medium/low confidence wrinkle-prone tag |

**Constraint (tag-confidence-gated).** Filter behavior depends on tag confidence. High-confidence tags filter; medium/low-confidence tags downrank. See Fabric Policy in Section 1 for the full rule. This prevents false-negative filtering when fabric properties are inferred from category-level data rather than confirmed from product information.

### Fabric — Q3 attention to detail

| Answer | Contribution |
|---|---|
| Notice immediately | attention_to_detail = high; weight construction details in scoring |
| Notice but not deal breaker | attention_to_detail = medium; modest weight |
| Don't pay much attention | attention_to_detail = low; minimal construction-detail weight |

**Modifier.** Modulates scoring weights.

### Pants/jeans — Q1 rise

| Answer | Contribution |
|---|---|
| Low rise | rise includes "low" |
| Mid rise | rise includes "mid" |
| High rise | rise includes "high" |
| None — flexible | rise = ["flexible"] (all rises available) |

**Preference.** Selected rises weighted up; non-selected rises available at neutral. "Flexible" leaves all neutral.

If user selects specific rise + body type rules suggest different default → user preference wins; body-compatible execution rules apply within unlocked category (e.g., apple user picks low-rise → low-rise items available, surfaced with execution rules favoring below-midsection rise + skim-fit hip + fluid fabric).

### Pants/jeans — Q2 cuts to avoid

| Answer | Contribution |
|---|---|
| Straight | cut_avoid includes "straight" |
| Wide | cut_avoid includes "wide" |
| Flared | cut_avoid includes "flared" |
| Bootcut | cut_avoid includes "bootcut" |
| Slim | cut_avoid includes "slim" |
| Barrel | cut_avoid includes "barrel" |
| I'm flexible | cut_avoid is empty |

**Constraint.** Filters explicitly. "We won't show them."

### Pants/jeans — Q3 lengths to avoid

| Answer | Contribution |
|---|---|
| Full length | length_pants.avoid includes "full" |
| Cropped | length_pants.avoid includes "cropped" |
| Capri | length_pants.avoid includes "capri" |
| None — flexible | length_pants.avoid is empty |

**Constraint.** Filters.

### Dresses/skirts — Q4 lengths preferred

| Answer | Contribution |
|---|---|
| Short — above the knee | length_skirts_dresses.preferred includes "short" |
| Mid — around the knee / mid-calf | length_skirts_dresses.preferred includes "mid" |
| Long — below the calf / full length | length_skirts_dresses.preferred includes "long" |

**Preference.** Selected lengths weighted up; non-selected lengths available at neutral but lower priority. Not a constraint — short items still available if user didn't pick short, just deprioritized.

### Exposure — Q5 Step 1

| Answer | Contribution |
|---|---|
| Comfortable with it | exposure_overall = comfortable |
| Only a little — depending on the area | exposure_overall = depends |
| I prefer coverage | exposure_overall = prefer_coverage |

**Modifier.** Modulates reveal mode access globally.

### Exposure — Q5 Step 2

| Answer | Contribution |
|---|---|
| Arms | exposure_covers includes "arms" → filter sleeveless |
| Shoulders | exposure_covers includes "shoulders" → filter off-shoulder, halter, strapless |
| Back | exposure_covers includes "back" → filter low-back, open-back, lace-up back |
| Chest / neckline | exposure_covers includes "chest" → filter deep V, plunging, low scoops |
| Midriff | exposure_covers includes "midriff" → filter crop tops, midriff cutouts |
| Legs (shorts, slits) | exposure_covers includes "legs" → filter short hems, mini, slits revealing thigh |

**Constraint.** Filters items revealing covered zones.

### Permissiveness derivation

Computed from question answers:

```
permissiveness.signals.multi_strategy = (count of selected strategies >= 3)
permissiveness.signals.multi_fit = (count of selected fit options across top + bottom >= 3)
permissiveness.signals.multi_volume = (count of selected volume options >= 2)
permissiveness.signals.multi_featuring = (count of named featuring zones >= 2)
permissiveness.signals.broad_fabric = (count of fabric discomforts <= 1)
permissiveness.signals.broad_exposure = (exposure_overall == comfortable AND count of covers <= 2)
permissiveness.signals.flexible_cut_or_rise = (cut_avoid is empty OR rise == flexible)

permissiveness.score:
  - High: 5+ signals fire
  - Medium: 3-4 signals fire
  - Low: 0-2 signals fire
```

Permissiveness output affects scoring strictness, catalog width, hero weighting, and behavior data sensitivity.

---

## Section 5: Worked Examples

*Note: Section 5 appears before Section 3 in document order because worked examples were built first and surface the combinations Section 3 then formalizes. Read in order: 1 → 2 → 5 (examples) → 3 (resolutions surfaced by examples) → 4 (scoring framework).*

This section walks complete users through the synthesis layer end-to-end. Each example validates the framework against a real case and surfaces patterns that go into Section 3 (Combination Resolutions).

### Worked Example 1 — Moran (tall rectangle, high permissiveness, multi-strategy)

User: Moran. Profile resolved from questionnaire answers.

#### Inputs from questionnaire

- Height: 170+ → height_tier = tall
- Body proportions: shoulders, waist, hips about same width → body_type = rectangle
- Snug: chest, waist/stomach
- Loose: seat
- Featuring zones: décolletage/collarbones, legs
- Fit issues: everything sits how it should
- Length issues: everything sits where it should
- Strategy: anchor + sculpt + edge + trace (with execution requirement noted in revision)
- Volume: mostly bottom + balanced
- Fit tops: relaxed + oversized + close (with shaping gate)
- Fit bottoms: close + relaxed + oversized
- Fabric importance: important
- Fabric discomforts: clings + stiff + heavy
- Attention to detail: low
- Rise: flexible
- Cut avoid: slim + barrel
- Length pants avoid: none
- Skirt/dress length preferred: mid + long
- Exposure overall: depends
- Exposure covers: back + midriff

#### Resolved profile

**Body identification:**

```
body_type: rectangle
variation:
  frame:
    value: standard
    confidence: medium (chest + waist snug suggest fuller torso, not lean; absence of fit issues prevents high confidence)
  ribcage_signal:
    value: wider
    confidence: low (single snug-zone signal at chest, no fit issue reported)
  midsection_signal:
    value: prone
    confidence: low (single snug-zone signal at waist, no fit issue reported)
  seat_signal:
    value: flat
    confidence: high (loose at seat is the classic rectangle signal AND aligns with body type default)
height_tier: tall
```

The chest + waist snug combination produces a "fuller torso, balanced overall" variation reading — applies both ribcage and midsection-prone modulators in mild form. Because both have low confidence, the variation rules apply as soft preferences rather than aggressive modifiers. Closed high necklines deprioritized but not filtered; drawstring-at-natural-waist deprioritized but not aggressively filtered. Behavior data will refine confidence over time.

**Strategies:**

```
strategies:
  - trace: selected = true, weight = high, execution_gate.quality_threshold = high
    notes: "user added trace with explicit perfect-execution requirement; cling-averse + stiff-averse + heavy-averse fabric profile means trace items must have body-with-drape fabric"
  - anchor: selected = true, weight = high
  - sculpt: selected = true, weight = high
  - edge: selected = true, weight = high
multi_strategy_signal: true (4 strategies)
```

All four strategies in play. The strategy-frame principle means items execute different strategies and get evaluated against their own strategy's criteria.

**Featuring zones:**

```
featuring_zones:
  décolletage:
    named: true
    treatment: amplify (rectangle default asset)
    mode: sophisticated (named + moderate exposure + chest available)
  legs:
    named: true
    treatment: amplify (rectangle default asset)
    mode: sophisticated (named + short not in length preferences + legs available in exposure)
nothing_in_particular: false
```

Two zones named. Both default rectangle assets. Both amplified. Mode for legs is sophisticated because user didn't pick short — leg featuring through fit, slit, ankle reveal, leg-line emphasis rather than skin reveal.

**Fit policy:**

```
fit_top:
  selected: [relaxed, oversized, close]
  shaping_gate: true (close fit available when item provides shaping — ribbed, structured, fitted with body)
fit_bottom:
  selected: [close, relaxed, oversized]
```

Tight not selected for either — bodycon and skintight items deprioritized.

**Volume policy:**

```
volume_preferences: [mostly_bottom, balanced]
```

Mostly-top not selected (oversized button-up tops would surface as "balanced overall" since they're roomy but flat, not voluminous). Minimal not selected.

**Fabric policy:**

```
fabric:
  importance: important
  attention_to_detail: low
  discomforts: [clings, stiff, heavy]
```

Filter: clingy thin fabrics (slinky polyester, thin viscose, thin jersey), stiff non-draping fabrics (stiff denim, structured cotton without give, taffeta), heavy bulky fabrics (thick wool, chunky knits, heavy canvas).

Surface: fluid drape with body (good silk, mid-weight cotton, viscose with body, modal jersey), structured stretch (ponte, structured stretch blends), soft-with-body knits (fine merino, soft cashmere, mid-weight cotton knit), ribbed knits with structure.

Quality threshold elevated for trace items specifically (execution gate).

**Length policy:**

```
length_pants:
  avoid: []
length_skirts_dresses:
  preferred: [mid, long]
  not_preferred: [short] — deprioritized but not filtered
```

Short is deprioritized for skirts/dresses but available if item is a strong match on other dimensions (e.g., short A-line in fluid fabric with V-neck featuring décolletage might still surface despite length not being preferred).

**Cut policy:**

```
cut_avoid: [slim, barrel]
cut_available: [straight, wide, flared, bootcut]
rise: [flexible]
```

**Exposure policy:**

```
exposure_overall: depends
exposure_covers: [back, midriff]
exposure_zones_available: [arms, shoulders, chest, legs]
```

Filter: low-back, open-back, keyhole back, lace-up back, halter with bare back, crop tops, midriff cutouts.

Available: sleeveless (arms ok), off-shoulder (shoulders ok), V-necks and scoops (chest ok), knee-and-up hems (legs ok — though length preference deprioritizes short).

**Reveal modes (per named zone):**

```
reveal_modes:
  décolletage: sophisticated
    derived from: named + moderate overall exposure + chest available + no plunging signal
  legs: sophisticated
    derived from: named + short not preferred + legs available in exposure
```

**Style policy:**

```
style_policy:
  primary_archetype: not_yet_captured
  secondary_archetypes: not_yet_captured
  intensity: not_yet_captured
  rejected_aesthetics: not_yet_captured
  status: not_yet_captured
```

Style archetype not captured in current questionnaire. Stated outfits (low-rise jeans + ribbed polos, oversized striped button-ups, fitted tank + wide-leg + boxy short jacket, V-neck midi dress with waist, ribbed turtleneck + structured blazer + denim) suggest a clean menswear-inflected aesthetic — fitted ribbed knits, denim, structured tailoring, occasional polka-dot midi for feminine accent. Behavior data over time will refine. Until style archetype is added to questionnaire, items like the fringed open knit cardigan (which rules-pass on body but reads as different style register) will surface and rely on behavior data to filter.

**Permissiveness:**

```
permissiveness:
  score: high
  signals:
    multi_strategy: true (4 strategies)
    multi_fit: true (6 fit options selected across top + bottom)
    multi_volume: true (2 volume options)
    multi_featuring: true (2 zones)
    broad_fabric: false (3 discomforts flagged)
    broad_exposure: false (depends + 2 covers)
    flexible_cut_or_rise: true (rise flexible)
  total_signals_fired: 5 of 7
```

High permissiveness despite 3 fabric discomforts and 2 covers, because everything else signals styling flexibility. Most signals firing.

**Filters (organized by category):**

```
true_hard_filters:
  # User-explicit cut avoids
  - slim cut trousers/jeans
  - barrel cut trousers/jeans
  
  # User-explicit exposure covers
  - low-back dresses and tops
  - open-back items
  - keyhole back
  - lace-up back
  - bare-back halter
  - crop tops
  - midriff cutouts
  
  # Fabric discomfort filters (HIGH-CONFIDENCE TAGS ONLY)
  # Items confidently tagged with these properties filter; uncertain tags downrank instead
  - clingy thin fabrics across torso (when product explicitly described as clingy, sheer, body-hugging stretch in thin gauge, etc.)
  - stiff non-draping fabrics (when product explicitly described as rigid, structured, non-stretch, crisp; high-weight wool without drape; taffeta; stiff denim)
  - heavy bulky fabrics (when product explicitly described as heavy-weight, thick, chunky; canvas-weight; >300gsm wool)

body_type_structural_filters:
  # Apply when item doesn't have compensating features that shift strategy frame
  - drop-waist dresses (failure crosses all strategies — eliminates leg asset regardless of execution)
  - empire-line column dresses with no features or openings (verify before filtering — empire-column with strong edge features could surface)
  - bulky chunky knit sweaters hanging straight from shoulder to hip with no openings (verify — knits with strategic openings could execute edge)
  - wide-strap tanks with no structure that read as flat panels (verify — tanks with construction or drape could pass)

strategy_frame_filters:
  trace:
    - poor-execution trace items (cheap stretch jersey, flimsy fitted construction)
    - close-fit tops without shaping support (apply when item executes trace)
    - quality threshold elevated for trace specifically (execution gate from user signal)
  anchor:
    - soft anchor items (drawstring, self-tie on flowy fabric, thin string belt on heavy fabric)
    - applies when item is executing anchor strategy
  sculpt:
    - fast-fashion sculpt items that promise structure but deliver polyester drape
    - applies when item is executing sculpt strategy
  edge:
    - single-feature edge items with no compensation (one open neckline but no other featuring)
    - soft filter — edge has lowest precision requirements

permissiveness_modulated_filters:
  # For high-permissiveness profile: most of these surface
  - items requiring sophisticated styling execution → surface (user has styling literacy)
  - items at edge of body type tolerance → surface (multi-strategy supports range)
  - items with marginal style match → surface (behavior data will refine)
  - medium/low-confidence fabric tags matching user discomforts → downrank significantly; surface only with strong compensating signals
    Example: a denim shirt tagged medium-confidence "stiff" (category default for denim) gets downranked, but doesn't filter. If the item has strong other signals (V-neck featuring named décolletage + oversized matching preference + boxy short proportion match), it can still surface despite the uncertain stiff tag. Behavior data on save/dismiss will refine the system's confidence in similar items over time.
```

For Moran's high-permissiveness profile, the permissiveness_modulated_filters mostly surface rather than filter. The catalog is wide; behavior data will refine ranking over time. This is especially important for fabric tags — the system surfaces uncertain-tag items rather than filtering them, accepting that some won't be hits but trusting Moran's styling literacy to dismiss what doesn't work and behavior data to refine the tagging precision over time.

**Restrictiveness output:**

```
restrictiveness: wide
catalog_width: large
hero_weighting: standard (not aggressive — broad catalog with ranking)
behavior_data_sensitivity: high (lots of space; behavior refines quickly)
```

#### What this profile means for surfacing

**Items the system would surface as heroes:**

Tops:
- Ribbed knit fitted tops (turtleneck, polo, scoop, V-neck) — trace + close with shaping gate satisfied
- Fitted ribbed polos with collar and buttons (your outfit 1)
- Fitted tank tops with structured construction (ribbed, ponte, structured stretch)
- Relaxed ribbed turtlenecks
- Soft drape blouses with V-neck or asymmetric neckline
- Oversized button-up shirts hitting at hip/seat (vertical line through collar + placket; edge through proportion play)

Bottoms:
- Close-fitting straight jeans (close fit, available cut)
- Bootcut jeans in dark wash (sophisticated leg feature through ankle flare)
- High-rise wide-leg trousers in fluid wool blend (relaxed/oversized + bottom volume)
- Semi-wide high-rise jeans (your outfit 6)
- Flared jeans with high or mid rise

Dresses:
- Midi A-line dresses with fitted bodice + V-neck (anchor through construction + sophisticated décolletage)
- Midi shirt dresses with structured belt
- Maxi dresses with high waistline and column skirt (vertical line + long preferred)
- Midi or maxi dresses with side slits (sophisticated leg featuring through controlled reveal)
- Structured wrap dresses with substantial wide-wrap construction and flared skirt
- Fit-and-flare midi dresses with structured bodice (sculpt)
- Long flowy fluid tunic dresses with strategic openings — V-neck, slits, wrist openings (edge through multiple strategic features — Moran's edge strategy executing without needing waist construction)

Outerwear:
- Tailored blazers with structured shoulder
- Boxy short jackets ending at waist (your outfit 4)
- Structured-shoulder wool blazers (sculpt)
- Long open dusters worn over fitted base (tall rectangle hero — vertical line)
- Princess-seamed coats with subtle waist shaping

Skirts:
- Midi A-line skirts in structured fabric
- Midi pleated skirts with structured waistband
- Midi pencil skirts paired with tucked fitted ribbed top
- Maxi skirts with high waistline and column drape

**Items the system would filter:**

- Anything in slim or barrel cut trousers/jeans (user-explicit avoid)
- Anything revealing back or midriff (user-explicit cover)
- Tight bodycon dresses (tight not selected for tops; cling-averse)
- Drop-waist dresses (universal rectangle structural failure)
- Empire-line column dresses (universal rectangle structural failure)
- Bulky chunky knit sweaters with no openings or features (universal failure)
- Stiff structured cottons without give (fabric discomfort)
- Heavy thick wool tops or chunky cardigans (fabric discomfort)
- Thin clingy jersey tops (fabric discomfort)
- Drawstring shapeless cotton tunic dress with no openings (fails as anchor AND fails as edge — no compensation in either strategy frame)

**Items the system would surface at lower priority (not filter, just deprioritize):**

- Short skirts and dresses (length preference)
- Short A-line dresses with V-neck and slit (could still surface as hero if execution is strong because décolletage and legs both featured, but ranked below mid-and-long options)
- Tight bodycon items (tight not selected)

**Validation against stated outfits:**

| Outfit | Profile match | Notes |
|---|---|---|
| Low-rise jeans + fitted ribbed black polo | ✓ Hero | Close fit with ribbed shaping gate; trace + edge through décolletage; flexible rise |
| Striped knit with collar and buttons, not long | ✓ Hero | Fitted knit with shaping; collar+buttons = vertical detail |
| Striped oversized shirt + straight jeans | ✓ Hero | Edge through proportion play; oversized top selected; close-to-relaxed straight jeans |
| Fitted tank + high-rise wide-leg + boxy short jacket | ✓ Hero | Edge through proportion play + sculpt through structured short jacket |
| V-neck/button midi dress with waist | ✓ Hero | Anchor through fitted bodice; sophisticated décolletage; sophisticated leg through length |
| Relaxed ribbed turtleneck + structured blazer + semi-wide denim | ✓ Hero | Sculpt through structured-shoulder blazer; trace through fitted-but-relaxed ribbed knit |

All six outfits map to hero patterns the profile produces. Strong validation.

**Validation against six test items shown (denim shirt, suede bomber, tunic dress, ribbed polo, asymmetric top, fringed cardigan):**

| Item | Profile verdict | Notes |
|---|---|---|
| TRF denim shirt (boxy V-neck) | Surfaced — fabric-quality gated | V-neck features décolletage; boxy short top matches oversized preference; denim drape quality determines final ranking |
| Faux suede bomber jacket | Surfaced as hero | Matches "boxy short jacket" pattern; sculpt + edge; oversized; structured shoulder; soft drape with body |
| Striped tunic dress (flowy long) | Surfaced as hero | Edge strategy executing through multiple strategic features (V-neck featuring décolletage, slits featuring legs, wrist openings featuring lean extremity, vertical fabric texture); long preferred; oversized acceptable; not filtered because anchor isn't the strategy in play |
| Ribbed polo T-shirt | Surfaced as hero | Trace with shaping gate satisfied; fitted close; ribbed knit; collar+placket vertical detail; named décolletage |
| Asymmetric ribbed top | Surfaced as hero | Trace + edge through asymmetric construction; ribbed knit; close fit with shaping; named featuring |
| Fringed open knit cardigan | Surfaced | Long open layer for tall rectangle (vertical line hero); decorative detail doesn't fail filters; style-aesthetic match not captured by current questions |

All six items resolve correctly against the framework, including the tunic dress (previously incorrectly filtered when I applied anchor rules to an edge item).

#### What this worked example reveals

Things the synthesis layer handles cleanly:

1. **Multi-strategy users get wide catalogs** — all four strategies' hero patterns surface; items execute whichever strategy they fit and get evaluated on that strategy's criteria.
2. **Featuring zones + mode derivation works** — décolletage + chest available + moderate exposure = sophisticated mode (not reveal, not coverage). Legs + short not preferred + legs exposure available = sophisticated mode through slits and fit.
3. **Permissiveness produces wide catalog** — even with 3 fabric discomforts, the overall signal is permissive because other signals indicate flexibility.
4. **Preference vs. constraint distinction holds** — short skirts deprioritized but not filtered; slim trousers filtered explicitly. Tight items not in fit selection but available for high-specificity contexts (evening) with stronger support required.
5. **Strategy-frame principle prevents over-filtering** — tunic dress that would fail anchor rules surfaces as hero edge piece.
6. **Confidence levels on variation prevent over-modulation** — Moran's mild wider-ribcage and midsection-prone signals (single snug-zone each, no fit issue) are low-confidence; the variation modulators apply as soft preferences rather than aggressive filters. A high-confidence wider-ribcage signal (snug + fit issue + repeated discomfort) would apply more strictly.
7. **Four-category filter structure prevents over-filtering** — true hard filters (user-explicit avoids, covers, high-confidence fabric discomforts) always filter; body-type structural failures verify strategy-frame before filtering; strategy-frame filters only fire when the corresponding strategy is in play; permissiveness-modulated filters mostly surface for permissive users.
8. **Fabric tag confidence prevents false-negative filtering** — when item fabric tags are uncertain (denim that could be stiff or drapey, knit that could be ribbed-structured or thin-synthetic), the system downranks rather than filters. False-negatives from over-filtering cost more than false-positives from surfacing borderline items; the user can dismiss what doesn't work, but she can't see what was filtered out. Behavior data refines tagging confidence over time.

Known gaps surfaced by this example:

1. **Style archetype not captured** — fringed cardigan rules-passes on body but reads as different style register than user's actual aesthetic (clean menswear-inflected). Style archetype isn't in current questionnaire; schema reserves placeholder; behavior data will refine until question is added. This is the highest-priority gap.
2. **Strategy weighting beyond binary selected/unselected** — currently all selected strategies weight equally. For multi-strategy permissive users (like Moran), the wide catalog absorbs this imprecision. For restrictive users, primary-strategy detection from secondary signals will matter more. Secondary-signal refinement logic documented in Section 2 Q5 but not fully implemented in scoring.

---

### Worked Example 2 — Lital (petite hourglass, low-medium permissiveness, anchor-primary with casual-classic style)

User: Lital. 160 cm, 55-56 kg, hourglass. Profile resolved from V2 questionnaire answers.

#### Inputs from questionnaire

- Height: 160-164 → height_tier = petite (borderline petite-mid; petite confirmed by pant-length-too-long signal)
- Body proportions: shoulders and hips similar with smaller waist → body_type = hourglass
- Snug zones: chest (ambiguous signal — could be fuller bust or wider ribcage; low confidence)
- Loose zones: waist (classic hourglass loose-at-waist confirmation)
- Featuring zones: waist + legs
- Fit issues: pulls across the front of pants (curvy-bottom signal — needs cut that accommodates thigh/front rise)
- Length issues: pants feel too long (petite confirmation)
- Strategy: trace + anchor, with anchor stated as primary ("mostly anchor")
- Volume: mostly bottom
- Fit tops: relaxed (only)
- Fit bottoms: relaxed (only)
- Fabric importance: not a priority (lowest tier)
- Fabric discomforts: stiff + heavy + clings
- Attention to detail: medium
- Rise: high
- Cut avoid: slim + barrel
- Length pants avoid: cropped + capri
- Skirt/dress length preferred: short
- Exposure overall: depends
- Exposure covers: midriff

Style archetype (inferred from stated wardrobe — gap pending questionnaire addition): **casual + classic, menswear-inflected** (jeans + t-shirts + button-downs + crew-neck knits + soft blazers worn open; no designed-feminine pieces, no romantic detail, no wraps/ties/bodices)

#### Resolved profile

**Body identification:**

```
body_type: hourglass
variation:
  frame:
    value: standard
    confidence: high
  bust_signal:
    value: standard
    confidence: low (chest snug "maybe" — ambiguous; could be fuller bust or wider ribcage; not strong enough to commit)
  midsection_signal:
    value: standard
    confidence: high (no fit issues at waist; loose at waist = classic hourglass)
  seat_signal:
    value: projected
    confidence: medium (hourglass default; no specific signal)
  additional: "pulls at front of pants = curvy-bottom signal — needs cut that accommodates thigh and front rise; high-rise + relaxed-leg combination addresses this"
height_tier: petite
```

**Strategy weighting:**

```
strategies:
  trace:
    selected: true
    weight: medium-high (secondary)
    notes: "trace + relaxed fit resolves through fabric drape — body-following items without skin-cling (soft-drape blouses, knits with body, fabric that follows form). Not skim-fit trace, which would require close fit."
  anchor:
    selected: true
    weight: high (primary — user stated "mostly anchor")
    notes: "primary strategy. Waist named + anchor selected + smaller waist = strong waist-emphasis intent."
  sculpt:
    selected: false
    weight: neutral
  edge:
    selected: false
    weight: neutral
primary_strategy: anchor
multi_strategy_signal: false (2 strategies, both honor-body)
```

**Featuring zones:**

```
featuring_zones:
  waist:
    named: true
    treatment: amplify (hourglass default asset)
    mode: sophisticated (named + moderate exposure + no plunging cues)
  legs:
    named: true
    treatment: unlock (legs aren't hourglass primary asset; user signal unlocks featuring)
    mode: reveal (named + short skirt preferred + legs available in exposure)
nothing_in_particular: false
```

**Fit policy:**

```
fit_top:
  selected: [relaxed]
  shaping_gate: false (close not selected; cross-garment fit propagation rule applies — no fitted upper body across any garment category)
fit_bottom:
  selected: [relaxed]
notes: "Single relaxed register. Cross-garment fit propagation: dresses with fitted bodice filter, jumpsuits with fitted upper body filter, fitted-closed blazers filter."
```

**Volume policy:**

```
volume_preferences: [mostly_bottom]
```

**Fabric policy:**

```
fabric:
  importance: low (not a priority)
  attention_to_detail: medium
  discomforts: [stiff, heavy, clings]
notes: "Three discomforts but low importance. Tag-confidence-gating critical — high-confidence tags filter; medium/low-confidence tags downrank. Quality threshold standard (low importance overrides any execution-gate elevation)."
```

**Length policy:**

```
length_pants.avoid: [cropped, capri]
length_skirts_dresses.preferred: [short]
```

**Cut policy:**

```
cut_avoid: [slim, barrel]
cut_available: [straight, wide, flared, bootcut]
rise: [high]
notes: "Pulls at front of pants + relaxed fit_bottom = high-rise + relaxed-leg cut (wide, straight, flared) in cuts that accommodate curvier bottom. Standard cuts may not work; brands offering curvier construction for these cuts are preferred when available."
```

**Exposure policy:**

```
exposure_overall: depends
exposure_covers: [midriff]
exposure_zones_available: [arms, shoulders, back, chest, legs]
```

**Reveal modes:**

```
reveal_modes:
  waist: sophisticated
  legs: reveal
```

**Style policy:**

```
style_policy:
  archetypes_selected: [casual, classic] (inferred — INFERRED status, not captured)
  intensity: clear
  rejected_archetypes: [romantic] (inferred from stated wardrobe avoiding wraps/ties/bodices/feminine detail)
  status: inferred
  notes: "Inferred from stated outfit examples — jeans + t-shirts + button-downs + crew necks + soft blazers, no designed-feminine pieces. Menswear-inflected casual-classic. Strong signal but pending direct capture."
```

**Permissiveness:**

```
permissiveness:
  signals:
    multi_strategy: false (2 strategies, both honor-body, anchor primary)
    multi_fit: false (relaxed only)
    multi_volume: false (mostly_bottom only)
    multi_featuring: true (2 zones)
    broad_fabric: false (3 discomforts, mitigated by low importance)
    broad_exposure: true (depends + 1 cover)
    flexible_cut_or_rise: false (cuts avoided + specific rise)
  total_signals_fired: 2 of 7
  score: low-medium
  notes: "Restrictive in styling space (narrow fit, narrow volume, specific cuts/rise) but clear about featuring (2 zones named). 'Narrow but clear' rather than 'narrow because unclear' — she knows what she wants in a tight zone."
```

**Restrictiveness output:**

```
restrictiveness: narrow-to-moderate
catalog_width: medium
hero_weighting: aggressive (surface clear heroes; fewer borderline items)
behavior_data_sensitivity: high (narrow space = each engagement signal more meaningful)
```

#### Rules that fire

**Body-type rules active:**
- Hourglass natural waist asset (confirmed: waist named as feature)
- Hourglass + petite variation (short jackets at waist; cautious with midi; high-rise critical)
- Hourglass + curvy-bottom fit need ("pulls at front of pants" confirms — high-rise + relaxed-leg + cuts that accommodate)
- Hourglass + named legs in reveal mode (atypical featuring for hourglass; user signal unlocks)

**Strategy-frame rules:**
- Anchor active → anchor items evaluated by anchor criteria. Hourglass has natural waist; both hard and soft anchor work in principle. But cross-garment fit propagation rule filters construction-based anchor that requires fitted upper body (wraps, fitted bodices, belted dresses with cinching).
- Trace active → trace items evaluated by trace criteria. With relaxed fit, trace executes through fabric drape — body-following items without skin-cling.
- Sculpt and edge unselected → those strategies' failure modes don't apply.

**Cross-garment fit propagation (Lital's defining rule):**
- fit_top is relaxed-only → filter all fitted-upper-body items across categories
- Filtered: wrap dresses, fit-and-flare with fitted bodice, sheath dresses, belted shirt dresses with waist-cinching belt, fitted-closed blazers
- Allowed: shirt dresses worn untied, t-shirt dresses, A-line dresses with relaxed torso, slip dresses with skim drape (not bodycon)

**Anchor through styling vs. anchor through construction:**
- Construction anchor (wraps, belts, fitted bodices) filtered for Lital due to cross-garment fit propagation
- Styling anchor surfaces strongly: high-rise tucked-relaxed-top pattern is her dominant uniform; the body provides the waist, the styling reveals it

**Style policy (inferred):**
- Items matching casual + classic archetype: boosted
- Items matching romantic archetype: filtered (inferred rejection)
- Items matching polished/structured archetype: downrank (not her register)
- Items matching bohemian/edgy: downrank (not her register)

**Featuring framework:**
- Waist named + body has waist + anchor selected = strong amplify; surface anchor heroes (with cross-garment fit propagation filtering construction-anchor in favor of styling-anchor)
- Legs named + short preferred + legs available = unlock + reveal mode; surface short skirts and dresses (with fit propagation filtering fitted-bodice versions)

#### Items boosted (heroes)

**The dominant uniform:** high-rise relaxed jeans in straight or mildly-wide cut + tucked relaxed top + simple footwear. Plus short A-line items in casual fabrics for warmer contexts. Plus soft blazers worn open as outer layer.

**Tops (relaxed heroes for casual-classic):**
- Relaxed crew-neck t-shirts in soft cotton, short or long sleeve, tuckable length
- Relaxed V-neck or scoop t-shirts in soft cotton
- Crew-neck soft knits, relaxed not oversized, tuckable length (winter)
- V-neck soft knits, relaxed fit
- Striped relaxed button-down shirts in cotton or cotton-blend
- Plain relaxed button-downs in cotton or linen
- Polo-style relaxed knit shirts
- Relaxed cotton blouses with simple necklines

**Bottoms (high-rise relaxed heroes):**
- High-rise relaxed straight jeans in mid or dark wash, petite full-length or ankle
- High-rise relaxed mildly-wide jeans
- High-rise relaxed wide-leg jeans, often with drawstring
- High-rise relaxed straight trousers in soft cotton or linen blend
- High-rise relaxed wide-leg trousers in fluid fabric

**Outerwear (with refinement — relaxed, NOT oversized for petite scale):**
- Soft unstructured blazers in linen, cotton, or soft wool blend, **relaxed cut to her scale** (not oversized; ending at high hip or just below; petite-cut)
- Soft single-breasted blazers without heavy structure, worn open
- Boxy short denim jackets ending at waist
- Cropped denim jackets
- Crew-neck cardigans in soft knit, relaxed not oversized
- Simple button-down cardigans
- Relaxed cotton over-shirts worn open as a jacket
- Trench coats with belt at waist worn untied or tied at back, petite-cut length

**Dresses (filtered for relaxed fit_top — only casual-classic relaxed-bodice options):**
- Short t-shirt dresses, crew or V-neck, relaxed through body
- Short shirt dresses worn untied
- Short A-line cotton dresses with crew or V-neck and **relaxed bodice** (A-line shape from cut, not bodice fitting)
- Short slip dresses with skim drape, not bodycon
- Short tunic dresses with relaxed body

NOT surfaced (filtered by cross-garment fit propagation + style):
- Wrap dresses
- Fit-and-flare with fitted bodice
- Belted shirt dresses (with cinching belt at waist)
- Sheath dresses
- Bodycon
- Princess-seamed dresses
- Designed-feminine pieces in general

**Skirts:**
- Short A-line denim skirts at high-rise
- Short A-line cotton skirts at high-rise

#### Items filtered (true hard filters + structural + cross-garment fit + style rejections)

**User-explicit avoids:**
- All slim trousers and jeans
- All barrel trousers and jeans
- All cropped pants
- All capri pants
- Crop tops, midriff cutouts

**Body-type structural failures:**
- Drop-waist dresses (eliminates the waist she named)
- Empire-line column dresses without slim variation

**Cross-garment fit propagation (fit_top relaxed-only):**
- Wrap dresses with fitted wrap top
- Fit-and-flare dresses with fitted/structured bodice
- Sheath dresses
- Bodycon dresses
- Belted dresses where belt cinches into fitted top
- Princess-seamed dresses
- Jumpsuits with fitted bodice
- Blazers exclusively in fitted-closed cut

**Fabric discomfort high-confidence filters:**
- Confidently-tagged stiff items (rigid denim, structured taffeta, heavy crisp cotton)
- Confidently-tagged heavy items (thick wool, chunky knits, canvas-weight)
- Confidently-tagged clingy items (thin slinky polyester, sheer body-hugging stretch)

**Style policy filters (inferred rejection of romantic):**
- Ruffled blouses and dresses
- Wrap dresses (also filtered by fit propagation — double signal)
- Decorative feminine detail
- Soft tie-front pieces (also filtered by fit propagation)
- Floral romantic prints in feminine styling

#### Items downranked

**Body-type-default items at low priority due to fit propagation or strategy:**
- Bodycon (filtered by fit, not just downranked)
- Pencil skirts (close-fitting bottom, fit_bottom is relaxed-only)
- Sheath dresses in skim-fit (filtered by fit)
- Tight knit tops (filtered by fit)

**Petite + length traps:**
- Midi dresses and skirts (hit at calf-widest on petite; downrank toward short)
- Maxi dresses (downrank; less petite-flattering)
- Long open dusters (significant downrank — swallow proportions at her scale)
- Long heavy outerwear (downrank — petite + heavy discomfort double signal)

**Style policy downranks (inferred archetype):**
- Polished/structured pieces (downrank — not her register)
- Bohemian items (downrank)
- Edgy items (downrank)
- Heavily embellished items (downrank)
- Loud prints in non-classic styling (downrank)

**Medium/low-confidence fabric tags matching discomforts:**
- Denim items with medium-confidence stiff tag → downrank but available (modern denim often has stretch; behavior data refines)
- Knit items with medium-confidence cling tag → downrank but available
- Wool items with medium-confidence heavy tag → downrank but available

**Strategy unselected (neutral, not boosted):**
- Sculpt-heavy structured pieces (available but not heroes)
- Edge-heavy statement pieces (available but not heroes)

**Featuring not named:**
- Deep V-necks beyond moderate depth (chest not specifically named)
- Plunging necklines (downrank)
- Off-shoulder, halter (shoulders not named)
- Low-back items (back not named, even though available)

#### Contradictions and uncertainty

**Contradictions:**

1. **Trace + relaxed fit.** Trace honors body shape; relaxed sits away from body. Resolution: trace executes through fabric drape (curvy-fit knit, fluid drape that follows form) rather than skin-fit. Not bodycon. Honor-through-fabric-behavior rather than honor-through-fit-closeness.

2. **Anchor + relaxed fit.** Anchor typically requires structure (wrap, belt, bodice). Resolution: anchor-through-styling — high-rise tuck point reveals the natural waist without garment construction. The body has the waist; styling shows it.

3. **Three fabric discomforts + lowest fabric importance.** She doesn't prioritize fabric quality but has specific discomfort properties. Resolution: tag-confidence gating handles this — high-confidence discomfort tags filter (physical comfort matters); low/medium-confidence tags downrank (quality compromises acceptable).

4. **Hourglass + named legs (atypical featuring).** Legs aren't hourglass primary asset. Resolution: user-named featuring unlocks; reveal mode unlocked through short preference + legs available; execution still respects body (full-thigh signal means leg-featuring through hem reveal, not through cling).

5. **Pulls at front of pants + relaxed bottom preference.** Pulls signal needs cut that accommodates fuller thigh/front rise; relaxed signal means leg shape is relaxed (wide, straight, flared — not slim). Resolution: high-rise + relaxed-leg cut in body-accommodating construction.

**Uncertainty in profile:**

- Chest snug "maybe" — ambiguous; could be fuller bust or wider ribcage; treating as standard with low confidence. Behavior data on neckline engagement refines.
- Style archetype inferred from stated wardrobe; not directly captured. Casual + classic is high-confidence inference but should be confirmed by direct question.

#### Final human-review questions

1. **Chest signal:** *Is the chest "snug" because tops feel tight there, or because shirts strain/pull there?* Resolves fuller-bust vs. wider-ribcage interpretation.

2. **Style archetype confirmation:** *Which describes your overall style: casual, classic, polished, romantic, edgy, sporty, bohemian, minimal, urban? (Select up to 3, rank top 2)* Fills the inferred gap directly.

3. **Bust featuring tolerance:** *Do you want chest area visible (V-necks, open collars) or prefer covered?* Resolves chest-not-named + chest-not-covered ambiguity.

4. **Length flexibility (skirts):** *Short preferred — would you ever wear knee-length or just-above-knee?* Distinguishes exclusive from preferred.

5. **Cross-garment fit confirmation:** *Would you wear a dress with fitted bodice for special occasions, or never?* Resolves whether cross-garment fit propagation is universal or context-dependent.

#### What this worked example reveals

**Things the synthesis layer handled cleanly:**

1. **Cross-body-type generalization** — same framework works for hourglass as for rectangle.
2. **Atypical strategy + body combination** — hourglass + anchor-primary + relaxed-fit works through anchor-through-styling rather than construction.
3. **Restrictive profile produces narrower hero-weighted catalog** — low-medium permissiveness, aggressive hero weighting, narrow space.
4. **Petite + curvy variation modulates correctly** — high-rise critical, full-length filtered, mid-length downranked, short heroed.
5. **Trace + relaxed conflict resolved through fabric interpretation** — trace as drape behavior, not fit closeness.

**Rules surfaced for Section 3 (newly documented):**

1. **Cross-garment fit propagation** — fit_top applies to dresses and other torso-engaging garments; fit_bottom applies to dress lower portions and jumpsuit legs. (Documented in Section 3.)
2. **Anchor through styling vs. anchor through construction** — body types with natural waist have two anchor mechanisms; cross-garment fit propagation determines which surfaces. (Documented in Section 3.)
3. **Strategy ranking from secondary signals** — multi-strategy users need primary detection from secondary signals; user-stated qualifiers matter. (Documented in Section 3.)

**Gaps revealed:**

1. **Style archetype** — the dominant gap. Lital's inferred casual + classic differs significantly from a polished-classic hourglass with identical body answers. Adding the style archetype question is the highest-priority next step.
2. **Curvy-bottom cut tagging** — "pulls at front of pants" needs corresponding item tagging (which cuts accommodate fuller thigh/front rise). Brand-level construction info matters here.
3. **Petite scale specification on outerwear** — "oversized soft blazer" works for tall scale; "soft relaxed blazer cut to petite scale" works for Lital. Item tagging needs petite-scale availability flag.



This section documents how the synthesis layer resolves combinations of signals where the resolution isn't obvious from Section 2 mappings alone. Rules emerge from worked examples; this section grows as new cases surface them.

### Cross-garment fit propagation

User fit preferences (Q7 fit_top, Q7 fit_bottom) apply across all garments engaging the corresponding body zone, not just to the named garment category.

**Principle:** fit is a per-body-zone experience, not a per-garment-category attribute. A user who doesn't want fitted upper body shouldn't be served fitted upper body in any garment category — including dresses, jumpsuits, or any garment whose upper portion covers the torso.

**fit_top selections apply to:**

- Standalone tops, t-shirts, blouses, sweaters, knits
- The upper portion (above natural waist) of: dresses, jumpsuits, rompers
- Blazers, jackets, cardigans when worn closed
- The experience-of-fit at the bust, ribcage, and upper torso

**fit_bottom selections apply to:**

- Standalone trousers, jeans, shorts
- The lower portion (below natural waist) of: dresses, skirts, jumpsuits
- The experience-of-fit at the hip, thigh, and leg

**Application logic:**

When fit_top does NOT include "close" or "tight":

*Filter standalone tops:*
- Wrap tops and surplice tops (the wrap construction creates fitted-bodice effect across the upper body)
- Fitted button-downs designed with darts, princess seams, or close-cut tailoring
- Fitted polos and fitted ribbed knits (fitted construction across torso)
- Peplum tops (the fitted bodice into peplum flare is fitted-upper-body)
- Bodysuits (fitted by construction across entire torso)
- Corset tops and corseted bodice tops
- Bustier tops
- Tied-waist tops where the tie cinches the fabric across the bust/ribcage
- Halter tops with fitted body
- Crop tops with fitted cut (separate from midriff-exposure rule; this filters the fitted-construction issue)
- Tank tops cut tight at the body (vs. relaxed-cut tanks which are fine)

*Filter dresses:*
- Wrap dresses (the wrap construction creates fitted-bodice effect)
- Fitted bodice construction in general (princess seams, boned bodice, structured tailored top)
- Sheath dresses (skim-fit through torso)
- Bodycon dresses
- Fit-and-flare with structured-fitted bodice (the bodice is fitted; even if the skirt is flared, the wearing experience is fitted-on-top)
- Belted dresses where the belt cinches into a fitted top
- Corset dresses and corseted bodice dresses

*Filter other categories:*
- Jumpsuits with fitted bodice or fitted upper body
- Rompers with fitted upper body
- Blazers/jackets that are exclusively fitted-cut and designed to be worn closed
- Vests with fitted/tailored construction worn closed

*Allow when fit_top is relaxed-only:*

*Standalone tops:*
- Relaxed t-shirts, blouses, knits in any neckline
- Oversized tops
- Relaxed button-downs (boyfriend fit, classic relaxed)
- Boxy tops and boxy cropped tops (boxy ≠ fitted)
- Loose tank tops
- Relaxed polo knits
- Soft drape blouses that follow body through fabric movement, not through fitted construction

*Dresses:*
- Shirt dresses worn untied or with relaxed belt at hip (not waist)
- T-shirt dresses
- A-line dresses with relaxed torso (A-line shape comes from cut, not from bodice fitting)
- Slip dresses with skim drape (drape that follows without clinging — distinct from bodycon)
- Tunic dresses with strategic features
- Trapeze and tent dresses
- Dresses where the waist break comes from styling (high-rise + tuck point of separates, or empire waist seam without bodice fitting) rather than construction

*Other categories:*
- Blazers and jackets in relaxed cut, especially when worn open
- Soft unstructured blazers in relaxed scale (size-appropriate; petite users get petite-cut relaxed, tall users get standard or oversized)
- Wide-leg jumpsuits with relaxed upper body
- Relaxed cardigans

When fit_bottom does NOT include "close" or "tight":

*Filter:*
- Skinny pants and skinny jeans
- Slim pants and slim jeans (when slim is fitted, not when slim is a leg-shape)
- Jumpsuits with skinny/slim leg construction
- Pencil skirts (close-fitting through hip and thigh)
- Bodycon dresses (already filtered by fit_top usually)
- Bodycon skirts
- Tight leggings as bottom layer (separate from athletic context)

*Allow:*
- A-line skirts
- Wide-leg pants and jumpsuits
- Relaxed straight-leg pants
- Bootcut and flared (relaxed through leg even when fitted at thigh)
- Trapeze and A-line dresses (relaxed through bottom)
- Pleated trousers

**Edge case: blazers worn open**

Blazers designed to be worn open (oversized cuts, drape-cut, lapel construction that implies open wear) function as outerwear layers rather than tops. The inner layer determines the top fit experience.

- Surface soft/relaxed blazers for relaxed-only users (worn open over fitted-or-tucked base)
- Continue to filter fitted-closed blazers (the kind that only works buttoned and creates a fitted-top experience)

**Why this rule matters:**

Without it, the system surfaces fitted-bodice dresses to users who only picked relaxed for tops, then can't explain why the recommendations feel wrong. The user said "relaxed only" — she meant it for upper body, regardless of whether the upper body is part of a top or part of a dress.

### Anchor through styling vs. anchor through construction (hourglass and pear)

For body types with a natural waist (hourglass, pear), anchor can be executed two ways:

**Anchor through construction:**
- Wrap dresses with substantial wrap
- Belted dresses at natural waist
- Belted blazers and coats
- Fitted bodice + skirt construction (fit-and-flare, sheath with waist seam)
- Peplum tops
- Tied-waist tops and blouses

The garment creates or emphasizes the waist through its own structure.

**Anchor through styling:**
- High-rise bottom + relaxed top tucked or half-tucked (the meeting point reveals the natural waist)
- High-rise bottom + tucked fitted top (similar pattern, fitted version)
- High-rise + crop tee combination at the waist meeting point
- Outerwear worn open over a relaxed base where the open layer frames the silhouette without engaging the waist

The body has the waist; styling reveals it. The garment doesn't construct anchor; the styling move creates it.

**When to surface each:**

- Anchor strategy selected + fit_top includes close: both construction-anchor and styling-anchor work; surface both
- Anchor strategy selected + fit_top is relaxed-only: filter construction-anchor items (wraps, belts, bodices, ties — they require fitted upper body to function); surface styling-anchor items (high-rise + tuck patterns)
- Anchor strategy + waist named as feature: both work; user is signaling she wants waist visible regardless of mechanism
- Anchor strategy + waist NOT named (user picked anchor but didn't name waist as feature): construction-anchor still surfaces but at lower confidence; styling-anchor may be more aligned with intent

**Why this rule matters:**

For body types without a natural waist (rectangle especially), anchor requires real construction because there's nothing underneath to reveal. For body types with a natural waist (hourglass, pear), anchor can be passive — the body provides the waist, the styling reveals it. The hourglass rules originally treated anchor as a category of garment construction; this rule extends anchor to include the styling moves that reveal the natural waist without garment-level construction.

### Strategy execution and item classification

When users select a strategy in Q5, they also select execution sub-classifications (which kind of anchor / sculpt / edge). The synthesis layer uses these to filter and rank items at higher precision than strategy alone.

**Item classification:**

Items are tagged with the strategy or strategies they execute, plus the execution sub-classification within each strategy:

- High-rise straight jeans → anchor (user_created); also potentially trace (if close-fit cut)
- Cropped top → anchor (user_created — the cut enables the meeting point with high-rise)
- Wrap top → anchor (garment_created)
- Wrap dress → anchor (garment_created)
- Belted shirt dress (belt is integral to silhouette) → anchor (garment_created)
- Fit-and-flare with structured bodice → anchor (garment_created) AND sculpt (waist_sculpt + lower_body_sculpt depending on flare drama)
- Corseted dress → sculpt (waist_sculpt)
- Princess-seamed sheath → sculpt (waist_sculpt)
- Peplum top → sculpt (lower_body_sculpt) AND anchor (garment_created)
- Mermaid skirt → sculpt (lower_body_sculpt)
- Structured-shoulder blazer → sculpt (shoulder_sculpt)
- Tailored blazer with strong waist suppression → sculpt (waist + shoulder)
- V-neck top → potentially edge (exposure_edge) if neckline is deep
- Off-shoulder top → edge (exposure_edge)
- Oversized button-up + slim jeans outfit → edge (proportion_edge)
- Bohemian decorative top → potentially edge (neither pure exposure nor pure proportion) — handled by user not selecting edge or by both edge options unselected

**User execution selections filter accordingly:**

When user selected a strategy AND selected execution sub-classifications:
- Items matching at least one selected execution within the selected strategy: surface
- Items in the selected strategy but matching only unselected executions: downrank
- Items in unselected strategies: evaluate by other rules (don't filter solely on strategy basis)

Example: Lital selects anchor + user_created only (no garment_created).
- High-rise straight jeans (anchor user_created): surface
- Cropped top (anchor user_created): surface
- Wrap dress (anchor garment_created): filter (cross-strategy with cross-garment fit propagation reinforcing)
- Princess-seamed sheath (sculpt waist_sculpt): she didn't select sculpt; not filtered solely on this; cross-garment fit propagation filters anyway because of relaxed-only fit_top

Example: Moran selects anchor + both user_created and garment_created.
- High-rise straight jeans: surface
- Cropped top: surface
- Wrap dress: surface (garment_created executed; she chose this execution)
- V-neck midi dress with fitted waist seam: surface (garment_created via waist seam)

**Overlap zones (items in multiple classifications):**

Some items execute multiple strategy/execution combinations. They surface for users who selected ANY of the matching executions:

- Wrap dress = anchor (garment_created) → surfaces for anchor+garment_created users
- Fit-and-flare with structured bodice = anchor (garment_created) AND sculpt (waist + lower_body) → surfaces for users selecting any of these
- Peplum top = sculpt (lower_body) AND anchor (garment_created) → surfaces for either
- Belted blazer (belt is integral) = anchor (garment_created) AND potentially sculpt (waist_sculpt if strong taper) → surfaces for either
- Structured-shoulder blazer with strong waist taper = sculpt (shoulder + waist) → surfaces for either execution

The union behavior is correct: an item that can execute multiple looks should be available to users who like any of those looks.

**The anchor-without-sculpt pattern (Dalia, Lital, Aunt):**

When user selects anchor + user_created only AND sculpt not selected:
- Surface: high-rise + tuck patterns, cropped + high-rise patterns, fitted button-downs worn untucked, soft tailored blazers worn open, belts as styling tool
- Filter: wraps (garment_created anchor), belted dresses (garment_created anchor), corseted bodices (sculpt), princess-seamed sheath (sculpt), peplum tops (sculpt), structured-shoulder-only blazers if shoulder is the dominant feature (sculpt)

This pattern is the meeting-point anchor archetype — body has natural waist (hourglass, pear) + user wants to control when/how it shows + no garment-imposed shape construction. Recognizable cluster across multiple users (Dalia, Lital, Aunt).

**The all-sculpt-options pattern (high-construction garment lover):**

When user selects sculpt + multiple execution options:
- Hero candidates include items combining multiple sculpt mechanisms (corseted-bodice fit-and-flare = waist + lower_body; structured-shoulder peplum jacket = shoulder + lower_body; etc.)
- Items doing only one sculpt move are heroes for users picking that one option specifically

### Strategy ranking from secondary signals

When a user selects multiple strategies in Q5, the synthesis layer should rank them rather than treat all as equally weighted. Primary strategy detection from secondary signals:

**Primary anchor signals:**
- User-stated "primary" or "mostly" qualifier (Lital said "mostly anchor")
- Waist named as featured zone
- High-rise rise preference (high-rise creates the anchor meeting point)
- Fitted bottom + tucked top in stated outfit examples

**Primary trace signals:**
- Close fit preference for tops AND bottoms
- High fabric importance + cling-averse (good trace requires good fabric)
- Stated outfit examples emphasize fitted/skim-fit construction
- Body type variation is lean (lean rectangle, slim hourglass)

**Primary sculpt signals:**
- Q8 attention to detail high (sculpt construction matters)
- Q1 fabric importance high (sculpt requires quality)
- Featuring zones that benefit from sculpt construction (rectangle waist, apple midsection)
- Stated outfit examples emphasize structured architectural pieces

**Primary edge signals:**
- Volume preferences mostly_bottom or mostly_top (proportion play)
- Multiple featuring zones named (multi-asset redirection)
- Stated outfit examples emphasize layered, proportion-play, or attention-redirect outfits

When secondary signals strongly point to one strategy, weight that strategy as primary even if user multi-selected. When signals are evenly distributed across selected strategies, weight equally.

For Lital: anchor selected + waist named + high-rise preferred + "mostly anchor" stated = strong anchor primary signal. Trace secondary.

### Multi-strategy users + permissiveness interaction

Multi-strategy selection is one of the strongest permissiveness signals — but it interacts with other signals to produce different patterns:

- *Multi-strategy + multi-fit + multi-zone + broad signals (Moran):* high permissiveness, wide catalog, all strategies surface, behavior data refines ranking
- *Multi-strategy + narrow fit + few zones + restrictive signals:* medium permissiveness, narrower catalog, strategies surface within fit constraints
- *Single strategy + narrow fit + few zones + restrictive signals (Lital):* low-medium permissiveness, hero-weighted catalog, surfacing precision matters
- *Single strategy + broad signals elsewhere:* medium permissiveness; strategy is clear but user is otherwise flexible

### Featuring zone reveal mode resolution

When a featuring zone is named, the reveal mode (reveal / sophisticated / coverage) is derived from:

- Exposure preferences for that zone
- Length preferences when relevant
- Other signals consistent with mode

Conflict patterns and resolutions:

- Zone named + zone covered in exposure → coverage mode (feature through fit/color/structure, not skin)
- Zone named + zone available in exposure + length preference deep/short → reveal mode
- Zone named + zone available in exposure + length preference moderate/sophisticated → sophisticated mode (default when ambiguous)
- Zone named + bust signal fuller + chest available → moderate-depth necklines; don't push to plunging without explicit signal

### Additional combination rules to be drafted

As more worked examples surface combinations that need explicit resolution, this section will grow. Patterns surfaced by Moran and Lital (relaxed-everywhere + anchor compensation; petite + curvy proportions; fabric discomfort + low importance interaction; trace + relaxed combination through fabric drape) are documented in their respective worked examples and will be generalized here as the framework stabilizes.

---

## Section 4: Item Scoring Framework

To be drafted after Section 3 stabilizes and additional worked examples (Lora) confirm the combination rules. Will cover:

- How items are evaluated against a resolved profile
- Strategy-frame scoring (items evaluated against the strategies they execute)
- Tag-based attribute matching with permissiveness-calibrated weights
- Style archetype multiplier
- Hard filter application vs. downrank application
- Final ranking output

---

## Sections to follow

Worked examples continue:

- **Worked Example 3: Lora** — petite rectangle with restrictive profile (trace-primary, narrow fit, restrictive fabric). Tests that the same body type rules apply at appropriate strictness for restrictive vs. permissive profiles within the same body type.

Additional examples (celebrities, edge cases) added as needed once Lora confirms the framework holds across permissiveness levels within a single body type.

