# M2-V4.6 — Radioionisation als Gate/Bias, nicht als Leistungsquelle

## Anlass

Sekundäre Testatika-Diskussionen behaupten teilweise, in "Crystal"-/Pot-Bereichen könnten radioaktive Mineralien oder Kristalle enthalten gewesen sein. Eine Rimstar-Theorieseite nennt unter anderem die spekulative Idee von "mountain crystals" und Beta-Emission; derselbe Quellenkomplex berichtet aber auch, dass Paul Baumann auf die konkrete Frage nach Radiumchlorid als Energiequelle mit "nein" geantwortet habe. Diese Aussagen sind **keine Primärbeweise** für radioaktives Material in der historischen Maschine.

V4.6 prüft deshalb nur die physikalisch konventionelle Frage:

> Könnte eine schwache radioaktive Quelle als Luft-Ionisator einen extrem hochohmigen elektrostatischen Lade-/Schaltpfad stabilisieren, ohne selbst die Ausgangsleistung zu liefern?

## Glühstrumpf als physikalischer Analogiekandidat

Historische Gasglühstrümpfe konnten Thorium enthalten. Thorium-232 selbst zerfällt überwiegend durch Alpha-Emission; in einer gealterten Thorium-Zerfallsreihe treten zusätzlich Beta- und Gamma-emittierende Tochterprodukte auf.

Daher ist "alter Glühstrumpf = Beta-Strahler" zu grob. Elektrostatisch interessanter ist die **starke lokale Ionisation durch Alpha-Teilchen**, ergänzt durch Tochterstrahlung.

Radioaktive Alphaquellen wurden und werden technisch tatsächlich als Static-Eliminator/Ionisator eingesetzt: Die Strahlung ionisiert Luft und macht einen sonst extrem hochohmigen Luftspalt leitfähiger. Das ist die relevante technische Analogie.

## Harte Energietrennung

Die mittlere Energie zur Bildung eines Ionenpaars in trockener Luft liegt bei rund 33.97 eV.

Für Aktivität `A`, tatsächlich in der Luft deponierte Energie `E_dep` und Sammelwirkungsgrad `eta` gilt als ideale Sättigungsstrom-Obergrenze:

```text
P_rad = A * E_dep
I_sat = eta * P_rad / (33.97 J/C)
```

Beispiel:

```text
A = 10 kBq
E_dep = 5 MeV/Zerfall
eta = 1 (extrem optimistische Obergrenze)
```

liefert nur

```text
P_rad ~= 8.0 nW
I_sat ~= 0.236 nA.
```

Das ist energetisch winzig, aber für einen elektrostatischen Knoten von nur `100 pF` nicht automatisch irrelevant. Als reine Strom-/Kapazitäts-Skala gilt bei bereits vorhandenem Sammelfeld

```text
dV/dt = I/C ~= 2.36 V/s.
```

Bei 15 rpm dauert eine Umdrehung 4 s; die zugehörige reine Ladungsstrom-Skala entspräche knapp 9.4 V pro Umdrehung an 100 pF.

### Präzisierung durch V4.7

Diese lineare `I/C`-Skala darf **nicht** als unbegrenztes Hochladen eines isolierten Kondensators aus der Radioquelle verstanden werden. Sobald zusätzliche Feldenergie aufgebaut wird, gilt gleichzeitig

```text
1/2 * C * V^2 <= P_rad * t.
```

Für 100 pF und 8.01 nW ergibt das selbst bei 100 % elektrischer Umsetzung:

```text
Vmax(40 s) ~= 80.05 V
Zeit bis 100 V >= 62.4 s.
```

Die vollständige energiebegrenzte Integration in die V4.2-Kapazitätsmatrix steht in

`docs/research/m2-v4-7-radioionization-integration.md`.

## Warum das zur Testatika passen könnte

Eine Radioionisationsquelle müsste nicht den Laststrom erzeugen. Sie könnte stattdessen:

```text
radioaktive Ionisation
        -> wenige pA/nA reproduzierbarer Luftstrom
        -> floating Grid/Pickup-Knoten lädt/entlädt sich definiert
        -> Crystal-/Diodenschwelle wird in richtiger Rotorphase erreicht
        -> vorhandene HV-/Feldenergie wird umgeschaltet
```

Damit wäre sie eher das elektrostatische Gegenstück zu einem **Gate-/Biasstrom** als zu einer Batterie.

Das passt qualitativ zu drei bereits untersuchten Punkten:

1. sehr kleine Steuerleistung kann einen größeren vorhandenen Energiepfad kommutieren;
2. eine Metallplatte kann die Feldlinien und damit die Sammlung der erzeugten Ionen verändern;
3. trockene Luft reduziert gewöhnliche Leckströme und kann deshalb die Wirkung eines sehr kleinen definierten Ionisationsstroms gegenüber parasitären Leckpfaden sichtbarer machen.

Punkt 3 ist eine Hypothese, kein historischer Nachweis.

## Metallplatten-Vorhersage

In einer ionisationskammerartigen Geometrie erzeugt die Quelle zunächst Ionenpaare; das elektrische Feld bestimmt dann, welcher Anteil an welchem Gitter gesammelt wird.

Eine rückseitige Metallplatte kann daher gleichzeitig

```text
E(r) verändern
-> Driftpfade der Ionen verändern
-> Rekombination/Wandverlust verändern
-> gerichteten Sammelstrom am Pickup reduzieren
-> Crystal-Kommutation unter Schwelle drücken.
```

Die Platte muss dafür weder geerdet sein noch die Ausgangsenergie absorbieren.

## Was die Hypothese NICHT erklärt

Ein kBq-artiger Thorium-/Glühstrumpfbereich liefert selbst nur Nanowatt bis höchstens sehr kleine Mikrowatt-Strahlungsleistung. Er kann deshalb **keine** behaupteten 100 W / 300 W direkt speisen.

Falls die historische hohe Ausgangsleistung real war, müsste weiterhin ein separater Hauptenergiepfad existieren. Radioionisation könnte nur dessen Gate/Bias/Kommutation erklären.

## Wichtige Korrektur zur "stimulierten Beta-Strahlung"

Ein gewöhnliches elektrostatisches Feld im kV- bis zig-kV-Bereich kann einen normalen Quarz- oder Bergkristall nicht dazu bringen, plötzlich nukleare Beta-Zerfälle als Leistungsquelle zu erzeugen. Kernzerfälle liegen auf MeV-Energieskalen; die Feldenergie über atomare oder nukleare Distanzen ist bei solchen Feldstärken viele Größenordnungen kleiner.

Physikalisch sinnvoll wäre daher nur:

```text
bereits radioaktives Material -> spontane Strahlung -> Ionisation
```

nicht:

```text
normaler Quarz + elektrisches Feld -> erzeugte Beta-Strahlung.
```

## Sicherheitsgrenze

Keine Replikationsarbeit soll alte Glühstrümpfe, Radium-/Thoriumminerale, Rauchmelderquellen oder andere radioaktive Verbraucherprodukte öffnen, zerreiben, erhitzen oder in die Maschine einbauen. Thoriumhaltige Glühstrümpfe können radioaktive Tochterprodukte und Thoron freisetzen; Kontamination/Inhalation ist die wesentlich kritischere Route als die schwache äußere Strahlung.

V4.6 bleibt deshalb **reines Simulations-/Messmodell**. Für einen Laborvergleich ist ein kontrollierter nicht-radioaktiver Ionisationspfad zu verwenden.

## Falsifizierbarer Test ohne Radioaktivität

Der Mechanismus kann mit einer sicheren, regelbaren externen Ionisations-/Leitfähigkeitsquelle nachgebildet werden. Entscheidend ist nicht die Kernphysik, sondern ob ein pA/nA-großer definierter Luftstrom:

1. Startup-/Crystal-Schwelle reproduzierbar verschiebt;
2. das Restdrehmoment beeinflusst;
3. beim Annähern einer isolierten Metallplatte stark verändert wird;
4. bei ausgeschalteter Ionisation wieder verschwindet.

Wenn das nicht passiert, verliert die Radioionisationshypothese stark an Plausibilität.

## Literatur-/Quellenhinweise

- U.S. NRC: Polonium-210 static eliminators; Alpha-Strahlung ionisiert Luft zur Beseitigung statischer Ladung.
- IAEA/INIS: Static eliminators mit Am-241/Po-210 als industrielle Ionisationsquellen.
- Luetzelschwab & Googins, Health Physics 46 (1984): radioaktive Thorium-Töchter in Gasglühstrümpfen und Freisetzung beim Brennen.
- Sorimachi et al., Rev. Sci. Instrum. 80 (2009): Thoronquelle aus handelsüblichen thoriumhaltigen Lantern Mantles.
- Shabana et al., Applied Radiation and Isotopes 51 (1999): gemessene Thoriumaktivitäten von etwa 350–4560 Bq pro untersuchtem Mantle, mit großer Streuung.
- IAEA nuclear-science data: mittlere Ionisationsenergie trockener Luft rund 33.97 eV/Ionenpaar.

## Code

```text
python sim/m2_v4_6_radioionization_gate.py
python sim/m2_v4_6_radioionization_gate.py --activity-bq 10000 --energy-mev 5 --cap-pf 100 --rpm 15
python -m unittest tests/test_m2_v4_6_radioionization_gate.py -v
```
