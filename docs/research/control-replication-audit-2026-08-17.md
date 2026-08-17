# Control / replication audit — 2026-08-17

## Purpose

Historical Testatika claims can only be interpreted against conventional electrostatic controls and known measurement failure modes. This file intentionally separates **control evidence** from **historical construction evidence**.

## 1. Marinov's own Wimshurst + electrostatic-motor control

Source:

- Stefan Marinov, *The Thorny Way of Truth, Part VII* (1990), later document mirror:
  https://www.scribd.com/document/117713319/The-Thorny-Way-of-Truth-Part7-Marinov

Marinov built a Wimshurst generator coupled mechanically and electrically to an electrostatic motor. In his additional note he reports that, for the corresponding electrical output/input condition, the generator's braking mechanical power was about **4–5 times greater** than the motor's driving mechanical power.

### Interpretation

- This is a useful **failed closed-loop control** from a Testatika advocate/source author.
- It shows that low apparent electrostatic torque or high voltage does not remove generator reaction.
- It does not prove or disprove Testatika; it establishes the need for simultaneous shaft torque, speed, bias/input power and storage-energy measurement.

## 2. Sven Bönisch 2003

Source:

- Sven Bönisch, “Electrostatic Discharge Power Transformation — An Approach to Understand the Working Principles of the ‘Thestatika’ Free Energy Device”, *ELEKTRIE*, No. 5–8, 2003, ISSN 0013-5399.
- public mirror: https://studfile.net/preview/8197487/

Bönisch explicitly states that his investigated system is based on known electrodynamics and should not exceed 100% efficiency. His laboratory setup used a brushless electrostatic generator and an HV pulse/transmission-line transformation network. The paper reports approximately milliwatt-scale mean load power in the measured configuration and concludes that the tested transformation device obeyed energy conservation; no over-unity effect was detected.

### What can be transferred to this project

- resonant HV waveforms are not themselves evidence of gain;
- parasitic capacitance and probe impedance can detune an electrostatic system;
- low-impedance load-side measurement can be more robust than probing a high-impedance HV node;
- every pulse-forming/storage element must appear in the energy balance.

### What cannot be transferred

- Bönisch's proposed transformer topology is not evidence that Methernitha used that exact topology;
- its measured conventional efficiency cannot be used as a measurement of an original Testatika.

## 3. Rimstar / Steven Dufresne measurement-grounding failure

Experiment index:

- https://rimstar.org/sdenergy/testa/

Rimstar's Testatika testbed notes document that an early experiment involving a nominally floating source was invalidated when the oscilloscope introduced an unintended ground reference. A later configuration corrected the floating measurement approach.

### Repository rule derived from this control

Before any result is accepted from M2/M6:

1. draw the complete galvanic/earth node map including oscilloscope protective earth;
2. include probe shields, USB grounds, DAQ grounds, power-supply PE, motor-controller grounds and computer connections;
3. repeat key measurements with an isolated/differential method appropriate to the voltage range;
4. perform an explicit “instrument connected vs disconnected” disturbance test;
5. document probe/input capacitance because it can materially alter high-impedance electrostatic nodes.

A result that disappears after isolating the measurement instrument is an instrumentation artifact until proven otherwise.

## 4. Testatika-specific null controls now required

### M2 orientation / startup

Because Marinov's direct-author material strengthens the East–West startup statement while separately reporting post-start orientation independence:

- randomize 0–360° azimuth before each startup;
- keep initial mechanical impulse energy controlled;
- log three-axis magnetic field, ambient electric field, RH and temperature;
- test post-start rotation of the whole apparatus independently from startup orientation.

This distinguishes an orientation-correlated startup effect from a generic field/history effect. It does not assume geomagnetism is the cause.

### M2 metal plate

For the direct Marinov metal-plate stop observation:

- plate absent;
- conductive plate floating;
- same plate earth-referenced;
- same plate connected through known R/C;
- nonconductive geometry-matched plate;
- distance sweep;
- plate area sweep.

Measure rotor torque/rpm, C(theta), surface potential and leakage. A capacitive boundary-condition effect must be excluded before invoking an unknown interaction.

### Startup memory / conditioning

Because Marinov reports easier second/third starts:

- fixed rest intervals;
- deliberate neutralization/discharge between selected trials;
- no-discharge history condition;
- surface-potential map before/after runs;
- randomized trial order;
- blind coding of conditioning state where possible.

This can distinguish persistent dielectric charge/electret-like memory from thermal, humidity or operator effects.

## 5. Minimum energy-accounting rule

For any coupled “ready-to-run” machine test:

`E_in = integral(P_mechanical_drive dt) + integral(P_bias dt) + integral(P_aux dt) + E_storage_initial`

`E_out = integral(V_load * I_load dt) + E_storage_final`

Include uncertainty bounds and all storage elements that can materially change state: explicit capacitors, dielectric polarization where measurable, inductors/magnetic cores, batteries/supplies and rotating kinetic energy.

No historical lamp brightness, meter deflection, short arc or lack of visually obvious rpm drop can replace this balance.
