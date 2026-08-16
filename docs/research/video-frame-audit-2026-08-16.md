# Historical video frame audit — 2026-08-16

## Scope

This audit covers every video file in the user-supplied Testatika archive. The third-party videos and extracted frames are **not** redistributed in the repository. Instead the repository records hashes, embedded metadata, decoded-frame coverage, time locators, machine assignment and evidence consequences.

The audit is specifically designed to avoid the common failure mode of transferring a visible detail from a large/workshop machine into the Marinov M2 small-machine baseline.

## Frame-analysis method

All eight video files were decoded through their video streams with `ffprobe`/`ffmpeg`.

Total decoded video frames: **35,445**.

The workflow used three layers:

1. full-stream decode / frame count to ensure the complete time span was traversed;
2. automatic scene-change extraction (`scene` threshold 0.22) plus fixed-time sampling;
3. targeted enlarged frames for visually important M2 and subsystem sequences.

The two legacy RealMedia files produce intermittent RV30 decoder warnings, so their visual evidence is treated as archival footage with codec-corruption caveats rather than pixel-perfect originals.

## File-level media ledger

| File | SHA-256 | Embedded title / role | Format / video | Duration | Decoded frames | Machine scope |
|---|---|---|---|---:|---:|---|
| `video/meth1.asf` | `10085bf6766628d01eaf08a1b43219e9bdc2ddcc9ccb6e7d20f9b53ab64112a4` | `Electrostatic Energy`; `Race to Zero Point Tape` | ASF / MSMPEG4v3, 320×240, 25 fps | 153.936 s | 3,821 | historical electrostatic context + mixed Testatika visuals |
| `video/meth2.asf` | `a9ad8108b7b2b7f2b43b7bc9c149c034c6db12bae1d7da43f2578f2a03dab331` | `Methernitha Testatika machine` | ASF / MSMPEG4v3, 320×240, 25 fps | 114.118 s | 2,776 | large/two-disc family |
| `video/meth3.asf` | `2dfbd6f48520adf5fa5e049b1ecc95ea0df2897319ebda605466d4564d8977c3` | `Methernitha Testatika 3 KWatts machine` | ASF / MSMPEG4v3, 320×240, 25 fps | 125.918 s | 3,129 | large 3-kW family |
| `video/meth4.asf` | `6a1c395231eb70185c0348cdf86a66bdfb00d089be6d6cfa274d43511c791d42` | `Methernitha Testatika smaller 300 Watts machine` | ASF / MSMPEG4v3, 320×240, 25 fps | 100.286 s | 2,476 | small single-disc machine; visually same assembly as `testabig.jpg`; high M2/M3 relevance |
| `video/meth5.asf` | `12d81a012b8b1c827c44de1ba735bd652858dc2cd474f1dbbf5d0f4bbce7b51d` | `Testatika 3 KWatts machine powering a load` | ASF / MSMPEG4v3, 320×240, 25 fps | 195.686 s | 4,869 | large 3-kW family load demonstration |
| `video/testa01.ram` | `7f021a14f67062107d75a8dffff5c42ceea9cc741f38cae3d484a9d7bc0af8ef` | metadata: `Dieter Dienst speaking with Luzi Cathomen`; abstract says visit to Methernitha labs | RealMedia / RV30, 352×288, 25 fps | 318.957 s | 7,955 | multi-machine workshop footage |
| `video/testa02.ram` | `3975094aa0d56a1b894d49ecc5b476e74f11705d1668bda66683851579f6c8df` | metadata author `Dieter Dienst`; same visit abstract | RealMedia / RV30, 352×288, 25 fps | 317.041 s | 7,899 | multi-machine workshop footage |
| `video/testatikadeutsch.wmv` | `19df1f29ffce63646ada6c2256b65bcd216e45d47fbe6ddeab4459b90e68575b` | `Methernitha Testatika machine` | ASF/WMV container, MSMPEG4v3, 320×240, 25 fps | 114.118 s | 2,520 | visually redundant with `meth2`; language/audio variant |

### Visual duplicate control

`meth2.asf` and `testatikadeutsch.wmv` have the same duration and the same visual sequence. Synchronized sampled frames from 0–90 s produced identical 16×16 average-hash patterns at each tested timestamp. Their compressed frame streams are not byte-identical and the audio differs, so they are retained as separate archival objects but **not counted as independent geometric evidence**.

---

# 1. `meth4.asf`: highest-value moving source for the small machine

The footage is visually the same physical assembly as `testabig.jpg`: black rear board, red base, single transparent rotor, two large side pots, mirrored perforated structures, top red module and the same central/lower architecture.

Embedded metadata calls it a `smaller 300 Watts machine`. That title is metadata from the archived file and is **not** an independently measured output rating.

## 1.1 00:00–00:07 — central hub close-up

The video resolves a feature that the high-resolution still could only describe as brown/red semicircular markings:

- two symmetric **copper-coloured arcuate pieces** surround the central clear hub area;
- changing video highlights make them appear raised/three-dimensional rather than flat printed marks;
- they stop short near the vertical centreline, producing left/right C-shaped arcs;
- their terminals/connections are not resolved.

**Evidence consequence:** V3 should model these as an explicit observed arc-conductor/rod candidate rather than merely painting semicircular markings. Electrical participation remains unknown.

## 1.2 00:10–00:35 — stable full frontal views

The frontal sequence reinforces:

- one central single disc;
- mirror-symmetric upper spring/pickup stations;
- separate outer panel assemblies;
- separate lower front panel;
- two large side pots;
- central lower vertical module;
- multiple conductor paths visible across the black rear plate.

No rubbing collector can be identified in these views.

## 1.3 00:40–00:47 — outer-panel close-ups

The video shows that each outer rectangular panel is not a single flat grid. At least three visible layers/elements exist:

1. coarse light/white perforated carrier;
2. darker fine rectangular lattice/inset;
3. reddish-brown elongated conductor/frame/comb associated with one long edge of the dark inset.

Separate metal leads enter/leave the assembly.

**Consequence:** V3 `outer_panel` must remain a layered assembly. The dark inset must not be treated as a colour-only decal or automatically labelled carbon/graphite.

## 1.4 00:50–01:05 — pots and lower-centre architecture

Close-ups show:

- the large side cylinders have dense horizontal/mesh-like conductor texture and substantial top/bottom metal rings;
- a dark conical/insulating-looking terminal structure sits at the top of each pot;
- adjacent small white perforated structures are mechanically separate from the cylinder body;
- long vertical springs terminate in separate lower circular eyelets;
- the central lower vertical element beneath the rotor looks like a **perforated cage/prismatic module with end caps**, not a plain solid cylinder;
- the lower front rectangular grid/panel is a separate assembly below it.

The footage remains consistent with Marinov's grid / plastic / central spiral description but is not high enough resolution to identify which visible texture belongs to the outer grid versus an inner spiral seen through a transparent layer.

## 1.5 01:10–01:40 — analogue meter sequence

The file shows a connected analogue multimeter and then the meter face/selector. The archived resolution is insufficient to establish a defensible electrical value and range from a single frame alone. Therefore no new numeric output claim is extracted from this sequence.

**Rule:** visual meter deflection is evidence that a demonstration measurement was shown, not a calibrated energy balance.

---

# 2. M2 visual-source consequences

## 2.1 `testabig.jpg` provenance strengthened

`testabig.jpg` SHA-256:

`1151cbcff9e1621c38340cab2c19c2ea60bbf646474358d0731cc292100eb1e7`

Dimensions: 1884 × 1601.

The still and `meth4.asf` show the same machine configuration with matching hub, top bar, outer panels, spring stations, pots, lower panel and back board. This provides a moving-image provenance bridge for the still's geometry.

It does **not by itself** prove the archived `300 Watts` metadata rating or settle every historical M2/M3 naming question.

## 2.2 Hub arcs upgraded from “markings” to physical-geometry candidate

The V3 photo analysis should no longer describe the copper-coloured semicircles only as markings. Best evidence wording:

> two symmetric copper-coloured arcuate pieces are visible around the central hub; video parallax/highlights support a raised physical-part interpretation, while electrical connection and exact section remain unresolved.

## 2.3 Outer panels are definitively layered visually

This narrows the reconstruction space. A single perforated plate is insufficient to reproduce the visible assembly.

Minimum visual layers:

- coarse perforated structural carrier;
- fine/dark inset grid;
- elongated reddish conductor/frame element;
- attached external leads.

## 2.4 Central lower module geometry refined

The lower centre should be represented as a perforated rectangular/cage-like element with separate end regions rather than a generic round post wherever the V3 external geometry is intended to follow the official footage.

---

# 3. Large-machine official video (`meth2`, `meth3`, `meth5`)

These videos are extremely useful for **model separation**.

Repeated visible features include:

- two large counter-rotating sector discs / dense lamella structures;
- perforated stationary field/pickup plates separated from the disc surfaces;
- tall perforated cylindrical assemblies;
- lower orange/red wound coils;
- mechanical speed-control / wheel structures;
- load demonstrations with incandescent lamps and analogue instrumentation.

This visual family matches the Hauser large-machine descriptions far better than Marinov's small-pot description.

**Consequence:** large-machine coil/cylinder internals, 50-sheet sector geometry, drive/regulation hardware and load claims must not be copied into M2 merely because all machines share the Testatika name.

`meth3` side views are particularly useful because they show the physical separation of the tall perforated cylinders, wound coils and disc plane.

`meth5` documents a load demonstration but still does not provide a closed accounting of all stored, mechanical and auxiliary energy inputs.

---

# 4. `testa01.ram` / `testa02.ram`: direct workshop provenance and multi-machine separation

Embedded metadata is unusually useful:

- creation date: 17 Nov 2001;
- `testa01` title metadata names a conversation between Dieter Dienst and Luzi Cathomen;
- author metadata: Dieter Dienst;
- abstract: visit to Methernitha labs and inspection of Testatika machines;
- keywords: `Testatika machines Methernitha`.

This metadata strengthens the provenance of the already archived Cathomen workshop source line. It is provenance for the media object; it is not independent validation of the technical claims made in the audio.

## 4.1 Visual content is multi-machine, not one Testatika

The two clips move through several different assemblies:

- workshop benches and loose components;
- a large black/red-disc experimental assembly viewed from front, side and rear;
- tall cylindrical modules and upper horizontal tube/coil-like components;
- a small Testatika-like frontal assembly shown separately;
- handheld/demonstration rotor/electrostatic models.

Therefore no geometry from these clips should be inherited by M2 without a timestamped object match.

## 4.2 Rear/side views are valuable for subsystem precedent

The clips provide views unavailable in the standard frontal stills:

- rear support frames;
- spacing between disc and vertical structures;
- mounting of tall cylinders relative to the disc plane;
- upper horizontal modules from below/side;
- separate mechanical/electrical subassemblies on the bench.

These are high-value **cross-machine precedents** but not M2 hidden-circuit evidence.

## 4.3 Codec caveat

Both files are RV30 RealMedia and generate intermittent decoder warnings. The full streams can still be traversed, but fine pixel measurements from corrupted frames must not be treated as metrology-grade source data.

---

# 5. `meth1.asf`: context, not a direct M2 construction source

`meth1` mixes conventional electrostatic-machine history, explanatory material and Testatika imagery. Its best use is comparison/provenance:

- conventional electrostatic machine precedents;
- non-contact electrostatic motor/generator context;
- historical comparison imagery.

It is not used to override direct Marinov/Hauser observations.

---

# 6. New machine-separation rule from the video corpus

The video archive requires at least four visual families to be kept separate:

1. **small single-disc / `meth4` / `testabig` family** — primary M2/M3 reconstruction interest;
2. **large two-disc / 3-kW official-video family** — M6 umbrella;
3. **2001 workshop black/red-disc prototype family** — separate workshop variant; do not call it M2;
4. **small handheld/principle demonstrators** — comparison/early prototypes.

This prevents later secondary drawings from forming a synthetic machine by combining the best-looking part of every video.

---

# 7. Highest-value changes justified by the video audit

1. Add explicit **hub arc geometry** to the V3 evidence model.
2. Preserve the outer panel as a **layered** carrier + inset grid + elongated conductor assembly.
3. Refine the lower central module to a perforated cage/prism in photo-faithful geometry.
4. Treat `meth4` and `testabig.jpg` as linked visual evidence for the same small assembly.
5. Add file-level hashes and embedded metadata for all historical videos.
6. Upgrade `testa01/testa02` provenance using their embedded 2001 author/title/abstract metadata.
7. Do not double-count `testatikadeutsch.wmv` and `meth2.asf` as independent visual evidence.
8. Keep large-machine cylinder/coil architecture out of the M2 pot baseline.
9. Treat analogue meter/lamp sequences as demonstration evidence only, not closed energy metrology.

## Remaining visual gaps

Even the complete video pass does not expose:

- back side of the exact `meth4` small assembly in sufficient detail;
- exact through-disc wire path;
- exact electrical node map;
- pot internal terminal connections;
- crystal interior/material;
- whether thin visually hidden layers exist inside every transparent stack.

Those remain legitimate historical unknowns rather than reasons to invent a circuit.
