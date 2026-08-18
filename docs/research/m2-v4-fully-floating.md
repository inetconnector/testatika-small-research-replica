# M2-V4 — vollständig floating, ohne Ground-Knoten

## Fragestellung

Dieses Modell prüft die Hypothese, dass die kleine Testatika als vollständig elektrisch schwebendes System funktionieren könnte: interne Polaritätsräume, 24 einzeln neutrale Rotorleiter, stationäre Gitter/Taster und passive Crystal-/Dioden-Kommutation — ohne galvanische Erdung und ohne versteckte Spannungsquelle.

Es ist **kein historischer Schaltplan** und **kein Over-Unity-Modell**. Alle Kapazitäten sind Platzhalter, bis Mess- oder FEM-Daten vorliegen.

## Wesentliche Änderung gegenüber älteren Modellen

Es gibt keinen `ground`-Knoten und keine Kapazität "nach Masse". Die Kapazitätsmatrix ist daher eine reine paarweise Maxwell-/Laplacian-Matrix. Ihre Zeilensummen sind null.

Die unvermeidliche gemeinsame Spannungsfreiheit wird nur mathematisch mit

```text
sum(V_i) = 0
```

fixiert. Diese Eichbedingung ist **keine physische Erdverbindung**.

Für die vier erhaltenen stationären Knoten gilt

```text
GRID_L, GRID_R, PICKUP_L, PICKUP_R
```

und die Gesamtladung muss erhalten bleiben:

```text
sum(Q_i) = 0.
```

Jeder der 24 Rotorleiter wird als neutraler floating conductor mit `Q_wire = 0` analytisch eliminiert. Damit bleibt seine Polarisations- und Vermittlungswirkung in `C(theta)` enthalten.

## Energie-Buchhaltung

Bei festgehaltener freier Ladung gilt

```text
U(theta) = 1/2 q^T V(theta).
```

Ändert sich die Rotorstellung von `theta_1` nach `theta_2`, wird

```text
Delta W_mech = U(theta_2) - U(theta_1)
```

als mechanische Arbeit gebucht. Passive Dioden/Crystal-Ventile dürfen Gesamtladung nur umverteilen und Feldenergie nur vermindern.

Damit ist jede scheinbare Selbstanregung direkt falsifizierbar: Ein Anstieg der Feldenergie muss entweder aus gebuchter mechanischer Arbeit oder aus einer explizit hinzugefügten externen Kopplung stammen.

## Ergebnis des ersten V4-Laufs

Default-Geometrie:

- 24 neutrale Rotorleiter;
- 10° Pickup-Halböffnung;
- phasenversetzte Grid/Pickup-Kopplung;
- zwei passive Cross-Valves;
- keine Metallplatte;
- keine Erdung;
- keine externe Spannungsquelle.

Ergebnis:

```text
Ceff min/max [pF]        = 8.19771 / 8.20666
Cmax/Cmin                = 1.00109223
final amplitude [V]      = 0.240166638
late per-rev gain        = 1.00000000
energy residual          ~ 1.8e-27 J
```

Die Startladung wird beim ersten Umlauf stark umverteilt; danach entsteht ein stationärer Zustand. **Es gibt in diesem passiven vollständig floating Basismodell keine weiter anwachsende Selbstanregung.**

Das ist ein wichtiges negatives Resultat: Das Entfernen des Ground-Knotens allein erzeugt keine fehlende Energiequelle.

## Metallplatten-Test

Die Platte wird ebenfalls als neutraler floating conductor modelliert und stärker an die rückseitigen Pickup-Knoten als an die Frontgitter gekoppelt. Sie ist also kein Ground-Ersatz.

Erster Sweep:

| Plate scale | Cmax/Cmin | finale Amplitude |
|---:|---:|---:|
| 0 | 1.00109 | 0.2402 V |
| 0.5 | 1.00124 | 0.2368 V |
| 1 | 1.00131 | 0.2336 V |
| 2 | 1.00135 | 0.2275 V |
| 5 | 1.00132 | 0.2110 V |
| 10 | 1.00121 | 0.1884 V |

Die floating Metallplatte verändert die Kapazitätsmatrix und reduziert im Platzhaltermodell die Differentialamplitude, **aber sie erzeugt keinen abrupten Kollaps**. Ein abrupter Stopp wie in der Marinov-Anekdote würde deshalb zusätzliche Nichtlinearität nahelegen, zum Beispiel:

- Crystal-/Dioden-Schwellwert;
- Corona-/Ionisationsschwelle;
- bistabile Ladungszustände;
- stark asymmetrische Umwelt-/Körperkopplung der Platte;
- ein noch fehlender stationärer Knoten bzw. Pot-Feedback-Pfad.

## Wichtigste Konsequenz

Der aktuelle V4-Test trennt zwei Fragen sauber:

1. **Kann das Gerät ohne galvanische Erdung elektrisch floating arbeiten?** — Ja. Ein vollständig floating bipolarer Ladungszustand ist elektrostatisch konsistent.
2. **Erklärt dies die behauptete Nettoleistung?** — Nein. Im passiven V4-Basismodell entsteht keine wachsende Energie ohne mechanische oder andere explizite Energiezufuhr.

Damit verschiebt sich die Suche auf einen engeren Punkt: Falls der Rotor wirklich nur sehr kleine mechanische Leistung hatte, muss ein zusätzlicher Kopplungsmechanismus vorhanden sein, der im bisherigen vier-Knoten-Modell fehlt.

## Nächste V4.1-Tests

Priorität:

1. zwei explizite Pot-/Leydener-Reservoirknoten ergänzen;
2. Crystal als gemessene bzw. gesweepte nichtlineare `I(V)`-Kennlinie statt idealer Diode;
3. Metallplatte in drei Zuständen vergleichen: vollständig floating, über Körperkapazität an Umgebung gekoppelt, stark asymmetrisch gekoppelt;
4. nicht nur 4, sondern 8–14 stationäre Gitter/Taster als phasenversetzte Knoten modellieren;
5. periodische Orbit-/Monodromieanalyse statt nur Endamplitude;
6. mechanisches mittleres Drehmoment explizit aus `dU/dtheta` bestimmen;
7. danach erst Last- und Leydener-Speicherpfad hinzufügen.

## Code

```text
python sim/m2_v4_fully_floating.py
python sim/m2_v4_fully_floating.py --plate 10
python -m unittest tests/test_m2_v4_fully_floating.py -v
```
