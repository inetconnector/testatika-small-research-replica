#!/usr/bin/env python3
"""Build the annotated V3 working map from the repository's historical Testatika image.

This script only adds labels/arrows; it does not alter the source interpretation data.
The historical image itself remains third-party material subject to its own rights.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "docs/publications/net-journal/Testatika_historisches_Foto.jpg"
OUT = ROOT / "docs/images/small_machine_v3_annotation.png"


def font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for p in candidates:
        try:
            return ImageFont.truetype(p, size)
        except OSError:
            pass
    return ImageFont.load_default()


def main():
    img = Image.open(SRC).convert("RGB")
    d = ImageDraw.Draw(img)
    f = font(20)
    fb = font(22, True)

    labels = [
        ((682,44),(870,24),'A  top "crystal" module'),
        ((1166,206),(1260,150),'B  right outer collector panel'),
        ((180,208),(6,150),'C  left outer collector panel'),
        ((570,260),(390,220),'D  left spring-loaded tower'),
        ((830,260),(1010,220),'E  right spring-loaded tower'),
        ((816,374),(1030,340),'F  right slanted pickup bar'),
        ((552,374),(316,340),'G  left slanted pickup bar'),
        ((698,545),(944,540),'H  hub / rotor center'),
        ((418,645),(290,760),'I  left lower clover plate'),
        ((944,645),(1072,760),'J  right lower clover plate'),
        ((190,915),(5,1005),'K  left storage pot'),
        ((1168,915),(1276,1005),'L  right storage pot'),
        ((686,995),(892,1080),'M  lower front collector'),
        ((552,876),(405,1010),'N  left lower spring'),
        ((840,876),(980,1010),'O  right lower spring'),
    ]

    for src, dst, txt in labels:
        d.line([src, dst], fill=(255,0,0), width=3)
        x, y = dst
        bbox = d.textbbox((x,y), txt, font=f)
        d.rounded_rectangle((bbox[0]-4,bbox[1]-2,bbox[2]+4,bbox[3]+2), radius=4,
                            fill=(255,255,240), outline=(180,0,0), width=2)
        d.text((x,y), txt, fill=(0,0,0), font=f)

    d.rectangle((0,0,img.width,34), fill=(0,0,0))
    d.text((12,6), 'Annotated working map — Testatika small machine V3 photo interpretation',
           fill=(255,255,255), font=fb)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()
