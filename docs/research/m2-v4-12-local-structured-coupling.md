# M2 V4.12 — local structured coupling / hidden-port bounds

## Status

**DERIVED diagnostic / conventional-source discriminator.** V4.12 does **not** add RF, resonant-power hardware, hidden transmitters or an active base to the historical M2 baseline.

V4.11 excluded ordinary fair-weather atmospheric conduction, ordinary ambient RF, Schumann/ELF background and Earth's static field as direct ~100-W tabletop reservoirs. V4.12 therefore asks a narrower question:

> If a historical demonstration really produced ~100 W, could a **local structured source** have supplied that power through base/table/chassis capacitance, a strong nearby magnetic field, or another hidden real-power path?

Canonical calculator: `sim/m2_v4_12_local_structured_coupling.py`.

---

## 1. Why this is now the highest-value conventional branch

Historical observations do not prove a hidden source, but they constrain simple versions of one:

- M5 witness material includes a report that the machine was lifted and the underside inspected, with no obvious external source seen.
- Holzherr reports that some small ~12-cm models could be lifted while running, which disfavors a fixed galvanic table feed for those particular models.
- Hauser later reports that a machine was physically relocated to test a fixed hidden-transmitter/focus explanation.
- Separately, a large-machine source relay describes a thick base as alternating perforated conductive and insulating layers; this is H2 and must not be transferred to M2 as fact.

These observations do not exclude a source built into the machine, a source moving with it, broad-area near-field coupling, common-mode coupling through instrumentation, finite storage, or a short demonstration powered from hidden chemical/electrical storage.

See `hidden-input-witness-constraints-2026-08-18.md`.

---

## 2. Capacitive local-source bound

For an RMS sinusoidal source coupled through an effective capacitance `C`, the displacement current scale is

`I = 2*pi*f*C*V`.

The corresponding source-side apparent-power scale is

`S = V*I = 2*pi*f*C*V^2`.

V4.12 uses this only as an **optimistic upper bound**. A real capacitive wireless-power path still needs:

- a real source supplying load power plus losses;
- a complete return path / second electrode / common-mode closure;
- matching or resonant compensation if the capacitive reactance is large;
- phase-correct rectification/load coupling.

Therefore a result such as `S = 100 VA` does not mean a passive capacitor generates 100 W. It means a local source could in principle push that scale of power through the coupling if the rest of the network is properly driven and matched.

---

## 3. Geometry example: 30 cm x 30 cm base plate

Take a purely comparative laboratory geometry:

- area `A = 0.09 m²`;
- dielectric gap `d = 5 mm`;
- relative permittivity `eps_r = 3`.

Parallel-plate estimate:

`C ~= eps0*eps_r*A/d ~= 478 pF`.

For a 100-W optimistic bound:

| Frequency | Required RMS voltage across 478 pF | Capacitive RMS current | Energy per source cycle |
|---:|---:|---:|---:|
| 50 Hz | ~25.8 kV | ~3.88 mA | 2 J |
| 1 kHz | ~5.77 kV | ~17.3 mA | 0.1 J |
| 10 kHz | ~1.82 kV | ~54.8 mA | 10 mJ |
| 100 kHz | **~577 V** | **~173 mA** | **1 mJ** |
| 1 MHz | ~182 V | ~548 mA | 0.1 mJ |

This is the first important V4.12 result:

> A local high-frequency capacitive source does **not** need enormous coupling capacitance. Hundreds of picofarads can carry a 100-VA scale at hundreds of volts once frequency reaches the 100-kHz range.

But the source current is no longer subtle: the 100-kHz example requires about **173 mA RMS displacement current** through the coupling. That must originate from a real transmitter/source and should be observable in a closed energy audit.

---

## 4. Thin or multilayer dielectric can raise coupling sharply

The same 30 cm x 30 cm area with `d = 0.5 mm`, `eps_r = 3` gives approximately

`C ~= 4.78 nF`.

At 100 kHz, the ideal 100-VA voltage becomes only about

`V ~= 182 V RMS`,

with about

`I ~= 0.548 A RMS`.

If multiple dielectric gaps were deliberately connected in parallel, effective capacitance could grow further. **This is a laboratory parameter only.** The historical relay about layered base construction does not recover its wiring, capacitance, frequency, or source.

This result makes a layered base worth measuring electrically, but it does not establish that it was an energy receiver.

---

## 5. Inverse question: how little capacitance would a strong local source need?

For 100 W at the same optimistic bound:

`C_required = P / (2*pi*f*V^2)`.

Selected examples:

| Local source | Required effective C for 100-VA scale |
|---|---:|
| 1 kV, 50 Hz | ~318 nF |
| 10 kV, 50 Hz | ~3.18 nF |
| **100 kV, 50 Hz** | **~31.8 pF** |
| 1 kV, 100 kHz | ~159 pF |
| **10 kV, 100 kHz** | **~1.59 pF** |
| 1 kV, 1 MHz | ~15.9 pF |

This creates a strong falsification criterion:

> If a hidden local source operates at high voltage and/or high frequency, even tiny parasitic capacitances can transmit a 100-VA scale. Therefore simply seeing “no wire” is not enough; the surrounding E-field, displacement currents and source-side real power must be measured.

The reverse is equally important: a 10-kV/100-kHz local source capable of supplying 100 W is not ordinary ambient background. It is an active transmitter and should produce measurable near fields and source currents.

---

## 6. Mechanical 60-rpm timing is compatible with a much faster carrier — but does not prove one

At 60 rpm the rotor makes one revolution per second. If a geometry gives ~50 electrical gating events per revolution, the mechanical event rate is ~50 Hz.

A hypothetical 100-kHz local carrier would contain roughly

`100000 / 50 = 2000 carrier cycles per mechanical event`.

At 100 W average:

- energy per 100-kHz carrier cycle = `1 mJ`;
- energy per 50-Hz mechanical event = `2 J`.

Thus a slow rotor could in principle **gate or phase-control** a much faster externally supplied carrier. That is a conventional architecture seen in many power-electronic systems.

However, direct Marinov small-machine correspondence argues against treating an HF/Tesla stage as established M2 history. V4.12 therefore keeps this only as a falsification/control branch.

---

## 7. Magnetic local-source bound

For a sinusoidal magnetic field and an optimally oriented pickup loop:

`V_rms = 2*pi*f*N*A*B_rms`.

Using a 200-mm-diameter loop area (`A ~= 0.0314 m²`):

### To induce 100 V RMS

| Frequency | 1 turn | 24 ideal turns |
|---:|---:|---:|
| 100 kHz | ~5.07 mT | **~0.211 mT** |
| 1 MHz | ~0.507 mT | **~21.1 µT** |

These field amplitudes are not an energy-source proof. To deliver 100 W at 100 V, the receiving circuit must also supply about 1 A load current, and the transmitting field source must provide at least the corresponding real power plus losses.

For a primary current of 1 A RMS, 100 V induced at 100 kHz requires an optimistic mutual inductance

`M ~= V/(2*pi*f*I) ~= 159 uH`.

A strong local magnetic transmitter can therefore transfer substantial power by ordinary physics — resonant magnetic wireless power transfer has been experimentally demonstrated in the scientific literature — but the transmitter is then the energy source.

Scientific control example:

- A. Kurs et al., *Wireless Power Transfer via Strongly Coupled Magnetic Resonances*, Science 317 (2007), DOI 10.1126/science.1143254. The paper reports tens-of-watts non-radiative transfer using deliberately driven resonant coils. This is a conventional comparison, not Testatika evidence.

---

## 8. What the rear metal plate would do in the local-source model

A conductive plate behind the machine can affect at least two independent layers:

1. **coupling:** change `C_front`, `C_rear`, common-mode return and source differential;
2. **tuning:** change the effective resonant capacitance and phase of any conditioning network.

Therefore the Marinov rear-plate stop does not distinguish by itself between:

- loss of external coupled input power;
- detuning of an internal high-Q network;
- collapse of electrostatic charge state / leakage boundary;
- some combination of those effects.

A decisive experiment must re-tune the internal network after each plate position. If output recovers after re-tuning while measured source-side power remains constant, detuning is favoured. If source-side displacement current/real power collapses with the plate even after re-tuning, an external differential coupling port is favoured.

---

## 9. Strongest modern falsification test

A convincing hidden-port test should separate **room-following**, **table-following**, **machine-following** and **stored-energy** explanations.

Low-energy diagnostic protocol:

- battery-powered isolated data acquisition with optical/fiber logging;
- no galvanic oscilloscope/USB/earth connection to the device;
- measure base/table/chassis capacitance and leakage before operation;
- wideband E-field and H/B-field probes around the complete device volume;
- conductive enclosure A/B test plus nonconductive geometric dummy;
- separate low-frequency magnetic shielding/field logging because a Faraday cage does not remove every magnetic near field;
- relocate and rotate the entire apparatus while keeping load/instrumentation unchanged;
- continuously account for mechanical work and all storage-energy change.

The decisive condition remains:

`P_load <= P_external_real + P_mechanical + (-dE_storage/dt)`

for ordinary physics.

If a sustained residual remains only after all terms are bounded with uncertainty, the source question becomes genuinely anomalous rather than merely uninstrumented.

---

## 10. V4.12 conclusion

V4.12 changes the source search in an important way.

**Ordinary ambient environment:** too weak.

**Local structured coupling:** physically capable of 100-W transfer, depending on voltage, frequency, capacitance/mutual inductance and matching.

That means the most serious conventional remaining hypothesis is now:

`local source / transmitter / active base or common-mode port`

→ `capacitive or inductive coupling`

→ `electrostatic influence / pickup`

→ `tuned conditioning / nonlinear commutation`

→ `storage / load`.

This does **not** explain where the local source itself gets its energy. It identifies exactly what must be measured to rule the hidden-port hypothesis in or out.

For the 30-cm, 5-mm, eps_r=3 comparison base, a 100-kHz 100-W path would require roughly **577 V RMS and 173 mA RMS through ~478 pF**. Those are now concrete falsification targets rather than a vague “energy from the environment” idea.
