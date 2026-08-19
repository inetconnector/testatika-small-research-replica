# M2 V4.22 — source reaction, source impedance and closed-boundary energy test

## Status

**DERIVED diagnostic / energy-source discriminator.**

This document does not change the historical M2 wiring, does not identify the `crystal`, and does not add an HF/Tesla stage to the small-machine baseline. Direct Marinov correspondence remains the controlling small-machine evidence: floating rotor wires, two-terminal side condensers, no conventional built-in motor, and no Tesla/AC interpretation of the visible side spirals.

The question here is narrower and more fundamental:

> If a sustained historical output of order 100 W were real, what source reaction or energy flux must necessarily exist somewhere outside the internal charge-sorting cycle?

Canonical calculator: `sim/m2_v4_22_source_reaction_boundary.py`.

---

## 1. The machine cannot hide the energy balance inside its own terminology

The rotor, grids, `crystal`, magnets, pots, rear plate and any resonant stage may redistribute, gate, commutate, transform or temporarily store energy. None of those internal labels removes the requirement that sustained real output must be balanced by real input.

For a closed measurement surface around the complete machine,

`P_EM,in + P_mech,in + P_thermal,in + P_chemical,in`

`= P_load + P_loss + dU_E/dt + dU_B/dt + dU_chem/dt + dK/dt + ...`

Over a periodic steady state, stored electrostatic, magnetic and kinetic energies return to the same average value, so their cycle-average derivatives vanish. Then

`<P_load> <= <P_EM,in + P_mech,in + P_thermal,in + P_chemical,in>`

minus losses.

This is the decisive source-search rule. `Regeneration`, `resonance`, `charge ordering`, `crystal gating` and electrostatic motor feedback are internal transfer mechanisms unless one of them is explicitly connected to an external reservoir.

For the M2 evidence base, the rear-metal-plate stop, humidity sensitivity and East-West startup instruction remain important perturbations, but their mechanisms are still **UNKNOWN**. They do not by themselves identify the bulk source.

---

## 2. Source impedance is more decisive than source voltage

Represent any external electrical reservoir at the machine port by an RMS Thevenin equivalent:

`V_oc` in series with `R_s`.

Even granting perfect lossless matching, the maximum real load power is

`P_max = V_oc^2 / (4 R_s)`.

Therefore the largest source resistance compatible with target power `P` is

`R_s,max = V_oc^2 / (4 P)`.

For `P = 100 W`:

| open-circuit source voltage | maximum `R_s` even with ideal matching |
|---:|---:|
| 10 kV | 250 kΩ |
| 100 kV | 25 MΩ |
| 250 kV | 156.25 MΩ |
| 1 MV | 2.5 GΩ |

This makes the source problem very concrete. A spectacular voltage is not enough. The source must also be many orders of magnitude stiffer than the ordinary fair-weather atmospheric circuit.

---

## 3. Fair-weather Earth–ionosphere source fails by about ten orders of source impedance

V4.14/V4.18 used a deliberately generous whole-column comparison:

- `V_oc ~= 250 kV`;
- current available to a `0.1 m^2` local collector at `~2 pA/m^2` fair-weather current density: `~0.2 pA`;
- effective source resistance scale `R_s ~= 1.25e18 ohm`.

With ideal matched loading,

`P_max = (250 kV)^2 / (4 * 1.25e18 ohm) ~= 12.5 nW`.

To obtain 100 W from that same source resistance would require

`V_oc >= 2*sqrt(P*R_s) ~= 22.36 GV`.

For 300 W the requirement rises to about

`38.73 GV`.

This is not a small mismatch that a better rectifier, resonator or variable capacitor can repair. It is the missing low-impedance channel problem.

**DERIVED conclusion:** ordinary fair-weather Earth–ionosphere DC remains incompatible with the claimed 100-W class by source impedance, even if one grants the full global potential and ideal matching.

---

## 4. A 100-kV / 100-W bus must be electrically stiff

If the useful electrical side is represented by

`100 kV rms` and `100 W`,

the equivalent resistive load is

`R_load = V^2/P = 100 Mohm`.

For a simple Thevenin source feeding that load, terminal-voltage droop imposes a much stronger source-resistance requirement than the absolute maximum-power condition:

| allowed voltage droop | maximum `R_s` |
|---:|---:|
| 1% | ~1.01 MΩ |
| 5% | ~5.26 MΩ |
| 10% | ~11.11 MΩ |
| 20% | 25 MΩ |

With the optimistic atmospheric `R_s ~= 1.25e18 ohm`, the loaded/open-circuit voltage fraction against a 100-MΩ load would be only about

`8e-11`.

So a high-voltage atmospheric bias can exist while still being completely unable to behave as the stiff source required by a 100-W load.

---

## 5. The missing real current is also enormous relative to fair weather

Real power requires an in-phase current component:

`I_real = P/(V*power_factor)`.

At unity power factor:

- `100 W @ 100 kV` -> `1 mA`;
- `100 W @ 250 kV` -> `0.4 mA`.

Spread over `0.1 m^2`, those correspond to current-density scales of

- `0.01 A/m^2` at 100 kV;
- `0.004 A/m^2` at 250 kV.

Compared with a fair-weather atmospheric conduction-current scale of order `2 pA/m^2`, these are approximately

- `5e9` times larger;
- `2e9` times larger.

Again, this is a real-current requirement, not a displacement-current amplitude. V4.18/V4.19 showed that pF-scale geometry can support mA-scale **reactive** current if a large alternating voltage already exists. V4.22 shows why that is not enough: the in-phase source current must still come from somewhere.

---

## 6. Finite electrostatic storage can imitate power only briefly

A capacitor stores

`U = 1/2*C*V^2`.

Examples:

| reservoir | stored energy | ideal duration at 100 W |
|---|---:|---:|
| 50 pF @ 100 kV | 0.25 J | 2.5 ms |
| 50 pF @ 250 kV | 1.5625 J | 15.625 ms |
| 100 pF @ 100 kV | 0.5 J | 5 ms |
| 1 nF @ 100 kV | 5 J | 50 ms |
| 1 nF @ 250 kV | 31.25 J | 0.3125 s |

Therefore electrostatic precharge, electret-like conditioning or hidden capacitance can explain startup memory, transients or short demonstrations, but not sustained 100 W unless the reservoir is continuously recharged.

The recharge path is the source.

---

## 7. What `source reaction` means experimentally

If a controlled external source drives the machine, sustained extraction must change the source's real-power balance.

For transfer efficiency `eta`, the minimum source power increase is

`Delta P_source >= P_load / eta`.

For a 100-W load:

| end-to-end efficiency | minimum source real-power increase |
|---:|---:|
| 100% | 100 W |
| 50% | 200 W |
| 10% | 1 kW |
| 1% | 10 kW |

A stiff source may show little voltage change, but its current/input power must increase. A high-impedance source may instead show strong voltage droop. Either is a source reaction.

This gives a more discriminating test than observing high voltage inside the machine.

---

## 8. Important nuance: a remote geophysical reservoir need not show an obvious local `generator slowdown`

If the hypothetical reservoir is the Earth, atmosphere, ionosphere or magnetosphere, its total stored energy is so large that a 100-W extraction would not measurably change the global reservoir.

That does **not** evade conservation. It only moves the reaction into the transmission channel.

A sustained 100-W output still requires at least 100 W of **net inward energy flux across a local closed boundary around the machine**, plus losses.

For a boundary area of:

- `0.1 m^2`: average net inward flux `>= 1000 W/m^2`;
- `0.5 m^2`: `>= 200 W/m^2`;
- `1 m^2`: `>= 100 W/m^2`.

Large reactive E/H fields can exist with near-zero cycle-average real flux. Therefore the required observable is the phase-correct net real power/energy flux, not field amplitude alone.

This is the local form of the source-reaction requirement and applies even when the remote reservoir is effectively infinite.

---

## 9. Consequence for the current M2 working hypothesis

The evidence-compatible functional chain may still be

`external field/boundary`

`-> floating rotor + grids/pickups`

`-> phase-selective nonlinear gate / crystal`

`-> pots/storage`

`-> load + electrostatic rotor feedback`.

But after V4.14–V4.22 the first arrow must satisfy a much stronger condition:

`external reservoir -> LOCAL LOW-IMPEDANCE REAL-POWER CHANNEL -> M2`.

The following do **not** by themselves satisfy that requirement:

- fair-weather atmospheric potential;
- ordinary atmospheric ion current;
- static permanent-magnet field;
- pF-scale capacitance without a powered AC source;
- resonance without a source;
- rear-plate capacitance;
- human/body capacitance;
- stored electrostatic charge after startup.

A strong powered HF/near-field source remains physically capable in principle, as V4.21 quantified, but it would be a real external source with corresponding loading and field strength. It remains a **comparison hypothesis**, not historical M2 evidence.

---

## 10. Highest-value low-voltage experiment: calibrated source substitution

Use only an isolated, current-limited low-voltage field fixture.

Drive the front/rear environmental plates from a source whose RMS voltage, current, phase and source impedance are known. Run the same passive M2 configuration under three states:

1. source present, machine detuned / storage disconnected;
2. source present, machine tuned / storage connected but unloaded;
3. source present, machine tuned / defined resistive load connected.

Record simultaneously:

- source voltage and current;
- source real power `P_source = <v(t)i(t)>`;
- front/rear complex admittance;
- storage-energy rate;
- load real power;
- rotor mechanical input/output if rotating;
- RH and temperature;
- rear-plate state.

The decisive signature is

`Delta P_source ~= P_load + Delta P_loss + Delta(dU/dt)`

within measurement uncertainty.

If internal voltage rises sharply but `Delta P_source` remains near zero, the effect is resonance/reactive storage, not a demonstrated energy source.

If the source is intentionally made high impedance, the complementary signature should be terminal-voltage droop rather than a large source-current increase.

---

## 11. Current source ranking after V4.22

1. **Ordinary fair-weather Earth–ionosphere DC:** rejected for 100-W class by source impedance and current-density bounds.
2. **Ordinary 230-V/50-Hz building stray pickup:** rejected by V4.20 for pF/nF accidental coupling.
3. **Ambient RF background:** far below the required real-power field scale in measured ordinary environments; strong powered local HF remains a separate conventional possibility.
4. **Rear plate / human / building capacitance:** important coupling and quench variables, but not independent energy reservoirs.
5. **Permanent magnets / static electrostatic storage:** bias, timing and finite-buffer candidates only unless continuously repumped.
6. **Mechanical, chemical, thermal, airflow or other conventional inputs:** still require explicit quantitative exclusion in a closed experiment.
7. **Historical output overestimate / incomplete metrology:** remains open because no surviving closed independent energy balance establishes the claimed net output.
8. **Unknown external channel / new physics:** remains `UNKNOWN`; it is not promoted until all conventional boundary terms are measured below the claimed output with adequate uncertainty.

The source hunt should therefore use one invariant criterion:

> **A sustained 100-W claim survives only if approximately 100 W of net energy can be traced crossing the machine boundary, or if a controlled closed-boundary measurement demonstrates that all known inputs are smaller than the output by more than the full uncertainty budget.**

That criterion does not prejudge the source. It tells us exactly what evidence would distinguish an unusual energy channel from ordinary coupling, storage or measurement error.
