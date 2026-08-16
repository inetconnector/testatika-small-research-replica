#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "release"
OUT.mkdir(exist_ok=True)
VERSION = "v0.3.0"
ZIP_PATH = OUT / f"testatika-small-research-replica-{VERSION}.zip"

# Complete research package. Historical release ZIPs are deliberately not nested.
INCLUDE = [
    "README.md",
    "STATE.md",
    "addon.md",
    "ADDON.md",
    "AGENTS.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "CONTRIBUTING.md",
    "LICENSE",
    "NOTICE.md",
    "PRESERVATION.md",
    "ROADMAP.md",
    "SECURITY.md",
    "MANIFEST.json",
    "MANIFEST_SHA256.txt",
    "requirements-cad.txt",
    "requirements-dev.txt",
    "cad",
    "docs",
    "hardware",
    "scripts",
]

files: set[Path] = set()
for rel in INCLUDE:
    item = ROOT / rel
    if not item.exists():
        raise SystemExit(f"missing release input: {rel}")
    if item.is_file():
        files.add(item)
    else:
        files.update(p for p in item.rglob("*") if p.is_file())

# Avoid self-inclusion and local caches/scratch even if future include roots expand.
files = {
    p for p in files
    if OUT not in p.parents
    and "__pycache__" not in p.parts
    and ".git" not in p.parts
}

with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for p in sorted(files, key=lambda x: x.relative_to(ROOT).as_posix()):
        archive.write(p, p.relative_to(ROOT).as_posix())

sha = hashlib.sha256(ZIP_PATH.read_bytes()).hexdigest()
sha_path = OUT / f"{ZIP_PATH.name}.sha256"
sha_path.write_text(f"{sha}  {ZIP_PATH.name}\n", encoding="utf-8")
print(ZIP_PATH)
print(sha_path)
print(f"files: {len(files)}")
