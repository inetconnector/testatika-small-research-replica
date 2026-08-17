# M2 regenerative-grid working model

## Purpose

This document turns the current Testatika M2 research hypothesis into a falsifiable numerical model. It does **not** claim to reproduce the historical wiring and it does **not** assume over-unity.

The model asks a narrower question:

> Can the observed small-M2 geometry plausibly support a self-excited electrostatic feedback loop in which mesh/grid electrodes, floating rotor sectors, side-pot spirals, and a one-way `crystal`/diode charge path create regenerative voltage growth?

## Current synthesis

The strongest working interpretation is a mechanically clocked electrostatic network with:

1. 24 individually floating rotor sectors.
2. An angle-dependent capacitance matrix `C(theta)` rather than a single scalar capacitance.
3. Left/right grid electrodes that act as field-forming and feedback electrodes.
4. Inner left/right spirals that provide a second electrostatic node inside each side pot.
5. Mesh-dependent field penetration, making each pot effectively a three-electrode structure: rotor/environment -> grid -> spiral.
6. Phase-selective charge transfer through a diode/`crystal` element.
7. Possible cross-coupling between opposite sides, analogous to regenerative influence machines and self-excited variable-capacitance generators.

The governing relation is:

```text
q = C(theta) v
```

For a charge state `q`, electrostatic field energy is:

```text
U = 1/2 q^T v
```

Any increase in `U` caused only by prescribed rotor motion is booked as mechanical work. Passive diode/valve transfers conserve total free charge and may only reduce electrostatic field energy.

## Why the grid matters

The grid is modeled differently from continuous foil because a mesh can permit substantially more field coupling from a passing rotor sector to the inner spiral while still carrying its own potential. This is a testable geometric hypothesis, not a known historical fact.

The code therefore exposes two cases:

- `foil`: very small rotor-to-spiral penetration through the outer electrode;
- `mesh`: larger rotor-to-spiral penetration.

The penetration factor must eventually be replaced by measured or FEM-derived mutual capacitances.

## Four primary falsification cases

The simulator always supports the following matrix:

| Case | Outer electrode | Cross feedback |
|---|---|---|
| A | foil | OFF |
| B | mesh | OFF |
| C | foil | ON |
| D | mesh | ON |

For each revolution the code measures an amplitude and computes the late per-revolution loop gain:

```text
g = A[n+1] / A[n]
```

A genuine regenerative build-up requires sustained `g > 1` while the energy balance remains closed.

## First numerical result

With the deliberately simple two-edge cross-valve topology

```text
SPIRAL_L -> GRID_R
SPIRAL_R -> GRID_L
```

and the baseline four stationary nodes, the model does **not** self-excite. It redistributes the initial seed charge and then settles to `g ~= 1`.

This negative result is useful: it means the desired behavior was not smuggled into the model. It also points to missing structure.

## What is probably missing

The best conventional analogue found so far is Charles H. Goldie's 1961 US patent **US3013201A, “Self-excited variable capacitance electrostatic generator.”** Its regenerative topology is richer than the current four-node baseline. It uses separate induction/charging and stator/collector functions, rectifiers, a load path, and cross-coupled output feedback between two generator sections.

That strongly suggests the Testatika search should next test at least these additional model elements:

1. Separate stationary **induction electrode** and **collector/pickup electrode** per side instead of collapsing them into one grid/spiral pair.
2. A storage/output node per side.
3. Multiple rectifier paths rather than only one cross diode per side.
4. A defined feedback fraction from stored output back to the opposite induction electrode.
5. Possible non-zero or history-dependent free charge on rotor sectors rather than the present neutral-sector baseline.
6. Surface/electret charge on PMMA as an explicit state variable.
7. Corona/space-charge current as a separately switchable hypothesis, never hidden inside a capacitance term.

## Sector timing

For 24 sectors the sector-event frequency is:

```text
f_sector = 24 * rpm / 60
```

Thus:

- 15 rpm -> 6 Hz
- 30 rpm -> 12 Hz
- 60 rpm -> 24 Hz

The relevant diode, leakage, dielectric-relaxation, and corona time constants should therefore be searched in relation to sector events, not merely the 0.25-1 Hz shaft rotation rate.

## Required bench measurements

The numerical placeholders should be replaced in this order:

1. `C(rotor sector, GRID_L/R, theta)`
2. `C(rotor sector, SPIRAL_L/R, theta)` for mesh and foil
3. `C(GRID_L, SPIRAL_L)` and right-side equivalent
4. left/right cross-capacitances
5. leakage resistance versus humidity
6. diode/`crystal` I-V curve at the relevant high-impedance scale
7. surface potential / retained charge of PMMA after controlled conditioning

The most important experiment newly emphasized by this model is direct measurement of **rotor-to-inner-spiral mutual capacitance through the outer grid**, then repeating the same measurement with solid foil.

## Energy-accounting rule

Every candidate topology must obey:

```text
E_initial + W_mechanical + E_external_bias + E_external_environment
  = E_final + E_load + E_losses
```

The baseline simulator has no external environment source. Therefore any apparent electrical field-energy growth must be matched by mechanical work. A residual above numerical tolerance is a model bug, not evidence of anomalous energy.

## Interpretation of an eventual `g > 1`

Even if a later topology produces `g > 1`, this proves only **regenerative voltage/charge build-up**. It does not by itself prove excess energy. Wimshurst, Kelvin-type influence systems, Bennet doublers, and other electrostatic charge pumps can all show strong voltage growth while obeying energy conservation.

The energy-origin question begins only after a topology reproduces the reported electrical behavior and its complete mechanical, stored-field, leakage, corona, and environmental power flows are measured.

## Run

```bash
python sim/m2_regenerative_grid_model.py --revolutions 40 --steps-per-rev 96 --sweep
python sim/m2_regenerative_grid_model.py --revolutions 8 --steps-per-rev 48 --search-topologies
python -m unittest discover -s tests -v
```

CSV traces can be written with:

```bash
python sim/m2_regenerative_grid_model.py --csv-dir out
```

## Next model version

`M2-V2` should implement a Goldie-like two-section regenerative generator as a **control topology** next to the Testatika geometry. If that control self-excites in the simulator while the simple Testatika four-node hypothesis does not, the exact missing electrical roles can then be introduced one at a time and tested against the historical M2 constraints.
