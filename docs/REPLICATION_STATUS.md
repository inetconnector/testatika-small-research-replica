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

## Current implementation milestone — V4 best-evidence M2

The repository now has a dedicated source-reproducible build family for the **current best-supported M2 physical reconstruction**:

- generator: `cad/generate_v4_best_evidence_m2.py`;
- canonical build definition: `docs/research/v4-best-evidence-m2.md`;
- BOM: `docs/research/v4-bom.md`;
- assembly: `docs/research/v4-assembly.md`;
- electrical evidence boundary: `docs/research/v4-electrical-boundary.md`;
- printing/fabrication guidance: `docs/research/v4-printing.md`;
- generated CAD: `hardware/experimental/v4-best-evidence-m2/`;
- deterministic ZIP: `release/experimental/testatika-m2-v4-best-evidence-build-package.zip`.

V4 fixes the following as the **preferred build baseline** because newer primary/source-audit evidence now supports them better than the older generic V2/V3 construction choices:

1. nominal 24 individually **floating** Cu-wire sectors, with 20/25 retained as count variants;
2. **no galvanic neighbour ring** in the M2 baseline;
3. conservative R0 routing as the least-speculative nominal physical build, with R4 explicitly separated as research;
4. **two external functional terminals per side pot**;
5. no Tesla/HF pot interpretation in the M2 baseline;
6. no built-in conventional drive motor in the historical baseline;
7. video-refined physical hub arcs, layered outer panels and lower central cage/prism;
8. Crystal retained as a reversible Blackbox rather than a solved circuit;
9. real-magnet positions plus geometry-matched nonmagnetic controls.

This closes **implementation** gaps — it does not close the remaining **historical evidence** gaps listed below.

## M2 first-small-machine completeness matrix

| Subsystem / property | Current best value | Status | Confidence | Repository implementation | What would close the gap |
|---|---|---|---|---|---|
| machine identity | first small machine, right side of Marinov figs. 13/14 | SOURCE-STATED | high | V2/V3/V4 | lock all Hauser/Marinov photo references to exact M2/M3 objects |
| moving visual source | `testabig.jpg` assembly visually matches `meth4.asf`; archive metadata calls video `smaller 300 Watts machine` | OBSERVED + archive metadata | high for same object; low for output rating | V3/V4 use both still and moving source | original film provenance / Methernitha catalogue |
| rotor count | one rotating disc | SOURCE-STATED/OBSERVED | high | V2/V3/V4 | none material |
| rotor diameter | ~200 mm | SOURCE-STATED | high | 200 mm baseline in V2/V3/V4 | original measured drawing/object |
| rotor thickness | ~3.5–4 mm working value | PHOTO-DERIVED | medium-low | V2/V3/V4 working value | calibrated side view/object |
| sector count | ~20–25, broader earlier range 20–30 | SOURCE-STATED | medium-high | 20/24/25 variants; V4 nominal 24 | high-resolution count / direct record |
| sector conductor | ~1 mm copper wire in Marinov publication | SOURCE-STATED | high for Marinov wording | real wire required | material analysis/original close-up |
| sector electrical interconnection | Marinov scan says wires on described small disk are `connected to nothing` | SOURCE-STATED | high for described small machine; exact M2/M3 photo assignment not fully locked | **floating individual wires are V4 M2 baseline**; no neighbour ring | exact photo/correspondence object identification or continuity measurement |
| late 1-kΩ neighbour-ring claim | secondary Frolov compilation | CONFLICT/HYPOTHESIS | low and conflicts with stronger small-machine primary statement | never M2 baseline; optional explicitly secondary control rotor only | original earlier machine-specific source |
| alternate conductor report | iron wire in Watson recollection | CONFLICT/H2 | low-medium | material A/B experiments | primary Marinov correspondence tying material to exact machine |
| through-disc routing | important, exact route unknown | SOURCE-STATED + UNKNOWN | high for importance | R0–R4 reversible families; V4 nominal R0, separate R4 build | original close-up / construction note |
| R4 three-side-change weave | reported by Holzherr for several machines | SOURCE-STATED, model assignment unknown | medium-high | optional R4 rotor and V4 R4 complete research assembly | proof specifically tying R4 to M2 |
| rubbing brushes | absent | SOURCE-STATED | very high | non-contact architecture | none material |
| conventional drive motor | Marinov says no motor in the described small machine | SOURCE-STATED | high for described small machine | V4 has no built-in historical drive motor; removable lab drive only | exact M2/M3 scan-object lock |
| stationary electrode count | unresolved | UNKNOWN | low | adjustable/modular research carriers | original side/front photographs or notes |
| electrode positions/angles | partly photo/video-derived | PHOTO-DERIVED | medium | V3/V4 external geometry; experimental inserts remain adjustable | calibrated multi-view imagery/object |
| hub copper-coloured arcs | two symmetric C/arcuate pieces visible in still; moving highlights in `meth4` support raised parts | OBSERVED/VIDEO-DERIVED | medium-high for physical geometry; low for electrical role | explicit V4 geometry + conductive/dummy/absent A/B plan | side macro / continuity / material record |
| outer panel layering | coarse light perforated carrier + dark fine inset + reddish elongated element + leads | OBSERVED/VIDEO-DERIVED | high for visible layering; material partly unknown | layered V4 panel geometry + interchangeable active materials | macro/material record |
| lower central module | moving footage favours perforated cage/prismatic form with end regions over plain solid cylinder | VIDEO-DERIVED | medium | V4 lower central cage geometry | higher-resolution side/rear footage |
| side pots present | yes, two | OBSERVED | high | V2/V3/V4 | none material |
| pot external leads | Marinov scan says two wires visibly go to each condenser | SOURCE-STATED | high for observed interface | **V4 two-terminal lid / historical mode** | exact terminal tracing |
| pot outer conductive grid | directly described by Marinov correspondence | SOURCE-STATED | high | real grid on former | close-up/material record |
| pot dielectric | cylindrical plastic insulation; PMMA/acrylic-like working material | SOURCE-STATED/DERIVED | medium-high | real PMMA recommended | material record |
| pot inner electrode | central copper spiral/helix | SOURCE-STATED | high | mandrel + real copper | exact turns/pitch/diameter source |
| pot capacitance | unknown | UNKNOWN | — | measure experimentally | original component measurement |
| pot exact internal wiring/polarity | unknown despite two-lead external form | UNKNOWN | — | V4 two-terminal historical mode + reversible internal research variants | original schematic/continuity map |
| large-machine cylinder equivalence to M2 pots | Hauser describes 3 grid tubes + acrylic + magnet tube + bifilar winding on M6a | CONFLICT / DIFFERENT MACHINE | high that M6a differs materially | explicitly segregated from M2/V4 pot baseline | direct proof that a specific M2 pot shared internals |
| horseshoe magnets | visible/source-supported on first small machine | SOURCE-STATED/OBSERVED | high | V4 real-magnet positions + matched dummy | dimensional/material close-up |
| magnet function | unknown | UNKNOWN | — | isolated A/B tests | original explanation/field measurement |
| magnet presence across small variants | direct Marinov scan distinguishes a no-magnet small machine from another with magnets | CONFLICT resolved as model-specific | high for model dependence | never generalize M2↔M3 | exact image mapping |
| upper “crystal” component | Baumann→Marinov term directly preserved in correspondence | SOURCE-STATED | high for term / low for function | V4 exchangeable black-box carrier | original part / schematic / material analysis |
| `crystal` vs institutional rectifying diode | Marinov says Baumann used `crystal`, not `rectifier`; Methernitha separately describes a rectifying diode | SOURCE CONVERGENCE + NON-IDENTITY | high for wording distinction | test related nonlinear functions but do not identify them as one proven part | authentic schematic/part tracing |
| crystal electrical behavior | unknown | UNKNOWN | — | diode/resistor/open/short/crystal surrogate matrix | original I-V/component analysis |
| four-terminal top-module precedent | Holzherr remembered an early/original-model rough coil around one central wire with four leads | SOURCE-STATED, different/uncertain small-model assignment | medium | V4 carrier supports isolated research positions while nominal visible build uses inner pair | source tying exact topology to M2 or original part |
| Tesla/HF core in M2 | Marinov directly rejects Tesla coils / AC and says spirals are condenser electrodes | SOURCE-STATED interpretation | high as Marinov's direct conclusion | absent from V4 M2 baseline | contrary primary evidence |
| black inset grids / dark parts | visible on photo/video; material unresolved | OBSERVED + UNKNOWN | medium-high geometry / low material | V4 layered geometry + interchangeable inserts | calibrated color/material close-up |
| black Plexiglas precedent | Cathomen identifies at least one black part as black Plexiglas on a workshop machine | SOURCE-STATED, model-specific | medium-high | retained as counter-hypothesis | proof for M2 part identity |
| hidden thin layers in transparent stacks | Holzherr observed that thin layers between Plexiglas can be visually hard to detect because of internal reflection | SOURCE-STATED optical caution | medium-high | photo-analysis caveat; reversible hidden-layer tests only | multi-angle close-up / original section |
| PMMA pre-conditioning/electret state | not historically established for M2; secondary Potter/Kelly/Hartmann-like hypothesis | HYPOTHESIS | low for history / high testability | conditioned-vs-neutral PMMA experiment | primary source or material measurement on original |
| rear plate / shield influence | Marinov directly reports that a large metal plate brought behind the running small machine stopped rotation and removed the rest torque | OBSERVED | high for observation / mechanism unknown | shield jig; floating/grounded/R/C/nonconductive controls | original calibrated repetition or independent controlled replication |
| east-west startup orientation | Baumann told Marinov the small-machine axis had to point East-West for startup; Marinov reports it was positioned that way to start, while after startup he directly moved/tilted the running machine without stopping | SOURCE-STATED + OBSERVED | medium-high for startup instruction and post-start observation / cause unknown | randomized turntable startup test + separate post-start reorientation test | original-language scan + blinded controlled replication |
| exact internal circuit | not known | UNKNOWN | — | V4-B0 null topology + named reversible node/topology variants only | authentic schematic or original continuity mapping |
| startup/priming procedure | hand impulse/start reported; exact electrical priming unresolved | SOURCE-STATED + UNKNOWN | medium | low-energy priming tests | original operating protocol |
| dry-air startup push count | Marinov reports about 3–4 finger pushes in dry air and more under humid conditions | SOURCE-STATED/OBSERVED account | medium-high | RH-controlled equal-impulse startup protocol | original-language page + controlled replication |
| restart history / memory | Marinov reports second/third restarts were easier after a metal-plate stop | OBSERVED account | medium | controlled discharge/rest/conditioning matrix with surface-potential logging | independent repetition / original object data |
| small-machine running speed | roughly one revolution per second (~60 rpm) in Marinov account | OBSERVED account | medium-high / model-specific | include ~60 rpm reference without making it universal | calibrated original footage/tachometer record |
| claimed self-rotation | historically reported | SOURCE-STATED claim | observation confidence varies | research target, not release promise | controlled independent replication |
| claimed electrical output | historical estimates/demos and `300 Watts` video metadata only | SOURCE-STATED/metadata claim | low for net-energy conclusion | not a V4 design guarantee | closed long-duration energy balance |
| net energy anomaly | not demonstrated | UNKNOWN / null hypothesis = conservation | high methodological confidence | complete metrology plan | independent closed energy balance |

## Cross-machine constraints reinforced by archive + video + Hauser scans

These facts are valuable but **must not be transferred into M2 without a source bridge**:

- Hauser's 1986 ~500-mm machine uses ~50 chrome-steel sheet lamellae, many non-contact stationary electrodes and materially complex cylindrical modules.
- Hauser's 1988 large-cylinder description gives **three concentric metal grids + acrylic separators + central magnet tube + bifilar copper winding**. This is not the simple M2-pot baseline.
- Holzherr 1999 reports a 50-cm machine running at approximately **15 rpm** during that demonstration; Hauser/Cathomen lines include ~60 rpm on other configurations.
- Holzherr reports multiple approximately **12-cm-disc** small models; these belong to M4/other small variants, not automatically M2.
- Baumann reportedly said large-machine capacitors contained **20 perforated-sheet layers**; this is M6-family evidence, not M2-pot evidence.
- A 12-cm early/original model top subsystem was remembered as a rough coil around a straight central conductor with **four leads**; useful as an experimental top-module topology lead only.
- Several machines reportedly used woven sector wires with three side changes; this strengthens R4 as a research family but does not solve M2 routing.
- `testa01/testa02` contain several workshop machines in one recording; side/rear geometry must be timestamp/object matched before any transfer.


## Internet source audit 2026-08-17

A broad public-web source audit corrected two M2 evidence rankings and expanded the machine taxonomy. See [`research/internet-source-audit-2026-08-17.md`](research/internet-source-audit-2026-08-17.md) and [`research/internet-source-ledger.tsv`](research/internet-source-ledger.tsv).

Key canonical consequences:

- East-West is now split into **Baumann→Marinov startup instruction** and **Marinov-observed post-start orientation independence**; geomagnetic causation remains unknown.
- The rear-metal-plate stop/rest-torque effect is upgraded to a **direct Marinov observation**.
- dry-air 3–4-push startup, humidity sensitivity, easier later restarts and ~60-rpm small-machine operation are explicitly retained as model/source-specific observations.
- Marinov TWT-VII gives a two-disc thick-grid/thin-sector asymmetry and insulating sector spray, but the exact M6 variant is unresolved; it is not silently injected into Hauser M6a CAD.
- `M6c`, `M8`, `M9` and `M10` are introduced to prevent large-under-construction, 1-m, 2-m and tandem workshop evidence from contaminating M6a/M6b.
- Marinov's own coupled Wimshurst/electrostatic-motor control failed to close energetically; full torque/input/storage accounting remains mandatory.

## What “complete 1:1 research replica” means here

A **complete research replica** contains every source-supported part, all documented dimensions, all known material constraints, reversible implementations of unresolved alternatives, a reproducible build package, and a measurement protocol capable of distinguishing those alternatives.

It does **not** mean that an unknown historical wire, polarity or material is silently guessed and relabelled as original. The new scans have closed several *partial* gaps, especially rotor electrical isolation and external pot lead count, but the following remain intrinsically unresolved historical fields:

1. exact rotor through-disc route;
2. exact stationary electrode count/angles and electrical grouping;
3. complete node-to-node wiring;
4. exact pot dimensions, capacitance, internal polarity and connection topology;
5. crystal material and electrical function;
6. magnet function;
7. exact startup/priming sequence;
8. historical energy source / stored-energy state.

## Replica package target

The repository now provides or preserves the following from one checkout:

- V2 conservative mechanical baseline;
- V3 photo + moving-video interpretation model;
- **V4 best-evidence M2 build family**;
- floating-sector M2 baseline plus clearly separated secondary electrical-topology controls;
- R0–R4 rotor routing family;
- grid-vs-foil fixture;
- shield/environment fixture;
- material-variant plan;
- historically faithful two-lead pot mode;
- four-terminal-or-less top-module research carrier;
- conditioned-vs-neutral PMMA control protocol;
- slow-rpm sweep including the 15-rpm historical large-machine anchor;
- removable/decouplable laboratory rpm drive that is not part of the M2 historical baseline;
- V4 BOM, assembly, printing and electrical-boundary documents;
- source/evidence ledgers;
- experiment schema and raw-data convention;
- generated manifest and hashes;
- deterministic V4 build archive tied to repository content.

Every future claim that a gap is “solved” must update this file with the source locator and evidence class.

### Source-independence hardening from the 1991 IECEC / 1984 witness audit

- Kelly/Bailey 1991 explicitly disclose that they relied on other researchers' documents and a videotape; Kelly geometry remains photo-derived/secondary and does not close M2 dimensions or wiring.
- Two March-1984 large-machine witness texts (`M5`, `M5a`) are strikingly similar and are not counted as independent confirmations until their source relationship is resolved.
- Neither witness lamp/heater demonstrations nor the Kelly/Bailey retelling provide a closed energy balance.

## Internet crawl round 2 provenance guard

The 2026-08-17 Round-2 crawl adds a specific warning for M2 historical reconstruction:

- Don Kelly later self-corrected an early Kelly-derived Testatika depiction that put twin horseshoe magnets/windings close to the twin discs. Therefore a Kelly schematic cannot override direct M2 Marinov/photo/video evidence.
- This does **not** remove the source-supported M2 magnet positions already present in V4; it only prevents an obsolete Kelly placement from being imported as corroboration.
- `Magnets` items from circa 1984?, Aug. 1987 and Dec. 1988 remain separate source objects until original pages prove their relationship.
- No Round-2 source closes the M2 node-to-node circuit, exact through-disc route, pot electrical internals or crystal identity.

Accordingly the V4 physical baseline remains unchanged by Round 2.

## Internet crawl round 3 — M2 source lock

Round 3 provides a stable public page-locatable Marinov author-text mirror for several M2 observations already present in the ledger: dry-air 3–4-push startup, humidity dependence, Baumann→Marinov East–West startup instruction, post-start orientation independence, ~1 rev/s running observation, direct rear-metal-plate stop and easier later restart.

The source is a later German translation of a text marked first-published 1989, so exact translation wording must not outrank an original-language scan if one is acquired later.

Importantly, Marinov also makes clear in the same article that he did not understand/reconstruct the operating principle. His proposed high-V driving bus / lower-V collecting bus remains a **testable interpretation**, not original wiring.

No V4 CAD geometry changes are justified by Round 3.

## Internet crawl round 4 — claim-conflation guard

The crawl explicitly rejects a common secondary-history shortcut: **`Marinov was given a 100-W Testatika in 1997` is not established by the located evidence.** Frolov 2021 makes the strong claim, but the earlier Watson transmission only says Baumann gave Marinov a small machine `to play with` and states that the observations/tests described were made at Linden without quantitative test equipment. The ~100-W figure comes from a rough resistor-heating estimate, not a nameplate/calibrated rating.

Therefore:

- no ownership/permanent-transfer state is inferred for M2 from Watson;
- no `100 W rated M2` field is added;
- the Frolov/Sapogin story remains preserved as a late secondary contradiction lead;
- V4 geometry/electrical baseline remains unchanged.

The Nuetec 1280×720-labelled film is not yet frame-audited and therefore supplies **no new M2 geometry yet**.
