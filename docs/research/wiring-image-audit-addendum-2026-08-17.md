# Verdrahtungsbild-Audit — Addendum 2026-08-17

Dieses Addendum ergänzt `wiring-and-lamella-audit-2026-08-17.md` um weitere **eigenständige Rekonstruktions-/Versuchsbildfamilien**, die beim Internet-Crawl gefunden wurden. Es verhindert insbesondere, dass ein technisch funktionierender Nachbauversuch mit einem authentischen Methernitha-Schaltplan verwechselt wird.

## A. Sven Bönisch, ELEKTRIE 5–8/2003

Publikation:

`Electrostatic Discharge Power Transformation – An Approach to Understand the Working Principles of the “Thestatika” Free Energy Device`, Sven Bönisch, ELEKTRIE No. 5–8 (2003), ISSN 0013-5399.

Ein öffentlicher Spiegel enthält die vollständige sieben-seitige Publikation mit mehreren Schaltbildern:

- Fig. 2 — Blockschaltung `electrostatic generator → HV transformation device → load`;
- Fig. 3 — rekonstruierter brushless electrostatic generator;
- Fig. 7 — transmission-line transformer;
- Fig. 9 — serielles Resonanz-/ESD pulse-forming network;
- Fig. 11 — vollständige Push-Pull-HV-Transformationsschaltung;
- Fig. 12/13 — mechanische und symmetrische Lastkonfiguration.

Besonders wertvoll ist die wissenschaftliche Grenze des Autors selbst:

- sein System basiert ausschließlich auf **bekannter Elektrodynamik** und soll daher nicht über 100 % Wirkungsgrad liegen;
- der Laboraufbau wird mechanisch per Handkurbel angetrieben;
- die Scheiben/Leydener Flaschen müssen zunächst geladen werden;
- die gemessene mittlere Lastleistung lag in der beschriebenen Konfiguration bei ungefähr 10 mW gegenüber einer theoretisch erwarteten Generatorleistung um 80 mW;
- er berichtet ausdrücklich, **keinen Over-Unity-Effekt** gefunden zu haben.

Damit ist Bönisch eine sehr gute **Engineering-Control-Familie**: Sie zeigt, wie eine hochimpedante elektrostatische Quelle über Impuls-/Resonanztechnik eine niederimpedantere Last treiben kann, ohne Energieerhaltung zu verletzen. Sie ist aber kein Nachweis dafür, dass Methernitha genau diese ~53–80-MHz-Übertragungsleitung verwendete.

**Repository-Einstufung:** `S2-ENGINEERING-CONTROL`, nicht historische Baseline.

## B. Jorge-Resines zugeschriebene Clone-Fotofamilie

Öffentliche Sammlung:

`https://rimstar.org/sdenergy/testa/testareplicationjr.htm`

Die Seite zeigt zahlreiche Fotos, eine Hufeisenmagnet-Spule, behauptete 240-V-DC-Ausgabe und am Ende ein Bild mit der Beschriftung `Plan`. Der Seitenautor sagt jedoch selbst, dass ihm außer den Bildern, wenigen deutschen Bildunterschriften und einer unsicheren Zuordnung zu Jorge Resines keine weiteren Details vorliegen.

**Konsequenz:**

- wertvoll als Dokumentation eines späteren Clone-/Replikationsversuchs;
- keine gesicherte Provenienz für interne Verbindungen;
- Leistungsbeschriftungen sind keine unabhängige Leistungsmessung;
- `Plan` darf nicht als Methernitha-Originalplan etikettiert werden.

**Repository-Einstufung:** `S3-CLONE-PHOTOSET`.

## C. Rimstar 276-mm Disk / Grid-Versuche

Öffentliche Versuchsserie:

`https://rimstar.org/sdenergy/testa/276diskg1.htm`

Diese Serie ist für unsere Laborplanung relevant, weil sie:

- eine reale rotierende Scheibe mit Grid-/Pot-Aufbau verwendet;
- einen expliziten Verdrahtungsplan und Oszilloskopkanäle dokumentiert;
- Messungen mit externer Van-de-Graaff-Anregung zeigt;
- die Signale vor, während und nach externer HV-Anregung vergleicht.

Der Autor bezeichnet die Ergebnisse selbst als **sehr vorläufig** und als Test einer Theorie. Deshalb stärkt die Seite nicht den historischen Methernitha-Knotenplan, ist aber ein brauchbares Beispiel dafür, wie die Grid-/Pot-Hypothese instrumentiert werden kann.

**Repository-Einstufung:** `S2-REPLICATION-DATA`.

## D. Rimstar Variable-Capacitance / Charge-Pump-Familie

Öffentliche Seite:

`https://rimstar.org/sdenergy/testa/varcapcircuit1.htm`

Diese Bildfamilie ordnet sichtbare Testatika-Baugruppen einem bekannten **variable-capacitor charge-pump**-Prinzip zu. Der Ansatz ist gerade deshalb nützlich, weil er eine konventionelle Vergleichsschaltung bereitstellt:

- variable Kapazität;
- Dioden/Gleichrichtung;
- gespeicherte Ladung;
- definierter Energieinput.

Sie ist eine **Theorie-/Vergleichsfamilie**, keine Quelle für den Originalkabelbaum.

**Repository-Einstufung:** `S2-CONVENTIONAL-COMPARATOR`.

## E. Was als `alle Bilder` praktisch bedeutet

Eine mathematisch vollständige Erfassung jedes jemals gespiegelt, umbenannt oder neu komprimiert veröffentlichten Testatika-Bildes ist im offenen Web nicht beweisbar. Für die Rekonstruktion ist das auch nicht die sinnvolle Einheit.

Der Audit erfasst deshalb die **unterschiedlichen technischen Bild-/Schaltfamilien**, die bei breit angelegten Suchläufen auffindbar sind, und dedupliziert ihre Kopien:

1. direkte Fotos/Video-Stills der Maschinen;
2. Marinov-Abbildungen und Texte;
3. Albert-Hauser-Besucherzeichnungen 3279 / connection views;
4. Don-Kelly-/Magnets-Schemata und deren Webkopien;
5. RexResearch `schemat1/schemat2`-Familie;
6. Paul-Potter-`Full Circuit`;
7. Wikimedia-/Atlas-/Blog-Neuzeichnungen;
8. Sven-Bönisch-2003-Elektrostatik-/HV-Transformationsschaltungen;
9. Rimstar Drei-Gitter-/Pot-, Variable-Capacitance- und Disk-Testfamilien;
10. Jorge-Resines-zugeschriebene Clone-Fotofamilie;
11. weitere Pająk/Frolov/sekundäre theoretische Zeichnungen, die nur als Hypothesenquellen geführt werden.

Neue Funde werden nur dann als **neue Evidenz** gezählt, wenn sie eine eigenständige Provenienz oder neue technische Information liefern. Ein weiterer Webmirror desselben Kelly- oder Potter-Bildes zählt nicht als Bestätigung.

## F. Konsequenz für die aktuelle Verdrahtung

Bönisch bestätigt eine wichtige methodische Entscheidung des Repositorys: Ein elektrostatischer Generator plus Spannungs-/Impedanzwandlungsstufe kann als **konventionelles, messbares Gesamtsystem** aufgebaut und charakterisiert werden, ohne daraus einen Energieüberschuss abzuleiten.

Darum bleiben die kanonischen `M2-W1`- und `M6-W1`-Pfade absichtlich einfacher und niederenergetischer als Bönischs Funken-/HF-Aufbau. Erst wenn die passive Ladungs-/Kapazitätskopplung reproduzierbar verstanden ist, können Resonanz- oder Impulswandler als **separate, vollständig bilanzierte** Vergleichsmodule untersucht werden.
