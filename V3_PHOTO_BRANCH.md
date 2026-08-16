# V3 photo-analysis branch

Branch: `research/small-machine-v3-pixel-analysis`

This branch contains the deeper high-resolution re-analysis of the first small Marinov Testatika and is intentionally separated from the baseline V2 release.

## Start here

- [`docs/research/v3-photo/README.md`](docs/research/v3-photo/README.md)
- [`docs/research/v3-photo/pixel-analysis.md`](docs/research/v3-photo/pixel-analysis.md)
- [`docs/research/v3-photo/functional-model.md`](docs/research/v3-photo/functional-model.md)
- [`docs/research/v3-photo/node-map.tsv`](docs/research/v3-photo/node-map.tsv)
- [`docs/research/v3-photo/connection-plan.tsv`](docs/research/v3-photo/connection-plan.tsv)
- [`docs/images/small_machine_v3_functional_schematic.svg`](docs/images/small_machine_v3_functional_schematic.svg)

## Generated assets

The workflow `.github/workflows/materialize-v3-photo.yml` generates and commits:

- `docs/images/small_machine_v3_annotation.png`
- `hardware/experimental/v3-photo/stl/`
- `hardware/experimental/v3-photo/step/`
- `hardware/experimental/v3-photo/complete-model/`
- `release/experimental/Testatika_Small_V3_Photo_Artifacts.zip`

The CAD source is [`cad/generate_v3_photo_interp.py`](cad/generate_v3_photo_interp.py).

## Scientific status

V3 improves the **visible external geometry and subsystem mapping**. It does not claim the hidden original circuit, black-grid material, crystal internals or historical energy balance have been solved.
