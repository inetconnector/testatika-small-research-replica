# M2 V4.19 — rear metal plate, human/body return and the remaining front-port bottleneck

## Status

**DERIVED diagnostic / HYPOTHESIS discriminator.**

Historical anchor, M2: Marinov directly reports that bringing a large metal plate behind the running small machine stopped rotation and removed the electrostatic rest torque. The plate material state, grounding state, exact distance and whether it was held by a person are not fixed by the surviving record.

V4.19 therefore does **not** claim that the plate was grounded, human-held or part of the historical energy source. It asks a narrower question:

> Could an apparently innocuous rear metal plate change the electro-quasistatic return path by enough to stop a very high-impedance machine, even if the plate supplies no energy?

Canonical calculator: `sim/m2_v4_19_rear_plate_human_return.py`.

---

## 1. Why this matters after V4.18

V4.18 found that the capacitance required to carry milliamp-scale **displacement current** at a 100–250-kV internal scale is not absurd. At 24 Hz and 250 kV,

`Ceq(1 mA) = I/(2*pi*f*V) ~= 26.5 pF`.

The missing issue remained the complete two-terminal path and, separately, the real-power source.

V4.19 adds a neglected experimental confound: a metal plate held by a person is not electrically equivalent to the same plate floating on dry dielectric supports. The human body itself has substantial electro-quasistatic capacitance to Earth and surrounding grounded structures.

Primary comparison literature:

- Shovan Maity et al., *Bio-Physical Modeling, Characterization, and Optimization of Electro-Quasistatic Human Body Communication*, IEEE TBME 66(6), 2019, DOI `10.1109/TBME.2018.2879462`. The experimentally validated EQS-HBC model uses body/environment return capacitance; later work from the same line cites a typical body-to-Earth value of about `150 pF`.
- Samyadip Sarkar et al., *Effect of Nearby Metals on Electro-Quasistatic Human Body Communication*, IEEE TBME 73(5), 2026, DOI `10.1109/TBME.2025.3616233`. FEM plus experiments show that nearby floating/grounded conductors substantially change an EQS return path; conductors within roughly 20 cm can alter channel loss by about 10 dB, and grounded-metal connection can change gain by 20 dB or more.
- Ivica Smolić and Bruno Klajn, *Capacitance matrix revisited*, 2020, arXiv `2007.10251`, gives the rigorous multi-conductor capacitance-matrix framework behind these lumped reductions.

These papers are conventional coupling precedents, not Testatika validation.

---

## 2. Geometry anchor

The V5 fabrication layer preserves the M2 working envelope:

- rear structural plate: `336 x 246 mm`, nominally nonconductive in the build kit;
- rotor: `200 mm` diameter;
- base: `370 x 180 mm`.

The historical glossy black rear board's exact electrical material state remains unresolved. V4.19 does not promote it to a conductor.

For Marinov's **external perturbation plate**, use a deliberately simple comparison geometry:

- `300 x 300 mm`, area `0.09 m²`;
- air gap `d` behind the machine.

Ideal local plate scale:

`C_machine-plate ~= eps0*A/d`.

This is a near-field geometry scale, not a precision BEM extraction.

---

## 3. Human-held plate becomes a real return network

If the plate is held by a person, the minimum reduced path is

`MACHINE -> C_machine-plate -> PLATE/BODY -> C_body-Earth -> EARTH`.

The effective rear return is therefore

`C_rear = C_machine-plate*C_body-Earth / (C_machine-plate + C_body-Earth)`.

Using `C_body-Earth = 150 pF` as a literature-scale comparison:

| plate gap | `C_machine-plate` | human-held `C_rear` | `I` @ 100 kV, 24 Hz | `I` @ 250 kV, 24 Hz |
|---:|---:|---:|---:|---:|
| 20 cm | 3.98 pF | 3.88 pF | 0.059 mA | 0.146 mA |
| 10 cm | 7.97 pF | 7.57 pF | 0.114 mA | 0.285 mA |
| 5 cm | 15.94 pF | 14.41 pF | 0.217 mA | 0.543 mA |
| 2 cm | 39.84 pF | 31.48 pF | 0.475 mA | **1.187 mA** |
| 1 cm | 79.69 pF | 52.04 pF | 0.785 mA | **1.962 mA** |
| 5 mm | 159.38 pF | 77.27 pF | **1.165 mA** | **2.913 mA** |

### Derived consequence

At an assumed `250-kV`, `24-Hz` internal differential scale, a 30-cm metal plate brought within only a few centimetres and capacitively returned through a human body can land directly in the **milliamp reactive-current range**.

That is large enough to be a serious perturbation of a high-impedance electrostatic oscillator/motor.

It does **not** show that the environment supplies 100 W.

---

## 4. This weakens the rear-plate observation as source proof

The plate stop observation remains historically important, but V4.19 gives a strong conventional explanation that does not require the plate to block an exotic energy inflow.

A close plate can instead act as:

- a capacitive shunt;
- a common-mode return;
- a charge sink/source for displacement current;
- a capacitance-matrix shield;
- a resonance/Q perturbation;
- a nonlinear damping path if crystal/corona/leakage elements rectify part of the current.

For the 2-cm / 150-pF-body example, the effective rear node is `~31.5 pF`.

Its stored-energy swing is

`0.5*C*V^2`.

At 250 kV this is about `0.984 J`. If a nonlinear gate forced a full charge/discharge event 24 times per second, the switched-energy scale would be about `23.6 W`.

This is **not** the sinusoidal real power of an ideal capacitor; ideal reactive energy is returned. It only shows why a rectified/lossy rear perturbation can heavily damp a delicate machine.

---

## 5. But the front side now becomes the bottleneck

A complete floating environmental link still needs

`ENV_FRONT -> C_front -> MACHINE -> C_rear -> ENV_REAR/EARTH`.

Thus

`Ceq = C_front*C_rear/(C_front + C_rear)`.

At `250 kV`, `24 Hz`, 1 mA requires `Ceq ~= 26.53 pF`.

For the 2-cm plate:

- if the plate were directly Earth-referenced, `C_rear ~= 39.84 pF`, requiring `C_front ~= 79.4 pF`;
- if human-held with `150 pF` body-to-Earth capacitance, `C_rear ~= 31.48 pF`, requiring **`C_front ~= 168.5 pF`**.

So the rear plate alone does not solve the milliamp path. The front/environment coupling must also be large.

Examples at 250 kV / 24 Hz with the human-held 2-cm rear plate:

| assumed `C_front` | full series `Ceq` | reactive current |
|---:|---:|---:|
| 5 pF | 4.31 pF | 0.163 mA |
| 10 pF | 7.59 pF | 0.286 mA |
| 20 pF | 12.23 pF | 0.461 mA |
| 50 pF | 19.32 pF | 0.728 mA |
| 100 pF | 23.94 pF | 0.903 mA |
| 200 pF | 27.20 pF | 1.025 mA |

This is the sharper V4.19 target:

> **Find or measure an effective front-side coupling of order 0.1–0.2 nF if the human-held rear-plate route is supposed to support 1 mA at 250 kV and 24 Hz.**

A direct `sky` capacitance of that size is not established by the historical geometry. Nearby walls, people, instrumentation, conductive furniture or building structures could raise the effective EQS capacitance, but then they are experimental boundary conditions that must be measured explicitly.

---

## 6. Current is still not the missing 100 W

At 250 kV and 1 mA,

`|S| = 250 VA`.

For 100 W real power,

`cos(phi) = 100/250 = 0.4`.

The plate/body calculation above establishes only a plausible **reactive current path**. The ordinary fair-weather Earth-ionosphere source still has the V4.14 source-impedance problem; lossless matching, a human body, a metal plate or a magnetized grid cannot turn nanowatt available power into 100 W.

Therefore the remaining bulk-source hypothesis still requires a real differential source with sufficient conductance/available power between the two environmental terminals.

---

## 7. Highest-value historical reproduction of Marinov's perturbation

The historical observation should be repeated only in a safe, current-limited low-voltage scaled setup.

For each plate distance, compare **one variable at a time**:

1. plate suspended fully floating on dry dielectric supports;
2. same plate connected only to a calibrated `150-pF` body-simulator capacitor to Earth;
3. same plate connected to several known return capacitors, e.g. 10/30/50/100/150/300 pF;
4. same plate Earth-referenced in the low-voltage rig;
5. insulating dummy of the same dimensions;
6. conductive plate present while internal resonance is retuned back to its pre-plate frequency/Q.

Measure simultaneously:

- plate potential;
- plate-to-Earth displacement current;
- front and rear complex admittance;
- internal differential voltage;
- resonance frequency and ring-down Q;
- rotor torque/speed if used;
- storage energy;
- RH/temperature;
- instrument-ground topology.

### Discriminator

If the plate-stop analogue scales mainly with its calibrated return capacitance to Earth/body, that is evidence for an ordinary EQS return/shunt mechanism.

If a strong effect remains when the plate is demonstrably floating, after resonance is retuned and after the capacitance-matrix change is characterized, the unexplained residual becomes substantially more interesting.

---

## 8. Current conclusion

V4.19 changes the interpretation of the strongest rear-plate clue:

`rear plate stops machine`

is **not equivalent to**

`rear plate blocks the machine's energy source`.

A nearby metal plate can conventionally alter the return path by enough to carry sub-mA/mA displacement current at the hypothesized internal HV scale. A human-held plate can be much less floating than it appears.

The source question is therefore narrowed again:

> **Can the untouched running machine show a front/rear environmental port with both (a) sufficient effective capacitance and (b) a measured in-phase real-power component large enough to account for the load?**

Until (b) is measured, the Earth–ionosphere–magnetosphere dynamo remains an unverified bulk-source hypothesis and the ordinary fair-weather implementation remains quantitatively far too high in source impedance.
