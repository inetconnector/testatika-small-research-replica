# Changelog

## Unreleased — V4 best-evidence build + archive/primary-source expansion

### Added — V4 best-evidence M2 physical-build family

- `cad/generate_v4_best_evidence_m2.py`: self-contained current-build generator integrating the strongest direct M2 electrical constraints with the best photo/video external geometry.
- complete nominal `Testatika_M2_V4_BEST_EVIDENCE.step/.stl` assembly generation.
- complete `Testatika_M2_V4_R4_RESEARCH.step/.stl` routing-control assembly generation.
- 20/24/25 floating-sector R0 rotors, with 24 sectors nominal.
- explicit 24-sector floating R4 research rotor; R4 remains a routing hypothesis rather than claimed M2 original.
- V4 two-terminal pot lid implementing the directly observed two-wire external condenser interface.
- V4 hub-arc, layered outer-panel and lower central cage geometry integrated into the complete assembly.
- V4 Crystal Blackbox carrier: two nominal visible positions plus isolated research positions without asserting a historical four-terminal M2 circuit.
- geometry-matched horseshoe magnet/dummy controls.
- `docs/research/v4-best-evidence-m2.md` canonical current build definition.
- `docs/research/v4-bom.md`, `v4-assembly.md`, `v4-electrical-boundary.md`, `v4-printing.md`.
- `docs/research/v4-configurations.yaml`: machine-readable baseline and one-variable-at-a-time configuration registry.
- `scripts/check_v4_assets.py`: materialized geometry/metadata verifier including 200-mm rotor tolerance and two-terminal pot-lid checks.
- `scripts/build_v4_package.py`: deterministic V4 research/build ZIP + SHA-256.
- `.github/workflows/materialize-v4-best-evidence.yml`: CI generation, verification, packaging, manifest refresh and binary materialization.
- `scripts/rebuild_research_assets.py` now rebuilds V4 as part of the source-reproducible CAD set.

### V4 source-control decisions

- direct Marinov `connected to nothing` outranks the late secondary 1-kΩ neighbour-ring claim: **floating individual sectors are the V4 M2 baseline**.
- direct two-wire condenser observation becomes the historical-facing pot interface.
- R0 is chosen only as the least-speculative nominal physical route; exact historical through-disc routing remains unknown.
- no built-in conventional motor, Tesla/HF pot stage, M6a three-grid/magnet/bifilar cylinder or radioactive-material path is introduced into M2 V4.
- Hub arcs/panel layering/central cage are promoted as geometry candidates from moving-image evidence, while their hidden electrical roles remain unresolved.
- Crystal remains a reversible Blackbox; no diode/crystal surrogate is labelled original.
- V2/V3 and earlier documentation remain preserved as historical/research states rather than being deleted.

### Added — historical archive / Kelly expansion

- `docs/research/archive-audit-2026-08-16.md`: provenance-first audit of the user-supplied historical Testatika archive without redistributing third-party source files.
- `docs/research/archive-source-ledger.tsv`: hash/source/evidence ledger for the highest-value archive items.
- `docs/research/kelly-free-energy-guide-audit-2026-08-16.md`: Testatika-focused audit of Patrick J. Kelly's large *A Practical Guide to 'Free-Energy' Devices* and linked Utkin material.
- Holzherr 1999 source details including the ~15-rpm 50-cm demonstration, 1.5-hour observation window, short load observations, Principle Experiment stack geometry, 12-cm small-machine family, 20-layer large capacitors and four-lead early top-module precedent.
- explicit optical warning that thin layers between transparent Plexiglas plates may be difficult to see and that photographic non-visibility is not proof of absence.
- PMMA pre-conditioning/electret-control experiments, surface-potential mapping and charge-decay measurement.
- expanded slow-rpm sweep and four-terminal top-module experiment matrix.

### Added — direct Hauser / Marinov primary-scan audit

- `docs/research/hauser-marinov-primary-scan-audit-2026-08-16.md`.
- `docs/research/hauser-source-ledger.tsv` with per-scan SHA-256, source role, date text, machine scope and evidence class.
- direct Marinov scan evidence that Baumann had **`ANOTHER language`** when trying to explain the principle. The popular phrase `like an unknown language` remains an unverified exact paraphrase, but the underlying language-mismatch statement is now primary-source supported.
- direct Marinov small-machine statement that rotor wires are **`connected to nothing`**; preferred M2 electrical baseline is now individually floating sectors.
- direct statement that two wires are visible going to each side condenser; historical research pots now require a two-terminal external mode.
- direct Marinov rejection of Tesla-coil/AC interpretation of the small machine and identification of the side spirals as condenser electrodes.
- direct small-machine no-conventional-drive-motor statement; laboratory rpm drives must be removable/decouplable instrumentation.
- direct source separation between Marinov's `crystal`, Methernitha's institutional `rectifying diode`, Hauser's large-machine top-crystal/rectifier interpretation and Holzherr's four-lead early top-module memory.
- Hauser 1986/1988 large-machine details including ~500-mm/50-lamella rotor geometry, non-contact stators, three concentric grid cylinders, acrylic separators, central magnet tube and bifilar winding; all kept outside the M2 pot baseline.

### Added — complete historical video pass

- `docs/research/video-frame-audit-2026-08-16.md`.
- `docs/research/video-source-ledger.tsv` with hashes, embedded metadata, durations, decoded frame counts and machine scopes.
- all eight archive video streams traversed: **35,445 decoded video frames** total.
- `meth4.asf` linked visually to `testabig.jpg`; moving close-ups strengthen V3 geometry for the small assembly.
- two symmetric copper-coloured hub arcs upgraded from flat `markings` to likely raised physical-component candidates; electrical role remains unknown.
- outer small-machine panels confirmed visually as layered structures rather than one flat perforated plate.
- lower central V3 module refined conceptually toward a perforated cage/prismatic geometry.
- `testa01.ram` / `testa02.ram` embedded 2001 metadata anchors Dieter Dienst / Luzi Cathomen Methernitha-lab provenance and multi-machine workshop context.
- `testatikadeutsch.wmv` identified as a visual duplicate/re-encode/language variant of `meth2.asf`; preserved but not double-counted as independent geometry evidence.
- machine taxonomy expanded with `M4a`, `M6a`, `M6b` and `M7` to prevent cross-machine component leakage.

### Source-control decisions

- Kelly/Potter/Utkin material remains S2/I1 hypothesis/source-discovery material, not Testatika primary evidence.
- 12-cm Holzherr/Hauser small machines are kept distinct from Marinov's ~200-mm M2 until identity is proven.
- the 20-layer perforated capacitor statement and Hauser's three-grid/magnet/bifilar cylinders are assigned to large-machine families and are not imported into M2 pots.
- the four-lead top-module description remains a small-family topology lead, not a solved M2 crystal circuit.
- electret/dielectric conditioning is only a controlled experiment, not an asserted historical mechanism or energy source.
- late `1 kΩ between lamellae` material is explicitly weaker than the direct small-machine `connected to nothing` statement and cannot be M2 baseline.
- archived power labels, lamp demonstrations and meter deflections remain demonstration/source claims, not closed energy measurements.

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

- the phrase `like an unknown language` was not verified as a direct Marinov quotation at v0.3.0 time; subsequent Unreleased primary-scan audit now finds the related direct wording `ANOTHER language` while preserving the exact-quote distinction.
- the V3 pixel-analysis document no longer derives claims from an invented quotation.
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
