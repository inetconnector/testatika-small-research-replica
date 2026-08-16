#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

required = [
    "README.md",
    "STATE.md",
    "LICENSE",
    "hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V2_COMPLETE.step",
    "hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V2_COMPLETE.stl",
    "hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V2_COMPLETE.glb",
    "hardware/stl/rotor_20wire.stl",
    "hardware/stl/rotor_24wire.stl",
    "hardware/stl/rotor_25wire.stl",
    "hardware/step/ASSEMBLY_REFERENCE.step",
    "docs/research/evidence_matrix.tsv",
    "docs/research/assembly.md",
    "docs/research/safety.md",
]

errors = []
for rel in required:
    p = ROOT / rel
    if not p.exists():
        errors.append(f"missing: {rel}")
    elif p.is_file() and p.stat().st_size == 0:
        errors.append(f"empty: {rel}")

try:
    import trimesh
    for p in sorted((ROOT/"hardware/stl").glob("*.stl")):
        mesh = trimesh.load_mesh(p, force="mesh")
        if len(mesh.vertices) < 3 or len(mesh.faces) < 1:
            errors.append(f"invalid mesh: {p.relative_to(ROOT)}")
        if any(float(x) <= 0 for x in mesh.extents):
            errors.append(f"zero extent: {p.relative_to(ROOT)}")
except Exception as e:
    errors.append(f"trimesh validation failed: {e}")

if errors:
    print("VALIDATION FAILED")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("VALIDATION OK")
print("STL files:", len(list((ROOT/"hardware/stl").glob("*.stl"))))
print("STEP files:", len(list((ROOT/"hardware/step").glob("*.step"))))
