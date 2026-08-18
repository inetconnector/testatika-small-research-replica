# Historical load-duration vs finite-storage audit — 2026-08-18

## Purpose

The unresolved energy-source question cannot be answered from voltage, lamp brightness, rotor runtime or a nameplate wattage alone. A finite-storage explanation is excluded only when the **time-integrated delivered load energy** is larger than any plausible stored-energy reservoir and all simultaneous external/mechanical inputs are also bounded.

This audit separates:

- machine running duration;
- actual load-connected duration;
- load nameplate/rating;
- measured electrical load power;
- operator power claims;
- observer inference.

It does not claim fraud, hidden batteries or anomalous energy.

---

## 1. Holzherr 1999 / M6b — the crucial duration distinction

Public preservation:

- https://rimstar.org/sdenergy/testa/report99.htm
- https://www.novakcorp.com/energy/experiments/tesnews.htm

Source chain: Hans Holzherr direct visitor report -> correspondence with Stefan Hartmann -> public English translation/preservation.

Machine: **M6b**, the approximately 50-cm-disc demonstration machine.

### What the report actually gives

Holzherr says the 50-cm machine was already running when the group entered and continued running throughout a visit of about **1.5 hours**.

The first explicitly described load was a lamp identified as **1000 W**, connected for only about **10 seconds**. He also describes a U-shaped heating element that became too hot to hold in about a second and a short visible arc when a contact lead was withdrawn.

The critical point is therefore:

> **1.5 hours is the machine-running interval, not a 1.5-hour 1000-W loaded interval.**

The report does not provide synchronized calibrated voltage and current for the 1000-W lamp during those ten seconds. `1000 W` is therefore retained as a **load rating / source-stated load description**, not automatically as a measured real output.

### Battery question

The correspondence explicitly asks whether flat batteries hidden in the base could account for the reported operation. Holzherr's technical answer is short: **“Unfortunately, I cannot judge that.”** He then gives a social/motivational reason why he personally found a battery trick implausible, while acknowledging the skeptical counterargument.

This is unusually important because later summaries often present the 1.5-hour visit as if it independently eliminated finite storage. Holzherr himself did not make that technical conclusion.

### Base inspection limit

For this 50-cm M6b machine, Holzherr says touching or lifting it was prohibited; it remained under a Plexiglas hood. He therefore could not determine the interior of the apparently solid base.

He separately says some smaller ~12-cm machines could be lifted/examined while their discs continued turning. Those are **M4-family observations** and cannot be transferred to M6b or M2.

---

## 2. Energy implied by the observed lamp interval

If, only as an upper comparison assumption, the lamp really received its full nameplate `1000 W` for `10 s`, then

`E = P*t = 1000 W * 10 s = 10,000 J`.

That is

`10,000 / 3600 ~= 2.78 Wh`.

This is a modest **energy quantity** even though `1 kW` is a large instantaneous power.

The distinction matters:

- `1 kW for 10 s` -> `2.78 Wh`;
- `1 kW for 1.5 h` -> `1500 Wh = 1.5 kWh`.

Those differ by a factor of **540**.

Nothing in the Holzherr report establishes the second quantity.

Therefore the 1999 demonstration, by itself, does not rule out finite internal chemical/electrical storage on an **energy-capacity** basis. Whether a concealed source could supply the required **peak power**, fit the observed geometry, avoid detection and reproduce all other observations is a separate engineering question.

---

## 3. Electrostatic-storage comparison

For a capacitor:

`E = 1/2 C V^2`, so `C = 2E/V^2`.

To store the 10-kJ rating-equivalent lamp energy electrostatically would require ideally:

- at `100 kV`: `C = 2 microfarads`;
- at `30 kV`: `C ~= 22.2 microfarads`.

Those are vastly above the pF/nF working scales used in the M2 V4 environmental-coupling diagnostics. This does not prove the M6b cylinders lacked such storage — their exact capacitance is not recovered — but it shows why **pure finite electrostatic storage in the visible Testatika-style capacitors needs direct capacitance/voltage measurement rather than assumption**.

For comparison, 100 W sustained for one hour is 100 Wh = 360 kJ and would require an ideal `72 microfarads at 100 kV` if stored electrostatically at fixed initial voltage with full usable discharge energy.

---

## 4. Schneider/Weber 13-Mar-1984 / M5 — operator claim versus witnessed duration

Public later reproduction:

- https://www.yumpu.com/de/document/view/4114787/paul-baumann-erbauer-der-energiemaschine-testatika-93jahrig-

The later NET-Journal reproduction attributes to Inge Schneider's account a nominal output statement of about **300 V DC / 10 A**, while the assertion that this could continue for hours or years is explicitly presented as something **Baumann told the visitors**.

The visitors describe a bright lamp and a heating element becoming very hot after a few seconds. The reproduced account does not establish a calibrated multi-hour `300 V x 10 A` load test.

It also says the physicist was allowed to lift the machine and inspect underneath and saw neither an obvious battery nor an externally connected source. That is a meaningful inspection constraint for **M5**, but not a destructive internal inspection, chemical-energy assay, RF-field survey or closed input/output/storage balance.

Evidence separation:

- `300 V / 10 A available` -> **SOURCE-STATED / witness-account claim**, not independently reconstructed metrology here;
- `continuous for hours/years` -> **Baumann operator claim**;
- bright lamp / hot heater -> **witnessed load effect**, duration short/qualitative in the later reproduction;
- no visible battery/external source under lifted machine -> **inspection observation**, not complete energy accounting.

---

## 5. Consequence for the energy-source search

The historical evidence recovered so far does **not** provide a clean interval of known real load power and known duration that forces the energy integral beyond plausible finite storage.

This is a stronger methodological statement than simply saying “batteries are possible.” It means that the correct next discriminator is:

`E_load = integral(V_load(t) * I_load(t) dt)`

compared against

`E_external + E_mechanical + E_storage_initial - E_storage_final`.

The machine's unloaded or lightly loaded running time is secondary unless its own mechanical/electrical loss power is measured.

---

## 6. Highest-value modern test

For any replica or original-like machine, define in advance a **minimum loaded-energy challenge**, not merely a runtime challenge.

Examples:

- `100 W for 10 s` = `0.278 Wh`;
- `100 W for 1 min` = `1.67 Wh`;
- `100 W for 1 h` = `100 Wh`;
- `1 kW for 10 s` = `2.78 Wh`;
- `1 kW for 1.5 h` = `1.5 kWh`.

A convincing source claim requires continuous isolated `V(t)` and `I(t)` logging, known load impedance, thermal cross-check where practical, full device mass/temperature/state before and after, and simultaneous monitoring of all electrical/mechanical/environmental input ports.

The experiment should continue long enough that the delivered energy materially exceeds the independently bounded initial storage reservoir. Otherwise finite storage remains an open conventional explanation regardless of how impressive the instantaneous lamp brightness appears.

---

## 7. Working conclusion

V4.13 changes the ranking of conventional source candidates:

1. **finite internal storage remains open** for short historical load demonstrations because the strongest recovered load-duration interval is short;
2. **local structured coupling remains open** from V4.12 and must be instrumented rather than inferred from absence of wires;
3. ordinary ambient atmospheric/RF/Schumann/geomagnetic bulk power remains excluded by V4.11;
4. an anomalous source term is justified only after load **energy**, not merely power or voltage, exceeds all bounded inputs and storage changes.

The key new discipline is therefore:

> **Do not confuse “ran for 1.5 hours” with “delivered 1 kW for 1.5 hours.”**

That distinction materially changes how strong the surviving historical energy evidence is.
