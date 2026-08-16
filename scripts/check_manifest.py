#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest_path = ROOT / "MANIFEST.json"
sha_path = ROOT / "MANIFEST_SHA256.txt"
errors: list[str] = []

try:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
except Exception as exc:
    raise SystemExit(f"cannot parse MANIFEST.json: {exc}")

entries = manifest.get("files", [])
if manifest.get("algorithm") != "sha256":
    errors.append("MANIFEST.json algorithm is not sha256")
if manifest.get("file_count") != len(entries):
    errors.append("MANIFEST.json file_count mismatch")

seen: set[str] = set()
ledger_lines: list[str] = []
for entry in entries:
    rel = entry.get("path", "")
    if not rel or rel in seen:
        errors.append(f"missing/duplicate manifest path: {rel!r}")
        continue
    seen.add(rel)
    p = ROOT / rel
    if not p.is_file():
        errors.append(f"manifest file missing: {rel}")
        continue
    data = p.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if len(data) != entry.get("size"):
        errors.append(f"size mismatch: {rel}")
    if digest != entry.get("sha256"):
        errors.append(f"sha256 mismatch: {rel}")
    ledger_lines.append(f"{digest}  {rel}\n")

expected_ledger = "".join(ledger_lines)
actual_ledger = sha_path.read_text(encoding="utf-8") if sha_path.exists() else ""
if actual_ledger != expected_ledger:
    errors.append("MANIFEST_SHA256.txt does not match MANIFEST.json/current files")

if errors:
    print("MANIFEST CHECK FAILED")
    for error in errors:
        print("-", error)
    sys.exit(1)

print(f"MANIFEST CHECK OK: {len(entries)} files")
