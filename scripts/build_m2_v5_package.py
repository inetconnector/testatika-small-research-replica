#!/usr/bin/env python3
from __future__ import annotations
import hashlib
from pathlib import Path
import zipfile
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"release"/"fabrication-kits"; OUT.mkdir(parents=True,exist_ok=True)
ZIP=OUT/"testatika-m2-v5-fabrication-kit.zip"; SHA=ZIP.with_suffix(ZIP.suffix+".sha256")
FILES=[
 "cad/generate_m2_v5_fabrication_kit.py","scripts/check_build_kits.py","scripts/normalize_buildkit_step.py",
 "docs/build-kits.md","docs/research/m2-v5-fabrication-kit.md","docs/research/v4-bom.md","docs/research/v4-assembly.md",
 "docs/research/v4-electrical-boundary.md","docs/research/safety.md","docs/REPLICATION_STATUS.md"]
DIRS=["hardware/build-kits/m2-v5"]
FIXED=(2026,8,17,0,0,0)
def entries():
 seen=set()
 for rel in FILES:
  p=ROOT/rel
  if not p.is_file(): raise FileNotFoundError(rel)
  seen.add(rel); yield rel,p
 for rd in DIRS:
  for p in sorted((ROOT/rd).rglob("*")):
   if p.is_file():
    rel=p.relative_to(ROOT).as_posix()
    if rel not in seen: seen.add(rel); yield rel,p
def main():
 with zipfile.ZipFile(ZIP,"w",zipfile.ZIP_DEFLATED,compresslevel=9) as zf:
  for rel,p in entries():
   info=zipfile.ZipInfo(rel,FIXED); info.compress_type=zipfile.ZIP_DEFLATED; info.external_attr=0o100644<<16
   zf.writestr(info,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
 d=hashlib.sha256(ZIP.read_bytes()).hexdigest(); SHA.write_text(f"{d}  {ZIP.name}\n",encoding="utf-8"); print(d)
if __name__=="__main__": main()
