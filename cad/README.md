# CAD

The repository contains five source-generating CAD families:

- `generate_v2.py` — parametric **core geometry** for the conservative V2 reconstruction;
- `generate_v3_experiments.py` — R4 rotor and controlled grid-vs-foil experiment assets;
- `generate_v3_photo_interp.py` — experimental high-resolution photo-interpretation geometry and assembled V3 STEP/STL;
- `generate_v3_video_refinements.py` — additive video-derived geometry for the hub arc pair, layered outer panel and lower central cage/prism;
- `generate_v4_best_evidence_m2.py` — **current best-evidence M2 build family**, integrating direct Marinov electrical constraints with the V3/video external geometry refinements.

Run all currently source-reproducible families with:

```bash
python scripts/rebuild_research_assets.py
```

## V4 best-evidence M2

V4 is the preferred build starting point for a new physical M2 research replica. It encodes:

- ~200-mm single rotor;
- 20/24/25 rotor choices, nominal 24;
- individually floating sector wires (`connected to nothing` in the direct Marinov scan);
- no rubbing collection;
- two side pots with grid/dielectric/Cu-spiral structure and exactly two historical external terminal positions per pot;
- no built-in conventional drive motor;
- two visible horseshoe-magnet positions with matched dummy controls;
- video-refined hub arcs, layered outer panels and lower central cage;
- a top `crystal` Blackbox carrier that preserves uncertainty rather than asserting a solved circuit.

Generated output lives under:

`hardware/experimental/v4-best-evidence-m2/`

Canonical documentation:

- [`../docs/research/v4-best-evidence-m2.md`](../docs/research/v4-best-evidence-m2.md)
- [`../docs/research/v4-bom.md`](../docs/research/v4-bom.md)
- [`../docs/research/v4-assembly.md`](../docs/research/v4-assembly.md)
- [`../docs/research/v4-electrical-boundary.md`](../docs/research/v4-electrical-boundary.md)
- [`../docs/research/v4-printing.md`](../docs/research/v4-printing.md)

## Evidence status of video refinements

The video-refinement geometry represents **visible external geometry candidates**, not recovered hidden circuitry.

In particular:

- hub arcs are supported as physical raised parts by moving highlights, but their material/connection/function remains unknown;
- the outer panel is visibly layered, while layer conductivity/material remains unresolved;
- the lower central module is better approximated as a perforated cage/prism than a plain cylinder, but its internals remain unknown.

See [`../docs/research/video-frame-audit-2026-08-16.md`](../docs/research/video-frame-audit-2026-08-16.md) and [`../docs/research/v3-photo/pixel-analysis.md`](../docs/research/v3-photo/pixel-analysis.md).

All historical/release STEP/STL assets remain committed so users do not need the CAD toolchain merely to print or inspect the model.

**Important:** `generate_v2.py` still does not regenerate every preserved V2 release asset. Those binaries remain intentionally preserved. V4, by contrast, has its own self-contained generator for its declared source-owned part/assembly set. The exact source/binary boundary is documented in [`../docs/research/cad-reproducibility.md`](../docs/research/cad-reproducibility.md).

Photogrammetric working dimensions are documented in [`../docs/research/photogrammetry.md`](../docs/research/photogrammetry.md). Historical completeness/unknowns are tracked in [`../docs/REPLICATION_STATUS.md`](../docs/REPLICATION_STATUS.md).
