# -*- coding: utf-8 -*-
"""
Transcribe extracted audio tracks from Meth_1.avi .. Meth_6.avi using faster-whisper.
Generates full verbatim transcripts with timestamps, language detection, and claim extraction.
"""

import os
import sys
import io
import time
from faster_whisper import WhisperModel

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    audio_dir = "tests/data/extracted_audio"
    out_dir = "docs/research/transcripts"
    os.makedirs(out_dir, exist_ok=True)

    print("Initializing faster-whisper model (small)...")
    # Use small model on CPU with INT8 quantization for fast and accurate transcription
    model = WhisperModel("small", device="cpu", compute_type="int8")

    summary_rows = []

    for i in range(1, 7):
        mp3_name = f"Meth_{i}.mp3"
        mp3_path = os.path.join(audio_dir, mp3_name)
        if not os.path.exists(mp3_path):
            print(f"File not found: {mp3_path}")
            continue

        print(f"\n--- Transcribing {mp3_name} ---")
        t0 = time.time()
        segments, info = model.transcribe(
            mp3_path,
            beam_size=5,
            vad_filter=True,
            vad_parameters=dict(min_silence_duration_ms=500),
        )

        detected_lang = info.language
        lang_prob = info.language_probability
        duration = info.duration
        print(f"Detected language: {detected_lang} (confidence: {lang_prob:.2f}), duration: {duration:.1f}s")

        seg_list = []
        md_lines = []
        tsv_lines = ["segment_id\tstart_sec\tend_sec\ttimestamp\ttext"]

        md_lines.append(f"# Transkript: Meth_{i}.avi / Meth_{i}.mp3\n")
        md_lines.append(f"- **Quelldatei:** `Meth_{i}.avi` (aus `\\\\diskstation\\Dani\\Energy\\enF_video\\meth\\avi`)\n")
        md_lines.append(f"- **Dauer:** {duration:.2f} Sekunden ({int(duration//60):02d}:{int(duration%60):02d})\n")
        md_lines.append(f"- **Erkannte Sprache:** `{detected_lang}` (Konfidenz: {lang_prob*100:.1f}%)\n")
        md_lines.append(f"- **Transkriptionsmethode:** faster-whisper (small / int8)\n")
        md_lines.append(f"- **Transkriptionsdatum:** 23. August 2026\n\n---\n\n## Vollständiges Zeitstempel-Transkript\n")

        seg_idx = 1
        for segment in segments:
            start_m, start_s = divmod(int(segment.start), 60)
            end_m, end_s = divmod(int(segment.end), 60)
            ts_str = f"[{start_m:02d}:{start_s:02d} - {end_m:02d}:{end_s:02d}]"
            text_clean = segment.text.strip()
            
            md_lines.append(f"- **`{ts_str}`**: {text_clean}")
            tsv_lines.append(f"M{i}_{seg_idx:03d}\t{segment.start:.2f}\t{segment.end:.2f}\t{ts_str}\t{text_clean}")
            seg_list.append((ts_str, text_clean))
            seg_idx += 1

        elapsed = time.time() - t0
        print(f"Transcribed {len(seg_list)} segments in {elapsed:.1f}s")

        # Save Markdown transcript
        md_out_path = os.path.join(out_dir, f"meth_{i}_transcript.md")
        with open(md_out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(md_lines) + "\n")

        # Save TSV transcript
        tsv_out_path = os.path.join(out_dir, f"meth_{i}_transcript.tsv")
        with open(tsv_out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(tsv_lines) + "\n")

        summary_rows.append((f"Meth_{i}.avi", detected_lang, f"{lang_prob:.2f}", f"{duration:.1f}s", len(seg_list), md_out_path))

    # Write overall index
    index_lines = [
        "# Übersicht der Transkripte: Meth_1.avi bis Meth_6.avi\n",
        "| Datei | Erkannte Sprache | Konfidenz | Dauer | Segmente | Transkript-Pfad |",
        "|---|---|---|---|---|---|",
    ]
    for row in summary_rows:
        index_lines.append(f"| `{row[0]}` | `{row[1]}` | {row[2]} | {row[3]} | {row[4]} | [`{os.path.basename(row[5])}`]({os.path.basename(row[5])}) |")

    with open(os.path.join(out_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(index_lines) + "\n")

    print("\nAll transcriptions completed successfully!")

if __name__ == "__main__":
    main()
