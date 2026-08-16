#!/usr/bin/env python3
"""Generate repository file manifest and SHA-256 ledger deterministically.

The generated files exclude themselves and Git metadata. Release ZIPs are included only
when already tracked/present, so a release can be independently integrity-checked.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "MANIFEST.json"
SHA_FILE = ROOT / "MANIFEST_SHA256.txt"
EXCLUDED = {
    "MANIFEST.json",
    "MANIFEST_SHA256.txt",
}
EXCLUDED_PARTS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}


def included(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    if rel in EXCLUDED:
        return False
    if any(part in EXCLUDED_PARTS for part in path.relative_to(ROOT).parts):
        return False
    return path.is_file()


entries = []
for path in sorted((p for p in ROOT.rglob("*") if included(p)), key=lambda p: p.relative_to(ROOT).as_posix()):
    data = path.read_bytes()
    entries.append({
        "path": path.relative_to(ROOT).as_posix(),
        "size": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    })

payload = {
    "schema_version": 2,
    "algorithm": "sha256",
    "generated_from": "working tree content; excludes MANIFEST.json and MANIFEST_SHA256.txt",
    "file_count": len(entries),
    "files": entries,
}
MANIFEST.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
SHA_FILE.write_text("".join(f"{e['sha256']}  {e['path']}\n" for e in entries), encoding="utf-8")
print(f"manifest entries: {len(entries)}")
