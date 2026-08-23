# Corrigendum: physical operating model — information thermodynamics and energy-boundary rules

**Document ID:** `DOC-METHERNITHA-PHYSICS-CORRIGENDUM-2026-08-23`  
**Applies to:** `docs/research/methernitha-physics-operating-model.md`  
**Status:** mandatory epistemic correction/addendum  
**Rule:** where this corrigendum conflicts with stronger causal wording in the earlier operating-model document, **this corrigendum controls** until a later source-qualified revision incorporates it.

## 1. Why this correction is necessary

The earlier operating-model synthesis contains useful candidate mechanisms, but some sentences are written too definitively for the available evidence. In particular, the following must not be treated as established properties of the historical machine:

- that a hidden motor is unnecessary **because a specific electrostatic self-drive mechanism has been demonstrated**;
- that the `crystal` or a diode switches at a particular rotor phase and thereby removes counter-torque;
- that the horseshoe magnets specifically act as an eddy-current speed brake;
- that the top-pot spiral necessarily forms a particular LC low-pass network;
- that a 10-s, 1000-W-rated lamp demonstration was **caused** by capacitor/dielectric discharge;
- that a one-hour 1-kW run would, by itself, exclude every conventional storage/feed explanation.

These remain **HYPOTHESES** unless supported by machine-specific measurements or stronger primary evidence.

## 2. Correct thermodynamic statement about "order"

The scientifically defensible translation is:

> **Order, information, correlations and a low-entropy or otherwise nonequilibrium state can be thermodynamic resources with work value. The complete cycle must account for how that resource is prepared/replenished and where entropy and dissipation go.**

At fixed temperature,

\[
F=U-TS.
\]

For the same `U` and `T`, lowering `S` raises Helmholtz free energy. Relaxation from a prepared nonequilibrium/low-entropy state can therefore yield useful work. That is not energy creation from nothing; it is conversion of free energy stored in the prepared state or in the resources used for measurement/feedback.

Relevant experimental/theoretical controls:
- Toyabe et al. 2010, DOI `10.1038/nphys1821`: feedback-based experimental information-to-free-energy conversion.
- Bérut et al. 2012, DOI `10.1038/nature10872`: experimental Landauer bound.
- Faist et al. 2015, DOI `10.1038/ncomms8669`: minimal work cost of information processing.
- Chida et al. 2017, DOI `10.1038/ncomms15301`: Maxwell-demon architecture producing electrical current and power while full information/memory thermodynamics preserves the second law.
- Strasberg et al. 2017, DOI `10.1103/PhysRevX.7.021003`: repeated nonequilibrium units as a free-energy resource.
- Sapienza et al. 2019, DOI `10.1038/s41467-019-10572-8`: correlations as thermodynamic resources.

## 3. Correct status of the `crystal` / diode hypothesis

A diode or other nonlinear gate may be important for:
- charge pumping;
- peak holding;
- phase-dependent routing;
- suppressing reverse current;
- rectifying a **driven or nonequilibrium** fluctuation/charge stream.

But **asymmetry alone is not an energy source**. In an equilibrium system a passive rectifier does not permit sustained net work from one bath. A positive cycle-averaged output requires a physical nonequilibrium resource, feedback/memory resource, work input, temperature/chemical/electric gradient, or depletion of stored free energy.

Therefore statements such as "the diode removes the counter-torque and creates directed work" must be read as a **candidate mechanism conditional on an unidentified resource**, not a completed energy-source explanation.

## 4. Correct status of capacitor storage

The 1999 Holzherr report states:
- ~1.5 h machine run;
- 1000-W-rated lamp connected for ~10 s;
- heater heated rapidly;
- hidden flat batteries in the inaccessible 50-cm base could not be judged by the witness.

For `1 kW × 10 s`, nominal load energy is `10 kJ`. At 20 kV an ideal capacitor storing 10 kJ would require only 50 µF. Thus the brief load is **compatible with** finite pre-stored electrical energy.

This is an exclusion statement, not a causal finding:
- `compatible with storage` ≠ `storage was demonstrated`;
- rated lamp wattage ≠ measured real power;
- lamp brightness/filament temperature ≠ calibrated `∫u(t)i(t)dt`.

## 5. New historical constraint: sustained-use claims are real source claims

The project must also avoid the opposite overcorrection: historical claims were not limited to a few-second lamp pulse.

The 17-Mar-1984 `L. L., Rorschach` report reproduced by Nieper says the converter supplied the company electrical network **every day** via an **inverter and accumulator**, while two to three wind converters also fed the network.

Nieper's own text says machine(s) had operated since 1982 and heated a ~5500-ft² greenhouse.

The 2-Jul-1988 visitor report later preserved in the DOE/Technidyne packet says **ten converters plus windmills** sufficed for the cooperative's **180 persons and businesses**.

Correct conclusion:

> A small precharged capacitor cannot explain a literal multi-day, kW-scale source-isolated output. But the surviving historical reports do not demonstrate source isolation: accumulator and wind are explicitly present, and continuous meter records are missing.

## 6. DOE provenance correction

The U.S. Department of Energy did **not** test or endorse Testatika merely because the 1988 visitor report appears in a DOE archival packet.

DOE's 26-May-1989 reply states that the information supplied on the M-L Converter was **insufficient for an informed opinion on technical merit**.

This caveat must accompany every project reference to the "DOE document".

## 7. Testable information-engine translation for Testatika

The interesting research question is no longer "can order create energy?" in an unrestricted sense. It is:

> **Does some Testatika subsystem repeatedly prepare, select, correlate, or relax a measurable nonequilibrium state whose free-energy decrease can account for the output, and what physical process pays the preparation/reset cost?**

Candidate resources to test, all presently `HYPOTHESIS`:
- charge separation / non-equilibrium sector charge distribution;
- ion/corona chemical-electrical gradients;
- electret or trapped-charge relaxation in PMMA/dielectrics;
- humidity/adsorbate chemical potential;
- thermal gradients;
- atmospheric/ground electric-field coupling;
- conventional battery/accumulator or hidden external feed.

No one of these is selected by the historical evidence.

## 8. Required experiment boundary

Future replica claims must integrate real power and bound all reservoirs:

\[
E_{\rm out}=\int u(t)i(t)\,dt.
\]

A valid anomaly claim requires:

\[
E_{\rm out} >
E_{\rm measured\,inputs}+
E_{\rm max\,credible\,internal\,depletion}
+\text{combined uncertainty}.
\]

The run time must be chosen from the measured/bounded storage capacity; one hour is not intrinsically decisive. Post-test state-of-charge, surface potential, temperature, dielectric polarization proxies and other candidate reservoirs must be checked.

For a proposed information engine, measure the state variable and probability distribution/correlations as well as the energetic reset/replenishment channel. Otherwise "information" remains a metaphor rather than an energy balance.

## 9. Linked full audit

See:
- `docs/research/continuous-power-and-information-thermodynamics-audit-2026-08-23.md`
- `docs/research/continuous-power-evidence-2026-08-23.tsv`
- `docs/research/continuous-power-info-thermo-provenance-2026-08-23.yaml`

These files contain the full duration/source genealogy, capacitor-energy bounds, information-thermodynamics literature and acquisition targets.
