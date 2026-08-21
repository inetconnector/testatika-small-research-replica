# V4.32 — physical reservoir siting and active-base discriminator

**Date:** 2026-08-21  
**Status:** **DERIVED + HYPOTHESIS ranking. Not a historical source claim.**

## 1. Question

V4.31 established two important limits:

1. a short `1 kW × 10 s = 10 kJ` load episode is only `2.78 Wh`, so a finite matter reservoir can be physically small;
2. the simple visible M2 side pots cannot store anything close to `10 kJ` as ordinary electrostatic field energy.

V4.32 therefore asks a more concrete question:

> **If a conventional finite reservoir existed, where in the surviving machine geometries could it physically sit?**

The analysis ranks candidate locations by both **geometric capacity** and **source compatibility**. It does not infer hidden material merely because volume exists.

Canonical calculator:

`sim/m2_v4_32_physical_reservoir_siting.py`

Regression tests:

`tests/test_m2_v4_32_physical_reservoir_siting.py`

---

## 2. Mandatory machine-family separation

The source rules remain unchanged.

### M2

Direct Marinov correspondence supports:

- one ~200-mm small-machine rotor;
- floating rotor wires `connected to nothing`;
- two side condensers with cylindrical conductive grid + plastic insulation + central copper spiral;
- two external wires per side condenser;
- no conventional built-in drive motor;
- an unresolved upper `crystal`.

The M2 source line does **not** report a hidden battery stack, electrolyte, active layered base or chemical fill.

### M6 / large family

Hauser's direct M6a line supports materially more complex large cylinders:

- three concentric metal-grid tubes;
- acrylic separators;
- central magnet tube;
- two-layer bifilar copper winding;
- top crystal/possible-rectifier assembly.

Holzherr's separate M6b line reports that large capacitors contained about 20 perforated-sheet layers.

A separate expanded large-family relay in `baumann-statements.tsv` (H005) says a thick wooden foundation plate was allegedly built from alternating perforated conductive and insulating plates. This has only **low-medium historical confidence** and is not a Hauser direct-observation anchor. Nevertheless it is a high-value acquisition/test lead because such a structure would place a large distributed electrical/chemical interface under the whole machine.

**Do not transfer H005 into M2.**

---

## 3. Working envelope volumes

All dimensions below are **current reconstruction working values**, not measurements of original objects.

### M2 V4 working CAD

| location | working envelope | gross volume |
|---|---:|---:|
| two side pots | 2 × Ø84 × 110 mm | **1.219 L** |
| top carrier | 170 × 28 × 18 mm | **0.0857 L** |
| lower central cage | 24 × 18 × 70 mm | **0.0302 L** |
| rotor gross PMMA disc | Ø200 × 3.5 mm | **0.110 L** |
| base gross working envelope | 370 × 180 × 30 mm | **1.998 L** |

### M6 V1/V2 working CAD

| location | working envelope | gross volume |
|---|---:|---:|
| two large cylinders | 2 × Ø146 × 235 mm | **7.869 L** |
| two capacitor cans | Ø78 × 112 mm + Ø62 × 92 mm | **0.813 L** |
| base gross working envelope | 760 × 340 × 28 mm | **7.235 L** |

These are upper geometric envelopes. Real usable volume is lower because shells, PMMA, grids, windings, structural members and air occupy space.

---

## 4. Energy-density discriminator

Three very different historical/scale questions must not be mixed:

- short witness burst: `1 kW × 10 s = 2.78 Wh`;
- sustained moderate output: `100 W × 1.5 h = 150 Wh`;
- sustained kilowatt output: `1 kW × 1.5 h = 1500 Wh`.

Required **gross-envelope** energy densities are:

| site | 10-kJ burst | 100 W × 1.5 h | 1 kW × 1.5 h |
|---|---:|---:|---:|
| M2 side-pot pair | 2.28 Wh/L | 123 Wh/L | 1230 Wh/L |
| M2 top carrier | 32.4 Wh/L | 1751 Wh/L | 17,507 Wh/L |
| M2 lower cage | 91.9 Wh/L | 4960 Wh/L | 49,603 Wh/L |
| M2 rotor gross disc | 25.3 Wh/L | 1364 Wh/L | 13,642 Wh/L |
| M2 base working envelope | 1.39 Wh/L | 75.1 Wh/L | 751 Wh/L |
| M6 two large cylinders | **0.353 Wh/L** | **19.1 Wh/L** | **190.6 Wh/L** |
| M6 two capacitor cans | 3.42 Wh/L | 184.5 Wh/L | 1845 Wh/L |
| M6 base working envelope | **0.384 Wh/L** | **20.7 Wh/L** | **207.3 Wh/L** |

### Interpretation

Geometry alone strongly favours the **M6 base and large-cylinder volumes** if one is testing a finite matter/chemical reservoir. Even the `1 kW × 1.5 h` scale corresponds to gross-envelope densities around only `190–207 Wh/L` there.

This does **not** show that such a reservoir existed. It only says that the large-family physical envelope does not rule out conventional finite-energy storage on volume grounds.

By contrast, a tiny M2 top module could easily contain enough energy for a single 10-kJ burst in abstract volumetric terms, but it would require implausibly extreme density for sustained high output, and the source evidence points more naturally toward a nonlinear/gating role than toward a bulk store.

---

## 5. Candidate-location ranking — M2

### 5.1 Side-pot grid / spiral interfaces — **best M2 matter-reservoir test location**

Why it deserves testing:

- directly source-supported conductive grid;
- directly source-supported copper spiral;
- dielectric/plastic separation;
- large fraction of the M2 visible volume;
- natural place for surface oxide, adsorbed water, charge trapping and slow interfacial transport.

Why it remains only a hypothesis:

- Marinov does not report electrolyte, dissimilar-metal pile, hidden active mass or third electrode;
- the direct construction description is comparatively simple;
- V4.31 excludes the simple pot pair as a kilojoule **electrostatic** store.

Current role ranking:

**slow charge reservoir / surface chemistry candidate > bulk electrostatic store.**

### 5.2 Layered outer panels — **strong interface / conversion candidate, weak bulk store**

The video shows a coarse perforated carrier, dark fine inset, reddish elongated conductor/frame and leads. This is genuine visible layering.

That makes the panels interesting for:

- field penetration;
- corona/ion transport;
- distributed contact-potential effects;
- thin interfacial redox/electret tests;
- noncontact pickup / charge sorting.

However the actual material volume is small. A genuinely thin coating would need high energy density to explain even a 10-kJ burst. The panels are therefore more credible as **conversion/interface structures** than as the principal reservoir.

### 5.3 Top `crystal` carrier — **best gate candidate, not best reservoir candidate**

The top carrier gross envelope is only ~`0.086 L`. A 10-kJ finite store would require ~`32 Wh/L`, which is geometrically possible for matter storage, but continuous 100-W or kW operation quickly requires extreme densities.

More importantly, source convergence points toward:

- `crystal` terminology;
- possible nonlinear rectification/phase control;
- a four-terminal coil/central-conductor precedent on a different early small model.

Therefore V4.32 keeps the working hierarchy:

**top module = gate / threshold / resonant-commutation candidate first; reservoir second.**

### 5.4 Lower central cage — **low priority bulk reservoir**

Its gross envelope is only ~`0.030 L`, and the video favours a perforated/cage-like structure rather than a dense hidden body. A 10-kJ store would need ~`92 Wh/L` even before subtracting void volume. Possible in abstract chemistry, but weakly supported structurally.

### 5.5 Rotor coating — **poor bulk-reservoir fit**

The M2 rotor is transparent PMMA with floating copper-wire sectors. A thick chemically active coating sufficient for meaningful energy storage should generally alter mass, appearance, dielectric behaviour or surface chemistry and would need direct evidence.

Thin electret/oxide/adsorbate layers remain legitimate **bias and charge-memory** variables, but not a credible high-energy bulk reservoir without new measurements.

### 5.6 M2 base — **do not import the large-family active-base story**

The M2 CAD base has substantial gross volume, but there is no M2-specific source evidence for an active layered base. The H005 foundation-plate lead belongs to a large-family retrospective line and must not be transferred into M2.

---

## 6. Candidate-location ranking — M6 / large family

### 6.1 Foundation/base stack — **highest-value overlooked reservoir lead**

H005 reports, at low-medium confidence, a thick wooden foundation plate allegedly containing alternating perforated conductive and insulating plates.

If true, this is important because it is structurally similar to several conventional device classes:

- multilayer capacitive stacks;
- distributed electrochemical/dry-pile structures;
- large-area contact-potential / surface-redox arrays;
- hidden return/electrode infrastructure.

The current M6 CAD base working envelope is ~`7.24 L`. On pure volume grounds:

- 10 kJ requires only `0.384 Wh/L`;
- 150 Wh requires `20.7 Wh/L`;
- 1.5 kWh requires `207 Wh/L`.

That makes the base the **best physical place to test a finite conventional reservoir in the large-family hypothesis space**, not because H005 proves one, but because it combines:

1. a source lead for actual conductive/insulating layering;
2. large hidden/interior area;
3. enough volume for substantial finite energy;
4. a natural capacitive/galvanic route into the rest of the machine.

This deserves a dedicated `ACTIVE_BASE vs INERT_BASE` experiment in large-family replicas.

### 6.2 Two large cylinders — **best directly observed large-volume electrical subsystem**

The pair occupies ~`7.87 L` gross envelope in the current reconstruction. Hauser's direct line says the cylinders contain three grids, acrylic separators, a central magnet tube and bifilar winding.

This is substantial distributed surface area and a plausible location for:

- slow interfacial charge generation;
- bias storage;
- impedance transformation;
- resonant/inductive conditioning;
- field-controlled ionic/corona processes.

A chemical bulk reservoir is **not directly observed**, but on volume grounds the cylinders could contain enough ordinary finite matter energy to cover even long demonstrations if hidden active material existed.

Because Hauser actually describes their internals in some detail without mentioning a conventional battery/electrolyte, the historical probability of a hidden dense chemical store should be considered lower than the raw volume calculation suggests.

### 6.3 Large capacitor cans / 20-layer family — **buffer candidate, but ordinary field energy remains far too small for 10 kJ**

The current M6 two-can external envelope is ~`0.813 L`. Holzherr separately reports ~20 perforated-sheet layers in large capacitors, but M6a and M6b must not be silently merged.

Even an intentionally absurd upper-bound calculation is revealing. Suppose **every cubic millimetre of both can envelopes** were a perfect linear dielectric with `er=3` and sustained a uniform `100 MV/m`. Then ideal stored field energy would be only about:

**`108 J`**.

At `30 MV/m`, it would be only about:

**`9.7 J`**.

Both are far below `10,000 J`.

A more geometry-like favourable example with 20 full Ø78-mm sheets, 19 parallel gaps, `er=3`, and 1-mm spacing gives only about `2.41 nF`; limiting the example to `30 MV/m` across each 1-mm gap gives only ~`1.09 J`.

These are illustrative bounds, not safe HV operating instructions or historical ratings.

**Conclusion:** the large capacitors may be important DC buffers / timing elements, but they are not credible as the sole 10-kJ field-energy reservoir under ordinary dielectric physics.

### 6.4 Top crystal/rectifier module — **routing/gate first**

Its direct/near-direct evidence points toward crystal/nonlinear/rectifying function. Nothing in the current corpus makes it the strongest bulk-source site.

### 6.5 Horseshoe magnets / timing hardware — **control, not sustained reservoir**

Permanent magnets can store finite magnetic free energy and can demagnetize, but a steady cyclic machine cannot repeatedly extract net work from an unchanged permanent magnet without paying the state-reset cost. Current sources fit regulation/timing/bias roles better than bulk sustained power.

---

## 7. New architecture suggested by the siting analysis

The strongest conventional large-family architecture now becomes:

`distributed active base OR large-cylinder matter/interface reservoir`

`-> low-average real-power charge regeneration`

`-> grid/cylinder electrostatic + inductive conditioning`

`-> top crystal / nonlinear phase gate`

`-> capacitor bus / field reservoirs`

`-> rotor/stator electromechanical conversion`

`-> occasional short load burst`.

This is **not** a recovered historical schematic. It is a falsifiable architecture that better matches the physical siting problem than asking a tiny `crystal` or pF-scale capacitor to be the energy source.

---

## 8. Decisive experiments

### M2

Highest-value low-energy discriminator:

- identical pot geometry;
- inert clean Cu/grid surfaces versus controlled oxide/dissimilar-metal/interface variants;
- fixed RH and gas composition;
- measure open-circuit potential, source resistance, recharge curve and chemical/mass changes;
- crystal module held identical.

### M6

Highest-value discriminator:

**replace the entire base function while preserving mechanics.**

Compare:

1. electrically inert insulating structural base;
2. conductive but chemically inert replicated layer stack;
3. controlled alternating dissimilar-metal / dielectric test stack;
4. original-style unknown/open-node emulation.

Measure all base-to-machine currents and displacement currents. If the machine behaviour is unchanged when the base is electrically isolated and structurally replicated, the active-base hypothesis weakens sharply.

The second experiment is to instrument each large cylinder as a four-terminal/multiport network and determine whether it delivers **net real energy** over repeated charge/discharge cycles or only routes energy supplied elsewhere.

---

## 9. Working conclusion

V4.32 changes the search priority.

### M2

The most defensible local reservoir test remains the **side-pot grid / dielectric / copper-spiral interface**, but only as a slow surface/matter-energy hypothesis. The `crystal` remains a better candidate for gating than for bulk energy.

### M6 / large family

The **foundation/base stack is now the highest-value overlooked finite-reservoir lead**, because a low-confidence source actually mentions alternating conductive/insulating layers there and the physical volume is large enough to contain conventional finite energy on the historical demonstration scale.

The **large cylinders** are the second-highest priority because they combine direct evidence, large volume and extensive distributed conductive/dielectric interfaces.

The visible large capacitors remain important buffers but ordinary electrostatic field energy is too small by orders of magnitude to explain a 10-kJ episode.

Nothing here proves chemistry, an active base, hidden storage or anomalous energy. The bulk source remains:

**UNKNOWN**.
