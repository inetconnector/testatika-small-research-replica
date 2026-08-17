# Beitragsvorschlag für das NET-Journal

Dieses Verzeichnis enthält einen **redaktionellen Beitragsvorschlag** zur Testatika-Forschung. Der Text ist **kein bereits erschienener Artikel des NET-Journals** und wurde nicht im Auftrag der Redaktion erstellt.

## Dateien

- `ARTICLE.md` – quelloffener Text des Beitragsvorschlags; maßgebliche aktuelle Textfassung.
- `Testatika_Beitragsvorschlag_NET-Journal_2026.docx` – Word-Fassung für redaktionelle Prüfung und Weitergabe.
- `Testatika_historisches_Foto.jpg` – historische Testatika-Aufnahme, als Illustrationsmaterial zum Vorschlag.
- `charge_state_model.png` – repository-eigene Funktionsgrafik zum aktuellen Arbeitsmodell.

## Erweiterung: Selbstanregung und Crystal-/Dioden-Kommutation

Die aktuelle Fassung erweitert das Arbeitsmodell um einen wichtigen Quellenhinweis aus der Methernitha-Beschreibung: Die Gleichrichterdiode wird dort nicht nur als Ausgangsgleichrichter beschrieben, sondern als Element, das den Anziehungs-/Abstoßungszyklus in einem stationären Zustand hält. Ohne diese Wirkung sollen sich die Impulse weiter aufsummieren und die Scheiben beschleunigen.

Daraus wird **nicht** vorschnell eine klassische LC-Resonanz abgeleitet. Das derzeit präzisere testbare Modell ist:

> **variable Kapazität → selbstangeregte Ladungszustände → Crystal-/Dioden-Phasenkommutation → phasenstabilisierter elektrostatischer Rotor → getrennte Drive-/Storage- bzw. Leistungspfade.**

Technisch entspricht dies einer positiven elektromechanischen Rückkopplung `ω → C(θ) → Q,V → τ → ω`, deren Schleifenwirkung durch einen nichtlinearen, winkelabhängigen Ladungspfad begrenzt bzw. kommutiert werden könnte. Eine hilfreiche Analogie ist ein Pendel mit phasenrichtigem Impuls und Hemmung: Nicht eine LC-Resonanz ist zwingend, sondern ein positiver Energieeintrag pro Zyklus plus phasenabhängige Begrenzung. Moderne variable-C-Energy-Harvester mit Dioden-/Kondensatornetzwerken zeigen, dass solche synchronisierten Lade-/Entladezyklen etablierte Elektromechanik sind; sie liefern jedoch keinen Hinweis auf Overunity. Eine zusätzliche LC-Resonanz in der großen Maschine bleibt möglich, ist aber derzeit nicht quellen- oder messseitig belegt.

Diese Erweiterung ist zugleich für die Lastfrage wichtig: Wenn historische Lastdemonstrationen real waren und kaum sichtbare Rotordrehzahländerung erzeugten, spricht das eher für eine **Taktgeber-/Kommutatorfunktion der Scheiben** als dafür, dass ihre Rotationsenergie direkt hunderte Watt oder Kilowatt liefert. Die Energiequelle eines solchen getrennten Leistungspfads bleibt ausdrücklich ungeklärt.

## Historisches Foto: Provenienz und Rechte

Das Bild wurde vom Repository-Eigentümer für diesen Beitragsvorschlag bereitgestellt. Es entspricht nach Abgleich der öffentlich gespiegelt vorliegenden historischen Datei `testabig.jpg`, u. a. unter:

`https://rimstar.org/sdenergy/testa/misc/testabig.jpg`

Das Repository **beansprucht keine Urheber- oder Nutzungsrechte** an dieser historischen Aufnahme. Sie ist nicht Bestandteil der MIT-Lizenz des repository-eigenen Codes/CAD/Textes. Vor Abdruck in einem Magazin oder einer anderen Veröffentlichung sollten Quelle und Abdruckrechte redaktionell abschließend geklärt werden. Falls ein Rechteinhaber eine Entfernung verlangt, sollte die Datei entfernt und im Artikel durch einen quellenrechtlich geklärten Ersatz ersetzt werden.

## Wissenschaftlicher Status

Der Beitrag beschreibt ein quellenkritisches **Arbeitsmodell**: elektrostatische Influenz/variable Kapazität, berührungslose Abnehmer, polaritätsselektive Ladungsführung, mögliche Crystal-/Dioden-Kommutation, positive Rückkopplung/Selbstanregung, phasensynchrone Drehzahlstabilisierung und getrennte Drive-/Storage-Zustände. Dieses Modell ist eine technische Übersetzung historischer Aussagen und **kein Nachweis eines Energieüberschusses**.

Die vollständige Forschungsbasis bleibt in `STATE.md`, `addon.md`, `docs/research/baumann-language-decoding.md`, `docs/research/baumann-statements.tsv` und `docs/scientific-status.md` erhalten.
