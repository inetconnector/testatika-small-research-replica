# M2-V4.28 — Source elimination matrix

**Date:** 2026-08-20  
**Status:** synthesis of existing quantitative bounds; no anomalous source assumed

## 1. Purpose

V4.26 made a conventional timing mechanism plausible:

`slow electrostatic event -> fast ringdown -> nonlinear crystal/diode gate -> directed storage charge`.

V4.27 then showed the real-power scale that any sustained reservoir must meet. At `50 Hz`, a `100 W` source must deliver about `2 J/event`; a `3 kW` source must deliver about `60 J/event`.

V4.28 now compares that requirement with the strongest ordinary ambient-source bounds already established in V4.11 and V4.23–V4.25. It is a **source-elimination matrix**, not a new mechanism proposal.

Code:

- `sim/m2_v4_28_source_elimination_matrix.py`
- `tests/test_m2_v4_28_source_elimination_matrix.py`

## 2. 100-W comparison matrix

For field-density comparisons a deliberately generous tabletop capture area of `0.1 m²` is used. Capture is treated as ideal where noted, so the numbers favor the environmental-source hypothesis.

| candidate | optimistic/stated bound | gap to 100 W | V4.28 status |
|---|---:|---:|---|
| fair-weather global electric circuit, granting full-column `0.5 µW/m²`, 0.1 m² | `5e-8 W` | `2.0e9 ×` | excluded as bulk ambient source |
| ordinary 50-Hz stray E-field, 100 V/m, `Ceq=50 pF`, 0.2-m span | `6.28 µW` | `1.59e7 ×` | excluded as bulk ambient source |
| extreme 50-Hz comparison field, 10 kV/m with same coupling | `62.8 mW` | `1.59e3 ×` | strongly constrained |
| ambient RF example, 200 µW/m², ideal capture over 0.1 m² | `20 µW` | `5.0e6 ×` | excluded as bulk ambient source |
| strong local RF comparison, 0.1 W/m², ideal capture over 0.1 m² | `10 mW` | `1.0e4 ×` | strongly constrained at that stated field density |
| Schumann/ELF order-of-magnitude proxy, `1.59e-10 W/m²`, 0.1 m² | `1.59e-11 W` | `6.29e12 ×` | excluded as bulk ambient source |

These are not claims that the historical Testatika coupled to each channel. They are deliberately favorable power-scale comparisons.

## 3. Natural geoelectric compact-span check

V4.25 already considered unusually strong natural geoelectric fields. A `30.3 V/km` comparison across a `0.2 m` apparatus span yields only about

`V_oc = 6.06 mV`.

To deliver `100 W` at that voltage would require approximately

`I = 16.5 kA`.

Even under ideal maximum-power transfer, the Thevenin source resistance would have to be no more than about

`R_s = 9.18e-8 ohm`.

This makes ordinary compact-span natural geoelectric coupling an implausible 100-W source. Long conductive infrastructure is a different geometry and must be treated as a hidden/local input path, not silently imported into a floating tabletop model.

## 4. Non-electrical thresholds remain consistent with V4.23

V4.23 already showed what a conventional non-electrical source would have to look like at the 100-W scale:

- airflow through `0.1 m²`: about `11.86 m/s` even at impossible 100% conversion, or `17.71 m/s` at 30%;
- acoustic capture through `0.1 m²`: about `150 dB` at perfect conversion;
- 50-Hz structural motion at `1 mm rms`: order `318 N rms` in favorable phase;
- generous 1-kg, 0.1-m-radius rotor at 60 rpm stores only about `0.0987 J`, less than 1 ms of 100-W output;
- a 10-K thermal gradient would require at least about `3.03 kW` heat flow even at the Carnot ceiling;
- ordinary weak illumination is directly limited by intercepted radiant power.

These channels are therefore not subtle explanations for a sustained 100-W tabletop output. If one of them powers a real apparatus, it should be measurable at a correspondingly large physical scale.

## 5. What V4.28 does NOT eliminate

The following remain **OPEN_MEASURE_DIRECTLY**, because no generic ambient bound can exclude a deliberately strong or concealed local source:

1. hidden galvanic/base/table/chassis wiring or a low-impedance earth/infrastructure path;
2. a strong local RF/inductive/capacitive near-field transmitter or coupler;
3. mechanical shaft, belt, fixture or base work;
4. finite chemical/electrical storage sufficient for the demonstration duration;
5. corona/ion current whose driving field is itself supplied by a local powered source;
6. a large directed airflow, thermal, acoustic or radiant source actually measured at the apparatus;
7. historical output overestimate or incomplete power measurement.

The point is important: **ordinary ambient fields are quantitatively too small; deliberately strong local inputs are not excluded by an ambient-field calculation.** They must be instrumented.

## 6. Consequence for resonance and the crystal

V4.28 does not weaken the V4.26 timing model. It sharpens its role.

Resonance and the crystal can plausibly provide:

`impedance transformation + transient voltage buildup + phase memory + one-way charge routing`.

They cannot turn a `µW`, `nW` or `pW` ambient real-power flux into `100 W` steady output without another real source crossing the boundary.

Therefore the current architecture is best separated into two layers:

### Routing/control layer — plausible

`C(theta) modulation -> transient/ringdown -> crystal phase gate -> DC storage`.

### Bulk-energy layer — unresolved

`UNKNOWN reservoir -> enough real energy/event to replenish the storage/load cycle`.

At 50 events/s, the bulk-energy layer must supply order `2 J/event` for 100 W and `60 J/event` for 3 kW before losses.

## 7. Quantum-vacuum / unknown-field status

A quantum-vacuum or other unknown-field interpretation is **not supported by the present calculations**. It also cannot be excluded merely by showing that ordinary atmospheric/RF/geoelectric sources are too small.

It becomes an experimentally meaningful hypothesis only after a real device produces a repeatable positive closed-budget residual:

`E_X = E_load + delta(E_stored) + E_losses - E_all_known_inputs > 0`

with the residual substantially larger than the full uncertainty budget, surviving shielding, load changes, long-duration tests, independent instrumentation and replication.

Until then the source field remains:

**UNKNOWN**.

## 8. Next decisive experiment

The next high-value experiment is no longer another passive topology sweep. It is a **closed watt-budget enclosure** around the V4.26 routing chain / physical replica.

Simultaneously measure:

- load real power;
- storage-energy change;
- shaft/fixture mechanical work;
- all intentional electrical feedthrough power;
- base/chassis/table displacement and galvanic currents;
- wideband local E/H fields and RF real-power bounds;
- ion/corona current and its source-port voltage;
- temperature/heat flow, airflow and relevant chemical/storage changes.

Only after that measurement can the `UNKNOWN` reservoir term be reduced further.
