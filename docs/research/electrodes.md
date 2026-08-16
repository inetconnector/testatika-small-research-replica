# Elektroden — Baseline und Testgeometrie

Marinov korrigiert die Bezeichnung „brushes“ ausdrücklich: Es gibt keinen Schleifkontakt.
Er beschreibt bei seinem eigenen Vergleichsmotor **sektorielle Elektroden**, deren Winkel und Höhe einstellbar sind. Er vermutet, dass Testatika-Elektroden sowohl Sammel- als auch Antriebsaufgaben haben könnten; ob es getrennte Gruppen sind, blieb ihm unklar.

V2 verwendet deshalb:
- 6 nominale Elektrodenrahmen;
- vollständig verstellbaren Winkel;
- verstellbare Höhe/Abstand;
- Metallgaze/Lochblech als echte Elektrode, gedruckter Rahmen nur als Träger.

## Funktionsbaseline
Für einen reproduzierbaren **extern gespeisten** Elektrostatik-Motortest kann zunächst die aus Marinovs Vergleichsmotor bekannte Anordnung mit zwei oder vier sektoriellem Elektrodenpaaren getestet werden. Dazu nur eine geeignete gekapselte, strombegrenzte Lehr-/Labor-Elektrostatikquelle verwenden.

Die externe Testanordnung beweist keine Testatika-Selbstversorgung; sie dient ausschließlich dazu, Mechanik, Elektrodenwinkel und Drehmoment zu validieren.

## Optionaler V3-A/B-Test: Gitter gegen Vollfolie

Der Bericht zum sogenannten Principle Experiment schreibt Baumann die Aussage zu, dass eine perforierte/Gitter-Elektrode funktioniere, während normale Metallfolie den Effekt nicht reproduziere. Dies ist ein historischer Claim, kein kontrollierter Nachweis.

Weil moderne Elektrostatik zeigt, dass Gittergeometrie Corona-Onset, Feldverteilung und Stromdichte deutlich verändern kann, ist die Aussage jedoch gut falsifizierbar.

`cad/generate_v3_experiments.py` erzeugt deshalb:

- `electrode_ab_carrier`
- `electrode_ab_clamp`
- `electrode_material_template`
- Abstandsmesslehren für 1 / 2 / 3 mm

Für A und B wird **derselbe Träger** verwendet. Nur der leitfähige Einsatz wechselt:

- A: Vollfolie
- B: Metallgitter / Lochblech

Konstant halten:

- aktive Öffnung;
- Außenkontur;
- Abstand zum Rotor;
- Elektrodenwinkel;
- Biasquelle;
- Rotor/Routing;
- Temperatur und relative Feuchte;
- Messverkabelung.

Messgrößen:

- Kapazität;
- Leckstrom;
- Corona-Onset;
- Strom-/Ladungswellenform;
- Oberflächenpotential;
- elektrostatisches Drehmoment.

Ein reproduzierbarer Unterschied zwischen Gitter und Folie wäre zunächst ein **Geometrie-/Corona-/Feldeffekt**, kein Nachweis eines Energieüberschusses.

Siehe `docs/research/r4-grid-vs-foil.md`.
