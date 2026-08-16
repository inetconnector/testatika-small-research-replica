# M6 Large V1 — detailed BOM

This BOM separates **historical target material**, **working-fit construction material**, and **laboratory-only fixtures**.

## A. Structural and rotor assembly

| Qty | Item | Target / working specification | Evidence |
|---:|---|---|---|
| 1 | base | ~760 × 340 × 28 mm wood/laminated structural plate | Hauser: wood base; dimensions drawing-fit |
| 2 | large discs | PMMA/Plexiglas, Ø500 × 5 mm | direct Hauser dimension/material |
| 50 | front-disc lamellae | chrome-steel / magnetically responsive sheet, ~0.2 × 20 × 160 mm | direct Hauser |
| 100 | rear-disc lamellae | same; rear disc described with lamellae on both faces | direct Hauser line |
| 1 | inner shaft | 12 mm working lab shaft | LAB-BUILD |
| 1 | hollow outer shaft | ~25 mm OD with clearance for inner shaft | LAB-BUILD |
| 2+ | bearing blocks | sized to chosen nested-shaft implementation | LAB-BUILD |
| 4 | structural braces | slotted/aluminium/printed prototype braces | derived mechanical necessity |

**Lamella note:** the source says ~0.2 mm. The STL reference uses 0.4 mm only so the surfaces survive generic mesh handling. Use sheet material near the source thickness for a serious physical reconstruction.

## B. Stationary electrodes

| Qty | Item | Working geometry |
|---:|---|---|
| 8 | front perforated stator electrodes | ~104 × 34 × 2.5 mm visual/build carrier |
| 6 | rear perforated stator electrodes | same family; last pair may be mounted at alternate/45° orientation |
| 28 | adjustable insulated spacers | maintain non-contact gap |
| 14 | removable lead tabs | each stator must be individually instrumentable before any grouping |

No stator is allowed to rub a disc.

## C. Two large cylinder assemblies

Per cylinder:

| Qty | Item | Working geometry / material |
|---:|---|---|
| 1 | outer grid tube | ~132 mm mean diameter × 205 mm high metal grid |
| 1 | middle grid tube | ~112 mm mean diameter × 199 mm high metal grid |
| 1 | inner grid tube | ~92 mm mean diameter × 193 mm high metal grid |
| 2 | acrylic insulating sleeves | nested between the three grids |
| 1 | central magnet tube | ~36 mm OD × ~185 mm long working geometry |
| 2 | interleaved winding layers | enamelled copper, source says ~18 gauge |
| 2 | thin insulation layers | plastic film between magnet tube / winding layers |
| 1 | top copper ring | removable output/test ring |
| 4 | isolated top test posts | LAB-BUILD breakout; exact historical topology unknown |

The CAD winding uses ~4.5 mm pitch over ~170 mm as a visual/build starting point, approximately 38 turns per helix. **Turn count is not a recovered original value.**

## D. Horseshoe modules

| Qty | Item | Notes |
|---:|---|---|
| 2 | horseshoe magnetic cores | large-machine source family |
| 4 | leg winding bobbins | two per horseshoe |
| 8 | layered perforated/insulating pole pieces | four-layer working stack per pole position in CAD |
| as needed | enamelled Cu wire | exact turns unknown; keep each winding separately terminated |

## E. Capacitor / spiral / top module

| Qty | Item | Notes |
|---:|---|---|
| 1 | large capacitor can position | pos. 7 family in Hauser drawing; exact C unknown |
| 1 | smaller capacitor can position | pos. 8 family; exact C unknown |
| 1 | pipe-with-spiral module | pos. 9 family |
| 1 | top perforated cage | pos. 12 / crystal-rectifier geometry |
| 1 | internal top coil/core carrier | geometry candidate |
| 3 | removable crystal surrogate seats | **empty by default**; no material claimed original |
| 2 | top end caps | Hauser interpreted them as magnetic; keep removable |

## F. Drive/regulation

Historical-facing M6a build:

- one small DC-motor position;
- one magnet/timing wheel position;
- removable speed-control linkage/working-fit geometry.

Safe laboratory build:

- adjustable mount for a low-voltage gearmotor body roughly 36–45 mm diameter;
- two coaxial rear driven pulleys on separate shaft members;
- two independent round-belt planes, one open and one crossed, to obtain opposite disc rotation;
- 3–4 mm polyurethane round belt recommended as a mechanically forgiving low-speed research solution;
- removable guard frame.

The lab counterrotation fixture is explicitly **not historical evidence**. It exists to test the M6 geometry reproducibly.

## G. Instrumentation / terminalization

Minimum:

- 18 isolated test-node positions arranged as three groups of six;
- insulated binding posts or guarded laboratory connectors;
- optical tachometer markers on both discs;
- current sensing for the low-voltage drive motor;
- vibration measurement point on each bearing support;
- high-impedance electrostatic voltage probes for later low-energy tests;
- discharge resistors and verified discharge procedure for every experimental capacitor.

## H. Fasteners

Use nonmagnetic fasteners where magnetic material would confound a test. Keep a hardware log per configuration. Base hole patterns in the CAD are **LAB-BUILD mounting provisions**, not claimed original fastener locations.
