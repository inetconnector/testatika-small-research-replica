#!/usr/bin/env python3
"""Integrate stronger primary/publication findings discovered during the 2026-08-17 web audit."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel, text):
    (ROOT / rel).write_text(text, encoding="utf-8", newline="\n")


def append_once(rel, marker, block):
    text = read(rel)
    if marker not in text:
        text = text.rstrip() + "\n\n" + block.strip() + "\n"
        write(rel, text)


append_once(
    "docs/research/source-basis.md",
    "## Primary-publication addendum: Kelly/Bailey 1991 and March-1984 witness lines",
    """
## Primary-publication addendum: Kelly/Bailey 1991 and March-1984 witness lines

See [`internet-source-audit-addendum-2026-08-17.md`](internet-source-audit-addendum-2026-08-17.md) and [`witness-source-independence-1984.md`](witness-source-independence-1984.md).

### Kelly/Bailey 1991 — evidence limit stated by the authors

The original 26th-IECEC paper is publicly available. Kelly and Bailey explicitly state that their real evidence consisted of **documents from researchers plus a videotape**, and that duplication attempts known to them had been unsuccessful. Their large-disc diameter is estimated from photographs; their later sections openly label multiple component functions as conjectural/thought/surmised. Their own `Solicited Opposing Views` section also warns that lamp/heater incandescence under HV/HF conditions is not a reliable average-power measurement.

Therefore:

- Kelly/Bailey is **P0 as a publication about what Kelly/Bailey claimed**, but remains **S2/photo-derived for original Testatika geometry/function**;
- Kelly's ~20–24-inch disc estimate and six-pickup interpretation cannot override direct Hauser/Marinov source material;
- `flux enhancement`, `electron cascading`, Searl/Ecklin and related mechanisms remain interpretation/hypothesis, not historical baseline.

### March 1984 source-independence warning

The Inge Schneider/Hans Weber 13-Mar-1984 account and the L. L. Rorschach 17-Mar-1984 report reproduced by Nieper describe nearly identical dimensions, materials, central rainbow disc, startup and output demonstration. They may describe the same object and/or share a text chain. Until original 1984 records resolve this, matching details are **not counted twice as independent corroboration**.

The L. L. report is assigned `M5a`; its air-molecule/neutron/tachyon/gravity explanations are witness theory, not observed engineering facts.

### 1999 demonstration date conflict

Retrospective public sources disagree between 5-Jun-1999 and 4-Aug-1999 for an engineer-group demonstration, while early-Aug Holzherr/Hartmann pages also carry email/translation dates. The calendar date remains **CONFLICT** pending contemporaneous invitation/attendee/photo/video evidence.
""",
)

append_once(
    "docs/research/kelly-free-energy-guide-audit-2026-08-16.md",
    "## 2026-08-17 correction from Kelly/Bailey's own 1991 IECEC paper",
    """
## 2026-08-17 correction from Kelly/Bailey's own 1991 IECEC paper

The original Kelly/Bailey conference paper has now been located at `https://www.padrak.com/ine/METHERNITHA_IECEC_1991.pdf` (26th IECEC, 1991, Vol. 4, pp. 467–472).

This materially strengthens the reason **not** to use later Kelly material as primary Testatika evidence:

- Kelly/Bailey explicitly state that their only real evidence was documents from researchers who saw/tested machines plus a videotape;
- they state that duplication attempts known to them had all been unsuccessful;
- their large-disc diameter is explicitly estimated from photographs;
- their system description is explicitly formulated from available information and includes conjectured component operation;
- they state that earlier Searl/Ecklin ideas no longer appeared applicable;
- the paper's own `Solicited Opposing Views` section challenges the crystal/magnet rectification interpretation, distinguishes Poggendorff self-start from self-running, and warns that incandescent lamps/heating wires under HV/HF conditions are unreliable average-power indicators.

Accordingly, the paper is high-quality provenance for **Kelly/Bailey's 1991 state of belief and uncertainty**, but it does not upgrade Kelly to a direct machine witness. Later Kelly/Potter/Utkin mechanism catalogs remain hypothesis/source-discovery material.
""",
)

append_once(
    "docs/REPLICATION_STATUS.md",
    "### Source-independence hardening from the 1991 IECEC / 1984 witness audit",
    """
### Source-independence hardening from the 1991 IECEC / 1984 witness audit

- Kelly/Bailey 1991 explicitly disclose that they relied on other researchers' documents and a videotape; Kelly geometry remains photo-derived/secondary and does not close M2 dimensions or wiring.
- Two March-1984 large-machine witness texts (`M5`, `M5a`) are strikingly similar and are not counted as independent confirmations until their source relationship is resolved.
- Neither witness lamp/heater demonstrations nor the Kelly/Bailey retelling provide a closed energy balance.
""",
)

append_once(
    "docs/M6_REPLICATION_STATUS.md",
    "## Additional large-family source separation from March 1984 and Kelly/Bailey 1991",
    """
## Additional large-family source separation from March 1984 and Kelly/Bailey 1991

- `M5` (Schneider/Weber, 13-Mar-1984) and `M5a` (L. L. Rorschach report dated 17-Mar-1984) are separate documentary IDs because source independence and exact object identity are unresolved. Both describe ~1.1-m-wide apparatuses and therefore are not silently folded into Hauser's later ~500-mm-disc M6a reconstruction.
- Kelly/Bailey 1991 is not a direct-observer source. Their disc-size/pickup/component descriptions are explicitly based on available reports/photos/video and contain conjecture. They cannot override Hauser direct-visit scans.
- The M6a V1 CAD remains unchanged by this addendum.
""",
)

# Append evidence-matrix rows without duplicating them.
p = "docs/research/evidence_matrix.tsv"
t = read(p).rstrip("\n")
rows = [
    "Kelly/Bailey 1991 evidence boundary\tKelly & Bailey 26th IECEC original paper\tauthors say only real evidence = visitor documents + videotape; known duplication attempts unsuccessful\tP0 for author statement / S2 for machine evidence\tKelly geometry/function cannot override direct witness/scan evidence",
    "Kelly/Bailey photo-estimated large discs\tKelly & Bailey 1991\tdiscs estimated from photographs at ~20-24 inches\tPHOTO-DERIVED / secondary\tnot a measured original dimension",
    "Kelly/Bailey opposing power view\tKelly & Bailey 1991 Solicited Opposing Views\tlamp/heater incandescence under HV/HF conditions called suspect as average-power indicator\tCONTROL/METHODOLOGY\trequires true synchronized V-I/energy balance",
    "M5 Schneider-Weber 13-Mar-1984\tSchneider 1994 account republished NET-Journal 2011\t>1m x45x60cm, ~20kg no cover, acrylic/light-metal grid/Cu conductors, non-contact pickup, hand-start twin discs, ~10cm rainbow disc\tW1/P1 republished witness account\tseparate M5; output figures/demo not closed metrology",
    "M5a L.L. Rorschach 17-Mar-1984\tWitness report reproduced in Nieper 1985\t~110x45x60cm, 20kg, twin ~45cm discs, 50 fan-like grid positions, ~60rpm, magnetic synchronization, ~10cm rainbow disc\tW1/P1 book reproduction\tseparate M5a; identity/source independence vs M5 unresolved",
    "M5/M5a source independence\tcomparison of two March-1984 published accounts\tphysical dimensions, terminology and demo sequence are unusually similar\tCONFLICT/DEPENDENCY UNKNOWN\tdo not count matching details as two independent measurements",
    "1999 engineer demo date\t2004 seminar vs 2011 NET-Journal vs Holzherr/Hartmann web dates\t5-Jun-1999 versus 4-Aug-1999/early-Aug publication chain\tCONFLICT\tretain date conflict until contemporaneous event record acquired",
    "M0 flattened hemisphere base\tRimstar preservation of additional correspondence\tbase below swinging arm described as flattened hemisphere / half electric bell\tH1/H2 geometry lead\toptional M0 geometry candidate only; original correspondence required for promotion",
    "M0 capacitor dimensions\tRimstar preservation of additional correspondence\ttwo capacitors approximately 8cm high and 3-4cm diameter\tH1/H2 geometry lead\tworking-fit lead, not primary measurement",
    "Methernitha 2010 later status\tNET-Journal recipient-side publication of reply\tresearch group no longer existed; Thestatika no longer shown; Internet entries without their knowledge\tH1/P1 correspondence reproduction\tprovenance warning only, not engineering evidence",
]
for row in rows:
    key = row.split("\t", 1)[0]
    if key not in t:
        t += "\n" + row
write(p, t + "\n")

# Add acquisition and audit references to handoff files.
block = """
## Primary-publication web-audit addendum 2026-08-17

New stronger sources: Kelly/Bailey 1991 original IECEC PDF; Nieper 1985 book mirror including the L. L. Rorschach 17-Mar-1984 witness report; Schneider/Weber 13-Mar-1984 account republished by NET-Journal; recipient-side publication of a 2010 Methernitha reply. See `docs/research/internet-source-audit-addendum-2026-08-17.md` and `witness-source-independence-1984.md`.

Do not double-count M5 and M5a as independent until source dependence is resolved. Kelly/Bailey explicitly were not direct machine witnesses and their geometry is secondary/photo-derived. The 1999 engineer-demo date is CONFLICT (5 Jun vs 4 Aug / early-Aug publication chain). No hidden original circuit or closed historical net-energy proof was found.
"""
for p in ("STATE.md", "addon.md"):
    text = read(p)
    if "## Primary-publication web-audit addendum 2026-08-17" not in text:
        write(p, text.rstrip() + "\n\n" + block)

# Changelog.
p = "CHANGELOG.md"
t = read(p)
marker = "### Added — primary-publication source hardening (2026-08-17)"
if marker not in t:
    anchor = "## Unreleased — V4 best-evidence build + archive/primary-source expansion\n"
    block = """

### Added — primary-publication source hardening (2026-08-17)

- located and audited the original Kelly/Bailey 1991 IECEC paper; its own evidence limitations, failed-replication statement, photo-derived dimensions and solicited opposing views are now canonical;
- located the relevant Nieper 1985 book pages and separated the `L. L., Rorschach` 17-Mar-1984 witness report as `M5a`;
- strengthened the Schneider/Weber `M5` 13-Mar-1984 line from the 2011 republication of Schneider's 1994 account;
- added an explicit M5/M5a source-independence matrix to prevent duplicate corroboration;
- preserved the 1999 engineer-demonstration date conflict rather than normalizing 5-Jun and 4-Aug claims;
- added recipient-side publication of Methernitha's 2010 status reply and new M0 Principle-Experiment geometry leads;
- added exact Magnets Dec-1988 pp19-26 and Raum & Zeit 40/1989 acquisition targets.
"""
    if anchor not in t:
        raise SystemExit("missing changelog anchor")
    t = t.replace(anchor, anchor + block, 1)
    write(p, t)

print("Primary-publication internet audit addendum integrated idempotently.")
