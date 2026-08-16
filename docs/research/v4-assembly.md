# V4 Montage — Best-evidence M2

## Ziel

Diese Reihenfolge baut zuerst die **mechanische, quellennahe M2-Baseline**. Elektrische Hypothesen werden erst danach als reversible Module ergänzt.

## A. Mechanischer Rahmen

1. Basis auf eine plane Unterlage montieren.
2. Rück-/Trägerplatte rechtwinklig ausrichten.
3. Welle und Lager ohne Rotor montieren.
4. Rundlauf und Lagerreibung dokumentieren.
5. Schutzhaubenpfosten montieren, Haube zunächst noch abnehmbar lassen.

Akzeptanz:

- Welle frei drehbar;
- kein fühlbares Klemmen;
- kein Kontakt zwischen bewegten und späteren stationären Teilen.

## B. Nominalrotor

Nominal:

`rotor_24wire_floating_R0_v4`

1. Rotor entgraten und auf Risse prüfen.
2. 24 einzelne ca. 1-mm-Cu-Drähte einsetzen.
3. **Keine** Nachbarverbindung herstellen.
4. Jeden Draht einzeln mechanisch sichern.
5. Durchgangsmatrix prüfen:
   - Sektor `i` ↔ Sektor `i+1`: offen;
   - Sektor `i` ↔ Welle: offen;
   - Sektor `i` ↔ Hub-Bogen: offen, solange nicht explizit in einem späteren Versuch verbunden.
6. Hubscheiben montieren.
7. C-förmige Hub-Bögen als eigene Bauteile montieren; zunächst elektrisch floating.
8. Rotor auf Welle montieren und auswuchten.

Vor jedem elektrischen Versuch erneut Sektortrennung prüfen.

## C. Stationäre sichtbare Strukturen

1. Mehrlagige Außenpanels links/rechts montieren.
2. Feines Inset und längliches Element als separat instrumentierbare Ebenen behandeln, soweit der reale Bau dies erlaubt.
3. Obere Türme/Federbaugruppen montieren.
4. schräge berührungslose Pickup-/Feldelektroden montieren.
5. Crossbars und untere symmetrische Platten montieren.
6. unteren perforierten Zentral-Käfig montieren.

Abstand zum Rotor zunächst großzügig; erst nach mechanischem Rundlauftest schrittweise reduzieren.

## D. Seiten-Pots

Je Seite:

1. mechanische Pot-Hülle;
2. echtes äußeres leitfähiges Gitter;
3. echtes PMMA-/Acryl-Dielektrikum;
4. innere dicke Kupferspirale;
5. zweipoligen V4-Deckel montieren;
6. Anschlüsse eindeutig markieren:
   - `GRID-L` / `SPIRAL-L`;
   - `GRID-R` / `SPIRAL-R`.

Vor Kopplung an andere Baugruppen messen:

- Kapazität;
- Leckstrom;
- Verlustfaktor soweit möglich;
- Isolationszustand;
- Entladeverhalten.

## E. Hufeisenmagnete

Für die visuelle M2-Baseline:

1. zwei dokumentierte Hufeisenmagnete in den vorgesehenen Positionen montieren;
2. Feldstärke und Orientierung protokollieren;
3. passende nichtmagnetische Dummys bereithalten.

Magnetfunktion wird **nicht** aus der Präsenz abgeleitet.

## F. Crystal-Blackbox

1. oberen Blackbox-Träger montieren.
2. In der visuellen Baseline nur die zwei inneren sichtbaren Pfosten bestücken.
3. elektrische Funktion zunächst `OPEN`.
4. zusätzliche isolierte Forschungspositionen bleiben unbeschaltet.

Erst nach vollständiger mechanischer/kapazitiver Basismessung einzelne Blackbox-Einsätze testen.

## G. Keine Reibkontakte

Vor dem ersten Lauf kontrollieren:

- kein Draht/Brush berührt den Rotor;
- keine Feder schleift;
- keine Elektrode streift bei maximalem Scheibenschlag;
- Schutzhaube montiert.

## H. Basis-Messzustand `V4-B0`

Der erste reproduzierbare Zustand soll **ohne erfundene interne Schaltung** erfolgen:

- Rotor: `24 / floating / R0`;
- Hub-Bögen: floating;
- Pots: GRID und SPIRAL jeweils separat zugänglich, untereinander offen;
- Crystal: open;
- Magnete: vorhanden;
- externe Last: keine;
- keine externe HV außer Messsignalen mit geringer Energie;
- kein permanenter Antriebsmotor.

Dieser Zustand liefert:

- mechanische Auslaufzeit;
- `C(theta)`-Matrix;
- parasitäre Kopplungen;
- Oberflächenpotential;
- Feuchteabhängigkeit;
- Einfluss von Magnet vs Dummy.

## I. Definierte Forschungsvarianten

Nach `V4-B0` wird immer **nur eine Variable** geändert.

Beispiele:

- `V4-R4`: R4-Rotor statt R0;
- `V4-MAG0`: nichtmagnetische Dummys;
- `V4-ARC0`: Hub-Bögen entfernt/isolierender Dummy;
- `V4-XDIODE`: Crystal-Blackbox mit Diode;
- `V4-POT-R`: definierter Widerstand GRID↔SPIRAL;
- `V4-MESH/FOIL`: gleicher Träger, anderes Elektrodeninsert;
- `V4-PMMA-COND`: dokumentierte PMMA-Vorkonditionierung.

## J. Externer Laborantrieb

Falls ein rpm-Sweep benötigt wird:

- Antrieb außerhalb der historischen Baugruppe;
- mechanisch leicht abkoppelbare Kupplung;
- Eingangsleistung separat messen;
- keine gemeinsame Masse/Versorgung ohne bewusst dokumentierte Messkopplung;
- nach dem Sweep Kupplung entfernen und Leerlauf erneut messen.

## K. Elektrische Sicherheit

`docs/research/safety.md` ist verbindlich.

Insbesondere:

- nur strombegrenzte gekapselte Labor-/Lehrquellen;
- keine offenen netzbetriebenen HV-Kaskaden;
- kleine gespeicherte Energie;
- vor Berührung entladen und Entladezustand prüfen;
- Rotor nur unter Schutzhaube.

## Fertigkriterium

Die mechanische V4-Replik ist fertig, wenn:

- Nominalbaugruppe ohne Kontakt läuft;
- jeder Rotordraht floating verifiziert ist;
- beide Pots zweipolig aufgebaut und charakterisiert sind;
- Hub-Bögen/Crystal/Magnete reversibel testbar sind;
- Config-ID und Messpunkte dokumentiert sind;
- keine unbekannte Verbindung stillschweigend als „Original“ eingebaut wurde.
