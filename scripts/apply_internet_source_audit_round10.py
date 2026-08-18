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
    "## Internet source audit round 10 — 2026-08-18",
    r'''## Internet source audit round 10 — 2026-08-18

Canonical Round-10 records:

- [`internet-source-audit-round10-2026-08-18.md`](internet-source-audit-round10-2026-08-18.md)
- [`internet-source-ledger-round10.tsv`](internet-source-ledger-round10.tsv)

High-value consequences:

1. **Sauder/Snicker tuning relay (H2):** an anonymized 1999 correspondence extract says two engineers who measured earlier converters found the top element to be a solenoid-like device with a movable jumper/contact rather than a normal rectifier, and that Baumann had to retune it after they partially dismantled and inspected a machine. The same source warns their observation/memory was imperfect. This is a strong acquisition/tunable-impedance lead, not recovered M2 hardware.
2. **L. L. 17-Mar-1984 witness wording (W1/I1):** the ~45-cm twin-disc machine is described as synchronized by magnetic impulses, with strong horseshoe magnets said to be parts of electrical resonance circuits involved in charging. This historicizes a magnet/resonance interpretation for M5a; it does not override Marinov's no-Tesla/no-AC small-machine line.
3. **Layered foundation-plate relay (H2):** Hauser's expanded report says other visitors described the thick wooden base as alternating perforated and insulating layers. Treat the large-machine base as a possible capacitive/field node in experiments, not as established hidden source hardware.
4. **Cathomen magnetized pickups (O1/P1):** in the workshop transcript Cathomen identifies the structures as `Abnehmer` and answers yes when asked if they are also magnetized. Keep this workshop-specific.
5. **Cathomen reduced-pressure/condenser component (O1/P1 with interviewer framing):** `Vakuum ist es noch nicht`; the discussed part is tied to a condenser. A reduced-pressure/nonlinear switch is a testable candidate, not a proven thermionic tube or energy source.
6. **Potter vacuum-valve downgrade:** Potter's detailed thermionic-valve identification remains photo back-engineering. Across variants, closer sources include an open/non-evacuated rectifier interpretation and Cathomen's not-full-vacuum wording; no universal vacuum-tube identity is source-secure.
7. **Dry ≠ cold:** low humidity is source-supported; `cold` as an independent optimum/requirement is not source-verified in this crawl.
8. **Cathomen interviewer identity:** public transcript names only M/D/T, while archive metadata says `Dieter Dienst speaking with Luzi Cathomen`. Earlier project-side `D = Stefan Hartmann` is therefore CONFLICT/unresolved; use `D`/`interviewer` until a timestamped identity bridge exists.

Cross-source convergence now justifies a **large/workshop-family** research hypothesis of magnetically biased/timed pickup → tunable L/C impedance/resonance conditioning → nonlinear commutation → Leyden storage. It is not an M2 historical baseline and does not identify the bulk-energy source.'''
)

append_block(
    "docs/REPLICATION_STATUS.md",
    "## Internet crawl round 10 — resonance/top-stage boundary",
    r'''## Internet crawl round 10 — resonance/top-stage boundary

Round 10 strengthens several **non-M2** conditioning-stage leads but adds no contrary primary evidence against the current M2 boundary:

- a Sauder/Snicker H2 relay describes an unresolved-machine top element as a tunable solenoid/jumper requiring retuning after partial disassembly;
- the 17-Mar-1984 L. L. witness report explicitly links strong horseshoe magnets to electrical resonance circuits in the M5a twin-disc machine;
- Cathomen's workshop line says pickups are magnetized and describes a not-full-vacuum condenser-associated component;
- Hauser relays a possible layered conductive/insulating foundation plate for a large machine.

These are retained as **cross-machine experimental variants only**. Marinov's direct small-machine statement rejecting Tesla coils/AC remains the M2 historical baseline. No M2 top-stage resonance circuit, magnetized pickup, reduced-pressure tube or layered base is promoted to historical fact.

The new material does strengthen one diagnostic priority: treat environment/base/rear coupling and the top-module impedance/phase state as separately measurable ports while maintaining a closed energy ledger.'''
)

append_block(
    "docs/M6_REPLICATION_STATUS.md",
    "## Internet crawl round 10 — tunable conditioning and base-node leads",
    r'''## Internet crawl round 10 — tunable conditioning and base-node leads

Round 10 adds three model-relevant but still non-authoritative leads for larger/workshop machines:

- **M5a witness interpretation:** a 17-Mar-1984 report reproduced by Nieper says the ~60-rpm discs are synchronized by magnetic impulses and describes strong horseshoe magnets as parts of electrical resonance circuits involved in charging.
- **M6/unspecified H2 tuning relay:** Sauder/Snicker are said to have seen a solenoid-like top element with movable tuning contact; Baumann allegedly had to retune it after their partial disassembly. Original engineer records are still missing.
- **M6a base H2:** Hauser relays reports from other visitors that the thick wooden foundation plate alternated perforated conductive and insulating layers.

These justify reversible `tunable impedance/resonance` and `active-base/dummy-base` experiment variants for large-family mechanism studies. They do not overwrite Hauser's direct M6a geometry, do not establish the exact node map, and do not constitute evidence of anomalous energy.'''
)

append_block(
    "docs/research/hartmann-overunity-cathomen-audit.md",
    "## Round-10 provenance correction — interviewer identity and exact component lines",
    r'''## Round-10 provenance correction — interviewer identity and exact component lines

The earlier project-side mapping `D = Stefan Hartmann` must no longer be treated as settled. The public transcript itself labels only `M`, `D`, and `T`, whereas repository-archived RealMedia metadata explicitly describes `testa01.ram` as `Dieter Dienst speaking with Luzi Cathomen` and identifies Dieter Dienst as author in the 2001 media line. Until voice/timestamp/credit continuity is established, use **`D` / `interviewer`** for the transcript and classify the person mapping as **CONFLICT / unresolved**.

Round-10 source wording also tightens two technical points:

- Cathomen identifies the non-contact structures as `Abnehmer`; when the interviewer asks `Auch wieder magnetisiert?`, Cathomen answers `Ja.` This is workshop-machine evidence for magnetized pickups, not an M2 fact.
- For the separate front component, `Funkenstrecke`, `Vakuum` and `luftleer` are prompted by the interviewer. Cathomen's stronger direct wording is `Vakuum ist es noch nicht`, followed by the statement that the part `hängt mit einem Kondenser ... drauf`. Therefore a reduced-pressure/nonlinear-switch hypothesis is permissible, but a sealed thermionic vacuum-tube identification is not established.

These corrections preserve speaker provenance and prevent interviewer terminology from being promoted into operator-authored engineering facts.'''
)

append_block(
    "STATE.md",
    "## Internet audit round 10 — 2026-08-18",
    r'''## Internet audit round 10 — 2026-08-18

Round 10 is recorded in `docs/research/internet-source-audit-round10-2026-08-18.md` and `internet-source-ledger-round10.tsv`.

New high-value leads: (1) Sauder/Snicker H2: unresolved-machine top element allegedly a movable-jumper solenoid/variable-inductor-like part, retuned by Baumann after partial disassembly; (2) L. L. 17-Mar-1984 W1/I1: M5a discs synchronized by magnetic impulses and strong horseshoe magnets described as parts of electrical resonance circuits; (3) Hauser H2: large-machine wooden base allegedly contains alternating perforated/insulating layers; (4) Cathomen O1/P1: workshop pickups explicitly described as magnetized; (5) separate Cathomen component: `Vakuum ist es noch nicht` and condenser-associated, supporting only a reduced-pressure/nonlinear-switch candidate; (6) `cold` is not source-verified independently of dry/low-RH operation; (7) Cathomen transcript interviewer identity is now CONFLICT because archive metadata names Dieter Dienst while the public transcript does not name D.

Cross-source consequence: a tunable magnetically biased L/C conditioning/commutation stage is now a higher-priority **large/workshop-family hypothesis**, but no resonance/top-stage hardware is added to the M2 historical baseline and no bulk-energy source is claimed.'''
)

append_block(
    "addon.md",
    "## Internet audit round 10 handoff — 2026-08-18",
    r'''## Internet audit round 10 handoff — 2026-08-18

Read `docs/research/internet-source-audit-round10-2026-08-18.md` and `internet-source-ledger-round10.tsv` before changing the top-stage, magnet or environment model.

Do not promote the Sauder/Snicker tuning story above H2; do not move the 1984 M5a resonance wording into M2; do not call Cathomen's condenser-associated component a proven vacuum tube; do not historicize `cold air` as required. Use `D/interviewer`, not `Hartmann`, for the workshop transcript until the Dieter-Dienst/Hartmann speaker conflict is resolved.'''
)

append_block(
    "CHANGELOG.md",
    "### Internet source audit round 10 — 2026-08-18",
    r'''### Internet source audit round 10 — 2026-08-18

- added the Sauder/Snicker H2 retuning-after-partial-disassembly account and its self-stated memory limitations;
- added the 17-Mar-1984 L. L. witness wording linking magnetic impulses and horseshoe magnets to electrical resonance circuits on M5a;
- added the Hauser-relayed layered foundation-plate lead without promoting it to observed construction;
- added Cathomen's explicit magnetized-pickup answer and not-full-vacuum/condenser-associated component wording;
- kept Potter's vacuum-valve model as back-engineering rather than recovered hardware;
- corrected `dry` versus unverified `cold` historical operating claims;
- downgraded `D = Stefan Hartmann` to unresolved speaker-identity conflict against Dieter Dienst archive metadata;
- strengthened a reversible large/workshop tunable-conditioning hypothesis without changing the M2 historical baseline.'''
)

append_tsv_rows(
    "docs/research/baumann-statements.tsv",
    [
        "C010\tLuzi Cathomen\tdirect amateur-video transcript\tlarge/workshop machine\tO1/P1\tNon-contact pickup structures are identified as Abnehmer; asked whether they are also magnetized, Cathomen answers yes\tmagnetically biased non-contact capacitive pickup / spatial phase structure\tmedium-high for workshop statement; transcript/object mapping caveat\tmeasure remanence/B-field and capacitive pickup separately; never transfer automatically to M2",
        "C011\tLuzi Cathomen\tdirect amateur-video transcript\tlarge/workshop machine\tO1/P1 with interviewer framing\tFor a front component Cathomen says 'Vakuum ist es noch nicht' and that it is connected with a condenser; spark-gap/vacuum/airless terms are prompted by interviewer\treduced-pressure gas-discharge or nonlinear HV switching candidate\tmedium; exact internal function withheld\ttest only as reversible reduced-pressure/nonlinear surrogate; do not claim thermionic tube or vacuum-energy source",
        "L001\tL. L., Rorschach\t17-Mar-1984 witness report reproduced by Nieper 1985\tM5a\tW1/I1\t~60-rpm discs described as synchronized by magnetic impulses; strong horseshoe magnets described as parts of electrical resonance circuits involved in charging discs\tmagnetically biased/timed resonant conditioning hypothesis for M5a\tmedium-high for preserved witness wording; low-medium for causal interpretation\tlarge-machine hypothesis only; do not override Marinov M2 no-Tesla/no-AC line",
        "S001\tSauder/Snicker\tengineers -> anonymous letter writer -> web preservation\tunspecified earlier M-L converter\tH2\tTop allegedly a solenoid-like element with movable jumper/contact; Baumann allegedly retuned it after S&S partially disassembled and inspected a machine\ttunable inductance/impedance/phase-setting lead\tlow-medium; original engineer records absent and relay warns memory was imprecise\tacquire originals; reversible test variant only; never M2 baseline fact",
        "S002\tSauder/Snicker\tengineers -> anonymous letter writer -> web preservation\tunspecified earlier M-L converter\tH2/CONFLICT\tEarlier large jars/pots allegedly plastic containers filled with aluminium lathe shavings\tpossible distributed granular electrode/capacitor variant\tlow; conflicts with stronger Marinov small-machine pot description\tdo not transfer to M2; retain only as machine-unresolved acquisition lead",
        "H005\tAlbert Hauser / other visitors\texpanded Hauser report relaying other-visitor reports\tM6a/large family\tH2\tThick wooden foundation plate allegedly alternated perforated conductive plates and insulating plates\tdistributed capacitive/field-forming base-node candidate\tlow-medium; hidden base not directly inspected by Hauser\tactive-base vs inert-base control for large-family tests; no M2 transfer",
        "A001\tAlbert Hauser relaying Baumann\tlater Hauser retrospective\tlarge-family retrospective\tH1/H2\tBaumann reportedly said machine would not work in space because atmospheric charged ions are collected/sorted; closed doors/windows stop and opening a window restarts; storms avoided\tenvironmental coupling/operator-source hypothesis\tmedium for Hauser retrospective wording; low for physical explanation\tmeasure RH, air exchange, ion concentration, E/B/RF and base/rear currents; do not assume ordinary ions supply claimed power",
    ],
)

append_tsv_rows(
    "docs/research/evidence_matrix.tsv",
    [
        "Sauder/Snicker top-stage tuning relay\tRob Kalmeijer preservation of anonymized letter dated 10-Mar-1999\tS&S allegedly measured earlier converters; top described as solenoid with movable jumper/contact and Baumann retuned after partial disassembly\tH2 / ACQUISITION LEAD\ttunable-L/impedance/phase experimental variant; original report/photos required before historical promotion",
        "Sauder/Snicker aluminium-shavings pots\tRob Kalmeijer preservation of anonymized letter dated 10-Mar-1999\tearlier pots allegedly plastic containers filled with aluminium lathe shavings\tH2 / CONFLICT\tmachine unresolved; conflicts with direct Marinov small-pot grid+plastic+Cu-spiral description; never M2 baseline",
        "M5a horseshoe-magnet resonance wording\tL. L. Rorschach 17-Mar-1984 report reproduced by Nieper 1985\t~60-rpm synchronization by magnetic impulses; horseshoe magnets described as parts of electrical resonance circuits involved in disc charging\tW1/I1\tlarge-machine resonant-conditioning hypothesis only; not proof of energy source and not M2",
        "M6a layered foundation-base relay\tHauser expanded report / other-visitor relay\tthick wooden foundation plate allegedly alternated perforated conductive and insulating layers\tH2\tinstrument base capacitance/displacement current; active-vs-inert dummy base control; do not claim hidden original without source",
        "Cathomen magnetized pickups\t2001 workshop transcript + archive video provenance\tCathomen identifies Abnehmer and answers yes to 'Auch wieder magnetisiert?'\tO1/P1 workshop-specific\tseparate magnetic remanence/B-map from capacitive pickup; no M2 transfer",
        "Cathomen reduced-pressure condenser component\t2001 workshop transcript\t'Vakuum ist es noch nicht'; component associated with condenser; spark-gap/vacuum wording initially interviewer-prompted\tO1/P1 + framing caveat\treduced-pressure/nonlinear switch surrogate only; no thermionic/vacuum-energy claim",
        "Cold-air requirement\tRound-10 public-source crawl against Marinov/institutional dry-air line\tlow humidity is supported; no reliable historical source recovered for cold itself as independent requirement\tNOT SOURCE-VERIFIED\tcontrol RH and temperature independently; do not encode cold as historical operating rule",
        "Cathomen interviewer identity\tpublic M/D/T transcript vs archived testa01/testa02 metadata\ttranscript does not name D; media metadata identifies Dieter Dienst speaking with Luzi Cathomen / Dieter Dienst author\tCONFLICT\tuse D/interviewer until timestamped identity bridge resolves Hartmann-vs-Dienst mapping",
    ],
)

append_backlog(
    [
        "P0\tOriginal Sauder/Snicker Testatika measurement/dismantling records\t1999 anonymized relay says they measured earlier converters and partially disassembled one\tCould directly verify movable-jumper solenoid, tuning requirement, machine identity and component values\tIdentify engineers; acquire signed notes, photos, schematics, measurement logs or correspondence; hash and provenance-audit\tOPEN",
        "P0\tOriginal March-10-1999 Sauder/Snicker relay letter with metadata\tWeb page heading says correspondence received March 1998 while embedded letter says March 10 99\tResolve date/transmission chain and recover deleted context identifying machine/engineers\tAcquire full letter/email headers/envelope and compare to web transcription\tOPEN-CONFLICT",
        "P0\tOriginal L. L. Rorschach 17-Mar-1984 witness report\tNieper 1985 reproduces report with explicit horseshoe-magnet/electrical-resonance wording\tCould determine whether resonance sentence is witness inference, Baumann explanation or edited Nieper framing\tAcquire original typed/manuscript report and publication proof; compare exact wording\tOPEN",
        "P1\tOriginal visitor reports behind Hauser layered-foundation statement\tHauser says other visitors described alternating perforated/insulating layers in thick wooden base\tCould confirm or falsify electrically active base architecture\tIdentify cited visitors/publications; acquire original notes/photos and machine identity\tOPEN",
        "P0\tTimestamp/object lock for Cathomen reduced-pressure component and magnetized pickups\tPublic transcript gives exact wording but testa01/testa02 contain multiple machines\tRequired before geometry/function can be assigned to a specific M7/M8/M9/M10 object\tSynchronize German audio, transcript and frames; record timestamp, object ID and visible connections\tOPEN",
        "P0\tDirect top-module electrical characterization from any surviving original\tCross-source leads now include 2/4 leads, crystals, coil, tunable jumper and possible reduced-pressure switching\tWould sharply distinguish diode/crystal, inductor/resonator and gas-switch hypotheses\tObtain terminal map, continuity, L(x), C, Q/f0, B-field, pressure/gas and I-V without destructive assumptions\tOPEN",
    ]
)

print("Internet source audit round 10 integrated idempotently.")