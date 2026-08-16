# Hauser / Marinov primary-scan audit — 2026-08-16

## Purpose

This document audits the `hauser/` scan set in the user-supplied historical archive and separates direct observation, direct correspondence, observer interpretation and later inference. The scans are not redistributed; file hashes and research consequences are recorded so that every claim can be traced back to the archive.

A central result is that several facts previously known only through later summaries are directly present in Stefan Marinov and Albert Hauser correspondence scans.

## Preservation / dating rule

The printed date strings are retained as they appear on the scans. Ambiguous numeric date formats are **not silently normalized**.

## File ledger

| Archive file | SHA-256 | Source role |
|---|---|---|
| `hauser/SMweb2.jpg` | `add0514f477f1e9046d96c65c622f9ac65d7abf854727c99df9575fef5a50064` | Stefan Marinov correspondence scan; printed `9-4-89`; P1 for Marinov's own statements |
| `hauser/SMwebL1.jpg` | `a69d3272d38f670c438895d71104a916c907571a29acc819d3eda3650aac9d93` | Stefan Marinov correspondence scan; printed `9/4/90` and `12/2/90`; P1 for Marinov's own statements |
| `hauser/ABweb1.jpg` | `fdf6b4cc07be6257bb8b6a79e7ddb3d1eddf9636f19b58390e06d582266fd8ed` | Albert Hauser direct-visit report, first page; P1 observation + I1 interpretation |
| `hauser/ABweb2.jpg` | `03027479e5652bc462ddd0514b1780746e682327f3a813b2eb2bc493c376a1a5` | Albert Hauser direct-visit report, continuation; P1/I1 |
| `hauser/ABweb3.jpg` | `f0a478802f9ef5bb5dc1f070e8eba994a40aa7e884d52358c73573b04bc080a0` | Hauser drawing no. 3279 / medium-machine geometry; P1 visual reconstruction, not an original factory drawing |
| `hauser/ABweb4.jpg` | `b3e4ad615c28ea6d6cb78aa752892651f1ba7ad194403da43b5f09bee10071a8` | Hauser connection/functional drawing; P1/I1 reconstruction, not an authentic circuit schematic |
| `hauser/ABweb9.jpg` | `a4b4e7a510300d1752f6544def283fb2697be0738127e47a721265ccc8271f34` | Hauser follow-up notes on drawing 3279; P1/I1 |
| `hauser/AHwebL5.jpg` | `030c4ff3784982027db7c452cad2af5531f94f3cdbc81cde0e45c840b5fcd488` | Hauser later correspondence / replication reasoning; H1/I1 with some relayed statements |
| `hauser/AHwebL6.jpg` | `1c31820fa91a1f69d09010497144f0b14e6deba1a999377032d605a90d8ed89f` | Hauser later correspondence; H1/I1 with model-separation clues |
| `hauser/AHwebL7.jpg` | `831ab0a45556e3ce6aa495e31e61d4ee9c0dae50fd42e5aed6a4fb3741f800bd` | Hauser letter dated Sept. 27, 1988; direct description of medium-machine cylinder internals; P1/I1 |
| `hauser/AHwebl8.jpg` | `27369d3df79f75f75c657641a841afe10e5427ac125aebeb82944c99d59cce70` | continuation of 1988 Hauser answers; P1/I1 |

All scans are 600 × 851 pixels in this archive copy.

---

# 1. Stefan Marinov correspondence: high-value M2/M3 constraints

## 1.1 The underlying “different language” statement is now primary-source supported

`SMweb2.jpg` contains Marinov's own statement that Baumann tried to explain the operating principle but Marinov could not understand it because Baumann had **“ANOTHER language”**.

This changes the previous repository conclusion in an important but narrow way:

- the later phrase **“like an unknown language”** is still not verified as Marinov's exact wording;
- however, the underlying proposition that Marinov explicitly described Baumann as using another/different language **is directly supported by a primary correspondence scan**.

Therefore the correct future wording is:

> Marinov directly wrote that Baumann had “ANOTHER language”; the popular wording “like an unknown language” remains an unverified paraphrase.

This wording must replace the stronger prior statement that no primary Marinov language reference had been found.

## 1.2 No Tesla coils / no AC in the small-machine interpretation

In the same correspondence Marinov explicitly rejects a Tesla-coil / alternating-current interpretation of the small machine. He says the visible spiral structures in the capacitors are electrodes of capacitors rather than Tesla transformer windings.

**Consequence:**

- M2 baseline remains electrostatic/DC-oriented;
- HF/Tesla networks remain comparison hypotheses only;
- a side-pot spiral must not be promoted to a Tesla secondary without new primary evidence.

## 1.3 Small-machine pot construction is stated directly

`SMwebL1.jpg` gives a concise small-pot description:

- cylindrical conductive `grid`;
- cylindrical plastic insulation;
- copper spiral in the centre.

The same scan says that **two wires** can clearly be seen going to the right condenser and two to the left condenser in the referenced photograph.

**Consequence:**

- the physical research pot should expose the historically visible two-terminal interface as the default external form;
- additional guard/test terminals may exist on the experimental fixture, but they must be hidden/separable from the historical two-lead configuration;
- exact internal polarity/topology is still unknown.

## 1.4 Rotor wires reported as electrically floating

`SMwebL1.jpg` states that the wires on the small-machine disk are **“connected to nothing”**.

This is a major constraint. Combined with the independently strong no-rubbing-contact evidence, the conservative small-machine baseline becomes:

- individual routed rotor conductors are electrically floating;
- no continuous collector ring is assumed;
- no neighbour-to-neighbour resistor ring is assumed;
- the late Frolov `1 kΩ between lamellae` claim is therefore not a valid M2 baseline and now conflicts with a stronger direct small-machine statement.

Caution: the correspondence refers to a photographed small machine; exact M2-versus-M3 assignment of every sentence still requires image-chain locking. Therefore this is a strong **small-machine-family** constraint and a preferred M2 baseline, not proof that every Testatika rotor used isolated conductors.

## 1.5 No mechanical drive motor in the described small machine

The correspondence states that there is no motor in the small machine and attributes rotation to electrostatic repulsion.

This is evidence about architecture, not proof of an energy anomaly. A hidden/stored electrical bias, initial charge, or other energy reservoir remains an experimental question.

**Consequence:** M2 mechanical baseline contains no conventional drive motor. Any laboratory motor used for controlled rpm sweeps is explicitly test equipment and must be mechanically decoupled for self-rotation trials.

## 1.6 Magnet presence is model-specific

`SMweb2.jpg` distinguishes one small machine with no magnets from another machine in which magnets are present. This supports the repository's existing rule that magnet presence must not be generalized across M2/M3/other variants.

It does not overturn the source/photo evidence for horseshoe magnets on the first small-machine variant; it strengthens the need for precise machine identity.

## 1.7 “Crystal” is the direct Baumann-to-Marinov term

`SMwebL1.jpg` states that Baumann spoke about a **“crystal”** and, according to Marinov, did not use the word `rectifier` in that conversation. Marinov says he did not know what the crystal was and that it could not be seen clearly.

This creates an important source distinction:

- **Baumann → Marinov small-machine line:** `crystal`;
- **Methernitha institutional technical description:** `rectifying diode` as part of cycle control;
- **Hauser medium/large-machine reconstruction:** possible rectifier/crystal assembly at the top.

These may describe related functions or different components/variants, but they must not be collapsed into one proven part.

## 1.8 Top “bar” remains visually unresolved

Marinov explicitly notes the bar at the top of the small machine but says the photograph does not reveal enough to reconstruct what is inside.

**Consequence:** the top-module carrier remains a black box; visible external geometry may be reconstructed, hidden internals remain reversible variants.

---

# 2. Albert Hauser 1986 direct-visit report: medium / ~500-mm family

These observations are valuable primarily for the large/medium lineage. They must **not** be imported into M2 without a source bridge.

## 2.1 Disk and sector geometry

Hauser describes a Plexiglas disk of approximately **500 mm diameter × 5 mm thickness** with **50 chrome-steel lamellae**, approximately **0.2 × 20 × 160 mm**, on the outside surface. A corresponding disk is described as darker, counter-rotating and carrying lamellae on both sides.

This is strong model-specific evidence for a large/medium two-disc machine and a useful control against later attempts to assign large-machine sheet sectors to M2's small wire-sector rotor.

## 2.2 Speed / mechanical regulation

The 1986 report associates the large assembly with a magnet wheel / timing arrangement and approximately **60 rpm**. Later Holzherr 1999 reports roughly **15 rpm** for a 50-cm demonstration.

**Consequence:** even within the ~50-cm class, speed is configuration/date specific; there is no universal Testatika rpm.

## 2.3 Stationary perforated electrodes

Hauser states that the lamellar/electrode pieces are perforated and do not rub the disks. His report describes approximately:

- 8 stationary pieces on the front;
- 6 on the back;
- the last two oriented differently, approximately edge/radial relative to the disk.

`ABweb9.jpg` reinforces this with the explicit note that none of the electrodes touch the disks.

**Consequence:** non-contact electrostatic coupling is not merely an M2 peculiarity; it recurs in a direct large-machine observation line.

## 2.4 Large cylindrical assemblies are materially different from M2 pots

The 1986/1988 Hauser material describes the large cylinder position as a multi-layer structure with:

- concentric metal grid tubes;
- acrylic/plastic insulating tubes between them;
- a central magnet tube;
- bifilar copper winding around the central tube.

`AHwebL7.jpg` gives a more explicit 1988 description of **three concentric metal grid tubes** per cylinder, separated by acrylic, with two winding layers and plastic foil insulation.

This is important because it explains why some secondary literature calls the large cylinders coils/transformers while Marinov insists that the small-machine side units are capacitors.

**Repository rule:** large-cylinder internal construction is M6a evidence and must not overwrite the simpler M2 pot baseline.

## 2.5 Horseshoe magnet modules

Hauser describes horseshoe magnets with windings on the legs and insulating/perforated layers between the poles. His later answer says the small coils seen beside the horseshoes are actually wound on the magnet legs.

Again this is large/medium-machine evidence, not automatic M2 internal geometry.

## 2.6 Top crystal/rectifier assembly — observer reconstruction

Hauser's 1986 report interprets a top assembly as possibly a rectifier. He describes an oblong perforated-metal piece around a coil and a glass-covered region containing one or more crystals, with end pieces he considered magnetic.

Evidence status is mixed:

- geometry: P1 observer reconstruction;
- identity/function as rectifier: I1 interpretation;
- exact crystal material: unknown.

This is a useful cross-machine precedent for a multi-terminal / nonlinear top module but not a solved M2 schematic.

## 2.7 Claimed 300 V × 10 A output and three isolated circuits

`ABweb9.jpg` reports a claimed usable performance of about **300 V × 10 A**, taken from copper rings on top of the large cylinders, and says the machine appears to contain three isolated circuits that must work together.

This is not a closed independent energy balance. It is useful as a **node/topology lead** only.

---

# 3. Hauser 1988 details

`AHwebL7.jpg` / `AHwebl8.jpg` add several concrete model-specific details:

- three concentric metal-grid cylinders with acrylic separators in the large cylinder assembly;
- central vertical magnet tube;
- two layers of approximately 18-gauge enamelled copper wire arranged so the winding acts bifilarly;
- plastic insulation between magnet tube / first winding and between winding layers;
- one observed magnet orientation with pole axis directed toward the disks;
- crystals observed only in the top position described as pos. 12;
- large machine speed regulation associated with the magnet wheel;
- large machine described as using a small DC motor in that configuration, while small machines were described as being driven by a `Poggendorff effect` / electrostatic mechanism.

This last point is another reason to maintain date/configuration-specific machine IDs: `drive motor present` is not a universal Testatika property.

---

# 4. Hauser 1992 correspondence: useful conflicts, not M2 baseline

`AHwebL5.jpg` and `AHwebL6.jpg` are particularly valuable because Hauser explicitly discusses his own reconstruction attempts and uncertainty.

Useful leads:

- he regarded magnetism as useful but not necessarily fundamental;
- he relays that small capacitors were said to be similar in principle to larger ones, but exact internal equivalence is not demonstrated;
- he distinguishes the large machine's magnetic sheet-like sectors from smaller machines using wire/thread-like conductors, possibly copper;
- he reports difficulty establishing the exact connections between grid and coil structures;
- he discusses multiple possible stationary-electrode connections rather than presenting one known authentic circuit.

These pages should therefore be treated as **source-conflict and experiment-design evidence**, not as a final wiring solution.

---

# 5. Direct implications for the M2 research replica

The following changes are justified by the primary scans:

1. **Floating rotor-sector baseline:** no neighbour resistor ring in the M2 baseline.
2. **Two-lead historical pot interface:** each small side condenser should have a historically faithful two-wire mode.
3. **No conventional drive motor in the M2 baseline:** rpm motor only as removable laboratory instrumentation.
4. **Crystal terminology split:** do not automatically equate Marinov's `crystal` with the institutional `rectifying diode` or Hauser's large-machine rectifier interpretation.
5. **No Tesla/AC baseline:** preserve low-frequency/electrostatic interpretation unless new primary evidence contradicts it.
6. **Machine-specific magnet rule:** M2/M3/large-machine magnet statements remain separated.
7. **Large-cylinder segregation:** Hauser's three-grid/bifilar/magnet-tube cylinder belongs to the medium/large family, not automatically to M2 pots.
8. **Language correction:** primary Marinov evidence now exists for `ANOTHER language`; only the popular exact wording remains unverified.

## Historical gaps that remain open

Even after this source upgrade, the scans do **not** reveal:

- exact M2 through-disc route;
- exact M2 stator grouping/polarity;
- complete M2 node-to-node wiring;
- exact M2 pot capacitance / spiral turns / polarity;
- material and I-V behaviour of the `crystal`;
- exact M2 startup charge state;
- any closed proof of net energy gain.
