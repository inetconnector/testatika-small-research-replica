# M2 replica configuration matrix

## Purpose

This file turns every important unresolved M2 construction detail into a **controlled, reversible configuration** instead of a hidden guess. The aim is one mechanical research platform that can cover the full evidence-compatible variant space without rebuilding the entire machine for every hypothesis.

## Baseline mechanical configuration

| Parameter | Baseline | Alternatives retained | Why |
|---|---|---|---|
| rotor diameter | 200 mm | none unless new primary scale evidence | strongest Marinov anchor |
| rotor sector count | 24 | 20 / 25 | source range |
| rotor conductor | ~1 mm Cu wire | Fe / stainless / Fe-Ni research coupons/rotors | Marinov baseline + later conflict/material hypotheses |
| rotor route | R0 as simplest setup reference | R1 / R2 / R3 / R4 | exact original route unknown |
| rotor substrate | 3–4 mm PMMA recommended | printable template for drilling/routing | planarity + historical material class |
| rubbing collection | none | none in M2 baseline | strongly source-supported |
| electrode carriers | adjustable | geometry/material inserts interchangeable | positions and grouping unresolved |
| side pots | two | internal connection variants | externally source-supported, internal topology unknown |
| horseshoe magnets | installed for first-machine visual baseline | remove/bypass for A/B | presence strong, function unknown |
| crystal module | electrically isolated exchangeable carrier | open / short / R / diode / antiparallel / crystal detector surrogate | function unknown |
| rear shield | absent baseline | floating / grounded / R-ground / C-ground | later shield claim test |

## Rotor routing set

Each route should use the same outer diameter, hub, conductor diameter and electrode environment.

- **R0:** one-side radial reference.
- **R1:** front radial → outer crossover → rear return.
- **R2:** sector-by-sector alternating face.
- **R3:** angularly offset through-disc path.
- **R4:** three side changes at nominal radii 40/60/80 mm between 27 and 94 mm anchors.

R4 is mandatory in the **research variant set**, not mandatory as the declared historical original.

## Rotor material set

The research package should permit geometrically identical conductor comparisons:

1. copper;
2. soft iron/low-carbon steel;
3. stainless steel;
4. Fe-Ni candidate where safely/legally obtainable and composition documented.

For each material record DC resistance, diameter, surface finish and magnetic response/remanence. Material must not be changed simultaneously with route geometry during comparison.

## Electrode insert set

Keep outer carrier, active window, angle and gap fixed while changing only the active insert:

1. solid metal foil;
2. square perforated sheet;
3. round perforated sheet;
4. fine brass/copper/steel mesh;
5. dark insulating backing control;
6. blackened conductive mesh only as an explicit material/finish experiment.

No black appearance is treated as proof of carbon, graphite, oxide or nanostructure.

## Side-pot configuration set

Each pot should expose independent terminals for:

- outer grid;
- inner copper spiral;
- any added guard/shield only if explicitly experimental.

Minimum reversible topology matrix:

- outer grid active / spiral floating;
- spiral active / outer grid floating;
- opposite-polarity outer/inner coupling;
- high-value resistive leakage coupling;
- diode-gated coupling;
- both disconnected for electrostatic-field control.

Before coupled-machine tests measure actual capacitance, leakage, dielectric loss and relaxation for each physical pot.

## Crystal black-box set

The historical material/function is unknown. The module should therefore be a removable four-terminal-or-less carrier capable of safely accepting low-energy surrogates:

- open circuit;
- short/bus;
- high-value resistor;
- silicon diode;
- suitable HV diode at controlled low stored energy;
- antiparallel diode pair;
- historical-style crystal detector where safe;
- purely capacitive coupling control.

Each surrogate must be labelled **experimental**, never “original crystal”.

## Magnet matrix

For the first small machine geometry:

- physical magnet-shaped position occupied with real documented horseshoe magnets for the source-supported presence test;
- same geometry with nonmagnetic dummy;
- magnet present but electrically isolated from nearby structures;
- orientation reversed where safe;
- field strength mapped before and after trials.

This isolates magnetic presence from hidden geometry changes.

## Environmental / shield matrix

Record or control:

- relative humidity;
- temperature;
- air pressure;
- 3-axis magnetic field;
- nearby mains/electric field where relevant;
- rear-plate distance and electrical state;
- whole-machine orientation for the low-confidence east-west hypothesis.

## Node/topology matrix

The V3 node families N-L, N-R and N-C are **working labels**, not historical labels. Wiring trials must be represented by named configuration IDs, for example:

- `M2-T1-R4-CU-MESH-XOPEN-MAG`
- `M2-T1-R4-CU-FOIL-XDIODE-MAG`
- `M2-T2-R1-FE-MESH-XR-MAG0`

Recommended ID fields:

`machine-topology-route-material-electrode-crystal-magnet-shield`

Every dataset must record the exact configuration ID and repository commit.

## Completion criterion

The mechanical/electrical **research platform** is complete when every configuration above can be selected without irreversible reconstruction and the experiment plan can compare configurations one variable at a time.

Historical 1:1 certainty remains bounded by `docs/REPLICATION_STATUS.md`: configuration coverage can be complete even while the unknown historical choice among configurations remains unresolved.