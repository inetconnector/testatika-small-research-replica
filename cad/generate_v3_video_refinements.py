#!/usr/bin/env python3
"""
Source-reproducible V3 geometry refinements derived from the complete historical
video audit, especially meth4.asf matched to testabig.jpg.

These parts improve visible external geometry only. They do NOT claim recovered
historical electrical connections, materials, dimensions or internal circuitry.

Generated families:
- hub_arc_pair_video_refined
- lower_central_cage_video_refined
- outer_panel_layered_video_refined
"""
from pathlib import Path
import cadquery as cq

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "hardware" / "experimental" / "v3-video-refinements"
STL = OUT / "stl"
STEP = OUT / "step"
for p in (STL, STEP):
    p.mkdir(parents=True, exist_ok=True)


def rr(w, d, h, r=1.5):
    o = cq.Workplane("XY").box(w, d, h, centered=(True, True, False))
    try:
        o = o.edges("|Z").fillet(r)
    except Exception:
        pass
    return o


def export_pair(name, obj):
    cq.exporters.export(
        obj,
        str(STL / f"{name}.stl"),
        tolerance=0.10,
        angularTolerance=0.20,
    )
    cq.exporters.export(obj, str(STEP / f"{name}.step"))


def hub_arc_pair(inner_r=18.0, outer_r=23.0, thickness=2.2, center_gap=7.0):
    """Two C-shaped hub arcs visible in meth4/testabig.

    Dimensions are working photo/video-fit values, not original measurements.
    Electrical connection is intentionally absent from the CAD source.
    """
    ring = cq.Workplane("XY").circle(outer_r).circle(inner_r).extrude(thickness)
    center_cut = (
        cq.Workplane("XY")
        .rect(center_gap, outer_r * 2.4)
        .extrude(thickness + 2.0)
        .translate((0, 0, -1.0))
    )
    return ring.cut(center_cut)


def perforated_cage(w=24.0, d=18.0, h=70.0, wall=2.0):
    """Working cage/prism interpretation of the lower central visible module."""
    body = cq.Workplane("XY").box(w, d, h, centered=(True, True, False))
    inner = (
        cq.Workplane("XY")
        .box(w - 2 * wall, d - 2 * wall, h - 8.0, centered=(True, True, False))
        .translate((0, 0, 4.0))
    )
    body = body.cut(inner)

    # Repeated through-openings make the source geometry visibly cage-like.
    # Hole count/size are video-fit working values and remain tunable.
    for z in range(10, int(h) - 7, 12):
        for x in (-6, 6):
            tool = (
                cq.Workplane("XZ")
                .center(x, z)
                .rect(6, 7)
                .extrude(d + 2.0, both=True)
            )
            body = body.cut(tool)
    return body


def layered_outer_panel():
    """Visible layered outer-panel interpretation from meth4 close-ups.

    Layers are kept as geometry only: coarse carrier, finer inset region and
    elongated edge element. Material/conductivity remains an experiment variable.
    """
    carrier = cq.Workplane("XY").rect(88, 74).extrude(2.5)
    for x in (-30, -20, -10, 0, 10, 20, 30):
        for y in (-24, -12, 0, 12, 24):
            carrier = carrier.cut(
                cq.Workplane("XY")
                .center(x, y)
                .rect(4, 6)
                .extrude(4.0)
                .translate((0, 0, -1.0))
            )

    inset = cq.Workplane("XY").rect(54, 28).extrude(1.5).translate((0, -10, 3.0))
    for x in (-20, -12, -4, 4, 12, 20):
        for y in (-8, 0, 8):
            inset = inset.cut(
                cq.Workplane("XY")
                .center(x, y - 10)
                .rect(4, 4)
                .extrude(3.0)
                .translate((0, 0, 2.5))
            )

    edge_element = rr(56, 5, 4, 0.8).translate((0, 14, 3.0))
    return carrier.union(inset).union(edge_element)


def main():
    export_pair("hub_arc_pair_video_refined", hub_arc_pair())
    export_pair("lower_central_cage_video_refined", perforated_cage())
    export_pair("outer_panel_layered_video_refined", layered_outer_panel())
    print("V3 video-derived refinement assets generated.")


if __name__ == "__main__":
    main()
