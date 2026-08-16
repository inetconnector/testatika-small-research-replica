#!/usr/bin/env python3
"""
Fast experimental external-geometry reconstruction of the first small Testatika machine
from the high-resolution frontal photograph plus Marinov constraints.

This V3 generator intentionally prioritizes visible layout and printability over hidden
internal certainty. It is an interpretation, not a verified historical CAD recovery.
"""
from pathlib import Path
import cadquery as cq
import math, json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "hardware" / "experimental" / "v3-photo"
STL = OUT / "stl"
STEP = OUT / "step"
COMP = OUT / "complete-model"
for p in (STL, STEP, COMP):
    p.mkdir(parents=True, exist_ok=True)

BASE_W, BASE_D, BASE_T = 370.0, 180.0, 30.0
BACK_W, BACK_H, BACK_T = 336.0, 246.0, 8.0
ROTOR_D, ROTOR_T = 200.0, 3.5
POT_OD, POT_H = 84.0, 110.0


def rr(w,d,h,r=2.0):
    o=cq.Workplane("XY").box(w,d,h,centered=(True,True,False))
    try:o=o.edges("|Z").fillet(r)
    except:pass
    return o


def export_pair(name, obj):
    cq.exporters.export(obj, str(STL/f"{name}.stl"), tolerance=0.12, angularTolerance=0.25)
    cq.exporters.export(obj, str(STEP/f"{name}.step"))


def hole_grid_plate(w,h,t,cols,rows,hole_w=4,hole_h=6,frame=5):
    p = cq.Workplane("XY").rect(w,h).extrude(t)
    x0, x1 = -w/2+frame, w/2-frame
    y0, y1 = -h/2+frame, h/2-frame
    xs = [x0 + i*((x1-x0)/(max(cols-1,1))) for i in range(cols)]
    ys = [y0 + j*((y1-y0)/(max(rows-1,1))) for j in range(rows)]
    for x in xs:
        for y in ys:
            p = p.cut(cq.Workplane("XY").center(x,y).rect(hole_w,hole_h).extrude(t+1).translate((0,0,-0.5)))
    return p


def square_grid_plate(w,h,t,cols,rows,hole=4,frame=3.5):
    p = cq.Workplane("XY").rect(w,h).extrude(t)
    x0, x1 = -w/2+frame, w/2-frame
    y0, y1 = -h/2+frame, h/2-frame
    xs = [x0 + i*((x1-x0)/(max(cols-1,1))) for i in range(cols)]
    ys = [y0 + j*((y1-y0)/(max(rows-1,1))) for j in range(rows)]
    for x in xs:
        for y in ys:
            p = p.cut(cq.Workplane("XY").center(x,y).rect(hole,hole).extrude(t+1).translate((0,0,-0.5)))
    return p


def base_board():
    return rr(BASE_W, BASE_D, BASE_T, 4)


def backplate():
    return rr(BACK_W, BACK_T, BACK_H, 6).rotate((0,0,0),(1,0,0),90)


def rotor(count=24):
    d = cq.Workplane("XY").circle(ROTOR_D/2).extrude(ROTOR_T)
    d = d.faces(">Z").workplane().hole(8.2)
    for a in range(0,360,60):
        x=15*math.cos(math.radians(a)); y=15*math.sin(math.radians(a))
        d = d.faces(">Z").workplane().center(x,y).hole(3.2)
    for i in range(count):
        a=math.radians(i*360/count)
        for r in (28, 92):
            x=r*math.cos(a); y=r*math.sin(a)
            d = d.faces(">Z").workplane().center(x,y).hole(1.7)
    return d


def hub():
    h = cq.Workplane("XY").circle(28).circle(12).extrude(10)
    h = h.faces(">Z").workplane().hole(8.2)
    for a in range(0,360,60):
        x=15*math.cos(math.radians(a)); y=15*math.sin(math.radians(a))
        h = h.faces(">Z").workplane().center(x,y).hole(3.2)
    return h


def pot_shell():
    p = cq.Workplane("XY").circle(POT_OD/2).circle(POT_OD/2-2).extrude(POT_H)
    p = p.union(cq.Workplane("XY").circle(46).circle(31).extrude(9))
    p = p.union(cq.Workplane("XY").circle(46).circle(31).extrude(9).translate((0,0,POT_H-9)))
    return p


def top_module():
    body = rr(170, 28, 18, 3)
    center = hole_grid_plate(100, 30, 3, 10, 4, 5, 5).translate((0,0,18))
    left = square_grid_plate(34, 26, 3, 4, 3, 4).translate((-68,0,18))
    right = square_grid_plate(34, 26, 3, 4, 3, 4).translate((68,0,18))
    post1 = cq.Workplane("XY").circle(2.2).extrude(18).translate((-36,0,0))
    post2 = cq.Workplane("XY").circle(2.2).extrude(18).translate((36,0,0))
    return body.union(center).union(left).union(right).union(post1).union(post2)


def outer_panel():
    frame = hole_grid_plate(88, 74, 3, 8, 4, 4, 9)
    inner = square_grid_plate(54, 28, 3, 6, 3, 4).translate((0,-10,3))
    coil = rr(54, 6, 6, 1).translate((0,14,3))
    return frame.union(inner).union(coil)


def bottom_panel():
    frame = hole_grid_plate(66, 74, 3, 6, 4, 4, 9)
    inner = square_grid_plate(48, 24, 3, 5, 3, 4).translate((0,8,3))
    return frame.union(inner)


def tower():
    return rr(34,26,22,2).union(rr(4,4,74,1).translate((-13,0,22))).union(rr(4,4,74,1).translate((13,0,22))).union(cq.Workplane("YZ").circle(10).extrude(6,both=True).translate((0,0,96)))


def pickup_bar():
    return hole_grid_plate(70,18,3,7,2,4,4).union(rr(24,10,8,1).translate((-22,0,-8)))


def crossbar_long():
    return hole_grid_plate(110,18,3,10,2,4,4)


def crossbar_short():
    return hole_grid_plate(36,30,3,4,3,4,4)


def clover_plate():
    base = rr(44, 34, 3, 1.2)
    pts=[]
    for row in range(3):
        n=4-row
        for col in range(n):
            x = col*12 - (n-1)*6 + row*6
            y = row*10 - 10
            pts.append((x,y))
    for x,y in pts:
        base = base.cut(cq.Workplane("XY").center(x,y).circle(3.8).extrude(5).translate((0,0,-1)))
    return base


def spring_wire(height=62.0, turns=8.5, radius=5.0, wire_r=0.75):
    helix = cq.Wire.makeHelix(pitch=height/turns, height=height, radius=radius)
    profile = cq.Workplane("XZ").circle(wire_r)
    return profile.sweep(helix)


def magnet_u():
    return rr(10,22,35,2).translate((-17,0,0)).union(rr(10,22,35,2).translate((17,0,0))).union(rr(44,22,10,2).translate((0,0,35)))


def build_complete(rotor_count=24):
    parts=[]
    parts.append(base_board())
    parts.append(backplate().translate((0,-BASE_D/2 + BACK_T/2 + 8, BASE_T)))
    parts.append(rotor(rotor_count).rotate((0,0,0),(1,0,0),90).translate((0,-10,160)))
    parts.append(hub().rotate((0,0,0),(1,0,0),90).translate((0,-5.5,160)))
    parts.append(hub().rotate((0,0,0),(1,0,0),90).translate((0,-14.5,160)))
    parts.append(pot_shell().translate((-143,-4,30)))
    parts.append(pot_shell().translate((143,-4,30)))
    parts.append(top_module().rotate((0,0,0),(1,0,0),90).translate((0,-6,258)))
    parts.append(hole_grid_plate(18,88,4,2,8,4,4).rotate((0,0,0),(1,0,0),90).translate((0,-4,169)))
    parts.append(outer_panel().rotate((0,0,0),(1,0,0),90).translate((-118,-8,210)))
    parts.append(outer_panel().rotate((0,0,0),(1,0,0),90).translate((118,-8,210)))
    parts.append(bottom_panel().rotate((0,0,0),(1,0,0),90).translate((0,-6,44)))
    parts.append(tower().rotate((0,0,0),(1,0,0),90).translate((-47,-8,168)))
    parts.append(tower().rotate((0,0,0),(1,0,0),90).translate((47,-8,168)))
    parts.append(spring_wire().rotate((0,0,0),(1,0,0),90).translate((-47,-1,176)))
    parts.append(spring_wire().rotate((0,0,0),(1,0,0),90).translate((47,-1,176)))
    parts.append(spring_wire(74,12,5,0.7).rotate((0,0,0),(1,0,0),90).translate((-57,-1,58)))
    parts.append(spring_wire(74,12,5,0.7).rotate((0,0,0),(1,0,0),90).translate((57,-1,58)))
    parts.append(pickup_bar().rotate((0,0,0),(0,0,1),-36).rotate((0,0,0),(1,0,0),90).translate((-23,-1,180)))
    parts.append(pickup_bar().rotate((0,0,0),(0,0,1),36).rotate((0,0,0),(1,0,0),90).translate((23,-1,180)))
    parts.append(crossbar_long().rotate((0,0,0),(1,0,0),90).translate((-71,-6,122)))
    parts.append(crossbar_long().rotate((0,0,0),(1,0,0),90).translate((71,-6,122)))
    parts.append(crossbar_short().rotate((0,0,0),(1,0,0),90).translate((-38,-6,126)))
    parts.append(crossbar_short().rotate((0,0,0),(1,0,0),90).translate((38,-6,126)))
    parts.append(crossbar_short().rotate((0,0,0),(1,0,0),90).translate((-20,-6,98)))
    parts.append(crossbar_short().rotate((0,0,0),(1,0,0),90).translate((20,-6,98)))
    parts.append(clover_plate().rotate((0,0,0),(1,0,0),90).translate((-94,-4,87)))
    parts.append(clover_plate().rotate((0,0,0),(1,0,0),90).translate((94,-4,87)))
    parts.append(magnet_u().translate((-44,-8,30)))
    parts.append(magnet_u().translate((44,-8,30)))
    return cq.Compound.makeCompound([p.val() for p in parts])


def main():
    export_pair('rotor_24wire_v3_photo', rotor(24))
    export_pair('top_module_v3_photo', top_module())
    export_pair('outer_panel_v3_photo', outer_panel())
    export_pair('side_pot_v3_photo', pot_shell())
    asm = build_complete(24)
    cq.exporters.export(asm, str(COMP/'Testatika_Small_Marinov_FirstMachine_V3_PHOTO_INTERP.stl'), tolerance=0.15, angularTolerance=0.3)
    cq.exporters.export(asm, str(COMP/'Testatika_Small_Marinov_FirstMachine_V3_PHOTO_INTERP.step'))
    (COMP/'MODEL_INFO_V3.json').write_text(json.dumps({
        'name':'Testatika_Small_Marinov_FirstMachine_V3_PHOTO_INTERP',
        'status':'experimental',
        'basis':['high-resolution frontal photo','Stefan Marinov Part V','existing V2 photogrammetry'],
        'notes':['external arrangement emphasized','internal circuit remains provisional','black-grid material unresolved']
    }, indent=2), encoding='utf-8')
    print('V3 photo interpretation assets generated.')

if __name__=='__main__':
    main()
