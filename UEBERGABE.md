# Testatika Research Replica — Vollständige Repository-, Forschungs- und KI-Übergabe

**Repository:** `inetconnector/testatika-small-research-replica`  
**GitHub:** https://github.com/inetconnector/testatika-small-research-replica  
**Default-Branch:** `main`  
**Repository-Status:** öffentlich, aktives Forschungs-, Rekonstruktions- und Falsifikationsprojekt  
**Stand dieser Übergabe:** 23. August 2026  
**Zweck dieses Dokuments:** Dieses Dokument konsolidiert die vollständige Repository-Übergabe, das externe Quellenregister (Q01–Q25), die historische Maschinen-Taxonomie (M0–M10), die 17 technischen Kern-Knackpunkte, die Konfliktmatrix, die physikalischen Gleichungsmodelle, den Master-Experimentierplan (E0–E11) sowie alle Governance- und Erhaltungsregeln in einem einzigen, verbindlichen Dokument.

---

# INHALTSVERZEICHNIS

1. [Teil I: Repository-Überblick, Methodik & Reale Bausätze](#teil-i-repository-überblick-methodik--reale-bausätze)
   - 1.1 Worum geht es hier überhaupt?
   - 1.2 Warum ist das Projekt schwierig?
   - 1.3 Ziel des Repositorys (Best-Evidence Research Replica)
   - 1.4 Die zwei primären Fertigungs-Bausätze: M2 V5 & M6 V2
   - 1.5 Referenz-CAD versus reale Fertigungs-CAD
   - 1.6 Historische Maschinen-Taxonomie (M0 bis M10, MX)
   - 1.7 Wissenschaftliche Grundposition & Epistemische Regeln
   - 1.8 Das Evidenz- und Provenienzsystem
   - 1.9 Primär- und Quellenpersonen strikt getrennt halten
   - 1.10 Kanonische Suchbegriffe und Aliase
2. [Teil II: Die 17 technischen Kern-Knackpunkte & Quellenanalysen](#teil-ii-die-17-technischen-kern-knackpunkte--quellenanalysen)
   - 2.1 Die 17 eigentlichen Knackpunkte des Projekts
   - 2.2 Die Meth_1–Meth_6-Video- und Audio-Transkriptionskorrektur
   - 2.3 Weber / Schneider (13. März 1984) — Technische Extraktion
   - 2.4 Hans Holzherr (5. Juni 1999) — Technische Ergänzungen
   - 2.5 Schlüsselhinweis: Dreifacher Seitenwechsel der Rotorleiter (R4)
   - 2.6 Principle Experiment (M0) — Vollständige Analyse
   - 2.7 Linden Experiment (M0b) — Quellenkritik
   - 2.8 Mike Watson (2001) — Konfliktquelle Fe vs. Cu & Ost-West
   - 2.9 Nieper / Matthey (1984) — Historische Leistungsclaims
   - 2.10 Konferenzpublikationen: Kelly/Bailey (1991) & Bailey/Grotz (1993)
   - 2.11 Methernitha-eigene Beschreibung & Methernitha-2010-Status
   - 2.12 Elena Novaretti & Schneider/Schneider (2023)
   - 2.13 V3-Photo-Branch Provenienz & Fotogrammetrie
3. [Teil III: Wissenschaftliche Grundlagen, Vorläufer & Gleichungsmodelle](#teil-iii-wissenschaftliche-grundlagen-vorläufer--gleichungsmodelle)
   - 3.1 Historische konventionelle Vorläufer (Poggendorff, Holtz, Wimshurst, Wommelsdorf)
   - 3.2 Moderne kontrollierte Wissenschaft (PMMA/Feuchte, Gitter/Corona, Wire-Plane, Electret)
   - 3.3 Minimales konventionelles Gleichungsmodell
   - 3.4 Umfassende Konfliktmatrix
   - 3.5 Häufige Mythen & Internetfehler (10 Kernirrtümer)
   - 3.6 Patentlage (Swissreg / Espacenet)
4. [Teil IV: Master-Experimentierplan, Metrologie & Datenschemata](#teil-iv-master-experimentierplan-metrologie--datenschemata)
   - 4.1 Experimentstrategie Stufe 0 bis Stufe 8
   - 4.2 MASTER-EXPERIMENTPLAN (E0 bis E11)
   - 4.3 Vollständige Metrologie-Checkliste
   - 4.4 Standardisiertes Datenschema für Messreihen
   - 4.5 Definition der Funktionsstufen (F1 Geometrie, F2 Elektrostatik, F3 Energieclaim)
5. [Teil V: Vollständiges externes Quellenregister (Q01–Q25) & Provenienz](#teil-v-vollständiges-externes-quellenregister-q01q25--provenienz)
   - 5.1 Externes Quellenregister Q01 bis Q25
   - 5.2 Quellenprioritäten (Rang A bis D) & Beschaffungsliste
6. [Teil VI: Arbeitsanweisungen, Prioritäten & Handoff für neue Sessions](#teil-vi-arbeitsanweisungen-prioritäten--handoff-für-neue-sessions)
   - 6.1 Startreihenfolge für jede neue Session
   - 6.2 Governance- und Erhaltungsregeln (AGENTS.md, Preservation, README-Sync)
   - 6.3 Kritische Invarianten & Build-Kit-Regeln
   - 6.4 Was eine übernehmende KI als Nächstes tun sollte (Prioritäten 1 bis 5)
   - 6.5 Was eine neue KI NICHT tun sollte
   - 6.6 Die drei wichtigsten offenen Fragen & Zentrale Forschungsfrage
   - 6.7 Empfohlener Handoff-Prompt für Folgesitzungen
   - 6.8 Wichtigste Repository-Dateien auf einen Blick

---

# Teil I: Repository-Überblick, Methodik & Reale Bausätze

## 1.1 Worum geht es hier überhaupt?

Dieses Repository versucht, die historische **Testatika / Thesta-Distatica** der Schweizer Methernitha-Gemeinschaft technisch, quellenkritisch und möglichst reproduzierbar zu rekonstruieren.

Die Testatika ist eine Familie historischer elektrostatischer Maschinen, die vor allem in den 1980er- und 1990er-Jahren fotografiert, gefilmt und von Besuchern beschrieben wurde. Von Betreiberseite wurden teils sehr hohe elektrische Ausgangsleistungen bis in den Kilowattbereich behauptet. Gleichzeitig ist bis heute kein vollständiger, authentischer Originalschaltplan bekannt, und es existiert keine öffentlich verfügbare, unabhängige und geschlossene Energiebilanz, die einen Nettoenergieüberschuss zweifelsfrei nachweist.

Das Projekt verfolgt deshalb **nicht** die Strategie:
> „Wir wissen bereits, wie die Testatika funktioniert, und bauen sie einfach nach.“

Sondern:
> „Wir rekonstruieren so genau wie möglich, was historisch tatsächlich beobachtet oder quellenbelegt ist, halten Unbekanntes ausdrücklich offen und bauen ein modulares Experimentiersystem, mit dem konkurrierende Funktionshypothesen sauber getestet werden können.“

Das Repository ist damit gleichzeitig:
1. **historisches Quellenprojekt**,
2. **technische Rekonstruktion**,
3. **CAD-/Fertigungsprojekt**,
4. **elektrostatisches Experimentierprojekt**,
5. **Provenienz- und Evidenzdatenbank**,
6. **Falsifikationsprojekt für verschiedene Testatika-Theorien**.

Es ist ausdrücklich **kein Repository, das Overunity, „freie Energie“, ZPE, Tachyonen oder Permanentmagnete als Energiequelle als bewiesen behandelt**.

---

## 1.2 Warum ist das Projekt schwierig?

Das Kernproblem ist nicht, dass zu wenig Material existiert. Das Gegenteil ist der Fall: Es gibt Fotos, alte Videos, Zeichnungen, Augenzeugenberichte, Marinov-Texte, Hauser-Unterlagen, Holzherr-Berichte, Methernitha-Texte, spätere Rekonstruktionen, Internetarchive und Replikationsversuche.

Das eigentliche Problem lautet:
> **Die Quellen beschreiben nicht immer dieselbe Maschine und stimmen nicht in allen Details überein.**

Unter dem Namen „Testatika“ wurden mehrere Generationen und Größen gebaut. Manche hatten eine Scheibe, zwei gegenläufige Scheiben, Hufeisenmagnete, keine sichtbaren Magnete, kleine Seitenkondensatoren, große komplexe Zylinder, unterschiedliche Drehzahlen, unterschiedliche Lamellen/Sektoren oder unterschiedliche obere Baugruppen.

Daraus folgt die wichtigste methodische Regel des gesamten Repositorys:
> **Eigenschaften dürfen nicht einfach von einer Testatika-Variante auf eine andere übertragen werden.**

---

## 1.3 Ziel des Repositorys (Best-Evidence Research Replica)

Das Ziel ist eine **Best-Evidence Research Replica**.

Das bedeutet:
- alles historisch Belegte möglichst genau nachbilden;
- Foto-/Video-Geometrie nachvollziehbar ableiten;
- widersprüchliche Angaben getrennt erhalten;
- unbekannte elektrische Knoten nicht erfinden;
- unbekannte Bauteile als modulare Blackboxes ausführen;
- Varianten reversibel bauen;
- jeden Versuch mit definierter Konfiguration durchführen;
- Energieerhaltung als Nullhypothese behandeln;
- Messungen so auslegen, dass eine echte Anomalie von gespeicherter Energie, Messfehlern, mechanischem Input oder Umweltkopplung unterschieden werden könnte.

---

## 1.4 Die zwei primären Fertigungs-Bausätze: M2 V5 & M6 V2

Das Repository hat zwei primäre reale Fertigungs-Bausätze:

### 1.4.1 M2 V5 — kleine Marinov-Maschine
- **Pfad:** `hardware/build-kits/m2-v5/`
- **Generator:** `cad/generate_m2_v5_fabrication_kit.py`
- **Dokumentation:** `docs/research/m2-v5-fabrication-kit.md`
- **Historische Kernmerkmale:** Einzelscheibe, 24 Sektoren, 2 große Hufeisenmagnete, 2 Seiten-Pots, 1 zentraler Gitter-T-Abgriff, oberes geschlossenes Gehäuse (`crystal`), untere Entladestrecke/Schalter.
- **Was V5 bedeutet:** V5 ist ein **echter Fertigungsbausatz aus realen Materialien**. 3D-Druck ist streng auf Halter, Klammern, Jigs, Wickeldorne und Schutzgehäuse beschränkt. Lagerböcke, Welle, Kugellager, PMMA-Scheibe, Kupferelektroden, Gitter, Hufeisenmagnete sind reale Kauf- bzw. Halbzeugteile.
- **Elektrische Grundregel M2:** Elektrischer Nullzustand ist `M2-V4-B0`: 24 floatende Cu-Sektoren, R0-Führung, Pots intern für Messungen offen, Hub-Bögen floatend, Crystal offen, Magnete montiert, keine Last, kein Laborantrieb.

### 1.4.2 M6 V2 — große ca. 500-mm-Zweischeibenmaschine
- **Pfad:** `hardware/build-kits/m6-v2/`
- **Generator:** `cad/generate_m6_v2_fabrication_kit.py`
- **Dokumentation:** `docs/research/m6-v2-fabrication-kit.md`
- **Quellenanker:** M6a (Hauser 1986–1988) als Konstruktionsanker; M6b (Holzherr 1999) als getrennte Variante.
- **Reale Fertigung:** 500-mm-PMMA-Scheiben, 2×50 Lamellen (~0,2 × 20 × 160 mm), Statorelektroden, Gitter, PMMA-Hülsen, Magnete, Wellen, Lager und Lagertürme sind reale Materialien. 3D-Druck nur für Halter, Distanzsterne, Modulträger, Klemmen und Bohrlehren. Echte flexible Riemen statt starrer Stangen. Koaxiale Labor-Wellenlagerung ist transparent als `LAB-BUILD` gekennzeichnet.
- **Elektrische Grundregel M6:** Der historische Innenaufbau der großen Zylinder, der oberen Drossel/Transformator-Baugruppe und der Statorelektroden ist historisch unbekannt bzw. widersprüchlich. Diese Knoten bleiben modular offen.

---

## 1.5 Referenz-CAD versus reale Fertigungs-CAD

- **Referenzmodelle (Legacy):**
  - M2 V4: `cad/reference/generate_v4_best_evidence_m2.py` → `hardware/reference/m2-v4/`
  - M6 V1: `cad/reference/generate_m6_large_v1.py` → `hardware/reference/m6-v1/`
  - *Zweck:* Visualisierung, Proportionen, Gesamtbaugruppen und Provenienz. Nicht als „Drucke alles“-Anleitung gedacht.
- **Aktuelle Fertigungsmodelle:**
  - M2 V5: `cad/generate_m2_v5_fabrication_kit.py` → `hardware/build-kits/m2-v5/`
  - M6 V2: `cad/generate_m6_v2_fabrication_kit.py` → `hardware/build-kits/m6-v2/`
  - *Zweck:* Reale Werkstattfertigung, Stücklisten, Fertigungszeichnungen, echte Materialien.

---

## 1.6 Historische Maschinen-Taxonomie

Die verbindliche Nomenklatur des Repositories (`docs/research/machines.yaml`):

- **M0 — Principle Experiment:** Kleines Vorführmodell mit Glocken-/Halbkugelfuß, schwenkbarem Plexiglasarm, 2 kleinen Gitterdosen (~8 cm hoch, Ø 3–4 cm). Baumann betonte: *Gitter zwingend nötig, Metallfolie funktioniere nicht*.
- **M0b — Linden Experiment:** Hearsay-Experimentieraufbau ohne Primärmessung (~700 V Claim unbestätigt).
- **M1 — frühe „Ruck-Zuck“-Familie:** 1970er/1980er Jahre, schwenkbare Arme, offene Aufbauten.
- **M2 — erste kleine Marinov-Maschine:** Einzelscheibe, 24 Sektoren, 2 Hufeisenmagnete, 2 Töpfe, Zylindergitter + Kupferspirale, oberes Crystal.
- **M3 — zweite kleine Marinov-Maschine:** Begleitmaschine mit abweichenden Details.
- **M4 — ca. 12-cm-Kleinmaschinenfamilie:** Von Holzherr 1999 und Hauser beschrieben.
- **M4a — Hauser 12-cm-Prototyp:** Hauser-Zeichnungen kleinerer Scheiben.
- **M5 — Weber/Schneider-Maschine (13. März 1984):** >1 m breit, ~45 cm tief, ~60 cm hoch, ~20 kg ohne Haube, zentrale ~10-cm-Scheibe, 300 V / 10 A Claim.
- **M5a — L. L. Rorschach (17. März 1984):** Separater Besuchsbericht.
- **M6 — Sammelkategorie große ca. 50-cm-Zweischeibenmaschinen:**
  - **M6a — Hauser 1986–1988:** Zeichnung 3279, 500-mm-Scheiben, 2×50 Lamellen (160 mm lang), 3-Gitter-Zylinder mit Magnet/Bifilarspule.
  - **M6b — Holzherr 1999:** Vorführung vor 34 Ingenieuren am 5. Juni 1999. Scheiben ~50 cm, 60 rpm, 50 Lamellen (~60 mm lang), dreifacher Seitenwechsel (R4).
  - **M6c — Marinov:** Große Maschine im Bau (1988/1989).
- **M7 — Dienst/Cathomen (2001):** Workshop-Variante mit Hufeisenmagneten und Frontklemmen.
- **M8 — ca. 1-m-Maschine:** Sehr großes unvollständiges Modell.
- **M9 — ca. 2-m-Maschine („Elefant“):** Großmaschine in separatem Raum.
- **M10 — Tandem / Double Converter:** Gekoppelte Doppelmaschinen.
- **MX — Unklare / unvollständige Fragmente.**

---

## 1.7 Wissenschaftliche Grundposition & Epistemische Regeln

### Nicht verhandelbare epistemische Regeln:
- **Beobachtung ≠ Funktionsdeutung.**
- **Augenzeugenbericht ≠ kontrolliertes Messprotokoll.**
- **Betreiberbehauptung ≠ unabhängige Messung.**
- **Rekonstruktionszeichnung ≠ Originalschaltplan.**
- **Ähnliche historische Maschine ≠ identische Testatika.**
- **Resonanz / hohe Spannung / großer Peak ≠ Energieüberschuss.**
- **Fehlende Erklärung ≠ Beweis exotischer Physik.**
- Eigenschaften dürfen nicht unzulässig zwischen Maschinentypen übertragen werden.
- Negative Replikationen beweisen nicht, dass jede historische Beobachtung falsch war; sie sind aber harte Gegeninformation gegen konkrete Rekonstruktionshypothesen.
- Energieerhaltung bleibt die **Nullhypothese**, bis eine geschlossene, unabhängige und reproduzierbare Energiebilanz das Gegenteil zeigt.

---

## 1.8 Das Evidenz- und Provenienzsystem

Jede technische Aussage, jedes Bauteil und jede CAD-Abmessung muss kanonisch klassifiziert sein:
- **OBSERVED:** Direkt auf Fotos/Videos/Originalobjekt sichtbar oder durch kalibrierte Messung belegt.
- **SOURCE-STATED:** Von einer namentlich genannten Primärquelle explizit behauptet.
- **PHOTO-DERIVED:** Aus Bild-/Videomaterial photogrammetrisch abgeleitet (mit Unsicherheitsintervall).
- **DERIVED:** Physikalisch oder geometrisch aus gesicherten Daten abgeleitet.
- **HYPOTHESIS:** Plausible, überprüfbare Annahme (z. B. unvollständige Leitungsführung).
- **CONFLICT:** Relevante Quellen widersprechen sich direkt.
- **UNKNOWN:** Historisch unbekannt / nicht überliefert.

---

## 1.9 Primär- und Quellenpersonen strikt getrennt halten

Niemals Aussagen verschiedener Akteure zu einem synthetischen Zitat verschmelzen:
- **Paul Baumann:** Erfinder / Konstrukteur in Methernitha; Erklärungen oft metaphorisch-religiös („Erde, Wolke, Gewitter“).
- **Stefan Marinov:** Bulgarischer/österreichischer Physiker, besuchte Methernitha 1988/1989; beschrieb M2 („connected to nothing“, „ANOTHER language“).
- **Albert Hauser:** Schweizer Ingenieur 1986–1988; Zeichnung 3279, 3-Gitter-Zylinder, Bifilarwicklung.
- **Hans Holzherr:** Schweizer Ingenieur, Vorführung 5. Juni 1999 vor 34 Ingenieuren; Bericht über 50-cm-Maschine, 60 rpm, eingewebte Drähte.
- **Luzi Cathomen / Dieter Dienst:** 2001 Workshop / Video-Interviews; Zeugen für M7.
- **Stefan Hartmann:** Betreiber von Overunity.com; Verbreiter und Übersetzer des Holzherr-Berichts (August 1999).
- **Methernitha-Kollektiv:** Offizielle Gemeinschaftsfilme und Stellungnahmen (1980er bis 2010).

---

## 1.10 Kanonische Suchbegriffe und Aliase

Bei Recherchen stets folgende Synonyme berücksichtigen:
- **Gerätenamen:** Testatika, Testatica, Thestatica, Thestatika, Thesta-Distatica, Thesta Distatica, Testa-Distatica, Swiss M-L Converter, Swiss ML Converter, M/L Converter, ML Converter, Methernitha converter.
- **Personen:** Paul Baumann, Stefan Marinov, Albert Hauser, Hans Holzherr, Luzi Cathomen, Dieter Dienst, Stefan Hartmann, Hans Weber, Inge Schneider, Adolf Schneider, Hans Nieper, Donald Hasler, Antonio Carlos M. de Queiroz.

---

# Teil II: Die 17 technischen Kern-Knackpunkte & Quellenanalysen

## 2.1 Die 17 eigentlichen Knackpunkte des Projekts

### KNACKPUNKT 1 — Der vollständige Originalschaltplan fehlt
Keine Zeichnung aus dem Umfeld von Methernitha oder Replikationsversuchen ist als authentischer Originalschaltplan verifiziert. Alle bekannten Schaltpläne im Internet sind Rekonstruktionshypothesen.

### KNACKPUNKT 2 — M2-Rotordrähte: mechanische Führung versus elektrische Verbindung
Marinov schrieb explizit, die Drähte seien **„connected to nothing“**.
- *Hypothese R0:* 24 getrennte, floatende U-förmige Drahtbügel (bevorzugte M2-Nullbasis).
- *Hypothese R1:* Durchgehender Zickzack-Draht.
- *Hypothese R2:* Front-Back-Kopplung mit leitender Nabe.
- *Hypothese R3:* Ring mit diskreten 1-kΩ-Widerständen (späterer Replikationsclaim, nicht primär belegt).
- *Hypothese R4:* Dreifacher Seitenwechsel („three-side-change weave“ nach Holzherr 1999).

### KNACKPUNKT 3 — Stationäre Elektroden
Die vorderen Abnehmer sind segmentierte Gitter- und Folienstrukturen. Form, Abstand und isolierte Abschnitte bestimmen die Ladungstrennung und Rückkopplung.

### KNACKPUNKT 4 — Die beiden M2-Seiten-Pots
Marinov beschreibt für M2: Zylindergitter + Kunststoffisolierung + zentrale Kupferspirale mit **genau 2 sichtbaren Anschlussdrähten pro Topf**. Hausers 3-Gitter-Zylinder mit Kernmagnet und Bifilarspule gehört zu M6a und darf nicht in M2 importiert werden.

### KNACKPUNKT 5 — Das `crystal`
Das obere zentrale Gehäuse enthält laut Berichten Kristalle / Halbleiterstrukturen. Historisch unklar: Uranglas, Bleiglanz, Dioden-Array, Wismut-Kombinationen oder rein mechanische Funkenstrecke. Wird als modulare Blackbox ausgeführt.

### KNACKPUNKT 6 — Welche Funktion haben die Magnete?
Hufeisenmagnete erzeugen statische Magnetfelder. Bei typischen Stromstärken im Mikro- bis Milliamperebereich ist die Lorentzkraft vernachlässigbar klein. Hypothesen: Magnetische Funkenlöschung, Wirbelstrombremsung / Drehzahlbegrenzung, Hall-Effekt oder Schauobjekt.

### KNACKPUNKT 7 — Warum soll die Maschine selbst drehen?
Elektrostatischer Motoreffekt (Poggendorff/Wommelsdorf) oder Corona-Wind erfordern mehrere Kilovolt. Selbstrotation erfordert, dass die erzeugte elektrostatische Ladung phasenrichtig auf Antriebselektroden rückgekoppelt wird.

### KNACKPUNKT 8 — Woher kommt die behauptete reale Leistung?
Elektrostatische Maschinen liefern typischerweise Mikroampere bei hoher Spannung (Milliwattbereich). Behauptete Kilowattleistungen bei 230–300 V DC erfordern eine extreme Stromverstärkung oder verdeckte Primärquellen.

### KNACKPUNKT 9 — M6-Zylinder widersprechen sich zwischen Quellen
Hauser (1986–1988) dokumentiert 3 perforierte Gitter + Innenmagnet + Spule. Holzherr (1999) dokumentiert 20 Lagen perforiertes Blech ohne Spule/Magnet. Quellen getrennt halten!

### KNACKPUNKT 10 — 50 Hz / 60 rpm
50 Lamellensektoren bei 60 rpm ergeben exakt \(50 	imes rac{60}{60} = 50\,	ext{Hz}\) Sektordurchgangsfrequenz. Dies erklärt eine Wechselspannungs-Welligkeit bei Drehzahlkopplung, belegt aber keine Netzwandlung.

### KNACKPUNKT 11 — Gitter versus Vollfolie
Baumann und Methernitha betonten mehrfach, dass Vollfolien nicht funktionierten und nur feinmaschige Gitter / perforierte Bleche die gewünschte Ladungsausbeute lieferten (Gitter-Corona-Effekt).

### KNACKPUNKT 12 — Luftfeuchtigkeit
Bei hoher Luftfeuchtigkeit bricht die Oberflächenladung auf PMMA zusammen. Historische Berichte erwähnen teils beheizte Räume oder Trocknungsmittel.

### KNACKPUNKT 13 — Metallplatte hinter der Maschine
Mehrere Berichte erwähnen eine rückseitige Kupfer- oder Aluminiumplatte als kapazitiven Bezugspunkt oder Raumladungs-Abschirmung.

### KNACKPUNKT 14 — Ost-West-Ausrichtung
Historische Betreiber behaupteten eine Ausrichtungsempfehlung nach dem Erdmagnetfeld. Konventionell: Minimierung von Störfeldern; experimentell im E6-Plan überprüfbar.

### KNACKPUNKT 15 — PMMA-Vorkonditionierung / Electret
Frisch gereinigtes oder ionisiertes PMMA speichert Oberflächenladungen über Tage bis Wochen (Elektret-Verhalten), was scheinbare Selbststart-Effekte ohne externe Quelle vortäuschen kann.

### KNACKPUNKT 16 — Historische Kurzzeitlasten
Glühlampen-Demos (10 Sekunden 1 kW) entsprechen einer Energiemenge von lediglich \(1000\,	ext{W} 	imes 10\,	ext{s} = 10\,	ext{kJ}\). Dies kann in hochspannungsfesten Kondensatorbänken rein elektrostatisch vorgeladen gespeichert gewesen sein.

### KNACKPUNKT 17 — Historische Quellen dürfen nicht doppelt gezählt werden
`meth2.asf` und `testatikadeutsch.wmv` sind dieselbe Bildsequenz; Hartmanns Übersetzung ist keine unabhängige Zweitquelle zu Holzherr.

---

## 2.2 Die Meth_1–Meth_6-Video- und Audio-Transkriptionskorrektur

- **Echte Audio-Transkription:** Alle 6 AVI-Dateien (`Meth_1.avi` bis `Meth_6.avi` aus `\\diskstation\Dani\Energy\enF_video\meth\avi`, Gesamtdauer 48,6 min) wurden mit `faster-whisper` vollständig transkribiert. Siehe [`docs/research/transcripts/README.md`](docs/research/transcripts/README.md).
- **Sprachbefund:** Durchgehend **Englisch** (Gespräch/Interview eines englischsprachigen Besuchers mit einem Vertreter der Methernitha-Gemeinschaft über das 50-jährige Kollektiv, humanitäre Ziele, Weltanschauung, innere Ordnung und osmotische Gleichspannungsfelder).
- **Kameradatum & Aufnahmeort-Evidenz:**
  - Im Videobild ist die Kamera-Uhr eingeblendet: **16. Juli 1990, ab ca. 18:45:23 Uhr**.
  - In `Meth_3` bei ca. 06:00 ist kurz ein Außengebäude mit dem Schild **`TRIGONORM AG`** (und `TRIGO`-Banner) zu sehen. Die Trigonorm AG war bereits 1984 in Linden registriert; heutige Schweizer Verzeichnisse führen sowohl *TRIGONORM AG* als auch *Methernitha* am **Moosbühlweg 2, 3673 Linden BE**.
  - **Kanonische Quellenformulierung:**
    > *„Aufgenommen am 16. Juli 1990 in Linden BE, sehr wahrscheinlich auf bzw. unmittelbar beim Methernitha-/Trigonorm-Gelände am Moosbühlweg.“*
- **Quellen-Wortlaut zu Baumanns Erklärungen:** Stefan Marinov schrieb in eigener Korrespondenz direkt **`ANOTHER language`** über Baumanns Erklärungsversuche. Die spätere Paraphrase *`like an unknown language`* ist nicht als wörtliches Zitat belegt.

---

## 2.3 Weber / Schneider (1984 / 2010) & Besuchsbericht 2. Juli 1988 (DOE-Archiv)
- **Weber & Schneider (13. März 1984 / Rückblick 2010):**
  - Maße: >1 m breit, ~45 cm tief, ~60 cm hoch; Gewicht ca. 20 kg ohne Acrylhaube.
  - Weber durfte die Maschine **hochheben und daruntersehen** (keine Zuleitungen durch den Tisch).
  - Baumann erklärte, die Leistung von 300 V / 10 A könne „stunden-, ja jahrelang“ abgegeben werden; dies war jedoch Baumanns Aussage, kein mehrstündiges Messprotokoll der Besucher.
  - 2010 bekräftigte Weber rückblickend die Behauptung von „1 kW Dauerleistung“.
- **Besuchsbericht 2. Juli 1988 (US-Department of Energy / Technidyne Associates 1989):**
  - Historischer Bericht übermittelt von D.A. Kelly ans US-DOE: In Linden seien damals **10 Konverter à 3 kW** (bei Sonne 4 kW) vorhanden gewesen, die zusammen mit Windmühlen die **180 Personen und Betriebe** der Methernitha versorgten; an der 11. Maschine wurde gearbeitet.
  - **Status:** Wichtiges Zeugnis für die Selbstwahrnehmung der Gemeinschaft. Das US-DOE stellte 1989 jedoch fest, dass die Daten für eine technische Beurteilung unzureichend sind. Zudem verfügte Methernitha über ein eigenes kleines Wasserkraftwerk.

## 2.4 Hans Holzherr (5. Juni 1999) & Albert Hauser (1986) — Dauerlauf- vs. Lastdauer-Audit
- **Hans Holzherr (1999, `report99.htm`):**
  - Vorführung vor 34 Ingenieuren; Scheiben drehten mit ~15–60 rpm für **1,5 Stunden ununterbrochen im Leerlauf**.
  - **Reale Lastdauer:** Die 1000-W-Glühlampe brannte **nur für ca. 10 Sekunden** (`W = 10 kJ = 2,78 Wh`); keine kontinuierliche 1,5-h-Dauerlast.
  - **Prüfgrenzen:** Holzherr durfte den Sockel der 50-cm-Maschine nicht berühren oder anheben; verdeckte Flachbatterien konnte er nicht ausschließen.
  - **Konstruktion:** 50 Lamellen (~60 mm lang) mit dreifachem Webmuster (R4); 20 Lagen perforiertes Blech in den Zylindern.
- **Albert Hauser (1986, `swiss Testakica.mht` / UFO-Contact / IECEC 1991):**
  - 4-stündiger Besuch; eine kleine 12-cm-Maschine lief für **2 Stunden ununterbrochen im Leerlauf**.
  - **Reale Lastdauer:** Hauser hielt explizit fest: *„We tested the machine with only measuring instruments. - It means to say, that we **didn't load the machine with any resistance**.“*
- **Physikalische Unterscheidung (10 kJ Impuls vs. 3,6 MJ Dauerlast):**
  - 10 Sekunden 1 kW = `10 kJ` (im Hochspannungsfeld durch Dielektrikum-Soakage mit `~50–88 µF` bei `15–20 kV` darstellbar).
  - 1 Stunde 1 kW = `3,6 MJ = 1 kWh` (360-mal mehr Energie; würde `18 mF` bei `20 kV` erfordern und ist in Tischgröße unmöglich speicherbar).
  - Ein echter 1-stündiger Dauerlasttest hätte die Kondensatorhypothese sofort entschieden – genau dieser Test fehlt in sämtlichen historischen Archiven.

## 2.5 Schlüsselhinweis: Dreifacher Seitenwechsel der Rotorleiter (R4)
- **Familie R4:** Ein Leiter startet auf der Vorderseite, taucht durch eine Bohrung auf die Rückseite, kehrt zurück und endet auf der Gegenseite.
- **Effekt:** Maximiert die kapazitive Wechselwirkung beider Scheibenseiten und verhindert einfache Dipolfelder.

## 2.6 Principle Experiment (M0) — Vollständige Analyse
- Kleines Demonstrationsgerät mit transparentem Glocken-/Halbkugelfuß.
- 2 kleine Zylinderkondensatoren (~8 cm hoch, Ø 3–4 cm) mit Gitterelektroden.
- Baumann demonstrierte hieran das Grundprinzip und betonte, dass massive Folien versagen.

## 2.7 Linden Experiment (M0b) — Quellenkritik
- Erinnerungsbericht über angebliche Hochspannungsversuche im Freien (~700 V).
- Keine zeitgenössischen Messprotokolle oder Fotos; als reine Hearsay-Quelle (Evidenzklasse HYPOTHESIS) eingestuft.

## 2.8 Mike Watson (2001) — Konfliktquelle Fe vs. Cu & Ost-West
- Marinov-Briefwechsel via Watson: Erwähnt Eisendraht versus Kupferdraht für die Rotordrähte.
- Erwähnt rückseitige Abschirmplatte und angebliche Ost-West-Vorzugsrichtung.

## 2.9 Nieper / Matthey (1984) — Historische Leistungsclaims
- Berichte über 3–4 kW bei 230 V DC und angebliche Versorgung eines Gewächshauses.
- Reine Betreiber-/Zeugenbehauptungen ohne geschlossene messtechnische Energiebilanz.

## 2.10 Konferenzpublikationen: Kelly/Bailey (1991) & Bailey/Grotz (1993)
- Echte Konferenzbeiträge (IECEC 1991), fassen historische Berichte zusammen, liefern aber keinen unabhängigen wissenschaftlichen Funktionsnachweis.

## 2.11 Methernitha-eigene Beschreibung & Methernitha-2010-Status
- Offizielle Veröffentlichungen betonen elektrostatische Prinzipien, Naturanalogien und lehnen kommerzielle Verwertung ab.
- 2010 erklärte die Gemeinschaft, die Energieforschungsgruppe existiere nicht mehr und Vorführungen fänden nicht mehr statt.

## 2.12 Elena Novaretti & Schneider/Schneider (2023)
- Sekundärquellen mit historischen Fotos und Zeitzeugenberichten; physische bibliographische Verifikation läuft.

## 2.13 V3-Photo-Branch Provenienz & Fotogrammetrie
- Der historische Entwicklungszweig `research/small-machine-v3-pixel-analysis` wurde vollständig in `main` konsolidiert.
- Detailanalysen befinden sich unter `docs/research/v3-photo/` (`pixel-analysis.md`, `functional-model.md`, `node-map.tsv`, `connection-plan.tsv`).
- CAD-Generator: `cad/generate_v3_photo_interp.py` generiert experimentelle Fotorekonstruktionen.

---

# Teil III: Wissenschaftliche Grundlagen, Vorläufer & Gleichungsmodelle

## 3.1 Historische konventionelle Vorläufer

Die Testatika entstand nicht im luftleeren Raum, sondern baut auf bekannten elektrostatischen Maschinen auf:

- **Poggendorff / Holtz (1865–1869):** Erste kontinuierliche Influenzmaschinen; zeigten elektrostatische Motor- und Generatorwirkung.
- **Wimshurst (1883):** Gegenläufige Scheiben mit metallischen Sektoren und Bürstenabgriffen; stabiler Selbsterregungsmechanismus.
- **Heinrich Wommelsdorf (1904–1920, US-Patent US883846A):** Kondensatormaschine mit in Isolierstoff eingebetteten Sektoren, Mehrfachplatten und hohen Wirkungsgraden bei minimierten Corona-Verlusten.

---

## 3.2 Moderne kontrollierte Wissenschaft

Für die Bewertung der Teilphänomene existiert fundierte Fachliteratur:

1. **PMMA-Oberflächenladung und Feuchtigkeit:** PMMA ist ein starker Ladungsspeicher (Elektret-Eigenschaften). Bei relativer Feuchte >60 % sinkt der Oberflächenwiderstand drastisch ab (Ladungsabfluss).
2. **Gittergeometrie und Corona-Entladung:** Feine Gitter und perforierte Bleche weisen an den Kanten mikroskopisch hohe Feldstärken auf, die schon bei moderaten Spannungen kontrollierte Spitzenentladungen und Raumladungen erzeugen.
3. **Draht-Platte-Corona:** Asymmetrische Elektrodenanordnungen erzeugen Ionenwinde (Corona-Wind), die mechanische Drehmomente ohne metallischen Kontakt bewirken können.
4. **Variable-Kapazitäts- und Elektret-Generatoren:** Zeitlich veränderliche Kapazitäten \(\frac{dC}{dt}\) wandeln mechanische Rotationsarbeit direkt in elektrostatische Energie um.

---

## 3.3 Minimales konventionelles Gleichungsmodell

Für eine rotierende Sektorenmaschine gelten die Grundgleichungen der Elektrostatik:

### 3.3.1 Variable Kapazität und Strom
\[
i(t) = rac{dq}{dt} = C(t)\,rac{du}{dt} + u(t)\,rac{dC}{dt}
\]
Bei konstanter Spannung \(U_0\) ergibt sich der Konversionsstrom aus der Kapazitätsänderung:
\[
i(t) = U_0\,rac{dC}{d	heta}\,\omega
\]

### 3.3.2 Gespeicherte elektrostatische Energie
\[
W_e = rac{1}{2}\,C\,U^2 = rac{1}{2}\,rac{Q^2}{C}
\]

### 3.3.3 Mechanische Leistung und Drehmoment
Die mechanische Leistung bei der Ladungstrennung entspricht der elektrostatischen Leistungsaufnahme:
\[
P_{	ext{mech}} = 	au\,\omega = rac{1}{2}\,U^2\,rac{dC}{d	heta}\,\omega
\]
Das elektrostatische Gegen-Drehmoment beträgt:
\[
	au_e = rac{1}{2}\,U^2\,rac{dC}{d	heta}
\]

### 3.3.4 Rotationsenergie der Scheiben
\[
W_{	ext{rot}} = rac{1}{2}\,J\,\omega^2
\]
Für zwei PMMA-Scheiben (\(arnothing 500\,	ext{mm}\), Dicke \(4\,	ext{mm}\), Dichte \(1180\,	ext{kg/m}^3\)) bei \(60\,	ext{rpm}\) (\(\omega pprox 6{,}28\,	ext{rad/s}\)) beträgt die im Rotor gespeicherte mechanische Energie ca. \(0{,}35\,	ext{J}\).

---

## 3.4 Umfassende Konfliktmatrix

| Themenbereich | Quelle A (Befund A) | Quelle B (Befund B) | Bewertung / Konsequenz |
|---|---|---|---|
| **M2-Rotordrähte** | Marinov (1989): Drähte „connected to nothing“, floatende Sektoren | Replikations-Claims: 1-kΩ-Widerstandsring | Floating ist M2-Baseline (R0); Ring nur Testvariante (R3). |
| **M2-Drahtmaterial** | Marinov (1989): Kupferleiter | Watson (2001): Eisendraht | Kupfer als Standard; Eisen als Materialvariante im E4-Plan. |
| **M6-Zylinder** | Hauser (1986): 3 Gitter + Magnet + Spule | Holzherr (1999): 20 Lagen Lochblech ohne Spule | M6a (Hauser) und M6b (Holzherr) als getrennte Baugruppen führen. |
| **M6-Lamellenlänge** | Hauser (1986): 160 mm lang | Holzherr (1999): ~60 mm lang | Hauser-Zeichnung 3279 ist M6a-Konstruktionsanker. |
| **Drehzahl M6** | Hauser: variabel / unbestimmt | Holzherr (1999): ca. 60 rpm | 60 rpm erzeugt 50 Hz Lamellenfrequenz bei 50 Segmenten. |
| **Crystal-Inhalt** | Berichte: Naturkristalle / Uranglas / Halbleiter | Cathomen/Dienst: geschlossener Messingblock | Modulare Blackbox-Schnittstelle im CAD. |
| **Magnete** | Sichtbare Hufeisenmagnete an M2, M6a, M7 | M5 (1984) und M0 ohne sichtbare Magnete | Magnete sind nicht bei allen Maschinengrößen vorhanden. |

---

## 3.5 Häufige Mythen & Internetfehler (10 Kernirrtümer)

1. **Mythos „Ingenieur-Demo am 4. August 1999“:** Die Vorführung vor 34 Ingenieuren fand am **5. Juni 1999** statt. Der 4. August 1999 war lediglich das Datum der Übersetzung durch Stefan Hartmann.
2. **Mythos „Paul Baumann starb 2008“:** Baumann verstarb am **19. August 2011** im Alter von 93 Jahren (belegt durch zeitgenössischen Nachruf).
3. **Mythos „Der vollständige Originalschaltplan ist bekannt“:** Kein veröffentlichter Schaltplan ist authentisch original.
4. **Mythos „Tesla-Spulen sind das Kernprinzip“:** Marinov schloss HF-/Tesla-Transformatoren für die kleine M2 explizit aus.
5. **Mythos „50 Segmente wandeln direkt in Netzwechselstrom“:** 50 Segmente bei 60 rpm erzeugen eine 50-Hz-Pulsation, aber keine sinusförmige 230-V-Netzleistung.
6. **Mythos „Magnete liefern die Energie“:** Statische Permanentmagnete leisten keine kontinuierliche Arbeit.
7. **Mythos „Radiumchlorid / Radioaktivität ist der Schlüssel“:** Weder nachgewiesen noch für Replikationen zulässig (Sicherheitsregeln!).
8. **Mythos „Konferenzpaper = wissenschaftlicher Nachweis“:** Kelly/Bailey (1991) dokumentierten Berichte, führten aber keine eigenen Labormessungen durch.
9. **Mythos „10 Sekunden 1-kW-Lampe = 1 kW Dauerleistung“:** Ein 10-s-Leuchtversuch benötigt nur 10 kJ gespeicherte Energie.
10. **Mythos „Keine sichtbare Batterie = freie Energie“:** Hochspannungskondensatoren, dielektrische Absorption und Elektret-Ladungen können beträchtliche Energie speichern.

---

## 3.6 Patentlage (Swissreg / Espacenet)

Systematische Recherchen in Swissreg, DPMA und Espacenet ergaben kein auf Methernitha oder Paul Baumann eingetragenes Patent für die Testatika. Relevante historische Patente betreffen konventionelle Vorläufer wie Heinrich Wommelsdorf (US883846A).

---

# Teil IV: Master-Experimentierplan, Metrologie & Datenschemata

## 4.1 Experimentstrategie Stufe 0 bis Stufe 8

1. **Stufe 0 — Mechanik:** Reibung, Rundlauf, Lagerspiel, Auswuchtung, Drehzahlabfall ohne elektrische Ladung.
2. **Stufe 1 — \(C(	heta)\) & Rotor-Routing:** Kapazitätsverlauf über Drehwinkel für R0–R4 mit LCR-Meter.
3. **Stufe 2 — Gitter versus Vollfolie:** Vergleichsmessung der Ladungsausbeute und Corona-Schwellspannung.
4. **Stufe 3 — Feuchte & PMMA:** Ladungszerfall auf PMMA bei 30 %, 50 % und 80 % relativer Luftfeuchte.
5. **Stufe 3b — Elektret-Vorkonditionierung:** Messung von Remanenzladungen nach Reibung/Hochspannung.
6. **Stufe 4 — Externes elektrostatisches Drehmoment:** Prüfung der Motorwirkung mit externer HV-Quelle (strombegrenzt).
7. **Stufe 5 — M2-Pots:** Impedanz, Kapazität und Feldverteilung der Topfkondensatoren.
8. **Stufe 6 — Crystal / Halbleiter:** Charakterisierung von Dioden-, Varistor- und Kristallmodulen als Blackbox.
9. **Stufe 7 — Phasenaufgelöste Node-Map:** Synchrone Erfassung von Sektorposition und Knotenspannungen.
10. **Stufe 8 — Zwei-Bus-Test:** Getrennte Messung von internem Erregerkreis und externem Lastkreis.

---

## 4.2 MASTER-EXPERIMENTPLAN (E0 bis E11)

- **E0 — Mechanische Nullmessung:** Bestimmung des Trägheitsmoments \(J\) und der Reibungsverluste aus der Auslaufkurve \(\omega(t)\).
- **E1 — Kapazitätsmatrix \(C(	heta)\):** Messung der Kapazitätsänderung \(rac{dC}{d	heta}\) zwischen Sektoren und Statoren.
- **E2 — PMMA-Oberflächenladungszerfall:** Elektrostatische Feldmühlentests bei variabler Luftfeuchte.
- **E3 — Verblindeter Gitter-vs.-Folien-Test:** Identische Elektrodengeometrie, einmal feinmaschiges Gitter, einmal massive Folie.
- **E4 — Rotormaterialien:** Vergleich von Cu, Fe, Edelstahl und Aluminium bei identischer Geometrie.
- **E5 — Elektrostatik-Motortest:** Ermittlung des Drehmoments bei Einspeisung definierter Hochspannung (\(<5\,	ext{mA}\)).
- **E6 — Raumorientierung (Ost-West vs. Nord-Süd):** Test auf messbare Einflüsse des Erdmagnetfelds.
- **E7 — Rückseitige Abschirmplatte:** Einfluss einer geerdeten / floatenden Rückwandplatte auf Kapazität und Verluste.
- **E8 — Topfkondensator-Charakterisierung:** Messung von Serienresonanz, Güte \(Q\) und dielektrischer Absorption.
- **E9 — Crystal-Blackbox-Matrix:** Test symmetrischer und asymmetrischer Leitfähigkeit sowie HF-Detektion.
- **E10 — Vollständig gekoppeltes Gesamtsystem:** Versuch des autonomen Selbstlaufs unter kontrollierten Bedingungen.
- **E11 — Unabhängige Replikation:** Wiederholung der Messungen an einem zweiten, baugleichen Bausatz.

---

## 4.3 Vollständige Metrologie-Checkliste

Ohne Einhaltung dieser Checkliste ist jede experimentelle Leistungsbehauptung wissenschaftlich wertlos:

### 1. Elektrische Messungen
- 4-Kanal-Speicheroszilloskop mit isolierten Tastköpfen (1000:1 HV-Probes).
- Echte Effektivwert-Leistungsmessung (\(P = rac{1}{T}\int u(t)\,i(t)\,dt\)) statt Produkt von Multimeter-Mittelwerten.
- Präzisions-Shunts im Rückleiter zur stromrichtigen Erfassung.
- Elektrostatische Feldmühle für berührungslose Oberflächenpotentiale.

### 2. Mechanische Messungen
- Berührungsloser optischer Drehzahlmesser.
- Drehmomentmessnabe oder kalibrierte Drehmomentwaage am Antrieb.
- Exakte Bestimmung des Trägheitsmoments \(J\) der rotierenden Massen.

### 3. Umwelt- & Hilfsenergiemessungen
- Kalibrierte Erfassung von Temperatur (\(^\circ	ext{C}\)), relativer Feuchte (\(\%\,	ext{rH}\)) und Luftdruck (\(	ext{hPa}\)).
- Kontinuierliche Überwachung aller Laborversorgungsleitungen auf vagabundierende HF-Einkopplungen.
- Vollständige Erfassung der eingesetzten mechanischen Startenergie (\(\int 	au\,\omega\,dt\)).

### 4. Ausschluss von Messfehlern
- Messung über ausreichend lange Zeiträume (>1 Stunde), um Entladung interner Kapazitäten auszuschließen.
- Blindversuche mit deaktiviertem Generator / Dummy-Elementen zur Nullpunktkontrolle.

---

## 4.4 Standardisiertes Datenschema für Messreihen

Jedes Experiment muss maschinenlesbar protokolliert werden:

```json
{
  "experiment_id": "EXP-M2-V5-20260823-01",
  "machine_id": "M2",
  "build_kit": "hardware/build-kits/m2-v5/",
  "configuration": "M2-V5-B0-CU-R0",
  "timestamp_utc": "2026-08-23T12:00:00Z",
  "environment": {
    "temperature_c": 21.5,
    "relative_humidity_pct": 42.0,
    "pressure_hpa": 1013.2
  },
  "rotor": {
    "routing_type": "R0",
    "conductor_material": "Cu",
    "rpm": 60.0
  },
  "measurements": {
    "mechanical_input_power_w": 0.12,
    "electrical_output_power_w": 0.00,
    "open_circuit_voltage_v": 12500.0,
    "short_circuit_current_ua": 1.2
  },
  "raw_data_file": "tests/data/20260823_m2_v5_run01.tsv"
}
```

---

## 4.5 Definition der Funktionsstufen

- **F1 — Geometrisch funktionierend:** Alle Teile passen mechanisch, Scheiben rotieren frei und vibrationsarm, Spaltmaße stimmen.
- **F2 — Elektrostatik-funktionierend:** Maschine trennt Ladung, erzeugt Hochspannung, zeigt messbare elektrostatische Kräfte und Ströme im Mikroamperebereich.
- **F3 — Historischer Energieclaim reproduziert:** Unabhängig und geschlossen nachgewiesener Nettoenergieüberschuss unter Ausschluss aller Speicher- und Hilfsenergiequellen.

---

# Teil V: Vollständiges externes Quellenregister (Q01–Q25) & Provenienz

# 29. Externes Quellenregister

Alle Links am 2026-08-16 recherchiert bzw. gegengeprüft.

## Q01 — Stefan Marinov, *The Thorny Way of Truth, Part V* (1989)

https://archive.org/details/thornywayoftruthpart5maririch

**Status:** wichtigste veröffentlichte direkte Quelle zur kleinen Maschine. Marinov sagt selbst, dass er Geheimnis/Schaltplan nicht vollständig kennt.

## Q02 — Hans Holzherr / Stefan Hartmann, 1999

https://rimstar.org/sdenergy/testa/report99.htm

**Status:** direkter Besucherbericht, Übersetzung 04.08.1999.  
**Schlüssel:** 15 rpm, Lastdemo, R4-Hinweis, 20-lagige Kondensatoren, kleine Modelle, DMM-Probleme.

## Q03 — Principle Experiment

https://rimstar.org/sdenergy/testa/principleexp.htm

**Schlüssel:** Gitter vs. Folie, 60 V, Plattenstapel, Zentralfuß.

## Q04 — Linden Experiment

https://rimstar.org/sdenergy/testa/lindenexp.htm

**Status:** ausdrücklich zweit-handige Erinnerung.

## Q05 — Testatika-Übersicht / Replikationen

https://rimstar.org/sdenergy/testa/

**Nutzen:** historische Archivierung vieler Quellen und negative/konventionelle Replikationen. Rimstar-eigene Theorie stets getrennt halten.

## Q06 — Methernitha technische Beschreibung, archivierte Wiedergabe

Über Rimstar-Testatika-Archiv erreichbar.

**Status:** Betreiber-Narrativ.

## Q07 — Weber/Schneider / Paul-Baumann-Retrospektive, NET-Journal 2011

https://www.yumpu.com/de/document/view/4114787/paul-baumann-erbauer-der-energiemaschine-testatika-93jahrig-

**Schlüssel:** 1984-Geometrie, Lastdemo, 2010-Status, Todesdatum 2011.

## Q08 — Seminarprogramm 13.03.2004

https://guns.connect.fi/innoplaza/energy/conference/Schneider/Testatika.html

**Schlüssel:** bestätigt 13.03.1984 und **05.06.1999**.

## Q09 — Kelly/Bailey IECEC 1991

https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=200902001434259167

**Status:** echte Proceedings-Referenz; keine unabhängige Validierung.

## Q10 — IECEC New Technology Area

https://www.padrak.com/ine/INE10.html

## Q11 — Related Published References / SAFE 1989

https://www.padrak.com/ine/INE11.html

Enthält Bibliographie:
`Methernitha (1989), Informationsfilm Thesta-Distatica: Sound Track Transcription`, Einsiedeln 1989.

## Q12 — Mike Watson 2001

https://www.novakcorp.com/energy/experiments/bswiss.htm

Alternativ:
https://www.robkalmeijer.nl/techniek/experiments/testakica/index.html

**Status:** H2.

## Q13 — Elena Novaretti

Verlags-/Händlerdatensatz:
https://www.gruppomacro.com/prodotti/tutta-la-verita-su-caso-testatika

Groups.io:
https://groups.io/g/testatika/topic/60555379

**ISBN:** 9788868320669

## Q14 — Schneider/Schneider 2023

Bibliographisch:
https://www.eurobuch.ch/buch/isbn/9783906571454.html

Händler:
https://www.kopp-verlag.de/a/testatika-und-weitere-freie-energie-geraete

Abweichende Metadaten:
https://www.auf1.shop/products/testatika-und-weitere-freie-energie-geraete

## Q15 — Relinfo 1990

https://www.relinfo.ch/methernitha/testatika.html

**Status:** unabhängiger Kontext, keine Energievalidierung.

## Q16 — Donald Hasler 1996/1997

https://www.relinfo.ch/methernitha/bericht.html

## Q17 — Elektrostatik-Archiv Antonio Carlos M. de Queiroz

Patente:
https://www.coe.ufrj.br/~acmq/patents.html

Wommelsdorf:
https://www.coe.ufrj.br/~acmq/wommelsd.html

Allgemein:
https://www.coe.ufrj.br/~acmq/electrostatic.html

## Q18 — Wommelsdorf US883846A

https://patents.google.com/patent/US883846A/en

**Schlüssel:** gegenläufige Platten/Systeme; historische Kondensatormaschine.

## Q19 — PMMA charge storage

DOI:
https://doi.org/10.1016/S0304-3886(98)00023-0

## Q20 — Grid geometry / corona

DOI:
https://doi.org/10.1016/j.elstat.2019.103367

## Q21 — Wire-plane corona

DOI:
https://doi.org/10.1016/j.elstat.2010.10.006

## Q22 — Electret review 2024

DOI:
https://doi.org/10.1016/j.nanoen.2024.110167

## Q23 — MEMS electret generator 2011

DOI:
https://doi.org/10.1002/tee.20631

## Q24 — Macroscale electret-like converter 2015

DOI:
https://doi.org/10.1016/j.eml.2015.07.008

## Q25 — Swissreg

https://www.swissreg.ch/

**Status:** offizielle Schweizer Patentdatenbank; systematische Testatika-Suche noch offen.

---

---

# 30. Quellenpriorität

## Rang A

- Marinov Part V
- Hauser-Originalkorrespondenz
- Originalfotos/-filme
- Holzherr 1999
- Weber/Schneider 1984 als Augenzeugenbericht
- Methernitha-Betreibertext nur für Betreiberbehauptungen

## Rang B

- Novaretti
- Schneider/Schneider quellengetrennt
- SAFE 1989
- Nieper/Matthey als Claims
- Relinfo für unabhängigen Kontext

## Rang C

- Kelly
- Potter
- Rimstar-eigene Theorien
- Watson-Hearsay

## Rang D

- Forenposts ohne Provenienz
- Free-energy-Sammelseiten
- ZPE/Tachyon/Orgon-Erklärungen ohne Messnachweis

---

---

# 31. Noch zu beschaffende Quellen

Höchste Priorität:

1. Novaretti 2015/2025 komplett.
2. SAFE Proceedings Einsiedeln 1989, besonders Soundtrack-Transkript.
3. Schneider/Schneider 2023 komplett quellenkritisch extrahieren; Impressum fotografieren.
4. Inge Schneider: frühere Publikation des 1984-Berichts.
5. Holzherr-Originalfotos 1999 in maximaler Auflösung.
6. Hauser-Originalskizzen in bestmöglicher Qualität.
7. Vollständige Marinov-Korrespondenz.
8. Methernitha-Film 1989 bestmögliche Masterkopie.
9. P. H. Matthey Originalbericht 1984.
10. Seminarvideo 13.03.2004.
11. Potter-Originaltexte mit Versionsdaten.
12. Kelly 1991 Volltext.
13. Sven Bönisch, `ELEKTRIE`, Nr. 5–8/2003, ISSN 0013-5399.
14. HCRS-Archiv / Originalmessungen.
15. Rimstar-Rohdaten, sofern vorhanden.

---

---

# Teil VI: Arbeitsanweisungen, Prioritäten & Handoff für neue Sessions

## 6.1 Startreihenfolge für jede neue Session

Jede neue Arbeitssitzung soll die Dokumente in folgender Reihenfolge konsultieren:
1. `AGENTS.md` (Verbindliche 38 Regeln)
2. `README.md` & `README.en.md` (Überblick und Bausatz-Status)
3. `UEBERGABE.md` (Dieses Dokument — vollständige Synthese und Handoff)
4. `STATE.md` (Konsolidierte, kumulative Wissensdatenbank)
5. `docs/REPLICATION_STATUS.md` (Replikations- und Vollständigkeitsmatrix)
6. `docs/research/machines.yaml` (Kanonische Maschinen-Taxonomie)
7. `docs/research/provenance-schema.yaml` (Quellen- und Provenienzschema)

---

## 6.2 Governance- und Erhaltungsregeln

1. **Erhaltungsgrundsatz (PRESERVATION.md):** Keine voreiligen Löschungen von Forschungsständen. Historische Stände bleiben über Git, Releases oder explizite Archivpfade rückführbar.
2. **README-Synchronität (Regel 35):** `README.md` (DE) und `README.en.md` (EN) müssen stets absolut spiegelbildlich gepflegt werden. Nach jeder README-Änderung ist `python scripts/check_readme_sync.py` auszuführen.
3. **Validierung & Manifeste (Regeln 9 & 25):** Nach Änderungen an Dateien müssen `python scripts/validate_assets.py`, `python scripts/generate_manifest.py` und `python scripts/check_manifest.py` fehlerfrei durchlaufen.

---

## 6.3 Kritische Invarianten & Build-Kit-Regeln

- **Reale Fertigung:** Für Bausätze (`hardware/build-kits/m2-v5/` und `m6-v2/`) sind Strukturteile (Wellen, Lager, Scheiben, Leiter, Magnete) als reale Halbzeuge auszuführen. 3D-Druck ist auf Halter, Klammern, Jigs und Gehäuse beschränkt.
- **Keine Spekulation als Fakt:** Unbekannte historische Schaltungsknoten bleiben als modulare Schnittstellen offen und dürfen nicht heimlich durch Fantasieschaltungen geschlossen werden.

---

## 6.4 Was eine übernehmende KI als Nächstes tun sollte (Prioritäten 1 bis 5)

1. **Priorität 1 — Audio-Transkription der Originalvideos:** Schweizerdeutsche Originaltöne in `tests/data/` vollständig linguistisch erfassen und gegen die Halluzinationen früherer Sitzungen absichern.
2. **Priorität 2 — M2-V5-Bausatz-Verifikation:** Fertigungszeichnungen und Toleranzen für die mechanische Bearbeitung der PMMA-Scheiben und Kupferelektroden prüfen.
3. **Priorität 3 — Kontrollierte Teilversuche (E0–E4):** Vorbereitung der Messaufbauten für Kapazitätsmessung \(C(	heta)\) und Gitter-vs-Folien-Vergleich.
4. **Priorität 4 — M6-Quellenkonflikt nicht glätten:** Die getrennten Bauzustände M6a (Hauser) und M6b (Holzherr) weiterhin strikt getrennt dokumentieren.
5. **Priorität 5 — Vollständige Energiebilanz vorbereiten:** Messplatz für geschlossene mechanisch-elektrische Leistungsmessung instrumentieren.

---

## 6.5 Was eine neue KI NICHT tun sollte

- Keine Behauptungen über freie Energie, Overunity, Tachyonen oder Raumenergie als gesichert darstellen.
- Keine Tesla-Transformatoren oder HF-Schwingkreise in die kleine M2-Maschine hineinerfinden.
- Keine Bauteileigenschaften unzulässig zwischen verschiedenen Maschinengrößen übertragen.
- Keine 3D-Druck-Ersatzteile für lasttragende Wellen oder PMMA-Rotorscheiben in den primären Bausätzen vorschlagen.
- Niemals nur eine README-Sprache aktualisieren.

---

## 6.6 Die drei wichtigsten offenen Fragen & Zentrale Forschungsfrage

### Die 3 Kernfragen:
1. **Wie war die reale elektrische Topologie?** (Welche Sektoren waren intern verbunden, welche floatend?)
2. **Wie entstand das historische Selbstrotationsverhalten?** (Reine elektrostatische Motorwirkung, Corona-Wind oder verborgener Antrieb?)
3. **Gibt es bei vollständig geschlossener Messung irgendeine reale Energieanomalie?** (Oder lassen sich alle historischen Effekte durch elektrostatische Ladungsspeicherung, dielektrische Effekte und konventionelle Wandlung erklären?)

### Die zentrale technische Forschungsfrage:
> *„Kann eine elektrostatische Gegenrotations- oder Einzelscheibenmaschine mit Gitterkondensatoren und segmentierten Elektroden unter streng geschlossener Messung mehr elektrische Wirkleistung an eine reale ohmsche Last abgeben, als mechanisch und elektrostatisch zugeführt wird?“*  
> **Nullhypothese der Wissenschaft:** Nein. Jede Abweichung bedarf des lückenlosen, reproduzierbaren Beweises.

---

## 6.7 Empfohlener Handoff-Prompt für Folgesitzungen

> *„Du übernimmst das Repository `inetconnector/testatika-small-research-replica`. Lies als Erstes `AGENTS.md`, `README.md`, `UEBERGABE.md` und `STATE.md`. Halte dich strikt an die 38 Regeln in `AGENTS.md`. Das Repository arbeitet an einer ergebnisoffenen, quellenkritischen Best-Evidence-Replikation der Testatika. Behandle Energieerhaltung als Nullhypothese, halte Maschinentypen strikt getrennt und achte bei allen Änderungen auf die synchrone Pflege von `README.md` und `README.en.md` sowie die Manifestintegrität.“*

---

## 6.8 Wichtigste Repository-Dateien auf einen Blick

| Pfad | Beschreibung |
|---|---|
| [`AGENTS.md`](AGENTS.md) | 38 verbindliche Arbeitsregeln |
| [`README.md`](README.md) / [`README.en.md`](README.en.md) | Hauptdokumentation (DE & EN synchron) |
| [`UEBERGABE.md`](UEBERGABE.md) | Konsolidierte Master-Übergabe & externes Quellenregister |
| [`STATE.md`](STATE.md) | Zentrale kumulative Wissensdatenbank |
| [`docs/research/methernitha-physics-operating-model.md`](docs/research/methernitha-physics-operating-model.md) | Physikalisches Funktionsmodell (Synthese Methernitha/Klassische Physik) |
| [`docs/REPLICATION_STATUS.md`](docs/REPLICATION_STATUS.md) | Replikations- und Vollständigkeitsstatus |
| [`hardware/build-kits/m2-v5/`](hardware/build-kits/m2-v5/) | Fertigungsbausatz kleine Marinov-Maschine |
| [`hardware/build-kits/m6-v2/`](hardware/build-kits/m6-v2/) | Fertigungsbausatz 500-mm-Zweischeibenmaschine |
| [`scripts/validate_assets.py`](scripts/validate_assets.py) | Repository- und Asset-Validierung |
| [`scripts/check_readme_sync.py`](scripts/check_readme_sync.py) | Prüfskript für synchrone READMEs |
