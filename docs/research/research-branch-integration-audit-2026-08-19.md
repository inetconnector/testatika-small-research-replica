# Research branch integration audit — 2026-08-19

## Scope

This audit checks all branch refs currently present in the repository and the historical research pull-request chain before deciding whether additional research content should be moved into `main`.

The integration rule is provenance-first: do not blindly merge stale branches when their substantive content is already present in `main`, because doing so could reintroduce old manifests, workflows, superseded interpretations or conflicts.

## Current branch inventory

At audit time the repository contains `main` plus these research branches:

- `agent/m2-v4-14-dynamo-port`
- `agent/m2-v4-16-corona-return-port`
- `agent/m2-v4-18-two-port-return`
- `agent/m2-v4-19-rear-plate-human-return`
- `agent/m2-v4-20-local-infrastructure-bound`
- `agent/m2-v4-21-real-power-field-bound`
- `agent/m2-v4-22-source-reaction-boundary`
- `agent/m2-v4-23-non-electrical-source-bounds`
- `agent/m2-v4-24-earth-rotation-coupling-bound`
- `agent/m2-v4-25-natural-geoelectric-bound`

No additional `research/*` branch refs remain.

## Integration status

The current V4.14–V4.25 branch line is already represented by merged pull requests #21 through #30. PR #30 was merged during this audit and therefore brings the latest V4.25, pre-2000 source excavation, Hartmann provenance cleanup and Schneider 2000 / retrospective-1984 source audit into `main`.

No open `agent/*` research pull request remains after that merge.

## Historical exception: PR #15

PR #15 (`research: add evidence-ranked wiring and lamella test plans`) was closed without being merged as a PR. It must **not** be re-merged blindly from its stale branch state.

Its substantive research package has already propagated into current `main`. Verified canonical files include:

- `docs/electrical/M2_V5_EVIDENCE_WIRING.md`
- `docs/electrical/M6_V2_EVIDENCE_WIRING.md`
- `docs/electrical/WIRING_VARIANTS.tsv`
- `docs/electrical/LAMELLA_TEST_MATRIX.tsv`
- `docs/electrical/SOURCE_IMAGE_FAMILIES.tsv`
- `docs/electrical/BUILD_ORDER.md`

These retain the important PR #15 distinctions: source-ranked wiring, open historical nodes, controlled laboratory variants, lamella/material controls, source-image genealogy and one-variable-at-a-time commissioning.

PR #16 was only a temporary synchronization PR and explicitly intended no project-content change, so there is nothing to recover from it.

## Content preserved in main

The audit therefore confirms that the important research line is cumulative in `main`, including:

- evidence-bound M2/M6 geometry and build kits;
- primary-source video/scan audit and machine-family separation;
- source-ranked electrical variants and lamella controls;
- regenerative-grid / distributed-floating-rotor diagnostics;
- phase-commutation / charge-state-regeneration working hypotheses;
- V4.1–V4.25 source-power and environmental-coupling bounds;
- pre-2000 provenance excavation and source ledgers;
- corrected Hartmann provenance;
- Schneider 2000 source audit of the retrospective summer-1984 Testatika demonstration.

## Guardrail

No branch integration changes the scientific status of the energy-source question. The historical bulk real-power reservoir remains `UNKNOWN`. Source-stated observations, retrospective eyewitness reports, secondary reconstruction, laboratory comparators and project hypotheses remain separate evidence classes.

## Decision

No additional stale research branch should be merged wholesale into `main` at this point. The only newly pending substantive branch, V4.25/PR #30, has been integrated. The former unmerged PR #15 content is already present canonically in `main`; PR #16 contains no independent research content.

Old merged branch refs may be retained for provenance or removed later as repository hygiene, but branch deletion is not part of this audit.
