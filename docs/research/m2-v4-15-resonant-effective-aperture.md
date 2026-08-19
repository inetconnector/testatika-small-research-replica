# M2 V4.15 — resonant effective-aperture loophole versus small-antenna Q

## Status

**DERIVED diagnostic / HYPOTHESIS discriminator.** This is not a historical M2 circuit claim and does not import RF/ELF resonance into the Marinov small-machine baseline.

V4.14 found that ordinary Earth–ionosphere fair-weather coupling is an enormous-source-impedance problem. A sophisticated objection remains:

> A resonant receiving antenna can have an **effective aperture** much larger than its physical area. Could an extremely high-Q, magnetically/electrically structured 20-cm machine therefore couple to a huge effective area of the Earth–ionosphere–magnetosphere field and evade the V4.14 physical-area bound?

This is a real electromagnetic loophole and should not be dismissed by geometry alone.

V4.15 therefore combines:

1. the ideal reciprocal receiving-aperture relation;
2. Chu/McLean electrically-small-antenna Q limits;
3. ring-up / bandwidth consequences;
4. radiation-resistance and finite-loss constraints.

Canonical calculator: `sim/m2_v4_15_resonant_effective_aperture.py`.

---

## 1. Why effective aperture matters

For a matched receiving antenna in a free-space plane wave,

`A_e = G * lambda^2 / (4*pi)`.

This follows from the classical reciprocal antenna/Friis framework.

Primary reference:

- H. T. Friis (1946), *A Note on a Simple Transmission Formula*, DOI `10.1109/JRPROC.1946.234568`.

For a dipole-like gain `G ~= 1.5`,

`A_e ~= 0.119 * lambda^2`.

At ELF/ULF wavelengths, this number becomes enormous. Therefore the statement

`a 0.1-m² object can only intercept 0.1 m² of wave power`

is **not a universal antenna theorem**.

That correction is important.

But `A_e` is a steady-state matched receiving result. For an electrically tiny resonator, the same electromagnetic theory that permits huge wavelength-scaled aperture also imposes extreme stored-energy/Q requirements.

---

## 2. The missing companion equation: electrically-small antenna Q

For an antenna contained in radius `a`, define

`ka = 2*pi*a/lambda`.

For `ka << 1`, the familiar single-mode Chu/McLean radiation-Q scale is

`Q_min ~= 1/(ka)^3 + 1/(ka)`.

The cubic term dominates strongly when the receiver is electrically tiny.

Primary foundations:

- L. J. Chu (1948), *Physical Limitations of Omni-Directional Antennas*, DOI `10.1063/1.1715038`;
- J. S. McLean (1996), *A Re-Examination of the Fundamental Limits on the Radiation Q of Electrically Small Antennas*, DOI `10.1109/8.496253`.

Later fundamental-bound work for arbitrary shapes and finite-conductivity antennas reinforces the same qualitative conclusion: shrinking electrical size imposes severe Q/bandwidth/efficiency cost; realistic tuning loss makes the situation worse, not better.

Useful primary analyses:

- O. S. Kim (2015), *Lower Bounds on Q for Finite Size Antennas of Arbitrary Shape*, arXiv `1506.03738`;
- C. Pfeiffer (2017), *Fundamental Efficiency Limits for Small Metallic Antennas*, arXiv `1612.07317`;
- L. Jelinek, K. Schab & M. Capek (2018), *The Radiation Efficiency Cost of Resonance Tuning*, arXiv `1712.02613`.

---

## 3. What happens at magnetospheric Pc5 frequency

Use the intense Pc5 example preserved in Pilipenko et al. 2014:

- magnetic pulsation amplitude about `400 nT` peak-to-peak scale;
- characteristic frequency about `2.5 mHz`.

Primary source:

- V. Pilipenko et al. (2014), *Modulation of total electron content by ULF Pc5 waves*, DOI `10.1002/2013JA019594`.

For a 20-cm-diameter device, use bounding radius

`a = 0.10 m`.

At `f = 2.5 mHz`,

`lambda ~= 1.20e11 m`.

Therefore

`ka ~= 5.24e-12`.

The ideal small-antenna lower-bound scale becomes

`Q_min ~= 6.95e33`.

An amplitude time constant of a lightly damped resonator is approximately

`tau ~= Q/(pi*f)`.

That gives

`tau ~= 2.8e28 years`.

The corresponding half-power bandwidth scale

`Delta f ~= f/Q`

is about

`3.6e-37 Hz`.

So a 20-cm passive resonant antenna cannot establish the formal steady-state wavelength-sized receiving aperture on any physically relevant Pc5 timescale.

This closes an important loophole in the simple source-area argument.

---

## 4. The same problem at Schumann frequency

Use the first Schumann resonance frequency as a convenient ELF comparison:

`f ~= 7.83 Hz`.

For `a = 0.10 m`,

`ka ~= 1.64e-8`,

`Q_min ~= 2.26e23`.

The corresponding amplitude time constant is about

`2.9e14 years`,

and the bandwidth is only about

`3.46e-23 Hz`.

This is far beyond any realistic lightning-driven field coherence or environmental stationarity interval.

### The deliberately paradoxical aperture result

At `7.83 Hz`, the ideal dipole receiving aperture would be

`A_e ~= 1.75e14 m²`.

If one incorrectly combines that steady-state aperture with a free-space plane-wave electric field of `0.2 mV/m`, the calculation can even produce an apparent available-power result of order

`~1.9e4 W`.

That number is **not evidence that a 20-cm Schumann receiver can collect kilowatts**. It exposes exactly why effective aperture cannot be used without its matching/Q/transient assumptions.

The receiver would need an absurdly narrow resonance and effectively geological-to-cosmological ring-up before that ideal steady state existed. In the real Earth–ionosphere cavity, source back-reaction, cavity losses, finite source coherence, finite antenna efficiency and material losses tighten the bound further.

---

## 5. Response-time form of the same bound

For a resonator to respond with amplitude time constant no longer than `T`,

`Q <= pi*f*T`.

At `7.83 Hz` and only `60 s` response time,

`Q_response <= ~1.48e3`.

Compare with the ideal electrically-small requirement

`Q_min ~= 2.26e23`.

The gap is about

`1.5e20`.

This is a useful way to phrase the problem experimentally:

> A device that starts after a few pushes and settles on human-observable timescales cannot simultaneously behave like the ultra-high-Q 20-cm ELF antenna required to realize the gigantic formal wavelength-scaled effective aperture.

That conclusion does not depend on whether the hidden structure is called a coil, crystal, magnetic grid, resonator or impedance transformer.

---

## 6. Radiation resistance is another way to see the problem

For a short uniform-current electric dipole,

`R_rad ~= 80*pi^2*(l/lambda)^2`.

Take `l = 0.20 m` at `7.83 Hz`:

`R_rad ~= 2.15e-14 ohm`.

To retain even `50%` radiation efficiency, total tuning/conductor/dielectric loss resistance would have to remain of the same order or smaller:

`R_loss <= ~2e-14 ohm`.

That is not a credible ordinary room-temperature copper/steel/magnet/PMMA structure.

For electrically small metallic antennas, rigorous finite-conductivity analyses find efficiency collapses strongly once electrical size becomes sufficiently small; resonance tuning itself adds further dissipation cost.

Therefore the enormous ideal `A_e` is bought with vanishing radiation resistance and extreme sensitivity to any real loss.

---

## 7. Does magnetic structure evade Chu/McLean?

Not by itself.

Magnetic materials, coupled electric/magnetic dipoles, helices, ferrites and metamaterial-like structures can change:

- current distribution;
- self-resonance;
- impedance match;
- internal wavelength;
- coupling to E versus B;
- directivity and polarization;
- practical Q and size tradeoffs.

They do not create incoming real power.

Fundamental small-antenna bounds have been generalized beyond one simple wire geometry, including mixed electric/magnetic currents and arbitrary shapes. The exact coefficient can move; the catastrophic `ka << 1` scale does not turn into a practical 20-cm mHz/Hz receiver with 100-W bandwidth and minute-scale startup.

A magnetic structure is therefore still a plausible **coupling/timing/impedance-conditioning component**, but it does not automatically provide the giant effective environmental aperture that V4.14 requires.

---

## 8. Frequency transition: where resonance becomes less absurd

For the same `a = 0.10 m` ideal bound:

| Frequency | `Q_min` scale | amplitude `tau` scale |
|---:|---:|---:|
| 2.5 mHz | `6.95e33` | `2.8e28 years` |
| 7.83 Hz | `2.26e23` | `2.9e14 years` |
| 24 Hz | `7.86e21` | `3.3e12 years` |
| 50 Hz | `8.69e20` | `1.75e11 years` |
| 1 kHz | `1.09e17` | `1.1e6 years` |
| 10 kHz | `1.09e14` | `~110 years` |
| 100 kHz | `1.09e11` | `~4 days` |
| 1 MHz | `1.09e8` | `~35 s` |

This table gives a major clue.

A compact 20-cm structure becomes capable of human-timescale high-Q electromagnetic ring-up only when the relevant carrier moves into roughly the **hundreds-of-kHz to MHz regime**, not at magnetospheric mHz/ELF frequencies.

That is compatible with a possible architecture of

`slow rotor / environmental bias -> triggered high-frequency internal burst -> rectification/storage`,

but it creates a new requirement:

> the **real power source must itself have spectral/near-field power in that higher-frequency band**, or some other pump must perform the frequency conversion.

Magnetospheric mHz energy cannot be passively frequency-upconverted into 100 W by resonance alone.

And because direct Marinov evidence rejects Tesla/AC as the M2 small-pot interpretation, such an HF stage remains a **comparison hypothesis**, not historical M2 baseline fact.

---

## 9. The correct interpretation of a huge effective aperture

The useful conclusion is not “effective aperture is impossible.” It is:

1. **Yes**, antenna effective aperture can exceed physical area.
2. **Yes**, at enormous wavelength the formal ideal aperture can be gigantic.
3. **But** the same electrically-small limit forces gigantic Q, negligible bandwidth, tiny radiation resistance and extreme ring-up time.
4. Any practical loss destroys the ideal coupling efficiency long before the formal aperture is realized.
5. For a finite global cavity/magnetospheric mode, a strongly coupled receiver would also load the source; the field cannot remain an unaffected prescribed background while arbitrary power is removed.

So V4.14's `500–833 km² equivalent area` must not be read as requiring a literal metal collector of that size. It can also be read as an **effective-aperture target**.

V4.15 then says that known passive small-antenna physics cannot produce that effective aperture at mHz/Hz with useful 100-W-scale bandwidth and startup time.

---

## 10. A better search target for the Testatika

This shifts the research away from “is there resonance?” to four measurable quantities:

`frequency`

`Q / decay time`

`effective source impedance`

`real power transfer`

A credible environmental-resonance mechanism must simultaneously show:

- an identifiable environmental carrier or port;
- a receiver resonance at that carrier;
- a measured ring-up/decay time consistent with its claimed Q;
- load power that does not exceed real incoming source power plus storage/mechanical terms;
- source impedance low enough to sustain the loaded state.

A high unloaded voltage by itself is not enough.

---

## 11. Highest-value new experiment

Use the low-energy replica as a calibrated receiving structure.

For each external drive frequency:

1. measure incident `E` and `B` with an independent probe;
2. measure replica open-circuit response;
3. measure resonance frequency and ring-down/Q;
4. apply several known loads and extract the Thevenin/Norton source;
5. calculate effective aperture from **real absorbed power**, not from voltage gain;
6. compare measured `A_e(f)` with the passive small-antenna bound and with the V4.14 aperture/source-impedance requirement.

The decisive measured quantity is

`A_e,measured = P_absorbed_real / S_incident_real`

where a plane-wave interpretation is valid. In quasi-static electric/magnetic drive, use the calibrated external-source real power and transfer coefficient instead of forcing a far-field `S` model.

Repeat with:

- magnets removed / dummy magnets;
- magnetic pickups demagnetized / magnetized;
- conductive rear plate floating / grounded / absent;
- RH controlled;
- rotor stopped / rotating at controlled rpm;
- crystal black-box open / linear surrogate / nonlinear surrogate.

This directly tests whether the visually unusual Testatika structures create an anomalously strong coupling coefficient without presupposing the energy source.

---

## 12. Falsification and escalation criterion

The passive Earth–ionosphere–magnetosphere resonant-aperture hypothesis is strongly disfavoured if:

- measured coupling follows ordinary passive antenna/capacitive/inductive scaling;
- measured Q is many orders below what the formal ELF aperture requires;
- load-step source impedance remains far above the `~1e8-ohm` target;
- apparent shielding effects vanish after retuning;
- no real incoming environmental power accompanies sustained load power.

It deserves escalation only if the replica shows a **repeatable real-power absorption cross-section or effective source impedance grossly exceeding passive calibrated controls**, with mechanical/storage/base/instrument ports closed in the energy ledger.

---

## 13. Working conclusion

V4.15 closes a subtle but important loophole in V4.14.

A resonant receiver is **not limited to its geometric area**, so the earlier physical-area comparison alone is insufficient as a fundamental proof.

However, for a 20-cm passive receiver at magnetospheric mHz or Schumann/ELF frequencies, the fundamental electrically-small Q/radiation-resistance cost is extreme. The formal huge receiving aperture is a steady-state idealization that cannot be reached on practical timescales with ordinary lossy materials.

The result therefore strengthens the source search:

> **If Testatika really accessed Earth–ionosphere–magnetosphere power, the missing element cannot be merely “very high Q” or “magnetically structured resonance.” It must provide a qualitatively different low-impedance coupling / effective-aperture mechanism, or couple to a much higher-frequency powered field.**

That is now experimentally testable.