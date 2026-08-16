#!/usr/bin/env python3
"""Repository-wide structural validator.

Validates research integrity and asset structure without trying to prove historical
claims. It catches stale paths, malformed ledgers, missing core assets, broken local
Markdown links, mesh errors and baseline dimensional drift.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "STATE.md",
    "addon.md",
    "ADDON.md",
    "PRESERVATION.md",
    "ROADMAP.md",
    "CITATION.cff",
    "LICENSE",
    "docs/REPLICATION_STATUS.md",
    "docs/research/machines.yaml",
    "docs/research/provenance-schema.yaml",
    "docs/research/replica-configuration-matrix.md",
    "docs/research/external-corpus.md",
    "docs/research/evidence_matrix.tsv",
    "docs/research/baumann-statements.tsv",
    "docs/research/hartmann-overunity-sources.tsv",
    "docs/research/assembly.md",
    "docs/research/safety.md",
    "docs/research/experiment-plan.md",
    "docs/research/stl_dimensions.json",
    "docs/research/v4-best-evidence-m2.md",
    "docs/research/v4-bom.md",
    "docs/research/v4-assembly.md",
    "docs/research/v4-electrical-boundary.md",
    "docs/research/v4-printing.md",
    "docs/research/v4-configurations.yaml",
    "cad/generate_v4_best_evidence_m2.py",
    "scripts/build_v4_package.py",
    "scripts/check_v4_assets.py",
    "scripts/apply_v4_state.py",
    ".github/workflows/materialize-v4-best-evidence.yml",
    "hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V2_COMPLETE.step",
    "hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V2_COMPLETE.stl",
    "hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V2_COMPLETE.glb",
    "hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V3_COMPLETE.step",
    "hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V3_COMPLETE.stl",
    "hardware/stl/rotor_20wire.stl",
    "hardware/stl/rotor_24wire.stl",
    "hardware/stl/rotor_25wire.stl",
    "hardware/step/ASSEMBLY_REFERENCE.step",
]

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
errors: list[str] = []
warnings: list[str] = []


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


for item in REQUIRED:
    p = ROOT / item
    if not p.exists():
        errors.append(f"missing: {item}")
    elif p.is_file() and p.stat().st_size == 0:
        errors.append(f"empty: {item}")

for p in ROOT.rglob("*.json"):
    if ".git" in p.parts:
        continue
    try:
        json.loads(p.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"invalid JSON {rel(p)}: {exc}")

for item in [
    "docs/research/evidence_matrix.tsv",
    "docs/research/baumann-statements.tsv",
    "docs/research/hartmann-overunity-sources.tsv",
    "docs/research/v3-photo/node-map.tsv",
    "docs/research/v3-photo/connection-plan.tsv",
]:
    p = ROOT / item
    if not p.exists():
        continue
    try:
        with p.open("r", encoding="utf-8", newline="") as fh:
            rows = list(csv.reader(fh, delimiter="\t"))
        if not rows:
            errors.append(f"empty TSV: {item}")
            continue
        width = len(rows[0])
        for n, row in enumerate(rows[1:], start=2):
            if len(row) != width:
                errors.append(f"ragged TSV {item}:{n}: expected {width}, got {len(row)}")
        first_header = rows[0][0].strip().lower() if rows[0] else ""
        if first_header in {"id", "source_id", "node", "from"}:
            ids = [r[0].strip() for r in rows[1:] if r and r[0].strip()]
            seen: set[str] = set()
            duplicates: set[str] = set()
            for value in ids:
                if value in seen:
                    duplicates.add(value)
                seen.add(value)
            if duplicates:
                errors.append(f"duplicate IDs in {item}: {', '.join(sorted(duplicates))}")
    except Exception as exc:
        errors.append(f"TSV validation failed {item}: {exc}")

for p in ROOT.rglob("*.md"):
    if ".git" in p.parts:
        continue
    try:
        text = p.read_text(encoding="utf-8")
    except Exception as exc:
        errors.append(f"UTF-8 read failed {rel(p)}: {exc}")
        continue
    for target in LINK_RE.findall(text):
        target = target.strip().split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:", "data:")):
            continue
        target = target.replace("%20", " ")
        candidate = (p.parent / target).resolve()
        try:
            candidate.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"link escapes repository in {rel(p)}: {target}")
            continue
        if not candidate.exists():
            errors.append(f"broken local link in {rel(p)}: {target}")

pixel = ROOT / "docs/research/v3-photo/pixel-analysis.md"
if pixel.exists() and "Baumann's explanation felt like an unknown language" in pixel.read_text(encoding="utf-8"):
    errors.append("stale unverified Marinov/unknown-language attribution returned in V3 pixel analysis")

state = (ROOT / "STATE.md").read_text(encoding="utf-8", errors="replace") if (ROOT / "STATE.md").exists() else ""
if "testatika.zip" in state and "not part of the public repository" not in state.lower() and "nicht bestandteil" not in state.lower():
    warnings.append("STATE.md mentions testatika.zip without an obvious public-repository exclusion marker")

# V4 source-level semantic guardrails are checked even before binary materialization.
v4_doc = (ROOT / "docs/research/v4-best-evidence-m2.md").read_text(encoding="utf-8", errors="replace") if (ROOT / "docs/research/v4-best-evidence-m2.md").exists() else ""
for required_phrase in ("individually floating", "two external", "R4", "Blackbox"):
    if required_phrase.lower() not in v4_doc.lower():
        errors.append(f"V4 build contract missing semantic guardrail: {required_phrase}")

try:
    import trimesh

    baseline_dir = ROOT / "hardware/stl"
    experimental_dir = ROOT / "hardware/experimental"
    stls = sorted(set(baseline_dir.glob("*.stl")) | set(experimental_dir.rglob("*.stl")))
    loaded = {}
    for p in stls:
        mesh = trimesh.load_mesh(p, force="mesh")
        loaded[p.resolve()] = mesh
        if len(mesh.vertices) < 3 or len(mesh.faces) < 1:
            errors.append(f"invalid mesh: {rel(p)}")
        if any(float(x) <= 0 for x in mesh.extents):
            errors.append(f"zero extent: {rel(p)}")

    # Protect the published baseline geometry against accidental silent drift.
    dim_ledger = json.loads((ROOT / "docs/research/stl_dimensions.json").read_text(encoding="utf-8"))
    tolerance_mm = 0.30
    for filename, expected in dim_ledger.items():
        p = (baseline_dir / filename).resolve()
        if not p.exists():
            errors.append(f"dimension-ledger STL missing: hardware/stl/{filename}")
            continue
        mesh = loaded.get(p)
        if mesh is None:
            mesh = trimesh.load_mesh(p, force="mesh")
        actual = [float(x) for x in mesh.extents]
        if len(expected) != 3:
            errors.append(f"invalid dimension ledger entry for {filename}: {expected}")
            continue
        for axis, (a, e) in enumerate(zip(actual, expected)):
            if abs(a - float(e)) > tolerance_mm:
                errors.append(
                    f"dimension drift {filename} axis {axis}: actual {a:.3f} mm, ledger {float(e):.3f} mm"
                )
except Exception as exc:
    errors.append(f"trimesh/dimension validation failed: {exc}")

for p in list((ROOT / "hardware/step").glob("*.step")) + list((ROOT / "hardware/experimental").rglob("*.step")) + list((ROOT / "hardware/complete-model").glob("*.step")):
    if p.stat().st_size < 128:
        errors.append(f"suspiciously small STEP: {rel(p)}")

if warnings:
    print("VALIDATION WARNINGS")
    for warning in warnings:
        print("-", warning)

if errors:
    print("VALIDATION FAILED")
    for error in errors:
        print("-", error)
    sys.exit(1)

print("VALIDATION OK")
print("Baseline STL files:", len(list((ROOT / "hardware/stl").glob("*.stl"))))
print("Baseline STEP files:", len(list((ROOT / "hardware/step").glob("*.step"))))
print("Experimental STL files:", len(list((ROOT / "hardware/experimental").rglob("*.stl"))))
print("Experimental STEP files:", len(list((ROOT / "hardware/experimental").rglob("*.step"))))
