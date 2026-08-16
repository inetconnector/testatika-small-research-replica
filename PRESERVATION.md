# Preservation policy

This repository is a cumulative research record. The default rule is **preserve first, refactor second**.

## Non-loss principles

1. `main` is cumulative. New research may correct earlier interpretations, but earlier evidence, hypotheses, CAD variants and experiment branches must remain recoverable through Git history, immutable-style snapshot tags, release archives, or an explicitly documented archive path.
2. Never force-push `main` or rewrite published snapshot tags.
3. Before a substantial merge, verify that the current `main` commit already has an automatic `snapshot-main-*` tag; if not, create an explicit preservation tag/branch before proceeding.
4. Do not delete historical CAD, STL, STEP, source notes, evidence tables or experimental variants merely because a newer version exists. Prefer additive replacement and explicit deprecation metadata.
5. `STATE.md` is the cumulative knowledge ledger. Corrections should be additive and explicitly identify what changed and why. Do not rewrite history silently.
6. Preservation-critical content includes at minimum `STATE.md`, `addon.md`, `PRESERVATION.md`, `docs/`, `cad/`, `hardware/`, research manifests, release metadata and provenance ledgers.
7. Every merge to `main` should remain reconstructable from Git history and an automatic snapshot tag.
8. Binary assets are part of the research record. Regeneration is useful, but generated assets must not be removed until their replacement has been validated and committed.
9. When sources conflict, retain both claims with provenance and evidence ranking. Never delete the losing hypothesis solely because the current interpretation changed.
10. If a change intentionally removes or consolidates material, the pull request must explain where the old information remains recoverable.
11. Historical branch names are not themselves guaranteed preservation anchors after consolidation; immutable snapshot tags and commit SHAs are the canonical anchors.
12. Third-party source scans that cannot legally be redistributed may remain external, but their provenance, archive identifier, local filename/hash (when held), and rights status should be recorded.

## Current recovery anchors

- `main` — current integrated state.
- automatic `snapshot-main-<timestamp>-<sha>` tags — immutable-style snapshots created after pushes to `main`.
- Git commit history — all normal merge parents and prior commits remain part of the repository graph.
- historical release ZIPs — retained as release-era artifacts; never silently overwritten.

The former `archive/main-2026-08-16-r4-merge` branch was a temporary consolidation anchor and was intentionally eligible for deletion after its content was verified to be present in `main`. Its commit remains recoverable from Git history/snapshots; it is therefore no longer listed as a current branch anchor.

## Automatic safeguards

The repository contains two primary CI safeguards:

- `preservation-guard.yml` rejects accidental deletion of preservation-critical paths in pull requests.
- `snapshot-main.yml` creates a timestamped snapshot tag after every push to `main`.

Repository validation should additionally verify manifests, references, evidence ledgers and release metadata. These safeguards complement Git history; they do not replace ordinary review and independent backups.
