# M2 V4.24 — Earth rotation / geomagnetic coupling bound

## Status

**DERIVED diagnostic / source discriminator.**

This document tests a specific idea that repeatedly arises around the Testatika: perhaps the large reservoir is ultimately the Earth's rotation and the geomagnetic field provides the coupling.

That proposal must be split into two separate statements:

1. the Earth certainly contains an enormous rotational-energy reservoir;
2. a tabletop machine can extract useful power from that reservoir only if a concrete local coupling produces EMF/current and an equal source reaction.

The second statement is the unresolved one.

Nothing here changes the historical M2 baseline. The East-West startup instruction is retained as Baumann->Marinov **SOURCE-STATED** evidence, while Marinov's reported post-start reorientation without stopping is retained separately as an **OBSERVED account**. Geomagnetic causation therefore remains **UNKNOWN**.

Canonical calculator: `sim/m2_v4_24_earth_rotation_coupling_bound.py`.

---

## 1. Relative motion is the key — not absolute speed through space

For an ordinary motional generator,

`E = v x B`

and a conductor length `L` can develop the scale

`V ~= v*B*L`

when velocity, field and conductor geometry are favorably oriented.

But `v` is the relevant relative motion in the electromagnetic system. A laboratory fixed to the Earth approximately co-rotates with the terrestrial magnetic-field system. One cannot simply insert the Earth's hundreds-of-metres-per-second inertial surface speed and declare a free generator voltage.

The familiar analogy is the user's train-window generator example: a generator works because the rotor/conductor has relative motion through a magnetic field and experiences a reaction torque. If the entire generator, field source and conductor are carried together with no relevant relative motion, common translational motion does not create free output.

Therefore the calculation below is deliberately **more favorable than reality**: it grants the machine the full Earth-surface speed through a perfectly stationary `50 uT` magnetic field.

If even that generous bound is weak, actual Earth-fixed coupling is weaker still unless an additional non-co-rotating current/field structure is identified.

---

## 2. Deliberately impossible best case: full Earth-surface speed through `50 uT`

Use

- Earth angular speed `Omega = 7.2921159e-5 rad/s`;
- Earth radius `R = 6.371e6 m`;
- field magnitude `B = 50 uT`;
- active conductor span `L = 0.2 m`.

Surface speed is

`v = Omega*R*cos(latitude)`.

### Equator

`v ~= 464.58 m/s`.

Granting perfect `v x B` alignment,

`V <= v*B*L ~= 4.646 mV`.

To transfer `100 W` at only `4.646 mV` would require

`I >= P/V ~= 21.5 kA`.

The corresponding resistive load scale is

`R_load = V^2/P ~= 216 nOhm`.

Even with ideal Thevenin matching, the source resistance would have to satisfy

`R_s <= V_oc^2/(4P) ~= 54 nOhm`.

### 47 degrees latitude comparison

For `47 deg`,

`v ~= 316.84 m/s`

and the same deliberately favorable model gives

`V <= 3.168 mV`.

Then `100 W` requires approximately

- `31.6 kA`;
- `R_load ~= 100 nOhm`;
- matched-source ceiling `R_s ~= 25 nOhm`.

These are not the electrical characteristics of a weak environmental pickup.

**DERIVED conclusion:** even if one incorrectly grants the entire Earth-surface inertial speed as useful motion through a stationary geomagnetic field, a 20-cm conductor produces only millivolts. Reaching 100 W would require an extraordinary kiloampere/nanohm current path.

---

## 3. The reaction closes the energy ledger

At the equator benchmark,

`I ~= 21.5 kA`.

The magnetic force scale on a `0.2-m` conductor is

`F = I*L*B ~= 0.215 N`.

Multiplying by the granted relative speed,

`F*v ~= 100 W`.

That is not an accidental coincidence. It is the source reaction required by electromechanical energy conservation.

If the machine truly extracted rotational energy from the Earth through an electromagnetic coupling, the corresponding reaction ultimately has to act back on the Earth/field-current system.

Because Earth's angular speed is only

`Omega ~= 7.29e-5 rad/s`,

an extraction of `100 W` directly from Earth rotation corresponds to a source torque

`tau = P/Omega ~= 1.37e6 N*m`.

The Earth's total inertia is immense, so such a torque would produce an immeasurably tiny change in global rotation. But the coupling channel that transmits that torque locally cannot disappear from the physics.

Thus `the Earth would not visibly slow down` is not an objection to conservation; it simply means the reaction must be sought in the local electromagnetic/mechanical coupling path.

---

## 4. Once-per-day changing flux is even smaller

Another possible interpretation is not translational `v x B`, but a loop whose orientation changes relative to a fixed magnetic field at the Earth's own rotation rate.

For a simple loop,

`V_peak = A*B*Omega`.

Take an intentionally generous

`A = 0.1 m^2`

and

`B = 50 uT`.

Then

`V_peak ~= 3.65e-10 V = 0.365 nV`.

The Earth-rotation frequency is only

`f ~= 1.16e-5 Hz`.

At that EMF scale, `100 W` would require roughly

`2.74e11 A = 274 GA`.

So ordinary Faraday induction from a once-per-day flux variation is not remotely a 100-W tabletop source.

---

## 5. What the East-West observation can and cannot mean

The surviving M2 evidence makes orientation worth testing:

- Baumann reportedly instructed Marinov that the small machine had to be East-West for startup;
- after startup, Marinov reports moving/tilting the running machine without stopping it.

That pattern is compatible with several very different possibilities:

- geomagnetic bias matters only during priming;
- an electrostatic/environmental field is correlated with the physical setup rather than magnetic north;
- orientation alters capacitance, wiring, support or operator coupling;
- the instruction was empirically useful but its proposed explanation was wrong;
- a machine state becomes self-maintaining after startup and no longer requires the original bias.

It is **not** sufficient evidence that the geomagnetic field supplies the bulk energy.

A static magnetic field can provide an orientation reference or bias while doing zero net work over a closed passive cycle. To make it an energy-transfer mechanism, there must be a changing flux, relative conductor motion or a time-varying current/magnetization system whose own energy cost is included.

---

## 6. Could telluric or ionospheric currents provide the missing low-impedance channel?

V4.24 does not rule out every geophysical coupling merely by ruling out naive Earth-surface `v x B` reasoning.

A more sophisticated Earth-source hypothesis would need an actual current/field system that does **not** simply co-rotate with the machine, for example a measurable telluric, ionospheric or magnetospheric disturbance.

But V4.22 still applies. The candidate channel must provide approximately the claimed real power across the local machine boundary. For a 100-W M2 hypothesis this means the channel must exhibit one or more of:

- sufficient real electric current at measurable potential difference;
- sufficient Poynting flux;
- sufficient mechanical stress/force with relative velocity;
- sufficient thermal/particle energy flux.

A field that merely sets orientation but carries negligible real local power is a **reference/bias**, not the bulk reservoir port.

This is the next place where source measurements, rather than internal-circuit speculation, matter.

---

## 7. Strong discriminator: independently rotate the apparatus relative to Earth

A safe low-energy test can distinguish an orientation reference from an energy source without any dangerous high voltage.

Mount the electrically passive/low-voltage replica on a turntable and vary orientation and angular speed independently of Earth rotation.

Measure:

- induced open-circuit voltages at the candidate pickup nodes;
- phase-resolved current under a known safe load;
- rotor/stator capacitance matrix versus angle;
- local magnetic-field vector;
- turntable torque and mechanical input;
- rear-plate state;
- RH and temperature.

Predictions:

### Ordinary Faraday / motional induction

If the effect is magnetic induction, voltage should scale with the appropriate

`dPhi/dt`

or

`v x B`

term and should reverse sign with reversed motion/orientation where geometry predicts.

### Static orientation bias

If magnetic direction only changes a threshold or priming state, a static orientation dependence may appear without a proportional continuous power term.

### Alleged Earth-rotation reservoir

If a residual effect is claimed to follow absolute Earth rotation rather than controlled relative rotation, the experiment must demonstrate why the much larger deliberately imposed turntable `dPhi/dt` does not dominate. That would be a highly discriminating result requiring independent replication.

---

## 8. Current conclusion

The strongest energy-source statement after V4.24 is:

`Earth rotational reservoir is enormous`

**does not imply**

`tabletop extractable power is large`.

A working Earth-rotation source requires the complete chain

`Earth rotation`

`-> non-co-rotating field/current/stress system`

`-> measurable local EMF/current or force/velocity port`

`-> Testatika conversion stage`

`-> load`

plus an equal source reaction.

No surviving M2 evidence currently identifies that middle low-impedance channel.

Therefore:

- **Earth rotation as ultimate reservoir:** physically possible only in the generic sense that rotational energy exists;
- **ordinary geomagnetic `v x B` from an Earth-fixed 20-cm machine:** not a viable 100-W explanation;
- **geomagnetic field as startup orientation/bias:** remains a reasonable, testable **HYPOTHESIS** consistent with the East-West clue;
- **telluric/ionospheric/magnetospheric dynamic channel:** remains **UNKNOWN** and requires quantitative local field/current measurements before being promoted.

The next source step should therefore quantify measured natural telluric and geomagnetic-disturbance power-density scales and compare them directly with the V4.22 `>=100 W` closed-boundary requirement.
