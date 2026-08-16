# Small machine V3 — functional model, provisional charge topology and build intent

## 1. Purpose of this model

This document turns the pixel analysis into a **usable experimental interpretation**. It is not claimed as the authentic original circuit. Instead, it provides the minimum structured model needed to:

- build a more photo-faithful STL/STEP version;
- keep node naming stable across experiments;
- avoid losing information between geometry and electrical test planning.

## 2. Subsystem naming

| ID | Subsystem | Type | Confidence |
|---|---|---|---|
| A | Rotor disc with 20–25 sectors | moving electrostatic transport element | high |
| B | Left spring tower + slanted pickup bar | stationary electrode family | medium |
| C | Right spring tower + slanted pickup bar | stationary electrode family | medium |
| D | Left outer collector panel | stationary collector / field shaper | medium |
| E | Right outer collector panel | stationary collector / field shaper | medium |
| F | Lower front collector panel | balancing / output-associated panel | medium-low |
| G | Left pot capacitor | reservoir / storage capacitor | medium-high |
| H | Right pot capacitor | reservoir / storage capacitor | medium-high |
| J | Top "crystal" module | asymmetry / rectification / threshold / bleed control | low-medium |
| K | Lower left spring path | adjustable lower node link | low-medium |
| L | Lower right spring path | adjustable lower node link | low-medium |
| M | Horseshoe magnets | auxiliary / unresolved | medium for presence, low for function |

## 3. Provisional node families

To organize future experiments, V3 uses three **working node families** instead of pretending the exact historical labels are known.

### 3.1 Node family N-L
Associated primarily with the left-hand stationary structures.

Likely members:
- left slanted pickup bar;
- left spring tower electrode head;
- left outer collector panel;
- one side of the top module;
- one side-pot electrode set.

### 3.2 Node family N-R
Associated primarily with the right-hand stationary structures.

Likely members:
- right slanted pickup bar;
- right spring tower electrode head;
- right outer collector panel;
- opposite side of the top module;
- opposite side-pot electrode set.

### 3.3 Node family N-C
A central or balancing family.

Likely members:
- lower front collector panel;
- central support-related plate family;
- possibly the lower spring terminations;
- possibly one intermediate output or balancing node.

## 4. Functional interpretation of each visible group

### 4.1 Rotor
The rotor is best interpreted as a moving field-conversion disc. It transports electrostatic states around the machine. Marinov's insistence on the importance of the wire path through the disc strongly suggests the rotor is not merely a front-surface segmented plate but a three-dimensional routed conductor pattern.

### 4.2 Left/right slanted pickup bars
These are the strongest candidates for the active non-rubbing coupling electrodes. They sit close to the rotor and visually aim into the active zone where a changing field would be largest.

### 4.3 Left/right upper spring towers
The towers likely support adjustable electrode heads and may simultaneously provide:
- position tuning,
- compliance,
- or a long leakage path with limited current.

The most practical reconstruction assumption is to make them electrically usable, even if later tests show part of the spring function is mainly mechanical.

### 4.4 Outer collector panels
These large framed structures likely shape a larger field envelope than the slanted inner bars. Because each contains a dark inset grid, the V3 interpretation treats them as **composite electrodes**:
- outer perforated support/shroud;
- inner active collector mesh;
- upper reddish bus/coil strip.

### 4.5 Side pots
Side pots are interpreted as intentional high-voltage, low-current storage modules. The outer mesh cylinder and inner spiral electrode strongly fit a capacitor/reservoir role.

### 4.6 Top "crystal" module
This module likely introduces asymmetry. In electrostatic terms, candidate functions include:
- directional leakage element;
- field-sensitive conduction element;
- relaxation threshold path;
- charge divider/balancer;
- node-bridging limiter.

The V3 branch therefore models it as a separate module so multiple internal surrogates can later be tested without rebuilding the full machine.

### 4.7 Lower front panel and lower springs
These elements plausibly form a third balancing/output node. They may also help stabilize the potential of the lower region relative to the moving disc and to the two side storage families.

## 5. Provisional charge-flow story

A cautious, experimentally useful narrative is:

1. the rotating sectors carry charge states around the rotor;
2. left and right slanted pickup bars interact capacitively with different angular regions of the disc;
3. charge is distributed into left/right stationary families rather than into direct rubbing collectors;
4. outer collector panels widen or reinforce the collection field and may separate active and guard surfaces;
5. side pots accumulate charge and smooth pulses into larger quasi-static potential differences;
6. the top "crystal" module introduces a further asymmetry between left and right charge families;
7. the lower front node collects, balances, or outputs a lower-current usable potential.

## 6. Why the model is intentionally modular

The true historical machine may differ in hidden ways. A rigid one-shot build would hide uncertainty. Modular reconstruction is therefore preferred.

### 6.1 Modules worth swapping in tests

- rotor routing pattern;
- black grid material / finish;
- top-module internals;
- side-pot internal connection choice;
- lower spring conductivity or isolation.

## 7. Black-grid hypotheses in functional terms

### H-B1 — active collector mesh
The black grids are conductive collection surfaces placed inside larger guard frames.

### H-B2 — dark-backed window into deeper electrode cavity
The apparent blackness is mostly optical, but the inset region still indicates the active area.

### H-B3 — deliberately blackened conductive mesh to influence leakage/corona
Possible but unproven. Must be tested, not assumed.

## 8. Minimal experiment topology for future branches

### Experimental topology T1
- left slanted bar = N-L
- right slanted bar = N-R
- left outer panel tied to N-L
- right outer panel tied to N-R
- left pot outer cylinder to N-L, inner spiral floating or via high-value leakage path
- right pot outer cylinder to N-R, inner spiral floating or via high-value leakage path
- lower front panel = N-C
- top module bridges N-L and N-R through asymmetrical internal element

### Experimental topology T2
Same as T1, but lower front panel is tied through a high-resistance or diode-like surrogate path to one side-pot family.

### Experimental topology T3
Same as T1, but the top module is bypassed to test whether it is essential to startup or only to stabilization.

## 9. What the V3 CAD should and should not represent

### Should represent
- external geometry;
- relative placement;
- visible panel families;
- top-module prominence;
- pot-capacitor geometry;
- spring and pickup-bar adjustability;
- presence of horseshoe magnets.

### Should not pretend to represent with certainty
- exact hidden internal wiring;
- exact materials of black surfaces;
- exact crystal device;
- definitive historic output circuit.
