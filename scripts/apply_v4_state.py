#!/usr/bin/env python3
"""Append the V4 best-evidence M2 handoff block without deleting prior state."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "<!-- V4_BEST_EVIDENCE_M2_2026-08-16 -->"

BLOCK = r'''

<!-- V4_BEST_EVIDENCE_M2_2026-08-16 -->
## V4 BEST-EVIDENCE M2 — current physical-build baseline (2026-08-16)

V4 is now the preferred starting point for any **new physical reconstruction of Marinov's first small machine (M2)**. V2/V3 remain preserved research/provenance families and must not be deleted.

Canonical files:

- `docs/research/v4-best-evidence-m2.md`
- `docs/research/v4-bom.md`
- `docs/research/v4-assembly.md`
- `docs/research/v4-electrical-boundary.md`
- `docs/research/v4-printing.md`
- `docs/research/v4-configurations.yaml`
- `cad/generate_v4_best_evidence_m2.py`
- `scripts/check_v4_assets.py`
- `scripts/build_v4_package.py`
- `.github/workflows/materialize-v4-best-evidence.yml`

Best-evidence V4 baseline:

1. one ~200-mm rotor;
2. nominal 24 sectors, with 20/25 count variants retained;
3. ~1-mm Cu wires;
4. **each sector individually floating / no neighbour ring**, based on direct Marinov `connected to nothing` wording;
5. R0 is the least-speculative nominal physical route; R4 is a separate research rotor and remains unproven specifically for M2;
6. no rubbing collectors;
7. two side pots with outer grid + dielectric/PMMA + inner Cu spiral;
8. **two external functional terminals per pot**, based on direct Marinov observation;
9. no Tesla/HF pot stage in the M2 baseline;
10. no built-in conventional drive motor in the historical baseline; any lab drive is removable instrumentation with separately measured input;
11. two visible horseshoe-magnet positions are retained, but magnet function remains unknown and matched nonmagnetic dummies are required for controls;
12. `meth4.asf`/`testabig.jpg` moving/still cross-check is integrated as geometry: two hub arcs, layered outer panels and a perforated lower central cage/prism;
13. `crystal` remains an unresolved Blackbox. V4 supports reversible low-energy surrogates but none is called original.

Nominal null configuration: `M2-V4-B0` in `docs/research/v4-configurations.yaml`.

Materialized CAD/output target:

- `hardware/experimental/v4-best-evidence-m2/stl/`
- `hardware/experimental/v4-best-evidence-m2/step/`
- `hardware/experimental/v4-best-evidence-m2/complete-model/Testatika_M2_V4_BEST_EVIDENCE.*`
- `hardware/experimental/v4-best-evidence-m2/complete-model/Testatika_M2_V4_R4_RESEARCH.*`
- `hardware/experimental/v4-best-evidence-m2/metadata/MODEL_INFO_V4.json`
- `release/experimental/testatika-m2-v4-best-evidence-build-package.zip`
- matching `.sha256`.

Still historically unresolved — do not invent:

- exact through-disc M2 routing;
- full node-to-node original wiring;
- exact pot polarity/capacitance/turn count;
- Crystal material/I-V/topology;
- exact stationary-electrode grouping;
- electrical role of hub arcs;
- magnet function;
- exact priming/start procedure;
- source of historical output claims / any net-energy anomaly.

Scientific boundary remains unchanged: no over-unity/free-energy claim is established. Energy conservation is the null hypothesis; any anomaly requires closed, uncertainty-aware energy accounting and independent replication.
'''


def apply(path: Path):
    text = path.read_text(encoding="utf-8")
    if MARKER in text:
        print(f"V4 state block already present: {path.name}")
        return False
    path.write_text(text.rstrip() + BLOCK + "\n", encoding="utf-8")
    print(f"Appended V4 state block: {path.name}")
    return True


def main():
    changed = False
    for rel in ("STATE.md", "addon.md"):
        changed = apply(ROOT / rel) or changed
    print("changed" if changed else "unchanged")


if __name__ == "__main__":
    main()
