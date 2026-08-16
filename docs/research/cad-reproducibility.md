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

These are **source-reproducible research geometries**, but not historically measured original parts. Their current dimensions are photo/video-fit working values. Electrical connections/materials remain deliberately unspecified.

The generator was locally smoke-tested with CadQuery and successfully exported both STEP and STL for all three parts before being committed.

## Generated-but-not-yet-committed binary refinement outputs

The video-refinement source owns the paths under:

- `hardware/experimental/v3-video-refinements/stl/`
- `hardware/experimental/v3-video-refinements/step/`

The source generator is canonical. If those generated binaries are absent from a checkout, run:

```bash
python scripts/rebuild_research_assets.py
```

Absence of generated refinement binaries is **not** evidence loss as long as the generator, source locators and parameter values remain versioned.

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

The CAD source layer is complete when:

1. every baseline STEP/STL pair has a named generator function or a documented external source procedure;
2. the complete V2/V3 assemblies are generated from those same source parts;
3. video-derived refinements that become part of the assembled V3 are integrated into the complete-model generator with explicit evidence status;
4. regenerated dimensions are checked against `docs/research/stl_dimensions.json` and model metadata;
5. generation does not erase experimental or superseded variants;
6. binary diffs are reviewed before replacing an established release asset.

Until then, the repository prioritizes preservation over destructive binary replacement.
