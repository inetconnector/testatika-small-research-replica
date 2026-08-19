# M2 V4.21 — real-power field bound for the remaining HF/environmental source hypothesis

## Status

**DERIVED diagnostic / source falsification bound.**

V4.20 leaves one conventional electrical route physically capable in principle: a **strong powered HF/near-field source** coupled to the floating machine through pF-scale environmental capacitances.

V4.21 tightens that route by correcting a subtle but important issue in earlier quick estimates:

`I = 2*pi*f*C*V`

is a displacement-current magnitude. Multiplying `V*I` gives apparent VA, **not the maximum real watts that can cross a lossless series capacitor into a resistive load**.

Canonical calculator: `sim/m2_v4_21_real_power_field_bound.py`.

No HF transmitter is added to the historical M2 baseline.

---

## 1. Exact ideal series-capacitor real-power bound

Take the most favorable simple circuit:

`ideal AC source Vs -> series coupling C -> resistive load R`.

With

`Xc = 1/(2*pi*f*C)`,

the load power is

`P = Vs^2 * R / (R^2 + Xc^2)`.

Differentiating with respect to `R` gives the maximum at

`R_opt = |Xc|`.

Therefore

`P_max = Vs^2 / (2*|Xc|)`

and

`Vs_required = sqrt(2*P*|Xc|)`.

At the optimum the source power factor is `1/sqrt(2) ~= 0.707`; equal real and reactive power circulate.

This is still extremely optimistic: source resistance, rectifier loss, dielectric loss, imperfect field overlap and receiver inefficiency all increase the required external source.

---

## 2. 50-pF coupling: exact 100-W source requirement

Use the V4.10/V4.18 comparison value `C = 50 pF` and a `0.20 m` machine-scale voltage span.

| external frequency | `|Xc|` | ideal `Vs` for 100 W | optimum current | equivalent `Vs/0.2m` field |
|---:|---:|---:|---:|---:|
| 24 Hz | 132.6 Mohm | 162.9 kV | 0.868 mA | 814 kV/m |
| 50 Hz | 63.7 Mohm | 112.8 kV | 1.25 mA | 564 kV/m |
| 1 kHz | 3.18 Mohm | 25.2 kV | 5.60 mA | 126 kV/m |
| 10 kHz | 318 kohm | 7.98 kV | 17.7 mA | 39.9 kV/m |
| 100 kHz | 31.8 kohm | 2.52 kV | 56.0 mA | 12.6 kV/m |
| 1 MHz | 3.18 kohm | 798 V | 177 mA | **3.99 kV/m** |
| 10 MHz | 318 ohm | 252 V | 560 mA | **1.26 kV/m** |
| 100 MHz | 31.8 ohm | 79.8 V | 1.77 A | **399 V/m** |

The earlier reactive-current estimate for `P ~ omega*C*V^2` underestimates the source voltage needed for this real-power transfer by `sqrt(2)` in the optimum simple series-link case.

---

## 3. A 100-V/m field is nowhere near 100 W in this model

For a uniform RMS field `E` across span `d`, take the optimistic source voltage

`Vs = E*d`.

At `E = 100 V/m`, `d = 0.20 m`, `C = 50 pF`:

- 1 MHz -> **0.0628 W** maximum ideal real load power;
- 10 MHz -> **0.628 W**;
- 100 MHz -> **6.28 W**.

Thus even a very conspicuous `100 V/m` HF electric field is still below the 100-W target for this 50-pF / 20-cm link.

Required ideal field levels are approximately:

- 1 MHz -> `4.0 kV/m`;
- 10 MHz -> `1.26 kV/m`;
- 100 MHz -> `399 V/m`.

These are **receiver-port bounds**, not statements that such fields existed near Methernitha.

---

## 4. Far-field energy flux gives an independent floor

If the source is a propagating far-field wave, no receiving model can extract more real power than crosses its effective capture area.

For RMS electric field in free space,

`S = E_rms^2 / Z0`,

with `Z0 ~= 376.73 ohm`.

Grant an optimistic effective capture area of `0.1 m²`.

To receive 100 W:

- at 100% capture efficiency: `S >= 1000 W/m²`, `E_rms >= 614 V/m`;
- at 50%: `E_rms >= 868 V/m`;
- at 10%: `E_rms >= 1.94 kV/m`;
- at 1%: `E_rms >= 6.14 kV/m`.

So at 100 MHz the simple capacitive-port value `~399 V/m` is actually too optimistic for a far-field source: the **energy-flux floor of ~614 V/m** already dominates even with perfect capture.

At lower frequencies the 20-cm receiver is also electrically small; V4.15 shows that electrically-small efficiency/bandwidth constraints make the idealized capture assumptions increasingly difficult.

A near-field transmitter can evade the far-field aperture geometry, but not conservation of real power: its source must still supply at least the extracted 100 W plus losses and should experience corresponding loading.

---

## 5. What a hidden powered HF source would have to look like

A viable conventional HF-source explanation is no longer “some radio energy in the room.” It requires all of the following simultaneously:

- a powered source with `>=100 W` real available power at the relevant frequency;
- sufficiently strong electric/magnetic near field at the machine;
- a return geometry consistent with V4.18/V4.19;
- coupling phase that produces a substantial in-phase current component after the machine's nonlinear conversion;
- source loading/reaction when the machine draws power;
- compatibility with the observed rear-plate and humidity sensitivity.

For the 50-pF benchmark, the field would be kV/m-class around 1–10 MHz, or hundreds V/m at 100 MHz. Such a source is not an innocuous ambient background.

This does not make a concealed transmitter impossible in principle. It makes the hypothesis **strongly testable**.

---

## 6. Best discriminator: reaction at the source

The decisive experiment for any external-field explanation is not merely finding a spectral line.

If the machine extracts real power, the transmitter/environment source must show reaction:

`Delta P_source >= P_machine_real + losses`.

For a controlled low-voltage experiment:

1. drive a calibrated external field source;
2. measure source forward real power and source impedance;
3. place the passive machine/replica in the field;
4. compare source loading with machine open, tuned, rotating, plate-present and plate-absent states;
5. measure machine-side real power independently.

A real receiver must increase source real-power demand or reduce reflected/source-terminal power by the corresponding amount. Internal high voltage alone is not evidence of energy transfer.

For historical investigation, the analogous question is whether any room/building transmitter, cable, electrode structure or powered oscillator capable of >100 W existed and whether demonstrations depended on location.

---

## 7. Implication for the Earth–ionosphere–magnetosphere hypothesis

This result is especially restrictive for the original environmental-dynamo idea.

The Earth–ionosphere system certainly has large potentials and the magnetosphere carries enormous total energy flows. But to account for a tabletop 100-W load, the machine needs a **local port that behaves as a strong real-power source**, not just a high open-circuit voltage or a weak ambient field.

The chain would have to be something like

`remote geophysical reservoir -> low-impedance dynamic field/current channel -> local front/rear ports -> machine`.

V4.14–V4.20 have not identified that middle channel:

- fair-weather conduction is too weak;
- ELF/ULF resonant capture is too slow/inefficient for the size;
- corona is charge-limited and self-biasing;
- local geomagnetic/corotation EMF is tiny;
- rear/body capacitance is a plausible return/shunt, not a reservoir;
- ordinary 50-Hz infrastructure pickup is far too weak.

V4.21 adds that a replacement dynamic HF channel would have to create **hundreds to thousands of V/m**, or equivalent near-field coupling, at substantial real source power. Nothing in the present M2 evidence establishes such a geophysical channel.

---

## 8. Current conclusion

The search has now separated three things that are easy to conflate:

1. **high voltage** — easy in electrostatic/resonant systems;
2. **milliamp displacement current** — plausible through tens of pF if frequency/voltage are high enough;
3. **100 W real power** — requires a stiff external source and measurable source reaction.

The third item remains unexplained.

The strongest surviving conventional electrical hypothesis is therefore not vague “energy from the environment,” but the much narrower:

> **an unidentified powered dynamic field/near-field source with >=100 W real available power and a measurable front/rear coupling path.**

If no such source can be found or reproduced, attention should shift away from field-voltage arguments and toward the remaining alternatives: stored energy, mechanical input, measurement/history error, or genuinely new physics requiring direct calorimetric/electrical proof rather than inference from machine behavior.
