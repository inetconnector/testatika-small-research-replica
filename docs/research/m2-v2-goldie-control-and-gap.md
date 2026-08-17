# M2-V2 — Goldie control, regeneration threshold, and the missing rotor state

## Purpose

This note compares the current M2 capacitance-network hypothesis with a known self-excited variable-capacitance electrostatic-generator topology without assuming an energy surplus.

The control is Charles H. Goldie's US 3,013,201. The patent uses a moving electrically neutral capacitive link between a charging/induction electrode and a stator/collector, rectifies the induced stator voltage, and returns part of the opposite section output to the charging electrode. A prime mover supplies the mechanical work.

The comparison is deliberately functional rather than a claim that the Testatika uses Goldie's exact circuit.

## 1. Goldie control model

`sim/goldie_self_excited_control.py` implements a reduced symmetric two-section model with:

- variable capacitance `Cmax -> Cmin`;
- opposite-polarity sections;
- one-time startup reference;
- passive cross-feedback fraction `beta`;
- rectified output storage;
- optional load and voltage limiter;
- explicit startup, shaft-work, storage, load, limiter, and conversion-loss energy ledger.

For the reduced model, the ideal small-signal voltage condition is

```text
G0 = beta * (Cmax/Cmin - 1) > 1
```

or

```text
beta_critical = 1 / (Cmax/Cmin - 1).
```

With the default control values

```text
Cmax = 100 pF
Cmin = 20 pF
Cmax/Cmin = 5
beta = 0.4
G0 = 1.6
beta_critical = 0.25
```

the one-time seed grows in the reduced model. The growth is not free energy: the increase in stored electrostatic energy is supplied by shaft work and the energy ledger must close.

The control is useful because it establishes that the simulator can represent ordinary regenerative electrostatic voltage growth without inserting an unexplained source term.

## 2. Bridge diagnostic applied to the current M2 model

`sim/m2_goldie_bridge.py` computes the angle-dependent effective differential capacitance for every pair among

```text
GRID_L, GRID_R, SPIRAL_L, SPIRAL_R
```

using the current 24-sector `q_rotor = 0` Schur-complement model. It then applies the reduced Goldie threshold as a diagnostic.

With the present placeholder M2 capacitances, the aggregate pair capacitances change only by roughly `10^-4 ... 10^-3` fraction over one revolution. Representative values from the default parameter set are:

```text
mesh GRID_L--GRID_R:   Cmax/Cmin ~= 1.000825   beta_critical ~= 1.21e3
mesh GRID_L--SPIRAL_R: Cmax/Cmin ~= 1.000497   beta_critical ~= 2.01e3
foil GRID_L--GRID_R:   Cmax/Cmin ~= 1.001187   beta_critical ~= 8.42e2
```

A passive returned-output fraction satisfies `beta <= 1`. Therefore the current aggregate four-node model is far below the reduced Goldie self-excitation threshold.

This is a falsification of one narrow hypothesis:

> **Four stationary nodes + individually neutral floating rotor sectors + the present lumped local coupling geometry are not sufficient to produce Goldie-like regenerative growth.**

It is not a falsification of the historical Testatika.

## 3. Why this result changes the M2 model

The current model makes two simplifying assumptions at once:

1. each rotor wire has zero net free charge (`q_i = 0`);
2. its angular coupling is represented as if the conductor were local to one sector position.

The evidence supports the first statement only in the weaker topological sense that the wires are `connected to nothing`: each conductor is floating and isolated from the other sectors. That does **not** imply that a conductor has no spatially separated polarization state.

A long floating conductor can remain net neutral while positive and negative induced surface charge reside at different portions of the same equipotential conductor. Goldie's patent explicitly exploits this kind of neutral moving capacitive link: one end is influenced by a charging electrode while the opposite end influences a stator.

This makes the unresolved Testatika through-disc wire route much more important than it appeared in the first M2 model.

## 4. New M2-V2 rotor representation

The next model should preserve each physical rotor wire as one electrically isolated conductor, but give it multiple geometrical coupling lobes.

For sector `i`:

```text
Q_i = sum(surface/lobe charges)
V_i = one conductor potential
```

while its capacitances are distributed over several locations:

```text
front-inner lobe
front-outer lobe
back-inner lobe
back-outer lobe
(optional phase-shifted lobe for R3/R4 routing)
```

The conductor stays equipotential, but the induced surface-charge distribution changes with rotor angle. This allows a net-neutral wire to act as a spatial capacitive shuttle between electrodes without adding any galvanic connection.

The route variants already defined in the repository become electrical model variants:

- `R0`: local one-face radial baseline;
- `R1`: front/back U or stitch route;
- `R3`: angularly shifted through-disc route;
- `R4`: three-side-change weave research route.

R3/R4 are especially important because they can introduce a geometric phase shift between induction and collection regions while retaining `E0` floating electrical topology.

## 5. Additional states to add one at a time

After the distributed floating-wire model, add only one hypothesis at a time:

1. **persistent rotor free charge**: conserve `Q_i != 0` between transfer/leakage events instead of forcing `Q_i = 0`;
2. **separate pickup/stator nodes** beyond `GRID` and `SPIRAL`;
3. **hub arcs / outer panels** as measured capacitive nodes;
4. **crystal/diode switching state** with measured threshold/leakage;
5. **PMMA fixed/trapped charge** as a separately bookkept initial state;
6. **surface leakage / corona / air-ion current** as explicit dissipative or environmental-current terms.

No environmental term may be introduced without appearing as an input in the energy ledger.

## 6. Better regeneration metric: one-cycle state map

A scalar `Cmax/Cmin` ratio is useful for the Goldie control but is not sufficient for the full M2 network.

Define the electrical state just before a repeated rotor phase as

```text
x_n = [Q_rotor[1..24], Q_stationary..., Q_storage..., diode/crystal state...]
```

and numerically advance one mechanical cycle:

```text
x_(n+1) = F(x_n).
```

Linearize around the zero/small-seed state:

```text
M = dF/dx
```

The largest eigenvalue magnitude (spectral radius) is the correct small-signal regeneration test:

```text
rho(M) < 1  -> perturbations decay
rho(M) = 1  -> neutral/marginal state
rho(M) > 1  -> electrical state grows from a small seed
```

Even if `rho(M) > 1`, this says only that the electrostatic state is regenerative. It does **not** establish an energy surplus. The simultaneous energy ledger must still satisfy

```text
Delta E_stored + E_load + E_loss
= E_mechanical + E_bias + E_environment
```

within numerical and experimental uncertainty.

## 7. Most informative next simulation matrix

Run the one-cycle eigenvalue test in this order while keeping all other parameters fixed:

```text
A  E0-R0, Q_i = 0, four stationary nodes
B  E0-R1, Q_i = 0
C  E0-R3, Q_i = 0
D  E0-R4, Q_i = 0
E  best route, conserved seeded Q_i
F  best route + separate pickup nodes
G  best route + crystal/diode state
```

Repeat each case for mesh and solid foil.

The first transition that changes `rho(M)` materially identifies the minimum missing mechanism. This is more informative than tuning arbitrary feedback gain until the model oscillates.

## Current conclusion

The Goldie control demonstrates a conventional route to self-excited electrostatic voltage growth: **spatial capacitive induction + changing capacitance + rectification + cross-feedback + mechanical work**.

The current M2 four-node model lacks enough effective capacitance modulation to realize that route. The strongest evidence-driven next hypothesis is therefore not a mysterious extra energy source but a **spatially distributed floating rotor conductor whose through-disc geometry transfers polarization between phase-separated electrode regions**.

That hypothesis is directly testable in simulation and on the physical R0/R1/R3/R4 rotor variants.
