# M2 V4.11 — environmental-port survey and quantitative source bounds

## Status

**DERIVED diagnostic / HYPOTHESIS discriminator.** This document does **not** add a resonant, RF, atmospheric-ion or magnetic-energy stage to the historical M2 baseline. The direct Marinov small-machine line still argues against Tesla coils / AC as the core interpretation of the described small machine.

V4.11 asks a narrower question:

> If historical environmental-language clues are taken seriously, which ordinary environmental electrical or electromagnetic reservoirs could even reach the claimed 100-W scale at tabletop dimensions?

The answer is tested with deliberately optimistic upper bounds. Resonance is allowed to raise internal voltage/current amplitudes, but it is never allowed to create real input power.

Canonical calculator: `sim/m2_v4_11_environmental_port_survey.py`.

---

## 1. Historical motivation, kept machine-specific

Several source lines motivate **measuring** environment coupling:

- M2: Marinov directly reports a rear metal plate stopping rotation/rest torque; dry air helps startup; Baumann gave an East-West startup instruction, while Marinov could reorient the already-running machine.
- M5a / large family: a 17-Mar-1984 witness report describes magnetic synchronization and interprets strong horseshoe magnets as parts of electrical resonance circuits involved in charging the discs.
- M6/large-family retrospective: Hauser relays Baumann's claim that atmospheric charged ions were collected/sorted and that windows/air exchange mattered. This is operator explanation, not independent measurement.
- M7/workshop: Cathomen describes magnetized non-contact pickups, a tuned/synchronized impulse path, storage in Leyden jars, and speaks of electricity as already present in nature.

These lines justify an **external-port measurement programme**. They do not establish which port supplies net power, and they must not be merged into one historical machine.

---

## 2. Critical Linden-Experiment provenance correction

The preserved second-hand Linden-Experiment letter says:

- a U-shaped magnet was wound with ordinary insulated wire;
- the two wire ends were stripped and galvanically joined into a closed loop;
- an Al/insulator/metal plate sandwich was held by Baumann between the magnet poles;
- a voltmeter reportedly indicated about 700 V;
- later attempts by the relayed witnesses did not reproduce the result.

The preserved letter **does not state an 80–140 MHz operating frequency**.

The often-repeated `80–140 MHz` statement appears in Paul E. Potter's later back-engineering and is explicitly framed there as something the Linden experiment was *thought* to register. It must therefore remain a **later secondary hypothesis**, not Baumann-source-stated frequency evidence.

This matters because the 80–140-MHz number has often been used to justify importing an HF/Tesla stage into Testatika reconstructions.

---

## 3. Independent replication control for the 700-V Linden claim

Steven Dufresne/Rimstar later performed several explicit replication attempts.

### Series 1

With the metal plates held by fingers, roughly 0.54 V appeared; moving the setup away from the magnet gave the same result. Replacing the fingers with a plastic clamp reduced the reading to zero. This is strong evidence that at least that small voltage was a body/contact/electrochemical or measurement bias, not a magnet-energy effect.

### Series 2

A driven UHF experiment swept roughly 280–425 MHz. In the direct Linden-style configuration, no additional voltage appeared beyond the finger-associated bias. Separate configurations produced ordinary induced/rectified signals, including roughly 0.25–0.42 V induced readings and a best reported configuration around 1 V at 10 microamps DC after introducing electrical contact to the driven magnet. Frequency-selective responses around 200/315/370 MHz were only about 80–120 mV DC and approximately microamp scale.

### Series 3

High-voltage pulses applied to magnet windings could be converted to low-voltage DC with conventional capacitor/rectifier behavior, but measured current remained only about 0.5–6 microamps and the low-voltage output was around 0.1 V in the described test.

**Consequence:** these replications do not reproduce the reported 700-V Linden effect or any anomalous bulk-energy source. They do show that magnet/coil/capacitor structures can exhibit ordinary frequency-selective induction, rectification and parasitic/contact effects. Any future resonance claim must therefore include source-side RF power and all galvanic/capacitive return paths in the ledger.

---

## 4. Candidate A — fair-weather global electric circuit

Representative measured values from atmospheric-electricity literature:

- near-surface fair-weather field: order `100 V/m`;
- fair-weather conduction current density: order `1–3 pA/m²`;
- ionosphere-to-ground potential: order `240–250 kV`.

For an ordinary DC atmospheric path the ideal power density cannot exceed

`P/A = J * DeltaV`.

Using `J = 2 pA/m²` and granting the completely optimistic **full 250-kV ionospheric potential** gives

`P/A = 5e-7 W/m² = 0.5 microW/m²`.

To obtain 100 W at that ideal density would require

`A = 100 / 5e-7 = 2e8 m² = 200 km²`.

That is already an unrealistically generous full-column bound. A tabletop object sampling `100 V/m` across only `0.20 m` sees about 20 V. With the same fair-weather current density:

`P/A = 2e-12 * 20 = 4e-11 W/m²`.

Ordinary fair-weather conduction therefore cannot be the 100-W tabletop bulk source.

**Status:** atmospheric electricity remains relevant as a bias/reference/charge-history influence, but conventional fair-weather ion current is quantitatively excluded as the main power reservoir.

---

## 5. Candidate B — 50-Hz mains electric-field pickup

Power-frequency fields are a serious hidden-input control because buildings contain 50-Hz wiring even when no visible wire enters the device.

Use the same intentionally generous floating two-port expression as V4.10:

`P_bound = 2*pi*f*Ceq*(E*h)^2`.

For:

- `f = 50 Hz`;
- `Ceq = 50 pF`;
- port span `h = 0.20 m`;
- `E = 100 V/m`;

we obtain only

`P_bound ~= 6.28 microW`.

Even an unusually high `10 kV/m` field gives only about `62.8 mW` with the same 50-pF coupling.

To reach 100 W at 50 Hz with `Ceq = 50 pF` and a 0.20-m span would require about

`E ~= 3.99e5 V/m rms`.

That is incompatible with an unnoticed ordinary room-field explanation.

A hidden galvanic or much larger-capacitance coupling through a base/table would be a different mechanism and must be measured separately.

---

## 6. Candidate C — ambient broadcast/cellular/Wi-Fi RF

Published ambient RF surveys commonly report broadband/band-specific average power densities from sub-microwatt/m² to tens or hundreds of microwatts/m² depending strongly on location and band. One field survey reported a highest outdoor average near `-7 dBm/m²`, about `0.2 mW/m² = 200 microW/m²`.

At `200 microW/m²`, an ideal 100% capture aperture for 100 W is

`100 / 200e-6 = 500,000 m² = 0.5 km²`.

At `100 microW/m²`, it is 1 km². At `0.316 microW/m²`, it is about 316 km².

Even taking a much stronger local public-field example of `0.1 W/m²`, ideal capture still requires about `1000 m²` for 100 W.

A resonator can increase stored reactive energy and local voltage. It **cannot** make the steady real load power exceed the real RF power entering the receiving aperture/near-field port.

**Status:** ordinary ambient broadcast RF is strongly disfavoured as a 100-W tabletop source. A deliberately nearby/hidden transmitter or direct near-field coupler remains physically possible, but then the local field/current should be easy to detect at the load-power scale.

---

## 7. Candidate D — Schumann / natural ELF resonance

Ground Schumann-resonance magnetic amplitudes are of order `~1 pT`. A published artificial-ELF experiment in the Schumann band reported roughly `1 pT` magnetic amplitude and about `0.2 mV/m` electric amplitude at a receiver 35 km away.

For an order-of-magnitude comparison only, treating those E and B values with

`S_proxy = E * B / mu0`

gives about

`1.59e-10 W/m²`.

A 100-W ideal aperture at that proxy density would be about

`6.28e11 m² ~= 628,000 km²`.

The Earth-ionosphere cavity is not a simple plane wave, so this is not a rigorous harvester theorem. It is nevertheless enough to show that ordinary Schumann fields are many orders of magnitude below a tabletop 100-W source.

**Status:** Schumann resonance may be a synchronization/noise/reference phenomenon; ordinary background SR is excluded as the bulk source.

---

## 8. Candidate E — Earth's static magnetic field

Earth's field is roughly `50 microtesla` in magnitude. A maximally oriented one-turn loop with the area of a 200-mm disc (`pi*0.1² m²`) rotating at 60 rpm would have an optimistic sinusoidal peak Faraday EMF of only

`N*B*A*omega ~= 9.87 microV` for one turn,

or about `0.237 mV` for 24 ideal series turns.

More importantly, when current is drawn from an ordinary rotating generator, electromagnetic torque opposes the motion. The electrical power comes from the mechanical shaft work. A static permanent or geomagnetic field can bias forces and timing; it is not an independent continuous bulk-energy source under ordinary electrodynamics.

**Status:** geomagnetism remains a possible startup/orientation bias variable, not a 100-W source unless another real input drives the motion/field cycle.

---

## 9. Candidate F — thunderstorms/lightning

Thunderstorm fields and lightning contain very large transient power, but they are intermittent and hazardous. Historical Hauser/Cathomen language compares the principle with natural lightning/weather electricity, while Hauser also says operation was stopped during atmospheric disturbances.

This makes lightning a **conceptual analogy / transient environmental disturbance**, not a credible steady tabletop source for normal operation.

No physical replication programme should attempt to couple to lightning.

---

## 10. What remains physically plausible after these bounds

The ordinary large-scale natural reservoirs above fail by many orders of magnitude for 100 W at tabletop size.

The remaining conventional possibilities are therefore narrower:

1. **overlooked local electrical input** — base/table/earth/chassis/wiring/instrument return path;
2. **strong local near-field transmitter** — intentional or accidental RF/inductive/capacitive coupling, not ordinary ambient RF;
3. **mechanical input** — shaft/bearing/belt/hidden motion path;
4. **finite stored energy** — charged dielectrics/electrets/capacitors/chemical storage, which must decay or be replenished;
5. **historical output estimate/demo error**;
6. an unexplained residual only after all of the above are instrumented and bounded.

The magnetized-grid / tuned-LC / nonlinear-commutation hypothesis remains useful as a **control and impedance-conversion mechanism**, especially for large/workshop machines. It is not itself an energy source.

---

## 11. Highest-value experiment now

Do not begin by trying to maximize output. First instrument the candidate input ports.

For a low-energy research replica or passive mockup, measure simultaneously:

- front/rear/base/chassis potential and displacement current;
- wideband electric and magnetic field spectra around the device;
- mechanical shaft torque/power where any drive exists;
- charge/storage energy before and after a run;
- load voltage and current with isolated differential instrumentation;
- effect of conductive versus nonconductive rear/base shields while separately measuring the capacitance change they introduce.

The decisive criterion is simple:

> Any conventional environmental-source hypothesis must show real incoming power at the same order as the sustained load power.

If the load is 100 W and every measured external/mechanical/storage port is orders of magnitude below 100 W for long enough to exclude stored-energy transients, only then is there an unexplained energy-balance residual worth escalating.

---

## 12. Working conclusion

The new historical resonance/environment statements are useful, but the quantitative survey sharply narrows their interpretation:

`environmental electrical state / bias`

→ `electrostatic influence / variable C`

→ `magnetically biased/timed pickup`

→ `tunable L/C impedance or resonance conditioning`

→ `nonlinear commutation`

→ `storage/load`.

The unresolved box remains **before** the conditioning chain:

`WHERE DOES THE REAL INPUT POWER ENTER?`

Ordinary fair-weather current, ordinary Schumann fields, Earth's static magnetic field and typical ambient RF are all far too small to account for a sustained ~100-W tabletop output. Resonance can condition or circulate supplied energy; it cannot close that power gap by itself.
