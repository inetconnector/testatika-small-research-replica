# M2-V4.10 — Kleines Crystal-Gate, großer externer Zwei-Port-Leistungspfad

## Ziel

V4.8/V4.9 haben gezeigt, dass ein sehr kleiner Bias unter günstigen Bedingungen einen Crystal-Arbeitspunkt beeinflussen könnte. Das erklärt jedoch **keine** hohe Ausgangsleistung.

V4.10 trennt deshalb Steuerung und Energiepfad vollständig:

```text
kleiner Gate-/Ionisationspfad
        -> Crystal-Kommutation
        -> schaltet/moduliert einen getrennten externen Zwei-Port-Pfad
        -> Last
```

Das ist prinzipiell wie bei einem Transistor: kleine Steuerleistung kann große Fremdleistung schalten, aber sie erzeugt diese Fremdleistung nicht.

## Externer floating Zwei-Port

Aus V4.5 gilt als bewusst optimistische kapazitive Leistungsobergrenze

```text
P_bound = 2*pi*f*Ceq*(DeltaV_env,rms)^2
```

mit

```text
Ceq = Cfront*Crear/(Cfront+Crear).
```

Für eine räumliche Trennung `h` zwischen den beiden Umweltports wird zusätzlich als günstige Uniformfeld-Näherung angesetzt:

```text
DeltaV_env,rms ~= E_rms * h.
```

Daraus folgt

```text
E_required ~= sqrt(P/(2*pi*f*Ceq)) / h.
```

Diese Rechnung ist bereits großzügig: Sie behandelt die kapazitive Scheinleistung als vollständig nutzbare Obergrenze und enthält noch keine Gleichrichter-, Matching-, Strahlungs-, Leitungs- oder Dielektrikverluste.

## Arbeitsgeometrie

Für die kleine M2 wird als **Arbeitswert**, nicht als historisch gesicherter Portabstand, verwendet:

```text
h = 0.20 m
Cfront = Crear = 100 pF
Ceq = 50 pF.
```

`0.20 m` entspricht ungefähr der bekannten Rotordurchmesser-Skala der kleinen Maschine und ist als günstige Größenordnung zu verstehen.

## Ergebnis: 100 W

Für 100 W ergeben sich ohne Metallplatte:

| Frequenz | erforderliches `DeltaV_env,rms` | erforderliches Uniformfeld bei 0.20 m | kapazitiver RMS-Strom |
|---:|---:|---:|---:|
| 50 Hz | 79.8 kV | 399 kV/m | 1.25 mA |
| 1 kHz | 17.8 kV | 89.2 kV/m | 5.61 mA |
| 10 kHz | 5.64 kV | 28.2 kV/m | 17.7 mA |
| 100 kHz | 1.78 kV | 8.92 kV/m | 56.0 mA |
| 1 MHz | 564 V | 2.82 kV/m | 177 mA |
| 10 MHz | 178 V | 892 V/m | 560 mA |
| 100 MHz | 56.4 V | 282 V/m | 1.77 A |

Damit wird ein wichtiger Punkt sichtbar:

> Höhere Frequenz reduziert die erforderliche Spannung/Feldstärke, erhöht bei gleicher Ziel-Leistung aber den erforderlichen kapazitiven Durchgangsstrom.

Ein 100-W-Pfad über nur `50 pF` Serienkopplung ist daher keineswegs „unsichtbar“: Selbst bei 10 MHz wären in dieser optimistischen Rechnung rund **0.56 A RMS Verschiebungsstrom** im gekoppelten Modus nötig.

## Ergebnis: 300 W

Da die Spannung mit `sqrt(P)` skaliert, braucht 300 W den Faktor `sqrt(3)` mehr Feldspannung.

Bei 10 MHz:

```text
DeltaV_env,rms ~= 309 V
E_rms ~= 1.55 kV/m  (bei h = 0.20 m)
```

Bei 1 MHz:

```text
DeltaV_env,rms ~= 977 V
E_rms ~= 4.89 kV/m.
```

Auch dies sind optimistische Untergrenzen.

## Umgekehrter Test: Was liefert ein gegebenes Feld maximal?

Für `Cfront = Crear = 100 pF`, `h = 0.20 m` und ohne Platte:

| Uniformfeld | 1 MHz | 10 MHz | 100 MHz |
|---:|---:|---:|---:|
| 1 V/m | 12.6 µW | 0.126 mW | 1.26 mW |
| 10 V/m | 1.26 mW | 12.6 mW | 0.126 W |
| 30 V/m | 11.3 mW | 0.113 W | 1.13 W |
| 100 V/m | 0.126 W | 1.26 W | 12.6 W |
| 300 V/m | 1.13 W | 11.3 W | 113 W |
| 1000 V/m | 12.6 W | 126 W | 1.26 kW |

Damit ist die noch offene externe-RF-Hypothese jetzt sehr konkret:

```text
Für 100 W bei 10 MHz und 100-pF-Ports
müsste die Maschine ungefähr 892 V/m RMS Differenzfeld sehen.
```

Für 100 W bei 100 MHz wären immer noch ungefähr

```text
282 V/m RMS
```

nötig — und das bei idealer Nutzung der kapazitiven Scheinleistung.

## Bedeutung für das kleine Gate

Der V4.6-Beispielstrahler lag bei etwa 8 nW. Gegenüber 100 W wäre das Verhältnis

```text
100 W / 8 nW ~= 1.25e10.
```

Das ist **kein Energiegewinn**. Ein Schaltelement darf ein solches Steuer-/Lastleistungsverhältnis haben, solange die 100 W von einer getrennten Quelle kommen.

V4.10 macht deshalb die Logik sauber:

```text
Radio-/Ionisationspfad: eventuell Gate
RF-/Feld-Zwei-Port: müsste die Hauptenergie liefern
Rotor: Timing/Kommutation
Crystal: Schalter/Rectifier
Pots/Leydener: Bias/Puffer
```

Wenn kein externer Zwei-Port mit Leistung in Lastgrößenordnung gemessen wird, kann das Gate die fehlende Energie nicht erklären.

## Metallplatte

V4.5 bleibt gleichzeitig relevant. Eine rückseitige Metallplatte kann

1. den internen Maxwell-/Crystal-Arbeitspunkt verändern und
2. einen externen Front↔Rear-Zwei-Port equalizen bzw. unterdrücken.

Damit könnte ein kleiner Gate-Effekt und ein großer externer Leistungspfad **denselben Plattentest** zeigen. Der Unterschied ist messtechnisch entscheidbar: Beim externen Leistungsmodell müssen an den Umweltports reale Wechselströme/Spannungen in der Größenordnung der Lastleistungsbilanz erscheinen.

## Schärfster Falsifikationstest

Bei laufender Replik gleichzeitig messen:

```text
P_load = <v_load*i_load>
P_mech = torque*omega
P_front = <v_front*i_front>
P_rear  = <v_rear*i_rear>
DeltaE_Pots/dt
P_aux
```

und

```text
P_residual = P_load + losses + dE_store/dt
             - P_mech - P_front - P_rear - P_aux.
```

Für eine externe RF-/Feldquelle muss

```text
P_front + P_rear
```

in der richtigen Vorzeichenkonvention und innerhalb der Messunsicherheit die Lastleistung erklären.

## Konsequenz

V4.10 macht den noch denkbaren konventionellen Hauptenergiepfad **messbar statt mystisch**:

- Ein winziger Gate-Strom kann prinzipiell einen größeren Fremdenergiepfad steuern.
- Aber ein 100-W-Pfad über pF-Kopplungen benötigt hohe HF-Feldstärken und erhebliche Verschiebungsströme.
- Wenn diese Felder/Ströme nicht vorhanden sind, scheidet die externe Zwei-Port-RF-Erklärung aus.

## Code

```text
python sim/m2_v4_10_gate_controlled_two_port_power.py
python sim/m2_v4_10_gate_controlled_two_port_power.py --sweep
python sim/m2_v4_10_gate_controlled_two_port_power.py --target-w 300 --freq-hz 10000000
python -m unittest tests/test_m2_v4_10_gate_controlled_two_port_power.py -v
```

## Sicherheit

Die Datei ist eine Kleinspannungs-/Analysegrundlage und keine Anleitung zum Erzeugen starker HF- oder Hochspannungsfelder. Reale Tests zuerst mit strombegrenzten Kleinspannungs-Surrogaten und geeigneter HF-/HV-Messtechnik durchführen.
