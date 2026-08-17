#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "docs/research/source-acquisition-backlog.tsv"
text = p.read_text(encoding="utf-8")
replacements = {
    "P0-MAGNETS-1984\t": "P0\t",
    "P1-TRIPP-NLS\t": "P1\t",
    "P1-NEN-1998-KELLY\t": "P1\t",
    "P1-EINSIEDELN-HOLDING\t": "P1\t",
}
for old, new in replacements.items():
    text = text.replace(old, new)
p.write_text(text, encoding="utf-8")
print("Round-2 acquisition priorities normalized.")
