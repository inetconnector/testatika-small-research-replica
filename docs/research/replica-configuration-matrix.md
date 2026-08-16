# M2 replica configuration matrix

## Purpose

This file turns every important unresolved M2 construction detail into a **controlled, reversible configuration** instead of a hidden guess. The aim is one mechanical research platform that can cover the full evidence-compatible variant space without rebuilding the entire machine for every hypothesis.

New primary Marinov correspondence narrows the baseline in two important places: the described small-machine rotor wires are stated to be **electrically unconnected**, and the visible side condensers have a **two-wire external interface**. Those now outrank later secondary reconstructions.

## Baseline mechanical / electrical configuration

| Parameter | Baseline | Alternatives retained | Why |
|---|---|---|---|
| rotor diameter | 200 mm | none unless new primary scale evidence | strongest Marinov anchor |
| rotor sector count | 24 | 20 / 25 | source range |
| rotor conductor | ~1 mm Cu wire | Fe / stainless / Fe-Ni research coupons/rotors | Marinov baseline + later conflict/material hypotheses |
| rotor electrical topology | **each sector floating / no galvanic neighbour ring** | explicitly secondary resistor-ring control only | direct Marinov scan says small-machine disk wires are `connected to nothing` |
| rotor route | R0 as simplest setup reference | R1 / R2 / R3 / R4 | exact through-disc route remains unknown |
| rotor substrate | 3–4 mm PMMA recommended | printable template for drilling/routing | planarity + historical material class |
| rotor dielectric state | untreated/neutral reference | documented pre-conditioned / neutralized / orientation controls | secondary electret lead; not historical baseline |
| rubbing collection | none | none in M2 baseline | strongly source-supported |
| conventional drive motor | none | removable/decouplable external laboratory rpm drive | Marinov says no motor in described small machine; lab drive is instrumentation only |
| electrode carriers | adjustable | geometry/material inserts interchangeable | positions and grouping unresolved |
| side pots | two, historically presented as two-terminal devices | internal connection research variants behind isolated test access | Marinov scan says two wires visibly go to each condenser |
| horseshoe magnets | installed for first-machine visual baseline | remove/bypass for A/B | presence source-supported for one first-machine line, not universal |
| hub arcs | two symmetric copper-coloured arcuate physical candidates | removable nonconductive dummy / isolated conductive arc | `meth4` moving highlights strengthen physical-part interpretation; electrical role unknown |
| crystal module | electrically isolated four-terminal-or-less exchangeable carrier | open / short / R / C / diode / antiparallel / crystal detector / coupled two-port surrogate | function unknown; four-lead precedent exists on another early small model |
| rear shield | absent baseline | floating / grounded / R-ground / C-ground | later shield claim test |

## Rotor electrical topology set

### E0 — historical small-machine baseline: isolated sectors

Each routed wire is electrically floating and **not galvanically connected to neighbouring wires**.

Basis: direct Marinov correspondence scan `SMwebL1.jpg` says the wires on the described small-machine disk are `connected to nothing`.

Implementation rules:

- no collector ring;
- no slip ring;
- no common hub bus;
- no neighbour resistor network;
- wire ends may be mechanically anchored but electrically insulated from each other and the shaft;
- continuity test every finished rotor and record pairwise isolation before use.

### E1 — secondary 1-kΩ neighbour-ring control

A late Frolov compilation attributes ~1-kΩ neighbour connections to Testatika lamellae. This has weak provenance and conflicts with the stronger direct small-machine statement.

Therefore E1 may exist only as a **clearly labelled secondary control rotor**. It must never be named `original`, `baseline` or `M2-authentic` unless an older machine-specific primary source appears.

This separation is important because changing from floating sectors to an RC ring fundamentally changes the capacitance matrix, charge relaxation and induced-current phase.

## Rotor routing set

Each route should use the same outer diameter, hub, conductor diameter, electrical topology E0 and electrode environment unless electrical topology itself is the variable under test.

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

## Hub-arc set

`meth4.asf` close-ups of the same visible assembly as `testabig.jpg` show two symmetric copper-coloured C/arcuate elements around the central hub. Video highlights support the interpretation that these are physical raised parts rather than only painted markings.

The external research geometry should therefore support:

- `H0`: conductive copper/brass arc pair, electrically floating;
- `H1`: same arc pair with independent terminals for measurement only;
- `H2`: nonconductive dimension-matched dummy;
- `H3`: arcs absent, to isolate their field/mechanical effect.

Historical connection is still unknown. **Do not silently wire the arcs to the shaft, rotor sectors, pots or crystal.**

Record arc dimensions, gap between left/right arcs, radial position, material and measured capacitance to shaft/rotor/stators.

## PMMA / dielectric-state set

Secondary Potter/Kelly/Hartmann-like interpretations suggest an electret-like or pre-conditioned dielectric state. This is **not** accepted as an original M2 fact, but it is sufficiently falsifiable to deserve a controlled variant family.

Keep geometry and electrode arrangement identical while comparing:

1. untreated PMMA reference;
2. documented low-energy electrostatic pre-conditioning;
3. neutralized/discharged control after the same handling history;
4. matched samples cut in different sheet/manufacturing directions if provenance permits;
5. optional different transparent dielectric only as a separate material experiment.

For every dielectric-state variant record:

- pre-run surface-potential map;
- conditioning voltage/current/time and total supplied energy;
- delay between conditioning and test;
- RH and temperature;
- post-run surface-potential map;
- charge-decay curve.

No apparent persistence may be called an energy source without complete accounting of conditioning and stored electrostatic energy.

## Electrode insert / outer-panel set

`meth4` shows the small machine outer panel as a visibly layered assembly, not one flat perforated plate. Keep outer carrier, active window, angle and gap fixed while separating visible layers:

1. coarse light perforated structural carrier;
2. fine/dark inset grid;
3. elongated reddish conductor/frame/comb element along the inset;
4. external lead attachment;
5. optional insulating backing/control layer.

Material variants for the active insert:

- solid metal foil;
- square perforated sheet;
- round perforated sheet;
- fine brass/copper/steel mesh;
- dark insulating backing control;
- blackened conductive mesh only as an explicit material/finish experiment.

No black appearance is treated as proof of carbon, graphite, oxide or nanostructure.

## Side-pot configuration set

### Historical external interface

Marinov's primary correspondence says two wires are clearly visible going to the right condenser and two to the left condenser. Therefore the historical-facing physical configuration must expose **exactly two functional external terminals per pot**.

The internal source description remains:

- outer cylindrical conductive grid;
- cylindrical plastic/PMMA insulation;
- central copper spiral.

### Laboratory access without corrupting the historical interface

For research, the construction may provide hidden/covered test access to outer grid and inner spiral separately, but:

- extra terminals must be electrically isolatable;
- the normal M2 presentation must reduce to the historical two-wire interface;
- test leads must be removed/disconnected for historical-mode runs;
- guard/shield terminals are experimental and must not appear as source-supported parts.

Minimum reversible internal topology matrix:

- outer grid active / spiral floating;
- spiral active / outer grid floating;
- opposite-polarity outer/inner coupling;
- high-value resistive leakage coupling;
- diode-gated coupling;
- both disconnected for electrostatic-field control.

Before coupled-machine tests measure actual capacitance, leakage, dielectric loss and relaxation for each physical pot.

### Large-machine 20-layer / Hauser-cylinder controls

Holzherr transmits Baumann's statement that **large-machine** capacitors contained 20 layers of perforated sheet. Hauser separately describes a medium/large cylinder with three concentric metal-grid tubes, acrylic separators, a central magnet tube and bifilar copper winding.

These belong to M6-family research and are explicitly **not** the M2 side-pot baseline.

Separate fixtures may test:

- 2/5/10/20 perforated capacitor layers;
- 3-grid concentric cylinder geometry;
- central magnet tube present/absent;
- bifilar winding present/absent.

They must use M6 configuration IDs and must not be substituted into an M2 build while retaining the M2 label.

## Crystal black-box set

The historical M2 material/function is unknown. The module should therefore be a removable **four-terminal-or-less** carrier capable of safely accepting low-energy surrogates.

Source distinction:

- Marinov correspondence: Baumann used the term **`crystal`**, and Marinov explicitly contrasts it with `rectifier` wording;
- Methernitha institutional description: a rectifying diode is described as regulating the attraction/repulsion cycle;
- Hauser large-machine material: top crystals are observed/reconstructed with a possible rectifier interpretation;
- Holzherr remembers a different early small-model top component with four leads.

These lines may be functionally related but are **not one proven component identity**.

Candidate configurations:

- all terminals open;
- short/bus;
- high-value resistor;
- capacitor;
- silicon diode;
- suitable HV diode at controlled low stored energy;
- antiparallel diode pair;
- historical-style crystal detector where safe;
- winding as one isolated two-terminal port + central conductor as second isolated two-terminal port;
- capacitive/R/diode coupling between the two ports;
- central conductor floating / referenced / guarded.

Each surrogate must be labelled **experimental**, never “original crystal”.

## Drive / rpm test fixture

The M2 historical baseline contains **no conventional drive motor** based on Marinov's small-machine description.

A laboratory motor may nevertheless be essential for controlled characterization. It must therefore be designed as **external instrumentation**:

- belt/coupler or clutch can be fully disengaged;
- motor electrical leads physically disconnected during claimed self-rotation trials;
- bearing drag of disconnected coupling characterized;
- rpm/torque measured independently;
- drive input power measured during forced-speed tests;
- configuration ID records `LABDRIVE-ON` or `LABDRIVE-OFF`.

This prevents the experiment fixture from becoming an undocumented energy path.

## Magnet matrix

For the first small machine geometry:

- physical magnet-shaped position occupied with real documented horseshoe magnets for the source-supported presence test;
- same geometry with nonmagnetic dummy;
- magnet present but electrically isolated from nearby structures;
- orientation reversed where safe;
- field strength mapped before and after trials.

A direct Marinov scan also describes another small machine without magnets. This reinforces that magnet presence/function is variant-specific rather than universal.

## Environmental / shield matrix

Record or control:

- relative humidity;
- temperature;
- air pressure;
- 3-axis magnetic field;
- nearby mains/electric field where relevant;
- rear-plate distance and electrical state;
- whole-machine orientation for the low-confidence east-west hypothesis.

## Speed matrix

Do not hard-code a universal Testatika rpm. Source reports are machine-specific: a large/workshop machine is associated with ~60 rpm in Hauser/Cathomen material, while Holzherr reports approximately **15 rpm** during the 1999 50-cm demonstration.

Recommended controlled sweep where mechanically safe:

`5 / 10 / 15 / 20 / 30 / 45 / 60 rpm`

Measure all electrical and torque quantities against rotor phase at every speed.

## Node/topology matrix

The V3 node families N-L, N-R and N-C are **working labels**, not historical labels. Wiring trials must be represented by named configuration IDs, for example:

- `M2-T1-E0-R4-CU-MESH-XOPEN-MAG`
- `M2-T1-E0-R4-CU-FOIL-XDIODE-MAG`
- `M2-T2-E0-R1-FE-MESH-XR-MAG0`
- `M2-T3-E0-R4-CU-MESH-X4PORT-PMMA-COND15`
- `M2-TCTRL-E1-R4-CU-MESH-XOPEN-MAG` — explicitly secondary resistor-ring control.

Recommended ID fields:

`machine-topology-electricalroute-route-material-electrode-crystal-dielectricstate-magnet-shield-speed-drive`

Every dataset must record the exact configuration ID and repository commit.

## Optical hidden-layer rule

Holzherr noted that a thin layer between Plexiglas plates can be difficult to see because of total internal reflection. Therefore a photo showing apparently clear Plexiglas does not prove that no thin conductor/coating/interface exists.

Any hidden-layer candidate remains a reversible **hypothesis** until confirmed by multi-angle imagery, construction records or examination of an original object.

## Completion criterion

The mechanical/electrical **research platform** is complete when every configuration above can be selected without irreversible reconstruction and the experiment plan can compare configurations one variable at a time.

Historical 1:1 certainty remains bounded by `docs/REPLICATION_STATUS.md`: configuration coverage can be complete even while the unknown historical choice among configurations remains unresolved.
