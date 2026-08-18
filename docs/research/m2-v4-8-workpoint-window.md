# M2-V4.8 — Crystal-Arbeitspunktfenster mit source-limited Ionisationsbias

## Ziel

V4.8 beantwortet die engste offene Frage aus V4.7:

> Muss der passive Rotor/Grid/Pickup-Kreis auf Mikrovolt genau am Crystal-Kippunkt liegen, damit ein pA/nA-Ionisationsstrom überhaupt relevant wird, oder existiert ein makroskopisch breites Arbeitspunktfenster?

Die Rechnung verwendet die **exakte V4.2-Maxwell-Kapazitätsmatrix** bei einem gewählten Rotorwinkel. Der Radio-/Ionisationspfad bleibt derselbe bewusst günstige V4.7-Obergrenzenfall. Die gesamte Quellleistung und der gesamte Ionisationsstrom werden auf alle vier Stationen verteilt.

V4.8 ist keine historische Schaltungsbehauptung und kein Leistungsnachweis.

## Crystal-Drive im aktuellen V4.2-Modell

Für eine gerade Station ist der Vorwärts-Drive

```text
Vdrive = Vpickup - Vpot+
```

für eine ungerade Station spiegelbildlich

```text
Vdrive = Vpot- - Vpickup.
```

Der V4.2-Nominalwert `seed_grid_charge = 5 nC` liegt bei `plate_scale = 0` zufällig bereits sehr nahe am gewählten Crystal-Knee von 100 V:

```text
Vdrive ~= 100.3214 V
Margin ~= +0.3214 V.
```

Das ist **kein historischer Messwert**; es folgt aus den bewusst gewählten Simulationsparametern. Es ist aber ideal, um die Gate-Hypothese numerisch zu testen.

## Effektive Gate-Kapazität

Aus der vollständigen Maxwell-Matrix ergibt sich für den Pickup↔Pot-Differentialmodus bei Rotorphase 0:

```text
Ceff ~= 3.5597 pF
```

ohne zusätzliche Metallplatte.

Mit einer floating Platte steigt diese effektive Differentialkapazität, während der passive Crystal-Drive gleichzeitig sinkt.

## Harte Doppelgrenze des Ionisationspfads

V4.8 übernimmt die V4.7-Korrektur: Ein Ionisationsstrom darf nicht wie eine kostenlose ideale Stromquelle behandelt werden.

Pro Station gelten gleichzeitig

```text
DeltaQ <= Ishare * t
DeltaU <= Pshare * t.
```

Für positiven Gate-Drive gilt damit als günstige Obergrenze

```text
Vcharge = V0 + Ishare*t/Ceff
Venergy = sqrt(V0^2 + 2*Pshare*t/Ceff)
Vbound  = min(Vcharge, Venergy).
```

Für den demonstrativen V4.7-Fall

```text
A = 10 kBq
Edep = 5 MeV/Zerfall
eta_current = 1
eta_energy = 1
rpm = 15
```

wird eine Umdrehung (`t = 4 s`) betrachtet.

## Kernergebnis 1: Das Gate-Fenster ist im Obergrenzenmodell nicht mikroskopisch schmal

Ohne Platte liegt der passive 100-V-Schwellenwert bei ungefähr

```text
seed_no_radio ~= 4.98398 nC.
```

Mit dem bewusst maximal günstigen source-limited Ionisationsbias kann die 100-V-Schwelle innerhalb einer Umdrehung bereits ab ungefähr

```text
seed_radio_min ~= 3.69594 nC
```

erreicht werden.

Das Kandidatenfenster ist damit

```text
Delta seed ~= 1.28804 nC.
```

Am unteren Rand dieses Fensters beträgt der passive Crystal-Drive nur ungefähr

```text
V0 ~= 74.16 V,
```

der günstige Ionisationspfad deckt im Modell also einen Fehlbetrag von ungefähr

```text
25.84 V
```

bis zum 100-V-Knee ab.

**Interpretation:** Die Spur scheitert in diesem Obergrenzenmodell nicht daran, dass sie nur in einem Mikrovolt-Feintuning funktionieren könnte. Das mögliche Gate-Fenster ist mehrere zehn Volt breit.

Das ist trotzdem noch kein Beweis für einen realen radioaktiven Gate-Mechanismus, weil reale Sammlung, Rekombination, Wandverluste, Geometrie, Duty-Cycle und Crystal-Last den Effekt nur verkleinern können.

## Kernergebnis 2: Eine floating Metallplatte kann das Fenster wieder schließen

Für den Nominal-Seed von `5 nC` fällt der passive Drive mit zunehmender floating Plattenkopplung ungefähr so:

| `plate_scale` | passiver `Vdrive` |
|---:|---:|
| 0.00 | 100.32 V |
| 0.05 | 94.75 V |
| 0.10 | 89.62 V |
| 0.15 | 84.86 V |
| 0.20 | 80.46 V |
| 0.25 | 76.36 V |
| 0.30 | 72.53 V |
| 0.50 | 59.51 V |

Der optimistische 10-kBq-Ionisationspfad kann bei einer Umdrehung noch bis ungefähr

```text
plate_scale_critical ~= 0.23110
```

den 100-V-Knee erreichen.

Damit ergibt sich im Modell qualitativ genau die gesuchte Topologie:

```text
freie Maschine
    -> passiver Drive nahe Crystal-Knee
    -> kleiner Ionisationsbias reicht
    -> Crystal-Kommutation aktiv

floating Metallplatte nähert sich
    -> Maxwell-Matrix ändert sich
    -> passiver Drive sinkt
    -> benötigte Gate-Energie steigt
    -> source-limited Ionisationsbias reicht nicht mehr
    -> Crystal bleibt unter Knee.
```

Der Übergang kann durch den nichtlinearen Crystal anschließend deutlich schärfer erscheinen als die zugrunde liegende kontinuierliche Kapazitätsänderung.

## Was V4.8 ausdrücklich NICHT zeigt

V4.8 zeigt nicht,

- dass in der historischen Testatika radioaktives Material enthalten war;
- dass ein alter Glühstrumpf verwendet wurde;
- dass der Crystal tatsächlich bei 100 V schaltete;
- dass die reale Gate-Kapazität 3.56 pF betrug;
- dass die Metallplattenkopplung dem dimensionslosen `plate_scale` der Simulation entsprach;
- dass Radioaktivität die Ausgangsleistung lieferte.

Die Energiequelle für behauptete 100-W-/300-W-Dauerleistung bleibt weiterhin ungelöst.

## Neue experimentelle Konsequenz

Die Gate-Hypothese kann vollständig **ohne Radioaktivität** getestet werden.

Ein sicherer Laborversuch sollte einen kontrollierten, extrem kleinen, strom- und energiebegrenzten Bias zwischen genau den simulierten Knoten einspeisen und dann messen:

1. Crystal-/Diodenaktivität gegen Biasstrom;
2. Arbeitspunkt gegen Rotorwinkel;
3. Arbeitspunkt gegen Metallplattenabstand;
4. Unterschied zwischen isolierter und umweltgekoppelter Platte;
5. Hysterese beim Hin- und Zurückfahren des Bias;
6. Pot-/Leydener-Differentialspannung;
7. Rotor-Restdrehmoment.

Wenn ein pA/nA-großer nicht-radioaktiver Ersatzbias **keinen** robusten Schaltbereich erzeugt, verliert die Radioionisationshypothese stark an Plausibilität.

## Code

```text
python sim/m2_v4_8_workpoint_window.py
python sim/m2_v4_8_workpoint_window.py --sweep
python sim/m2_v4_8_workpoint_window.py --seed-nc 5 --activity-bq 10000 --plate 0.2
python -m unittest tests/test_m2_v4_8_workpoint_window.py -v
```

## Sicherheitsgrenze

V4.8 ist Simulation. Keine Replikationsanweisung verwendet alte Glühstrümpfe, Thorium-/Radiumminerale, Rauchmelderquellen oder andere radioaktive Verbraucherprodukte. Ein realer Gate-Test soll mit einer **nicht-radioaktiven, kontrollierten und strombegrenzten Ersatzquelle** erfolgen.
