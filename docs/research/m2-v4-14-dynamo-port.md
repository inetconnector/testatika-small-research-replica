# M2 V4.14 — Earth–ionosphere–magnetosphere dynamo-port coupling bound

## Status

**DERIVED diagnostic / HYPOTHESIS discriminator.** This document does **not** add a Tesla/HF stage, a magnetospheric energy source, or a solved environmental port to the historical M2 baseline.

It asks the next narrower question after V4.11–V4.13:

> **Could an extremely high-impedance, resonant, magnetically structured machine couple strongly enough to the Earth–ionosphere–magnetosphere dynamo potentials to supply sustained real power?**

The target discriminator is intentionally severe:

`100 W ~= 100 kV * 1 mA`.

If no physically defensible coupling can reduce the effective source impedance enough to support approximately this operating point, the magnetosphere/ionosphere explanation also fails as the bulk source for a 100-W-class tabletop machine.

Canonical calculator: `sim/m2_v4_14_dynamo_port.py`.

---

## 1. First correction: the large voltage is real, but it is not a low-impedance socket

Primary atmospheric-electricity literature supports all of the following at once:

- ionosphere-to-ground potential of order `240–250 kV`;
- fair-weather current density of only a few `pA/m²`;
- near-ground electric field of order `100 V/m`;
- high-latitude magnetospheric/ionospheric potentials can modulate the surface electric field and air–Earth current.

Representative primary sources:

- Lucas et al. (2015), *A global electric circuit model within a community climate model*, DOI `10.1002/2015JD023562`;
- Roble & Hays (1979), *A quasi-static model of global atmospheric electricity 2*, DOI `10.1029/JA084iA12p07247`;
- Reddell et al. (2004), *Seasonal variations of atmospheric electricity measured at Amundsen-Scott South Pole Station*, DOI `10.1029/2004JA010536`.

The key missing quantity is therefore **source impedance**.

With an intentionally optimistic full-column model,

`V_oc = 250 kV`

and

`J = 2 pA/m²`.

The area-normalized Thevenin resistance is

`R_A = V_oc / J = 1.25e17 ohm*m²`.

For a generous tabletop collection footprint `A = 0.1 m²`,

`R_s = R_A / A = 1.25e18 ohm`.

The corresponding short-circuit current scale is only

`I_sc = J*A = 0.2 pA`.

Even while granting the **entire 250-kV ionospheric potential** to that 0.1-m² port, the ideal matched-load power is only

`P_max = V_oc² / (4 R_s) ~= 12.5 nW`.

This is already an extremely optimistic upper bound because a 20-cm tabletop machine does not physically span the ionosphere-to-ground column.

---

## 2. The exact 100-W source-impedance target

For an ideal Thevenin source with `V_oc = 250 kV`, the largest source resistance that can deliver `100 W` under perfect matching is

`R_s,100W = V_oc² / (4 P) ~= 156.25 Mohm`.

Compare this with the optimistic 0.1-m² fair-weather-column value:

`1.25e18 ohm / 1.5625e8 ohm ~= 8.0e9`.

So the missing coupling is not a small efficiency improvement. It must reduce the effective source impedance by roughly **eight billion times** compared with the ordinary 0.1-m² fair-weather column.

If the desired loaded operating point is explicitly

`V_load = 100 kV`, `I_load = 1 mA`,

then a 250-kV Thevenin source may have at most

`R_s = (250 kV - 100 kV) / 1 mA = 150 Mohm`.

The effective fair-weather collection area required for that source resistance is

`A_eff ~= 8.33e8 m² ~= 833 km²`.

A simpler current-only bound gives

`A = 1 mA / (2 pA/m²) = 5e8 m² = 500 km²`.

Both calculations say the same thing: a self-contained tabletop machine needs a hitherto unidentified coupling that behaves as if it accesses **hundreds of square kilometres of atmospheric current collection**, or some completely different low-impedance port.

---

## 3. Resonance and impedance transformation do not remove this deficit

This is the central point for an extremely high-impedance resonant machine.

An ideal transformer or lossless resonator can transform voltage, current and impedance:

`V2 = n*V1`

`I2 = I1/n`

`R2 = n²*R1`.

But

`P_max = V_oc²/(4R_s)`

is unchanged by ideal impedance transformation.

Example using the more realistic local 20-cm fair-weather field:

- `E ~= 100 V/m`;
- `h = 0.20 m`;
- local open-circuit scale `V ~= 20 V`;
- inferred conductivity `sigma = J/E ~= 2e-14 S/m`;
- for `A = 0.1 m²`, local `R_s ~= 1e14 ohm`;
- matched real-power bound `~1 pW`.

An ideal 1:5000 step-up can turn 20 V into 100 kV, but it transforms the source resistance to about

`2.5e21 ohm`

and the transformed short-circuit current to only about

`4e-17 A`.

The 100-kV number can therefore be made impressive while the available real power becomes effectively zero.

**This distinction—high open-circuit voltage versus low source impedance—is probably the most important discriminator in the entire environmental-source search.**

---

## 4. There is one interesting near-hit: full-potential switched capacitance

Suppose, only as a deliberately optimistic thought experiment, that the machine could actually switch a capacitance directly across the full `250 kV` environmental potential.

If each event transfers the full capacitor energy

`E_event = 1/2 C V²`,

then at `24 events/s`, the capacitance required for `100 W` is

`C ~= 133 pF`.

That is not geometrically absurd for a Testatika-sized electrostatic structure.

The corresponding full recharge charge-transport scale is

`I_Q = C*V*f ~= 0.8 mA`.

This is strikingly close to the desired `~1 mA` scale.

But it does **not** solve the source problem. It sharpens it:

> If the historical mechanism really used the Earth–ionosphere potential as the voltage reservoir, it still needed a way to recharge roughly 100-pF-scale effective capacitances at **sub-milliamp to milliamp average charge transport**, not at `pA/m²` fair-weather current density.

For the ordinary 0.1-m² fair-weather port, `0.8 mA / 0.2 pA ~= 4e9`.

So the missing element would need to increase effective environmental charge transport by billions, while remaining visually compatible with the apparatus.

This is now a concrete quantitative target rather than a vague “environmental energy” statement.

---

## 5. Magnetosphere-to-ground coupling is real, but measured surface currents stay tiny

The magnetosphere is not electrically irrelevant to the lower atmosphere.

Roble & Hays modeled ionospheric dynamo and magnetospheric-convection potentials mapping downward and found high-latitude perturbations of the ground electric field and air–Earth current on the order of tens of percent under quiet conditions, with larger and more variable effects during storms.

Reddell et al. used a magnetospheric potential model for South Pole atmospheric-electricity data. Their magnetospheric corrections reached approximately:

- `+15 to -25 V/m` in ground electric field;
- `+0.5 to -0.8 pA/m²` in current density.

Those are experimentally relevant modulations, but not a hidden 1-mA port.

For `A = 0.1 m²`, `0.8 pA/m²` corresponds to only

`0.08 pA`.

Across a 20-cm height, `25 V/m` is only about

`5 V`.

Thus magnetospheric dynamo potentials can plausibly modulate startup threshold, charge state, leakage history or timing—especially at high latitude—but the measured lower-atmosphere coupling remains an **ultra-high-impedance control/bias channel**, not a 100-W power channel.

Switzerland/central Europe is not the polar cap; a mechanism relying on the strongest high-latitude mapping would need an additional geographic explanation for routine operation there.

---

## 6. Auroral Poynting flux proves the reservoir exists—but mostly above us

The solar-wind–magnetosphere–ionosphere system carries enormous real electromagnetic power.

DMSP/LEO measurements report typical quasi-steady downward Poynting flux near auroral/cusp regions of order `1–10 mW/m²`, with larger values during active conditions.

Primary examples:

- Kilcommons et al. (2022), *DMSP Poynting Flux: Data Processing and Inter-Spacecraft Comparisons*, DOI `10.1029/2022JA030299`;
- Lu et al. (2018), *Poynting Flux in the Dayside Polar Cap Boundary Regions From DMSP F15 Satellite Measurements*, DOI `10.1029/2018JA025309`.

At `10 mW/m²`, even a physically colocated ideal 100% receiver would need

`A = 100 W / 0.01 W/m² = 10,000 m²`

to intercept 100 W.

More importantly, these fluxes are measured in the ionosphere/upper atmosphere, where they are largely dissipated through ionospheric Joule heating and plasma processes. A tabletop device at ground is not sitting in that Poynting-flux sheet.

Therefore “the magnetosphere carries plenty of power globally” is true, but it does not establish a ground-level low-impedance port.

---

## 7. Ground ULF magnetic coupling is far too weak

Magnetospheric ULF waves are genuinely observed on the ground.

Representative primary measurements include:

- Hartinger et al. (2020), *Simultaneous Observations of Geoelectric and Geomagnetic Fields Produced by Magnetospheric ULF Waves*, DOI `10.1029/2020GL089441`;
- Pilipenko et al. (2014), *Modulation of total electron content by ULF Pc5 waves*, DOI `10.1002/2013JA019594`.

Use a deliberately large ground magnetic fluctuation:

- sinusoidal `B = 400 nT`;
- `f = 5 mHz`;
- one-turn loop with area of a 200-mm disc, `A ~= 0.0314 m²`.

Faraday's law gives a peak EMF of only

`V_ind = A*2*pi*f*B ~= 3.95e-10 V`.

To obtain 100 kV from that one-turn induced voltage by pure resonant voltage gain would require a ratio of about

`2.5e14`.

Interpreting that naively as a Q-like voltage enhancement at `5 mHz` implies an amplitude ring-down time

`tau ~= Q/(pi*f)`

of roughly **5e8 years**.

Even granting an extravagant combined `turns × magnetic-flux concentration = 10^6`, the required gain remains about `2.5e8`, corresponding to a centuries-scale low-frequency ring-down.

That is not a credible tabletop resonator.

And again: even a magical lossless voltage step-up would not increase the incident real power.

---

## 8. Magnetic structure does not turn ordinary near-ground air ions into a field-aligned plasma wire

A particularly important question is whether magnetized pickups/grids could somehow guide atmospheric charge along magnetic field lines and thereby bypass the enormous atmospheric resistance.

For a singly charged drift carrier, the magnetization/Hall parameter can be written

`beta = omega_c*tau = mobility * B`.

Atmospheric small-ion mobility near standard conditions is of order

`mu ~= 1.5 cm²/(V*s) = 1.5e-4 m²/(V*s)`.

Primary source:

- Tammet (1998), *Reduction of air ion mobility to standard conditions*, DOI `10.1029/97JD01429`.

Even at an extremely strong local field of `B = 1 T`,

`beta ~= 1.5e-4 << 1`.

That means ordinary small atmospheric ions near ground are overwhelmingly **collision dominated**, not magnetically tied to field lines.

At `0.5 T`, the number is even smaller.

So magnetized grids can certainly shape local magnetic forces, material hysteresis, electron trajectories in special discharge regions, or timing. But they do **not** create a low-loss magnetic ion conduit from a tabletop machine through the neutral troposphere to the ionosphere.

A reduced-pressure discharge would be a different local plasma regime, but then its ionization/sustaining energy must itself appear in the energy ledger.

---

## 9. Magnetotelluric / geomagnetically induced ground fields also fail at tabletop length

During major geomagnetic storms, measurable geoelectric fields appear in the ground and can drive large currents in power grids and pipelines because those systems have **tens to thousands of kilometres of conductor length**.

A recent primary example from the May 2024 superstorm reports localized surface geoelectric fields reaching roughly `1.5 V/km` in North China:

- Ma et al. (2025), *Mid-Latitude Geoelectric Field Response in North China During the May 2024 Superstorm*, DOI `10.1029/2025SW004557`.

Across `0.20 m`, even `1.5 V/km` gives only

`0.3 mV`.

Delivering 100 W at `0.3 mV` would require roughly

`333 kA`.

This is why geomagnetically induced currents matter in continental infrastructure but not as an unnoticed 20-cm tabletop power source.

A genuine telluric-energy hypothesis therefore needs a large conductive baseline, ground electrodes, building wiring, buried metal or another external structure. If none exists, the port is absent.

---

## 10. What the M2 clues can still mean without supplying bulk power

The direct M2 evidence remains compatible with environmental **control**:

- dry air changes leakage and surface-charge lifetime;
- rear metal plate changes capacitance/boundary conditions and may detune or suppress a threshold process;
- East–West startup instruction could reflect an electric/magnetic/orientation-sensitive threshold even though post-start reorientation did not stop the machine;
- floating rotor wires are extremely sensitive to weak external fields and charge history;
- a nonlinear `crystal` could turn a tiny bias change into a large **state change** without supplying the load energy itself.

A threshold system can therefore be very sensitive to an environment that contributes almost no real power.

This distinction is crucial:

`environment controls whether the machine oscillates`

is not equivalent to

`environment supplies the load power`.

---

## 11. The strongest surviving magnetosphere hypothesis

After the source-impedance calculation, only a much more specific hypothesis remains:

> There is an **unidentified effective-aperture / return-path mechanism** that couples the tabletop apparatus to a far larger Earth–ionosphere–magnetosphere current system than its physical size suggests.

For this to explain 100 W, it must satisfy at least one of these measurable conditions:

1. expose an effective environmental source resistance of roughly `<= 150–160 Mohm` at a `~250-kV` open-circuit scale; or
2. deliver roughly `1 mA` at `~100 kV` equivalent after conversion; or
3. provide at least `100 W` of real incoming electromagnetic/mechanical power through a separately identifiable port.

Known passive mechanisms—ordinary atmospheric conduction, local fair-weather field pickup, ULF induction, auroral Poynting flux at ground, normal telluric gradients, magnetic guidance of atmospheric small ions, or ideal resonance/transformer action—do not meet that requirement.

That does **not** prove that no unknown coupling exists. It gives the unknown coupling a hard engineering specification.

---

## 12. Highest-value experimental search for the missing coupling

The next replica programme should not chase higher open-circuit voltage. It should measure **source impedance and effective aperture**.

### A. Environmental electric-port transfer function

On a safe low-voltage passive M2 geometry, apply a calibrated external electric field between large front/rear plates and measure:

- internal floating-node voltages;
- displacement current;
- storage charging rate;
- real input power at the external plates;
- response versus frequency from quasi-static through the internally relevant band.

Define

`H_E(f) = V_internal(f) / E_external(f)`

and, more importantly,

`eta_E(f) = P_storage_or_load / P_external_real`.

This calibrates how much natural field would actually be required.

### B. Magnetic-port transfer function

Use a calibrated low-field Helmholtz/large-loop drive around the replica and measure

`H_B(f) = V_internal(f) / B_external(f)`

plus real source power and rotor-angle dependence.

Sweep through:

- quasi-static Earth-field scale (`tens of microtesla`);
- ULF-equivalent modulation;
- rotor/event envelope frequencies.

Do not use the historical magnets themselves as the energy source in the ledger.

### C. Faraday enclosure with retuning control

Compare operation inside/outside a conductive enclosure, but **retune the internal resonant frequency/Q to the same values** before interpreting suppression.

Otherwise shielding and simple detuning are confounded.

If the effect remains suppressed after equivalent retuning, an external electric/RF port becomes more credible.

### D. Ground/telluric port isolation

Repeat with:

- dielectric stand;
- conductive but floating base plate;
- intentionally earth-grounded base;
- high-value resistive ground return;
- isolated/fibre instrumentation.

Measure every base/ground current directly.

### E. Natural-correlation channel

Log simultaneously:

- local atmospheric potential gradient;
- air–Earth current if available;
- local magnetometer `B(t)` and `dB/dt`;
- local ground electric field / electrode voltage if available;
- RH, temperature and ion concentration;
- rotor speed/start threshold/internal pickup voltage.

A magnetosphere-driven effect should show repeatable coherence with the relevant environmental channel. A pure humidity/leakage effect should instead follow surface-resistance/charge-decay variables.

### F. Load-step source-impedance measurement

This is the decisive test for a high-voltage high-impedance machine.

Measure the internal source under at least two known loads and determine its Thevenin/Norton equivalent:

`R_s = DeltaV / DeltaI`.

A system that reaches very high open-circuit voltage but collapses under microamp loading is a high-impedance electrostatic source, not a 100-W source.

The target is explicit:

`R_s <= O(1e8 ohm)` at the relevant high-voltage equivalent scale.

---

## 13. Falsification criteria

The Earth–ionosphere–magnetosphere bulk-source hypothesis should be rejected for the M2-scale machine if controlled measurements show all of the following:

- environmental electric coupling extrapolates to real input power many orders below the load;
- magnetic transfer function is consistent with ordinary Faraday induction and passive flux concentration;
- shielding effects disappear after capacitance/resonance retuning;
- grounding/base changes reveal no large hidden return current;
- natural output/start behavior has no reproducible coherence with geomagnetic/electric activity after controlling RH and charge history;
- load-step testing yields a source impedance far above the `~1e8-ohm` order required for 100 W at the proposed HV scale.

Conversely, the hypothesis becomes materially more interesting only if a low-energy replica demonstrates an unexpectedly large **real-power transfer coefficient** from an externally calibrated field while all local conductive/mechanical inputs are measured.

---

## 14. Working conclusion

The answer is now sharper than “the atmosphere is too weak.”

**Yes:** Earth, ionosphere and magnetosphere form real coupled electrical/current systems; magnetospheric potentials measurably modulate surface atmospheric electricity, and large electromagnetic power flows into the high-latitude ionosphere.

**But:** the known coupling to a self-contained 20-cm ground device is extraordinarily high impedance. A resonator can build voltage, and magnetic structure can alter local timing/field geometry, but neither changes the maximum real power available from the environmental port.

For a 0.1-m² fair-weather collector, the optimistic full-column source is roughly

`250 kV open circuit / 1.25e18 ohm`

with only

`~12.5 nW ideal matched power`.

The 100-W explanation therefore requires a missing coupling that changes the effective source impedance by roughly

`~8e9`.

That is the new search target:

> **Find a physically identifiable mechanism that turns the Earth–ionosphere–magnetosphere environment into a <=~150-Mohm source at the 250-kV scale, or produces an equivalent ~1 mA at ~100 kV. If it cannot be found or measured, this bulk-energy hypothesis falls.**
