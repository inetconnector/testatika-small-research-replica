# AGENTS.md

1. Preserve the distinction between **observed, source-stated, photo/video-derived, derived, hypothesized, conflicting, and unknown** details.
2. Never present a speculative Testatika connection as an original verified connection.
3. Do not add a Tesla/HF stage to the small-machine baseline without new contrary primary evidence; direct Marinov correspondence currently argues against Tesla coils/AC for the described small machine.
4. Do not claim over-unity, free energy, ZPE, tachyon energy or permanent-magnet energy as established.
5. Every geometry change must update the corresponding evidence/photogrammetry/video documentation and `docs/REPLICATION_STATUS.md` when it affects M2 completeness.
6. Keep STL and STEP outputs synchronized with CAD changes where the source generator owns those outputs; source-only experimental generators may document regenerated-but-uncommitted binary outputs in `docs/research/cad-reproducibility.md`.
7. Keep `STATE.md` as the consolidated, cumulative project knowledge base. Corrections are additive; do not silently erase earlier evidence, hypotheses, conflicts, or conclusions.
8. High-voltage instructions must remain safety-limited; do not add an open mains-powered HV supply design.
9. Maintain `.gitignore`, validation scripts, manifest integrity and release metadata.
10. Use clear commit messages describing the actual change.
11. Follow `PRESERVATION.md`: never force-push `main`; preserve superseded research/CAD in Git, snapshot tags, historical releases or an archive/deprecated path instead of silently deleting it.
12. Before substantial destructive cleanup or history-changing work, verify a recovery anchor exists at the pre-change `main` commit.
13. Treat `STATE.md`, `addon.md`, `ADDON.md`, `docs/`, `cad/`, `hardware/`, manifests and provenance ledgers as preservation-critical.
14. When two sources conflict, retain both source claims and their provenance/evidence rankings even if one is currently preferred.
15. Before changing the operating theory, electrical topology, `crystal` interpretation, pickup/drive classification or energy-source hypothesis, read `docs/research/baumann-language-decoding.md`, `docs/research/baumann-statements.tsv`, `docs/REPLICATION_STATUS.md`, `docs/research/hauser-marinov-primary-scan-audit-2026-08-16.md`, `docs/research/video-frame-audit-2026-08-16.md`, and the relevant machine entry in `docs/research/machines.yaml`.
16. Source-language rule: Stefan Marinov's primary scan directly contains **`ANOTHER language`** regarding Baumann's attempted explanation. The popular wording **`like an unknown language`** is still not verified as Marinov's exact phrase and must not be quoted as such.
17. Small-machine electrical baseline: direct Marinov correspondence says the described disk wires are **`connected to nothing`**. Treat individually floating sectors as the preferred M2 baseline; the late 1-kΩ neighbour-ring claim is only a secondary control hypothesis unless stronger machine-specific evidence appears.
18. Small-pot baseline: direct Marinov correspondence describes cylindrical grid + plastic insulation + central copper spiral and says two wires are visible going to each condenser. Preserve a historically faithful two-terminal external mode; do not import Hauser's large-machine three-grid/magnet/bifilar cylinder into M2.
19. Keep speaker identity explicit: Paul Baumann, institutional Methernitha narration, Stefan Marinov, Albert Hauser, Hans Holzherr, Luzi Cathomen, Dieter Dienst and Stefan Hartmann are separate sources/roles and must not be merged into a synthetic quotation.
20. Do not transfer a property from one machine ID to another without an explicit source argument. Use `docs/research/machines.yaml` as the canonical taxonomy, including M6a/M6b/M7 subfamilies where appropriate.
21. For high-value source additions, follow `docs/research/provenance-schema.yaml`: include machine ID, file hash and page/frame/timecode locator whenever available.
22. Do not double-count re-encodes/language variants as independent geometry evidence; `meth2.asf` and `testatikadeutsch.wmv` are preserved separately but share the same visual sequence.
23. A plausible reconstruction does **not** close a historical 1:1 gap. Only new primary evidence or controlled measurement of an original object can promote an `UNKNOWN`/`HYPOTHESIS` field to a historical fact.
24. Binary CAD assets without a complete source-generation path remain preserved. Do not claim `generate_v2.py` regenerates the full V2 library until `docs/research/cad-reproducibility.md` says so.
25. Run `python scripts/validate_assets.py`; after content changes regenerate/check manifests with `python scripts/generate_manifest.py` and `python scripts/check_manifest.py`.
26. For a **new physical M2 build**, use `docs/research/v4-best-evidence-m2.md` and `cad/generate_v4_best_evidence_m2.py` as the current build starting point. V2/V3 are preserved comparison/provenance families, not the current final build recommendation.
27. V4 nominal electrical null state is `M2-V4-B0`: 24 floating Cu sectors, R0 physical route, two-terminal pots open internally to measurement, hub arcs floating, Crystal open, magnets present, load disconnected and lab drive disconnected. See `docs/research/v4-configurations.yaml`.
28. Never silently change more than one V4 experimental variable. New variants must inherit from a named configuration ID and explicitly list `change_only` fields, unless a predeclared factorial experiment requires otherwise.
29. V4 materialized outputs are source-owned by `cad/generate_v4_best_evidence_m2.py`; after generator changes run `python scripts/check_v4_assets.py` and rebuild `release/experimental/testatika-m2-v4-best-evidence-build-package.zip`.
30. For the **large ~500-mm two-disc line**, use `docs/research/m6-large-v1-best-evidence.md` and `cad/generate_m6_large_v1.py`. Do not copy M6 electrical internals back into M2.
31. M6 V1 construction anchor is M6a/Hauser 1986-1988. M6b/Holzherr 1999 remains a separate configuration source where speed, capacitor construction or other details differ.
32. M6 nominal electrical state is `M6-V1-B0`: unknown stator, cylinder, horseshoe, capacitor and top-module nodes remain **open** at explicit test terminals. Visual completeness is never permission to invent the hidden circuit.
33. M6 first powered configuration is `M6-V1-LAB-MECH`: guarded low-voltage mechanical counterrotation only, no electrostatic bias and no load. Laboratory drive/guard geometry must be labelled derived, not historical.
34. M6 materialized outputs are source-owned by `cad/generate_m6_large_v1.py`; after generator changes run `python scripts/normalize_m6_step.py`, `python scripts/check_m6_assets.py` and rebuild `release/experimental/testatika-m6-large-v1-best-evidence-build-package.zip`.
