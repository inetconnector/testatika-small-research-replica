# Hufeisenmagnete — Korrektur gegenüber V1

Marinov schreibt ausdrücklich, dass Hufeisenmagnete bei der **ersten kleinen Maschine rechts in Abb. 13/14** sichtbar waren.
Bei der zweiten kleinen Maschine links waren sie dagegen nicht sichtbar.

Daher enthält V2:
- 2× `horseshoe_magnet_mount`
- 1× geometrischen `horseshoe_magnet_dummy` als Größen-/Montageprobe

Der Dummy ist **kein Magnet**. Für magnetische Experimente ist ein realer Hufeisenmagnet erforderlich.

Wichtig: Die Funktion der Magnete war Marinov selbst unklar. Spulen auf diesen kleinen Magneten sind nicht als gesicherte Eigenschaft dokumentiert. `optional_magnet_leg_bobbin` liegt deshalb nur im Paket als experimentelles Zusatzteil und gehört nicht zur Baseline.
