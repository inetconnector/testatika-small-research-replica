# M6 Large V1 — assembly procedure

## 0. Build philosophy

Assemble the machine in a way that permits **single-variable substitution**. Do not bury unknown electrical joints inside glued parts.

## 1. Base and frame

1. Prepare the ~760 × 340 mm base.
2. Transfer the CAD mounting pattern or use the STEP model as drilling reference.
3. Install front/rear bearing pedestals loosely.
4. Install side-cylinder base rings but leave the cylinders removable.
5. Install the front terminal board and cable channels.
6. Verify the base is flat before rotor alignment.

## 2. Nested shaft and counter-rotating discs

1. Fit the inner shaft through the hollow outer shaft with insulating/mechanical spacers as required by the chosen bearing solution.
2. Mount the front disc to one shaft member and the rear disc to the other.
3. Set the axial disc spacing to the CAD working value, then verify that no lamella/stator can contact the opposite disc.
4. Measure radial runout at the 250 mm radius.
5. Before installing stators, rotate each disc by hand through at least five full turns.

Target for first mechanical qualification:

- no hard contact;
- no bearing bind;
- visibly stable disc plane;
- runout logged rather than assumed.

## 3. Lamella installation

Front disc:

- install 50 radial sheet lamella positions on the designated face.

Rear disc:

- install 50 positions per described face set; the V1 reference models lamellae on both sides of the rear disc.

Keep every lamella installation reversible where possible. Do not add hidden neighbour connections unless testing a named configuration.

## 4. Stationary perforated electrodes

1. Install the eight front and six rear electrode carriers.
2. Use insulated adjustable standoffs.
3. Set a generous initial non-contact gap.
4. Rotate both discs through 360° by hand.
5. Reduce gaps only after measuring disc runout.
6. Bring every electrode to its own terminal before any electrical grouping.

The last rear pair may be tested in the Hauser-noted alternate/45° orientation. Treat orientation as a variable.

## 5. Large cylinders

Build each cylinder from the inside out:

1. central magnet tube;
2. first insulation layer;
3. first winding conductor;
4. interleaved/second winding conductor to produce the bifilar test geometry;
5. second insulation layer;
6. inner grid tube;
7. acrylic separator;
8. middle grid tube;
9. acrylic separator;
10. outer grid tube;
11. base/top retaining rings;
12. top copper/output ring;
13. four isolated laboratory breakout posts.

Do **not** internally bridge grid/winding terminals without a named experiment configuration.

## 6. Horseshoe modules

1. Install the two horseshoe cores.
2. Install separate windings on each leg.
3. Add the layered perforated/insulating pole structures.
4. Route all four leg windings independently to the terminal board.
5. Record magnet orientation. Reverse only one variable at a time.

## 7. Capacitors and spiral pipe

Install the two capacitor positions and the pipe/spiral module as removable units. Exact capacitance and connection are historical unknowns, so the default build uses safe low-energy test capacitors or empty housings until the corresponding experiment begins.

## 8. Top crystal / rectifier black box

The top module is mechanically complete but electrically open by default.

- perforated outer cage;
- internal coil/core carrier;
- glass/window carrier;
- three removable crystal/surrogate seats;
- removable end caps.

No semiconductor/mineral is labelled “original crystal” without evidence.

## 9. Drive and regulation

### Historical-facing assembly

Install the small DC-motor position and magnet/timing wheel geometry as shown in the M6a research reconstruction. Exact transmission details remain working-fit.

### Safe laboratory counterrotation

For reproducible mechanical testing, fit the removable dual-belt fixture:

- one belt drives the outer shaft member;
- one crossed belt drives the inner shaft member in the opposite direction;
- use two separated belt planes;
- keep speed initially below 15 rpm;
- increase toward 60 rpm only after vibration/runout qualification.

This fixture is laboratory instrumentation, not a claim about the historical drivetrain.

## 10. Guard and interlocks

The guarded model supplies standoff geometry. A real build should use a continuous transparent guard around the 500 mm discs and belts, not only the printed posts.

Minimum interlock logic:

- guard open → drive disabled;
- emergency stop removes motor power;
- experimental electrical bias automatically discharges to a verified safe state;
- no access to rotating lamella edges.

## 11. Final pre-run checklist

- all fasteners torqued/marked;
- discs hand-rotated without contact;
- stator gaps measured at multiple angles;
- both disc rpm channels working;
- motor current channel working;
- all unknown electrical nodes open;
- capacitors discharged;
- guard closed;
- configuration ID recorded.

First run must be `M6-V1-LAB-MECH`, not an energy-production test.
