# V4 — Best-evidence M2 research replica

## Zweck

V4 ist der **derzeit bestbelegte mechanisch-elektrische Forschungs-Bauzustand** der ersten kleinen Testatika, die Stefan Marinov untersucht und beschrieben hat (`M2`).

V4 bedeutet nicht, dass der historische Originalschaltplan wiedergefunden wurde. Die Konstruktion fixiert nur solche Eigenschaften, die durch die stärksten M2-Quellen hinreichend gestützt sind, und lässt ungelöste Details reversibel.

## Kanonische V4-Baseline

| Bereich | V4-Baseline | Evidenzstatus |
|---|---|---|
| Maschine | Marinovs erste kleine Maschine `M2` | hoch |
| Rotor | eine Scheibe, ca. 200 mm | hoch |
| Sektorzahl | nominal 24; 20/25 als Alternativen | mittel-hoch |
| Sektorleiter | ca. 1-mm-Kupferdraht | hoch für Marinovs Wortlaut |
| elektrische Sektorverbindung | **jeder Draht einzeln floating; keine Nachbar-Ringverbindung** | hoch: Marinov-Scan `connected to nothing` |
| Drahtführung | R0 als konservative Bau-Baseline | historische Route weiterhin unbekannt |
| alternative Drahtführung | R4 als Forschungsrotor | quellenübergreifend testwürdig, nicht M2-belegt |
| Bürsten | keine Reib-/Sammelbürsten | sehr hoch |
| Seiten-Pots | zwei | hoch |
| Pot-Innenklasse | äußeres Gitter + Isolator/PMMA + innere dicke Cu-Spirale | hoch-mittel bis hoch |
| Pot-Anschlüsse | **zwei externe Anschlüsse pro Pot** | hoch: direkter Marinov-Scan |
| Pot-Tesla-Funktion | nicht Teil der Baseline | Marinov widerspricht Tesla-/AC-Deutung |
| konventioneller Antriebsmotor | **nicht Teil der historischen Baseline** | direkter Marinov-Hinweis |
| Magnete | zwei Hufeisenmagnete an der sichtbaren ersten Maschine | hoch für Präsenz, Funktion unbekannt |
| Topmodul | `crystal` als Blackbox | Begriff hoch, Funktion/Material unbekannt |
| Hub-Bögen | zwei C-förmige sichtbare Bauteilkandidaten | video/photo-derived |
| Außenpanels | mehrlagige perforierte Struktur + feineres Inset + längliches Element | video/photo-derived |
| unteres Zentralmodul | perforierter Käfig/Prisma als beste visuelle Rekonstruktion | video/photo-derived |
| Energieüberschuss | nicht behauptet | unbekannt / experimentell zu prüfen |

## Warum R0 die Nominal-Baseline ist

Marinov betont, dass die Art, wie die Drähte **durch die Scheibe** geführt sind, wichtig sei, liefert aber keine vollständige reproduzierbare Route. Holzherr beschreibt bei anderen Maschinen mehrfaches Seitenwechseln.

Deshalb gilt:

- `R0` = konservativster, minimal spekulativer Bauzustand;
- `R4` = wichtigster alternativer Forschungsrotor;
- **keine** Route wird als historisch bewiesene M2-Originalführung bezeichnet.

Die elektrische Baseline ist davon getrennt: auch bei R4 bleiben die einzelnen Sektordrähte voneinander isoliert/floating.

## V4-CAD

Generator:

`cad/generate_v4_best_evidence_m2.py`

Ausgabe:

`hardware/experimental/v4-best-evidence-m2/`

### Einzelteile

- `rotor_20wire_floating_R0_v4`
- `rotor_24wire_floating_R0_v4`
- `rotor_25wire_floating_R0_v4`
- `rotor_24wire_floating_R4_v4_research`
- `hub_disk_v4`
- `hub_arc_pair_v4_video_refined`
- `pot_outer_shell_v4`
- `pot_grid_former_v4`
- `pot_acrylic_sleeve_jig_v4`
- `pot_spiral_mandrel_v4`
- `pot_terminal_lid_2wire_v4`
- `outer_panel_layered_v4`
- `lower_central_cage_v4`
- `top_crystal_carrier_4pos_v4`
- `horseshoe_magnet_shape_v4`
- `horseshoe_dummy_v4`
- `guard_post_v4`

### komplette Baugruppen

- `Testatika_M2_V4_BEST_EVIDENCE.step/.stl`
- `Testatika_M2_V4_R4_RESEARCH.step/.stl`

Die erste Datei ist die nominelle V4-Baseline. Die zweite ändert gezielt nur den Rotor-Bohr-/Routingraum auf R4.

## Crystal-Modul

Die M2-Quelle stützt den Begriff `crystal`, aber weder Material noch I-V-Kennlinie noch vollständige Anschlusstopologie sind bekannt.

V4 verwendet deshalb einen Blackbox-Träger:

- in der sichtbaren Nominalbaugruppe sind zwei innere Pfosten bestückt;
- der Träger besitzt vier isolierbare Forschungspositionen;
- zusätzliche Positionen sind **Forschungsoption**, nicht historische Behauptung;
- jede elektrische Einlage muss eindeutig als `open`, `short`, `R`, `C`, `diode`, `crystal detector` usw. protokolliert werden.

## Pot-Modul

Jeder V4-Pot soll physisch vier Ebenen trennen:

1. mechanische Außenhülle;
2. echtes leitfähiges äußeres Gitter;
3. echtes isolierendes Rohr, bevorzugt PMMA/Acryl für die historische Materialklasse;
4. echte innere Kupferspirale.

Das gedruckte `pot_acrylic_sleeve_jig_v4` ist ein Maß-/Montagekörper, **kein Ersatz für einen qualifizierten elektrischen Isolator**.

Die V4-Deckel haben genau zwei historische Außenanschlusspositionen: `GRID` und `SPIRAL`.

## Rotorleiter

Die STL/STEP-Datei bildet die Scheibe und Führungsbohrungen ab. Die leitfähigen Sektoren werden **nicht als elektrisch verbundene Druckgeometrie** erzeugt.

Für den realen Rotor:

- jeden Draht separat einsetzen;
- ca. 1 mm Cu als Nominalmaterial;
- zwischen unterschiedlichen Sektoren vor Einbau Durchgang prüfen: **kein Durchgang**;
- nach Einbau nochmals jeden Sektor gegen beide Nachbarsektoren und Welle prüfen;
- Messwert protokollieren.

## Laborantrieb

V4 enthält keinen eingebauten historischen Elektromotor.

Für Messungen ist ein externer Laborantrieb zulässig, wenn:

- mechanisch vollständig abkoppelbar;
- seine Eingangsleistung separat messbar;
- keine elektrische Verbindung zur Maschine außer definierter Messtechnik;
- die Messung mit abgekoppeltem Antrieb wiederholbar ist, wenn der Versuch dies erfordert.

Ein Laborantrieb ist **Instrumentierung**, nicht Bestandteil des behaupteten Originals.

## Was V4 bewusst nicht festlegt

1. exakte historische through-disc Route;
2. genaue Pot-Kapazität und interne Polarität;
3. vollständige stationäre Elektroden-Node-Map;
4. elektrische Funktion der Hub-Bögen;
5. Crystal-Material und Kennlinie;
6. Magnetfunktion;
7. exakte Priming-/Startprozedur;
8. Energiequelle der historischen Leistungsbehauptungen.

## Definition „fertig“

V4 gilt als **mechanisch vollständiger best-evidence Forschungsbau**, wenn:

- alle V4-CAD-Dateien aus dem Generator reproduzierbar entstehen;
- der Nominalrotor elektrisch floating aufgebaut ist;
- beide Pots echten Grid-/Dielectric-/Spiral-Aufbau und zwei externe Anschlüsse besitzen;
- keine reibenden Sammler eingebaut sind;
- Crystal, Magnete, Hub-Bögen und alternative Rotorroute austausch-/messbar bleiben;
- Schutzhaube und definierte Messpunkte vorhanden sind;
- jede elektrische Topologie mit Config-ID dokumentiert wird.

Historische 1:1-Gewissheit bleibt trotzdem durch `docs/REPLICATION_STATUS.md` begrenzt.
