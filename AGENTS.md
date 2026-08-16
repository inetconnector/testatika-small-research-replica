# AGENTS.md

1. Preserve the distinction between **observed, source-stated, photo-derived, derived, hypothesized, conflicting, and unknown** details.
2. Never present a speculative Testatika connection as an original verified connection.
3. Do not add a Tesla/HF stage to the small-machine baseline without primary evidence.
4. Do not claim over-unity, free energy, ZPE, tachyon energy or permanent-magnet energy as established.
5. Every geometry change must update the corresponding evidence/photogrammetry documentation and `docs/REPLICATION_STATUS.md` when it affects M2 completeness.
6. Keep STL and STEP outputs synchronized with CAD changes where the source generator owns those outputs.
7. Keep `STATE.md` as the consolidated, cumulative project knowledge base. Corrections are additive; do not silently erase earlier evidence, hypotheses, conflicts, or conclusions.
8. High-voltage instructions must remain safety-limited; do not add an open mains-powered HV supply design.
9. Maintain `.gitignore`, validation scripts, manifest integrity and release metadata.
10. Use clear commit messages describing the actual change.
11. Follow `PRESERVATION.md`: never force-push `main`; preserve superseded research/CAD in Git, snapshot tags, historical releases or an archive/deprecated path instead of silently deleting it.
12. Before substantial destructive cleanup or history-changing work, verify a recovery anchor exists at the pre-change `main` commit.
13. Treat `STATE.md`, `addon.md`, `ADDON.md`, `docs/`, `cad/`, `hardware/`, manifests and provenance ledgers as preservation-critical.
14. When two sources conflict, retain both source claims and their provenance/evidence rankings even if one is currently preferred.
15. Before changing the operating theory, electrical topology, `crystal` interpretation, pickup/drive classification or energy-source hypothesis, read `docs/research/baumann-language-decoding.md`, `docs/research/baumann-statements.tsv`, `docs/REPLICATION_STATUS.md`, and the relevant machine entry in `docs/research/machines.yaml`.
16. Do not quote the phrase that Baumann's explanation was "like an unknown language" as a direct Marinov statement unless a primary Marinov source is found. Current evidence separates Marinov's admitted non-understanding from Holzherr's report of Baumann's non-scientific terminology.
17. Keep speaker identity explicit: Paul Baumann, institutional Methernitha narration, Stefan Marinov, Hans Holzherr, Luzi Cathomen and Stefan Hartmann are separate sources/roles and must not be merged into a synthetic quotation.
18. Do not transfer a property from one machine ID to another without an explicit source argument. Use `docs/research/machines.yaml` as the canonical taxonomy.
19. For high-value source additions, follow `docs/research/provenance-schema.yaml`: include machine ID and page/frame/timecode locator whenever available.
20. A plausible reconstruction does **not** close a historical 1:1 gap. Only new primary evidence or controlled measurement of an original object can promote an `UNKNOWN`/`HYPOTHESIS` field to a historical fact.
21. Binary CAD assets without a complete source-generation path remain preserved. Do not claim `generate_v2.py` regenerates the full V2 library until `docs/research/cad-reproducibility.md` says so.
22. Run `python scripts/validate_assets.py`; after content changes regenerate/check manifests with `python scripts/generate_manifest.py` and `python scripts/check_manifest.py`.
