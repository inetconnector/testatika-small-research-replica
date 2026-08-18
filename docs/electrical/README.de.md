# Testatika — elektrische Baudokumentation

<p align="center">
  <strong>Deutsch</strong> · <a href="README.md">English</a>
</p>

## Kanonische Pläne

### Kleine M2 V5

- [`M2_V5_EVIDENCE_WIRING.md`](M2_V5_EVIDENCE_WIRING.md)
- [`diagrams/M2_V5_EVIDENCE_WIRING.svg`](diagrams/M2_V5_EVIDENCE_WIRING.svg)

### Große M6 V2

- [`M6_V2_EVIDENCE_WIRING.md`](M6_V2_EVIDENCE_WIRING.md)
- [`diagrams/M6_V2_EVIDENCE_WIRING.svg`](diagrams/M6_V2_EVIDENCE_WIRING.svg)

## Maschinenlesbare Register

- [`WIRING_VARIANTS.tsv`](WIRING_VARIANTS.tsv) — alle Verdrahtungsvarianten mit Evidenzklasse und Claim-Grenze
- [`LAMELLA_TEST_MATRIX.tsv`](LAMELLA_TEST_MATRIX.tsv) — Material-/Magnetisierungs-/Geometrie-A/B-Matrix
- [`SOURCE_IMAGE_FAMILIES.tsv`](SOURCE_IMAGE_FAMILIES.tsv) — deduplizierte Schaltbild-/Bildfamilien
- [`SOURCE_IMAGE_FAMILIES.md`](SOURCE_IMAGE_FAMILIES.md) — Leseschlüssel
- [`BUILD_ORDER.md`](BUILD_ORDER.md) — elektrische Inbetriebnahmereihenfolge

## Quellen-Audits

- [`../research/wiring-and-lamella-audit-2026-08-17.md`](../research/wiring-and-lamella-audit-2026-08-17.md)
- [`../research/wiring-image-audit-addendum-2026-08-17.md`](../research/wiring-image-audit-addendum-2026-08-17.md)
- [`../research/hauser-marinov-primary-scan-audit-2026-08-16.md`](../research/hauser-marinov-primary-scan-audit-2026-08-16.md)
- [`../research/hartmann-overunity-cathomen-audit.md`](../research/hartmann-overunity-cathomen-audit.md)
- [`../research/r4-grid-vs-foil.md`](../research/r4-grid-vs-foil.md)

## Elektrischer Vertrag

1. **Keine versteckten geratenen Verdrahtungen.** Jede historisch unsichere Verbindung wird extern gepatcht und erhält eine Config-ID.
2. **Direkte Quellen schlagen Reverse Engineering.** Marinov-/Hauser-/Cathomen-/Holzherr-Grenzen stehen über Kelly-/Potter-/Rimstar-Rekonstruktionen, wo sie sich widersprechen.
3. **Eine elektrisch funktionierende Laborschaltung ist nicht automatisch die historische Originalschaltung.**
4. **Hochspannungsversuche beginnen mit kleiner gespeicherter Energie und kommerzieller strombegrenzter Laborausrüstung.**
5. **Floating-Systeme brauchen potentialfreie/differenzielle Messtechnik.** Eine Oszilloskopmasse darf nicht ungeprüft angeschlossen werden.
6. **Energiebehauptungen benötigen eine geschlossene Bilanz** aus Motor, Biasquelle, Anfangs-/Endenergie aller Speicher, Mechanik, Last und Messunsicherheit.

## Was weiterhin unbekannt ist

Das öffentlich zugängliche Material legt weiterhin **keinen reproduzierbaren authentischen Knoten-für-Knoten-Methernitha-Stromlaufplan** offen. Ebenfalls offen bleiben unter anderem Crystal-Material/-Funktion, genaue M2-Pot-Polung, exakte M6-Gitterverschaltung und die von Cathomen nicht erklärte obere Konditionierungs-/Kapazitätsstufe.

Diese Lücken werden als offene Schnittstellen abgebildet und nicht durch erfundene Bauteile verdeckt.
