# M6 Large V1 — electrical boundary and terminal map

## Core rule

The large-machine geometry is much better documented than the complete wiring. Therefore the V1 build is **terminal-complete but circuit-open**.

## Historical evidence that constrains the electrical model

- non-contact perforated electrodes recur around the disc;
- the large cylinders contain three concentric metal grids separated by acrylic;
- a central magnet tube and two-layer bifilar winding are described;
- top copper rings are reported as an output location;
- Hauser reports a machine that appears to contain three isolated circuits that must work together;
- a top crystal/possible-rectifier assembly is described, but exact material/topology is unknown;
- a small DC drive motor exists in the Hauser large-machine configuration;
- historical output figures are not independently closed energy balances.

## Canonical test-node groups

The CAD terminal board provides 18 open positions in three isolated groups.

### Group A — front/rear electrostatic field system

Recommended breakout allocation:

- A1–A8: front stator electrodes individually;
- A9–A14: rear stator electrodes individually;
- additional stator guard/reference connections stay on separate auxiliary blocks if needed.

Do not pre-group them into +/− rails.

### Group B — left/right cylinder internals

Each side cylinder should expose independently:

- outer grid;
- middle grid;
- inner grid;
- bifilar winding conductor 1;
- bifilar winding conductor 2;
- central magnet tube / shield reference if conductive;
- top copper ring.

Use additional local breakout blocks if the 18-position central board is insufficient.

### Group C — horseshoe / capacitor / top module

Keep independent:

- four horseshoe leg-winding ends per side module as applicable;
- big capacitor terminals;
- smaller capacitor terminals;
- spiral-pipe conductor(s);
- top module coil/core terminals;
- each crystal/surrogate seat terminal.

## `M6-V1-B0` electrical state

Baseline/open state:

- all stator electrodes open except measurement probes;
- all cylinder grids open;
- bifilar conductors open and separately measurable;
- magnet tube electrically isolated unless a measurement requires reference;
- top copper rings open;
- horseshoe windings open;
- capacitors discharged/open;
- crystal seats empty/open;
- load disconnected;
- lab electrostatic bias disconnected;
- low-voltage motor disconnected unless performing mechanical qualification.

This is the only honest “ready” state before experiments because the hidden historical circuit is unresolved.

## Safe laboratory energization boundary

This repository does **not** provide an open mains-derived high-voltage power-supply design.

When introducing electrostatic bias:

- use enclosed, current-limited laboratory/educational electrostatic equipment;
- keep stored energy deliberately low;
- add known discharge resistors;
- record initial stored energy;
- instrument the motor input separately;
- account for every bias source, initial charge and capacitor state in any energy balance.

## Forbidden baseline shortcuts

Do not call the machine historically faithful if you silently:

- connect all stators into two guessed buses;
- connect all three cylinder grids together;
- treat the magnet tube as a power source;
- substitute a Tesla transformer network without an explicit experimental label;
- install an arbitrary crystal/diode and call it original;
- hide a mains/HV supply inside the base;
- omit the drive-motor input from power accounting.

## Historical claim test boundary

Any claim of net output requires, at minimum:

1. motor electrical input integrated over time;
2. all electrostatic/bias source energy integrated over time;
3. initial/final capacitor energy;
4. mechanical kinetic-energy change;
5. measured load energy;
6. uncertainty bounds;
7. repeated controls with the active module removed/dummied;
8. independent replication.
