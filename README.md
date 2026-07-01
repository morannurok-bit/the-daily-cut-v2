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
    style thumbnails 4.pdf            Style thumbnails (source PDF)
    V2 Questions 9.pdf                Questionnaire (English)
    V2 Questions 16.pdf               Questionnaire (English, later rev)
    שאלון בעברית v2 2.pdf             Questionnaire (Hebrew)

src/
  engine_v2.py         Matching engine (Layer 3) — reference implementation

data/
  V2Grid_view_42.csv   The item catalog the engine scores against (595 items)

assets/
  register_intensity_chart_v4.html   Register intensity chart
  images/              95 reference/style images (Q9/Q11/Q13 options, product & photo refs)
    _manifest.json     Maps each original filename -> saved file
```

> **Image format note:** the 95 files in `assets/images/` were pulled from the
> claude.ai project, which only exposes them as **webp previews (~444px)**, not the
> original JPEG/PNG. `_manifest.json` records each original filename. If you need the
> full-resolution originals, they live in your local `~/Downloads` / Photos.

> **Catalog / engine path note:** `src/engine_v2.py` hardcodes
> `/mnt/project/V2Grid_view_40.csv` (a Claude-sandbox path, and note it references
> **v40**). The current catalog in this repo is **v42** (`data/V2Grid_view_42.csv`,
> byte-identical to the project's version). To run the engine locally, point
> `load_catalog(...)` at `data/V2Grid_view_42.csv`. Left as-is here to keep the
> migration faithful — adjust when you're ready.

## Provenance

These files were migrated from the "The Daily Cut" project knowledge on claude.ai.
Git is now the single source of truth. When a file changes here, re-upload the updated
version to the claude.ai project knowledge so Claude works from the latest.

> Note: `docs/reference/body_types_rules_extracted.txt` is the **extracted text** of the
> original `body types rules.pdf` (the API exposed text, not the binary). It largely
> overlaps with `docs/body_types_rules_v2.md`. Keep the original PDF elsewhere if you
> need the binary.
