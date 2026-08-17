# Testatika Research Replica — Small M2 + Large M6

<p align="center">
  <a href="README.md">Deutsch</a> · <strong>English</strong>
</p>

[![Validate repository](https://github.com/inetconnector/testatika-small-research-replica/actions/workflows/validate.yml/badge.svg)](https://github.com/inetconnector/testatika-small-research-replica/actions/workflows/validate.yml)
![Status](https://img.shields.io/badge/status-research%20replica-orange)
![CAD](https://img.shields.io/badge/CAD-STEP%20%7C%20STL%20%7C%20GLB-blue)
![License](https://img.shields.io/badge/license-MIT-green)

<!-- README-SYNC:principle-report -->
## “Earth – Cloud – Thunderstorm” operating-principle report

The detailed source-guided technical summary of the current working hypothesis — including variable capacitance, influence, grids/pickups, crystal/diode phase commutation, electrostatic torque, speed stabilization, dry-air/humidity dependence, and the open energy-balance question — is available as a Word document in both languages:

- **Deutsch:** [`Testatika_Funktionsprinzip_Erde_Wolke_Trockenluft.docx`](docs/research/Testatika_Funktionsprinzip_Erde_Wolke_Trockenluft.docx)
- **English:** [`Testatika_Functional_Principle_Earth_Cloud_Dry_Air.docx`](docs/research/Testatika_Functional_Principle_Earth_Cloud_Dry_Air.docx)

> The documents describe a testable electrostatic working hypothesis; they are not evidence for over-unity or an unidentified net-energy source.

<!-- README-SYNC:build-lines -->
<!-- BUILD-LINES-START -->

## Start here — real fabrication kits

| Build line | Fabrication kit | Assembly/fit reference | Legacy full-model reference |
|---|---|---|---|
| **Small M2 — V5 fabrication kit** | [`testatika-m2-v5-fabrication-kit.zip`](release/fabrication-kits/testatika-m2-v5-fabrication-kit.zip) | [STEP](hardware/build-kits/m2-v5/assembly-reference/Testatika_M2_V5_FABRICATION_ASSEMBLY_REFERENCE_NOT_FOR_PRINT.step) | [V4 reference, view only](hardware/experimental/v4-best-evidence-m2/reference-visual-only/complete-model/Testatika_M2_V4_REFERENCE_VISUAL_ONLY.step) |
| **Large M6 — V2 fabrication kit** | [`testatika-m6-v2-fabrication-kit.zip`](release/fabrication-kits/testatika-m6-v2-fabrication-kit.zip) | [STEP](hardware/build-kits/m6-v2/assembly-reference/Testatika_M6_V2_FABRICATION_ASSEMBLY_REFERENCE_NOT_FOR_PRINT.step) | [V1 reference, view only](hardware/experimental/m6-large-v1-best-evidence/reference-visual-only/complete-model/Testatika_M6_LARGE_V1_REFERENCE_VISUAL_ONLY.step) |

**Important:** STL files under `hardware/build-kits/*/print/` are only genuine printable supports such as holders, clips, jigs and guards. Conductors, metal grids, lamellae, magnets, shafts, bearings and PMMA rotor discs are real fabricated/purchased parts. Primary bearing towers and rotor hubs are also real metal/G10 fabrication parts. Assembly STLs are fit/view references and explicitly **not print jobs**. Historically unknown internal circuitry remains modular/open instead of being invented.

<!-- BUILD-LINES-END -->

<!-- README-SYNC:intro -->
**Evidence-led Testatika reconstruction project with two separated build lines: the small Marinov M2 and the large ~500-mm M6 family.**

> This repository is a historical/electrostatic research project. It is **not** presented as a proven free-energy or over-unity device. The original complete electrical circuit is not known, and no net-energy anomaly is claimed here.

![Photogrammetric front view](docs/images/photogrammetric_front_view.png)

<!-- README-SYNC:replication-completeness -->
## Replication completeness — read this first

The repository is designed to become as close to a **1:1 research replica** of Marinov's first small machine (M2) as surviving evidence permits. It does **not** convert missing historical information into invented certainty.

The canonical completeness ledger is [`docs/REPLICATION_STATUS.md`](docs/REPLICATION_STATUS.md). For every major subsystem it records whether a detail is observed, source-stated, photo/video-derived, derived, hypothesized, conflicting, or still unknown.

A "complete research replica" therefore means: all source-supported geometry and materials are represented, every unresolved alternative is made reversible/testable where practical, and the experiment package can distinguish competing hypotheses. It does **not** mean that unknown original wiring, crystal material or pot topology is guessed and relabelled as historical fact.

<!-- README-SYNC:m2-target -->
## Small M2 build target: V4 best-evidence M2

For a **new physical build**, use V4 rather than treating the older V2/V3 models as the final assembly.

V4 integrates the strongest direct Marinov scan constraints with the complete photo/video audit:

- one ~200-mm rotor;
- 20/24/25 choices, nominal 24;
- **individually floating rotor wires** — no galvanic neighbour ring in the M2 baseline;
- R0 as the least-speculative nominal routing and R4 as a separate research rotor;
- no rubbing collectors;
- two side pots with grid + dielectric + inner Cu spiral;
- **exactly two historical external terminal positions per pot**;
- no built-in conventional drive motor;
- two visible horseshoe-magnet positions plus matched nonmagnetic controls;
- video-refined hub arcs, layered outer panels and lower central cage;
- unresolved `crystal` retained as a removable black box rather than a guessed original circuit.

Start here:

- [`docs/research/v4-best-evidence-m2.md`](docs/research/v4-best-evidence-m2.md)
- [`docs/research/v4-bom.md`](docs/research/v4-bom.md)
- [`docs/research/v4-assembly.md`](docs/research/v4-assembly.md)
- [`docs/research/v4-electrical-boundary.md`](docs/research/v4-electrical-boundary.md)
- [`docs/research/v4-printing.md`](docs/research/v4-printing.md)

Generator:

`cad/generate_v4_best_evidence_m2.py`

Materialized output:

`hardware/experimental/v4-best-evidence-m2/`

Deterministic build package:

`release/experimental/testatika-m2-v4-best-evidence-build-package.zip`

<!-- README-SYNC:included -->
## Included

This repository targets the **small, single-disc machine shown on the right in Marinov's figures 13/14** while preserving older and cross-machine research separately.

- nominal **200 mm rotor**;
- **20 / 24 / 25** radial copper-wire rotor variants;
- direct-source preferred **floating-sector** electrical topology;
- R0–R4 experimental routing families;
- non-contact adjustable sector electrodes;
- two side capacitor/"pot" modules: outer grid + dielectric + inner copper spiral;
- source-supported two-wire pot interface;
- two horseshoe-magnet positions for the first small-machine variant;
- exchangeable "crystal" carrier;
- video-derived hub-arc, layered-panel and central-cage refinements;
- rear shield-plate experiment jig;
- preserved V2 and V3 STEP/STL research models;
- reproducible V4 complete STEP/STL assemblies;
- evidence matrix, photogrammetry, BOM, assembly and experiment documentation;
- consolidated research knowledge base in [`STATE.md`](STATE.md);
- external/session handoff in [`addon.md`](addon.md) with case-safe [`ADDON.md`](ADDON.md) compatibility entry point;
- detailed Baumann / Methernitha language decoder;
- canonical machine taxonomy and provenance schema;
- deterministic manifest/hash generation and repository validation.

<!-- README-SYNC:quick-access -->
## Quick access

| Asset | Path |
|---|---|
| Replication completeness | [`docs/REPLICATION_STATUS.md`](docs/REPLICATION_STATUS.md) |
| **V4 current build definition** | [`docs/research/v4-best-evidence-m2.md`](docs/research/v4-best-evidence-m2.md) |
| **V4 BOM** | [`docs/research/v4-bom.md`](docs/research/v4-bom.md) |
| **V4 assembly** | [`docs/research/v4-assembly.md`](docs/research/v4-assembly.md) |
| **V4 electrical boundary** | [`docs/research/v4-electrical-boundary.md`](docs/research/v4-electrical-boundary.md) |
| **V4 printing** | [`docs/research/v4-printing.md`](docs/research/v4-printing.md) |
| V4 generated CAD | `hardware/experimental/v4-best-evidence-m2/` |
| V4 build ZIP | `release/experimental/testatika-m2-v4-best-evidence-build-package.zip` |
| Complete V2 STEP | `hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V2_COMPLETE.step` |
| Complete V2 STL | `hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V2_COMPLETE.stl` |
| Complete V2 GLB | `hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V2_COMPLETE.glb` |
| Experimental V3 STEP | `hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V3_COMPLETE.step` |
| Experimental V3 STL | `hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V3_COMPLETE.stl` |
| Legacy printable parts | [`hardware/stl/`](hardware/stl/) |
| Legacy editable parts | [`hardware/step/`](hardware/step/) |
| CAD reproducibility | [`docs/research/cad-reproducibility.md`](docs/research/cad-reproducibility.md) |
| Legacy V2 BOM | [`docs/research/bom.md`](docs/research/bom.md) |
| Legacy V2 assembly | [`docs/research/assembly.md`](docs/research/assembly.md) |
| Safety | [`docs/research/safety.md`](docs/research/safety.md) |
| Evidence matrix | [`docs/research/evidence_matrix.tsv`](docs/research/evidence_matrix.tsv) |
| Machine taxonomy | [`docs/research/machines.yaml`](docs/research/machines.yaml) |
| Provenance schema | [`docs/research/provenance-schema.yaml`](docs/research/provenance-schema.yaml) |
| Full video audit | [`docs/research/video-frame-audit-2026-08-16.md`](docs/research/video-frame-audit-2026-08-16.md) |
| Marinov/Hauser scan audit | [`docs/research/hauser-marinov-primary-scan-audit-2026-08-16.md`](docs/research/hauser-marinov-primary-scan-audit-2026-08-16.md) |
| External corpus boundary | [`docs/research/external-corpus.md`](docs/research/external-corpus.md) |
| Full research state | [`STATE.md`](STATE.md) |
| External handoff | [`addon.md`](addon.md) |
| Baumann language decoder | [`docs/research/baumann-language-decoding.md`](docs/research/baumann-language-decoding.md) |
| Baumann statement ledger | [`docs/research/baumann-statements.tsv`](docs/research/baumann-statements.tsv) |
| Hartmann/Overunity audit | [`docs/research/hartmann-overunity-testatika.md`](docs/research/hartmann-overunity-testatika.md) |
| Current experiment plan | [`docs/research/experiment-plan.md`](docs/research/experiment-plan.md) |

<!-- README-SYNC:source-correction -->
## Source correction: Baumann's explanation language

The full archive scan audit materially improves the old wording.

A direct Marinov correspondence scan states that Baumann used **`ANOTHER language`** when attempting to explain the principle. Therefore the underlying language-mismatch point is now primary-source supported.

What is **still not verified** is the popular later wording that Baumann's explanation was literally *"like an unknown language"*. Do not present that later paraphrase as Marinov's exact quotation.

Separately:

1. Marinov did not understand the complete operating secret or exact schematic.
2. Hans Holzherr reported that Baumann was difficult to understand because he spoke softly/quickly and used non-scientific terminology.
3. Methernitha's own technical description used special vocabulary such as `Taster` / `antenna keys`.

See [`docs/research/baumann-language-decoding.md`](docs/research/baumann-language-decoding.md) and the primary-scan audit.

<!-- README-SYNC:operating-model -->
## Current operating-model hypothesis

After separating Baumann, Methernitha, Marinov, Holzherr, Luzi Cathomen, Albert Hauser and Stefan Hartmann statements by provenance, the strongest **testable** model is:

> **electrostatic influence / variable capacitance → non-contact pickup → polarity-selective charge routing → crystal/diode phase commutation → drive/storage buses → cyclic bias regeneration → model-dependent downstream impedance conditioning.**

This can explain much of the historical vocabulary without assuming a Tesla/HF core or permanent-magnet energy source. It does **not** by itself explain or validate a net-energy surplus.

<!-- README-SYNC:reference-geometry -->
## Reference geometry

The strongest scale anchor is Marinov's statement that the small-machine disc was approximately **20 cm** in diameter. Other dimensions are photogrammetric/video-fit working estimates.

| Feature | Working value |
|---|---:|
| Rotor diameter | 200 mm |
| Base width | ~370 mm |
| Base depth | ~180 mm |
| Side-pot OD | ~84 mm |
| Side-pot body height | ~110 mm |
| Rotor center above base | ~160 mm |
| Complete assembly envelope | ~370 × 182 × 324 mm |

Photo/video-derived dimensions should be treated as approximate unless a calibrated primary view or original-object measurement becomes available.

<!-- README-SYNC:versions -->
## V2 / V3 / V4 relationship

- **V2:** conservative mechanical baseline and preserved release library.
- **V3:** photo interpretation plus separate video-derived refinements.
- **V4:** current best-evidence physical-build family; it integrates the stronger primary-scan electrical constraints with the best current visible geometry.

Older versions are not deleted; they remain provenance and comparison assets.

<!-- README-SYNC:evidence-choices -->
## Evidence-led choices

### Strongly supported

- one rotating disc for the small model;
- radial conductive sectors made from roughly 1-mm wire;
- roughly 20–25 sectors as the tighter later range;
- direct-source statement that the described small-disk wires are **`connected to nothing`**;
- no rubbing collector brushes;
- importance of how wires pass through the disc;
- side pots with grid/dielectric/copper-spiral structure;
- two visible leads to each condenser;
- a component Baumann called a **`crystal`**;
- no Tesla-coil/AC interpretation for the described small machine according to Marinov;
- horseshoe magnets on the first small-machine line, but not universal to every small variant.

### Deliberately not assumed

- 1-kΩ neighbour ring as M2 baseline;
- Tesla coils as the core mechanism;
- 50/60-Hz mains-frequency design as the fundamental principle;
- hidden 230-V AC stage;
- permanent magnets as a net energy source;
- verified 100-W / 1-kW / multi-kW over-unity output;
- fully known original schematic;
- black appearance as proof of carbon/graphite/nanocoating/black copper oxide;
- R4 as definitively the original M2 wire route;
- Hauser's large-machine 3-grid/magnet/bifilar cylinders as M2 pots.

<!-- README-SYNC:rotor-routing -->
## Rotor routing research

The precise through-disc wire geometry remains one of the most important unresolved details:

- **R0** — one-sided radial reference and V4 nominal build route;
- **R1** — front radial path, through outer hole, return on rear;
- **R2** — alternating front/rear sectors;
- **R3** — angularly offset through-disc routing;
- **R4** — three-side-change weave derived from Holzherr's report for multiple machines; not yet verified specifically for Marinov M2.

Electrical topology is a separate variable: V4 keeps individual sectors floating even on the R4 research rotor.

See [`docs/research/rotor-wire-routing.md`](docs/research/rotor-wire-routing.md).

<!-- README-SYNC:scientific-status -->
## Scientific status

Conventional and reproducible effects relevant to this project include electrostatic induction, variable capacitance, non-contact capacitive coupling, electrostatic motor torque, capacitor storage, corona/ion transport and nonlinear charge gating.

What is **not** established is that the historical Testatika produced more energy than all inputs plus initial stored energy. Energy conservation is the null hypothesis of this repository.

See [`docs/scientific-status.md`](docs/scientific-status.md).

<!-- README-SYNC:safety -->
## Safety

High-voltage electrostatic systems can be dangerous, especially with capacitors. This project does **not** include an open mains-powered high-voltage supply design.

Use enclosed, current-limited educational/laboratory electrostatic equipment, keep stored energy low, discharge capacitors before handling, and use a rotor guard. No radioactive-material replication path is part of this project.

Read [`docs/research/safety.md`](docs/research/safety.md).

<!-- README-SYNC:layout -->
## Repository layout

```text
.
├── STATE.md
├── addon.md / ADDON.md
├── cad/
├── hardware/
│   ├── stl/
│   ├── step/
│   ├── experimental/
│   │   └── v4-best-evidence-m2/
│   └── complete-model/
├── docs/
│   ├── REPLICATION_STATUS.md
│   ├── research/
│   └── images/
├── scripts/
├── .github/
└── release/
    └── experimental/
```

<!-- README-SYNC:validate -->
## Validate locally

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_assets.py
python scripts/check_readme_sync.py
python scripts/check_manifest.py
```

After intentional content changes regenerate integrity metadata:

```bash
python scripts/generate_manifest.py
python scripts/check_manifest.py
```

<!-- README-SYNC:cad-regeneration -->
## CAD regeneration

Install the CAD environment:

```bash
python -m pip install -r requirements-cad.txt
```

Rebuild all currently source-reproducible CAD families:

```bash
python scripts/rebuild_research_assets.py
```

Or run individual generators:

```bash
python cad/generate_v2.py
python cad/generate_v3_experiments.py
python cad/generate_v3_photo_interp.py
python cad/generate_v3_video_refinements.py
python cad/generate_v4_best_evidence_m2.py
```

Important: `generate_v2.py` regenerates the V2 **core geometry**, not every preserved V2 release asset. V4 has its own declared source-owned part and assembly family. See [`docs/research/cad-reproducibility.md`](docs/research/cad-reproducibility.md).

<!-- README-SYNC:build-packages -->
## Build packages

The preservation/research release remains **v0.3.0**. In addition, the current physical-build package is generated deterministically with:

```bash
python cad/generate_v4_best_evidence_m2.py
python scripts/build_v4_package.py
```

Result:

- `release/experimental/testatika-m2-v4-best-evidence-build-package.zip`;
- matching `.sha256` file.

The package contains the V4 generator, STEP/STL assets, complete assemblies, BOM, assembly instructions, printing guidance, electrical evidence boundary, safety and the primary-source/video audit context needed to interpret the model correctly.

<!-- README-SYNC:sources -->
## Sources and external corpus

The most important published source for this small machine is Stefan Marinov, *The Thorny Way of Truth, Part V* (1989), supplemented by the direct Marinov/Hauser correspondence scans and historical media audited in this project.

Full third-party scans/videos are intentionally not redistributed. Project history also refers to an externally held corpus named `testatika.zip`; it is **not part of the public repository**. Hashes/locators and derived research findings are documented without silently republishing third-party media.

See [`docs/research/external-corpus.md`](docs/research/external-corpus.md), [`docs/sources.md`](docs/sources.md), [`docs/research/source-basis.md`](docs/research/source-basis.md), the primary-scan audit and the video-frame audit.

<!-- README-SYNC:contributing -->
## Contributing

The most valuable contributions are higher-resolution primary photographs, independently sourced dimensions, original correspondence with provenance, controlled electrostatic measurements, and falsification tests for wire-routing/electrode/charge-commutation hypotheses.

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md).

**Language rule:** `README.md` (German) and `README.en.md` (English) are equal, fully synchronized versions. Content changes to the README must always be made in both languages; `python scripts/check_readme_sync.py` checks structural parity.

<!-- README-SYNC:license -->
## License

Repository-authored code, CAD source, documentation and derived models are released under the [MIT License](LICENSE), unless explicitly stated otherwise. Third-party historical publications, scans and photographs remain subject to their respective rights.
