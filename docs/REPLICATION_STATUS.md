# Replication completeness ledger

## Purpose

This file is the canonical answer to the question: **How close is this repository to a 1:1 historical replica of the first small Marinov Testatika (M2)?**

The project never fills an evidentiary gap by invention. A historically unknown detail is represented as an explicit unknown plus one or more reversible test variants. This makes the research package as complete as the surviving evidence permits while preserving a strict boundary between historical reconstruction and experimental interpretation.

## Status vocabulary

- **OBSERVED** — directly visible in a source of adequate provenance.
- **SOURCE-STATED** — stated by a direct/near-direct source but not independently measured.
- **PHOTO-DERIVED** — estimated from imagery; uncertainty must be retained.
- **DERIVED** — engineering consequence of better-supported observations.
- **HYPOTHESIS** — testable reconstruction choice, not claimed original.
- **UNKNOWN** — no reliable evidence currently fixes the value/function.
- **CONFLICT** — reliable sources disagree or likely refer to different variants.

## M2 first-small-machine completeness matrix

| Subsystem / property | Current best value | Status | Confidence | Repository implementation | What would close the gap |
|---|---|---|---|---|---|
| machine identity | first small machine, right side of Marinov figs. 13/14 | SOURCE-STATED | high | V2/V3 | better original figure provenance |
| rotor count | one rotating disc | SOURCE-STATED/OBSERVED | high | V2/V3 | none material |
| rotor diameter | ~200 mm | SOURCE-STATED | high | 200 mm baseline | original measured drawing/object |
| rotor thickness | ~3.5–4 mm working value | PHOTO-DERIVED | medium-low | V2/V3 variants | calibrated side view/object |
| sector count | ~20–25, broader earlier range 20–30 | SOURCE-STATED | medium-high | 20/24/25 variants | high-resolution count / direct record |
| sector conductor | ~1 mm copper wire in Marinov publication | SOURCE-STATED | high for Marinov wording | real wire required | material analysis/original close-up |
| alternate conductor report | iron wire in Watson recollection | CONFLICT/H2 | low-medium | material A/B experiments | primary Marinov correspondence |
| through-disc routing | important, exact route unknown | SOURCE-STATED + UNKNOWN | high for importance | R0–R4 reversible families | original close-up / construction note |
| R4 three-side-change weave | reported by Holzherr for several machines | SOURCE-STATED, model assignment unknown | medium-high | optional R4 rotor | proof specifically tying R4 to M2 |
| rubbing brushes | absent | SOURCE-STATED | very high | non-contact architecture | none material |
| stationary electrode count | unresolved | UNKNOWN | low | adjustable modular carriers | original side/front photographs or notes |
| electrode positions/angles | partly photo-derived | PHOTO-DERIVED | medium-low | adjustable | calibrated multi-view photos |
| side pots present | yes, two | OBSERVED | high | V2/V3 | none material |
| pot outer conductive grid | reported | SOURCE-STATED | high | real grid on former | close-up/material record |
| pot dielectric | plastic/acrylic-like insulating cylinder | SOURCE-STATED/DERIVED | medium-high | real PMMA recommended | material record |
| pot inner electrode | thick copper spiral/helix | SOURCE-STATED | high | mandrel + real copper | exact turns/pitch/diameter source |
| pot capacitance | unknown | UNKNOWN | — | measure experimentally | original component measurement |
| pot exact wiring | unknown | UNKNOWN | — | separate terminals / reversible topology | original schematic/continuity map |
| horseshoe magnets | visible on first small machine | SOURCE-STATED/OBSERVED | high | mounts + real magnet option | dimensional/material close-up |
| magnet function | unknown | UNKNOWN | — | isolated A/B tests | original explanation/field measurement |
| upper “crystal” component | term reported; function unresolved | SOURCE-STATED | medium-high term / low function | exchangeable black-box carrier | original part / schematic / material analysis |
| crystal electrical behavior | unknown | UNKNOWN | — | diode/resistor/open/short/crystal surrogate matrix | original I-V/component analysis |
| black inset grids / dark parts | visible on photo; material unresolved | OBSERVED + UNKNOWN | medium | V3 visual interpretation | calibrated color/material close-up |
| black Plexiglas precedent | Cathomen identifies at least one black part as black Plexiglas on a workshop machine | SOURCE-STATED, model-specific | medium-high | retained as counter-hypothesis | proof for M2 part identity |
| rear plate / shield influence | metal-plate stop effect only through later transmission | HYPOTHESIS/H2 | low-medium | shield jig | primary source or controlled replication |
| east-west orientation | later recollection | HYPOTHESIS/H2 | low | turntable experiment only | primary source + blinded replication |
| exact internal circuit | not known | UNKNOWN | — | node families + reversible topologies only | authentic schematic or original continuity mapping |
| startup/priming procedure | hand impulse/start reported; exact electrical priming unresolved | SOURCE-STATED + UNKNOWN | medium | low-energy priming tests | original operating protocol |
| claimed self-rotation | historically reported | SOURCE-STATED claim | observation confidence varies | research target, not release promise | controlled independent replication |
| claimed electrical output | historical estimates/demos only | SOURCE-STATED claim | low for net-energy conclusion | not a design guarantee | closed long-duration energy balance |
| net energy anomaly | not demonstrated | UNKNOWN / null hypothesis = conservation | high methodological confidence | complete metrology plan | independent closed energy balance |

## What “complete 1:1 research replica” means here

A **complete research replica** contains every source-supported part, all documented dimensions, all known material constraints, reversible implementations of unresolved alternatives, a reproducible build package, and a measurement protocol capable of distinguishing those alternatives.

It does **not** mean that an unknown historical wire, polarity or material is silently guessed and relabelled as original. Until new primary evidence appears, the following remain intrinsically unresolved historical fields:

1. exact rotor through-disc route;
2. exact stationary electrode count/angles and electrical grouping;
3. complete node-to-node wiring;
4. exact pot dimensions, capacitance and connection topology;
5. crystal material and function;
6. magnet function;
7. exact startup/priming sequence;
8. historical energy source / stored-energy state.

## Replica package target

The repository should make the following reproducible from one checkout:

- V2 conservative mechanical baseline;
- V3 photo-interpretation model;
- R0–R4 rotor test family;
- grid-vs-foil fixture;
- shield/environment fixture;
- material-variant plan;
- BOM and assembly sequence;
- source/evidence ledger;
- experiment schema and raw-data convention;
- generated manifest and hashes;
- release archive tied to one commit.

Every future claim that a gap is “solved” must update this file with the source locator and evidence class.