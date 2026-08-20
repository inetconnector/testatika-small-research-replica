# M2-V4.26 simulation results — 2026-08-20

## Purpose

This note records the first numerical test of the V4.26 hypothesis:

`slow event clock -> resonant phase memory -> passive crystal/diode gate -> directed storage charge`.

The model is deliberately conventional and energy-accounted. Each rotor/segment event is represented as an explicit charge impulse into a damped parallel LC mode. A passive diode branch can conduct only when the resonator voltage exceeds the storage voltage plus a threshold. No anomalous or quantum-vacuum source term is present.

Code:

- `sim/m2_v4_26_two_time_phase_resonance.py`
- `tests/test_m2_v4_26_two_time_phase_resonance.py`

## Baseline parameters

Illustrative low-energy values, not historical Testatika component measurements:

- resonator `C = 10 nF`;
- resonator `L = 10 mH`;
- resonator `Q = 20`;
- storage `C = 100 nF`;
- imposed event charge `10 nC`;
- event rate `50 Hz`;
- diode drop `0.2 V`;
- diode series resistance `1 kOhm`;
- duration `0.2 s` / 10 imposed events.

The resulting electrical eigenfrequency is

`f0 = 15.915 kHz`.

The event-frequency ratio is

`f0 / fevent = 318.31`.

The modeled ringdown amplitude time constant is

`tau = 0.400 ms`,

while the event period is

`20 ms = 50 tau`.

### Consequence

At this baseline the resonant burst is essentially gone before the next rotor/segment event. Therefore the model does **not** support coherent resonance accumulation from one 50-Hz event to the next at `Q=20`. It supports the narrower two-timescale mechanism:

`one slow event -> one fast ringdown burst -> phase-selective rectification within that burst`.

That is an important refinement of V4.26.

## Baseline result with passive diode enabled

Numerical result:

- 10 imposed events;
- 25 separate diode-conduction windows;
- maximum resonator voltage about `1.0 V`;
- storage voltage after 0.2 s about `0.3917 V`;
- imposed pump/boundary energy `5.000e-8 J`;
- final storage energy `7.672e-9 J`;
- resonator loss `2.2676e-8 J`;
- diode loss `1.9637e-8 J`;
- load leakage energy `1.484e-11 J`;
- final resonator energy negligible;
- numerical energy residual about `-1.39e-13 J`.

The residual is only about `2.8e-6` of the imposed pump energy, so the bookkeeping closes to numerical accuracy.

Approximate fate of the imposed energy:

- storage: `15.3 %`;
- resonator loss: `45.4 %`;
- diode loss: `39.3 %`;
- load leakage: `0.03 %`.

### Interpretation

The test confirms that a passive nonlinear gate can turn a fast alternating ringdown into directed DC accumulation. The diode/crystal can therefore plausibly be a **phase-selection / charge-routing component** without being an energy source.

## Control: diode removed

With identical imposed impulses but the diode branch disabled:

- storage voltage remains `0 V`;
- storage energy remains `0 J`;
- the imposed energy decays in the resonator loss path;
- energy balance still closes.

This directly supports the functional statement:

`resonance alone does not accumulate DC; nonlinear one-way transfer is required`.

## Control: no imposed pump / no initial energy

With zero impulse charge and all initial states at zero:

- no resonator growth occurs;
- no diode conduction occurs;
- no storage charging occurs.

Therefore this passive V4.26 model does **not** self-start and does not extract energy from a modeled background. Any future claim of autonomous growth requires an explicit additional physical reservoir or a measured unexplained residual.

## Capacitance / field-perturbation threshold test

A second run used a smaller `3 nC` event impulse so that the diode threshold sits near the resonator voltage step. Effective resonator capacitance was then varied as a proxy for a nearby field/metal-plate perturbation.

| C/C0 | f0 | storage V | conduction windows | result |
|---:|---:|---:|---:|---|
| 0.80 | 17.794 kHz | 0.0604 V | 20 | conducts |
| 1.00 | 15.915 kHz | 0.0320 V | 20 | conducts |
| 1.10 | 15.175 kHz | 0.0209 V | 20 | conducts |
| 1.20 | 14.529 kHz | 0.0127 V | 12 | weakened |
| 1.40 | 13.451 kHz | 0.00249 V | 10 | barely conducts |
| **1.50** | **12.995 kHz** | **0 V** | **0** | **blocked** |
| 1.60 | 12.582 kHz | 0 V | 0 | blocked |
| 2.00 | 11.254 kHz | 0 V | 0 | blocked |

The abrupt cutoff at `C/C0 = 1.5` has a simple reason in this illustrative case:

`Delta V = Delta Q / C`.

For `Delta Q = 3 nC` and `C = 15 nF`, the initial step is exactly `0.2 V`, equal to the diode threshold, so the branch no longer turns on.

### Consequence

This reproduces the qualitative V4.1 result with an explicit resonator: a continuous capacitance perturbation can cause an abrupt macroscopic loss of directed charge transfer when a nonlinear threshold is crossed.

That makes a nearby floating metal plate a plausible **field/timing/threshold perturbation** without making it an energy shield.

## What this test confirms

The simulation confirms four limited claims:

1. A slow event can excite a much faster electrical ringdown.
2. A passive nonlinear gate can select part of that later phase and accumulate DC.
3. A capacitance shift can move the system through a sharp conduction threshold.
4. All of this is compatible with ordinary energy conservation when the event/pump energy is explicitly counted.

## What this test rejects or weakens

At the baseline values it weakens the idea that a `50 Hz` rotor-event train directly maintains a `~16 kHz` resonator by coherent cycle-to-cycle buildup: the modeled burst decays about 50 amplitude time constants before the next event.

For direct inter-event resonance to matter, at least one of the following must be true:

- the relevant electrical resonance is much lower;
- the event rate is much higher than assumed;
- the resonator Q is extraordinarily high;
- multiple sub-events occur within each apparent rotor-sector passage;
- another continuously pumped oscillator exists.

Those are separate hypotheses and require evidence.

## Current mechanism status

The strongest surviving V4.26 interpretation is now:

`slow electrostatic/geometry event`
`-> fast local ringdown`
`-> crystal/diode phase gate`
`-> directed storage-charge step`
`-> next slow event`.

This gives a concrete technical role for resonance and the crystal while leaving the sustained real-power reservoir **UNKNOWN**.

No result in this simulation supports a quantum-vacuum energy source. Such a hypothesis would require a reproducible positive energy residual after mechanical/boundary work, initial storage, RF, thermal, atmospheric, chemical/corona and measurement contributions are independently bounded.
