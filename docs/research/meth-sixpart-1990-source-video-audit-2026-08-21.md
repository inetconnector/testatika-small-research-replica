# Six-part `Meth_1`…`Meth_6` source-video audit — 2026-08-21

**Status:** provenance/visual-source audit. No recovered circuit. No energy-source promotion.  
**Archive supplied by user:** `meth.zip`  
**Archive SHA-256:** `cc8f66d2f557af5b2fde7193db52b06b8b0505d76a79183a0bc148571f94a320`  
**Rights:** third-party source held externally; videos and extracted frames are not redistributed by this repository.

## 1. Scope and evidence boundary

The supplied archive contains twelve files: six AVI files and six same-number FLV files. Every video stream was traversed in full and the six AVI/FLV pairs were compared visually and acoustically.

The user described these as new original videos. They are important newly acquired **source copies**, but the container metadata proves that the supplied bitstreams themselves are not camera-original masters:

- AVI files carry `software=Lavf51.12.1`, consistent with a later FFmpeg/libavformat transcode;
- FLV files carry `creator=YouTube, Inc.` and `metadatacreator=YouTube Metadata Injector.`, proving a YouTube-derived encode path.

The in-picture camera date/time can still derive from an older source recording. Therefore this audit distinguishes:

`underlying historical recording` ≠ `supplied derivative bitstream`.

No claim from the soundtrack is promoted to Paul Baumann, Luzi Cathomen, Methernitha or any machine family until the German audio has been timestamp-transcribed and the speakers/source chain have been locked.

## 2. File-level result

Detailed hashes and media properties are in [`meth-sixpart-1990-source-ledger.tsv`](meth-sixpart-1990-source-ledger.tsv).

AVI characteristics:

- MSMPEG4v2 video;
- `368 × 208`;
- `25 fps`;
- MP3 `44.1 kHz`, stereo;
- `Lavf51.12.1` software tag.

FLV characteristics:

- FLV1 video;
- `320 × 240`;
- `30 fps`;
- MP3 `22.05 kHz`, mono;
- YouTube creator/metadata tags.

The six AVI durations sum to approximately **2916.94 s = 48.62 min**.

Full AVI decode traversed **72,920 frames**:

| part | duration | decoded AVI frames |
|---|---:|---:|
| Meth_1 | 565.838 s | 14,145 |
| Meth_2 | 526.840 s | 13,171 |
| Meth_3 | 549.094 s | 13,727 |
| Meth_4 | 481.881 s | 12,047 |
| Meth_5 | 366.158 s | 9,152 |
| Meth_6 | 427.128 s | 10,678 |

## 3. The twelve files are six recordings, not twelve independent sources

Synchronized ten-second samples were normalized and compared by perceptual hash. The AVI and FLV file of each part match as the same underlying visual sequence; all sampled pairwise pHash distances were small.

| pair | mean pHash Hamming | median | maximum |
|---|---:|---:|---:|
| 1 | 1.93 | 2 | 8 |
| 2 | 1.51 | 2 | 6 |
| 3 | 1.49 | 0 | 8 |
| 4 | 0.38 | 0 | 2 |
| 5 | 0.70 | 0 | 2 |
| 6 | 1.02 | 0 | 4 |

The audio independently reaches the same conclusion. After conversion to a common 8-kHz mono representation, coarse 100-Hz amplitude-envelope correlations for AVI↔FLV were:

| pair | correlation | best lag |
|---|---:|---:|
| 1 | 0.9651 | ~0.02 s |
| 2 | 0.9701 | ~0.02 s |
| 3 | 0.9726 | ~0.02 s |
| 4 | 0.9776 | ~0.03 s |
| 5 | 0.9781 | ~0.03 s |
| 6 | 0.9767 | ~0.03 s |

**Evidence consequence:** count these as **six underlying recordings preserved in two derivative encode families**, not twelve independent observations.

## 4. New date/provenance information

The strongest new source information is the in-picture camera clock.

The beginning of `Meth_1` visibly reads approximately:

`16/07/1990 18:45:23`.

The visible clock then continues across the first three parts:

- `Meth_1`: approximately `18:45:23` → `18:54:51`;
- `Meth_2`: approximately `18:54:52` → `19:03:40`;
- `Meth_3`: approximately `19:03:40` → about `19:09:40/41` before a source/visual transition.

This is much stronger dating evidence for the **underlying camera material** than the derivative file metadata. It is not proof that every later frame in parts 3–6 belongs to one uninterrupted camera take; see the transition caveat below.

Key frame locators are recorded in [`meth-sixpart-1990-frame-locators.tsv`](meth-sixpart-1990-frame-locators.tsv).

## 5. Full visual traversal: no new Testatika-machine geometry recovered

This is the central negative result.

Across the full 48.6-minute traversal, the camera is overwhelmingly:

- obstructed by clothing;
- aimed at a coat, knit garment, trousers, hands, floor/nearby surfaces;
- or otherwise not showing a Testatika machine in a usable way.

The scan did **not** reveal a defensible new view of:

- M2 rotor routing or rear side;
- side-pot internals or terminal map;
- the `crystal` interior;
- M2 stator grouping/polarity;
- an active M2 base;
- M6 cylinder hidden wiring;
- a layered M6 foundation interior;
- a load/input meter arrangement sufficient for energy accounting.

Therefore **no CAD geometry or electrical baseline is changed by the visual track**.

This new source is presently much more valuable as an **audio-bearing visit record and provenance object** than as a mechanical video.

## 6. Important transition around `Meth_3` ≈ 06:00

At roughly `Meth_3 00:05:58–00:06:01`, the decoded sequence rapidly alternates among:

- the earlier green/timestamped view;
- tan/khaki clothing without the timestamp;
- orange fabric;
- a very brief exterior view.

The same transition pattern is present in both the AVI and FLV copies. It therefore should not be dismissed as a decoder-only artifact.

Possible explanations include source switching, edit/capture discontinuity or mixed/corrupted transfer. The audit cannot uniquely distinguish them.

**Rule:** isolated frames around this transition must not be treated as one continuous physical camera movement or used to infer a machine-to-building spatial route.

The audio spectrum also changes across this region. The earlier parts show a pronounced narrow 50-Hz harmonic comb whereas the later sequence does not show the same pattern as strongly. This supports the existence of a recording/environment/transfer change, but the 50-Hz comb is **not** Testatika-output evidence; mains/recording hum is the conservative interpretation.

## 7. New exterior-site provenance clue: `TRIGONORM AG`

A rare exterior frame near `Meth_3 ≈ 00:06:00.06` shows a grey industrial/community building on a rural hillside. Enlarged inspection makes the horizontal sign read most consistently as **`TRIGONORM AG`**, with `TRIGO` branding also visible on a vertical banner.

This is technically important only as **provenance**, not as machine evidence.

Independent public-source cross-checks:

- an ETH/e-periodica-hosted 1984 directory lists `Trigonorm AG`, `Betriebs- und Lagereinrichtungen`, at `3517 Linden`, telephone `031/9711 21`;
- current Swiss directory listings place `TRIGONORM AG` at `Moosbühlweg 2, 3673 Linden BE`;
- current Swiss directory listings also place `Methernitha` administration at `Moosbühlweg 2, 3673 Linden BE`.

Reference URLs:

- https://www.e-periodica.ch/cntmng?pid=geo-006%3A1984%3A82%3A%3A1219
- https://search.ch/tel/linden/moosbuehlweg-2/trigonorm-ag
- https://search.ch/tel/linden/moosbuehlweg-2/methernitha-3

### Consequence

The exterior frame gives the six-part material a **substantially stronger Linden/Methernitha-site-area provenance anchor** than a generic web filename would provide. The 1984 directory independently establishes Trigonorm at Linden before the visible 1990 camera date, so the chronology is plausible.

What this does **not** establish:

- that the preceding dialogue was physically inside a Testatika workshop;
- that the speaker is Luzi Cathomen;
- that Trigonorm manufactured any Testatika component;
- that the building visible in the brief frame contains a Testatika machine;
- any electrical or energy-source mechanism.

No material/fabrication property is transferred from Trigonorm to M2/M6 without a direct source bridge.

## 8. External catalogue match: likely `dialogue with Luzi Cathomen`, but identity is still provisional

A public historical video index lists exactly six consecutive items titled:

`Testatika generator - dialogue with Luzi Cathomen - part 1` … `part 6`.

The same six-part catalogue appears in more than one surviving index/mirror. Example:

- https://matri-x.ru/video.shtml

This is a strong source-discovery match to the supplied `Meth_1`…`Meth_6` six-part set, but the supplied derivative files contain no title metadata identifying Cathomen, and the audio has not yet been semantically/transcript-locked in this audit.

Therefore current classification is:

- **six-part Testatika/Cathomen catalogue identity: PROVISIONAL / high-value lead**;
- **speaker identity: UNKNOWN pending audio/source-chain lock**.

Do not merge this material with the repository's separate **2001** `testa01.ram` / `testa02.ram` Dienst–Cathomen workshop source. The new footage has an in-picture 16-Jul-1990 sequence and a very different visual character. The two source families remain separate unless direct audio or archive metadata proves continuity.

## 9. Audio status

The soundtrack is potentially the highest-value part of this acquisition. However, this pass did not have a reliable local German ASR model or a source transcript available. No semantic quotation is therefore fabricated from the audio.

Pending work is documented in [`meth-sixpart-1990-audio-backlog.md`](meth-sixpart-1990-audio-backlog.md).

Until timestamped transcription is complete:

- no new Baumann statement is added to `baumann-statements.tsv`;
- no new Cathomen technical statement is added;
- no machine-specific topology is inferred from speech;
- no energy-source claim is upgraded.

## 10. Consequences for the current technical model

### What changes

1. The corpus gains a new ~48.6-minute six-part historical recording family with a visible `16/07/1990` camera-time sequence.
2. The archive contains two derivative representations of each part; duplication is now quantified and must not be double-counted.
3. A brief exterior frame strongly anchors the material to Linden/Methernitha's Moosbühlweg site area through the independently corroborated `TRIGONORM AG` sign/address.
4. The source is now a P0 target for timestamped German audio transcription and master-source acquisition.

### What does not change

1. No new M2 CAD geometry is justified.
2. No new M6 electrical connection is justified.
3. No new proof of an active foundation/base is present.
4. No crystal material is identified.
5. No input/output power balance is present.
6. The V4.26–V4.32 resonance/reservoir work remains hypothesis/discriminator work rather than recovered historical function.
7. The sustained bulk-energy source remains **UNKNOWN**.

## 11. Highest-value next acquisition/test actions

1. **Timestamp-transcribe the German soundtrack** for all six parts, preserving speaker uncertainty and marking unintelligible spans.
2. Compare voice/acoustic content against independently identified Cathomen recordings only after a valid reference source is available; do not identify a person from appearance alone.
3. Acquire the **pre-YouTube / pre-FFmpeg master or earliest available six-part copy** and hash it.
4. Recover the original source page/archive metadata for the six `dialogue with Luzi Cathomen` catalogue entries and compare exact durations/file sizes.
5. Use the transcript to search for explicit machine IDs, component names, measurements, dates, locations and first-person operator statements; only then update source-statement ledgers.

## 12. Bottom line

The new videos do not presently solve the machine electrically. Their strongest new contribution is **provenance and chronology**:

> a roughly 48.6-minute six-part recording family contains a continuous visible camera-time sequence beginning `16/07/1990 18:45:23`, and a transition frame shows `TRIGONORM AG` in Linden at the same address area currently associated with Methernitha.

That materially strengthens the historical source chain, but it does not close any M2/M6 hidden-circuit or energy-reservoir gap. Those remain **UNKNOWN** pending the soundtrack transcription and stronger original-master provenance.
