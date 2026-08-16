# Baumanns Erklärsprache entschlüsselt — primärquellen-korrigierte Fassung

**Stand:** 2026-08-16  
**Status:** Forschungsdokument / keine behauptete Originalschaltung  
**Zweck:** Aussagen von Paul Baumann, Methernitha, Stefan Marinov, Hans Holzherr, Albert Hauser und Luzi Cathomen strikt nach Sprecher, Maschine und Übertragungskette trennen und in messbare technische Hypothesen übersetzen.

> Preservation: Die vollständige Fassung vor Entdeckung der Marinov/Hauser-Primärscans bleibt unverändert unter [`../repository-history/baumann-language-decoding-pre-primary-scan-2026-08-16.md`](../repository-history/baumann-language-decoding-pre-primary-scan-2026-08-16.md) erhalten.

---

# 1. Wichtigste Quellenkorrektur: `ANOTHER language` ist direkt belegt

Die frühere Arbeitsfassung hatte korrekt davor gewarnt, die populäre Formulierung **`like an unknown language`** als wörtliches Marinov-Zitat auszugeben. Sie ging aber zu weit mit der Aussage, es gebe überhaupt keinen direkten Marinov-Beleg für eine Sprachbarriere.

Der Archivscan `hauser/SMweb2.jpg` schließt diese Lücke.

Stefan Marinov schreibt dort in eigener Korrespondenz, Baumann habe versucht, ihm das Wirkprinzip zu erklären, Marinov habe es aber nicht verstanden, weil Baumann **`ANOTHER language`** habe.

Damit gilt künftig:

- **direkt primär belegt:** Marinovs Wortlaut `ANOTHER language`;
- **nicht als exaktes Zitat belegt:** die spätere Formulierung `like an unknown language`;
- **unabhängige Konvergenz:** Holzherr berichtet 1999 von Baumanns leiser/schneller und nicht-wissenschaftlicher Ausdrucksweise;
- **institutionelle Konvergenz:** Methernitha verwendet eigene Begriffe und erklärt selbst, konventionelle Terminologie reiche aus ihrer Sicht nur teilweise.

Die korrekte Kurzform ist deshalb:

> **Marinov schrieb direkt, Baumann habe `ANOTHER language`; die bekannte Formulierung `like an unknown language` ist eine spätere, nicht als exakter Wortlaut verifizierte Paraphrase.**

Primärscan-Audit und Hash:

- [`hauser-marinov-primary-scan-audit-2026-08-16.md`](hauser-marinov-primary-scan-audit-2026-08-16.md)
- [`hauser-source-ledger.tsv`](hauser-source-ledger.tsv)

---

# 2. Quellenhierarchie speziell für „Was sagte Baumann / was sahen Besucher?“

| ID | Quelle | Sprecher / Übertragung | Klasse | Verwendbarkeit |
|---|---|---|---|---|
| B01 | ehemalige Methernitha-Web-/Film-Beschreibung | institutionelle Methernitha-Erklärung | O1 | beste Quelle für Methernithas eigene Begriffe; keine unabhängige Physikvalidierung |
| B02 | Hans Holzherr 1999 | direkter Besucher; Baumann vor Ort | P1 | stark für beobachtete Demo und klar Baumann zugeschriebene kurze Aussagen |
| B03 | Principle Experiment 1999 | Holzherr beobachtet Baumanns Demonstration | P1 | stark für Geometrie/Demo; Erklärung des Grundprinzips unvollständig |
| B04 | Linden Experiment | zwei Besucher → Dritter schreibt Erinnerung | H2 | interessante Baumann-Zuschreibung, aber second hand |
| B05 | Stefan Marinov Publikationen | direkte Besuche/Untersuchung | P1/I1 | stark für Beobachtung; eigene Funktionsdeutung separat |
| B06 | Stefan Marinov Primärscans `SMweb2` / `SMwebL1` | direkte Korrespondenz | P1 | jetzt besonders wichtig für `ANOTHER language`, floating Rotorwires, Pots, Crystal/Tesla-Abgrenzung |
| B07 | Luzi Cathomen / Dienst 2001 | direkte Werkstattaufnahme | O1/P1 | wertvoll für Werkstattdenken und große Varianten; nicht Baumann |
| B08 | Albert Hauser 1986/1988 | direkter Besucher + eigene Zeichnungen/Interpretation | P1/I1 | stark für M6a-Geometrie; Funktionen/Schaltung teilweise Interpretation |
| B09 | Mike Watson 2001 | Marinov → Watson → Mail/Web | H2 | Source Lead, keine Primärquelle |
| B10 | Frolov späte Kompilation | unbekannte ältere Ketten | H2/I1 | nur Source Leads |
| B11 | Potter/Kelly/Utkin | Backengineering / Kompilation | S2/I1 | Hypothesen und Vergleichssysteme, keine Baumann-Primäraussagen |

Maschinenzuordnung ist zwingend. Siehe [`machines.yaml`](machines.yaml).

---

# 3. Neue direkte Marinov-Kleinmaschinenanker

Die Primärscans verändern nicht die gesamte Theorie, aber sie reduzieren den zulässigen M2-Rekonstruktionsraum deutlich.

## 3.1 Rotorwires `connected to nothing`

`SMwebL1.jpg` sagt über die Drähte der beschriebenen kleinen Rotorscheibe, sie seien **`connected to nothing`**.

Technische Bedeutung für die bevorzugte Kleinmaschinen-Baseline:

- einzelne Leiter floating;
- kein gemeinsamer Schleif-/Kollektorring;
- kein Hub-Bus;
- keine Nachbarverdrahtung als Baseline;
- Ladungszustand jedes Leiters wird primär durch kapazitive/elektrostatische Kopplung bestimmt.

Das ist eine starke neue Einschränkung gegenüber der späten Frolov-Zuschreibung, benachbarte Lamellen seien über 1 kΩ verbunden.

### Quellenkonflikt

`1 kΩ neighbour ring` bleibt als sekundärer Kontrollversuch zulässig, ist aber **kein M2-Baseline-Detail**, solange keine ältere maschinenspezifische Primärquelle gefunden wird.

---

## 3.2 Zwei Leitungen zu jedem Seitenkondensator

Marinov schreibt in `SMwebL1.jpg`, im referenzierten Kleinmaschinenfoto seien **zwei Leitungen zum rechten und zwei zum linken Kondensator** klar sichtbar.

Zusammen mit seiner Bauteilbeschreibung ergibt sich:

- äußeres zylindrisches Gitter;
- zylindrische Kunststoffisolation;
- zentrale Kupferspirale;
- historische externe Schnittstelle: zwei Leitungen.

Nicht geklärt:

- welches Kabel an welcher Elektrode liegt;
- Polarität;
- floating-/gated-Phasen;
- exakte Kapazität;
- Spiralwindungszahl.

Daher sind versteckte Labortaps erlaubt, aber der historische Testmodus bleibt zweipolig.

Siehe [`pots.md`](pots.md).

---

## 3.3 Kein Tesla-/AC-Kern in Marinovs kleiner Maschine

In `SMweb2.jpg` widerspricht Marinov ausdrücklich einer Tesla-Spulen-/Wechselstrom-Deutung. Die sichtbaren Spiralen seien Elektroden von Kondensatoren, keine Tesla-Transformatoren.

Das ist keine universelle Aussage über jede große Testatika-Variante. Es ist aber ein starker Grund, **Tesla/HF nicht in die M2-Baseline** zu importieren.

---

## 3.4 Kein konventioneller Antriebsmotor in der beschriebenen kleinen Maschine

`SMwebL1.jpg` sagt, die kleine Maschine habe keinen Motor; Marinov interpretiert die Rotation als elektrostatische Abstoßungswirkung.

Das beweist keine Energieanomalie. Es bedeutet nur:

- ein eingebauter konventioneller Motor gehört nicht zur bevorzugten historischen Kleinmaschinen-Baseline;
- ein moderner Labor-RPM-Motor ist Mess-/Testtechnik und muss vollständig abkoppelbar sein.

---

## 3.5 `crystal`, nicht automatisch `rectifier`

Marinov schreibt, Baumann habe ihm gegenüber vom **`crystal`** gesprochen und nicht vom `rectifier`.

Diese Quellen müssen getrennt bleiben:

1. **Baumann → Marinov Kleinmaschinenlinie:** `crystal`, Material/Funktion unbekannt;
2. **Methernitha institutionell:** `rectifying diode` halte den Anziehungs-/Abstoßungszyklus im Takt;
3. **Hauser M6a:** Kristall(e) im oberen Bereich beobachtet; `rectifier` teilweise Hausers Funktionsinterpretation;
4. **Holzherr frühes Kleinmodell:** grobe Wicklung um Zentralleiter mit vier Leads aus Erinnerung.

Eine funktionale Verwandtschaft ist plausibel und testbar, aber eine Identität ist nicht bewiesen.

---

# 4. Methernithas institutionelle Begriffe — technische Übersetzung

## 4.1 Wolke / Erde

Nicht automatisch: atmosphärische Energiequelle.

Konservative Übersetzung:

**zwei elektrostatische Potential-/Feldreservoirs bzw. Polaritätsräume.**

## 4.2 Gitter „hält Ladung fest“

Messbare Kandidaten:

- field-forming / floating electrode;
- induzierte Oberflächenladung;
- kapazitiver Speicher;
- Raumladungs-/Corona-Steuerung;
- reduzierte Leckage / Ladungspersistenz.

Perforation verändert Feldpenetration, Randlänge, Corona und die Kapazitätsmatrix und ist deshalb experimentell wesentlich.

## 4.3 `Taster` / `antenna keys`

Konservativ:

**nichtkontaktierender kapazitiver/Influenz-Abnehmer.**

Nicht automatisch:

- Funkantenne;
- HF-Resonator.

Messen:

- lokale Potentiale;
- displacement current;
- induzierte Ladung;
- ggf. Ionenstrom.

## 4.4 Ladungen „ordnen“

Technische Arbeitsübersetzung:

**polarity sorting / charge routing / asymmetrische Ladungsübertragung.**

## 4.5 `rectifying diode` hält den Zyklus im Takt

Eine Diode im mechanischen Anziehungs-/Abstoßungszyklus kann:

- Rückladung in bestimmten Rotorphasen sperren;
- erst oberhalb eines Schwellwerts Ladung transferieren;
- floating node über eine Winkelphase klemmen;
- positive/negative Drehmomentphasen asymmetrisch machen;
- einen wiederkehrenden Grenzzyklus stabilisieren.

Arbeitsbegriff:

**phasenselektives nichtlineares Ladungsventil / elektrostatischer Kommutator.**

## 4.6 Langsam und gleichmäßig

Plausible klassische Zeitkonstanten:

- `R*C`;
- Oberflächenleckage;
- dielektrische Relaxation;
- Corona-/Ionentransport;
- Charge trapping;
- Crystal-/Diodenschwelle.

Daher kein universeller 50/60-rpm- oder 50-Hz-Schluss. Das Archiv belegt ohnehin maschinenspezifische ~15-rpm- und ~60-rpm-Linien.

## 4.7 Gitterkondensatoren

Konventionell erklärbar als:

- Ladungsspeicher;
- DC-Puffer;
- Glättung;
- floating Potentialreservoir.

Sie erzeugen nicht automatisch Energie.

## 4.8 Hohe Spannung heruntersetzen / Leistung aufbauen

Technische Kandidaten:

- gepulste Impedanzumformung;
- Ladungsumlagerung zwischen unterschiedlichen Kapazitäten;
- induktive Zwischenstufe bei zeitlich veränderlichem Strom;
- charge pump;
- Pulsformung.

Bei ideal konstantem DC funktioniert kein gewöhnlicher Transformator; eine induktive Umformung setzt zeitliche Änderungen voraus.

## 4.9 Trockene Luft funktioniert besser

Vollständig mit bekannter Elektrostatik vereinbar:

- PMMA-Oberflächenleitfähigkeit;
- Ladungsspeicherung;
- Corona-Onset;
- Ionenpfade;
- Leckstrom

ändern sich mit Feuchte.

Daher RH kontrollieren; keine exotische Physik nötig, um eine Feuchteabhängigkeit zu erklären.

---

# 5. Principle Experiment — stärkster einfacher Mechanismus-Hinweis

Holzherr 1999 beobachtet:

- schwenkenden Plexiglasarm;
- quadratisch perforiertes Aluminium;
- Messinggitter;
- gestapelte Plexiglas-/Gitterlagen;
- zwei parallele Kondensatoren;
- ungefähr zehn Hin-/Herbewegungen;
- berichtete ~60 V DC;
- hörbare Entladung beim Kurzschluss.

Baumann wird die konkrete Aussage zugeschrieben, mit **geschlossener Metallfolie statt Drahtgitter** entstehe der Effekt nicht in gleicher Weise.

Das rechtfertigt einen streng kontrollierten `mesh/perforated vs foil`-Test.

Gitter/Folie ändern gleichzeitig:

- Kapazitätsmatrix;
- Randfeld;
- Corona-Onset;
- Ionentransport;
- Feldpenetration;
- Oberflächenladungsverteilung.

Deshalb darf ein Unterschied nicht vorschnell einer exotischen Energiequelle zugeschrieben werden.

---

# 6. Linden-Experiment — interessante, aber schwache Baumann-Semantik

Überlieferung: Besucher → Erinnerung → Dritter/Web. Status **H2**.

Baumann wird sinngemäß zugeschrieben:

- sehr feine zufällig bewegte Teilchen existierten;
- deren Fluss müsse „gerichtet/gleichgerichtet“ werden.

Operational brauchbare Übersetzung:

> Ein zunächst bidirektionaler/fluktuierender Ladungs- oder Feldprozess soll durch Geometrie/Nichtlinearität in einen gerichteten Transfer überführt werden.

Mögliche konventionelle Träger/Quellen:

- Luftionen / Raumladung;
- induzierte Leiterladung;
- mechanisch modulierte Kapazität;
- atmosphärisches Feld;
- Corona;
- gespeicherte Electret-/Dielektrikumsladung;
- externe EM-Kopplung.

Thermisches Gleichgewichtsrauschen allein kann nicht passiv zu dauerhafter Nettoarbeit gleichgerichtet werden.

---

# 7. Albert Hauser: direkte Großmaschinenbeobachtung, nicht M2-Schaltplan

Die Primärscans 1986/1988 liefern wertvolle M6a-Geometrie:

- ~500 × 5 mm Plexiglasdisk;
- ~50 Chromstahl-Lamellen;
- gegenläufige Disc-Linie;
- ungefähr 8 perforierte stationäre Elektroden vorn + 6 hinten;
- ausdrücklich kein Reibkontakt;
- Geschwindigkeits-/Magnetrad-Hardware;
- komplexe Zylinder mit **drei konzentrischen Metallgittern**, Acryltrennung, zentraler Magnetröhre und zweilagiger/bifilarer Cu-Wicklung;
- obere Kristallregion; `rectifier` als teilweise Hauser'sche Deutung.

Diese Daten erklären, warum spätere Rekonstruktionen große Testatika-Zylinder als Coil-/Magnetmodule darstellen.

Sie dürfen aber **nicht** den viel einfacher beschriebenen Marinov-Kleinmaschinen-Pot überschreiben.

Siehe [`hauser-marinov-primary-scan-audit-2026-08-16.md`](hauser-marinov-primary-scan-audit-2026-08-16.md).

---

# 8. Luzi Cathomen / Dienst 2001 — Werkstattlinie

Die RealMedia-Metadaten im Archiv verankern:

- Dieter Dienst;
- 17.11.2001;
- Besuch in Methernitha-Laboren;
- Gespräch mit Luzi Cathomen.

Cathomen ist **nicht Paul Baumann**.

Werkstattaussagen umfassen sinngemäß:

- große Rotorsegmente als spezielle/magnetisierbare Legierungen;
- ~60 rpm auf bestimmten großen Varianten;
- Kondensatoren/Leydener Flaschen;
- sehr hohe interne Spannungen;
- obere Stufen mit Kapazitäts-/Magnet-/Spulenbezug;
- Fühler/Synchronsteuerung;
- Entwicklung aus statischer Elektrizität;
- Kernproblem: nicht nur einen Spannungsimpuls erzeugen, sondern Spannung **aufrechterhalten**.

Der letzte Punkt unterstützt als Arbeitshypothese eine **zyklische Bias-Regeneration**, aber keine Energiequelle.

---

# 9. Vollständiger Videoaudit — neue externe M2-Geometrie

Alle acht Archivvideos wurden vollständig durch die Videostreams traversiert: **35.445 decodierte Frames**.

Besonders wichtig: `meth4.asf` zeigt dieselbe kleine Baugruppe wie `testabig.jpg`.

Neue/gestärkte sichtbare Details:

- zwei kupferfarbene, wahrscheinlich räumliche C-/Bogenstücke am Hub;
- mehrlagige Außenpanels aus grobem Träger, dunklem feinem Gitter, länglichem rötlichem Element und Leads;
- unteres Zentralmodul eher als perforierter Käfig/Prisma denn als massiver Zylinder;
- Seitenpots mit mehreren sichtbaren strukturellen Ebenen, ohne dass ihre interne Verdrahtung aus der Videoauflösung abgeleitet werden kann.

Siehe [`video-frame-audit-2026-08-16.md`](video-frame-audit-2026-08-16.md).

---

# 10. Marinovs eigenes Funktionsmodell — Interpretation, nicht Baumanns Schaltplan

Marinov entwickelte später ein Modell aus:

- Influenzgenerator;
- elektrostatischem Motor;
- gemeinsamem Rotor;
- möglicher Trennung von hochspannungs-/kleinkapazitivem Drive-Bus und größerem Load-/Storage-Bus.

Das ist als Topologieklasse plausibel und testbar.

Marinovs eigene Experimente erzielten jedoch nicht den behaupteten hohen Testatika-Strom. Das ist eine wichtige negative Information: Selbst wenn die Topologieklasse stimmt, fehlt weiterhin ein Mechanismus, der historische hohe Lastclaims quantitativ erklärt.

---

# 11. Quellenübergreifendes Arbeitsmodell

Das derzeit stärkste falsifizierbare Modell lautet:

> **phasengesteuertes elektrostatisches Charge-State-Management einer selbstangeregten/initial geladenen Variable-C-Maschine mit floating Rotorleitern, nichtkontaktierenden Pickups, Gitter-Feldsteuerung, nichtlinearer Crystal-/Dioden-Kommutation, getrennten Drive-/Storage-Knoten und zyklischer Bias-Regeneration.**

Blockweise:

```text
        START / PRIMING / INITIAL CHARGE
                    |
                    v
        [floating sector rotor]
                    |
           C(theta), influence
                    v
        [grid / pickup nodes]
                    |
         polarity / charge routing
                    v
       [crystal / diode hypothesis]
             /               \
            v                 v
     [HV DRIVE BUS]      [LOAD/STORE BUS]
            |                 |
     electrostatic torque     | buffer / output
            |                 v
            +----> ROTOR     DC LOAD
              ^
              |
        possible regeneration
```

Dieses Diagramm ist **kein Originalschaltplan**.

---

# 12. Mathematisches Minimalmodell

Für mehrere floating/leitfähige Knoten ist eine winkelabhängige Kapazitätsmatrix sinnvoll:

`Q_i = sum_j C_ij(theta) * (V_i - V_j)`

und

`I_i = dQ_i/dt`.

Damit entstehen Beiträge aus:

- `dV/dt` bei gegebener Geometrie;
- `dC/dt` durch Rotorbewegung.

Für ein vereinfachtes elektrostatisches Drehmoment gilt qualitativ:

`tau_e ~ 1/2 * V^2 * dC/dtheta`.

Floating Sektoren machen die vollständige Knoten-/Kapazitätsmatrix wichtiger als eine einfache Ein-Kondensator-Näherung.

Eine Diode/ein nichtlinearer Kristallpfad macht das System stückweise nichtlinear:

- Knoten lädt floating;
- Schwellwert wird erreicht;
- Ladung wird übertragen;
- Pfad sperrt wieder;
- Rotorwinkel bestimmt die Phase.

---

# 13. Energiefrage: was das Arbeitsmodell nicht erklärt

Selbst wenn die gesamte Charge-State-Architektur stimmt, bleibt offen:

> **Woher stammt die unter Last übertragene Nettoenergie?**

Jeder Versuch muss bilanzieren:

- mechanische Rotorarbeit;
- externe Laborantriebsenergie;
- Initial-/Primingladung;
- gespeicherte Kondensator-/Electretenergie;
- Biasquellen;
- Hilfselektronik;
- atmosphärisches Feld;
- Corona/Ionisation;
- RF/EM-Einkopplung;
- Temperatur-/Feuchtegradienten;
- chemische/materialbedingte Energie.

Bilanz:

`E_out <=/> E_mech,in + E_bias,in + E_aux,in + E_stored,initial - E_stored,final`

Eine Anomalie ist erst diskutierbar, wenn die Unsicherheit deutlich kleiner als eine reproduzierbare positive Differenz ist.

Hohe Leerlaufspannung, ein kurzer Lampenlauf oder Nachlauf beweisen keinen Energieüberschuss.

---

# 14. Priorisierte Hypothesen nach dem Primärscan-Upgrade

| Code | Hypothese | Aktueller Status | stärkster Test |
|---|---|---|---|
| B-H01 | Taster = kapazitiver Influenz-Pickup | stark | `C(theta)` + Pickup-Strom |
| B-H02 | M2-Rotorsektoren sind elektrisch floating | **stark für beschriebene Kleinmaschine** | Isolations-Baseline + Vergleich gegen E1-Ring |
| B-H03 | `ordnen` = polarity-selective charge routing | stark-mittel | Mehrkanal U/I vs Rotorwinkel |
| B-H04 | Crystal/Diode kann phasenselektives Gate sein | mittel | Open/short/R/C/verschiedene Dioden vs Phase/Torque |
| B-H05 | slow/steady = elektrische Relaxations-/Phasenbedingung | mittel-stark | 5–60-rpm Sweep + Node Map |
| B-H06 | Mesh funktionell wegen Feld/Corona/Charge transport | mittel-stark | geometriekontrollierter Mesh-vs-Foil-Test |
| B-H07 | PMMA-Ladungszustand beeinflusst Start/Feld | mittel | conditioned-vs-neutral + Surface Potential/RH |
| B-H08 | Drive- und Load-Bus getrennt | mittel | Node Mapping + Load Perturbation |
| B-H09 | Rotor bleibt Bias-/Feldmodulator statt direkter galvanischer Output | mittel-stark | Rotorpotential/torque unter Last |
| B-H10 | Hub-Arcs sind elektrisch/feldtechnisch relevant | neu, mittel-niedrig | arcs floating/terminal/dummy/absent |
| B-H11 | größere Zusatzmodule dienen Impedanz-/Pulsumformung | mittel-low, M6 | Waveform-/Energieanalyse |
| B-H12 | random particles = Luftionen | low-mittel | Ionenzähler + kontrollierte Atmosphäre |
| B-H13 | Ost-West-Effekt real | niedrig | randomisierter Orientierungstest |
| B-H14 | Permanentmagnete sind universelle Energiequelle | sehr niedrig / verworfen als Universalmodell | small-machine magnet/no-magnet A/B |
| B-H15 | Tesla/HF ist notwendiger M2-Kern | niedrig / gegen Marinov | keine M2-Baseline; nur Vergleich |
| B-H16 | thermisches Gleichgewichtsrauschen liefert passiv Nettoarbeit | verworfen ohne Nichtgleichgewichtsquelle | geschlossene Energiebilanz |
| B-H17 | 1-kΩ-Nachbarring ist M2-Original | **niedrig und Primärquellenkonflikt** | ältere maschinenspezifische Primärquelle nötig |

---

# 15. Experimente mit höchstem Informationsgewinn

## X1 — Floating E0 vs Secondary E1

Geometrisch identische Rotoren:

- E0: jedes Segment floating;
- E1: 1-kΩ-Nachbarverbindung nur als Sekundär-Kontrollhypothese.

Messen:

- `C(theta)`;
- Sektorpotentiale;
- Ladungsrelaxation;
- Pickup-Strom;
- Torque;
- Lastreaktion.

## X2 — phasenaufgelöste Node Map

Synchron erfassen:

- Rotorwinkel;
- alle Pickup-Potentiale;
- Pot-Terminals;
- Crystal-/Gate-Strom;
- Speicherenergie;
- Torque/rpm.

## X3 — Crystal-Falsifikation

- offen;
- kurz;
- R;
- C;
- verschiedene Dioden/Schwellen;
- antiparallel;
- geeigneter historischer Kristalldetektor.

## X4 — Mesh vs Folie

Gleiche Geometrie/Abstände/Materialklasse; messen:

- C;
- Leakage;
- Corona-Onset;
- Ionenstrom;
- Surface Potential;
- Torque;
- charge/cycle.

## X5 — RH / PMMA

- 10 / 20 / 40 / 60 / 80 % RH;
- conditioned / neutralized PMMA;
- Surface Potential Decay;
- Leakage;
- C(theta);
- Corona;
- Torque.

## X6 — Hub-Arcs

- leitend floating;
- leitend instrumentiert;
- nichtleitender Dummy;
- absent.

Keine historische Verbindung voraussetzen.

## X7 — Load Reaction

Offen vs definierte Lasten; gleichzeitig:

- rpm;
- Torque;
- Drive/Bias input;
- Load V/I;
- Speicherenergie vorher/nachher.

## X8 — Shield / Environment

- rear shield floating/geerdet/R/C gekoppelt;
- Abstand variieren;
- Orientierung randomisieren;
- 3-axis B-field, E-field, RH und Temperatur loggen.

---

# 16. Quellen, die niemals still zusammengeführt werden dürfen

## Marinov M2/M3 Kleinmaschinen

- floating wire sectors;
- zwei Pot-Leitungen;
- no rubbing;
- small-pot grid/plastic/spiral;
- `crystal`;
- no Tesla/AC interpretation;
- kein konventioneller Motor in beschriebener Kleinmaschine.

## Hauser M6a

- ~500-mm Discs;
- 50 sheet lamellae;
- 8/6 non-contact stators;
- magnet-wheel regulation;
- 3-grid/magnet-tube/bifilar cylinders;
- top crystal/possible rectifier.

## Holzherr M6b / M4

- ~15-rpm 50-cm Demo;
- 20-layer large capacitors;
- ~12-cm models;
- four-lead early top-module memory;
- three-side-change wire routing on several machines.

## Dienst/Cathomen M7 / multiple workshop machines

- side/rear views;
- special alloys;
- ~60-rpm line;
- magnet/coil/upper conditioning systems;
- synchronization language.

## Potter/Kelly/Frolov

- reconstruction / secondary theories;
- never automatically promoted over direct machine-specific evidence.

---

# 17. Aktuelles Forschungsurteil

## Deutlich besser verstanden

Die historischen Begriffe lassen sich weitgehend auf bekannte elektrostatische Funktionsklassen abbilden:

- floating charge nodes;
- variable capacitance;
- Influence pickup;
- field-shaping grids;
- polarity routing;
- nonlinear threshold conduction;
- phase commutation;
- charge storage;
- possible impedance conversion.

Die neuen Primärscans machen die kleine Replik **konkreter**:

- floating Rotordrähte als bevorzugte Baseline;
- zweipolige Pots;
- kein Tesla-/AC-Baselinekern;
- kein konventioneller eingebauter Antriebsmotor;
- `crystal` als authentischer Begriff, Funktion weiter unbekannt.

## Weiter nicht gelöst

- exakte M2 through-disc route;
- vollständige statische Elektrodenzuordnung;
- M2 node-to-node circuit;
- Pot-Polung/Innenanschluss;
- Crystal-Material/I-V;
- Hub-Arc-Funktion;
- Magnetfunktion;
- Primingzustand;
- Energiequelle der historischen Leistungsclaims.

### Präziseste aktuelle Aussage

> **Baumanns/Methernithas Sprache lässt sich plausibel als phasenabhängiges elektrostatisches Charge-State-Management lesen. Die neuen Marinov-Primärscans engen die kleine Maschine auf floating Rotorleiter, zweipolige Kondensator-Pots und eine nicht-Teslaartige elektrostatische Architektur ein. Das verbessert die Reproduzierbarkeit erheblich, liefert aber weiterhin weder den authentischen vollständigen Schaltplan noch einen Nachweis von Nettoenergieerzeugung.**

---

# 18. Quellenregister

## Primär-/nahe Quellen im Archiv

- `hauser/SMweb2.jpg` — Marinov direct correspondence (`ANOTHER language`, Tesla/AC-Abgrenzung).
- `hauser/SMwebL1.jpg` — Marinov direct correspondence (floating wires, pots, two leads, no motor, `crystal`).
- `hauser/ABweb1.jpg`, `ABweb2.jpg`, `ABweb3.jpg`, `ABweb4.jpg`, `ABweb9.jpg` — Hauser 1986 visit/drawings.
- `hauser/AHwebL7.jpg`, `AHwebl8.jpg` — Hauser 1988 large-cylinder details.
- `HTML_UND_BILDER/report99.htm` — Holzherr 1999 witness report.
- `video/meth1.asf` … `meth5.asf`, `testa01.ram`, `testa02.ram`, `testatikadeutsch.wmv` — historical media corpus.

Repository provenance:

- [`hauser-source-ledger.tsv`](hauser-source-ledger.tsv)
- [`video-source-ledger.tsv`](video-source-ledger.tsv)
- [`archive-source-ledger.tsv`](archive-source-ledger.tsv)
- [`evidence_matrix.tsv`](evidence_matrix.tsv)

## Other near/secondary sources

- archived Methernitha technical description;
- Linden Experiment transmission;
- Mike Watson recollection;
- Potter/Kelly/Frolov source leads.

## Physikalische Kontrollliteratur

- Wommelsdorf US883846A — historical multiple-influence/condenser machines;
- PMMA charge storage DOI `10.1016/S0304-3886(98)00023-0`;
- grid-corona geometry DOI `10.1016/j.elstat.2019.103367`;
- humidity / three-electrode corona DOI `10.1016/0304-3886(95)00009-Y`.

---

# 19. Regel für zukünftige Quellenfunde

Jede technische Aussage wird mindestens mit folgenden Feldern gespeichert:

```yaml
statement_id: ...
speaker: ...
transmission: direct_scan|direct_audio|direct_witness|letter|second_hand|compilation
archive_or_url_locator: ...
file_sha256: ...
date_as_source: ...
machine_id: M0|M2|M3|M4|M6a|M6b|M7|MX
source_wording_short: ...
paraphrase: ...
evidence_class: ...
confidence: ...
conflicts: [...]
cad_implication: ...
experiment_implication: ...
```

**Interpretationen dürfen nie in das Feld `source_wording_short` hineingeschrieben werden.**
