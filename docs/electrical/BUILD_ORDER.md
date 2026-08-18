# Elektrische Inbetriebnahme — Reihenfolge

Diese Reihenfolge verhindert, dass ein Verdrahtungsfehler oder eine unerkannte externe Energiequelle als Testatika-Effekt fehlinterpretiert wird.

1. **Mechanik fertig und geschützt:** Rundlauf, Auswuchtung, Spalte, Lager, Schutzhaube.
2. **W0:** alle ungesicherten Knoten offen; Isolation, Kapazitätsmatrix, Wicklungsdaten, `C(theta)` und Phasenkarte messen.
3. **Dummy-Kontrollen:** nichtmagnetische Lamellen-/Magnet-Dummys und Vollfolie/Lochblech/Gitter vergleichen.
4. **W1:** ausschließlich die dokumentierte strombegrenzte Labor-Bias-/Pickup-/Gleichrichter-/Speicher-Schaltung verwenden.
5. **Energiepfade schließen:** Motor, Biasquelle und jeder Anfangsladungszustand gleichzeitig messen.
6. **W2/W3:** nur eine Hypothesenverbindung bzw. ein Modul pro Versuch ändern; Config-ID protokollieren.
7. **Lamellenmatrix:** Legierung, Magnetisierung, Perforation und Oberfläche jeweils einzeln variieren.
8. **Top-Modul:** erst nach reproduzierbarer Grundkopplung Kandidaten an die BLACK-BOX-Schnittstelle stecken; nie eine Kandidatenbox als Original ausgeben.
9. **Replikation:** überraschende Resultate mit Dummy, zweitem Messprinzip und vollständiger Energiebilanz wiederholen.

## Stoppbedingungen

Versuch abbrechen bei unkontrollierter Funkenbildung, Erwärmung, Rotorberührung, unerwartetem Erdpfad, Sättigung/Überlastung eines Messgeräts oder unbekanntem Kondensator-Ladezustand.
