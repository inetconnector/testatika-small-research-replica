# M2-V4.4 — Rückweg und lokale Feldspannung bei vollständig floating Betrieb

## Warum V4.4 nötig ist

V4.3 war bewusst großzügig und hat externe Energiepfade einzeln nach oben begrenzt. Für eine **wirklich floating** Maschine kommt aber noch eine strengere Bedingung hinzu:

> Dauerhafte elektrische Leistung braucht immer einen geschlossenen Energie-/Ladungspfad.

Ohne Erdungsdraht bedeutet das bei elektrischer Umweltkopplung mindestens zwei getrennte Ports bzw. Rückwege.

## 1. Kapazitive Umweltkopplung braucht zwei Kapazitäten

Ein floating Gerät kann nicht dauerhaft Leistung aus nur einer einzelnen parasitären Kapazität beziehen. Für einen geschlossenen Verschiebungsstrompfad braucht es beispielsweise

```text
externe Quelle -> C1 -> Maschine -> C2 -> externe Umgebung/Quelle
```

Die wirksame Serienkapazität ist

```text
Ceq = C1*C2 / (C1 + C2).
```

Bei gleichen Kopplungen `C1 = C2 = C` gilt deshalb

```text
Ceq = C/2.
```

Die bereits optimistische V4.3-Grenze verschärft sich damit nochmals.

### 100 W bei 230 V / 50 Hz

V4.3 ergab als idealisierte Mindest-`Ceq` ungefähr 6.02 µF. Bei zwei gleich großen floating Kopplungen wären daher notwendig:

```text
C1 = C2 >= 12.03 µF.
```

Für 300 W:

```text
C1 = C2 >= 36.10 µF.
```

Das liegt weit jenseits üblicher parasitärer Raumkopplungen einer kompakten Maschine.

### Beispiel mit 100 pF auf beiden Seiten

```text
C1 = C2 = 100 pF
Ceq = 50 pF
```

Bei 230 V / 50 Hz ergibt selbst die großzügige Scheinleistungsgrenze nur ungefähr

```text
0.831 mW.
```

Damit fällt normale 50-Hz-Streufeldkopplung als 100-W-Quelle praktisch aus.

## 2. Wichtigste Korrektur der Atmosphärenidee: lokal zählt E*h

Die frühere Rechnung mit ungefähr 250 kV Erde–Ionosphäre war bewusst eine extreme obere Grenze. Für eine kompakte, ungeerdete Maschine gilt diese gesamte Potentialdifferenz **nicht automatisch**.

Wenn das lokale Feld ungefähr `E` beträgt und zwei Umweltports nur um die Maschinenhöhe `h` getrennt sind, ist die direkt verfügbare lokale Potentialdifferenz näherungsweise

```text
DeltaV_local ~= E*h.
```

Beispiel:

```text
E = 100 V/m
h = 0.5 m
```

liefert nur

```text
DeltaV_local ~= 50 V.
```

Um darüber 100 W zu übertragen, wären selbst ideal

```text
I = P/DeltaV = 2 A
```

notwendig.

Das steht in völlig anderer Größenordnung als ein Schönwetter-Ionenstrom.

## 3. Konsequenz für die Schönwetter-Stromdichte

Mit dem bisherigen Vergleichswert

```text
J = 2 pA/m²
```

und `DeltaV_local = 50 V` wäre die idealisierte Leistungsdichte nur

```text
P/A = J*DeltaV
    = 1e-10 W/m².
```

Für 100 W ergäbe das

```text
A = 1e12 m²
  = 1,000,000 km².
```

Für 300 W entsprechend ungefähr

```text
3,000,000 km².
```

Das ist nochmals viel ungünstiger als die bereits extrem optimistische V4.3-Rechnung mit der vollständigen 250-kV-Ionosphärenspannung.

### Wann wäre die 250-kV-Betrachtung überhaupt relevant?

Nur wenn ein separater physikalischer Mechanismus die kompakte Maschine tatsächlich mit weit entfernten Potentialregionen koppelt, zum Beispiel über

- eine hohe Antenne,
- einen weit reichenden Ionen-/Plasmakanal,
- einen langen leitfähigen Pfad,
- oder eine andere nachweisbare Feldkopplung zur oberen Atmosphäre.

Für die kleine Testatika ist ein solcher Pfad bislang nicht belegt.

## 4. Floating Ionenbetrieb braucht ebenfalls einen Rückweg

Ein Gerät kann kurzfristig Netto-Ladung aus der Luft aufnehmen. Dauerhaft geht das nicht beliebig weiter, weil sein Potential sich verschiebt und den Strom schließlich stoppt.

Für stationären floating Betrieb muss daher näherungsweise gelten

```text
I1 + I2 = 0
```

für zwei externe Ladungsports.

Die externe Leistung lautet dann

```text
P_env = V1*I1 + V2*I2
```

und mit `I2 = -I1`:

```text
P_env = (V1 - V2)*I1.
```

Das ist eine zentrale Aussage:

> **Nicht der absolute Außenpotentialwert liefert die Energie, sondern die Potentialdifferenz zwischen zwei real gekoppelten Umweltports.**

Sind beide Ports praktisch am gleichen Umweltpotential, ist trotz großer absoluter Spannung kein dauerhafter Energiefluss möglich.

## 5. Was bedeutet das für das Testatika-Modell?

Der bisher stärkste interne Mechanismus bleibt:

```text
Rotor -> variable C(theta)
      -> phasenversetzte Gitter/Taster
      -> Crystal-Kommutation
      -> Pot/Leydener-Reservoirs
      -> Feld/Drive-Bias
```

Die Metallplatte kann diesen Kreislauf plausibel über Kapazitätsänderung und einen nichtlinearen Crystal-/Corona-Kippunkt stören.

**Aber der Primärenergiepfad wird durch V4.4 noch enger:**

- normaler 230-V-/50-Hz-Raumfeld-Pickup: zu klein;
- passiver lokaler Schönwetterstrom: um viele Größenordnungen zu klein;
- endlicher Elektret-/Leydener-Speicher: nur kurzzeitig;
- sichtbarer langsamer Rotor: bei Finger-Stopp kaum 100-W-Hauptquelle.

Damit bleiben für eine echte hohe Dauerleistung nur noch Kandidaten, bei denen ein messbarer externer Energiefluss existieren müsste:

1. starkes zeitveränderliches Hochspannungs-/RF-Feld mit **zwei** realen Kopplungsports;
2. ein starker räumlich getrennter Ionen-/Plasmastrom;
3. materialinterne chemische/elektrochemische Energie;
4. eine andere mechanische Quelle;
5. oder die historischen Leistungsangaben waren überschätzt.

## 6. Entscheidender Versuch

Für einen Nachbau wäre jetzt ein **gestufter Abschirmversuch** besonders aussagekräftig:

1. Maschine frei im Raum messen;
2. nur elektrische 50-Hz-/RF-Abschirmung hinzufügen, Luftaustausch offen lassen;
3. Faraday-Käfig schließen, aber kontrollierten Luft-/Ionenpfad erhalten;
4. anschließend auch den Ionen-/Luftpfad filtern bzw. elektrostatisch neutralisieren;
5. gleichzeitig messen:
   - Ausgangsleistung,
   - Rotor-Drehmoment,
   - Strom zur Käfigwand,
   - Käfigpotential,
   - HF-/50-Hz-Spektrum,
   - Ionenstrom durch definierte Öffnungen,
   - Pot-Energie vor/nach dem Test.

Damit ließen sich kapazitive/RF-Kopplung und Ionenenergie experimentell voneinander trennen.

## Code

```text
python sim/m2_v4_4_floating_return_path.py
python sim/m2_v4_4_floating_return_path.py --power-w 300 --field-v-m 100 --height-m 0.5
python -m unittest tests/test_m2_v4_4_floating_return_path.py -v
```
