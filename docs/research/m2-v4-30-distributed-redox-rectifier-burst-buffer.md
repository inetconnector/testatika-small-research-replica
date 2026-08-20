# M2 V4.30 — distributed redox reservoir + rectifying winding + burst buffer

**Date:** 2026-08-20  
**Status:** **HYPOTHESIS / cross-family discriminator. Not a historical wiring or material claim.**

## 1. Why V4.30 changes the power question

The historical witness corpus does not justify treating every reported high-power load as a continuous high-power output for the entire demonstration.

Hans Holzherr's 1999 report says the ~50-cm machine continued running during an approximately 1.5-hour visit, but the specifically reported `1000 W` lamp was connected for only about `10 s`; the heater and arc observations were shorter still. Therefore:

`machine observed running for ~1.5 h` **does not imply** `1000 W continuously for ~1.5 h`.

The reported lamp episode corresponds to only

`1000 W * 10 s = 10,000 J = 2.7778 Wh`.

If a finite reservoir/HV store had accumulated those 10 kJ over the full 1.5 h, the required average recharge power would be only

`10,000 J / 5,400 s = 1.85 W`.

Even a 30-minute recharge interval would require only about `5.56 W` average.

This does not validate the witness power figure. It changes the falsification target: a **slowly charged store followed by a short high-power burst** is a conventional alternative that must be excluded before a kilowatt-class continuous reservoir is inferred.

Canonical calculator:

`sim/m2_v4_30_burst_buffered_redox.py`

Regression tests:

`tests/test_m2_v4_30_burst_buffered_redox.py`

---

## 2. Source constraints that must remain separated

### Small M2 / Marinov line

Direct Marinov correspondence supports:

- cylindrical conductive grid in each side pot;
- cylindrical plastic insulation;
- central copper spiral;
- two visible external wires per pot;
- floating rotor conductors;
- no conventional drive motor in the described small machine;
- Baumann's direct term `crystal`, with material/function unresolved;
- no Tesla-coil / AC interpretation of the small-machine side spirals.

Therefore V4.30 does **not** insert aluminum, brass, zinc, manganese dioxide, electrolyte, Cu2O, nickel or a dry pile into the historical M2 baseline.

### Holzherr early/original-model line

Holzherr remembered an upper object associated with Baumann's `crystal diode` language and, on an early/original model, a rough coil around one straight central wire with **four leads**. This is an important functional clue but not a solved M2 schematic.

### Principle Experiment / larger layered family

The separate Principle Experiment report describes square-hole perforated aluminum on the moving arm, brass wire mesh in lower plates, additional stacked plates/mesh, and capacitors. The large-machine line also contains perforated layered structures. These facts motivate a **dissimilar-metal / distributed-interface control experiment** in those machine families only. They do not prove that any layer was an electrochemical cell.

---

## 3. The strongest material/function split is now two-stage, not one magical crystal

A single equilibrium rectifying junction cannot be both an inexhaustible reservoir and a passive diode. V4.30 therefore separates two physical jobs.

### A. Bulk-energy branch — distributed matter reservoir

Candidate functional class:

`many small redox / galvanic interfaces`

`-> series/parallel distributed source`

`-> slow recharge of a storage node`.

The exact historical material remains **UNKNOWN**.

A dry-pile-like architecture is a useful control because conventional electrochemistry can produce high voltage by stacking many low-voltage cells. US2762858A describes a Zamboni-type punched laminated dry-cell construction that can be cascaded into a multicell battery. This is a technological precedent only; the zinc/MnO2/wax chemistry in that patent is **not** Testatika evidence.

### B. Routing/gate branch — nonlinear rectifying winding

The strongest concrete test candidate for the unresolved four-terminal / crystal-like module is a **distributed copper/cuprous-oxide rectifying winding**, because a historical electrotechnical precedent actually exists.

US2564881A describes a winding in which a copper conductor carries a cuprous-oxide rectifying layer and a second conductive sheath/contact. Electrically, the device forms two coextensive conductors/coils separated along their length by rectifying material. The patent also gives a Cu/Cu2O/Ni/outer-conductor example.

Separately, Grondahl & Place, *Proceedings of the IRE* 20 (1932), pp. 1599–1614, showed that a copper/cuprous-oxide rectifier could be used for radio-frequency detection when its capacitance was compensated/tuned with inductance.

This makes the following a legitimate **functional test article**:

`inductive branch + distributed Cu/Cu2O nonlinear branch -> four accessible terminals`.

It does **not** establish that Baumann's historical `crystal` was Cu2O.

---

## 4. Thermodynamic scale of copper oxidation

NIST-JANAF gives, at 298.15 K:

- `Delta_f G°(CuO, cr) = -128.292 kJ/mol`;
- `Delta_f G°(Cu2O, cr) = -147.886 kJ/mol`.

Using copper metal and oxygen in their standard states as the reference, ideal maximum free-energy scales are therefore approximately:

- `Cu -> CuO`: **560.8 Wh/kg Cu**;
- `2 Cu -> Cu2O`: **323.2 Wh/kg Cu**.

These are **thermodynamic ceilings**, not practical electrical specific energies. Real surface oxidation can be drastically slower, passivated, kinetically blocked, dissipative, or incapable of delivering useful current without an appropriate ionic/electrochemical pathway.

For comparison, V4.29 used `1878 Wh/kg` as a practical aluminum-air literature scale. This remains a generic comparison rather than evidence that aluminum powered a Testatika.

---

## 5. The 10-kJ burst changes the required hidden-material scale

For a hypothetical verified `1 kW * 10 s = 10 kJ` burst, the active-material equivalents are only:

| reservoir scale | active material for 10 kJ |
|---|---:|
| Al-air comparison, 1878 Wh/kg | ~1.48 g |
| ideal Cu -> CuO, 560.8 Wh/kg | ~4.95 g Cu |
| ideal Cu -> Cu2O, 323.2 Wh/kg | ~8.59 g Cu |

These small masses demonstrate only **energetic plausibility of a finite burst reservoir**. They do not demonstrate reaction rate, power density, electrical accessibility, or historical presence.

Continuous operation is much harder. For `100 W` sustained for `1.5 h` (`150 Wh`), the same scales require about:

- `79.9 g` Al-air-equivalent;
- `267 g` Cu at the ideal CuO ceiling;
- `464 g` Cu at the ideal Cu2O ceiling.

For `1 kW` sustained for `1.5 h`, those values become roughly `0.799 kg`, `2.67 kg`, and `4.64 kg` respectively.

Hence a short burst and a continuous kilowatt claim are physically very different hypotheses.

---

## 6. High-voltage storage can make a short burst look disproportionate to the recharge source

An ideal capacitor storing energy `E` obeys

`E = 1/2 C V^2`.

For `E = 10 kJ`, the ideal capacitance scale is:

| storage voltage | ideal C for 10 kJ |
|---:|---:|
| 300 V | 0.222 F |
| 10 kV | 200 uF |
| 50 kV | 8 uF |
| 100 kV | 2 uF |

These are energy-equivalence values, not proposed historical component ratings or build instructions. Real stores have voltage droop, leakage, dielectric loss, ESR, breakdown limits and safe-clearance constraints.

The important systems consequence is nevertheless robust:

`few-watt average reservoir -> slow HV charge -> short kW-class discharge`

is compatible with energy conservation if the store is large enough and the duty cycle is low enough.

This architecture must therefore be ruled out experimentally before interpreting a short load demonstration as evidence for a continuous high-power source.

---

## 7. Why a low-voltage redox source alone does not fit the visible electrostatic machine

At `100 W`, an ideal `1 V` source would have to supply `100 A`. That is a poor match to a delicate high-impedance electrostatic network.

The conventional architecture becomes more plausible only if one or both of these occur:

- many microcells are stacked in series so the reservoir voltage is much higher;
- the reservoir charges a high-voltage buffer slowly, while the buffer supplies the transient load.

That leads to the V4.30 working chain:

`distributed matter reservoir`

`-> series/parallel voltage/current scaling`

`-> slow storage recharge`

`-> C(theta) / electrostatic pickup`

`-> transient resonance`

`-> crystal / distributed rectifier phase gate`

`-> HV storage / load burst`.

The first block remains historically **UNKNOWN**. The middle routing blocks are functional hypotheses constrained by the source corpus. The last load claims remain witness reports until a closed energy balance exists.

---

## 8. Material candidate ranking for experiments

This ranking is about **discriminating function**, not reconstructing an undocumented original material recipe.

| candidate | role | source compatibility | current status |
|---|---|---|---|
| Cu/Cu2O distributed rectifying winding | crystal/top-module gate | copper is source-supported in M2; four-terminal coil clue exists in early-model witness line; Cu2O itself is not source-supported | **best gate test candidate** |
| conventional point-contact Ge/Si crystal rectifier + separate coil | crystal/top-module gate | technologically plausible literal `crystal`; material not source-supported | strong control |
| dissimilar-metal perforated/mesh microcell stack | bulk reservoir | Al + brass are reported in the separate Principle Experiment, not M2 | strongest cross-family chemical control |
| Zamboni/dry-pile stack | bulk-reservoir architecture control | no direct Testatika material evidence | architecture control only |
| single Cu/Cu2O junction as both source and rectifier | source + gate | no mechanism for sustained equilibrium energy creation | weak; do not conflate roles |
| quantum-vacuum/Casimir reservoir | bulk source | no positive closed-budget residual exists | unsupported at present |

---

## 9. Decisive low-energy tests

The highest-value discriminator is **recovery after a controlled burst**, not maximum voltage.

A safe, current-limited research module should measure whether a load pulse causes a reproducible storage droop followed by a slower recharge curve. Simultaneously log reservoir-side voltage/current, storage energy, temperature and any measurable chemical/mass change.

For a candidate four-terminal rectifying winding, characterize all six terminal pairs with low-energy instrumentation:

- DC I-V in both polarities;
- resistance and continuity;
- capacitance versus bias;
- inductance/Q;
- mutual/cross-coupling between putative conductor pairs;
- isolated pulse/ringdown response.

A distributed rectifying winding predicts a combination of **inductive continuity plus asymmetric nonlinear cross-conduction**, whereas a plain copper coil preserves the inductance but removes the rectification.

No high-voltage improvised synthesis is required to test this functional distinction.

---

## 10. Hard falsifiers

V4.30 becomes weak or fails if a well-instrumented replica/device can sustain the same real load power continuously while simultaneously showing:

- no measurable storage droop/recovery cycle;
- no adequate chemical/free-energy consumption;
- no thermal or mass signature consistent with the required chemistry;
- no electrical, RF, mechanical, pneumatic or environmental input at the required scale;
- and a positive residual well above the full uncertainty budget.

Conversely, observation of a slow recharge curve followed by brief high-power discharge would strongly favor a mundane **reservoir + buffer** explanation even if the voltage waveform and crystal gating were unusual.

## 11. Working conclusion

The strongest new synthesis is not `mystery crystal = energy source`.

It is:

**`finite distributed reservoir -> slow charge accumulation -> resonant/nonlinear crystal gating -> high-voltage buffer -> short load burst`.**

The most useful concrete gate material to test first is **Cu/Cu2O as a distributed rectifying winding**, because there is a real historical electrotechnical precedent for exactly that type of wound rectifier and for RF detection with copper-oxide rectification.

The strongest bulk-source control is a **distributed galvanic/dry-stack architecture**, especially in the separate layered/perforated machine families where dissimilar metals are actually source-reported.

Neither candidate is established as the historical Testatika reservoir. The bulk source remains **UNKNOWN** until measurement distinguishes continuous power from stored/burst power and closes every boundary term.
