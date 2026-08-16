#!/usr/bin/env python3
"""
Optional evidence-led V3 experiment assets for the Testatika Small Research Replica.

This generator does NOT replace the V2 baseline. It adds:
- R4 rotor variants implementing the Holzherr-reported "changing sides three times"
  wire-routing hypothesis as a testable geometry, not as a claimed M2 original.
- A geometry-controlled A/B electrode fixture for blinded mesh-vs-foil experiments.

Historical uncertainty is explicit. Conductive inserts are real metal foil / mesh;
printed parts are only mechanical carriers, templates and gap gauges.
"""
from pathlib import Path
import cadquery as cq
import math

ROOT = Path(__file__).resolve().parents[1]
STL = ROOT / "hardware/stl"
STEP = ROOT / "hardware/step"
STL.mkdir(parents=True, exist_ok=True)
STEP.mkdir(parents=True, exist_ok=True)

ROTOR_D = 200.0
ROTOR_T = 4.0
M3 = 3.4
M4 = 4.5
WIRE_GROOVE_W = 1.4
WIRE_GROOVE_D = 0.65
R4_RADII = (27.0, 40.0, 60.0, 80.0, 94.0)


def rr(w, d, h, r=2.5):
    obj = cq.Workplane("XY").box(w, d, h, centered=(True, True, False))
    try:
        obj = obj.edges("|Z").fillet(r)
    except Exception:
        pass
    return obj


def export(name, obj):
    cq.exporters.export(obj, str(STL / f"{name}.stl"), tolerance=0.12, angularTolerance=0.25)
    cq.exporters.export(obj, str(STEP / f"{name}.step"))


def radial_groove(r0, r1, angle_deg, z0, depth):
    length = r1 - r0
    center_r = (r0 + r1) / 2
    part = cq.Workplane("XY").box(length, WIRE_GROOVE_W, depth, centered=(True, True, False))
    part = part.translate((center_r, 0, z0))
    return part.rotate((0, 0, 0), (0, 0, 1), angle_deg)


def rotor_r4(count):
    """R4 research rotor with exactly three through-disc side changes per sector.

    Intended wire path:
      front 27->40 mm,
      rear  40->60 mm,
      front 60->80 mm,
      rear  80->94 mm.

    Crossovers occur at 40, 60 and 80 mm. Holes at 27 and 94 mm are endpoint
    anchors. This geometry is a testable interpretation of Holzherr's report and
    is not asserted to be the verified Marinov M2 original.
    """
    p = cq.Workplane("XY").circle(ROTOR_D / 2).extrude(ROTOR_T)
    p = p.union(cq.Workplane("XY").circle(21).extrude(8))
    p = p.faces(">Z").workplane().hole(20.4)

    for a in range(0, 360, 60):
        x = 15 * math.cos(math.radians(a))
        y = 15 * math.sin(math.radians(a))
        p = p.faces(">Z").workplane().center(x, y).hole(M3)

    for i in range(count):
        angle = i * 360.0 / count
        ar = math.radians(angle)
        for rad in R4_RADII:
            x = rad * math.cos(ar)
            y = rad * math.sin(ar)
            p = p.faces(">Z").workplane().center(x, y).hole(1.75)

        p = p.cut(radial_groove(27, 40, angle, ROTOR_T - WIRE_GROOVE_D, WIRE_GROOVE_D + 0.05))
        p = p.cut(radial_groove(40, 60, angle, -0.05, WIRE_GROOVE_D + 0.05))
        p = p.cut(radial_groove(60, 80, angle, ROTOR_T - WIRE_GROOVE_D, WIRE_GROOVE_D + 0.05))
        p = p.cut(radial_groove(80, 94, angle, -0.05, WIRE_GROOVE_D + 0.05))
    return p


def electrode_ab_carrier():
    """Common carrier; same geometry is used for both conductive materials."""
    p = rr(58, 88, 4, 3)
    p = p.faces(">Z").workplane().rect(44, 72).cutThruAll()
    for x in (-25, 25):
        for y in (-39, 39):
            p = p.faces(">Z").workplane().center(x, y).hole(M3)
    p = p.union(rr(18, 18, 4, 2).translate((0, -53, 0)))
    return p.faces(">Z").workplane().center(0, -53).hole(M4)


def electrode_ab_clamp():
    p = rr(58, 88, 2.2, 2.5)
    p = p.faces(">Z").workplane().rect(44, 72).cutThruAll()
    for x in (-25, 25):
        for y in (-39, 39):
            p = p.faces(">Z").workplane().center(x, y).hole(M3)
    return p


def electrode_material_template():
    """Tracing/drilling template for equally sized metal foil or mesh inserts."""
    p = rr(54, 84, 1.2, 2)
    for x in (-25, 25):
        for y in (-39, 39):
            p = p.faces(">Z").workplane().center(x, y).hole(2.0)
    for x in (-22, 22):
        for y in (-36, 36):
            p = p.faces(">Z").workplane().center(x, y).hole(1.0)
    return p


def gap_gauge(gap_mm):
    """U-shaped non-conductive gauge for repeatable electrode/rotor gaps."""
    p = rr(28, 3, 36, 1.5)
    for i in range(int(round(gap_mm))):
        p = p.faces(">Z").workplane().center(-8 + i * 5, 0).hole(1.5)
    tongue = cq.Workplane("XY").box(gap_mm, 18, 15, centered=(True, True, False)).translate((0, 0, 36))
    return p.union(tongue)


def main():
    for count in (20, 24, 25):
        export(f"rotor_{count}wire_R4_3cross", rotor_r4(count))

    export("electrode_ab_carrier", electrode_ab_carrier())
    export("electrode_ab_clamp", electrode_ab_clamp())
    export("electrode_material_template", electrode_material_template())
    for gap in (1, 2, 3):
        export(f"electrode_gap_gauge_{gap}mm", gap_gauge(gap))

    print("V3 experiment assets regenerated: R4 rotors + grid/foil A/B fixture.")


if __name__ == "__main__":
    main()
