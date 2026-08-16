# Testatika Small Research Replica

[![Validate repository](https://github.com/inetconnector/testatika-small-research-replica/actions/workflows/validate.yml/badge.svg)](https://github.com/inetconnector/testatika-small-research-replica/actions/workflows/validate.yml)
![Status](https://img.shields.io/badge/status-research%20replica-orange)
![CAD](https://img.shields.io/badge/CAD-STEP%20%7C%20STL%20%7C%20GLB-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**Evidence-led, photogrammetric reconstruction of the first small Testatika machine described and tested by Stefan Marinov.**

> This repository is a historical/electrostatic research project. It is **not** presented as a proven free-energy or over-unity device. The original complete electrical circuit is not known, and no net-energy anomaly is claimed here.

![Photogrammetric front view](docs/images/photogrammetric_front_view.png)

## Replication completeness — read this first

The repository is designed to become as close to a **1:1 research replica** of Marinov's first small machine (M2) as surviving evidence permits. It does **not** convert missing historical information into invented certainty.

The canonical completeness ledger is [`docs/REPLICATION_STATUS.md`](docs/REPLICATION_STATUS.md). For every major subsystem it records whether a detail is:

- observed;
- source-stated;
- photo-derived;
- derived;
- hypothesized;
- conflicting;
- or still unknown.

A "complete research replica" therefore means: all source-supported geometry and materials are represented, every unresolved alternative is made reversible/testable where practical, and the experiment package can distinguish competing hypotheses. It does **not** mean that unknown original wiring, crystal material or pot topology is guessed and relabelled as historical fact.

## Included

This release targets the **small, single-disc machine shown on the right in Marinov's figures 13/14**. It keeps source-supported geometry, photo-derived dimensions, test hypotheses and unknown wiring explicitly separated.

- nominal **200 mm rotor**
- **20 / 24 / 25** radial copper-wire rotor variants
- through-disc routing points for alternative wire paths
- R0–R4 experimental routing families, including a source-qualified three-side-change R4 research route
- non-contact adjustable sector electrodes
- two side capacitor/"pot" modules: outer grid + dielectric + inner copper spiral
- two horseshoe-magnet mounts for the first small-machine variant
- exchangeable "crystal" carrier
- rear shield-plate experiment jig
- complete STL and STEP part libraries
- complete assembled V2 STEP / STL / OBJ / GLB model
- experimental V3 photo-interpretation STEP/STL model
- evidence matrix, photogrammetry, BOM, assembly and experiment documentation
- consolidated research knowledge base in [`STATE.md`](STATE.md)
- external/session handoff in [`addon.md`](addon.md) with case-safe [`ADDON.md`](ADDON.md) compatibility entry point
- detailed **Baumann / Methernitha language decoder** mapping historical terminology to testable engineering hypotheses
- canonical machine taxonomy and provenance schema
- deterministic manifest/hash generation and repository validation

## Quick access

| Asset | Path |
|---|---|
| Replication completeness | [`docs/REPLICATION_STATUS.md`](docs/REPLICATION_STATUS.md) |
| Complete V2 STEP | `hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V2_COMPLETE.step` |
| Complete V2 STL | `hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V2_COMPLETE.stl` |
| Complete V2 GLB | `hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V2_COMPLETE.glb` |
| Experimental V3 STEP | `hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V3_COMPLETE.step` |
| Experimental V3 STL | `hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V3_COMPLETE.stl` |
| Printable parts | [`hardware/stl/`](hardware/stl/) |
| Editable parts | [`hardware/step/`](hardware/step/) |
| CAD reproducibility | [`docs/research/cad-reproducibility.md`](docs/research/cad-reproducibility.md) |
| BOM | [`docs/research/bom.md`](docs/research/bom.md) |
| Assembly | [`docs/research/assembly.md`](docs/research/assembly.md) |
| Safety | [`docs/research/safety.md`](docs/research/safety.md) |
| Evidence matrix | [`docs/research/evidence_matrix.tsv`](docs/research/evidence_matrix.tsv) |
| Machine taxonomy | [`docs/research/machines.yaml`](docs/research/machines.yaml) |
| Provenance schema | [`docs/research/provenance-schema.yaml`](docs/research/provenance-schema.yaml) |
| External corpus boundary | [`docs/research/external-corpus.md`](docs/research/external-corpus.md) |
| Full research state | [`STATE.md`](STATE.md) |
| External handoff | [`addon.md`](addon.md) |
| Baumann language decoder | [`docs/research/baumann-language-decoding.md`](docs/research/baumann-language-decoding.md) |
| Baumann statement ledger | [`docs/research/baumann-statements.tsv`](docs/research/baumann-statements.tsv) |
| Hartmann/Overunity audit | [`docs/research/hartmann-overunity-testatika.md`](docs/research/hartmann-overunity-testatika.md) |
| Current experiment plan | [`docs/research/experiment-plan.md`](docs/research/experiment-plan.md) |
| Repository hardening plan | [`docs/repository-hardening-plan-2026-08-16.md`](docs/repository-hardening-plan-2026-08-16.md) |

## Important source correction: Baumann's "unknown language"

A literal Marinov quote saying Baumann's explanation sounded like an **"unknown language" has not been verified**.

The evidence supports three separate points:

1. Marinov did not understand the complete operating secret or exact schematic.
2. Hans Holzherr reported that Baumann was difficult to understand because he spoke softly/quickly and used non-scientific terminology.
3. Methernitha's own technical description explicitly says conventional physical terminology was, in its view, only partly adequate and uses special terms such as `Taster` / `antenna keys`.

The repository therefore does not preserve the later paraphrase as a direct Marinov quotation. The source-by-source reconstruction and engineering translation are in [`docs/research/baumann-language-decoding.md`](docs/research/baumann-language-decoding.md).

## Current operating-model hypothesis

After separating Baumann, Methernitha, Marinov, Holzherr, Luzi Cathomen and Stefan Hartmann statements by provenance, the strongest **testable** model is:

> **electrostatic influence / variable capacitance → non-contact pickup → polarity-selective charge routing → crystal/diode phase commutation → drive/storage buses → cyclic bias regeneration → model-dependent downstream impedance conditioning.**

This can explain much of the historical vocabulary (`earth/cloud`, `Taster`, `sort`, `keep in rhythm`, `grid condensers`, `keep the voltage up`) without assuming a Tesla/HF core or permanent-magnet energy source. It does **not** by itself explain or validate a net-energy surplus.

## V2 reference geometry

The strongest scale anchor is Marinov's statement that the small-machine disc was approximately **20 cm** in diameter. Other dimensions are photogrammetric working estimates.

| Feature | Working value |
|---|---:|
| Rotor diameter | 200 mm |
| Base width | ~370 mm |
| Base depth | ~180 mm |
| Side-pot OD | ~84 mm |
| Side-pot body height | ~110 mm |
| Rotor center above base | ~160 mm |
| Complete assembly envelope | ~370 × 182 × 324 mm |

Photo-derived dimensions should be treated as roughly **±10–15%** unless a better primary source becomes available.

## V3 photo interpretation

The V3 assembled files improve visible external geometry and subsystem placement using the higher-resolution frontal image. Their filename contains `V3_COMPLETE` only as a discoverability/convenience alias: the model metadata remains **experimental**, and hidden circuit, dark material identity and crystal internals remain unresolved.

The canonical interpretation is in [`docs/research/v3-photo/`](docs/research/v3-photo/).

## Evidence-led choices

### Strongly supported
- one rotating disc for the small model
- radial conductive sectors made from roughly 1 mm wire
- roughly 20–30 sectors; later wording narrows this to around 20–25
- no rubbing collector brushes
- importance of how wires pass **through the disc**
- side "pots" with grid/dielectric/copper-spiral structure
- a component Baumann called a **"crystal"**
- horseshoe magnets on the **first** small machine, while the second small machine did not visibly require them

### Deliberately not assumed
- Tesla coils as the core mechanism
- 50/60 Hz mains-frequency design as the fundamental principle
- a hidden 230 V AC stage
- permanent magnets as a net energy source
- verified 100 W / 1 kW / multi-kW over-unity output
- a fully known original schematic
- black appearance as proof of carbon/graphite/nanocoating/black copper oxide
- R4 as definitively the original M2 wire route

## Rotor routing research

The precise through-disc wire geometry is one of the most important unresolved details. The repository distinguishes test families rather than declaring one historical route as certain:

- **R0** — one-sided radial wire
- **R1** — front radial path, through outer hole, return on rear
- **R2** — alternating front/rear sectors
- **R3** — angularly offset through-disc routing
- **R4** — three-side-change weave derived from Holzherr's report for multiple machines; **not yet verified specifically for Marinov M2**

See [`docs/research/rotor-wire-routing.md`](docs/research/rotor-wire-routing.md).

## Scientific status

Conventional and reproducible effects relevant to this project include electrostatic induction, variable capacitance, non-contact capacitive coupling, electrostatic motor torque, capacitor storage, corona/ion transport and nonlinear charge gating.

What is **not** established is that the historical Testatika produced more energy than all inputs plus initial stored energy. Energy conservation is the null hypothesis of this repository.

See [`docs/scientific-status.md`](docs/scientific-status.md).

## Safety

High-voltage electrostatic systems can be dangerous, especially with capacitors. This project does **not** include an open mains-powered high-voltage supply design.

Use enclosed, current-limited educational/laboratory electrostatic equipment, keep stored energy low, discharge capacitors before handling, and use a rotor guard. No radioactive-material replication path is part of this project.

Read [`docs/research/safety.md`](docs/research/safety.md).

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
│   └── complete-model/
├── docs/
│   ├── REPLICATION_STATUS.md
│   ├── research/
│   └── images/
├── scripts/
├── .github/
└── release/
```

## Validate locally

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_assets.py
python scripts/check_manifest.py
```

After intentional content changes regenerate integrity metadata:

```bash
python scripts/generate_manifest.py
python scripts/check_manifest.py
```

## CAD regeneration

Install the CAD environment:

```bash
python -m pip install -r requirements-cad.txt
```

Rebuild all **currently source-reproducible** CAD families:

```bash
python scripts/rebuild_research_assets.py
```

Or run individual generators:

```bash
python cad/generate_v2.py
python cad/generate_v3_experiments.py
python cad/generate_v3_photo_interp.py
```

Important: `generate_v2.py` regenerates the V2 **core geometry**, not yet every preserved V2 release asset. See [`docs/research/cad-reproducibility.md`](docs/research/cad-reproducibility.md). Committed binary STEP/STL files are intentionally preserved until their replacement/source path is verified.

## Release package

The current research package version is **v0.3.0**. The release builder includes documentation, CAD sources, scripts, manifests and preserved binary research assets while retaining old release ZIPs as historical artifacts rather than overwriting them.

```bash
python scripts/build_release.py
```

## Sources and external corpus

The most important published source for this small machine is Stefan Marinov, *The Thorny Way of Truth, Part V* (1989), including his Methernitha/Testatika observations and figures 13/14. A scan is available through the Internet Archive under identifier `thornywayoftruthpart5maririch`.

Full third-party scans are intentionally not redistributed. Project history also refers to an externally held corpus named `testatika.zip`; it is **not part of the public repository** and must not be silently reconstructed from unrelated files. See [`docs/research/external-corpus.md`](docs/research/external-corpus.md), [`docs/sources.md`](docs/sources.md) and [`docs/research/source-basis.md`](docs/research/source-basis.md).

## Contributing

The most valuable contributions are higher-resolution primary photographs, independently sourced dimensions, original correspondence with provenance, controlled electrostatic measurements, and falsification tests for wire-routing/electrode/charge-commutation hypotheses.

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

Repository-authored code, CAD source, documentation and derived models are released under the [MIT License](LICENSE), unless explicitly stated otherwise. Third-party historical publications, scans and photographs remain subject to their respective rights.

---

### Deutsch

Dies ist eine **quellenkritische Forschungsreplik**, keine Behauptung, dass eine Freie-Energie-Funktion bewiesen sei. Schwerpunkt sind eine möglichst originalnahe Geometrie der kleinen Marinov-Maschine, die saubere Übersetzung historischer Erklärbegriffe in messbare Größen und experimentell überprüfbare Varianten für die nicht überlieferten Details. Der aktuelle Vollständigkeitsstand steht verbindlich in [`docs/REPLICATION_STATUS.md`](docs/REPLICATION_STATUS.md).
