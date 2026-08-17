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


def append_tsv_rows(path: str, rows: list[str]) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        text += "\n"
    changed = False
    for row in rows:
        key = row.split("\t", 1)[0]
        # first-column exact-key check
        if any(line.split("\t", 1)[0] == key for line in text.splitlines() if line):
            continue
        text += row.rstrip("\n") + "\n"
        changed = True
    if changed:
        p.write_text(text, encoding="utf-8")


append_block(
    "docs/research/source-basis.md",
    "## Internet source audit round 2 — 2026-08-17",
    r'''## Internet source audit round 2 — 2026-08-17

Round 2 is documented in:

- [`internet-source-audit-round2-2026-08-17.md`](internet-source-audit-round2-2026-08-17.md)
- [`internet-source-ledger-round2.tsv`](internet-source-ledger-round2.tsv)
- [`kelly-source-revision-chain-2026-08-17.md`](kelly-source-revision-chain-2026-08-17.md)

High-value consequences:

1. **Kelly self-correction:** in an Aug. 1998 NEN letter Don Kelly explicitly says an early `Magnets` depiction with twin horseshoe magnets/windings close to the twin electrostatic discs was later shown incorrect. This is an author-level correction of Kelly-derived geometry, not a statement that no named Testatika variant ever contained horseshoe magnets.
2. **`Magnets` chronology remains unresolved:** the official `raum&zeit` archive says its reproduced Kelly electro-schematic came from a Kelly `Magnets` article in Aug. 1987, while Kelly's 1998 retrospective dates the erroneous early study to roughly 1984. Until the original issues are acquired, these are not silently treated as the same article.
3. **M5a publication text:** the L. L./Rorschach 17-Mar-1984 witness report in Nieper's book supports the existing ~110 × 45 × 60 cm, ~20 kg, twin ~45-cm-disc, 50-position, ~60-rpm geometry line. Its neutron/tachyon/resonance explanations remain witness interpretation. Its strong similarity to Schneider/Weber M5 means source independence is still unresolved.
4. **Kelly 1998 prototype:** NEN reports that Kelly's Space Energy Association was building a prototype. No validated success result was found. `building` must never be rewritten as `replicated successfully`.
5. **Sarah Tripp documentary:** authoritative film catalogues identify a 20-min `Testatika` documentary and an archival route through the National Library of Scotland. Catalogues disagree between 2001 and 2002, so the date remains a catalogue conflict until the archive object is inspected.
6. **Digital-forensics leads:** the historic `colossus2` Testatika directory and `phoenix.oulu.fi/pub/free_energy` FTP tree are now explicit acquisition targets; surviving forum copies prove URL history, not technical truth.
7. **Patent-search boundary:** a targeted public patent search did not identify a provenance-secure Testatika/Methernitha patent. Unrelated inventors named Paul Baumann are an identity-confound. This is a bounded negative search result, not proof that no patent or filing can exist.

Round 2 does not recover the hidden circuit, crystal material, M2 through-disc route or M6a node map. Those remain UNKNOWN.'''
)

append_block(
    "docs/REPLICATION_STATUS.md",
    "## Internet crawl round 2 provenance guard",
    r'''## Internet crawl round 2 provenance guard

The 2026-08-17 Round-2 crawl adds a specific warning for M2 historical reconstruction:

- Don Kelly later self-corrected an early Kelly-derived Testatika depiction that put twin horseshoe magnets/windings close to the twin discs. Therefore a Kelly schematic cannot override direct M2 Marinov/photo/video evidence.
- This does **not** remove the source-supported M2 magnet positions already present in V4; it only prevents an obsolete Kelly placement from being imported as corroboration.
- `Magnets` items from circa 1984?, Aug. 1987 and Dec. 1988 remain separate source objects until original pages prove their relationship.
- No Round-2 source closes the M2 node-to-node circuit, exact through-disc route, pot electrical internals or crystal identity.

Accordingly the V4 physical baseline remains unchanged by Round 2.'''
)

append_block(
    "docs/M6_REPLICATION_STATUS.md",
    "## Internet crawl round 2 — M6 provenance guard",
    r'''## Internet crawl round 2 — M6 provenance guard

Round 2 strengthens source separation rather than changing the M6a CAD baseline:

- Kelly's 1998 self-correction explicitly downgrades an early Kelly-derived horseshoe-magnet-near-disc depiction. It must not be used as an M6a geometry authority.
- Hauser's direct 1986/1988 source line remains the construction anchor for M6a.
- The L. L./Nieper 17-Mar-1984 machine is retained as M5a because it may be the same object/source family as Schneider/Weber M5 and is not proven to be Hauser M6a.
- Kelly/SEA prototype construction reported in 1998 is replication-history evidence only; a successful result has not been recovered.
- No new source closes the three-grid-cylinder node map, top-crystal electrical function, original speed-control transmission or hidden historical buses.

No M6 V1 STEP/STL geometry is silently altered by these provenance findings.'''
)

append_tsv_rows(
    "docs/research/evidence_matrix.tsv",
    [
        "Kelly frühe Magnetplatzierung selbst korrigiert\tDon Kelly, NEN Aug 1998\tFrühe Magnets-Darstellung mit zwei Hufeisenmagneten/Wicklungen nahe den Zwillingsscheiben sei später als falsch erkannt worden\thoch für Kelly-Selbstkorrektur / nicht universell für alle Maschinen\tKelly-nahe-Scheiben-Geometrie nicht als M2/M6-Baseline verwenden; direkte Marinov/Hauser-Evidenz bleibt separat",
        "Kelly Magnets Datierungskonflikt\traum&zeit Publisher 1989 + Kelly NEN 1998\traum&zeit nennt Aug 1987; Kelly nennt rückblickend frühe Studie um 1984\tCONFLICT für Publikationsidentität\tOriginalhefte getrennt beschaffen; nicht zu einer Quelle verschmelzen",
        "M5a 17-März-1984 Geometrie\tL. L. Rorschach in Nieper 1985\t~110x45x60 cm, ~20 kg, zwei ~45-cm Acrylscheiben, 50 Gitter/Sektorpositionen, ~60 rpm, verstellbare Gitterabnehmer, ~10-cm Zentralscheibe\tmittel-hoch als publizierter direkter Augenzeugenbericht / Identität zu M5 ungeklärt\tals M5a getrennt; nicht automatisch M6a-CAD übertragen",
        "M5/M5a Quellenunabhängigkeit\tSchneider/Weber 13.3.1984 vs L.L. 17.3.1984\tnahezu gleiche Abmessungen und Demoangaben trotz vier Tagen Datumsabstand\tCONFLICT/DEPENDENCY-UNKNOWN\tnicht als zwei unabhängige Bestätigungen zählen; Originalnotizen/Fotos priorisieren",
        "Kelly SEA Nachbau 1998\tNew Energy News Vol 6 No 6 Nov 1998\tSpace Energy Association baue einen Swiss-M-L-Converter-Prototyp; kein validiertes Ergebnis im gefundenen Text\thoch für Bauankündigung / unbekannt für Ergebnis\tReplication-history only; niemals als erfolgreicher Nachbau bezeichnen",
        "Sarah-Tripp-Dokumentarfilm Archivspur\tBritish Council + European Film Gateway/National Library of Scotland\t20-min Testatika-Dokumentarfilm, Cineworks; Katalogjahr 2001/2002 widersprüchlich\thoch für Existenz/Archivroute / ungeprüft für Technik\trechtmäßig beschaffen und frame-auditen; bis dahin keine CAD-Übertragung",
        "Colossus2/phoenix digitale Provenienz\tBönisch 2003 + erhaltene 2003 Forum-URLs\thistorische Testatika-Web/FTP-Pfade sind konkret rekonstruierbar\tmittel-hoch für URL-Provenienz / niedrig für Inhaltswahrheit\tArchive/FTP-Snapshots suchen, hashen, deduplizieren; Claims upstream zuordnen",
        "Testatika Patent-Suche 2026-08-17\tgezielte öffentliche Patent-/Websuche\tkein provenance-sicheres Testatika/Methernitha-Patent gefunden; Namensgleichheit Paul Baumann erzeugt Fehlhits\tNEGATIVE SEARCH / begrenzt\tkeine Patentgeometrie importieren; Nichtfund nicht als Nichtexistenzbeweis verwenden",
    ],
)

append_tsv_rows(
    "docs/research/source-acquisition-backlog.tsv",
    [
        "P0-MAGNETS-1984\tPossible Kelly Magnets Testatika item circa 1984\tKelly NEN Aug 1998 refers retrospectively to an early Magnets study around 1984\tDetermine whether this is distinct from the Aug-1987 article and identify the self-corrected diagram\tAcquire original issue/article with cover/date/pages; compare figure-by-figure with Aug-1987 and Dec-1988 items\tOPEN",
        "P1-TRIPP-NLS\tSarah Tripp Testatika archival copy / catalogue record\tEuropean Film Gateway points to National Library of Scotland; British Council lists Cineworks 20-min film\tPotential independent 2001/2002 video/interview imagery\tObtain lawful archive viewing/reference identifier; preserve catalogue metadata; frame-audit before technical use\tOPEN",
        "P1-NEN-1998-KELLY\tKelly/SEA 1998 prototype build outcome\tNEN Vol6 No6 Nov1998 says prototype was being built\tDetermine whether project reached operation/test and recover actual measurements\tRequire dated Kelly/SEA project report, photos or test data; build announcement alone is not success\tOPEN",
        "P1-EINSIEDELN-HOLDING\tLibrary/archive holding of 1989 Einsiedeln SAFE proceedings\tEngeler/Müller/Rusterholz bibliography + ISBN 3-9520025-1-8\tCould recover exact official Methernitha soundtrack-transcription pages\tLocate institutional catalogue/physical copy; scan title/copyright/TOC plus Methernitha pages with page identifiers\tOPEN",
    ],
)

append_block(
    "STATE.md",
    "## Internet audit round 2 — 2026-08-17",
    r'''## Internet audit round 2 — 2026-08-17

Continuation of the verified Internet crawl is recorded in `docs/research/internet-source-audit-round2-2026-08-17.md`, `internet-source-ledger-round2.tsv` and `kelly-source-revision-chain-2026-08-17.md`.

Key state changes: Kelly early horseshoe-near-disc geometry is explicitly self-corrected/superseded by Kelly; `Magnets` 1984?/Aug-1987/Dec-1988 objects remain separate pending originals; M5a direct-published geometry is strengthened but M5/M5a independence remains unresolved; Kelly 1998 build is only a build attempt with unknown outcome; Sarah Tripp film has an NLS archive route; old colossus2/Oulu FTP paths are acquisition leads. No M2/M6 CAD baseline is changed by this round.'''
)

append_block(
    "addon.md",
    "## Internet audit round 2 handoff — 2026-08-17",
    r'''## Internet audit round 2 handoff — 2026-08-17

For future sessions, read these after the first Internet audit:

- `docs/research/internet-source-audit-round2-2026-08-17.md`
- `docs/research/internet-source-ledger-round2.tsv`
- `docs/research/kelly-source-revision-chain-2026-08-17.md`

Do not re-promote early Kelly schematic magnet placement: Kelly himself later called the early close-to-disc horseshoe-magnet depiction incorrect. Preserve the unresolved 1984-vs-1987 `Magnets` chronology. Treat M5/M5a as possible same-machine/source-dependent witness lines. Continue acquisition of original `Magnets`, DIFØT, Einsiedeln proceedings, Sarah Tripp/NLS film and Yahoo archive before claiming further historical closure.'''
)

append_block(
    "CHANGELOG.md",
    "### Internet source audit round 2 — 2026-08-17",
    r'''### Internet source audit round 2 — 2026-08-17

- added second verified Internet-source audit and ledger;
- documented Don Kelly's 1998 self-correction of an early horseshoe-near-disc Testatika depiction;
- preserved the unresolved `Magnets` circa-1984 vs Aug-1987 publication chronology instead of conflating sources;
- strengthened M5a 17-Mar-1984 publication provenance while retaining M5/M5a source-dependency warning;
- recorded Kelly/SEA 1998 prototype construction as an attempt with unknown outcome;
- added Sarah Tripp/National Library of Scotland archival acquisition route;
- added colossus2/Oulu FTP digital-forensics leads and bounded negative patent-search result;
- no historical CAD baseline changed in this audit round.'''
)

print("Internet source audit round 2 integrated idempotently.")
