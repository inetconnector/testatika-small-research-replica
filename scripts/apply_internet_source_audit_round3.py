#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def append_block(path: str, marker: str, block: str) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    if marker in text:
        return
    if not text.endswith("\n"):
        text += "\n"
    text += "\n" + block.strip() + "\n"
    p.write_text(text, encoding="utf-8")


def append_rows_by_first_column(path: str, rows: list[str]) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    lines = text.splitlines()
    keys = {line.split("\t", 1)[0] for line in lines if line}
    changed = False
    if not text.endswith("\n"):
        text += "\n"
    for row in rows:
        key = row.split("\t", 1)[0]
        if key in keys:
            continue
        text += row.rstrip("\n") + "\n"
        keys.add(key)
        changed = True
    if changed:
        p.write_text(text, encoding="utf-8")


def append_backlog_rows(rows: list[str]) -> None:
    p = ROOT / "docs/research/source-acquisition-backlog.tsv"
    text = p.read_text(encoding="utf-8")
    targets = set()
    for line in text.splitlines()[1:]:
        cols = line.split("\t")
        if len(cols) > 1:
            targets.add(cols[1])
    changed = False
    if not text.endswith("\n"):
        text += "\n"
    for row in rows:
        cols = row.split("\t")
        target = cols[1]
        if target in targets:
            continue
        text += row.rstrip("\n") + "\n"
        targets.add(target)
        changed = True
    if changed:
        p.write_text(text, encoding="utf-8")


append_block(
    "docs/research/source-basis.md",
    "## Internet source audit round 3 — 2026-08-17",
    r'''## Internet source audit round 3 — 2026-08-17

Canonical Round-3 records:

- [`internet-source-audit-round3-2026-08-17.md`](internet-source-audit-round3-2026-08-17.md)
- [`internet-source-ledger-round3.tsv`](internet-source-ledger-round3.tsv)

Key corrections/refinements:

1. A complete 29-page public German translation mirror of Marinov's 1989 `Die Maschine TESTATIKA und ihr physikalischer Hintergrund` gives a page-locatable author-text source for the M2 startup/shield observations and for several medium/large-machine constraints. It remains a later translation, so exact wording still requires a source-language scan.
2. Marinov says the medium-machine image shows **9 countable stationary electrodes and surely at least 10**. Exact total and identity with Hauser M6a remain unresolved.
3. Marinov distinguishes perforated sector hole scale: smaller holes on the medium machine, larger holes on the large machine. Baumann-attributed Fe-Ni composition/slight magnetization remains source-stated rather than measured.
4. Marinov says the large-machine counterrotation cord/string he saw was quite loose. This is a mechanical lead, not a solved drive system.
5. Marinov's proposed high-voltage drive-capacitor versus lower-voltage collecting-capacitor architecture is explicitly inferential in the same text and remains **HYPOTHESIS**, not recovered wiring.
6. Independent Marinov and contemporary Relinfo accounts converge that the **27–29 Oct 1989 Einsiedeln SAFE Testatika presentation was film-only**. Attendance remains approximate/conflicting (~700 vs ~500).
7. Hauser's later author retrospective preserves Baumann-attributed atmospheric-ion/window/storm claims, but the same web transcription contains obvious numeric corruption versus the direct scans. These statements are retained only as `LATE-RETROSPECTIVE / BAUMANN→HAUSER`, not as established energy-source physics.
8. Kelly's 1992 SAE paper 929472 is explicitly a Kelly-derived quad-disc design, not a recovered Testatika circuit.

No Round-3 item closes the hidden historical circuit or changes the M2/M6 CAD baseline automatically.'''
)

append_block(
    "docs/REPLICATION_STATUS.md",
    "## Internet crawl round 3 — M2 source lock",
    r'''## Internet crawl round 3 — M2 source lock

Round 3 provides a stable public page-locatable Marinov author-text mirror for several M2 observations already present in the ledger: dry-air 3–4-push startup, humidity dependence, Baumann→Marinov East–West startup instruction, post-start orientation independence, ~1 rev/s running observation, direct rear-metal-plate stop and easier later restart.

The source is a later German translation of a text marked first-published 1989, so exact translation wording must not outrank an original-language scan if one is acquired later.

Importantly, Marinov also makes clear in the same article that he did not understand/reconstruct the operating principle. His proposed high-V driving bus / lower-V collecting bus remains a **testable interpretation**, not original wiring.

No V4 CAD geometry changes are justified by Round 3.'''
)

append_block(
    "docs/M6_REPLICATION_STATUS.md",
    "## Internet crawl round 3 — medium/large constraints",
    r'''## Internet crawl round 3 — medium/large constraints

Round 3 adds cross-machine constraints without silently rewriting M6a:

- Marinov's medium-machine image count: 9 stationary electrodes visible, with his statement that there were surely at least 10. Exact total and identity with Hauser M6a's 8-front + 6-rear line remain unresolved.
- Marinov distinguishes perforated-sector hole scale between medium (smaller holes) and large (larger holes).
- Marinov reports a quite loose counterrotation cord/string on the large-machine hardware he saw.
- His open-large-cylinder observation (outer cylinder + inner thick-Cu-wire coil) continues to support separate M6c conflict handling and does not erase Hauser M6a's three-grid/acrylic/magnet-tube/bifilar source line.
- Hauser's later atmosphere/window/storm statements are retrospective/operator explanations only; direct Hauser scans remain the numeric source of record.

Accordingly the current M6a V1 STEP/STL remains unchanged pending an explicit object/source bridge.'''
)

append_rows_by_first_column(
    "docs/research/evidence_matrix.tsv",
    [
        "Marinov Medium-Maschine Elektroden-Untergrenze\tMarinov 1989 author-text translation mirror\t9 Elektroden im Bild zählbar, laut Marinov sicher mindestens 10\thoch für Marinovs Text/Bildzählung; genaue Gesamtzahl/Identität zu M6a ungeklärt\tCross-check für M6-Familie; Hauser 8+6 nicht ersetzen",
        "Medium-vs-Large Lochskala\tMarinov 1989 author-text translation mirror\tMetallsektoren beider Maschinen perforiert; Medium kleinere, Large größere Löcher\tmittel-hoch für relative Geometrie / keine Maße\tkeine M6a-CAD-Änderung ohne Maschinenbrücke; bei neuer Variante relative Lochskala berücksichtigen",
        "Large counterrotation cord loose\tMarinov 1989 author-text translation mirror\tMarinov sah an der großen Maschine eine ziemlich lockere Schnur/cord der Gegenrotation\tmittel-hoch als qualitative Beobachtung / Zuordnung M6a-M6c offen\tmechanische Forschungsvariable: Riemenspannung/Parasitärmoment messen; nicht als exakte Transmission behaupten",
        "Marinov Zweibusmodell ausdrücklich Hypothese\tMarinov 1989 author text\tHV-Antriebskondensatoren und niedrigere-V-Sammelkondensatoren werden von Marinov als Annahme formuliert; tatsächliche Funktion unklar\thoch für Klassifikation als Hypothese\tnur benannte Experimentkonfiguration; niemals Originalschaltplan nennen",
        "Einsiedeln 1989 Präsentationsformat\tMarinov TWT VII + Relinfo Mai 1990\t27-29 Okt 1989 Testatika in Einsiedeln per Film; Relinfo ausdrücklich nicht in natura\thoch durch unabhängige Konvergenz; Besucherzahl ~500 vs ~700 konfliktär\tEvent-Provenienz auf FILM-ONLY korrigieren; Live-Demo nicht diesem Event zuschreiben ohne neue Quelle",
        "Hauser Atmosphäre/Fenster/Gewitter spät\tAlbert Hauser spätere Autorenversion\tBaumann zugeschrieben: Atmosphäre/Ionen, geschlossene Fenster Stop, offenes Fenster Restart, Gewitter-Abschaltung; Standortwechsel als Senderkontrolle\tmittel für späte Hauser-Erinnerung / niedrig für Mechanismus; Webtext numerisch fehlerhaft\tumweltkontrollierte A/B-Tests motivieren; keine Luftionen-Energiequelle als Fakt",
        "Kelly Quad-Disc 1992\tSAE 929472, Donald A. Kelly\teigener Vier-Scheiben-Entwurf mit Swiss-ML-ähnlichen kapazitiven Transformatoren\thoch für Kelly-Design / niedrig-null als historische Testatika-Evidenz\tnur Vergleich/Hypothese; nicht in M6-Historik-CAD importieren",
    ],
)

append_block(
    "docs/research/experiment-plan.md",
    "## Round-3 environment-source discrimination",
    r'''## Round-3 environment-source discrimination

Later Albert Hauser recollection attributes to Baumann a claim that atmospheric charged ions/fresh-air access mattered, including a closed-window stop/open-window restart and storm-related shutdown. This is **not established mechanism evidence**. If tested, the experiment must separate correlated environmental variables.

Minimum randomized matrix:

- enclosure air exchange: controlled low / medium / high;
- RH and temperature independently controlled/logged;
- positive/negative ion concentration measured where instrumentation permits;
- ambient electrostatic field logged;
- three-axis magnetic field logged;
- mains electric field / RF spectrum logged or bounded;
- machine and dielectric charge-history standardized before each run;
- identical dummy-airflow runs where ion/RH conditions are held as constant as practicable.

Outcomes to record:

- startup pushes / startup probability;
- surface-potential map;
- leakage/relaxation time;
- torque and rpm;
- pickup current/charge per cycle;
- any load-node energy, with full auxiliary input accounting.

A simple `window open works` observation is not interpretable because ventilation simultaneously changes humidity, ions, temperature, electric-field boundaries and external EM coupling.

### Medium/large mechanical cross-check

Marinov's author text says the large-machine contra-rotation cord/string he saw was quite loose. For any M6/M6c comparison fixture, log belt/cord tension and bearing/drive parasitic torque before attributing rotation changes to electrostatics. Do not force the current M6a lab drive to mimic an unresolved historical transmission.'''
)

append_backlog_rows(
    [
        "P0\tOriginal-language/print source for Marinov 1989 Die Maschine TESTATIKA und ihr physikalischer Hintergrund\tNuetec provides complete later German translation mirror marked First Published in 1989\tVerify exact wording/figures and remove translation ambiguity for medium/M2 observations\tAcquire source-language print scan with title/copyright/page context; compare paragraph-by-paragraph to translation\tOPEN",
        "P0\tOriginal Einsiedeln 27-29 Oct 1989 SAFE congress programme / proceedings pages for Testatika film\tMarinov TWT VII and Relinfo May 1990 independently indicate film presentation; ISBN proceedings target already known\tLock event programme, film duration, speakers and attendance documentation\tAcquire contemporaneous programme/TOC/Methernitha transcript pages; distinguish attendee estimate from registered count\tOPEN",
        "P1\tOriginal source behind Hauser atmosphere/window/storm recollection\tLater Hauser author article attributes statements to Baumann but contains numeric transcription errors\tDetermine whether atmosphere/ions/window/storm claims exist in contemporaneous 1986/1988 notes or were added later\tSearch DIFØT originals, notebooks or dated correspondence; late web text alone remains retrospective\tOPEN",
        "P1\tNuetec linked Marinov/Methernitha companion PDFs and open correspondence\tNuetec Testatika page links Die Gemeinde, revised Hauser/Kelly, Saunier response and open witness correspondence\tPotential source-language/provenance material not yet parseable in current web cache\tAcquire each document lawfully, hash, identify author/date/publication, and classify before extracting claims\tOPEN",
    ]
)

append_block(
    "STATE.md",
    "## Internet audit round 3 — 2026-08-17",
    r'''## Internet audit round 3 — 2026-08-17

Round 3 is recorded in `docs/research/internet-source-audit-round3-2026-08-17.md` and `internet-source-ledger-round3.tsv`.

Key changes: Marinov's 1989 Testatika article is now available as a complete page-locatable German translation mirror; medium-machine >=10-electrode lower bound, medium/large perforation-scale distinction and loose large counterrotation cord are documented; Marinov's two-bus wiring model is explicitly demoted to hypothesis; independent Marinov + Relinfo evidence strongly classifies Einsiedeln 27–29 Oct 1989 as film-only; late Hauser atmosphere/window/storm claims are preserved as retrospective Baumann-attributed statements only; Kelly SAE 929472 is classified as a derivative design. No historical CAD baseline changed.'''
)

append_block(
    "addon.md",
    "## Internet audit round 3 handoff — 2026-08-17",
    r'''## Internet audit round 3 handoff — 2026-08-17

Read `docs/research/internet-source-audit-round3-2026-08-17.md` and `internet-source-ledger-round3.tsv` before making further historical claims.

Important guards:

- Marinov medium-machine `>=10 electrodes` is not automatically Hauser M6a.
- Marinov's high-V/low-V bus concept is his hypothesis, not recovered wiring.
- Einsiedeln 27–29 Oct 1989 is now strongly film-only for Testatika; attendance remains ~500/~700 conflict.
- Hauser atmosphere/window/storm claims are late retrospective/operator statements and must be experimentally decomposed, not promoted to an energy-source fact.
- No CAD changes from Round 3 without an explicit source-to-machine bridge.'''
)

append_block(
    "CHANGELOG.md",
    "### Internet source audit round 3 — 2026-08-17",
    r'''### Internet source audit round 3 — 2026-08-17

- added a complete page-locatable Marinov 1989 Testatika translation-mirror audit;
- added medium-machine >=10-electrode lower bound and medium/large perforation-scale distinction;
- added loose large-machine counterrotation-cord observation;
- explicitly classified Marinov's proposed two-bus wiring as hypothesis;
- corrected the 27–29 Oct 1989 Einsiedeln Testatika presentation to strong FILM-ONLY convergence, retaining attendee-count conflict;
- added late Hauser atmosphere/window/storm claims with numeric-corruption and retrospective-source guards;
- classified Kelly SAE 929472 as a derivative design, not historical Testatika wiring;
- added controlled environment-variable experiment requirements;
- no historical CAD baseline changed.'''
)

print("Internet source audit round 3 integrated idempotently.")
