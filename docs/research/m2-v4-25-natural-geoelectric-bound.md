# M2 V4.25 — natural geoelectric / telluric storm-field bound

## Status

**DERIVED diagnostic / external-source discriminator with primary geophysics controls.**

V4.24 showed that naive Earth-surface `v x B` reasoning does not produce a useful 100-W tabletop source. A stronger geophysical alternative remains:

> Time-varying magnetospheric/ionospheric currents really do induce measurable horizontal electric fields in the conducting Earth. Could the M2 have tapped that telluric/geoelectric field?

This is a legitimate conventional geophysical coupling mechanism. Geomagnetic storms are known to drive geomagnetically induced currents in long grounded infrastructure.

The question is therefore not whether geoelectric fields exist. They do. The question is whether their **local voltage and source-impedance scale across a ~20-cm machine** can approach the historical 100-W-class claim.

Nothing in V4.25 adds ground electrodes or a telluric circuit to the historical M2 baseline. Such a connection is not source-supported for M2. The model deliberately grants the full horizontal field potential across a 0.2-m span as an optimistic upper bound.

Canonical calculator: `sim/m2_v4_25_natural_geoelectric_bound.py`.

---

## 1. Primary-source field scales

The source set below is deliberately restricted to primary geophysics studies or official publication records of those studies.

### Moderate-storm direct measurements

Hartinger et al. (2020), *Geophysical Research Letters*, DOI `10.1029/2020GL089441`, report simultaneous geoelectric/geomagnetic observations associated with magnetospheric ULF waves. Their study includes geoelectric fields of approximately

`~1 V/km`

during two moderate storms.

This is particularly valuable because it is a direct natural-field measurement rather than a Testatika-specific inference.

### April 2023 severe storm, northern Europe

Wawrzaszek et al. (2024), *Scientific Reports* 14, 25074, report modeled European geoelectric-field peaks during the 23–24 April 2023 storm. Selected high-latitude stations reached approximately

`1.8 V/km`

and

`3.0 V/km`.

These are storm-time peaks and are highly location/geology dependent.

### March 1989 Britain

Hübert et al. (2025), *Space Weather*, DOI `10.1029/2025SW004427`, used long-period magnetotelluric data and modeled geoelectric fields for major historical storms. Their Britain model reaches approximately

`12 V/km`

in central Britain during the March 1989 storm.

### March 1989 United States

Love et al. (2022), *Space Weather*, DOI `10.1029/2021SW003030`, map the March 1989 superstorm using magnetotelluric/surface-impedance data. Their reported peak 1-minute-resolution field amplitudes include approximately

`21.66 V/km`

in Maine and `19.02 V/km` in Virginia.

### Carrington-class model

Love et al. (2025), *Geophysical Research Letters*, DOI `10.1029/2025GL116835`, model a Carrington-intensity storm across the United States. Their Virginia result includes a median peak field of about

`30.30 V/km`

with a stated 68% confidence interval extending to

`47.20 V/km`

at the high end.

This last value is a **modeled confidence-bound comparison**, not an observed historical Testatika environment and not a direct 1859 local measurement.

---

## 2. A compact 20-cm machine integrates almost none of a V/km field

For a roughly uniform horizontal geoelectric field,

`Delta V = E * L`.

The machine span is only

`L = 0.2 m = 0.0002 km`.

Therefore:

| geoelectric field | full potential across 20 cm |
|---:|---:|
| 1 V/km | 0.2 mV |
| 3 V/km | 0.6 mV |
| 12 V/km | 2.4 mV |
| 21.66 V/km | 4.332 mV |
| 30.30 V/km | 6.06 mV |
| 47.20 V/km | 9.44 mV |

This is the decisive geometric scale.

Even a modeled Carrington-class upper comparison produces only **millivolts across a 20-cm baseline**.

A floating tabletop apparatus without two ideal Earth-coupled terminals could see less. So the table is already favorable to the telluric-source hypothesis.

---

## 3. 100 W at millivolts requires kiloamperes

For real power,

`I = P/V`.

At `P = 100 W`:

| geoelectric field | `V` across 20 cm | current required for 100 W |
|---:|---:|---:|
| 1 V/km | 0.2 mV | 500 kA |
| 3 V/km | 0.6 mV | 167 kA |
| 12 V/km | 2.4 mV | 41.7 kA |
| 21.66 V/km | 4.332 mV | 23.1 kA |
| 30.30 V/km | 6.06 mV | 16.5 kA |
| 47.20 V/km | 9.44 mV | 10.6 kA |

A transformer or resonant converter could change the voltage/current ratio after collection, but it cannot reduce the real input-power requirement.

Thus the geoelectric source would have to behave as an extraordinarily low-voltage, extraordinarily high-current source at the local 20-cm scale.

---

## 4. The source-impedance requirement becomes nanohms

V4.22 gives the best-case Thevenin matched-power condition

`P_max = V_oc^2/(4 R_s)`.

Therefore

`R_s,max = V_oc^2/(4P)`.

Using the complete 20-cm geoelectric potential as `V_oc`, the 100-W source-resistance ceilings become approximately:

| field | 20-cm `V_oc` | `R_s,max` for 100 W |
|---:|---:|---:|
| 1 V/km | 0.2 mV | 0.1 nOhm |
| 3 V/km | 0.6 mV | 0.9 nOhm |
| 12 V/km | 2.4 mV | 14.4 nOhm |
| 21.66 V/km | 4.332 mV | 46.9 nOhm |
| 30.30 V/km | 6.06 mV | 91.8 nOhm |
| 47.20 V/km | 9.44 mV | 223 nOhm |

This is a much stronger constraint than merely saying that storm fields are `small`.

A compact source capable of turning a few millivolts of natural geoelectric gradient into 100 W would need a source impedance in the tens-to-hundreds-of-nanohms range even under severe/Carrington-class comparison fields.

V4.25 does not need a detailed soil-electrode model to reject the simple interpretation. The required source resistance itself is already extreme, and the historical M2 does not expose kilometer-scale grounded conductors that would integrate the field over a large baseline.

---

## 5. Why power grids can experience GIC while a tabletop machine cannot simply copy that effect

This is an important distinction.

Geomagnetically induced currents are real, and long grounded technological systems can experience substantial currents during storms. The reason is geometric:

`V_line = integral(E . dl)`.

A nearly uniform `1 V/km` field produces approximately:

- 1 V over 1 km;
- 10 V over 10 km;
- 100 V over 100 km.

A `30.3 V/km` extreme comparison gives approximately:

- 30.3 V over 1 km;
- 303 V over 10 km;
- 3030 V over 100 km.

Shao et al. (2024), *Space Weather*, DOI `10.1029/2023SW003758`, explicitly find >`1 V/km` geoelectric fields in parts of North China during the March 2015 storm and modeled induced voltages exceeding `100 V` on parts of the regional transmission network.

That is a conventional and well-understood example of a natural field becoming technologically important because the infrastructure provides **long conductive baselines and Earth connections**.

The M2 has a roughly 20-cm physical scale and no source-supported kilometers-long buried/grounded collector.

Therefore `power grids get geomagnetically induced currents` is not evidence that a 20-cm floating Testatika can collect comparable power.

---

## 6. Direct accumulation to 100 kV would require continental baselines

Suppose one tried to obtain the historical high-voltage scale directly from the geoelectric field before any transformer/converter.

Required baseline is

`L = V/E`.

For `100 kV`:

| field | baseline required |
|---:|---:|
| 1 V/km | 100,000 km |
| 3 V/km | 33,333 km |
| 12 V/km | 8,333 km |
| 21.66 V/km | 4,617 km |
| 30.30 V/km | 3,300 km |
| 47.20 V/km | 2,119 km |

Clearly the M2 does not directly span such distances.

An impedance converter can raise a millivolt input to high voltage, but then the input current must increase correspondingly. At `6.06 mV`, an ideal 100-W converter begins with roughly `16.5 kA`; there is no energy advantage.

---

## 7. Storm timing is another discriminator

A bulk source based on geomagnetic-storm induction makes a strong empirical prediction:

> output should increase dramatically during severe geomagnetic disturbances and fall during quiet conditions.

The primary geophysics literature shows that storm-time geoelectric fields can vary by orders of magnitude with event, location and geology.

The surviving M2 reports instead emphasize dry-air/humidity behavior, startup orientation and the rear-metal-plate perturbation. The currently audited corpus does not contain a calibrated correlation between M2 output and geomagnetic-storm indices or measured local telluric field.

That absence does not prove no relationship existed, because historical monitoring was incomplete. But it means a storm-powered interpretation is presently **HYPOTHESIS**, not source-supported fact.

A modern test should therefore record local magnetic and geoelectric conditions rather than infer them from weather or compass orientation.

---

## 8. Could a hidden long baseline exist through the building or Earth?

This remains the strongest conventional version of the telluric hypothesis.

If some hidden conductor, pipe, grounding network, power-line shield, building reinforcement or other extended structure provided a long baseline, the apparatus could in principle couple to a much larger integrated geoelectric voltage than its own 20-cm dimensions suggest.

But then that extended structure is part of the **source system** and must be included inside the experimental boundary.

The falsification test is simple in concept:

- run on an isolated nonconductive platform;
- record every Earth/building connection;
- compare floating versus one-point Earth-referenced operation;
- change location/building while keeping the machine configuration fixed;
- measure actual potential differences between candidate building/Earth nodes;
- correlate output with measured geoelectric field and geomagnetic disturbance.

A real long-baseline source should reveal a corresponding terminal voltage/current and location dependence.

This test does not require hazardous voltage injection.

---

## 9. Relationship to the rear-metal-plate effect

V4.19 showed that a nearby conductive plate can strongly change a high-impedance electrostatic return path. V4.25 does not negate that result.

The rear plate may still control:

- common-mode capacitance;
- Earth/building return capacitance;
- field-line redistribution;
- resonator detuning/Q;
- nonlinear threshold crossing.

But these are **coupling conditions**, not proof that the underlying energy is telluric.

In fact, the combination of V4.19 and V4.25 suggests a useful separation:

`rear plate / humidity / orientation = possible coupling or threshold controls`

while

`bulk 100-W source = still requires a much stronger real-power port`.

That distinction remains one of the most important results of the current investigation.

---

## 10. Current conclusion

Natural geoelectric/telluric fields are real and can drive significant currents in **long grounded infrastructure**.

But for a 20-cm tabletop machine:

- moderate-storm `~1 V/km` -> only `0.2 mV` across the device;
- severe `~12–22 V/km` -> only a few millivolts;
- modeled Carrington-class `~30–47 V/km` -> still only `6–9 mV`.

At 100 W those local voltages demand approximately `10 kA` to `500 kA` and matched source impedances from sub-nanohm to a few hundred nanohms.

Therefore:

**DERIVED:** ordinary compact coupling to known natural telluric/geoelectric fields is not a credible 100-W source for M2.

**OPEN HYPOTHESIS:** a hidden long-baseline Earth/building coupling could integrate larger voltage, but then the extended infrastructure is part of the source and should be measurable.

**UNKNOWN:** an unrecognized geophysical channel with very different local impedance/field structure remains logically possible, but it is not represented by the measured storm-time geoelectric fields quantified here.

The energy-source chain is now narrowed further:

`large geophysical reservoir`

`-> ??? low-impedance local channel`

`-> electrostatic M2 coupling/commutation`

`-> storage/load`.

The unresolved `???` cannot be replaced simply by `telluric current`, because known telluric field measurements do not provide the required compact-scale voltage/current product.

---

## 11. Primary comparison sources

- Hartinger, M. D. et al. (2020), *Simultaneous Observations of Geoelectric and Geomagnetic Fields Produced by Magnetospheric ULF Waves*, **Geophysical Research Letters** 47, DOI `10.1029/2020GL089441`.
- Love, J. J. et al. (2022), *Mapping a magnetic superstorm: March 1989 geoelectric hazards and impacts on United States power systems*, **Space Weather** 20, DOI `10.1029/2021SW003030`.
- Shao, Y. et al. (2024), *Geoelectric Field Estimations During Geomagnetic Storm in North China From SinoProbe Magnetotelluric Impedances*, **Space Weather**, DOI `10.1029/2023SW003758`.
- Wawrzaszek, A. et al. (2024), *Geoelectric fields and geomagnetically induced currents during the April 23–24, 2023 geomagnetic storm*, **Scientific Reports** 14, 25074.
- Hübert, J. et al. (2025), *Developing a New Ground Electric Field Model for Geomagnetically Induced Currents in Britain Based on Long-Period Magnetotelluric Data*, **Space Weather**, DOI `10.1029/2025SW004427`.
- Love, J. J. et al. (2025), *Mapping a Carrington storm*, **Geophysical Research Letters** 52, DOI `10.1029/2025GL116835`.

These papers validate the **geophysical comparison scales**, not Testatika performance.
