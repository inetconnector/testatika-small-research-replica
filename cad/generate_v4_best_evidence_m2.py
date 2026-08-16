#!/usr/bin/env python3
"""
V4 best-evidence CAD generator for the Marinov first small Testatika (M2).

This generator integrates the strongest surviving M2 constraints after the complete
archive, Marinov/Hauser scan and historical-video audits. It intentionally separates
historical baseline geometry from unresolved electrical hypotheses.

Baseline encoded here:
- one ~200 mm rotor;
- 20/24/25 individually floating ~1 mm wire-sector positions;
- no rubbing collector brushes;
- two side condenser/pot modules with outer grid + dielectric + inner Cu spiral;
- two external pot terminals per side in the historical baseline;
- two horseshoe-magnet positions for the first small-machine visual baseline;
- video-refined hub arcs, layered outer panels and lower central cage;
- removable top "crystal" black-box carrier with two populated visible posts and
  four isolated research terminal positions available without asserting topology;
- no built-in conventional drive motor.

All photo/video-fit dimensions that are not direct source measurements remain working
values. Generated geometry is a research reconstruction, not a claim of recovered
original electrical wiring or anomalous energy performance.
"""
from __future__ import annotations

from pathlib import Path
import json
import math
import cadquery as cq

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "hardware" / "experimental" / "v4-best-evidence-m2"
STL = OUT / "stl"
STEP = OUT / "step"
COMP = OUT / "complete-model"
META = OUT / "metadata"
for p in (STL, STEP, COMP, META):
    p.mkdir(parents=True, exist_ok=True)

BASE_W, BASE_D, BASE_T = 370.0, 180.0, 30.0
BACK_W, BACK_H, BACK_T = 336.0, 246.0, 8.0
ROTOR_D, ROTOR_T = 200.0, 3.5
SHAFT_D = 8.2
POT_OD, POT_H = 84.0, 110.0


def rr(w: float, d: float, h: float, r: float = 2.0):
    obj = cq.Workplane("XY").box(w, d, h, centered=(True, True, False))
    try:
        obj = obj.edges("|Z").fillet(r)
    except Exception:
        pass
    return obj


def export_pair(name: str, obj):
    cq.exporters.export(obj, str(STL / f"{name}.stl"), tolerance=0.10, angularTolerance=0.20)
    cq.exporters.export(obj, str(STEP / f"{name}.step"))


def perforated_plate(w, h, t, cols, rows, hole_w=4.0, hole_h=5.0, frame=5.0):
    p = cq.Workplane("XY").rect(w, h).extrude(t)
    x0, x1 = -w / 2 + frame, w / 2 - frame
    y0, y1 = -h / 2 + frame, h / 2 - frame
    xs = [x0 + i * ((x1 - x0) / max(cols - 1, 1)) for i in range(cols)]
    ys = [y0 + j * ((y1 - y0) / max(rows - 1, 1)) for j in range(rows)]
    for x in xs:
        for y in ys:
            p = p.cut(cq.Workplane("XY").center(x, y).rect(hole_w, hole_h).extrude(t + 2.0).translate((0, 0, -1.0)))
    return p


def base_board():
    return rr(BASE_W, BASE_D, BASE_T, 4.0)


def backplate():
    return rr(BACK_W, BACK_T, BACK_H, 6.0).rotate((0, 0, 0), (1, 0, 0), 90)


def rotor_floating(count=24, route="R0"):
    """Mechanical rotor for individually floating conductor sectors.

    R0 is the conservative one-side radial working baseline. R4 adds the three-side-
    change drill pattern as a research geometry but does not electrically connect
    neighbouring sectors. Conductors themselves are installed as separate wires.
    """
    p = cq.Workplane("XY").circle(ROTOR_D / 2).extrude(ROTOR_T)
    p = p.faces(">Z").workplane().hole(SHAFT_D)
    for a in range(0, 360, 60):
        x = 15 * math.cos(math.radians(a))
        y = 15 * math.sin(math.radians(a))
        p = p.faces(">Z").workplane().center(x, y).hole(3.2)
    radii = (27.0, 94.0) if route == "R0" else (27.0, 40.0, 60.0, 80.0, 94.0)
    for i in range(count):
        a = math.radians(i * 360 / count)
        for rad in radii:
            x = rad * math.cos(a)
            y = rad * math.sin(a)
            p = p.faces(">Z").workplane().center(x, y).hole(1.75)
    return p


def hub_disk():
    h = cq.Workplane("XY").circle(28).circle(12).extrude(10)
    h = h.faces(">Z").workplane().hole(SHAFT_D)
    for a in range(0, 360, 60):
        x = 15 * math.cos(math.radians(a))
        y = 15 * math.sin(math.radians(a))
        h = h.faces(">Z").workplane().center(x, y).hole(3.2)
    return h


def hub_arc_pair(inner_r=18.0, outer_r=23.0, thickness=2.2, center_gap=7.0):
    ring = cq.Workplane("XY").circle(outer_r).circle(inner_r).extrude(thickness)
    center_cut = cq.Workplane("XY").rect(center_gap, outer_r * 2.4).extrude(thickness + 2.0).translate((0, 0, -1.0))
    return ring.cut(center_cut)


def pot_shell():
    p = cq.Workplane("XY").circle(POT_OD / 2).circle(POT_OD / 2 - 2.5).extrude(POT_H)
    p = p.union(cq.Workplane("XY").circle(46).circle(31).extrude(7))
    p = p.union(cq.Workplane("XY").circle(46).circle(31).extrude(7).translate((0, 0, POT_H - 7)))
    return p


def pot_grid_former():
    return cq.Workplane("XY").circle(37).circle(35).extrude(96)


def pot_dielectric_sleeve_jig():
    return cq.Workplane("XY").circle(33).circle(31).extrude(92)


def pot_spiral_mandrel():
    return (cq.Workplane("XY").circle(21).circle(18).extrude(88)
            .union(cq.Workplane("XY").circle(25).circle(18).extrude(4))
            .union(cq.Workplane("XY").circle(25).circle(18).extrude(4).translate((0, 0, 84))))


def pot_terminal_lid_2wire():
    lid = cq.Workplane("XY").circle(42).extrude(5)
    lid = lid.faces(">Z").workplane().hole(18.0)
    for x in (-16.0, 16.0):
        lid = lid.faces(">Z").workplane().center(x, 0).hole(4.2)
    return lid


def pot_visual_assembly():
    return (pot_shell()
            .union(pot_grid_former().translate((0, 0, 7)))
            .union(pot_dielectric_sleeve_jig().translate((0, 0, 9)))
            .union(pot_spiral_mandrel().translate((0, 0, 11)))
            .union(pot_terminal_lid_2wire().translate((0, 0, POT_H))))


def layered_outer_panel():
    carrier = perforated_plate(88, 74, 2.5, 7, 5, 4, 6, 9)
    inset = perforated_plate(54, 28, 1.5, 6, 3, 4, 4, 4).translate((0, -10, 3.0))
    edge_element = rr(56, 5, 4, 0.8).translate((0, 14, 3.0))
    leads = (cq.Workplane("XY").circle(2.0).extrude(8).translate((-25, 19, 3))
             .union(cq.Workplane("XY").circle(2.0).extrude(8).translate((25, 19, 3))))
    return carrier.union(inset).union(edge_element).union(leads)


def lower_central_cage(w=24.0, d=18.0, h=70.0, wall=2.0):
    body = cq.Workplane("XY").box(w, d, h, centered=(True, True, False))
    inner = cq.Workplane("XY").box(w - 2 * wall, d - 2 * wall, h - 8.0, centered=(True, True, False)).translate((0, 0, 4.0))
    body = body.cut(inner)
    for z in range(10, int(h) - 7, 12):
        for x in (-6, 6):
            body = body.cut(cq.Workplane("XZ").center(x, z).rect(6, 7).extrude(d + 2, both=True))
    return body


def top_crystal_carrier():
    body = rr(170, 28, 18, 3)
    center = perforated_plate(100, 30, 3, 10, 4, 5, 5, 5).translate((0, 0, 18))
    ends = perforated_plate(34, 26, 3, 4, 3, 4, 4, 4).translate((-68, 0, 18)).union(
        perforated_plate(34, 26, 3, 4, 3, 4, 4, 4).translate((68, 0, 18)))
    for x in (-52, -36, 36, 52):
        body = body.faces(">Z").workplane().center(x, 0).hole(3.2)
    return body.union(center).union(ends)


def visible_crystal_posts():
    return (cq.Workplane("XY").circle(2.2).extrude(18).translate((-36, 0, 0))
            .union(cq.Workplane("XY").circle(2.2).extrude(18).translate((36, 0, 0))))


def upper_tower():
    return (rr(34, 26, 22, 2)
            .union(rr(4, 4, 74, 1).translate((-13, 0, 22)))
            .union(rr(4, 4, 74, 1).translate((13, 0, 22)))
            .union(cq.Workplane("YZ").circle(10).extrude(6, both=True).translate((0, 0, 96))))


def pickup_bar():
    return perforated_plate(70, 18, 3, 7, 2, 4, 4, 4).union(rr(24, 10, 8, 1).translate((-22, 0, -8)))


def crossbar_long():
    return perforated_plate(110, 18, 3, 10, 2, 4, 4, 4)


def crossbar_short():
    return perforated_plate(36, 30, 3, 4, 3, 4, 4, 4)


def lower_clover_plate():
    base = rr(44, 34, 3, 1.2)
    for row in range(3):
        n = 4 - row
        for col in range(n):
            x = col * 12 - (n - 1) * 6 + row * 6
            y = row * 10 - 10
            base = base.cut(cq.Workplane("XY").center(x, y).circle(3.8).extrude(5).translate((0, 0, -1)))
    return base


def spring_wire(height=62.0, turns=8.5, radius=5.0, wire_r=0.75):
    helix = cq.Wire.makeHelix(pitch=height / turns, height=height, radius=radius)
    return cq.Workplane("XZ").circle(wire_r).sweep(helix)


def horseshoe_magnet_shape():
    return (rr(10, 22, 35, 2).translate((-17, 0, 0))
            .union(rr(10, 22, 35, 2).translate((17, 0, 0)))
            .union(rr(44, 22, 10, 2).translate((0, 0, 35))))


def horseshoe_dummy():
    return horseshoe_magnet_shape()


def guard_post():
    return rr(10, 10, 210, 1.5)


def build_complete(rotor_count=24, route="R0", include_real_magnet_geometry=True):
    parts = [base_board()]
    parts.append(backplate().translate((0, -BASE_D / 2 + BACK_T / 2 + 8, BASE_T)))
    parts.append(rotor_floating(rotor_count, route).rotate((0, 0, 0), (1, 0, 0), 90).translate((0, -10, 160)))
    parts.append(hub_disk().rotate((0, 0, 0), (1, 0, 0), 90).translate((0, -5.5, 160)))
    parts.append(hub_disk().rotate((0, 0, 0), (1, 0, 0), 90).translate((0, -14.5, 160)))
    parts.append(hub_arc_pair().rotate((0, 0, 0), (1, 0, 0), 90).translate((0, -0.5, 160)))
    parts.append(pot_visual_assembly().translate((-143, -4, 30)))
    parts.append(pot_visual_assembly().translate((143, -4, 30)))
    top = top_crystal_carrier().union(visible_crystal_posts().translate((0, 0, 18)))
    parts.append(top.rotate((0, 0, 0), (1, 0, 0), 90).translate((0, -6, 258)))
    parts.append(perforated_plate(18, 88, 4, 2, 8, 4, 4, 4).rotate((0, 0, 0), (1, 0, 0), 90).translate((0, -4, 169)))
    parts.append(layered_outer_panel().rotate((0, 0, 0), (1, 0, 0), 90).translate((-118, -8, 210)))
    parts.append(layered_outer_panel().rotate((0, 0, 0), (1, 0, 0), 90).translate((118, -8, 210)))
    parts.append(lower_central_cage().translate((0, -6, 48)))
    parts.append(upper_tower().rotate((0, 0, 0), (1, 0, 0), 90).translate((-47, -8, 168)))
    parts.append(upper_tower().rotate((0, 0, 0), (1, 0, 0), 90).translate((47, -8, 168)))
    parts.append(spring_wire().rotate((0, 0, 0), (1, 0, 0), 90).translate((-47, -1, 176)))
    parts.append(spring_wire().rotate((0, 0, 0), (1, 0, 0), 90).translate((47, -1, 176)))
    parts.append(spring_wire(74, 12, 5, 0.7).rotate((0, 0, 0), (1, 0, 0), 90).translate((-57, -1, 58)))
    parts.append(spring_wire(74, 12, 5, 0.7).rotate((0, 0, 0), (1, 0, 0), 90).translate((57, -1, 58)))
    parts.append(pickup_bar().rotate((0, 0, 0), (0, 0, 1), -36).rotate((0, 0, 0), (1, 0, 0), 90).translate((-23, -1, 180)))
    parts.append(pickup_bar().rotate((0, 0, 0), (0, 0, 1), 36).rotate((0, 0, 0), (1, 0, 0), 90).translate((23, -1, 180)))
    parts.append(crossbar_long().rotate((0, 0, 0), (1, 0, 0), 90).translate((-71, -6, 122)))
    parts.append(crossbar_long().rotate((0, 0, 0), (1, 0, 0), 90).translate((71, -6, 122)))
    for x, z in ((-38, 126), (38, 126), (-20, 98), (20, 98)):
        parts.append(crossbar_short().rotate((0, 0, 0), (1, 0, 0), 90).translate((x, -6, z)))
    parts.append(lower_clover_plate().rotate((0, 0, 0), (1, 0, 0), 90).translate((-94, -4, 87)))
    parts.append(lower_clover_plate().rotate((0, 0, 0), (1, 0, 0), 90).translate((94, -4, 87)))
    magnet = horseshoe_magnet_shape() if include_real_magnet_geometry else horseshoe_dummy()
    parts.append(magnet.translate((-44, -8, 30)))
    parts.append(magnet.translate((44, -8, 30)))
    return cq.Compound.makeCompound([p.val() for p in parts])


def write_metadata():
    data = {
        "name": "Testatika_M2_V4_BEST_EVIDENCE",
        "machine_id": "M2",
        "status": "best-evidence research reconstruction; historical wiring incomplete",
        "baseline": {
            "rotor_diameter_mm": 200,
            "nominal_sector_count": 24,
            "alternate_sector_counts": [20, 25],
            "sector_electrical_state": "individually floating; no neighbour ring",
            "nominal_route": "R0 conservative straight radial working baseline; exact historical route unknown",
            "collector_contact": "none; non-contact architecture",
            "pot_external_terminals_each": 2,
            "pot_internal_class": "outer grid + dielectric + inner copper spiral",
            "conventional_drive_motor": "absent from historical baseline",
            "horseshoe_magnets": "present in first-small-machine visual baseline; function unknown",
            "crystal": "black-box; material/function/topology unknown"
        },
        "video_derived_refinements": [
            "two C-shaped hub-arc component candidates",
            "layered outer panels",
            "perforated lower central cage/prism"
        ],
        "not_claimed": [
            "exact through-disc wire route",
            "complete node wiring",
            "pot polarity/capacitance",
            "crystal material or I-V",
            "magnet function",
            "over-unity/free-energy performance"
        ]
    }
    (META / "MODEL_INFO_V4.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main():
    for count in (20, 24, 25):
        export_pair(f"rotor_{count}wire_floating_R0_v4", rotor_floating(count, "R0"))
    export_pair("rotor_24wire_floating_R4_v4_research", rotor_floating(24, "R4"))
    export_pair("hub_disk_v4", hub_disk())
    export_pair("hub_arc_pair_v4_video_refined", hub_arc_pair())
    export_pair("pot_outer_shell_v4", pot_shell())
    export_pair("pot_grid_former_v4", pot_grid_former())
    export_pair("pot_acrylic_sleeve_jig_v4", pot_dielectric_sleeve_jig())
    export_pair("pot_spiral_mandrel_v4", pot_spiral_mandrel())
    export_pair("pot_terminal_lid_2wire_v4", pot_terminal_lid_2wire())
    export_pair("outer_panel_layered_v4", layered_outer_panel())
    export_pair("lower_central_cage_v4", lower_central_cage())
    export_pair("top_crystal_carrier_4pos_v4", top_crystal_carrier())
    export_pair("horseshoe_magnet_shape_v4", horseshoe_magnet_shape())
    export_pair("horseshoe_dummy_v4", horseshoe_dummy())
    export_pair("guard_post_v4", guard_post())

    asm = build_complete(24, "R0", True)
    cq.exporters.export(asm, str(COMP / "Testatika_M2_V4_BEST_EVIDENCE.stl"), tolerance=0.12, angularTolerance=0.25)
    cq.exporters.export(asm, str(COMP / "Testatika_M2_V4_BEST_EVIDENCE.step"))

    asm_r4 = build_complete(24, "R4", True)
    cq.exporters.export(asm_r4, str(COMP / "Testatika_M2_V4_R4_RESEARCH.stl"), tolerance=0.12, angularTolerance=0.25)
    cq.exporters.export(asm_r4, str(COMP / "Testatika_M2_V4_R4_RESEARCH.step"))

    write_metadata()
    print("V4 best-evidence M2 CAD assets generated.")


if __name__ == "__main__":
    main()
