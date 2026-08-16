# Audit of uploaded historical Testatika archive — 2026-08-16

## Scope and preservation rule

This audit covers the user-supplied archive `testatika(2).zip` without redistributing its third-party contents. The repository records provenance, hashes, source relationships and research consequences. Historical files are not silently promoted to primary evidence merely because they occur in the archive.

Archive SHA-256:

`9a78f965651232b986ba38fdc671c5831205641763861b566e457ec423a3c14c`

Archive size: 76,288,768 bytes. Inventory: 189 ZIP entries including historical photographs, HTML/MHT mirrors, reports, DOC/PDF material, image sequences and legacy video files.

## Highest-value archive components

### A1 — Hans Holzherr / Stefan Hartmann 1999 demonstration report

Local archive path:

`HTML_UND_BILDER/report99.htm`

SHA-256:

`17830349b29051b8aac393e0ef19dae885c0a8d28fa55b7454fae282d4bf5d22`

Evidence class: direct witness report transmitted/published through Hartmann; P1 for Holzherr observations, H1/Hartmann for transmission/questions.

Important additions or clarifications:

1. The 50-cm machine ran throughout an approximately 1.5-hour visit.
2. Holzherr reports a 1000-W lamp connected for about 10 s without an obvious brightness decrease.
3. He reports a U-shaped heating element becoming too hot to hold within about one second.
4. He reports an approximately 1-cm arc lasting roughly one second when one output lead was withdrawn.
5. He reports approximately **15 rpm** for that 50-cm demonstration, much slower than older ~50/60 rpm reports.
6. He did not notice an obvious rpm drop during load, while explicitly acknowledging that observers were looking at the load rather than instrumenting rpm.
7. He says the rotation rate was magnetically regulated.
8. He describes multiple small Plexiglas blocks carrying perforated sheet; some have perforated sheet on opposite faces and others have one sheet bent across two adjacent faces.
9. In the separate Principle Experiment, the lower side of the swivel arm had square-hole perforated aluminium while the lower plates used brass wire mesh. Five additional plates were stacked under each moving end plate, with mesh between each pair.
10. The lowest mesh layer was wired to two capacitors connected in parallel.
11. Baumann moved the arm back and forth about ten times; Holzherr reports a measured 60 V DC and an audible discharge after shorting the capacitors.
12. Baumann reportedly said the effect did not occur with solid metal foil replacing wire mesh.
13. Small approximately **12-cm-disc** models were present and could be lifted/examined. This is a separate machine family and must not be conflated with Marinov's ~200-mm M2.
14. The earliest model was reported as the only one whose discs were propelled by an electric motor fed by a capacitor that was continuously recharged.
15. A 12-cm "original model" was reported at about 130 V and was loaded with two small lamps plus an unknown resistor. This is a witness report, not an energy balance.
16. Several machines, including a 1-m model under construction, reportedly used sector wires "woven" through the disc with **three side changes**. This strengthens R4 as a research route but still does not prove R4 for M2.
17. Baumann reportedly said the large capacitors contained **20 layers of perforated sheet**. This applies to the large machine, not Marinov's M2 side pots.
18. Holzherr associated the upper object with Baumann's "crystal diode" comment. On the early/original model he remembered a rough coil around one straight central wire with a total of **four leads**. On the 50-cm machine the structure was much harder to resolve.
19. Holzherr explicitly notes that very thin layers between Plexiglas plates can become almost invisible because of total internal reflection; this is an important caution against declaring hidden layers absent from photographs.
20. Holzherr says Baumann rejected radium chloride as the Testatika energy source.

### A2 — Paul E. Potter / historical reconstruction web package

Representative local paths:

- `HTML_UND_BILDER/index.html`
- `HTML_UND_BILDER/principles.htm`
- `HTML_UND_BILDER/rectifier.htm`
- `HTML_UND_BILDER/electroncasc.htm`
- `HTML_UND_BILDER/orsshoe.htm`
- associated circuit/figure GIFs

Representative SHA-256:

- `index.html`: `7a65a79254ba37fc166eaa35762e7898279cb4352e40f9947677d9d3365e6163`
- `principles.htm`: `a3108d01e87d175bd51c42e03c8a61494665407ef078b766c735274f1bef7cfc`
- `rectifier.htm`: `3bffee7bf28197700999b2bf4fb83d45c2f48646f70a3fe1aa49f3d91eae0d37`

Evidence class: S2/I1 reconstruction/hypothesis unless an embedded statement is independently traced to a direct source.

Useful ideas to preserve as experiments, not historical facts:

- variable-capacitance framing for non-contact pickup;
- electret/long-lived dielectric surface-charge state as a possible experimental variable;
- perforated-grid versus foil geometry as a field/corona/charge-transport variable;
- phase-selective rectification / oscillatory charge conditioning;
- explicit interest in electrostatic motors and variable-capacitance machines as conventional comparison systems;
- output pulse-forming / impedance-conditioning networks as a downstream comparison hypothesis.

Claims not promoted into the historical baseline:

- electron-cascade energy extraction from ambient air;
- special plasma bridge as the proven Testatika mechanism;
- Potter's inferred vacuum-tube/rectifier identities;
- Tesla-coil interpretation of side cans;
- paramagnetic-doped dielectric blocks as original components;
- assertions of environmental energy gain.

### A3 — anonymous/later replication-claim documents

Examples:

- `Testatika - Replication Claim of the Swiss ML.doc`
- `testatika1.doc`
- `swiss Testakica free energy device.mht`

The large replication-claim DOC has SHA-256:

`72d3ca4720de5ac604c3e535aa814c19b4584b87318eaa1270e3f9ad457410b3`

Evidence class: S2/I1 or lower until authorship and original provenance are independently established.

Potentially testable ideas include dielectric pre-conditioning, material dependence and deliberately asymmetric electrode geometry. These remain research variants only.

### A4 — historical photographs and video corpus

The archive includes high-resolution or legacy images such as `testabig.jpg`, `TESTA7.jpg`, `TESTA9.jpg`, Hauser image sets and older ASF/RAM/WMV media. These are valuable for future source-preserving photogrammetry and frame extraction.

Do not infer scale or hidden circuit topology from one frontal image alone. Image provenance should be tied to machine IDs before geometry is promoted to the baseline.

## New source-conflict controls created by this archive

1. **12 cm vs 20 cm small machine** — these are not automatically the same object. Marinov M2 remains ~200 mm; Holzherr's 12-cm models need separate IDs until photo/report identity is resolved.
2. **15 rpm vs 50/60 rpm** — speed is strongly machine/demo-specific. The experiment plan should sweep slow rotational regimes rather than hard-code 60 rpm.
3. **four-lead upper module vs simpler visual interpretations** — the crystal/top subsystem must support a four-terminal research carrier while keeping actual historical topology unknown.
4. **20-layer large capacitor vs M2 small pots** — never import the 20-layer structure into M2 merely because both are called capacitors/pots.
5. **hidden thin layers** — photograph-based absence claims must account for optical invisibility between transparent plates.

## Research consequences

The archive materially improves the repository by adding:

- a slow-rpm experimental anchor around 15 rpm for the 50-cm family;
- a stronger reason to measure rpm/load reaction with instrumentation rather than observation;
- a model-specific 20-layer perforated-capacitor lead;
- a four-terminal top-module possibility;
- better Principle Experiment geometry/material detail;
- an optical caveat for hidden interfaces;
- a separate 12-cm small-machine family requiring taxonomy work;
- a richer but explicitly secondary Potter hypothesis catalogue.

No archive item closes the M2 exact circuit, crystal material/function, exact pot topology or exact M2 through-disc routing.