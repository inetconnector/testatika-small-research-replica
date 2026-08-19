# M2 V4.17 — Earth-rotation / geomagnetic corotation-dynamo bound

## Status

**DERIVED diagnostic / HYPOTHESIS discriminator.** This document addresses the specific idea that the Testatika might tap the Earth's rotation through the geomagnetic field or the Earth–ionosphere–magnetosphere corotation dynamo. It does not assert that the historical M2 used this mechanism.

Canonical calculator: `sim/m2_v4_17_corotation_dynamo_bound.py`.

---

## 1. The Earth really does have a rotation-driven electromagnetic system

The premise is not nonsense: a conducting rotating Earth in its geomagnetic field develops a corotation electric field and induced charge distribution. The ionosphere/plasmasphere is part of that coupled electrodynamic system.

A particularly useful primary calculation is:

- Stefan Maus (2017), *A corotation electric field model of the Earth derived from Swarm satellite magnetic field measurements*, JGR Space Physics, DOI `10.1002/2017JA024221`.

Maus explicitly derives the primary rotation-related field and the secondary field of induced charges in the conducting Earth/ionosphere system. The important result for a ground device is that the naive motional `u x B` term is largely compensated by charge redistribution.

In the lower atmospheric insulating gap, Maus finds a vertical electric-field contribution from the corotation charges of only about

`0.3 mV/m`.

The model also finds larger potentials/fields farther out in the polar/magnetospheric system, but these are not equivalent to a low-impedance tabletop terminal at ground.

---

## 2. Why the naive `v x B` calculation is misleading

At latitude about `47 deg`, Earth's surface speed is roughly

`v ~= 317 m/s`.

With a geomagnetic field scale `B ~= 50 uT`, the maximum kinematic magnitude

`|v x B|`

is about

`0.0158 V/m`.

Across `0.20 m`, that would be only

`~3.17 mV`

even before considering the correct corotating electrodynamic boundary conditions.

But a laboratory, the conducting Earth beneath it, and most of the lower atmosphere are all in the terrestrial rotating system. Free charges in the conducting Earth redistribute until the appropriate primary rotation-related force is compensated. The Swarm-derived model gives a lower-atmosphere corotation-charge field much smaller than the raw `vB` estimate.

Thus simply writing

`E = v x B`

for the Earth's surface speed and geomagnetic field and treating that as a free laboratory voltage source double-counts a field that the conducting Earth has already electrostatically adjusted to.

---

## 3. The measured/modelled lower-atmosphere corotation scale is tiny

Take Maus's lower-atmosphere field scale:

`E_cor ~= 0.3 mV/m`.

Across a 20-cm machine:

`DeltaV ~= 60 uV`.

At the target current `1 mA`, that is only

`P ~= 60 nW`.

Conversely, obtaining `100 W` from a `60-uV` differential would require about

`1.67 MA`.

So the Earth-rotation corotation field as it appears in the lower atmosphere is not the missing `100 kV / 1 mA` port.

This is a stronger statement than saying the geomagnetic field is weak: the global corotation system exists, but its **accessible local differential potential at ground is tiny**.

---

## 4. The static geomagnetic field cannot directly do work on a charge

For a charge `q` moving with velocity `v` in a magnetic field `B`,

`F_B = q (v x B)`.

The instantaneous magnetic power is

`P_B = F_B . v = q v . (v x B) = 0`.

Therefore a static magnetic field can:

- redirect charge trajectories;
- create Hall voltages when another force/current exists;
- alter commutation and timing;
- mediate mechanical-to-electrical conversion;
- couple moving conductors and plasma flows.

It cannot by itself supply energy to the charge.

This matters for the magnetized Testatika grids: magnetic structure can be functionally essential without being the bulk energy reservoir.

---

## 5. What if the rotor cuts Earth's magnetic field?

For an ideal homopolar conducting disk, center-to-rim motional EMF is

`V = 1/2 B omega R^2`.

Use the small-machine scales:

- `R = 0.10 m`;
- `f = 1 Hz` (`~60 rpm`);
- `B = 50 uT` Earth field.

Then

`V ~= 1.57 uV`.

A 100-W output at that voltage would require about

`64 MA`.

This is plainly not the historical output route.

Even replacing the Earth field by an illustrative strong local permanent-magnet field `B = 0.5 T` gives only

`~15.7 mV`

for the same 10-cm, 60-rpm ideal disk scale.

At 100 W, that would require about

`6.4 kA`.

And in a real loaded homopolar generator the required electrical output is paid by mechanical torque.

At `1 Hz`, 100 W mechanical conversion requires

`tau = P/omega ~= 15.9 N m`.

That is exactly the large shaft-power signature already found in V4.3/V4.13-type bounds and is incompatible with treating the rotor's gentle motion as a hidden 100-W mechanical source.

---

## 6. Why Earth's rotation is different from a wind turbine

A wind turbine works because the turbine and ground are not comoving with the wind; there is relative flow through the rotor and the flow loses kinetic energy.

For an ordinary tabletop apparatus bolted to the Earth:

- the apparatus co-rotates with the Earth;
- the conducting ground co-rotates;
- the large-scale geomagnetic field is approximately part of the Earth-fixed system on laboratory timescales;
- charge redistribution in the conducting Earth establishes the corotation electrostatic boundary condition.

So there is no 317-m/s stream of terrestrial magnetic-field energy crossing the machine analogous to air crossing a turbine.

To extract rotational energy electromagnetically, a generator requires differential motion or a remote/non-corotating electrical connection. Examples in planetary electrodynamics involve plasma regions whose angular velocity differs from that of the planet, field-aligned currents, or conductors moving relative to the magnetic system.

A self-contained 20-cm ground machine has no known connection of that kind.

---

## 7. The magnetosphere does contain differential motion and large potentials

The magnetosphere is not a rigid extension of the laboratory. Solar-wind-driven convection and imperfect plasmaspheric corotation create genuine electric fields, currents and energy transfer. The global system can involve kilovolt-scale potentials and large powers.

That leaves a logically possible hypothesis:

> the machine somehow couples through the atmosphere to a non-corotating magnetospheric/plasmaspheric potential and completes the return path through Earth.

But V4.14–V4.16 impose the missing engineering requirements:

- the lower-atmosphere coupling is extraordinarily high impedance;
- ordinary small ions are not magnetically tied to field lines near ground;
- passive ELF/ULF resonant effective aperture has impossible Q/ring-up for a 20-cm receiver;
- corona can increase current under storms but a floating collector self-biases and needs a second terminal;
- measured magnetospheric modulation of surface atmospheric electricity remains pA/m²-scale.

Therefore the presence of large potentials in the magnetosphere does not automatically make them electrically accessible to the machine.

---

## 8. East–West startup remains interesting—but not as proof of rotational power

The Baumann→Marinov East–West startup instruction is worth preserving because orientation sensitivity can reveal a field-dependent threshold.

Possible conventional roles include:

- geomagnetic bias of a magnetized structure;
- phase relation between local magnetic bias and electrostatic pickup geometry;
- anisotropic leakage/charge redistribution;
- mechanical bearing/magnet alignment;
- environmental E/B coupling.

But if the machine can be moved/tilted after startup without stopping, orientation is more naturally a startup/threshold condition than a continuously aligned bulk-energy extraction geometry.

A static geomagnetic field can select a direction or phase without supplying the output power.

---

## 9. A decisive experimental split

The Earth-rotation hypothesis and the ordinary atmospheric-electricity hypothesis make different predictions.

### Corotation/geomagnetic hypothesis

If the geomagnetic/corotation system is functionally important, low-energy replica behavior should respond reproducibly to:

- controlled DC magnetic-field vector and polarity;
- device azimuth and inclination;
- reversal/demagnetization of the grid/magnet structures;
- slow imposed rotation of the entire apparatus relative to local `B`.

But a passive magnetic-bias effect should not produce real power beyond the measured mechanical/electrical inputs.

### Atmospheric-electric / leakage hypothesis

If the environment acts mainly through electrostatic charge retention, behavior should track:

- RH / surface resistance;
- external electric field;
- rear-plate capacitance;
- common-mode charge;
- insulation history.

The experiment should measure both sets simultaneously rather than treating orientation as a binary mystical condition.

---

## 10. The strongest surviving Earth-rotation version needs a remote terminal

After V4.17, the only serious version of “Earth rotation powers it” is no longer a local `v x B` generator.

It would have to be something like:

`non-corotating magnetosphere/plasma potential`

`-> remote field-aligned / ionospheric coupling`

`-> atmosphere / machine environmental terminal`

`-> nonlinear M2 conversion`

`-> Earth return`

This is a genuine two-terminal planetary-generator topology.

The problem is the middle link: the lower atmosphere and 20-cm machine must transform a remote kV-scale planetary potential into an effective source of roughly

`<=100 Mohm`

at the relevant power-transfer frequency, or approximately

`1 mA at 100 kV equivalent`.

No known passive ground-level coupling identified so far comes close.

---

## 11. Working conclusion

**Yes, Earth's rotation and geomagnetic field participate in real global electrodynamics.** The Swarm-derived corotation model explicitly calculates the associated induced charges and fields.

**No, the naive local `Earth surface speed x geomagnetic B` term is not an available tabletop power source.** In the corotating conducting Earth system it is largely compensated by induced charge, and the residual lower-atmosphere corotation-charge field is only about `0.3 mV/m` in the cited model.

For a 20-cm apparatus that corresponds to only about `60 uV`.

The rotor cutting Earth's `~50 uT` field at `~60 rpm` likewise produces only microvolt-scale homopolar EMF.

Therefore the current working hierarchy becomes:

1. **Static/local geomagnetic field:** plausible directional bias or commutation aid; not bulk source.
2. **Earth corotation field at ground:** real but far too small locally.
3. **Remote magnetospheric differential potentials:** globally energetic, but the required low-impedance ground coupling remains unidentified.
4. **Rear/base/front environmental two-port:** now the highest-value place to search experimentally for that missing coupling.

The source problem has therefore been narrowed again:

> **Do not search for more voltage in the Earth's rotation. Search for the missing remote second terminal and measure whether it can actually carry ~mA real current into the machine.**