# Internet source audit — round 11 — 2026-08-18

## Scope

Round 11 follows the newly strengthened historical `environment / resonance / magnetized pickup` line and asks two separate questions:

1. Which statements are genuinely present in the preserved historical/replication sources, and which frequencies/mechanisms were added later by back-engineering?
2. Can ordinary environmental electrical reservoirs quantitatively supply a sustained ~100-W tabletop load?

The canonical quantitative companion is [`m2-v4-11-environmental-port-survey.md`](m2-v4-11-environmental-port-survey.md). The calculations are source-discrimination tools, not a claim that M2 contained RF/resonance hardware.

---

## 1. Major provenance correction: the Linden relay itself does not say 80–140 MHz

Preserved source:

- https://rimstar.org/sdenergy/testa/lindenexp.htm

The page explicitly describes the Linden account as second-hand: two visitors witnessed Baumann's demonstration, then described it to a third person who wrote the surviving letter from memory.

The actual relayed construction is:

- U-shaped/meter-like magnet;
- ordinary insulated installation wire wound around its middle;
- the two wire ends stripped and galvanically connected, forming a closed loop;
- two dissimilar/metal plates with paper/insulator between them;
- Baumann holds the sandwich with his fingers between the magnet poles;
- a voltmeter reportedly indicates ~700 V;
- later attempts by the witnesses fail to reproduce it;
- the reported voltage slowly drops while the meter remains connected.

The preserved relayed text contains **no 80–140-MHz frequency statement**.

By contrast Paul E. Potter's later back-engineering says that the Linden experiment was *thought* to register about 80–140 MHz and uses this in an HF/electron-cascade theory:

- https://www.rexresearch.com/testatik/testart.htm

Therefore:

- `Linden ~700 V` = H2 relayed historical claim;
- `Linden 80–140 MHz` = **later Potter secondary interpretation / not original relay wording**;
- no M2 or M0b historical baseline may encode 80–140 MHz as Baumann-stated fact.

This is a material correction because the frequency has repeatedly been used online as if it were a direct operating specification.

---

## 2. Rimstar Series 1: finger/body bias reproduced, magnet-specific effect not reproduced

Preserved experiment:

- https://rimstar.org/sdenergy/testa/lindentests1.htm

Steven Dufresne reports about 540 mV with the metal plates held in the fingers. The same reading occurs away from the magnet. When a plastic clamp replaces the fingers, the reading goes to zero.

This is a strong control result:

- the small measured voltage in that setup does not require the magnet;
- hand contact/body coupling/contact potentials are sufficient to create the reading;
- any future Linden replication must use noncontact fixtures and explicitly characterize body/earth/probe capacitance and dissimilar-metal electrochemistry.

It does not prove the historical 700-V report was a measurement artifact, but it gives a concrete conventional artifact that must be excluded before accepting the claim.

---

## 3. Rimstar Series 2: UHF drive produces ordinary small induction, not 700 V or anomalous power

Preserved experiment:

- https://rimstar.org/sdenergy/testa/testamagseries2.htm

Key results:

- UHF oscillator sweep roughly 280–425 MHz in a direct Linden-style configuration: no additional voltage beyond the finger-associated bias;
- induced/rectified measurements around 297 MHz: about 0.25 V and ~0.42 V depending on probe/contact placement;
- a later partial galvanic connection from oscillator to magnet produced about 1 V at 10 microamps DC;
- an explicitly tuned capacitor attempt near ~333 MHz did not reproduce the Linden result;
- another configuration showed frequency-selective DC readings around 200, 315 and 370 MHz, but only about 80–120 mV and microamp scale.

The author himself describes this as resonance/frequency selectivity, but the energy scale is tiny and the circuit contains an explicit powered UHF oscillator and rectification path.

**Consequence:** frequency-selective behavior is real in the replication, but it is fully compatible with conventional induction, parasitic coupling and rectification. It supplies no evidence that a historical Testatika obtained bulk energy from a resonance.

---

## 4. Rimstar Series 3: HV spike conversion to low-voltage DC is conventional and low-current

Preserved experiment:

- https://rimstar.org/sdenergy/testa/testatika_magnets_hv_to_dc.htm

Dufresne pulsed magnet windings with high-voltage spikes from a Van de Graaff source and added a capacitor/measurement load. The experiment demonstrates that short HV pulses can be converted to lower-voltage DC in a straightforward way.

Reported scale:

- low-voltage output around 0.1 V in the illustrated test;
- current fluctuating roughly 0.5–6 microamps.

This is useful as a control against claims that `high voltage -> low voltage / higher current` necessarily requires an exotic transformer. It is ordinary energy conversion; the source-side pulse energy remains the source.

---

## 5. Hauser retrospective: strongest explicit atmosphere/operator-source statement recovered on the public web

Public author page:

- https://equapio.com/energie/testatika-legendaere-energiemaschine-der-methernitha/

Albert Hauser retrospectively states that his group moved the generator to test the hidden-transmitter/focus possibility. He says Baumann answered that the device would not work in space because it collected/sorted charged ions present in the atmosphere; he also relays a closed-window stop / open-window restart claim and says the generator was stopped during atmospheric disturbances/thunderstorms. He states that Baumann related the technique to lightning and weather-light phenomena.

Evidence status remains:

- Hauser location-change observation: H1/P1 retrospective of his own visit;
- `space / ions / windows / storms / lightning` mechanism explanation: Baumann→Hauser retrospective relay;
- not a quantitative measurement of source current or power.

The same page contains obvious numeric corruption in some machine dimensions/speeds, so it is not used as numeric source of record.

---

## 6. Atmospheric-electricity quantitative control

Scientific source examples:

- G. M. Lucas et al., atmospheric/global electric circuit literature: near-surface fair-weather field around 100–200 V/m and current density around 1–3 pA/m².
- A. J. G. Baumgaertner et al., global electric circuit models: ionosphere ~250 kV relative to ground, fair-weather current density ~1 pA/m².

Representative URLs:

- https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2016JD025944
- https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/jgrd.50725
- https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2021JD035954

At the optimistic full-column values `J=2 pA/m²`, `V=250 kV`:

`P/A = J*V = 0.5 microW/m²`.

Thus 100 W requires an ideal effective area of `2e8 m² = 200 km²` even before collection losses.

For a 0.2-m tabletop span in a 100-V/m fair-weather field, the local potential difference is only ~20 V and the corresponding conduction-power density is ~`4e-11 W/m²`.

**Conclusion:** ordinary fair-weather atmospheric conduction can influence bias/charge state but cannot be the claimed ~100-W bulk source of a tabletop machine.

---

## 7. 50-Hz mains-field control

WHO/ICNIRP environmental summaries give typical natural/household/power-line field scales. A WHO summary lists home background fields away from transmission lines at up to roughly 100 V/m electric and 0.2 microtesla magnetic, with much larger fields possible directly under high-voltage lines.

Representative public source:

- https://www.who.int/news-room/questions-and-answers/item/radiation-electromagnetic-fields

Using the V4.10 optimistic floating-capacitive bound with `Ceq=50 pF`, `span=0.20 m`:

- 50 Hz and 100 V/m -> ~6.28 microW;
- 50 Hz and 10 kV/m -> ~62.8 mW;
- 100 W would require ~399 kV/m at the same capacitance/span.

Therefore unnoticed ordinary room 50-Hz field pickup cannot explain 100 W through pF-scale coupling. A hidden galvanic/base/table path or much larger capacitance is a different hypothesis and must be directly measured.

---

## 8. Ambient RF control

A field survey in the 0.8–2.45-GHz bands reported average ambient power densities commonly between about `-35` and `-10 dBm/m²`, with a highest outdoor average around `-7 dBm/m²` (~200 microW/m²) in that measurement environment.

Representative source:

- https://www.mdpi.com/1424-8220/21/23/7838

At 200 microW/m², ideal 100-W capture requires 500,000 m² (0.5 km²) aperture before rectifier/matching loss.

Even a much stronger local field of 0.1 W/m² would require 1000 m² ideal capture for 100 W.

**Conclusion:** ordinary ambient broadcast/cellular/Wi-Fi RF is excluded as the tabletop bulk source. A strong local hidden transmitter/near-field coupler is not excluded by this ambient calculation, but it would require correspondingly strong measurable local fields or currents.

---

## 9. Schumann resonance control

Natural Schumann resonance magnetic fields are around the pT scale. One Radio Science study explicitly notes ~1 pT amplitudes; an artificial ELF excitation experiment in the Schumann band reported ~1 pT magnetic and ~0.2 mV/m electric amplitude at a receiver.

Representative sources:

- https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2014RS005567
- https://agupubs.onlinelibrary.wiley.com/doi/10.1029/RS025i006p01291

Using only an order-of-magnitude `E*B/mu0` power-flux proxy gives ~`1.6e-10 W/m²`. A 100-W ideal aperture would be ~`6.3e11 m²`, around 628,000 km².

Because the Earth-ionosphere cavity is not a simple free-space plane wave, this proxy is not a rigorous harvester model. It is nevertheless sufficient to show the enormous scale mismatch.

**Conclusion:** ordinary Schumann background may provide timing/noise/reference structure but not the claimed bulk power.

---

## 10. Geomagnetic field control

Earth's magnetic field is around 50 microtesla. A 200-mm one-turn loop rotating at 60 rpm has an optimistic peak Faraday EMF only around 9.9 microvolts; even 24 ideal series turns give only ~0.237 mV.

More fundamentally, ordinary magnetic generation loads the rotor with counter-torque; electrical output is paid for by mechanical input.

Reference background:

- https://www.nist.gov/news-events/news/2013/06/mri-phantoms-moving-next-stage
- https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2000RG000097

**Conclusion:** geomagnetism may remain a startup/orientation/bias variable, but not an independent sustained 100-W reservoir under standard electrodynamics.

---

## 11. What genuinely became stronger after Round 11

### Strengthened

- Environmental language exists in source chains and deserves direct measurement rather than dismissal.
- Magnetized pickups + resonance/tuning are historically meaningful for large/workshop variants.
- The exact Linden historical relay is simpler than Potter's later HF theory.
- Independent replication work shows real frequency-selective induction/rectification but at tiny conventional power scales.
- Ordinary atmospheric DC, Schumann ELF, geomagnetic and normal ambient-RF reservoirs are quantitatively far too small for sustained ~100-W tabletop output.

### Downgraded/corrected

- `80–140 MHz Linden frequency` is **not** source-stated in the preserved Linden relay; it is later secondary back-engineering.
- `resonance` must not be equated with `energy source`.
- `air ions` may be a historical operator explanation, but measured fair-weather conduction current is far too small to supply the claimed load power directly.

---

## 12. Highest-priority remaining conventional source search

After these bounds, the conventional source space becomes much narrower:

1. hidden/overlooked galvanic base, table, chassis or measurement return;
2. strong local near-field RF/inductive/capacitive transmitter rather than ambient background;
3. mechanical shaft/bearing/belt work;
4. finite stored electrostatic/electret/chemical energy;
5. incorrect historical power estimate/demonstration interpretation.

Any next experiment must measure these incoming ports simultaneously with output. A resonance peak without a source-side real-power balance is not evidence of anomalous energy.

---

## 13. Historical baseline consequence

**No M2 historical CAD/electrical baseline change is justified by Round 11.**

M2 remains:

- individually floating small rotor conductors;
- no rubbing contacts;
- two-terminal side pots as directly described;
- Crystal black box;
- horseshoe magnets present on the first small machine but function unknown;
- no Tesla/HF stage added as historical fact.

Round 11 adds a measurement/calculation layer only: `V4.11 environmental-port survey`.
