# The Daily Cut

A personal styling recommendation system. Given a user's diagnosis (body signals,
context, preferences), it classifies **intents** (silhouette moves), pulls candidate
items from the catalog, filters and scores them for body compatibility, and returns
ranked recommendations.

`src/engine_v2.py` is the validated **reference implementation** of the matching
pipeline — the logic there is the spec, intended to be ported to Bolt/TS. The `docs/`
folder holds the frameworks and rules that define the system's behavior.

## Repository layout

```
docs/                  Specs & frameworks (the "source of truth" for behavior)
  intent_framework_v2.1.md      Intent classification — the 8 silhouette intents
  fit_matching_model.md         Fit matching logic
  style_world_doc_v8.md         Style world reference
  style_thumbnails_v9.md        Style thumbnails
  overrides_and_vocabulary.md   Override rules & vocabulary
  styling_framework.md          Consolidated styling framework
  synthesis_layer.md            Synthesis layer (strategy model)
  body_types_rules_v2.md        Body type rules
  reference/
    body_types_rules_extracted.txt   Extracted text of the original body-types PDF

src/
  engine_v2.py         Matching engine (Layer 3) — reference implementation

assets/
  register_intensity_chart_v4.html   Register intensity chart
```

## Provenance

These files were migrated from the "The Daily Cut" project knowledge on claude.ai.
Git is now the single source of truth. When a file changes here, re-upload the updated
version to the claude.ai project knowledge so Claude works from the latest.

> Note: `docs/reference/body_types_rules_extracted.txt` is the **extracted text** of the
> original `body types rules.pdf` (the API exposed text, not the binary). It largely
> overlaps with `docs/body_types_rules_v2.md`. Keep the original PDF elsewhere if you
> need the binary.
