# The Daily Cut — Styling Framework

This document consolidates the body type rules, cross-body framework, and synthesis layer into a single reference. It covers how user signals translate into recommendation policy, with the body type rules as supporting reference material.

---

## Part 1: Core Operating Principle

**The system doesn't decide what is "flattering." It resolves what the user gave permission to use, then surfaces the most body-compatible version of her chosen direction.**

Body type rules describe geometric truth and strategy-specific success/failure modes — they are reference material, not filters. The user's signals (strategies, fits, featured zones, exposure, fabrics, cuts) define her operating universe. The system's job is to find items within that universe that work best for her body.

Consequences:

- Pear in celebrate mode gets bodycon hip-emphasis items. Body type rules inform which bodycon items work for pear curves (skim fabric, curvy-fit construction), not whether to filter bodycon.
- Rectangle selecting edge strategy gets items executing edge. Body type rules inform what good edge execution looks like for rectangle (multiple strategic features, asset-aligned redirects), not whether to filter items lacking anchor.
- Apple selecting low-rise gets low-rise items. Body type rules inform which low-rise works for apple (below-midsection rise, skim-fit hip, fluid fabric), not whether to filter low-rise.

**The system is anatomically intelligent, not anatomically prescriptive.**

---

## Part 2: The Strategy-Frame Principle

This is the most foundational rule. Read it before anything else.

Each body type has four strategies available: **trace, anchor, sculpt, edge**. Each strategy has its own success criteria and failure modes. The strategies are parallel options, not a hierarchy.

**The user's strategy selection determines which sections of body type rules apply.** Rules for strategies the user did not select do not apply.

Examples:
- Rectangle + edge + relaxed fit + no anchor mechanism → not a failure. Edge succeeds through strategic features (V-neck, slits, wrist openings), not anchor construction.
- Apple + edge + multiple alternative-zone features → not a failure. Midsection-management rules apply when anchor or trace is in play. Edge bypasses midsection by directing attention to legs, décolletage, face, ankles.
- Hourglass + edge + relaxed fit + no anchor → not a failure. Edge says "don't make silhouette the visual story; feature these zones instead."

**Item evaluation:** identify which strategy/strategies the item executes (wrap dress executes anchor; tunic with strategic openings executes edge; fit-and-flare executes sculpt; fitted ribbed knit executes trace). Evaluate against that strategy's criteria — not against all four.

An edge item that succeeds at edge (multiple features, asset-aligned redirects, proportion play) is a hero even without anchor mechanism. An edge item that fails at edge (single feature, no compensation, features that don't align with assets) gets filtered.

---

## Part 3: Filter Categories

Four filter categories with different override behavior:

### True hard filters (always filter, no override)

User-explicit signals the system honors absolutely:
- User-explicit cut avoids (Q3 cuts marked "won't show")
- User-explicit length avoids (Q3 lengths marked "won't show")
- User-explicit exposure covers (Q4 zones marked covered)
- Fabric discomforts WHEN tag confidence is high (see Part 7)

### Body-type structural filters (default filter, verify before applying)

Items where geometric failure crosses all strategies:
- Drop-waist on rectangle (shortens leg asset regardless of strategy)
- Empire-line column dresses with no features (verify — empire-column with strong edge features could surface)
- Bulky knit sweaters hanging straight with no openings (verify — knits with strategic openings could execute edge)

Test: does the failure mode cross all strategy frames, or is it specific to one?

### Strategy-frame filters (filter only when corresponding strategy is in play)

- Soft anchor (drawstring, self-tie) → fails when anchor is the strategy; doesn't apply when edge is the strategy
- Poor-fabric trace → fails when trace is the strategy
- Fast-fashion sculpt → fails when sculpt is the strategy
- Single-feature edge with no compensation → fails when edge is the strategy

### Permissiveness-modulated filters (filter for restrictive, surface for permissive)

- Items requiring sophisticated styling execution
- Items at the edge of body type tolerance
- Items that work but require careful pairing
- Fabric discomforts WHEN tag confidence is medium or low

For permissive users: surface; behavior data refines.
For restrictive users: filter; only obvious heroes surface.

---

## Part 4: Featuring Framework

Two signal streams from the questionnaire, both producing intent signals that interact with body-type defaults:

### Stream 1: Asset confirmation (Q1)

*What parts of your body do you naturally feel good about?* (Multi-select)

Zones the user identifies as existing assets. Triggers featuring with **trace-existing execution** — honor what's there.

### Stream 2: Help intent (Q2)

*Are there any areas you'd like some help with? Think about your go-to outfits — what are they doing for your body?*

- Make my legs look longer
- Create more waist definition
- Add more shape around hips / seat
- Smooth around my waist / stomach
- Make my bust look fuller
- Make my bust feel less prominent
- Make my shoulders feel softer
- Nothing specific

Zones where the user wants clothes to do work. Triggers featuring with **create-shape execution** (engineer dimension) or **management execution** (smooth, minimize, soften) depending on direction.

### How the streams combine

| Signal pattern | Treatment |
|---|---|
| Q1 names asset + Q2 enhances same zone | Strongest amplify (named asset AND active enhancement) |
| Q1 names asset alone | Standard amplify (asset confirmed, no active enhancement) |
| Q2 alone, create-direction | Unlock with create-shape execution (rectangle wanting seat shape) |
| Q2 alone, manage-direction | Unlock with management execution (apple wanting midsection smoothed) |
| Q1 names asset + Q2 manage on same zone | Contextual signal (likes it but manages it situationally — sophisticated mode with context awareness) |
| Neither | Fall back to body-type default |

### The four cross-body treatments (per zone)

When a zone is named (Q1 or Q2), the system applies one of four treatments depending on how the zone relates to the body type's geometric defaults:

- **Amplify** — named zone is a body-type default asset. Surface featuring items aggressively.
- **Unlock** — named zone is geometrically neutral. Treat as featuring zone even though defaults didn't elevate it.
- **Respect over default** — named zone is one the body type typically manages. User preference shifts toward celebrate-mode (or create-shape mode via Q2). Suppress default minimization moves for that zone.
- **Fall back** — zone not named. Apply body-type defaults; behavior data refines.

When user selects "nothing in particular" / "nothing specific": conservative body-type defaults, hero-weighted, behavior data critical.

---

## Part 5: The Three-Mode Framework

For each named featuring zone, the user operates in one of three modes. The mode determines which featuring items get prioritized.

### Reveal mode
Sustained skin reveal is acceptable. Bare-shoulder off-shoulder, deep V, fully open back, mini hems, crop tops, halter with bare shoulders.

### Sophisticated mode
Featured through fit, line, framing, and intermittent or controlled reveal rather than sustained exposure. Boat necks (broaden without bare shoulder), keyhole or asymmetric cutouts, three-quarter sleeves with detail, midi with slit (leg reveal in motion, not at rest), fitted bodice without cleavage, sheer panel insets.

### Coverage mode
Featured through emphasis (fit, structure, color, detail) but skin stays covered. High necklines with detail, structured shoulders with long sleeves, fitted-waist tops with closed necklines, color/print emphasis without skin reveal, monochromatic leg-extending palettes.

**Sophisticated mode is the most common state for adult dressers.** Default to sophisticated when signals are ambiguous. Reveal and coverage both real but require clearer signals.

### Mode detection

Detected through combination of:
- Featuring-zone question answers (Q1 + Q2)
- Exposure preferences (zone-specific when possible)
- Length preferences (short hems, mini, midi, maxi, crop, long sleeves)
- Behavior data over time

Resolution patterns:
- Names zone + selects reveal-friendly preferences → reveal mode
- Names zone + selects non-reveal preferences → sophisticated mode
- Names zone + selects coverage preferences → coverage mode (featured through styling, no skin)
- Doesn't name zone + reveals through exposure → defer to body-type defaults
- Doesn't name zone + covers it → primary emphasis elsewhere

### Featuring intent changes the goal, not the geometry

When a user names a zone the body type typically manages, the system shifts from "minimize this zone" to "feature this zone well" — but "well" still respects body-compatible execution. Featuring intent is not a permission slip to abandon geometry rules; it is a redirection of what geometry rules are optimizing for.

Example: Pear naming hips unlocks celebrate-mode (bodycon, pencil skirts following hip, low-rise, bright bottoms, hip-detail cuts). Still filters clingy cheap fabric that distorts the curve, hip-pocket bulk that adds visual width without shape, horizontal seams that segment rather than celebrate the hip line. Goal moved from "skim hips" to "feature hips well" — the second goal still has rules.

---

## Part 6: Profile Permissiveness

A user who signals high styling flexibility (multi-strategy, multi-fit, multi-volume, multiple zones, broad fabric tolerance, broad exposure) is telling the system: "I know how to use clothes. Most things work if not actively broken."

A user who signals narrow styling space (single strategy, single fit register, single volume, few zones, multiple fabric discomforts, restrictive exposure) is telling the system: "I need help. Working in a tight space. Surface only what definitely works."

**Same body type, opposite catalog widths. Body type rules don't change; their application strictness does.**

### High-permissiveness signals
- 3-4 strategies selected
- 3-4 fit options across top + bottom
- Multiple volume preferences
- Multiple featuring zones named
- Few or no fabric discomforts
- Broad exposure with few specific covers
- "Flexible" or "no preference" on rise, cut, length

### Low-permissiveness signals
- 1 strategy selected
- 1-2 fit options, skewed to one register
- Single volume preference or "minimal"
- "Nothing in particular" featuring or 1 zone only
- Multiple fabric discomforts
- Multiple zones covered
- Specific preferences on rise/cut/length

### Application strictness

- **High permissiveness:** negative signals require multiple to filter; single positive can rescue; wide catalog; behavior data refines aggressively
- **Restrictive:** single negative signal can filter; multiple positives required to overcome negatives; narrow hero-weighted catalog; behavior data confirms slowly
- **Median:** standard application

### What "obvious fail" means for a permissive user

- Actively works against the body in a way styling can't fix
- Closed item that can't be styled (tight items that don't allow layering, belting, tucking, or compensation)
- Explicit user constraint violated
- Universal structural failure for the body type

For permissive users, an item with one soft-rule signal but multiple compensating positives is not a fail. Restrictive users have lower thresholds for soft rules.

---

## Part 7: Tag-Confidence-Gated Filtering

Fabric discomforts (Q2) filter items only when the item's fabric tag has high confidence. When the tag is inferred or uncertain, treat as strong downrank rather than hard filter.

```
For each item matching a user discomfort:
  If item.fabric_tag.confidence = high → hard filter
  If item.fabric_tag.confidence = medium → strong downrank
  If item.fabric_tag.confidence = low → moderate downrank
```

**Tag confidence depends on data source:**
- **High:** explicit product description states the property; product imagery confirms; trusted brand tagging
- **Medium:** category-level inference with reasonable reliability ("denim" defaults to medium-stiff; "ponte" defaults to structured stretch)
- **Low:** category-level inference with high variation ("knit" — could be ribbed structured cotton or thin synthetic jersey)

**Principle:** false-negatives from over-aggressive filtering cost more than false-positives from surfacing borderline items. User can dismiss what doesn't work; can't see what was filtered. Applies to all fabric discomforts (clings, stiff, heavy, wrinkles).

---

## Part 8: Cross-Garment Fit Propagation

User fit preferences apply across all garments engaging the corresponding body zone, not just the named garment category.

**Principle:** fit is a per-body-zone experience, not a per-garment-category attribute. A user who doesn't want fitted upper body shouldn't be served fitted upper body in any category — including dresses, jumpsuits, or any garment whose upper portion covers the torso.

### fit_top applies to:
- Standalone tops, t-shirts, blouses, sweaters, knits
- Upper portion of dresses, jumpsuits, rompers
- Blazers/jackets when worn closed
- Experience-of-fit at bust, ribcage, upper torso

### fit_bottom applies to:
- Standalone trousers, jeans, shorts
- Lower portion of dresses, skirts, jumpsuits
- Experience-of-fit at hip, thigh, leg

### When fit_top is relaxed-only (no close, no tight)

**Filter standalone tops:** wrap tops, fitted button-downs, fitted polos, fitted ribbed knits, peplum tops, bodysuits, corset tops, bustier tops, tied-waist tops, fitted halter, fitted crop tops, tight tanks.

**Filter dresses:** wrap dresses, fitted bodice construction (princess seams, structured tailored top), sheath dresses, bodycon, fit-and-flare with structured-fitted bodice, belted dresses where belt cinches into fitted top, corset dresses.

**Filter other:** jumpsuits with fitted bodice, rompers with fitted upper body, blazers in fitted-closed cut, vests with fitted construction worn closed.

**Allow:** relaxed tops in any neckline, oversized tops, boxy tops, soft drape blouses that follow body through fabric movement (not fitted construction), shirt dresses worn untied, t-shirt dresses, A-line with relaxed torso, slip dresses with skim drape, tunic dresses, trapeze/tent dresses, dresses where waist comes from styling (high-rise + tuck) not construction, blazers worn open, soft unstructured blazers in relaxed scale.

### When fit_bottom is relaxed-only

**Filter:** skinny pants/jeans, slim pants when fitted-construction, jumpsuits with skinny/slim leg, pencil skirts, bodycon skirts, tight leggings.

**Allow:** A-line skirts, wide-leg pants and jumpsuits, relaxed straight-leg, bootcut and flared (relaxed through leg), trapeze dresses, pleated trousers.

### Edge case: blazers worn open

Blazers designed to be worn open function as outerwear layers rather than tops. Inner layer determines top fit experience. Surface soft/relaxed blazers for relaxed-only users (worn open over fitted-or-tucked base). Continue to filter fitted-closed blazers that only work buttoned.


---

## Part 9: Anchor Through Styling vs. Through Construction

For body types with a natural waist (hourglass, pear), anchor can be executed two ways.

### Anchor through construction
- Wrap dresses with substantial wrap
- Belted dresses at natural waist
- Belted blazers and coats
- Fitted bodice + skirt construction (fit-and-flare, sheath with waist seam)
- Peplum tops
- Tied-waist tops and blouses

The garment creates or emphasizes the waist through its own structure.

### Anchor through styling
- High-rise bottom + relaxed top tucked or half-tucked (meeting point reveals natural waist)
- High-rise bottom + tucked fitted top (similar pattern, fitted version)
- High-rise + crop tee at waist meeting point
- Outerwear worn open over relaxed base (frames silhouette without engaging waist)

The body has the waist; styling reveals it. Garment doesn't construct anchor.

### When to surface each

- Anchor + fit_top includes close → both work; surface both
- Anchor + fit_top is relaxed-only → filter construction-anchor (requires fitted upper body); surface styling-anchor
- Anchor + waist named → both work
- Anchor + waist NOT named → construction-anchor at lower confidence; styling-anchor more aligned

For body types without natural waist (rectangle, apple), anchor requires real construction because there's nothing to reveal. Hourglass and pear have a natural waist; anchor can be passive.

---

## Part 10: Profile Schema

The synthesis layer produces a structured profile per user. Schema below.

### Body identification
```
body_type: rectangle | inverted_triangle | hourglass | pear | apple
variation:
  frame: lean | standard | soft | athletic
  ribcage_signal: standard | wider (rectangle, hourglass)
  bust_signal: smaller | standard | fuller
  midsection_signal: standard | prone
  seat_signal: flat | projected | fuller
  additional: free-form
  (each with confidence: low | medium | high)
height_tier: petite | mid | tall
```

Confidence:
- **High:** multiple signals confirm
- **Medium:** single strong signal or consistent secondary signals
- **Low:** single weak signal

Higher confidence = variation rules fire more aggressively. Behavior data refines over time.

### Strategy weighting
```
strategies: array
  - strategy: trace | anchor | sculpt | edge
  - selected: boolean
  - weight: float (relative emphasis)
  - execution: object (sub-classification per strategy — see below)
  - execution_gate: { quality_threshold: high | standard | none }
```

Strategy execution sub-classifications (from Q5 follow-ups):

**Anchor execution:**
- user_created (rise, tucking, belting)
- garment_created (wraps, belted dresses, shaped-waist pieces)

**Sculpt execution:**
- waist_sculpt (corseted, princess-seamed, dramatic taper)
- lower_body_sculpt (peplum, fuller skirt, mermaid)
- shoulder_sculpt (structured blazer, defined shoulder)

**Edge execution:**
- exposure_edge (open necklines, slits, bare shoulder, open back)
- proportion_edge (oversized + slim, short + wide combinations)

### Featuring zones (Q1 — asset signal)
```
featuring_zones: array (one per named zone)
  - zone: décolletage | bust | shoulders | arms | waist | hips_curves | seat | legs | back
  - named: boolean
  - mode: reveal | sophisticated | coverage
  - treatment: amplify | unlock | respect_over_default | fall_back
nothing_in_particular: boolean
```

### Help intents (Q2 — enhancement/management signal)
```
help_intents: array
  - intent: legs_longer | waist_definition | hips_seat_shape | smooth_midsection |
            bust_fuller | bust_less_prominent | shoulders_softer
  - selected: boolean
nothing_specific: boolean
```

### Fit policy
```
fit_top:
  selected: subset of [tight, close, relaxed, oversized]
  shaping_gate: boolean
fit_bottom:
  selected: subset of [tight, close, relaxed, oversized]
```

### Volume, fabric, length, cut, exposure, style
```
volume_preferences: subset of [mostly_top, mostly_bottom, balanced, minimal]
fabric:
  importance: very_important | important | low
  attention_to_detail: high | medium | low
  discomforts: subset of [clings, stiff, heavy, wrinkles]
length_pants.avoid: subset of [full, cropped, capri]
length_skirts_dresses.preferred: subset of [short, mid, long]
cut_avoid: subset of [straight, wide, flared, bootcut, slim, barrel]
rise: subset of [low, mid, high, flexible]
exposure_overall: comfortable | depends | prefer_coverage
exposure_covers: subset of [arms, shoulders, back, chest, midriff, legs]
style_policy:
  archetypes: subset of [casual, classic, polished, romantic, edgy, sporty, bohemian, minimal, urban]
  intensity: quiet | clear | strong
  rejected: array
  status: captured | inferred | not_yet_captured
```

### Permissiveness
```
permissiveness:
  score: high | medium | low
  signals: {
    multi_strategy: boolean (3+ strategies)
    multi_fit: boolean (3+ fit options)
    multi_volume: boolean (2+ volumes)
    multi_featuring: boolean (2+ zones)
    broad_fabric: boolean (0-1 discomforts)
    broad_exposure: boolean (comfortable + 0-2 covers)
    flexible_cut_or_rise: boolean
  }
```

High: 5+ signals. Medium: 3-4. Low: 0-2.

---

## Part 11: Strategy Execution Patterns

Items are tagged with strategies they execute + execution sub-classification(s). User's execution selections filter accordingly.

### Anchor patterns

**user_created anchor items:**
- High-rise straight jeans → anchor (user_created); enables tuck meeting-point
- Cropped tops → anchor (user_created); enables high-rise meeting point

**garment_created anchor items:**
- Wrap tops, wrap dresses
- Belted shirt dress (belt integral to silhouette)
- Fitted bodice + skirt construction

**Both:**
- Items that work with either styling approach

### Sculpt patterns

- Corseted dress → sculpt (waist_sculpt)
- Princess-seamed sheath → sculpt (waist_sculpt)
- Peplum top → sculpt (lower_body_sculpt) AND anchor (garment_created) [overlap]
- Mermaid skirt → sculpt (lower_body_sculpt)
- Structured-shoulder blazer → sculpt (shoulder_sculpt)
- Tailored blazer with strong waist suppression → sculpt (waist + shoulder)

### Edge patterns

- V-neck top (deep) → edge (exposure_edge)
- Off-shoulder top → edge (exposure_edge)
- Oversized button-up + slim jeans outfit → edge (proportion_edge)

### Overlap zones

Some items execute multiple combinations. They surface for users who selected ANY matching execution:

- Wrap dress = anchor (garment_created)
- Fit-and-flare with structured bodice = anchor (garment_created) AND sculpt (waist + lower_body)
- Peplum top = sculpt (lower_body) AND anchor (garment_created)
- Belted blazer (belt integral) = anchor (garment_created) AND potentially sculpt (waist_sculpt)
- Structured-shoulder blazer with strong waist taper = sculpt (shoulder + waist)

### Application

When user selected a strategy AND execution sub-classifications:
- Items matching at least one selected execution within the strategy → surface
- Items in the strategy but only matching unselected executions → downrank
- Items in unselected strategies → evaluate by other rules (don't filter solely on strategy)

### The anchor-without-sculpt pattern

When user selects anchor + user_created only AND sculpt not selected:
- Surface: high-rise + tuck patterns, cropped + high-rise, fitted button-downs untucked, soft tailored blazers worn open, belts as styling tool
- Filter: wraps (garment_created), belted dresses (garment_created), corseted bodices (sculpt), princess-seamed sheath (sculpt), peplum tops (sculpt)

This is the meeting-point anchor archetype — body has natural waist + user wants to control when/how it shows + no garment-imposed shape construction.


---

## Part 12: Question-by-Question Mapping

### Q1: Height
| Answer | Contribution |
|---|---|
| Under 159 | height_tier = petite |
| 160-164 | height_tier = mid (lean petite) |
| 165-169 | height_tier = mid |
| 170-175 | height_tier = tall |
| 175+ | height_tier = tall |

Modifier (not constraint). Affects length defaults, jacket length thresholds, midi-vs-maxi perception.

### Q2: Body proportions (primary diagnostic)
| Answer | body_type |
|---|---|
| Shoulders, waist, hips about same width | rectangle |
| Shoulders and hips similar, smaller waist | hourglass |
| Shoulders broadest | inverted_triangle |
| Hips broadest | pear |
| Fullness around midsection | apple |

### Q3: Distribution — snug zones (variation refinement)

Diagnostic, not preference.

| Zone | Contribution |
|---|---|
| Chest | rectangle → variation.ribcage_signal may = wider; hourglass/apple → bust_signal may = fuller |
| Arms | bulk-aversion flag; not diagnostic alone |
| Shoulders | inverted_triangle confirms; apple → top_heavy_signal |
| Waist/stomach | rectangle → midsection_signal may = prone; apple confirms |
| Hips/thighs | pear confirms; hourglass → bottom_fuller |
| Seat | pear/hourglass → projected seat; rectangle → seat_signal = fuller |
| Nowhere specific | variation.frame = lean |

### Q3: Distribution — loose zones

| Zone | Contribution |
|---|---|
| Chest | pear → smaller bust; rectangle → lean frame |
| Arms | lean signal |
| Shoulders | pear → narrower shoulders |
| Waist | rectangle → lean frame (not hourglass — needs Q2) |
| Hips/thighs | inverted_triangle → narrower hips; rectangle → lean |
| Seat | rectangle → flat (typical); inverted_triangle/apple → confirms flat |

### Q3: Featuring zones (Q1 in styling framework)

Multi-select: décolletage, bust, shoulders, arms, waist, hips/curves, seat, legs, back, "nothing in particular."

Each named zone creates featuring_zones entry. Treatment derived from cross-body framework (amplify / unlock / respect over default / fall back). Mode derived from exposure + length.

"Nothing in particular" → lowers permissiveness, conservative defaults.

### Q3: Help intents (Q2 in styling framework — new)

Multi-select: longer legs, waist definition, shape around hips/seat, smooth midsection, fuller bust, less-prominent bust, softer shoulders, "nothing specific."

Each selected creates help_intents entry. Combined with featuring_zones from Q1 per the cross-body framework.

### Q4: Fit issues (variation refinement)

| Answer | Contribution |
|---|---|
| Tight in chest | rectangle → variation.ribcage_signal may = wider |
| Tight in arms | bulk-aversion flag |
| Tight in waist | rectangle → midsection_signal may = prone; apple confirms |
| Pulls across thighs | pear confirms |
| Tight around hips/seat | pear/hourglass confirms |
| Loose around hips/seat | rectangle/inverted_triangle confirms |
| Gaps at waist | hourglass/pear confirms (waist-hip differential) |
| Everything sits how it should | no specific flag |

### Q4: Length issues
| Answer | Contribution |
|---|---|
| Pants too short | tall confirms; modify length defaults |
| Pants too long | petite confirms |
| Tops too cropped | tall → need longer tops |
| Tops too long | petite → need shorter/cropped |

### Q5: Strategy + execution

**Main question:** *How do you usually like clothes to sit on your body?* (Multi-select)

| Answer | Strategy |
|---|---|
| Follow my natural shape | trace |
| Defined around a certain area | anchor |
| Create a more structured/shaped look | sculpt |
| Sit away from the body | edge |

Weighting:
- 1 strategy → high weight, others neutral
- 2 strategies → both high, others neutral
- 3+ strategies → all high + multi-strategy permissiveness signal
- 0 (fallback) → all neutral

**Execution follow-ups (only for selected strategies):**

Trace: no follow-up. Use fit + fabric to determine execution.

Anchor: *When you like shape around the waist, what feels most like you?*
- I like creating shape myself (rise, tucking, belts) → user_created
- I like when the piece creates the shape (wrap, belted dress) → garment_created
- I'm not sure → unsure

Sculpt: *Where do you like the shape to come from?*
- Defined sharper waist (corset, princess seams) → waist_sculpt
- Curve through lower body (peplum, fuller skirt) → lower_body_sculpt
- Stronger shoulder line (structured blazer) → shoulder_sculpt
- I'm not sure → unsure

Edge: *What kind of interest feels like you?*
- Showing skin (open neckline, slit, bare shoulders) → exposure_edge
- Playing with proportions → proportion_edge

### Q6: Volume preference
Subset of: mostly_top, mostly_bottom, balanced, minimal.

### Q7: Fit — tops and bottoms
Subset of: tight, close, relaxed, oversized (per top and bottom).

Cross-garment fit propagation applies (see Part 8). Tight is high-specificity — if not selected, tight items not filtered but require stronger support to rank.

Shaping gate: if user selected close but also flagged cling-averse OR selected relaxed/oversized as primary, set shaping_gate = true. Close-fit items must provide shaping support (ribbed, structured, fitted with body) to surface.

### Fabric questions
- Importance: very_important / important / low → modulates quality threshold
- Discomforts: clings, stiff, heavy, wrinkles → tag-confidence-gated (see Part 7)
- Attention to detail: high / medium / low → modulates construction-detail weighting

### Pants/jeans
- Rise: low, mid, high, flexible
- Cut avoid: subset of [straight, wide, flared, bootcut, slim, barrel] → filters
- Length avoid: subset of [full, cropped, capri] → filters

### Dresses/skirts length preferred
Subset of [short, mid, long] → non-selected deprioritized but not filtered.

### Exposure
- Overall: comfortable / depends / prefer_coverage
- Covers: subset of [arms, shoulders, back, chest, midriff, legs] → filters items revealing covered zones


---

# Part 13: Body Type Reference

Each section describes geometric truth, default assets, strategy execution patterns, and hero/disqualified categories. These are reference material applied through the strategy-frame principle (Part 2) and modulated by permissiveness (Part 6) and featuring signals (Parts 4-5).

---

## Rectangle

**TL;DR:** Balanced shoulders/waist/hips with no taper. Needs trace precision, real anchor, real sculpt, or intentional edge/proportion play. What fails: fake shape, limp anchor, clingy column, bulky box, unintentional length.

### Geometric truth
- Balanced shoulder/bust/hip widths (within 5%)
- Undefined waist (less than 25% smaller than bust)
- Flat or minimally curved seat
- Legs typically proportionally longer than torso

### Variations
- **Wider-ribcage:** fuller chest/ribcage panel. Open necklines critical; closed/high with fitted ribcage reads boxy.
- **Narrow-frame:** lean throughout. Broader styling tolerance; risk of being swallowed by oversized.
- **Fuller-bottom:** volume at seat without hip flare. Suppress seat-shaping defaults.
- **Athletic:** muscle definition. Cautious with cap sleeves and structured shoulders on already-strong upper body.
- **Midsection-prone:** soft/full midsection. Anchor moves above or below (not at) natural waist.

### Default assets
- **Long slim legs** (primary)
- **Lean arms**
- **Décolletage and collarbones**
- **Wrists and ankles** (lean extremities — useful for edge)
- **Lean back**
- **Shoulders** (carry structured tailoring beautifully)
- **Waist** (created through anchor or sculpt — engineered, not natural)
- **Vertical line** (uninterrupted shoulder-to-hip becomes elegance with right styling)

### Featuring-zone treatment
- *Legs named:* amplify (default asset)
- *Arms named:* amplify; surface sleeveless
- *Décolletage named:* amplify; resolves open-neckline relief vs. featuring
- *Shoulders named:* amplify + unlock structured-shoulder tailoring, off-shoulder, statement-shoulder
- *Waist named:* unusual but meaningful — signals waist creation prioritized; surface anchor/sculpt aggressively
- *Back named:* signature unlock — lean back works for low-back, open-back, keyhole, lace-up
- *Hips/seat named:* unusual; signals lower body featuring desired. Surface hip-emphasis cuts cautiously — shaped-pocket denim, low-rise, jeans that lift seat visibility. **Filter items designed for projected seats (curve-cut bodycon drafted for hourglass projection that reads empty on flat-seat rectangle).** Q2 "add more shape around hips/seat" produces this signal directly without requiring Q1 naming.

### Strategy execution

**Trace:** narrowest margin. Works for lean/narrow-frame where column reading is naturally muted. Fails when natural shape gets traced and amplified. Trace tops trace boxy ribcage; trace bottoms trace flat seat. Hero items: fitted polos and button-downs, slim straight-leg pants, sheath dresses (skim-fit fabric on lean rectangle), fitted ribbed knit tops at high hip, tailored shirt dresses with subtle waist shaping, slim trousers.

**Anchor:** strongest single move from boxy to shaped. Rectangle anchor must be HARD anchor (real construction or substantial belt) because no waist underneath fills in soft anchor. Hero items: wrap dresses with substantial tie + structured fabric, belted dresses with real belts, peplum tops/jackets with structured construction, fitted bodice + flared skirt dresses, princess-seamed dresses, high-rise + fitted-tucked top combinations. **Fails:** drawstring waists, self-tie on flowy fabric, thin string belts on heavy fabric.

**Sculpt:** physically creates curves where body lacks them. Quality matters more for rectangle than other body types — body doesn't have shape to fill poor construction. Hero items: corseted bodice dresses, fit-and-flare with very fitted bodice + dramatic skirt flare, princess-seamed dresses, tailored peplum jackets with strong waist shaping. **Fails:** sculpt in thin cheap fabric, sculpt that promises structure but delivers polyester drape, empire that puts waist seam too high.

**Edge:** when user doesn't want to deal with body shape, redirects attention to assets and uses proportion play. Both featuring (legs, arms, décolletage, back) and balancing (volume distribution) modes work. Hero items: short A-line dresses/skirts, slits on midi/maxi, sleeveless and short sleeves, V-necks/scoops/deep V, low-back dresses, halter, crop tops over high-rise, wide-leg + fitted tank, boxy short jacket + slim trouser, statement sleeves + slim bottom.

### Disqualified (universal)
- Drop-waist dresses (eliminates leg asset)
- Empire-line column dresses with no features
- Bulky chunky knit sweaters hanging straight with no openings (filter unless strategic openings shift to edge)
- Wide-strap tanks reading as flat panels

### Common "looks right but disappoints"
- Wrap dresses in flimsy fabric (wrap doesn't do real cinching)
- "Belted" oversized dresses in unstructured fabric (reads as cinched bag)
- Fast-fashion sculpt (structure collapses on body)
- "Universal flattering" trapeze dresses (boxy under boxy)

### Petite rectangle (height_tier = petite)
- Short jackets ending at waist
- Cautious with midi unless slit or break
- Long heavy outerwear filters
- Oversized + petite = highest-restriction; structured oversized only

### Tall rectangle (height_tier = tall)
- Standard cuts often run short
- Long open dusters work particularly well
- Cropped items read as standard-length

---

## Inverted Triangle

**TL;DR:** Shoulders broadest, narrower hips, no defined waist. Four strategies available. Anchor most powerful (creates waist + adds lower-body volume). Edge bypasses proportion question. Sculpt builds shape. Trace works for narrow-frame variations. Lean lower body is strongest natural asset.

### Geometric truth
- Shoulders broadest part of body, distinctly wider than hips
- Bust often fuller (contributes to upper-body dominance)
- Ribcage may also be wider than lower half
- Undefined waist
- Narrow hips relative to shoulders
- Flat or minimally curved seat
- Legs lean and proportionally longer than torso

### Variations
- **Athletic:** muscle development in shoulders/arms. Carries structured tailoring beautifully but cap sleeves and structured shoulders amplify what's there.
- **Bust-forward:** broad shoulders + full bust. Upper body dominance from both width and depth.
- **Narrow-frame (including tall-lean):** lean throughout, shoulders only meaningfully wider point. Most styling tolerance. Tall-lean subset operates with significantly broader tolerance — V-taper reads as body signature.
- **Hip-fuller:** shoulders still broadest but lower body isn't as narrow. "Add hip volume" defaults soften.

### Default assets
- **Long slim legs** (most reliable)
- **Narrow waist** (relative to shoulders — waist-marking creates dramatic visual narrowing)
- **Décolletage and collarbones**
- **Strong shoulders** (asset when user wants the look; risk to balance when she doesn't)
- **Lean lower body**
- **Lean ankles**

### Featuring-zone treatment
- *Legs named:* amplify (strongest asset)
- *Bust named (any size):* significant unlock — directly resolves bust-as-asset signal. Surface sweetheart, deeper V, surplice at exposure-appropriate depth.
- *Shoulders named:* significant — user wants to feature natural shoulder line. Reduce default shoulder-minimizing; unlock shoulder-featuring access. Default surfaced execution is body-compatible (one-shoulder asymmetric, halter, clean sleeveless, sharp controlled tailoring, narrow-strap tops). Heavy puff sleeves, dramatic shoulder pads, stiff boat necks remain filtered unless edgy/dramatic style + reveal mode signaled.
- *Décolletage named:* amplify; surface open V, scoop, asymmetric
- *Arms named:* surface sleeveless, short sleeves
- *Waist named:* confirms anchor direction; surface anchor aggressively
- *Back named:* unlock as alternate focal point (redirects from front-facing shoulder breadth)
- *Hips/seat named:* unusual; signals lower body featuring; surface hip-emphasis cautiously

### Strategy execution

**Trace:** the riskiest strategy. Honors body's shape — but inverted triangle's natural shape is exactly the proportion problem most users want to balance. Trace-only signals narrow-frame, athletic she's proud of, or limited strategy understanding. Hero items (when trace works): open V-neck/scoop tops, button-downs worn open, mid-to-high rise straight or wide-leg pants, fitted A-line or full skirts, wrap tops that follow body but cinch waist, soft drape blouses, trousers with subtle hip detail.

**Anchor:** strongest strategy. Creates defined waist that breaks the column AND adds visual volume below. Both hard and soft anchor work — waist is narrow enough that even soft mechanisms can pull in and create definition. Hero items: A-line skirts and dresses, wrap dresses, skater dresses, fit-and-flare dresses, belted shirt dresses with full skirt, high-rise wide-leg or flare pants, peplum tops, drawstring/wrap tops over fitted bottoms. **Fails:** cropped peplum at rib, belts at empire line, drop-waist, wide belts shortening petite torso.

**Sculpt:** creates artificial waist and lower-body shape. Hero items: fit-and-flare with structured bodice + full skirt, sculpt midis with A-line or fishtail skirts, tailored peplum jackets at natural waist, princess-seamed dresses. **Fails:** sculpt with structured shoulders or shoulder pads (unless shoulders named), sculpt fitting close all the way down with no skirt volume, sculpt in heavy fabric that doesn't drape at shoulders.

**Edge:** bypasses proportion problem by redirecting attention. Featuring modes: legs (most accessible default), bust (when user opts in via featuring-zone), décolletage, open back (redirect from front-facing shoulders), ankle. Attention-redirect: color blocking dark-on-top/light-on-bottom, statement bottoms with plain tops, print/detail below waist. **Fails:** statement tops with plain bottoms, bold prints/bright colors on top alone, embellishments at neckline/shoulders/bust (unless those zones named), light colors on top with dark on bottom.

### Disqualified (default — overridden when relevant zone named)
- Structured shoulder pads (override: shoulders named)
- Puff sleeves and dramatic sleeve volume (override: shoulders named)
- Padded/push-up bust
- Off-shoulder, bateau, Sabrina necklines (override: shoulders named)
- Boat necks (override: shoulders named)
- Wide square necklines on tops (override: shoulders named)
- Tight column dresses
- Bold prints on tops without compensation
- Drop-waist
- Empire-line tops/dresses
- Bandeau/strapless as default
- Mermaid skirts tight to knee then flaring

### Common "looks right but disappoints"
- Crew-neck T-shirts (closed neckline + fitted ribcage on broad upper body reads boxy)
- Boxy crewneck sweaters (closed neck + shoulder breadth amplified)
- Pencil skirts in stretchy fabric (tight skirt on narrow hips emphasizes proportion mismatch)
- Tank tops with wide straps or wide armholes (extend shoulder line)


---

## Hourglass

**TL;DR:** Defined waist with balanced bust and hips. Anchor and trace both strong because body has its own structure. Job is to honor curves, not fight them or amplify artificially. Bust depth and hip emphasis depend heavily on featuring-zone signal.

### Geometric truth
- Bust and hips approximately equal width (within 5%)
- Waist significantly narrower (25%+) than bust and hips
- Defined taper at natural waist
- Seat typically projected (not flat)
- Shoulders typically aligned with hips

### Variations
- **Lean:** smaller curves but proportion holds. Most styling tolerance.
- **Soft/fleshy:** fuller curves, sometimes soft midsection. Stretch and curvy-fit critical.
- **Full-bust:** bust significantly fuller. Bra fit and bust support critical.
- **Athletic:** muscular curves rather than soft. Holds shape without fabric assistance.
- **Top hourglass:** bust slightly fuller than hips. Leans inverted triangle on top.
- **Bottom hourglass:** hips slightly fuller than bust. Leans pear on bottom.
- **Midsection-prone:** defined waist but softer midsection (post-pregnancy, post-menopause). Sculpt valuable.
- **Petite:** same proportions at smaller scale. Standard items often run long.

### Default assets
- **Defined waist** (central asset)
- **Curves at bust and hips**
- **Décolletage and collarbones**
- **Projected seat** (asset when user wants lower-body emphasis)
- **Proportional shoulders**

### Featuring-zone treatment
- *Waist named:* amplify (default asset). Q2 "create more waist definition" reinforces.
- *Bust named:* resolves depth ambiguity directly. Surface bust-featuring at exposure-appropriate depth (reveal/sophisticated/coverage).
- *Hips named:* unlocks hip emphasis (low-rise, bodycon, pencil following curve, hip-detail). Celebrate mode for lower body.
- *Seat named:* unlocks seat-featuring (fitted bottoms, bodycon, jeans with back-pocket detail).
- *Legs named:* unlock leg-featuring.
- *Décolletage named:* amplify; open V, scoop, sweetheart at appropriate depth.
- *Shoulders named:* unusual; surface structured-shoulder pieces despite hourglass default of soft shoulders.

### Mode signal (honor vs. celebrate)

Central modulator. Detection:
- **Honor mode** (default): items honor curves through skim-fit; bodycon and low-rise deprioritized
- **Celebrate mode:** body follows curves; bodycon, low-rise, hip-detail items become hero

Mode detection: featuring-zone (hips/seat named = celebrate signal), exposure preferences, fit preferences (close everywhere = celebrate), behavior data.

### Strategy execution

**Trace:** most natural strategy. Honors defined curves directly. Strongest silhouette read with minimal styling intervention. Curvy-fit availability is biggest factor for trace success. Hero items: fitted dresses in skim-fit fabric, sheath dresses cut curvy, fitted button-downs in stretch/curvy fit, wrap dresses following body, bodycon (celebrate mode), fitted knit tops tucked in, curvy-fit jeans, pencil skirts following hip.

**Anchor:** universal hero. Body has real waist; almost any anchor mechanism succeeds. Particularly valuable for relaxed-fit hourglass — preserves waist visibility despite loose fabric. Hero items: wrap dresses, belted dresses, belted shirt dresses, tucked-in tops at natural waist, high-rise + fitted-tucked top, wrap tops, dresses with built-in waist seams, statement belts over relaxed tops, fit-and-flare. **Fails:** drop-waist, empire (eliminates taper), hip belts, cinches at wrong position.

**Sculpt:** less critical than for rectangle — body has shape already. Valuable when honoring isn't enough (formal occasions, structured looks, midsection-prone). Sculpt should follow existing curves rather than impose new shape. Hero items: fit-and-flare with structured bodice + full skirt, tailored sheath with princess seams, corseted bodice with skirt (evening), structured fit-and-flare coats, peplum jackets at natural waist. **Peplum is sculpt for hourglass** (creates shape that emphasizes existing waist), not anchor.

**Edge:** typically features natural assets — waist, bust, décolletage, curves. Less about redirecting from problems, more about choosing which asset to feature. Hero items: statement belts over wrap dresses, V-neck + tucked fitted top + belt, sweetheart bodice (when bust named), bodycon with statement neckline (celebrate mode), pencil skirt + fitted top + belt (celebrate mode).

### Disqualified
- Shapeless tunic tops hanging shoulder to mid-thigh
- Drop-waist dresses
- Empire-waist tops/dresses (unless slim/lean variation + bust featured)
- Boxy oversized blazers without belt or waist shaping
- Straight-cut column dresses
- Standard-cut bottoms with significant waist gap

### Common "looks right but disappoints"
- Wrap dresses in thin clingy fabric (wrap is right but fabric clings without supporting)
- Pencil skirts in stretchy thin fabric (shows contour without elevating silhouette)
- Standard-cut sheath dresses (waist gaps when bust and hips fit)

---

## Pear

**TL;DR:** Hips/thighs/seat fuller with narrower upper body and defined waist. Balance mode (minimize lower) vs. celebrate mode (feature lower) split is strongest of any body type. Upper-body skin reveal is a signature pear strength — upper body is the lean, proportional zone.

### Geometric truth
- Hips and thighs widest part of body
- Shoulders narrower than hips (sometimes 5-15%+)
- Bust typically smaller (B cup or smaller common)
- Defined waist noticeably narrower than hips
- Seat with projection and shape
- Full thighs, often touching at top

### Variations
- **Lean pear:** smaller overall frame, hips still wider. More styling tolerance.
- **Soft/fleshy:** fuller hips/thighs/seat with soft musculature. Stretch and curvy-fit critical.
- **Athletic:** muscular thighs and seat. Same proportions as fleshy, firmer feel.
- **Spoon pear:** sharp horizontal shelf at hip line. Careful with mid-rise (sits on shelf).
- **Petite pear:** same proportions at smaller scale. Hip volume reads as visually large relative to body length.
- **Pear + larger bust:** less common but real. Apply hourglass-bust rules; pear lower-body rules still apply.

### Default assets
- **Defined waist** (central asset alongside lower-body shape)
- **Upper body proportions** (shoulders, arms, bust — often delicate)
- **Décolletage and collarbones**
- **Lean upper back** (often overlooked)
- **Curves** (when celebrated — opt-in)
- **Smaller bust** (allows high necklines, button-downs, structured tops without pulling)

### Upper-body skin reveal as signature play

Pear has unusually clear upper-body featuring potential. The upper body is pear's leanest, most proportional zone. Unlike other body types with constraints on upper-body reveal (hourglass cleavage management, inverted triangle shoulder amplification, apple midsection sensitivity), pear has no inherent constraint beyond user preference. Off-shoulder, low-back, chest cutouts, halter, crop tops feature lean assets without creating proportion problems.

### Featuring-zone treatment
- *Hips/seat named:* shifts toward celebrate mode. Surface hip-emphasis cuts, low-rise, bodycon, prominent back pockets, bright bottoms. Filter clingy cheap fabric that distorts curve.
- *Legs named:* unlock leg-featuring (fitted bottoms showing line, short hems, slits).
- *Waist named:* confirms anchor direction (already default).
- *Shoulders named:* unlock off-shoulder, halter, one-shoulder, structured shoulders.
- *Back named:* signature pear unlock — lean upper back works exceptionally for low-back, open-back, keyhole, lace-up.
- *Décolletage named:* surface open necklines.
- *Bust named:* if fuller bust, surface featuring at appropriate depth.
- *Midriff named (less common):* surface crop tops for confident dressers.

### Mode signal (balance vs. celebrate)

Central modulator. Detection:
- **Balance mode default:** user names upper-body zones only, doesn't name lower-body zones, reports hips/thighs/seat as snug fit issues
- **Celebrate mode opt-in:** user names hips/seat/legs as featuring zones, opts for high lower-body exposure, behavior shows preference for hip-emphasis cuts

### Strategy execution

**Trace:** works for pear with correct fit — curvy-fit cuts accommodating waist-to-hip ratio. Standard cuts often fail. Curvy-fit availability is biggest factor for trace success. Hero items: fitted tops in soft fabric or stretch, wrap and surplice tops, fitted button-downs in stretch, tucked-in fitted knit tops, curvy-fit jeans (universal pear need), high-rise straight or slim jeans fitting waist and skimming hip, tapered trousers with hip ease and waist fit, A-line skirts (trace at waist, A-line below as light sculpt).

**Anchor:** universally useful. Waist is asset; emphasizing via tucking, belting, wrap, or fitted bodice all work. Both hard and soft anchor work — waist exists. Hero items: wrap dresses and wrap tops, belted dresses, belted shirt dresses, belted blazers and coats, tucked-in tops (full or half tuck), high-rise bottoms (creates implicit anchor), cropped tops at natural waist, statement belts.

**Sculpt:** mode-dependent more than for any other body type. *Balance mode:* sculpt on upper body — structured shoulders, peplum tops with structured shoulders, statement-shoulder blazers. *Celebrate mode:* sculpt amplifying lower body — corseted bodice + dramatic full skirt, fit-and-flare exaggerating hip flare, mermaid skirts.

**Edge:** uniquely strong upper-body featuring vocabulary. Featuring modes (balance — upper body):

*Upper-body skin reveal (signature):*
- Shoulder reveal: off-shoulder/Bardot (universally flattering), one-shoulder, cold-shoulder, halter
- Chest reveal: keyhole, drop-front, geometric cutouts, deeply open button-ups, square neck (wide shallow), sweetheart/strapless for smaller-bust
- Back reveal: low-back dresses/tops, open back, scoop back, low V back, lace-up back, halter with bare back. Most distinctive pear category.
- Waist reveal: crop tops

*Upper-body emphasis without reveal:* statement sleeves (puff, bishop, bell, flutter), bold print/color on top with simple bottoms, embellished bodice, decorative collars, boat neck without bare shoulder, statement earrings.

Featuring modes (celebrate — lower body): hip features (cuts, low-rise, contoured waistbands), seat features (fitted pants/skirts following projection, bodycon), thigh features (slits, side cutouts, fitted in dramatic fabric), leg features (fitted bootcut/flared, cropped with ankle reveal, slim trousers, monochromatic leg-extending), bottom prints and color.

### Disqualified
- Hip-length jackets ending at widest point
- Shapeless tunics shoulder-to-mid-thigh
- Drop-waist dresses
- Empire-waist (unless explicit user preference)
- Stiff fabrics in bottoms that don't drape
- Mom jeans with very loose hip (waist gap problem)
- Heavy front-pleat trousers with hip detail

**Mode-disqualified:**
- *Balance mode:* bodycon, tight pencil skirts (unless very confident), low-rise, bright bottoms, hip-detail items, statement bottoms
- *Celebrate mode:* voluminous upper-body hiding bust/shoulder, heavy structured shoulder pads, tops with very loose hem hiding waist

### Common "looks right but disappoints"
- Wrap dresses in clingy fabric (cling to hip and emphasize what should skim)
- A-line skirts in stiff fabric (stiffness stands away creating bulk)
- Peplum tops on hip-prone pears (flare hits at hip-widest, doubles volume)
- Mid-rise bootcut on spoon pear (sits on hip shelf)


---

## Apple (Oval)

**TL;DR:** Widest point at midsection with narrower shoulders and hips. Job is to skim (not cling) midsection, feature alternative zones (legs typically strongest, décolletage reliable), use vertical lines to slim torso. Anchor at natural waist almost always fails — anchor moves above (empire, gated by tummy) or below (high hip, low anchor).

### Geometric truth
- Midsection (stomach, ribcage, sometimes back) is widest part
- Shoulders and hips typically narrower than midsection
- Bust often fuller (C+ common, not universal)
- Waist undefined or fuller than bust/hips
- Seat typically flat or minimally projected
- Legs typically lean and proportionally slim (often strongest asset)

### Variations
- **Slim/lean:** lower weight overall, midsection still widest. Less stomach to manage; broader tolerance.
- **Soft/fleshy:** fuller throughout upper-mid body, stomach more prominent.
- **Top-heavy (leans inverted triangle):** shoulders also broader. Inverted triangle softening on top + apple midsection management.
- **Full-bust:** most common variation. Bra fit and support critical.
- **Lean lower body:** the typical apple — flat seat, narrow hips, lean thighs and legs.
- **Post-pregnancy/post-menopause:** developed from previous body type. Classify by current geometry.
- **Petite/Tall:** scale modulators apply.

### Default assets
- **Legs** (universal apple asset — single strongest)
- **Ankles** (slim — cropped pants, slim heels work)
- **Calves** (typically lean)
- **Décolletage and collarbones** (sits above midsection)
- **Bust** (often fuller, becomes asset with support and appropriate necklines)
- **Shoulders** (proportional or narrower than midsection)
- **Face and neck** (with right neckline, becomes focal point)

### Featuring-zone treatment
- *Legs named:* amplify aggressively (universal apple asset)
- *Décolletage named:* amplify; resolves open-neckline depth question
- *Bust named:* unlocks bust-featuring at exposure-appropriate depth (critical for full-bust apple)
- *Shoulders named:* surface structured shoulder pieces (caution for top-heavy variation)
- *Arms named:* surface sleeveless when comfortable
- *Face/collarbone named:* surface open necklines, statement jewelry, items pulling attention up
- *Midsection named:* rare confident-feature signal. Q2 "smooth around waist/stomach" is the much more common Q2 signal — produces management mode (vertical line, tunic length, long open layers, fluid drape; suppress natural-waist anchors)
- *Hips/seat named:* very unusual for apple (typically flat); surface hip-emphasis cautiously

### Strategy execution

**Trace:** riskiest strategy. Honors body's natural shape — but that shape is exactly the proportion problem most users want to manage. Trace tops trace midsection; trace bottoms trace lean legs (fine). Trace-only signals very slim apple, confident dresser, or doesn't realize what trace will do. Works on lower body (legs lean) but fails on upper body/midsection. Half-trace (fitted legs + skim-fit torso) is essentially the apple uniform.

**Anchor:** trickiest of all body types. Body has no natural waist; anchoring at natural waist is the worst failure (line at widest point). Apple anchor means anchoring above or below — empire (under bust) or low-anchor (high hip). Hero items: empire-waist tops/dresses (gated by tummy presence), tunic tops ending below midsection, long open dusters/cardigans creating vertical line + low break, tops with vertical seam detail, half-tucked tops where tuck point is below natural waist, layered looks. **Fails:** belts at natural waist (almost universal), wide belts at natural waist (severe), drawstring at natural waist, built-in waist seams at natural waist, tucked-in tops with full tuck at natural waist, cropped tops at natural waist, drop-waist hitting at lower stomach.

**Sculpt:** potentially useful but rarely heroic. Structured construction can impose smoother silhouette through midsection. Sculpt that imposes defined waist where there isn't one fails. Most useful: structural support that compresses or smooths without creating fake waist. Hero items: tailored blazers with structured shoulders + skim-fit through torso, fit-and-flare where fit is at bust line (empire) and flare bypasses midsection, structured sheath that smooths midsection, princess seams running vertically through torso. **Fails:** sculpt with natural-waist seam, sculpt with heavy structured shoulders creating barrel silhouette, bodycon sculpt following midsection, corseted bodice ending at natural waist, empire sculpt on full-tummy apple.

**Edge:** strongest and most useful strategy. Redirects attention away from midsection by featuring alternatives — legs, décolletage, face, ankles, shoulders. Apple has unusually clear featuring potential because natural assets are pronounced relative to midsection.

*Legs as primary feature (almost universal):* knee-length and shorter A-line skirts/dresses, slim trousers showing leg line, cropped pants with ankle reveal, slim pencil skirts with appropriate top coverage, heels and pointed shoes elongating.

*Décolletage as feature:* open V-necks (especially deep V), scoop necks, sweetheart (for full-bust with support), open button-downs, statement necklaces above bust.

*Face and upper body:* statement earrings, bold lipstick, hair framing face, open necklines drawing eye to face, hats and headwear pulling focus up.

*Vertical line as feature:* monochromatic outfits, long open jackets and dusters, long necklaces, vertical seam detail, color blocking with darker midsection panel.

### Disqualified
- Tight bodycon dresses
- Fitted ribbed knits across midsection
- Tucked-in fitted tops at natural waist (full tuck)
- Cropped tops at natural waist
- Wide belts at natural waist
- Heavy chunky belts at natural waist
- Drop-waist dresses
- Empire-waist for full-tummy apple
- Pleated front trousers with heavy waist pleating
- Tiered/ruffled skirts gathered at natural waist
- Halter pulling attention to bust without vertical break
- Bandeau/strapless without compensating coverage
- Tube dresses
- Wrap dresses tying tightly at natural waist
- Bodycon midi dresses

### Common "looks right but disappoints"
- Wrap dresses on apple (wrap tie often hits at natural waist — widest point — and emphasizes width)
- Empire-waist on full-tummy apple (empire seam emphasizes midsection directly below)
- Boxy tunics (hide body but read shapeless/lumpy)
- Bodycon with shapewear (still reveals every contour)
- Belted blazers (belt at natural waist creates failure — surface unbelted worn open)
- "Universal" maxi dresses (those gathering at natural waist fail — surface column maxis with empire bodice)


---

## Part 14: Combination Resolutions

### Strategy ranking from secondary signals

When user selects multiple strategies, rank rather than treat as equally weighted:

**Primary anchor signals:** user-stated "primary" qualifier, waist named, high-rise preference, fitted bottom + tucked top in stated outfits.

**Primary trace signals:** close fit for tops AND bottoms, high fabric importance + cling-averse, fitted/skim-fit in stated outfits, body type variation is lean.

**Primary sculpt signals:** high attention to detail, high fabric importance, featuring zones benefiting from sculpt (rectangle waist, apple midsection), structured architectural pieces in stated outfits.

**Primary edge signals:** volume preferences mostly_bottom or mostly_top (proportion play), multiple featuring zones named (multi-asset redirection), layered/proportion-play outfits stated.

When secondary signals strongly point to one strategy, weight that strategy as primary even if user multi-selected.

### Multi-strategy + permissiveness interaction

- **Multi-strategy + multi-fit + multi-zone + broad signals:** high permissiveness, wide catalog, all strategies surface, behavior refines ranking
- **Multi-strategy + narrow fit + few zones + restrictive signals:** medium permissiveness, narrower catalog, strategies surface within fit constraints
- **Single strategy + narrow fit + few zones + restrictive signals:** low-medium permissiveness, hero-weighted catalog, surfacing precision matters
- **Single strategy + broad signals elsewhere:** medium permissiveness, strategy clear but user otherwise flexible

### Featuring zone reveal mode resolution

When a zone is named, mode is derived from:
- Exposure preferences for that zone
- Length preferences when relevant
- Q2 help intents (when zone has corresponding Q2 option)
- Other consistent signals

Conflict patterns:
- Zone named + covered in exposure → coverage mode (feature through fit/color/structure, no skin)
- Zone named + available in exposure + deep/short length preference → reveal mode
- Zone named + available + moderate/sophisticated length → sophisticated mode (default when ambiguous)
- Zone named + bust signal fuller + chest available → moderate-depth necklines; don't push to plunging without explicit signal

---

## Part 15: Item Tagging

Items are tagged with attributes that the matching engine uses. Key tag dimensions:

- **product_type, silhouette, length** (objective)
- **bottom_rise** for bottoms
- **color_family, color_density, pattern**
- **primary_fabric, fabric_quality, fabric_behavior, fabric_risks**
- **strategy** (which strategy/strategies the item executes — single or multi-valued)
- **edge_break** (closing details that contribute to strategy execution — V-neck, wrap, slit, etc.)
- **closeness_to_body_top, closeness_to_body_bottom**
- **volume**
- **body_visibility_demand**
- **featuring_zones** (which body zones the item engages)
- **exposure_level, exposure_location**
- **styling_flexibility** (open/closed — how many ways item can be worn)
- **body_type_best, body_type_ok, body_type_risky** (geometric compatibility — represents default mode)
- **body_modulators** (which body variations the item actively serves)
- **fit_failures_addressed** (e.g., has_stretch, long_inseam, forgiving_midsection)
- **scale** (height tiers the item works for)
- **core_style, adjacent_style** (style world membership)
- **item_role** (hero, bridge — within style worlds)
- **context** (everyday, work, weekend, vacation, mom_duty, formal, evening, active_leisure)

### Tagging conventions

**Tag intrinsic character, not styling.** Item is tagged based on its own silhouette/fabric/cut, not how it's styled in product photos.

**has_stretch threshold:** 2%+ elastane. Below = recovery only, not user-experienced stretch.

**midsection_friendly requires coverage + give.** Rigid + close-fit doesn't qualify even if high-rise.

**Foundational items live in 1-2 cores max.** Classic items get tight adjacencies, not sprawled.

**Color doesn't shift core_style.** Only affects adjacency strength and context.

**fabric_quality convention:** Items below "acceptable" get flagged for removal. acceptable/high are the only valid tags.

**Crop hem behavior:** crop_hem in edge_break removes neutral from strategy (item pre-tucked by design).

**styling_flexibility:** co-ord sets ALWAYS open (pieces work with other wardrobe items). Single garments closed unless convertible (button-down open/closed, wrap configurations).

**Slim/cigarette cut:** Cannot be neutral strategy (commits to silhouette statement). Only trace + styling_anchor.

**Body modulators standard:** "Actively serves" not "doesn't penalize."
- short_torso_friendly: close fit + waist length OR cropped (NOT relaxed hip-length, NOT skirts/bottoms)
- full_arm_friendly: wide/drapey/oversized sleeve (NOT standard short sleeve)
- midsection_friendly: coverage + give
- curvy_lower_body_friendly: wide/A-line/relaxed (NOT close/slim)

**5-value scale buckets:**
- petite_friendly: under 159cm
- mid_short_friendly: 160-164cm
- mid_tall_friendly: 165-169cm
- tall_friendly: 170-175cm
- tall_required: 175cm+ proportion-locked

**Co-ord set tagging:** multi-tag product_type (co-ord-sets + both garment types) and silhouette (both pieces' values). length_(non_pants) = dominant top piece's length. Skip pants silhouette if no value adds signal.

### Body type tagging at item level

Body type tags describe geometric compatibility **at default mode** (since we have to pick a default for users who haven't given clear mode signals). The matching engine modulates by mode signals at the synthesis layer.

- **best:** item's geometric character actively serves this body type's defaults
- **ok:** item works for this body type but isn't optimized
- **risky:** item's geometric character works against this body type's default mode preferences

A slim/cigarette jean tagged risky for triangle (pear) represents default balance mode. The synthesis layer reads Q2 "add more shape around hips/seat" + close fit_bottom + short length preference and resolves to celebrate mode, which surfaces the item despite the risky tag.

### Tagging gaps for v3

Three potential tag dimensions identified but deferred to v3 unless behavior data shows precision is needed:

1. **seat_shaping** — items engineering lower-body shape (back-pocket placement that lifts, contoured waistband, shaped construction). Distinct from "close fit at hip."

2. **midsection_smoothing** — items engineered for active midsection management (control panels, structured smoothing fabric, shapewear integration). Distinct from "skims midsection through cut."

3. **bust_volume_adding** vs **bust_minimizing** — direction of bust engagement. Distinct from "bust featuring" which doesn't specify direction.

Existing tag combinations (closeness, strategy, edge_break, featuring_zones, fabric_behavior) carry most signal for launch. Behavior data tells you whether the precision matters.

---

## Part 16: Worked Examples Summary

The synthesis layer was validated against three worked examples (Moran, Lital — others in development). Key patterns confirmed:

### Moran (tall rectangle, high permissiveness, multi-strategy)
- 4 strategies, 6 fit options, 2 zones named, 3 fabric discomforts, 2 covers
- High permissiveness despite discomforts and covers (5 of 7 signals fire)
- Wide catalog, standard hero weighting, high behavior data sensitivity
- All four strategies' hero patterns surface; items execute whichever they fit
- Strategy-frame principle prevents over-filtering (tunic dress that would fail anchor surfaces as edge hero)
- Confidence levels on variation prevent over-modulation (low-confidence wider-ribcage and midsection-prone apply as soft preferences)
- Style archetype gap identified — fringed cardigan rules-passes on body but reads as different style register

### Lital (petite hourglass, low-medium permissiveness, anchor-primary with casual-classic style)
- Anchor + trace, anchor stated as primary, fit relaxed only
- 3 discomforts mitigated by low fabric importance
- Restrictiveness narrow-to-moderate, hero-weighted
- Cross-garment fit propagation critical — relaxed-only fit_top filters all fitted-bodice dresses, wraps, sheaths
- Anchor through styling vs. construction split — body has natural waist; styling reveals it through high-rise + tuck patterns; construction-anchor (wraps, belted dresses, fitted bodices) filtered by fit propagation
- Atypical strategy + body combination (hourglass + anchor-primary + relaxed) resolves through anchor-through-styling

### Patterns surfaced
1. **Cross-garment fit propagation** — fit_top applies to all torso-engaging garments
2. **Anchor through styling vs. construction** — natural waist body types have two anchor mechanisms; cross-garment fit determines which surfaces
3. **Strategy ranking from secondary signals** — multi-strategy users need primary detection
4. **Featuring zone mode resolution** — combination of zone + exposure + length + Q2 signals
5. **Trace + relaxed conflict** — resolves through fabric behavior (drape that follows body) not fit closeness
6. **Restrictive profile produces narrower hero-weighted catalog** — same body type rules, different application strictness

### Known gaps
1. **Style archetype not captured** in questionnaire — highest-priority next addition
2. **Curvy-bottom cut tagging** — "pulls at front of pants" needs item tagging for cuts accommodating fuller thigh/front rise
3. **Petite scale on outerwear** — "oversized" works for tall scale; "relaxed in petite scale" works for petite

---

## Reference: The Full Operating Sequence

When a user completes the questionnaire:

1. **Resolve body identification** — body_type from Q2; variation from Q3 snug/loose zones + Q4 fit issues, with confidence levels.
2. **Resolve strategy weighting** — strategies from Q5; execution sub-classifications from follow-ups; primary strategy from secondary signals when multiple selected.
3. **Resolve featuring** — featuring_zones from Q1 (asset signal); help_intents from Q2 (enhancement/management signal); combine per cross-body framework treatments.
4. **Resolve modes per zone** — for each named zone, derive mode (reveal/sophisticated/coverage) from featuring + exposure + length + behavior data.
5. **Resolve fit policy** — fit_top + fit_bottom selections; apply cross-garment propagation; set shaping_gate where applicable.
6. **Resolve fabric policy** — importance, discomforts (tag-confidence-gated), attention to detail.
7. **Resolve length, cut, exposure** — preferences and avoids.
8. **Compute permissiveness** — count signals (multi-strategy, multi-fit, multi-volume, multi-featuring, broad-fabric, broad-exposure, flexible-cut-or-rise).
9. **Compute restrictiveness output** — catalog width, hero weighting, behavior data sensitivity.

For each item in catalog:

1. **Apply true hard filters** — user-explicit avoids/covers, high-confidence fabric discomforts.
2. **Apply body-type structural filters** — verify item doesn't have compensating features that shift strategy frame.
3. **Apply strategy-frame filters** — only when item executes that strategy.
4. **Apply permissiveness-modulated filters** — filter for restrictive, surface for permissive.
5. **Score remaining items** against user's strategy weights, featuring zones (Q1 + Q2), modes, fit preferences, fabric tolerance, style archetype.
6. **Rank and surface** — hero-weighted for restrictive users, ranking-based for permissive users; behavior data refines over time.

