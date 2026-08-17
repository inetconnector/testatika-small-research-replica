#!/usr/bin/env python3
"""Normalize volatile OpenCascade STEP header timestamps in build-kit outputs."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [ROOT / "hardware" / "build-kits" / "m2-v5", ROOT / "hardware" / "build-kits" / "m6-v2"]
FIXED = "2000-01-01T00:00:00"
PATTERN = re.compile(r"(FILE_NAME\('[^']*',)'[^']*'")


def normalize(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    updated, count = PATTERN.subn(rf"\1'{FIXED}'", text, count=1)
    if count != 1:
        raise SystemExit(f"could not locate STEP timestamp: {path.relative_to(ROOT)}")
    if updated != text:
        path.write_text(updated, encoding="utf-8", newline="\n")
        return True
    return False


def main():
    files = []
    for target in TARGETS:
        files.extend(sorted(target.rglob("*.step")))
    if not files:
        raise SystemExit("no build-kit STEP files found")
    changed = sum(1 for p in files if normalize(p))
    print(f"Normalized {changed}/{len(files)} build-kit STEP headers to {FIXED}.")

if __name__ == "__main__":
    main()
