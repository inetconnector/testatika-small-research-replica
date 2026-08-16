#!/usr/bin/env python3
from pathlib import Path
import hashlib, zipfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "release"
OUT.mkdir(exist_ok=True)
version = "v0.2.0"
zip_path = OUT / f"testatika-small-research-replica-{version}.zip"

items = [
    ROOT/"hardware",
    ROOT/"docs",
    ROOT/"README.md",
    ROOT/"STATE.md",
    ROOT/"LICENSE",
    ROOT/"NOTICE.md",
]

files=[]
for item in items:
    if item.is_file():
        files.append(item)
    elif item.is_dir():
        files.extend(p for p in item.rglob("*") if p.is_file())

with zipfile.ZipFile(zip_path,"w",zipfile.ZIP_DEFLATED) as z:
    for p in sorted(files):
        z.write(p,p.relative_to(ROOT))

sha=hashlib.sha256(zip_path.read_bytes()).hexdigest()
(OUT/f"{zip_path.name}.sha256").write_text(f"{sha}  {zip_path.name}\n",encoding="utf-8")
print(zip_path)
