# M2 V4.16 — passive atmospheric corona-current and floating-return bound

## Status

**DERIVED diagnostic / HYPOTHESIS discriminator.** This document does not assert that the historical M2 used corona as its bulk source. It asks whether point discharge, sharp/magnetized grids, wind and dry air could supply the missing environmental current found in V4.14–V4.15.

The target remains:

`100 W ~= 100 kV * 1 mA`.

V4.14 showed that the ordinary fair-weather Earth–ionosphere port is voltage-rich but current-poor. V4.15 showed that an electrically tiny passive ELF/ULF resonator cannot rescue the missing coupling merely through enormous formal effective aperture.

V4.16 tests the next conventional loophole:

> **Could the machine create/collect atmospheric ions through point discharge or corona and thereby raise the environmental current from pA to mA?**

Canonical calculator: `sim/m2_v4_16_corona_return_port.py`.

---

## 1. Corona can increase atmospheric current — but under strong fields

Point discharge from grounded sharp objects is a real atmospheric-electricity mechanism. Under thunderstorms, the ambient field is concentrated at trees, towers and other points; corona then injects ions and creates a space-charge layer that partly shields the ground field.

Primary source anchors:

- Chapman (1970), *Corona point current in wind*, JGR, DOI `10.1029/JC075i012p02165`;
- Chapman (1977), *The Magnitude of Corona Point Discharge Current*, J. Atmos. Sci., DOI `10.1175/1520-0469(1977)034<1801:TMOCPD>2.0.CO;2`;
- Standler & Winn (1979), *Effects of coronae on electric fields beneath thunderstorms*, QJRMS, DOI `10.1002/qj.49710544319`;
- Guerra-Garcia et al. (2020), *Corona Discharge in Wind for Electrically Isolated Electrodes*, JGR Atmospheres, DOI `10.1029/2020JD032908`;
- McFarland et al. (2026), *Corona Discharges Glow on Trees Under Thunderstorms*, GRL, DOI `10.1029/2025GL119591`.

The important magnitude separation is:

- fair-weather vertical current density: order `2 pA/m²`;
- under a thunderstorm, Standler & Winn found typical corona current density around `1 nA/m²` in a ground field around `8 kV/m`;
- recent direct tree-corona observations infer branch currents of order `1 uA`, with larger short pulses coincident with lightning.

So corona can raise local atmospheric current by hundreds to thousands of times relative to fair weather. That is physically real.

It is still far from a quiet-room 1-mA source.

---

## 2. Chapman current law gives the right microamp scale

Chapman's approximate ambient-field point-discharge relation can be written

`i ~= 3.9 eps0 k E0 (Vp - V0p)`

with

`Vp = E0 h`,

for a point of effective height `h` in external field `E0`, ion mobility `k`, and starting potential `V0p`, provided the point is above corona onset.

This is not a universal geometric onset law, but it is useful as a scale check.

Use:

- `k = 1.5e-4 m²/(V s)`;
- `E0 = 8 kV/m`;
- `h = 4 m`;
- `V0p = 5 kV`.

Then

`Vp = 32 kV`

and

`i ~= 1.12 uA`.

That agrees in order of magnitude with thunderstorm point/tree measurements.

This is important because it says the model is not missing a hidden factor of a billion. The known corona mechanism naturally lives in the microamp-per-point regime under strong storm fields.

---

## 3. A 20-cm fair-weather machine does not reach ordinary point-corona onset

For a 20-cm vertical scale in a fair-weather field `E0 ~= 100 V/m`,

`Vp = E0 h ~= 20 V`.

Chapman's measured positive/negative starting potentials were several kilovolts under his experimental conditions; the 1970 measurements quote approximately `+6.9 kV` and `-4.9 kV` at standard-density scale.

So the macroscopic fair-weather potential available across a 20-cm object is not close to ordinary atmospheric point-corona onset.

As an intentionally unrealistic upper bound, set the onset potential to **zero**. Then the same Chapman scaling gives only about

`10 pA`

for one 20-cm point in `100 V/m`.

Even if almost `10 pA` per point were available and every point acted independently, reaching `1 mA` would require roughly

`9.7e7` independent points.

Real closely spaced points do not remain independent: their fields and space-charge clouds shield each other. Chapman explicitly notes that many points can fail to multiply current proportionally, especially in strong fields or weak wind.

Thus nanoscale sharpness or “many grid points” is not a plausible missing nine-order current multiplier by itself.

---

## 4. The area bound remains severe even during storms

Standler & Winn report a typical corona current density around

`J_corona ~= 1 nA/m²`

under a thunderstorm field of roughly `8 kV/m`.

To collect `1 mA` at that current density:

`A = I/J ~= 1e6 m² = 1 km²`.

That is already a **thunderstorm** condition, not fair weather.

At ordinary `2 pA/m²`, the corresponding current-collection area remains

`5e8 m² = 500 km²`.

Recent 2026 tree observations make the same point in a more intuitive way: branch corona currents are of order `1 uA` under a thunderstorm. A milliamp would be of order **one thousand such branch-current equivalents**, and that is before asking where the 100-kV loaded voltage comes from.

Corona therefore helps the current side of the environmental-source problem under electrified weather, but not enough for a quiet 20-cm tabletop machine.

---

## 5. The strongest result: an electrically floating corona source self-quenches

This is especially relevant to the M2 evidence because the small machine is electrically unusual and many of its conductors are floating.

Guerra-Garcia et al. experimentally and theoretically studied corona in wind from electrically isolated electrode systems. For isolated structures, charge carried away by corona changes the potential of the whole structure. That self-charging opposes the field that created the corona; depending on geometry and wind, the current can decrease strongly or vanish while the floating potential saturates.

That is exactly what charge conservation predicts.

For a floating conductor,

`I = C_body dV/dt`.

Approximate a 20-cm-diameter body by an isolated sphere of radius `R = 0.1 m`:

`C_body = 4 pi eps0 R ~= 11.1 pF`.

Now suppose a unipolar corona current leaves the floating machine.

At only `1 uA`:

`dV/dt ~= 90 kV/s`.

A `5 kV` self-bias change occurs in only

`~56 ms`.

At the desired `1 mA`:

`dV/dt ~= 90 MV/s`,

and the same `5 kV` self-bias develops in about

`56 us`.

Even if the effective whole-machine capacitance were ten times larger, the times are only ten times longer.

Therefore a **continuously floating unipolar corona collector cannot be the missing 1-mA port**. It charges itself to a potential that suppresses further current unless there is a second current path.

---

## 6. The missing coupling is necessarily a two-port / return-path problem

A sustained source needs charge to complete a circuit.

If an environmental collector carries `1 mA`, and its potential may shift by no more than `5 kV` before the coupling is badly altered, the effective balancing return resistance must satisfy

`R_return <= DeltaV / I`

or

`R_return <= 5 Mohm`.

Even allowing a full `100 kV` drop gives

`R_return <= 100 Mohm`.

This independently reproduces the V4.14 source-impedance target.

So there is a useful contradiction in the phrase

> “extremely high impedance, fully floating, yet continuously supplies 1 mA.”

A machine can be extremely high impedance internally and still transfer power, but **the complete environmental source loop cannot be arbitrarily high impedance at the power-transfer frequency** if it is to deliver 1 mA.

This does not require a visible DC wire. A return can be:

- capacitive/displacement-current coupling;
- alternating bipolar charge exchange;
- a conductive base/earth path;
- inductive coupling to an external field;
- a large external structure;
- or an active local transmitter.

But some second port must exist in the real-power ledger.

---

## 7. Could alternating corona avoid the floating self-charge problem?

Partly—but it does not remove the source requirement.

Imagine the rotor/crystal/grid system alternately emits positive and negative charge so that the machine's net charge returns to zero each cycle.

Then the body does not accumulate unlimited DC potential. This is a plausible reason a rotating influence machine can operate while remaining globally floating.

However, the alternating current must transfer charge between **two environmental potentials**.

For `1 mA` average at `24 events/s`, the transported charge scale is

`Q_event ~= I/f ~= 41.7 uC per event`.

At a `250 kV` differential scale this is equivalent to

`C_eq = Q/V ~= 167 pF`.

That is close to the V4.14 `~133 pF` energy-per-event estimate because the two estimates use slightly different current/energy conventions.

Again, the capacitance is not absurd. The hard part is replenishing tens of microcoulombs per event from the environment.

Ordinary fair-weather current supplies to `0.1 m²` only

`~0.2 pA`,

or over one 1/24-s event interval only about

`8e-15 C`.

The desired `~4e-5 C` packet is roughly **five billion times larger**.

This is the missing coupling in charge-domain form.

---

## 8. Wind is helpful for grounded corona, but floating wind coupling has a built-in ceiling

Corona literature repeatedly finds that wind can increase point-discharge current because wind removes the local ion cloud that otherwise shields the emitter.

Chapman measured currents up to `290 uA` in a wind tunnel with point potentials up to `±60 kV` and strong imposed conditions.

This is sometimes tempting as a route toward the milliamp target.

But two qualifications matter:

1. those large currents involve an externally established high point potential / grounded collection geometry;
2. in the later isolated-electrode experiments, wind also transports charge away from the floating system, causing the system to charge itself and weaken its own corona; in some regimes the current vanishes and the potential saturates.

So “wind removes the ions” is not a free current multiplier for a floating generator. The exported charge has to be replaced through another port.

---

## 9. What about dry, cold air?

The M2 dry-air startup evidence remains important, but V4.16 changes how it should be interpreted.

If atmospheric point discharge were the **bulk power source**, the strongest conventional predictors should be:

- external electric field magnitude;
- point geometry/effective height;
- wind / ion removal;
- existence and impedance of the return path;
- proximity to storm/electrified-cloud conditions.

The historical emphasis on dry air is more naturally consistent with:

- reduced surface leakage on PMMA/insulators;
- longer electrostatic charge retention;
- higher attainable internal electrostatic voltage;
- less damping of a threshold/commutation process.

That does not rule out corona inside the mechanism. It suggests corona is more likely to be a **nonlinear switch, leakage path, or charge-transfer gate** than the reservoir delivering the full 100 W.

A clean experiment should therefore vary humidity while independently holding external E-field, airflow and imposed source impedance constant.

---

## 10. Magnetized grids do not solve the return-path problem

Magnetic structure can influence:

- local electron trajectories in a discharge;
- plasma attachment/ionization regions;
- force/phase relationships;
- material permeability and local field geometry;
- rotor timing and commutation.

But ordinary atmospheric small ions near ground are collision-dominated (`mu*B << 1` even for tesla-scale fields, V4.14).

More fundamentally, magnetic shaping cannot make net charge disappear.

If `1 mA` leaves one part of a floating machine continuously, `1 mA` must enter somewhere else in steady state.

The magnetized grids may help define *where and when* the current flows. They cannot eliminate the second terminal required by charge conservation.

---

## 11. Stronger storm corona actually gives a falsification signature

If corona collection were the bulk source, the machine should become dramatically easier to energize when exposed to a much stronger externally applied atmospheric-like electric field or controlled ion flux.

The predicted order is not subtle:

- fair weather: `~100 V/m`, no ordinary 20-cm point-discharge onset in the Chapman scale;
- thunderstorm ground fields: several `kV/m`, microamp-class point/tree corona appears;
- intense imposed HV/wind-tunnel conditions: tens to hundreds of microamps are possible.

A replica whose behavior depends strongly on RH but hardly at all on calibrated external E-field and controlled ion current would argue **against corona as the bulk environmental source** and toward insulation/charge-state effects instead.

This is a valuable discriminator because it separates two environmental explanations that otherwise look similar observationally.

---

## 12. The next low-energy experiment should measure a two-port charge transfer coefficient

Do not start by trying to create historical-scale corona or 100 kV.

Use a safe low-voltage scaled structure and explicitly instrument two external environmental ports:

`ENV_A <-> machine <-> ENV_B`.

Measure:

- real current into both external electrodes;
- machine common-mode charge;
- internal floating-node potentials;
- rotor angle/speed;
- storage capacitor energy;
- E-field and B-field;
- RH and airflow.

Then impose small calibrated alternating external fields and determine

`Q_transfer / cycle`

and

`P_real, absorbed / P_external, real`.

Critical controls:

- fully floating machine;
- one external plate grounded;
- both plates floating;
- high-R return deliberately inserted and swept;
- magnetic grids magnetized/demagnetized/dummy;
- rear plate absent/floating/grounded;
- rotor stopped/rotating;
- nonlinear crystal surrogate open/linear/nonlinear.

The return-resistance sweep is especially diagnostic. If the effect dies when `R_return` rises above the value predicted by `DeltaV/I`, then the machine is behaving like an ordinary two-port electrostatic converter.

---

## 13. A specific falsification target for the corona hypothesis

For the `100 kV / 1 mA` explanation to survive, a replica/environment model must identify a path that does **all** of the following:

1. transports about `1 mA` average charge without indefinite common-mode charging;
2. exposes a differential environmental potential large enough that the current represents substantial real power;
3. has effective source/return impedance on the `<= 1e8 ohm` scale at the relevant power-transfer frequency;
4. does not rely on an unmeasured external HV supply, ground current, mechanical input or stored energy;
5. remains compatible with the M2's observed floating/non-contact architecture.

Ordinary fair-weather point discharge fails (1) and (3) by many orders of magnitude.

Thunderstorm corona can reach microamp scales and much larger current densities than fair weather, but it requires strong external fields and still does not explain routine indoor operation.

A purely floating unipolar corona source self-quenches unless a second port is present.

---

## 14. Working conclusion

Corona is worth retaining in the model—but its role changes.

**Supported physics:**

- sharp grounded structures under storms can produce microamp-class corona currents;
- wind can increase corona current by removing shielding ions;
- atmospheric corona contributes materially to the global electric circuit under storms;
- electrically isolated structures self-charge, which can suppress or terminate corona current.

**Derived implication for M2:**

A floating 20-cm Testatika-like machine cannot get a sustained `~1 mA` merely by adding sharper points or magnetized grids to the ordinary fair-weather field. At milliamp current, a roughly 11-pF floating body would self-bias by kilovolts in tens of microseconds unless an equally large balancing current enters elsewhere.

So the missing coupling is now even more precisely defined:

> **Find the second environmental terminal / return path that can carry sub-mA to mA charge while maintaining a large differential potential.**

The most promising remaining conventional searches are therefore no longer “more corona points,” but:

- hidden capacitive return through backboard/base/building/ground;
- bipolar displacement-current pumping between front and rear environmental nodes;
- a strong higher-frequency external near field;
- or another active external source whose current can be measured.

If none provides approximately the `<=100 Mohm / ~1 mA / ~100 kV-equivalent` port, Earth–ionosphere atmospheric collection also falls as the bulk explanation for 100 W.