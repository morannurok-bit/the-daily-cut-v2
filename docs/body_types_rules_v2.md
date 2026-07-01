# Body Types Rules

## Cross-Body Framework: Featuring Zones and Reveal Modes

This framework applies across all body types and resolves several ambiguities that the original body-type rules tried to handle through inference. Read this first; each body type references it rather than restating.

### Strategy selection determines which rules apply

This is the most foundational principle of the recommendation system. It precedes everything else in this document.

Each body type document describes how four strategies — trace, anchor, sculpt, edge — succeed and fail on the body. Each strategy has its own success criteria and its own failure modes. The strategies are parallel options, not a hierarchy with one default and others as backups.

**The user's strategy selection determines which sections of the body type rules apply to her profile.** Rules for strategies the user did not select do not apply.

A user who selected edge is not subject to anchor-failure rules. A user who selected trace is not subject to edge-redirect requirements. A user who selected sculpt is not subject to trace fit-precision rules. The body type document describes how each strategy works on the body; the user's strategy selection tells us which strategies are in play.

Implications:

- *Rectangle + edge + relaxed fit + no waist construction in item:* not a failure. Edge doesn't require waist construction. Edge succeeds through strategic features that redirect attention to specific zones. An item with multiple strategic features (V-neck, slits, wrist openings) executes edge well; the absence of anchor mechanism is the absence of a strategy not in play, not a failure of the strategy that is in play.
- *Hourglass + edge + relaxed fit + no anchor:* not a failure. The body has natural waist; honoring it or redirecting from it are both valid. Edge says "don't make the silhouette the visual story; feature these zones instead."
- *Apple + edge + multiple alternative-zone features:* not a failure. The midsection-management rules apply when anchor or trace is the strategy. Edge bypasses midsection entirely by directing attention to legs, décolletage, face, ankles.
- *Pear + edge + balance mode + upper body featuring:* not a failure. Edge through upper-body features (V-neck, statement sleeve, low back) executes balance mode without requiring hip-skimming anchor construction.

The implication for item evaluation: when scoring an item, the system identifies which strategies the item executes (a wrap dress executes anchor; a tunic with strategic openings executes edge; a fit-and-flare dress executes sculpt; a fitted ribbed knit executes trace). The item is then evaluated against the success criteria of those strategies — not against the success criteria of all four strategies.

An item executing edge is evaluated against edge criteria. If it succeeds at edge (multiple features, asset-aligned redirects, proportion play), it's a hero — even if it doesn't satisfy anchor criteria, because anchor is not the strategy in play. If it fails at edge (single feature with no compensation, features that don't align with named assets, proportion play that fights the body), it's filtered.

### What filters items and what doesn't

Following from the strategy-frame principle, the rules that filter items break into three categories:

**Universal hard filters — items that fail regardless of strategy, profile, or user signals:**

- Items explicitly avoided by the user (Q3 cut avoids, Q3 length avoids)
- Items in zones the user covers (Q4 exposure covers)
- Items in fabrics flagged as discomforts (Q2 fabric discomforts)
- Structural failures specific to the body type (drop-waist on rectangle eliminates the leg asset entirely; bodycon on apple at default cover-mode for midsection; etc.)

These filter for everyone with that body type regardless of permissiveness or strategy.

**Strategy-frame filters — items that fail within a specific strategy frame:**

- Soft anchor (drawstring, self-tie) on rectangle — fails when anchor is the strategy; doesn't apply when edge is the strategy
- Trace items in cheap fabric — fails when trace is the strategy; doesn't apply when edge or sculpt is the strategy
- Sculpt items with poor construction — fails when sculpt is the strategy
- Single-feature edge with no compensation — fails when edge is the strategy

These filter when the strategy is in play and don't apply when it isn't.

**Permissiveness-modulated filters — items that filter for restrictive profiles and surface for permissive profiles:**

- Items requiring sophisticated styling execution
- Items at the edge of body type tolerance
- Items that work but require careful pairing

A permissive user (multi-strategy, multi-fit, broad fabric tolerance, multiple featuring zones) gets these surfaced because she signals styling competence. A restrictive user (single strategy, narrow fit, restrictive fabric, few featuring zones) gets these filtered because she signals she needs help.

### Profile permissiveness calibrates rule strictness

A user who signals high styling flexibility — multi-strategy, multi-fit, multi-volume, multiple featuring zones, broad fabric tolerance, broad exposure — is telling the system: "I know how to use clothes. Most things work for me if they're not actively broken. Only flag the genuine failures."

A user who signals narrow styling space — single strategy, one fit register, single volume preference, few or no featuring zones, multiple fabric discomforts, restrictive exposure — is telling the system: "I need help. I'm working in a tight space. Surface only what definitely works."

Same body type, opposite catalog widths. The body type rules don't change; their application strictness does.

**High permissiveness signals:**

- 3-4 strategies selected
- 3-4 fit options selected across top + bottom
- Multiple volume preferences
- Multiple featuring zones named
- Few or no fabric discomforts flagged
- Broad exposure with few specific covers
- "Flexible" or "no preference" on rise, cut, length

**Low permissiveness signals:**

- 1 strategy selected (possibly with execution gates)
- 1-2 fit options, often skewed to one register
- Single volume preference or "minimal"
- "Nothing in particular" featuring or 1 zone only
- Multiple fabric discomforts
- Multiple zones covered
- Specific preferences on rise/cut/length (constraints, not flexibility)

Most users fall on a spectrum. The synthesis layer produces a permissiveness score that calibrates how strictly the body type rules apply.

For permissive users: negative signals require multiple to filter; single positive signal can rescue; wide catalog; behavior data refines aggressively.

For restrictive users: single negative signal can filter; multiple positives required to overcome negatives; narrow hero-weighted catalog; behavior data confirms slowly.

For median users: median strictness, standard application.

### What "obvious fail" means

For a permissive user, an obvious fail is:

- Actively works against the body in a way styling can't fix (bodycon column in clingy fabric on cling-averse user — no styling rescues it)
- Closed item that can't be styled (tight items that don't allow layering, belting, tucking, or compensation; the user has no agency over the silhouette)
- Explicit user constraint violated (avoided cut, covered zone, flagged fabric)
- Universal structural failure for the body type

For a permissive user, an item that has *one* soft-rule signal but multiple compensating positives is not a fail. Restrictive users have lower thresholds for soft rules.

This is the core operating principle: flag only what definitely fails for this user. The body type rules describe the geometric truth and failure modes. The user's permissiveness signals tell us how strictly to apply them.

### The featuring-zone question

The questionnaire asks the user: *"What do you like most about your body?"* (multi-select)

- Décolletage / collarbones
- Bust
- Shoulders
- Arms
- Waist
- Hips / curves
- Seat
- Legs
- Back
- I'm not sure / nothing in particular

This gives direct signal about which zones to feature, which the rules previously tried to infer from Q3 distribution, Q4 fit issues, and exposure preferences alone. The featuring-zone signal doesn't replace those other signals; it complements them and resolves several common ambiguities.

### How named-zone signals interact with body-type defaults

When the user names a featuring zone, the system applies one of four treatments depending on how the zone relates to the body type's geometric defaults:

- *Named zone is a default body-type asset:* **amplify**. Surface featuring items for that zone aggressively. The user's named preference resolves any ambiguity about featuring intent that the rules previously gated behind combinational signals.
- *Named zone is geometrically neutral for the body type:* **unlock**. Treat it as a featuring zone even though body-type defaults didn't elevate it. Surface featuring items for that zone.
- *Named zone is one the body type typically manages or hides:* **respect over default**. The user's stated preference shifts toward celebrate-mode for that zone. Surface featuring items at the appropriate mode (reveal/sophisticated/cover); suppress default minimization moves for that zone.
- *Named zone is not relevant to the body type's defaults:* **unlock as edge target**. Same as neutral.

When the user doesn't name a zone, fall back to body-type defaults for that zone.

When the user selects "I'm not sure / nothing in particular," interpret as a lower-confidence signal: surface conservative body-type defaults, hero-weighted recommendations; don't push edge-featuring strategies; rely on behavior data to refine over time.

### Featuring intent changes the goal, not the geometry

When a user names a zone the body type typically manages, the system shifts from "minimize this zone" to "feature this zone well" — but "well" still respects body-compatible execution. Featuring intent is not a permission slip to abandon geometry rules; it is a redirection of what the geometry rules are optimizing for.

Examples of the distinction:

- *Pear naming hips:* unlocks celebrate-mode items (bodycon, pencil skirts following the hip, low-rise, bright bottoms, hip-detail cuts). Still filters clingy cheap fabric that distorts the curve, hip-pocket bulk that adds visual width without shape, horizontal seams that segment rather than celebrate the hip line. The goal moved from "skim hips" to "feature hips well" — the second goal still has rules.
- *Inverted triangle naming shoulders:* unlocks shoulder-featuring access. Default surfaced execution is body-compatible — one-shoulder asymmetric, halter, clean sleeveless, sharp tailoring with controlled shoulder, open necklines with narrow strap. Not heavy puff sleeves, 80s shoulder pads, stiff boat necks — those amplify in ways that don't actually flatter the body even when the user wants shoulders featured. Style archetype modulates intensity: edgy/dramatic archetype + reveal mode unlocks more aggressive execution; clean/minimal archetype keeps featuring at controlled sophisticated execution.
- *Apple naming midsection:* very rare confident-feature signal. Unlocks fitted dresses with structural support, skim-fit construction that doesn't hide the body. Still filters thin clingy fabric that reveals every contour without supporting the silhouette, and items that lack structural integrity for the featuring to read intentionally.
- *Rectangle naming hips/seat:* unlocks hip-emphasis cuts cautiously. Surfaces fitted bottoms, low-rise, hip-detail items at the user's mode. Still respects the flat-seat reality — surface items that work with the body's actual shape rather than items designed for projected seats that read empty on a flat-seat rectangle.

The principle: a named feature zone redirects the system's goal for that zone from "manage" to "feature well." The "feature well" goal is still subject to geometry. The body type knows how to execute the feature in a way that flatters; the user's preference unlocks the access, the geometry still informs the execution.

### The three-mode framework: reveal, sophisticated, coverage

For each named featuring zone, the user operates in one of three modes. The mode determines which featuring items get prioritized.

- *Reveal mode:* sustained skin reveal is acceptable. Surface bare-shoulder off-shoulder for shoulders, deep V for chest, fully open back for back, mini hems for legs, crop tops for midriff, etc.
- *Sophisticated mode:* the zone is featured through fit, line, framing, and intermittent or controlled reveal rather than sustained exposure. Surface boat necks (broadens without bare shoulder), keyhole or asymmetric cutouts, three-quarter sleeves with detail, midi or maxi with slit (leg reveal in motion, not at rest), fitted bodice without cleavage, sheer panel insets, scoop back without fully open back.
- *Coverage mode:* the zone is featured through emphasis (fit, structure, color, detail) but skin stays covered. Surface high necklines with detail, structured shoulders with long sleeves, fitted-waist tops with closed neckline, color or print emphasis without skin reveal, fitted pants in interesting fabric, monochromatic leg-extending palettes.

**Sophisticated mode is the most common state for adult dressers** — feature the asset without going full reveal. Default to sophisticated when signals are ambiguous. Reveal mode and coverage mode are both real but require clearer signals.

### Mode detection

The system detects mode through the combination of:

- Featuring-zone question answers
- Exposure preferences (zone-specific when possible: chest, back, arms, midriff, legs)
- Length preferences (short hems, mini, midi, maxi, crop, long sleeves, etc.)
- Behavior data over time

Combinations and their resolutions:

- Names zone + selects reveal-friendly preferences for that zone → **reveal mode**
- Names zone + selects non-reveal preferences for that zone (midi/maxi but slit available, fitted but not bare, fitted three-quarter sleeves, etc.) → **sophisticated mode**
- Names zone + selects coverage preferences (long lengths, high necklines, full coverage) → **coverage mode** (still featuring through styling, no skin)
- Doesn't name zone + reveals it through exposure → user comfortable showing it but it's not a featuring zone; defer to body-type defaults
- Doesn't name zone + covers it → cover the zone without featuring; primary emphasis elsewhere
- Named multiple zones → sophisticated multi-strategy user; widen catalog
- "Nothing in particular" → conservative defaults; lower-confidence baseline; behavior data refinement becomes more important

### Browse mode vs. search mode

The featuring-zone framework matters most for browse mode (no explicit query). When the user searches "midi dress with slit," her query overrides the inferred mode for that session — she's telling the system exactly what she wants. The stored mode profile shapes what the system surfaces when she opens the app with no query.

Per-user, per-zone storage:
- One mode value per featuring zone (bust, back, shoulders, arms, waist, midriff, hips/seat, legs, décolletage)
- Initial state from questionnaire (featuring-zone question + exposure + length preferences)
- Refined over time through behavior (saves, dismisses, purchases, searches, dwell time)

### Cross-body principle on conflicts

When a user names a feature that her body type typically manages (apple names midsection, inverted triangle names shoulders, pear names hips when balance mode would suggest minimizing), the system respects the user's stated preference. Surface items that feature the zone at her detected mode. This is the user telling the system "stop trying to hide this; help me feature it."

When a user doesn't name a zone the body type considers an asset (rectangle doesn't name legs even though legs are the rectangle's default asset), still surface body-type defaults for that zone but at lower priority than the named zones. The user didn't reject the zone; she just didn't actively name it. Surface conservative defaults; learn from behavior.

---

# Body Type: Rectangle

**TL;DR:** Rectangle needs either trace precision, real anchor, real sculpt, or intentional edge/proportion play. What fails is fake shape, limp anchor, clingy column, bulky box, or unintentional length.

## 1. Identification

**How users self-identify in Q2:** "My shoulders, waist, and hips are about the same width."

**Confirming signals from Q3 (distribution):**

*Snug zones — diagnostic:*
- Chest and/or waist/stomach
- Nowhere specific (lean rectangles)

*Snug zones — noisy / not diagnostic:*
- Arms, hips/thighs, seat (these can fire for many reasons unrelated to rectangle classification)

*Loose zones — diagnostic:*
- Seat (rectangles commonly have flat seats and back-gaping pants is a near-universal complaint)
- Arms, hips/thighs (lean rectangles often report these as loose)
- Chest (lean rectangles)

*Loose zones — noisy:*
- Waist/stomach (a "loose at waist" answer suggests slim rectangle, not a contradiction)

**Confirming signals from Q4 (fit issues):**

*Fit issues — diagnostic:*
- Feels tight in the chest (wider ribcage rectangle)
- Feels tight in the waist (the fact that the natural waist isn't smaller than chest/hips means standard tailoring assumes a taper that isn't there)
- Feels too loose around hips/seat (the universal flat-seat complaint)
- "Everything usually sits how it should" — also possible for lean balanced rectangles

*Length issues — diagnostic:*
- Pants feel too short / tops feel too cropped → if tall (rectangles tend to have longer legs and arms; standard cuts run short on tall rectangles)
- Pants feel too long / tops feel too long → if petite (same proportional reality, just at smaller scale)
- "Everything usually sits where it should" — common for mid-height rectangles around 165–172 cm

**Conflicting or ambiguous signals to watch for:**

- *Snug at seat:* fuller-bottomed rectangle exists. Treat as a real geometric variation. Rectangle styling rules still apply (waist creation, vertical line moves, ribcage ease) but suppress the "seat shaping" default — she has volume there already.
- *Snug at arms or hips/thighs:* common in non-lean rectangles. Doesn't indicate a different body type. Use it to flag bulk-aversion in those zones but don't reclassify.
- *Loose at waist:* indicates slim rectangle. Don't interpret as evidence of a defined waist (which would suggest hourglass). The waist is loose because the body is narrow throughout, not because there's a taper.
- *Snug at chest with no other signals:* could be wider ribcage rather than fuller bust. If the user didn't flag chest exposure as covered and didn't pick anchor strategies emphasizing bust, default to ribcage interpretation.

**Distinctions from adjacent body types:**

- *Rectangle vs. hourglass:* hourglass has a measurable taper (waist 25%+ smaller than bust/hips). Rectangle does not. The Q3 + Q4 combination (loose at seat, tight at waist, gaping waistbands) reliably distinguishes.
- *Rectangle vs. inverted triangle:* inverted triangles have shoulders distinctly broader than hips. Rectangles have balanced shoulders and hips. If user says shoulders are broadest, it's inverted triangle, not rectangle.
- *Rectangle vs. apple:* apples carry weight specifically at the midsection, with the waist being the widest point. Rectangles are uniform — waist isn't widest, just not smaller. If user picks "fullness around midsection" she's apple, not rectangle.

## 2. Geometric Truth

**Core proportions:**
- Balanced shoulder, bust, and hip widths, generally within 5% of each other
- Undefined waist: typically less than 25% smaller than the bust
- Straight silhouette through the ribcage and hips
- Flat or minimally curved seat

**Where volume sits:**
- Tendency toward fullness: waist, midsection, chest (when present), upper arms (sometimes)
- Tendency toward flatness: seat, hip curve
- Typically lean: arms, legs (proportionally)

**Length tendencies:**
- Legs longer than torso (consistent across heights)
- Arms tend to run long
- Tall rectangles (170+): legs read as a clear visual asset; can carry longer outerwear, longer skirts, longer dresses
- Mid rectangles (165–169): proportional in standard sizing
- Petite rectangles (under 160): long legs proportionally but absolute length is short; standard items often run long

**Common geometric variations within the type:**

- *Wider-ribcage rectangle:* fuller through the chest panel and ribcage. Needs ease through the ribcage. Open necklines become high-priority relief moves. Closed/high necklines combined with fitted ribcage panels read boxy fast.
- *Narrow-frame rectangle:* lean throughout. More styling tolerance — can wear a wider range of cuts because the body itself is small in volume. Also more risk of "swallowing" in oversized cuts; structure matters more.
- *Fuller-bottom rectangle:* has volume at the seat without hip flare. Seat-shaping defaults are suppressed (volume already exists). All other rectangle rules apply.
- *Athletic rectangle:* visible muscle definition, sometimes broader shoulders without inverted-triangle proportions. Carries structured tailoring beautifully. Watch for cap sleeves and structured shoulders that amplify what's already visible.
- *Midsection-prone rectangle:* shoulders and hips balanced but the midsection is the softest or fullest zone, often post-pregnancy, post-menopause, or natural body composition. Different rules fire from those for slim or wider-ribcage rectangles. See the midsection-prone modulator in section 6.

## 3. Visual Assets (default, before strategy modulation)

**Natural assets (read well without intervention):**

- *Long, slim legs:* the default geometric asset for rectangle. Proportionally longer than torso across heights, slim because rectangles don't carry hip flare. Surfaced as a primary recommendation lever when confirmed by featuring-zone, exposure, or length-preference signals; otherwise treated as a background asset informing secondary item selection.
- *Lean arms:* proportionally narrow. Sleeveless and short-sleeve cuts work without arm self-consciousness for most rectangles.
- *Décolletage and collarbones:* the chest area below the neck and above the bust often reads cleanly because rectangles tend not to have heavy bust-forward weight.
- *Wrist and ankle:* lean extremities. Become useful in edge strategy (cuffed sleeves, cropped pants that hit just above ankle, wrist-tie details).
- *Back:* typically lean and clean; works as a back-detail featuring zone when user wants it.

**Features that become assets when used intentionally:**

- *Shoulders:* can carry structured tailoring beautifully. Tailored blazers, structured outerwear, defined shoulder lines — rectangles often look better in these than other body types.
- *Waist (created):* through anchor or sculpt, a waist can be constructed where none exists. A well-cinched rectangle reads more dramatic-hourglass than a natural hourglass because the contrast is engineered.
- *Vertical line:* the rectangle's natural line is uninterrupted from shoulder to hip. With the right styling (open layers, single-color outfits, length-emphasizing cuts), this becomes elegance rather than boxiness.

**Override conditions:**

- *Legs not an asset:* if user covers legs in exposure, refuses short lengths, refuses skirts/dresses entirely, or marks both relaxed/oversized on bottom AND no preference for short — assume she doesn't want leg focus. Suppress short-length and slit-forward recommendations.
- *Décolletage not an asset:* if user covers chest/neckline in exposure or specifically marks chest as snug. Suppress open-neckline-as-relief defaults; treat closed/modest necklines as preferred.
- *Shoulders not a feature:* if user is wider-ribcage rectangle who finds tailored items feel boxy (rare; most rectangles benefit from tailoring). Trust her stated preferences here over the default.

**Featuring-zone signals from the questionnaire (cross-body framework):**

- *Legs named:* amplify. Surface short hems, slits, fitted bottoms showing leg line. Rectangle's primary asset confirmed.
- *Arms named:* amplify. Surface sleeveless, short sleeves, arm-revealing cuts; reverse any default cap-sleeve filters.
- *Décolletage named:* amplify. Surface open V-necks, scoops, deep necklines; resolves the open-neckline relief vs. featuring ambiguity.
- *Shoulders named:* amplify and unlock. Surface structured-shoulder tailoring, off-shoulder, one-shoulder, statement-shoulder edge items.
- *Waist named:* unusual but meaningful for rectangle (no natural waist). Signals user wants waist creation prioritized. Surface anchor and sculpt items aggressively even if she didn't explicitly pick those strategies.
- *Bust named:* if she has bust to feature, surface bust-emphasis items; combine with exposure to determine depth (see three-mode framework).
- *Back named:* unlock signature back-featuring move (low-back, open-back, keyhole back, lace-up back). Rectangle's lean back is well-suited to this category.
- *Hips/seat named:* unusual for rectangle; signals user wants to feature lower body despite the flat-seat default. Surface hip-emphasis cuts cautiously — low-rise becomes available; jeans with shaped back pockets that lift seat visibility surface. Filter items designed for projected seats that read empty on a flat-seat rectangle (curve-cut bodycon that's drafted for hourglass seat projection). Behavior data refines whether this is genuine preference or experimental.
- *"Nothing in particular":* conservative defaults; hero-weighted recommendations; don't push edge-featuring; rely on behavior data to refine.

## 4. Visual Risks (default, before strategy modulation)

**Silhouettes that fight this body type:**

- *Tight column dresses (closed neckline + no waist + no slit + midi/long):* the body reads as a flat rectangle painted onto a flat fabric rectangle. No vertical break, no interest, no shape. Failure mode: "looks like a brick."
- *Dropped waist:* shifts the visual waistline below the natural waist, elongating the torso and shortening the leg — exactly opposite to what rectangles need. The body's only real asset (legs) is visually shortened.
- *Over-the-waist jacket (mid-thigh outerwear with no shape):* covers the only place a rectangle could create a waist. Hides the proportion break and reads as a long tunic over pants.
- *Bulky knits and sweatshirts:* horizontal volume on a body without horizontal taper amplifies the boxy reading. The bulk doesn't drape over curves; it just sits.
- *Clingy thin fabrics:* show every contour without adding shape. Rectangle + clingy = visible flat panel + visible underwear lines + no improvement to silhouette.
- *Fake anchor (drawstring, self-tie, thin belt) without real construction:* implies a waist that isn't there; the garment hangs limp at the cinching point. Especially severe failure for midsection-prone rectangles — the gathered fabric adds visible width at the body's widest point.
- *Square necklines:* on a rectangle, a square neckline creates a square on a square — visually amplifies the boxy reading. Particularly bad on wider-ribcage rectangles.
- *Cap sleeves (on broader rectangles):* extend the shoulder horizontal without breaking the upper body; cap sleeves work better on lean rectangles where the shoulder doesn't need narrowing.
- *Drop-shoulder dolman:* extends the visual shoulder width without intentional broadening; reads as sloppy rather than tailored.

**Construction details that fail:**

- *Heavy horizontal seaming at the natural waist:* implies a waist that isn't constructed strongly enough to actually create one; the seam reads as a horizontal stripe rather than a break point.
- *Side seams with hip ease but no waist taper:* leaves the silhouette boxy without giving the structure a purpose.
- *Heavy fabric without lining:* sits stiffly without drape; on a body without curves, this reads as cardboard.

**Fabric behaviors that fail:**

- *Thin clingy jersey:* shows every contour, no shape support.
- *Stiff heavy denim without stretch:* sits away from the body, adds visual bulk.
- *Bulky chunky knits across the torso:* horizontal volume on a body that needs vertical lines.

**Necklines that fail (default):**

- High closed crew, mock neck, turtleneck on wider-ribcage rectangle (creates wall, emphasizes the ribcage panel).
- Square necklines (double-square problem).
- Boat necks on broader rectangles (extends shoulder horizontal).

**Length traps:**

- For petite rectangle: standard midi often hits at calf-widest; standard tops often run long, hiding the natural waist meeting point; oversized + petite is the highest-restriction combination.
- For tall rectangle: standard cuts run short on tops and pants; cropped items intended as cropped read as standard-length on tall rectangles; long outerwear works particularly well.
- For mid-height: standard cuts usually work without modification.

**Override conditions:**

- *Boxy tops:* can work when worn open over a fitted base (open layer + closed neckline becomes vertical-line-with-relief).
- *Long heavy outerwear:* works on tall rectangle, fights petite rectangle.
- *Cap sleeves on broader rectangles:* override when paired with strong waist anchor that breaks the silhouette below the shoulder.

## 5. Strategy Modulation

### Trace

**What trace means for this body type:**

Trace has the narrowest margin for error on rectangle — works for lean and narrow-frame variations where the column reading is muted by overall slenderness, fails when the body's natural shape (column from shoulder to hip without taper) gets traced and amplified. Trace tops will trace the boxy ribcage; trace bottoms will trace the flat seat. A user picking trace-only is signaling either (a) lean rectangle where the boxy reading is naturally muted, or (b) very specific styling vocabulary that requires hero-weighted selection.

**What works under trace:**

- Fitted polos and fitted button-downs (skim the body, create vertical line through placket and collar)
- Slim straight-leg pants (legs are an asset, no flare needed)
- Sheath dresses in skim-fit fabric (close-fit but not clinging; works on lean rectangle)
- Fitted ribbed knit tops ending at high hip (clean line, no bulk)
- Tailored shirt dresses with subtle waist shaping
- Slim trousers and tapered pants (lean legs featured)

**What fails under trace:**

- Tight column dresses with closed necklines (the failure mode)
- Bodycon in cheap stretch (reveals every contour without adding shape)
- Thin fitted tees that show ribcage outline
- Stretchy pencil skirts that hug a flat seat (no shape to honor)

**Special considerations:**

- Lean rectangle: most trace items work; the boxy reading is mild.
- Wider-ribcage rectangle: trace tops at the ribcage fail; surface trace items with shoulder structure or vertical line breaks.
- Petite rectangle + trace-only: highest-restriction combination. Surface fewer items, all hero-quality.

### Anchor

**What anchor means for this body type:**

Anchor *creates* a waist the rectangle doesn't have. This is the strongest single move for shifting the body's silhouette from boxy to shaped. Rectangle anchor must be **hard** anchor — real construction or substantial belt with proper cinching — because there's no waist underneath to fill in a soft anchor.

*Note on strategy-frame application:* the failure modes below (soft anchor, drawstring on relaxed dresses, self-tie on flowy fabric) apply when anchor is the strategy the item is executing. They do not apply to items executing edge or other strategies. A flowy tunic with drawstring at the neckline is not "failing soft anchor" if the strategy in play is edge — the drawstring isn't trying to be a waist anchor, and the item's success depends on its edge execution (strategic features, asset-aligned redirects), not on anchor mechanism. See the cross-body framework for the full principle.

**Hard vs. soft anchor:**

- *Hard anchor (real waist creation):* defined waist seam with darts, structured belt with proper cinching, peplum that flares from a constructed waist, fitted bodice with real shaping, wrap dress with substantial tie that pulls in fabric. These create the waist the body doesn't have.
- *Soft anchor (drawstring, self-tie, thin belt):* fails on rectangle because the body doesn't have a waist to anchor to — the soft mechanism cinches the fabric but the fabric just gathers without creating shape. The gathered point looks like added bulk, not a defined waist. Particularly severe for midsection-prone rectangles where the gathered fabric adds visible width at the widest point.

**Specific anchor moves that work:**

- Wrap dresses with substantial tie and structured fabric (the tie does real cinching work)
- Belted dresses with real belts (medium to wide width, proper buckle, real grip)
- Belted shirt dresses (belt creates shape, shirt provides drape)
- Peplum tops and peplum jackets with structured construction
- Fitted bodice + flared skirt dresses (the bodice creates the waist illusion through fit)
- Princess-seamed dresses (vertical shaping that implies taper through construction)
- High-rise bottoms with fitted top tucked in (the tuck point + waistband + fitted top creates implied anchor)

**Anchor moves that fail:**

- Drawstring waists on relaxed dresses (fake anchor — gathers fabric without creating shape)
- Self-tie waists on flowy fabric (same problem)
- Thin string belts on heavy fabric (decorative, not functional)
- Wide belts on flat-seat rectangles (cinches into the waist but the contrast with the flat hips below makes it look forced)

**Special considerations:**

- Rectangle anchor is binary: it either works (real construction) or fails (fake anchor). Avoid the middle ground.
- Wider-ribcage rectangle: anchor must accommodate the ribcage volume; surface items with ease through ribcage + cinch at natural waist.
- Midsection-prone rectangle: anchor moves to *above* the midsection (high-rise meeting fitted top above the widest point), or *below* the midsection (low anchor at high hip). Anchor at the natural waist on midsection-prone rectangle creates a horizontal line at the widest point.

### Sculpt

**What sculpt means for this body type:**

Sculpt imposes shape through construction. Different from anchor: anchor frames an existing waist position; sculpt creates a shape that doesn't exist. For rectangle, sculpt is the strongest evening-wear strategy because it physically creates curves where the body lacks them.

**What good sculpt looks like for this body:**

- Corseted bodice dresses (creates dramatic waist)
- Fit-and-flare dresses with very fitted bodice + dramatic skirt flare
- Princess-seamed dresses that pull in at the waist more sharply than the body's natural line
- Tailored peplum jackets with strong waist shaping
- Structured fit-and-flare coats
- Bustier-style dresses with full skirts

**What bad sculpt looks like:**

- Sculpt in thin cheap fabric that doesn't hold shape (the sculpt collapses on the body and reads worse than no sculpt)
- Sculpt that promises structure but delivers polyester drape (the Aritzia navy dress failure mode — looks like sculpt in photos, fails on the body)
- Sculpt with heavy shoulder pads on top of strong waist construction (over-engineered; reads costume-y)
- Empire sculpt that puts the waist seam too high (above the natural waist) and creates a column from bust down

**Special considerations:**

- Sculpt quality matters more for rectangle than for other body types because the body doesn't have shape to fill in poor construction. Fabric weight, construction quality, and brand tier matter.
- Lean rectangle: sculpt creates dramatic results because the body has minimal volume; the sculpt does all the shape work.
- Midsection-prone rectangle: sculpt becomes especially valuable for evening because structured construction can physically smooth and reshape the midsection where fluid clothing can't.

### Edge

**What edge means for this body type:**

When the user doesn't want to deal with body shape at all, edge redirects attention to assets and uses proportion play to control the eye. Rectangles have clear assets edge can work with (legs, arms, décolletage, back) and clear proportion-play options (volume distribution across top and bottom).

**Featuring vs. balancing modes for this body type:**

Both modes work. Many rectangles use both depending on the outfit.

- *Featuring mode:* draws eye to legs (slits, short hems, leg-revealing cuts), arms (sleeveless, short sleeves), décolletage (open necklines), back (low-back, open-back) — assets the rectangle naturally has.
- *Balancing mode:* uses volume distribution to create proportion play. Volume on top + fitted bottom (boxy short jacket + slim trouser), or volume on bottom + fitted top (fitted tank + wide-leg pants). Both create proportion break that the body's column doesn't have.

**Edge moves that work:**

*Featuring mode:*
- Short A-line dresses and skirts (legs feature)
- Mini hems on lean rectangle (with proportion check on petite)
- Slits on midi and maxi dresses (sophisticated leg feature)
- Sleeveless and short sleeves (arms feature)
- V-necks, scoops, deep V (décolletage feature)
- Low-back dresses, open-back tops, keyhole back, lace-up back (back is a non-front asset surface for rectangles)
- One-shoulder asymmetric (diagonal break + back/shoulder feature)
- Halter (narrow at neck, exposes upper back and shoulder line)
- Crop tops over high-rise bottoms (waist meeting point exposes the constructed-waist illusion)

*Balancing mode:*
- Wide-leg trouser + fitted tank
- Fitted top + voluminous skirt
- Boxy short jacket + slim trouser
- Statement sleeves + slim bottom
- Volume on one zone + fitted compensation elsewhere

**Edge moves that fail:**

- Edge moves that draw attention to risks rather than assets (cropped tops that emphasize a wider ribcage on wider-ribcage rectangle)
- Edge that hides assets while featuring nothing (long heavy jacket over fitted dress on tall rectangle — covers the legs without giving the eye anywhere else to go)
- Statement features at the wrong zone for the user (waist features on a rectangle who doesn't want waist creation)

## 6. Combinational Rules

**Body + strategy combinations:**

- *Rectangle + trace:* surface fitted skim-fit items, slim bottoms, sheath dresses. Hero-weighted for trace-only users. Wider-ribcage rectangles need vertical line breaks within trace.
- *Rectangle + anchor:* when anchor is the selected strategy, surface hard-anchor items (real construction, real belts, structured peplum). Filter soft anchors aggressively. Note: these filter rules apply when the item is executing anchor; items executing edge or other strategies are evaluated on those strategies' criteria, not anchor's.
- *Rectangle + sculpt:* surface sculpt with quality construction. Filter low-quality sculpt that promises structure but delivers drape.
- *Rectangle + edge:* both featuring and balancing modes available; weight visual asset featuring (legs, arms, décolletage, back) and proportion-play balancing (volume + fit).
- *Rectangle + trace only:* hero-weighted surfacing; narrow item set.
- *Rectangle + multiple strategies:* widen catalog; sophisticated rectangle dressers like Anastasia can use all strategies in different outfits.

**Body + fit combinations:**

- *Rectangle + close everywhere:* fights the body's column; requires real anchor construction or sculpt to add shape.
- *Rectangle + close top + relaxed bottom:* works when relaxed bottom is structured (wide-leg trousers) and close top provides the upper-body definition.
- *Rectangle + relaxed top + close bottom:* the classic rectangle uniform when paired with proportion play. Boxy short jacket + slim trouser pattern.
- *Rectangle + relaxed everywhere:* requires compensation that prevents column-reading. Acceptable compensation includes: (a) hard anchor (real belt, real wrap, structured construction creating waist), (b) sculpt outer layer (structured blazer or jacket over relaxed base), (c) edge through multiple strategic features (V-neck + slits + asymmetric detail + wrist openings — strong featuring across multiple zones that redirect attention from the column). Pure shapeless without any compensation = failure. Strategy selection determines which compensation type applies: anchor strategy needs (a); sculpt needs (b); edge needs (c). Multi-strategy users have multiple paths available.

**Body + fabric combinations:**

- *Rectangle + cling-averse:* filter thin clingy fabrics; surface structured fabrics with body.
- *Rectangle + heavy-averse:* applies more to top half; bottoms can be substantial.
- *Rectangle + soft drape preferred:* surface fluid fabrics for tops; structured for bottoms.
- *Rectangle + structured preferred:* surface tailored fabrics with body; works particularly well for rectangle.

**Body + bust + exposure combinations:**

The bust + exposure intersection for rectangle works similarly to hourglass, calibrated by featuring-zone signal:

- *Rectangle + names bust + high exposure preference:* deep V, plunging, low sweetheart available. Cleavage-revealing necklines surfaced.
- *Rectangle + names bust + medium exposure + chest not flagged covered:* moderate-depth open necklines (V at collarbone-to-mid-chest, scoop at clavicle).
- *Rectangle + names bust + medium exposure + chest flagged covered:* moderate open necklines at shallower depth (V ending above bust, scoop at collarbone).
- *Rectangle + names bust + low exposure:* higher slim necklines, button-up with placket, layered.
- *Rectangle + doesn't name bust:* default body-type rules apply (open necklines for relief from boxy reading on wider ribcage; otherwise neutral).

**Body + featuring-zone combinations:**

- *Legs named:* amplify leg-featuring edge. Surface short A-line, slits, fitted bottoms showing leg line. Reveal mode unlocks mini hems; sophisticated mode unlocks fitted bootcut with slim trouser + ankle reveal; coverage mode features leg through line and length-elongating styling.
- *Arms named:* amplify arm-featuring. Surface sleeveless, fitted short sleeves, off-shoulder. Reveal mode unlocks fully bare arms; sophisticated mode unlocks three-quarter sleeves with fitted construction; coverage mode features through fitted long sleeves.
- *Décolletage named:* amplify chest-featuring. Surface open V, scoop, deep V at exposure-appropriate depth. Resolves the open-neckline relief vs. featuring question.
- *Shoulders named:* amplify and unlock. Surface structured-shoulder tailoring, statement-shoulder edge, off-shoulder, one-shoulder. Particularly meaningful for rectangles who like the tailored look.
- *Waist named:* unusual for rectangle but meaningful — user wants waist creation prioritized. Surface anchor and sculpt items aggressively. Strengthens the anchor strategy weighting.
- *Bust named:* see bust + exposure combinations above.
- *Back named:* signature unlock. Rectangle's lean back works well for low-back dresses, open-back tops, keyhole back, lace-up back. Surface these as heroes.
- *Hips/seat named:* unusual for rectangle (typically flat). Signals user wants to feature lower body. Surface hip-emphasis cuts cautiously; learn from behavior whether genuine preference.
- *"Nothing in particular":* conservative rectangle defaults; hero-weighted recommendations; don't push edge-featuring strategies.

**Body + variation modulators:**

- *Wider-ribcage rectangle:* surface vertical line breaks aggressively (V-necks, button plackets, open necklines); filter closed high necks; surface ease through ribcage.
- *Narrow-frame rectangle:* most items work; broader styling tolerance; surface structure to avoid being swallowed by oversized cuts.
- *Fuller-bottom rectangle:* suppress seat-shaping defaults (volume already exists); apply other rectangle rules.
- *Athletic rectangle:* surface tailored structure; cautious with cap sleeves and structured shoulders if combined with strong upper body definition.
- *Midsection-prone rectangle:* high-rise hits *above* the widest point; drawstring/self-tie waists fail more severely (gathered fabric adds width); shapeless volume at the midsection fails harder; sculpt becomes especially valuable; short hemlines and open necklines more important.

**Body + height variation:**

- *Tall rectangle:* surface longer items confidently; long open outerwear works particularly well; standard cuts may run short.
- *Mid-height rectangle:* most standard cuts work.
- *Petite rectangle:* short jackets ending at waist; cropped-at-waist preferred over cropped-above-waist; cautious with midi unless slit or with break; oversized + petite = highest-restriction combination, surface structured oversized only.

## 7. Hero Categories

**Hero items (consistent across rectangle):**

- Controlled wide-leg pants (high-rise, structured waistband, clean leg line)
- Slim straight-leg jeans (curvy fit when seat is present)
- Fitted polos and fitted button-downs
- Tailored blazers with shoulder structure
- Easy knits ending at high hip
- A-line short dresses and skirts (legs feature)
- Sheath dresses (skim-fit)
- Wrap dresses with substantial tie and structured fabric
- Belted shirt dresses
- Halter tops and halter dresses
- Asymmetric necklines (including one-shoulder)
- Crop tops over high-rise bottoms
- Boxy short jacket worn open over fitted base
- Long open dusters (especially for tall rectangle)
- Tunic dresses with slit and open neckline

**Hero necklines:**

- V-neck at varied depths (calibrated by bust + exposure + featuring-zone signal)
- Scoop neck
- Deep V (when chest exposure permits)
- Wrap/surplice
- Asymmetric one-shoulder
- Halter (narrow at neck, exposes upper back)
- Open button placket with vertical line down the front
- Square neck (caution — works only on lean rectangle without wider-ribcage signal)

**Necklines to avoid (default):**

- Closed high crew, mock neck, turtleneck on wider-ribcage rectangle
- Square neck on wider-ribcage rectangle (double-square problem)
- Boat neck on broader rectangles

**Hero sleeves:**

- Sleeveless and tank cuts (lean arms are an asset)
- Fitted short sleeves
- Three-quarter sleeves
- Fitted long sleeves
- Bishop and bell sleeves (when balanced with proportional bottom)
- Set-in sleeves with shoulder structure

**Sleeves to avoid:**

- Drop-shoulder dolman (extends visual shoulder without intention)
- Cap sleeves on broader rectangles (extends shoulder horizontal)
- Heavy puff sleeves (adds upper-body bulk without compensation)

**Hero pant silhouettes:**

- High-rise wide-leg (controlled, structured)
- High-rise straight
- Slim straight-leg jeans (curvy fit)
- Tapered trousers
- Skinny jeans (work for lean rectangle who wants to feature legs)
- Bootcut and flared jeans (subtle flare adds ankle interest)

**Pants to avoid:**

- Mom jeans with very loose hip (creates back-gap problem on flat-seat rectangle)
- Cropped pants hitting at calf-widest on petite rectangle
- Heavy front-pleated trousers (adds visual bulk to flat hip area)

**Hero dress and skirt silhouettes:**

- A-line short
- Wrap dresses with substantial construction
- Sheath dresses
- Belted shirt dresses
- Fit-and-flare with constructed bodice
- Tunic dresses with slit
- Short fit-and-flare with structured bodice
- Bias-cut maxi (drapes vertically; works for tall rectangle)
- Mermaid skirts (creates sculpt-style shape)

**Dresses and skirts to avoid:**

- Drop-waist dresses (shortens leg asset, lowers visual waist)
- Empire-line column dresses (eliminates waist creation opportunity)
- Bulky knit dresses without shape
- Wide-strap tanks that read flat and shapeless
- Fast-fashion "sculpt" items that promise shape but deliver drape

**Hero outerwear:**

- Tailored blazers with shoulder structure
- Belted trench coats (real belt, real cinching)
- Cropped jackets ending at natural waist
- Boxy short jackets worn open over fitted base
- Long open dusters (tall rectangle hero)
- Princess-seamed coats with waist shaping
- Moto jackets worn open or belted

**Outerwear to avoid:**

- Over-the-waist mid-thigh jackets without shape (covers the waist-creation zone)
- Long heavy outerwear on petite rectangle
- Boxy cocoon coats without belt or structure
- Double-breasted with heavy bulk down the front

**Hero items by strategy:**

- *Trace hero:* fitted polo + high-rise straight jeans; sheath dress; slim trouser + fitted ribbed knit
- *Anchor hero:* wrap dress with substantial tie; belted shirt dress; peplum top + slim trouser
- *Sculpt hero:* corseted fit-and-flare evening dress; princess-seamed fitted coat; bustier + full skirt
- *Edge hero (featuring):* short A-line + V-neck (legs + décolletage); low-back dress; halter top + slim trouser; sleeveless + statement bottom
- *Edge hero (balancing):* wide-leg trouser + fitted tank; voluminous skirt + fitted top; boxy short jacket + slim trouser

## 8. Disqualified Categories

**Items that don't work, regardless of strategy (universal hard filters):**

- Drop-waist dresses (structural failure — shortens leg asset across all strategies)
- Empire-line column dresses (eliminates waist creation opportunity AND has no edge features)
- Bulky chunky knit sweaters that hang straight from shoulder to hip with no openings or features (no strategy can rescue this — too heavy for trace, no anchor mechanism, no shape, no edge features)
- Wide-strap tanks with no structure that read as flat panels (no body engagement, no shape, no features)

**Items that fail when sculpt is the strategy:**

- Fast-fashion sculpt items that promise structure but deliver polyester drape (the construction quality doesn't survive — the sculpt collapses on the body)

**Items that fail when anchor is the strategy in play:**

These items execute anchor poorly. They filter when anchor is the user's selected strategy. They are evaluable for other purposes when other strategies are in play — a flimsy wrap dress might still execute edge through its drape and openings if those features are present.

- Wrap dresses in flimsy thin fabric (wrap doesn't do real cinching work — "looks right but disappoints" if user expected anchor)
- Drawstring waists on otherwise shapeless dresses (gathers fabric without creating waist)
- Self-tie waists on flowy fabric (same problem)
- Thin string belts on heavy fabric (decorative, doesn't anchor)

**Items disqualified by specific answer combinations:**

- Short hems disqualified for: rectangle + legs covered preference + relaxed bottom
- Sleeveless disqualified for: rectangle + arms covered preference
- Closed high necklines disqualified for: wider-ribcage rectangle + chest not flagged covered (failure of fit, not preference)
- Cropped jackets above waist disqualified for: petite rectangle (cuts off too high)
- Bodycon disqualified for: rectangle + cling-averse signal

**Items disqualified by featuring-mode signals:**

- Sustained skin reveal items disqualified for: zone in coverage mode (no bare-shoulder for shoulders in coverage mode; no plunging V for chest in coverage mode; etc.)
- Featuring items in named-but-coverage-mode zones surface at coverage-mode execution (high necklines with detail instead of plunging; structured shoulders with sleeves instead of off-shoulder)

**Items that look right but disappoint:**

- *Wrap dresses in flimsy fabric:* marketed as universal hero, but on rectangle the flimsy wrap doesn't create real anchor — the tie cinches but the fabric just gathers without shape. Surface wrap dresses in fabric with body and substantial tie.
- *"Belted" oversized dresses:* the belt at natural waist on relaxed fabric creates implied waist, but on flat-seat rectangle without structured fabric the belt + fabric reads as cinched bag rather than shaped silhouette. Surface belted items with structured fabric.
- *Fast-fashion sculpt:* the structure promised in photos doesn't survive the construction at price point; the sculpt collapses on the body.
- *"Universal flattering" trapeze dresses:* hide the body without giving it shape; rectangle reads as boxy under boxy.

## 9. The Uniform

**Daytime / casual uniform (mid-height, mid-sophistication, mixed strategy):**

High-rise straight or slim jeans in mid or dark wash, fitting through the leg without back-waistband gap. A fitted ribbed knit or fine-cotton tee in V-neck or scoop, ending at high hip, either tucked or half-tucked. Optionally, a boxy short jacket (cropped denim, structured blazer ending at waist) worn open over the fitted base, creating proportion play.

Footwear: pointed flats, ankle boots, or low heels. Pointed shoes extend the leg line.

**Variations by strategy:**

- *Trace-primary rectangle:* sheath dress alone; slim trouser + fitted button-down tucked in.
- *Anchor-primary rectangle:* wrap dress with substantial tie; belted shirt dress; peplum top + slim trouser.
- *Sculpt-primary rectangle:* corseted fit-and-flare for evening; princess-seamed structured pieces; fit-and-flare midi with strong bodice.
- *Edge-primary rectangle (featuring):* short A-line dress with V-neck (legs + décolletage); low-back evening dress; halter dress.
- *Edge-primary rectangle (balancing):* wide-leg trouser + fitted tank; boxy short jacket + slim trouser; volume play on one zone + fitted compensation.

**Variations by register:**

- *Work:* tailored trousers + fitted button-down + tailored blazer; sheath dress with structured blazer; pencil skirt + fitted knit.
- *Evening:* sculpt fit-and-flare; one-shoulder column with structure; low-back dress; halter gown.
- *Occasion:* belted shirt dresses, fit-and-flare midis, structured A-line dresses.

**Variations by season:**

- *Summer:* fitted tanks + slim cropped pants; short A-line dresses; sleeveless wrap dresses; light layered outfits with open jackets.
- *Winter:* fitted knits + slim pants + tailored coats; belted wool coats; long open dusters over fitted base + slim trouser.

## 10. Inference Notes for the Recommender

**Default rules that fire on rectangle identification alone:**

1. Surface anchor and sculpt strategies aggressively when user picks them. The body's lack of natural waist makes constructed shape valuable.
2. Filter fake anchors (drawstring, self-tie, thin belts on heavy fabric) when anchor is the strategy the item is executing — they fail on the rectangle body. Don't apply this filter to items executing edge or other strategies where anchor isn't in play.
3. Surface vertical-line items (open layers, V-necks, vertical seam construction) for wider-ribcage rectangle.
4. Surface fitted bottoms (slim, straight, tapered, skinny for lean) as the rectangle's leg-asset feature.
5. Filter drop-waist and empire-column items universally for rectangle.
6. Surface tailored blazers and structured outerwear — rectangle's shoulder structure works.
7. Petite rectangle + oversized = filter unless structured oversized; highest-restriction combination.
8. Wider-ribcage rectangle + closed high necklines = filter; surface open necklines and vertical line breaks.
9. Lean rectangle has broader styling tolerance; most items work.
10. Midsection-prone rectangle: anchor moves above or below the natural waist; drawstring fails more severely; sculpt becomes valuable for evening.
11. Color/value contrast at the waistline functions as anchor through visual break — surface items that create this through styling combinations.
12. Slits and release points on long bottoms (maxi, midi) work; long bottoms without slits read as column failure.
13. Knits must avoid both bulk and midsection-width; surface fine-gauge knits with shape over chunky styles.
14. Sleeve construction matters for outerwear sculpt; structured shoulders + cinched waist creates the chest-to-waist ratio rectangle lacks.

**Modulators that change defaults:**

- *Strategy selection:* trace highly restrictive (hero-weighted only); anchor must be hard anchor (filter soft); sculpt requires quality construction; edge offers both featuring and balancing modes.
- *Fit preferences:* close everywhere requires real construction (anchor strategy needs hard anchor; trace needs precise fit; sculpt needs quality construction). Close top + relaxed bottom works with structured bottom for proportion play (edge). Relaxed top + close bottom is the proportion-play uniform (edge). Relaxed everywhere requires compensation appropriate to selected strategy: anchor compensation if anchor selected, sculpt outer layer if sculpt selected, multiple strategic edge features if edge selected.
- *Fabric importance:* high importance + sculpt or structure → strict quality filter; high importance + drape preferred → fluid fabric with body, not clingy thin.
- *Featuring-zone signal:* primary modulator alongside strategy and fit. Named zones amplify featuring for that zone; named risk-zones shift toward celebrate-mode for that zone; "nothing in particular" signals lower confidence and conservative defaults.
- *Per-zone reveal mode (reveal/sophisticated/cover):* detected through combination of featuring-zone naming, exposure preferences, and length preferences. Default to sophisticated when signals are ambiguous.
- *Variation modulators:* wider-ribcage (open necklines critical); narrow-frame (broader tolerance); fuller-bottom (suppress seat-shaping defaults); athletic (cautious with shoulder amplification); midsection-prone (anchor moves above/below natural waist; drawstring filters more aggressively).

**Sophistication and restrictiveness signals:**

- Multi-strategy + flexible fit + multi-zone featuring named → widen catalog (sophisticated rectangle dresser; can use rule-bending compensation)
- Trace-only + multiple covered zones + petite + wider-ribcage → tighten catalog significantly; surface fewer items, hero-weighted only
- Strong featuring-zone signal for shoulders or back → unlock structured tailoring and back-detail items as heroes
- "Nothing in particular" → conservative defaults; surface hero items; behavior data refinement critical

**Risk-scanning patterns common to rectangle:**

- Whether items create real waist or fake-anchor failure
- Whether sculpt items have construction quality matching the silhouette they promise
- Whether wider-ribcage signal is being respected in neckline selection
- Whether long bottoms have release points (slit, movement, asymmetric hem)
- Whether knits avoid bulk and midsection width
- Whether color/value contrast at waist functions as visual anchor in outfit combinations
- Whether sleeve construction supports outerwear shape

**Common "knows the trick" non-traditional moves:**

- Sophisticated rectangle dressers may wear drop-waist if compensating with peplum-like fit on a petite frame (Anastasia pattern)
- May use color blocking with dark waist panel within lighter outfit to create implied waist
- May wear long heavy outerwear if tall, using the length to create vertical line rather than fighting the body
- May feature back as primary attention zone (low-back, open-back, keyhole) — rectangle's lean back is an underused asset
- May feature shoulders aggressively through structured tailoring or off-shoulder when user signals shoulders as a featured zone

**On rule restrictiveness vs. user variation:**

Rectangle rules optimize for the population of rectangle users, not every variation within. Some rectangles look great in items the rules filter out (very lean rectangles in column dresses; sophisticated dressers in drop-waist with peplum-functioning hems on petite). The rules correctly don't surface these proactively because the cost of mis-surfacing them to the median rectangle is higher than the cost of missing them for variation users. Variation users find items through search and behavior over time.

## 11. Open Questions and Edge Cases

**Cases the rules don't yet handle:**

- *Rectangle + significant athletic training:* may shift toward inverted triangle if upper body develops broader; re-classify based on current proportions.
- *Rectangle + post-pregnancy:* often shifts toward midsection-prone variation; apply the midsection-prone modulator.
- *Very-lean rectangle (Olivia Jade pattern):* operates outside median rules; column dresses work because the body is small enough; system stays out of her way.
- *Rectangle + statement bust:* bust featuring becomes a meaningful edge play if combined with named-bust signal and appropriate exposure.

**Borderline body-type identifications:**

- *Rectangle vs. inverted triangle with broad shoulders:* if shoulders are 1-3% wider than hips, treat as rectangle (rules will mostly serve). If 5%+ wider, treat as inverted triangle.
- *Rectangle vs. hourglass with mild waist taper:* if waist is less than 25% smaller than bust/hips, rectangle. If 25%+, hourglass.
- *Rectangle vs. apple:* if midsection is the *widest* point (projecting beyond shoulders and hips), apple. If midsection is *equal to* shoulders and hips but soft, midsection-prone rectangle.

**Things behavior data should resolve:**

- Mode preferences for each named featuring zone (reveal vs. sophisticated vs. cover)
- Whether named features actually drive behavior (some users name features they like in principle but don't actually shop for; learn from purchases and saves)
- Tolerance for sculpt construction quality (some rectangle users buy fast-fashion sculpt that fails; learn whether to filter brand-tier or by individual brand)
- Length tolerance at various heights
- Trace tolerance for lean rectangles (some embrace column items; others want construction)
- Color/value contrast as anchor effectiveness in individual outfit combinations


---

# Body Type: Inverted Triangle

**TL;DR:** Inverted triangle has four strategies available. Anchor is the most powerful for users who want to create waist and add lower-body volume. Edge bypasses the proportion question by redirecting attention to assets (legs, décolletage). Sculpt builds shape. Trace works for narrow-frame and athletic variations. The body's lean lower body is the strongest natural asset. Strategy choice determines which rules apply.

## 1. Identification

**How users self-identify in Q2:** "My shoulders are the broadest part of my body."

**Confirming signals from Q3 (distribution):**

*Snug zones — diagnostic:*
- Shoulders and/or arms
- Chest
- Waist/stomach (tops cut for proportional bodies pull across the upper body)

*Snug zones — noisy / not diagnostic:*
- Hips/thighs, seat (these can fire for many reasons unrelated to inverted triangle)

*Loose zones — diagnostic:*
- Seat (inverted triangles commonly have flat seats and narrow hips)
- Hips/thighs (the bottom half is narrower than the top, so standard pants gap or sit loose)
- Arms (if lean or athletic-leaning)

*Loose zones — noisy:*
- Waist/stomach (a "loose at waist" answer suggests narrow-frame inverted triangle, not a contradiction)

**Confirming signals from Q4 (fit issues):**

*Fit issues — diagnostic:*
- Feels tight in the chest (top half carries more volume)
- Feels tight in the shoulders or arms
- Tops don't button across the bust or shoulder
- Feels too loose around hips/seat (universal narrow-bottom complaint)
- Bottoms gap at the back waistband (hip narrowness means pants cut for proportional hips don't fill out at the back)
- "Everything usually sits how it should" — possible for lean inverted triangles where overall scale is small enough that proportion mismatch is muted

*Length issues — diagnostic:*
- Pants feel too short / tops feel too cropped → if tall
- Pants feel too long / tops feel too long → if petite
- "Everything usually sits where it should" — common for mid-height inverted triangles around 165–172 cm

**Conflicting or ambiguous signals to watch for:**

- *Snug at seat:* possible for inverted triangles who carry more weight at the bottom despite shoulder dominance. Treat as a real geometric variation. Inverted triangle rules still apply (balance shoulders down, add bottom volume, avoid bust/shoulder emphasis) but the "add visual hip volume" default softens.
- *Loose at waist:* indicates narrow-frame inverted triangle, often lean throughout the body with the shoulder breadth being the only meaningful proportion signal. Don't reclassify as rectangle; the geometric reality is shoulders > hips even if she's slim.
- *Snug at chest with no other signals:* could be fuller bust without shoulder breadth (would suggest hourglass with bust) or could be wider ribcage. If shoulders are explicitly described as broadest, trust that signal and treat as inverted triangle.
- *Snug at arms specifically:* athletic inverted triangle pattern. Shoulders are developed, arms are toned but proportional to shoulders. Surface this as a known variation.

**Distinctions from adjacent body types:**

- *Inverted triangle vs. hourglass:* hourglass has balanced shoulders and hips with a defined waist (25%+ taper). Inverted triangle has broader shoulders than hips with no defined waist.
- *Inverted triangle vs. rectangle:* rectangles have balanced shoulders and hips. Inverted triangles have shoulders distinctly broader than hips. The diagnostic question is whether shoulders are the widest point of the body.
- *Inverted triangle vs. apple:* apples have weight at the midsection with shoulders and hips narrower than the middle. Inverted triangles have weight at the upper body (shoulders/chest) with the midsection narrower than the shoulders.
- *Inverted triangle vs. athletic build:* substantial overlap. Athletic builds with developed shoulders and slim hips are inverted triangles.

## 2. Geometric Truth

**Core proportions:**
- Shoulders are the broadest point of the body, distinctly wider than hips
- Bust often fuller, contributing to upper-body dominance
- Ribcage may also be wider than the lower half
- Waist is undefined or straight — not a sharp taper
- Hips are narrow relative to shoulders
- Seat is typically flat or minimally curved
- Legs tend to be lean and proportionally longer than torso

**Where volume sits:**
- Tendency toward fullness: shoulders, upper back, bust, upper arms (sometimes)
- Tendency toward flatness: seat, hips
- Typically lean: legs, lower body generally
- Midsection: usually straight rather than full

**Length tendencies:**
- Legs proportionally longer than torso (the "swimmer's build" pattern)
- Tall inverted triangles (170+): legs read as a strong visual asset; the shoulder breadth is balanced by overall body length
- Mid inverted triangles (165–169): proportional in standard sizing
- Petite inverted triangles (under 160): shoulder breadth more visually dominant on smaller frame; harder to balance

**Common geometric variations within the type:**

- *Athletic inverted triangle:* visible muscle development in shoulders and arms, contributing to upper-body dominance through muscle rather than weight. Often very lean. Carries structured tailoring beautifully but cap sleeves and structured shoulders amplify what's already there.
- *Bust-forward inverted triangle:* shoulders broad and bust also full. Upper body dominance comes from both width and depth. Open necklines and V-necks balance differently than for athletic types. May unlock bust-as-edge featuring move if user opts in.
- *Narrow-frame inverted triangle:* lean throughout, with shoulders being the only meaningfully wider point. Has the most styling tolerance of the variations. The tall-lean subset (170+, low body fat, often associated with model proportions) sees this tolerance amplified by scale; the V-taper reads as a body signature rather than a proportion problem to solve. Rules apply less aggressively to this variation.
- *Hip-fuller inverted triangle:* shoulders are still broadest but the lower body isn't as narrow as typical. Inverted triangle rules still apply but the "add hip volume" default softens.

## 3. Visual Assets (default, before strategy modulation)

**Natural assets (read well without intervention):**

- *Long, slim legs:* the most reliable inverted triangle asset. Bottom half is naturally lean and proportionally longer than torso. Strong leg-forward potential.
- *Narrow waist (relative to shoulders):* even though the waist isn't defined by taper, it's narrow compared to the shoulder line, which means waist-marking can create dramatic visual narrowing.
- *Décolletage and collarbones:* often a feature for inverted triangles since the upper chest area is prominent without being heavy.
- *Strong shoulders (when desired):* for users who like the strong-shouldered look, this is a natural asset. For users who want to soften, it's a risk to balance.
- *Lean lower body:* hips, thighs, seat all tend to be slim. Bottom-fitting clothes work without hip self-consciousness.
- *Lean ankles:* often paired with the long-leg pattern.

**Features that become assets when used intentionally:**

- *Hips and seat (visually added through clothing):* wider hems, A-line skirts, full pants can create visual hip volume that balances the shoulders.
- *Waist (created through anchor):* a defined waist breaks up the column from shoulder to hip and creates the hourglass illusion. Anchor strategy is the most powerful tool for inverted triangles.
- *Length of leg (extended visually):* high-rise bottoms + leg-revealing cuts can emphasize the leg asset and pull attention down from the shoulders.
- *Bust (when fuller and user opts to feature):* sweetheart, deeper V, surplice necklines turn the bust into a featured asset rather than a proportion problem.

**Override conditions:**

- *Legs not an asset:* if user covers legs in exposure, refuses short lengths, refuses skirts/dresses entirely. Suppress short-length and slit-forward recommendations.
- *Décolletage/chest not an asset:* if user covers chest/neckline in exposure or marks chest as snug. Default open-neckline strategy still applies but bust-emphasis necklines (sweetheart, deep V) should be suppressed.
- *Shoulders should be minimized:* default for most inverted triangles. Surface softening through fabric and cut.
- *Bust not for featuring:* default. Even with fuller bust, treat as a proportion-problem zone unless user explicitly opts into bust-featuring.

**Featuring-zone signals from the questionnaire (cross-body framework):**

- *Legs named:* amplify. Surface short hems, slits, leg-revealing cuts. Inverted triangle's strongest asset confirmed.
- *Décolletage named:* amplify. Surface open V, scoop, asymmetric necklines that show décolletage without crossing into bust dominance.
- *Bust named:* significant unlock. The featuring-zone signal directly provides the bust-as-asset confirmation that the rules previously gated behind combinational detection. Surface sweetheart, deeper V, surplice at exposure-appropriate depth. User is telling the system she wants bust featured rather than minimized.
- *Shoulders named:* significant signal — user wants to feature her natural shoulder line rather than soften it. Reduce shoulder-minimizing defaults and unlock shoulder-featuring access. Default surfaced execution is body-compatible: clean sleeveless, halter (narrow at neck), one-shoulder asymmetric, sharp tailoring with controlled shoulder, narrow-strap tops, open necklines that show shoulder line without amplifying. Style archetype modulates intensity — edgy/dramatic archetype + reveal mode unlocks more aggressive options (off-shoulder, Bardot, statement shoulder); clean/minimal archetype keeps featuring at sophisticated execution. Heavy puff sleeves, dramatic shoulder pads, and stiff boat necks remain filtered unless the user signals dramatic styling explicitly — they amplify without flattering even when shoulders are the featured zone.
- *Arms named:* surface sleeveless and arm-revealing cuts when combined with leg-uncovered preference. Reverses default cap-sleeve filter.
- *Waist named:* confirms anchor direction. Surface anchor items aggressively even if user didn't pick anchor strategy explicitly.
- *Back named:* surface open-back items as alternate focal point (redirects attention from front-facing shoulder breadth).
- *Hips/seat named:* unusual; signals user wants to feature lower body. Surface hip-emphasis cuts; surface featuring through fitted bottoms.
- *"Nothing in particular":* conservative inverted triangle defaults; hero-weighted; rely on behavior data.

## 4. Visual Risks (default, before strategy modulation)

**Silhouettes that fight this body type:**

- *Boxy tops that emphasize shoulder width:* drop-shoulder, boxy crew, oversized sweatshirts that hang straight from the shoulder line. They amplify the broadest point.
- *Closed high necklines on broad shoulders:* combined with shoulder width, closed necklines create a solid wall across the upper body.
- *Detailed or embellished tops:* anything that adds visual interest to the upper body draws attention exactly where the body is already drawing attention.
- *Puff sleeves, leg-of-mutton, dramatic shoulder volume:* adds width to the already-wide shoulder.
- *Structured shoulder pads:* same problem — amplifies the existing structure.
- *Tight column dresses with no waist break:* the lack of waist combined with shoulder dominance creates a body that reads as triangular, not hourglass.
- *Pencil skirts that are too tight at the hip:* emphasize the narrow lower half by clinging to it.
- *Slim/skinny jeans:* don't balance the shoulder-hip proportion mismatch. Not a universal failure — some users prefer them for featuring the lean lower half. Allow by default with low priority; promote when user signals close-to-body bottom preference; filter only when user explicitly rejects skinny.
- *Cropped tops that end at the rib:* extends the visual upper body further.

**Construction details that fail:**

- *Structured shoulder pads*
- *Padded bust details or push-up construction*
- *Horizontal seaming across the chest or shoulders*
- *Embellishment at the bust or neckline*
- *Bows, ruffles, or details at the shoulder or chest*

**Fabric behaviors that fail:**

- *Stiff fabric on top:* doesn't drape over the shoulders softly; the rigidity makes shoulders read sharper and broader
- *Heavy or thick fabric on top:* adds visual bulk where the body is already dominant
- *Clingy fabric on top with full bust:* shows the bust outline and emphasizes upper-body weight
- *Shiny fabric on top alone:* light reflection draws the eye

**Necklines that fail (default):**

- *Boat neck:* extends shoulder horizontally
- *Wide square neck:* squares the already-wide top
- *Off-shoulder, bateau, Sabrina:* present full shoulder breadth without strap interruption (default — overridden when shoulders are named as featured zone)
- *High closed crew on its own:* creates wall across upper body

**Length traps:**

- For tall inverted triangles: standard tops run short and create awkward crop at the rib
- For petite inverted triangles: shoulder breadth is harder to balance because lower-body volume options are more constrained
- For mid-height: usually no length traps unless very specific cuts

**Override conditions:**

- *Boxy tops:* work when worn open over a fitted base, but the boxy outer layer must not have structured shoulders.
- *Detail on top:* works when paired with strong visual interest on the bottom that competes for attention.
- *Statement sleeves:* almost universally fail. Rare exceptions for very narrow-frame users who want to play with proportion.
- *Off-shoulder/Bardot:* defaults to filter, but unlocks when shoulders are named as featured zone (user wants to feature shoulders).
- *Statement-shoulder tailoring:* defaults to filter, but unlocks when shoulders are named.

## 5. Strategy Modulation

### Trace

**What trace means for this body type:**

The riskiest strategy for inverted triangle. Trace honors the body's natural shape — but the inverted triangle's natural shape is exactly the proportion problem the user often wants to balance. A user picking trace-only is signaling either (a) very narrow-frame where the proportion mismatch is muted, (b) athletic body she's proud of and wants to feature, or (c) doesn't know what other strategies offer.

**What works under trace:**

- Open V-neck and scoop tops (skim the body but break the chest vertically)
- Button-downs worn open or partially open
- Mid-to-high rise straight or wide-leg pants (skim the lower body, the rise creates implied waist)
- Fitted A-line or full skirts (skim the waist, flare at the hip to add lower-body volume)
- Wrap tops that follow the body but cinch the waist
- Soft drape blouses in fluid fabric
- Trousers with subtle hip detail (pleats, pockets) that add visual interest at the lower body

**What fails under trace:**

- Tight tops at the shoulder/chest
- Snug button-downs that pull at the bust
- Tight column dresses
- Snug pencil skirts at narrow hips
- Anything that hugs the upper body fully

**Special considerations:**

- Trace-only signals limited strategy options. Recommendations should be carefully selected toward items that follow the body without emphasizing the proportion mismatch. Hero-weighted surfacing applies.

### Anchor

**What anchor means for this body type:**

The strongest strategy for inverted triangle. Anchor creates a defined waist that breaks the column from shoulder to hip and adds visual volume below the waist, which balances the upper body. Anchor engages directly with the proportion problem through silhouette construction.

**Hard vs. soft anchor:**

Both work for inverted triangles, unlike for rectangles. The waist is narrow enough that even soft anchor (drawstring, wrap-tie, gentle gathering) can pull in and create visible definition.

Special exception: belts at the waist work but must be calibrated. A wide belt at the natural waist can shorten the torso visually on inverted triangles whose torso is already proportionally short.

**Specific anchor moves that work:**

- A-line skirts (creates lower-body volume below a defined waist)
- A-line dresses
- Wrap dresses (cinches the narrow waist, often has bias drape on top that softens shoulders)
- Skater dresses (fitted bodice + full skirt, very strong for inverted triangle)
- Fit-and-flare dresses
- Belted shirt dresses with full skirt below
- High-rise wide-leg or flare pants (the waist hits at natural waist, the flare adds lower-body volume)
- Peplum tops (creates artificial hip volume at the natural waist line)
- Drawstring or wrap tops over fitted bottoms

**Anchor moves that fail:**

- Cropped peplum tops that hit at the rib
- Belts at the empire line (under the bust — extends the upper body further)
- Drop-waist styles (drops the visual waist below natural)
- Belts so wide they shorten the torso on petite inverted triangles

### Sculpt

**What sculpt means for this body type:**

Sculpt creates artificial waist and lower-body shape. Effective for inverted triangles when the sculpt construction adds visual hip volume or shapes a defined waist. Sculpt that emphasizes the upper body fails.

**What good sculpt looks like for this body:**

- Fit-and-flare construction with structured bodice and full skirt
- Sculpt midi dresses with A-line or fishtail skirts
- Tailored peplum jackets that hit at the natural waist
- Princess-seamed dresses that bring the eye inward at the waist
- Corseted or boned bodice with skirt volume below

**What bad sculpt looks like:**

- Sculpt with structured shoulders or shoulder pads (amplifies the existing upper-body dominance) — unless shoulders are named as featured zone
- Sculpt that fits closely all the way down with no skirt volume
- Sculpt in heavy fabric that doesn't drape at the shoulders
- Sculpt with detail or embellishment at the bust

**Sculpt-friendly items:**

- Fit-and-flare cocktail and midi dresses
- Tailored peplum blazers in soft (not stiff) fabric
- Bustier-style dresses with full skirts (only when chest exposure is comfortable)
- Sculpt jumpsuits with wide-leg trousers

### Edge

**What edge means for this body type:**

Edge bypasses the body's proportion problem rather than solving it through silhouette engineering. Attention is redirected to specific features or zones so the body's overall shape isn't the dominant visual signal. Unlike anchor (which creates the missing waist) or sculpt (which builds the missing shape), edge leaves the silhouette alone and changes where the eye lands.

**Featuring modes (single-target attention):**

- *Legs:* short hems, slits, leg-revealing cuts. The most accessible default for inverted triangle since legs are typically a natural asset.
- *Bust:* for users with fuller bust who have chest exposure permitted and have signaled bust as an asset to feature (via featuring-zone question), featuring bust through deeper V, sweetheart, or surplice necklines.
- *Décolletage:* open neckline showing collarbones without significant bust emphasis. Works for users with smaller bust who want to feature the upper chest area as elegant rather than dominant.
- *Open back:* redirects attention to the back as alternate focal point, away from front-facing shoulder breadth.
- *Ankle:* cropped pants showing the ankle, statement footwear.

**Attention-redirect modes:**

- *Color blocking with dark on top + light/bright on bottom:* the standard inverted triangle styling move. Outfit-level logic, not item-level.
- *Statement bottoms with plain tops:* printed skirts, patterned pants, embellished bottoms paired with simple tops.
- *Print or detail placement below the waist:* the print itself is the attention-grabber, located in the area that benefits from added visual weight.

**Edge moves that fail:**

- Statement tops with plain bottoms (places attention exactly where the body is already drawing it)
- Bold prints, bright colors, or detail on top alone (without compensation on bottom)
- Embellishments at neckline, shoulders, or bust — unless shoulders or bust are named as featured zones
- Light or bright colors on top with dark on bottom (reverses the desired attention flow)

**Note on edge vs. anchor confusion:**

A-line skirts, fit-and-flare dresses, wrap dresses, peplum, and other items that *create* hip volume or waist definition are anchor moves, not edge. They engage with the proportion problem directly through construction. Edge is reserved for moves that bypass the silhouette question.

## 6. Combinational Rules

**Body + strategy combinations:**

- *Inverted triangle + trace only:* show few, precise items; hero-weighted surfacing. Trace is the most restrictive strategy for this body type.
- *Inverted triangle + anchor:* surface anchor items aggressively; this is the strongest strategy for the body type.
- *Inverted triangle + sculpt:* require sculpt that defines the waist AND adds lower-body volume. Filter sculpt that emphasizes the upper body alone.
- *Inverted triangle + edge:* unlock featuring modes (legs, décolletage primarily; bust, shoulders, back when named as featured zones) and attention-redirect modes.
- *Inverted triangle + multiple strategies:* sophistication signal. Widen the catalog.

**Body + fit combinations:**

- *Inverted triangle + relaxed top + close bottom:* fights anchor strategy's proportion-balancing approach. Works when edge is the strategy and the close bottom is the featured zone, OR when the relaxed top has strong open neckline and the outfit's overall attention flows downward.
- *Inverted triangle + close top + relaxed bottom:* classic inverted triangle balancing setup. Surface aggressively.
- *Inverted triangle + close everywhere:* requires items with strong waist creation (anchor through cut). Also signals skinny/slim bottoms are user-preferred.
- *Inverted triangle + relaxed everywhere:* when anchor is the selected strategy, requires structure in the bottom to provide hip volume. When edge is the selected strategy, features at the lower body (statement skirts, attention-grabbing trousers, color-blocking) substitute for structural hip volume by drawing the eye downward through alternative means. Pure shapeless without compensation or downward attention redirect = failure.

**Body + fabric combinations:**

- *Inverted triangle + cling-averse:* filter out thin jersey, thin viscose, slinky polyester on tops especially.
- *Inverted triangle + heavy-averse:* applies more to tops than bottoms.
- *Inverted triangle + soft drape preferred on top + structured on bottom:* the inverse of rectangle. Fluid drape on top softens shoulders; structured bottom holds the volume that balances the shoulders.

**Body + exposure combinations:**

- *Inverted triangle + legs uncovered:* leg-forward silhouettes weighted high.
- *Inverted triangle + chest covered:* significant constraint. Most softening necklines (V, scoop) become unavailable. Surface high-but-detailed necklines (mandarin, henley, button-up) instead.
- *Inverted triangle + back uncovered + edge:* open-back items become hero.
- *Inverted triangle + shoulders covered:* prefers sleeves and shoulder coverage. Limits asymmetric and one-shoulder options.

**Body + featuring-zone combinations:**

The featuring-zone question is especially valuable for inverted triangle because it resolves the bust-featuring unlock and the shoulders-as-asset signal that the rules previously gated behind multi-combination detection.

- *Legs named:* amplify leg-featuring edge. Inverted triangle's strongest asset.
- *Bust named (any size):* unlocks bust-featuring at exposure-appropriate depth. The featuring-zone signal replaces the previous "fuller bust + chest exposure comfortable + bust signaled as asset" combination. User is telling the system she wants bust featured.
- *Shoulders named:* significant — user wants to feature her natural shoulder line. Reduce shoulder-minimizing defaults and unlock shoulder-featuring access. Default surfaced execution is body-compatible (one-shoulder asymmetric, halter, clean sleeveless, sharp controlled tailoring, narrow-strap tops). Style archetype modulates intensity — edgy/dramatic + reveal mode unlocks off-shoulder, Bardot, statement shoulder; clean/minimal keeps featuring at sophisticated execution. Heavy puff sleeves, dramatic shoulder pads, and stiff boat necks remain filtered unless dramatic styling is explicitly signaled.
- *Décolletage named:* surface open V, scoop, asymmetric necklines as featuring move and relief move simultaneously.
- *Arms named:* surface sleeveless and arm-revealing cuts. Reverses default cap-sleeve filter.
- *Waist named:* confirms anchor direction; surface anchor items aggressively.
- *Back named:* surface open-back items aggressively as alternate focal point.
- *Hips/seat named:* unusual; signals user wants to feature lower body despite the narrow-hip default. Surface hip-emphasis cuts cautiously.
- *"Nothing in particular":* conservative defaults; surface hero items; behavior refinement.

**Body + variation modulators:**

- *Athletic inverted triangle (developed shoulders, lean):* avoid structured shoulders on outerwear entirely unless shoulders are named as featured zone. Soft drape and rounded shoulders on jackets.
- *Bust-forward inverted triangle:* deeper V-necks work to break the upper body; sweetheart works only when bust is named as featured zone. Avoid bust-emphasis details by default.
- *Narrow-frame inverted triangle:* more styling tolerance. The tall-lean subset operates with significantly broader tolerance; the V-taper reads as a body signature rather than proportion problem.
- *Hip-fuller inverted triangle:* suppress "add hip volume" defaults. Surface items that balance through waist creation rather than added volume.

## 7. Hero Categories

**Hero items (consistent across inverted triangle):**

- Wrap dresses (waist cinch + softening drape on shoulders)
- A-line and fit-and-flare dresses (waist + skirt volume)
- Full skirts: A-line, circle, pleated, trumpet (hip volume)
- Wide-leg trousers, palazzo pants (lower-body volume)
- High-rise flared jeans (waist + flare)
- High-rise straight jeans paired with fitted top
- Tank tops with narrow straps (don't extend shoulder line)
- V-neck and scoop neck tops
- Halter tops (for smaller bust universally; for fuller bust with careful selection)
- Open button-downs (vertical break)
- Soft drape blouses
- Cardigans worn open
- Knee-length or shorter A-line dresses with simple tops
- Wide-leg jumpsuits with belt at natural waist

**Hero necklines:**

- V-neck (medium to deep depth) — breaks the chest panel, softens shoulders
- Scoop neck — softens angular shoulders
- Halter — narrow V at the neck creates diagonal lines that draw attention inward and downward; elongates the upper body
- Open button placket — vertical break, calibrated reveal
- Sweetheart (with caution; works when featuring bust is the goal, gated by featuring-zone signal)
- Asymmetric one-shoulder (diagonal break disrupts the wide upper body)
- Mandarin/band collar with vertical button placket (when chest covered)

**Necklines accessible based on featuring-zone signal:**

- *Shoulders named as featured:* off-shoulder, Bardot, wide square, boat neck — all unlock because user wants to feature shoulder line
- *Bust named as featured:* deeper V, sweetheart, surplice, plunging at exposure-appropriate depth

**Necklines to avoid (default):**

- Boat neck (default — overridden when shoulders named)
- Wide square (default — overridden when shoulders named)
- Off-shoulder, bateau, Sabrina (default — overridden when shoulders named)
- High closed crew on its own (creates wall across upper body)

**Hero sleeves:**

- Cap sleeves (caution — work for narrow-frame, fail for athletic or broader)
- Three-quarter or bracelet length
- Bishop sleeves with structured shoulder
- Bell sleeves
- Sleeveless with narrow strap
- Set-in sleeves with soft drape (not structured shoulders)

**Sleeves accessible based on featuring-zone signal:**

- *Shoulders named:* structured shoulders, statement sleeves with shoulder structure
- *Arms named:* sleeveless, fitted short sleeves

**Sleeves to avoid:**

- Puffed sleeves at the shoulder (adds shoulder volume — unless shoulders named)
- Statement shoulders, shoulder pads (amplifies existing structure — unless shoulders named)
- Cap sleeves on athletic or bust-forward types
- Drop-shoulder with no structure (widens the visual shoulder line)

**Hero pant silhouettes:**

- High-rise wide-leg
- High-rise flare
- High-rise palazzo
- Pleated trousers with hip detail
- Bootcut jeans (subtle flare adds ankle interest)
- Wide-leg jumpsuits
- Straight-leg jeans (medium volume option)

**Pants with user-specific gating:**

- Slim/skinny jeans: not in default hero set; promote when user signals close-to-body bottom preference; allow at low priority by default; filter only on explicit rejection.

**Hero dress and skirt silhouettes:**

- Wrap dresses
- Skater dresses
- Fit-and-flare dresses
- A-line midi or knee-length dresses
- Full circle skirts
- A-line midi skirts
- Pleated midi skirts
- Trumpet/mermaid skirts (the flare at knee adds lower-body volume)

**Hero outerwear:**

- Trench coats with belted waist (creates waist, adds lower-body volume through flared skirt of coat)
- Wrap coats with structured waist
- Open cardigans without structured shoulders
- Knee-length A-line coats
- Soft drape blazers (worn open, with subtle shoulder construction not heavy)
- Peplum jackets in soft fabric
- Single-breasted styles (double-breasted adds upper body volume)

**Hero items by strategy:**

- *Trace hero:* open V-neck top + high-rise wide-leg pant; soft drape blouse + A-line skirt
- *Anchor hero:* wrap dress in soft fabric; fit-and-flare dress with full skirt; peplum top + slim trouser
- *Sculpt hero:* fit-and-flare cocktail dress with structured bodice + full skirt; sculpt jumpsuit with wide-leg
- *Edge hero:* short A-line dress with plain neckline (legs feature); halter top + simple wide-leg (décolletage feature); statement printed bottom + plain top (attention redirect)

## 8. Disqualified Categories

**Items that don't work, regardless of strategy (with featuring-zone overrides noted):**

- Structured shoulder pads (default — overridden when shoulders named)
- Puff sleeves and dramatic sleeve volume at the shoulder (default — overridden when shoulders named)
- Padded or push-up bust
- Off-shoulder, bateau, Sabrina necklines (default — overridden when shoulders named)
- Boat necks (default — overridden when shoulders named)
- Wide square necklines on tops (default — overridden when shoulders named)
- Tight column dresses
- Statement collars and embellished necklines
- Bold prints or detail on tops without compensation on bottom
- Drop-waist dresses (extends upper body, shortens leg)
- Empire-line tops or dresses that emphasize the upper body
- Bandeau and strapless tops as default (with override when bust is being featured intentionally and shoulders are comfortable for the user)
- Mermaid skirts that are tight to the knee then flare

**Items disqualified by specific answer combinations:**

- Short skirts and dresses disqualified for: inverted triangle + legs covered
- Wide-leg pants disqualified for: inverted triangle + very narrow-frame + close fit preference
- Backless items disqualified for: inverted triangle + back covered
- Sleeveless items disqualified for: inverted triangle + arms covered
- Sweetheart and deep-V disqualified for: inverted triangle + chest covered or bust not named as featured zone

**Items disqualified by featuring-mode signals:**

- Reveal-mode shoulder items (off-shoulder, strapless) disqualified for: shoulders in coverage mode
- Reveal-mode chest items (deep V, plunging) disqualified for: chest in coverage mode + bust not named

**Items that look right but disappoint:**

- *Crew-neck T-shirts on inverted triangle:* mainstream basics, look fine on the hanger, but the closed neckline + fitted ribcage on a broad upper body reads as boxy. Surface V-necks and scoop necks instead.
- *Boxy crewneck sweaters:* "oversized" item that fails on inverted triangle through both fronts — closed neck and shoulder breadth amplified.
- *Pencil skirts in stretchy fabric:* market themselves as universally flattering, but on inverted triangles the tight skirt on narrow hips emphasizes the proportion mismatch.
- *Tank tops with wide straps or wide armholes:* even sleeveless can fail if the strap extends the shoulder line or exposes the full shoulder breadth without compensation.

## 9. The Uniform

**Daytime / casual uniform (mid-height, mid-sophistication, mixed strategy):**

A pair of high-rise wide-leg or straight-leg pants in mid or dark wash denim, or a tailored trouser in neutral fabric, sitting at the natural waist with a clean break into the leg. Length is full or near-full.

On top, a fitted V-neck or scoop neck tank or knit, ending at the high hip. The neckline is open to break the chest panel; the fit is close to skim the body without bulk. If layering, a soft drape blouse or open button-down worn unbuttoned, sleeves rolled. The layer is in fluid fabric without structured shoulders.

Optionally, a soft drape blazer or open cardigan as a third layer, worn open to create a vertical line down the front.

Footwear: low-profile or with a heel that extends the leg. Pointed flats, ankle boots, simple sandals.

**Variations by strategy:**

- *Trace-primary inverted triangle:* swap to fitted button-down (worn slightly open) with straight-leg trouser. Less proportion play, more careful body skimming.
- *Anchor-primary inverted triangle:* lead with wrap top + flared skirt, or fit-and-flare dress as a single piece.
- *Sculpt-primary inverted triangle:* swap separates for a fit-and-flare dress with structured bodice and full skirt.
- *Edge-primary inverted triangle:* short A-line dress for casual; halter top + wide-leg for evening-leaning casual; statement-printed bottom + plain top for color play.

**Variations by register:**

- *Work:* swap to tailored trousers in wool or substantial cotton, fitted V-neck knit or button-down worn open over a base layer, soft-shoulder blazer.
- *Evening:* fit-and-flare dresses, wrap dresses, halter dresses (especially with full skirt below), fluid drape gowns with defined waist.
- *Occasion:* full A-line dresses, fit-and-flare midi, wrap dresses.

**Variations by season:**

- *Summer:* wide-leg cotton or linen trousers, V-neck tanks, halter tops, sleeveless wrap dresses, A-line short skirts, fit-and-flare sundresses, soft drape sleeveless blouses, soft sandals.
- *Winter:* wide-leg wool trousers, fine knit V-necks tucked in, soft drape cashmere, trench or wrap coats with belt, knee-length A-line wool coats, knee-high boots paired with skirts.

## 10. Inference Notes for the Recommender

**Default rules that fire on inverted triangle identification alone:**

1. Lower-body volume is a goal; surface items that add visual hip volume (A-line, full, flared, wide-leg).
2. Upper-body softening is a goal; filter or downrank structured shoulders, shoulder pads, puff sleeves *unless shoulders named as featured zone*.
3. Waist creation is a primary tool; surface anchor items.
4. Legs are an asset by default; short lengths and slits available.
5. Open necklines are a default relief move; surface V, scoop, halter, asymmetric, open button placket. Filter boat neck, wide square, off-shoulder/bateau/Sabrina *unless shoulders named*.
6. Closed crew necks on tops downweighted.
7. Bulk on top is a risk; thin fluid drape preferred over thick structured fabric.
8. Bulk on bottom is welcome; structured A-line, full skirts, wide-leg pants are heroes.
9. Soft fabric on top, structured on bottom is the default fabric preference (inverse of rectangle).
10. Bottom-up attention is the goal; surface items that draw the eye to legs, waist, or lower body.
11. Sleeves vary by strategy and body variation: cap sleeves work for narrow-frame, fail for athletic and bust-forward (unless featuring-zone signal overrides); bishop and bell sleeves work universally.
12. Athletic variation modifies sleeve and shoulder defaults significantly.
13. Standard pant lengths may run wrong at height extremes; surface tall and petite cuts where available.
14. Petite + inverted triangle: shoulder breadth is harder to balance on smaller frame.
15. Bust-as-edge featuring directly signaled by featuring-zone question (replaces previous combinational detection).
16. Shoulders-as-asset directly signaled by featuring-zone question (reverses default shoulder-softening rules for that user).

**Modulators that change defaults:**

- *Strategy selection:* anchor strongly preferred and weighted up; sculpt requires waist + lower volume; edge unlocks featuring and attention-redirect modes; trace requires hero-weighted surfacing.
- *Fit preferences:* close top + relaxed bottom is the natural inverted triangle setup for anchor and sculpt strategies. Relaxed top + close bottom fights anchor strategy but can work for edge when the close bottom is the featured zone. Close-everywhere preference flags skinny/slim bottoms as user-preferred.
- *Fabric importance:* high importance + structured items → strict construction filter; high importance + soft drape → quality drape filter.
- *Exposure modulates asset access:* chest covered constrains necklines significantly; arms covered limits sleeveless options; legs covered removes the primary balancing asset.
- *Featuring-zone signal:* primary modulator alongside strategy and fit. Named bust unlocks bust-featuring; named shoulders unlocks shoulder-featuring (reverses defaults); named legs amplifies leg-featuring.
- *Per-zone reveal mode (reveal/sophisticated/cover):* detected through combination of featuring-zone naming, exposure preferences, and length preferences. Default to sophisticated when signals are ambiguous.

**Sophistication and restrictiveness signals:**

- Multi-strategy + flexible answers → widen catalog
- Trace-only + multiple covered zones + petite → tighten catalog, hero-weight, fewer items higher quality
- Multiple zones named → confident multi-strategy dresser; widen catalog

**Risk-scanning patterns common to inverted triangle:**

- How tops sit at the shoulder (does fabric pull or pucker, do button-downs gap at the chest)
- Whether a sleeve adds shoulder width through cut or padding
- Whether a top's volume sits at the bust or the hip (latter is better)
- Whether bottoms have enough volume to balance the top
- How pants fit at the waist when they fit at the hip (universal narrow-hip complaint)

**Common "knows the trick" non-traditional moves:**

- Sophisticated inverted triangles may wear strong horizontal interest at the hip (cargo pockets, hip detail, dropped yoke) as deliberate hip-volume creation.
- May wear long full skirts as a fashion-forward balancing move when most users wear pants.
- May use color blocking with dark on top, bright on bottom to redirect attention downward.
- May feature bust intentionally with sweetheart or surplice cuts when bust is the preferred feature rather than the proportion problem.
- May feature shoulders aggressively when she likes her natural shoulder line — structured tailoring, off-shoulder, halter — and the rules respect this through the featuring-zone signal.

**On rule restrictiveness vs. user variation:**

Inverted triangle rules optimize for the realistic majority population — users who come to styling seeking balance for the shoulder-hip mismatch. Model-type inverted triangles (Naomi Campbell, Jessica Alba, Cindy Crawford, Halle Berry — tall, lean, V-taper reads as body signature) operate outside the median rules. The narrow-frame variation captures part of this; the rules apply less aggressively for very lean tall users. These variation users find items through search and behavior; the system stays out of their way.

## 11. Open Questions and Edge Cases

**Cases the rules don't yet handle:**

- *Inverted triangle + apple borderline:* user with shoulder breadth and midsection width. Both rule sets fire partially; need to determine which dominates.
- *Inverted triangle + hourglass with broad shoulders:* user with defined waist AND broad shoulders. Hourglass rules mostly apply (honor the natural shape) but with caution about emphasizing shoulders further (unless shoulders named as featured zone).
- *Inverted triangle with heavy bust:* when chest is the more dominant feature than shoulder width. May need separate bust-focused rule set.
- *Inverted triangle who loves her shoulders:* now resolved through featuring-zone signal; surface shoulder-feature items.

**Borderline body-type identifications:**

- *Inverted triangle vs. rectangle with broad shoulders:* if shoulders are 1-3% wider than hips, treat as rectangle. If 5%+ wider, treat as inverted triangle.
- *Athletic build vs. inverted triangle:* essentially the same body type for styling purposes.
- *Pear with strong shoulders:* if hips are broader than shoulders but shoulders are still developed, treat as pear.

**Things behavior data should resolve:**

- Mode preferences for each named featuring zone (reveal vs. sophisticated vs. cover)
- Color preferences (dark on top vs. bottom is a common inverted triangle move; learn whether individual users do this)
- Specific brand affinities (some brands cut tops with more shoulder room)
- Tolerance for hip-volume intensity (some users want subtle A-line; others want dramatic full skirt)
- Sleeve volume tolerance (bishop and bell are heroes but volume varies)
- Skinny jeans preference (default low priority, but learn whether individual users prefer them)
- Whether named features actually drive behavior (some users name features they like in principle but don't actually shop for; learn from purchases and saves)


---

# Body Type: Hourglass

**TL;DR:** Hourglass has a real waist; anchor and trace are both strong because the body has its own structure. The job is to honor the curves, not fight them or amplify them artificially. Bust depth and hip emphasis depend heavily on the featuring-zone signal.

## 1. Identification

**How users self-identify in Q2:** "My bust and hips are about the same width, with a clearly defined waist."

**Confirming signals from Q3 (distribution):**

*Snug zones — diagnostic:*
- Chest/bust AND hips/thighs together (the universal hourglass signal)
- Seat (hourglass typically has projected seat)
- Bust alone with explicit defined-waist signal

*Snug zones — noisy / not diagnostic:*
- Arms (hourglass sometimes carries upper-arm volume but isn't diagnostic alone)
- Waist (if reported, may indicate hourglass + midsection-prone variation)

*Loose zones — diagnostic:*
- Waist (the defining hourglass signal — narrower than both bust and hips)

*Loose zones — noisy:*
- Shoulders (some hourglasses have narrower shoulders, which can lean toward pear; check whether bust width matches hip width)
- Arms (lean hourglass — possible but doesn't override the bust + hip + waist signal)

**Confirming signals from Q4 (fit issues):**

*Fit issues — diagnostic:*
- Buying tops one size up for bust → loose at the waist
- Buying bottoms one size up for hips → loose at the waist
- Dresses fit bust and hips but balloon at the waist
- "I always need tailoring at the waist" — strong hourglass signal
- Pants gap at the back waistband (curvy proportional fit issue — defined waist relative to fuller seat)

*Length issues — diagnostic:*
- Pants feel too short → if tall
- Pants feel too long → if petite
- "Everything usually sits where it should" — common for mid-height hourglass with brand familiarity

**Conflicting or ambiguous signals to watch for:**

- *Snug at waist:* contradicts pure hourglass. Possibilities: (a) hourglass + midsection-prone variation (post-pregnancy, post-menopause, soft midsection at high weight); (b) misclassification — actually apple if waist is the widest point.
- *Loose at hips when bust is snug:* possibly top hourglass leaning inverted triangle or bust-forward variation. Check whether seat is also loose; if so, lean inverted triangle.
- *Loose at bust when hips are snug:* possibly bottom hourglass leaning pear. Check magnitude of difference; if hips are 10%+ wider than bust, treat as pear.
- *"Defined waist" reported but not narrow:* user perception varies. If she reports defined waist but Q3 doesn't confirm narrower waist than bust/hips, may be rectangle with stronger body awareness. Check fit issues — true hourglass has the buying-up-for-bust-then-loose-at-waist pattern.

**Distinctions from adjacent body types:**

- *Hourglass vs. rectangle:* hourglass has 25%+ waist taper from bust/hips. Rectangle doesn't. The fit-issue diagnostic is reliable.
- *Hourglass vs. pear:* hourglass has bust and hips balanced. Pear has hips significantly wider than bust (10%+). If she reports both as snug AND the magnitudes feel similar, hourglass. If hips dominate, pear.
- *Hourglass vs. inverted triangle:* inverted triangle has shoulders broader than hips. Hourglass has shoulders proportional to hips. If shoulders are wider than hips with a defined waist, that's still inverted triangle with a waist (rare but real); apply inverted triangle rules with hourglass-style anchor.
- *Hourglass vs. apple:* apple has waist as widest point. Hourglass has waist as narrowest point. Direct opposite signals.

## 2. Geometric Truth

**Core proportions:**
- Bust and hips approximately equal width (within 5%)
- Waist significantly narrower (25%+) than bust and hips
- Defined taper at the natural waist
- Seat typically projected (not flat)
- Shoulders typically aligned with hips, sometimes slightly narrower

**Where volume sits:**
- Tendency toward fullness: bust, hips/thighs, seat
- Tendency toward narrowness: waist
- Variable: shoulders (often proportional), arms (variable)

**Length tendencies:**
- Variable across heights; no consistent torso/leg ratio specific to hourglass
- Tall hourglass (170+): standard cuts may run short on tops and pants
- Mid hourglass (165–169): proportional in standard sizing
- Petite hourglass (under 160): standard cuts may run long; curves at smaller scale

**Common geometric variations within the type:**

- *Lean hourglass:* lower overall weight, smaller curves but the proportion holds. Most styling tolerance.
- *Soft/fleshy hourglass:* fuller curves, sometimes with soft midsection. Stretch fabrics matter; curvy-fit cuts essential.
- *Full-bust hourglass:* bust is significantly fuller. Bra fit and bust support become critical. Necklines need calibration to avoid bust-dominance.
- *Athletic hourglass:* muscular curves rather than soft. Holds shape without fabric assistance. Often paired with broader shoulders.
- *Top hourglass:* bust slightly fuller than hips while still maintaining defined waist. Leans toward inverted triangle on top.
- *Bottom hourglass:* hips slightly fuller than bust while still maintaining defined waist. Leans toward pear on bottom.
- *Hourglass + midsection-prone:* defined waist but softer at midsection (post-pregnancy, post-menopause). Sculpt becomes more valuable; structural support important.
- *Petite hourglass:* same proportions at smaller scale. Standard items often run long; short jackets at waist work; cautious with midi.

## 3. Visual Assets (default, before strategy modulation)

**Natural assets (read well without intervention):**

- *Defined waist:* the central asset. The body's natural taper is what anchor and trace work with.
- *Curves at bust and hips:* often the body's defining features. Items that follow these curves (trace) work directly with the body.
- *Décolletage and collarbones:* often a feature, particularly for fuller-bust hourglasses where the upper chest area sits above the bust.
- *Seat shape:* projected seat is an asset for users who want lower-body emphasis; can be featured through fit-following bottoms.
- *Proportional shoulders:* allow most necklines to work without amplification or softening concerns.

**Features that become assets when used intentionally:**

- *Bust featuring:* hourglass can carry deeper necklines, sweetheart, surplice when user wants bust as featured zone. Calibrated by bust size and exposure.
- *Hip emphasis (opt-in):* hourglass can wear low-rise, hip-detail cuts, bodycon for users who want to feature the lower-body curve rather than just honor it.
- *Waist emphasis through belt or fit:* the waist asset can be made dramatic through anchor moves.

**Override conditions:**

- *Curves not for celebrating:* some hourglasses prefer to dress in ways that minimize curves (professional contexts, personal preference). Surface structured fits over body-skimming; surface vertical line emphasis; surface non-bodycon options.
- *Bust not for featuring:* default for full-bust hourglass at low exposure. Suppress deeper necklines; surface higher-but-detailed options.
- *Hips not for featuring:* default for hourglass who wants to honor the body without emphasizing the lower half. Surface skim-fit bottoms rather than follow-the-curve.

**Featuring-zone signals from the questionnaire (cross-body framework):**

The featuring-zone question is especially valuable for hourglass because it resolves the bust depth ambiguity that the rules previously gated behind a follow-up question.

- *Waist named:* amplify. Surface waist-emphasis items aggressively (anchor, fitted bodice, belt, wrap). Already default for hourglass; named preference confirms.
- *Bust named:* significant. Directly resolves the bust depth ambiguity. Surface bust-featuring items at exposure-appropriate depth (reveal/sophisticated/cover mode). Eliminates the need for separate follow-up question.
- *Hips named:* unlocks hip emphasis. Surface low-rise, bodycon, pencil skirts that follow the curve, hip-detail items. Confirms celebrate-mode preference.
- *Seat named:* unlocks seat-featuring. Surface fitted bottoms that show seat shape, jeans with prominent back pockets, bodycon dresses.
- *Legs named:* unlock leg-featuring (short hems, slits, fitted bottoms showing leg line).
- *Décolletage named:* amplify. Surface open V, scoop, sweetheart at appropriate depth.
- *Shoulders named:* unusual for hourglass; surface structured-shoulder pieces despite hourglass default of soft shoulders.
- *Arms named:* surface sleeveless and arm-revealing cuts.
- *Back named:* surface back-detail items (less common as a featuring zone for hourglass but accessible).
- *"Nothing in particular":* conservative hourglass defaults; rely on body-type asset detection; behavior data refines.

## 4. Visual Risks (default, before strategy modulation)

**Silhouettes that fight this body type:**

- *Shapeless oversized items:* hide the body's natural taper; the curves provide the structure the outfit needs, and hiding them creates a tent silhouette.
- *Straight-cut column dresses:* eliminate the waist asset; the body's defining feature is lost.
- *Drop-waist dresses:* same problem; drop the visual waist below natural, eliminating taper.
- *Boxy oversized tops without anchor:* shapeless on top with curves underneath reads as hidden body, not styled body.
- *Heavy stiff fabrics that don't drape:* stand away from the curves and create bulk where the body has natural shape.
- *High empire-waist tops with no bust support:* cinch above the bust on full-bust hourglass and create odd proportion.
- *Tight clingy fabric in cheap stretch:* shows every contour and reveals bra/underwear lines without elevating the silhouette.

**Construction details that fail:**

- *Drop yoke at the hip:* adds horizontal break at the wrong line.
- *Heavy gathering at the waist on cheap fabric:* creates bulk rather than emphasizing taper.
- *Princess seams set too wide:* miss the actual curve and create a column rather than waist.

**Fabric behaviors that fail:**

- *Stiff fabrics that don't follow the curve:* heavy unforgiving wools, stiff cottons that stand away from the body.
- *Thin clingy synthetic fabrics:* show contours without supporting the silhouette.
- *Heavy bulky knits across the torso:* hide the waist asset and add visual width.

**Necklines that fail (default for full-bust hourglass):**

- High closed crew or mock without compensation (creates wall across upper body, emphasizes bust as solid panel).
- Boat necks on full-bust hourglass (broaden upper body unnecessarily).

**Length traps:**

- For petite hourglass: midi hems often hit at calf-widest; maxi can swallow the proportions; mini may read disproportionate without modulation.
- For tall hourglass: standard cuts may run short; longer items work well.
- For mid-height: usually no length traps.

**Override conditions:**

- *Bodycon, low-rise, hip-detail items:* hero items in celebrate-curves mode (user names hips/seat as featured zones).
- *High closed necklines:* work when paired with vertical line break (button placket, layered jewelry) or for smaller-bust hourglass.
- *Empire waist:* works for slim hourglass without midsection-prone signal.

## 5. Strategy Modulation

### Trace

**What trace means for this body type:**

The most natural strategy for hourglass. Trace honors the body's defined curves directly — the body has shape, and trace lets the clothing follow that shape. Trace produces the strongest silhouette read for hourglass with minimal styling intervention.

**What works under trace:**

- Fitted dresses in skim-fit fabric
- Sheath dresses cut for curvy proportions
- Fitted button-downs in stretch fabric or curvy fit
- Wrap dresses that follow the body
- Bodycon dresses (when user wants celebrate mode)
- Fitted knit tops tucked in
- Curvy-fit jeans (high-rise, fits at waist + seat + thigh)
- Pencil skirts that follow the hip

**What fails under trace:**

- Standard cuts not designed for curvy proportions (gap at waist when fitted at bust/hips)
- Stiff fabric that doesn't follow the curve
- Thin clingy fabric in cheap stretch (reveals contours without supporting)

**Special considerations:**

- Curvy-fit availability is the biggest factor for trace success on hourglass. Same logic as pear — brands that cut for curves make trace possible; standard cuts often fail through waist gap.
- Trace works for both honor-mode and celebrate-mode hourglass; the items follow the body either way, and the user's other styling choices determine direction.

### Anchor

**What anchor means for this body type:**

Universal hero strategy. The body has a real waist; anchor emphasizes it. Almost any anchor mechanism succeeds because there's real waist underneath. Anchor is particularly valuable for hourglass users who prefer relaxed-fit clothing — it preserves waist visibility despite loose fabric elsewhere.

**Hard vs. soft anchor:**

Both work because the waist exists. Hard anchor (real construction, structured belt) and soft anchor (drawstring, wrap-tie) both create visible waist definition because the waist is there to anchor to.

**Specific anchor moves that work:**

- Wrap dresses (universal hourglass hero)
- Belted dresses at natural waist
- Belted shirt dresses
- Tucked-in tops at natural waist (waist meeting point exposes the asset)
- High-rise bottoms with fitted top tucked in
- Wrap tops (fitted or relaxed)
- Dresses with built-in waist seams at natural waist
- Statement belts over relaxed tops
- Belted blazers and coats
- Fit-and-flare dresses
- Princess-seamed dresses with waist taper at natural waist

**Anchor moves that fail:**

- Drop-waist (drops the visual waist below natural)
- Empire-waist (raises the visual waist above natural, eliminates the taper)
- Hip belts (defeats waist emphasis)
- Cinches at wrong position

**Special considerations:**

- Anchor is mode-neutral for hourglass. In honor mode, anchor + skim-fit body creates the classic "tiny waist, body honored" pattern. In celebrate mode, anchor + body-following bottoms creates the "tiny waist + dramatic curves" pattern.

### Sculpt

**What sculpt means for this body type:**

Less critical for hourglass than for rectangle because the body has shape already. Sculpt becomes valuable when honoring the body isn't enough — formal occasions, structured looks, midsection-prone variation. Sculpt for hourglass should follow the existing curves rather than impose new shape.

**What good sculpt looks like for this body:**

- Fit-and-flare dresses with structured bodice + full skirt
- Tailored sheath dresses with princess seams
- Corseted bodice with skirt (evening)
- Structured fit-and-flare coats
- Peplum jackets that hit at natural waist (peplum is sculpt for hourglass — it creates shape that may not match the body for other types but follows hourglass curves)

**What bad sculpt looks like:**

- Sculpt that imposes a different waist position than the user's natural waist
- Sculpt with heavy shoulder pads (amplifies upper body unnecessarily)
- Sculpt in stiff fabric that fights the body's curves

**Special considerations:**

- Peplum is sculpt for hourglass, not anchor. The peplum creates a shape (flare at hip) that emphasizes the existing waist. Works when the peplum hem doesn't hit at hip-widest.
- Midsection-prone hourglass benefits from sculpt structural support; surface structured bodices, princess seams, fit-and-flare with built-in shaping.

### Edge

**What edge means for this body type:**

Hourglass edge typically features the natural assets — waist, bust, décolletage, curves. Less about redirecting attention away from problems (because hourglass doesn't have geometric problems to redirect from) and more about choosing which asset to feature.

**Featuring modes:**

- *Waist features:* statement belts, color-blocked waist, fitted-waist construction with contrasting fabric above and below. Already the default for hourglass.
- *Décolletage and bust features (mode-dependent):* in honor mode, moderate open necklines (V at collarbone, scoop at clavicle). In celebrate mode for users who name bust, deeper V, sweetheart, plunging. Calibrated by bust size and exposure.
- *Hip and seat features (opt-in):* low-rise, bodycon, pencil skirts following the curve. Surfaced when user names hips/seat.
- *Leg features:* short hems, slits, fitted bottoms showing leg line. Surfaced when user names legs.

**Edge moves that work:**

- Statement belts over wrap dresses (waist + accessory feature)
- V-neck + tucked-in fitted top (décolletage + waist)
- Sweetheart bodice on fit-and-flare (bust + waist feature combined — gated by bust named)
- Bodycon dress with statement neckline (curves + neckline feature — celebrate mode)
- Pencil skirt + fitted top + belt (hip + waist feature — celebrate mode)

**Edge moves that fail:**

- Edge moves that hide the waist (the body's central asset)
- Statement features at upper body alone that compete with natural curves
- Heavy embellishment that distracts from the natural shape

## 6. Combinational Rules

**Body + strategy combinations:**

- *Hourglass + trace:* surface curvy-fit trace items. Works for both honor and celebrate modes; items follow the body either way.
- *Hourglass + anchor:* universal hero strategy; surface aggressively. Particularly important for relaxed-fit hourglass users (preserves waist visibility despite loose fabric).
- *Hourglass + sculpt:* surface fit-and-flare, structured bodices, peplum at natural waist. Less critical than for rectangle but valuable for evening and midsection-prone variation.
- *Hourglass + edge:* feature waist (default), décolletage (with bust calibration), hips (opt-in via featuring-zone), legs (opt-in via featuring-zone).
- *Hourglass + trace only:* the simplest hourglass uniform; works well because body has shape.
- *Hourglass + multiple strategies:* widen catalog; sophisticated hourglass dressers can use all strategies.

**Body + fit combinations:**

- *Hourglass + close everywhere:* the celebrate-curves uniform. Bodycon, fitted top + pencil skirt, fitted everything. Works for hourglass who wants to feature curves.
- *Hourglass + close top + relaxed bottom:* fitted bodice + A-line or full skirt. Honor mode with skirt drape over hip curve.
- *Hourglass + relaxed top + close bottom:* less common; works when relaxed top is belted or tucked.
- *Hourglass + relaxed everywhere:* when anchor is the selected strategy, requires anchor compensation (belt, tuck, wrap). When edge is the selected strategy with strong feature signals, the body's natural waist visibility is itself the anchor — items that don't engage with the waist but feature other zones (statement neckline + slits + asymmetric detail) can work without explicit anchor mechanism. The natural waist is always there to be revealed when the user wants it revealed; she doesn't need an item to create it. Pure shapeless without any compensation or featuring = failure regardless of strategy. The failure mode is items that hide the body without giving the eye anywhere else to go.

**Body + fabric combinations:**

- *Lean hourglass + broad fabric tolerance:* most fabrics work.
- *Soft/fleshy hourglass + stretch importance:* curvy-fit and stretch fabrics weighted up.
- *Athletic hourglass + structure preference:* structured stretch (ponte) follows muscle definition.
- *Hourglass + cling-averse:* filter thin clingy fabrics; surface skim-fit drape with body.

**Body + bust + exposure combinations:**

The featuring-zone signal resolves the bust depth ambiguity that the rules previously gated behind a follow-up question:

- *Hourglass + names bust + high exposure preference:* deep V, plunging, low sweetheart available. Reveal mode unlocked.
- *Hourglass + names bust + medium exposure + chest not flagged covered:* moderate-depth open necklines (V at collarbone-to-mid-chest, scoop at clavicle). Sophisticated mode default.
- *Hourglass + names bust + medium exposure + chest flagged covered:* moderate open necklines at shallower depth (V ending above bust, scoop at collarbone). Coverage mode for bust featuring.
- *Hourglass + names bust + low exposure:* higher slim necklines with detail or vertical break. Featuring through structure rather than skin.
- *Hourglass + doesn't name bust + medium exposure:* default to body-type appropriate but conservative necklines (V at collarbone, scoop at clavicle).
- *Hourglass + doesn't name bust + chest covered:* high-but-slim necklines; vertical break through button placket or layered jewelry.

**Body + featuring-zone combinations:**

- *Waist named:* confirms anchor direction; surface waist-emphasis items aggressively (already default).
- *Bust named:* resolves depth ambiguity (see above).
- *Hips named:* unlocks hip emphasis; surface low-rise, bodycon, hip-detail items. Celebrate mode for lower body.
- *Seat named:* unlocks seat-featuring; surface fitted bottoms, jeans with back-pocket detail, bodycon dresses.
- *Legs named:* unlock leg-featuring; short hems, slits, fitted leg-line bottoms.
- *Décolletage named:* surface open necklines as featuring move.
- *Shoulders named:* unusual; surface structured-shoulder pieces despite hourglass default of soft shoulders.
- *Arms named:* surface sleeveless and arm-revealing.
- *Back named:* surface back-detail items.
- *Multiple zones named:* sophistication signal; widen catalog.
- *"Nothing in particular":* conservative defaults; hero-weighted; behavior refinement.

**Body + variation modulators:**

- *Lean hourglass:* most cuts work; broader styling tolerance.
- *Soft/fleshy hourglass:* stretch and curvy-fit critical; ponte and structured stretch heroes.
- *Full-bust hourglass:* bust support critical; neckline calibration by exposure; high closed necklines filtered.
- *Athletic hourglass:* structured stretch follows muscle; cautious with very loose drape.
- *Top hourglass:* apply inverted triangle modulators on top (softening) while preserving hourglass anchor moves.
- *Bottom hourglass:* apply pear modulators on bottom (curvy fit, skim hips) while preserving hourglass anchor moves.
- *Midsection-prone hourglass:* sculpt structural support critical; surface fit-and-flare with built-in shaping; filter clingy at midsection.
- *Petite hourglass:* short jackets at waist; cautious with midi unless slit or with break; standard items often run long.

## 7. Hero Categories

**Hero items (consistent across hourglass):**

- Wrap dresses (universal hourglass hero)
- Fit-and-flare dresses
- Sheath dresses in curvy fit
- Belted shirt dresses
- Pencil skirts (especially with tucked fitted top)
- High-rise curvy-fit jeans
- Tucked fitted tops
- Wrap tops
- Belted blazers and coats
- Trench coats with real belt at natural waist
- Princess-seamed dresses and coats
- Fitted button-downs in stretch fabric (curvy fit)
- Cropped jackets ending at natural waist
- Statement belts over relaxed tops

**Hero necklines:**

- V-neck at varied depths (calibrated by bust + exposure + featuring-zone signal)
- Scoop neck
- Sweetheart (gated by bust named as featured + appropriate exposure)
- Wrap/surplice
- Soft crew neck on smaller-bust hourglass
- Boat neck (for users who don't have full bust)

**Necklines to avoid (default for full-bust hourglass):**

- High closed crew without compensation
- Boat necks (broaden upper body)
- Heavy embellishment at the bust line

**Hero sleeves:**

- Fitted long sleeves
- Three-quarter sleeves
- Fitted short sleeves
- Set-in sleeves with subtle shoulder
- Cap sleeves (for users without full upper-arm volume)

**Sleeves to avoid:**

- Heavy structured shoulders (unnecessary; body has shape)
- Drop-shoulder dolman (extends shoulder without intention)
- Snug tight sleeves on full-arm hourglass

**Hero pant silhouettes:**

- High-rise curvy-fit straight
- High-rise curvy-fit bootcut
- High-rise curvy-fit flare
- Tapered curvy-fit trousers
- Wide-leg in fluid fabric with curvy waist fit

**Pants with mode-specific gating:**

- Skinny and bodycon-fit jeans: hero in celebrate mode; available in honor mode but not weighted up
- Low-rise: gated by hip-featuring signal

**Pants to avoid:**

- Standard-cut bottoms (gap at waist when fitted at hip/seat)
- Mom jeans with very loose hip (waist gap problem)
- Drop-yoke construction at hip

**Hero dress and skirt silhouettes:**

- Wrap dresses
- Fit-and-flare dresses
- Sheath dresses (curvy fit)
- Belted shirt dresses
- A-line dresses (when waist is defined through belt or seam)
- Pencil skirts
- High-rise A-line skirts
- Mermaid skirts (celebrate mode for users who name hips/seat)

**Hero outerwear:**

- Belted trench coats
- Belted wrap coats
- Princess-seamed coats
- Tailored blazers ending at waist or with strong waist shaping
- Cropped jackets ending at natural waist
- Belted blazers

**Outerwear to avoid:**

- Boxy oversized coats without belt
- Long coats with no waist shaping
- Bulky cocoon coats without structural break

**Hero items by strategy:**

- *Trace hero:* curvy-fit straight jeans + fitted ribbed knit; sheath dress; pencil skirt + fitted top
- *Anchor hero:* wrap dress; belted shirt dress; tucked fitted top + high-rise bottom
- *Sculpt hero:* fit-and-flare with structured bodice; peplum top + slim bottom; princess-seamed dress
- *Edge hero:* statement belt over relaxed top; deep V + tucked top + statement belt; bodycon (celebrate mode)

## 8. Disqualified Categories

**Items that don't work, regardless of strategy:**

- Shapeless tunic tops hanging from shoulder to mid-thigh
- Drop-waist dresses
- Empire-waist tops or dresses (unless slim hourglass + bust featuring)
- Boxy oversized blazers without belt or waist shaping
- Straight-cut column dresses
- Heavy bulky knits that hang straight from shoulder to hip
- Standard-cut bottoms with significant waist gap

**Items disqualified by mode:**

*Honor mode:*
- Bodycon (deprioritized rather than disqualified; available)
- Low-rise (filtered)
- Heavy hip-detail items (filtered)

*Celebrate mode:*
- Items that hide curves entirely (loose oversized without anchor)
- Items that minimize the waist (shapeless drapes)

**Items disqualified by specific answer combinations:**

- Empire-waist disqualified for: hourglass without slim/lean variation + bust not named as featured
- Bodycon disqualified for: hourglass + cling-averse + honor mode
- High closed necklines disqualified for: full-bust hourglass + chest not flagged covered

**Items that look right but disappoint:**

- *Wrap dresses in thin clingy fabric:* the wrap is right but the fabric clings to curves without supporting; bra and underwear lines show. Surface wrap dresses in fabric with body.
- *Pencil skirts in stretchy thin fabric:* shows every contour without elevating the silhouette. Surface pencil skirts in structured stretch (ponte, sturdy stretch).
- *Standard-cut sheath dresses:* marketed as universal but on hourglass the waist gaps when bust and hips fit. Surface curvy-fit sheath dresses.

## 9. The Uniform

**Daytime / casual uniform (mid-height, mid-sophistication, mixed strategy):**

A pair of high-rise curvy-fit jeans (straight or slim) in mid or dark wash, fitting at the waist without back gap and at the seat and thigh without pulling. A fitted ribbed knit top in V-neck or scoop, tucked in fully or half-tucked at the natural waist. Optionally, a cropped blazer or fitted jacket ending at the waist worn open, or a belted wrap blazer.

Footwear: pointed ankle boots, pointed flats, or low pointed heels.

**Variations by strategy:**

- *Trace-primary hourglass:* fitted curvy-fit pieces; sheath dress; pencil skirt + tucked top.
- *Anchor-primary hourglass:* wrap dresses; belted everything; tucked tops at high-rise meeting point.
- *Sculpt-primary hourglass:* fit-and-flare with structured bodice; peplum jacket + slim bottom.
- *Edge-primary hourglass (honor):* statement belt over wrap dress; deep V + fitted top + belt; layered jewelry.
- *Edge-primary hourglass (celebrate):* bodycon dress; pencil skirt + fitted top + belt; low-rise jeans + fitted top.

**Variations by register:**

- *Work:* curvy-fit tailored trousers + fitted button-down; sheath dress + belted blazer; pencil skirt + tucked knit.
- *Evening:* wrap dress; fit-and-flare cocktail; bodycon (celebrate mode); fitted dress with statement neckline.
- *Occasion:* belted shirt dresses, fit-and-flare midis, wrap dresses.

**Variations by season:**

- *Summer:* fitted tank tops or short-sleeve tops tucked into A-line or pencil skirts; sundresses with defined waist; wrap dresses in cotton.
- *Winter:* fitted knits tucked into high-rise jeans; belted wool coats; structured blazers over fitted base.

## 10. Inference Notes for the Recommender

**Default rules that fire on hourglass identification alone:**

1. Honor the waist — the body's central asset. Filter anything that hides it without compensation.
2. Surface curvy-fit cuts when available. Single biggest factor for hourglass fit satisfaction.
3. Anchor strategy is universal hero; surface aggressively in both honor and celebrate modes.
4. Trace works directly; the body has shape for items to follow.
5. Drop-waist and empire-waist filtered (default).
6. Soft shoulder structure preferred; heavy structured shoulders deprioritized.
7. Standard-cut bottoms filtered when curvy-fit available.
8. Bust + exposure combinations resolved through featuring-zone signal (named bust = featuring intent confirmed).
9. Hip and seat featuring opt-in through featuring-zone signal (hips/seat named = celebrate mode).
10. Stretch fabrics weighted up for fleshy/athletic hourglass.
11. Skim-fit construction (not clingy) for full-bust hourglass; supports without revealing contours.
12. Petite hourglass: short jackets at waist; cautious with midi.
13. Midsection-prone hourglass: sculpt structural support critical.

**Modulators that change defaults:**

- *Mode signal (honor vs. celebrate):* primary modulator. Bodycon, low-rise, hip-detail items shift between deprioritized and hero based on mode.
- *Featuring-zone signal:* primary modulator alongside strategy and fit. Named bust resolves depth ambiguity; named hips/seat unlocks celebrate-mode items; named legs unlocks leg-featuring.
- *Per-zone reveal mode (reveal/sophisticated/cover):* detected through featuring-zone + exposure + length preferences. Default to sophisticated when signals are ambiguous.
- *Strategy selection:* trace and anchor both heroes; sculpt valuable for evening and midsection-prone; edge typically features waist + chosen asset.
- *Fit preferences:* close everywhere = celebrate mode (works directly with curves); close top + relaxed bottom = honor mode; relaxed everywhere requires compensation appropriate to selected strategy — anchor compensation if anchor selected, edge featuring if edge selected, sculpt outer structure if sculpt selected.
- *Bust signal:* full bust requires neckline calibration; smaller bust has broader neckline access.
- *Variation modulators:* lean (broader tolerance), soft (stretch and curvy-fit essential), athletic (structured stretch), full-bust (bust support critical), top/bottom hourglass (apply adjacent body type modulators on dominant zone).

**Sophistication and restrictiveness signals:**

- Multi-strategy + flexible answers + curvy-fit availability → widen catalog
- Trace-only + full-bust + petite + soft hourglass → tighten significantly; hero-weighted
- Strong featuring-zone signal for hips/seat → unlock celebrate mode aggressively
- "Nothing in particular" → conservative honor mode defaults

**Risk-scanning patterns common to hourglass:**

- Whether bottoms gap at the back waistband
- Whether the waist is visible in the finished outfit
- Whether fabric supports the silhouette or reveals contours
- Whether bust support is appropriate for the construction
- Whether items honor curves or fight them

**Common "knows the trick" non-traditional moves:**

- Sophisticated hourglass dressers may wear oversized if consistently belted
- May wear menswear-inspired tailored pieces with strong waist construction (the contrast amplifies)
- May feature hips intentionally (J.Lo-leaning hourglass aesthetic) — surfaces through featuring-zone signal
- May wear monochromatic with subtle fit variation to honor curves without high contrast

**On rule restrictiveness vs. user variation:**

Hourglass is the body type that styling literature treats as the "easy" body type because the geometric defaults are flattering. The featuring-zone question reveals that within hourglass, mode preference (honor vs. celebrate) varies significantly, and bust depth tolerance varies even more. The rules optimize for the median user who comes to styling for help (typically honor mode with sophisticated featuring), while leaving celebrate mode and reveal mode accessible through clear opt-in signals.

## 11. Open Questions and Edge Cases

**Cases the rules don't yet handle:**

- *Hourglass + significant weight gain:* may shift toward apple (midsection becomes widest) or remain hourglass with midsection-prone variation. Re-classify based on current geometry.
- *Hourglass + post-pregnancy:* waist may soften; apply midsection-prone modulator.
- *Hourglass + post-menopause:* waist often softens or shifts higher; re-evaluate proportions.
- *Hourglass + significant athletic training:* may develop top hourglass or pure inverted triangle; re-classify.

**Borderline body-type identifications:**

- *Hourglass vs. pear:* if hips are 10%+ wider than bust, treat as pear with hourglass-style anchor moves.
- *Hourglass vs. inverted triangle:* if shoulders are wider than hips with defined waist, inverted triangle with hourglass anchor moves.
- *Hourglass vs. rectangle:* if waist taper is less than 25% from bust/hips, rectangle with anchor weighted up.
- *Hourglass vs. apple:* if waist becomes equal to or larger than bust/hips, apple.

**Things behavior data should resolve:**

- Honor vs. celebrate mode preference (primary behavioral signal)
- Bust depth tolerance (default sophisticated mode, but learn whether user prefers reveal or coverage)
- Hip-emphasis intensity (when celebrate mode fires, how dramatic?)
- Empire-waist tolerance (works for slim hourglass; behavior reveals individual preference)
- Curvy-fit brand preferences
- Bodycon comfort
- Standard-cut tolerance (some hourglass users adapt buying patterns to standard cuts)
- Whether named features actually drive behavior (some users name features they like in principle but don't actually shop for; learn from purchases and saves)


---

# Body Type: Pear

**TL;DR:** Pear has fuller hips/thighs/seat with narrower upper body and defined waist. The mode split between balance (minimize lower body) and celebrate (feature lower body) is the strongest of any body type. Upper-body skin reveal is a signature pear strength because the upper body is the lean, proportional zone.

## 1. Identification

**How users self-identify in Q2:** "My hips are wider than my shoulders and bust."

**Confirming signals from Q3 (distribution):**

*Snug zones — diagnostic:*
- Hips and thighs together (the universal pear signal — fuller lower body)
- Seat (pear typically has projected seat)
- Hips/thighs and seat all snug (strong pear signal)
- Thighs only (athletic pear variation)

*Snug zones — noisy / not diagnostic:*
- Chest only (if reported alone without hip signals, suggests inverted triangle or hourglass rather than pear)
- Arms (full-bottom pear sometimes carries weight in upper arms, but not diagnostic on its own)
- Waist/stomach (rarely snug for pear; if reported, suggests pear + midsection-prone variation)

*Loose zones — diagnostic:*
- Chest/bust (pear typically has smaller bust relative to hips)
- Shoulders (narrower shoulders compared to hips)
- Arms (often lean upper body)
- Waist (defined waist between small upper body and full lower body)

*Loose zones — noisy:*
- Hips and thighs loose (would contradict pear classification)

**Confirming signals from Q4 (fit issues):**

*Fit issues — diagnostic:*
- Pants gap at the back waistband (universal complaint — small waist + full hip/seat)
- Pants too tight at the thigh when fitted at the waist
- Buying bottoms one size up for thighs → waist gaps
- Dresses fit hips but loose at bust
- Buying dresses to fit hips → bodice is loose and ill-fitting
- Tops fit fine but bottoms are difficult
- "Bottoms are always the hard part" — strong pear signal

*Length issues — diagnostic:*
- Pants feel too short → if tall
- Pants feel too long → if petite
- Mid-thigh shorts ride up too much (fuller thighs)
- Mini skirts feel proportionally wrong (hit at widest hip point on petite pear)
- "Everything usually sits where it should" — possible for mid-height pear who has adapted buying patterns

**Conflicting or ambiguous signals to watch for:**

- *Snug at chest/bust + snug at hips:* possibly bottom hourglass leaning pear, rather than true pear. The chest signal matters — if bust is also full, hourglass rules apply more.
- *Loose at hips and thighs:* contradicts pear. Check whether geometry was misreported.
- *Snug at waist + snug at hips:* possibly pear + midsection-prone variation. Still pear if hips remain widest; rules adjust for softer waist definition.
- *Loose at bust + snug at hips + sloped shoulders:* classic pear, often petite or with smaller frame upper body. Pear rules apply strongly.

**Distinctions from adjacent body types:**

- *Pear vs. hourglass:* pear has hips noticeably wider than bust (more than 5%). Hourglass has bust and hips balanced. If bust is small relative to hips, it's pear.
- *Pear vs. bottom hourglass:* bottom hourglass has hips slightly larger than bust but still relatively balanced. Pear has a more dramatic difference. Threshold: if hips are more than ~10% wider than bust, treat as pear.
- *Pear vs. rectangle:* rectangle has minimal waist taper and balanced shoulders/hips. Pear has both defined waist and wider hips.
- *Pear vs. apple:* apple has widest point at midsection. Pear has widest point at hips/thighs. Apples often have narrower hips and legs; pears have narrow waist and full legs.
- *Pear vs. spoon:* spoon is a pear variation with shelf-hips (sharp horizontal projection at hip). Same rules apply with stronger emphasis on managing the hip-shelf line.

## 2. Geometric Truth

**Core proportions:**
- Hips and thighs are the widest part of the body
- Shoulders are narrower than hips (sometimes by 5-15%+)
- Bust is typically smaller (B cup or smaller is common, though pears can have larger busts)
- Waist is defined and noticeably narrower than hips
- Seat has projection and shape from the side
- Thighs are full, often touching at the top
- Calves and ankles vary

**Where volume sits:**
- Hips, thighs, seat — the primary volume zones
- Bust, shoulders, upper arms typically lean
- Waist is the narrowest zone

**Length tendencies:**
- Variable across pear users
- Pear can have proportionally shorter legs (when hip volume reads as visually shortening)
- Tall pear (170+) has more visual length to balance hip volume; petite pear (under 160) has the hardest proportion challenge

**Common geometric variations within the type:**

- *Lean pear:* smaller overall frame, hips still wider than bust but in absolute terms not large. More styling tolerance.
- *Soft/fleshy pear:* fuller hips, thighs, seat with naturally soft musculature. Stretch fabrics matter critically; tailoring becomes essential.
- *Athletic pear:* muscular thighs and seat (sprinter, cyclist, dancer). Bottom volume is muscle. Same proportions as fleshy pear but firmer feel.
- *Spoon pear:* sharp horizontal shelf at the hip line — hips project outward and then drop relatively straight.
- *Petite pear:* same proportions at smaller scale. Hip volume reads as visually large relative to overall body length.
- *Pear + larger bust:* less common but real. Hips still widest, but bust also fuller.
- *Pear + midsection-prone:* post-pregnancy or natural soft midsection. Waist still defined relative to hips but less sharply.

## 3. Visual Assets (default, before strategy modulation)

**Natural assets (read well without intervention):**

- *Defined waist:* the central asset alongside the natural lower-body shape.
- *Upper body proportions:* shoulders, arms, and bust often read as delicate or proportional, making the upper body easy to dress without bulk.
- *Décolletage and collarbones:* often a feature for smaller-bust pears.
- *Lean upper back:* often overlooked but a real pear asset — the upper back is typically narrow and clean.
- *Curves (when celebrated):* the lower-body shape is itself an asset for users who want to feature it.
- *Smaller bust:* often makes high necklines, button-downs, and structured tops fit without pulling.

**Features that become assets when used intentionally:**

- *Upper-body skin reveal as signature play:* the upper body is pear's leanest, most proportional zone. Unlike other body types that have constraints on upper-body reveal (hourglass cleavage management, inverted triangle shoulder amplification, apple midsection sensitivity), pear has no inherent constraint beyond user preference. Off-shoulder, low-back, chest cutouts, halter, crop tops, and similar items feature lean assets without creating proportion problems. This is one of pear's distinctive strengths.
- *Hip emphasis (opt-in):* low-rise bottoms, hip-detail cuts, prints and color at the hip line, bodycon dresses that follow hip curves.
- *Upper body amplification (balance mode):* structured shoulders, statement sleeves, embellished necklines, bright/printed tops.
- *Lengthening the silhouette:* vertical lines, monochromatic outfits with subtle color shifts, pointed shoes.

**Override conditions:**

- *Lower body to be minimized (default balance mode):* surface upper-body emphasis, dark bottoms, A-line skirts skimming hips, structured shoulders.
- *Lower body to be featured (opt-in via signals):* surface hip-emphasis cuts, low-rise, bodycon, bright bottoms, prints below the waist.

**Featuring-zone signals from the questionnaire (cross-body framework):**

- *Hips/seat named:* shifts toward celebrate mode. Surface hip-emphasis cuts, low-rise, bodycon, jeans with prominent back pockets, bright bottoms. Geometry rules still apply to execution — filter clingy cheap fabric that distorts the curve, hip-pocket bulk that adds visual width without shape, horizontal seams that segment rather than celebrate the hip line. Goal shifts from "skim hips" to "feature hips well"; "well" still has rules.
- *Legs named:* unlock leg-featuring. Surface fitted bottoms showing leg line, short hems, slits.
- *Waist named:* confirms anchor direction. Surface anchor items aggressively (already default for pear).
- *Shoulders named:* unlock shoulder-feature items — off-shoulder, halter, one-shoulder, structured shoulders.
- *Back named:* signature pear unlock. Lean upper back works exceptionally well for low-back dresses, open-back tops, keyhole back, lace-up back.
- *Décolletage named:* surface open necklines as featuring move.
- *Bust named:* if fuller bust, surface bust-featuring items at exposure-appropriate depth.
- *Arms named:* surface sleeveless and arm-revealing cuts.
- *Midriff named (less common):* surface crop tops and waist-baring items for confident dressers.
- *"Nothing in particular":* conservative balance-mode defaults; hero-weighted; behavior data critical.

## 4. Visual Risks (default, before strategy modulation)

**Silhouettes that fight this body type (default balance approach):**

- *Skinny jeans and tight tapered pants:* cling to hip, thigh, and calf, emphasizing volume difference. Not universally bad — celebrate-mode users may want this — but in balance mode they amplify the contrast.
- *Tight pencil skirts:* cling to hips and thighs. Filtered in balance mode; surfaced in celebrate mode.
- *Bodycon dresses:* follow every curve. Filtered in balance mode; surfaced in celebrate mode.
- *Hip-length jackets and tops:* end at the widest hip point, creating horizontal break that emphasizes hip width.
- *Tops that flare at the hip without compensation:* peplums, dropped yokes, gathered hems at hip — add volume to the already-wide hip area in balance mode.
- *Low-rise bottoms (in balance mode):* sit at widest hip line. Hero in celebrate mode.
- *Heavy/stiff fabrics in bottoms:* don't drape over the curve, add visual bulk.
- *Bright colors or bold prints on bottoms (in balance mode):* draw attention down.
- *Cargo pants, pleated pants with hip detail, paneled hip seams:* add visual interest at the hip.
- *Drop-waist dresses:* eliminates the asset and emphasizes the column from shoulder to mid-thigh.
- *Empire-waist dresses (sometimes):* some sources recommend; others note it eliminates the waist asset. Treat as situational.
- *Shapeless tunic tops:* hang straight from shoulder to mid-thigh, hide the waist, and end at hip-widest.

**Construction details that fail (balance mode):**

- Patch pockets at the hip or back pockets too close together
- Horizontal seams at the hip line
- Embellishments at the hip, thigh, or seat
- Pleats at the front waist
- Big buttons or details down the front of skirts
- Heavy embroidery or print placement at the hip

**Fabric behaviors that fail:**

- Stiff bottoms that don't drape over the curve
- Thin clingy bottoms on fleshy pear
- Heavy fabric overall on lower body

**Necklines that fail (default balance mode):**

- Narrow high necklines without embellishment (minimize what balance mode wants to maximize)
- Deep plunging without structure (draws eye down without compensating volume)

**Length traps:**

- For petite pear: midi often hits at calf-widest; mini reads disproportionate; bermuda hits at thigh-widest. Knee-length or just-above-knee works best.
- For tall pear: standard pants often too short, especially when sized up for thighs.

**Override conditions:**

- *Skinny jeans, bodycon, hip-emphasis items:* hero items in celebrate mode, not failures.
- *Cropped tops:* work for both modes — they end above the hip, exposing the waist.

## 5. Strategy Modulation

### Trace

**What trace means for this body type:**

Trace works for pear when the fit is correct — meaning curvy-fit cuts that accommodate the waist-to-hip ratio. Standard cuts often fail because they're designed for proportional bodies. Trace honors the body's actual shape and lets the user decide through other styling whether to draw eye up (balance) or down (celebrate).

**What works under trace:**

- Fitted tops in soft fabric or stretch
- Wrap tops and surplice tops
- Fitted button-downs in stretch fabric
- Tucked-in fitted knit tops
- Curvy-fit jeans (the universal pear need)
- High-rise straight or slim jeans that fit the waist and skim the hip
- Tapered trousers with hip ease and waist fit
- A-line skirts (trace at waist, A-line below as light sculpt)

**What fails under trace:**

- Standard-cut tops with no shaping (pull at hip when long enough to cover hips)
- Stiff fabric bottoms that don't follow hip curve
- Tight clingy bottoms in cheap stretch
- Skinny jeans in stiff denim

**Special considerations:**

- Curvy-fit availability is the single biggest factor for trace success on pear.
- Trace serves both balance and celebrate modes equally — the items follow the body either way.

### Anchor

**What anchor means for this body type:**

Universally useful for pear. The waist is the asset, and emphasizing it via tucking, belting, wrap, or fitted bodice all work. Anchor is particularly powerful for pear because the waist is the meeting point between the smaller upper body and the fuller lower body.

**Hard vs. soft anchor:**

Both work because the waist exists. Anchor allows pear users who prefer relaxed-fit clothing to still preserve waist visibility.

**Specific anchor moves that work:**

- Wrap dresses and wrap tops
- Belted dresses at natural waist
- Belted shirt dresses
- Belted blazers and coats
- Tucked-in tops (full or half tuck)
- High-rise bottoms (creates implicit anchor)
- Cropped tops ending at the natural waist
- Statement belts over relaxed tops

**Anchor moves that fail:**

- Drop-waist (eliminates the asset)
- Empire-waist (creates column from bust down)
- Wide belts that cover too much torso (especially petite)
- Hip belts (defeats waist emphasis)

**Special note on mode interaction:**

Anchor is mode-neutral — emphasizing the waist serves both balance and celebrate modes. In balance mode, anchor + upper-body emphasis = "draw eye up + define waist + skim hips." In celebrate mode, anchor + hip-emphasis bottoms = "tiny waist + dramatic hip."

### Sculpt

**What sculpt means for this body type:**

Mode-dependent more than for any other body type.

*Balance mode:* sculpt on the upper body — structured shoulders, peplum tops, statement-shoulder blazers — creates artificial upper-body volume that balances the lower body.

*Celebrate mode:* sculpt that amplifies the lower body — corseted bodice + dramatic full skirt, fit-and-flare that exaggerates hip flare, mermaid skirts.

**What good upper-body sculpt looks like (balance mode):**

- Tailored blazers with subtle shoulder structure
- Peplum tops with structured shoulders (when hem doesn't hit at hip-widest)
- Structured-shoulder jackets cropped at the waist
- Boat-neck tops in structured fabric

**What good lower-body sculpt looks like (celebrate mode):**

- Mermaid skirts and dresses
- Fit-and-flare with dramatic skirt volume
- Corseted bodice + full skirt
- Pencil skirts that follow the hip closely

**What bad sculpt looks like:**

- Sculpt that adds volume at hip line in balance mode (peplum at hip-widest)
- Sculpt with stiff fabric that fights the body's give
- Heavy structured shoulder pads (read costume-y)

### Edge

**What edge means for this body type:**

Pear has a uniquely strong upper-body featuring vocabulary because the upper body is the lean, proportional zone — skin reveal, cutouts, and play-with-shape items work there with fewer constraints than any other body type.

**Featuring modes (balance — upper body):**

*Upper-body skin reveal (pear signature):*
- *Shoulder and collarbone reveal:* off-shoulder/Bardot (universally flattering — broadens shoulder line AND features lean shoulders); one-shoulder asymmetric; cold-shoulder cutouts; halter
- *Chest reveal:* keyhole cutouts; drop-front necklines; geometric chest cutouts; deeply open button-ups; square neck (wide and shallow); sweetheart and strapless for smaller-bust pears
- *Back reveal:* low back dresses and tops, open back, scoop back, low V back, lace-up back, halter neck with bare back. Most distinctive pear featuring category.
- *Waist reveal:* crop tops exposing the midriff.

*Upper-body emphasis without skin reveal:*
- Statement sleeves (puff, bishop, bell, flutter)
- Bold print or color on top with simple bottoms
- Embellished bodice
- Decorative collars
- Boat neck without bare shoulder
- Statement earrings and jewelry pulling eye up

*Décolletage and bust features:*
- Open necklines at depth calibrated to comfort
- Fitted bodice that shows shape without revealing skin
- Wrap front showing décolletage at moderate depth

**Featuring modes (celebrate — lower body):**

- *Hip features:* hip-emphasis cuts, low-rise bottoms, contoured waistbands
- *Seat features:* fitted pants and skirts that follow seat projection, bodycon dresses
- *Thigh features:* slits, side cutouts on dresses, fitted pants in dramatic fabric
- *Leg features:* fitted bootcut and flared pants, cropped pants with ankle reveal, slim trousers, monochromatic leg-extending palettes
- *Bottom prints and color:* bright bottoms, printed skirts

**Three-mode framework for upper-body featuring:**

For each named upper-body zone (bust, shoulders, back, arms, midriff):
- *Reveal mode:* bare-shoulder off-shoulder, deep V, fully open back, crop tops, halter with bare shoulders
- *Sophisticated mode:* boat neck (broadens without bare shoulder), keyhole back, asymmetric necklines, fitted bodice with moderate neckline, sheer panel insets
- *Coverage mode:* high necklines with detail, structured shoulders with long sleeves, fitted-waist tops with closed neckline, color/print emphasis without skin reveal

Default to sophisticated when signals are ambiguous.

## 6. Combinational Rules

**The balance vs. celebrate mode signal:**

Central modulator for pear. Detection through featuring-zone question:

- *Balance mode default:* user names upper-body zones only, or doesn't name lower-body zones; reports hips/thighs/seat as snug fit issues; signals desire to minimize lower body.
- *Celebrate mode opt-in:* user names hips, seat, or legs as featuring zones; opts for high exposure on lower body; behavior shows preference for hip-emphasis cuts.
- *Mode unclear:* default to balance mode; refine through behavior.

**Body + strategy combinations:**

- *Pear + trace:* surface curvy-fit trace items. Works for both modes.
- *Pear + anchor:* surface aggressively. Universal hero strategy regardless of mode.
- *Pear + sculpt + balance mode:* surface upper-body sculpt; filter peplum if it adds volume at hip-widest.
- *Pear + sculpt + celebrate mode:* surface lower-body sculpt (mermaid, dramatic fit-and-flare).
- *Pear + edge + balance mode:* surface upper-body features (statement neckline, sleeves, upper-body skin reveal at appropriate mode), waist features. Filter hip-emphasis edge.
- *Pear + edge + celebrate mode:* surface hip, seat, leg features. Filter upper-body-only features.

**Body + fit combinations:**

- *Pear + close everywhere:* requires trace + curvy-fit + waist-emphasis. Celebrate mode default.
- *Pear + close top + relaxed bottom:* classic balance-mode pattern.
- *Pear + relaxed top + close bottom:* less common; works when relaxed top is belted/tucked.
- *Pear + relaxed everywhere:* when anchor is the selected strategy, requires anchor compensation. When edge is the selected strategy, the strategy bypasses the hip-skimming requirement by featuring other zones (upper-body featuring in balance mode; lower-body featuring in celebrate mode) — items can succeed through strong featuring without explicit anchor. Pure shapeless without any compensation or featuring = failure regardless of strategy.

**Body + fabric combinations:**

- *Lean pear:* most fabrics work.
- *Soft/fleshy pear:* stretch in bottoms weighted up significantly; curvy-fit critical.
- *Athletic pear:* stretch for muscle accommodation; structure for muscular legs.
- *Pear + cling-averse:* filter thin clingy bottoms; surface structured stretch.

**Body + bust combinations:**

- *Pear + smaller bust (most common):* wide range of necklines accessible including high necks, boat necks, off-shoulder, square.
- *Pear + larger bust:* apply hourglass-bust rules to neckline selection; pear lower-body rules still apply.

**Body + exposure combinations:**

- *Pear + legs uncovered:* shorter hems available; celebrate mode reveals the point. Balance mode prefers knee-length or longer.
- *Pear + chest covered:* less constraining than for hourglass; higher necklines work; cutouts/reveal shift to back, shoulder, waist categories.
- *Pear + back uncovered + edge:* signature unlock. Open-back items become heroes.
- *Pear + shoulders uncovered + edge:* off-shoulder, Bardot, one-shoulder become heroes.
- *Pear + lower body covered:* signals balance mode.
- *Pear + lower body uncovered + edge:* signals celebrate mode.

**Body + featuring-zone combinations:**

- *Pear + named upper-body zones (bust, shoulders, back, arms, décolletage, waist):* reinforce balance mode; surface featuring at user's detected reveal/sophisticated/cover mode.
- *Pear + named lower-body zones (hips, seat, legs):* shifts toward celebrate mode.
- *Pear + named upper AND lower zones:* sophisticated multi-strategy user; widen catalog.
- *Pear + no zones named or "nothing in particular":* conservative balance-mode defaults.

**Body + variation modulators:**

- *Lean pear:* broader styling tolerance.
- *Soft/fleshy pear:* stretch and curvy-fit essential.
- *Athletic pear:* stretch for muscle; structure for muscular legs.
- *Spoon pear:* careful with mid-rise (sits on shelf); high-rise above shelf, low-rise below.
- *Petite pear:* short jackets at waist; knee or just-above-knee skirts; cautious with midi unless slit.
- *Pear + midsection-prone:* fit-and-flare with built-in shaping; ponte and structured stretch.

## 7. Hero Categories

**Hero items (consistent across pear, both modes):**

- A-line skirts (balance: skims hips; celebrate: amplifies hip flare)
- Wrap dresses (universal pear hero)
- Fit-and-flare dresses with knee or midi hem
- High-rise bootcut or flared jeans
- High-rise wide-leg trousers
- High-rise straight jeans (curvy fit)
- Tucked fitted tops
- Wrap tops and surplice tops
- Cropped jackets ending at natural waist
- Statement belts over relaxed tops
- Fitted button-downs in stretch fabric

**Hero items (balance mode — upper-body featuring):**

*Reveal mode upper-body heroes (signature category):*
- Off-shoulder and Bardot tops and dresses
- One-shoulder asymmetric
- Cold-shoulder cutouts
- Halter tops and dresses
- Open-back dresses and tops
- Low-back dresses (scoop back, V back, fully open back)
- Lace-up back details
- Chest cutout tops (keyhole, geometric)
- Crop tops exposing midriff
- Strapless and sweetheart for smaller-bust pears

*Sophisticated mode upper-body heroes:*
- Boat neck tops
- Square neck (wide and shallow)
- Wide V or wide scoop
- One-shoulder with covered shoulder
- Keyhole back and back cutouts
- Asymmetric necklines that frame
- Wrap tops with moderate crossover
- Fitted bodices with closed necklines but defined shape
- Sheer panel insets

*Coverage mode upper-body heroes:*
- Statement-sleeve tops (puff, bishop, bell, flutter)
- Tops with bold prints or bright color
- Embellished bodice tops
- Structured-shoulder blazers
- Peplum tops with structured shoulders
- High necklines with detail, embellishment, or texture
- Tops with princess seams or ruching at the bust

**Hero items (celebrate mode — lower-body featuring):**

- Bodycon dresses (when comfortable)
- Pencil skirts that follow the hip
- Fitted leather pants or statement bottoms
- Low-rise bottoms (when user opts in)
- Mermaid skirts and dresses
- Fit-and-flare with dramatic skirt volume
- High-rise jeans with prominent back pockets
- Hip-detail bottoms
- Bright bottoms or printed skirts/pants
- Skirts with side slits showing the leg
- Maxi and midi dresses with high slits

**Hero necklines:**

For balance mode (widen the upper body visually):
- Boat neck
- Bardot/off-shoulder
- Square neck (wide)
- Sweetheart (for smaller-bust pears, the structure adds volume)
- Wide V or wide scoop
- Cowl neck
- High neck with detail or embellishment
- Halter (narrow at neck, exposes upper back)
- Keyhole and chest cutout necklines
- One-shoulder asymmetric

For celebrate mode (keep top simple, let lower body feature):
- Simple V-neck
- Simple scoop
- Crew neck and mock neck
- Turtleneck (works for most pears with small bust)
- Simple high necks without embellishment

**Hero back details (pear signature):**

- Low-back dresses
- Open-back tops
- Scoop back, V back
- Lace-up back
- Halter neck with low back
- Cutouts at the back
- Keyhole back (sophisticated mode)
- Sheer panel back insets (sophisticated mode)

**Hero sleeves:**

For balance mode:
- Puff sleeves
- Bishop sleeves
- Bell sleeves
- Flutter sleeves
- Statement sleeves with structure
- Cap sleeves with subtle shoulder lift
- Set-in sleeves with structured shoulder

For celebrate mode:
- Simple fitted sleeves
- Sleeveless
- Three-quarter
- Long sleeves in fluid fabric without volume

**Hero pant silhouettes:**

- High-rise bootcut or flared (universal — tapers attention through ankle flare)
- High-rise wide-leg
- High-rise straight (curvy fit)
- Tapered trousers with hip ease
- Dark wash jeans (balance mode default)
- Bright wash or printed jeans (celebrate mode)

**Pants with mode-specific gating:**

- Skinny jeans and tight tapered pants: hero in celebrate mode; downranked in balance mode
- Low-rise: hero in celebrate mode; filtered in balance mode

**Hero dress and skirt silhouettes:**

- A-line midi or knee-length
- Wrap dresses
- Fit-and-flare dresses
- Skater dresses
- Maxi dresses with high waistline
- Maxi and midi dresses with side or front slits (sophisticated leg feature)
- Mermaid skirts (celebrate mode)
- Pencil skirts (celebrate mode)
- High-rise A-line skirts

**Hero outerwear:**

- Cropped jackets ending at natural waist
- Belted trench coats
- Belted blazers
- Princess-seamed coats with waist shaping
- Wrap coats
- Soft-structured blazers with subtle shoulder

**Hero items by strategy:**

- *Trace hero:* curvy-fit straight jeans + fitted ribbed knit; wrap dress; tucked fitted button-down
- *Anchor hero:* belted wrap dress; statement belt over relaxed top; tucked-in tops at high-rise meeting point
- *Sculpt hero (balance):* structured-shoulder blazer + dark trouser; peplum top + slim bottom
- *Sculpt hero (celebrate):* mermaid skirt + simple top; fit-and-flare with dramatic skirt
- *Edge hero (balance + reveal):* off-shoulder top + high-rise jeans; low-back dress; halter top + A-line midi
- *Edge hero (balance + sophisticated):* boat neck top + tailored trouser; keyhole back dress; one-shoulder with covered shoulder
- *Edge hero (balance + coverage):* statement-sleeve top + dark high-rise jeans; embellished bodice + simple skirt
- *Edge hero (celebrate):* bodycon dress; high-rise jeans + fitted top showing curve; bright printed skirt + simple top

## 8. Disqualified Categories

**Items that don't work, regardless of strategy or mode:**

- Shapeless tunic tops hanging from shoulder to mid-thigh
- Drop-waist dresses
- Empire-waist tops or dresses (unless explicit user preference)
- Hip-length jackets that end exactly at hip-widest
- Boxy oversized blazers without belt or fitted base
- Heavy bulky knit sweaters that hang straight from shoulder to hip
- Stiff fabrics in bottoms that don't drape over the curve
- Mom jeans with very loose hip
- Heavy front-pleat trousers with hip detail

**Items disqualified by mode:**

*Balance mode disqualifies:*
- Bodycon dresses
- Tight pencil skirts (unless very confident user)
- Low-rise bottoms
- Bright bottoms and printed skirts/pants
- Hip-detail items
- Statement bottoms in eye-catching fabrics
- Skinny jeans (deprioritized rather than disqualified)

*Celebrate mode disqualifies:*
- Voluminous upper-body items that hide the bust/shoulder area
- Heavy structured shoulder pads
- Tops with very loose hem that hides waist
- Items that draw all attention to upper body alone

**Items disqualified by featuring-mode signals:**

- Off-shoulder, low-back, halter, cutouts disqualified for: pear + coverage mode on the relevant zone
- Bare-shoulder reveal disqualified for: pear + sophisticated or coverage mode on shoulders
- Crop tops disqualified for: pear + cover mode on midriff

**Items that look right but disappoint:**

- *Wrap dresses in clingy fabric:* marketed as universal pear hero, but cling to the hip and emphasize what they should skim. Surface wrap dresses with body and drape.
- *A-line skirts in stiff fabric:* shape is right but stiff fabric stands away and creates bulk. Surface A-line in soft drapey fabric or knit.
- *Peplum tops on hip-prone pears:* peplum flare often hits at hip-widest and doubles the volume. Surface peplum only when hem hits above hip line.
- *Mid-rise bootcut jeans on spoon pear:* mid-rise sits on the hip shelf, creating bunching. Surface high-rise or low-rise instead.

## 9. The Uniform

**Daytime / casual uniform (balance mode):**

High-rise curvy-fit straight or bootcut jeans in mid or dark wash, sitting at the natural waist without back gap. A fitted top in soft fabric tucked into the jeans, with interest at the top half — wrap front, fitted button-down with rolled sleeves, fitted V or scoop neck, soft statement sleeve, or upper-body reveal piece like a cold-shoulder top or keyhole-back blouse. Optionally a cropped blazer or open denim jacket ending at the natural waist. Footwear: pointed ankle boots, pointed flats, or low pointed heels.

**Daytime / casual uniform (celebrate mode):**

High-rise or mid-rise fitted jeans (skinny, slim, or bodycon-fit) following the hip and thigh curve. A simple fitted tucked top — crew, V, or scoop — in soft fabric. The bottom is the focal point. Optional belt at the waist.

**Variations by strategy:**

- *Trace-primary:* fitted curvy-fit pieces.
- *Anchor-primary:* wrap dresses, belted everything, tucked-in tops.
- *Sculpt-primary (balance):* structured-shoulder blazer + dark trouser.
- *Sculpt-primary (celebrate):* mermaid skirt + simple top.
- *Edge-primary (balance + reveal):* off-shoulder top + high-rise dark jeans; low-back dress.
- *Edge-primary (balance + sophisticated):* boat neck top + tailored trouser; keyhole back dress.
- *Edge-primary (celebrate):* bodycon dress; bright printed skirt + simple top.

**Variations by register:**

- *Work:* curvy-fit tailored trousers + fitted button-down (curvy fit); A-line dress with belted blazer; sheath dress in curvy fit; coverage-mode upper-body featuring for offices where reveal isn't appropriate.
- *Evening:* wrap dress; fit-and-flare cocktail; off-shoulder top + tailored skirt; low-back dresses; halter gowns; mermaid dress (celebrate); bodycon (celebrate + comfortable).
- *Occasion:* belted shirt dresses, A-line midis, fit-and-flare, low-back dresses.

**Variations by season:**

- *Summer:* fitted tank tops or off-shoulder tops tucked into A-line skirts or high-rise shorts; sundresses with defined waist; off-shoulder summer dresses; halter sundresses.
- *Winter:* fitted knits tucked into high-rise jeans; belted wool coats; structured-shoulder blazers over fitted base; keyhole-back sweaters for sophisticated featuring.

## 10. Inference Notes for the Recommender

**Default rules that fire on pear identification alone:**

1. Show the waist — central rule.
2. Surface curvy-fit cuts when available. Single biggest factor for pear satisfaction.
3. High-rise bottoms preferred almost universally.
4. Default to balance mode unless celebrate signals fire.
5. Detect mode through featuring-zone question + exposure + behavior. Default conservative.
6. Upper-body skin reveal is a signature pear strength — surfaced for balance mode users who haven't marked upper-body coverage. Pear has fewer constraints on upper-body reveal than any other body type.
7. Anchor items surfaced universally (both modes benefit).
8. Stretch fabrics weighted up for soft/athletic pear.
9. Skim-the-hip silhouettes (A-line, bootcut, wide-leg) heroed in balance mode; follow-the-hip silhouettes (skinny, bodycon, pencil) heroed in celebrate mode.
10. Upper-body sculpt and edge surfaced in balance mode.
11. Hip-emphasis items filtered in balance mode; heroed in celebrate mode.
12. Hip-length tops and jackets filtered (universal).
13. Drop-waist filtered universally; empire filtered unless explicit user preference.
14. Petite + pear: short jackets at waist; knee or just-above-knee skirts.
15. Stretch + curvy-fit critical for fleshy/athletic pear.
16. Standard-cut bottoms filtered when curvy-fit available.

**Modulators that change defaults:**

- *Mode signal (balance vs. celebrate):* primary modulator. Skinny jeans, low-rise, bodycon, bright bottoms shift between hero and filter based on mode.
- *Featuring-zone signals:* named upper-body zones reinforce balance mode and unlock reveal/sophisticated/cover modes for those zones; named lower-body zones shift toward celebrate mode.
- *Strategy selection:* trace universal; anchor universal; sculpt mode-dependent; edge mode-dependent.
- *Per-zone reveal mode:* detected through featuring-zone + exposure + length preferences.

**Sophistication and restrictiveness signals:**

- Multi-strategy + flexible answers + curvy-fit availability → widen catalog
- Trace-only + multiple covered zones + petite + soft pear → tighten significantly
- Named multiple featuring zones → confident multi-strategy dresser

**Risk-scanning patterns common to pear:**

- Whether bottoms gap at the back waistband
- Whether bottoms pull at the thigh
- Whether tops end at hip-widest
- Whether the waist line is visible
- Whether fabric drapes over hip curve or stands away
- Whether sleeve volume balances or competes with hip volume
- Whether upper-body reveal items match user's mode for that zone

**Common "knows the trick" non-traditional moves:**

- May wear oversized items if consistently belted or tucked
- May wear bodycon as evening piece for celebrate mode
- May use color blocking with dark waist panel
- Celebrate-mode pear may use bright bottoms + simple tops as signature look
- May use upper-body reveal aggressively as balance strategy — backless dresses, off-shoulder tops, halters — features lean upper body to draw attention up
- May combine sophisticated reveal moves (keyhole back, sheer panels, asymmetric cuts) for elevated featuring

**On rule restrictiveness vs. user variation:**

Pear has the strongest mode-split of any body type. Same item can be hero or filter depending on balance vs. celebrate. Same upper-body reveal item can be hero or filter depending on reveal/sophisticated/cover mode. The system needs to detect both overall mode AND per-zone reveal modes. Conservative defaults (balance mode + sophisticated reveal mode) serve most users; celebrate mode and reveal mode serve opt-in users.

## 11. Open Questions and Edge Cases

**Cases the rules don't yet handle:**

- *Pear + post-pregnancy:* hips remain wider but waist softens; surface fit-and-flare with built-in shaping; filter clingy at midsection.
- *Pear + post-menopause:* sometimes shifts toward spoon or apple; re-classify.
- *Pear + significant midsection weight gain:* may shift toward apple temporarily.
- *Pear + significant athletic training:* may shift toward more muscular pear or inverted triangle if upper body develops.

**Borderline body-type identifications:**

- *Pear vs. bottom hourglass:* threshold around 10% hip-bust difference.
- *Pear vs. spoon:* both have wider hips; spoon has horizontal shelf, pear has gradual curve.
- *Pear with broader shoulders (athletic):* if shoulders still narrower than hips, pear with inverted triangle elements on top.

**Things behavior data should resolve:**

- Mode preference (balance vs. celebrate) — single most important behavioral signal
- Per-zone reveal mode for each named upper-body featuring zone
- Curvy-fit brand preferences
- Skinny jeans tolerance
- Length tolerance at various heights
- Hip-emphasis intensity (mild vs. dramatic celebrate mode)
- Empire-waist preference
- Statement sleeve tolerance
- Pencil skirt comfort
- Back-feature tolerance
- Off-shoulder tolerance
- Whether named features actually drive behavior (some users name features they like in principle but don't actually shop for; learn from purchases and saves)


---

# Body Type: Apple (Oval)

*Note: "Apple" and "oval" refer to the same body type. The terms are used interchangeably in styling resources; "oval" is increasingly preferred to avoid fruit-shaming language but "apple" remains the more commonly recognized term.*

**TL;DR:** Apple has the widest point at the midsection with narrower shoulders and hips. The job is to skim (not cling) the midsection, feature alternative zones (legs are typically the strongest asset, décolletage is reliable), and use vertical lines to slim the torso. Anchor at the natural waist almost always fails — anchor moves either above (empire, gated by tummy) or below (high hip, low anchor).

## 1. Identification

**How users self-identify in Q2:** "My midsection is the widest part of my body, with narrower hips and shoulders."

**Confirming signals from Q3 (distribution):**

*Snug zones — diagnostic:*
- Waist/stomach (universal apple signal)
- Waist/stomach AND chest together (very common — apple with fuller bust)
- Back (sometimes — fuller apple may carry weight in upper/middle back)
- Chest only with snug waist (top-heavy apple, may overlap with inverted triangle)

*Snug zones — noisy / not diagnostic:*
- Arms (apple may carry upper arm volume, but not diagnostic on its own)
- Shoulders (if alone, could suggest inverted triangle; with snug waist, confirms apple variation)

*Loose zones — diagnostic:*
- Hips and thighs (apples typically have lean lower body)
- Seat (apples often have flat or minimally projected seat)
- Legs (often lean throughout)

*Loose zones — noisy:*
- Waist/stomach loose (would contradict apple classification)

**Confirming signals from Q4 (fit issues):**

*Fit issues — diagnostic:*
- Pants gap at the seat or back of waistband
- Tops pull at the midsection but fit shoulders and arms
- Buying tops one size up to fit the midsection → boxy at shoulders and chest
- Dresses fit shoulders and bust but pull at the midsection
- Pants fit at the waist but loose at the seat
- Pants fit at the seat but cut into the waist (universal apple bottom problem)
- "Tops are always the hard part" — strong apple signal

*Length issues — diagnostic:*
- Tops feel too short → if tall (looking for tunic-length items)
- Pants feel too short → if tall
- Pants feel too long → if petite

**Conflicting or ambiguous signals to watch for:**

- *Snug at hips/thighs:* contradicts pure apple. May be apple + bottom-fuller variation, or borderline apple/rectangle/hourglass with midsection-prone status.
- *Loose at chest/bust:* possible for smaller-bust apple. Doesn't reclassify; midsection signal dominates.
- *Snug at shoulders + snug waist:* top-heavy apple (leans inverted triangle but waist still widest). Apple rules with inverted triangle modulators on shoulders.
- *Defined waist + snug waist:* contradictory. May be post-pregnancy hourglass or rectangle with new midsection volume. Re-classify based on current geometry.

**Distinctions from adjacent body types:**

- *Apple vs. rectangle:* rectangle has minimal taper but waist is not the widest point. Apple has widest point at midsection. Rectangle + midsection-prone is the borderline case.
- *Apple vs. hourglass:* hourglass has waist visibly smaller than bust/hips. Apple has waist visibly larger. Direct opposites.
- *Apple vs. inverted triangle:* inverted triangle has widest at shoulders. Apple has widest at midsection.
- *Apple vs. pear:* pear has widest at hips. Apple has widest at midsection.
- *Apple vs. midsection-prone rectangle:* rectangle has balanced shoulders/hips with no taper but midsection softer/fuller than peak. Apple has shoulders/hips narrower than midsection — midsection projects beyond.

## 2. Geometric Truth

**Core proportions:**
- Midsection (stomach, ribcage, sometimes back) is the widest part of the body
- Shoulders and hips typically narrower than midsection and roughly aligned with each other
- Bust often fuller (C+ common but not universal)
- Waist undefined or fuller than bust/hips — no clear taper
- Seat typically flat or minimally projected
- Legs typically lean and proportionally slim — often the strongest natural asset
- Arms vary

**Where volume sits:**
- Midsection (stomach, ribcage), bust, sometimes upper back and upper arms
- Tendency toward leanness: hips, thighs, seat, legs, ankles

**Length tendencies:**
- Variable; no consistent torso/leg ratio
- Apples often have proportionally shorter torsos (midsection volume compresses visually)
- Legs often appear longer relative to the torso, which becomes a styling asset

**Common geometric variations within the type:**

- *Slim/lean apple:* lower weight overall, midsection still widest. Less stomach to manage; broader styling tolerance.
- *Soft/fleshy apple:* fuller throughout upper-mid body; stomach more prominent; back and ribcage may also carry weight.
- *Top-heavy apple (leans inverted triangle):* shoulders also broader. Inverted triangle softening on top + apple at midsection.
- *Full-bust apple:* most common variation. Bra fit and bust support critical.
- *Lean lower body apple:* the typical apple — flat seat, narrow hips, lean thighs and legs.
- *Post-pregnancy/post-menopause apple:* developed from previous body type through hormonal weight gain. May still mentally identify with old body type; classify by current geometry.
- *Petite apple:* same proportions at smaller scale. Vertical line emphasis even more important.
- *Tall apple:* more visual length to balance midsection.

## 3. Visual Assets (default, before strategy modulation)

**Natural assets (read well without intervention):**

- *Legs:* the universal apple asset. Often lean and proportionally slim. The single strongest natural asset most apple users have.
- *Ankles:* often slim. Cropped pants, slim heels, ankle straps work.
- *Calves:* typically lean. Knee-length and below-knee hems show this asset.
- *Décolletage and collarbones:* often a natural asset; sits above the midsection.
- *Bust (when proportional and supported):* often fuller, becomes an asset with bra support and appropriate necklines.
- *Shoulders:* often proportional or narrower than midsection.
- *Face and neck:* with right neckline, becomes the focal point.

**Features that become assets when used intentionally:**

- *Vertical line:* monochromatic outfits, long open jackets and dusters, vertical seams, long necklaces. Central styling tool for apple.
- *High waist position (above the midsection):* empire-style break that visually shortens the upper torso.
- *Low waist position (below the midsection):* high hip break that bypasses midsection volume.
- *Featured legs as primary focus:* knee-length and shorter skirts, fitted pants showing leg line, slim trousers, ankle reveal.
- *Statement upper body:* draws attention to the face and upper chest. Statement earrings, long necklaces ending above the bust, structured shoulders (for non-top-heavy variation).

**Override conditions:**

- *Legs not an asset:* rare but possible — user covers legs in exposure, refuses short/knee lengths. Suppress short-length defaults. Surface featuring through alternative zones.
- *Bust not for featuring:* if user signals bust to be minimized. Surface higher-but-detailed necklines, layering, vertical line emphasis.
- *Midsection to be acknowledged or featured:* uncommon but real (body-positivity styling, confident dressers). Surface fitted dresses with structural support, skim-fit construction.

**Featuring-zone signals from the questionnaire (cross-body framework):**

- *Legs named:* amplify aggressively. Apple's strongest asset confirmed. Surface short A-line, slim pants, knee-length skirts, ankle reveal items.
- *Décolletage named:* amplify. Surface open V, scoop, deep necklines. Resolves the open-neckline depth question for apple.
- *Bust named:* unlocks bust-featuring. Surface deeper open necklines at exposure-appropriate depth. Critical for full-bust apple.
- *Shoulders named:* surface structured shoulder pieces (caution: not for top-heavy variation).
- *Arms named:* surface sleeveless and arm-revealing cuts (often appropriate since arms can be lean even on fuller apple).
- *Face/collarbone named:* surface open necklines, statement jewelry, items that pull attention up.
- *Back named:* less commonly named for apple; if named, surface back-detail items.
- *Midsection named:* rare confident-feature signal. Unlocks fitted dresses with structural support, skim-fit construction, items that don't hide the midsection. Geometry rules still apply to execution — filter thin clingy fabric that reveals every contour without supporting the silhouette, and items that lack structural integrity for the featuring to read intentionally. Goal shifts from "skim midsection" to "feature midsection well"; "well" still requires structural support and intentional construction.
- *Hips/seat named:* very unusual for apple (typically flat). Suggests user wants to feature lower body despite the geometry; surface hip-emphasis cuts cautiously.
- *"Nothing in particular":* especially important for apple. Conservative defaults; vertical line emphasis; legs-feature surfacing as default (apple's geometric default asset); hero-weighted recommendations.

## 4. Visual Risks (default, before strategy modulation)

**Silhouettes that fight this body type:**

- *Tight tops that cling to the midsection:* fitted ribbed tees, bodycon tops, thin clingy fabric on torso — the #1 universal apple failure.
- *Tucked tops at the natural waist:* horizontal line at widest point. Full tuck almost always fails; half-tuck and French tuck with longer top can work if positioned correctly.
- *Cropped tops at the natural waist:* same problem.
- *Belts at the natural waist:* emphasizes width. Heavy belts especially fail.
- *Bodycon dresses:* follow every contour. Universal failure for most apple users.
- *Empire-waist tops and dresses with a tummy below the seam:* the seam draws attention to the midsection directly below. Empire works only when no significant midsection volume below the bust.
- *Drop-waist dresses:* falls at lower edge of midsection — emphasizing the widest point.
- *Built-in waist seams at the natural waist:* same as belt at natural waist.
- *Shift dresses cut without flare:* column from shoulder to knee lacking the flare needed to skim midsection.
- *Boxy oversized tops without structure:* hide body but read as "lumpy."
- *Tunic dresses without shape:* same problem if lacking vertical line or structural break.
- *Pleats at the front waist:* add bulk at midsection transition.
- *Frills, ruffles, embellishment at the midsection:* draw attention to the widest point.
- *Horizontal stripes across the midsection:* widen visually.
- *Patch pockets at the midsection or above:* bulk at wrong zone.
- *Big buttons or front detail at midsection:* visual clutter at focal point to avoid.

**Construction details that fail:**

- Heavy embellishment at bust line that draws eye down into midsection
- Horizontal seaming across the midsection
- Heavy ruffles or peplum at the natural waist
- Double-breasted blazer with buttons across midsection
- Stiff fabric across bust and midsection that holds away (barrel effect)

**Fabric behaviors that fail:**

- Thin clingy fabric across midsection
- Stiff structured fabric that doesn't drape
- Thick, bulky knits across the torso
- Heavy embellishment on upper body ending at midsection
- Synthetic fabrics that don't breathe and cling when warm

**Necklines that fail (default):**

- High closed necklines (turtleneck, mock neck, crew neck) on full-bust apple — create wall, emphasize bust-midsection connection.
- Halter drawing all attention to bust line without vertical break.
- Boat necks on full-bust apple.
- Round jewel necklines at collarbone (don't create vertical break).

**Length traps:**

- For petite apple: midi skirts hit at calf-widest; mini reads disproportionate; tunic tops without compensation hit at hip-widest.
- For tall apple: standard tunic lengths run short; standard pants often too short.
- For mid-height: standard knee-length usually works.

**Override conditions:**

- *Bodycon, tight tops, tucked tops at waist:* hero items in confident-feature mode (rare).
- *Empire waist:* works for slim apples or those without significant tummy below the bust.
- *Wrap dresses:* depends on construction. Wrap that ties at natural waist fails; wrap with empire-position tie or draped front that skims can work.
- *Skinny jeans:* work when paired with long tunic tops, dusters, or long open layers covering midsection.

## 5. Strategy Modulation

### Trace

**What trace means for this body type:**

The riskiest strategy for apple. Trace honors the body's natural shape — but apple's natural shape is exactly the proportion problem most users want to manage. Trace tops will trace the midsection; trace bottoms will trace the lean legs (which is fine — but midsection trace creates the failure). A user picking trace-only is signaling (a) very slim apple, (b) confident dresser, or (c) doesn't realize what trace will do.

**What works under trace:**

- Slim trousers (legs are lean)
- Fitted bootcut and flare pants
- Slim pencil skirts when worn with tunic or long top covering midsection
- Skim-fit tops in fluid fabric (not clinging, but following body softly)
- Wrap tops where the wrap creates vertical line and fabric drapes rather than clings

**What fails under trace:**

- Tight fitted tops at the midsection
- Bodycon dresses
- Tucked-in fitted tops
- Fitted shift dresses
- Anything that closely follows midsection contour

**Special considerations:**

- Trace works for apple on the lower body but fails on the upper body/midsection. Half-trace approaches — fitted legs + skim-fit torso — are essentially the apple uniform.
- A trace-only user signals limited strategy options. Hero-weighted, careful focus on items that flatter without clinging at midsection.

### Anchor

**What anchor means for this body type:**

Apple anchor is the trickiest of all body types. The body doesn't have a natural waist, and anchoring at the natural waist creates the worst failure (line at widest point). Apple anchor almost always means anchoring above or below the natural waist — empire (under bust) or low-anchor (high hip).

**Hard vs. soft anchor:**

*Empire anchor (under the bust):*
- Works for slim/lean apple without significant tummy below the bust
- Works for apple with smaller bust who can create a column from under-bust down
- Fails for apple with full bust AND full tummy — empire seam emphasizes the connection

*Low anchor (at the high hip):*
- Tunic tops ending below the midsection at the high hip create visual break bypassing midsection
- Long open jackets and cardigans hitting at high hip work as low anchors
- Tops with seam detail or color block at high hip create implied anchor below the widest point

*Natural waist anchor:*
- Almost always fails for apple
- Exception: very specific structured construction that physically compresses while creating shape — mostly evening wear, rare in everyday wardrobe

**Specific anchor moves that work:**

- Empire-waist tops and dresses (gated by tummy presence)
- Tunic tops ending below the midsection
- Long open dusters or cardigans creating vertical line + low break point
- Tops with vertical seam detail
- Half-tucked tops where the tuck point is below the natural waist
- Layered looks where inner layer covers midsection and outer layer creates structure

**Anchor moves that fail:**

- Belts at the natural waist (almost universally)
- Wide belts at the natural waist (severe failure)
- Drawstring at natural waist
- Built-in waist seams at natural waist
- Tucked-in tops with full tuck at natural waist
- Cropped tops at natural waist
- Drop-waist hitting at the lower stomach

**Special considerations:**

- Apple anchor is more about avoiding bad placement than creating new anchor. Most apple uniforms work through vertical line + skim fabric rather than traditional waist emphasis.
- "Anchor below the widest point" principle from midsection-prone rectangle applies as default.

### Sculpt

**What sculpt means for this body type:**

Potentially useful but rarely heroic. Structured construction can impose smoother silhouette through midsection, but sculpt that imposes a defined waist where there isn't one tends to fail. Most useful sculpt: structural support that compresses or smooths without creating fake waist.

**What good sculpt looks like for this body:**

- Tailored blazers with structured shoulders and skim-fit through torso
- Fit-and-flare dresses where fit is at the bust line (empire) and flare bypasses midsection
- Structured sheath dresses that smooth the midsection
- Shapewear or supportive undergarments under draped fabric
- Princess seams running vertically through torso

**What bad sculpt looks like:**

- Sculpt with built-in waist seam at natural waist
- Sculpt with heavy structured shoulders creating "barrel" silhouette
- Bodycon sculpt following the midsection
- Corseted bodice ending at natural waist
- Empire sculpt on apple with full tummy

**Special considerations:**

- For slim apple, sculpt rarely needed.
- For soft apple, sculpt becomes valuable as structural support.
- Sculpt for apple isn't about creating curves; it's about smoothing the existing silhouette.

### Edge

**What edge means for this body type:**

The strongest and most useful strategy for apple. Edge redirects attention away from the midsection by featuring alternative zones — legs, décolletage, face, ankles, shoulders. Apple has unusually clear featuring potential because the natural assets (legs especially) are pronounced relative to the midsection.

**Featuring modes (the standard apple approach):**

*Legs as primary feature (almost universal):*
- Knee-length and shorter A-line skirts
- Knee-length and shorter A-line dresses
- Slim trousers showing the leg line
- Cropped pants with ankle reveal
- Slim pencil skirts with appropriate top coverage
- Heels and pointed shoes elongating the leg

*Décolletage as feature:*
- Open V-necks, deep V-necks
- Scoop necks
- Sweetheart necklines (for full-bust apple with support)
- Open button-downs
- Statement necklaces ending above the bust

*Face and upper body as feature:*
- Statement earrings
- Bold lipstick or strong eye makeup
- Hair styled to frame the face
- Open necklines drawing eye to the face
- Hats and headwear pulling focus up

*Vertical line as feature:*
- Monochromatic outfits
- Long open jackets and dusters
- Long necklaces creating vertical line
- Vertical seam detail
- Color blocking with darker midsection panel within lighter overall outfit

**Three-mode framework for upper-body featuring:**

For each named upper-body zone (décolletage, shoulders, arms, bust):
- *Reveal mode:* deep V, sleeveless, off-shoulder, open back at appropriate registers
- *Sophisticated mode:* moderate V at collarbone, three-quarter sleeves, sheer panels, keyhole details
- *Coverage mode:* high necklines with detail, long sleeves with structure, accessory focus

Most apple users operate in sophisticated or coverage mode for upper body, paired with reveal or sophisticated mode for legs.

**Edge moves that work:**

- Knee-length A-line dresses with V-neck (legs + décolletage)
- Slim pants with long open duster and statement earrings (legs + vertical line + face frame)
- Tunic + slim pants + heels (legs featured, midsection skimmed, ankles visible)
- Wide-leg pants + fitted blazer + statement necklace (balanced silhouette with face-frame edge)
- Knee-length skirt + structured top with V-neck

**Edge moves that fail:**

- Edge moves drawing attention to midsection (statement belts at waist, embellishment, contrast color at waist)
- Statement features at bust or hip without compensation that bypasses midsection

## 6. Combinational Rules

**Body + strategy combinations:**

- *Apple + trace:* surface skim-fit trace items, fitted lower body. Filter clinging-at-midsection. Most restrictive for apple.
- *Apple + anchor:* surface empire styles (gated by tummy), tunic-length tops, long open layers, vertical seam details. Filter natural-waist anchors aggressively.
- *Apple + sculpt:* surface structured pieces that smooth without cinching. Filter sculpt with natural-waist seams.
- *Apple + edge:* surface aggressively. Strongest strategy. Legs, décolletage, face-frame, vertical line all primary tools.
- *Apple + trace only:* highest-restriction. Surface hero items with midsection management.
- *Apple + multiple strategies:* widen catalog; sophisticated apple dressers use edge + structured layering + occasional empire.

**Body + fit combinations:**

- *Apple + close everywhere:* fights body almost entirely. Requires featuring through accessories rather than silhouette.
- *Apple + close top + relaxed bottom:* unusual for apple. Works only when relaxed bottom is structured and close top is in compressive supportive fabric.
- *Apple + relaxed top + close bottom:* classic apple uniform. Tunic + slim pants. Surface aggressively.
- *Apple + relaxed everywhere:* requires compensation appropriate to selected strategy. Anchor strategy needs anchor mechanism above or below the midsection (empire when slim, tunic length, long open layer). Edge strategy needs multiple strategic features redirecting from midsection (V-neck featuring décolletage, slit on long dress featuring legs, vertical line through fabric texture, asymmetric hem). Sculpt strategy needs structured outer over relaxed base. Pure shapeless without any compensation = failure.

**Body + fabric combinations:**

- *Apple + cling-averse:* filter thin clingy across torso; surface flowing drape and structured fabrics with body.
- *Apple + heavy-averse:* applies to upper body. Filter heavy thick knits; surface fine gauge knits, fluid drape, lightweight structure.
- *Apple + fluid drape + structure preference:* ideal — fluid fabric draping over midsection + structured layering.
- *Apple + bust-support importance:* universal for full-bust. Surface items with structural bust support.

**Body + bust + exposure combinations:**

- *Apple + names bust + high exposure preference:* deep V, plunging styles, open necklines. Bust featured + chest panel broken vertically.
- *Apple + names bust + medium exposure + chest not flagged covered:* moderate-depth open necklines (V at collarbone-to-mid-chest, scoop at clavicle).
- *Apple + names bust + low exposure or chest covered:* higher slim necklines with vertical break (button placket, vertical detail, layered jewelry).
- *Apple + smaller bust + any exposure:* most necklines accessible. Vertical line and midsection management still matter.

**Body + leg-featuring combinations:**

- *Apple + legs uncovered + edge:* short and knee-length hems surfaced aggressively. Legs are primary asset.
- *Apple + legs covered:* significant constraint. Apple's strongest featuring zone unavailable. Surface vertical line emphasis, face-frame, décolletage instead. Long pants with leg-line emphasis substitute.
- *Apple + legs featured at sophisticated mode:* surface fitted bootcut, slim trousers, knee-length skirts with appropriate slit, fitted pants in interesting fabric, ankle reveal.
- *Apple + legs featured at reveal mode:* surface mini A-line, short A-line dresses, knee-and-above skirts, leg-revealing cuts. Reveal mode for legs more accessible for apple than any other body type.

**Body + exposure combinations (other zones):**

- *Apple + chest covered:* surface vertical-line tops, layering, V-shapes within closed neckline.
- *Apple + back uncovered + edge:* less of a signature unlock than for pear. Available when user signals back fine to feature; not default.
- *Apple + arms covered:* surface long sleeves; three-quarter sleeves work as midsection-shortening tool.
- *Apple + midriff covered:* universal for apple. Filter crop tops, midriff-baring items.

**Body + featuring-zone combinations:**

- *Apple + legs named:* amplify aggressively. Almost universal for apple users.
- *Apple + décolletage named:* surface open necklines at user's mode (reveal/sophisticated/coverage). Resolves the open-neckline depth question.
- *Apple + bust named:* surface bust-featuring at exposure-appropriate depth.
- *Apple + shoulders named:* surface structured shoulders (caution for top-heavy variation).
- *Apple + arms named:* surface sleeveless when comfortable; otherwise sophisticated-mode three-quarter with fitted construction.
- *Apple + midsection named (rare):* confident-feature mode. Unlocks fitted dresses with structural support, items that don't hide midsection. Still filters thin clingy fabric and items without structural integrity. Featuring intent unlocks the access; geometry still informs the execution.
- *Apple + "nothing in particular":* especially important for apple. Conservative defaults; surface legs-feature as default geometric asset; vertical line emphasis; hero-weighted.

**Body + variation modulators:**

- *Slim/lean apple:* broader tolerance; empire works; mini hems easier; some trace items accessible.
- *Soft/fleshy apple:* stricter midsection coverage; structured layering critical; stretch fabrics important.
- *Top-heavy apple:* apply inverted triangle softening on top (V-necks, no structured shoulders) AND apple midsection management.
- *Full-bust apple:* bust support critical; deeper open necklines work; high closed necklines filtered.
- *Post-pregnancy/post-menopause apple:* respect that midsection sensitivity is often higher.
- *Petite apple:* short jackets at high hip (not natural waist); knee-length skirts; vertical line critical.
- *Tall apple:* longer tunic and duster options; more length for vertical line; midi skirts work better.

## 7. Hero Categories

**Hero items (consistent across apple/oval):**

- A-line dresses (knee or just above knee)
- Fit-and-flare dresses with empire bodice (gated by tummy)
- Sheath dresses in skim-fit fabric (not clinging)
- Tunic tops ending below the midsection
- Long open dusters, cardigans, and jackets
- Slim trousers and tapered pants in mid-rise
- Bootcut and flared pants in mid- or high-rise
- Wide-leg trousers in fluid fabric
- Knee-length A-line skirts
- Pencil skirts (with tunic-length top covering midsection)
- Soft drape blouses in fluid fabric
- V-neck and scoop neck tops
- Tailored blazers worn open over fitted base
- Wrap tops where wrap creates vertical line without cinching at natural waist

**Hero necklines:**

- V-neck (especially deep V) — breaks chest panel vertically
- Scoop neck — open and softening
- Sweetheart (for full-bust apple with support, at appropriate exposure)
- Surplice and wrap necklines
- Open button placket (vertical break)
- Cowl neck (drapes softly without bulk)
- Asymmetric necklines
- Off-shoulder for users comfortable with shoulder reveal

**Necklines to avoid (default):**

- High closed crew, mock, turtleneck on full-bust apple
- Boat neck on full-bust apple
- Halter without compensation
- Round jewel neckline at collarbone
- High necks with heavy embellishment

**Hero sleeves:**

- Three-quarter sleeves (universal apple recommendation for visual midsection-shortening)
- Long fluid sleeves
- Bishop sleeves with structure
- Set-in sleeves with subtle shoulder
- Bell sleeves (volume at wrist doesn't drop to midsection)

**Sleeves to avoid:**

- Drop-shoulder dolman
- Heavy puff sleeves at shoulder (amplifies top-heavy reading)
- Cap sleeves on top-heavy apple
- Tight short sleeves cutting into upper arm
- Very fitted sleeves on soft-arm apple

**Hero pant silhouettes:**

- Mid-rise straight (rise doesn't cut into midsection)
- Mid-rise bootcut
- Mid-rise wide-leg
- High-rise with wide flat smoothing waistband (when comfortable)
- Flared jeans (balances narrow legs with wider midsection)
- Slim trousers (legs are the asset)

**Pants with specific gating:**

- Skinny jeans: work with long tunic top or duster covering midsection; filtered with cropped or fitted tops.
- High-rise: gated by comfort — smoothing waistband works; cuts into midsection fails.

**Pants to avoid:**

- Pants with pleats at front waist (adds midsection bulk)
- Tight skinny jeans without long top compensation
- Low-rise (sits at lower edge of midsection)
- Heavy waistbands cutting into midsection
- Tapered pants without flare (emphasizes narrow-leg-wide-torso mismatch)

**Hero dress and skirt silhouettes:**

- A-line dresses (knee length)
- Fit-and-flare with empire bodice (gated by tummy)
- Sheath dresses in skim-fit fabric
- Wrap dresses (with vertical line wrap, not natural-waist cinch)
- Shift dresses with open neckline and slight A-line flare
- Knee-length A-line skirts
- Bias-cut skirts (drape vertically)
- Pencil skirts with tunic top
- Maxi dresses with empire bodice and column skirt

**Dresses and skirts to avoid:**

- Bodycon dresses
- Tight pencil skirts without top coverage
- Tiered or ruffled skirts that add bulk at waist
- Mini skirts hitting at thigh-widest (debated — some apples do this with confidence)
- Heavily gathered or pleated at natural waist
- Empire dresses with significant tummy

**Hero outerwear:**

- Long open dusters
- Long open cardigans (knee length or longer)
- Tailored blazers worn open over fitted base
- Knee-length straight coats
- Moto jackets worn open (subtle shape without cinching)
- Trench coats with belt tied at back or worn open
- Long unstructured coats with vertical line

**Outerwear to avoid:**

- Cropped jackets at natural waist
- Double-breasted coats with buttons across midsection
- Belted coats with belt at natural waist (filter unless belt sits at empire or low position)
- Bulky shapeless coats without vertical line
- Boxy short jackets

**Hero items by strategy:**

- *Trace hero:* slim trousers + skim-fit fluid top; fitted bootcut + tunic
- *Anchor hero:* empire-waist dress (gated by tummy); tunic top + slim trouser; long open duster + simple base
- *Sculpt hero:* tailored blazer worn open + structured A-line dress; structured sheath in supportive fabric
- *Edge hero:* knee-length A-line dress + V-neck + statement necklace; slim trousers + tunic + long duster + heels; short A-line + simple top

## 8. Disqualified Categories

**Items that don't work, regardless of strategy:**

- Tight bodycon dresses
- Fitted ribbed knits across the midsection
- Tucked-in fitted tops at natural waist (full tuck)
- Cropped tops at natural waist
- Wide belts at natural waist
- Heavy chunky belts at natural waist
- Drop-waist dresses (typically)
- Empire-waist dresses for full-tummy apple
- Pleated front trousers with heavy pleating at waist
- Tiered or ruffled skirts gathered at natural waist
- Halter tops pulling attention to bust without vertical break
- Bandeau and strapless without compensating coverage
- Tube dresses
- Wrap dresses tying tightly at natural waist
- Bodycon midi dresses

**Items disqualified by specific answer combinations:**

- Empire-waist disqualified for: apple with significant tummy below the bust
- Skinny jeans disqualified for: apple + cropped top preference + no long-top coverage
- Mini skirts disqualified for: petite apple unless explicit confident-feature signal
- Pencil skirts disqualified for: apple + relaxed top preference
- High closed necklines disqualified for: full-bust apple + no vertical line compensation
- Belts at natural waist disqualified for: any apple unless very specific structured construction

**Items disqualified by featuring-mode signals:**

- Midriff-exposing crop tops disqualified for: apple + cover mode on midriff (default)
- Crop tops available for: apple + reveal or sophisticated mode on midriff (rare opt-in)
- Bodycon dresses disqualified for: apple + cover mode on midsection (default)
- Bodycon available for: apple + reveal mode on midsection (very rare explicit opt-in)

**Items that look right but disappoint:**

- *Wrap dresses on apple:* marketed as universal hero, but wrap tie often hits at natural waist (widest point) and emphasizes width. Surface wraps with vertical-line construction or empire-tied wraps; filter wraps that cinch at natural waist.
- *Empire-waist dresses on apple:* mainstream styling recommends empire universally, but for full-tummy apple the empire seam emphasizes midsection directly below. Gate by tummy presence.
- *Boxy tunics:* hide the body but read as shapeless and "lumpy." Surface tunics with structure (princess seams, vertical detail, slim sleeves).
- *Bodycon with shapewear:* shapewear compresses but bodycon still reveals every contour. Surface skim-fit alternatives.
- *Belted blazers:* belt at natural waist creates the failure. Surface unbelted blazers worn open or with belt tied at back.
- *"Universal" maxi dresses:* maxi dresses that gather at natural waist fail. Surface column maxis with empire bodice or vertical-line construction.

## 9. The Uniform

**Daytime / casual uniform (mid-height, mid-sophistication, mixed strategy):**

Mid-rise straight or bootcut pants in dark wash, fitting at the seat without back gap and not cutting into midsection at the waistband. Leg shape shows lean lower body — straight or with subtle bootcut flare.

On top, tunic-length blouse or top in fluid fabric (silk, cotton voile, fine cotton, soft modal jersey) ending at the high hip, just below widest point of midsection. V-neck or scoop neck breaking chest panel vertically. Three-quarter sleeves keep proportions long.

Over the top, open long cardigan, duster, or tailored blazer worn unbuttoned and unbelted. Outer layer creates vertical line; open front shows strip of inner layer creating implied column. Outer layer ends below high hip — knee length for duster, just below high hip for tailored blazer.

Statement necklace ending above the bust line. Statement earrings drawing eye to the face.

Footwear: pointed flats, pointed ankle boots, or low pointed heels.

**Variations by strategy:**

- *Trace-primary apple:* tunic top + slim trouser. Specific selection because trace is restrictive.
- *Anchor-primary apple:* tunic + slim bottom + statement vertical-line necklace; long open duster over fitted slim base.
- *Sculpt-primary apple:* tailored blazer worn open over structured A-line dress; structured sheath dress in supportive fabric.
- *Edge-primary apple:* knee-length A-line dress + deep V + statement earrings; slim trouser + tunic + long duster + heels.

**Variations by register:**

- *Work:* tailored slim trousers + fluid silk blouse + open tailored blazer; sheath dress in skim-fit fabric with V-neck; knee-length A-line dress with three-quarter sleeves.
- *Evening:* knee-length A-line dress + statement jewelry; bias-cut maxi with empire bodice and vertical column skirt; structured cocktail dress with V-neck and skim-through-midsection construction.
- *Occasion:* A-line dresses, knee-length sheath dresses, empire-bodice maxi dresses (gated by tummy).

**Variations by season:**

- *Summer:* fluid sleeveless or short-sleeve tops in cotton voile or silk + slim trousers; A-line cotton sundresses with V-neck; cropped wide-leg pants + simple top + statement accessories.
- *Winter:* fine-gauge knit tunics + slim trousers + long wool coats; sweater dresses in skim-fit fabric (not clingy) with three-quarter sleeves; structured wool blazers over fluid base + slim trousers.

## 10. Inference Notes for the Recommender

**Default rules that fire on apple identification alone:**

1. Skim the midsection — central rule.
2. Filter natural-waist anchors aggressively when anchor is the strategy the item is executing: belts at natural waist, drawstring at natural waist, tucked tops at natural waist, cropped tops at natural waist, built-in waist seams at natural waist. These items fail because they try to anchor at apple's widest point. When an item executes edge or other strategies (a flowy tunic with strategic openings at neckline and slits, executing edge), it's not subject to anchor-failure rules even if it lacks waist construction.
3. Surface vertical-line items aggressively: long open dusters, long cardigans, monochromatic outfits, vertical seam construction, long pendant necklaces.
4. Legs are typically the strongest asset; surface leg-featuring items.
5. Three-quarter sleeves preferred (universal styling-source recommendation).
6. V-necks, scoops, and open necklines break the chest-midsection connection.
7. Empire-waist gated by tummy presence: surface for slim/lean apple; filter for full-tummy apple.
8. Wrap dresses gated by construction: surface when wrap creates vertical line; filter when wrap cinches at natural waist.
9. Tunic-length tops preferred over hip-length and waist-length.
10. Bootcut and flared pants weighted up to balance narrow legs.
11. Skinny jeans gated by compensating top length.
12. Stretch fabrics with body weighted up; thin clingy fabrics filtered for torso pieces.
13. Petite + apple: short jackets at high hip (not natural waist); knee-length skirts; vertical line critical.
14. Full-bust + apple: bust support critical; open necklines required; high closed necklines filtered.
15. Top-heavy apple: apply inverted triangle softening on top AND apple midsection management.
16. Standard pant rises gated by comfort: smoothing waistband works; rises that cut into midsection fail.

**Modulators that change defaults:**

- *Strategy selection:* trace highly restricted; anchor about avoiding bad placement; sculpt mostly structural support; edge primary tool.
- *Fit preferences:* relaxed top + close bottom is the natural apple uniform.
- *Fabric importance:* high importance + soft drape → skim-fit fluid weighted up; high importance + structured → tailored layering surfaced.
- *Bust signal modulates neckline access:* full-bust has tighter neckline rules; smaller-bust has broader access.
- *Tummy signal modulates empire access:* empire fails for full-tummy apple, works for slim apple.
- *Featuring-zone signals:* named upper-body zones modulate neckline and feature selection; legs almost universally named — surface aggressively when named.
- *Per-zone reveal mode:* detected through featuring-zone + exposure + length preferences. Default to sophisticated when signals are ambiguous.

**Sophistication and restrictiveness signals:**

- Multi-strategy + flexible answers + clear edge-featuring zones → widen catalog
- Trace-only + multiple covered zones + full-bust + soft apple → tighten significantly
- Strong leg-featuring signal → unlock strongest apple styling moves
- No leg-featuring signal (legs covered) → significant constraint; surface vertical line and face-frame edge

**Risk-scanning patterns common to apple:**

- Whether items cling to or cinch at the midsection
- Whether construction creates horizontal line at natural waist
- Whether silhouette creates vertical lines or horizontal ones
- Whether upper body break is at right level (under bust for slim; at high hip for everyone)
- Whether leg asset is featured or hidden
- Whether bust support is appropriate
- Whether fabric drapes over midsection or stands away

**Common "knows the trick" non-traditional moves:**

- Sophisticated apple dressers may wear bodycon with confidence (long open duster over bodycon, statement accessories, confident posture)
- May use color blocking strategically — darker midsection panel within lighter outfit
- May wear monochromatic outfits in textured fabrics (lace overlay, ribbed knit)
- May use vertical-line necklaces and accessories aggressively as constant styling tools
- May wear empire styles confidently when bust is supported and skirt drapes vertically
- May feature midsection through structured shapewear under fluid drape

**On rule restrictiveness vs. user variation:**

Apple is the most styling-rule-restrictive body type in mainstream literature — the universal "skim midsection, feature legs, vertical lines" framework has near-100% agreement across sources. Apple users also have unusually clear featuring potential: legs almost universally an asset, vertical line works for everyone, V-necks suit nearly all apple variations.

Rules should be confident about filtering failure modes (natural-waist cinches, clinging, horizontal lines) and confident about surfacing hero categories (A-line, V-necks, vertical line, leg-featuring, three-quarter sleeves). User variations modulate execution but rarely overturn core rules.

The hardest user to serve is the apple who wants to dress in current trends that fight her body (cropped tops, bodycon, belted-at-waist). System should surface modified versions where possible.

## 11. Open Questions and Edge Cases

**Cases the rules don't yet handle:**

- *Apple + significant weight loss:* if proportions shift toward rectangle. Re-classify based on current geometry.
- *Apple + recent weight gain:* user was rectangle or hourglass, now apple. May resist apple recommendations.
- *Apple + pregnancy:* not the same body type; maternity has own rules.
- *Slim apple who's actually rectangle:* if midsection only mildly the widest, may be functionally rectangle with mild midsection-prone signal.
- *Apple with very flat seat:* may benefit from pear styling techniques in reverse (adding back-pocket detail to lift seat shape).
- *Apple with unusually defined waist that's still wider than bust/hips:* curved torso but still apple-classification. Hourglass-style anchor at actual waist, but keep apple's other rules.

**Borderline body-type identifications:**

- *Apple vs. rectangle midsection-prone:* threshold is whether midsection projects beyond shoulders and hips, or just equal to them. Projecting = apple. Equal but soft = rectangle with midsection modulator.
- *Apple vs. inverted triangle top-heavy:* if shoulders wider than midsection, inverted triangle. If midsection wider than shoulders (and hips), apple.
- *Apple vs. hourglass with weight gain:* if waist still smaller than bust and hips, hourglass with midsection-prone. If waist equal to or larger than bust/hips, apple.

**Things behavior data should resolve:**

- Tummy intensity (slim apple vs. full-tummy) — affects empire-access threshold
- Bust featuring preference and depth tolerance
- Leg-featuring intensity (most users feature heavily, but some prefer slim pants only over knee-and-shorter skirts)
- Bodycon and tight-fit tolerance
- Crop top tolerance
- Belt tolerance (default filter at natural waist; learn whether user buys/wears belts despite the rule)
- Wrap dress tolerance (different wraps work differently)
- Vertical line aggressiveness (some users use long dusters constantly; others stay minimal)
- Three-quarter sleeve preference (universal recommendation; learn whether individual user feels it's frumpy)
- Tucked vs. untucked preference
- High-rise vs. mid-rise comfort
- Whether named features actually drive behavior (some users name features they like in principle but don't actually shop for; learn from purchases and saves)

