#!/usr/bin/env python3
"""Add repository-hardening corrections to cumulative research ledgers.

The migration is deliberately idempotent and additive: no prior STATE/addon material is
deleted. New blocks explicitly supersede stale repository-metadata statements where
necessary while preserving the historical text for provenance.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def append_once(rel: str, marker: str, block: str) -> bool:
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    if marker in text:
        return False
    if not text.endswith("\n"):
        text += "\n"
    text += "\n" + block.strip() + "\n"
    path.write_text(text, encoding="utf-8")
    return True


changed = []

state_block = r'''
# 104. Repository hardening / public-corpus boundary — 2026-08-16

**Korrekturhinweis zu älteren Repository-Metadaten:** Frühere Abschnitte dieses kumulativen Ledgers nennen Arbeitsdateien wie `testatika.zip` und `state_pre_corpus_rebuild.md`. Diese Hinweise bleiben aus Preservation-Gründen stehen, dürfen aber nicht so gelesen werden, als lägen die Originalbytes heute im öffentlichen Git-Tree.

- `testatika.zip` bezeichnet einen historisch verwendeten externen Forschungskorpus mit Drittmaterial. Er ist **not part of the public repository / nicht Bestandteil des öffentlichen Repositories**, weil Redistribuierungsrechte für enthaltene Scans/Bücher/Bilder nicht pauschal geklärt sind.
- `state_pre_corpus_rebuild.md` wird in älteren Projektnotizen als Sicherung genannt; im auditierten öffentlichen Tree lag diese exakte Datei nicht vor. Es wird **kein Ersatzinhalt erfunden**. Falls eine authentische Kopie wiedergefunden wird, ist sie bytegetreu mit Hash/Provenienz zu archivieren.
- Der öffentliche Reproduzierbarkeitsrahmen ist jetzt in `docs/research/external-corpus.md` dokumentiert.
- Historische Recovery-Anker sind Git-History und `snapshot-main-*`-Tags; temporäre Konsolidierungsbranches sind nicht mehr als dauerhaft existierende Branches vorauszusetzen.

## 104.1 1:1-Begriff

Der verbindliche Vollständigkeitsstatus der kleinen Marinov-Maschine M2 steht in `docs/REPLICATION_STATUS.md`. Eine **vollständige Forschungsreplik** bedeutet: alle belegten Merkmale + dokumentierte Unsicherheiten + reversible Testvarianten. Sie bedeutet nicht, dass unbekannte Originalverdrahtung, Crystal-Material oder Pot-Topologie geraten und anschließend als Original ausgegeben werden.

## 104.2 Kleine quantitative Korrektur

Die an anderer Stelle verwendete Größenordnung `10 kJ` Lastenergie gegenüber ungefähr `1.4 J` Rotationsenergie entspricht einem Faktor von rund `7143`, also `log10(7143) ≈ 3.85` Größenordnungen. Die physikalische Schlussfolgerung bleibt unverändert (Rotationsspeicher ist viel zu klein), die Formulierung „mehr als vier Größenordnungen“ ist jedoch mathematisch etwas zu stark.

## 104.3 Kanonische neue Struktur

- Maschinen-IDs: `docs/research/machines.yaml`
- Provenienzschema: `docs/research/provenance-schema.yaml`
- Replikationslücken: `docs/REPLICATION_STATUS.md`
- CAD-Reproduzierbarkeit: `docs/research/cad-reproducibility.md`
- externer/nicht redistribuierter Korpus: `docs/research/external-corpus.md`
- Hardening-Plan: `docs/repository-hardening-plan-2026-08-16.md`

Diese Ergänzung löscht oder entwertet ältere Forschungsabschnitte nicht; sie definiert lediglich den aktuellen Repository-/Provenienzrahmen.
'''

if append_once("STATE.md", "# 104. Repository hardening / public-corpus boundary", state_block):
    changed.append("STATE.md")

addon_block = r'''

---

# POST-AUDIT HARDENING NOTE — 2026-08-16

Dieser Block ist **additiv** und hat Vorrang vor veralteten Repository-Metadaten im Kopf dieser Datei.

1. Die kanonische Datei heißt weiterhin `addon.md`. Zusätzlich existiert nun `ADDON.md` als case-sicherer Kompatibilitäts-Einstieg, damit ältere Session-Anweisungen auf Linux/macOS nicht ins Leere laufen.
2. Der im historischen Header genannte Audit-Tree `aa20ef...` ist ein damaliger Audit-Anker, **nicht der aktuelle Repository-Head**. Aktuelle Sessions müssen den tatsächlichen `main`-Commit aus Git bestimmen und dürfen keinen fest verdrahteten alten SHA als Gegenwartsstand behandeln.
3. Vor `STATE.md` sollte eine neue Session jetzt `docs/REPLICATION_STATUS.md`, `docs/research/machines.yaml` und `docs/research/provenance-schema.yaml` berücksichtigen.
4. `testatika.zip` ist ein externer/nicht öffentlich redistribuierter Forschungskorpus und **nicht Bestandteil des öffentlichen Git-Repositories**. Siehe `docs/research/external-corpus.md`.
5. Die historische Sicherungsreferenz `state_pre_corpus_rebuild.md` war beim Audit nicht als Datei im öffentlichen Tree vorhanden; kein Ersatzinhalt darf erfunden werden.
6. V3 ist in `main` integriert. Der frühere Branch `research/small-machine-v3-pixel-analysis` ist nur noch Provenienz, keine Voraussetzung für Zugriff auf V3-Dateien.
7. `V3_COMPLETE` ist ein Convenience-Dateiname; die V3-Modellmetadaten bleiben `experimental` / photo interpretation.
8. Der 1:1-Zielbegriff ist evidenzgebunden: unbekannte Originaldetails bleiben UNKNOWN und werden durch reversible Varianten abgedeckt, bis Primärevidenz sie schließt.

## Aktualisierte Startreihenfolge

1. `AGENTS.md`
2. `README.md`
3. `docs/REPLICATION_STATUS.md`
4. `addon.md`
5. `STATE.md`
6. `docs/sources.md`
7. `docs/research/source-basis.md`
8. `docs/research/evidence_matrix.tsv`
9. `docs/research/machines.yaml`
10. `docs/research/provenance-schema.yaml`
11. `docs/research/experiment-plan.md`
12. relevante Subsystem-Dokumente
'''

if append_once("addon.md", "# POST-AUDIT HARDENING NOTE — 2026-08-16", addon_block):
    changed.append("addon.md")

print("updated:", ", ".join(changed) if changed else "nothing (already applied)")
