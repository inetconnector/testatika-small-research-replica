# M2-V4.7 — Radioionisation direkt im floating Grid/Crystal-Netz

## Ziel

V4.7 koppelt die V4.6-Radioionisationsgrenze direkt an das V4.2-Netz mit

- 4 `GRID`-Knoten,
- 4 `PICKUP`-Knoten,
- zwei internen Pot-/Leydener-Knoten,
- 24 einzeln neutralen Rotorleitern,
- kontinuierlicher Crystal-Kommutation,
- passivem Corona-/Ionenpfad,
- optionaler vollständig floating Metallplatte.

Die neue Frage lautet nicht mehr, ob Radioaktivität die Ausgangsleistung liefert. Das ist energetisch ausgeschlossen. Geprüft wird nur:

> Kann ein pA-/nA-Ionisationsstrom in einem extrem hochohmigen floating Netz den Arbeitspunkt der Crystal-Kommutation verschieben oder stabilisieren?

V4.7 ist ein Forschungs- und Falsifikationsmodell, kein historischer Schaltplan.

## Wichtige Korrektur gegenüber der naiven `I/C`-Extrapolation

V4.6 berechnet für ein absichtlich optimistisches Beispiel

```text
Aktivität = 10 kBq
Gasdeposition = 5 MeV/Zerfall
Sammlung = 100 %
```

ungefähr

```text
P_decay ~= 8.01 nW
I_sat   ~= 0.236 nA.
```

Der Wert `I_sat/C` ist eine sinnvolle Größenordnung für einen bereits vorhandenen elektrischen Feldzustand, der erzeugte Ionen sammelt. Er darf aber **nicht** als unbegrenzter idealer Konstantstrom zum Hochladen eines isolierten Kondensators interpretiert werden.

Denn zum Aufbau von Feldenergie gilt zusätzlich

```text
1/2 * C * V^2 <= P_source * t.
```

Daraus folgt die absolute, bereits unrealistisch günstige Energiegrenze

```text
Vmax = sqrt(2 * P_source * t / C).
```

Für `C = 100 pF` und `P_source = 8.01 nW`:

| Zeit | absolute `Vmax`-Grenze |
|---:|---:|
| 1 s | 12.66 V |
| 4 s | 25.32 V |
| 10 s | 40.03 V |
| 20 s | 56.61 V |
| 40 s | 80.05 V |
| 60 s | 98.05 V |

100 V aus Nullfeldenergie an 100 pF benötigen selbst bei 100 % elektrischer Umsetzung mindestens

```text
t ~= 62.4 s.
```

Bei 15 rpm sind das etwa

```text
15.6 Umdrehungen.
```

Das ist die entscheidende Einordnung:

- als **schnelle 100-V-Energiequelle** ist ein 10-kBq-Beispiel schwach;
- als **langsamer Bias von wenigen Volt bis einigen zehn Volt** oder als Leitfähigkeits-/Gate-Effekt kann dieselbe Größenordnung in einem pF-Netz durchaus relevant sein;
- liegt der Crystal ohnehin nur wenige Volt vor seinem Umschaltbereich, kann ein sehr kleiner Ionisationsstrom funktional großen Einfluss haben, ohne energetisch groß zu sein.

## Integration in V4.2

V4.7 benutzt weiterhin kein Ground. Die radioaktive Quelle erzeugt auch keine Nettoladung des Gesamtgeräts.

Stattdessen wird als absichtlich günstige obere Grenze eine **bipolare Ladungstrennung innerhalb des floating Netzes** modelliert. Die Geometrie wird so gewählt, dass sie den bereits vorhandenen gespiegelten Crystal-Drive unterstützt:

```text
gerade Station: POT_P -> PICKUP_i
ungerade Station: PICKUP_i -> POT_N
```

Dadurch wird genau die Spannungsdifferenz vergrößert, die der V4.2-Crystal anschließend gleichrichtet.

Das ist ausdrücklich eine Forschungs-Topologie. Es gibt keinen Beleg, dass die historische Testatika einen radioaktiven Stoff genau so angeordnet hatte.

## Zwei harte Grenzen pro Zeitschritt

Jeder Radioionisationsschritt muss gleichzeitig erfüllen:

### 1. Ladungsgrenze

```text
|Delta Q| <= I_sat * Delta t.
```

Der gesamte berechnete Sättigungsstrom wird auf die Stationen verteilt. Er wird nicht versehentlich pro Gitter vervielfacht.

### 2. Energiegrenze

Wenn der Ionisationsschritt die elektrostatische Feldenergie erhöht, gilt

```text
Delta U_field <= P_decay * eta_energy * Delta t.
```

Die Änderung wird mit der vollständigen V4.2-Kapazitätsmatrix berechnet. Reicht die verfügbare Zerfallsenergie nicht für den vom Stromlimit vorgeschlagenen Ladungsschritt, wird `Delta Q` numerisch so weit verkleinert, bis die Energiebilanz exakt passt.

Falls die gleiche Ionisation Ladung **mit** dem vorhandenen Feld verschiebt und dadurch Feldenergie abbaut, wird diese Energie nicht der Radioquelle zugeschrieben, sondern als passiver Ionisationsverlust verbucht.

## Geschlossene Energiebilanz

Die neue Bilanz lautet

```text
E_initial
+ W_mech
+ E_radio,elektrisch
=
E_final
+ E_crystal_loss
+ E_corona_loss
+ E_radio_passive_loss
+ E_load.
```

Damit kann ein kleiner Strahler keinen versteckten Energiegewinn erzeugen.

## Erwartete qualitative Signatur

V4.7 sucht nach einem schmalen Arbeitspunktfenster:

```text
ohne Ionisation:
V_pickup knapp unter Crystal-Arbeitsbereich
        -> schwache/instabile Kommutation

mit pA/nA-Ionisation:
V_pickup um einige Volt verschoben
        -> Crystal-Kommutation reproduzierbarer

Metallplatte:
C-Matrix/Feldverteilung verändert
        -> derselbe kleine Bias reicht nicht mehr
        -> Crystal-/Corona-Zustand kippt.
```

Ein solches Ergebnis würde **nicht** bedeuten, dass Radioaktivität die Ausgangsenergie liefert. Es würde nur erklären, warum ein winziges, verborgenes Materialdetail für Start, Trockenluftabhängigkeit oder Plattenempfindlichkeit wichtig sein könnte.

## Falsifikation

Die Radioionisationshypothese verliert stark an Plausibilität, wenn eine reale Replica folgende Tests nicht zeigt:

1. Ein definierter nicht-radioaktiver Ionisationsersatz im pA-/nA-Bereich verändert den Crystal-/Pickup-Arbeitspunkt überhaupt nicht.
2. Der Effekt skaliert nicht mit dem eingespeisten Ionisationsstrom.
3. Der Metallplatten-Kippunkt bleibt völlig unverändert, obwohl der definierte Bias um Größenordnungen variiert wird.
4. Der behauptete Dauerleistungsfluss kann nicht über einen separaten Hauptenergiepfad geschlossen werden.

## Sicherer experimenteller Ersatz

Für einen Nachbau wird **kein** alter Glühstrumpf, Radium-/Thoriummineral, Rauchmeldermaterial oder anderer radioaktiver Gegenstand verwendet.

Die Funktion ist sicherer testbar durch einen kontrollierten, nicht-radioaktiven und strombegrenzten Laborersatz, der lediglich pA-/nA-Ladung bzw. definierte Luftleitfähigkeit erzeugt. Entscheidend ist die elektrische Wirkung, nicht die radioaktive Quelle selbst.

## Code

```text
python sim/m2_v4_7_radioionization_integration.py
python sim/m2_v4_7_radioionization_integration.py --sweep
python sim/m2_v4_7_radioionization_integration.py --activity-bq 10000 --rpm 15 --plate 2
python -m unittest tests/test_m2_v4_7_radioionization_integration.py -v
```

## Zwischenfazit

V4.7 verschiebt die Radioaktivitätsidee in eine physikalisch sinnvolle Rolle:

```text
nicht:  radioaktiver Kristall -> 100 W Quelle
sondern:
        schwache Ionisation
        -> winziger bipolarer Bias / Leitfähigkeit
        -> Crystal-/Kommutations-Arbeitspunkt
        -> großer vorhandener Leistungspfad wird nur gesteuert.
```

Der **große vorhandene Leistungspfad** bleibt separat nachzuweisen. V4.7 löst die Primärenergiefrage daher nicht, sondern prüft ein mögliches fehlendes Gate-/Startdetail.
