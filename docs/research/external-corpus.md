# External / non-redistributed source corpus

## Why this file exists

`STATE.md` was built partly from source archives and historical materials that are **not all redistributed in this public repository**. Earlier project notes mention names such as `testatika.zip` and `state_pre_corpus_rebuild.md`. Their absence from the current public tree must not be mistaken for evidence that the underlying historical sources never existed, nor should a replacement be invented.

## `testatika.zip`

Project history records an externally held research corpus under the working name `testatika.zip`, including third-party scans/images/documents. It is **not part of the public repository** because the archive includes third-party material whose redistribution rights are not established.

Rules:

- do not fabricate or silently recreate the archive from unrelated Internet files;
- do not commit full third-party books/scans merely to make the repository self-contained;
- when the archive is available to an authorized researcher, record its SHA-256, file inventory, original filenames and source locators without relicensing third-party content;
- derived statements in the public repository must increasingly point back to stable source IDs/locators.

## `state_pre_corpus_rebuild.md`

Historical notes refer to a pre-corpus-rebuild state backup by this name. That exact standalone file is not currently present in the audited public tree. The repository therefore does **not** claim to possess its original bytes.

The recoverable historical record is Git history/snapshot tags plus the cumulative `STATE.md`. If an authentic copy of `state_pre_corpus_rebuild.md` is recovered, preserve it byte-for-byte under an archive path and record its hash/provenance instead of synthesizing a substitute.

## Public-repository reproducibility boundary

A new session can reproduce the **public research state, CAD assets, evidence ledgers and experiment plans** from Git. It cannot reproduce every third-party source scan solely from this checkout.

For high-value external sources, the target metadata is defined by `docs/research/provenance-schema.yaml` and should include:

- source ID;
- author/speaker;
- machine ID;
- page/frame/timecode;
- stable URL/archive snapshot;
- local original filename/hash if legally held;
- rights status;
- short statement summary;
- conflicts and replication effect.

This explicit boundary is preferable to embedding copyrighted scans or pretending missing source bytes are present.