# Internet source audit — round 5 — 2026-08-17

## Scope

Round 5 resolves two provenance problems that materially affect the research archive:

1. the frequently repeated `4 August 1999 Testatika demonstration` date;
2. Stefan Hartmann's very early digital Testatika animation/source-image distribution (`PERPET.LZH`, `100Watt.fli`).

The round also records the limits of the current search: the early binary media package itself has **not** yet been recovered.

## 1. 4 August 1999 is explicitly a translation date in the preserved Holzherr/Hartmann source

Two preserved copies of the Hans Holzherr report state at the head of the document:

> `Translation by Stefan Hartmann and Hans Holzherr on 4th of August 1999.`

Public preservation copies:

- https://rimstar.org/sdenergy/testa/report99.htm
- https://www.novakcorp.com/energy/experiments/tesnews.htm

The Novak preservation copy also retains a later part of the correspondence with an explicit email header:

- `Date: Mon, 2 August 1999 16:39:44 -0400`
- From Hans Holzherr to Stefan Hartmann.

A report email dated 2 August cannot have originated from a visit that first occurred on 4 August. Therefore **4 August 1999 cannot be the visit date for the Holzherr report represented by this preserved source chain**.

### Consequence for the later NET-Journal date

The 2011 Schneider/NET-Journal retrospective says a demonstration for 30 Swiss engineers occurred on 4 August 1999. Given that 4 August is explicitly the Hartmann/Holzherr translation date in the older preserved source, the later 4-Aug visit date is now best classified as:

`LIKELY RETROSPECTIVE DATE CONFLATION WITH TRANSLATION/PUBLICATION DATE`.

This is a source-critical inference based on the chronology; it is not proof of which earlier day the visit occurred.

## 2. 5 June 1999 becomes the current best-supported concrete visit-date candidate

The surviving programme for the 13-Mar-2004 Zurich seminar `Das Geheimnis der Testatika` explicitly schedules a retrospective presentation titled:

`Experimente vor 34 Ingenieuren am 5. Juni 1999 — Eindrücke von einer Demo vor Altherren des Technikums Burgdorf`.

Source:

- https://guns.connect.fi/innoplaza/energy/conference/Schneider/Testatika.html

This is not contemporaneous 1999 documentation, but it is:

- more specific about the event identity;
- earlier than the 2011 retrospective;
- consistent with the Holzherr material's broad `over 30 technicians and engineers` wording;
- not contradicted by the 2-Aug/4-Aug correspondence chronology.

### Current event-date status

Use:

> **5 June 1999 = current best-supported candidate for the Burgdorf/over-30-engineer visit.**

But do **not** upgrade it to `historically proven exact date` until a contemporaneous invitation, attendee list, dated photograph/video, signed visit note or other 1999 event record is recovered.

The `4 August 1999` visit date should no longer be shown as an equal unresolved candidate for the same Holzherr event; it is now specifically tagged as likely translation-date conflation.

## 3. Hartmann's early Testatika digital animation is a concrete historical media artifact

A preserved early Stefan Hartmann message describes an IBM-compatible Testatika animation package distributed through CompuServe:

- forum: `GRAPHSUPPORT`;
- download library: `9`;
- archive: **`PERPET.LZH`**;
- stated archive size: about **225 KB**;
- included ASCII documentation: **`energy2.txt`**.

Preserved source:

- https://newtotse.com/oldtotse/en/fringe/free_energy/statika1.html

Hartmann identifies himself as the creator of the computer animation and says it used digitized pictures from a videotape sold by Methernitha.

This is valuable as **media provenance**, regardless of the physical claims Hartmann makes elsewhere in the same message.

## 4. `100Watt.fli`: eight 640×480×256 frames from the Methernitha tape

A later preserved copy of the demo instructions gives much more technical detail:

- command `run1` loads **`100Watt.fli`**;
- it contains **8 frames**;
- frame format is stated as **640 × 480 × 256 colours**;
- Hartmann says the frames were digitized from the Methernitha Testatika videotape;
- he says he used image-enhancement tools and converted them to SVGA FLI format;
- `run2` is described as a greyscale VGA lamp-demo animation;
- `run3` is described as showing a complete running Testatika machine in VGA;
- Hartmann mentions a Fricke HVGA frame-grabber/digitizer in connection with the greyscale animation.

Preserved copy:

- https://keskustelu.suomi24.fi/t/419517/tietaako-kukaan-mista---

### Why this matters technically

The project's current archive video sources are mostly 320×240 or 352×288. If `100Watt.fli` really contains eight separately digitized 640×480 source frames rather than simple interpolation from those exact low-resolution encodes, it could preserve additional visible structure.

However, the text also says Hartmann **enhanced** and converted the images. Therefore even if recovered:

- 640×480 does not automatically mean 640×480 native optical detail;
- sharpening/contrast/resampling may create apparent edges;
- each frame must be compared against matching frames in the surviving videos before geometry is upgraded.

## 5. The early media package itself is not yet recovered

Targeted searches in this round for:

- `PERPET.LZH`;
- `100Watt.fli`;
- `energy2.txt` together with the Testatika package;
- Internet Archive exact-name matches;

found preserved textual descriptions, but **did not locate a provenance-secure downloadable copy of the original binary archive**.

Therefore the repository must say:

> `PERPET.LZH / 100Watt.fli are historically documented acquisition targets; binary artifact not yet acquired.`

It must **not** say the 640×480 frames have been inspected.

## 6. Message-date/version conflict is retained

Preserved copies of Hartmann's early distribution text carry different date markers:

- one block says Berlin, 3 February 1991;
- another block says 20 January 1991;
- the later demo-instruction copy says 20 January 1992.

A surviving Google Groups Hartmann post from early February 1992 refers to the Methernitha Testatika `SVGA animation` as something he had already done and mentioned in an earlier posting.

This establishes that the animation existed by early 1992, but it does not by itself determine which preserved 1991/1992 header is the canonical original release date.

Decision:

- artifact existence/properties = relatively strong Hartmann-self-report provenance;
- exact first-release date = `VERSION/TRANSMISSION CONFLICT` pending original CompuServe/archive metadata.

## 7. Claims inside the Hartmann package description are not imported as operator facts

The same Hartmann text asserts, among other things, that Testatika:

- supplies kilowatt-scale power;
- uses charged/ionized air as energy source;
- has no hidden source;
- works as a modified Wimshurst machine.

Those statements remain **Hartmann 1991/92 claims/theory**. The fact that the message accurately documents a file package does not raise the physical assertions to primary Methernitha evidence.

Source-role separation:

- `Hartmann created/distributed PERPET.LZH` → Hartmann direct evidence about his own artifact;
- `frames came from a Methernitha-sold tape` → Hartmann direct source-provenance statement;
- `machine produces 3 kW / energy comes from ionized air` → Hartmann assertion, not independent measurement.

## 8. Relationship to the old Oulu/colossus archive trail

A 2003 Finnish discussion preserves a statement that Testatika files had been copied from the vanished FTP tree:

`ftp://phoenix.oulu.fi/pub/free_energy`

and says the source files dated back to the early 1990s.

The same discussion preserves the detailed `run1/run2/run3` Hartmann animation instructions.

This makes the Oulu FTP lineage a particularly promising recovery route for `PERPET.LZH` or its unpacked contents. The text alone does not prove the FTP held that exact archive at a specific date; the actual archived directory listing or files are still required.

## 9. Round-5 source hierarchy changes

### Upgraded

- `4 Aug 1999` = explicit **translation date** in preserved Holzherr/Hartmann source.
- Holzherr correspondence existed by **2 Aug 1999**.
- `5 Jun 1999 / 34 engineers` = current best-supported candidate for the Burgdorf/over-30-engineer demonstration, still not contemporaneously proven.
- `PERPET.LZH`, `energy2.txt`, `100Watt.fli`, run1/run2/run3 = concrete early Hartmann digital-media artifact family.
- `100Watt.fli` = Hartmann-described 8-frame, 640×480×256 enhanced/digitized animation from Methernitha tape.

### Downgraded/corrected

- `4 Aug 1999 = visit date` → likely retrospective conflation for the Holzherr/Burgdorf event.
- `Hartmann 640×480 source proves more detail` → **not established until binary recovery and synchronized frame comparison**.
- Hartmann's kilowatt/air-ion claims remain Hartmann assertions.

## 10. Still unresolved

Round 5 still does not recover:

- `PERPET.LZH` binary;
- `100Watt.fli` binary;
- original CompuServe upload metadata;
- contemporaneous 5-Jun-1999 invitation/attendee record;
- authentic hidden Testatika circuit;
- crystal identity/function;
- exact M2 wire route;
- M6a cylinder node map;
- closed independent energy balance.

These remain OPEN/UNKNOWN.
