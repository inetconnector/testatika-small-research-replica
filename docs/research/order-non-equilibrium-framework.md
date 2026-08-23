# Energie durch Ordnung — Nichtgleichgewichts- und Gleichrichterrahmen

**Datum:** 23. August 2026  
**Status:** **HYPOTHESIS FRAMEWORK / FALSIFICATION PLAN — keine bestätigte Energiequelle, keine behauptete Originalschaltung**  
**Geltungsbereich:** Testatika-Familie M0–M10/MX; maschinenspezifische Übertragung nur gemäß `machines.yaml`  
**Kontrollierende Vorarbeit:** `continuous-power-and-information-thermodynamics-audit-2026-08-23.md` und `methernitha-physics-operating-model-corrigendum-2026-08-23.md`  

---

## 1. Ziel

`Meth_5` verbindet Energiegewinn mit „organization“ bzw. dem Aufbau „inner order“. `Meth_6` spricht über Osmose, Membranen, schwache DC-Felder und Energie, welche die Natur bereitstelle.

Diese Sprache wird hier **nicht** als Beweis einer neuen Energiequelle behandelt. Sie wird in eine experimentell prüfbare Forschungsfrage übersetzt:

> **Welcher reale Nichtgleichgewichtsgradient, Speicherzustand oder externe Energiefluss wird durch die Testatika-Struktur selektiert, geordnet, gekoppelt oder gleichgerichtet?**

Arbeitsdefinition:

> **„Ordnung“ = selektive Kopplung, Ladungssortierung, Gleichrichtung, Phasensteuerung, Korrelation oder kontrollierte Relaxation eines Nichtgleichgewichtszustands.**

Ordnung kann die Nutzbarkeit vorhandener freier Energie verändern. Sie ist ohne separaten Ressourcenterm **keine Bulk-Energiequelle**.

---

## 2. Thermodynamische Grenze

Für ein System bei Temperatur `T` gilt

`F = U - T*S`.

Bei gleichem `U` und `T` erhöht geringere Entropie `S` die Helmholtz-Freie-Energie. Ein präparierter Nichtgleichgewichtszustand kann deshalb Arbeit liefern, wenn er relaxiert.

In der Informationsthermodynamik können Messinformation und Korrelationen ebenfalls einen Arbeitswert besitzen. Der vollständige Zyklus muss aber immer die Präparation, den Reset bzw. die Replenishment-Kosten und die Entropieproduktion enthalten.

Daher ist folgende Schlusskette unzulässig:

`Ordnung -> Energie aus dem Nichts`.

Zulässig ist:

`reale Ressource / gespeicherte freie Energie / Nichtgleichgewichtsgradient`

`-> Ordnung / Selektion / Gleichrichtung`

`-> gerichteter Energiefluss`

`-> Speicher / Last`.

Ein passiver Gleichrichter, eine Ratchet-Struktur oder geometrische Asymmetrie kann ein einzelnes thermisches Gleichgewicht nicht zyklisch in Nettoarbeit umwandeln.

---

## 3. Historische Evidenzgrenze

Der neue Rahmen muss zwei gegenläufige Fehler vermeiden.

### 3.1 Nicht alles auf einen kurzen Lampenpuls reduzieren

Der aktuelle Dauerleistungs-Audit hält reale historische **Claims** fest, die deutlich länger reichen als die Holzherr-Lampendemonstration:

- der 17.-März-1984-Bericht `L. L., Rorschach` behauptet tägliche Einspeisung in ein Betriebsnetz über Inverter und Akkumulator;
- Nieper 1985 behauptet Betrieb seit 1982 und Gewächshausheizung;
- der 2.-Juli-1988-Bericht im späteren DOE-Paket behauptet zehn Konverter plus Windmühlen für 180 Personen und Betriebe.

Diese Aussagen sind historisch relevant und dürfen nicht als „nur 10 Sekunden Last“ weggekürzt werden.

### 3.2 Claims sind keine geschlossene Energiebilanz

Gleichzeitig sind die genannten Versorgungsaussagen **nicht source-isoliert**:

- 1984 werden Akkumulator und Windkonverter ausdrücklich genannt;
- 1988 werden Windmühlen ausdrücklich genannt;
- kontinuierliche unabhängige `∫u(t)i(t)dt`-Protokolle fehlen;
- das DOE hat die Maschine nicht validiert; seine Antwort von 1989 bezeichnet die Unterlagen als unzureichend für eine technische Beurteilung.

Damit bleibt die historische Bulk-Energiequelle `UNKNOWN`.

---

## 4. Baumann-/Methernitha-Sprache konservativ übersetzen

Die bestehende kanonische Übersetzung aus `baumann-language-decoding.md` und `baumann-statements.tsv` bleibt maßgeblich:

| Quellenbegriff | zulässige Arbeitsübersetzung | nicht zulässige Hochstufung |
|---|---|---|
| „Ladungen ordnen“ | polarity sorting / charge routing / asymmetrische Übertragung | „Ordnung erzeugt Energie“ |
| `rectifying diode` hält Zyklus im Takt | phasenselektives Ladungsventil / elektrostatischer Kommutator | Diode als Energiequelle |
| Wolke / Erde | Potential-/Feldreservoirs bzw. Polaritätsräume | automatische atmosphärische kW-Quelle |
| Gitter halten Ladung | field-forming/floating electrode; mögliche Raumladungssteuerung | bewiesener Corona-Energiegewinn |
| `crystal` | unbekannter Funktionsblock / mögliche Nichtlinearität | automatisch identisch mit institutioneller Diode |
| Osmose / Membran / schwaches DC-Feld | Hinweis auf Gradienten- oder Grenzflächenprozesse | nachgewiesene Maxwell-Wagner-Energiequelle |

---

## 5. Offenes Funktionsschema

```text
[UNKNOWN: Quelle / gespeicherte freie Energie / Nichtgleichgewichtsressource]
                                |
                                v
[Gradient / Bias / Speicherzustand / externer Energiefluss]
                                |
                                v
[Ordnung: C(theta) + Gitter + crystal/Diode + Phasensteuerung]
                                |
                                v
[gerichteter Ladungs-/Energiefluss]
                                |
                                v
[Speicher / Impedanzwandlung / DC-Bus]
                                |
                                v
[Last]
```

Die zentrale Trennung lautet:

1. **Kann die sichtbare Struktur Ladung/Feld phasenabhängig ordnen oder routen?**
2. **Welche reale Ressource speist den dadurch gerichteten Energiefluss?**

Eine positive Antwort auf 1 beantwortet 2 nicht automatisch.

---

## 6. Variable Kapazität und `crystal`/Diode

Ein Rotorsektor und eine stationäre Elektrode bilden eine winkelabhängige Kapazität `C(theta)`.

`Q = C*V`

und

`E_C = 1/2*C*V^2`.

Bei einem konventionellen elektrostatischen Generator stammt zusätzliche elektrische Energie aus der mechanischen Arbeit, die beim Ändern der Kapazität gegen elektrostatische Kräfte verrichtet wird, sofern kein anderer Ressourcenterm einspeist.

Eine Diode oder ein anderer nichtlinearer Schalter kann plausibel:

- Rückstrom blockieren;
- Ladung nur in ausgewählten Rotorphasen übertragen;
- floating Knoten zeitweise klemmen;
- Peak-Holding bzw. Charge-Pumping ermöglichen;
- Lastreaktion und Drehmomentphase verändern;
- einen Grenzzyklus stabilisieren.

Nicht belegt ist eine konkrete historische Schaltphase oder die Behauptung

`Diode entfernt Gegenmoment -> kostenlose positive Nettoarbeit`.

Zu messen sind deshalb synchron:

- `C(theta)`;
- `V(theta)`;
- `I(theta)`;
- `tau(theta)`;
- `omega(t)`;
- Lastleistung und Speicherzustände.

---

## 7. Gitter und Corona

Gitter können gegenüber geschlossener Folie verändern:

- lokale Feldstärke und Randfelder;
- Feldpenetration;
- Kapazitätsmatrix;
- Oberflächenladungsverteilung;
- Raumladungs- und mögliche Coronawege;
- Leckage und Entladungsdynamik.

Corona ist jedoch gewöhnlich dissipativ. Deshalb wird **nicht** angenommen, sie sei ein „entropiearmer Energiekanal“.

Die testbare Hypothese lautet lediglich:

> **Gittergeometrie strukturiert Feld- und Ladungstransport anders als eine geschlossene Folie.**

Das macht den M0-`mesh vs foil`-Befund zu einem hochwertigen A/B-Test, nicht zu einem Energiequellennachweis.

---

## 8. Pots, Dielektrika und Speicher

### M2

Direkt quellenkompatibel sind:

- zylindrisches leitfähiges Gitter;
- Kunststoffisolation;
- zentrale Kupferspirale;
- zwei sichtbare externe Leitungen je Pot.

Exakte Kapazität, interne Polarität und vollständige Verschaltung bleiben `UNKNOWN`.

V4.31 setzt eine wichtige negative Grenze: Die **einfache sichtbare M2-Pot-Geometrie** kann kein `10 kJ`-Elektrostatikspeicher sein; eine großzügige idealisierte Koaxialabschätzung bleibt um viele Größenordnungen darunter.

Deshalb dürfen `dielectric soakage`, Maxwell-Wagner-Polarisation oder Elektret-Effekte zwar gemessen werden, aber nicht als bereits nachgewiesene 10-kJ-Erklärung für M2 ausgegeben werden.

### M6

Hauser/Holzherr beschreiben deutlich komplexere große Zylinder und Multilayer-Strukturen. Deren Speichergrenzen müssen **separat** aus M6-Geometrie und Messung bestimmt werden. M6-Details dürfen nicht nach M2 übertragen werden.

---

## 9. Kandidaten für die fehlende Ressource

Diese Matrix ist eine Falsifikationsliste, keine Rangliste bestätigter Quellen.

| Ressource | mögliche Kopplung | entscheidender Test | Status |
|---|---|---|---|
| mechanische Arbeit | `C(theta)`, elektrostatisches Drehmoment | `tau*omega` gegen elektrische Leistung integrieren | muss immer bilanziert werden |
| elektrische Vorladung / endlicher Speicher | Kondensatoren, Elektrete, unbekannte Speicher | Droop + Recovery + Vor-/Nachenergie | offen |
| chemische freie Energie | Material-/Grenzflächenreaktionen | Masse, Potential, Chemie, Kapazitätsverbrauch | HYPOTHESIS |
| thermischer Gradient | Kontakte, Gas, Materialien | isotherme Kontrolle + Wärmefluss | HYPOTHESIS |
| Feuchte / Adsorbate / Ionen | PMMA, Luftionen, Oberflächen | RH-/Ionenkonzentrationsmatrix | hohe Testpriorität |
| atmosphärisches E-Feld | Earth/cloud, Erde, Basis, Luftionen | isolierte Erde, Abschirmung, Feld-/Strommessung | Kopplungskandidat |
| externe RF/EM | Leiter, Messkabel, Umgebung | Faraday-/RF-Kontrolle und Spektrum | Kontrollterm |
| Vibration / Luftströmung | Rotor/Mechanik | mechanische Isolation, Luftstrom | Kontrollterm |
| Akkumulator / verborgene konventionelle Quelle | historische Mischversorgung bzw. unerfasste Einspeisung | vollständige Zugangs-/Masse-/Energiegrenze | Ausschlusskontrolle |

### Atmosphärische Größenordnung

Das globale atmosphärische elektrische System ist ein reales Nichtgleichgewichtssystem. Das Schönwetterfeld kann in der Größenordnung `~100 V/m` liegen, der vertikale Leitungsstrom aber nur bei wenigen `pA/m²`.

Daher ist atmosphärische Kopplung als Bias-, Priming- oder Sensitivitätsterm ernst zu nehmen, aber gewöhnlicher Schönwetter-Leitungsstrom erklärt keine direkte kontinuierliche kW-Leistung eines Tischgeräts.

---

## 10. Quanteninformation: Vergleichsrahmen, nicht Testatika-Bauteil

Information, Feedback und Korrelation können in wohldefinierten Nichtgleichgewichtsprotokollen einen Arbeitswert besitzen. Das ist ein sinnvoller theoretischer Vergleich für Baumanns Begriff „Ordnung“.

Es gibt derzeit aber keine Testatika-Evidenz für:

- kontrollierte langlebige Verschränkung;
- kohärente Qubits;
- Quantum Energy Teleportation;
- ein Quantenreservoir als Bulk-Energiequelle.

Daher wird Quanteninformation **nicht** in die historische Maschinenbaseline aufgenommen.

---

## 11. Geschlossene Energiebilanz

Für einen Lasttest ist eine Systemgrenze um das gesamte Gerät zu definieren.

`E_out = ∫u(t)i(t)dt`

und als Arbeitsform

`E_residual = E_out - E_mech,in - E_elec,in - E_thermal,in - E_EM,in - E_environment,in - E_chemical,in + Delta(E_stores)`.

Zu `E_stores` gehören mindestens:

- Kondensator-/Feldenergie;
- Oberflächen-/Elektretladung;
- Rotationsenergie;
- magnetische Energie;
- chemische freie Energie;
- thermische Speicher;
- Akkumulatoren oder andere konventionelle Speicher;
- Mess-/Bias-/Erdpfade.

Die Testdauer darf nicht pauschal auf „eine Stunde“ festgelegt werden. Sie muss aus der gemessenen bzw. konservativ geboundeten maximalen Speicherenergie und der behaupteten Ausgangsleistung abgeleitet werden.

Ein `UNKNOWN_POSITIVE_RESIDUAL` darf erst verwendet werden, wenn:

1. der positive Rest reproduzierbar ist;
2. er deutlich über dem vollständigen Unsicherheitsbudget liegt;
3. bekannte oder konservativ geboundete Speicherdepletion nicht ausreicht;
4. mechanische, chemische, thermische, RF/EM-, Erd-/Atmosphären- und Messgerätepfade quantitativ begrenzt sind;
5. blind/randomisierte Kontrollen den Effekt nicht erklären.

Ein solcher Residual wäre zunächst **eine offene Messanomalie**, keine automatische Erklärung durch ZPE, Vakuumenergie oder Quantenverschränkung.

---

## 12. Experimentprogramm OQ-0 bis OQ-8

Die ausführbare Matrix liegt in [`order-non-equilibrium-test-matrix.tsv`](order-non-equilibrium-test-matrix.tsv).

- **OQ-0:** Nullbilanz / Messkettenvalidierung an konventioneller Kontrolle.
- **OQ-1:** `crystal`/Diode-Phasenmatrix.
- **OQ-2:** Gitter vs. Folie.
- **OQ-3:** Feuchte-/Ionenkonzentrationsmatrix.
- **OQ-4:** Earth/cloud-/Umgebungskopplung.
- **OQ-5:** Speicher-Droop und Recovery.
- **OQ-6:** mechanische Grenzbilanz `tau*omega`.
- **OQ-7:** Material-/Chemiekontrolle.
- **OQ-8:** integrierter Residualtest erst nach den Einzelkontrollen.

---

## 13. Maschinenfamilien strikt getrennt halten

### M2

- floating rotor wires als bevorzugte Baseline;
- zwei externe Pot-Leads;
- keine Tesla/HF-Pot-Baseline;
- `crystal` als Blackbox;
- historische Energiequelle/Speicherzustand `UNKNOWN`.

### M6a / M6b

- große Zylinder und Multilayer-Angaben als eigene Speicher-/Kopplungshypothesen;
- Hauser- und Holzherr-Konfigurationen getrennt halten;
- Lastbeobachtung, Laufdauer und Dauerleistungsclaim getrennt klassifizieren.

### M0 / M0b

- besonders wertvoll für `mesh vs foil` und asymmetrische Transport-/Umweltkopplungsfragen;
- keine automatische Schaltungsvorlage für M2.

---

## 14. Arbeitskonsens

Der Forschungsrahmen lautet:

`Quelle / Speicher / Nichtgleichgewichtsgradient UNKNOWN`

`-> ordnende/gleichrichtende Testatika-Struktur`

`-> messbarer gerichteter Energiefluss`

`-> geschlossene Energie- und Speicherbilanz`.

Der wissenschaftliche Nutzen von Baumanns „Energie durch Ordnung“ besteht damit nicht darin, „Ordnung“ als neue Energieform zu deklarieren, sondern darin, eine präzise experimentelle Frage zu stellen:

> **Welcher reale Ressourcenterm verändert oder erschöpft sich, wenn die ordnende Struktur Arbeit liefert — und wie wird dieser Term wieder aufgebaut?**

---

## 15. Verknüpfte Repository-Dokumente

- `continuous-power-and-information-thermodynamics-audit-2026-08-23.md` — historische Dauerleistungsclaims + Informationsthermodynamik.
- `continuous-power-evidence-2026-08-23.tsv` — Claim-/Evidenzmatrix.
- `continuous-power-info-thermo-provenance-2026-08-23.yaml` — Provenienz und Literaturanker.
- `methernitha-physics-operating-model-corrigendum-2026-08-23.md` — kontrollierende Korrektur des älteren Betriebmodells.
- `m2-v4-31-pot-envelope-reservoir-bound.md` — M2-Pot-Speichergrenzen.
- `baumann-language-decoding.md` und `baumann-statements.tsv` — kanonische Sprach-/Quellenübersetzung.
- `machines.yaml` — verbindliche Maschinenfamilien-Trennung.
