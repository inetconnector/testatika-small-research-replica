# M2 V4.20 — local building, mains-field and accidental-coupling bound

## Status

**DERIVED diagnostic / conventional-source discriminator.**

V4.19 showed that nearby conductive objects and a human/body return can materially alter a high-impedance electro-quasistatic machine. That immediately raises a conventional alternative:

> Could the missing real power simply come from ordinary building/mains infrastructure through stray capacitance, with the machine acting as a high-voltage transformer/rectifier?

V4.20 quantifies that possibility. It does **not** claim that the historical M2 was connected to mains and it does not add any mains/HF stage to the M2 baseline.

Canonical calculator: `sim/m2_v4_20_local_infrastructure_bound.py`.

---

## 1. Deliberately generous mains assumption

Use the common European reference:

- `V_mains = 230 V rms`;
- `f_mains = 50 Hz`;
- target real output `P = 100 W`.

To make the accidental-coupling hypothesis as favorable as possible, grant the **full 230 V rms across the stray coupling capacitance**. A genuinely floating tabletop machine would normally see less because it also requires a return path; therefore this is an optimistic upper bound for ordinary one-capacitance pickup.

At unity power factor a 100-W source at 230 V must supply

`I = P/V ~= 0.435 A`.

An ideal transformer could convert this to approximately `100 kV x 1 mA`, but it cannot remove the primary power requirement. At 100% efficiency the 230-V side still supplies `~0.435 A`; at 80% efficiency it supplies `~0.543 A`.

---

## 2. Ordinary pF/nF stray coupling at 50 Hz is far too weak

For a capacitive path,

`I_C = 2*pi*f*C*V`.

At 230 V / 50 Hz:

| stray `C` | current | apparent power `V*I` | ratio to 100-VA current scale |
|---:|---:|---:|---:|
| 50 pF | 3.61 µA | 0.831 mVA | ~1.2e5 lower |
| 150 pF | 10.84 µA | 2.49 mVA | ~4.0e4 lower |
| 1 nF | 72.26 µA | 16.6 mVA | ~6.0e3 lower |
| 10 nF | 0.723 mA | 0.166 VA | ~602 lower |

To carry `0.435 A` reactively at 230 V / 50 Hz requires

`C = I/(2*pi*f*V) ~= 6.02 uF`.

That is not a plausible accidental tabletop stray capacitance. It is roughly:

- `~40,000 x` a 150-pF body/environment scale;
- `~6,000 x` 1 nF.

And even `6.02 uF` would merely provide a **100-VA reactive current path** if ideal. A real 100-W load still requires an in-phase source-current component.

Thus ordinary 50-Hz electric-field pickup through pF/nF environmental capacitance cannot explain sustained 100 W.

---

## 3. Variable-capacitance switching does not rescue 230-V mains pickup

A separate optimistic bound assumes a coupling capacitor is fully charged from 0 to 230 V and completely discharged into a load once per rotor event.

Per event:

`E = 1/2*C*V^2`.

At 24 events/s:

- `150 pF`: `3.97 uJ/event`, only `~95.2 uW`;
- `1 nF`: `26.45 uJ/event`, only `~0.635 mW`;
- `10 nF`: only `~6.35 mW`.

To reach 100 W by that idealized full-swing mechanism at 230 V and 24 events/s would require

`C ~= 158 uF`.

This is even farther from the pF/nF environmental geometry.

Therefore a rotor cannot turn weak 50-Hz mains stray capacitance into a 100-W source merely by phase switching or charge sorting. The charge/energy must still enter through a sufficiently strong source port.

---

## 4. Could resonance make 50-Hz pF pickup large?

At 50 Hz, the reactance of `150 pF` is about

`21.2 Gohm`.

Losslessly resonating `150 pF` at 50 Hz would require

`L = 1/((2*pi*f)^2*C) ~= 67.5 kH`.

For `1 nF`, the requirement is still about

`10.1 kH`.

These are not credible hidden lumped inductances in the small machine. More importantly, ideal resonance does not create real source power; it only cancels reactance and magnifies circulating voltage/current.

So ordinary 50-Hz mains plus a pF-scale receiver is not rescued by a compact passive resonance.

---

## 5. The important transition occurs at hundreds of kHz to MHz

The same pF/nF geometry becomes a much better **current path** if the external source frequency is high.

Ask what frequency would let the full 230 V rms drive the `0.435-A` current magnitude associated with 100 VA:

- `150 pF` -> `~2.01 MHz`;
- `1 nF` -> `~301 kHz`.

At those frequencies the corresponding ideal resonance inductances are ordinary component scales:

- `150 pF @ 2.01 MHz` -> `~42 uH`;
- `1 nF @ 301 kHz` -> `~280 uH`.

This is an important **conditional near-hit**:

> A powered external RF/HF source at hundreds of kHz–MHz can couple substantial current through pF/nF capacitance, whereas ordinary 50-Hz mains cannot.

But this does not identify an energy source. It changes the question to:

> Was there a real powered HF/near-field source with sufficient field amplitude and real available power near the historical machine?

If yes, it should be measurable spectrally and spatially. It is not supplied by passive resonance, static magnets or the ordinary fair-weather atmospheric circuit.

The frequency transition is also an **experimental comparison hypothesis only**. Marinov's direct small-machine line rejects Tesla coils/AC as the M2 operating explanation, so V4.20 does not import an HF transmitter into the historical baseline.

---

## 6. Why stepping 230 V up to 100 kV changes no energy balance

An ideal transformer/impedance converter obeys approximately

`P_primary = P_secondary`.

So a hypothetical conversion

`230 V x 0.435 A -> 100 kV x 1 mA`

is perfectly conventional at the 100-W scale.

It would actually solve the *voltage/current-form* puzzle: high voltage and small current are easy to obtain by impedance transformation.

But it would also mean that somewhere the machine has a **real ~100-W connection to the building/source**. A few pF of 50-Hz stray coupling cannot be that connection.

This gives a sharp hidden-source discriminator:

- **pF/nF accidental 50-Hz coupling:** ruled out quantitatively for 100 W;
- **galvanic/low-impedance hidden source:** possible in principle, but no longer an environmental-energy hypothesis and should be detectable by isolation/current accounting;
- **powered HF/near-field source:** possible in principle if strong enough, but should produce measurable external spectrum/field and real source loading.

---

## 7. Highest-value low-voltage discriminator

No hazardous mains/HV injection is needed.

Use an isolated, current-limited low-voltage field fixture and characterize the replica as a receiver over frequency:

- 50 Hz;
- 1 kHz;
- 10 kHz;
- 100 kHz;
- 300 kHz;
- 1 MHz;
- a few MHz.

At each frequency measure:

- front/rear complex admittance;
- real input power;
- common-mode voltage;
- internal pickup/storage response;
- resonance frequency and Q;
- rear-plate state;
- magnetic-state control;
- rotor stopped / controlled-speed states;
- RH/temperature.

Separately, with the original machine location unavailable, a historical-source investigation should look for evidence of an external powered field source rather than infer one from resonance alone.

A real environmental/built-in receiver hypothesis survives only if the measured transfer function identifies a frequency band in which the required source field and **real source power** are physically plausible.

---

## 8. Current source ranking after V4.14–V4.20

The conventional source search is now sharply constrained:

1. **Ordinary fair-weather Earth-ionosphere DC:** far too high source impedance; nanowatt-scale optimistic available power.
2. **ELF/ULF resonant giant aperture:** electrically-small Q/ring-up bound makes a 20-cm passive receiver unusable on relevant timescales.
3. **Corona/air-ion collection:** useful as nonlinear gating under strong fields, but fair-weather charge transport is far below mA and a floating body self-biases.
4. **Local Earth rotation / geomagnetic field:** plausible bias/phase reference, not a local 100-W reservoir.
5. **Rear plate / human / building capacitance:** can absolutely perturb or quench the machine and can carry mA-scale *reactive* current at hypothesized HV, but does not itself supply the real energy.
6. **Ordinary 230-V/50-Hz stray pickup:** quantitatively far too weak through pF/nF coupling.
7. **Strong powered HF/near-field source or genuine low-impedance electrical input:** remains physically capable in principle, but would be a measurable external/conventional source and is not established historically.
8. **Stored chemical/electrical energy, overlooked mechanical input, or historical output overestimate:** remain open conventional alternatives until a closed long-duration energy balance exists.

The next source-hunt should therefore stop asking only whether a field is present and instead ask:

> **Which external port can deliver >=100 W of measured real power into the machine, and where is the corresponding source reaction/loading?**
