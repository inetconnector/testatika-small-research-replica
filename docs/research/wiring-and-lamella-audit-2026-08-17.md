# Testatika — Verdrahtungsbild- und Lamellen-Audit 2026-08-17

## Zweck

Dieser Audit wertet öffentlich auffindbare Verdrahtungszeichnungen, Besucherzeichnungen, Amateurvideo-Transkripte und direkte Marinov-/Hauser-Quellen gegeneinander aus. Ziel ist **nicht**, aus Lücken einen angeblich authentischen geheimen Schaltplan zu erfinden. Ziel ist eine belastbare Trennung zwischen:

- direkt beobachteter Hardware;
- direkt berichteten Verbindungen;
- Besucherrekonstruktionen;
- späteren Reverse-Engineering-Schaltungen;
- experimentell prüfbaren, konventionell funktionsfähigen Verdrahtungsvarianten.

Die daraus abgeleiteten Laborverdrahtungen stehen in `docs/electrical/`.

---

## 1. Wichtige Korrektur zu Stefan Marinov

Eine verbreitete Erzählung lautet, Marinov habe das vollständige physikalische Grundprinzip verstanden und nur den geheimen Konstruktionsplan nicht erhalten. Das ist mit Marinovs eigener 1989 publizierter Aussage **nicht vereinbar**.

Marinov schreibt ausdrücklich:

> `Ich habe das Wirkprinzip von TESTATIKA nicht verstanden und kann es nicht rekonstruieren.`

Quelle:
`https://nuetec-forschung.de/Thesta-Distatika/Marinov_physik_Hintergrund.pdf`, S. 4 des PDF/Artikelbeginn.

Später trennt Marinov zwei Fragen:

1. die elektrostatische Selbstrotations-/Motorwirkung, für die er eine Erklärung suchte und der er sich näher glaubte;
2. die behauptete hohe elektrische Ausgangsleistung, deren Erklärung er ausdrücklich als ungelöst behandelt.

**Repository-Regel:** Marinov ist eine sehr wichtige direkte Beobachtungsquelle, aber nicht der Besitzer eines verifizierten vollständigen Testatika-Schaltplans.

---

## 2. Öffentliche Bildfamilien — nicht alles ist unabhängige Evidenz

### 2.1 RexResearch: Diagram #1

Direktbild:
`https://www.rexresearch.com/testatik/schemat1.jpg`

Erkennbar sind unter anderem:

- gegenläufige Scheiben;
- Collector-/Collection-Elemente;
- seitliche große Kondensator-/Pot-Strukturen;
- Hufeisenmagnete mit Wicklungen;
- ein zentrales/oberes Verstärkungs-/Konditionierungsnetz;
- zahlreiche eingezeichnete Verbindungen, die in direkten Besucherquellen nicht vollständig bestätigt sind.

**Einstufung:** spätere Kelly-/Reverse-Engineering-Familie; nützlich als Hypothesenkarte, **kein authentischer Methernitha-Werksplan**.

### 2.2 RexResearch: Diagram #2

Direktbild:
`https://www.rexresearch.com/testatik/schemat2.jpg`

Explosions-/Funktionsdarstellung mit Scheiben, Elektroden, Kondensator-/Magnet-/Spulenbaugruppen und Verbindungslinien.

**Einstufung:** gleiche Sekundär-/Rekonstruktionsfamilie. Nicht als zweite unabhängige Bestätigung von Diagram #1 zählen.

### 2.3 Albert Hauser 1988 — Frontansicht

Direktbild:
`https://www.rexresearch.com/testatik/diagram1.jpg`

Diese Zeichnung gehört zur Hauser-Besucherrekonstruktion und nummeriert reale beobachtete Baugruppen. Sie ist für **Geometrie und Baugruppenlage** deutlich stärker als Kelly-/Potter-Rekonstruktionen, bleibt aber eine nachträgliche Beobachterzeichnung.

### 2.4 Albert Hauser 1988 — Draufsicht / `connection`

Direktbild:
`https://www.rexresearch.com/testatik/diagram2.jpg`

Besonders wichtig, weil hier reale Leitungswege/Anschlusspunkte in der Draufsicht wiedergegeben werden. Hauser warnt im Begleittext jedoch ausdrücklich, dass die elektrischen Verbindungen nur unvollständig genannt werden können.

### 2.5 Albert Hauser 1988 — Seitenansicht

Direktbild:
`https://www.rexresearch.com/testatik/diagram3.jpg`

Hilfreich zur Tiefenlage von Scheiben, Elektroden und rückwärtigen Baugruppen, aber kein vollständiger Stromlaufplan.

### 2.6 Albert Hauser 1988 — Legende / Zeichnung 3279

Direktbild:
`https://www.rexresearch.com/testatik/diagram4.jpg`

Die Legende verankert u. a. Positionen für Rectifier, Magnet, Horseshoe magnets, Pipe with spiral, Capacitors, Big capacitors, Electrodes, Lamellae, Gear wheel und die beiden Scheiben. Datierung in der Zeichnung: `1.8.1988 AH`.

### 2.7 Paul E. Potter — `Full Circuit`

Seite:
`https://www.novakcorp.com/energy/experiments/testatika.htm`

Bild:
`https://www.novakcorp.com/energy/experiments/fullcircit.gif`

Potter zeichnet einen sehr detaillierten vollständigen Stromlauf mit HF-Chokes, Wicklungen, Gleichrichtung und zusätzlichen elektromagnetischen Baugruppen. Der Begleittext ist jedoch klar als **Back-Engineering/Interpretation** formuliert und enthält zahlreiche `I think/I believe`-Annahmen.

**Konflikt:** Marinovs direkte kleine-Maschinen-Aussage widerspricht einer pauschalen HF-/Tesla-Transformator-Deutung der kleinen Pots. Potter darf daher nicht in die M2-Nominalverdrahtung übernommen werden.

### 2.8 Rimstar — `DC from the Pots`

Seite:
`https://rimstar.org/sdenergy/testa/thpotsdc.htm`

Bild:
`https://rimstar.org/sdenergy/testa/thpotsdc/wiring_pots_for_dc.jpg`

Das ist besonders wertvoll als **reale experimentelle Verdrahtungsvariante**, nicht als Historienbeweis. Die beiden Pots besitzen drei konzentrische Gitter; Außen- und Zentralstruktur bilden das Feld, während links das mittlere und rechts das innere Gitter als unterschiedliche Abnahmeknoten verwendet werden. Der Autor hat reale Pulsformen gemessen, sagt aber ausdrücklich, dass der Versuch **keinen Energieüberschuss** demonstriert.

### 2.9 Wikimedia-/Wikipedia-Linienschema

Bild:
`https://upload.wikimedia.org/wikipedia/en/d/d0/Testatika-Line.png`

Dieses verbreitete Linienschema ist eine gute visuelle Übersicht über eine spätere Schaltungsinterpretation, aber keine neue Primärquelle. Es darf nicht durch seine häufige Wiederverwendung zu höherer Evidenz hochgestuft werden.

### 2.10 `Fig1kelly.gif` / Kelly-Derivate

Ein weit verbreitetes Diagramm liegt z. B. hier:
`https://1stmuse.com/adonis/Fig1kelly.gif`

Es verbindet u. a. Collector-/Motor-brushes, Horseshoe magnets/coils, `Crystal diode / Capacitor` und Leyden jars. Don Kelly korrigierte später selbst frühe magnet-/coil-nahe Darstellungen als unzutreffend. Derartige Bilder bleiben deshalb **sekundäre Rekonstruktionshistorie**, nicht CAD-/Verdrahtungsbaseline.

---

## 3. Deduplizierung: welche Bilder bestätigen einander NICHT unabhängig?

| Bildfamilie | Unabhängige Evidenz? | Verwendung |
|---|---:|---|
| Kelly / `schemat1` / zahlreiche Webkopien | nein | historische Rekonstruktionshypothese |
| `schemat2` und Ableitungen | eingeschränkt | Baugruppen-/Hypothesenkatalog |
| Potter `Full Circuit` | nein, eigene Back-Engineering-Theorie | Vergleichsvariante |
| Wikimedia-/Atlas-/Blog-Neuzeichnungen | überwiegend nein | Übersicht, keine Quellenverstärkung |
| Hauser 1988 Zeichnungen | **ja, Besucherrekonstruktion** | starke M6-Geometrie-/Anschlussindizien |
| Marinov 1989 Text/Abbildungen | **ja, direkte Beobachterquelle** | starke M2/Mittel-/Großfamiliengrenzen |
| Cathomen Amateurvideo | **ja, Betreiber-/Werkstattdialog** | Material-, Baugruppen- und Zurückhaltungsindizien |
| Holzherr Principle Experiment 1999 | **ja, Besucherbericht** | Mesh/Lochblech-vs-Folie-Testanker |
| Rimstar Versuche | nein für Historie, ja für Reproduktionsdaten | technische A/B-Tests |

---

# 4. Was an den Lamellen/Segmenten tatsächlich besonders belegt ist

## 4.1 Cathomen: ohne Segmente funktioniert die unfertige große Maschine noch nicht

Im erhaltenen Amateurvideo-Transkript sagt Luzi Cathomen bei einer unfertigen Maschine sinngemäß:

- die Segmente müssten noch angebracht werden;
- **erst dann** beginne die Maschine zu funktionieren;
- auf die Frage `Sind das Magnete?` antwortet er `Nein, das sind Speziallegierungen.`;
- auf die Nachfrage nach Magnetfolien sagt er, man könne sie magnetisieren;
- später werden die Teile als plan aufliegend und mit kleinen Nieten befestigt beschrieben;
- sie sollen die gegenüberliegenden Strukturen **nicht berühren**.

Transkriptspiegel:
`https://www.allmystery.de/themen/gw11473-5`

Das ist ein wesentlich stärkerer Befund als die pauschale Aussage `50 Stahlsegmente`.

## 4.2 Marinov: große Segmente als leicht magnetisierte Fe-Ni-Legierung

Marinovs direkte Großmaschinenbeschreibung nennt die Segmente als spezielle **Fe-Ni-Legierung**, leicht magnetisiert.

Wichtig: Frühere kleine Maschinen werden von Marinov zugleich mit einfachen Drahtsektoren beschrieben. Daraus folgt:

> Die Fe-Ni-Legierung kann **nicht allein** das universelle Testatika-Geheimnis sein.

Sie kann für die große Maschinenfamilie eine wichtige Optimierung oder Voraussetzung darstellen.

## 4.3 Hauser: Chrome-steel, leicht magnetisiert, Corona-/Oxidationsschutz

Hausers 1986/1988 Besucherrekonstruktion beschreibt für die ca. 500-mm-Familie:

- ca. 50 Lamellen;
- etwa `0.2 × 20 × 160 mm`;
- `chrome-steel`;
- ein wenig magnetisiert;
- Materialzustand/Beschichtung zum Schutz vor Corona-Oxidation;
- perforierte Metallstruktur;
- keine Reibberührung.

Quelle:
`https://www.robkalmeijer.nl/techniek/experiments/testakica/index.html`

## 4.4 Holzherr / Principle Experiment: Gitter ist nicht einfach durch Vollfolie ersetzbar

Beim 1999 beschriebenen `Principle Experiment` bestehen bewegte und stationäre Flächen aus Lochblech bzw. Drahtgitter, zwischen mehreren Plexiglas-/Isolierlagen. Baumann soll auf Nachfrage ausdrücklich gesagt haben, dass **Vollmetallfolie statt Drahtgitter** den beobachteten Effekt nicht erzeuge.

Quelle:
`https://rimstar.org/sdenergy/testa/principleexp.htm`

Das beweist keine neue Energiequelle. Es ist aber ein sehr konkreter Grund, **Geometrie/Perforation nicht als kosmetisches Detail zu behandeln**.

---

# 5. Wahrscheinlich wichtiges Merkmalsbündel — nicht auf eine `magische Legierung` reduzieren

Die stärksten Quellen konvergieren nicht auf einen einzigen Stoff, sondern auf ein Bündel:

1. **leitfähige, aber strukturierte Oberfläche:** Lochblech/Gitter statt einfacher Vollfolie;
2. **dielektrische Trennung:** PMMA/Acryl zwischen leitfähigen Ebenen;
3. **Nichtkontaktbetrieb:** kapazitive/elektrostatische Kopplung über Luft-/Dielektrikumsspalt;
4. **magnetisch beeinflussbares Segmentmaterial:** große Familie, Fe-Ni/chromstahlartig, schwach magnetisiert;
5. **Corona-/Oberflächenzustand:** Hauser nennt Material/Beschichtung gegen Corona-Oxidation;
6. **Phasen-/Positionsabhängigkeit:** die Segmente bewegen sich periodisch an Pickup-/Drive-Elektroden vorbei;
7. **mehrlagige Gitterstrukturen:** auch in den großen Zylindern und im Principle Experiment wiederkehrend.

**Arbeitshypothese:** Das `Besondere` ist wahrscheinlich eher die Kombination aus **variabler Kapazität/Feldmodulation + strukturierter Elektrode + Dielektrikum + Material-/Magnetisierungszustand** als nur der Legierungsname.

Diese Aussage ist eine Synthese/Versuchshypothese, kein historisch gelüftetes Geheimnis.

---

# 6. Cathomen zeigt sogar zwei getrennte `Geheimniszonen`

Der Videoausschnitt ist hier wichtiger als viele spätere Internetpläne.

### Zone A — Rotorsegmente

Cathomen nennt die Segmente Speziallegierungen und sagt, dass die unfertige Maschine sie benötigt.

### Zone B — obere Verstärkungs-/Kapazitätsstufe

Im selben Dialog beschreibt Cathomen einen Pfad:

`Abnahme an Polen → nach oben → dort verstärkt/aufgewandelt → Kondensatoren/Leydener Flaschen → Ausgang`

Bei der Nachfrage, **wie** die Kapazität/obere Stufe arbeitet, nennt er Magnete und weitere Dinge/Spulen, verweigert aber ausdrücklich die genaue Erklärung.

Damit ist quellenmäßig falsch, das Geheimnis ausschließlich in den Lamellen zu suchen. Das Video lokalisiert zusätzlich eine **bewusst nicht erklärte Konditionierungs-/Kopplungsstufe**.

Die vorhandenen Kelly-/Potter-Vollschaltungen versuchen genau diese Lücke zu füllen, besitzen dafür aber keine ausreichende Primärevidenz.

---

# 7. Hausers Anschlussgrenze

Hauser liefert die bislang brauchbarste direkte M6-Anschlussrekonstruktion, schreibt aber selbst, dass die elektrischen Verbindungen nur **unvollständig** angegeben werden können.

Direkt gestützt sind unter anderem:

- stationäre horizontale Elektroden übertragen hohe Spannung in Richtung der Zylinderbaugruppe `pos. 6`;
- mehrere leitfähige Schichten/Coatings sind intern verbunden;
- Verbindungen reichen auch zu `pos. 7`, `8` und teilweise `9`, `10`, `12`;
- die nutzbare Abnahme erscheint in seiner Rekonstruktion an zwei Metallringen oben an `pos. 6`;
- pro großem Zylinder: drei konzentrische Metallgitter mit Acryltrennung sowie zentrale Magnet-/Bifilar-Struktur.

Nicht direkt gelöst sind:

- exakte Polaritäten;
- welche der 14+ Statoren gemeinsam gebust werden;
- exakte Verschaltung der drei Zylindergitter;
- Wicklungsanfänge/-enden/Phasenlage;
- genaue Top-Modul-Schaltung;
- Kondensatorwerte und innere Schichtverschaltung;
- exakte Crystal-Funktion.

Deshalb bleibt der neue Bausatz **terminal-complete, patch-defined**.

---

# 8. Was jetzt als `funktionierend` gilt

Die neuen Verdrahtungspläne in `docs/electrical/` haben zwei Ebenen:

### Historische Evidenzebene

Alles, was nicht belegt ist, bleibt steck-/messbar und wird nicht verdeckt hartverdrahtet.

### Labor-Funktionsebene

Es gibt definierte, konventionell funktionsfähige Testschaltungen, mit denen man nachweisen kann:

- statische/rotationsabhängige Kapazität;
- induzierte Ladung und Polarität;
- gepulste DC-Abnahme nach passiver Gleichrichtung;
- Feld-/Drehmomentwirkung einer definierten externen Biasquelle;
- Einfluss von Mesh vs Vollfolie;
- Einfluss von Legierung und schwacher Magnetisierung;
- Zylinder-/Pot-Kopplung;
- echte Eingangs-/Ausgangsenergiebilanz.

`Funktionierend` bedeutet **nicht**: historischer Selbstlauf oder Nettoenergieüberschuss sei garantiert.

---

# 9. Konsequenz für CAD und Verdrahtung

Die jetzigen real-material M2-V5- und M6-V2-Bausätze sind für diese Quellenlage richtig aufgebaut, weil sie Elektroden, Gitter, Spiralen, Wicklungen und unbekannte Module separat zugänglich machen. Es ist **kein weiterer Plastikersatz** erforderlich.

Neu maßgeblich sind:

- `docs/electrical/M2_V5_EVIDENCE_WIRING.md`
- `docs/electrical/M6_V2_EVIDENCE_WIRING.md`
- `docs/electrical/WIRING_VARIANTS.tsv`
- `docs/electrical/LAMELLA_TEST_MATRIX.tsv`
- `docs/electrical/diagrams/M2_V5_EVIDENCE_WIRING.svg`
- `docs/electrical/diagrams/M6_V2_EVIDENCE_WIRING.svg`

Diese Dateien bilden die Verdrahtung **explizit als prüfbares Konfigurationssystem** ab, anstatt eine unbewiesene Webzeichnung zum Original zu erklären.
