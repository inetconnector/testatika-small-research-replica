# CAD reproducibility ledger

## Rule

A committed binary CAD asset is not described as source-reproducible unless a versioned generator in `cad/` deterministically recreates the relevant geometry. Existing binary research assets are preserved even when their original generation path is incomplete.

## Source-reproducible families

### `cad/generate_v2.py`

Generates the V2 **core** geometry:

- `rotor_20wire`
- `rotor_24wire`
- `rotor_25wire`
- `hub_front`
- `hub_rear`
- `bearing_tower`
- `electrode_wedge_frame`
- `pot_outer_shell`
- `pot_grid_former`
- `pot_acrylic_sleeve_jig`
- `pot_spiral_mandrel`
- `horseshoe_magnet_mount`
- `crystal_bridge`

It does **not yet regenerate the complete V2 binary library**.

### `cad/generate_v3_experiments.py`

Generates:

- R4 20/24/25-sector research rotors;
- common grid/foil A/B carrier and clamp;
- material template;
- 1/2/3-mm gap gauges.

### `cad/generate_v3_photo_interp.py`

Generates the V3 photo-interpretation part subset and the experimental V3 assembled STEP/STL model.

### `cad/generate_v3_video_refinements.py`

Generates three additive geometry refinements from the fully audited historical moving-image source, especially `meth4.asf` matched to `testabig.jpg`:

- `hub_arc_pair_video_refined`;
- `lower_central_cage_video_refined`;
- `outer_panel_layered_video_refined`.

These are **source-reproducible research geometries**, but not historically measured original parts. Their dimensions are photo/video-fit working values. Electrical connections/materials remain deliberately unspecified.

### `cad/generate_v4_best_evidence_m2.py`

V4 is the self-contained current-build generator for the small M2 line. It generates the declared M2 V4 part family, nominal/R4 complete STEP/STL assemblies and `MODEL_INFO_V4.json` under `hardware/experimental/v4-best-evidence-m2/`.

The V4 materialization workflow normalizes volatile STEP header timestamps, checks the declared geometry and creates the deterministic M2 build package.

### `cad/generate_m6_large_v1.py`

M6 Large V1 is the self-contained current-build generator for the large ~500-mm two-disc line. It is anchored primarily to Hauser M6a construction evidence and keeps M6b configuration-specific details separate.

It generates:

- ~500-mm front and rear disc assemblies with the 50-lamella source count;
- nested shaft/counterrotation working geometry;
- 8-front/6-rear non-contact perforated stator set;
- two large three-grid cylinder systems including acrylic separators, magnet tube and bifilar winding geometry;
- wound horseshoe modules;
- capacitor, spiral-pipe, top crystal/possible-rectifier and motor/magnet-wheel modules;
- explicit open terminal board;
- removable low-voltage counterrotation laboratory fixture and guard geometry;
- complete `Testatika_M6_LARGE_V1_BEST_EVIDENCE.step/.stl`;
- complete guarded `Testatika_M6_LARGE_V1_SAFE_LAB_GUARDED.step/.stl`;
- service/exploded complete assembly;
- `MODEL_INFO_M6_V1.json`.

M6 output path:

`hardware/experimental/m6-large-v1-best-evidence/`

`scripts/normalize_m6_step.py` fixes only the volatile OpenCascade STEP timestamp to `2000-01-01T00:00:00`; `scripts/check_m6_assets.py` verifies the declared geometry and metadata; `scripts/build_m6_package.py` creates the deterministic package.

## Generated binary policy

### V3 video refinements

Source owns:

- `hardware/experimental/v3-video-refinements/stl/`
- `hardware/experimental/v3-video-refinements/step/`

If absent, run `python scripts/rebuild_research_assets.py`.

### V4

Source owns:

- `hardware/experimental/v4-best-evidence-m2/stl/`
- `hardware/experimental/v4-best-evidence-m2/step/`
- `hardware/experimental/v4-best-evidence-m2/complete-model/`
- `hardware/experimental/v4-best-evidence-m2/metadata/`.

CI materializes these outputs and the deterministic package:

- `release/experimental/testatika-m2-v4-best-evidence-build-package.zip`
- `release/experimental/testatika-m2-v4-best-evidence-build-package.zip.sha256`.

### M6 Large V1

Source owns:

- `hardware/experimental/m6-large-v1-best-evidence/stl/`
- `hardware/experimental/m6-large-v1-best-evidence/step/`
- `hardware/experimental/m6-large-v1-best-evidence/complete-model/`
- `hardware/experimental/m6-large-v1-best-evidence/metadata/`.

CI materializes these outputs and the deterministic package:

- `release/experimental/testatika-m6-large-v1-best-evidence-build-package.zip`
- `release/experimental/testatika-m6-large-v1-best-evidence-build-package.zip.sha256`.

A generated binary is convenience/reproducibility material. The versioned generator and evidence documentation remain the semantic source of truth.

## Preserved binary assets not yet covered by the V2 core generator

At minimum the baseline library contains additional historically useful/release assets such as base/frame, terminal, shield and complete V2 model files. These remain valid **preserved research assets**. Their presence must not be interpreted as proof that `generate_v2.py` regenerates the full historical V2 library.

## Completion targets

For M2 V4, source-level completeness means that every declared V4 part/complete assembly and metadata file regenerates from its generator and the deterministic V4 package verifies.

For M6 Large V1, source-level completeness means:

1. all declared M6 individual STEP/STL modules regenerate;
2. best-evidence, guarded-lab and service/exploded complete assemblies regenerate;
3. metadata preserves the 500-mm, 50-lamella, 8+6 stator and three-grid cylinder anchors;
4. historical unknown electrical connections remain explicit/open rather than silently filled;
5. deterministic STEP normalization/package/hash checks pass;
6. repository validation and manifest checks pass after materialization.

For the older V2 preserved library, source-level coverage remains incomplete by design and must not be overstated.

Across all families, generation must never erase experimental or superseded evidence/variants.
