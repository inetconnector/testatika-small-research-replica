#!/usr/bin/env python3
"""
Parametric core CAD generator for the Testatika Small Marinov First Machine V2.

Historical uncertainty is explicit. Generated release assets in hardware/
remain authoritative for this release; this source regenerates the core
evidence-bearing geometry.
"""
from pathlib import Path
import cadquery as cq
import math

ROOT=Path(__file__).resolve().parents[1]
STL=ROOT/"hardware/stl"
STEP=ROOT/"hardware/step"
STL.mkdir(parents=True,exist_ok=True)
STEP.mkdir(parents=True,exist_ok=True)

ROTOR_D=200.0
ROTOR_T=4.0
ROTOR_CENTER_Z=160.0
SHAFT_D=8.2
BEARING_OD=22.25
POT_OD=84.0
POT_H=110.0
M3=3.4

def rr(w,d,h,r=3):
    o=cq.Workplane("XY").box(w,d,h,centered=(True,True,False))
    try:
        o=o.edges("|Z").fillet(r)
    except Exception:
        pass
    return o

def export(name,obj):
    cq.exporters.export(obj,str(STL/f"{name}.stl"),tolerance=0.12,angularTolerance=0.25)
    cq.exporters.export(obj,str(STEP/f"{name}.step"))

def rotor(count):
    p=cq.Workplane("XY").circle(ROTOR_D/2).extrude(ROTOR_T)
    p=p.union(cq.Workplane("XY").circle(21).extrude(8))
    p=p.faces(">Z").workplane().hole(20.4)
    for a in range(0,360,60):
        x=15*math.cos(math.radians(a)); y=15*math.sin(math.radians(a))
        p=p.faces(">Z").workplane().center(x,y).hole(M3)
    for i in range(count):
        a=math.radians(i*360/count)
        for rad in (27,94):
            x=rad*math.cos(a); y=rad*math.sin(a)
            p=p.faces(">Z").workplane().center(x,y).hole(1.75)
    return p

def hub(front):
    p=cq.Workplane("XY").circle(20).extrude(10)
    if front:
        p=p.union(cq.Workplane("XY").circle(12).extrude(18))
    p=p.faces(">Z").workplane().hole(SHAFT_D)
    for a in range(0,360,60):
        x=15*math.cos(math.radians(a)); y=15*math.sin(math.radians(a))
        p=p.faces(">Z").workplane().center(x,y).hole(M3)
    return p

def bearing_tower():
    p=rr(50,32,9,3)
    p=p.union(rr(30,18,ROTOR_CENTER_Z-26,3).translate((0,0,9)))
    p=p.union(cq.Workplane("XZ").center(0,ROTOR_CENTER_Z).circle(20).extrude(18,both=True))
    p=p.cut(cq.Workplane("XZ").center(0,ROTOR_CENTER_Z).circle(BEARING_OD/2).extrude(20,both=True))
    return p

def electrode_wedge():
    outer=[(-7,0),(7,0),(18,62),(-18,62)]
    inner=[(-3,7),(3,7),(12,55),(-12,55)]
    return (cq.Workplane("XY").polyline(outer).close().extrude(3)
            .cut(cq.Workplane("XY").polyline(inner).close().extrude(5).translate((0,0,-1))))

def pot_shell():
    return (cq.Workplane("XY").circle(POT_OD/2).circle(POT_OD/2-2.5).extrude(POT_H)
            .union(cq.Workplane("XY").circle(46).circle(31).extrude(7))
            .union(cq.Workplane("XY").circle(46).circle(31).extrude(7).translate((0,0,POT_H-7))))

def pot_grid():
    return cq.Workplane("XY").circle(37).circle(35).extrude(96)

def pot_dielectric():
    return cq.Workplane("XY").circle(33).circle(31).extrude(92)

def pot_spiral_mandrel():
    return (cq.Workplane("XY").circle(21).circle(18).extrude(88)
            .union(cq.Workplane("XY").circle(25).circle(18).extrude(4))
            .union(cq.Workplane("XY").circle(25).circle(18).extrude(4).translate((0,0,84))))

def horseshoe_mount():
    return (rr(66,34,8,3)
            .union(rr(8,28,55,2).translate((-27,0,8)))
            .union(rr(8,28,55,2).translate((27,0,8))))

def crystal_bridge():
    return rr(118,26,10,3).union(cq.Workplane("XY").circle(15).extrude(24).translate((0,0,10)))

def main():
    export("rotor_20wire",rotor(20))
    export("rotor_24wire",rotor(24))
    export("rotor_25wire",rotor(25))
    export("hub_front",hub(True))
    export("hub_rear",hub(False))
    export("bearing_tower",bearing_tower())
    export("electrode_wedge_frame",electrode_wedge())
    export("pot_outer_shell",pot_shell())
    export("pot_grid_former",pot_grid())
    export("pot_acrylic_sleeve_jig",pot_dielectric())
    export("pot_spiral_mandrel",pot_spiral_mandrel())
    export("horseshoe_magnet_mount",horseshoe_mount())
    export("crystal_bridge",crystal_bridge())
    print("Core V2 CAD regenerated.")

if __name__=="__main__":
    main()
