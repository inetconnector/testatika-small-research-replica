# CAD

The repository contains three source-generating CAD families:

- `generate_v2.py` — parametric **core geometry** for the conservative V2 reconstruction;
- `generate_v3_experiments.py` — R4 rotor and controlled grid-vs-foil experiment assets;
- `generate_v3_photo_interp.py` — experimental high-resolution photo-interpretation geometry and assembled V3 STEP/STL.

Run all currently source-reproducible families with:

```bash
python scripts/rebuild_research_assets.py
```

All historical/release STEP/STL assets remain committed so users do not need the CAD toolchain merely to print or inspect the model.

**Important:** `generate_v2.py` does not yet regenerate every preserved V2 release asset or the historical V2 complete assembly. Those binaries are intentionally retained rather than deleted or falsely described as regenerated. The exact source/binary boundary and completion target are documented in [`../docs/research/cad-reproducibility.md`](../docs/research/cad-reproducibility.md).

Photogrammetric working dimensions are documented in [`../docs/research/photogrammetry.md`](../docs/research/photogrammetry.md). Historical completeness/unknowns are tracked in [`../docs/REPLICATION_STATUS.md`](../docs/REPLICATION_STATUS.md).
