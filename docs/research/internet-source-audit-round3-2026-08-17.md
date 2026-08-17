# Internet source audit — round 3 — 2026-08-17

## Scope

Round 3 continues the provenance-first public-Internet crawl. It focuses on two things:

1. recovering a directly attributable Marinov text block for machine-specific observations that were previously scattered through later retellings;
2. separating later Albert Hauser recollections/operator statements from contemporaneous Hauser numeric evidence.

No historical CAD is changed merely because a web source repeats a claim. Translation, retrospective memory and machine identity are retained as explicit limitations.

## 1. Marinov's 1989 Testatika article: a complete 29-page German translation mirror is publicly recoverable

Public PDF mirror:

- Stefan Marinov, `Die Maschine TESTATIKA und ihr physikalischer Hintergrund`, marked `First Published in 1989`, German translation hosted by Nuetec:
  https://nuetec-forschung.de/Thesta-Distatika/Marinov_physik_Hintergrund.pdf

The PDF explicitly says Marinov did **not** understand the operating principle and could not reconstruct it. This is a key source boundary: his observations are valuable; his proposed electrical explanation remains interpretation.

The mirror is a later German translation, not an original-language 1989 print scan. Exact wording should therefore be checked against a source-language edition before treating translation nuances as verbatim Marinov language.

## 2. Machine taxonomy in Marinov's own article

In the Testatika section Marinov distinguishes:

- **small machines:** one wheel/disc;
- **medium and large machines:** two counterrotating wheels/discs;
- two small machines he personally saw, with the first/right-hand one being the one he says he tested;
- the medium machine, which he says he knew from film;
- the large machine under construction, of which he says he saw many components/elements.

This is important because later Internet diagrams often collapse all Testatikas into one machine.

### Consequence

Observations must be scoped at least to `small / medium / large` unless figure/object continuity proves a more precise M-ID.

## 3. Medium-versus-large perforated-sector geometry

Marinov states that the medium and large machines used perforated metal sectors, but describes a visible scale difference:

- medium machine: **smaller holes**;
- large machine: **larger holes**.

He says Baumann showed him sectors for the large machine and told him they were a special Fe-Ni alloy intended to be slightly magnetized.

Evidence classification:

- perforated-sector geometry and relative hole-scale statement: `MARINOV AUTHOR TEXT / OBSERVATION-REPORT`;
- special Fe-Ni alloy and intended magnetization: `BAUMANN → MARINOV SOURCE-STATED`;
- exact alloy chemistry, hole diameters and magnetization values: `UNKNOWN`.

This does not identify the medium machine as Hauser M6a with certainty and therefore does not directly edit M6a CAD.

## 4. Medium-machine stationary electrodes: visible count lower bound

Marinov writes that on the medium-machine image he could count **9 electrodes and that there were surely at least 10**. He explicitly says he did not determine whether the same electrodes both collected and drove, or whether those functions were separated.

This is a new useful constraint:

- `medium machine visible electrode count >= 9, author infers >=10`;
- exact total count: `UNKNOWN`;
- collector/driver grouping: `UNKNOWN`;
- exact identity with M6a's Hauser 8-front + 6-rear source line: `UNRESOLVED`.

Therefore the Marinov count is a **cross-source consistency/conflict check**, not a replacement for the Hauser M6a count.

## 5. Small-machine startup and metal-shield observations are now directly locatable

The same Marinov text states:

- dry air: about **3–4 pushes** were enough to start;
- humid air: more pushes were required;
- Baumann told him the small-machine axis had to point East–West for startup;
- once running, Marinov says he tested moving/tilting/reorienting the small machine and rotation continued;
- running speed about **1 revolution per second (~60 rpm)**;
- a large metal plate brought behind the machine stopped rotation and removed the static torque;
- second/third restarts were easier than the first.

These observations were already upgraded in Round 1; Round 3 supplies a stable, page-locatable public text source for them.

Mechanisms remain open: shielding, capacitance, field-boundary conditions, leakage, building fields, ambient magnetic field and charge-history effects must be separated experimentally.

## 6. Counterrotation cord/string: direct Marinov observation on large-machine hardware

Marinov says the medium machine used the same type of contra-rotation arrangement he discusses earlier and adds that the **cord/string he saw in the large machine was quite loose**. He interpreted that looseness as suggesting weak forces on the wheels.

Use:

- historical mechanical lead for a large/two-disc family;
- useful when checking transmission tension and parasitic torque.

Limitations:

- exact large-machine identity versus M6a/M6c is unresolved;
- Marinov's inference from belt/string looseness to force magnitude is qualitative.

No existing M6a drive geometry is silently overwritten.

## 7. Large open cylindrical parts: strong Marinov observation, but interpretation remains his

Marinov says he saw the large-machine `capacitive transformers` open. He describes:

- an outer cylindrical electrode;
- an inner electrode in the form of a coil of thick copper wire.

He then states his opinion that these are simple capacitors, not Tesla transformers or resonant HF circuits. He also says he had only seen the medium machine on film and the large machine was, in his description, a roughly 2:1 copy of the medium machine.

This reinforces the existing `M6c` conflict family. It does **not** erase Hauser M6a's separate direct 1988 three-grid + acrylic + magnet-tube + bifilar description. Possible explanations include different machines, different build stages or observers seeing different subassemblies.

## 8. Marinov's proposed high-V drive / lower-V collection buses are explicitly hypothesis

After describing uncertainty about electrode roles, Marinov uses explicitly inferential language to propose:

- high-voltage capacitors connected to driving electrodes;
- lower-voltage capacitors connected to collecting electrodes;
- both replenished by the machine.

He then says it is not clear to him how the machine really works.

Therefore this two-bus model is **MARINOV-HYPOTHESIS**, not recovered wiring. It remains useful as a falsifiable experiment configuration but cannot be labelled `original schematic`.

## 9. Einsiedeln SAFE congress 27–29 Oct 1989: strong convergence on film-only Testatika presentation

Two source lines now converge on the presentation format:

### Marinov, TWT VII

Marinov states that at the 27–29 Oct 1989 SAFE congress in Einsiedeln, with about **700 participants** by his count, a **30-minute film** about Testatika/Methernitha was presented and Methernitha representatives supplied information.

### Oswald Eggenberger / Relinfo, May 1990

A contemporary external information sheet says Methernitha's Bosshard presented Testatika before about **500 attendees**, **not in natura but only in film**.

### Corrected conclusion

- `Einsiedeln 27–29 Oct 1989 Testatika presentation = FILM-ONLY` — strong source convergence;
- attendance = approximate/conflicting (`~500` vs `~700`);
- later statements that imply a live machine at **that same event** should be treated as conflation unless a date-locked contemporaneous source proves otherwise.

This materially reduces the previous live-machine-vs-film ambiguity for the 1989 Einsiedeln event itself.

## 10. Albert Hauser later retrospective: atmospheric/window/storm claims

Albert Hauser's later author article preserves several qualitative statements he attributes to Baumann or to his own visit:

- Hauser says his group changed the generator's physical location to test a hidden-transmitter/focus idea;
- he asked whether it would work in space; he reports Baumann answered no and described atmospheric charged ions as being collected/sorted;
- he reports Baumann saying that with doors/windows closed the device would stop, while opening a window would allow restart;
- he reports the generator being stopped during atmospheric disturbances/thunderstorms to reduce damage risk;
- he reports Baumann likening the technique to lightning/weather-light phenomena;
- he retrospectively mentions a temporary 2-m-wheel version and an operator-level 30-kW claim.

Public author article:

- https://equapio.com/energie/testatika-legendaere-energiemaschine-der-methernitha/

### Critical limitation

The same web transcription contains obvious numeric corruption relative to Hauser's contemporaneous scanned material (for example `500 cm` where the direct source line is ~500 mm, and an implausible ~1 rpm transcription). Therefore:

- **do not use this later page as numeric source of record**;
- qualitative statements are classified `HAUSER-LATE-RETROSPECTIVE / BAUMANN→HAUSER`;
- atmospheric ions are an operator explanation, not an established energy source.

### Experimental consequence

The claims justify a controlled environmental test matrix, not belief in the mechanism. Variables to separate include:

- relative humidity and temperature;
- controlled fresh-air exchange;
- measured ion concentration;
- ambient electrostatic field;
- local magnetic field;
- mains/RF/EM environment;
- charge-history/preconditioning state.

A window-open/window-closed effect without those controls would be uninterpretable.

## 11. Kelly 1992 quad-disc paper is a derivative design, not Testatika evidence

Official SAE record:

- Donald A. Kelly, `An Enhanced Quad-Disc Electrostatic Generator`, SAE Technical Paper 929472, 27th IECEC, 3 Aug 1992, DOI `10.4271/929472`.

The paper proposes Kelly's own four-disc electrostatic design and explicitly extends ordinary Wimshurst-style ideas with stator discs and speculative capacitive-transformer functions said to be similar to the Swiss converter.

Classification:

- `KELLY-DERIVED-DESIGN / HYPOTHESIS`;
- useful as a comparison experiment or history of Kelly's evolving model;
- **not** a recovered Testatika schematic and not authority for historical M6 wiring.

## 12. Round-3 status

### Newly tightened

- Marinov medium machine: `9 visible; surely >=10` electrodes.
- medium vs large: perforated sector hole scale differs.
- loose large-machine counterrotation cord/string is directly locatable in Marinov's text.
- Marinov's two-bus electrical model is explicitly hypothesis.
- Einsiedeln 1989 is now strongly classified as **film-only** for Testatika; attendee count remains approximate/conflicting.
- Hauser atmospheric/window/storm statements are preserved at the correct retrospective/operator-evidence level.
- Kelly 1992 quad-disc work is explicitly derivative.

### Still not solved

No Round-3 source provides:

- an authentic complete M2 or M6 node-to-node schematic;
- exact M2 through-disc route;
- exact M2 pot internal topology/capacitance;
- crystal material or measured I–V curve;
- exact M6a three-grid-cylinder node map;
- closed historical input/output/storage metrology;
- independently replicated net energy gain.

Those remain UNKNOWN.
