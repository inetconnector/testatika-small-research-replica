# M6 Large V1 — best-evidence ~500 mm two-disc research build

## Status

This is the canonical **large-machine build line** of the repository. It is separate from the small Marinov M2/V4 line.

Machine scope:

- **M6a anchor:** Albert Hauser direct-visit material, drawing no. 3279, and 1988 follow-up details;
- **M6 visual cross-check:** official large-machine footage `meth2`, `meth3`, `meth5` and the archived front/rear stills;
- **M6b comparison:** Holzherr 1999 ~50 cm demonstration, kept separate where speed/configuration differs.

The model is intentionally a **research reconstruction**, not a claim that the hidden original circuit has been recovered.

## Build products

The generator `cad/generate_m6_large_v1.py` creates:

- complete historical-facing best-evidence assembly:
  - `Testatika_M6_LARGE_V1_BEST_EVIDENCE.step`
  - `Testatika_M6_LARGE_V1_BEST_EVIDENCE.stl`
- guarded laboratory assembly with removable counterrotation fixture:
  - `Testatika_M6_LARGE_V1_SAFE_LAB_GUARDED.step`
  - `Testatika_M6_LARGE_V1_SAFE_LAB_GUARDED.stl`
- service/exploded assembly;
- individual STEP/STL modules for discs, stators, large cylinders, cylinder internals, horseshoe modules, capacitors, top module, drive/regulator, terminal board and guard.

Materialized path:

`hardware/experimental/m6-large-v1-best-evidence/`

## Directly anchored dimensions

| Feature | V1 value | Evidence status |
|---|---:|---|
| Disc diameter | 500 mm | Hauser direct report |
| Disc thickness | 5 mm | Hauser direct report |
| Lamella count | 50 per described disc face set | Hauser direct report |
| Lamella sheet thickness | source ~0.2 mm | source-stated; CAD uses a printable 0.4 mm visual surrogate |
| Lamella width | ~20 mm | Hauser direct report |
| Lamella radial length | ~160 mm | Hauser direct report |
| Front stationary electrodes | ~8 | Hauser direct report |
| Rear stationary electrodes | ~6 | Hauser direct report |
| Large cylinder grid count | 3 concentric metal grids per cylinder | Hauser 1988 correspondence |
| Winding | two layers, functionally bifilar, ~18-gauge enamelled Cu | Hauser 1988 correspondence |

## Photo/drawing-fit working geometry

The following are build dimensions, not original-object measurements:

- base: ~760 × 340 × 28 mm;
- disc centre: ~315 mm above datum;
- two large side cylinders: ~146 mm OD × ~235 mm high;
- full unguarded envelope: approximately 766 × 340 × 642 mm;
- large-cylinder grid radii and acrylic spacing are chosen to fit the Hauser section geometry while remaining separable and manufacturable.

All such values remain `PHOTO-FIT / DRAWING-FIT` until a calibrated original measurement becomes available.

## Visible/source-supported architecture represented

1. two large coaxial/counter-rotating disc positions;
2. dense sheet-lamella rotor architecture distinct from the M2 wire rotor;
3. non-contact perforated stationary electrodes around front/rear disc faces;
4. two tall side cylinder assemblies;
5. **three concentric metal-grid tubes** inside each large cylinder;
6. acrylic/plastic insulating sleeves between the grids;
7. central magnet tube;
8. two-layer bifilar winding around the central tube;
9. top copper/output ring geometry;
10. wound horseshoe-magnet modules with layered pole structures;
11. large and smaller capacitor-can positions;
12. pipe/spiral module;
13. top perforated `crystal / possible rectifier` black-box geometry;
14. magnet-wheel / speed-regulation family;
15. small DC-motor position for the Hauser large-machine configuration;
16. nested-shaft and bearing support required to make the two-disc research assembly mechanically buildable;
17. three-group open terminal board reflecting the report of multiple isolated circuits without inventing their hidden interconnection.

## M6a versus M6b

Do not silently merge them.

- M6a/Hauser: ~500 mm, ~60 rpm reported in the 1986 line, small DC motor + magnet-wheel/speed-control hardware, three-grid cylinder internals.
- M6b/Holzherr 1999: ~50 cm demonstration, ~15 rpm reported, large capacitor construction reportedly using 20 perforated-sheet layers.

V1 uses **M6a as the physical anchor** because its direct-visit drawing and cylinder section are more construction-specific. M6b speed and 20-layer capacitor claims are test/configuration variants, not injected into the V1 baseline.

## What is deliberately left open

The following are not solved by the surviving sources and therefore terminate at reversible interfaces:

- exact node-to-node wiring;
- exact polarity/grouping of the 8+6 stationary electrodes;
- exact connections between each large cylinder's three grids, magnet tube and bifilar winding;
- exact capacitances and dielectric stack;
- exact top crystal material, number, polarity and I-V behaviour;
- exact magnetic function of the cylinder magnet tube and horseshoe modules;
- exact original motor/gearing/belt train;
- exact startup/priming state;
- exact load/output connection and any source of the historical power claims.

## Ready-to-run boundary

`M6-V1-B0` is mechanically complete and electrically **open by default**. Unknown historical nodes are not shorted together merely to make the model look finished.

For first operation use `M6-V1-LAB-MECH`:

- guarded rotor;
- removable low-voltage counterrotation fixture;
- no electrostatic bias;
- no load bus;
- verify shaft runout, clearances, bearing temperature, vibration and rpm.

Only after a successful mechanical qualification should low-energy electrostatic experiments be introduced according to `m6-large-v1-experiment-sequence.md`.

## Scientific boundary

The historical `3 kW`, `300 V × 10 A`, lamp/heater and arc demonstrations are source claims/observations, **not closed energy balances**. No over-unity claim is encoded into the model. Energy conservation remains the null hypothesis.
