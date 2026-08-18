# M2-V4.2 — multiphasige floating Gitter + kontinuierlicher Crystal + Corona-Pfad

## Ziel

V4.2 prüft den nächsten engeren Mechanismus nach V4/V4.1:

- kein Ground-Knoten;
- zwei interne Pot-/Leydener-Reservoirs;
- 24 einzeln neutrale floating Rotorleiter;
- **8 explizite stationäre Phasenelektroden**: 4 `GRID` + 4 `PICKUP`;
- kontinuierliche Crystal-Leitkennlinie statt harter Ein/Aus-Schwelle;
- separater lokaler Corona-/Ionenpfad zwischen jedem Grid/Pickup-Paar;
- optionale vollständig floating Metallplatte;
- vollständige Energie- und Ladungsbilanz.

Das Modell ist kein rekonstruierter historischer Schaltplan. Alle Kapazitäten, Spannungskennwerte und `plate_scale` sind Forschungsparameter.

## Warum diese Erweiterung wichtig ist

V4.1 konnte einen abrupten Platten-Kippunkt mit einer idealisierten Crystal-Schwelle erzeugen. Das war nützlich, aber zu idealisiert. V4.2 fragt deshalb:

> Bleibt der Platteneffekt bestehen, wenn der Crystal **kontinuierlich** leitet und der eigentliche scharfe Übergang aus einem separaten Luft-/Ionisationspfad kommt?

## Netzwerk

Die zehn erhaltenen stationären Knoten sind:

```text
GRID_0 ... GRID_3
PICKUP_0 ... PICKUP_3
POT_N, POT_P
```

Die vier Grid/Pickup-Paare sind phasenversetzt um den Rotor verteilt. Die Pot-Knoten bilden ein internes differentielles Reservoir. Es gibt weiterhin keine Verbindung zur Erde.

Für jeden Rotorleiter gilt:

```text
Q_wire = 0
```

und für das ganze Gerät:

```text
sum(Q_i) = 0.
```

Die gemeinsame Spannungsfreiheit wird nur mathematisch durch eine Gauge-Bedingung fixiert.

## Kontinuierlicher Crystal

Statt eines harten Schalters benutzt V4.2 eine glatte monotone Vorwärtskennlinie. Die effektive Transferfraktion steigt sigmoid um einen Forschungsparameter `V_knee` an.

Wichtig:

```text
V_a <= V_b  -> kein Vorwärtstransfer
V_a > V_b   -> passiver Transfer a -> b
```

Jeder einzelne Transfer wird numerisch gegen die Feldenergie geprüft:

```text
U_after <= U_before.
```

Der Crystal ist deshalb im Modell ausschließlich **Kommutator / Gleichrichter**, nie Energiequelle.

## Separater Corona-/Ionenpfad

Zwischen jedem lokalen `GRID_i` und `PICKUP_i` wird zusätzlich ein bidirektionaler passiver Luftpfad zugelassen. Erst wenn

```text
|V_grid - V_pickup| > V_corona
```

wird eine zunehmende Leitfähigkeit aktiviert.

Dieser Pfad ist absichtlich dissipativ. Er kann Feldenergie vernichten und Ladung umverteilen, aber keine Energie erzeugen.

Das Modell bildet noch keine reale Gasentladungsphysik, Paschen-Kurve oder Ionenmobilität ab. Der Pfad ist nur ein Falsifikationsmodell für die Frage, ob eine Feldänderung durch die Metallplatte einen ionischen Shunt auslösen könnte.

## Neuer Befund: Metallplatte kann Crystal-Pfad durch Corona-Shunt verdrängen

Mit den aktuellen Platzhalterwerten:

```text
Crystal knee     = 100 V
Corona onset     = 240 V
4 Grid + 4 Pickup
24 Rotorleiter
10 Umdrehungen
48 Winkelschritte/Umdrehung
keine Last
```

ergibt der Sweep:

| floating plate scale | Crystal transfer | Corona transfer | Corona events | finale Pot-Differenz |
|---:|---:|---:|---:|---:|
| 0 | 1.17882e-9 C | 0 | 0 | 81.551 V |
| 0.5 | 8.02178e-10 C | 0 | 0 | 79.491 V |
| 1 | 4.61405e-10 C | 0 | 0 | 77.528 V |
| 2 | 8.92699e-11 C | 0 | 0 | 74.538 V |
| **5** | **0** | **2.89768e-10 C** | **511** | **69.343 V** |

Das ist qualitativ ein stärkeres Ergebnis als V4.1:

1. die Crystal-Kennlinie selbst ist **nicht hart geschaltet**;
2. die Platte schwächt den Crystal-Transfer kontinuierlich;
3. bei genügend starker Plattenkopplung überschreitet ein lokaler Grid/Pickup-Spalt den Corona-Onset;
4. der ionische Shunt übernimmt die Ladungsumlagerung;
5. der gerichtete Crystal-Transfer fällt in diesem Parameterfall auf praktisch null.

Damit existiert ein rein konventioneller Kandidat für

```text
Metallplatte nähert sich
        -> Maxwell-Kapazitätsmatrix ändert sich
        -> lokales Grid/Pickup-Feld steigt
        -> Corona-/Ionenpfad schaltet ein
        -> Pickup-Zustand wird geshuntet
        -> Crystal-Kommutation bricht zusammen
```

Die Metallplatte ist dabei weiterhin **nicht geerdet**.

## Was das für den historischen Plattentest bedeuten würde

Falls die überlieferte Beobachtung korrekt ist, wäre eine konkrete Vorhersage dieses Modells:

> Beim Annähern einer floating Metallplatte sollte unmittelbar vor dem Funktionsverlust ein reproduzierbarer Anstieg von lokalem Ionen-/Corona-Strom oder HF-Entladungsrauschen an bestimmten Gitterkanten auftreten, während der gerichtete Crystal-/Pot-Ladungstransfer gleichzeitig stark abfällt.

Die Position des Kippunkts müsste sich mit Luftfeuchte, Luftdruck, Elektrodenabstand, Oberflächenzustand und Anfangsbias verschieben.

Das ist experimentell deutlich spezifischer als die unscharfe Aussage, die Platte "schirmt Energie ab".

## Energiefrage: weiterhin kein zusätzlicher Energieeintrag

Mit einer kleinen passiven Last (`load_relaxation = 0.005`) und 10 Umdrehungen ergeben sich beispielsweise:

### Keine Platte

```text
initial field energy = 3.00009e-6 J
load energy          = 3.97454e-7 J
mechanical work      = 8.70587e-11 J
crystal loss         = 7.20331e-8 J
corona loss          = 0
final field energy   = 2.53069e-6 J
energy residual      = 0
```

### Starke floating Platte (`plate_scale = 5`)

```text
initial field energy = 2.72483e-6 J
load energy          = 3.01367e-7 J
mechanical work      = 2.75435e-10 J
crystal loss         = 2.01786e-9 J
corona loss          = 5.06118e-8 J
final field energy   = 2.37111e-6 J
energy residual      = 0
```

Damit bleibt die zentrale Aussage bestehen:

**Ein passiver Crystal plus passiver Corona-/Ionenpfad kann den Platten-/Kommutationsmechanismus erklären, aber keine Dauerleistung erzeugen.**

Die Lastenergie stammt weiterhin fast vollständig aus der anfänglich gespeicherten Feldenergie; der gebuchte mechanische Beitrag ist in diesem Platzhalterlauf sehr klein.

## Was V4.2 neu ausschließt

Wenn der historische Rotor wirklich nur sehr geringe mechanische Leistung abgab und eine nennenswerte elektrische Dauerlast versorgt wurde, dann reicht folgende vollständig passive Klasse nicht aus:

```text
floating Kapazitäten
+ passive Dioden/Crystal
+ passive Corona/Ionenleitung
+ interne Pot-Speicher
```

Mindestens einer der folgenden Punkte müsste dann zusätzlich vorhanden sein:

1. ein externer Energiefluss, der bisher nicht modelliert ist;
2. eine aktive/materialinterne Energiequelle;
3. eine wesentlich größere mechanische Energieübertragung als historisch vermutet;
4. oder eine Überschätzung der historischen Ausgangsleistung bzw. Lastdauer.

## Nächster sinnvoller Test: V4.3

V4.3 sollte nicht einfach noch mehr passive Nichtlinearitäten hinzufügen. Priorität haben jetzt messbare externe Kopplungen:

1. Plattenabstand in Millimetern statt `plate_scale` durch FEM/Geometrie;
2. lokale elektrische Feldstärke an jeder Grid-/Pickup-Kante;
3. gemessene Corona-/Ionenströme und Luftfeuchteabhängigkeit;
4. reale Crystal-`I(V)`-Kennlinie;
5. Pot-Kapazitäten aus Geometrie;
6. vollständige Lastbilanz über viele Speicherzeitkonstanten;
7. explizite Kandidaten für externe Kopplung nur mit eigener Energie-Buchung.

Der zentrale Falsifikationstest lautet jetzt:

> **Tritt beim Metallplatten-Kippunkt tatsächlich ein lokaler ionischer Shunt auf?**

Wenn nein, fällt dieser V4.2-Mechanismus weg. Wenn ja, wäre der Platteneffekt weitgehend konventionell erklärt — die Primärenergiefrage bliebe davon getrennt.

## Code

```text
python sim/m2_v4_2_multiphase_corona.py --sweep
python sim/m2_v4_2_multiphase_corona.py --plate 5
python sim/m2_v4_2_multiphase_corona.py --plate 5 --load-relax 0.005
python sim/m2_v4_2_multiphase_corona.py --plate 5 --load-relax 0.005 --free-rotor
python -m unittest tests/test_m2_v4_2_multiphase_corona.py -v
```
