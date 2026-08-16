#!/usr/bin/env python3
"""Normalize volatile OpenCascade STEP header metadata for V4 reproducibility.

OpenCascade writes the current export timestamp into FILE_NAME. That makes byte hashes
change on every rebuild even when geometry is identical. This script rewrites only the
volatile STEP header timestamp to a fixed value; DATA geometry is untouched.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
V4 = ROOT / "hardware" / "experimental" / "v4-best-evidence-m2"
FIXED_TIMESTAMP = "2000-01-01T00:00:00"
PATTERN = re.compile(r"(FILE_NAME\('[^']*',)'[^']*'")


def normalize(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    replacement = rf"\1'{FIXED_TIMESTAMP}'"
    updated, count = PATTERN.subn(replacement, text, count=1)
    if count != 1:
        raise SystemExit(f"could not locate STEP FILE_NAME timestamp: {path.relative_to(ROOT)}")
    if updated == text:
        return False
    path.write_text(updated, encoding="utf-8", newline="\n")
    return True


def main():
    step_files = sorted(V4.rglob("*.step"))
    if not step_files:
        raise SystemExit("no V4 STEP files found to normalize")
    changed = 0
    for path in step_files:
        if normalize(path):
            changed += 1
    print(f"Normalized {changed}/{len(step_files)} V4 STEP headers to {FIXED_TIMESTAMP}.")


if __name__ == "__main__":
    main()
