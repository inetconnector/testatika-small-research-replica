#!/usr/bin/env python3
"""Build deterministic V4 best-evidence M2 research/build package."""
from __future__ import annotations

import hashlib
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "release" / "experimental"
ZIP_PATH = OUT_DIR / "testatika-m2-v4-best-evidence-build-package.zip"
SHA_PATH = OUT_DIR / "testatika-m2-v4-best-evidence-build-package.zip.sha256"

INCLUDE_FILES = [
    "cad/generate_v4_best_evidence_m2.py",
    "scripts/check_v4_assets.py",
    "docs/REPLICATION_STATUS.md",
    "docs/research/v4-best-evidence-m2.md",
    "docs/research/v4-bom.md",
    "docs/research/v4-assembly.md",
    "docs/research/v4-electrical-boundary.md",
    "docs/research/v4-printing.md",
    "docs/research/v4-configurations.yaml",
    "docs/research/v4-experiment-sequence.md",
    "docs/research/replica-configuration-matrix.md",
    "docs/research/experiment-plan.md",
    "docs/research/safety.md",
    "docs/research/hauser-marinov-primary-scan-audit-2026-08-16.md",
    "docs/research/video-frame-audit-2026-08-16.md",
]
INCLUDE_DIRS = ["hardware/experimental/v4-best-evidence-m2"]
FIXED_TIME = (2026, 8, 16, 0, 0, 0)


def iter_files():
    seen = set()
    for rel in INCLUDE_FILES:
        path = ROOT / rel
        if not path.is_file():
            raise FileNotFoundError(rel)
        seen.add(rel)
        yield rel, path
    for rel_dir in INCLUDE_DIRS:
        directory = ROOT / rel_dir
        if not directory.is_dir():
            raise FileNotFoundError(rel_dir)
        for path in sorted(directory.rglob("*")):
            if path.is_file():
                rel = path.relative_to(ROOT).as_posix()
                if rel not in seen:
                    seen.add(rel)
                    yield rel, path


def build():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for rel, path in iter_files():
            info = zipfile.ZipInfo(rel, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            zf.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    digest = hashlib.sha256(ZIP_PATH.read_bytes()).hexdigest()
    SHA_PATH.write_text(f"{digest}  {ZIP_PATH.name}\n", encoding="utf-8")
    print(ZIP_PATH.relative_to(ROOT))
    print(digest)


if __name__ == "__main__":
    build()
