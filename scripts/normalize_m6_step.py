#!/usr/bin/env python3
"""Normalize volatile OpenCascade STEP header metadata for M6 Large V1."""
from __future__ import annotations
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "hardware" / "experimental" / "m6-large-v1-best-evidence"
FIXED_TIMESTAMP = "2000-01-01T00:00:00"
PATTERN = re.compile(r"(FILE_NAME\('[^']*',)'[^']*'")


def normalize(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    updated, count = PATTERN.subn(rf"\1'{FIXED_TIMESTAMP}'", text, count=1)
    if count != 1:
        raise SystemExit(f"could not locate STEP FILE_NAME timestamp: {path.relative_to(ROOT)}")
    if updated == text:
        return False
    path.write_text(updated, encoding="utf-8", newline="\n")
    return True


def main():
    files = sorted(BASE.rglob("*.step"))
    if not files:
        raise SystemExit("no M6 STEP files found")
    changed = sum(1 for p in files if normalize(p))
    print(f"Normalized {changed}/{len(files)} M6 STEP headers to {FIXED_TIMESTAMP}.")

if __name__ == "__main__":
    main()
