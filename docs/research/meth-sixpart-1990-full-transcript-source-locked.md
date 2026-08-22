# Meth_1…Meth_6 — transcript source-lock correction

**Date:** 2026-08-22  
**Status:** **DEPRECATED / INVALID SOURCE MATCH**

The previous revision of this file incorrectly claimed that a German Luzi-Cathomen transcript was source-locked to the six uploaded AVI files.

This is not valid. The user directly identified the audio in `Meth_1.avi` as **English**. That observation is incompatible with the prior claim that the German `M/D/T` dialogue was a verbatim transcript of this exact AVI audio track.

The earlier VAD/reference alignment was therefore a false-positive sequence match. Similar timing around the camera disturbance was insufficient to prove audio identity.

## Consequence

- The German `M/D/T` transcript must **not** be cited as the transcription of `Meth_1.avi`.
- Engineering claims previously promoted solely through that assumed source lock are withdrawn pending real transcription of the uploaded audio.
- The older German Cathomen transcript remains a separate historical source lead and can still be studied on its own provenance chain, but not mapped onto these AVI files without direct acoustic verification.
- The prior text remains recoverable in Git history for research transparency.

## Exact file currently under correction

`Meth_1.avi` SHA-256: `b91ef047534d1748f06f49b4c43de08153f53470834d78d00cb3d22fa50fdf72`

Media properties already verified locally:

- duration: `565.838367 s` (~09:25.84)
- video: `MSMPEG4v2`, 368×208, 25 fps
- audio: MP3, 44.1 kHz, stereo
- language: **English according to direct listening by the user; independent ASR transcription still pending**

## Required next step

Perform actual audio transcription of `Meth_1.avi` from the audio stream itself, then continue file-by-file through `Meth_2.avi`…`Meth_6.avi`. Do not use the German historical transcript as replacement text.

Bulk-energy source remains **UNKNOWN**.