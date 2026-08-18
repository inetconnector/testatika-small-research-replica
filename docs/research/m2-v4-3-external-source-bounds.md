# M2-V4.3 — externe Energiepfade ohne Erdungsdraht

## Ausgangspunkt

V4, V4.1 und V4.2 haben inzwischen drei Dinge getrennt:

1. Ein Testatika-artiges Netzwerk kann **vollständig floating** formuliert werden. Ein Erdungsdraht ist für hohe interne Potentialdifferenzen nicht notwendig.
2. Variable Kapazitäten, Crystal-/Dioden-Kommutation und ein zusätzlicher Corona-/Ionenpfad können einen **Metallplatten-Kippmechanismus** erzeugen.
3. Solange alle diese Elemente passiv sind, entsteht daraus **keine dauerhafte Nettoenergie**. Lastenergie stammt dann aus Anfangsspeicher oder explizit gebuchter mechanischer Arbeit.

V4.3 prüft deshalb nicht noch mehr interne passive Schaltungstopologien. Stattdessen werden die verbleibenden externen Energiepfade quantitativ begrenzt, die auch bei einer Maschine **ohne galvanische Erdung** möglich wären.

## 1. Mechanische Rotorleistung

Für

```text
P = tau * omega
```

folgt bei 15 rpm:

| elektrische Leistung | erforderliches mittleres Drehmoment |
|---:|---:|
| 100 W | 63.66 N m |
| 300 W | 190.99 N m |
| 1000 W | 636.62 N m |

Wenn die historische Beobachtung zutrifft, dass sich der laufende Rotor leicht mit der Hand bzw. einem Finger stoppen ließ, kann der Rotor kaum der direkte Hauptleistungsweg für 100-W- bis kW-Ausgangsleistung gewesen sein.

Damit bleibt die Rotorfunktion als **Taktgeber / elektrostatischer Kommutator** plausibler als die Rolle eines konventionellen Hauptgenerators.

## 2. Kapazitive Kopplung an ein zeitveränderliches externes Feld

Eine floating Maschine kann ohne Draht an eine externe Wechselspannung kapazitiv gekoppelt sein. Für eine Kopplungskapazität `C`, externe RMS-Spannung `V` und Frequenz `f` gilt

```text
I_rms = 2*pi*f*C*V
```

und als bewusst großzügige obere Grenze des verfügbaren Scheinleistungsflusses

```text
S_bound = V * I_rms = 2*pi*f*C*V^2.
```

Die reale nutzbare Wirkleistung kann diese Grenze nicht überschreiten und ist wegen Anpassung, Gleichrichtung und Verlusten geringer.

### 230 V / 50 Hz

| Kopplung C | I_rms | großzügige S-Grenze |
|---:|---:|---:|
| 10 pF | 0.72 µA | 0.166 mW |
| 100 pF | 7.23 µA | 1.66 mW |
| 1 nF | 72.3 µA | 16.6 mW |
| 10 nF | 0.723 mA | 0.166 W |
| 100 nF | 7.23 mA | 1.66 W |
| 1 µF | 72.3 mA | 16.6 W |

Bereits unter dieser optimistischen Grenze wären für 100 W bei 230 V / 50 Hz mindestens

```text
C >= 6.02 µF
```

und für 300 W mindestens

```text
C >= 18.05 µF
```

notwendig.

Das ist kein typischer parasitärer floating-Kapazitätswert einer kompakten Maschine. Eine versteckte normale 50-Hz-Raumfeldkopplung ist damit als Erklärung von 100–300 W sehr unplausibel.

### Hochspannungs-AC wäre anders

Bei einem real vorhandenen externen 10-kV-RMS-/50-Hz-Reservoir läge die optimistische Mindestkopplung für 100 W nur bei ungefähr

```text
3.18 nF
```

und für 300 W bei

```text
9.55 nF.
```

Das wäre geometrisch nicht prinzipiell unmöglich — aber dann müsste **dieses externe 10-kV-Wechselfeld selbst real vorhanden sein** und die Energie liefern. Es wäre also keine quellenlose Maschine, sondern ein kapazitiv gespeister Empfänger.

## 3. Ionischer Ladungsaustausch mit der Umgebung

Der wichtigste strukturelle Unterschied zu V4.0–V4.2 wäre folgender:

```text
sum(Q_machine) = 0
```

muss nicht gelten, wenn die Maschine tatsächlich Ionen in die Luft emittiert oder aus der Luft sammelt.

Dann ist das Gerät zwar weiterhin **ohne Erdungsdraht**, aber energetisch nicht mehr geschlossen. Für extern übertragene Ladung gilt

```text
E_env = integral(V_env dQ_ext)
```

und bei stationärem Strom vereinfacht

```text
P_env = V_env * I_env.
```

Beispiel: Selbst bei einer extrem großzügig angesetzten Potentialdifferenz von 250 kV wären für

```text
100 W -> 0.4 mA
300 W -> 1.2 mA
```

externer Netto-Ladungsstrom erforderlich.

Mit dem für die bisherige atmosphärische Vergleichsrechnung verwendeten Schönwetterwert von ungefähr `2 pA/m²` ergibt die ideale Grenze

```text
100 W -> 200 km²
300 W -> 600 km²
```

wirksame Sammelfläche bei 250 kV.

Damit ist der normale passive Schönwetterstrom keine plausible Quelle für eine kompakte 100-W-Maschine.

Anders wäre die Situation nur, wenn die Testatika **lokal einen um Größenordnungen stärkeren externen Ionenstrom** erzeugte oder anzapfte. Dann müsste dieser Strom aber messbar sein, und die Energie für Ionisation bzw. das aufrechterhaltende externe Feld müsste ebenfalls bilanziert werden.

## 4. Elektret / voraufgeladener Feldspeicher

Ein Elektret oder ein vorgeladener Pot kann den Bias liefern und einen Generator starten. Als reine Energiequelle ist der Vorrat jedoch endlich:

```text
E = 1/2 C V^2.
```

Beispiel:

```text
C = 120 pF
V = 30 kV
E = 0.054 J
```

Bei 100 W wäre dieser ideale Speicher nach nur

```text
0.54 ms
```

erschöpft.

Selbst `1 µF` bei `30 kV` speichert nur

```text
450 J
```

und reicht bei 100 W ideal für ungefähr

```text
4.5 s.
```

Für **100 W während einer Stunde** wären bei 30 kV ideal bereits

```text
800 µF
```

notwendig — bei 300 W entsprechend 2400 µF.

Ein Elektret kann daher sehr gut **Feld/Bias**, aber nicht ohne Nachladung eine lange hohe Dauerleistung erklären.

## 5. Was bleibt nach V4.3 übrig?

Nach den bisherigen Modellen sind folgende einfachen Erklärungen deutlich geschwächt:

```text
Rotor als 100-W-Hauptgenerator
normale 230-V-/50-Hz-Streukapazität
endlicher Leydener-/Elektret-Speicher
passiver Schönwetter-Ionenstrom
rein passive Crystal-/Corona-Schaltung
```

Wenn die historischen Angaben zu geringer Rotorleistung und hoher elektrischer Dauerleistung beide stimmen sollten, verbleiben nur noch enger definierte Kategorien:

1. **ein echter externer, aber drahtlos gekoppelter Energiefluss**, z. B. starkes zeitveränderliches E-Feld / RF / induktive Kopplung;
2. **ein externer Ionen-/Plasmastrom**, dessen Größe mA- statt pA-Ordnung erreichen müsste und dessen Energiequelle identifizierbar sein muss;
3. **eine materialinterne chemische/elektrochemische Energiequelle**;
4. eine andere mechanische Energiequelle als der sichtbare Rotor;
5. oder die historischen Leistungs-/Dauerangaben waren wesentlich zu hoch.

## Wichtigste neue experimentelle Konsequenz

Der nächste Nachbau sollte nicht nur Ausgangsspannung messen, sondern gleichzeitig folgende Bilanzkanäle erfassen:

```text
P_load(t)
P_shaft(t)
I_external_ion(t) und V_machine-to-environment(t)
50-Hz-/RF-Verschiebungsstrom zur Umgebung
E_pot_initial - E_pot_final
Corona-/Crystal-Verluste
```

Besonders aussagekräftig wäre ein vollständiger Faraday-Käfig-Test mit Batterie-/optisch isolierter Messtechnik:

- läuft die Maschine unverändert, fällt gewöhnliche kapazitive/RF-Umweltkopplung stark zurück;
- ändert sich die Leistung stark, muss der gekoppelte Frequenzbereich anschließend gezielt bestimmt werden;
- bleibt ein Netto-Ionenstrom durch den Käfig messbar, wird daraus ein expliziter externer Ladungs-/Energiepfad.

## V4.4 — nächste Priorität

Die nächste Modellstufe sollte deshalb zwei **aktive externe Ports** enthalten, beide mit eigenem Energiekonto:

1. einen zeitveränderlichen kapazitiven Umweltport `V_env(t), C_env`;
2. einen externen Ionenport `I_ion(V,E)`.

Dann kann man direkt testen, welche Kombination aus realistischen `C_env`, Feldstärken und Ionenströmen notwendig wäre, um 100 W oder 300 W dauerhaft zu halten.

Der entscheidende Punkt ist: V4.4 darf keinen ungebuchten Gain enthalten. Sobald 100 W am Ausgang erscheinen, müssen dieselben 100 W plus Verluste an einem expliziten externen Port oder mechanischen Eingang auftauchen.

## Code

```text
python sim/m2_v4_3_external_source_bounds.py
python sim/m2_v4_3_external_source_bounds.py --power-w 300 --rpm 15
python -m unittest tests/test_m2_v4_3_external_source_bounds.py -v
```
