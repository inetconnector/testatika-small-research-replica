# Continuous-power claims and information-thermodynamics audit — 2026-08-23

**Document ID:** `DOC-CONTINUOUS-POWER-INFO-THERMO-2026-08-23`  
**Scope:** Testatika / Swiss M-L Converter / Methernitha claims of sustained electrical output, community supply, and the scientific meaning of "energy through order"  
**Status:** source audit + physics control framework; **not** a validation of over-unity  
**Evidence rule:** observed load, observed run time, operator/witness claim, later compilation, and derived physics are kept separate.

## Executive result

The internet record contains substantially stronger historical claims than a few-second lamp demonstration:

1. A first-person report dated **17 March 1984**, reproduced by Hans A. Nieper in 1985 and signed `L. L., Rorschach`, says that the converter supplied the company's electrical network **every day** through an **inverter and accumulator**; the same sentence says current from **two to three wind converters** was also fed into that network.
2. Nieper's own 1985 text says one converter, "possibly one or two more", had been running since **1982** and, among other uses, heated a roughly **5,500 ft² greenhouse**, including in winter. He states roughly **3–4 kW at 230 V DC**.
3. A visitor report dated **2 July 1988**, later enclosed by Don Kelly in correspondence now preserved in a U.S. Department of Energy file, says there were ten converters and an eleventh under construction; it claims that **ten converters plus windmills** provided enough electricity for the cooperative's **180 persons and businesses**, with possible wind surplus supplied to the Bernese utility.
4. Albert Hauser's 1986 visit report documents a **two-hour run** of a small machine, but explicitly says it was **not loaded with a resistance** during that test.
5. Hans Holzherr's 1999 report documents a roughly **1.5-hour run** of the 50-cm machine, but the explicit 1000-W lamp connection lasted only **about 10 seconds**; he also says he could not judge whether flat batteries could have been hidden in the base.

Therefore:

- It is **too strong** to say that all historical operating claims reduce to a few seconds of capacitor discharge. Contemporary/near-contemporary sources do claim daily, seasonal, and community-scale use.
- It is also **not justified** to say that sustained anomalous generation was experimentally established. No recovered source provides a source-isolated, continuously logged `∫P dt` energy balance over hours or days.
- The historical network claims are explicitly **confounded by storage and other generation**: an accumulator is named in 1984; wind generation is named in both 1984 and 1988. The DOE did **not** validate the converter; its 1989 reply says the submitted information was insufficient for an informed technical opinion.
- The strongest immediate witness tests separate into two categories: **long run time without calibrated sustained load**, and **brief load demonstrations without closed energy accounting**.

This distinction is now a project-level evidence constraint.

---

## 1. Evidence classes used in this audit

| Class | Meaning | Example |
|---|---|---|
| `OBS-RUN` | Witness directly reports machine remaining in operation for a stated time | Hauser 2 h; Holzherr ~1.5 h |
| `OBS-LOAD` | Witness directly reports a connected load | 1000-W-rated lamp, heating element |
| `MEASURED-ENERGY` | Continuous voltage/current/power and time integration with known instrument bandwidth and load | **Not recovered** |
| `OPERATION-CLAIM` | Witness/operator says device was used routinely, but no complete metering record is supplied | daily company-grid contribution; greenhouse |
| `MIXED-SUPPLY-CLAIM` | Claimed supply is explicitly mixed with storage and/or another generator | accumulator + wind; ten converters + windmills |
| `DOWNSTREAM` | Later paper repeats an earlier account | Kelly/Bailey repeating Nieper/L.L. |
| `CONTROL-PHYSICS` | Established physics used to define what a valid test must account for | capacitor energy, free energy, Landauer/info thermodynamics |

A long `OBS-RUN` is **not automatically** a long `OBS-LOAD`. A rated lamp is **not a wattmeter**. A network-use statement is **not a source-isolated energy balance**.

---

## 2. Historical chronology focused on duration and power

### 2.1 17 March 1984 — L. L., Rorschach: daily electrical-network claim

Nieper's 1985 book reproduces a report titled **"Inspection of the Swiss Tachyon Converter on 17 March 1984"**, ending `L. L., Rorschach, Switzerland`.

The report describes:
- manual start of the counter-rotating discs;
- Leyden-bottle storage;
- a bright incandescent-lamp demonstration;
- a heating element that became too hot to touch after a few seconds;
- a source-stated claim that 300 V DC / 10 A could be available continuously.

The most important duration statement for the present audit is separate from the brief load demo: L. L. says the converter produced current **every day of the week**, via an **inverter and an accumulator**, for the company's electrical network. The report immediately adds that **two to three wind converters** also fed current into that network.

**Evidence interpretation**
- `OBS-LOAD`: yes, but duration of the lamp/heater demonstration is brief.
- `OPERATION-CLAIM`: yes, daily network contribution.
- `MIXED-SUPPLY-CLAIM`: yes, explicitly accumulator + wind.
- `MEASURED-ENERGY`: no recovered continuous meter record.
- Consequence: a one-shot 10-kJ capacitor pulse cannot by itself explain a literal daily-network claim, but the historical text does **not isolate the Testatika as the network's sole energy source**.

Primary surviving publication:
- Hans A. Nieper, *Conversion of Gravity Field Energy / Revolution in Technology, Medicine and Society*, expanded English edition, section pp. 360–361 (book pagination), visitor report dated 17-Mar-1984.
- Public PDF mirror: https://navegantesdelcosmos.ec/repositorio/libros/Revolution%20In%20Technology%20Medicine%20And%20Society.%20Conversion%20Of%20Gravity%20Field%20Energy%20-%20Hans%20Alfred%20Nieper.pdf

### 2.2 1985 — Nieper: running since 1982 and greenhouse heating

In the preceding section, Nieper says he personally inspected the converter on **28 October 1984** and relays P. H. Matthey's 20-Oct-1984 visit. Nieper states that the machine, "possibly one or two more", had been running since **1982**, including heating a roughly **5,500-square-foot greenhouse** at roughly 2,600 ft altitude in winter, and assigns an output of about **3–4 kW at 230 V DC**.

**Evidence interpretation**
- This is a historically early and explicit long-duration operational claim.
- It is **not** accompanied by greenhouse energy bills, meter logs, wiring topology, accumulator state, wind contribution, or input/output integration.
- Nieper strongly advocates a nonstandard "tachyon/gravity field" theory; his causal interpretation is not evidence for the energy source.
- Later Kelly repetitions of this passage do not create independent confirmations.

### 2.3 14 February 1986 — Albert Hauser: two-hour run, explicitly no resistive load

The Kelly/Bailey conference paper reproduces an English translation of Hauser's report. Hauser says:
- the large machine was tested with a **1000-W glow lamp**;
- a smaller machine was running for **two hours**;
- for that small-machine test they used measuring instruments and **did not load the machine with any resistance**;
- he estimated about 200 W, but this was not a sustained resistive-load measurement.

**Evidence interpretation**
- Strong evidence for the witness's claim of a long-running small machine.
- Not evidence for `200 W × 2 h`.
- The report is especially valuable because it explicitly prevents the common internet conflation "two hours running" → "two hours delivering rated power".

Sources:
- Kelly & Bailey paper mirror: https://hiroko.or.jp/wp-content/file/nextgenerationenergy/TESTATIKA/1994-0821_swissMLconvertor-English.pdf
- Hauser mirror currently catalogued by the repository: https://www.robkalmeijer.nl/techniek/experiments/testakica/index.html

### 2.4 2 July 1988 — visitor report in DOE file: ten converters + wind for 180 persons/businesses

A German-language visit report dated **Saturday, 2 July 1988** is preserved as an enclosure in a 1989 Technidyne/Don Kelly correspondence file. It states:
- Luzius Cathomen was working on an **11th Testatika**;
- a converter produced about **3 kW**, and, according to the writer, about **4 kW in sunshine**;
- if all **ten converters** were in use **and the windmills were running**, the cooperative's **180 persons and businesses** had enough electricity for their needs;
- with strong wind, surplus could allegedly be fed to BKW;
- Cathomen started a converter by hand during the visit.

The same page refers to a forthcoming book by **Kaspar & Karlen**, but the exact authorship/signature of the surviving report page should remain `UNRESOLVED` unless the original source container proves it.

**Crucial provenance correction**
The document is in a U.S. Department of Energy archival packet because Don Kelly sent it to DOE. It is **not a DOE test**. DOE's Ryszard Gajewski replied on **26 May 1989** that the M-L Converter information was insufficient for him to offer an informed opinion on the device's technical merit.

Packet:
- https://documents.theblackvault.com/documents/doe/osti-coldfusion/Technidyne%20Associates.pdf
- Current mirror SHA-256 captured 2026-08-23: `9e0ad98d96fc2fbcdeb692a9e253da6881f0e1308cc1c177ae550ca5488d4816`

### 2.5 1991 — Kelly & Bailey: useful source genealogy and explicit skeptical control

Kelly & Bailey's paper is not an independent power test. It explicitly says their "only real evidence" consisted of documents from others and a videotape, and that known duplication attempts had failed.

This makes the paper valuable for **source genealogy**:
- its greenhouse/running-since-1982 passage is explicitly introduced as quotation/paraphrase from an earlier reference;
- its Hauser material is explicitly a reproduced translation;
- it must not be counted as another independent witness.

The paper also contains a solicited opposing view that is methodologically important:
- lamp and heater were described as the only actual-witness load tests;
- high-voltage/high-frequency effects can make filaments and thin conductors very hot;
- incandescence is therefore a poor indicator of **average real power** without electrical measurement;
- no test away from buildings was identified.

This is a useful historical reminder that the central measurement objection existed already in the contemporary technical discussion.

### 2.6 5 June 1999 — Hans Holzherr: 1.5 h run, ~10 s 1000-W-rated lamp

Holzherr reports a demonstration to more than 30 technicians/engineers:
- the 50-cm machine was already running when the group entered and was not stopped during their roughly **1.5-hour** visit;
- a **1000-W-rated lamp** was connected for approximately **10 seconds**;
- a U-shaped heater became too hot for him to hold within about a second;
- he did not notice a speed drop, but says attention shifted to the load;
- visitors were not allowed to touch/lift the 50-cm machine;
- when asked whether flat batteries could be concealed in the base, he explicitly answered that he **could not judge** that.

This is the cleanest recovered example of why duration categories must not be merged:
`~1.5 h machine running` ≠ `~1.5 h × 1 kW delivered`.

Source:
- https://rimstar.org/sdenergy/testa/report99.htm

---

## 3. What can and cannot be concluded from the historical record

### Supported as historical-source facts

It is supported that near-contemporary sources **made** claims of:
- operation since 1982;
- greenhouse heating;
- daily contribution to a company electrical network;
- ten converters plus windmills meeting the cooperative's electrical needs;
- self-running demonstrations lasting around 1.5–2 hours.

It is also supported that actual witnesses reported:
- bright lamp demonstrations;
- rapidly heated resistive elements;
- arcs/high voltage;
- long machine rotation.

### Not established by recovered records

No recovered online source yet provides all of the following in one test:
- calibrated continuous real-power measurement;
- known load impedance over time;
- simultaneous voltage/current waveforms or traceable power analyzer;
- complete accounting of accumulator state before/after;
- complete accounting of wind, grid, ground, mechanical, RF, thermal, optical, chemical, pneumatic, or other inputs;
- physical exclusion of concealed storage;
- continuous energy integral over hours;
- independent custody of the machine and instruments.

Therefore the historically interesting `OPERATION-CLAIM` evidence is **not equivalent** to a modern closed energy balance.

---

## 4. Capacitor-discharge analysis

For an ideal capacitor,

\[
E_C=\frac{1}{2}CV^2,\qquad C=\frac{2E}{V^2}.
\]

A nominal 1000-W load for 10 s requires only:

\[
E = Pt = 1000 \times 10 = 10{,}000\ \mathrm{J}=10\ \mathrm{kJ}.
\]

Ideal capacitance needed for 10 kJ:

| Voltage | Capacitance |
|---:|---:|
| 10 kV | 200 µF |
| 20 kV | 50 µF |
| 50 kV | 8 µF |

Thus the 1999 `1000 W rated lamp × ~10 s` observation is **energetically compatible** with prior electrical storage. That does not prove that storage caused the demonstration; it means the observation alone does not exclude it.

Longer energy scales are different:

| Claimed output | Duration | Energy | Ideal C at 20 kV |
|---:|---:|---:|---:|
| 1 kW | 1 h | 1 kWh = 3.6 MJ | 18 mF |
| 1 kW | 24 h | 24 kWh = 86.4 MJ | 0.432 F |
| 3 kW | 1 h | 3 kWh = 10.8 MJ | 54 mF |
| 3 kW | 24 h | 72 kWh = 259.2 MJ | 1.296 F |
| 4 kW | 1 h | 4 kWh = 14.4 MJ | 72 mF |
| 4 kW | 24 h | 96 kWh = 345.6 MJ | 1.728 F |

If a compact device truly supplied 3–4 kW continuously for days **after all conventional stored and incoming energy were excluded**, a brief precharged-capacitor explanation would be inadequate. But the historical network sources do not provide that isolation: they explicitly name an **accumulator** and/or **wind generation**.

Also, a one-hour 1-kW test would only rule out a sufficiently small **capacitor-only** reservoir. It would not automatically rule out a battery, chemical reservoir, external feed, or other unmeasured input.

---

## 5. Information thermodynamics: what "energy through order" can mean scientifically

A scientifically defensible translation of "order creates energy" is:

> **Order, information, correlations, and low-entropy / nonequilibrium states can constitute thermodynamic resources with extractable work value. They do not create energy ex nihilo; the complete cycle must include the resource preparation, feedback/memory reset, reservoirs, and entropy export.**

### 5.1 Free energy and low entropy

At fixed temperature,

\[
F = U - TS.
\]

For two states with equal internal energy `U` and temperature `T`, the lower-entropy state has higher Helmholtz free energy. A controlled relaxation toward equilibrium can, in principle, yield work bounded by the relevant free-energy decrease.

Sapienza, Cerisola & Roncaglia (2019) explicitly discuss correlations as thermodynamic resources and state the standard relation between free energy and average extractable work in the macroscopic regime.

### 5.2 Toyabe et al. 2010 — experimental information-to-energy conversion

Toyabe et al. used real-time information about a Brownian particle to apply feedback. The particle climbed a potential and gained free energy in an experiment designed to verify a generalized Jarzynski equality.

Scientific relevance to this project:
- **supports:** information can have operational thermodynamic work value;
- **does not support:** passive macroscopic geometry can continuously extract work from one equilibrium bath without a resource/reset cost.

DOI: `10.1038/nphys1821`

### 5.3 Chida et al. 2017 — Maxwell-demon electrical power

Chida et al. experimentally used monitoring and feedback on individual electron motion to produce directional electrical current and output power. Their paper also emphasizes the thermodynamic bookkeeping: the generated free energy is tied to the demon's information/memory cycle, so the second law is preserved.

Scientific relevance:
- demonstrates a real `information + fluctuations → electrical power` architecture;
- shows why the memory/feedback subsystem belongs inside the energy/entropy boundary;
- does **not** identify a corresponding subsystem in Testatika.

DOI: `10.1038/ncomms15301`

### 5.4 Landauer and the work cost of information processing

Bérut et al. experimentally verified the Landauer bound for erasing a one-bit memory in the slow-cycle limit. Faist et al. generalized work-cost statements for logical processes.

At 300 K,

\[
k_B T\ln 2 \approx 2.87\times 10^{-21}\ {\rm J}.
\]

As a **scale comparison only**, a 1-kW power rate divided by the Landauer energy is about `3.48×10^23 bits/s`; 3 kW is about `1.05×10^24 bits/s`. This is **not** a universal required information rate for an engine. It only shows that macroscopic kilowatt output is enormously larger than single-bit thermal energy scales, so a proposed information-engine mechanism must identify a correspondingly macroscopic physical resource flow or many microscopic events.

DOIs:
- Bérut et al.: `10.1038/nature10872`
- Faist et al.: `10.1038/ncomms8669`

### 5.5 Nonequilibrium resource streams

Strasberg et al. (2017) show that a stream of independently prepared units in arbitrary nonequilibrium states can serve as a resource of **nonequilibrium free energy** and can behave as heat, work, or information reservoirs.

This is potentially the most useful formal analogy for Testatika's repeated rotating sectors:
- if each sector/air region/dielectric interface is repeatedly prepared in a nonequilibrium charge state,
- and a state-dependent gate routes relaxation in a useful direction,
- then the repeated stream can in principle carry work value.

But the crucial unresolved question becomes:

> **What physical process prepares and continually replenishes that nonequilibrium state, and where is its free-energy/entropy cost?**

DOI: `10.1103/PhysRevX.7.021003`

### 5.6 Why a diode or asymmetry alone is not enough

A diode, ratchet, asymmetric electrode, or one-way gate can rectify a **driven** or **nonequilibrium** process. It does not by itself provide a sustained energy reservoir.

For a genuine information/ratchet interpretation the project must identify at least:
1. the fluctuating or nonequilibrium degree of freedom;
2. the state-dependent selection/gating variable;
3. the physical reservoir being depleted or driven;
4. the reset/replenishment process;
5. entropy exported per cycle;
6. measurable free-energy decrease or input power in that reservoir.

This corrects the stronger earlier wording in `methernitha-physics-operating-model.md`: merely "breaking symmetry" with a diode does **not** prove positive net work over a complete equilibrium cycle.

---

## 6. Testatika-specific hypotheses generated by information thermodynamics

The following are **research hypotheses, not historical facts**.

| Hypothesis | Possible thermodynamic resource | What would have to be measured | Falsification signal |
|---|---|---|---|
| `H-INFO-01` charge-sorting stream | repeatedly prepared non-equilibrium charge distribution on sectors/air | phase-resolved charge probability distribution, current, field, entropy/free-energy proxy | no non-equilibrium distribution beyond measurement noise |
| `H-INFO-02` corona/ion gradient | ionization / atmospheric chemical-electrical free energy | ion density, corona current, ozone/NOx, field energy, environmental dependence | output persists unchanged in ion-suppressed controlled atmosphere |
| `H-INFO-03` electret/dielectric relaxation | pre-polarized PMMA/interfacial charge | thermally stimulated depolarization, surface potential maps, dielectric absorption before/after | no stored polarization change despite output |
| `H-INFO-04` humidity/adsorbate gradient | chemical potential / surface conduction nonequilibrium | humidity, adsorption/desorption heat, leakage, surface current | no correlation over controlled RH sweep |
| `H-INFO-05` thermal gradient | heat flow between unequal temperatures | multi-point calorimetry and temperature gradients | no sufficient heat flow/exergy |
| `H-INFO-06` environmental electric field | atmospheric/ground electrostatic energy | field probes, earth current, shielding/orientation dependence | output survives Faraday/field controls with no equivalent source |
| `H-INFO-07` hidden conventional storage/feed | battery, accumulator, wire/RF/inductive feed | exhaustive source isolation, mass/chemistry/state-of-charge, RF/ground monitoring | energy exceeds bounded storage/input under custody |

No recovered historical source currently selects one of these mechanisms.

---

## 7. Decisive experimental protocol for a replica or any claimed original

The project should not use "lamp brightness" as its endpoint. A convincing test is an **energy-boundary experiment**.

### 7.1 Pre-test
- Photograph and document the complete device and all conductive paths.
- Measure accessible capacitances, battery/storage state, mass, temperatures, and surface potentials.
- Discharge known capacitors under a controlled procedure and document recovery/dielectric absorption.
- Establish environmental controls: ground connection, RF environment, light, airflow, humidity, temperature, vibration, magnetic/electric fields.
- Define the load and measurement bandwidth before the run.

### 7.2 During test
- Use a known resistive load or calibrated electronic load compatible with the output.
- Record `u(t)` and `i(t)` simultaneously and compute **real power** `p(t)=u(t)i(t)`, not `Vrms×Irms` unless power factor and waveform justify it.
- Integrate:
  \[
  E_{\rm out}=\int_0^T u(t)i(t)\,dt.
  \]
- Simultaneously log every allowed input channel.
- Record rotor speed/torque and device temperature.
- For an information-engine hypothesis, additionally log the proposed state variable and its probability distribution/correlation so entropy/free-energy changes can be estimated.

### 7.3 Post-test
- Re-measure storage state, capacitance, surface potential, temperature, mass and any chemical/electret indicators.
- Compute a conservative uncertainty budget.
- Claim an anomaly only if `E_out` exceeds **all measured inputs plus the maximum credible depletion of every bounded internal reservoir**, by more than the combined uncertainty.

A long run is useful only if its duration is chosen to exceed the bounded storage capacity. "One hour" is not a magic proof threshold.

---

## 8. Ranked evidence conclusion

### Historical claim strength

**Tier A — important, near-contemporary operational claims**
- L. L. 17-Mar-1984: daily company-network contribution, explicitly through accumulator and with wind contribution.
- Nieper 1985: since-1982 / greenhouse-heating / 3–4-kW claim.
- 2-Jul-1988 visitor report: ten converters + windmills sufficient for 180 persons/businesses.

These are strong evidence that **long-duration claims existed early**, not later internet inventions.

### Tier B — direct long-run observations
- Hauser: 2 h small-machine run, explicitly unloaded by resistance.
- Holzherr: ~1.5 h large-machine run, brief load tests.

These support long **operation**, not a calibrated long kW **energy delivery**.

### Tier C — downstream repetitions
- Kelly/Bailey and later web literature often repeat Nieper/L.L./Hauser. They add source genealogy and criticism, but repeated wording is not independent corroboration.

### Scientific bottom line

The evidence now supports the following careful statement:

> **Historical sources from the 1980s do claim that Testatika converters operated routinely and contributed to practical electrical supply over periods far longer than a capacitor flash. If those claims represented source-isolated 3–4-kW output, a small precharged capacitor would be grossly insufficient. However, the surviving reports do not contain the independent continuous energy measurements needed to establish that premise, and the strongest network claims explicitly include an accumulator and wind power.**

The information-thermodynamics literature materially improves the project's theoretical framing:

> **"Order" can carry free energy and information/correlations can be converted into work, including electrical power, but only as part of a complete thermodynamic resource cycle. A Testatika analogue would require identifying the concrete nonequilibrium resource and its replenishment/reset cost.**

This is a scientifically interesting direction to test; it is not an over-unity conclusion.

---

## 9. Key sources

### Historical
- Hans A. Nieper, *Conversion of Gravity Field Energy / Revolution in Technology, Medicine and Society* (expanded English edition; 1985-era source container), Swiss ML-Converter and 17-Mar-1984 report:  
  https://navegantesdelcosmos.ec/repositorio/libros/Revolution%20In%20Technology%20Medicine%20And%20Society.%20Conversion%20Of%20Gravity%20Field%20Energy%20-%20Hans%20Alfred%20Nieper.pdf
- DOE/Technidyne archival packet, including 2-Jul-1988 visitor report and DOE reply of 26-May-1989:  
  https://documents.theblackvault.com/documents/doe/osti-coldfusion/Technidyne%20Associates.pdf
- Donald Kelly & Patrick Bailey, *The Methernitha Free Energy Machine: The Swiss M-L Converter*, conference-paper mirror:  
  https://hiroko.or.jp/wp-content/file/nextgenerationenergy/TESTATIKA/1994-0821_swissMLconvertor-English.pdf
- Hans Holzherr, 1999 demonstration correspondence/report:  
  https://rimstar.org/sdenergy/testa/report99.htm
- Albert Hauser material mirror:  
  https://www.robkalmeijer.nl/techniek/experiments/testakica/index.html

### Information thermodynamics / controls
- Toyabe, S. et al. (2010), *Experimental demonstration of information-to-energy conversion and validation of the generalized Jarzynski equality*, Nature Physics 6, 988–992. DOI `10.1038/nphys1821`
- Bérut, A. et al. (2012), *Experimental verification of Landauer's principle linking information and thermodynamics*, Nature 483, 187–189. DOI `10.1038/nature10872`
- Parrondo, J. M. R., Horowitz, J. M. & Sagawa, T. (2015), *Thermodynamics of information*, Nature Physics 11, 131–139. DOI `10.1038/nphys3230`
- Faist, P. et al. (2015), *The minimal work cost of information processing*, Nature Communications 6, 7669. DOI `10.1038/ncomms8669`
- Chida, K. et al. (2017), *Power generator driven by Maxwell's demon*, Nature Communications 8, 15301. DOI `10.1038/ncomms15301`
- Strasberg, P. et al. (2017), *Quantum and Information Thermodynamics: A Unifying Framework Based on Repeated Interactions*, Physical Review X 7, 021003. DOI `10.1103/PhysRevX.7.021003`
- Sapienza, F., Cerisola, F. & Roncaglia, A. J. (2019), *Correlations as a resource in quantum thermodynamics*, Nature Communications 10, 2492. DOI `10.1038/s41467-019-10572-8`

---

## 10. Open acquisition targets

1. Original typed `L. L.` 17-Mar-1984 report, rather than the Nieper reproduction.
2. Original P. H. Matthey 20-Oct-1984 report.
3. DVS/GAGFE records identifying all alleged inspection dates and instrumentation.
4. Metering/utility/greenhouse records, if any, for the 1982–1988 operational claims.
5. Original source container and authorship/signature for the 2-Jul-1988 Kaspar/Karlen-associated report.
6. Any contemporary photographs showing the inverter/accumulator/network interface.
7. Any continuous oscilloscope/power-meter traces or filmed uncut load tests.
8. Any documentation of wind/accumulator state simultaneous with claimed Testatika supply.

Until one of these closes the energy boundary, the status remains **historically significant sustained-use claims, experimentally unresolved source of energy**.
