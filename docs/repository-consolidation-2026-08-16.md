# Repository consolidation — 2026-08-16

## Goal

Consolidate all useful work into `main` without deleting any file from `main`, then remove obsolete branch refs only after a preservation check proves that no branch-only file would be lost.

## Preservation rule

**`main` is extended, never reduced, by this consolidation.**

No repository file is intentionally deleted or renamed as part of this operation. Old branch refs are deleted only after their file trees are checked against the consolidated `main` tree.

## Work already integrated

- R4 rotor / grid-vs-foil research was merged through PR #1.
- Baumann / Methernitha language-decoding research was merged through PR #3. The principal research files on the old branch and on `main` have identical blob content after the merge.
- NET-Journal proposal material is already present on `main`; the related old publication branches have no commits ahead of `main`.
- V3 high-resolution photo analysis and experimental CAD was merged through PR #5 with **0 deletions**. The merge commit is `d30e1f37a7ee07676b4626092d1dca89347d3782`.
- After the V3 merge, both the repository validation workflow and the automatic `main` snapshot completed successfully.

## Canonical V3 complete-model aliases

The generated V3 model already exists under:

- `hardware/experimental/v3-photo/complete-model/Testatika_Small_Marinov_FirstMachine_V3_PHOTO_INTERP.step`
- `hardware/experimental/v3-photo/complete-model/Testatika_Small_Marinov_FirstMachine_V3_PHOTO_INTERP.stl`

For discoverability and direct V2/V3 comparison, the consolidation workflow also copies these **without removing the experimental originals** to:

- `hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V3_COMPLETE.step`
- `hardware/complete-model/Testatika_Small_Marinov_FirstMachine_V3_COMPLETE.stl`
- `hardware/complete-model/MODEL_INFO_V3.json`

The V2 complete-model files remain untouched.

## Branches scheduled for removal after preservation check

- `archive/main-2026-08-16-r4-merge`
- `docs/net-journal-proposal`
- `publication/net-journal-proposal`
- `research/baumann-language-decoding`
- `research/small-machine-v3-pixel-analysis`
- `ops/main-consolidation-cleanup`

## Automated safety check

Before any branch is deleted, the one-shot workflow fetches all remote branches and checks each old branch against the final `main` tree. If a file exists on an old branch but is absent from `main`, the workflow fails and **does not delete any branch**.

Only if every branch passes this file-preservation test are the obsolete remote branch refs deleted.

## Expected final state

- `main` contains all prior baseline files plus R4 research, Baumann analysis, publication material and V3 photo/CAD work.
- V2 and V3 complete models coexist.
- no content file from `main` is removed by consolidation.
- only the `main` branch remains after cleanup.
