#!/usr/bin/env python3
"""Synchronously update the German and English README build-line blocks for fabrication kits."""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
START="<!-- BUILD-LINES-START -->"; END="<!-- BUILD-LINES-END -->"
DE=f'''{START}

## Hier beginnen — reale Fertigungs-Bausätze

| Baulinie | Fertigungs-Bausatz | Montage-/Passungsansicht | Alte Vollmodell-Referenz |
|---|---|---|---|
| **Kleine M2 — V5 Fertigungs-Bausatz** | [`testatika-m2-v5-fabrication-kit.zip`](release/fabrication-kits/testatika-m2-v5-fabrication-kit.zip) | [STEP](hardware/build-kits/m2-v5/assembly-reference/Testatika_M2_V5_FABRICATION_ASSEMBLY_REFERENCE_NOT_FOR_PRINT.step) | [V4 Referenz, nur Ansicht](hardware/experimental/v4-best-evidence-m2/reference-visual-only/complete-model/Testatika_M2_V4_REFERENCE_VISUAL_ONLY.step) |
| **Große M6 — V2 Fertigungs-Bausatz** | [`testatika-m6-v2-fabrication-kit.zip`](release/fabrication-kits/testatika-m6-v2-fabrication-kit.zip) | [STEP](hardware/build-kits/m6-v2/assembly-reference/Testatika_M6_V2_FABRICATION_ASSEMBLY_REFERENCE_NOT_FOR_PRINT.step) | [V1 Referenz, nur Ansicht](hardware/experimental/m6-large-v1-best-evidence/reference-visual-only/complete-model/Testatika_M6_LARGE_V1_REFERENCE_VISUAL_ONLY.step) |

**Wichtig:** STL-Dateien unter `hardware/build-kits/*/print/` sind ausschließlich echte Druckteile wie Halter, Clips, Jigs und Schutzteile. Leiter, Metallgitter, Lamellen, Magnete, Wellen, Lager und PMMA-Rotorscheiben werden als reale Fertigungs-/Kaufteile ausgeführt. Primär tragende Lagerträger und Rotorhubs sind ebenfalls reale Metall/G10-Fertigungsteile. Assembly-STLs sind nur Passungs-/Ansichtsmodelle und ausdrücklich **nicht zum Drucken**. Die historisch unbekannte interne Schaltung bleibt modular/offen statt erfunden.

{END}'''
EN=f'''{START}

## Start here — real fabrication kits

| Build line | Fabrication kit | Assembly/fit reference | Legacy full-model reference |
|---|---|---|---|
| **Small M2 — V5 fabrication kit** | [`testatika-m2-v5-fabrication-kit.zip`](release/fabrication-kits/testatika-m2-v5-fabrication-kit.zip) | [STEP](hardware/build-kits/m2-v5/assembly-reference/Testatika_M2_V5_FABRICATION_ASSEMBLY_REFERENCE_NOT_FOR_PRINT.step) | [V4 reference, view only](hardware/experimental/v4-best-evidence-m2/reference-visual-only/complete-model/Testatika_M2_V4_REFERENCE_VISUAL_ONLY.step) |
| **Large M6 — V2 fabrication kit** | [`testatika-m6-v2-fabrication-kit.zip`](release/fabrication-kits/testatika-m6-v2-fabrication-kit.zip) | [STEP](hardware/build-kits/m6-v2/assembly-reference/Testatika_M6_V2_FABRICATION_ASSEMBLY_REFERENCE_NOT_FOR_PRINT.step) | [V1 reference, view only](hardware/experimental/m6-large-v1-best-evidence/reference-visual-only/complete-model/Testatika_M6_LARGE_V1_REFERENCE_VISUAL_ONLY.step) |

**Important:** STL files under `hardware/build-kits/*/print/` are only genuine printable supports such as holders, clips, jigs and guards. Conductors, metal grids, lamellae, magnets, shafts, bearings and PMMA rotor discs are real fabricated/purchased parts. Primary bearing towers and rotor hubs are also real metal/G10 fabrication parts. Assembly STLs are fit/view references and explicitly **not print jobs**. Historically unknown internal circuitry remains modular/open instead of being invented.

{END}'''

def apply(path, block):
    text=path.read_text(encoding="utf-8")
    if START not in text or END not in text: raise SystemExit(f"build markers missing in {path.name}")
    a=text.index(START); b=text.index(END,a)+len(END)
    path.write_text(text[:a]+block+text[b:],encoding="utf-8",newline="\n")

apply(ROOT/"README.md",DE)
apply(ROOT/"README.en.md",EN)
print("README.md and README.en.md fabrication-kit blocks updated together")
