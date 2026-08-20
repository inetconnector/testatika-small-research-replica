# M2 V4.29 — field-gated surface-redox reservoir hypothesis

**Date:** 2026-08-20  
**Status:** HYPOTHESIS / quantitative discriminator. Not a historical-source claim.

## 1. Why this candidate is worth adding

V4.28 strongly constrains ordinary weak ambient reservoirs at the 100-W tabletop scale: fair-weather atmospheric current, normal 50-Hz stray fields, ambient RF, Schumann/ELF, compact-span natural geoelectric pickup, weak airflow, ordinary sound, small thermal gradients and weak illumination are all far too small unless a strong local source is present.

That leaves two broad conventional classes capable of supplying real power without an obvious external wire:

1. finite high-energy-density storage inside matter;
2. a local nonequilibrium chemical process that consumes reactants while the electrostatic machine only routes/conditions the released energy.

V4.29 examines a specific form of class 2:

`metal / oxide / adsorbed water / oxygen interface`

`-> field-gated redox / ion-electron transfer`

`-> low-voltage high-charge source`

`-> variable-C / resonance / crystal gate`

`-> high-voltage storage and electrostatic motor feedback`.

The point is not that Testatika used this mechanism. The point is that a **surface-chemical Gibbs-free-energy reservoir** can satisfy a power-density problem that weak ambient fields cannot.

## 2. External scientific motivation

Two modern literature lines motivate the discriminator:

- ACS Applied Electronic Materials (2023), DOI `10.1021/acsaelm.3c01263`: non-noble metal electrodes in moisture-electric generators can make the apparent driving force switch from a humidity gradient to ordinary metal oxidation. Reported open-circuit outputs depended strongly on Al, Fe and Cu electrodes. The paper explicitly warns that corrosion/electrochemical contributions must be separated from genuine humidity harvesting.
- Nature Communications (2025), DOI `10.1038/s41467-025-61913-9`: a moisture energy harvester deliberately combining ion storage with Faradaic redox couples reported `6.7 W/m²` peak power density. This establishes that moisture-driven interfacial charge transport and redox chemistry can coexist and materially raise output.

These papers do not support Testatika historically. They show that "humidity + metal/oxide interfaces + charge separation" can hide a chemical-energy contribution if only voltage/current behavior is inspected.

For a high-energy-density scale comparison, Communications Materials (2024), DOI `10.1038/s43246-024-00662-6`, tabulates practical aluminum-air specific-energy values around `1878 Wh/kg` for static-electrolyte systems and `2566 Wh/kg` for flowing-electrolyte systems.

## 3. Quantitative scale

Canonical calculator:

`sim/m2_v4_29_surface_redox_reservoir.py`

Regression tests:

`tests/test_m2_v4_29_surface_redox_reservoir.py`

### 3.1 Pure humidity harvesting is still too weak for a compact 100-W machine

Using the 2025 `6.7 W/m²` peak comparison value:

- `100 W` requires about `14.9 m²` projected active area;
- `3 kW` requires about `448 m²` projected active area.

Therefore a simple moisture harvester on the visible surface of a small machine does not close the historical power scale. Large internal stacked area could raise geometric area, but moisture mass transport and heat/chemical-potential flux would then have to be measured explicitly.

### 3.2 Battery-like surface chemistry can meet finite demonstration scales

Using `1878 Wh/kg` as a practical aluminum-air comparison:

- `100 W` for `1 h` corresponds to about `53 g` active-Al-equivalent;
- `300 W` for `1 h` corresponds to about `160 g`;
- `3 kW` for `10 min` corresponds to about `266 g`;
- `3 kW` for `1 h` corresponds to about `1.60 kg`.

These are not microscopic reservoirs, but they are vastly more compact than the ambient-field capture areas required by V4.28.

For the 100-W / 1-h comparison, ideal aluminum oxidation would also require about `47 g O2`. Therefore a real metal-air-like source would necessarily leave measurable stoichiometric signatures: oxidant consumption, solid reaction products, mass redistribution, heat and surface-composition change.

## 4. Why it fits several clues without making them the energy source

This hypothesis separates **bulk source** from **routing clues**.

### Humidity

A nanometre-scale adsorbed water film can enable ionic transport and electric-double-layer formation, while excessive humidity can simultaneously increase surface leakage and destroy an electrostatic machine's working field. Therefore the historical statement "dry air helps startup" does not by itself exclude a small amount of interfacial water chemistry; it predicts an optimum window rather than monotonic humidity dependence.

### Ozone / negative-ion language

Corona and strong local fields can create ozone, ions and reactive oxygen species. Under V4.29 these are possible by-products or reaction mediators, not proof that atmospheric ions provide the 100-W bulk power.

### Non-contact capacitive pickup

The Weber non-contact pickup architecture remains compatible: a chemical reservoir could establish/replenish charge while the rotor and stationary plates perform electrostatic impedance conversion and phase-dependent charge transfer.

### Crystal / diode / resonance

The V4.26 chain remains unchanged:

`slow C(theta) event -> fast ringdown -> nonlinear crystal gate -> directed storage charge`.

The crystal need not carry the original chemical reaction current directly. It can act as the timing/rectification element that converts a low-voltage/high-charge reservoir into a high-voltage electrostatic state.

### Rear metal plate stop effect

The rear-plate effect can still be a threshold/control phenomenon. A nearby conductor changes the capacitance matrix and pickup amplitude; if the crystal gate falls below threshold the machine can stop abruptly even though the reservoir itself remains present.

### East-West startup

A weak geomagnetic/electrostatic asymmetry can provide startup bias or polarity selection without supplying appreciable real power. V4.29 therefore does not require Earth fields to be the bulk reservoir.

## 5. Strong falsification protocol

The decisive test is not "does humidity matter?". It is to hold humidity constant while changing chemistry.

Run the same low-energy replica / candidate module under:

1. air at fixed RH;
2. nitrogen at the same RH;
3. oxygen-enriched nitrogen at the same RH;
4. dry air at the same oxygen fraction;
5. repeated long-duration cycling with pre/post component mass and surface inspection.

Measure simultaneously:

- output real power;
- O2 concentration / gas consumption;
- humidity;
- temperature and heat flow;
- mass change;
- corrosion/oxide signatures on candidate electrodes;
- charge/current through every deliberate electrical path.

Predictions if surface redox is the bulk reservoir:

- output should track reactant availability at fixed RH;
- long runs should produce stoichiometric material changes;
- a 100-W-class source should not remain chemically invisible;
- disabling the electrostatic routing chain may stop useful output while chemical reaction can still be detected separately.

If power survives oxygen removal, fixed-RH inert-gas operation, mass/surface controls and all other V4.28 ports, this hypothesis is strongly falsified.

## 6. A second unbounded conventional gap: stored pressure / sorption

V4.23 bounded external airflow but did not explicitly bound a **precharged internal pressure/vacuum or sorption reservoir**. A sealed pressure vessel, gas-loaded porous solid, spring or sorption material can store finite mechanical/chemical free energy and then release it slowly. This is therefore another finite-duration reservoir class that a closed watt-budget experiment should inventory.

It fits the historical electrostatic clues much worse than surface redox and would require a transduction path into rotor/field work, but it should not be silently omitted from the boundary ledger.

## 7. Working conclusion

The strongest new conventional reservoir candidate after V4.28 is not another weak ambient field. It is:

**a local nonequilibrium surface-chemical reservoir, possibly metal/oxide/water/oxygen redox, with the visible electrostatic/resonant machine acting mainly as a high-voltage charge pump and timing network.**

This candidate can satisfy 100-W-class finite-duration energy density, naturally creates humidity/ion/surface-potential dependencies, and makes hard stoichiometric predictions.

It is not evidence for the historical Testatika and it is not inexhaustible. If long-duration closed-budget experiments exclude it together with stored pressure/sorption, hidden local powered inputs and other V4.28 channels, the residual remains **UNKNOWN** rather than automatically becoming a quantum-vacuum source.
