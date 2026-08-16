#!/usr/bin/env python3
"""Repository-wide structural validator.

This intentionally validates research integrity and asset structure without trying to
prove historical claims. It catches stale paths, malformed ledgers, missing core assets
and broken local Markdown links in addition to basic mesh validity.
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
    "docs/research/evidence_matrix.tsv",
    "docs/research/baumann-statements.tsv",
    "docs/research/hartmann-overunity-sources.tsv",
    "docs/research/assembly.md",
    "docs/research/safety.md",
    "docs/research/experiment-plan.md",
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

try:
    import trimesh

    stls = sorted(set((ROOT / "hardware/stl").glob("*.stl")) | set((ROOT / "hardware/experimental").rglob("*.stl")))
    for p in stls:
        mesh = trimesh.load_mesh(p, force="mesh")
        if len(mesh.vertices) < 3 or len(mesh.faces) < 1:
            errors.append(f"invalid mesh: {rel(p)}")
        if any(float(x) <= 0 for x in mesh.extents):
            errors.append(f"zero extent: {rel(p)}")
except Exception as exc:
    errors.append(f"trimesh validation failed: {exc}")

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
