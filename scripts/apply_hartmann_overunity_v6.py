#!/usr/bin/env python3
"""Additive V6 source-audit update for Hartmann / Overunity.com material.

This script intentionally never deletes existing research text. It appends or inserts
new provenance/correction blocks only when their marker is absent.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel: str, text: str) -> None:
    (ROOT / rel).write_text(text, encoding="utf-8")


def append_once(rel: str, marker: str, block: str) -> bool:
    text = read(rel)
    if marker in text:
        return False
    if not text.endswith("\n"):
        text += "\n"
    text += "\n" + block.strip() + "\n"
    write(rel, text)
    return True


def insert_after_once(rel: str, marker: str, anchor: str, insertion: str) -> bool:
    text = read(rel)
    if marker in text:
        return False
    if anchor not in text:
        raise RuntimeError(f"Anchor not found in {rel}: {anchor!r}")
    text = text.replace(anchor, anchor + insertion, 1)
    write(rel, text)
    return True


changed = []

# Preserve the historical V5 version line exactly and add a current additive marker.
if insert_after_once(
    "STATE.md",
    "**Aktuelle Ergänzung:** 6.0 — Hartmann / Overunity.com",
    "**Stand:** 2026-08-16  ",
    "\n**Aktuelle Ergänzung:** 6.0 — Hartmann / Overunity.com Quellen- und Hypothesenaudit; Version-5-Inhalt bleibt vollständig erhalten.  ",
):
    changed.append("STATE.md header")

state_block = r'''
# 93. V6 – Stefan Hartmann / Overunity.com: Quellenrolle und Archivgrenzen

Die V6-Erweiterung untersucht Stefan Hartmann und `overunity.com` separat vom Marinov-/Hauser-/Holzherr-Primärkorpus. Das ist notwendig, weil Hartmann zugleich **Archivar/Verteiler**, **Fragensteller/Übersetzer** und später **eigener Hypothesenautor** war.

Quellenklassen:

- **H1:** direkt von Hartmann verfasster, datierter Text/Interview;
- **H1-M:** als Hartmann-Mail gekennzeichneter historischer Mirror;
- **W1:** zeitnaher Augenzeugenbericht, den Hartmann nur erfragte/übersetzte;
- **A1:** Archiv-/Hostingbeleg für Thread oder Medium;
- **S2:** spätere Sekundärzuschreibung ohne gefundenes Originalprotokoll.

Wichtig: Das heutige `overunityarchives.com` ist nur eingeschränkt durchsuchbar und weist auf kostenpflichtigen Vollzugang hin. Deshalb ist dieser Audit **kein Anspruch auf vollständige Auswertung jedes historischen Overunity-Posts**. Belegt sind aber der historische Testatika-Threadpfad `topic 75`, mehrere auf Overunity gehostete Testatika-Filmdateien und die direkte Hartmann-Holzherr-Übertragungskette.

Vollständiges Dossier: `docs/research/hartmann-overunity-testatika.md`  
Quellenledger: `docs/research/hartmann-overunity-sources.tsv`

# 94. V6 – Hartmann-Zeitachse 1992 → 1999 → 2000 → später → 2008

## 1992
Hartmann vergleicht William Hydes US-Patent 4,897,592 (`Electrostatic Energy Field Power Generating System`) mit der Testatika und verweist auf eine von ihm zuvor erstellte Testatika-SVGA-Animation. Sein früher Deutungsrahmen ist damit klar **elektrostatisch / Rotor-Stator / variable Kapazität**. Er äußert gleichzeitig Skepsis gegenüber einer 900-%-Hyde-Behauptung.

## 1999
Hartmann befragt Hans Holzherr nach dessen Methernitha-Besuch, übersetzt/verteilt die Antworten und fragt um Erlaubnis, ein Bild auf `overunity.com` zu hosten. Die technischen Beobachtungen sind Holzherrs, nicht Hartmanns.

## Juni 2000
Hartmann formuliert ein **Electret-/Influenz-Modell**: Plexiglas/Gitter als polarisierte dielektrische Struktur, `Taster` als nichtkontaktierende Influenz-Pickups, elektrostatische Ausrichtung/Restmoment, phasenabhängige Umpolung/Impulse und kapazitive Spannungsumformung.

## später, im gefundenen Mirror undatiert
Hartmann wechselt zu einer **schwach-radioaktive-Mineralien-/Beta-Elektronen-Hypothese**.

## 2008
Hartmann bezeichnet in einem Interview `negative resistance` und angeregten radioaktiven Zerfall/Beta-Elektronen als Haupteffekt bei Moray und Methernitha/Testatika.

**Quellenkritische Konsequenz:** Es existiert nicht eine unveränderte „Hartmann-Geheimtheorie“. Seine Erklärung änderte sich materiell.

# 95. V6 – 1999 Holzherr über Hartmann: was neu für die Provenienz ist

Die 1999er Korrespondenz belegt explizit:

- Hartmann fragt Holzherr, ob er dessen Bild auf den `overunity.com`-Server stellen dürfe;
- Hartmann kündigt an, Holzherrs E-Mails ins Englische zu übersetzen und in Free-Energy-Listen zu posten;
- Holzherr stimmt zu;
- Holzherr bezeichnet sich selbst als Zeugen, der die Funktion nicht absolut beweisen könne;
- Holzherr kann eine versteckte Batterie nicht messtechnisch ausschließen;
- Baumann verneint laut Holzherr ausdrücklich **Radiumchlorid** als Energiequelle;
- Hartmann fügt damals hinzu, dass er Nelson Camus' Radiumchlorid-Geschichte stark bezweifle.

Damit ist `overunity.com` historisch als **Distributionsknoten** belegt, nicht als unabhängige Messinstanz.

Weitere Holzherr-Punkte bleiben hochrelevant: ca. 15 rpm bei diesem Besuch, Principle Experiment mit perforiertem Gitter, ungefähr 60 V nach mehreren Schwenks, Aussage `Vollfolie funktioniert nicht`, kleine Ein-Scheiben-Varianten, eingewebte Drahtsektoren und die schwierige nicht-wissenschaftliche Erklärsprache Baumanns.

# 96. V6 – Hartmanns Juni-2000-Electret-Modell: technisch wertvollster Teil

Hartmanns 2000er Hypothese konvergiert überraschend gut mit dem heutigen V5-Arbeitsmodell, obwohl sie **keine Primärbeschreibung des Originalgeheimnisses** ist:

1. Plexiglas/Dielektrikum trägt einen persistenten oder langsam relaxierenden Ladungs-/Polarisationszustand;
2. Rotor und feste Elektroden bilden eine winkelabhängige Kapazitätsmatrix `C_ij(theta)`;
3. `Taster` koppeln berührungslos über Influenz/Displacement Current;
4. Gitter/Lochbleche formen Feld, Oberflächenladung, Corona und Raumladung anders als Vollfolie;
5. ein nichtlineares Element (`crystal`/Diode) kann Ladung nur in ausgewählten Phasen weiterleiten;
6. getrennte Hochspannungs-Bias- und niedrigere Speicher-/Lastzustände sind möglich;
7. Kondensatorstufen können Spannung/Strom/Impedanz umformen, ohne Energie zu erzeugen.

Das stärkt **H11/H27/H28/H30/H32** aus V5 und führt zu H36–H38 unten.

# 97. V6 – Quantitativer Audit des `capacitive transformer`-Beispiels

Hartmann nennt: `1 µF @ 1000 V` wird auf `100 µF` entladen → ungefähr `10 V` und höhere Stromfähigkeit.

Für direkte Ladungsteilung gilt:

`V_f = C1*V1/(C1+C2) = 9.90099 V`.

Die Spannungsaussage stimmt größenordnungsmäßig. Die Energie jedoch:

- `E_i = 0.5 J`
- `E_f = 0.0049505 J`
- Differenz `≈ 0.49505 J = 99.01 %` der Anfangsenergie.

Bei einfacher dissipativer Ladungsteilung wird diese Differenz in realen Schalt-/Leitungs-/Strahlungsmechanismen verloren. Ein guter Wandler kann Hochspannung gegen höheren Strom bei niedrigerer Spannung tauschen, aber die Energie nicht vervielfachen.

**V6-Bewertung:** Die Form spezieller Testatika-Kondensatoren bleibt als Impedanz-/Feldgeometrie relevant. `Großer C bei kleinerem V` ist **kein Energiegewinnmechanismus**.

# 98. V6 – Gitter/Luftionen: wertvolle Geometriehypothese, schwache Energiequellenhypothese

Hartmann vermutet 2000, Gitter ließen ionisierte/polarisierte Luft besser an die Electret-Oberfläche koppeln und nennt ungefähr `10^23 Moleküle/cm³`.

Korrektur über ideales Gas bei ungefähr Raumtemperatur und 1 atm:

`n ≈ 2.5 × 10^19 Moleküle/cm³`.

Hartmanns Zahl ist damit ungefähr vier Größenordnungen zu hoch. Zudem ist normale Luft überwiegend neutral; aus der Moleküldichte folgt keine entsprechende frei verfügbare Ladungsdichte.

Trotzdem ist die Gitterspur experimentell stark, weil Mesh/Lochblech gegenüber Vollfolie ändern kann:

- lokale Feldspitzen;
- effektive Kapazität;
- Corona-/Ionisationsschwelle;
- Luft-/Ionentransport;
- Oberflächenladung;
- Leck- und Relaxationspfade.

**Priorität:** geometriekontrollierter Mesh-vs-Lochblech-vs-Folie-A/B-Test bleibt hoch. Ein Unterschied beweist zunächst nur einen Feld-/Transporteffekt.

# 99. V6 – Spätere Radioaktivitäts-/Betavoltaik-Hypothese Hartmanns

Ein späterer undatierter Hartmann-Kommentar im gleichen historischen Mirror behauptet/hypothetisiert, gepulste Hochspannung könne schwach radioaktive Mineralien/Gesteine in Testatika-Baugruppen stimulieren, sodass Beta-Elektronen von Drähten/Gittern gesammelt würden.

V6-Quellenbewertung:

- mehrfach spekulative Formulierungen (`probably`, `must be`);
- keine gefundene Testatika-Materialanalyse;
- keine Isotopenidentifikation;
- keine Dosis-/Aktivitätsmessung;
- keine geschlossene nukleare Energiebilanz;
- spezifische Radiumchlorid-Geschichte war 1999 laut Holzherr von Baumann verneint worden und wurde damals auch von Hartmann bezweifelt.

Betavoltaik selbst ist reale Physik: Betaenergie eines **konkreten Radioisotops** wird in elektrische Energie umgewandelt. Publizierte Modelle rechnen Isotop, Aktivität, Spektrum, Geometrie und Selbstabsorption explizit. Eine Hochleistungsarbeit nennt für 0.1-W- bis Watt-Niveaus Radioisotopenbeladungen >`10^13 Bq`.

**Konsequenz:** Selbst bei Nachweis radioaktiver Komponenten wäre die Energiequelle Kernzerfall, nicht Overunity. Für dieses Replikationsprojekt werden **keine radioaktiven Stoffe beschafft oder eingesetzt**.

# 100. V6 – `negative resistance` bei Hartmann 2008

Hartmann verbindet 2008 Testatika/Moray mit `negative resistance` und angeregtem radioaktivem Zerfall/Beta-Elektronen.

Negative differentielle Widerstandskennlinien sind real, aber keine selbständige Energiequelle. Reale NDR-Bauelemente oder aktive negative Impedanzen benötigen Bias/Pumpenergie oder setzen gespeicherte Energie um. Eine radioaktive NDR-/Verstärkerhypothese müsste wiederum die Kernzerfallsenergie bilanzieren.

**Status:** historisch wichtig für Hartmanns spätere Position; niedrig als Beweis für die Testatika.

# 101. V6 – Kristallspur: neue, aber sekundäre Hartmann-Zuschreibung

Rimstar führt eine Aussage, Hartmann habe Methernitha besucht und dort erfahren, das Geheimnis liege in den Kristallen. Im aktuellen Audit wurde **kein originales Hartmann-Besuchsprotokoll** gefunden, das diese konkrete Aussage verifiziert.

Daher:

- nicht als Baumann-Fakt behandeln;
- nicht als Hartmann-Primärbeobachtung behandeln;
- als **S2-Suchspur** erhalten;
- mit der bereits starken unabhängigen Tatsache trennen, dass Marinov/Baumann tatsächlich ein unbekanntes `crystal` erwähnen.

# 102. V6 – Neue Hypothesen H36–H42

**H36 — electretartige Rotorpolarisation / persistente Dielektrikum-Ladungszustände**  
Status: **mittel bis mittel-stark** als testbare Sekundärhypothese. Keine Evidenz, dass das Original zwingend thermisch hergestellte Electrets verwendete.

**H37 — Gittergeometrie koppelt/ordnet relevante Oberflächen-/Raumladung besser als Vollfolie**  
Status: **mittel-stark als Geometrie-/Transporthypothese**, niedrig als externe Energiequelle.

**H38 — `capacitive transformer` als Spannungs-/Impedanzkonditionierung**  
Status: **mittel**. Keine Energievervielfachung; vollständige Ladungs-/Energiebilanz erforderlich.

**H39 — schwach radioaktive Mineralien als Testatika-Kern**  
Status: **niedrig**. Hartmann-Späthypothese ohne Testatika-spezifische Material-/Strahlungsbefunde.

**H40 — negative resistance / stimulierter Zerfall als Kernmechanismus**  
Status: **niedrig**. Keine Testatika-Kennlinie oder Isotopen-/Leistungsbilanz.

**H41 — `Kristalle sind das Geheimnis`, Hartmann-Besuch**  
Status: **mittel-niedrig als Suchspur**, nicht verifiziert als Primärquelle.

**H42 — overunity.com als historischer Testatika-Medien-/Diskussionsknoten**  
Status: **stark**. Thread- und Dateipfade sowie Hartmann-Holzherr-Korrespondenz mehrfach erhalten.

# 103. V6 – Arbeitskonsens nach Hartmann-/Overunity-Audit

Die neue Recherche verändert den V5-Kern **nicht** in Richtung Tesla/HF oder Radioaktivität. Sie stärkt vielmehr eine konventionell testbare elektrostatische Rekonstruktion:

> **persistenter Dielektrikum-/Oberflächen-Ladungszustand → winkelabhängige Kapazitätsmatrix → berührungslose Taster/Influenz → Gitter-Feldformung → phasenselektives Crystal/Diode-Charge-Gating → getrennte Bias-/Speicherzustände → kapazitive/induktive Impedanzkonditionierung.**

Hartmanns Juni-2000-Electret-Modell ist hierfür eine wertvolle **sekundäre** Konvergenzquelle. Seine Luftionen-kW-Erklärung, spätere Radioaktivitätstheorie und Negative-Resistance-Deutung liefern dagegen derzeit **keinen geschlossenen Energiequellennachweis**.

Neue Forschungspriorität:

1. dielektrische Ladungs-/Polarisationsrelaxation messen;
2. Mesh/Lochblech/Folie kontrolliert vergleichen;
3. Metallplatten-Grenzbedingung wiederholen;
4. getrennte Drive-/Pickup-Elektroden testen;
5. Crystal/Diode als phasenselektives Charge-Gate testen;
6. Kondensatorstufen mit vollständiger Energie-/Ladungsbilanz prüfen;
7. erst danach Magnet-/Spulen-Zusatzstufen untersuchen.

**Keine radioaktiven Materialien im Replikationspfad.**
'''
if append_once("STATE.md", "# 93. V6 – Stefan Hartmann / Overunity.com", state_block):
    changed.append("STATE.md V6")

sources_block = r'''
## Stefan Hartmann / Overunity.com archival trail — V6

A dedicated source audit is maintained in [`research/hartmann-overunity-testatika.md`](research/hartmann-overunity-testatika.md) with a machine-readable ledger in [`research/hartmann-overunity-sources.tsv`](research/hartmann-overunity-sources.tsv).

Key provenance findings:

- **1992:** Stefan Hartmann directly compared the Testatika with William Hyde's electrostatic rotor/stator patent and referenced an earlier Testatika animation: `https://groups.google.com/g/sci.energy/c/pVGecAtRSXc`.
- **1999:** Hans Holzherr's eyewitness email is distinct from Hartmann's role as questioner/translator/distributor. The correspondence explicitly records Hartmann asking permission to put Holzherr's picture on the `overunity.com` server: `https://www.novakcorp.com/energy/experiments/tesnews.htm`.
- **June 2000:** a historical mirror preserves a Hartmann email proposing an electret/influence interpretation with non-contact `Taster` pickups and capacitive voltage transformation: `https://www.robkalmeijer.nl/techniek/experiments/testakica/index.html`.
- **Later:** the same mirror preserves a materially different Hartmann hypothesis involving weak radioactive minerals and beta electrons. This is a later Hartmann hypothesis, not a Baumann statement.
- **2008:** an interview records Hartmann associating Testatika with `negative resistance` and excited radioactive decay: `https://dandelionsalad.wordpress.com/2008/06/27/free-energy-and-the-open-source-energy-movement-part-one/`.
- Historical external links preserve an Overunity Testatika `topic 75` and media paths `testa01.rm`, `testa02.rm`, `meth5.asf`.
- The current `overunityarchives.com` search page indicates full archive access is restricted to paid subscribers; therefore V6 does not claim exhaustive post-by-post coverage of the old forum.

**Source rule:** Hartmann is treated as an important archivist/distributor and evolving hypothesis author, not as a stable primary witness to the internal Testatika circuit. A Hartmann-hosted Holzherr statement remains a Holzherr statement.
'''
if append_once("docs/sources.md", "## Stefan Hartmann / Overunity.com archival trail — V6", sources_block):
    changed.append("docs/sources.md")

source_basis_block = r'''
## V6-Ergänzung: Stefan Hartmann / Overunity.com

Stefan Hartmann erhält eine eigene Provenienzklasse, weil seine Rolle über die Zeit wechselte:

1. **Hartmann direkt (H1):** eigene datierte Beiträge/Interviews — verlässlich für die Frage, *was Hartmann zu diesem Zeitpunkt dachte*, nicht automatisch für das Originalprinzip.
2. **Hartmann-Mirror (H1-M):** als Hartmann-Mail gekennzeichnete historische Kopie — technisch verwertbar mit Mirror-Vorbehalt.
3. **Hartmann als Übermittler von Augenzeugen (W1 via Hartmann):** z. B. Holzherr 1999 — die Beobachtung bleibt Holzherr zugeordnet.
4. **Overunity-Archivspur (A1):** belegt Thread-/Medienexistenz und Überlieferung, nicht physikalische Richtigkeit.
5. **Sekundäre Hartmann-Zuschreibung (S2):** z. B. Rimstar `secret is in crystals` — Suchspur bis Primärbeleg gefunden ist.

Hartmanns Hypothesen dürfen nicht zeitlich zusammengeschoben werden: 1992 elektrostatischer Hyde-Vergleich; 2000 Electret/Influenz/Luftionen; später radioaktive Mineralien; 2008 `negative resistance`/angeregter Zerfall. Die **2000er Electret-/Influenzkomponente** ist die stärkste technische Konvergenz mit dem aktuellen Charge-State-Modell; die späteren Energiequellenbehauptungen bleiben niedrig gewichtet.
'''
if append_once("docs/research/source-basis.md", "## V6-Ergänzung: Stefan Hartmann / Overunity.com", source_basis_block):
    changed.append("docs/research/source-basis.md")

evidence_rows = """\
Hartmann früher Deutungsrahmen\tStefan Hartmann Usenet 1992\tTestatika mit William-Hyde-Elektrostatiksystem verglichen; frühere Testatika-Animation erwähnt\thoch für Hartmann-Historie / niedrig-mittel für Originalprinzip\tstützt variable-Kapazität-/Elektrostatik-Vergleich, keine CAD-Pflicht\nOverunity Übertragungskette\tHolzherr↔Hartmann 1999\tHartmann fragt nach Hosting auf overunity.com und kündigt Übersetzung/Verteilung der Augenzeugenmails an\thoch für Provenienz\tkeine Geometrieänderung; Sprecherrollen strikt trennen\nHartmann Electret-Modell\tStefan Hartmann Juni 2000 Mirror\tPlexiglas/Gitter als electretartige Struktur; Taster als berührungslose Influenz-Pickups\tmittel als Mechanismushypothese / hoch als Hartmann-Text\tV3/R4: Dielektrikum-Ladungszustand und Pickup-Kopplung messbar machen\nHartmann capacitive transformer\tStefan Hartmann Juni 2000 Mirror\tHV von kleiner C auf größere C umverteilen; Spannung sinkt, Stromfähigkeit steigt\tmittel für Impedanzkonditionierung / Energiegewinn widerlegt\tKondensatorvarianten nur mit vollständiger Energie-/Ladungsbilanz\nHartmann Mesh/Luftionen\tStefan Hartmann Juni 2000 Mirror\tGitter soll Luftionen an Electret koppeln; Luft als Energiequelle vermutet\tmittel für Feld-/Transportgeometrie / niedrig für Energiequelle\tMesh-vs-Lochblech-vs-Folie A/B; Corona/Leakage/Feld messen\nHartmann Luftdichte\tStefan Hartmann Juni 2000 Mirror\t~10^23 Moleküle/cm3 genannt\thoch als Quellenwortlaut / quantitativ falsch\tKorrektur: ~2.5e19/cm3 bei Raumtemperatur/1 atm; nicht als Energieargument verwenden\nHartmann Radioaktivität spät\tspäter Hartmann-Kommentar im historischen Mirror\tschwach radioaktive Mineralien + gepulste HV + Beta-Elektronen als Testatikaquelle vermutet\tniedrig für Testatika / hoch als spätere Hartmann-Hypothese\tkeine radioaktiven Materialien; nur Quellen-/Messhypothese\nHartmann negative resistance\tStefan Hartmann Interview 2008\tTestatika/Moray mit negativer Resistenz und angeregtem radioaktivem Zerfall verbunden\tniedrig für Testatika-Wirkprinzip\tnicht Baseline; NDR ist ohne Energiequellenbilanz kein Gain-Nachweis\nHartmann Kristall-Geheimnis\tRimstar Sekundärzuschreibung\tHartmann habe bei Methernitha erfahren, das Geheimnis liege in Kristallen\tS2 / mittel-niedrig als Suchspur\tCrystal-Modul bleibt testbar, Zuschreibung nicht als Fakt ausgeben\nOverunity Testatika Thread/Media\texterne Archivzeiger 2005/2006\ttopic 75 sowie testa01.rm/testa02.rm/meth5.asf historisch unter overunity.com belegt\thoch für Hosting-Provenienz\tVideo-Linie dokumentieren; technische Aussagen separat bewerten\n"""
if "Hartmann früher Deutungsrahmen\tStefan Hartmann Usenet 1992" not in read("docs/research/evidence_matrix.tsv"):
    text = read("docs/research/evidence_matrix.tsv")
    if not text.endswith("\n"):
        text += "\n"
    text += evidence_rows
    write("docs/research/evidence_matrix.tsv", text)
    changed.append("docs/research/evidence_matrix.tsv")

scientific_block = r'''
## V6: Stefan Hartmann / Overunity source audit

The Hartmann audit does **not** add evidence for a closed net-energy surplus. It does add a useful historical convergence on an electrostatic charge-state topology.

### Strongest useful Hartmann contribution

Hartmann's June-2000 electret/influence interpretation is compatible with established mechanisms already in the repository:

- persistent dielectric polarization / surface charge;
- angle-dependent capacitance;
- non-contact capacitive/influence pickup;
- mesh-dependent field, corona and leakage behavior;
- nonlinear diode/crystal charge routing;
- voltage/current impedance conversion through capacitor networks.

### Quantitative corrections

Hartmann's `1 µF at 1000 V -> 100 µF` example does give about 9.90 V after direct charge sharing, but the initial 0.5 J becomes only about 0.00495 J stored in the two capacitors in the idealized final state; direct charge sharing therefore does not demonstrate energy amplification.

His quoted air density of about `10^23 molecules/cm3` is also incorrect by roughly four orders of magnitude; an ideal-gas estimate near room conditions and one atmosphere is about `2.5e19 molecules/cm3`. More importantly, neutral molecular density is not free-charge density.

### Later radioactive / negative-resistance hypothesis

Hartmann later proposed weakly radioactive minerals and, by 2008, `negative resistance` plus excited radioactive decay. No Testatika-specific isotope, activity, dose-rate, material assay or nuclear energy balance has been found in the audited corpus. Betavoltaic conversion is real physics, but its source is radioactive decay and therefore would require explicit isotope/activity accounting; it is not over-unity.

The repository therefore keeps **energy conservation as the null hypothesis** and does not use radioactive materials in replication work.
'''
if append_once("docs/scientific-status.md", "## V6: Stefan Hartmann / Overunity source audit", scientific_block):
    changed.append("docs/scientific-status.md")

baumann_block = r'''
# V6-Ergänzung: Hartmann ist nicht Baumann

Der Hartmann-/Overunity-Audit liefert eine wichtige zusätzliche Sprechertrennung:

- Hartmanns **Juni-2000-Electret-/Influenzmodell** ist eine technische Interpretation Hartmanns;
- Hartmanns spätere **Radioaktivitäts-/Beta-Elektronen-Hypothese** ist ebenfalls Hartmanns eigene spätere Theorie;
- Hartmanns 2008er `negative resistance`-Aussage darf nicht rückwirkend als Baumanns Erklärung gelesen werden;
- der von Holzherr berichtete Satz, Baumann habe **Radiumchlorid** als Energiequelle verneint, bleibt als zeitnaher Augenzeugenbericht erhalten;
- eine sekundäre Rimstar-Zuschreibung, Hartmann sei gesagt worden `the secret is in the crystals`, bleibt offen, solange kein originales Hartmann-Besuchsprotokoll gefunden ist.

Für die Entschlüsselung von Baumanns Begriffen darf daher nur dort Hartmann herangezogen werden, wo er eine **engineering translation** anbietet, nicht als Ersatz für Baumann-Wortlaut. Besonders nützlich ist 2000 die Deutung `Taster -> non-contact influence pickup` und `grid/electret -> charge-state/field-forming structure`; die behauptete Energiequelle bleibt separat offen.
'''
if append_once("docs/research/baumann-language-decoding.md", "# V6-Ergänzung: Hartmann ist nicht Baumann", baumann_block):
    changed.append("docs/research/baumann-language-decoding.md")

readme_block = r'''
## Hartmann / Overunity.com source audit

The historical Internet layer is now separated from the direct Marinov/Hauser/Holzherr evidence. See:

- [`docs/research/hartmann-overunity-testatika.md`](docs/research/hartmann-overunity-testatika.md) — dated Hartmann timeline, Overunity archive trail, electret/air-ion/radioactivity/negative-resistance hypothesis audit and quantitative corrections;
- [`docs/research/hartmann-overunity-sources.tsv`](docs/research/hartmann-overunity-sources.tsv) — machine-readable provenance ledger.

The strongest useful convergence is Hartmann's **June-2000 electret/influence model**. His later radioactive-mineral and negative-resistance explanations are preserved as later hypotheses, not as verified Baumann/Methernitha statements or proof of net energy gain.
'''
if append_once("README.md", "## Hartmann / Overunity.com source audit", readme_block):
    changed.append("README.md")

safety_block = r'''
## V6-Ergänzung: radioaktive Hypothesen

Spätere Internet-/Hartmann-Hypothesen zu schwach radioaktiven Mineralien sind **kein Replikationspfad** dieses Projekts. Keine radioaktiven Minerale, Isotope oder Quellen beschaffen, präparieren, anregen oder in die Maschine einbauen. Eine historische Radioaktivitätshypothese wäre ausschließlich durch professionelle, nicht-invasive Strahlungs-/Materialmessung an einem Originalgerät zu prüfen.
'''
if append_once("docs/research/safety.md", "## V6-Ergänzung: radioaktive Hypothesen", safety_block):
    changed.append("docs/research/safety.md")

changelog_block = r'''
## Unreleased — Hartmann / Overunity.com V6 source audit

### Added
- `docs/research/hartmann-overunity-testatika.md`: dated source-role audit from Hartmann's 1992 electrostatic frame through the 1999 Holzherr distribution chain, June-2000 electret model and later radioactive/negative-resistance hypotheses
- `docs/research/hartmann-overunity-sources.tsv`: machine-readable provenance ledger
- historical Overunity Testatika thread/media provenance (`topic 75`, `testa01.rm`, `testa02.rm`, `meth5.asf`)
- quantitative audit of Hartmann's capacitor-sharing example and air-density statement
- H36–H42 hypothesis set

### Updated additively
- `STATE.md`, `docs/sources.md`, `docs/research/source-basis.md`, `docs/research/evidence_matrix.tsv`, `docs/scientific-status.md`, `docs/research/baumann-language-decoding.md`, `docs/research/safety.md`, and `README.md`

### Scientific position
Hartmann's June-2000 electret/influence interpretation is retained as a useful secondary convergence with the charge-state model. His atmospheric-ion energy-source, weak-radioactive-mineral and negative-resistance explanations remain unverified hypotheses. No radioactive-material experiments are part of this repository.
'''
if append_once("CHANGELOG.md", "## Unreleased — Hartmann / Overunity.com V6 source audit", changelog_block):
    changed.append("CHANGELOG.md")

print("Additive Hartmann/Overunity V6 update complete.")
for item in changed:
    print(f"- changed: {item}")
if not changed:
    print("- no changes needed (already applied)")
