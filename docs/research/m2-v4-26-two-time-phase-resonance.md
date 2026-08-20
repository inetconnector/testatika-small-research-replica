# M2-V4.26 — Two-time phase memory, resonance and crystal gating

**Date:** 2026-08-20  
**Status:** working hypothesis / falsifiable model, not an asserted original Testatika circuit

## 1. Core idea

The useful interpretation of a "potential between two times" is **not** a literal voltage between `t1` and `t2`. The physically meaningful object is a difference/correlation between two states of the same time-varying electrostatic network:

`state(t1) != state(t2)`

with a resonator retaining phase memory from `t1` until `t2`, and a nonlinear crystal/diode selecting which phase is allowed to transfer charge.

For a time-varying capacitance network the electrostatic energy may be written

`U = 1/2 q^T C(theta)^(-1) q`.

Differentiating gives the bookkeeping identity

`dU/dt = V^T dq/dt - 1/2 V^T (dC/dt) V`.

The second term is the power exchanged with whatever changes the geometry/capacitance. Therefore a rotating or moving boundary can pump an electrical mode, but that energy is then accounted for as mechanical/boundary work unless an additional reservoir is measured.

## 2. Why resonance changes the topology question

A resonator stores phase information. A short charge impulse at `t1` can produce a ringdown

`V(t) = A exp(-t/tau) cos(omega0 t + phi)`

with

`omega0 = 1/sqrt(L C)`.

The crystal/diode can then conduct at a later phase `t2` while blocking the opposite phase. In that sense it is a **two-time phase gate**:

`impulse at t1 -> resonant memory -> selected phase at t2 -> one-way charge transfer`.

This is operationally similar to synchronous rectification or phase-sensitive detection, but with a passive/nonlinear element if no external gate signal exists.

## 3. Source compatibility

The hypothesis is motivated by, but must not be confused with, the following source lines already separated elsewhere in the repository:

- non-contact capacitive pickup / `Taster` in the Schneider/Weber retrospective witness line;
- Baumann->Marinov `crystal` terminology with material/function unresolved;
- Methernitha institutional `rectifying diode` terminology associated with keeping an attraction/repulsion cycle in step;
- Holzherr's memory of an early top module with a coarse winding around a central conductor and four leads;
- Weber's retrospective statement that a diode-like element could rectify very high frequencies;
- Cathomen's later synchronization / sensor language and separate reduced-pressure component on other machine variants.

These do **not** prove one common four-terminal resonant rectifier. V4.26 treats that topology as a testable bridge hypothesis only.

## 4. Minimal cycle

A minimal two-timescale cycle is:

1. rotor/segment motion changes the capacitance matrix `C(theta)`;
2. a non-contact pickup receives a displacement-charge impulse;
3. the impulse excites an electrical eigenmode;
4. the mode rings for a short time at `f0`;
5. the crystal conducts only during one polarity/threshold window;
6. charge is transferred into a floating reservoir / pot / storage capacitor;
7. the stored potential biases the next electrostatic torque/collection phase;
8. the next segment repeats the cycle.

The important separation is:

`slow mechanical/event clock -> short electrical transient -> resonant ringdown -> nonlinear rectification -> slow DC/storage state`.

This does **not** require the rotor itself to rotate at the electrical resonance frequency.

## 5. "Potential between two times" as a phase-space loop

The cleanest experimental signature is not `V(t2)-V(t1)` by itself, but a reproducible non-zero loop area in charge-voltage space.

For an electrical port, energy transfer over a cycle is

`W = integral V dq`.

If the trajectory in `(q,V)` closes with zero enclosed directed area, there is no net electrical work from that port over the cycle. A diode/threshold can reshape the path so that charge is accepted at one phase and blocked at another, yielding a directed loop.

However, the loop area is only an energy-transfer measure. It does not identify the source. The source must be found from the simultaneous mechanical, stored-field, environmental and electrical energy terms.

## 6. Parametric-resonance branch

If the rotating geometry modulates a resonant capacitance,

`C(t) = C0 [1 + m cos(Omega t)]`,

then the electrical eigenfrequency is time-dependent. In the simplest Mathieu-like case strong parametric gain can occur near

`Omega ~ 2 omega0`

(and in narrower higher-order tongues).

For a Testatika geometry this direct condition may be difficult if the mechanical/event frequency is only tens of hertz and the electrical mode is much faster. Therefore V4.26 distinguishes two mechanisms:

### A. Direct parametric modulation

A low-frequency electrical eigenmode is pumped directly by `C(theta)`.

Prediction: narrow output peaks at specific rpm/event-frequency ratios.

### B. Impulse-triggered ringdown

Slow charge accumulation reaches a threshold; a fast nonlinear event then launches a much higher-frequency ringdown.

Prediction: electrical burst frequency is largely set by `L` and `C`, while burst repetition is set by rotor/segment/threshold timing.

The second branch is currently more compatible with the project's two-timescale working model.

## 7. Crystal/top-module candidate model

A four-terminal research carrier should remain possible:

`X1--X2`: resonant/inductive branch

`X3--X4`: nonlinear crystal/rectifier branch

No identity is asserted. Experimental modules should be replaceable and separately characterized.

Measurements required before energizing the full replica:

- DC I-V in both polarities;
- junction/differential capacitance versus bias;
- small-signal impedance versus frequency;
- ringdown frequency `f0` and quality factor `Q`;
- two-port transfer (`X1-X2` to `X3-X4`) if four independent terminals exist;
- threshold/hysteresis versus temperature and humidity;
- phase of diode current relative to pickup voltage and rotor angle.

## 8. Energy-source guardrail

A passive resonator + passive rectifier does not by itself create energy. In a time-varying-capacitance model the energy supplied by the modulation appears explicitly through

`P_boundary = -1/2 V^T (dC/dt) V`.

Therefore a convincing anomaly requires, cycle by cycle,

`E_load + delta(E_stored) + losses > E_mechanical + E_bias + E_known_environment`

with uncertainty small enough that the positive residual cannot be explained by instrumentation, initial charge, rotor kinetic energy, corona chemistry, thermal gradients, RF pickup or atmospheric-field/ion current.

The quantum-vacuum interpretation remains **unsupported** unless such a residual survives those controls. A two-time correlation or resonant phase memory is a mechanism for selective transfer, not evidence of a vacuum-energy reservoir.

## 9. Falsifiable predictions

If V4.26 is directionally correct:

1. The top/crystal module should show a measurable nonlinear threshold/asymmetry and a distinct electrical eigenfrequency or coupled resonance.
2. Pickup voltage and crystal current should have a reproducible phase relationship to rotor angle.
3. Replacing the nonlinear element by open/short/symmetric resistance should strongly alter DC accumulation even if the raw pickup transient remains.
4. Replacing it by a known fast diode should reproduce at least part of the phase-selection behaviour if the historical material is not essential.
5. Output should show narrow phase/rpm/gap regions if resonance is central, rather than only monotonic scaling with rpm.
6. A nearby floating metal plate should measurably shift capacitance/eigenfrequency/threshold timing before the macroscopic effect disappears.
7. In an impulse-triggered branch, burst repetition frequency should track rotor/segment events while intra-burst frequency should remain approximately fixed by the electrical network.
8. With all known pumps removed and all storage discharged, a passive version should decay rather than self-amplify.

## 10. Highest-value experiment

Use a low-stored-energy bench version first. Measure simultaneously:

- rotor angle `theta(t)`;
- pickup voltage/current;
- all storage-capacitor voltages;
- crystal current;
- top-module ringdown waveform;
- rotor torque / drive-motor electrical and mechanical input;
- temperature and relative humidity.

Then compute per cycle:

- `W_pickup = integral V_pickup dq_pickup`;
- `W_boundary` from measured torque/angle or a calibrated capacitance/force model;
- `E_store = 1/2 C V^2` for every storage capacitor;
- `E_load`;
- losses and residual.

The decisive plot is a synchronized overlay of rotor angle, resonant voltage, crystal current and storage-charge increment. If the crystal is genuinely a phase gate, conduction events must cluster at a reproducible phase and each event should correspond to a directional storage-charge step.

## 11. Current conclusion

V4.26 sharpens the working architecture to:

`spatially varying capacitance + temporal phase memory + resonance + nonlinear phase-selective charge transfer`.

This architecture can explain how a slow mechanical machine could create short fast electrical events and accumulate DC without rubbing brushes. It still leaves the sustained real-power reservoir **UNKNOWN**.
