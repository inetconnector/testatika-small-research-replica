# CAD

The repository contains six source-generating CAD families:

- `generate_v2.py` — parametric **core geometry** for the conservative V2 reconstruction;
- `generate_v3_experiments.py` — R4 rotor and controlled grid-vs-foil experiment assets;
- `generate_v3_photo_interp.py` — experimental high-resolution photo-interpretation geometry and assembled V3 STEP/STL;
- `generate_v3_video_refinements.py` — additive video-derived geometry for the hub arc pair, layered outer panel and lower central cage/prism;
- `generate_v4_best_evidence_m2.py` — **current best-evidence small M2 build family**;
- `generate_m6_large_v1.py` — **current best-evidence large ~500-mm M6 build family**, anchored to Hauser M6a and cross-checked against the official large-machine video corpus.

Run all currently source-reproducible families with:

```bash
python scripts/rebuild_research_assets.py
```

## Two current physical build lines

### Small M2 — V4

Generated output:

`hardware/experimental/v4-best-evidence-m2/`

Canonical guide:

[`../docs/research/v4-best-evidence-m2.md`](../docs/research/v4-best-evidence-m2.md)

### Large M6 — V1

Generated output:

`hardware/experimental/m6-large-v1-best-evidence/`

Primary complete assembly:

`complete-model/Testatika_M6_LARGE_V1_BEST_EVIDENCE.step/.stl`

Guarded mechanical/laboratory assembly:

`complete-model/Testatika_M6_LARGE_V1_SAFE_LAB_GUARDED.step/.stl`

Canonical guide:

[`../docs/research/m6-large-v1-best-evidence.md`](../docs/research/m6-large-v1-best-evidence.md)

M6 V1 models:

- two ~500 × 5 mm discs;
- 50 sheet-lamella positions using the Hauser ~0.2 × 20 × 160 mm source dimensions as the historical target;
- 8 front + 6 rear non-contact perforated stator positions;
- two detailed large cylinder assemblies with three concentric grid tubes, acrylic separators, central magnet tube and bifilar winding;
- wound horseshoe modules;
- capacitor and spiral-pipe positions;
- top crystal/possible-rectifier Blackbox;
- motor/magnet-wheel large-machine configuration;
- explicit open test-node terminalization;
- removable guarded counterrotation lab fixture.

The lab drive/guard are engineering fixtures and are never labelled original.

## Evidence status

Visible/source-supported geometry and hidden electrical topology are tracked separately. A visually complete model does not imply that the original node map has been recovered.

Important cross-machine rule:

- M2 small-pot internals must not inherit M6 large-cylinder details without a source bridge;
- M6a Hauser and M6b Holzherr details remain configuration-specific when they differ.

See:

- [`../docs/research/hauser-marinov-primary-scan-audit-2026-08-16.md`](../docs/research/hauser-marinov-primary-scan-audit-2026-08-16.md)
- [`../docs/research/video-frame-audit-2026-08-16.md`](../docs/research/video-frame-audit-2026-08-16.md)
- [`../docs/research/machines.yaml`](../docs/research/machines.yaml)

All historical/release STEP/STL assets remain committed so users do not need the CAD toolchain merely to inspect the models.

**Important:** `generate_v2.py` still does not regenerate every preserved V2 release asset. V4 and M6 V1 each have a self-contained generator for their declared source-owned families.
