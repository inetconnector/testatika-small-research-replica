# Meth_1…Meth_6 — transcript technical audit correction

**Date:** 2026-08-22  
**Status:** **DEPRECATED AS AUDIO MATCH**

The previous revision asserted that an older German human transcript had been matched to the six uploaded AVI files. That source lock was not sufficiently established.

The user directly identified the audio in `Meth_1.avi` as English. This contradicts the previous claim that the German `M/D/T` dialogue was the transcript of that exact file.

The prior VAD/reference alignment must therefore be treated as a false-positive alignment and not as acoustic transcription evidence.

## Validity split

Still valid:

- the German historical Cathomen transcript exists as a separate source;
- its statements may be studied under its own provenance;
- the AVI file hashes, durations, codecs and visual audit remain valid.

Invalid / withdrawn:

- calling the German transcript a transcript of `Meth_1.avi`;
- using approximate VAD timing to assign German transcript statements to the uploaded AVI files;
- promoting engineering claims from that assumed match into the AVI-derived evidence layer.

## Correct workflow

1. Extract and transcribe the actual audio stream of each uploaded AVI.
2. Detect/record language per file.
3. Produce timestamps directly from ASR/manual listening.
4. Compare the resulting text with historical transcripts only afterward.
5. Promote technical claims only when the actual audio supports them.

Current confirmed correction: `Meth_1.avi` is English by direct user listening.

The sustained bulk-energy source remains **UNKNOWN**.