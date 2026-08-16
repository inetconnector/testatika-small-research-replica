# Changelog

## Unreleased — archive + Kelly source expansion

### Added

- `docs/research/archive-audit-2026-08-16.md`: provenance-first audit of the user-supplied historical Testatika archive without redistributing third-party source files.
- `docs/research/archive-source-ledger.tsv`: hash/source/evidence ledger for the highest-value archive items.
- `docs/research/kelly-free-energy-guide-audit-2026-08-16.md`: Testatika-focused audit of Patrick J. Kelly's large *A Practical Guide to 'Free-Energy' Devices* and linked Utkin material.
- Holzherr 1999 source details including the ~15-rpm 50-cm demonstration, 1.5-hour observation window, short load observations, Principle Experiment stack geometry, 12-cm small-machine family, 20-layer large capacitors and four-lead early top-module precedent.
- explicit optical warning that thin layers between transparent Plexiglas plates may be difficult to see and that photographic non-visibility is not proof of absence.
- PMMA pre-conditioning/electret-control experiments, surface-potential mapping and charge-decay measurement.
- expanded slow-rpm sweep and four-terminal top-module experiment matrix.

### Source-control decisions

- Kelly/Potter/Utkin material remains S2/I1 hypothesis/source-discovery material, not Testatika primary evidence.
- 12-cm Holzherr machines are kept distinct from Marinov's ~200-mm M2.
- the 20-layer perforated capacitor statement is assigned to the large-machine family and is not imported into M2 pots.
- the four-lead top-module description is retained as a small-family topology lead, not a solved M2 crystal circuit.
- electret/dielectric conditioning is promoted only to a controlled experiment, not to an asserted historical mechanism or energy source.

## v0.3.0 — 2026-08-16

Integrated research-hardening release covering R4, V3 photo interpretation, Baumann/Methernitha language reconstruction, Hartmann/Overunity provenance, replication-completeness tracking and repository integrity automation.

### Added — replication and provenance

- `docs/REPLICATION_STATUS.md`: canonical M2 completeness ledger distinguishing observed, source-stated, photo-derived, derived, hypothesized, conflicting and unknown details.
- `docs/research/machines.yaml`: canonical machine taxonomy preventing silent property transfer between variants.
- `docs/research/provenance-schema.yaml`: canonical source/provenance fields and evidence-distance vocabulary.
- `docs/repository-hardening-plan-2026-08-16.md`: preservation-first execution and acceptance plan.
- `ADDON.md`: case-safe compatibility entry point; `addon.md` remains the canonical large handoff.
- `docs/research/cad-reproducibility.md`: explicit source-to-binary CAD reproducibility boundary.
- `scripts/rebuild_research_assets.py`: one entry point for all currently source-reproducible CAD families.
- deterministic manifest generation/checking through `scripts/generate_manifest.py` and `scripts/check_manifest.py`.
- automatic manifest refresh workflow.

### Added — R4 / grid-vs-foil research

- `cad/generate_v3_experiments.py`.
- R4 research geometry for 20/24/25-sector rotors.
- explicit three-side-change routing hypothesis from the Holzherr report.
- geometry-controlled mesh-vs-solid-foil A/B electrode fixture.
- 1/2/3-mm gap-gauge generation.
- `docs/research/r4-grid-vs-foil.md` protocol.

R4 remains a high-priority cross-source hypothesis, **not** a claimed known Marinov M2 original.

### Added — V3 photo interpretation

- higher-resolution external geometry reconstruction.
- V3 STEP/STL complete photo-interpretation model.
- annotated photo and functional schematic.
- node-map and provisional connection-plan research ledgers.
- explicit black-material uncertainty and reversible test strategy.

The V3 model remains **experimental/photo-interpreted** even where a convenience alias uses `V3_COMPLETE` in the filename.

### Added — Baumann / Methernitha language reconstruction

- `docs/research/baumann-language-decoding.md`.
- `docs/research/baumann-statements.tsv`.
- source-by-source engineering translation of `Taster`, charge sorting, diode/crystal commutation, grid capacitors and drive/storage concepts.
- prioritized phase-resolved falsification experiments.

### Corrected

- the phrase "like an unknown language" is **not verified as a direct Marinov quotation**.
- the V3 pixel-analysis document no longer derives claims from that unverified attribution.
- black visible parts are not automatically interpreted as carbon, oxide, nanocoating or conductive blackening; Cathomen's black-Plexiglas statement is retained as a model-specific counter-hypothesis.
- stale branch-based preservation wording is replaced by snapshot-tag/Git-history recovery rules.

### Added — Hartmann / Overunity.com V6 source audit

- `docs/research/hartmann-overunity-testatika.md`.
- `docs/research/hartmann-overunity-sources.tsv`.
- `docs/research/hartmann-overunity-cathomen-audit.md`.
- `docs/research/hartmann-overunity-provenance.md`.
- historical Overunity Testatika thread/media provenance (`topic 75`, `testa01.rm`, `testa02.rm`, `meth5.asf`).
- quantitative audit of Hartmann's capacitor-sharing example and air-density statement.
- H36–H42 hypothesis set.

Hartmann's June-2000 electret/influence interpretation is retained as a useful secondary convergence. Atmospheric-ion energy-source, weak-radioactive-mineral and negative-resistance explanations remain unverified hypotheses. No radioactive-material experiments are part of the project.

### Repository engineering

- repository validation expanded beyond simple file existence/STL checks to JSON, TSV, local Markdown references, core V2/V3 assets and known stale-attribution regressions.
- release builder advanced to `v0.3.0` and expanded to include source, documentation, CAD, scripts, manifests and preserved binary research assets.
- `CITATION.cff` advanced to 0.3.0.
- old v0.2.0 release artifacts remain preserved and are not overwritten.

### Current scientific position

The strongest source-compatible working model is electrostatic charge-state management:

> influence / variable capacitance → non-contact pickup → polarity-selective routing → nonlinear crystal/diode commutation → drive/storage buses → cyclic bias regeneration → model-dependent impedance conditioning.

This is a falsifiable engineering model, **not** evidence for net energy creation. A historical 1:1 detail is never declared resolved merely because a plausible reconstruction exists.

## v0.2.0 — 2026-08-16

First publication-ready repository release.

### Added

- first-small-machine photogrammetric V2 reconstruction.
- 20/24/25-wire rotor variants.
- STL and STEP part libraries.
- complete assembled STEP/STL/OBJ/GLB model.
- evidence matrix and source hierarchy.
- rotor wire-routing hypotheses R0–R3.
- first-machine horseshoe-magnet correction.
- experimental shield-plate jig.
- scientific-status and safety documentation.
- initial repository validation workflow.

### Scientific position

No over-unity or free-energy claim is asserted. Unknown historical wiring remains explicitly unknown.