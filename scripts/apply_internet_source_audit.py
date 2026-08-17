#!/usr/bin/env python3
"""Integrate the 2026-08-17 verified Internet source audit additively and idempotently."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel, text):
    (ROOT / rel).write_text(text, encoding="utf-8", newline="\n")


def replace_once(text, old, new, label):
    if new in text:
        return text
    if old not in text:
        raise SystemExit(f"missing patch anchor: {label}")
    return text.replace(old, new, 1)


# 1) Canonical M2 completeness corrections.
p = "docs/REPLICATION_STATUS.md"
t = read(p)
t = replace_once(
    t,
    "| rear plate / shield influence | metal-plate stop effect only through later transmission | HYPOTHESIS/H2 | low-medium | shield jig | primary source or controlled replication |",
    "| rear plate / shield influence | Marinov directly reports that a large metal plate brought behind the running small machine stopped rotation and removed the rest torque | OBSERVED | high for observation / mechanism unknown | shield jig; floating/grounded/R/C/nonconductive controls | original calibrated repetition or independent controlled replication |",
    "M2 metal plate status",
)
t = replace_once(
    t,
    "| east-west orientation | later recollection | HYPOTHESIS/H2 | low | turntable experiment only | primary source + blinded replication |",
    "| east-west startup orientation | Baumann told Marinov the small-machine axis had to point East-West for startup; Marinov reports it was positioned that way to start, while after startup he directly moved/tilted the running machine without stopping | SOURCE-STATED + OBSERVED | medium-high for startup instruction and post-start observation / cause unknown | randomized turntable startup test + separate post-start reorientation test | original-language scan + blinded controlled replication |",
    "M2 east-west status",
)
anchor = "| startup/priming procedure | hand impulse/start reported; exact electrical priming unresolved | SOURCE-STATED + UNKNOWN | medium | low-energy priming tests | original operating protocol |"
extra = anchor + "\n| dry-air startup push count | Marinov reports about 3–4 finger pushes in dry air and more under humid conditions | SOURCE-STATED/OBSERVED account | medium-high | RH-controlled equal-impulse startup protocol | original-language page + controlled replication |\n| restart history / memory | Marinov reports second/third restarts were easier after a metal-plate stop | OBSERVED account | medium | controlled discharge/rest/conditioning matrix with surface-potential logging | independent repetition / original object data |\n| small-machine running speed | roughly one revolution per second (~60 rpm) in Marinov account | OBSERVED account | medium-high / model-specific | include ~60 rpm reference without making it universal | calibrated original footage/tachometer record |"
if "| dry-air startup push count |" not in t:
    if anchor not in t:
        raise SystemExit("missing startup row anchor")
    t = t.replace(anchor, extra, 1)

# Add audit note before What complete means.
marker = "## Internet source audit 2026-08-17"
if marker not in t:
    insert = """
## Internet source audit 2026-08-17

A broad public-web source audit corrected two M2 evidence rankings and expanded the machine taxonomy. See [`research/internet-source-audit-2026-08-17.md`](research/internet-source-audit-2026-08-17.md) and [`research/internet-source-ledger.tsv`](research/internet-source-ledger.tsv).

Key canonical consequences:

- East-West is now split into **Baumann→Marinov startup instruction** and **Marinov-observed post-start orientation independence**; geomagnetic causation remains unknown.
- The rear-metal-plate stop/rest-torque effect is upgraded to a **direct Marinov observation**.
- dry-air 3–4-push startup, humidity sensitivity, easier later restarts and ~60-rpm small-machine operation are explicitly retained as model/source-specific observations.
- Marinov TWT-VII gives a two-disc thick-grid/thin-sector asymmetry and insulating sector spray, but the exact M6 variant is unresolved; it is not silently injected into Hauser M6a CAD.
- `M6c`, `M8`, `M9` and `M10` are introduced to prevent large-under-construction, 1-m, 2-m and tandem workshop evidence from contaminating M6a/M6b.
- Marinov's own coupled Wimshurst/electrostatic-motor control failed to close energetically; full torque/input/storage accounting remains mandatory.

"""
    target = "## What “complete 1:1 research replica” means here"
    if target not in t:
        raise SystemExit("missing REPLICATION_STATUS insertion target")
    t = t.replace(target, insert + target, 1)
write(p, t)


# 2) Experiment-plan corrections and new controls.
p = "docs/research/experiment-plan.md"
t = read(p)
t = replace_once(
    t,
    "## Stufe 11 — Ost-West-Test\n\nNur als H2-Prüfung:",
    "## Stufe 11 — Ost-West-Startup und Post-Start-Reorientierung\n\nQuellenstatus korrigiert: Die East-West-Anweisung ist **Baumann→Marinov SOURCE-STATED**, nicht bloß H2. Separat berichtet Marinov direkt, dass die laufende Kleinmaschine nach dem Start bewegt, gekippt und umorientiert werden konnte. Eine geomagnetische Ursache ist damit **nicht** belegt.\n\nStartup-Test:",
    "experiment east-west heading",
)
old = "- Bediener möglichst blind.\n\n## Stufe 12 — gekoppelte Forschungsvariante"
new = "- Bediener möglichst blind.\n- Startimpuls mechanisch quantifizieren/standardisieren.\n- RH und Temperatur protokollieren; trockene/feuchte Bedingungen separat randomisieren.\n- Anzahl identischer Startimpulse bis zum stabilen Lauf erfassen.\n\nPost-Start-Test separat:\n\n- erst bei definierter Referenzorientierung starten;\n- nach stabilem Lauf die gesamte Maschine auf randomisierte Azimute/Neigungen bewegen;\n- rpm, Torque, Surface Potential und Feldvektoren kontinuierlich loggen.\n\n### Stufe 11b — Restart-Memory / Zustandsabhängigkeit\n\nMarinov berichtet, dass zweite/dritte Starts nach dem Metallplatten-Stopp leichter waren. Daher vergleichen:\n\n- definierte Ruhezeit ohne Entladung;\n- kontrollierte Neutralisierung/Entladung;\n- identische RH/Temperatur;\n- Surface-Potential-Map vor/nach jedem Lauf;\n- randomisierte Reihenfolge und gleicher mechanischer Startimpuls.\n\nZiel: persistente Dielektrikum-/Oberflächenladung, Feuchtehistorie und Bedienereffekt von einer echten Orientierungsabhängigkeit trennen.\n\n## Stufe 12 — gekoppelte Forschungsvariante"
t = replace_once(t, old, new, "experiment startup memory")

# Strengthen plate controls near stage 1.
old = "- Shield floating / geerdet / R-gekoppelt / C-gekoppelt vergleichen."
new = "- Shield floating / geerdet / R-gekoppelt / C-gekoppelt vergleichen.\n- geometriegleiche nichtleitende Platte als Kontrolle; Abstand und Plattenfläche systematisch variieren.\n- Der Metallplatten-Stopp ist nun als direkte Marinov-Beobachtung eingestuft; seine Ursache bleibt offen."
t = replace_once(t, old, new, "plate control expansion")
write(p, t)


# 3) Source basis append.
p = "docs/research/source-basis.md"
t = read(p)
marker = "## Internet source audit 2026-08-17 — verified corrections and acquisition leads"
if marker not in t:
    t += """

## Internet source audit 2026-08-17 — verified corrections and acquisition leads

Canonical audit:

- [`internet-source-audit-2026-08-17.md`](internet-source-audit-2026-08-17.md)
- [`internet-source-ledger.tsv`](internet-source-ledger.tsv)
- [`control-replication-audit-2026-08-17.md`](control-replication-audit-2026-08-17.md)
- [`source-acquisition-backlog.tsv`](source-acquisition-backlog.tsv)

High-value additions/corrections:

1. Marinov direct-author material upgrades the M2 rear-metal-plate stop from H2 to direct observation and the East-West startup claim from H2 to Baumann→Marinov source-stated. Post-start orientation independence is a separate Marinov observation; mechanism remains unknown.
2. Marinov's direct account adds dry-air ~3–4 initial pushes, more pushes with humidity, easier later restarts and roughly one revolution per second for the tested small machine.
3. Marinov TWT-VII states that a two-disc Testatika had thick electrically connected grid sectors on both sides of one Plexiglas wheel and thin sectors only on the external side of the other, with insulating spray on slightly magnetized sectors. Exact machine identity is unresolved; do not retrofit M6a without a bridge.
4. Marinov's author text states that Kelly only saw photographs while Hauser examined a machine; Kelly geometry is therefore secondary/photo-derived.
5. A Marinov large-under-construction description conflicts materially with Hauser M6a cylinder internals. It is isolated as `M6c`, not averaged into one fictional machine.
6. Marinov and the later Cathomen workshop line independently support 1-m and 2-m large-scale objects; the workshop transcript also distinguishes tandem/double-converter objects (`M8`–`M10`).
7. Exact acquisition targets now include DIFØT-nyt 5/1986 and 14/1988, the official 1989 film transcript ISBN 3-9520025-1-8, the Yahoo/PG-Offline 11,284-message archive, original Weber/Schneider material and the actual Matthey/Nieper pages.
8. Conventional controls from Marinov himself and Bönisch 2003 do not show a self-closing/over-unity conventional electrostatic loop; Rimstar work adds a documented floating-source oscilloscope-ground failure mode.

The audit changes evidence ranking and experiment design. It does **not** reveal an authentic complete circuit or establish net energy creation.
"""
write(p, t)


# 4) Evidence matrix append rows.
p = "docs/research/evidence_matrix.tsv"
t = read(p).rstrip("\n")
rows = [
    "M2 East-West startup\tMarinov direct-author account / Baumann→Marinov\tBaumann told Marinov small-machine axis must point East-West for startup; machine was positioned accordingly\tSOURCE-STATED medium-high / cause unknown\tupgrade from H2; randomized azimuth startup test, no assumed geomagnetic mechanism",
    "M2 post-start orientation independence\tMarinov direct observation\tafter startup running small machine could be moved/tilted/reoriented without stopping\tOBSERVED high for account\tseparate post-start reorientation experiment",
    "M2 dry-air startup pushes\tMarinov direct-author account\t~3-4 finger pushes in dry air, more in humid conditions\tSOURCE-STATED/OBSERVED account medium-high\tRH-controlled equal-impulse startup matrix",
    "M2 restart memory\tMarinov direct observation\tsecond/third starts easier after plate stop\tOBSERVED account medium\tcontrolled discharge/rest/surface-potential history test",
    "M2 rear metal plate stop\tMarinov direct observation\tlarge metal plate behind machine stopped rotation and removed rest torque\tOBSERVED high for account / mechanism unknown\tupgrade from H2; floating/grounded/R/C/nonconductive plate controls",
    "M2 running speed\tMarinov direct-author account\t~1 revolution/s (~60 rpm)\tOBSERVED account medium-high model-specific\tretain as reference point, not universal speed",
    "Kelly geometry provenance\tMarinov author text\tDon Kelly had only seen photographs; Albert Hauser had examined machine\tSOURCE-STATED high for Marinov wording\tKelly drawings remain S2/photo-derived, never primary geometry",
    "Two-disc sector asymmetry\tMarinov TWT-VII\tthick electrically connected GRID sectors both sides of one wheel; thin sectors one external side of other\tP0 primary-author mirror / exact machine unresolved\tlarge-family constraint only; no automatic M6a CAD change",
    "Two-disc sector insulating spray\tMarinov TWT-VII\tslightly magnetized sector surfaces covered by insulating spray\tP0 primary-author mirror / exact machine unresolved\tmaterial/coating experiment lead; no cross-machine transfer",
    "Marinov electrostatic closed-loop control\tMarinov TWT-VII\tcoupled Wimshurst generator braking mechanical power ~4-5x electrostatic motor driving mechanical power\tCONTROL direct-author\tnegative/control evidence; torque/power accounting mandatory",
    "M6c large open cylinder conflict\tMarinov direct-author large-under-construction account\touter cylindrical electrode + thick Cu-wire inner coil interpretation conflicts with Hauser M6a 3-grid/magnet/bifilar cylinder\tCONFLICT / variant evidence\tnew M6c taxonomy; do not overwrite M6a",
    "M8 1-m scale family\tMarinov 1989 + Cathomen workshop transcript\t100-cm machine under construction / later one-metre object discussed\tSOURCE CONVERGENCE, identity not proven\tseparate machine ID M8",
    "M9 2-m scale family\tMarinov 1989 + Cathomen workshop transcript\t200-cm machine under construction / later two-metre object discussed\tSOURCE CONVERGENCE, identity not proven\tseparate machine ID M9",
    "M10 tandem/double converter\tCathomen amateur-video transcript mirror\tdouble converter and tandem arrangement explicitly distinguished\tW1/A1 mirror; wording translation degraded\tseparate machine ID M10; topology unknown",
    "Bönisch 2003 conventional control\tSven Bönisch ELEKTRIE 5-8/2003\tknown-electrodynamics ESD/HV transformation study; no over-unity detected\tCONTROL published author work\tcomparison/metrology only; not historical circuit evidence",
    "Floating oscilloscope ground artifact\tRimstar/Steven Dufresne testbed\tearly floating-source result invalidated by unintended scope ground\tCONTROL experimental report\tmandatory full earth/probe node map before accepting electrostatic measurements",
]
for row in rows:
    if row.split("\t",1)[0] not in t:
        t += "\n" + row
write(p, t + "\n")


# 5) M6 source map append.
p = "docs/research/m6-large-v1-source-map.tsv"
t = read(p).rstrip("\n")
rows = [
    "M6V1-S28\ttwo-disc sector asymmetry\tM6/MX\tMarinov TWT-VII direct-author additional note\tP0 source-stated, exact variant unresolved\tNOT injected into M6a V1; configuration constraint only\tlock exact machine/object to Hauser/Cathomen family",
    "M6V1-S29\tsector insulating spray\tM6/MX\tMarinov TWT-VII\tP0 source-stated, exact variant unresolved\tNOT injected into M6a V1\tcoating chemistry/thickness/machine identity",
    "M6V1-S30\tlarge open cylindrical capacitor form\tM6c\tMarinov 1989 direct-author large-under-construction observation\tP0 observation/interpretation\tseparate M6c conflict family; no M6a overwrite\texact object/stage identity and electrical construction",
    "M6V1-S31\tlarge Fe-Ni perforated sectors\tM6c/M6\tBaumann→Marinov direct-author report\tP1 source-stated\tmaterial hypothesis isolated from M6a chrome-steel wording\talloy analysis / object identity",
    "M6V1-S32\tlarge horseshoe magnet scale\tM6c\tMarinov direct-author account\tP0 observation account\t~30-cm-scale conflict/variant clue only\tcalibrated image/object",
    "M6V1-S33\t1-m large-scale family\tM8\tMarinov 1989 + Cathomen workshop transcript\tP0/W1 convergence, continuity unresolved\tseparate taxonomy only\tdate/object match and geometry",
    "M6V1-S34\t2-m large-scale family\tM9\tMarinov 1989 + Cathomen workshop transcript\tP0/W1 convergence, continuity unresolved\tseparate taxonomy only\tdate/object match and geometry",
    "M6V1-S35\ttandem/double-converter family\tM10\tCathomen amateur-video transcript mirror\tW1/A1 mirror\tseparate taxonomy only; no inferred bus topology\toriginal German transcript + timestamped object map",
]
for row in rows:
    if row.split("\t",1)[0] not in t:
        t += "\n" + row
write(p, t + "\n")


# 6) M6 status: variant boundary.
p = "docs/M6_REPLICATION_STATUS.md"
t = read(p)
marker = "## Internet-audit variant boundary — 2026-08-17"
if marker not in t:
    t += """

## Internet-audit variant boundary — 2026-08-17

The public-source crawl found additional primary-author large-machine evidence, but it does **not** justify silently modifying the existing Hauser-anchored M6a V1 CAD.

Newly separated evidence:

- Marinov TWT-VII: thick electrically connected grid sectors on both faces of one wheel versus thin sectors only on the external face of the other, plus insulating spray on slightly magnetized sectors; exact medium/large object unresolved.
- `M6c`: Marinov's 1989 large-under-construction / approximately 2:1-medium-copy line, including a simpler open cylindrical outer-electrode + thick-Cu-inner-coil capacitor interpretation and ~30-cm horseshoe-magnet scale. This conflicts with M6a enough to remain a separate family.
- `M8` / `M9`: approximately 1-m / 2-m large-scale machines under construction/workshop discussion.
- `M10`: tandem/double-converter workshop family.

**M6a V1 therefore remains frozen as the Hauser-1986/1988 best-evidence build.** A future M6c/M8/M9/M10 CAD package must be source-separated rather than averaged into M6a.
"""
write(p, t)


# 7) Changelog additive entry.
p = "CHANGELOG.md"
t = read(p)
heading = "### Added — verified Internet source audit (2026-08-17)"
if heading not in t:
    anchor = "## Unreleased — V4 best-evidence build + archive/primary-source expansion\n"
    block = """

### Added — verified Internet source audit (2026-08-17)

- broad multilingual public-web source audit with provenance/evidence ranking rather than claim aggregation;
- `internet-source-audit-2026-08-17.md`, `internet-source-ledger.tsv`, `control-replication-audit-2026-08-17.md`, `source-acquisition-backlog.tsv`;
- M2 East-West startup upgraded from H2 to Baumann→Marinov source-stated, with post-start orientation independence separately retained as Marinov observation;
- M2 rear metal-plate stop/rest-torque loss upgraded to direct Marinov observation;
- dry-air 3–4-push startup, humidity dependence, easier later restarts and ~60-rpm small-machine observation added;
- Marinov TWT-VII two-disc thick-grid/thin-sector asymmetry and insulating-spray statement added without forcing identity with M6a;
- new `M6c`, `M8`, `M9`, `M10` machine IDs prevent large-under-construction, metre-scale and tandem evidence leakage;
- Kelly geometry explicitly downgraded by Marinov's statement that Kelly had only seen photographs;
- Marinov failed electrostatic closed-loop control, Bönisch 2003 conservation-law control and Rimstar floating-scope-ground artifact integrated into methodology;
- acquisition backlog now targets original DIFØT issues, official 1989 transcript ISBN 3-9520025-1-8, Yahoo 11,284-message corpus, Weber/Schneider originals and Matthey/Nieper pages.
"""
    if anchor not in t:
        raise SystemExit("missing changelog anchor")
    t = t.replace(anchor, anchor + block, 1)
write(p, t)


# 8) Handoff/state additive block.
block = """
## Internet source audit 2026-08-17

A broad provenance-first public Internet crawl is integrated. Canonical entry points: `docs/research/internet-source-audit-2026-08-17.md`, `internet-source-ledger.tsv`, `control-replication-audit-2026-08-17.md`, `source-acquisition-backlog.tsv`.

Important corrections: M2 East-West startup is Baumann→Marinov source-stated (post-start orientation independence is separately Marinov-observed); rear metal-plate stop is direct Marinov observation; dry-air ~3–4 pushes, humidity dependence, restart memory and ~60 rpm are retained as model-specific observations. TWT-VII adds unresolved two-disc thick-grid/thin-sector asymmetry. New taxonomy: M6c large-under-construction Marinov conflict family, M8 ~1m, M9 ~2m, M10 tandem/double converter. Do not alter Hauser M6a CAD from these without an explicit object/source bridge. Kelly remains photo-derived/S2. No authentic complete hidden circuit or net-energy proof was found.
"""
for p in ("STATE.md", "addon.md"):
    t = read(p)
    if "## Internet source audit 2026-08-17" not in t:
        t = t.rstrip() + "\n\n" + block
    write(p, t)

print("Internet source audit integrated idempotently.")
