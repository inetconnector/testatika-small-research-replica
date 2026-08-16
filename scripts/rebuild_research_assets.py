#!/usr/bin/env python3
"""Rebuild all currently source-reproducible research assets.

This script intentionally does not delete or overwrite binary-only legacy assets beyond
the outputs owned by the existing generators. See docs/research/cad-reproducibility.md.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMMANDS = [
    [sys.executable, "cad/generate_v2.py"],
    [sys.executable, "cad/generate_v3_experiments.py"],
    [sys.executable, "cad/generate_v3_photo_interp.py"],
]

for command in COMMANDS:
    print("+", " ".join(command))
    subprocess.run(command, cwd=ROOT, check=True)

print("Source-reproducible CAD families rebuilt.")
print("Preserved binary-only/legacy assets were not deleted.")
