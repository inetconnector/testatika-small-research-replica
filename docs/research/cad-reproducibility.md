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

V4 is the first self-contained generator intended to be a **current build starting point** rather than only an evidence fragment.

It generates:

- 20/24/25-sector floating R0 rotors;
- a 24-sector floating R4 research rotor;
- hub disk and video-refined hub arcs;
- M2 pot shell/grid/dielectric-jig/spiral-mandrel/**two-terminal lid**;
- video-refined layered outer panel;
- video-refined lower central cage;
- top Crystal Blackbox carrier;
- real-magnet envelope and matched dummy;
- guard post;
- complete nominal `Testatika_M2_V4_BEST_EVIDENCE.step/.stl`;
- complete `Testatika_M2_V4_R4_RESEARCH.step/.stl`;
- `MODEL_INFO_V4.json`.

The generator was locally executed with CadQuery 2.8.0 before commit. All declared individual parts plus both complete STEP/STL assemblies exported successfully.

V4 output path:

`hardware/experimental/v4-best-evidence-m2/`

The V4 materialization workflow regenerates these binaries in CI and packages them with the canonical V4 documentation.

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

A generated binary is convenience/reproducibility material. The versioned generator and evidence documentation remain the semantic source of truth.

## Preserved binary assets not yet covered by the V2 core generator

At minimum the baseline library contains additional historically useful/release assets such as:

- `base_left` / `base_right`
- `side_frame_column`
- `top_bridge`
- `center_crossbar`
- `electrode_swivel`
- `electrode_tilt_head`
- `electrode_angle_jig`
- `pot_terminal_lid`
- `crystal_insert_carrier`
- `guard_post`
- `terminal_block`
- `wire_bending_jig`
- `horseshoe_magnet_dummy`
- `optional_magnet_leg_bobbin`
- rear-shield experimental rail/carriage
- `ASSEMBLY_REFERENCE.step`
- the historical V2 complete assembly and its OBJ/GLB derivatives.

These files remain valid **preserved research assets**. Their presence must not be interpreted as proof that `generate_v2.py` regenerates them.

## Completion target

For the **current V4 build family**, the source layer is complete when:

1. every V4 file listed in `v4-best-evidence-m2.md` regenerates from one generator;
2. complete nominal and R4 assemblies regenerate in STEP and STL;
3. metadata names all historically unresolved electrical fields;
4. the deterministic V4 ZIP and SHA-256 are reproducible from one checkout;
5. repository validation and manifest checks pass after materialization.

For the older V2 preserved library, source-level coverage remains incomplete by design and must not be overstated.

Across all families, generation must never erase experimental or superseded evidence/variants.
