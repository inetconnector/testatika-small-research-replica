# `Meth_1`…`Meth_6` 1990 six-part source — P0 audio/provenance backlog

**Date:** 2026-08-22  
**Parent audit:** [`meth-sixpart-1990-source-video-audit-2026-08-21.md`](meth-sixpart-1990-source-video-audit-2026-08-21.md)  
**Transcript audit:** [`meth-sixpart-1990-transcript-technical-audit-2026-08-22.md`](meth-sixpart-1990-transcript-technical-audit-2026-08-22.md)

## Status update — 2026-08-22

The previous state said that the soundtrack lacked a usable German transcript. That is no longer true.

An older human transcript of the same amateur-video dialogue has been located in two independent web-preservation lines:

- a 2010 German mirror explicitly titled `Dokumentation des Testa Distatika Amateur-Videofilms`, assigning speaker roles `M`, `D`, `T` and attributing `M` to Luzi Cathomen;
- a 2009 Bulgarian Testatika forum post that describes an amateur video with Luzi Cathomen and exposes a `testatika.txt` attachment, proving that a transcript circulated before the 2010 mirror.

A reproducible local alignment tool now exists:

- [`../../scripts/align_meth_reference_transcript.py`](../../scripts/align_meth_reference_transcript.py)
- [`meth-sixpart-1990-alignment-summary.tsv`](meth-sixpart-1990-alignment-summary.tsv)

The recovered text contains 309 parsed turns / ~2507 words. VAD/reference alignment against the user-supplied six AVI audio tracks covers the complete 48.6-minute recording family. The resulting timestamps are **approximate**, not word-level forced alignment.

A strong sequence-level consistency check is present: the transcript statement that the camera is not working maps to approximately `Meth_3 05:46.9`, while the prior independent frame audit placed the visible/source disturbance at `Meth_3 ~05:58–06:01`. This supports same-recording identity without pretending to be biometric or word-for-word acoustic verification.

The full generated transcript is retained as a user-session artifact rather than committed to the public repository because third-party redistribution rights are unresolved.

## P0-1 — timestamped German transcription — SUBSTANTIALLY COMPLETE / AUDIO-LOCK PENDING

Completed:

- full textual dialogue sequence recovered from older human transcription;
- all six best-available AVI audio tracks extracted and traversed;
- speaker-role labels retained (`M`, `D`, `T`);
- approximate per-turn part/global timestamps generated reproducibly;
- technical claims extracted with attribution discipline.

Still required for publication-grade verbatim status:

- word-level forced alignment or careful re-listening of every unclear phrase;
- explicit confidence per disputed token;
- correction of old-transcript ambiguities such as `100 kW` vs the interlocutor's `100 kV`, `(Spulen?)`, `Plastikkammerzellen`, and dialect words;
- neutral speaker IDs in any claim where the Cathomen attribution itself matters.

Do not silently normalize dialect, technical vocabulary or non-standard Baumann/Methernitha terminology.

## P0-2 — speaker/source identity lock — UPGRADED LEAD

Evidence now converges beyond a generic six-part catalogue match:

1. the older German transcript names the workshop setting and assigns `M` to Luzi Cathomen;
2. a separate 2009 forum preservation line also labels the amateur video as Cathomen;
3. the recovered transcript contains a camera-failure discussion that aligns closely with the independently observed source/visual disturbance in the supplied recording.

Current classification:

- `M = Luzi Cathomen` is a **high-confidence historical transcript attribution**;
- it is not a face/voice biometric identification;
- the supplied derivative bitstreams still lack embedded identity metadata.

Acceptance rule for final P0 identity lock remains an original label/tape record, exact early source-page metadata, or equivalent contemporaneous provenance.

## P0-3 — acquire earliest/pre-transcode master — OPEN

Current copies are derivative:

- AVI: `Lavf51.12.1` transcodes;
- FLV: YouTube-derived encodes.

Acquire the earliest available six-part copy/master and record exact filename, byte size, SHA-256, container/codec, native dimensions/fps/audio, creation/encoder tags, any cassette/tape/source annotations and exact source URL/archive record.

The goal is to determine whether the visible `16/07/1990` clock belongs to a first-generation recording or an earlier insert copied into a later edit.

## P0-4 — source-transition characterization — OPEN

Around `Meth_3 ~05:58–06:01`, both derivative families inherit rapid interleaving among timestamped green footage, clothing/orange frames and a brief exterior frame.

The transcript alignment now gives an additional clue: a camera-malfunction statement occurs only seconds before this region in the approximate alignment.

This does not prove the transition mechanism. On the earliest master determine whether it is a continuous tape glitch, edit, camera/source switch or capture corruption. Do not interpret isolated transition frames as a continuous spatial route.

## P0-5 — transcript-to-existing-corpus comparison — ACTIVE

The technical audit has already extracted the strongest statements. Remaining corpus work should compare the exact source-attributed claims against:

- the 2001 Dienst/Cathomen `testa01.ram` / `testa02.ram` source;
- archived Methernitha institutional film text;
- known Cathomen transcript mirrors;
- Baumann-source statement ledger;
- Marinov and Hauser direct-source constraints.

The purpose is chronology and source identity, not merging all operator language into one synthetic explanation.

## P1 — engineering extraction — FIRST PASS COMPLETE

The 2026-08-22 technical audit records explicit/near-explicit statements concerning:

- magnetizable `Speziallegierungen` on one unfinished workshop machine;
- machine-size and kW claims, explicitly unverified;
- approximate 60-rpm statement, with the 50-Hz interpretation correctly attributed to visitor `D` rather than `M`;
- `Kondenser` / Leyden-bottle storage and output takeoff;
- upper `Kapazität`-increase / conditioning stage;
- magnets and uncertain `(Spulen?)` in that upper stage;
- spark-gap / reduced-pressure component associated with a condenser;
- non-contact `Abnehmer` and bearing-only wear statement;
- clear/black Plexiglas;
- counter-rotation;
- impulse `Fühler` and synchronization/frequency control;
- development origin in record/plate static electricity;
- voltage-maintenance as the key engineering difficulty;
- a single-disc/stationary-plate variant requiring higher rotational speed;
- a 1000-W-lamp historical claim and a claimed 1985 milestone;
- an automobile starter visible/used in a historical setup;
- fabrication statements;
- the important interviewer/operator-adjacent `aus der Luft` / lightning / nature discussion.

None of these statements supplies a closed energy balance. The air/nature language also does not overcome the V4.28 quantitative bound showing that ordinary fair-weather atmospheric electrical flux is far too small for the claimed power scale.

## Current technical status

The transcript strengthens the historical architecture:

`electrostatic generation -> non-contact pickup -> upper capacity/conditioning stage -> storage -> synchronized cyclic voltage maintenance`.

It does **not** identify a bulk source, prove an active foundation, prove a chemical reservoir, prove vacuum extraction, or validate kW output claims.

The sustained energy source remains **UNKNOWN**.
