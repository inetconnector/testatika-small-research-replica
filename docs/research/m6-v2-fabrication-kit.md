# M6 V2 — professioneller Fertigungs-Bausatz für die große Maschine

## Ziel

M6 V2 ist die real-materialisierte Baupaket-Schicht über der M6-V1/Hauser-Evidenz. Die bisherige all-solid Darstellung bleibt als Referenz erhalten, ist aber kein Fertigungsmodell mehr.

## Erhaltene Quellenanker

- zwei ca. Ø500 × 5 mm Scheiben;
- 50 Lamellen pro beschriebener Scheibenflächengruppe;
- historische Ziel-Lamelle ca. 0,2 × 20 × 160 mm;
- etwa 8 stationäre Elektroden vorn und 6 hinten;
- zwei große Zylinder mit drei konzentrischen Metallgittern;
- PMMA-/Kunststoff-Isolation zwischen Gittern;
- Zentralrohr/Magnetfamilie und zweilagige bifilare Wicklung als M6a-Quellenfamilie.

## Stabiler mechanischer Aufbau

### Basis

- 760 × 340 × 18 mm steife nichtleitende Strukturplatte;
- Montagebohrungen sind LAB-BUILD und werden nicht als historische Originalbohrungen ausgegeben;
- alle rotierenden Baugruppen müssen auf einer planen, verwindungsarmen Basis ausgerichtet werden.

### Getrennte koaxiale Wellen

Die V2-Laborlösung verwendet bewusst reale Standardteile:

- Innenwelle: Ø12 mm Präzisionsstahl/-edelstahl;
- äußere Hohlwelle: ca. 25 mm OD / 16 mm ID, Präzisionsrohr;
- 6001-2RS für die 12-mm-Welle;
- 6805-2RS für die 25-mm-Hohlwelle;
- **keine gedruckten Dauer-Lagerböcke:** vier hohe Lagerträger werden aus 12-mm-G10/FR4 oder 6061-T6 gefertigt und nach gemeinsamer Bezugsachse bearbeitet;
- die 6805-Träger sitzen näher an den Enden der Hohlwelle (ca. Y=±72 mm), die 6001-Träger weiter außen (ca. Y=±128 mm), damit die Innenwelle unabhängig durch die Hohlwelle läuft;
- vordere PMMA-Scheibe: eigener 25-mm-Metallhub auf der Hohlwelle; hintere PMMA-Scheibe: eigener 12-mm-Metallhub auf der Innenwelle;
- die beiden Scheiben haben deshalb bewusst unterschiedliche Zentralbohrungen und sind mechanisch unabhängig;
- alle Hubs/Klemmnaben sind Metall und müssen als Rotorbaugruppe ausgewuchtet werden.

Diese konkrete Lagerlösung ist **abgeleitete Labor-Mechanik**, nicht behauptete historische Originalmechanik. Sie macht die zwei Scheiben aber real und unabhängig drehbar.

### Rotoren und Lamellen

- beide Scheiben aus echtem gegossenem PMMA Ø500 × 5 mm;
- Lamellen aus realem magnetisch reagierendem/chromstahlartigem Blech entsprechend der Quellenfamilie;
- die 10-Positionen-Lehre ist nur ein wiederverwendbares Ausrichthilfsmittel;
- nach kompletter Lamellenmontage müssen beide Rotoren ausgewuchtet werden;
- Betrieb nur mit vollständigem Schutz.

## Stationäre Elektroden

- Elektroden selbst: leitfähiges Lochblech/Metallgitter;
- gedruckte V2-Halter besitzen verstellbare Positionen und halten den Nichtkontakt-Spalt;
- jede Elektrode bleibt zunächst separat instrumentierbar;
- keine gedruckte Plastikplatte wird als funktionale Elektrode ausgegeben.

## Große Zylinder

Je Zylinder:

- drei echte gerollte Metallgitter;
- zwei echte PMMA-Isolierhülsen;
- gedruckte Zentrierringe und -spider halten konzentrische Abstände;
- reales Zentralrohr/Magnetbauteil gemäß jeweiliger Testkonfiguration;
- echte Kupferlackdraht-Wicklung; das STEP zeigt nur den Wickelpfad;
- alle unbekannten Anschlüsse werden auf offene Testpunkte geführt.

## Kondensatoren

Die früheren massiven `capacitor_can`-Körper sind **keine Fertigungsteile** mehr. V2 liefert ausschließlich:

- einen 78-mm-Modulhalter;
- einen 62-mm-Modulhalter;
- Befestigungs-/Terminalraum für austauschbare reale, gekapselte Versuchs-Kondensatormodule.

Wert, Dielektrikum und historische interne Topologie bleiben unbekannt und dürfen nicht durch eine Kunststoffdose vorgetäuscht werden.

## Antrieb und Schutz

- externer Niederspannungs-Labormotor auf verstellbarem Halter;
- zwei getrennte Riemenebenen für Gegenrotation, eine offen und eine gekreuzt;
- reale 3–4-mm-PU-Rundriemen;
- die CAD-Assembly modelliert **keine starren Fake-Riemenstäbe** mehr, sondern nur die Riemenscheiben/Schnittstellen;
- Eingangsleistung des Motors muss separat gemessen werden;
- vollständige Polycarbonat-Schutzhaube vor jedem Drehversuch.

## Akzeptanzkriterien vor elektrischen Tests

- beide Rotoren unabhängig frei drehbar;
- Lagerblöcke koaxial, keine Verspannung;
- Rotoren ausgewuchtet und mit dokumentiertem Scheibenschlag;
- alle 14 Statoren berührungslos;
- drei Gitter pro Zylinder mechanisch konzentrisch und elektrisch separat zugänglich;
- Wicklungen/Metallteile real ausgeführt, nicht gedruckt;
- Kondensator-/Crystal-Positionen modular und klar als unbekannt/experimentell gekennzeichnet;
- Schutz vollständig geschlossen.

## Mechanische Qualitätsgrenzen

- Die vier Lagerträger werden nicht nach einzelnen Druckmaßen ausgerichtet, sondern auf einer gemeinsamen Wellenachse montiert und erst dann final gebohrt/gerieben bzw. über Präzisionslagergehäuse ausgerichtet.
- Hohlwelle und Innenwelle müssen ohne gegenseitiges Schleifen frei laufen; axialer Abstand der beiden Rotorebenen wird mit Metall-Distanzringen eingestellt.
- Für die 500-mm-Rotoren sind alle tragenden Lager-, Wellen- und Hubteile echte Metall-/G10-Fertigungsteile; 3D-Druck bleibt auf Lehren, Clips, Zentrierringe und Modulhalter beschränkt.
- Kein Riemen wird als starrer CAD-Stab ausgegeben; die Assembly zeigt nur Riemenscheiben und Schnittstellen für echte flexible PU-Rundriemen.

## Verbindlicher elektrischer Begleitplan

Die M6-V2-Baugruppe wird nicht nach einem beliebigen im Internet kursierenden Vollschaltbild hart verdrahtet. Maßgeblich sind:

- [`../electrical/M6_V2_EVIDENCE_WIRING.md`](../electrical/M6_V2_EVIDENCE_WIRING.md)
- [`../electrical/diagrams/M6_V2_EVIDENCE_WIRING.svg`](../electrical/diagrams/M6_V2_EVIDENCE_WIRING.svg)
- [`../electrical/WIRING_VARIANTS.tsv`](../electrical/WIRING_VARIANTS.tsv)
- [`../electrical/LAMELLA_TEST_MATRIX.tsv`](../electrical/LAMELLA_TEST_MATRIX.tsv)
- [`wiring-and-lamella-audit-2026-08-17.md`](wiring-and-lamella-audit-2026-08-17.md)

`M6-W0` hält alle ungesicherten Knoten offen. `M6-W1` ist der erste konventionell funktionsfähige Drei-Gitter-/Variable-Capacitance-Test. `M6-W2` bildet die Hauser-Anschlussfamilie als Patchkonfiguration ab. `M6-W3` ist eine separat gekennzeichnete Rimstar-Reproduktion. Die von Cathomen nicht erklärte obere Stufe bleibt als `M6-W5` BLACK-BOX-Schnittstelle offen.

## Lamellen sind jetzt ein kontrollierter Versuchsparameter

Die Video-/Marinov-/Hauser-Linie rechtfertigt **nicht**, irgendein einzelnes Fe-Ni-Produkt als Originalmaterial festzuschreiben. Stattdessen wird für die große Maschine die Material-/Geometrie-Matrix aus `LAMELLA_TEST_MATRIX.tsv` verwendet:

- chromstahlartige magnetische Kontrolle;
- Fe-Ni-Familien als Zusammensetzungs-Sweep;
- jeweils entmagnetisiert vs schwach magnetisiert;
- identisches Material als Vollfolie, Lochblech und Drahtgitter;
- dokumentierter Oberflächen-/Beschichtungszustand.

So wird getrennt geprüft, ob der beobachtete Effekt aus Legierung, Magnetisierung, Perforation, Oberflächenzustand oder deren Kombination stammt.
