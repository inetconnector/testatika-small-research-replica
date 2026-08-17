# Fertigungs-Bausätze: M2 V5 und M6 V2

Dieses Repository trennt ab jetzt strikt zwischen **anschaulicher Referenz-CAD** und **realen Fertigungs-Bausätzen**.

## Grundregel

Eine STL-Datei im Ordner `print/` darf nur ein Bauteil darstellen, dessen technische Funktion tatsächlich mit einem geeigneten 3D-Druckwerkstoff erfüllt werden kann: Halter, Clip, Abstandshalter, Wickeldorn, Montagelehre, Modulträger oder Schutzteil. Primär tragende Lagerböcke gehören bei den aktuellen Kits ausdrücklich **nicht** dazu.

Folgende Funktionsklassen werden **nicht** als Kunststoffersatz ausgegeben:

- elektrische Leiter und Elektroden;
- Kupferwicklungen;
- Metallgitter;
- Rotorlamellen;
- Magnete oder magnetische Kerne;
- Wellen und Präzisionslager;
- PMMA-Rotorscheiben;
- unbekannte historische Kondensator- oder `Crystal`-Interna.

Dafür gibt es `fabricate/`-STEP-Dateien, Material-/Schnittlisten und reale Kaufteile. Die zusammengebauten STL-Dateien liegen ausschließlich unter `assembly-reference/` und tragen `REFERENCE_NOT_FOR_PRINT` im Namen.

## M2 V5

Primärer Pfad: `hardware/build-kits/m2-v5/`

- `print/`: Ausrichtlehre, Pot-Träger, Mesh-Clips, Wickeldorn, Statorclips, Magnethalter, Crystal-Modulträger, Tower-/Modulhalter und Schutzrahmen-Ecken;
- `fabricate/`: echte PMMA-Rotorscheibe, strukturelle Basis/Rückplatte, 8-mm-Metallwelle, **reale Metall/G10-Lagerträger und Hubflansche**, leitfähige Stator-/Pickup-Einsätze, Hub-Bogen-/Crossbar-Kandidaten, PMMA-Pot-Isolator, Metallgitter-Hülle und Kupferspiralpfad;
- `metadata/`: maschinenlesbare Fertigungsklassifikation, Kaufteilliste und Schnittliste;
- `assembly-reference/`: Zusammenbau zur Kollisions-/Passungsprüfung, ausdrücklich kein Druckauftrag.

Der Bausatz übernimmt die M2-V4-Evidenzgrenzen: ca. 200-mm-Scheibe, nominell 24 elektrisch getrennte Cu-Sektoren, zwei externe Anschlüsse pro Pot und offene/reversible unbekannte elektrische Funktionen.

## M6 V2

Primärer Pfad: `hardware/build-kits/m6-v2/`

- `print/`: Lamellen-Abstandslehre, verstellbare Statorhalter, Gitter-Zentrierringe/-spider, Kondensatorhalter **ohne Fake-Kondensator**, Hufeisenhalter, Topmodulträger, 18-Knoten-Terminalboard, Motorhalter und Schutzecken;
- `fabricate/`: zwei echte Ø500×5-mm-PMMA-Scheiben mit **getrennten 25-mm-/12-mm-Hubbohrungen**, ~0,2×20×160-mm-Metalllamelle, leitfähige Statorplatte, 12-mm-Innenwelle, 25/16-mm-Hohlwelle, **vier reale Metall/G10-Lagerträger und Retainer**, Metallhubs, Metallgitter-Hüllen, PMMA-Isolierhülsen, Zentralrohr und bifilarer Kupferwickelpfad;
- `metadata/`: Kaufteilliste, Schnittliste, Materialklassen und Evidenzgrenze;
- `assembly-reference/`: mechanische Passungs-/Schutzansicht. Riemen werden nicht als starre Pseudostäbe modelliert.

Die M6-V2-Mechanik ist eine stabile, abgeleitete Laborumsetzung der M6a/Hauser-Geometrie. Die 500-mm-/50-Lamellen-Anker und die 8-vorn/6-hinten-Statoren bleiben erhalten. Die exakte historische Wellen-, Motor- und Elektro-Topologie ist nicht vollständig bekannt und wird daher nicht als Original behauptet.

## Was „funktionierend“ hier bedeutet

Die Bausätze sind so ausgelegt, dass die **Mechanik real aufgebaut, ausgerichtet, gedreht, geschützt, instrumentiert und mit realen Materialien bestückt** werden kann. Unbekannte elektrische Baugruppen werden als austauschbare Module oder offene Messknoten ausgeführt.

Nicht seriös garantierbar ist eine historische Selbstlauf-/Overunity-Funktion, solange die ursprüngliche vollständige Schaltung und belastbare geschlossene Energiebilanzen fehlen. Diese Unsicherheit wird im CAD nicht durch erfundene Bauteile verdeckt.

## Referenzmodelle

Die bisherigen all-solid/all-plastic-orientierten Komplettmodelle werden nicht gelöscht. Für die wichtigsten Komplettansichten werden **zusätzliche klar umbenannte Kopien** unter `reference-visual-only/` mit `REFERENCE_VISUAL_ONLY` bzw. `LEGACY_REFERENCE_ONLY` erzeugt. Die alten Pfade bleiben nur als Kompatibilitätsalias erhalten, damit historische Links nicht brechen. Beides ist ausdrücklich keine Fertigungsanweisung.
