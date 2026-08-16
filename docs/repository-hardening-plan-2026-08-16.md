# Repository hardening and replication-completeness plan — 2026-08-16

## Goal

Bring the repository to a clean, internally consistent, preservation-safe and reproducible research state without deleting historical information. The project should become as close to a 1:1 **research replica** of the first small Marinov machine (M2) as surviving evidence allows.

The core rule is: **preserve evidence, add provenance, never invent an unknown historical detail.**

## Phase A — preservation and terminology

1. Work on a dedicated branch from the audited `main` head.
2. Keep all existing research/CAD/assets; do not delete superseded information solely because it is old.
3. Add a canonical replication-completeness ledger.
4. Add a canonical machine taxonomy and provenance schema.
5. Mark external/non-redistributed source archives explicitly instead of implying they are present in Git.

## Phase B — stale-content corrections

1. Correct the obsolete `unknown language` attribution in V3 photo analysis.
2. Replace stale references to deleted research branches with historical wording.
3. Update `PRESERVATION.md` to use immutable snapshot tags/Git history rather than a branch that was intentionally removed.
4. Update `ROADMAP.md` to the actual V3/V6 state.
5. Refresh `addon.md` naming and audit-head language.
6. Add explicit links from README to replication status and canonical taxonomies.

## Phase C — repository validation

Extend validation to cover:

- required research files;
- UTF-8 text readability;
- Markdown relative-link existence;
- TSV rectangularity and duplicate IDs for known ledgers;
- valid machine IDs where applicable;
- JSON parseability;
- STL geometry across baseline and V3 trees;
- V2/V3 complete-model existence;
- stale `ADDON.md` path references;
- stale active-branch wording;
- explicit external-source markers for non-repository archives.

Manifest integrity is separated from ordinary content validation so the manifest can be regenerated deterministically after all content changes.

## Phase D — reproducibility

1. Add a deterministic manifest generator for all tracked files except the generated manifest outputs themselves.
2. Add a manifest checker.
3. Add a single `scripts/rebuild_research_assets.py` entry point documenting/generating all CAD assets that are currently source-reproducible.
4. Maintain an explicit legacy/non-source-generated asset inventory until every V2 part is covered by parametric source.
5. Expand CAD source over time rather than claiming non-reproducible files are regenerated.

## Phase E — release/version hygiene

1. Advance the research package version to `0.3.0` after V3/R4/Baumann/Hartmann integration.
2. Synchronize `CITATION.cff`, changelog and release builder.
3. Build releases from an explicit include policy containing source, documentation, CAD, scripts, manifests and binary research assets.
4. Generate SHA-256 for the release archive.
5. Keep old `v0.2.0` archive as historical evidence; do not overwrite it.

## Phase F — 1:1 research-replica completion

The replication package is considered complete only in the evidence-aware sense documented in `docs/REPLICATION_STATUS.md`.

High-priority gaps:

1. rotor route: R0–R4 reversible test set;
2. rotor material: Cu/Fe/SS/Fe-Ni controlled variants;
3. electrode material/geometry: mesh/perforated/foil controlled set;
4. side-pot exact C/leakage/geometry measurements;
5. crystal black-box surrogate matrix;
6. rear shield/environment jig;
7. photo-derived M2 dimensional uncertainty ledger;
8. phase-resolved node map;
9. startup/priming protocol variants;
10. closed energy balance and independent replication.

No unknown item may be promoted to `historical original` without new primary evidence.

## Phase G — source preservation

For every high-value source, record where legally possible:

- stable source ID;
- speaker/author;
- machine ID;
- date;
- page/frame/timecode locator;
- original language;
- archive identifier/snapshot;
- original filename and SHA-256 when locally held;
- rights status;
- short statement summary;
- conflicts and project effect.

Full third-party scans remain outside public distribution unless redistribution rights are clear.

## Acceptance criteria

The hardening work is ready to merge when:

- preservation-critical information has not been deleted;
- validation succeeds;
- stale known contradictions are corrected;
- version/release metadata agrees;
- replication unknowns are explicit;
- machine/source provenance is structurally documented;
- a PR diff shows additive/hardening changes rather than destructive cleanup.

## Execution result

The hardening branch was reviewed through PR #7 and merged into `main` after both the expanded repository validator/manifest check and the preservation guard succeeded. The v0.3.0 research package was then materialized into `release/` with its own SHA-256 file. This final note intentionally triggers the post-release integrity cycle so the newly materialized package itself is incorporated into the repository manifest and covered by the final validation/snapshot state.
