# M2-V4.9 — Robustheit des Crystal-Gate-Fensters gegen Verluste

## Ziel

V4.8 zeigte im absichtlich maximal günstigen 100%-Obergrenzenfall ein mehrere zehn Volt breites Crystal-Gate-Fenster. V4.9 prüft, wie schnell dieses Fenster verschwindet, wenn nur ein Teil des idealen Ionisationsstroms beziehungsweise des radioaktiven Energiebudgets am richtigen Gate wirksam wird.

Die beiden Wirkungsgrade werden bewusst getrennt:

```text
eta_current = Anteil des idealen Ionisations-/Sättigungsstroms,
              der wirklich in der gewünschten Gate-Richtung gesammelt wird

eta_energy  = Anteil der Zerfallsleistung,
              der im bewusst günstigen V4.7/V4.8-Pumpmodell
              als zusätzliche elektrostatische Feldenergie verfügbar ist.
```

Keiner dieser Werte ist ein historisch gemessener Testatika-Wert. Es handelt sich um eine Robustheitsanalyse.

## Referenzfall

Wie in V4.8:

```text
A = 10 kBq
Edep = 5 MeV/Zerfall
rpm = 15
Crystal-Knee = 100 V
seed = 5 nC
Beobachtungszeit = 4 s = 1 Umdrehung
```

Der 100%-Fall liefert ungefähr:

```text
Gate-Defizit überbrückbar ~= 25.84 V
Seed-Fenster               ~= 1.288 nC
kritische plate_scale      ~= 0.2311
```

## Sweep bei gleichem Strom- und Energie-Wirkungsgrad

| `eta_current = eta_energy` | kleinster Seed mit Gate-Bias | Seed-Fenster | überbrückbares Spannungsdefizit | kritische `plate_scale` |
|---:|---:|---:|---:|---:|
| 100 % | 3.6959 nC | 1.2880 nC | 25.84 V | 0.2311 |
| 30 % | 4.6353 nC | 0.3487 nC | 7.00 V | 0.0639 |
| 10 % | 4.8705 nC | 0.1135 nC | 2.28 V | 0.0225 |
| 3 % | 4.9502 nC | 0.0338 nC | 0.677 V | 0.00864 |
| 1 % | 4.9728 nC | 0.0112 nC | 0.225 V | 0.00472 |
| 0.3 % | 4.9806 nC | 0.00337 nC | 0.0675 V | 0.00336 |
| 0.1 % | 4.9829 nC | 0.00112 nC | 0.0225 V | 0.00297 |

## Interpretation

Das Ergebnis ist deutlich strenger als V4.8 allein:

- Bei **30 %** Gesamtwirksamkeit bleibt ein klarer Mehrvolt-Arbeitspunktbereich übrig.
- Bei **10 %** bleiben noch rund 2.3 V.
- Bei **1 %** ist das Fenster nur noch ungefähr 0.23 V breit.
- Bei **0.1 %** wäre eine sehr feine Abstimmung nötig.

Damit wird die Radioionisations-Gate-Hypothese erstmals quantitativ angreifbar:

> Sie ist nur dann als robuster Start-/Kommutationsmechanismus interessant, wenn ein überraschend großer Anteil der erzeugten Ladungsträger räumlich und phasenrichtig am relevanten Pickup gesammelt wird oder wenn ein anderer externer Feldpfad die eigentliche Gate-Energie liefert.

## Stromlimit und Energielimit sind nicht gleich wichtig

Die getrennte Sensitivität zeigt für den gleichen Referenzfall:

| `eta_current` | `eta_energy` | überbrückbares Gate-Defizit | kritische `plate_scale` |
|---:|---:|---:|---:|
| 100 % | 10 % | 2.28 V | 0.0225 |
| 10 % | 100 % | 6.62 V | 0.0607 |
| 10 % | 10 % | 2.28 V | 0.0225 |
| 100 % | 1 % | 0.225 V | 0.00472 |
| 1 % | 100 % | 0.662 V | 0.00851 |
| 1 % | 1 % | 0.225 V | 0.00472 |

Im aktuellen bewusst günstigen Modell ist daher in diesem Arbeitspunkt häufig das **zulässige zusätzliche Feldenergiebudget** strenger als das reine Ionenstromlimit.

Das ist wichtig: Ein großer Ionisationsstrom allein genügt nicht, wenn keine Energiequelle vorhanden ist, die den Gate-Knoten tatsächlich gegen sein vorhandenes Feldpotential verschieben kann.

## Konsequenz für einen echten Versuch

Der sinnvollste nächste Labortest braucht **keine Radioaktivität**. Stattdessen soll ein definierter Ersatzpfad die zwei V4.9-Grenzen unabhängig variieren:

1. maximalen Biasstrom begrenzen;
2. maximal verfügbare Gate-Leistung separat begrenzen;
3. Crystal-/Diodenaktivität gegen beide Größen messen;
4. Plattenabstand gleichzeitig sweepen;
5. den Rotorwinkel bzw. die Phase mit erfassen.

Dann lässt sich feststellen, ob das reale Gerät eher

```text
stromlimitiert,
energielimitiert,
kapazitäts-/phasenlimitiert
```

oder überhaupt nicht durch einen solchen Gate-Pfad bestimmt wird.

## Wichtigste Falsifikationsregel

Wenn ein sicherer nicht-radioaktiver Ersatzbias selbst bei

```text
eta-äquivalenten Gatebedingungen von 10–30 %
```

keinen reproduzierbaren Mehrvolt-Schaltbereich erzeugt, wird die Radioionisations-Gate-Hypothese sehr schwach.

Umgekehrt wäre ein breiter, reproduzierbarer, stark metallplattenabhängiger Gate-Bereich ein echter mechanistischer Hinweis — aber weiterhin **kein Beweis für die Hauptenergiequelle**.

## Energiegrenze bleibt unverändert

Auch V4.9 liefert keine 100-W-/300-W-Quelle. Der hypothetische radioaktive Anteil bleibt Nanowatt-Klasse und kann höchstens Bias/Ionisation/Kommutation erklären. Eine behauptete hohe Dauerleistung benötigt weiterhin einen getrennt messbaren Hauptenergiepfad.

## Code

```text
python sim/m2_v4_9_gate_efficiency_sensitivity.py
python sim/m2_v4_9_gate_efficiency_sensitivity.py --eta-current 0.1 --eta-energy 0.1
python -m unittest tests/test_m2_v4_9_gate_efficiency_sensitivity.py -v
```

## Sicherheit

Simulation only. Keine alten Glühstrümpfe, Rauchmelderquellen, Thorium-/Radiumminerale oder andere radioaktive Verbraucherprodukte für Replikationsversuche verwenden. Reale Gate-Tests ausschließlich mit einer kontrollierten nicht-radioaktiven, strom- und energiebegrenzten Ersatzquelle durchführen.
