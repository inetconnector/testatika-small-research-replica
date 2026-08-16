# M6 Large V1 — staged run / experiment sequence

The sequence is intentionally conservative: **mechanics → passive characterization → low-energy electrostatics → subsystem coupling → only then load tests**.

## Stage 0 — metrology and as-built record

Record:

- disc diameters/thickness;
- mass and inertia estimate of each disc/lamella assembly;
- shaft runout;
- electrode gap at every stator and at multiple rotor angles;
- cylinder grid diameters/heights;
- winding resistance/inductance of every separate winding conductor;
- capacitor values actually installed;
- magnet field/orientation if magnetic cores are present;
- temperature and relative humidity.

## Stage 1 — hand rotation

Configuration: `M6-V1-B0`.

Pass criteria:

- no contact through 360° on either disc;
- no cable snag;
- no rotor/lamella migration;
- bearings remain smooth.

## Stage 2 — guarded powered mechanical run

Configuration: `M6-V1-LAB-MECH`.

Run both discs counter-rotating using the removable low-voltage fixture.

Sequence:

1. 5 rpm;
2. 10 rpm;
3. 15 rpm;
4. 30 rpm;
5. 45 rpm;
6. 60 rpm only if previous stages pass.

At each point log:

- rpm of each disc independently;
- motor voltage/current/input power;
- bearing temperature;
- vibration;
- acoustic anomalies;
- minimum observed stator clearance.

## Stage 3 — passive electrostatic mapping

No active bias. Use high-impedance probes/electrometers to map:

- charge acquired from handling/rotation;
- front/rear stator potentials;
- grid-to-grid induced potentials;
- top-ring potential;
- humidity dependence.

Repeat with discs stationary as control.

## Stage 4 — stator geometry map

Use one stator at a time or one declared symmetric pair.

Variables:

- angle;
- gap;
- front versus rear;
- 45° rear orientation;
- rpm.

Do not simultaneously change cylinder wiring.

## Stage 5 — large-cylinder characterization

With the cylinder disconnected from other machine networks:

- capacitance matrix among outer/middle/inner grids;
- each grid to magnet tube;
- each grid to each winding conductor;
- winding self/mutual inductance;
- leakage resistance;
- response versus frequency using low-energy instrumentation.

This stage is crucial because surviving sources do not specify the hidden interconnection.

## Stage 6 — bifilar connection controls

Test named configurations only:

- open/open;
- conductor 1;
- conductor 2;
- series aiding;
- series opposing.

Record induced voltage, phase and losses. Never infer “correct historical wiring” from one high reading alone.

## Stage 7 — magnetic dummy controls

Substitute a matched nonmagnetic dummy for the magnetic candidate while keeping geometry fixed.

Test separately:

- cylinder central magnet tube;
- horseshoe modules;
- magnet/timing wheel influence.

## Stage 8 — top-module blackbox controls

Start empty.

Then compare known controls only:

- passive capacitive insert;
- known diode control;
- instrumented candidate material.

No test material is labelled the historical crystal without provenance.

## Stage 9 — coupled low-energy electrostatic experiment

Only after stages 0–8 are characterized, connect a declared subset of stators/cylinder nodes. Use enclosed current-limited electrostatic equipment and low stored energy.

Mandatory accounting:

- motor input;
- bias-source input;
- initial/final capacitor energy;
- load energy;
- all discharge events.

## Stage 10 — load tests

Begin with instrumentation loads, not incandescent-lamp spectacle.

Recommended order:

1. very high resistance measurement load;
2. known resistor with low stored energy;
3. capacitor charging with measured C and V(t);
4. only then more substantial loads if the energy accounting justifies it.

Historical 3-kW/300 V × 10 A claims are not target specifications for initial experiments.

## Stop conditions

Immediately stop if:

- any rotor/stator contact occurs;
- lamella movement is detected;
- bearing temperature rises unexpectedly;
- vibration grows sharply;
- a capacitor cannot be verified discharged;
- unexplained current path reaches the frame/base;
- instrumentation saturates or loses isolation.
