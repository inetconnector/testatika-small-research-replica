#!/usr/bin/env python3
"""Final low-risk classification additions for the 2026-08-17 Internet audit."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def r(p): return (ROOT/p).read_text(encoding='utf-8')
def w(p,s): (ROOT/p).write_text(s,encoding='utf-8',newline='\n')

def append_block(path, marker, block):
    s=r(path)
    if marker not in s:
        w(path,s.rstrip()+"\n\n"+block.strip()+"\n")

# Final audit notes.
append_block('docs/research/internet-source-audit-addendum-2026-08-17.md',
             '## J. Don Kelly replication-history lead — prototype construction reported in 1998', '''
## J. Don Kelly replication-history lead — prototype construction reported in 1998

The Institute for New Energy / *New Energy News*, Vol. 6 No. 6 (Nov. 1998), reports that Don Kelly's Space Energy Association was **building a prototype Swiss M-L converter**. This is useful replication-history evidence because Kelly/Bailey's 1991 IECEC paper had stated that all duplication attempts then known to them were unsuccessful.

No indexed source found in this crawl establishes the later outcome of the reported 1998 build. Therefore the correct statement is only: **prototype construction was reported**. Do not infer success or failure without a later project report.

Source: `https://www.padrak.com/ine/`

## K. Jan Pajak material explicitly self-downgrades as non-witness reconstruction

Jan Pajak's own monograph says he never personally saw the Thesta-Distatica and that the detailed machine he documents is a **telekinetic influenzmaschine of his own invention**, designed to correspond to information he had gathered. He also says the available details came from mixed sources, sometimes gossip, and could not all be scientifically verified.

Accordingly, Pajak drawings, dimensions, circuit details and telekinetic/UFO mechanism claims are **S2/I1 reconstruction material**, not historical Testatika geometry or wiring. They are not imported into CAD.

## L. Einsiedeln congress — live-machine versus film-only conflict

A contemporary external information sheet dated May 1990 reports that Methernitha representative Bosshard presented the Testatika to about 500 congress attendees in Einsiedeln **only by film, not in natura**. By contrast, later Testatika literature (including Kelly/Bailey's transmission of earlier claims) describes a live demonstration at a Zurich/Einsiedeln congress to a larger audience.

This is a genuine provenance conflict. It may reflect different events, later conflation, or inaccurate transmission. Until a contemporaneous congress programme, photographs or multiple date-locked reports resolve it, the repository must not state that the 1989 Einsiedeln congress definitely contained a live machine demonstration.

Contemporary source: `https://www.relinfo.ch/methernitha/testatika.html`
''')

# Append to internet source ledger.
p='docs/research/internet-source-ledger.tsv'; s=r(p).rstrip('\n')
rows=[
"WEB-028\tNew Energy News / Institute for New Energy\tNov 1998, Vol.6 No.6\thttps://www.padrak.com/ine/\tREPLICATION-HISTORY\tA1/S2\tReports Space Energy Association / Don Kelly was building a prototype Swiss M-L converter\tNo later indexed result found in this audit; construction report does not establish success or failure",
"WEB-029\tJan Pajak telekinetic-device monograph\tlater online mirror\thttps://www.scribd.com/document/420361575/15e-10\tMX/HYPOTHESIS\tS2/I1 SELF-DECLARED\tAuthor explicitly says he never personally saw Thesta-Distatica and documents a machine of his own invention based on mixed sources\tNot historical geometry/wiring evidence; telekinetic/UFO theory not imported",
]
for row in rows:
    if row.split('\t',1)[0] not in s: s+='\n'+row
w(p,s+'\n')

# Canonical evidence rows.
p='docs/research/evidence_matrix.tsv'; s=r(p).rstrip('\n')
rows=[
"Kelly 1998 prototype construction report\tNew Energy News Nov 1998\tSpace Energy Association / Don Kelly reported building Swiss M-L prototype\tA1/S2 replication-history lead\ttrack outcome separately; no success/failure inference",
"Pajak non-witness reconstruction\tJan Pajak own monograph\tauthor says never personally saw Thesta-Distatica and detailed design is his own invention\tS2/I1 self-declared\tdo not import Pajak dimensions/circuit/mechanism into historical CAD",
"Einsiedeln congress presentation mode\tRelinfo May 1990 versus later Kelly/Nieper transmission\tcontemporary external source says film-only before ~500; later literature describes live demonstration/larger audience\tCONFLICT\tdo not assert live 1989 congress machine until date-locked primary evidence resolves it",
]
for row in rows:
    if row.split('\t',1)[0] not in s: s+='\n'+row
w(p,s+'\n')

# Acquisition backlog: outcome of Kelly prototype and congress primary record.
p='docs/research/source-acquisition-backlog.tsv'; s=r(p).rstrip('\n')
rows=[
"P2\tDon Kelly / Space Energy Association 1998 prototype outcome\tNEN Vol.6 No.6 reports prototype construction\tCould determine whether a concrete Kelly replication reached testing and what was measured\tAcquire dated project report/photos/test data; never infer result from construction announcement\tOPEN",
"P1\t1989/1990 Einsiedeln SAFE congress programme/photos\tRelinfo May 1990 says film-only; later literature says live demonstration\tResolve live-machine versus film-only provenance conflict and audience/date confusion\tRequire contemporaneous programme, photographs or date-locked attendee report\tOPEN",
]
for row in rows:
    if row.split('\t',1)[1] not in s: s+='\n'+row
w(p,s+'\n')

# Canonical source-basis warning.
append_block('docs/research/source-basis.md','### Final web-audit downgrades and unresolved event conflict','''
### Final web-audit downgrades and unresolved event conflict

- NEN Nov-1998 reports that Don Kelly's group was building an M-L prototype; no indexed outcome was found, so only construction is recorded.
- Jan Pajak explicitly says he never personally saw Thesta-Distatica and that his detailed device is his own reconstruction/invention; his geometry/circuit/theory remains S2/I1.
- A May-1990 contemporary external source says the Einsiedeln congress presentation was film-only, conflicting with later live-demonstration accounts. The event mode/audience remains CONFLICT.
''')

print('Final Internet-audit classifications integrated idempotently.')
