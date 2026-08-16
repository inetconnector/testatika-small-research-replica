# M6 Large V1 — manufacturing / printing guidance

The complete STL is primarily a **geometry and assembly reference**. A 500 mm rotating machine should not be treated as one giant consumer-FDM print.

## Recommended manufacturing split

### Laser/CNC cut rather than FDM

- two Ø500 × 5 mm PMMA discs;
- large base plate;
- large flat perforated electrode carriers if metal/perforated sheet is available;
- transparent safety guard panels.

### Metal fabrication

- sheet lamellae;
- shafts;
- bearing hardware;
- three cylinder grid tubes;
- top copper/output rings;
- horseshoe magnetic cores if testing magnetic baseline;
- motor/pulley shafts.

### 3D-printable jigs / low-stress parts

- bearing alignment jigs;
- stator mounting brackets;
- cylinder grid-forming jigs;
- acrylic sleeve spacing rings;
- coil bobbins;
- terminal board;
- top crystal carrier;
- motor mount prototype;
- pulley prototypes for low-speed dry tests;
- guard standoffs.

For a final rotating assembly, replace printed high-load pulleys/hubs if their material strength or heat resistance is uncertain.

## Files

`hardware/experimental/m6-large-v1-best-evidence/stl/` contains all part references.

The most useful manufacturing references are:

- `front_disc_500mm_50lamella_m6_v1.stl`;
- `rear_disc_500mm_50lamella_both_sides_m6_v1.stl`;
- `stationary_electrode_perforated_m6_v1.stl`;
- `large_cylinder_complete_3grid_bifilar_m6_v1.stl`;
- individual three-grid / acrylic / magnet-tube / bifilar-winding files;
- `horseshoe_wound_module_m6_v1.stl`;
- `top_crystal_rectifier_blackbox_m6_v1.stl`;
- `lab_counterrotation_drive_m6_v1.stl`;
- `terminal_board_3isolated_open_m6_v1.stl`.

## Tolerances

Use the STEP models for dimensional work. STL tessellation is not the source of truth.

Initial recommendations:

- rotor/stator radial-clearance experiments: start generous, ≥8–10 mm physical clearance until runout is known;
- shaft/bearing fits: machine to the actual bearing manufacturer's tolerance, not generic FDM dimensions;
- cylinder nesting: allow 1–2 mm radial assembly clearance for prototype sleeves/grids;
- removable electrical modules: provide at least 0.5 mm printer-fit clearance per side where printed.

## Material-state logging

Because electrostatic behaviour depends strongly on surface condition and humidity, record:

- PMMA grade;
- surface cleaning method;
- humidity/temperature;
- lamella material and magnetic response;
- grid material;
- insulating-film type/thickness;
- winding wire diameter;
- any coating/corona treatment.

Do not treat two visually identical builds as electrically identical without this log.
