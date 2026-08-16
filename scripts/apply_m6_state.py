#!/usr/bin/env python3
"""Add M6 Large V1 state/handoff information without replacing older research."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MARKER="<!-- M6-LARGE-V1-STATE -->"
BLOCK=f'''\n\n{MARKER}\n## M6 Large V1 best-evidence build\n\nThe repository now has a second canonical physical-build line for the large ~500-mm two-disc family. `M6-V1-B0` is anchored primarily to Albert Hauser's 1986/1988 M6a material and cross-checked against `meth2/meth3/meth5`. It is separate from M2 V4.\n\nCanonical generator: `cad/generate_m6_large_v1.py`.\nMaterialized CAD: `hardware/experimental/m6-large-v1-best-evidence/`.\nPrimary STL: `complete-model/Testatika_M6_LARGE_V1_BEST_EVIDENCE.stl`.\nGuarded lab STL: `complete-model/Testatika_M6_LARGE_V1_SAFE_LAB_GUARDED.stl`.\nBuild docs: `docs/research/m6-large-v1-*`.\n\nDirect anchors include ~500 x 5 mm disc geometry, ~50 sheet lamellae (~0.2 x 20 x 160 mm source dimensions), ~8 front + ~6 rear non-contact perforated stators, three concentric grid tubes per large cylinder, acrylic separators, central magnet tube, two-layer bifilar ~18-gauge winding, wound horseshoe modules, top crystal/possible-rectifier geometry, and Hauser's motor/magnet-wheel large-machine configuration.\n\nHistorical hidden node wiring, exact crystal material/function, exact magnetic function, exact cylinder interconnections, exact startup state and any net-energy source remain unresolved. The V1 electrical default leaves unknown networks open at explicit test terminals. No over-unity claim is made.\n'''
for name in ("STATE.md","addon.md"):
    p=ROOT/name
    text=p.read_text(encoding="utf-8")
    if MARKER not in text:
        p.write_text(text.rstrip()+BLOCK+"\n",encoding="utf-8",newline="\n")
        print("updated",name)
    else:
        print("already present",name)
