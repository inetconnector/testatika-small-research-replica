# CAD

The repository contains four source-generating CAD families:

- `generate_v2.py` — parametric **core geometry** for the conservative V2 reconstruction;
- `generate_v3_experiments.py` — R4 rotor and controlled grid-vs-foil experiment assets;
- `generate_v3_photo_interp.py` — experimental high-resolution photo-interpretation geometry and assembled V3 STEP/STL;
- `generate_v3_video_refinements.py` — additive video-derived geometry for the hub arc pair, layered outer panel and lower central cage/prism, based mainly on `meth4.asf` matched to `testabig.jpg`.

Run all currently source-reproducible families with:

```bash
python scripts/rebuild_research_assets.py
```

All historical/release STEP/STL assets remain committed so users do not need the CAD toolchain merely to print or inspect the model.

## Evidence status of video refinements

The video-refinement generator represents **visible external geometry candidates**, not recovered hidden circuitry.

In particular:

- hub arcs are supported as physical raised parts by moving highlights, but their material/connection/function remains unknown;
- the outer panel is visibly layered, while layer conductivity/material remains unresolved;
- the lower central module is better approximated as a perforated cage/prism than a plain cylinder, but its internals remain unknown.

See [`../docs/research/video-frame-audit-2026-08-16.md`](../docs/research/video-frame-audit-2026-08-16.md) and [`../docs/research/v3-photo/pixel-analysis.md`](../docs/research/v3-photo/pixel-analysis.md).

**Important:** `generate_v2.py` does not yet regenerate every preserved V2 release asset or the historical V2 complete assembly. Those binaries are intentionally retained rather than deleted or falsely described as regenerated. The exact source/binary boundary and completion target are documented in [`../docs/research/cad-reproducibility.md`](../docs/research/cad-reproducibility.md).

Photogrammetric working dimensions are documented in [`../docs/research/photogrammetry.md`](../docs/research/photogrammetry.md). Historical completeness/unknowns are tracked in [`../docs/REPLICATION_STATUS.md`](../docs/REPLICATION_STATUS.md).
