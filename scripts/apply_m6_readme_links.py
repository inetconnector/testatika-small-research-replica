#!/usr/bin/env python3
"""Idempotently place the M2/M6 complete-build links at the top of README.md."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/"README.md"
text=p.read_text(encoding="utf-8")
START="<!-- BUILD-LINES-START -->"
END="<!-- BUILD-LINES-END -->"
block=f'''{START}\n\n## Start here — complete current models\n\n| Build line | Complete STL | Complete STEP | Build guide |\n|---|---|---|---|\n| **Small M2 — V4 best evidence** | [Download / open STL](hardware/experimental/v4-best-evidence-m2/complete-model/Testatika_M2_V4_BEST_EVIDENCE.stl) | [STEP](hardware/experimental/v4-best-evidence-m2/complete-model/Testatika_M2_V4_BEST_EVIDENCE.step) | [M2 V4 guide](docs/research/v4-best-evidence-m2.md) |\n| **Large M6 — V1 best evidence (~500 mm twin disc)** | [Download / open STL](hardware/experimental/m6-large-v1-best-evidence/complete-model/Testatika_M6_LARGE_V1_BEST_EVIDENCE.stl) | [STEP](hardware/experimental/m6-large-v1-best-evidence/complete-model/Testatika_M6_LARGE_V1_BEST_EVIDENCE.step) | [M6 Large V1 guide](docs/research/m6-large-v1-best-evidence.md) |\n| **Large M6 — guarded lab/mechanical version** | [Guarded STL](hardware/experimental/m6-large-v1-best-evidence/complete-model/Testatika_M6_LARGE_V1_SAFE_LAB_GUARDED.stl) | [Guarded STEP](hardware/experimental/m6-large-v1-best-evidence/complete-model/Testatika_M6_LARGE_V1_SAFE_LAB_GUARDED.step) | [Assembly](docs/research/m6-large-v1-assembly.md) |\n\n**Important:** the CAD can be mechanically complete while historical hidden wiring remains unknown. Unknown nodes are kept reversible/open rather than invented. No free-energy/over-unity function is claimed.\n\n{END}\n'''
if START in text and END in text:
    a=text.index(START); b=text.index(END,a)+len(END)
    text=text[:a]+block.rstrip()+text[b:]
else:
    anchor="![License](https://img.shields.io/badge/license-MIT-green)\n"
    if anchor not in text: raise SystemExit("README badge anchor not found")
    text=text.replace(anchor,anchor+"\n"+block,1)
text=text.replace("**Evidence-led, photogrammetric reconstruction of the first small Testatika machine described and tested by Stefan Marinov.**",
                  "**Evidence-led Testatika reconstruction project with two separated build lines: the small Marinov M2 and the large ~500-mm M6 family.**")
p.write_text(text,encoding="utf-8",newline="\n")
print("README build links applied")
