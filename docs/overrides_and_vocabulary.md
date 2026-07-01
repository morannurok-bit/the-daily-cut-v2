# Override Patterns & Vocabulary — The Daily Cut

How body-type-risky items become available to risky body types via user signals. Built and locked during V2 catalog tagging.

---

## Purpose

The `body_type_risky` tag means an item's geometric defaults work against a body type's structure. Without intervention, the engine filters those items out for that body type.

Override patterns are the structured exception logic: under specific user signal combinations, a risky-tagged item surfaces anyway because the user has signaled she'd wear it well despite the body-default concern.

---

## When to Add Overrides

Add overrides when **both** conditions are true:

1. The body-default risk is *overcomable* by user choice (she can wear the item in a way that works for her body)
2. There's a clear signal pattern that distinguishes the user who'd wear it well from a user who'd struggle

**Don't add overrides when:**
- The body-default risk is structural (e.g., high-rise rigid cotton at oval's midsection — no user signal makes the fabric give where it doesn't)
- The user has reasonable alternatives elsewhere in the catalog
- The override conditions would be too thin to meaningfully filter

When no override is added, the body type stays risky and the item is cleanly filtered for that body type. This is honest — not every risky tag needs an override.

---

## Override Vocabulary — 4 Standardized Types

### 1. `acceptance_and_celebration`

User accepts the structural commitments of the item (cut, rise, closeness, length) AND celebrates a featured zone that the item engages.

**Use when:** The body-default risk is overcomable when the user actively wants to feature the zone the item engages. The celebration is the unlock.

**Standard condition structure:**
- Acceptance condition(s) — pants_cuts_accepted, closeness_to_body_X_accepted, bottom_rise_accepted, length_skirts_dresses_accepted
- Featuring condition — featuring_zones includes [relevant zone(s)]

**Example — Item 13 (faux suede mini skirt, triangle risky):**
```
{
  body_type: triangle,
  override_type: acceptance_and_celebration,
  conditions: [
    "length_skirts_dresses_accepted includes short",
    "closeness_to_body_bottom_accepted includes close",
    "featuring_zones includes legs OR hips_and_curves"
  ]
}
```

She accepts the structural commitments (short hem, close fit) AND celebrates the lower body (legs or hips). The mini skirt's hip-amplifying default is overcome by her celebrate intent.

---

### 2. `acceptance_and_intent_formula`

User accepts structural commitments AND has committed to a specific Q6 proportion formula that makes the item's wearing pattern work for her.

**Use when:** The unlock is the user's wearing pattern commitment (Intent 4, Intent 5, Intent 6 step-back register), signaled via Q6 rather than via featured zone celebration.

**Standard condition structure:**
- Acceptance condition(s)
- Q6 condition — `Q6 = [formula]`
- Optional: featuring zone (when Q6 alone is insufficient to unlock)

**Example — Item 25 (Zara interlock co-ord set, triangle risky):**
```
{
  body_type: triangle,
  override_type: acceptance_and_intent_formula,
  conditions: [
    "length_skirts_dresses_accepted includes short",
    "featuring_zones includes legs",
    "Q6 = top_and_bottom_same"
  ]
}
```

She commits to the balanced proportion (Q6 = top and bottom same) AND celebrates legs AND accepts short hems. Combined with her Q7 closeness signals (which determine whether she's in step-back-loose or balanced-close mode), the mid-thigh hem at her widest zone is overcome by her proportion commitment + leg celebration.

---

### 3. `acceptance_celebration_and_formula`

User accepts structural commitments AND celebrates featured zone AND commits to Q6 formula.

**Use when:** The body-default risk is strong enough that no single signal (celebration alone OR formula alone) is sufficient. Requires both.

**Standard condition structure:**
- Acceptance condition(s)
- Featuring zone condition
- Q6 formula condition

**Example — Item 23 oval override (slim cigarette jeans, oval risky):**
```
{
  body_type: oval,
  override_type: acceptance_celebration_and_formula,
  conditions: [
    "pants_cuts_accepted includes slim",
    "closeness_to_body_bottom_accepted includes close",
    "featuring_zones includes legs",
    "Q6 = more_room_on_top_slimmer_bottom"
  ]
}
```

For oval, slim cigarette is risky default. She needs both: legs celebration (her asset) AND Intent 5 formula commitment (knows she'll wear oversized on top to balance). Either alone isn't enough commitment.

---

### 4. `acceptance_and_fired_intent`

User accepts structural commitments AND has fired a specific intent that aligns with the item's primary register.

**Use when:** The item's primary register (typically Intent 6 step-back or Intent 9 cover-with-opening) makes the body-default risk moot because the outfit isn't engaging the body in the way that creates the risk.

**Standard condition structure:**
- Fired intent condition — `fired_intents includes intent_X`
- Acceptance condition(s) for the item's fit

**Example — Item 1 (linen short-sleeve shirt, triangle risky):**
```
{
  body_type: triangle,
  override_type: acceptance_and_fired_intent,
  conditions: [
    "fired_intents includes intent_6 OR intent_9",
    "closeness_to_body_top_accepted includes relaxed OR oversized"
  ]
}
```

For triangle, hip-length linen shirt is risky because the hem terminates at her widest zone. But if she's fired Intent 6 (step-back) or Intent 9 (cover-with-opening), the outfit's mode isn't engaging body geometry — the hip-line termination is no longer a problem because no part of the outfit foregrounds the body.

---

## Condition Vocabulary

### Acceptance conditions

These check that the user accepts the item's structural commitments (didn't exclude them in her preferences).

- `pants_cuts_accepted includes [slim/straight/wide/cigarette/bootcut/flared/barrel]`
- `closeness_to_body_top_accepted includes [tight/close/relaxed/oversized]`
- `closeness_to_body_bottom_accepted includes [tight/close/relaxed]`
- `bottom_rise_accepted includes [low/mid/high]`
- `length_skirts_dresses_accepted includes [very_short/short/3_4/long/sleeveless]`
- `exposure_covers does NOT include [arms/shoulders/back/chest/midriff/legs]`

### Celebration conditions

These check that the user's named featuring zones overlap with the item's featuring zones.

- `featuring_zones includes [zone]` — single zone
- `featuring_zones includes [zone1] OR [zone2]` — any of multiple zones

Available zones: `decollete`, `bust`, `shoulders`, `arms`, `waist`, `hips_and_curves`, `seat`, `legs`, `back`

### Formula conditions

These check the user's Q6 proportion commitment. Q6 is purely about proportion balance between top and bottom; it does NOT carry closeness information (which is handled separately via closeness_to_body_X_accepted at the hard filter layer).

- `Q6 = slimmer_top_more_room_on_bottom` → Intent 4 amplification proportion (was previously `fitted_top_more_room_on_bottom`)
- `Q6 = more_room_on_top_slimmer_bottom` → Intent 5 leg-feature proportion
- `Q6 = top_and_bottom_same` → balanced proportion (combined with Q7 closeness determines exact intent — could be Intent 1 if tight, Intent 6/9 if relaxed)

The fourth option ("not much extra room") was dropped — duplicated Q7 closeness signal. The third option was reworded from "room on both" to "top and bottom the same" — the prior phrasing implied looseness, but the actual signal is balance, not looseness.

Body-traced users (Intent 1, Intent 2) signal through Q5a + Q7 closeness, not through Q6 directly. A user picking "top and bottom the same" with tight Q7 closeness fires Intent 1.

### Intent conditions

These check which intents the user has fired.

- `fired_intents includes intent_X`
- `fired_intents includes intent_X OR intent_Y`

---

## Multiple Override Blocks Per Item

An item can have multiple override blocks for the same body type when there are multiple unlock paths. Item 23 has three override blocks for triangle:

1. `acceptance_and_celebration` (celebrate-mode unlock)
2. `acceptance_and_intent_formula` (Intent 5 formula commitment unlock)
3. `acceptance_celebration_and_formula` (for oval, requiring both)

The engine evaluates each block independently. If ANY block's conditions are satisfied, the item surfaces. Multiple unlock paths give the engine flexibility while keeping each path's logic transparent.

---

## When NOT to Add an Override

Examples of when overrides shouldn't be added:

**Structural impossibility (Item 26 oval):**
ATA wide-leg cool_tlv pants are risky for oval (high-rise rigid cotton at midsection). No user signal can make rigid cotton give where the construction has none. Oval is filtered cleanly. Alternative wide-leg items exist in the catalog (Item 12 stretch denim, Item 20 drapey viscose-poly) that serve her better.

**Risk concerns no signal addresses (Item 24 oval):**
Jersey midi dress with natural-waist seam is risky for oval — the seam sits at her midsection prominence zone. No user signal overcomes that structural placement. Oval is filtered.

**Risk concerns no celebration overcomes (Item 27 inverted_triangle):**
Compact cotton tee with cap sleeves at natural shoulder edge is risky for inverted_triangle. Cap sleeves emphasize shoulder breadth structurally. No celebration redirect overcomes the geometric concern. Inverted_triangle is filtered.

These examples show: overrides aren't about being inclusive of all body types. They're about identifying the specific cases where user choice meaningfully overcomes the body-default risk. When it doesn't, filter cleanly.

---

## How Overrides Interact with Lounge Context

The new `lounge` context value (added during V2 tagging) softens body-rules risky tags in lounge browse mode. This means:

- In lounge browse mode: items surface to risky body types **without override firing**, because the body-rules concern is public-facing and doesn't apply when she's not presenting
- In all other contexts: overrides must fire for the item to surface to risky body types

Exposure preferences remain enforced across all contexts including lounge. A user who covers legs doesn't see leg-exposing items even in lounge browse — that's a personal preference, not a body-rules concern.

---

## Catalog Override Inventory (V2)

| Item | Body type | Override type |
|---|---|---|
| 1, 2, 3 | triangle | acceptance_and_fired_intent |
| 4 | inverted_triangle | acceptance_and_celebration |
| 4 | oval | acceptance_and_celebration |
| 5 | hourglass | acceptance_and_fired_intent |
| 5 | inverted_triangle | acceptance_and_celebration |
| 7 | inverted_triangle | acceptance_and_celebration |
| 7 | oval | acceptance_and_celebration |
| 8 | hourglass | acceptance_and_fired_intent |
| 8 | triangle | acceptance_and_fired_intent |
| 8 | inverted_triangle | acceptance_and_fired_intent |
| 11 | oval | acceptance_and_celebration |
| 12 | triangle | acceptance_celebration_and_formula |
| 13 | triangle | acceptance_and_celebration |
| 17, 18 | oval | acceptance_and_celebration |
| 19 | triangle | acceptance_and_intent_formula |
| 23 | triangle (path 1) | acceptance_and_celebration |
| 23 | triangle (path 2) | acceptance_and_intent_formula |
| 23 | oval | acceptance_celebration_and_formula |
| 25 | triangle | acceptance_and_intent_formula |
| 26 | triangle | acceptance_and_celebration |
| 28 | triangle | acceptance_and_intent_formula |
| 30 | triangle | acceptance_celebration_and_formula |
| 30 | oval | acceptance_and_celebration |

**Items with risky body types but no overrides (filtered cleanly):**
- Item 24: oval risky (natural waist seam at midsection)
- Item 26: oval risky (high-rise rigid cotton at midsection)
- Item 27: inverted_triangle, oval risky (cap sleeve emphasizes shoulders; close fit at midsection)
- Item 21: oval risky (close ribbed at midsection, no featured zone to leverage)

---

## Override Authoring Checklist

When writing an override for a body-type-risky item:

- [ ] Is the risk genuinely overcomable by user choice, or is it structural?
- [ ] Is there a clear signal pattern that distinguishes "would wear well" from "would struggle"?
- [ ] Have I picked the right override type (celebration / formula / both / fired intent)?
- [ ] Do the acceptance conditions cover ALL structural commitments the item requires?
- [ ] If using formula, does the Q6 value match the wearing pattern the item actually delivers?
- [ ] If using celebration, are the featured zones genuinely overlapping with what the item draws attention to?
- [ ] Could a user pass all conditions while still being structurally unsuited? (Then conditions are insufficient.)
- [ ] Could a user genuinely well-suited fail conditions? (Then conditions are over-strict.)
- [ ] Are there multiple unlock paths for the same body type? Add multiple blocks.

---

End of override patterns and vocabulary documentation.
