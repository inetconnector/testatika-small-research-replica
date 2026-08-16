# Scientific status

## Conclusion

The historical Testatika is credible as a real electrostatic-machine research project. Its visible electrostatic core mechanisms are compatible with established physics. The historically claimed large net power output is **not supported by a closed, independently reproducible energy balance** in the available material.

A renewed source audit of Paul Baumann/Methernitha explanations supports a more precise conventional working model:

> **self-excited / primed electrostatic influence and variable-capacitance system + non-contact pickups + polarity-selective charge routing + nonlinear crystal/diode commutation + storage/drive buses + model-dependent downstream impedance conditioning.**

See [`research/baumann-language-decoding.md`](research/baumann-language-decoding.md).

## Important source correction

A literal Marinov statement that Baumann's explanation sounded like an "unknown language" has not been verified. The supported facts are instead:

- Marinov did not understand the complete operating principle or exact schematic;
- Hans Holzherr reported that Baumann's explanations were difficult to understand because they were delivered softly/quickly and in non-scientific terms;
- Methernitha's own technical description says conventional physical terminology was, in its view, only partly adequate and uses special terms such as `Taster` / `antenna keys`.

## Conventional mechanisms relevant here

- electrostatic influence
- variable capacitance `C(theta)`
- non-contact capacitive / influence pickup
- displacement current
- electrostatic motor torque
- floating-potential nodes
- surface-charge storage on/inside dielectrics
- charge storage in capacitors
- rectification / nonlinear charge gating
- phase-selective electrostatic commutation
- corona / ion transport
- humidity-dependent surface leakage
- transient resonance and impedance transformation

None of these mechanisms requires new physics.

## Technical interpretation of Methernitha vocabulary

| Historical vocabulary | Conservative engineering translation |
|---|---|
| earth / cloud | opposite potential / field reservoirs |
| grid holds charge | field-forming or floating capacitive electrode |
| Taster / antenna key | non-contact capacitive/influence pickup |
| sort/order charge | polarity-selective routing / rectification |
| diode keeps cycle in rhythm | phase-selective clamp / electrostatic commutator |
| slow and steady | compatibility with RC/leakage/corona relaxation time |
| grid condenser | charge reservoir / buffer |
| increase capacity | change capacitance / charge storage / impedance, not energy creation |
| build up power | power conditioning / U-I transformation, not proof of gain |
| rectify random particles | asymmetric carrier transport; energy source still must be identified |

## Strongest present mechanism hypothesis

The most coherent reconstruction is **charge-state management** rather than a hidden Tesla coil or permanent-magnet energy source:

1. a charged/primed rotor establishes an electrostatic field;
2. rotor motion changes the capacitance matrix relative to fixed electrodes;
3. non-contact pickups acquire induced/displacement current;
4. nonlinear paths route charge only during selected rotor phases;
5. a high-voltage drive/bias state can be regenerated while a separate storage/load state is charged;
6. capacitors smooth the resulting pulses;
7. larger machines may add inductive/capacitive impedance-conversion stages.

This architecture can explain many observed components **without** explaining a net-energy surplus.

## Mathematical minimum

For a multi-node system:

`Q_i = sum_j C_ij(theta) * (V_i - V_j)`

and

`I_i = dQ_i/dt`.

A rotating geometry therefore produces current through both voltage change and `dC/dt`.

For a simplified voltage-driven element, electrostatic torque scales with:

`tau_e ~ 1/2 * V^2 * dC/dtheta`.

A diode/crystal makes the network piecewise nonlinear and can create phase-selective charge transfer. This is a natural technical interpretation of the historical phrases `sort`, `rectify`, and `keep in rhythm`.

## Requirements for an energy anomaly

A credible claim would require simultaneous measurement of:

- mechanical torque and angular velocity;
- all electrical bias/input supplies;
- auxiliary power;
- initial stored capacitor/electret energy;
- final stored energy;
- output voltage and current at a known load;
- time-resolved real power;
- humidity, temperature and relevant environmental fields;
- uncertainty bounds;
- sufficiently long operation to exclude stored-energy transients;
- independent replication.

The most important load test is whether extracting real output power produces:

- additional rotor braking;
- additional bias recharge current;
- depletion of stored field energy;
- or a measurable external/environmental input.

This repository therefore uses **energy conservation as the null hypothesis**.
