#!/usr/bin/env python3
"""Generate the M2 V5 fabrication kit.

The V5 engineering kit is based on the M2 V4 evidence baseline but separates
manufacturing classes so that conductive, magnetic and structural functional parts
are never silently replaced by 3D-printed plastic.

Output classes:
- print/                only non-functional polymer supports, jigs, retainers and guards;
- fabricate/            real-material parts (PMMA, metal, shaft, copper-path references);
- assembly-reference/   assembled geometry for fit/inspection, explicitly NOT for printing;
- metadata/             machine-readable fabrication and purchasing manifests.

The historical hidden circuit remains unresolved. The kit therefore exposes reversible
interfaces and does not claim anomalous/free-energy operation.
"""
from __future__ import annotations

from pathlib import Path
import csv
import json
import math
import cadquery as cq

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "hardware" / "build-kits" / "m2-v5"
PRINT = OUT / "print"
FAB = OUT / "fabricate"
ASSY = OUT / "assembly-reference"
META = OUT / "metadata"
for p in (PRINT, FAB, ASSY, META):
    p.mkdir(parents=True, exist_ok=True)

BASE_W, BASE_D = 370.0, 180.0
BASE_T_BUILD = 18.0
BACK_W, BACK_H, BACK_T = 336.0, 246.0, 8.0
ROTOR_D, ROTOR_T = 200.0, 3.5
ROTOR_Z = 160.0
SHAFT_D = 8.0
POT_OD, POT_H = 84.0, 110.0
BEARING_608_OD, BEARING_608_ID, BEARING_608_W = 22.0, 8.0, 7.0


def box(w, d, h, r=1.5):
    obj = cq.Workplane("XY").box(w, d, h, centered=(True, True, False))
    if r:
        try:
            obj = obj.edges("|Z").fillet(r)
        except Exception:
            pass
    return obj


def ring(ro, ri, h):
    return cq.Workplane("XY").circle(ro).circle(ri).extrude(h)


def compound(*items):
    shapes = []
    for obj in items:
        if obj is None:
            continue
        if isinstance(obj, (list, tuple)):
            for sub in obj:
                if sub is not None:
                    shapes.extend(sub.vals() if hasattr(sub, "vals") else [sub])
        else:
            shapes.extend(obj.vals() if hasattr(obj, "vals") else [obj])
    return cq.Compound.makeCompound(shapes)


def export_print(name, obj):
    cq.exporters.export(obj, str(PRINT / f"{name}.stl"), tolerance=0.10, angularTolerance=0.20)
    cq.exporters.export(obj, str(PRINT / f"{name}.step"))


def export_fab(name, obj):
    cq.exporters.export(obj, str(FAB / f"{name}.step"))


def export_assy(name, obj):
    cq.exporters.export(obj, str(ASSY / f"{name}.step"))
    cq.exporters.export(obj, str(ASSY / f"{name}.stl"), tolerance=0.18, angularTolerance=0.28)


def baseplate_build():
    p = box(BASE_W, BASE_D, BASE_T_BUILD, 3)
    for x in (-155, -120, 0, 120, 155):
        for y in (-65, 65):
            try:
                p = p.faces(">Z").workplane().center(x, y).hole(4.5)
            except Exception:
                pass
    return p


def backplate_build():
    p = box(BACK_W, BACK_H, BACK_T, 3)
    for x in (-150, 150):
        for y in (-105, 105):
            try:
                p = p.faces(">Z").workplane().center(x, y).hole(4.5)
            except Exception:
                pass
    return p


def rotor_disc(count=24, route="R0"):
    p = cq.Workplane("XY").circle(ROTOR_D / 2).extrude(ROTOR_T)
    p = p.faces(">Z").workplane().hole(SHAFT_D + 0.2)
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


def shaft_8mm(length=245.0):
    return cq.Workplane("XY").circle(SHAFT_D / 2).extrude(length / 2, both=True)


def bearing_block_608_metal():
    """Fabricated nonmagnetic bearing tower; NOT a printed load-bearing part."""
    center_z = ROTOR_Z - BASE_T_BUILD
    plate = box(70, 10, 174, 2)
    foot = box(90, 52, 8, 2)
    stiff_l = box(10, 36, 152, 1).translate((-28,0,8))
    stiff_r = box(10, 36, 152, 1).translate((28,0,8))
    obj = compound(plate, foot, stiff_l, stiff_r)
    bore = cq.Workplane("XZ").circle((BEARING_608_OD + 0.04) / 2).extrude(24, both=True).translate((0, 0, center_z))
    return obj.cut(bore.val())


def bearing_retainer_608_metal():
    r = ring(16.0, (BEARING_608_OD + 0.08) / 2, 3.0)
    for a in (0, 120, 240):
        x = 13.5 * math.cos(math.radians(a)); y = 13.5 * math.sin(math.radians(a))
        r = r.faces(">Z").workplane().center(x, y).hole(3.3)
    return r


def hub_flange_8mm_metal():
    h = ring(28.0, 4.08, 6.0)
    for a in range(0, 360, 60):
        x = 15 * math.cos(math.radians(a)); y = 15 * math.sin(math.radians(a))
        h = h.faces(">Z").workplane().center(x, y).hole(3.3)
    return h


def shaft_alignment_jig():
    p = box(50, 24, 22, 2)
    bore = cq.Workplane("XZ").circle(4.15).extrude(30, both=True).translate((0, 0, 12))
    return p.cut(bore)


def pot_bottom_carrier():
    base = ring(46, 16, 7)
    g = ring(39.5, 37.2, 7).translate((0, 0, 7))
    d = ring(35.2, 33.0, 7).translate((0, 0, 7))
    return compound(base, g, d)


def pot_top_carrier():
    lid = ring(46, 16, 7)
    for x in (-16, 16):
        lid = lid.faces(">Z").workplane().center(x, 0).hole(4.4)
    return lid


def pot_mesh_clip():
    body = box(16, 10, 12, 1.5)
    slot = box(10, 2.0, 9, 0).translate((0, 0, 2))
    return body.cut(slot)


def pot_spiral_winding_mandrel():
    core = ring(21.0, 18.0, 88.0)
    flange1 = ring(25.0, 18.0, 4.0)
    flange2 = ring(25.0, 18.0, 4.0).translate((0, 0, 84.0))
    return compound(core, flange1, flange2)


def pot_dielectric_tube_reference():
    return ring(33.0, 31.0, 92.0)


def pot_grid_envelope_reference():
    return ring(37.0, 36.2, 96.0)


def pot_spiral_copper_path():
    helix = cq.Wire.makeHelix(pitch=8.0, height=82.0, radius=20.0)
    return cq.Workplane("XZ").circle(1.0).sweep(helix)


def stator_insert():
    w, h, t = 88.0, 74.0, 1.2
    p = cq.Workplane("XY").rect(w, h).extrude(t)
    for ix in range(7):
        for iy in range(5):
            x = -30 + ix * 10
            y = -22 + iy * 11
            p = p.cut(cq.Workplane("XY").center(x, y).rect(4.5, 6.0).extrude(t + 2).translate((0, 0, -1)))
    return p


def hub_arc_metal_insert(inner_r=18.0, outer_r=23.0, thickness=1.5, center_gap=7.0):
    obj = ring(outer_r, inner_r, thickness)
    cut = box(center_gap, outer_r * 2.5, thickness + 2, 0).translate((0,0,-1))
    return obj.cut(cut)


def pickup_metal_insert():
    p = cq.Workplane("XY").rect(70, 18).extrude(1.2)
    for ix in range(7):
        x = -27 + ix * 9
        p = p.cut(cq.Workplane("XY").center(x, 0).rect(4.0, 6.0).extrude(3).translate((0,0,-1)))
    return p


def crossbar_metal_long():
    return cq.Workplane("XY").rect(110, 18).extrude(1.5)


def crossbar_metal_short():
    return cq.Workplane("XY").rect(36, 30).extrude(1.5)


def lower_central_cage_metal_candidate():
    body = box(24, 18, 70, 0)
    inner = box(20, 14, 62, 0).translate((0,0,4))
    return body.cut(inner)


def upper_tower_holder():
    base = box(38, 30, 10, 2)
    left = box(6, 12, 72, 1.5).translate((-13,0,10))
    right = box(6, 12, 72, 1.5).translate((13,0,10))
    return compound(base,left,right)


def spring_wire_path(height=62.0, turns=8.5, radius=5.0, wire_r=0.75):
    helix = cq.Wire.makeHelix(pitch=height / turns, height=height, radius=radius)
    return cq.Workplane("XZ").circle(wire_r).sweep(helix)


def stator_insert_clip():
    foot = box(26, 18, 5, 1.5)
    upright = box(6, 18, 28, 1.5).translate((-10, 0, 5))
    jaw = box(20, 18, 5, 1.5).translate((-2, 0, 28))
    slot = box(13, 2.2, 13, 0).translate((-2, 0, 20))
    return compound(foot, upright, jaw).cut(slot.val())


def magnet_cradle():
    base = box(54, 34, 6, 2)
    left = box(8, 34, 26, 2).translate((-23, 0, 6))
    right = box(8, 34, 26, 2).translate((23, 0, 6))
    return compound(base, left, right)


def crystal_module_tray():
    body = box(176, 36, 10, 3)
    pocket = box(110, 24, 7, 2).translate((0, 0, 4))
    body = body.cut(pocket)
    for x in (-56, -38, 38, 56):
        body = body.faces(">Z").workplane().center(x, 0).hole(4.4)
    return body


def guard_corner():
    foot = box(34, 34, 6, 2)
    a = box(8, 28, 52, 2).translate((-13, 0, 6))
    b = box(28, 8, 52, 2).translate((0, -13, 6))
    return compound(foot, a, b)


def guard_panel_reference():
    return box(330, 4, 250, 1)


def hub_collar_reference():
    return ring(14.0, 4.1, 10.0)


def pot_material_stack_reference():
    return compound(
        pot_bottom_carrier(),
        pot_grid_envelope_reference().translate((0, 0, 7)),
        pot_dielectric_tube_reference().translate((0, 0, 9)),
        pot_spiral_copper_path().translate((0, 0, 13)),
        pot_top_carrier().translate((0, 0, POT_H)),
    )


def assembly_reference():
    parts = [baseplate_build()]
    parts.append(backplate_build().rotate((0, 0, 0), (1, 0, 0), 90).translate((0, -78, BASE_T_BUILD + BACK_H / 2)))
    parts.append(rotor_disc(24, "R0").rotate((0, 0, 0), (1, 0, 0), 90).translate((0, -10, ROTOR_Z)))
    parts.append(shaft_8mm().rotate((0,0,0),(1,0,0),90).translate((0,-10,ROTOR_Z)))
    parts.append(bearing_block_608_metal().translate((0, -62, BASE_T_BUILD)))
    parts.append(bearing_block_608_metal().translate((0, 42, BASE_T_BUILD)))
    parts.append(hub_flange_8mm_metal().rotate((0,0,0),(1,0,0),90).translate((0,-5,ROTOR_Z)))
    parts.append(hub_flange_8mm_metal().rotate((0,0,0),(1,0,0),90).translate((0,-15,ROTOR_Z)))
    parts.append(hub_collar_reference().rotate((0,0,0),(1,0,0),90).translate((0,2,ROTOR_Z)))
    parts.append(pot_material_stack_reference().translate((-143, -4, BASE_T_BUILD)))
    parts.append(pot_material_stack_reference().translate((143, -4, BASE_T_BUILD)))
    parts.append(crystal_module_tray().rotate((0, 0, 0), (1, 0, 0), 90).translate((0, -6, 258)))
    parts.append(stator_insert().rotate((0, 0, 0), (1, 0, 0), 90).translate((-118, -8, 205)))
    parts.append(stator_insert().rotate((0, 0, 0), (1, 0, 0), 90).translate((118, -8, 205)))
    parts.append(hub_arc_metal_insert().rotate((0,0,0),(1,0,0),90).translate((0,-1,ROTOR_Z)))
    parts.append(lower_central_cage_metal_candidate().translate((0,-6,48)))
    parts.append(upper_tower_holder().rotate((0,0,0),(1,0,0),90).translate((-47,-8,168)))
    parts.append(upper_tower_holder().rotate((0,0,0),(1,0,0),90).translate((47,-8,168)))
    parts.append(spring_wire_path().rotate((0,0,0),(1,0,0),90).translate((-47,-1,176)))
    parts.append(spring_wire_path().rotate((0,0,0),(1,0,0),90).translate((47,-1,176)))
    parts.append(magnet_cradle().translate((-58, -70, BASE_T_BUILD)))
    parts.append(magnet_cradle().translate((58, -70, BASE_T_BUILD)))
    return compound(parts)


PRINT_PARTS = {
    "shaft_alignment_jig_m2_v5": shaft_alignment_jig(),
    "pot_bottom_carrier_m2_v5": pot_bottom_carrier(),
    "pot_top_carrier_m2_v5": pot_top_carrier(),
    "pot_mesh_clip_m2_v5": pot_mesh_clip(),
    "pot_spiral_winding_mandrel_m2_v5": pot_spiral_winding_mandrel(),
    "stator_insert_clip_m2_v5": stator_insert_clip(),
    "magnet_cradle_m2_v5": magnet_cradle(),
    "crystal_module_tray_m2_v5": crystal_module_tray(),
    "upper_tower_holder_m2_v5": upper_tower_holder(),
    "guard_corner_m2_v5": guard_corner(),
}

FAB_PARTS = {
    "baseplate_370x180x18_structural_m2_v5": baseplate_build(),
    "backplate_336x246x8_structural_m2_v5": backplate_build(),
    "rotor_disc_pmMA_200x3p5_24wire_R0_m2_v5": rotor_disc(24, "R0"),
    "rotor_disc_pmMA_200x3p5_24wire_R4_research_m2_v5": rotor_disc(24, "R4"),
    "shaft_8mm_x245_m2_v5": shaft_8mm(),
    "bearing_block_608_nonmagnetic_m2_v5": bearing_block_608_metal(),
    "bearing_retainer_608_nonmagnetic_m2_v5": bearing_retainer_608_metal(),
    "hub_flange_8mm_nonmagnetic_m2_v5": hub_flange_8mm_metal(),
    "stator_perforated_metal_insert_m2_v5": stator_insert(),
    "hub_arc_metal_candidate_m2_v5": hub_arc_metal_insert(),
    "pickup_metal_insert_candidate_m2_v5": pickup_metal_insert(),
    "crossbar_long_metal_candidate_m2_v5": crossbar_metal_long(),
    "crossbar_short_metal_candidate_m2_v5": crossbar_metal_short(),
    "lower_central_cage_metal_candidate_m2_v5": lower_central_cage_metal_candidate(),
    "spring_wire_path_reference_m2_v5": spring_wire_path(),
    "pot_dielectric_pmMA_tube_reference_m2_v5": pot_dielectric_tube_reference(),
    "pot_grid_metal_mesh_envelope_reference_m2_v5": pot_grid_envelope_reference(),
    "pot_spiral_copper_wire_path_reference_m2_v5": pot_spiral_copper_path(),
    "guard_panel_transparent_reference_m2_v5": guard_panel_reference(),
    "hub_clamp_collar_metal_envelope_reference_m2_v5": hub_collar_reference(),
}

for name, obj in PRINT_PARTS.items():
    print("print", name)
    export_print(name, obj)
for name, obj in FAB_PARTS.items():
    print("fabricate", name)
    export_fab(name, obj)

assy = assembly_reference()
export_assy("Testatika_M2_V5_FABRICATION_ASSEMBLY_REFERENCE_NOT_FOR_PRINT", assy)
export_assy("Testatika_M2_V5_MECHANICAL_QUALIFICATION_REFERENCE_NOT_FOR_PRINT", assy)

manifest = {
    "schema_version": 1,
    "kit": "M2-V5-FABRICATION",
    "evidence_parent": "M2 V4 best-evidence",
    "purpose": "stable mechanical/fabrication kit with real-material interfaces",
    "guarantee_boundary": "mechanically buildable research replica; historical hidden circuit and anomalous energy performance are not recovered/guaranteed",
    "rules": [
        "STL files under print/ are only non-load-critical supports, jigs, clips, carriers or guard fittings.",
        "Conductive, magnetic, shaft, bearing and structural fabrication items are never represented as plastic substitutes.",
        "Assembly STL files are visual fit references and are explicitly not print jobs.",
        "Unknown historical electrical functions terminate at reversible interfaces.",
    ],
    "direct_or_preferred_anchors": {
        "rotor_diameter_mm": 200.0,
        "nominal_sector_count": 24,
        "sector_conductor": "~1 mm copper wire, individually floating",
        "pot_external_terminals_each": 2,
    },
    "printable_parts": [
        {"name": n, "class": "PRINTABLE_SUPPORT", "material": "PETG/PA-CF/PC selected for environment; never substitutes for metal/electrode/magnet", "functional_electrode": False}
        for n in PRINT_PARTS
    ],
    "fabricated_parts": [
        {"name": "baseplate_370x180x18_structural_m2_v5", "class": "CUT_STRUCTURAL", "material": "18 mm birch ply, phenolic laminate or equivalent rigid nonconductive plate"},
        {"name": "backplate_336x246x8_structural_m2_v5", "class": "CUT_STRUCTURAL", "material": "8 mm cast PMMA or rigid nonconductive plate"},
        {"name": "rotor_disc_pmMA_200x3p5_24wire_R0_m2_v5", "class": "CUT_PMMA", "material": "cast PMMA, 3.5 mm working thickness"},
        {"name": "shaft_8mm_x245_m2_v5", "class": "METAL_SHAFT", "material": "8 mm precision stainless/ground steel"},
        {"name": "bearing_block_608_nonmagnetic_m2_v5", "class": "MACHINED_BEARING_SUPPORT", "material": "6061-T6 aluminium or G10/FR4 plate; precision bore/ream after machining"},
        {"name": "bearing_retainer_608_nonmagnetic_m2_v5", "class": "MACHINED_BEARING_RETAINER", "material": "6061-T6 aluminium or equivalent nonmagnetic rigid material"},
        {"name": "hub_flange_8mm_nonmagnetic_m2_v5", "class": "MACHINED_HUB_FLANGE", "material": "balanced 6061-T6 aluminium; two flanges clamp the PMMA rotor"},
        {"name": "stator_perforated_metal_insert_m2_v5", "class": "METAL_ELECTRODE", "material": "conductive perforated sheet/mesh; document alloy"},
        {"name": "pot_dielectric_pmMA_tube_reference_m2_v5", "class": "PMMA_DIELECTRIC", "material": "real PMMA/acrylic tube"},
        {"name": "pot_grid_metal_mesh_envelope_reference_m2_v5", "class": "METAL_MESH", "material": "metal gauze/mesh"},
        {"name": "pot_spiral_copper_wire_path_reference_m2_v5", "class": "WIND_COPPER", "material": "copper conductor wound on mandrel"},
    ],
    "purchased_components": [
        {"qty": 2, "item": "608-2RS bearing", "spec": "8x22x7 mm, quality low-runout"},
        {"qty": 2, "item": "8 mm metal clamp collar", "spec": "balanced low-profile collars; lock hub stack axially without relying on plastic"},
        {"qty": 2, "item": "horseshoe magnet", "spec": "document geometry and field; use matched nonmagnetic dummies for controls"},
        {"qty": 4, "item": "isolated terminal/binding post", "spec": "two per side pot"},
        {"qty": 1, "item": "transparent rotor guard", "spec": "polycarbonate preferred for impact resistance"},
        {"qty": 1, "item": "fastener set", "spec": "M3/M4 nonmagnetic where magnetic confounding matters"},
    ],
}
(META / "FABRICATION_MANIFEST_M2_V5.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

with (META / "PURCHASED_COMPONENTS_M2_V5.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["qty", "item", "spec"])
    for row in manifest["purchased_components"]:
        w.writerow([row["qty"], row["item"], row["spec"]])

with (META / "CUT_LIST_M2_V5.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["qty", "part", "material", "process"])
    w.writerow([1, "baseplate 370x180x18", "birch/phenolic/nonconductive structural plate", "CNC/router/saw + drill"])
    w.writerow([1, "backplate 336x246x8", "cast PMMA/nonconductive plate", "CNC/laser where material permits + drill"])
    w.writerow([1, "rotor disc Ø200x3.5 R0", "cast PMMA", "CNC/router + drill; deburr/polish edges"])
    w.writerow([2, "608 bearing tower", "6061-T6 aluminium or G10/FR4", "CNC/mill; finish bearing bore coaxially"])
    w.writerow([2, "608 bearing retainer", "6061-T6 aluminium", "CNC/laser + finish"])
    w.writerow([2, "8 mm hub flange", "6061-T6 aluminium", "CNC/lathe + 6-hole bolt circle; balance as pair"])
    w.writerow([2, "stator perforated insert", "conductive metal sheet/mesh", "laser/waterjet/shear + deburr"])
    w.writerow([2, "pot dielectric tube", "PMMA tube", "cut square to length"])
    w.writerow([2, "pot grid sleeve", "metal mesh", "roll/cut; seam mechanically/electrically documented"])

print("M2 V5 fabrication kit generated at", OUT.relative_to(ROOT))