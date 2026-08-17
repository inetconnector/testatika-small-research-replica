#!/usr/bin/env python3
"""
M6 Large V1 best-evidence CAD generator.

Research reconstruction of the ~500 mm two-disc Testatika large/3-kW visual family,
anchored primarily to Albert Hauser's 1986/1988 direct-visit drawings/correspondence
(M6a) and cross-checked against the historical large-machine videos (M6 umbrella).
Holzherr 1999 (M6b) is retained as a separate configuration source where it differs.

This is a mechanically detailed, modular research build. It does NOT claim recovery
of the original hidden wiring, crystal material, exact magnetic function, or a proven
net-energy anomaly. Unknown electrical connections terminate at explicit open test
nodes rather than being invented.
"""
from __future__ import annotations

from pathlib import Path
import json
import math
import cadquery as cq

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "hardware" / "experimental" / "m6-large-v1-best-evidence"
STL = OUT / "stl"
STEP = OUT / "step"
COMP = OUT / "complete-model"
META = OUT / "metadata"
for p in (STL, STEP, COMP, META):
    p.mkdir(parents=True, exist_ok=True)

DISC_D = 500.0
DISC_T = 5.0
LAMELLA_COUNT = 50
LAMELLA_T = 0.40
LAMELLA_W = 20.0
LAMELLA_L = 160.0
BASE_W, BASE_D, BASE_T = 760.0, 340.0, 28.0
DISC_CENTER_Z = 315.0
DISC_Y_FRONT, DISC_Y_REAR = -11.0, 11.0
SHAFT_D_INNER, SHAFT_D_OUTER = 12.0, 25.0
CYL_OD, CYL_H = 146.0, 235.0
CYL_X = 300.0
CYL_Y = -5.0
CYL_Z = BASE_T


def box(w, d, h, r=1.0):
    p = cq.Workplane("XY").box(w, d, h, centered=(True, True, False))
    if r > 0:
        try:
            p = p.edges("|Z").fillet(r)
        except Exception:
            pass
    return p


def ring(ro, ri, h):
    return cq.Workplane("XY").circle(ro).circle(ri).extrude(h)


def compound(*objs):
    shapes = []
    for obj in objs:
        if obj is None:
            continue
        if isinstance(obj, (list, tuple)):
            for x in obj:
                if x is not None:
                    shapes.extend(x.vals() if hasattr(x, 'vals') else [x])
        else:
            shapes.extend(obj.vals() if hasattr(obj, 'vals') else [obj])
    return cq.Compound.makeCompound(shapes)


def export_pair(name, obj, tol=0.18):
    cq.exporters.export(obj, str(STL / f"{name}.stl"), tolerance=tol, angularTolerance=0.30)
    cq.exporters.export(obj, str(STEP / f"{name}.step"))


def perforated_plate(w, h, t, cols=8, rows=3, hole_w=6.0, hole_h=8.0, frame=5.0):
    p = cq.Workplane("XY").rect(w, h).extrude(t)
    xs = [(-w/2+frame) + i*((w-2*frame)/max(cols-1,1)) for i in range(cols)]
    ys = [(-h/2+frame) + j*((h-2*frame)/max(rows-1,1)) for j in range(rows)]
    for x in xs:
        for y in ys:
            p = p.cut(cq.Workplane("XY").center(x,y).rect(hole_w,hole_h).extrude(t+2).translate((0,0,-1)))
    return p


def base_platform():
    base = box(BASE_W, BASE_D, BASE_T, 5)
    patterns=[]
    for cx in (-CYL_X, CYL_X):
        for a in (45,135,225,315):
            x=cx+58*math.cos(math.radians(a)); y=CYL_Y+58*math.sin(math.radians(a))
            patterns.append((x,y,6.5))
    for y in (-70,70):
        for x in (-24,24): patterns.append((x,y,6.5))
    for cx in (-120,120):
        for dx in (-34,34):
            for dy in (-18,18): patterns.append((cx+dx,-105+dy,5.2))
    for x in (-105,105): patterns.append((x,-145,5.2))
    for x in (-285,285):
        for y in (-95,95): patterns.append((x,y,6.5))
    for x,y,d in patterns:
        try:
            base=base.faces(">Z").workplane().center(x,y).hole(d)
        except Exception:
            pass
    rails = [box(BASE_W-40, 18, 10, 2).translate((0, y, BASE_T)) for y in (-125, 125)]
    feet = []
    for x in (-BASE_W/2+35, BASE_W/2-35):
        for y in (-BASE_D/2+35, BASE_D/2-35):
            feet.append(cq.Workplane("XY").circle(13).extrude(10).translate((x,y,-10)))
    return compound(base, rails, feet)


def disc_blank():
    p = cq.Workplane("XY").circle(DISC_D/2).extrude(DISC_T)
    p = p.faces(">Z").workplane().hole(SHAFT_D_OUTER + 1.0)
    for a in range(0,360,60):
        x,y=28*math.cos(math.radians(a)),28*math.sin(math.radians(a))
        p = p.faces(">Z").workplane().center(x,y).hole(4.2)
    return p


def lamella_sector_pack(face="outer"):
    items=[]
    for i in range(LAMELLA_COUNT):
        a=i*360/LAMELLA_COUNT
        strip = cq.Workplane("XY").box(LAMELLA_L, LAMELLA_W, LAMELLA_T, centered=(True,True,False))
        strip = strip.translate((165,0,0)).rotate((0,0,0),(0,0,1),a)
        items.append(strip)
    return compound(items)


def front_disc_assembly():
    blank=disc_blank()
    lam=lamella_sector_pack().translate((0,0,DISC_T))
    hub=ring(42,13,8).translate((0,0,DISC_T+LAMELLA_T))
    return compound(blank,lam,hub)


def rear_disc_assembly():
    blank=disc_blank()
    lam1=lamella_sector_pack().translate((0,0,DISC_T))
    lam2=lamella_sector_pack().translate((0,0,-LAMELLA_T))
    hub=ring(42,13,8).translate((0,0,DISC_T+LAMELLA_T))
    return compound(blank,lam1,lam2,hub)


def verticalize(obj, y, z=DISC_CENTER_Z):
    return obj.rotate((0,0,0),(1,0,0),90).translate((0,y,z))


def shaft_system():
    inner = cq.Workplane("XY").circle(SHAFT_D_INNER/2).extrude(150).rotate((0,0,0),(1,0,0),90).translate((0,75,DISC_CENTER_Z))
    outer = cq.Workplane("XY").circle(SHAFT_D_OUTER/2).circle(7.25).extrude(105).rotate((0,0,0),(1,0,0),90).translate((0,52.5,DISC_CENTER_Z))
    spacers=[]
    for y in (-25,-3,3,25):
        spacers.append(ring(34,13,5).rotate((0,0,0),(1,0,0),90).translate((0,y,DISC_CENTER_Z)))
    return compound(inner,outer,spacers)


def bearing_pedestal(y):
    post = box(54,24,220,3).translate((0,y,BASE_T))
    cap = box(80,28,44,4).translate((0,y,DISC_CENTER_Z-22))
    bore = cq.Workplane("XZ").circle(17).extrude(40,both=True).translate((0,y,DISC_CENTER_Z))
    try:
        cap = cap.cut(bore)
    except Exception:
        pass
    brace1 = box(18,22,155,2).rotate((0,0,0),(0,1,0),-18).translate((-48,y,BASE_T+35))
    brace2 = box(18,22,155,2).rotate((0,0,0),(0,1,0),18).translate((48,y,BASE_T+35))
    return compound(post,cap,brace1,brace2)


def grid_tube(radius, height, n_vertical=28, n_rings=22, wire=1.8):
    parts=[]
    for i in range(n_vertical):
        a=math.radians(i*360/n_vertical)
        x=radius*math.cos(a); y=radius*math.sin(a)
        bar=box(wire,wire,height,0.25).translate((x,y,0)).rotate((0,0,0),(0,0,1),i*360/n_vertical)
        parts.append(bar)
    for j in range(n_rings):
        z=4+j*((height-8)/max(n_rings-1,1))
        parts.append(ring(radius+wire/2,radius-wire/2,wire).translate((0,0,z)))
    return compound(parts)


def acrylic_sleeve(ro, ri, height):
    return ring(ro,ri,height)


def bifilar_winding(radius=23.0, height=170.0, pitch=4.5, wire_r=0.65):
    h1=cq.Wire.makeHelix(pitch=pitch,height=height,radius=radius)
    c1=cq.Workplane("XZ").circle(wire_r).sweep(h1)
    h2=cq.Wire.makeHelix(pitch=pitch,height=height,radius=radius+1.6)
    c2=cq.Workplane("XZ").circle(wire_r).sweep(h2).rotate((0,0,0),(0,0,1),180)
    return compound(c1,c2)


def central_magnet_tube():
    shell=ring(18,12,185)
    cap1=cq.Workplane("XY").circle(18).extrude(7)
    cap2=cq.Workplane("XY").circle(18).extrude(7).translate((0,0,178))
    return compound(shell,cap1,cap2)


def large_cylinder_core():
    g1=grid_tube(66,205,30,24,1.8)
    s1=acrylic_sleeve(62.0,59.5,199).translate((0,0,3))
    g2=grid_tube(56,199,26,22,1.6).translate((0,0,3))
    s2=acrylic_sleeve(52.0,49.5,193).translate((0,0,6))
    g3=grid_tube(46,193,24,20,1.6).translate((0,0,6))
    magnet=central_magnet_tube().translate((0,0,10))
    coil=bifilar_winding(23,170,4.5,0.65).translate((0,0,18))
    foil1=ring(26,25.3,174).translate((0,0,16))
    return compound(g1,s1,g2,s2,g3,magnet,coil,foil1)


def large_cylinder_complete():
    base=ring(CYL_OD/2+5,50,8)
    core=large_cylinder_core().translate((0,0,10))
    top=ring(CYL_OD/2+7,50,8).translate((0,0,CYL_H-8))
    copper_ring=ring(CYL_OD/2+10,CYL_OD/2+4,5).translate((0,0,CYL_H+2))
    term=[]
    for a in (45,135,225,315):
        x=(CYL_OD/2+2)*math.cos(math.radians(a)); y=(CYL_OD/2+2)*math.sin(math.radians(a))
        term.append(cq.Workplane("XY").circle(2.6).extrude(18).translate((x,y,CYL_H+5)))
    return compound(base,core,top,copper_ring,term)


def large_cylinder_cutaway():
    return large_cylinder_core()


def stationary_electrode():
    plate=perforated_plate(104,34,2.5,9,3,6,7,6)
    edge=box(104,5,4,0.8).translate((0,14.5,2.5))
    tabs=box(14,12,8,1).translate((-40,-23,0)).union(box(14,12,8,1).translate((40,-23,0)))
    return compound(plate,edge,tabs)


def place_electrode(angle_deg, y, tangent=True, extra_angle=0.0):
    r=DISC_D/2+33
    a=math.radians(angle_deg)
    x=r*math.cos(a); z=DISC_CENTER_Z+r*math.sin(a)
    p=stationary_electrode().rotate((0,0,0),(1,0,0),90)
    rot = (-angle_deg + (90 if tangent else 0) + extra_angle)
    p=p.rotate((0,0,0),(0,1,0),rot).translate((x,y,z))
    return p


def stationary_electrode_sets():
    front_angles=[-42,-12,22,52,82,112,142,168]
    rear_angles=[-30,10,50,90,130,170]
    front=[place_electrode(a,-31,True,0) for a in front_angles]
    rear=[]
    for idx,a in enumerate(rear_angles):
        extra=45 if idx>=4 else 0
        rear.append(place_electrode(a,31,True,extra))
    return compound(front,rear)


def horseshoe_core():
    left=box(16,28,80,2).translate((-30,0,0))
    right=box(16,28,80,2).translate((30,0,0))
    bridge=box(76,28,18,2).translate((0,0,0))
    return compound(left,right,bridge)


def coil_bobbin_leg(x):
    rings=[]
    for z in range(28,72,3):
        rings.append(ring(15,9,2).translate((x,0,z)))
    return compound(rings)


def perforated_pole_stack(x):
    layers=[]
    for k in range(4):
        p=perforated_plate(28,34,1.5,3,3,5,6,4).translate((x,0,82+k*3))
        layers.append(p)
    return compound(layers)


def horseshoe_wound_module():
    return compound(horseshoe_core(),coil_bobbin_leg(-30),coil_bobbin_leg(30),perforated_pole_stack(-30),perforated_pole_stack(30))


def capacitor_can(od=74,h=112):
    shell=ring(od/2,od/2-2.5,h)
    top=cq.Workplane("XY").circle(od/2).extrude(5).translate((0,0,h))
    posts=[]
    for x in (-14,14):
        posts.append(cq.Workplane("XY").circle(2.5).extrude(15).translate((x,0,h+5)))
    return compound(shell,top,posts)


def spiral_pipe():
    tube=ring(18,14,115).rotate((0,0,0),(0,1,0),90)
    helix=cq.Wire.makeHelix(pitch=9,height=110,radius=20)
    coil=cq.Workplane("XZ").circle(1.0).sweep(helix).rotate((0,0,0),(0,1,0),90)
    return compound(tube,coil)


def horizontal_grid_cage(length=150, radius=22, n_long=18, n_rings=12, wire=1.5):
    cage=grid_tube(radius,length,n_long,n_rings,wire)
    return cage.rotate((0,0,0),(0,1,0),90)


def top_crystal_rectifier_module():
    cage=horizontal_grid_cage(150,22,18,12,1.5)
    core=cq.Workplane("XY").circle(8).extrude(92).rotate((0,0,0),(0,1,0),90)
    coil=[]
    for x in range(-44,45,5):
        coil.append(ring(14,12.5,2).rotate((0,0,0),(0,1,0),90).translate((x,0,0)))
    glass=box(76,32,3,2).translate((0,-2,22))
    crystals=[]
    for x in (-22,0,22):
        crystal=box(10,8,7,1).rotate((0,0,0),(0,0,1),45).translate((x,-2,25))
        crystals.append(crystal)
    end1=cq.Workplane("XY").circle(24).extrude(10).rotate((0,0,0),(0,1,0),90).translate((-80,0,0))
    end2=cq.Workplane("XY").circle(24).extrude(10).rotate((0,0,0),(0,1,0),90).translate((70,0,0))
    mounts=[box(8,18,55,1).translate((-72,0,-55)), box(8,18,55,1).translate((72,0,-55))]
    return compound(cage,core,coil,glass,crystals,end1,end2,mounts)


def drive_motor_body():
    body=cq.Workplane("XY").circle(30).extrude(80).rotate((0,0,0),(1,0,0),90)
    shaft=cq.Workplane("XY").circle(5).extrude(35).rotate((0,0,0),(1,0,0),90).translate((0,-40,0))
    foot=box(86,65,10,2).translate((0,0,-38))
    return compound(body,shaft,foot)


def magnet_timing_wheel():
    wheel=ring(58,46,8).rotate((0,0,0),(1,0,0),90)
    tabs=[]
    for i in range(12):
        a=math.radians(i*30)
        x=67*math.cos(a); z=67*math.sin(a)
        tab=box(16,8,10,1).rotate((0,0,0),(1,0,0),90).rotate((0,0,0),(0,1,0),-i*30).translate((x,0,z))
        tabs.append(tab)
    hub=ring(18,7,14).rotate((0,0,0),(1,0,0),90)
    return compound(wheel,tabs,hub)


def drive_regulator_module():
    motor=drive_motor_body().translate((95,96,115))
    wheel=magnet_timing_wheel().translate((0,96,DISC_CENTER_Z))
    pulley=ring(24,6,10).rotate((0,0,0),(1,0,0),90).translate((95,55,115))
    belt1=box(8,4,205,1).rotate((0,0,0),(0,1,0),-24).translate((48,91,178))
    belt2=box(8,4,205,1).rotate((0,0,0),(0,1,0),-15).translate((30,91,207))
    return compound(motor,wheel,pulley,belt1,belt2)


def terminal_board():
    board=box(250,42,10,2)
    holes=board
    for row,y in enumerate((-12,0,12)):
        for col in range(6):
            x=-100+col*40
            try:
                holes=holes.faces(">Z").workplane().center(x,y).hole(5.2)
            except Exception:
                pass
    partitions=[box(4,38,14,1).translate((-20,0,0)),box(4,38,14,1).translate((60,0,0))]
    return compound(holes,partitions)


def lab_drive_pulley(radius=46.0, width=10.0, bore=13.0):
    p=ring(radius,bore/2,width)
    try:
        groove=cq.Workplane("XZ").circle(2.2).sweep(cq.Wire.makeCircle(radius-2.0))
        p=p.cut(groove)
    except Exception:
        pass
    return p


def adjustable_lab_motor_mount():
    plate=box(120,78,8,3)
    cradle=ring(24,21,58).rotate((0,0,0),(1,0,0),90).translate((0,0,28))
    cradle=cradle.cut(box(60,30,70,1).translate((0,-20,0)))
    uprights=compound(box(8,70,55,2).translate((-45,0,8)),box(8,70,55,2).translate((45,0,8)))
    return compound(plate,cradle,uprights)


def lab_counterrotation_drive():
    p1=lab_drive_pulley(48,10,25.5).rotate((0,0,0),(1,0,0),90).translate((0,103,DISC_CENTER_Z))
    p2=lab_drive_pulley(48,10,12.5).rotate((0,0,0),(1,0,0),90).translate((0,121,DISC_CENTER_Z))
    mount=adjustable_lab_motor_mount().translate((112,105,BASE_T))
    mp1=lab_drive_pulley(28,8,5.5).rotate((0,0,0),(1,0,0),90).translate((112,103,112))
    mp2=lab_drive_pulley(28,8,5.5).rotate((0,0,0),(1,0,0),90).translate((112,121,112))
    b1a=box(4,4,230,1).rotate((0,0,0),(0,1,0),-26).translate((56,103,202))
    b1b=box(4,4,230,1).rotate((0,0,0),(0,1,0),-18).translate((43,103,220))
    b2a=box(4,4,245,1).rotate((0,0,0),(0,1,0),-31).translate((58,121,205))
    b2b=box(4,4,245,1).rotate((0,0,0),(0,1,0),-10).translate((32,121,212))
    return compound(p1,p2,mount,mp1,mp2,b1a,b1b,b2a,b2b)


def guard_frame():
    posts=[]
    for x in (-285,285):
        for y in (-95,95):
            posts.append(box(12,12,590,2).translate((x,y,BASE_T)))
    top1=box(590,12,12,2).translate((0,-95,BASE_T+578))
    top2=box(590,12,12,2).translate((0,95,BASE_T+578))
    return compound(posts,top1,top2)


def mechanical_frame():
    front=bearing_pedestal(-70)
    rear=bearing_pedestal(70)
    cross=box(470,28,22,3).translate((0,-70,185))
    rearcross=box(470,28,22,3).translate((0,70,185))
    sidebrace=[]
    for x in (-230,230):
        sidebrace.append(box(20,24,310,2).rotate((0,0,0),(0,1,0), -12 if x<0 else 12).translate((x,0,BASE_T+25)))
    return compound(front,rear,cross,rearcross,sidebrace)


def complete_assembly(include_guard=False):
    parts=[]
    parts.append(base_platform())
    parts.append(mechanical_frame())
    parts.append(verticalize(front_disc_assembly(),DISC_Y_FRONT))
    parts.append(verticalize(rear_disc_assembly(),DISC_Y_REAR))
    parts.append(shaft_system())
    parts.append(stationary_electrode_sets())
    parts.append(large_cylinder_complete().translate((-CYL_X,CYL_Y,CYL_Z)))
    parts.append(large_cylinder_complete().translate((CYL_X,CYL_Y,CYL_Z)))
    parts.append(horseshoe_wound_module().translate((-120,-105,BASE_T)))
    parts.append(horseshoe_wound_module().translate((120,-105,BASE_T)))
    parts.append(capacitor_can(78,112).translate((-55,-108,BASE_T)))
    parts.append(capacitor_can(62,92).translate((42,-108,BASE_T)))
    parts.append(spiral_pipe().translate((-5,-118,88)))
    parts.append(top_crystal_rectifier_module().translate((0,-8,600)))
    parts.append(drive_regulator_module())
    parts.append(terminal_board().translate((0,-145,BASE_T)))
    if include_guard:
        parts.append(lab_counterrotation_drive())
        parts.append(guard_frame())
    return compound(parts)


def service_exploded_assembly():
    parts=[base_platform()]
    parts.append(verticalize(front_disc_assembly(),-40,DISC_CENTER_Z))
    parts.append(verticalize(rear_disc_assembly(),40,DISC_CENTER_Z))
    parts.append(large_cylinder_complete().translate((-300,-20,CYL_Z)))
    parts.append(large_cylinder_cutaway().translate((300,-20,CYL_Z+10)))
    parts.append(top_crystal_rectifier_module().translate((0,0,650)))
    parts.append(horseshoe_wound_module().translate((-120,-120,BASE_T)))
    parts.append(horseshoe_wound_module().translate((120,-120,BASE_T)))
    return compound(parts)


PARTS = {
    "base_platform_m6_v1": base_platform(),
    "front_disc_500mm_50lamella_m6_v1": front_disc_assembly(),
    "rear_disc_500mm_50lamella_both_sides_m6_v1": rear_disc_assembly(),
    "shaft_nested_counterrotation_m6_v1": shaft_system(),
    "bearing_pedestal_m6_v1": bearing_pedestal(0),
    "stationary_electrode_perforated_m6_v1": stationary_electrode(),
    "stationary_electrode_sets_8front_6rear_m6_v1": stationary_electrode_sets(),
    "large_cylinder_complete_3grid_bifilar_m6_v1": large_cylinder_complete(),
    "large_cylinder_cutaway_3grid_bifilar_m6_v1": large_cylinder_cutaway(),
    "large_cylinder_grid_outer_m6_v1": grid_tube(66,205,30,24,1.8),
    "large_cylinder_grid_middle_m6_v1": grid_tube(56,199,26,22,1.6),
    "large_cylinder_grid_inner_m6_v1": grid_tube(46,193,24,20,1.6),
    "large_cylinder_acrylic_outer_m6_v1": acrylic_sleeve(62,59.5,199),
    "large_cylinder_acrylic_inner_m6_v1": acrylic_sleeve(52,49.5,193),
    "large_cylinder_magnet_tube_m6_v1": central_magnet_tube(),
    "large_cylinder_bifilar_winding_m6_v1": bifilar_winding(),
    "horseshoe_wound_module_m6_v1": horseshoe_wound_module(),
    "capacitor_big_m6_v1": capacitor_can(78,112),
    "capacitor_small_m6_v1": capacitor_can(62,92),
    "spiral_pipe_m6_v1": spiral_pipe(),
    "top_crystal_rectifier_blackbox_m6_v1": top_crystal_rectifier_module(),
    "magnet_timing_wheel_m6_v1": magnet_timing_wheel(),
    "drive_regulator_module_m6_v1": drive_regulator_module(),
    "terminal_board_3isolated_open_m6_v1": terminal_board(),
    "lab_counterrotation_drive_m6_v1": lab_counterrotation_drive(),
    "adjustable_lab_motor_mount_m6_v1": adjustable_lab_motor_mount(),
    "lab_drive_pulley_m6_v1": lab_drive_pulley(),
    "lab_guard_frame_m6_v1": guard_frame(),
}

for name,obj in PARTS.items():
    print('export',name)
    export_pair(name,obj)

complete=complete_assembly(False)
complete_guard=complete_assembly(True)
exploded=service_exploded_assembly()
print('export complete')
cq.exporters.export(complete,str(COMP/'Testatika_M6_LARGE_V1_BEST_EVIDENCE.step'))
cq.exporters.export(complete,str(COMP/'Testatika_M6_LARGE_V1_BEST_EVIDENCE.stl'),tolerance=0.22,angularTolerance=0.35)
cq.exporters.export(complete_guard,str(COMP/'Testatika_M6_LARGE_V1_SAFE_LAB_GUARDED.step'))
cq.exporters.export(complete_guard,str(COMP/'Testatika_M6_LARGE_V1_SAFE_LAB_GUARDED.stl'),tolerance=0.22,angularTolerance=0.35)
cq.exporters.export(exploded,str(COMP/'Testatika_M6_LARGE_V1_SERVICE_EXPLODED.step'))
cq.exporters.export(exploded,str(COMP/'Testatika_M6_LARGE_V1_SERVICE_EXPLODED.stl'),tolerance=0.22,angularTolerance=0.35)

metadata={
  "schema_version":1,
  "machine_family":"M6a best-evidence large / ~500 mm two-disc research reconstruction",
  "primary_anchor":"Albert Hauser direct-visit report and drawing 3279, 1986/1988",
  "cross_checks":["meth2.asf","meth3.asf","meth5.asf","3kwfront.jpg","3kwrear.jpg"],
  "historical_separation":"M6b/Holzherr-1999 observations are not silently merged when conflicting",
  "direct_anchor_mm":{
    "disc_diameter":DISC_D,"disc_thickness":DISC_T,"lamella_width":LAMELLA_W,"lamella_length":LAMELLA_L,"lamella_count":LAMELLA_COUNT
  },
  "working_fit_mm":{
    "base":[BASE_W,BASE_D,BASE_T],"disc_center_z":DISC_CENTER_Z,"cylinder_od":CYL_OD,"cylinder_height":CYL_H
  },
  "observed_or_source_supported_features":[
    "two large counter-rotating discs","~50 sheet lamellae","non-contact perforated stator electrodes","8 front / 6 rear electrode working count",
    "two large cylinder modules","three concentric metal grids per large cylinder","acrylic separators","central magnet tube","two-layer bifilar winding",
    "wound horseshoe-magnet modules","top crystal/possible-rectifier geometry","magnet-wheel/speed-control family","small DC drive motor in Hauser configuration"
  ],
  "open_unknowns":[
    "complete node-to-node wiring","exact stator grouping/polarity","exact cylinder grid/coil connections","crystal material and I-V","magnet function",
    "exact motor/regulator train geometry","startup/priming procedure","source of claimed net output"
  ],
  "electrical_default":"M6-V1-B0: all unknown electrical networks open at test terminals; only low-voltage lab motor may be powered",
  "scientific_boundary":"No over-unity claim; closed energy balance required for any anomaly claim."
}
(META/'MODEL_INFO_M6_V1.json').write_text(json.dumps(metadata,indent=2)+"\n",encoding='utf-8')
print('done',OUT)
