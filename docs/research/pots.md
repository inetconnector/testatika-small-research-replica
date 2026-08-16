# Seitliche „Pots“ — M2/M3 Kleinmaschinen

## Primärquellenstand

Die kleinen Seitenmodule werden in Stefan Marinovs direkter Korrespondenz als **Kondensatoren** beschrieben. Der Archivscan `hauser/SMwebL1.jpg` ist hierfür inzwischen eine Primärquelle und wird in [`hauser-marinov-primary-scan-audit-2026-08-16.md`](hauser-marinov-primary-scan-audit-2026-08-16.md) mit Hash dokumentiert.

Marinovs Beschreibung ergibt für die kleine Maschine:

- äußere zylindrische leitfähige **Gitterelektrode**;
- zylindrische Kunststoffisolation;
- zentrale **Kupferspirale** als zweite Elektrode;
- im referenzierten Foto seien **zwei Leitungen zu jedem Kondensator** sichtbar.

Marinov widerspricht dabei ausdrücklich einer Tesla-/AC-Deutung: Die Spirale sei eine Elektrode des Kondensators, keine Tesla-Sekundärspule.

## Konsequenz für die historische Baseline

Der externe historische Modus jedes M2-Forschungspots besitzt **zwei funktionale Anschlussleitungen**.

Die Primärquelle legt damit die äußere Schnittstelle stärker fest als bisher, aber weiterhin nicht:

- welche der beiden Leitungen an Gitter bzw. Spirale liegt;
- Polarität;
- ob ein Anschluss zeitweise floating ist;
- exakte Windungszahl/Pitch der Spirale;
- exakte Kapazität;
- Dielektrikumstärke;
- interne Zusatzschichten.

Deshalb bleiben diese Eigenschaften experimentell reversibel.

## V2/V3-Aufbau

V2 trennt weiterhin:

1. `pot_outer_shell` — mechanische Hülle;
2. `pot_grid_former` — Träger für echte Metallgaze;
3. `pot_acrylic_sleeve_jig` — Maßkörper; für elektrische Versuche durch echtes Acryl-/PMMA-Rohr ersetzen;
4. `pot_spiral_mandrel` — Wickelkörper für dickeren Kupferdraht;
5. `pot_terminal_lid`.

Für die Forschung darf unter einem abnehmbaren Deckel zusätzliche Messzugänglichkeit vorhanden sein, aber im historischen Testmodus gilt:

- nur zwei externe Pot-Leitungen aktiv;
- zusätzliche Guard-/Messleitungen vollständig isoliert oder entfernt;
- jede interne Topologie bekommt eine eigene Configuration-ID;
- vor dem Versuch werden C, Leakage und Verlustfaktor gemessen.

## Was `meth4.asf` ergänzt

Das vollständig ausgewertete historische Kleinmaschinenvideo zeigt die Seitenzylinder aus mehreren Nahwinkeln. Sichtbar sind:

- dichte horizontale/gitterartige Leiterstruktur;
- ausgeprägte metallische obere und untere Ringe;
- ein dunkler konischer/isolierender Terminalbereich oben;
- benachbarte perforierte Bauteile, die mechanisch vom eigentlichen Zylinder getrennt erscheinen.

Die Videoauflösung reicht **nicht**, um sicher zu entscheiden, ob einzelne sichtbare Linien dem äußeren Gitter oder der durch transparente Isolation sichtbaren inneren Spirale zuzuordnen sind. Daher wird aus dem Video keine zusätzliche interne Verdrahtung erfunden.

Siehe [`video-frame-audit-2026-08-16.md`](video-frame-audit-2026-08-16.md).

## Strikte Abgrenzung zu Hausers großen Zylindern

Albert Hausers 1986/1988-Unterlagen beschreiben bei einer ~500-mm-Groß-/Mittelmaschine eine deutlich komplexere Zylinderbaugruppe:

- drei konzentrische Metallgitterrohre;
- Acryl-/Kunststoffrohre als Trennung;
- zentrale Magnetröhre;
- zweilagige/bifilare Kupferwicklung;
- zusätzliche Isolationslagen.

Diese Konstruktion gehört zur großen/medium Familie (`M6a`) und darf **nicht** rückwirkend zum M2-Pot erklärt werden.

Genauso gilt Holzherrs Aussage über **20 perforierte Lagen** für große Kondensatoren, nicht automatisch für die kleinen M2-Seitenmodule.

## Forschungsregel

Die Kleinmaschinen-Baseline lautet daher bis zu gegenteiliger Primärevidenz:

> **zweipoliger, zylindrischer elektrostatischer Kondensator: äußeres Gitter — Dielektrikum — zentrale Kupferspirale.**

Die Kupferspirale wird **nicht** als Tesla-Sekundärspule behandelt. Großmaschinen-Zylinder, Mehrlagenkondensatoren und Coil/Magnet-Tube-Strukturen werden ausschließlich als getrennte Vergleichsvarianten geführt.
