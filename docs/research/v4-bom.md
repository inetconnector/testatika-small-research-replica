# V4 Stückliste — Best-evidence M2

Diese Stückliste gehört zur nominellen V4-Baugruppe `Testatika_M2_V4_BEST_EVIDENCE`.

## 1. Druck-/CAD-Teile

| Teil | Menge | Hinweis |
|---|---:|---|
| `rotor_24wire_floating_R0_v4` | 1 | Nominalrotor; 20/25 optional |
| `hub_disk_v4` | 2 | Vorder-/Rückseite |
| `hub_arc_pair_v4_video_refined` | 1 | video-derived; elektrische Funktion offen |
| `pot_outer_shell_v4` | 2 | mechanisch |
| `pot_grid_former_v4` | 2 | Träger für echtes Metallgitter |
| `pot_acrylic_sleeve_jig_v4` | 2 | Maßkörper, nicht finaler HV-Isolator |
| `pot_spiral_mandrel_v4` | 2 | Wickel-/Montagehilfe |
| `pot_terminal_lid_2wire_v4` | 2 | genau zwei externe Pot-Anschlüsse |
| `outer_panel_layered_v4` | 2 | video-derived Mehrlagengeometrie |
| `lower_central_cage_v4` | 1 | video-derived Zentralmodul |
| `top_crystal_carrier_4pos_v4` | 1 | Blackbox-Forschungsträger |
| `horseshoe_magnet_shape_v4` | 2 | Form-/Einbauposition |
| `horseshoe_dummy_v4` | 2 | Blindkontrolle |
| `guard_post_v4` | 4 | Schutzhaube |

Die komplette STEP/STL-Baugruppe enthält zusätzlich sichtbare Träger-, Feder-, Pickup- und Crossbar-Geometrie aus dem V3-Fotobasismodell; diese werden in der kompletten Baugruppe positionsrichtig mitgeführt.

## 2. Mechanik

- 8-mm-Welle, gerade, ca. 220–260 mm;
- 2 geeignete Lager, V2-Baseline 608-2RS;
- M3/M4-Schrauben, Muttern, Unterlegscheiben;
- Distanzhülsen und isolierende Abstandshalter;
- transparente Schutzhaube;
- stabile nichtleitende Basis/Träger, falls gedruckte Basis nur als Schablone genutzt wird.

## 3. Rotor

- ca. 1-mm-Kupferdraht für 24 einzelne Sektoren;
- Reserve für 20/25-Sektor- und R4-Forschungsrotoren;
- Schrumpfschlauch/isolierende Fixierung nur dort, wo sie die Feldgeometrie nicht unbeabsichtigt verändert;
- Multimeter/Megohmmeter bzw. geeignete Isolationsprüfung für Sektor-zu-Sektor-Kontrolle bei niedriger Prüfenergie.

**Pflicht:** Jeder Rotordraht bleibt elektrisch von jedem Nachbarsektor getrennt.

## 4. Zwei Seiten-Pots

Je Pot:

- Metallgaze oder dokumentiertes leitfähiges Gitter für die äußere Elektrode;
- echtes PMMA-/Acrylrohr oder ein anderes explizit dokumentiertes Isolierrohr;
- dickere Kupferleitung für die innere Spirale;
- 2 isolierte Mess-/Anschlussbuchsen: `GRID`, `SPIRAL`;
- keine zusätzliche versteckte dritte Elektrode in der M2-Nominalbaseline.

Optional für Forschung, aber **nicht** Baseline:

- austauschbare andere Gittergeometrien;
- anderes Dielektrikum;
- definierte PMMA-Vorkonditionierung;
- R/C/Diode zwischen GRID und SPIRAL.

## 5. Stator-/Panel-Einsätze

- leitfähige Metallgaze bzw. Lochblech für aktive Inserts;
- identisch geformte Vollfolien-Kontrolle;
- isolierende Dummy-Inserts;
- dunkle PMMA-/Backing-Kontrolle;
- dokumentierte Anschlussleitungen mit ausreichend Abstand.

## 6. Crystal-Blackbox

Für die nominelle mechanische Replik ist **kein bestimmtes Crystal-Material vorgeschrieben**.

Für kontrollierte Niedrigenergieversuche:

- offene Steckbrücke;
- Kurzschlussbrücke;
- Hochwertwiderstand;
- Kondensator;
- passive Diode;
- antiparallele Dioden;
- geeigneter historischer Kristalldetektor als Vergleich.

Jeder Einsatz erhält eine eindeutige Config-ID.

## 7. Magnete

- 2 kleine Hufeisenmagnete mit dokumentierter Geometrie/Feldstärke für den sichtbaren M2-Bauzustand;
- 2 gleich geformte nichtmagnetische Dummys für Blind-/A/B-Versuche.

## 8. Messausstattung

Mindestens:

- optischer Encoder/Tachometer;
- Drehmoment-/Kraftmessmöglichkeit;
- hochohmige geeignete Spannungsmessung;
- strombegrenzte Elektrostatik-/Laborquelle nur für kontrollierte Teiltests;
- Temperatur-/RH-Sensor;
- Kapazitäts-/LCR-Messung;
- sichere Entladevorrichtung;
- bei Corona-Tests geeignete Strommessung und Abschirmung.

## 9. Bewusst nicht als Einkaufsvorgabe spezifiziert

- vermeintliches „Original-Crystal“;
- radioaktive Materialien;
- Tesla-Spulen/HF-Stufe;
- offene netzbetriebene Hochspannungserzeugung;
- Großmaschinen-3-Gitter/Magnetröhren-Zylinder aus Hausers M6a;
- 1-kΩ-Nachbarring als M2-Nominalrotor.
