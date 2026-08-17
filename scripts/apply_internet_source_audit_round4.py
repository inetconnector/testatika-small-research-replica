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


def append_evidence(rows: list[str]) -> None:
    p = ROOT / "docs/research/evidence_matrix.tsv"
    text = p.read_text(encoding="utf-8")
    existing = {line.split("\t", 1)[0] for line in text.splitlines() if line}
    if not text.endswith("\n"):
        text += "\n"
    changed = False
    for row in rows:
        key = row.split("\t", 1)[0]
        if key in existing:
            continue
        text += row.rstrip("\n") + "\n"
        existing.add(key)
        changed = True
    if changed:
        p.write_text(text, encoding="utf-8")


def append_backlog(rows: list[str]) -> None:
    p = ROOT / "docs/research/source-acquisition-backlog.tsv"
    text = p.read_text(encoding="utf-8")
    targets = set()
    for line in text.splitlines()[1:]:
        cols = line.split("\t")
        if len(cols) > 1:
            targets.add(cols[1])
    if not text.endswith("\n"):
        text += "\n"
    changed = False
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
    "## Internet source audit round 4 — 2026-08-17",
    r'''## Internet source audit round 4 — 2026-08-17

Canonical Round-4 records:

- [`internet-source-audit-round4-2026-08-17.md`](internet-source-audit-round4-2026-08-17.md)
- [`internet-source-ledger-round4.tsv`](internet-source-ledger-round4.tsv)

High-value provenance corrections:

1. The late claim that Marinov **received a 100-W Testatika generator in 1997** appears in Frolov 2021 but is not supported by a contemporaneous transfer source found in the crawl. Watson 2001 only relays that Baumann gave Marinov a small machine `to play with`, then explicitly says the observations were made at Linden without quantitative test gear. The ~100-W number is a resistor-heating estimate, not a recovered device rating. Treat the 1997 permanent-gift story as **unsupported late secondary / likely conflation**.
2. The 1999 engineer demonstration has an unresolved source conflict: the preserved 2004 seminar programme says **5-Jun-1999 / 34 engineers**, while the 2011 Schneider retrospective says **4-Aug-1999 / 30 Swiss engineers**. Do not normalize these.
3. The 13-Mar-2004 Zurich seminar is a strong provenance node for later theories: Hans Weber explicitly presented a `polymer-chain charge exchange during air ionization` model and the programme says his 1984 presentation used video. These are dated later interpretations, not Methernitha primary engineering.
4. The 2011 NET-Journal article reproduces a 2010 Methernitha reply as recipient-published institutional correspondence. It is stronger than a forum mirror but still not the original message/header.
5. Nuetec's parenthetical `WR: im November 1980` attached to a Marinov/Nieper statement is an editor/translator annotation. The crawl has not verified 1980 as the date Nieper had seen/tested Testatika.
6. Marinov sources give **1977 and 1978** in different retrospective/construction contexts. Preserve this as a milestone/prototype chronology issue instead of forcing one universal first-build date.
7. Hauser's publication chain is now concrete: 14-Feb-1986 visit → `DIFOT-News` no.5 May-1986 → `UFO-Contact` no.6 1986 → English version Feb-1987 → later expanded Hauser material.
8. Nuetec publicly links a 30-minute Methernitha film labelled **1280×720**, but the file has not yet been frame-audited and could be an upscale. It is an acquisition target, not new geometry evidence.

Round 4 does not justify an automatic historical CAD change.'''
)

append_block(
    "docs/REPLICATION_STATUS.md",
    "## Internet crawl round 4 — claim-conflation guard",
    r'''## Internet crawl round 4 — claim-conflation guard

The crawl explicitly rejects a common secondary-history shortcut: **`Marinov was given a 100-W Testatika in 1997` is not established by the located evidence.** Frolov 2021 makes the strong claim, but the earlier Watson transmission only says Baumann gave Marinov a small machine `to play with` and states that the observations/tests described were made at Linden without quantitative test equipment. The ~100-W figure comes from a rough resistor-heating estimate, not a nameplate/calibrated rating.

Therefore:

- no ownership/permanent-transfer state is inferred for M2 from Watson;
- no `100 W rated M2` field is added;
- the Frolov/Sapogin story remains preserved as a late secondary contradiction lead;
- V4 geometry/electrical baseline remains unchanged.

The Nuetec 1280×720-labelled film is not yet frame-audited and therefore supplies **no new M2 geometry yet**.'''
)

append_block(
    "docs/M6_REPLICATION_STATUS.md",
    "## Internet crawl round 4 — chronology and publication guards",
    r'''## Internet crawl round 4 — chronology and publication guards

Round 4 adds provenance constraints without modifying M6a CAD:

- 1999 engineer-demonstration chronology remains CONFLICT: `5-Jun-1999 / 34 engineers` in the 2004 seminar programme versus `4-Aug-1999 / 30 engineers` in a 2011 Schneider retrospective.
- Weber's 2004 `polymer-chain charge exchange during air ionization` is a later explanatory model, not recovered M6 circuitry.
- Hauser's source-publication chain is more precise (`DIFOT-News` 5/May-1986 → `UFO-Contact` 6/1986 → English Feb-1987), but original issues remain acquisition targets; direct project Hauser scans stay the numeric source of record.
- A Nuetec 1280×720-labelled Methernitha film is publicly linked but has not been source-resolution/frame compared; no M6 geometry is upgraded from it yet.

M6a V1 remains source-anchored to the direct Hauser 1986/1988 material.'''
)

append_evidence([
    "Marinov 1997 100-W Geschenkbehauptung\tFrolov 2021 vs Watson 2001 vs Marinov 1989\tFrolov behauptet 1997er 100-W-Geschenk; Watson sagt nur 'to play with' und alle Beobachtungen in Linden ohne Messgeräte; ~100 W nur Heizwirkungs-Schätzung\tUNSUPPORTED-LATE-SECONDARY / likely conflation\tnicht als M2-Eigentum, Übergabe oder Nennleistung in CAD/Status übernehmen",
    "1999 Ingenieur-Demo Datum/Teilnehmer\tJupiter-Seminarprogramm 2004 vs Schneider NET-Journal 2011\t5.6.1999/34 Ingenieure versus 4.8.1999/30 Schweizer Ingenieure\tCONFLICT\tbeide Angaben getrennt bewahren; zeitgenössischen Einladungs-/Teilnehmer-/Bildbeleg suchen",
    "Weber Polymerketten-Luftionisation\tJupiter-Seminarprogramm 13.3.2004\tHans Weber präsentierte 'Ladungsaustausch über Polymerketten bei Luftionisation' als Erklärungsmodell\thoch für Weber-2004-Theorie / niedrig für historisches Testatika-Prinzip\tnur Hypothese/Experimentlead; nicht mit Baumann/Hauser/Hartmann zu Primärmechanismus verschmelzen",
    "Methernitha Antwort 2010\tNET-Journal 2011 als Korrespondenzempfänger\tForschungsgruppe bestehe nicht mehr; Thestatika nicht mehr zeigbar; Interneteinträge ohne ihr Wissen\tmittel-hoch als recipient-published institutional correspondence\tOriginalmail/Brief weiter suchen; keine technische Funktionsaussage daraus ableiten",
    "Nieper November-1980 Zuschreibung\tNuetec WR-Annotation zu Marinov-Zitat\tWR setzt Hannover-Konferenz auf Nov 1980; direkte Marinov/Nieper Testatika-Datierung nicht gefunden\tUNVERIFIED EDITOR ATTRIBUTION\tkeinen 1980 Erstzeugen-Timeline-Fakt setzen; Original-TWT-V-Stelle/zeitgenössischen Nieper-Beleg beschaffen",
    "Testatika Baujahr 1977/1978\tMarinov 1996 retrospective + 1989 author text\t1977 für 'first functioning' in spätem Text; 1978 für die zwei fotografierten Ein-Scheiben-Maschinen; früher Hebel/Zamboni-Vorläufer\tCONFLICT/MILESTONE-SPECIFIC\tkeine einzige universelle Erstbaudatierung erzwingen; Prototypstadien getrennt halten",
    "Hauser Publikationskette 1986-1987\tHauser report mirror\t14.2.1986 Besuch; DIFOT-News 5 Mai 1986; UFO-Contact 6/1986; englische Fassung Feb 1987\thoch für Hauser-eigene Publikationsprovenienz / Mirror-Vorbehalt\tOriginalausgaben beschaffen; direkte Projekt-Scans für Zahlen weiter bevorzugen",
    "Nuetec HD-Filmquelle\tNuetec Testatika page\t30-min Methernitha-Film als 1280x720 und 640x360 verlinkt\thoch für Linkexistenz / UNKNOWN native image detail\terst Download, ffprobe/hash, Framevergleich gegen Archiv; bis dahin keine Geometrie-Hochstufung",
])

append_backlog([
    "P0\tSecret.tv recording of 13-Mar-2004 Testatika seminar\tAllmystery preserves article1527374 URL; seminar programme says Weber 1984 presentation used video\tCould recover Weber/Schneider first-person retelling and possibly embedded 1984 footage\tLocate lawful archive/video copy; hash; timestamp speakers and any inserted historical footage separately\tOPEN",
    "P0\tContemporaneous documentation for 1999 Burgdorf/Swiss-engineer demonstration\t2004 programme says 5-Jun/34; 2011 NET-Journal says 4-Aug/30\tResolve whether there were two events or a retrospective date/count error\tRequire dated invitation, attendee list, original report, photo/video metadata or signed diary/letter\tOPEN-CONFLICT",
    "P0\tOriginal source for Marinov-to-Nieper first-witness statement\tNuetec TWT-V translation page adds editor note WR: Nov 1980\tCould determine whether Nieper really reported Testatika by 1980 or at a later Hannover meeting\tAcquire exact TWT-V original-language page and any cited Nieper conference/report; separate Marinov wording from editor annotation\tOPEN",
    "P1\tOriginal 2010 Methernitha reply to NET-Journal\t2011 NET-Journal publishes recipient-side wording\tLocks institutional authorship/date and removes transcription ambiguity\tAcquire original letter/email with date/header/signature; preserve published reproduction as secondary archival proof\tOPEN",
    "P1\tDIFOT-News no.5 May 1986 / UFO-Contact no.6 1986 / English Feb 1987 Hauser chain\tHauser report mirror names all three publication steps\tCan expose editing/translation changes and additional original images\tAcquire complete issues/pages; hash and compare line/figure provenance with current Hauser scans\tOPEN",
    "P0\tNuetec 1280x720-labelled 30-minute Methernitha film\tNuetec Testatika page directly links MP4 plus 640x360 version\tPotentially higher-information visual source than 320x240/352x288 archive videos\tDownload lawfully; SHA-256; ffprobe native codec/resolution; detect upscale/re-encode; synchronized frame comparison before extracting geometry\tOPEN",
    "P1\tNuetec companion PDF corpus\tTWT_Marinov_Die_Gemeinde.pdf, revised Hauser/Kelly, Saunier response, open eyewitness correspondence linked from page\tMay contain stronger source-language scans/correspondence not yet in repository\tAcquire each file, hash, page-audit, identify author/date/transmission before promoting any claim\tOPEN",
])

append_block(
    "STATE.md",
    "## Internet audit round 4 — 2026-08-17",
    r'''## Internet audit round 4 — 2026-08-17

Round 4 is recorded in `docs/research/internet-source-audit-round4-2026-08-17.md` and `internet-source-ledger-round4.tsv`.

Key state: Frolov's `1997 100-W gift` story is classified unsupported late secondary/likely conflation; 1999 engineer demo remains 5-Jun/34 vs 4-Aug/30 conflict; 2004 Weber polymer-chain/air-ion theory is dated hypothesis only; 2010 Methernitha reply is recipient-published correspondence; Nuetec `Nov-1980` Nieper date is editor attribution and unverified; 1977/1978 construction chronology remains milestone-specific conflict; Hauser DIFOT/UFO-Contact/English transmission chain is now explicit; Nuetec 1280x720 film is a high-priority uninspected acquisition lead. No historical CAD baseline changed.'''
)

append_block(
    "addon.md",
    "## Internet audit round 4 handoff — 2026-08-17",
    r'''## Internet audit round 4 handoff — 2026-08-17

Before continuing, read `docs/research/internet-source-audit-round4-2026-08-17.md` and `internet-source-ledger-round4.tsv`.

Do not repeat as fact that Marinov received a `100-W Testatika` in 1997. The located chain does not support a permanent gift or rated output. Preserve the 1999 5-Jun/34 vs 4-Aug/30 conflict. Treat Weber's polymer-chain/air-ionization as a 2004 theory. Treat Nuetec's Nov-1980 Nieper date as editor annotation until original TWT-V/Nieper evidence is obtained. The Nuetec HD-labelled film has not yet been frame-audited.'''
)

append_block(
    "CHANGELOG.md",
    "### Internet source audit round 4 — 2026-08-17",
    r'''### Internet source audit round 4 — 2026-08-17

- classified the Frolov/Sapogin `1997 100-W Testatika gift` story as unsupported late secondary/likely conflation against Watson/Marinov source details;
- preserved the 1999 engineer-demo `5-Jun/34` versus `4-Aug/30` date/count conflict;
- added the 13-Mar-2004 seminar as a provenance node and Weber polymer-chain/air-ionization as a dated later hypothesis;
- upgraded the 2010 Methernitha response to recipient-published correspondence while keeping original message acquisition open;
- prevented Nuetec's editor-added `Nov 1980` from becoming a false Nieper/Testatika timeline fact;
- preserved 1977/1978 construction dates as prototype/milestone conflict;
- documented Hauser's DIFOT/UFO-Contact/English publication chain;
- added Nuetec HD-labelled video and companion-document corpus as acquisition targets without claiming uninspected content;
- no historical CAD baseline changed.'''
)

print("Internet source audit round 4 integrated idempotently.")
