# M2 V4.31 — pot-envelope reservoir and buffer feasibility bound

**Date:** 2026-08-20  
**Status:** **DERIVED / HYPOTHESIS discriminator. Not a historical material or wiring claim.**

## 1. Purpose

V4.30 showed that the historical load reports must be separated into **continuous running** versus **short load episodes**. In particular, Holzherr's 1999 witness report describes a ~50-cm machine running during an approximately 1.5-hour visit, while the explicitly mentioned `1000 W` lamp was connected for only about `10 s`. A short load burst therefore does not by itself prove a continuous kilowatt reservoir.

V4.31 now asks a narrower geometric question for the current **small M2 research-CAD pot envelope**:

1. Is there enough visible cylindrical area for a low-power surface reservoir to recharge a burst store slowly?
2. Is there enough physical volume for a finite matter reservoir?
3. Could the simple visible `grid + dielectric + copper spiral` geometry itself hide a `10 kJ` electrostatic buffer?

The answer is mixed:

- **surface/chemical finite-energy storage is not geometrically excluded at the few-watt / few-Wh burst scale;**
- **the simple M2 pot geometry is excluded by many orders of magnitude as a 10-kJ electrostatic capacitor store.**

Canonical calculator:

`sim/m2_v4_31_pot_envelope_reservoir_bound.py`

Regression tests:

`tests/test_m2_v4_31_pot_envelope_reservoir_bound.py`

---

## 2. Evidence boundary before using any dimensions

The direct Marinov small-machine line supports the **construction class** of the side pots:

- cylindrical conductive grid;
- cylindrical plastic insulation;
- central copper spiral;
- two visible external wires per pot.

It does **not** supply exact original pot diameter, height, capacitance, spiral turns, dielectric constant, hidden chemistry or a recovered internal circuit.

The numerical dimensions used below come from the current V4 research CAD and are explicitly reconstruction working values:

- pot external envelope: `84 mm OD × 110 mm high`;
- grid-former envelope: approximately `74 mm diameter × 96 mm high`;
- spiral-mandrel envelope: approximately `42 mm diameter × 88 mm high`.

Therefore every numerical result in V4.31 is a **replica-envelope bound**, not a measurement of an original Testatika.

---

## 3. Generous visible electrode-envelope area

Treat both grid cylinders and both spiral envelopes as if their full cylindrical lateral area were active:

`A = 2 * [pi * D_grid * H_grid + pi * D_spiral * H_spiral]`.

For the current V4 dimensions:

- two grids: `0.04464 m²`;
- two spiral envelopes: `0.02322 m²`;
- generous total envelope: **`0.06786 m²`**.

This is deliberately favorable to a surface-process hypothesis. The real microscopic active area could be larger if the surface is rough/porous, or smaller if only part of the structure is electrochemically wetted/coupled.

---

## 4. Burst recharge changes the surface-power target

A `1000 W × 10 s` episode corresponds to

`E_burst = 10,000 J`.

If that energy were accumulated over `1.5 h = 5400 s`, the required average recharge power would be only

`P_recharge = 10,000 / 5400 = 1.85 W`.

Spread over the generous `0.06786 m²` two-pot envelope, the required average real-power density is

**`27.3 W/m²`.**

Using the V4.29 literature comparison of `6.7 W/m²` for a modern moisture/redox harvester only as a scale reference, the required effective active area would be about

**`4.07 ×`**

the visible smooth-cylinder envelope.

That is a very different result from continuous-output assumptions:

| required average power | density over 0.06786 m² | area multiplier vs 6.7 W/m² |
|---:|---:|---:|
| `1.85 W` | `27.3 W/m²` | `4.07 ×` |
| `100 W` | `1474 W/m²` | `220 ×` |
| `1 kW` | `14.7 kW/m²` | `2200 ×` |

**Interpretation:** a simple passive moisture-harvester interpretation is still too weak even for the slow-recharge case at the visible smooth area, but only by a single-digit area factor rather than millions/billions. A deliberately rough, porous, multilayer or chemically active internal surface could in principle close that geometric area gap. No such hidden M2 structure is source-supported at present.

This comparison must not be misread as saying that all redox chemistry is limited to `6.7 W/m²`; battery-like reactions have different rate limits. The benchmark is only a discriminator for the specific moisture-harvesting class.

---

## 5. Bounding volume: finite matter storage easily fits the burst-energy quantity

The external volume of two ideal `84 mm × 110 mm` cylinders is approximately

**`1.219 L`.**

That is an **upper bounding volume**, not actual free internal volume. Shells, grid, PMMA, spiral, terminals, clearances and air occupy part of it.

If energy were stored somewhere inside that bounding volume, the required volumetric energy densities would be:

| energy requirement | equivalent | density over 1.219 L |
|---:|---:|---:|
| `10 kJ` | `2.78 Wh` | **`2.28 Wh/L`** |
| `100 W × 1.5 h` | `150 Wh` | **`123 Wh/L`** |
| `1 kW × 1.5 h` | `1500 Wh` | **`1230 Wh/L`** |

The first number is tiny by ordinary chemical-storage standards. Therefore **geometry alone cannot exclude a finite hidden matter reservoir for a single 10-kJ burst**.

The source evidence is the limiting factor: Marinov's M2 pot description does not report a battery stack, liquid electrolyte, third electrode, multilayer galvanic pile or other obvious high-capacity reservoir. Thus `fits in the volume` is not evidence that it was present.

---

## 6. Simple visible pots fail catastrophically as a 10-kJ electrostatic buffer

To make the capacitor comparison favorable, replace the sparse copper spiral by a **solid inner coaxial cylinder**, replace the grid by a continuous outer cylinder, and assume the whole inter-electrode region has relative permittivity `er = 3`.

Using approximately:

- inner radius `a = 21 mm`;
- outer radius `b = 35 mm`;
- active length `L = 88 mm`;
- two identical pots;

an ideal coaxial calculation gives only about

**`57.5 pF` for the pair.**

This is already more favorable than the real sparse `spiral + grid + partial dielectric` geometry.

Stored energy is

`E = 1/2 C V²`.

The resulting ideal pair energies are approximately:

| voltage | simple two-pot stored energy |
|---:|---:|
| `300 V` | `2.59 µJ` |
| `10 kV` | `2.88 mJ` |
| `50 kV` | `0.0719 J` |
| `100 kV` | **`0.288 J`** |

A `10 kJ` burst at `100 kV` would instead require

`C = 2 µF`.

That is about

**`34,800 ×`**

the optimistic simple-pair capacitance.

At `50 kV`, the required capacitance is `8 µF`, about

**`139,000 ×`**

the optimistic simple-pair capacitance.

Therefore:

> **The visible/simple M2 side pots cannot be a 10-kJ electrostatic buffer unless their real internal construction differs radically from the direct small-machine grid/plastic/spiral description.**

This is one of the strongest negative results in the current reservoir search.

---

## 7. Consequence for the V4.30 architecture

V4.30 proposed the conventional chain:

`distributed matter reservoir -> slow recharge -> electrostatic/resonant routing -> crystal gate -> HV buffer -> short load burst`.

V4.31 now splits that chain further.

### Still geometrically possible

- a **few-Wh chemical / redox / other matter reservoir** occupying part of the pot or another machine volume;
- a **few-watt average recharge path**;
- a larger microscopic surface area than the smooth visible envelope;
- the crystal/rotor network acting as control, commutation or voltage transformation rather than bulk source.

### Not plausible in the simple M2 geometry

- storing `10 kJ` directly as ordinary electrostatic energy in the two visible side pots;
- treating `57 pF`-class visible-pot capacitance as a hidden kilojoule reservoir;
- using resonance to evade the energy requirement. Resonance can circulate/reactively magnify voltage but cannot turn `0.3 J` of stored field energy into a repeatable `10 kJ` load event without replenishment.

---

## 8. Important cross-family caution

The `1000 W for ~10 s` witness episode belongs to the **~50-cm machine family**, not to Marinov's small M2. Holzherr separately relayed that large capacitors could contain many perforated-sheet layers.

Therefore V4.31 does **not** claim that the large machine had only `57.5 pF`, nor does it import the large-machine multilayer capacitor into M2.

The purpose of using the 10-kJ episode here is purely to establish scale:

- if an M2-sized simple pot pair were asked to buffer such an event electrostatically, it fails by ~`10^4–10^5` even at tens to 100 kV;
- a large-machine buffer must be analyzed from its own geometry and dielectric stack before any conclusion is made.

---

## 9. New highest-value discriminator

The reservoir question now separates into two experimentally different possibilities:

### A. Matter reservoir + direct/slow conversion

Prediction:

- measurable long-term chemical/material/thermal change;
- storage recovery after load follows chemistry / transport timescale;
- total extractable energy is finite unless reactants are replenished.

### B. Large hidden electrical buffer charged from a smaller source

Prediction:

- measurable pre-load stored field energy;
- load pulse produces a calculable voltage droop;
- recharge curve reveals the real average source power;
- the required capacitance can be measured directly with isolated low-energy instrumentation before high-voltage operation.

The decisive experimental quantity is therefore no longer peak voltage. It is:

`E_store(t) before load -> E_store(t) after load -> recovery slope dE/dt`.

If a claimed kilowatt burst occurs without a corresponding decrease in any measured electrical, mechanical, thermal or chemical store and without sufficient incoming boundary power, only then does an `UNKNOWN` residual survive.

---

## 10. Working conclusion

V4.31 materially narrows the search:

1. **A finite chemical/matter reservoir can easily fit the energy quantity of a short 10-kJ demonstration inside an M2-sized volume.** This is a volume/energy statement only, not historical evidence.
2. **A pure smooth-surface moisture harvester remains too weak**, although slow 1.85-W recharge reduces the area gap to only about `4×` relative to the cited 6.7-W/m² comparison.
3. **The simple visible M2 pots cannot hide a 10-kJ electrostatic buffer.** Even an optimistic solid-coax/`er=3` approximation stores only about `0.29 J` at `100 kV` for both pots combined.
4. Therefore a burst-buffer explanation, if real, requires either a **radically different hidden capacitor structure elsewhere**, a **chemical/matter store capable of direct burst delivery**, or a historically overstated/mischaracterized load episode.
5. The bulk source remains **UNKNOWN**. V4.31 does not promote chemistry, Cu2O, dry piles, Casimir/vacuum coupling or any other candidate into the historical baseline.
