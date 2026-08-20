# M2-V4.27 — Reservoir isolation and missing-source scale

**Date:** 2026-08-20  
**Status:** quantitative source-isolation model; no anomalous source assumed

## 1. Why V4.27 exists

V4.26 showed that the proposed signal-processing chain is physically coherent at low energy:

`slow event -> fast LC ringdown -> nonlinear crystal/diode gate -> directed storage charge`.

That result did **not** identify a sustained energy source. V4.27 therefore stops adding topology and asks only:

> What energy per event, charge per event and average source current would any missing reservoir actually have to supply?

The calculator separates measured/tracked sinks from independently measured or upper-bounded inputs:

`E_residual = E_load + delta(E_stored) + E_losses - E_known_inputs`.

Known inputs are kept separate as mechanical, bias, RF, thermal, atmospheric and chemical contributions. A positive residual is only an **unresolved bookkeeping term**. It is not automatically quantum-vacuum energy or evidence of new physics.

Code:

- `sim/m2_v4_27_reservoir_isolation.py`
- `tests/test_m2_v4_27_reservoir_isolation.py`

## 2. V4.26 reference impulse

The first V4.26 simulation used the illustrative values

- impulse charge `DeltaQ = 10 nC`;
- resonator capacitance `C = 10 nF`.

The electrostatic energy associated with one imposed charge step is

`E = DeltaQ^2 / (2 C) = 5 nJ/event`.

At 50 events/s this source scale is only

`P = 250 nW`.

This is sufficient to test timing, ringdown and rectification. It is deliberately nowhere near a claimed useful-power Testatika regime.

## 3. Event-energy scale required by useful output

For event rate `f = 50 Hz`, a sustained real power `P` requires at least

`E_event = P / f`

before losses are included.

| target real power | required energy/event | ratio to 5-nJ V4.26 reference |
|---:|---:|---:|
| 1 W | 0.02 J | 4.0e6 |
| 100 W | 2 J | 4.0e8 |
| 300 W | 6 J | 1.2e9 |
| 3000 W | 60 J | 1.2e10 |

This is the most important V4.27 result.

A mechanism that only explains nanjoule timing pulses has **not** explained the reported watt/kilowatt power. To reach 100 W at 50 Hz, the energy transferred per event must be about four hundred million times the V4.26 reference impulse. For a 3-kW claim, the gap is about twelve billion.

Resonance and rectification may organize energy efficiently, but they do not erase this scale requirement.

## 4. Charge-flow requirement at a hypothetical 100-kV internal transfer level

If the relevant energy transfer occurred near `100 kV`, the minimum average current scale is

`I = P / V`

and the idealized charge transferred per 50-Hz event is

`DeltaQ = P / (f V)`.

| target power | average current at 100 kV | charge/event at 50 Hz |
|---:|---:|---:|
| 1 W | 10 uA | 0.2 uC |
| 100 W | 1 mA | 20 uC |
| 300 W | 3 mA | 60 uC |
| 3000 W | 30 mA | 600 uC |

These values are useful because every proposed reservoir can now be rejected or retained by a direct current/charge bound.

Example: a proposed atmospheric/ion mechanism for 100 W at a 100-kV working potential must ultimately support an energy-flow scale equivalent to roughly `1 mA` average at that potential, not merely occasional picoampere or nanoampere signals.

The exact voltage at which energy crosses the source boundary is unknown; `100 kV` is only a comparison scale taken from historical high-voltage descriptions. The correct experiment must measure the real source-port voltage and current simultaneously.

## 5. Equivalent 10-nF capacitor scale

If one asks what voltage on the illustrative `10 nF` resonator would contain the required event energy,

`E_event = 1/2 C V^2`, therefore `V = sqrt(2 E_event / C)`.

At 50 Hz:

| target power | event energy | equivalent 10-nF voltage |
|---:|---:|---:|
| 1 W | 0.02 J | 2.0 kV |
| 100 W | 2 J | 20.0 kV |
| 300 W | 6 J | 34.6 kV |
| 3000 W | 60 J | 109.5 kV |

This does **not** mean a Testatika used a 10-nF capacitor or discharged it fully every event. It shows the scale relation between capacitance, voltage and real energy.

An important consequence follows: very high voltage is not by itself evidence of high power, but tens of joules per event at 50 Hz necessarily imply substantial charge/field energy somewhere in the system.

## 6. Energy-accounting gate before any exotic interpretation

For one common measurement interval define

`E_demand = E_load + delta(E_stored) + E_losses`

and

`E_known = E_mechanical + E_bias + E_RF + E_thermal + E_atmospheric + E_chemical`.

Then

`E_X = E_demand - E_known`.

Interpretation:

- `E_X ~= 0` within uncertainty: known-source model closes;
- `E_X < 0`: one or more inputs/sinks are overestimated or missing from the bookkeeping;
- `E_X > 0`: unresolved source term, but **not yet anomalous**;
- only a repeatable positive `E_X` well above the complete uncertainty budget justifies searching for an unmodeled reservoir.

Independent one-sigma uncertainties are combined conservatively in the calculator by root-sum-square. A `5 sigma` residual is only a metrology gate; systematic errors still have to be excluded separately.

## 7. V4.26 bookkeeping re-check

Using the rounded V4.26 reported terms:

- load leakage `1.484e-11 J`;
- storage increase `7.672e-9 J`;
- resonator loss `2.2676e-8 J`;
- diode loss `1.9637e-8 J`;
- imposed pump `5.000e-8 J`;

we obtain

`E_demand = 4.999984e-8 J`

and

`E_residual = -1.6e-13 J`.

That mismatch is at the rounding/numerical level and confirms the earlier conclusion: the passive resonance/diode model closes without an unknown reservoir.

## 8. Consequence for the candidate sources

V4.27 turns the source question into quantitative falsification:

### Mechanical/boundary work

Measure shaft torque and angle/speed synchronously. If the per-event mechanical work tracks the electrical event energy, the source is conventional electromechanical conversion.

### Initial/electret/dielectric storage

Measure every capacitor/electret surface state before and after a long run. A declining stored-energy inventory can mimic autonomous operation over short demonstrations.

### Atmospheric ions / corona

Measure actual source-port ion current and potential. Compare `integral V I dt` with the required event energy. Humidity dependence alone is not evidence of atmospheric power extraction.

### RF/environmental electromagnetic pickup

Bound absorbed RF energy with shielding and independent field measurements. High resonator Q can increase voltage amplitude but cannot make the absorbed real power exceed the incoming/pump power.

### Thermal / chemical

Track temperatures, mass/material change, ozone/corona chemistry and any electrochemical potential. These terms must be quantitatively bounded before an unexplained residual is claimed.

### Quantum-vacuum / unknown field reservoir

This category remains **last**, not first. It becomes experimentally relevant only if a positive residual survives the complete conventional source inventory with adequate uncertainty margin and independent replication.

## 9. Strongest new conclusion

V4.26 made the crystal/resonance timing mechanism plausible. V4.27 shows that this is only the **routing layer**.

The missing-source problem is now numerically explicit:

`timing pulse scale: nJ/event`

versus

`100-W class at 50 Hz: J/event`

versus

`3-kW class at 50 Hz: tens of J/event`.

Therefore the next useful experiment is not another diode topology. It is a simultaneous measurement of:

`mechanical work/event + source-port V/I + storage delta + load energy + environmental bounds`.

Any candidate reservoir that cannot supply the required joules per event is eliminated regardless of whether it can reproduce the observed timing, voltage, resonance or threshold behavior.
