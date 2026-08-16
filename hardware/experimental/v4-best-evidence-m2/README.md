# V4 best-evidence M2 generated assets

This directory is owned by `cad/generate_v4_best_evidence_m2.py`.

It contains generated research geometry for the current best-evidence physical M2 build family. The geometry integrates direct Marinov small-machine constraints with photo/video-derived external refinements while preserving unknown wiring as unknown.

Expected generated subdirectories:

- `stl/`
- `step/`
- `complete-model/`
- `metadata/`

Canonical build documentation is in `docs/research/v4-best-evidence-m2.md`.

Important boundaries:

- floating individual rotor sectors are the M2 baseline;
- pots expose two historical external terminals;
- R0 is only the least-speculative nominal route, not a recovered original route;
- R4 is a separate research geometry;
- hub arcs/panel/cage geometry is photo/video-derived;
- Crystal and full electrical topology remain unresolved;
- no over-unity/free-energy performance is asserted.

Regenerate with:

```bash
python cad/generate_v4_best_evidence_m2.py
python scripts/check_v4_assets.py
```
