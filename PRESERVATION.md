# Preservation policy

This repository is a cumulative research record. The default rule is **preserve first, refactor second**.

## Non-loss principles

1. `main` is cumulative. New research may correct earlier interpretations, but earlier evidence, hypotheses, CAD variants and experiment branches must remain recoverable.
2. Never force-push `main` or any `archive/*` branch.
3. Before a substantial merge or destructive cleanup, create an `archive/*` branch at the current `main` commit.
4. Do not delete historical CAD, STL, STEP, source notes, evidence tables or experimental variants merely because a newer version exists. Move superseded material under an archive/deprecated path when practical and document the replacement.
5. `STATE.md` is the cumulative knowledge ledger. Corrections should be additive and explicitly identify what changed and why. Do not rewrite history silently.
6. `addon.md`, `docs/research/`, `cad/`, `hardware/stl/` and `hardware/step/` are preservation-critical trees.
7. Every merge to `main` should remain reconstructable from Git history and an automatic snapshot tag.
8. Binary assets are part of the research record. Regeneration is useful, but generated assets must not be removed until their replacement has been validated and committed.
9. When sources conflict, retain both claims with provenance and evidence ranking. Never delete the losing hypothesis solely because the current interpretation changed.
10. If a change intentionally removes or consolidates material, the pull request must explain where the old information remains recoverable.

## Current recovery anchors

- `main` — current integrated state.
- `archive/main-2026-08-16-r4-merge` — snapshot immediately after PR #1 / R4 merge, commit `95efff27cd4f165fa487e335562eccd34948aeb5`.
- Git history — all normal merge parents and prior commits remain part of the repository graph.

## Automatic safeguards

The repository contains two CI safeguards:

- `preservation-guard.yml` rejects accidental deletion of preservation-critical paths in pull requests.
- `snapshot-main.yml` creates a timestamped snapshot tag after every push to `main`.

These safeguards complement Git history; they do not replace ordinary review and backups.
