# V4 Reproduzierbarkeitsnachweis

## Problem

OpenCascade/CadQuery schreibt beim STEP-Export standardmäßig die aktuelle Uhrzeit in den `FILE_NAME`-Header. Dadurch waren zwei geometrisch identische STEP-Neubauten byteweise verschieden.

## Lösung

`scripts/normalize_v4_step.py` ersetzt ausschließlich den volatilen STEP-Header-Zeitstempel durch:

`2000-01-01T00:00:00`

Der DATA-Abschnitt und damit die CAD-Geometrie werden nicht verändert.

Die Materialisierung führt deshalb in dieser Reihenfolge aus:

1. V4 CAD generieren;
2. STEP-Header normalisieren;
3. `scripts/check_v4_assets.py` ausführen;
4. deterministisches ZIP erzeugen;
5. ZIP-SHA-256 prüfen;
6. Repository-Manifest regenerieren/prüfen.

## Isolierter Wiederholungsnachweis

Nach einer vollständigen normalisierten Materialisierung wurde ein dedizierter Triggerlauf über `.github/V4_MATERIALIZE_TRIGGER` gestartet. Der allgemeine Manifest-Workflow ignoriert genau diese Triggerdatei, damit der V4-Lauf nicht durch einen konkurrierenden Writer verdrängt wird.

Ergebnis des Materialisierungscommits `668fc6439042548371707c32759886a4945fa11b`:

- keine STEP-Datei geändert;
- keine STL-Datei geändert;
- kein V4-Metadatenfile geändert;
- das V4-ZIP nicht geändert;
- `STATE.md` / `addon.md` nicht geändert;
- nur `MANIFEST.json` und `MANIFEST_SHA256.txt` geändert, weil die neue Triggerdatei erstmals in den Manifestbestand aufgenommen wurde.

Damit ist nachgewiesen, dass der materialisierte V4-Inhalt bei identischem Quellstand byte-stabil wiedererzeugt wird.

## Aktueller Build-Paket-Hash

Siehe stets die committed Datei:

`release/experimental/testatika-m2-v4-best-evidence-build-package.zip.sha256`

Der Hash gehört zum vollständigen V4-Paket einschließlich CAD-Ausgaben und kanonischer Bau-/Versuchsdokumentation.
