# M2 V4.18 — explicit front/rear environmental two-port and rear-plate return

## Status

**DERIVED diagnostic / HYPOTHESIS discriminator.** This document does not claim that the historical M2 had an external AC transmitter or that Marinov's rear metal plate was grounded. It asks the most concrete remaining coupling question after V4.14–V4.17:

> **Can the visible/front environmental coupling plus the rear/backboard/base coupling form a two-terminal displacement-current path capable of carrying the required milliamp-scale charge, and can that path deliver real power rather than only reactive current?**

Canonical calculator: `sim/m2_v4_18_two_port_return.py`.

---

## 1. The model must have two environmental terminals

A floating machine cannot sustain a net DC current through only one environmental terminal. In steady periodic operation,

`dQ_machine/dt = I_front + I_rear + I_base + ...`

and the cycle-average common-mode charge must remain bounded.

The minimal external model is therefore

`ENV_FRONT / sky-side`

`-> C_front`

`-> machine conversion/load`

`-> C_rear`

`-> ENV_REAR / Earth-base-side`.

For a simple series capacitive path,

`C_eq = C_front*C_rear/(C_front + C_rear)`.

If the rear metal plate itself is floating rather than Earth-referenced, its return introduces another series coupling, e.g.

`machine -> C_machine-plate -> floating plate -> C_plate-Earth -> Earth`.

Therefore the plate's electrical state — absent, floating, resistively referenced, or grounded — is not a cosmetic detail.

This is consistent with mainstream capacitive power-transfer physics. A primary IEEE study by Zou et al., *Modeling Single-Wire Capacitive Power Transfer System With Strong Coupling to Ground* (DOI `10.1109/JESTPE.2019.2942034`), explicitly models ground coupling and ground equivalent impedance as part of the power-transfer path. The source is an active transmitter; ground coupling does not create energy.

A separate primary experimental/modeling study by Zhu et al., *Effect of Surrounding Conductive Object on Four-Plate Capacitive Power Transfer System* (arXiv `1907.11138`), used a capacitance-matrix model and a large nearby conductive plate. Bringing that plate closer changed the coupling and reduced output voltage through field redistribution/shielding. This gives a conventional precedent for a rear conductive plate strongly changing an electrostatic/capacitive machine even when the plate is not the energy source.

---

## 2. Current-carrying requirement is surprisingly plausible geometrically

For a sinusoidal differential voltage, a capacitive path carries

`|I_C| = 2*pi*f*C_eq*V_rms`.

Set the explicit target

`I = 1 mA`

at

`V = 100 kV rms`.

The required **series equivalent capacitance** is:

| Frequency | `C_eq` for 1 mA @ 100 kV | two equal external ports each |
|---:|---:|---:|
| 1 Hz | 1.59 nF | 3.18 nF |
| 24 Hz | 66.3 pF | 132.6 pF |
| 50 Hz | 31.8 pF | 63.7 pF |
| 1 kHz | 1.59 pF | 3.18 pF |
| 100 kHz | 15.9 fF | 31.8 fF |
| 1 MHz | 1.59 fF | 3.18 fF |

This is a major refinement.

At rotor/event frequencies of order `24–50 Hz`, the required capacitive return is **tens of pF**, not farads. That is completely plausible as geometry in a 20-cm electrostatic apparatus.

So the coupling problem is **not** that a 20-cm device cannot carry 1 mA of displacement current through stray capacitance if a huge alternating differential voltage exists.

The unresolved problem is where the alternating high-voltage source gets its **real power**.

---

## 3. Rear-plate geometry lands in the interesting pF range

For an ideal parallel-plate scale,

`C ~= eps0*A/d`.

Take a deliberately simple comparison plate:

- area `A = 0.09 m²` (`30 cm x 30 cm`);
- air dielectric.

Then:

- 20 cm gap -> ~`4.0 pF`;
- 10 cm -> ~`8.0 pF`;
- 5 cm -> ~`15.9 pF`;
- 2 cm -> ~`39.8 pF`;
- 1 cm -> ~`79.7 pF`;
- 5 mm -> ~`159 pF`.

For two equal ports to provide the `66.3-pF` series equivalent needed for `1 mA @ 100 kV, 24 Hz`, each port would be about `132.6 pF`. An ideal 30 x 30 cm plate gets that capacitance at roughly

`6.0 mm`.

At `50 Hz`, each equal port needs only `63.7 pF`, corresponding to roughly

`12.5 mm`.

These are not absurd geometries.

A single `30 x 30 cm` rear plate only `2 cm` away has the ideal scale `~39.8 pF`. If every other part of the return were much larger, it could carry about

- `0.60 mA` at `100 kV, 24 Hz`;
- `1.50 mA` at `250 kV, 24 Hz`.

If **both** front and rear ports were only `39.8 pF`, their series equivalent is `~19.9 pF`, giving about

- `0.30 mA` at `100 kV, 24 Hz`;
- `0.75 mA` at `250 kV, 24 Hz`.

This is the first conventional coupling calculation in the current search that lands near the desired milliamp scale without an absurd component value.

But it is only a **current-carrying/reactive coupling scale**.

---

## 4. 1 mA at 100 kV can still mean zero watts

This distinction is decisive.

The apparent power magnitude is

`|S| = V_rms*I_rms`.

At `100 kV` and `1 mA`,

`|S| = 100 VA`.

Real power is

`P = V_rms*I_rms*cos(phi)`.

For an ideal capacitor,

`phi = 90 deg`

and

`P = 0`.

Therefore observing or calculating `1 mA` of displacement current at `100 kV` does **not** demonstrate the required `100 W`.

At exactly `100 kV / 1 mA`, 100 W requires

`cos(phi) = 1`.

At `250 kV / 1 mA`, 100 W still requires

`cos(phi) = 0.4`.

A real source, rectifier/nonlinear gate and load can make the input current acquire an in-phase component. But then the source must supply that real energy.

This is the quantity a modern experiment must measure:

`P_env = <v_front*i_front + v_rear*i_rear>`

over an integer number of cycles, with phase-correct instrumentation.

---

## 5. Resonance can remove reactance but not source resistance

Suppose the two environmental capacitors give `C_eq = 66.3 pF` at `24 Hz`.

Their reactance is

`X_C = 1/(2*pi*f*C_eq) ~= 100 Mohm`.

With an ideal zero-resistance voltage source and **no inductive compensation**, this series capacitive link feeding an optimally chosen resistor can deliver at most about

`50 W`

from `100 kV rms`. The optimum resistive load is `~100 Mohm`.

A lossless resonant network could cancel the `100-Mohm` capacitive reactance and thereby improve transfer. That is exactly what resonant capacitive-power-transfer systems do.

But after ideal compensation the maximum real power is still limited by the external source's Thevenin resistance:

`P_available <= V_source^2/(4 R_source)`.

Thus resonance can solve **reactance matching**. It cannot solve the V4.14 **source-impedance** deficit.

For the deliberately optimistic fair-weather full-column source

`V_oc = 250 kV`, `R_s ~= 1.25e18 ohm`,

even perfect lossless matching gives only

`~12.5 nW`.

That remains true whether the machine contains a tuned coil, magnetized grid, crystal gate, rear plate, or ideal impedance transformer.

---

## 6. Recharge time exposes why quasi-DC atmospheric potential is different from a 24-Hz 100-kV source

The Earth–ionosphere potential is not an ideal stiff `100–250 kV, 24-Hz` AC generator.

Use the `66.3-pF` series coupling required for the `1-mA/100-kV/24-Hz` current scale and the optimistic V4.14 atmospheric source resistance

`R_s ~= 1.25e18 ohm`.

The source-capacitance recharge time is

`tau = R_s*C ~= 8.29e7 s ~= 2.63 years`.

One rotor-event interval at 24 Hz is only

`41.7 ms`.

The first-order recharge fraction in one interval is only about

`5.0e-10`.

So a rotor cannot simply discharge a pF-scale capacitor and expect the ordinary fair-weather global circuit to refill it on every sector passage.

This is another expression of the same missing milliamp problem.

---

## 7. Variable capacitance does not make the recharge cost disappear

A rotating influence machine can convert a quasi-DC field into pulses by changing capacitances with angle:

`i = C(theta)*dV/dt + V*dC/dt`.

That absolutely can create alternating current internally even when the external bias is quasi-DC.

But the energy ledger must include the work associated with changing capacitance.

For fixed charge,

`U = Q^2/(2C)`;

for a constant-voltage source,

`U_C = 1/2*C*V^2`

and source/mechanical work exchange accompanies `dC`.

Therefore variable-C pumping offers two conventional possibilities:

1. **mechanical energy** pays for the electrical output; or
2. an **external electrical source** replenishes charge and supplies real energy.

It cannot turn a source that can supply only pA into a stiff mA source without another port or pump.

The M2 rotor may still be the commutator/timing element rather than the bulk mechanical source, but then the external real-power input must be found elsewhere.

---

## 8. Why the rear metal plate is now the most valuable historical perturbation

Marinov's rear metal-plate observation is unusually diagnostic because an external conductor can do at least three physically distinct things:

### A. Pure detuning

The plate changes parasitic capacitance and shifts an internal resonance.

Prediction:

- `f_res` shifts;
- Q/amplitude changes;
- if L/C is retuned to restore the original `f_res` and Q, operation should substantially recover.

### B. Field shielding / capacitance-matrix redistribution

The plate diverts electric-field lines and changes mutual capacitances among the rotor/stators/environment.

This behavior has direct conventional precedent in the Zhu et al. four-plate CPT experiment, where a nearby large conductor reduced output and changed field distribution.

Prediction:

- even after local resonator retuning, the transfer coefficient from external front/rear fields changes;
- floating versus grounded plate state matters through the capacitance matrix.

### C. Actual return-port modification

The plate is part of the environmental power loop. Changing its distance, area or grounding state alters `C_rear` and therefore the current that can flow between environmental terminals.

Prediction:

- external port current and **real input power** change systematically with plate geometry;
- grounding/resistive referencing produces a quantitatively different response from a truly floating plate;
- the effect persists even after compensating simple resonance detuning.

These three hypotheses can be separated experimentally.

---

## 9. Floating versus grounded rear plate is a critical test

If a conductive rear plate is directly Earth-referenced, the machine-to-plate capacitance can act almost directly as `C_rear`.

If the plate is floating, its effective return to Earth is instead approximately

`C_return = C_machine-plate * C_plate-Earth / (C_machine-plate + C_plate-Earth)`.

For example:

`C_machine-plate = 100 pF`

and

`C_plate-Earth = 100 pF`

give only

`C_return = 50 pF`.

So “metal plate present” is not a sufficient experimental description. One must record:

- plate size and distance;
- plate orientation;
- plate floating potential;
- capacitance to machine;
- capacitance/impedance to Earth/building;
- whether the experimenter is holding it;
- instrument grounds.

A human-held plate is itself capacitively coupled to floor/building/Earth and may behave very differently from the same plate suspended on dry dielectric supports.

---

## 10. An important external validation from capacitive power-transfer research

Modern capacitive wireless power systems support exactly the kind of reasoning required here, without implying anything anomalous.

Zou et al. (`10.1109/JESTPE.2019.2942034`) model a single-wire CPT system in which coupling to ground and ground equivalent impedance participate in the current path; resonance is used to tune the link. The energy still originates in the powered transmitter.

Zhu et al. (`arXiv:1907.11138`) model a four-plate CPT system plus an additional conductive object using a `5 x 5` mutual-capacitance matrix. Their experiment with four `100 x 100 mm` plates and an additional `300 x 300 mm` conductor found that bringing the extra conductor closer reduces output voltage and redistributes/shields the electric field.

Those results establish two useful conventional controls for Testatika research:

- a machine can appear “wireless” while the ground/environment is electrically part of the return path;
- a nearby rear plate can strongly suppress output through ordinary capacitance-matrix/field-boundary changes.

Neither result shows environmental free energy. They tell us exactly how to design the falsification experiment.

---

## 11. V4.18 experimental protocol — low voltage only

The most useful next physical experiment is a calibrated low-energy two-port transfer measurement.

Construct two large external electrodes around the passive replica:

`FRONT_ENV plate`

and

`REAR_ENV plate`.

Drive them differentially from a **current-limited, isolated low-voltage source** over a frequency sweep. Keep all Testatika internal nodes floating except through explicitly measured couplings.

Measure simultaneously:

- `V_front-rear(t)`;
- `I_front(t)` and `I_rear(t)`;
- machine common-mode charge/potential;
- internal pickup voltage/current;
- storage-capacitor energy change;
- rotor angle/speed if rotating;
- rear perturbation plate potential/current;
- RH and temperature.

Then determine:

`Y_env(f) = I_env(f)/V_env(f)`

and

`P_env = <V_env(t)*I_env(t)>`.

The critical quantity is not `|I|` alone but the **real part** of the measured admittance:

`G_env(f) = Re[Y_env(f)]`.

At `100 kV` equivalent, 100 W requires an effective conductance

`G_required = P/V^2 = 10 nS`

or an effective resistive scale

`R_required = 100 Mohm`.

That is the exact target to compare against the scaled transfer measurement.

---

## 12. Rear-plate A/B matrix

For each drive frequency and fixed safe excitation, test the same machine state with the perturbation plate:

1. absent;
2. present and fully floating on dry supports;
3. connected to Earth through a known high resistance;
4. directly Earth-referenced in the low-voltage test;
5. same geometry but insulating dummy plate;
6. same conductor at multiple distances.

At each point record:

- resonance frequency;
- Q/ring-down;
- external complex admittance;
- real input power;
- internal pickup amplitude/phase;
- common-mode machine potential.

Then retune any internal adjustable resonator to restore the no-plate resonance frequency and Q.

If suppression disappears, the historical effect is consistent with **detuning**.

If suppression remains but tracks capacitance-matrix geometry with negligible real-power change, it is consistent with **shielding/field redistribution**.

If the external **real conductance/power-transfer coefficient** changes strongly with the plate's Earth reference even after retuning, the plate is behaving as part of the missing environmental return port.

That is the highest-value discriminator currently available from the historical rear-plate observation.

---

## 13. Working result

V4.18 produces a more nuanced answer than the earlier simple atmospheric-power bounds.

### What now looks physically plausible

A Testatika-sized front/rear capacitive geometry can readily have **tens to hundreds of pF**. At `24–50 Hz`, that is enough to carry sub-mA to mA displacement current if the differential voltage really is tens or hundreds of kilovolts.

A nearby rear conductive plate can strongly alter that coupling through ordinary capacitance-matrix effects, and its floating/grounded state matters.

This makes the Marinov rear-plate observation more—not less—interesting as a diagnostic.

### What is still missing

Capacitive current is not real power.

The ordinary Earth–ionosphere DC source still has an enormous source impedance and cannot recharge the needed charge packets at rotor rate. Resonance can cancel reactance but cannot increase the source's available real power.

Therefore the most precise current hypothesis is now:

> **The machine may contain a geometrically plausible front/rear displacement-current transformer, but the bulk source still requires an unidentified active or low-impedance environmental differential potential.**

The next search target is no longer generic “energy from the atmosphere.” It is:


a) identify the two external nodes;

b) measure `C_front`, `C_rear`, and their complex admittance;

c) determine whether the rear plate changes only resonance/shielding or changes **real input power**;

and d) find a source capable of maintaining roughly

`G ~= 10 nS`

at the `100-kV` equivalent scale, i.e.

`~100 Mohm / ~1 mA / ~100 W`.

If that real component cannot be found, the capacitive environmental-return explanation also fails as the bulk 100-W source.