# V3 photo-analysis provenance

Historical source branch: `research/small-machine-v3-pixel-analysis`.

The V3 high-resolution re-analysis was originally developed on that branch and is now integrated into the cumulative repository. The branch name is retained here only as provenance; the active canonical files are on `main` after merge.

V3 remains intentionally distinct from the conservative V2 baseline in **scientific status**, not because it requires a separate active branch.

## Start here

- [`docs/research/v3-photo/README.md`](docs/research/v3-photo/README.md)
- [`docs/research/v3-photo/pixel-analysis.md`](docs/research/v3-photo/pixel-analysis.md)
- [`docs/research/v3-photo/functional-model.md`](docs/research/v3-photo/functional-model.md)
- [`docs/research/v3-photo/node-map.tsv`](docs/research/v3-photo/node-map.tsv)
- [`docs/research/v3-photo/connection-plan.tsv`](docs/research/v3-photo/connection-plan.tsv)
- [`docs/images/small_machine_v3_functional_schematic.svg`](docs/images/small_machine_v3_functional_schematic.svg)
- [`docs/REPLICATION_STATUS.md`](docs/REPLICATION_STATUS.md)

## Generated assets

The historical materialization workflow generated and committed:

- `docs/images/small_machine_v3_annotation.png`
- `hardware/experimental/v3-photo/stl/`
- `hardware/experimental/v3-photo/step/`
- `hardware/experimental/v3-photo/complete-model/`
- `release/experimental/Testatika_Small_V3_Photo_Artifacts.zip`

The source generator is [`cad/generate_v3_photo_interp.py`](cad/generate_v3_photo_interp.py). Current source-reproducibility boundaries are documented in [`docs/research/cad-reproducibility.md`](docs/research/cad-reproducibility.md).

## Scientific status

V3 improves the **visible external geometry and subsystem mapping**. It does not claim the hidden original circuit, black-region material, crystal internals or historical energy balance have been solved. Convenience aliases named `V3_COMPLETE` remain experimental photo-interpretation assets according to their model metadata.
