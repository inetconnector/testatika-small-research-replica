# M2-V4.5 — zwei Umweltports und Metallplatten-Kollaps

## Ziel

V4.5 prüft die bisher engste noch konventionell mögliche externe Energiehypothese für eine **nicht galvanisch geerdete** Maschine:

> Die Maschine könnte zwei räumlich verschiedene Umweltpotentiale kapazitiv abgreifen. Der Rotor/Gitter/Crystal-Kreis wäre dann hauptsächlich Kommutator und Ladungsmanager; die externe Energie müsste über einen Front- und einen Rückseitenport in einem geschlossenen Verschiebungsstromkreis eintreten.

Das ist **keine Behauptung**, dass die historische Testatika so arbeitete. Das Modell liefert nur quantitative Bedingungen, die eine solche Hypothese erfüllen müsste.

## Zwei getrennte Umweltreservoirs

Wir bezeichnen die externen Potentialräume als `A` und `B`.

```text
Umwelt A
   |
 C_front
   |
 FRONT / Grid-Taster-Port
   |
 [interne Testatika / Last]
   |
 REAR / rückseitiger Port
   |
 C_rear
   |
Umwelt B
```

Eine vollständig floating Maschine kann so Leistung aufnehmen, obwohl kein Draht zur Erde vorhanden ist. Entscheidend ist nicht `ground`, sondern eine reale zeitabhängige Potentialdifferenz

```text
DeltaV_env = V_A - V_B
```

und ein geschlossener Hin-/Rückweg.

Ohne Metallplatte ist die optimistische Serienkopplung

```text
Ceq = C_front * C_rear / (C_front + C_rear)
```

und die AC/RF-Scheinleistungs-Obergrenze

```text
P_bound = 2*pi*f*Ceq*(DeltaV_env,rms)^2.
```

Diese Formel ist bereits großzügig: sie setzt perfekte Nutzung des kapazitiven Stroms voraus und ist keine reale Gleichrichter-Wirkungsgradrechnung.

## Neue Rolle einer Metallplatte

V4.5 modelliert eine zweite Möglichkeit für den historischen Platteneffekt, zusätzlich zu V4/V4.2:

Eine Platte hinter der Maschine könnte den rückseitigen Port kapazitiv **zum selben Umweltreservoir A ziehen**, an das bereits der Frontport gekoppelt ist.

```text
                 Umwelt A
                 /      \
           C_front      C_plate
              |            |
           FRONT          REAR
              |            |
              +-- Maschine-+
                           |
                        C_rear
                           |
                        Umwelt B
```

Für den Rückseitenport ergibt sich dann der kapazitive Thevenin-Wert

```text
V_R,th = (C_rear*V_B + C_plate*V_A)/(C_rear + C_plate)
```

und damit

```text
DeltaV_eff = |V_A - V_R,th|
           = C_rear/(C_rear + C_plate) * |V_A - V_B|.
```

Je stärker `C_plate`, desto mehr wird der Rückseitenport auf dasselbe externe Potential wie die Front gezogen. **Der nutzbare Differenzpfad kann dadurch kollabieren, obwohl die Platte selbst keine Energie absorbieren muss.**

## Symmetrischer Spezialfall

Für

```text
C_front = C_rear = C
x = C_plate/C
```

gilt für die optimistische Leistungsgrenze

```text
P_plate/P_clear = 2 / ((1+x)*(2+x)).
```

Daraus folgen beispielsweise:

| `C_plate/C` | verbleibende externe DeltaV | `P_plate/P_clear` |
|---:|---:|---:|
| 0 | 100 % | 100 % |
| 0.1 | 90.9 % | 86.6 % |
| 0.5 | 66.7 % | 53.3 % |
| 1 | 50 % | 33.3 % |
| 5 | 16.7 % | 4.76 % |
| 10 | 9.09 % | 1.52 % |
| 100 | 0.99 % | 0.0194 % |

Damit kann eine **kontinuierlich zunehmende Plattenkopplung** den externen Leistungspfad sehr stark unterdrücken. In Kombination mit Crystal-/Corona-Schwellen aus V4.1/V4.2 kann daraus ein scheinbar abrupter Funktionsverlust entstehen.

## Beispielrechnung: 100-pF-Ports

Mit

```text
C_front = C_rear = 100 pF
DeltaV_env = 10 kV rms
f = 50 Hz
```

liefert die bereits optimistische Obergrenze ohne Platte nur

```text
P_bound = 1.5708 W.
```

Der Plattensweep ergibt:

| `C_plate` | `DeltaV_eff` | `P_bound` |
|---:|---:|---:|
| 0 pF | 10.0 kV | 1.5708 W |
| 50 pF | 6.67 kV | 0.8378 W |
| 100 pF | 5.00 kV | 0.5236 W |
| 500 pF | 1.67 kV | 0.0748 W |
| 1 nF | 0.909 kV | 0.0238 W |
| 10 nF | 99 V | 0.000305 W |

V4.5 zeigt deshalb gleichzeitig zwei Dinge:

1. **Ja:** Eine Platte kann einen realen Zwei-Umweltport-Leistungspfad sehr stark kollabieren.
2. **Nein:** Kleine parasitäre pF-Kopplungen an niedriger Frequenz erklären noch keine 100-W-Klasse.

## Welche externe Feldquelle wäre für 100 W nötig?

Für zwei gleiche 100-pF-Ports und **keine Platte** beträgt die mindestens erforderliche externe sinusförmige Potentialdifferenz in der großzügigen Obergrenze:

| Frequenz | `DeltaV_env,rms` für 100 W |
|---:|---:|
| 50 Hz | 79.8 kV |
| 1 kHz | 17.8 kV |
| 10 kHz | 5.64 kV |
| 100 kHz | 1.78 kV |
| 1 MHz | 564 V |
| 10 MHz | 178 V |

Das ist der wichtigste neue Suchhinweis: **Falls** eine reale externe elektrische Energiequelle existierte, ist ein hochfrequenter/starkes-Feld-Zweipunktpfad wesentlich weniger geometrisch unmöglich als gewöhnliche 50-Hz- oder Schönwetterkopplung. Dafür gibt es bisher aber keinen Nachweis an der Testatika.

## Zwei verschiedene Plattenmechanismen müssen getrennt werden

Die bisherigen Modelle unterscheiden jetzt ausdrücklich:

### A. vollständig isolierte floating Platte

Eine isolierte neutrale Platte verändert die Maxwell-Kapazitätsmatrix und kann Crystal-/Corona-Schwellwerte verschieben. Das ist der V4/V4.2-Mechanismus.

### B. umweltgekoppelte Platte

Eine Platte mit relevanter Kapazität zu demselben externen Potentialraum wie der Frontport kann zusätzlich den **externen Differenzenergiepfad** kurzschließen/equalisieren. Das ist V4.5.

Diese beiden Effekte sind experimentell unterscheidbar.

## Historische Quellenbegrenzung

Die sekundäre Watson-Wiedergabe von Marinovs Aussagen formuliert lediglich, dass ein Metallblech hinter die Maschine **gehalten** wurde und Rotation sowie Restdrehmoment verschwanden. Sie dokumentiert nicht, ob die Platte elektrisch isoliert war, von einer Person gehalten wurde, Kontakt zu einem Leiter hatte oder welche Abmessungen/Abstände verwendet wurden.

Quelle: Mike-Watson-Wiedergabe auf Novak Corp, `https://www.novakcorp.com/energy/experiments/bswiss.htm`.

Darum darf V4.5 nicht rückwirkend behaupten, dass ein menschlicher Körper oder ein bestimmtes Umweltpotential der historische Rückweg war. Genau diese unbekannte Randbedingung wird zum neuen Experiment.

## Entscheidender Low-Energy-Test

Noch **ohne Hochspannung und ohne offene HV-Speicher**:

1. Replica nur mit kleiner AC-Testspannung/Impedanzanalysator betreiben.
2. Front↔Umwelt- und Rear↔Umwelt-Transferkapazitäten getrennt messen.
3. Metallplatte hinter der Maschine auf isolierendem Stativ platzieren.
4. Danach dieselbe Platte über eine bekannte kleine Kapazität an einen definierten externen Referenzleiter koppeln.
5. Danach Platte durch eine Person halten lassen, aber weiterhin galvanisch isoliert.
6. Für alle Fälle messen:
   - `C_front,A`
   - `C_rear,B`
   - `C_plate,A/B`
   - phasenaufgelöste Pickup-Spannung
   - Crystal-Schaltaktivität
   - Rotor-Restdrehmoment bei sehr kleinem Bias.

Vorhersage von V4.5:

> Wenn der historische Platteneffekt einen **externen Zwei-Port** unterbrach, muss die Wirkung stark davon abhängen, woran die Platte kapazitiv gekoppelt ist. Eine vollkommen isolierte Platte und eine umwelt-/körpergekoppelte Platte dürfen dann nicht identisch wirken.

Falls dagegen beide nahezu identisch wirken, spricht das stärker für den reinen internen Maxwell-/Schwellwertmechanismus aus V4/V4.2.

## Konsequenz für die Energiefrage

V4.5 findet **noch keine Energiequelle**, aber es macht die fehlende Quelle experimentell lokalisierbar.

Für eine reale externe elektrische Quelle müssen gleichzeitig gelten:

```text
1. zwei getrennte Umweltports,
2. messbare DeltaV_env(t),
3. messbare Hin-/Rückströme,
4. P_env = <V_A I_A + V_B I_B> in der Größenordnung der Lastleistung,
5. Plattenstörung verändert genau diesen Leistungsfluss.
```

Wenn Punkt 4 nicht erfüllt ist, kann der Umweltport nicht die behauptete Dauerleistung liefern — unabhängig davon, wie gut Rotor, Crystal und Leydener-Kreis funktionieren.

## Code

```text
python sim/m2_v4_5_two_environment_ports.py
python sim/m2_v4_5_two_environment_ports.py --sweep
python sim/m2_v4_5_two_environment_ports.py --front-pf 100 --rear-pf 100 --plate-pf 1000 --dv-v 10000 --freq-hz 50
python -m unittest tests/test_m2_v4_5_two_environment_ports.py -v
```
