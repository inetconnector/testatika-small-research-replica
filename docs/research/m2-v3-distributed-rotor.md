# M2-V3 — distributed floating rotor + narrow pickup diagnostic

## Purpose

M2-V3 tests a narrower and more physically specific hypothesis than the earlier four-stationary-node model:

> A nominally neutral, electrically isolated rotor wire may act as a **spatially extended capacitive bridge** between two different stationary field regions. The decisive modulation may then come from a **narrow contactless pickup/Taster aperture**, while the broader grids/pots serve field-forming, storage, or feedback roles.

This is a falsifiable research hypothesis, not a recovered historical schematic and not an over-unity claim.

## Why this model was added

The previous M2 bridge diagnostic used broad ~38° stationary coupling windows. With 24 equally spaced rotor wires, the individual sector events are strongly averaged and the resulting aggregate effective capacitance varies only at the ~10^-3 level. That makes a passive Goldie-like regenerative feedback ratio impossible in that reduced geometry.

Goldie's US 3,013,201 provides a useful conventional control case. Its isolated rotor is explicitly used as a capacitive link between a charging electrode and a stator. The rotor remains electrically neutral while opposite parts carry induced charge of opposite sign. The two generator sections then cross-feed a fraction of their outputs and shaft work supplies the increasing electrostatic energy.

The M2 evidence already keeps the rotor wires individually floating while also preserving separate candidate nodes for hub arcs and outer panel/pickup structures. Methernitha's `Taster` / `antenna keys` language has already been conservatively decoded in this repository as a non-contact capacitive/influence pickup.

## Reduced V3 geometry

Each of the nominal 24 rotor wires is represented as one equipotential isolated conductor with several spatial coupling lobes.

The first diagnostic divides the wire into:

- an **inner ARC region**;
- an **outer PICKUP region**;
- optional intermediate front/back regions for through-disc routes.

For one neutral floating wire with capacitances `Ca` to ARC, `Cp` to PICKUP and `Cg` to environment, Schur elimination for `Q_wire = 0` gives the mediated mutual capacitance

```text
Cmed = Ca * Cp / (Ca + Cp + Cg)
```

The 24 wire contributions are summed as the rotor advances through one 15° sector pitch.

## Route encodings

These remain research geometries, exactly as in `rotor-wire-routing.md`:

- `R0`: same-face radial inner→outer path;
- `R1`: inner front / outer back U-stitch abstraction;
- `R3`: inner sector `i` to outer sector `i+1`, i.e. 15° phase offset at 24 sectors;
- `R4`: nominal same-azimuth route with three face changes through five radial zones.

No R1/R3/R4 route is claimed as the proven historical M2 original.

## Main result from placeholder geometry

Using the same nominal 24-sector count, passive feedback fraction `beta = 0.4`, and placeholder per-wire capacitances, the pickup aperture dominates the reduced regeneration metric.

Representative results:

| Route | aperture half-width | Cmax/Cmin | beta_critical | rho_bridge at beta=0.4 |
|---|---:|---:|---:|---:|
| R0 | 10° | ~3.575 | ~0.388 | ~1.030 |
| R0 | 38° | ~1.0063 | ~157.8 | ~0.0025 |
| R1 | 10° | ~3.554 | ~0.392 | ~1.022 |
| R3 | 10° | ~1.564 | ~1.77 | ~0.226 |
| R3 | 15° | ~3.871 | ~0.348 | ~1.149 |
| R4 | 10° | ~3.509 | ~0.399 | ~1.004 |
| R4 | 38° | ~1.0061 | ~162.6 | ~0.0025 |

where the reduced bridge metric is

```text
rho_bridge = beta * (Cmax/Cmin - 1)
```

and

```text
beta_critical = 1 / (Cmax/Cmin - 1)
```

`rho_bridge > 1` does **not** prove that the M2 circuit self-excites. It only means that the static geometry has enough capacitance modulation to stop ruling out a conventional two-section Goldie-like regenerative topology on modulation grounds alone.

## Important interpretation

The result changes the search priority.

The earlier broad-electrode model effectively averages over several rotor wires at once. With a 15° sector pitch, sufficiently broad stationary electrodes suppress the event-by-event capacitance swing.

A narrow pickup does the opposite: individual wire passages become visible in `C(theta)`. In the placeholder model this can increase `Cmax/Cmin` by orders of magnitude relative to the 38° case.

This makes the following physical division of labor newly plausible as a test hypothesis:

```text
broad grid / pot field     -> bias / storage / feedback field
inner hub arc              -> induction / field-forming node
floating distributed wire  -> neutral capacitive bridge
narrow outer Taster/pickup  -> strongly modulated collector
crystal / diode             -> phase-selective charge routing
opposite-side pot/grid      -> cross-feedback reservoir
```

This is not yet a historical wiring claim.

## Sector-pitch / aperture prediction

The effect is not simply monotonic with electrode width. Because the rotor is a 24-element angular comb, aperture width and route phase offset interact with the 15° sector pitch.

The R3 placeholder route demonstrates this directly: a 15° inner/outer offset suppresses the 10° case but moves a strong modulation window toward a 15° half-width.

Therefore a real experiment should not compare only `broad` vs `narrow`. It should sweep pickup angular width and phase continuously.

## Decisive bench experiment

Before any closed-loop or high-voltage test, measure only geometry:

1. electrically isolate all 24 rotor wires;
2. keep pots/crystal/load open;
3. drive rotor externally at low speed;
4. excite ARC with a small known AC/electrometer-compatible signal;
5. measure transfer capacitance/current at PICKUP versus angle;
6. repeat with pickup masks giving e.g. 3°, 5°, 7°, 10°, 15°, 20°, 38° half-width equivalents;
7. repeat R0/R1/R3/R4 rotor routes without changing stationary hardware;
8. derive measured `Cmax/Cmin` and `beta_critical`;
9. only if measured ratios are large enough, proceed to passive rectifier/cross-feedback tests.

The most useful first measurement is therefore no longer only aggregate `C(theta)` at the pots. It is **phase-resolved ARC↔PICKUP transfer capacitance with controlled pickup aperture**.

## What remains missing

V3 still does not model:

- the complete eight-plus stationary-node M2 network;
- measured front/back electrode geometry;
- conserved non-zero net charge on rotor wires;
- corona/ion transfer;
- dielectric/electret memory;
- crystal I-V behavior;
- actual pot cross-feedback topology;
- electromechanical torque;
- a full hybrid one-revolution Jacobian/monodromy matrix.

Those states must be added one at a time after the geometry-only transfer measurement. Arbitrary feedback gain must not be used to force regeneration.

## Code

```text
python sim/m2_v3_distributed_rotor.py
python sim/m2_v3_distributed_rotor.py --feedback 0.4 --csv out/m2_v3.csv
python -m unittest tests/test_m2_v3_distributed_rotor.py -v
```

## Source anchors

- `docs/research/rotor-wire-routing.md`
- `docs/research/v4-electrical-boundary.md`
- `docs/research/baumann-language-decoding.md`
- Goldie, C. H., US Patent 3,013,201, *Self-excited variable capacitance electrostatic generator*, 1961.
