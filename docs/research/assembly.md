# Montage — Marinov First Machine V2

> **Historischer V2-Montagepfad.** Für einen neuen Nachbau ist jetzt der quellenkritisch engere V4-Pfad maßgeblich: [`v4-assembly.md`](v4-assembly.md). V2 bleibt vollständig erhalten, damit frühere Geometrie-/Versuchsstände reproduzierbar bleiben.

## A. Basis
1. `base_left` und `base_right` verbinden.
2. Gesamtarbeitsmaß: etwa 370 × 180 mm.
3. Zwei `side_frame_column` symmetrisch montieren.
4. `top_bridge` oben und `center_crossbar` mittig verschrauben.

## B. Rotor
1. Zwei 608-2RS-Lager in `bearing_tower`.
2. 8-mm-Welle einsetzen.
3. `hub_front` + gewählten Rotor + `hub_rear`.
4. Nominal: `rotor_24wire`.
5. Kupferdraht nach einer dokumentierten R0–R3-Variante montieren.

**Quellenkorrektur seit V4:** Direkte Marinov-Korrespondenz stützt elektrisch voneinander getrennte/floating Sektordrähte. Für einen aktuellen M2-Bau keine Nachbar-Ringverbindung verwenden.

## C. Elektroden
1. Metallgaze in `electrode_wedge_frame`.
2. Rahmen an `electrode_tilt_head`.
3. Kopf auf `electrode_swivel`.
4. Sechs Module zunächst mit großem Abstand zur Scheibe montieren.
5. Kein Kontakt zur Scheibe.

## D. Seitliche Pots
Je Seite:
- Pot-Hülle;
- äußeres leitfähiges Gitter auf Former;
- echtes Acrylrohr/Dielektrikum;
- innere Kupferspirale;
- Deckel/Messanschluss.

**Quellenkorrektur seit V4:** Zwei sichtbare Leitungen pro Kondensator sind direkt belegt; siehe `v4-bom.md` und `v4-electrical-boundary.md`.

## E. Magnete
Zwei `horseshoe_magnet_mount` unterhalb/seitlich des Rotorzentrums montieren.
Die Fotogeometrie zeigt die Baugruppe im unteren Zentralbereich.

## F. Crystal
`crystal_bridge` am oberen Rahmen; `crystal_insert_carrier` bleibt austauschbar.
Kein bestimmtes Crystal-/Diodenmaterial wird als Original behauptet.

## G. Sicherheit
Vor elektrischen Versuchen Schutzhaube über `guard_post`.
Zuerst nur mechanische Auslaufmessung und C(θ)-Messungen durchführen.
