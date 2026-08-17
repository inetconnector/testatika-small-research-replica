#!/usr/bin/env python3
"""Generate the M6 V2 fabrication kit for the large ~500 mm two-disc family.

The V2 engineering kit preserves the M6 V1 evidence geometry while separating real
materials from printable supports. No conductive/magnetic/shaft/bearing component is
silently replaced by plastic. Legacy all-solid CAD remains reference-only elsewhere.

Outputs:
- print/                polymer supports, jigs, retainers and guards only;
- fabricate/            real-material STEP parts and manufacturing envelopes;
- assembly-reference/   full fit/reference assemblies, NOT print jobs;
- metadata/             fabrication, cut and purchased-component manifests.

The original hidden electrical node map, capacitor internals and crystal/rectifier
construction are unresolved. Those locations are modular/open, not invented.
"""
from __future__ import annotations

from pathlib import Path
import csv
import json
import math
import cadquery as cq

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "hardware" / "build-kits" / "m6-v2"
PRINT = OUT / "print"
FAB = OUT / "fabricate"
ASSY = OUT / "assembly-reference"
META = OUT / "metadata"
for p in (PRINT, FAB, ASSY, META):
    p.mkdir(parents=True, exist_ok=True)

DISC_D, DISC_T = 500.0, 5.0
LAMELLA_COUNT = 50
LAMELLA_T, LAMELLA_W, LAMELLA_L = 0.20, 20.0, 160.0
BASE_W, BASE_D, BASE_T = 760.0, 340.0, 18.0
DISC_CENTER_Z = 315.0
DISC_Y_FRONT, DISC_Y_REAR = -11.0, 11.0
INNER_SHAFT_D = 12.0
OUTER_SHAFT_OD, OUTER_SHAFT_ID = 25.0, 16.0
BEARING_INNER_OD, BEARING_INNER_ID, BEARING_INNER_W = 28.0, 12.0, 8.0
BEARING_OUTER_OD, BEARING_OUTER_ID, BEARING_OUTER_W = 37.0, 25.0, 7.0
CYL_OD, CYL_H = 146.0, 235.0
CYL_X, CYL_Y = 300.0, -5.0


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
    cq.exporters.export(obj, str(PRINT / f"{name}.stl"), tolerance=0.12, angularTolerance=0.22)
    cq.exporters.export(obj, str(PRINT / f"{name}.step"))


def export_fab(name, obj):
    cq.exporters.export(obj, str(FAB / f"{name}.step"))


def export_assy(name, obj):
    cq.exporters.export(obj, str(ASSY / f"{name}.step"))
    cq.exporters.export(obj, str(ASSY / f"{name}.stl"), tolerance=0.24, angularTolerance=0.34)


def baseplate():
    p = box(BASE_W, BASE_D, BASE_T, 4)
    for x in (-330, -300, -140, 0, 140, 300, 330):
        for y in (-140, 140):
            try:
                p = p.faces(">Z").workplane().center(x, y).hole(6.5)
            except Exception:
                pass
    return p


def rotor_disc(bore):
    p = cq.Workplane("XY").circle(DISC_D / 2).extrude(DISC_T)
    p = p.faces(">Z").workplane().hole(bore + 0.30)
    for a in range(0, 360, 60):
        x = 32 * math.cos(math.radians(a)); y = 32 * math.sin(math.radians(a))
        p = p.faces(">Z").workplane().center(x, y).hole(5.2)
    return p


def lamella_strip():
    return cq.Workplane("XY").box(LAMELLA_L, LAMELLA_W, LAMELLA_T, centered=(True, True, False))


def lamella_pack(one_face=True):
    parts = []
    for i in range(LAMELLA_COUNT):
        a = i * 360.0 / LAMELLA_COUNT
        strip = lamella_strip().translate((165, 0, 0)).rotate((0, 0, 0), (0, 0, 1), a)
        parts.append(strip)
    if not one_face:
        parts.extend([p.translate((0, 0, -(DISC_T + LAMELLA_T))) for p in list(parts)])
    return compound(parts)


def bearing_tower_metal(od):
    """Fabricated load-bearing tower; never printed for the 500-mm rotor."""
    center_z = DISC_CENTER_Z - BASE_T
    plate = box(112, 12, 330, 2)
    foot = box(140, 92, 12, 2)
    stiff_l = box(12, 62, 296, 1).translate((-46,0,12))
    stiff_r = box(12, 62, 296, 1).translate((46,0,12))
    obj = compound(plate, foot, stiff_l, stiff_r)
    bore = cq.Workplane("XZ").circle((od + 0.05) / 2).extrude(30, both=True).translate((0,0,center_z))
    return obj.cut(bore.val())


def bearing_retainer_metal(od):
    outer = od / 2 + 9
    obj = ring(outer, (od + 0.10) / 2, 4)
    for a in (0,120,240):
        x=(outer-4.5)*math.cos(math.radians(a)); y=(outer-4.5)*math.sin(math.radians(a))
        obj=obj.faces(">Z").workplane().center(x,y).hole(4.2)
    return obj


def inner_shaft(length=300.0):
    return cq.Workplane("XY").circle(INNER_SHAFT_D / 2).extrude(length/2, both=True)


def outer_shaft_tube(length=180.0):
    return ring(OUTER_SHAFT_OD / 2, OUTER_SHAFT_ID / 2, length).translate((0,0,-length/2))


def disc_hub_metal_envelope(bore):
    hub = ring(46, bore / 2 + 0.15, 14)
    for a in range(0, 360, 60):
        x = 32 * math.cos(math.radians(a)); y = 32 * math.sin(math.radians(a))
        hub = hub.faces(">Z").workplane().center(x, y).hole(5.2)
    return hub


def lamella_pitch_jig_10():
    plate = box(190, 38, 5, 2)
    for i in range(10):
        x = -81 + i * 18
        slot = box(2.4, 28, 7, 0).translate((x, 0, -1))
        plate = plate.cut(slot)
    return plate


def stator_electrode():
    w, h, t = 104.0, 34.0, 1.5
    p = cq.Workplane("XY").rect(w, h).extrude(t)
    for ix in range(9):
        for iy in range(3):
            x = -42 + ix * 10.5; y = -10 + iy * 10
            p = p.cut(cq.Workplane("XY").center(x, y).rect(6.0, 7.0).extrude(t + 2).translate((0, 0, -1)))
    return p


def stator_adjustable_bracket():
    base = box(52, 28, 7, 2)
    upright = box(8, 28, 72, 2).translate((-21, 0, 7))
    arm = box(58, 18, 8, 2).translate((4, 0, 65))
    for x in (-15, 15):
        base = base.faces(">Z").workplane().center(x, 0).hole(5.5)
    slot = box(34, 3.0, 12, 0).translate((7, 0, 62))
    return compound(base, upright, arm).cut(slot.val())


def horseshoe_magnetic_core_reference():
    left=box(16,28,80,2).translate((-30,0,0))
    right=box(16,28,80,2).translate((30,0,0))
    bridge=box(76,28,18,2)
    return compound(left,right,bridge)


def place_stator(angle_deg, y, extra_angle=0.0):
    r=DISC_D/2+33
    a=math.radians(angle_deg)
    x=r*math.cos(a); z=DISC_CENTER_Z+r*math.sin(a)
    p=stator_electrode().rotate((0,0,0),(1,0,0),90)
    p=p.rotate((0,0,0),(0,1,0),-angle_deg+90+extra_angle).translate((x,y,z))
    return p


def stator_sets_reference():
    front_angles=[-42,-12,22,52,82,112,142,168]
    rear_angles=[-30,10,50,90,130,170]
    front=[place_stator(a,-31,0) for a in front_angles]
    rear=[place_stator(a,31,45 if i>=4 else 0) for i,a in enumerate(rear_angles)]
    return compound(front,rear)


def grid_separator_ring(radius, width=5.0):
    return ring(radius + width, radius - width, 6.0)


def grid_centering_spider(outer_r=72.0):
    center = ring(22, 12, 6)
    spokes = [box(outer_r - 20, 8, 6, 1).translate(((outer_r + 20) / 2, 0, 0)).rotate((0,0,0),(0,0,1),a) for a in (0,90,180,270)]
    rim = ring(outer_r, outer_r - 6, 6)
    return compound(center, spokes, rim)


def grid_tube_envelope(radius, height, wall=0.8):
    return ring(radius + wall / 2, radius - wall / 2, height)


def acrylic_sleeve(ro, ri, height):
    return ring(ro, ri, height)


def central_tube_reference():
    return ring(18, 12, 185)


def bifilar_winding_path():
    h1 = cq.Wire.makeHelix(pitch=4.5, height=170, radius=23.0)
    h2 = cq.Wire.makeHelix(pitch=4.5, height=170, radius=24.6)
    c1 = cq.Workplane("XZ").circle(0.65).sweep(h1)
    c2 = cq.Workplane("XZ").circle(0.65).sweep(h2).rotate((0,0,0),(0,0,1),180)
    return compound(c1, c2)


def cylinder_separator_stack():
    bottom = compound(grid_separator_ring(66), grid_separator_ring(56), grid_separator_ring(46))
    top = bottom.translate((0, 0, 205))
    return compound(bottom, top)


def capacitor_mount(od):
    base = box(od + 36, 50, 8, 3)
    cradle = ring(od / 2 + 5, od / 2 + 1, 14).translate((0, 0, 18))
    stop1 = box(8, 44, 42, 2).translate((-od/2 - 8, 0, 8))
    stop2 = box(8, 44, 42, 2).translate((od/2 + 8, 0, 8))
    return compound(base, cradle, stop1, stop2)


def horseshoe_mount():
    base = box(92, 52, 8, 3)
    left = box(10, 44, 42, 2).translate((-36, 0, 8))
    right = box(10, 44, 42, 2).translate((36, 0, 8))
    return compound(base, left, right)


def top_module_tray():
    body = box(190, 52, 10, 3)
    pocket = box(156, 38, 7, 2).translate((0, 0, 4))
    body = body.cut(pocket)
    for x in (-78, -52, 52, 78):
        body = body.faces(">Z").workplane().center(x, 0).hole(4.5)
    return body


def terminal_board():
    board = box(250, 52, 10, 2)
    for y in (-15, 0, 15):
        for col in range(6):
            x = -100 + col * 40
            board = board.faces(">Z").workplane().center(x, y).hole(5.2)
    return board


def motor_mount():
    plate = box(140, 92, 10, 4)
    left = box(10, 80, 64, 3).translate((-55, 0, 10))
    right = box(10, 80, 64, 3).translate((55, 0, 10))
    for x in (-45, 45):
        for y in (-30, 30):
            plate = plate.faces(">Z").workplane().center(x, y).hole(6.5)
    return compound(plate, left, right)


def drive_pulley_reference(radius, bore, width=10):
    return ring(radius, bore / 2 + 0.15, width)


def guard_corner():
    foot = box(44, 44, 8, 3)
    a = box(10, 36, 70, 2).translate((-17, 0, 8))
    b = box(36, 10, 70, 2).translate((0, -17, 8))
    return compound(foot, a, b)


def guard_frame_reference():
    parts = []
    for x in (-330, 330):
        for y in (-145, 145):
            parts.append(box(20, 20, 620, 2).translate((x, y, BASE_T)))
    parts.append(box(680, 20, 20, 2).translate((0, -145, BASE_T + 600)))
    parts.append(box(680, 20, 20, 2).translate((0, 145, BASE_T + 600)))
    return compound(parts)


def cylinder_real_material_reference():
    return compound(
        cylinder_separator_stack(),
        grid_tube_envelope(66, 205),
        acrylic_sleeve(62, 59.5, 199).translate((0, 0, 3)),
        grid_tube_envelope(56, 199).translate((0, 0, 3)),
        acrylic_sleeve(52, 49.5, 193).translate((0, 0, 6)),
        grid_tube_envelope(46, 193).translate((0, 0, 6)),
        central_tube_reference().translate((0, 0, 10)),
        bifilar_winding_path().translate((0, 0, 18)),
    )


def verticalize(obj, y, z=DISC_CENTER_Z):
    return obj.rotate((0,0,0),(1,0,0),90).translate((0, y, z))


def assembly_reference(include_guard=True):
    parts = [baseplate()]
    front_disc = rotor_disc(OUTER_SHAFT_OD).union(lamella_pack(True).translate((0,0,DISC_T)))
    rear_disc = rotor_disc(INNER_SHAFT_D).union(lamella_pack(True).translate((0,0,DISC_T)))
    rear_disc = rear_disc.union(lamella_pack(True).translate((0,0,-LAMELLA_T)))
    parts.append(verticalize(front_disc, DISC_Y_FRONT))
    parts.append(verticalize(rear_disc, DISC_Y_REAR))
    parts.append(outer_shaft_tube().rotate((0,0,0),(1,0,0),90).translate((0,0,DISC_CENTER_Z)))
    parts.append(inner_shaft().rotate((0,0,0),(1,0,0),90).translate((0,0,DISC_CENTER_Z)))
    parts.append(disc_hub_metal_envelope(OUTER_SHAFT_OD).rotate((0,0,0),(1,0,0),90).translate((0,DISC_Y_FRONT,DISC_CENTER_Z)))
    parts.append(disc_hub_metal_envelope(INNER_SHAFT_D).rotate((0,0,0),(1,0,0),90).translate((0,DISC_Y_REAR,DISC_CENTER_Z)))
    parts.append(bearing_tower_metal(BEARING_OUTER_OD).translate((0,-72,BASE_T)))
    parts.append(bearing_tower_metal(BEARING_OUTER_OD).translate((0,72,BASE_T)))
    parts.append(bearing_tower_metal(BEARING_INNER_OD).translate((0,-128,BASE_T)))
    parts.append(bearing_tower_metal(BEARING_INNER_OD).translate((0,128,BASE_T)))
    parts.append(stator_sets_reference())
    parts.append(cylinder_real_material_reference().translate((-CYL_X,CYL_Y,BASE_T)))
    parts.append(cylinder_real_material_reference().translate((CYL_X,CYL_Y,BASE_T)))
    parts.append(capacitor_mount(78).translate((-70,-108,BASE_T)))
    parts.append(capacitor_mount(62).translate((55,-108,BASE_T)))
    parts.append(horseshoe_mount().translate((-145,-105,BASE_T)))
    parts.append(horseshoe_mount().translate((145,-105,BASE_T)))
    parts.append(horseshoe_magnetic_core_reference().translate((-145,-105,BASE_T+6)))
    parts.append(horseshoe_magnetic_core_reference().translate((145,-105,BASE_T+6)))
    parts.append(top_module_tray().translate((0,-8,600)))
    parts.append(terminal_board().translate((0,-145,BASE_T)))
    parts.append(drive_pulley_reference(48,OUTER_SHAFT_OD).rotate((0,0,0),(1,0,0),90).translate((0,95,DISC_CENTER_Z)))
    parts.append(drive_pulley_reference(48,INNER_SHAFT_D).rotate((0,0,0),(1,0,0),90).translate((0,118,DISC_CENTER_Z)))
    if include_guard:
        parts.append(guard_frame_reference())
    return compound(parts)


PRINT_PARTS = {
    "lamella_pitch_jig_10position_m6_v2": lamella_pitch_jig_10(),
    "stator_adjustable_bracket_m6_v2": stator_adjustable_bracket(),
    "grid_separator_ring_outer_m6_v2": grid_separator_ring(66),
    "grid_separator_ring_middle_m6_v2": grid_separator_ring(56),
    "grid_separator_ring_inner_m6_v2": grid_separator_ring(46),
    "grid_centering_spider_m6_v2": grid_centering_spider(),
    "capacitor_mount_78mm_m6_v2": capacitor_mount(78),
    "capacitor_mount_62mm_m6_v2": capacitor_mount(62),
    "horseshoe_mount_m6_v2": horseshoe_mount(),
    "top_module_tray_m6_v2": top_module_tray(),
    "terminal_board_18node_m6_v2": terminal_board(),
    "adjustable_lab_motor_mount_m6_v2": motor_mount(),
    "guard_corner_m6_v2": guard_corner(),
}

FAB_PARTS = {
    "baseplate_760x340x18_structural_m6_v2": baseplate(),
    "front_rotor_disc_pmMA_500x5_25mm_bore_m6_v2": rotor_disc(OUTER_SHAFT_OD),
    "rear_rotor_disc_pmMA_500x5_12mm_bore_m6_v2": rotor_disc(INNER_SHAFT_D),
    "lamella_chromesteel_0p2x20x160_m6_v2": lamella_strip(),
    "stator_perforated_metal_electrode_m6_v2": stator_electrode(),
    "inner_shaft_12mm_x300_m6_v2": inner_shaft(),
    "outer_hollow_shaft_25od_16id_x180_m6_v2": outer_shaft_tube(),
    "bearing_tower_6001_nonmagnetic_m6_v2": bearing_tower_metal(BEARING_INNER_OD),
    "bearing_retainer_6001_nonmagnetic_m6_v2": bearing_retainer_metal(BEARING_INNER_OD),
    "bearing_tower_6805_nonmagnetic_m6_v2": bearing_tower_metal(BEARING_OUTER_OD),
    "bearing_retainer_6805_nonmagnetic_m6_v2": bearing_retainer_metal(BEARING_OUTER_OD),
    "front_disc_hub_metal_25mm_bore_reference_m6_v2": disc_hub_metal_envelope(OUTER_SHAFT_OD),
    "rear_disc_hub_metal_12mm_bore_reference_m6_v2": disc_hub_metal_envelope(INNER_SHAFT_D),
    "large_cylinder_outer_grid_metal_mesh_envelope_m6_v2": grid_tube_envelope(66,205),
    "large_cylinder_middle_grid_metal_mesh_envelope_m6_v2": grid_tube_envelope(56,199),
    "large_cylinder_inner_grid_metal_mesh_envelope_m6_v2": grid_tube_envelope(46,193),
    "large_cylinder_outer_pmMA_sleeve_m6_v2": acrylic_sleeve(62,59.5,199),
    "large_cylinder_inner_pmMA_sleeve_m6_v2": acrylic_sleeve(52,49.5,193),
    "large_cylinder_central_tube_reference_m6_v2": central_tube_reference(),
    "large_cylinder_bifilar_copper_winding_path_m6_v2": bifilar_winding_path(),
    "horseshoe_magnetic_core_reference_m6_v2": horseshoe_magnetic_core_reference(),
    "lab_drive_pulley_outer_reference_m6_v2": drive_pulley_reference(48,OUTER_SHAFT_OD),
    "lab_drive_pulley_inner_reference_m6_v2": drive_pulley_reference(48,INNER_SHAFT_D),
    "guard_frame_structural_reference_m6_v2": guard_frame_reference(),
}

for name, obj in PRINT_PARTS.items():
    print("print", name)
    export_print(name, obj)
for name, obj in FAB_PARTS.items():
    print("fabricate", name)
    export_fab(name, obj)

assy = assembly_reference(True)
export_assy("Testatika_M6_V2_FABRICATION_ASSEMBLY_REFERENCE_NOT_FOR_PRINT", assy)
export_assy("Testatika_M6_V2_MECHANICAL_QUALIFICATION_GUARDED_REFERENCE_NOT_FOR_PRINT", assy)

manifest = {
    "schema_version": 1,
    "kit": "M6-V2-FABRICATION",
    "evidence_parent": "M6 V1 best-evidence / M6a Hauser anchor",
    "purpose": "stable low-speed fabrication/mechanical qualification kit with real-material interfaces",
    "guarantee_boundary": "mechanically buildable research replica; original hidden electrical topology, capacitor internals, crystal/rectifier construction and anomalous energy operation are unresolved",
    "rules": [
        "STL files under print/ are only non-load-critical jigs, spacers, clips, module carriers and guard fittings.",
        "No capacitor can, magnetic core, conductive grid, winding, shaft, bearing, lamella or rotor disc is supplied as a plastic functional substitute.",
        "Assembly STL is a fit/reference visualization and is not a print job.",
        "The lab drive shows pulleys and interfaces only; rigid fake belt rods are prohibited.",
    ],
    "direct_anchor_mm": {
        "disc_diameter": 500.0,
        "disc_thickness": 5.0,
        "lamella_count": 50,
        "lamella_source_thickness": 0.2,
        "lamella_width": 20.0,
        "lamella_length": 160.0,
    },
    "source_supported_architecture": [
        "8 front / 6 rear stationary electrode positions",
        "three concentric metal grids per large cylinder",
        "two-layer bifilar copper winding around central tube",
        "two large side cylinder positions",
    ],
    "printable_parts": [
        {"name": n, "class": "PRINTABLE_SUPPORT", "material": "PA-CF/PETG/PC selected for environment; never used as bearing tower/electrode/magnet/shaft", "functional_electrode": False}
        for n in PRINT_PARTS
    ],
    "fabricated_parts": [
        {"name": "baseplate_760x340x18_structural_m6_v2", "class": "CUT_STRUCTURAL", "material": "18 mm birch ply/phenolic/nonconductive structural board"},
        {"name": "front_rotor_disc_pmMA_500x5_25mm_bore_m6_v2", "class": "CUT_PMMA", "material": "cast PMMA 5 mm; outer-shaft hub bore"},
        {"name": "rear_rotor_disc_pmMA_500x5_12mm_bore_m6_v2", "class": "CUT_PMMA", "material": "cast PMMA 5 mm; inner-shaft hub bore"},
        {"name": "lamella_chromesteel_0p2x20x160_m6_v2", "class": "METAL_LAMELLA", "material": "~0.2 mm chrome-steel/magnetically responsive sheet per source family"},
        {"name": "stator_perforated_metal_electrode_m6_v2", "class": "METAL_ELECTRODE", "material": "conductive perforated sheet; document alloy"},
        {"name": "inner_shaft_12mm_x300_m6_v2", "class": "METAL_SHAFT", "material": "12 mm precision steel/stainless"},
        {"name": "outer_hollow_shaft_25od_16id_x180_m6_v2", "class": "METAL_SHAFT", "material": "25 mm OD / 16 mm ID precision tube, lab-derived"},
        {"name": "bearing_tower_6001_nonmagnetic_m6_v2", "class": "MACHINED_BEARING_SUPPORT", "material": "12 mm G10/FR4 structural laminate or 6061-T6; precision bearing seat"},
        {"name": "bearing_tower_6805_nonmagnetic_m6_v2", "class": "MACHINED_BEARING_SUPPORT", "material": "12 mm G10/FR4 structural laminate or 6061-T6; precision bearing seat"},
        {"name": "large_cylinder_*_grid_*", "class": "METAL_MESH", "material": "rolled metal grid/mesh"},
        {"name": "large_cylinder_*_pmMA_sleeve_*", "class": "PMMA_DIELECTRIC", "material": "real PMMA/acrylic sleeve"},
        {"name": "large_cylinder_bifilar_copper_winding_path_m6_v2", "class": "WIND_COPPER", "material": "~18 AWG enamelled copper, source family; exact turns remain working-fit"},
    ],
    "purchased_components": [
        {"qty": 2, "item": "6001-2RS bearing", "spec": "12x28x8 mm, low-runout"},
        {"qty": 2, "item": "6805-2RS bearing", "spec": "25x37x7 mm, low-runout"},
        {"qty": 2, "item": "balanced metal disc hub/clamp", "spec": "one for 12 mm shaft, one for 25 mm hollow shaft"},
        {"qty": 2, "item": "round belt", "spec": "3-4 mm polyurethane, one open and one crossed path for lab counterrotation"},
        {"qty": 1, "item": "low-voltage geared motor", "spec": "external laboratory drive only; input power measured"},
        {"qty": 2, "item": "capacitor module", "spec": "removable/guarded experimental module; value/topology intentionally not claimed historical"},
        {"qty": 2, "item": "horseshoe magnetic assembly", "spec": "document material, geometry and field; keep removable"},
        {"qty": 18, "item": "isolated terminal/binding post", "spec": "three groups of six for open-node breakout"},
        {"qty": 1, "item": "rotor guard", "spec": "polycarbonate preferred; complete enclosure around 500 mm discs"},
        {"qty": 1, "item": "fastener set", "spec": "M4/M5/M6; nonmagnetic where magnetic confounding matters"},
    ],
}
(META / "FABRICATION_MANIFEST_M6_V2.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

with (META / "PURCHASED_COMPONENTS_M6_V2.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["qty", "item", "spec"])
    for row in manifest["purchased_components"]:
        w.writerow([row["qty"], row["item"], row["spec"]])

with (META / "CUT_LIST_M6_V2.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["qty", "part", "material", "process"])
    w.writerow([1, "baseplate 760x340x18", "birch/phenolic/nonconductive structural plate", "CNC/router/saw + drill"])
    w.writerow([1, "front rotor disc Ø500x5 / 25.3 mm hub bore", "cast PMMA", "CNC/router + drill; balance after lamella installation"])
    w.writerow([1, "rear rotor disc Ø500x5 / 12.3 mm hub bore", "cast PMMA", "CNC/router + drill; balance after lamella installation"])
    w.writerow([150, "lamella 0.2x20x160", "chrome-steel/magnetically responsive sheet", "laser/waterjet/shear; deburr; 50 front + 100 rear-face total target"])
    w.writerow([14, "stator electrode 104x34", "conductive perforated metal", "laser/waterjet/shear; 8 front + 6 rear"])
    w.writerow([6, "rolled cylinder grid", "metal grid/mesh", "cut/roll; three per side cylinder"])
    w.writerow([4, "PMMA cylinder sleeve", "cast PMMA/acrylic tube/sheet", "cut/roll/machine to fit"])
    w.writerow([1, "inner shaft Ø12x300", "precision steel/stainless", "cut + deburr"])
    w.writerow([1, "outer shaft tube 25OD/16IDx180", "precision steel/stainless tube", "cut + face ends"])
    w.writerow([2, "6001 bearing tower", "12 mm G10/FR4 or 6061-T6", "CNC/mill; finish bore coaxially on assembled datum"])
    w.writerow([2, "6805 bearing tower", "12 mm G10/FR4 or 6061-T6", "CNC/mill; finish bore coaxially on assembled datum"])

print("M6 V2 fabrication kit generated at", OUT.relative_to(ROOT))