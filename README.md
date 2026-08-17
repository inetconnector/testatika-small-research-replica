# Testatika-Forschungsreplik — Kleine M2 + Große M6

<p align="center">
  <strong>Deutsch</strong> · <a href="README.en.md">English</a>
</p>

[![Repository validieren](https://github.com/inetconnector/testatika-small-research-replica/actions/workflows/validate.yml/badge.svg)](https://github.com/inetconnector/testatika-small-research-replica/actions/workflows/validate.yml)
![Status](https://img.shields.io/badge/status-research%20replica-orange)
![CAD](https://img.shields.io/badge/CAD-STEP%20%7C%20STL%20%7C%20GLB-blue)
![Lizenz](https://img.shields.io/badge/license-MIT-green)

<!-- README-SYNC:principle-report -->
## Funktionsprinzip „Erde – Wolke – Gewitter“

Die ausführliche quellengeleitete technische Zusammenfassung der aktuellen Arbeitshypothese — einschließlich variabler Kapazität, Influenz, Gitter/Taster, Crystal-/Dioden-Phasenkommutation, elektrostatischem Drehmoment, Drehzahlstabilisierung, Trockenluft-/Feuchteabhängigkeit und der offenen Energiebilanz — liegt als Word-Dokument in beiden Sprachen vor:

- **Deutsch:** [`Testatika_Funktionsprinzip_Erde_Wolke_Trockenluft.docx`](docs/research/Testatika_Funktionsprinzip_Erde_Wolke_Trockenluft.docx)
- **English:** [`Testatika_Functional_Principle_Earth_Cloud_Dry_Air.docx`](docs/research/Testatika_Functional_Principle_Earth_Cloud_Dry_Air.docx)

> Die Dokumente beschreiben eine testbare elektrostatische Arbeitshypothese und sind kein Nachweis für Overunity oder eine ungeklärte Nettoenergiequelle.

<!-- README-SYNC:build-lines -->
<!-- BUILD-LINES-START -->

## Hier beginnen — reale Fertigungs-Bausätze

| Baulinie | Fertigungs-Bausatz | Montage-/Passungsansicht | Alte Vollmodell-Referenz |
|---|---|---|---|
| **Kleine M2 — V5 Fertigungs-Bausatz** | [`testatika-m2-v5-fabrication-kit.zip`](release/fabrication-kits/testatika-m2-v5-fabrication-kit.zip) | [STEP](hardware/build-kits/m2-v5/assembly-reference/Testatika_M2_V5_FABRICATION_ASSEMBLY_REFERENCE_NOT_FOR_PRINT.step) | [V4 Referenz, nur Ansicht](hardware/experimental/v4-best-evidence-m2/reference-visual-only/complete-model/Testatika_M2_V4_REFERENCE_VISUAL_ONLY.step) |
| **Große M6 — V2 Fertigungs-Bausatz** | [`testatika-m6-v2-fabrication-kit.zip`](release/fabrication-kits/testatika-m6-v2-fabrication-kit.zip) | [STEP](hardware/build-kits/m6-v2/assembly-reference/Testatika_M6_V2_FABRICATION_ASSEMBLY_REFERENCE_NOT_FOR_PRINT.step) | [V1 Referenz, nur Ansicht](hardware/experimental/m6-large-v1-best-evidence/reference-visual-only/complete-model/Testatika_M6_LARGE_V1_REFERENCE_VISUAL_ONLY.step) |

**Wichtig:** STL-Dateien unter `hardware/build-kits/*/print/` sind ausschließlich echte Druckteile wie Halter, Clips, Jigs und Schutzteile. Leiter, Metallgitter, Lamellen, Magnete, Wellen, Lager und PMMA-Rotorscheiben werden als reale Fertigungs-/Kaufteile ausgeführt. Primär tragende Lagerträger und Rotorhubs sind ebenfalls reale Metall/G10-Fertigungsteile. Assembly-STLs sind nur Passungs-/Ansichtsmodelle und ausdrücklich **nicht zum Drucken**. Die historisch unbekannte interne Schaltung bleibt modular/offen statt erfunden.

<!-- BUILD-LINES-END -->

<!-- README-SYNC:intro -->
**Evidenzgeleitetes Testatika-Rekonstruktionsprojekt mit zwei getrennten Baulinien: der kleinen Marinov-M2 und der großen ~500-mm-M6-Familie.**

> Dieses Repository ist ein historisches/elektrostatisches Forschungsprojekt. Es wird **nicht** als bewiesene Freie-Energie- oder Overunity-Maschine dargestellt. Die vollständige ursprüngliche elektrische Schaltung ist nicht bekannt; eine Nettoenergie-Anomalie wird hier nicht behauptet.

![Photogrammetrische Frontansicht](docs/images/photogrammetric_front_view.png)

<!-- README-SYNC:replication-completeness -->
## Replikationsvollständigkeit — zuerst lesen

Das Repository soll so nahe wie es die erhaltene Evidenz erlaubt an eine **1:1-Forschungsreplik** von Marinovs erster kleiner Maschine (M2) herankommen. Fehlende historische Informationen werden **nicht** in erfundene Gewissheit umgewandelt.

Das verbindliche Vollständigkeitsregister ist [`docs/REPLICATION_STATUS.md`](docs/REPLICATION_STATUS.md). Für jedes wichtige Teilsystem wird dort festgehalten, ob ein Detail beobachtet, quellenbelegt, aus Foto/Video abgeleitet, hergeleitet, hypothetisch, widersprüchlich oder weiterhin unbekannt ist.

„Vollständige Forschungsreplik“ bedeutet daher: Alle quellenbelegten Geometrien und Materialien sind abgebildet, ungelöste Alternativen werden soweit praktisch reversibel/testbar gemacht und das Experimentpaket kann konkurrierende Hypothesen unterscheiden. Es bedeutet **nicht**, unbekannte Originalverdrahtung, Kristallmaterial oder Topf-Topologie zu erraten und als historische Tatsache auszugeben.

<!-- README-SYNC:m2-target -->
## Bauziel kleine M2: V4 Best-Evidence M2

Für einen **neuen physischen Nachbau** ist V4 zu verwenden; die älteren V2/V3-Modelle sind nicht als endgültige Baugruppe zu behandeln.

V4 verbindet die stärksten direkten Marinov-Scanbedingungen mit dem vollständigen Foto-/Video-Audit:

- ein Rotor mit ~200 mm Durchmesser;
- Varianten mit 20/24/25 Elementen, nominal 24;
- **einzeln potentialfreie Rotordrähte** — kein galvanischer Nachbarring in der M2-Basislinie;
- R0 als am wenigsten spekulative nominale Führung und R4 als separater Forschungsrotor;
- keine schleifenden Kollektoren;
- zwei seitliche Töpfe mit Gitter + Dielektrikum + innerer Cu-Spirale;
- **genau zwei historische externe Anschlusspositionen pro Topf**;
- kein eingebauter konventioneller Antriebsmotor;
- zwei sichtbare Hufeisenmagnet-Positionen plus passende nichtmagnetische Kontrollen;
- videobasierte Verfeinerungen von Nabenbögen, geschichteten Außenplatten und unterem Zentralkäfig;
- ungelöster `crystal` als entnehmbare Blackbox statt als erfundene Originalschaltung.

Einstieg:

- [`docs/research/v4-best-evidence-m2.md`](docs/research/v4-best-evidence-m2.md)
- [`docs/research/v4-bom.md`](docs/research/v4-bom.md)
- [`docs/research/v4-assembly.md`](docs/research/v4-assembly.md)
- [`docs/research/v4-electrical-boundary.md`](docs/research/v4-electrical-boundary.md)
- [`docs/research/v4-printing.md`](docs/research/v4-printing.md)

Generator:

`cad/generate_v4_best_evidence_m2.py`

Materialisierte Ausgabe:

`hardware/experimental/v4-best-evidence-m2/`

Deterministisches Baupaket:

`release/experimental/testatika-m2-v4-best-evidence-build-package.zip`

<!-- README-SYNC:included -->
## Enthalten

Dieses Repository zielt auf die **kleine Einscheibenmaschine rechts in Marinovs Abbildungen 13/14**, während ältere und maschinenübergreifende Forschung getrennt erhalten bleibt.

- nominaler **200-mm-Rotor**;
- **20 / 24 / 25** radiale Kupferdraht-Rotorvarianten;
- nach Direktquellen bevorzugte elektrische **Floating-Sector**-Topologie;
- experimentelle Führungsfamilien R0–R4;
- berührungsfreie, einstellbare Sektorelektroden;
- zwei seitliche Kondensator-/„Topf“-Module: Außengitter + Dielektrikum + innere Kupferspirale;
- quellenbelegte Zweidraht-Schnittstelle der Töpfe;
- zwei Hufeisenmagnet-Positionen für die erste Kleinmaschinenvariante;
- austauschbarer „Kristall“-Träger;
- videoabgeleitete Verfeinerungen an Nabenbogen, Schichtplatten und Zentralkäfig;
- Versuchsvorrichtung für die hintere Abschirmplatte;
- erhaltene V2- und V3-STEP/STL-Forschungsmodelle;
- reproduzierbare vollständige V4-STEP/STL-Baugruppen;
- Evidenzmatrix, Photogrammetrie, BOM, Montage- und Experimentdokumentation;
- konsolidierte Forschungswissensbasis in [`STATE.md`](STATE.md);
- externe/Sitzungs-Übergabe in [`addon.md`](addon.md) mit groß-/kleinschreibungssicherem Einstieg [`ADDON.md`](ADDON.md);
- detaillierter Baumann-/Methernitha-Sprachdecoder;
- verbindliche Maschinentaxonomie und Provenienzschema;
- deterministische Manifest-/Hash-Erzeugung und Repository-Validierung.

<!-- README-SYNC:quick-access -->
## Schnellzugriff

| Inhalt | Pfad |
|---|---|
| Replikationsvollständigkeit | [`docs/REPLICATION_STATUS.md`](docs/REPLICATION_STATUS.md) |
| **Aktuelle V4-Baudefinition** | [`docs/research/v4-best-evidence-m2.md`](docs/research/v4-best-evidence-m2.md) |
| **V4-BOM** | [`docs/research/v4-bom.md`](docs/research/v4-bom.md) |
| **V4-Montage** | [`docs/research/v4-assembly.md`](docs/research/v4-assembly.md) |
| **V4-elektrische Evidenzgrenze** | [`docs/research/v4-electrical-boundary.md`](docs/research/v4-electrical-boundary.md) |
| **V4-Druckhinweise** | [`docs/research/v4-printing.md`](docs/research/v4-printing.md) |
| Generiertes V4-CAD | `hardware/experimental/v4-best-evidence-m2/` |
| V4-Bau-ZIP | `release/experimental/testatika-m2-v4-best-evidence-build-package.zip` |
| Vollständige V2-STEP | `hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V2_COMPLETE.step` |
| Vollständige V2-STL | `hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V2_COMPLETE.stl` |
| Vollständige V2-GLB | `hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V2_COMPLETE.glb` |
| Experimentelle V3-STEP | `hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V3_COMPLETE.step` |
| Experimentelle V3-STL | `hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V3_COMPLETE.stl` |
| Ältere druckbare Teile | [`hardware/stl/`](hardware/stl/) |
| Ältere editierbare Teile | [`hardware/step/`](hardware/step/) |
| CAD-Reproduzierbarkeit | [`docs/research/cad-reproducibility.md`](docs/research/cad-reproducibility.md) |
| Ältere V2-BOM | [`docs/research/bom.md`](docs/research/bom.md) |
| Ältere V2-Montage | [`docs/research/assembly.md`](docs/research/assembly.md) |
| Sicherheit | [`docs/research/safety.md`](docs/research/safety.md) |
| Evidenzmatrix | [`docs/research/evidence_matrix.tsv`](docs/research/evidence_matrix.tsv) |
| Maschinentaxonomie | [`docs/research/machines.yaml`](docs/research/machines.yaml) |
| Provenienzschema | [`docs/research/provenance-schema.yaml`](docs/research/provenance-schema.yaml) |
| Vollständiger Video-Audit | [`docs/research/video-frame-audit-2026-08-16.md`](docs/research/video-frame-audit-2026-08-16.md) |
| Marinov-/Hauser-Scan-Audit | [`docs/research/hauser-marinov-primary-scan-audit-2026-08-16.md`](docs/research/hauser-marinov-primary-scan-audit-2026-08-16.md) |
| Grenze des externen Korpus | [`docs/research/external-corpus.md`](docs/research/external-corpus.md) |
| Vollständiger Forschungsstand | [`STATE.md`](STATE.md) |
| Externe Übergabe | [`addon.md`](addon.md) |
| Baumann-Sprachdecoder | [`docs/research/baumann-language-decoding.md`](docs/research/baumann-language-decoding.md) |
| Baumann-Aussagenregister | [`docs/research/baumann-statements.tsv`](docs/research/baumann-statements.tsv) |
| Hartmann-/Overunity-Audit | [`docs/research/hartmann-overunity-testatika.md`](docs/research/hartmann-overunity-testatika.md) |
| Aktueller Versuchsplan | [`docs/research/experiment-plan.md`](docs/research/experiment-plan.md) |

<!-- README-SYNC:source-correction -->
## Quellenkorrektur: Baumanns Erklärungssprache

Der vollständige Archivscan-Audit verbessert die frühere Formulierung wesentlich.

Ein direkter Marinov-Korrespondenzscan sagt, Baumann habe beim Versuch, das Prinzip zu erklären, **`ANOTHER language`** benutzt. Damit ist der grundsätzliche Punkt einer Sprach-/Begriffsdifferenz primärquellenbelegt.

**Noch nicht verifiziert** ist dagegen die populäre spätere Formulierung, Baumanns Erklärung sei wörtlich *„like an unknown language“* gewesen. Diese spätere Paraphrase darf nicht als exaktes Marinov-Zitat dargestellt werden.

Getrennt davon gilt:

1. Marinov verstand das vollständige Funktionsgeheimnis bzw. den exakten Schaltplan nicht.
2. Hans Holzherr berichtete, Baumann sei schwer zu verstehen gewesen, weil er leise/schnell sprach und nichtwissenschaftliche Begriffe verwendete.
3. Methernithas eigene technische Beschreibung verwendete Spezialbegriffe wie `Taster` / `antenna keys`.

Siehe [`docs/research/baumann-language-decoding.md`](docs/research/baumann-language-decoding.md) und den Primärscan-Audit.

<!-- README-SYNC:operating-model -->
## Aktuelle Arbeitshypothese zum Funktionsmodell

Nach getrennter Provenienzanalyse der Aussagen von Baumann, Methernitha, Marinov, Holzherr, Luzi Cathomen, Albert Hauser und Stefan Hartmann ist das derzeit stärkste **testbare** Modell:

> **elektrostatische Influenz / variable Kapazität → berührungsfreie Abnahme → polaritätsselektive Ladungsführung → Kristall-/Dioden-Phasenkommutation → Antriebs-/Speicherbusse → zyklische Bias-Regeneration → modellabhängige nachgeschaltete Impedanzanpassung.**

Damit lässt sich ein erheblicher Teil der historischen Begriffswelt erklären, ohne einen Tesla/HF-Kern oder Permanentmagnete als Energiequelle anzunehmen. Ein Nettoenergieüberschuss wird dadurch **nicht** erklärt oder bestätigt.

<!-- README-SYNC:reference-geometry -->
## Referenzgeometrie

Der stärkste Maßstabsanker ist Marinovs Angabe, dass die Scheibe der kleinen Maschine ungefähr **20 cm** Durchmesser hatte. Weitere Maße sind photogrammetrische/videoangepasste Arbeitswerte.

| Merkmal | Arbeitswert |
|---|---:|
| Rotordurchmesser | 200 mm |
| Basisbreite | ~370 mm |
| Basistiefe | ~180 mm |
| Außendurchmesser Seitentopf | ~84 mm |
| Höhe Seitentopf-Körper | ~110 mm |
| Rotorzentrum über Basis | ~160 mm |
| Hüllmaß der Gesamtbaugruppe | ~370 × 182 × 324 mm |

Foto-/videoabgeleitete Maße sind als Näherungen zu behandeln, solange keine kalibrierte Primäransicht oder Originalobjektmessung verfügbar ist.

<!-- README-SYNC:versions -->
## Verhältnis V2 / V3 / V4

- **V2:** konservative mechanische Basislinie und erhaltene Release-Bibliothek.
- **V3:** Fotointerpretation plus getrennte videoabgeleitete Verfeinerungen.
- **V4:** aktuelle Best-Evidence-Familie für einen physischen Nachbau; verbindet die stärkeren Primärscan-Elektrobedingungen mit der derzeit besten sichtbaren Geometrie.

Ältere Versionen werden nicht gelöscht; sie bleiben Provenienz- und Vergleichsstände.

<!-- README-SYNC:evidence-choices -->
## Evidenzgeleitete Entscheidungen

### Stark gestützt

- eine rotierende Scheibe beim kleinen Modell;
- radiale leitfähige Sektoren aus ungefähr 1-mm-Draht;
- etwa 20–25 Sektoren als engerer späterer Bereich;
- Direktquellenaussage, dass die beschriebenen Drähte der kleinen Scheibe **`connected to nothing`** sind;
- keine schleifenden Kollektorbürsten;
- Bedeutung der Drahtführung durch die Scheibe;
- seitliche Töpfe mit Gitter/Dielektrikum/Kupferspirale;
- zwei sichtbare Leitungen zu jedem Kondensator;
- ein von Baumann **`crystal`** genanntes Bauteil;
- laut Marinov keine Tesla-Spulen-/AC-Interpretation für die beschriebene kleine Maschine;
- Hufeisenmagnete in der ersten Kleinmaschinenlinie, aber nicht universell für jede kleine Variante.

### Bewusst nicht angenommen

- 1-kΩ-Nachbarring als M2-Basislinie;
- Tesla-Spulen als Kernmechanismus;
- 50/60-Hz-Netzfrequenzdesign als Grundprinzip;
- versteckte 230-V-AC-Stufe;
- Permanentmagnete als Nettoenergiequelle;
- verifizierte 100-W-/1-kW-/mehrere-kW-Overunity-Leistung;
- vollständig bekannter Originalschaltplan;
- schwarze Optik als Beweis für Kohlenstoff/Graphit/Nanobeschichtung/schwarzes Kupferoxid;
- R4 als definitiv originale M2-Drahtführung;
- Hausers große 3-Gitter-/Magnet-/Bifilarzylinder als M2-Töpfe.

<!-- README-SYNC:rotor-routing -->
## Forschung zur Rotor-Drahtführung

Die genaue Drahtgeometrie durch die Scheibe bleibt eines der wichtigsten ungelösten Details:

- **R0** — einseitige radiale Referenz und nominale V4-Bauführung;
- **R1** — vorderer radialer Verlauf, durch äußeres Loch, Rückweg hinten;
- **R2** — alternierende Vorder-/Rückseitensektoren;
- **R3** — winkelversetzte Durch-Scheiben-Führung;
- **R4** — Dreifach-Seitenwechsel-Geflecht aus Holzherrs Bericht für mehrere Maschinen; für Marinov M2 noch nicht spezifisch verifiziert.

Die elektrische Topologie ist eine eigene Variable: V4 hält die einzelnen Sektoren auch beim R4-Forschungsrotor potentialfrei.

Siehe [`docs/research/rotor-wire-routing.md`](docs/research/rotor-wire-routing.md).

<!-- README-SYNC:scientific-status -->
## Wissenschaftlicher Status

Konventionelle und reproduzierbare Effekte, die für dieses Projekt relevant sind, umfassen elektrostatische Influenz, variable Kapazität, berührungsfreie kapazitive Kopplung, elektrostatisches Motordrehmoment, Kondensatorspeicherung, Corona-/Ionentransport und nichtlineares Ladungs-Gating.

**Nicht** belegt ist, dass die historische Testatika mehr Energie erzeugte als sämtliche Eingänge plus anfänglich gespeicherte Energie. Energieerhaltung ist die Nullhypothese dieses Repositories.

Siehe [`docs/scientific-status.md`](docs/scientific-status.md).

<!-- README-SYNC:safety -->
## Sicherheit

Elektrostatische Hochspannungssysteme können insbesondere mit Kondensatoren gefährlich sein. Dieses Projekt enthält **keinen** offenen netzbetriebenen Hochspannungsversorgungsentwurf.

Verwende gekapselte, strombegrenzte Lehr-/Labor-Elektrostatikgeräte, halte gespeicherte Energie klein, entlade Kondensatoren vor Berührung und verwende einen Rotorschutz. Ein Nachbaupfad mit radioaktivem Material ist nicht Bestandteil dieses Projekts.

Lies [`docs/research/safety.md`](docs/research/safety.md).

<!-- README-SYNC:layout -->
## Repository-Struktur

```text
.
├── STATE.md
├── addon.md / ADDON.md
├── cad/
├── hardware/
│   ├── stl/
│   ├── step/
│   ├── experimental/
│   │   └── v4-best-evidence-m2/
│   └── complete-model/
├── docs/
│   ├── REPLICATION_STATUS.md
│   ├── research/
│   └── images/
├── scripts/
├── .github/
└── release/
    └── experimental/
```

<!-- README-SYNC:validate -->
## Lokal validieren

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_assets.py
python scripts/check_readme_sync.py
python scripts/check_manifest.py
```

Nach beabsichtigten Inhaltsänderungen die Integritätsmetadaten neu erzeugen:

```bash
python scripts/generate_manifest.py
python scripts/check_manifest.py
```

<!-- README-SYNC:cad-regeneration -->
## CAD neu erzeugen

CAD-Umgebung installieren:

```bash
python -m pip install -r requirements-cad.txt
```

Alle derzeit aus Quellen reproduzierbaren CAD-Familien neu bauen:

```bash
python scripts/rebuild_research_assets.py
```

Oder einzelne Generatoren ausführen:

```bash
python cad/generate_v2.py
python cad/generate_v3_experiments.py
python cad/generate_v3_photo_interp.py
python cad/generate_v3_video_refinements.py
python cad/generate_v4_best_evidence_m2.py
```

Wichtig: `generate_v2.py` erzeugt die **Kerngeometrie** von V2 neu, nicht jedes erhaltene V2-Release-Asset. V4 besitzt eine eigene deklarierte, quelleneigene Teile- und Baugruppenfamilie. Siehe [`docs/research/cad-reproducibility.md`](docs/research/cad-reproducibility.md).

<!-- README-SYNC:build-packages -->
## Baupakete

Das Preservation-/Research-Release bleibt **v0.3.0**. Zusätzlich wird das aktuelle physische Baupaket deterministisch erzeugt mit:

```bash
python cad/generate_v4_best_evidence_m2.py
python scripts/build_v4_package.py
```

Ergebnis:

- `release/experimental/testatika-m2-v4-best-evidence-build-package.zip`;
- passende `.sha256`-Datei.

Das Paket enthält den V4-Generator, STEP/STL-Assets, vollständige Baugruppen, BOM, Montageanleitung, Druckhinweise, elektrische Evidenzgrenze, Sicherheit sowie den Primärquellen-/Video-Audit-Kontext, der für die korrekte Interpretation des Modells nötig ist.

<!-- README-SYNC:sources -->
## Quellen und externer Korpus

Die wichtigste veröffentlichte Quelle für diese kleine Maschine ist Stefan Marinov, *The Thorny Way of Truth, Part V* (1989), ergänzt durch direkte Marinov-/Hauser-Korrespondenzscans und historische Medien, die in diesem Projekt auditiert wurden.

Vollständige fremde Scans/Videos werden bewusst nicht weiterverteilt. Die Projektgeschichte verweist außerdem auf einen extern gehaltenen Korpus namens `testatika.zip`; er ist **nicht Teil des öffentlichen Repositories**. Hashes/Locatoren und abgeleitete Forschungsergebnisse werden dokumentiert, ohne fremde Medien stillschweigend neu zu veröffentlichen.

Siehe [`docs/research/external-corpus.md`](docs/research/external-corpus.md), [`docs/sources.md`](docs/sources.md), [`docs/research/source-basis.md`](docs/research/source-basis.md), den Primärscan-Audit und den Video-Frame-Audit.

<!-- README-SYNC:contributing -->
## Mitwirken

Besonders wertvoll sind höher aufgelöste Primärfotos, unabhängig gewonnene Maße, Originalkorrespondenz mit Provenienz, kontrollierte elektrostatische Messungen und Falsifikationstests für Drahtführungs-/Elektroden-/Ladungskommutationshypothesen.

Bitte [`CONTRIBUTING.md`](CONTRIBUTING.md) lesen.

**Sprachregel:** `README.md` (Deutsch) und `README.en.md` (Englisch) sind gleichwertige, vollständig synchron zu haltende Fassungen. Inhaltliche README-Änderungen müssen immer in beiden Sprachen erfolgen; `python scripts/check_readme_sync.py` prüft die strukturelle Parität.

<!-- README-SYNC:license -->
## Lizenz

Vom Repository selbst erstellter Code, CAD-Quelltext, Dokumentation und abgeleitete Modelle stehen, sofern nicht ausdrücklich anders angegeben, unter der [MIT-Lizenz](LICENSE). Historische Publikationen, Scans und Fotos Dritter unterliegen weiterhin ihren jeweiligen Rechten.
