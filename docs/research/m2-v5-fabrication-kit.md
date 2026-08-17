# M2 V5 — professioneller Fertigungs-Bausatz

## Ziel

M2 V5 ist die technische Baupaket-Schicht über der quellenkritischen M2-V4-Geometrie. Sie ersetzt die missverständliche Vorstellung, ein vollständiges STL sei automatisch ein funktionaler Kunststoff-Nachbau.

## Konstruktionsprinzip

1. **Evidenzgeometrie bleibt erhalten.** Die ca. 200-mm-Rotorscheibe, die nominell 24 getrennten Cu-Sektoren, die zwei Seiten-Pots und die sichtbaren Magnet-/Statorpositionen bleiben die Ausgangsbasis.
2. **Werkstofffunktion entscheidet über den Dateityp.** Kunststoffteile sind nur Träger, Halter, Jigs, Schutz- und Isolierteile. Leiter/Magnete/Wellen/Lager/PMMA-Scheiben werden aus real geeigneten Werkstoffen gefertigt oder gekauft.
3. **Unbekannt bleibt modular.** Crystal und unbekannte interne Verbindungen werden nicht erfunden, sondern an isolierten, austauschbaren Schnittstellen terminiert.
4. **Mechanik zuerst.** Vor elektrischen Versuchen müssen Rundlauf, Lagerung, Rotorfreiheit, Schutz, Auswuchtung und Isolation nachgewiesen sein.

## Mechanischer Aufbau

### Basis und Rückplatte

- Basis: 370 × 180 × 18 mm, steife nichtleitende Strukturplatte (z. B. hochwertiges Birke-Multiplex/Phenolplatte; Material dokumentieren).
- Rückplatte: 336 × 246 × 8 mm, vorzugsweise gegossenes PMMA oder gleichwertige steife nichtleitende Platte.
- Die alten massiven CAD-Körper bleiben Referenz; die V5-Platten sind reale Zuschnittteile.

### Welle und Lager

- Präzisionswelle: 8 mm Metall, ca. 245 mm Arbeitslänge.
- Zwei 608-2RS Qualitätslager.
- **Keine gedruckten Dauer-Lagerböcke:** die beiden Lagerträger und Retainer werden aus 6061-T6-Aluminium oder steifem G10/FR4 gefertigt; die 22-mm-Lagersitze werden präzise nachbearbeitet.
- Die beiden Lager liegen auf derselben Y-Achse bei Rotorzentrum Z=160 mm; eine gedruckte Ausrichtlehre dient nur zur Montagekontrolle.
- Der Rotor wird zwischen zwei ausgewuchteten Metallflanschen mit 6-Loch-Kreis geklemmt; reale 8-mm-Klemmringe sichern die Nabe axial. Kunststoff übernimmt keine Rotorlast oder Drehmomentübertragung.

### Rotor

- Rotorscheibe: reales gegossenes PMMA, Ø200 × 3,5 mm Arbeitsdicke.
- R0-Nominalteil: 24 getrennte Cu-Drähte, ca. 1 mm.
- R4 bleibt separate Forschungsvariante.
- Jeder Draht muss elektrisch gegen Nachbarn, Welle und nicht deklarierte Strukturen offen sein.
- Nach Montage: statisch/dynamisch auswuchten und Scheibenschlag prüfen.

## Seiten-Pots

Der Pot wird nicht als „gedruckter Kondensator“ behandelt. V5 besteht aus:

- gedrucktem unteren/oberen Träger;
- Clips für echtes Metallgitter;
- echtem PMMA-/Acryl-Dielektrikrohr;
- echter Kupferleitung für die innere Spirale;
- gedrucktem Wickeldorn als Montagewerkzeug;
- zwei isolierten realen Anschlussbuchsen pro Pot.

Die internen Werte/Materialzustände sind experimentell zu charakterisieren; eine unbekannte historische C-/Dioden-Topologie wird nicht hineinerfunden.

## Statoren, Magnete, Crystal

- aktive Stator-/Panel-Einsätze: leitfähiges Metall/Metallgitter; gedruckte Teile dienen nur als Clips/Halter;
- Hufeisenmagnete: reale Magnetkomponenten in gedruckten Cradles; passende nichtmagnetische Dummys für Kontrollversuche;
- Crystal: wechselbarer Modulträger mit vier isolierten Positionen; nominell offen, bis eine klar benannte Testkonfiguration eingesetzt wird.

## Druckwerkstoffe

- PETG für allgemeine Halter bei niedriger Temperatur;
- PA-CF/PC für höher belastete **nicht primär tragende** Modulhalter; Lagerträger bleiben echte Fertigungsteile aus Metall/G10;
- keine elektrisch funktionale Elektrode aus leitfähigem Filament als Ersatz für Metall;
- Gewindeeinsätze nur dort, wo Kriechstrecken und Feldgeometrie nicht unkontrolliert beeinflusst werden.

## Akzeptanzkriterien vor elektrischen Tests

- Rotor dreht unter Schutz frei ohne Kontakt;
- Lager sind fluchtend, keine fühlbare Verspannung;
- Rundlauf und Scheibenschlag dokumentiert;
- alle 24 Sektoren elektrisch getrennt;
- Pot-Gitter/Spirale jeweils separat zugänglich und isoliert;
- alle unbekannten Knoten offen oder mit definierter Config-ID bestückt;
- kein Kunststoffteil übernimmt unbemerkt eine metallische/magnetische Funktion.

## Mechanische Qualitätsgrenzen

- Lagerbohrungen beider Träger müssen nach Montage koaxial geprüft werden; Ziel für den Laboraufbau: kein fühlbares Klemmen und dokumentierter radialer Scheibenschlag.
- Alle rotierenden Metallflansche, Schrauben und Klemmringe müssen symmetrisch montiert und die Rotorbaugruppe anschließend ausgewuchtet werden.
- Gedruckte Teile dürfen weder Lagerhauptlast noch Rotor-Drehmoment übertragen.
- Der Schutz wird aus Polycarbonat/realer Platte gefertigt; gedruckte Ecken sind nur Befestigungselemente.

## Verbindlicher elektrischer Begleitplan

Die mechanische V5-Baugruppe wird **nicht frei nach einem beliebigen Internet-Schaltbild verdrahtet**. Maßgeblich sind:

- [`../electrical/M2_V5_EVIDENCE_WIRING.md`](../electrical/M2_V5_EVIDENCE_WIRING.md)
- [`../electrical/diagrams/M2_V5_EVIDENCE_WIRING.svg`](../electrical/diagrams/M2_V5_EVIDENCE_WIRING.svg)
- [`../electrical/WIRING_VARIANTS.tsv`](../electrical/WIRING_VARIANTS.tsv)
- [`wiring-and-lamella-audit-2026-08-17.md`](wiring-and-lamella-audit-2026-08-17.md)

Der Standardzustand ist `M2-W0` (alle historisch unbekannten Verbindungen offen). `M2-W1` ist die erste konventionell funktionsfähige, strom-/energielimitierte Laborverdrahtung zum Nachweis der realen elektrostatischen Ladungsübertragung. Jede weitere Verbindung erhält eine Config-ID.
