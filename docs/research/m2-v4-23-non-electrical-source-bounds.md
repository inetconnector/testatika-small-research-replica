# M2 V4.23 — non-electrical conventional source bounds

## Status

**DERIVED diagnostic / closed-boundary completion step.**

V4.14–V4.22 progressively constrained electrical/environmental source hypotheses. V4.23 closes the largest remaining **ordinary non-electrical boundary terms** with intentionally favorable upper bounds.

It does not claim that wind, sound, heat, light, vibration or stored chemical energy powered the historical M2. It asks how large each channel would have to be to sustain a nominal `100 W` output.

Canonical calculator: `sim/m2_v4_23_non_electrical_source_bounds.py`.

Historical caution remains unchanged:

- the M2 output figure is not independently verified;
- the archived `300 Watts` title for `meth4.asf` is metadata, not a closed energy balance;
- Marinov's direct small-machine line remains a single-disc electrostatic machine with no conventional built-in drive motor and no Tesla/AC interpretation of the side spirals;
- the rear-plate, humidity and East-West effects are genuine research clues but do not identify the bulk source.

---

## 1. Airflow / hidden wind

The maximum kinetic power intercepted by a flow is

`P_flow = 1/2 * rho * A * v^3`.

Use a generous projected area

`A = 0.1 m^2`

and air density

`rho = 1.2 kg/m^3`.

To obtain `100 W`:

- at impossible `100%` conversion: `v >= 11.86 m/s`;
- at `30%` conversion: `v >= 17.71 m/s`.

For `300 W`:

- `100%`: `v >= 17.10 m/s`;
- `30%`: `v >= 25.54 m/s`.

These are strong, obvious airflows rather than unnoticed room convection.

**DERIVED consequence:** ordinary still-room air motion cannot plausibly supply a 100-W class output through a 20-cm-scale apparatus. A hidden duct/jet would be a conventional mechanical source and should be straightforward to detect with flow and pressure measurements.

---

## 2. Acoustic power

For a plane acoustic wave,

`I = p_rms^2/(rho*c)`.

A 100-W capture through `0.1 m^2` requires at least

`I = 1000 W/m^2`

at `100%` capture.

With `rho = 1.2 kg/m^3` and `c = 343 m/s`, this corresponds to approximately

`p_rms ~= 642 Pa`

or

`SPL ~= 150.1 dB re 20 uPa`.

At only `10%` conversion the required sound level rises to roughly

`160.1 dB`.

This is not a subtle ambient-acoustic reservoir.

**DERIVED consequence:** ordinary room sound cannot be the missing 100-W source. Any acoustic source strong enough to matter would be extreme and independently measurable.

---

## 3. Structural vibration

For an optimistic in-phase sinusoidal mechanical transfer,

`P = F_rms * v_rms`

with

`v_rms = 2*pi*f*x_rms`.

At `50 Hz`:

- `x_rms = 1 mm` requires `F_rms >= ~318 N` for 100 W;
- `x_rms = 0.1 mm` requires `F_rms >= ~3183 N`.

This deliberately grants perfect phase alignment and perfect conversion.

The historical M2 does not have an identified floor shaker, hidden mechanical transducer or equivalent source. The calculation therefore serves as a falsification scale: a building vibration source capable of 100 W would require a substantial force/velocity product, not merely imperceptible microvibration.

---

## 4. Rotor inertia is negligible as a sustained source

Take an intentionally generous rotor:

- solid disk;
- mass `1 kg`;
- radius `0.1 m`;
- speed `60 rpm`.

For a solid disk,

`I = 1/2*m*r^2`

and

`K = 1/2*I*omega^2`.

The stored rotational energy is only

`K ~= 0.0987 J`.

At `100 W` this would last only

`~0.000987 s`.

The real M2 rotor was likely far lighter than this deliberately generous 1-kg bound.

**DERIVED consequence:** rotor kinetic energy can smooth torque ripple and bridge individual commutation events, but it cannot be the bulk source of a sustained 100-W output.

---

## 5. Thermal-gradient source

A heat engine cannot exceed the Carnot efficiency

`eta_C = 1 - T_cold/T_hot`.

Take room-temperature cold side

`T_cold = 293 K`.

For `100 W` electrical/mechanical output, even an ideal reversible engine would need at least:

| temperature difference | Carnot ceiling | minimum heat flow |
|---:|---:|---:|
| 10 K (`303/293 K`) | ~3.30% | ~3030 W |
| 50 K (`343/293 K`) | ~14.58% | ~686 W |
| 100 K (`393/293 K`) | ~25.45% | ~393 W |

Real devices would require more heat flow.

Thus a modest room-temperature gradient cannot quietly supply 100 W. A thermal explanation would require a clearly identifiable hot/cold reservoir and substantial heat transfer.

This does not exclude short thermal transients; it excludes an unspecified small ambient temperature difference as a high-power source.

---

## 6. Illumination / radiant power

Radiant input is bounded directly by

`P_intercept = irradiance * area * conversion_efficiency`.

For `A = 0.1 m^2`:

- `10 W/m^2` incident -> at most `1 W` before conversion loss;
- `100 W/m^2` -> at most `10 W`;
- `1000 W/m^2` -> at most `100 W` at perfect conversion.

At a realistic-but-still-generous comparison efficiency of `20%`, obtaining `100 W` from `0.1 m^2` would require

`5000 W/m^2`

incident irradiance.

Therefore light can only be a 100-W-scale source if the apparatus is exposed to a strong directed radiant flux and has an efficient absorber/converter. That condition would be directly measurable.

For the historically shown indoor demonstrations, the surviving evidence does not identify a dedicated optical collector. V4.23 therefore retains radiant input as a measurable control, not a supported M2 source claim.

---

## 7. Finite chemical/electrical storage remains a serious conventional alternative for short demonstrations

Any hidden finite reservoir must provide at least

`E = P*t`.

For `100 W`:

| duration | minimum stored energy |
|---:|---:|
| 1 s | 100 J |
| 1 min | 6 kJ |
| 10 min | 60 kJ = 16.67 Wh |
| 1 h | 360 kJ = 100 Wh |

This is fundamentally different from pF-scale electrostatic storage. Tens to hundreds of watt-hours are quite ordinary energy quantities for chemical batteries, while their historical concealability depends on the specific machine volume, mass, date and inspection quality.

Therefore **stored chemical/electrical energy cannot be dismissed from short demonstration reports merely because the visible rotor had little kinetic energy**.

The correct discriminator is duration plus mass/thermal accounting:

- operate long enough that a plausible hidden reservoir would materially discharge;
- measure machine mass before/after where relevant;
- monitor temperature;
- inspect all accessible volumes and wiring paths;
- repeat after controlled rest/storage intervals.

No claim is made that a hidden battery existed. This remains a conventional alternative until a long-duration closed energy balance excludes it.

---

## 8. Human handling / manual startup is only a seed unless repeated mechanical work enters

The historical small machine was reportedly started by several finger pushes in dry air, with humidity affecting startup difficulty.

That startup impulse can supply a finite initial mechanical energy and can also change electrostatic charge state. But once the operator stops touching the machine, sustained 100-W output for

- `1 minute` requires `6 kJ`;
- `10 minutes` requires `60 kJ`;
- `1 hour` requires `360 kJ`.

A few startup pushes cannot supply those totals unless a separate reservoir is subsequently tapped.

Thus the startup procedure is best modeled as a **priming/initial-condition operation**, not automatically as the long-duration bulk energy source.

---

## 9. What remains after V4.23

The ordinary ambient-source search is now substantially narrower.

### Strongly constrained for 100-W class

- fair-weather atmospheric DC: source impedance/current far too weak;
- ordinary 230-V/50-Hz stray capacitive pickup: far too weak;
- ordinary ambient RF: far below the strong-field real-power requirement;
- rotor inertia: sub-millisecond-scale reservoir even under a generous 1-kg rotor assumption;
- still-room airflow: would require strong wind;
- ordinary acoustic background: would require extreme sound pressure;
- small structural vibration: would require a large force/velocity product;
- modest thermal gradients: would require hundreds to thousands of watts of heat flow;
- ordinary weak illumination: bounded directly by intercepted radiant power.

### Still open conventional alternatives

- a **strong powered local HF/near-field source**;
- a hidden galvanic/low-impedance electrical input;
- a substantial concealed chemical/electrical reservoir for finite-duration demonstrations;
- a substantial mechanical source not represented in the visible rotor motion;
- a strong directed thermal/radiant/airflow source not documented in the surviving evidence;
- historical output overestimate or incomplete input accounting.

### Still unknown

An unrecognized environmental or physical channel remains logically possible, but it must satisfy the V4.22 boundary criterion:

> approximately the claimed real output must cross the local measurement boundary as net energy flux, or a controlled experiment must demonstrate a statistically significant residual after every known boundary term and storage term is measured.

---

## 10. Best next physical protocol: complete watt-budget enclosure

A modern low-energy replica should be instrumented as a **closed watt-budget object**, not merely as a high-voltage generator.

Simultaneously record:

- electrical real power through every intentional feedthrough;
- mechanical shaft/fixture work;
- airflow speed/pressure around the enclosure;
- acoustic pressure;
- base vibration/acceleration and force where practical;
- surface and ambient temperatures;
- incident optical/radiant flux;
- machine mass and long-duration thermal drift;
- electrostatic/magnetic stored-energy changes;
- load real power.

The experiment should first be validated with known injected power so the uncertainty budget is demonstrated before any anomalous interpretation is attempted.

For Testatika research, this is more decisive than trying additional speculative internal wiring variants without first proving where the watts cross the boundary.
