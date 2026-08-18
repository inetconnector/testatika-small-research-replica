# M2-V4.1 — floating Pot-/Leydener-Reservoirs + Crystal-Schwellwert

## Ziel

V4.1 erweitert das vollständig floating V4-Modell um genau die Bauteile, die für den berichteten Metallplatteneffekt und die Leistungsfrage entscheidend sein könnten:

- zwei interne Reservoirknoten `POT_N` und `POT_P`;
- 24 einzeln neutrale floating Rotorleiter;
- zwei Grid-Knoten und zwei schmale Pickup-/Taster-Knoten;
- einen **nichtlinearen, rein passiven Crystal-/Dioden-Schwellwert**;
- eine optionale neutrale floating Metallplatte;
- einen expliziten Lastpfad;
- eine energieerhaltend bilanzierte freie Rotordynamik.

Es gibt weiterhin **keinen Ground-Knoten, keine externe Spannungsquelle und keinen versteckten Gain**. `sum(V)=0` ist nur die mathematische Eichbedingung des vollständig schwebenden Systems.

Das Modell ist kein rekonstruierter historischer Schaltplan. Alle Kapazitäten und der Crystal-Schwellwert sind Forschungsparameter, bis Mess- oder FEM-Daten vorliegen.

## Sechs stationäre Knoten

```text
GRID_L, GRID_R,
PICKUP_L, PICKUP_R,
POT_N, POT_P
```

Die beiden Pot-Knoten bilden ein differentielles internes Reservoir. Ihre Ladungen müssen nicht gegen Erde definiert sein; nur Potentialdifferenzen sind physikalisch relevant.

Die 24 Rotorleiter bleiben einzeln neutral:

```text
Q_wire = 0
```

und werden als floating Leiter analytisch eliminiert. Ihre Polarisationswirkung bleibt vollständig in der winkelabhängigen Kapazitätsmatrix `C(theta)` enthalten.

## Crystal als Schwellenbauteil

V4 hatte ideale passive Ventile ohne ausgeprägte Einschaltgrenze. V4.1 verwendet stattdessen

```text
V_a - V_b > V_th
```

als notwendige Leitbedingung. Erst oberhalb des Schwellwerts wird positive Ladung passiv vom höheren zum niedrigeren Potential verschoben.

Jeder Transfer wird gegen die elektrostatische Feldenergie geprüft:

```text
U_after <= U_before
```

Der Crystal kann daher in diesem Modell **keine Energie erzeugen**. Er kann nur eine phasen- und amplitudenabhängige Kommutation erzeugen.

Die verwendeten spiegelbildlichen Hypothesenpfade sind:

```text
PICKUP_L -> POT_P
POT_N    -> PICKUP_R
```

Damit können die Pot-Polaritäten durch phasenabhängige Pickup-Zustände getrennt werden, ohne Gesamtladung des Geräts zu erzeugen.

## Wichtigster neuer Befund: abrupter Platten-Kippunkt ist möglich

Mit dem Platzhalter-Schwellwert `V_th = 100 V`, 24 Rotorleitern und derselben vollständig floating Metallplatte wie in V4 entsteht erstmals ein **diskontinuierlich wirkender Funktionsverlust**:

Beispiel, 10 Umdrehungen / 96 Schritte pro Umdrehung:

| floating plate scale | Crystal-Ereignisse | Pot-Differenz am Ende |
|---:|---:|---:|
| 0.00 | 111 | 40.50 V |
| 0.05 | 101 | 40.32 V |
| 0.10 | 97 | 40.15 V |
| 0.15 | 104 | 39.97 V |
| **0.20** | **0** | 39.80 V |
| 0.25 | 0 | 39.66 V |
| 0.50 | 0 | 39.06 V |
| 1.00 | 0 | 38.17 V |

Die Platte ist dabei **nicht geerdet**. Sie verändert nur die Maxwell-Kapazitätsmatrix. Sobald dadurch die Pickup-Pot-Spannung unter `V_th` fällt, wird der Crystal-Pfad vollständig inaktiv.

Damit kann aus einer kontinuierlichen geometrischen Kapazitätsänderung ein abruptes elektrisches Verhalten entstehen:

```text
floating Metallplatte
        -> C_ij verändert
        -> Pickup-Spannung sinkt
        -> V_pickup-pot < V_th
        -> Crystal sperrt
        -> phasenabhängige Kommutation fällt weg
```

Das ist qualitativ wesentlich näher am überlieferten "Platte hin -> Effekt weg" als das lineare V4-Modell.

### Wichtig: kein Fit und kein Beweis

Der `100-V`-Schwellwert ist ein bewusster Sweep-Parameter. Dass sich ein Kippunkt erzeugen lässt, beweist weder diesen historischen Schwellwert noch die tatsächliche Crystal-Kennlinie. Entscheidend ist die **falsifizierbare Vorhersage**:

> Falls der Metallplatteneffekt wirklich durch einen nichtlinearen Crystal-/Ionisationsschwellwert entsteht, muss die Leitaktivität beim Annähern der Platte nahe einem reproduzierbaren Abstand abrupt verschwinden und sich durch Änderung der Bias-/Startladung verschieben lassen.

## Energie-Bilanz bleibt geschlossen

Bei vorgeschriebener Drehzahl wird jede Feldenergieänderung durch Rotorbewegung als mechanische Arbeit verbucht:

```text
Delta W_mech = U(theta + dtheta, q) - U(theta, q)
```

Für den Lasttest mit `load_relaxation = 0.01` und ohne Metallplatte ergab ein 10-Umdrehungs-Lauf beispielsweise:

```text
initial field energy  = 1.38516e-6 J
load energy           = 9.87862e-8 J
mechanical work       = 8.17715e-11 J
crystal loss          = 1.67791e-8 J
final field energy    = 1.26967e-6 J
energy residual       ~ 0 J
```

Der entscheidende Befund ist damit negativ und wichtig:

**Die Lastenergie stammt in diesem passiven V4.1-Lauf fast vollständig aus der anfänglich gespeicherten Feldenergie, nicht aus einem unbekannten neuen Reservoir.**

Das Hinzufügen von Pot-Knoten und Crystal-Schwelle erklärt also einen möglichen **Schalt-/Kippmechanismus**, aber noch nicht die behauptete Dauerleistung.

## Freier Rotor statt vorgeschriebener Drehzahl

V4.1 besitzt zusätzlich einen Modus ohne externe Wellenleistung. Die Rotorenergie ist

```text
K = 1/2 I omega^2
```

und jede positive Feldenergieänderung wird direkt aus `K` entnommen. Negative Feldenergieänderung kann an den Rotor zurückgegeben werden. Reibungsverluste werden separat gebucht.

Damit gilt numerisch:

```text
U_initial + K_initial
=
U_final + K_final
+ Crystal-Verlust
+ Lastenergie
+ Reibungsverlust
```

bis auf Rundungsfehler.

Das verhindert, dass die Simulation "Selbstlauf" nur deshalb erzeugt, weil die Rotorbewegung kostenlos vorgeschrieben wurde.

## Was V4.1 jetzt tatsächlich erklärt

V4.1 zeigt, dass folgende Kombination ohne Erdung elektrostatisch konsistent ist:

```text
floating bipolare Reservoirs
        +
variable C(theta)
        +
phasenverschobene Pickups
        +
passiver Crystal-Schwellwert
        +
floating Metallplatte
```

und dass daraus ein **abrupter Kommutationsausfall** entstehen kann.

V4.1 erklärt dagegen noch **nicht**:

- eine Dauerleistung von 100 W, 300 W oder mehr;
- eine externe Primärenergiequelle;
- die reale Kennlinie des historischen "Crystal";
- die genaue Pot-/Leydener-Kapazität;
- Corona-/Ionentransport;
- die tatsächliche Anzahl und Verschaltung aller kleinen Gitter;
- den überlieferten Selbstlauf des Rotors.

## Nächster Test: V4.2

Der nächste sinnvolle Schritt ist nicht mehr, weitere passive Dioden hinzuzufügen. Stattdessen müssen die noch physikalisch eigenständigen Kandidaten getrennt geprüft werden:

1. **Crystal-I(V)-Sweep** statt harter idealer Schwelle;
2. **Corona-/Ionisationszustand** als eigener, energiebilanzierter Ladungspfad;
3. 8–14 einzelne Gitter-/Tasterknoten statt nur zwei Pickups;
4. zwei reale Pot-Kapazitäten aus Geometrie/FEM statt Platzhalter;
5. Plattenabstand als echte Geometriegröße statt dimensionsloser `plate_scale`;
6. Monodromie/Jacobian eines vollständigen Umlaufs;
7. Lasttest mit gleichzeitigem mittlerem Rotor-Drehmoment.

Der wichtigste Falsifikationstest bleibt dabei:

> Wird Crystal-/Ionisationsaktivität durch eine floating Metallplatte scharf abgeschaltet, ohne dass eine nennenswerte elektrische Leistung in die Platte fließt?

Wenn ja, wäre die Platte sehr wahrscheinlich ein **Feld-/Schwellwert-Störer** und keine Energieabschirmung.

## Code

```text
python sim/m2_v4_1_pot_crystal.py
python sim/m2_v4_1_pot_crystal.py --threshold-v 100 --plate 0.5
python sim/m2_v4_1_pot_crystal.py --threshold-v 100 --sweep
python sim/m2_v4_1_pot_crystal.py --threshold-v 100 --load-relax 0.01
python sim/m2_v4_1_pot_crystal.py --threshold-v 100 --load-relax 0.01 --free-rotor
python -m unittest tests/test_m2_v4_1_pot_crystal.py -v
```
