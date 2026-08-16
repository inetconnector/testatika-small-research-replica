#!/usr/bin/env python3
"""Build deterministic M6 Large V1 research/build package."""
from __future__ import annotations
import hashlib
from pathlib import Path
import zipfile

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"release"/"experimental"
ZIP=OUT/"testatika-m6-large-v1-best-evidence-build-package.zip"
SHA=OUT/"testatika-m6-large-v1-best-evidence-build-package.zip.sha256"
FILES=[
    "cad/generate_m6_large_v1.py",
    "scripts/check_m6_assets.py",
    "scripts/normalize_m6_step.py",
    "docs/research/m6-large-v1-build-summary.md",
    "docs/research/m6-large-v1-best-evidence.md",
    "docs/research/m6-large-v1-bom.md",
    "docs/research/m6-large-v1-assembly.md",
    "docs/research/m6-large-v1-electrical-boundary.md",
    "docs/research/m6-large-v1-printing.md",
    "docs/research/m6-large-v1-configurations.yaml",
    "docs/research/m6-large-v1-experiment-sequence.md",
    "docs/research/m6-large-v1-reproducibility.md",
    "docs/research/m6-large-v1-source-map.tsv",
    "docs/research/m6-large-v1-terminal-map.tsv",
    "docs/M6_REPLICATION_STATUS.md",
    "docs/research/safety.md",
    "docs/research/hauser-marinov-primary-scan-audit-2026-08-16.md",
    "docs/research/video-frame-audit-2026-08-16.md",
    "docs/research/machines.yaml",
]
DIRS=["hardware/experimental/m6-large-v1-best-evidence"]
FIXED_TIME=(2026,8,17,0,0,0)


def entries():
    seen=set()
    for rel in FILES:
        p=ROOT/rel
        if not p.is_file(): raise FileNotFoundError(rel)
        seen.add(rel); yield rel,p
    for rd in DIRS:
        d=ROOT/rd
        if not d.is_dir(): raise FileNotFoundError(rd)
        for p in sorted(d.rglob("*")):
            if p.is_file():
                rel=p.relative_to(ROOT).as_posix()
                if rel not in seen:
                    seen.add(rel); yield rel,p


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(ZIP,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=9) as zf:
        for rel,p in entries():
            info=zipfile.ZipInfo(rel,FIXED_TIME); info.compress_type=zipfile.ZIP_DEFLATED; info.external_attr=0o100644<<16
            zf.writestr(info,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
    digest=hashlib.sha256(ZIP.read_bytes()).hexdigest()
    SHA.write_text(f"{digest}  {ZIP.name}\n",encoding="utf-8")
    print(ZIP.relative_to(ROOT)); print(digest)

if __name__ == "__main__": main()
