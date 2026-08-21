#!/usr/bin/env python3
"""Reference-assisted alignment for the six-part 1990 Testatika audio.

This script does NOT perform semantic ASR. It aligns a pre-existing human transcript
against speech-active regions of the user-supplied audio, preserving uncertainty.
Timestamps are approximate until word-level acoustic alignment is available.

Inputs:
  audio/Meth_1.wav ... audio/Meth_6.wav (16 kHz mono PCM)
  reference_transcript.txt (speaker-prefixed M:/D:/T: lines)
Outputs:
  meth-sixpart-1990-reference-assisted-transcript.md
  meth-sixpart-1990-reference-assisted-transcript.tsv
  vad_summary.tsv
"""
from __future__ import annotations
import argparse, csv, re, wave
from dataclasses import dataclass
from pathlib import Path
import numpy as np

@dataclass
class Part:
    name: str
    path: Path
    duration: float
    global_start: float
    active_times: np.ndarray
    threshold_db: float
    active_fraction: float


def read_wav(path: Path):
    with wave.open(str(path), 'rb') as w:
        if w.getnchannels() != 1 or w.getsampwidth() != 2:
            raise ValueError(f'{path}: expected mono 16-bit PCM')
        sr = w.getframerate()
        x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
    return sr, x


def binary_close_open(mask: np.ndarray, close_frames: int, min_run: int) -> np.ndarray:
    mask = mask.astype(bool).copy()
    d = np.diff(np.r_[False, mask, False].astype(np.int8))
    starts = np.where(d == 1)[0]; ends = np.where(d == -1)[0]
    for a, b in zip(ends[:-1], starts[1:]):
        if b - a <= close_frames:
            mask[a:b] = True
    d = np.diff(np.r_[False, mask, False].astype(np.int8))
    starts = np.where(d == 1)[0]; ends = np.where(d == -1)[0]
    for a, b in zip(starts, ends):
        if b - a < min_run:
            mask[a:b] = False
    return mask


def vad_times(path: Path, global_start: float, frame_s: float = 0.02):
    sr, x = read_wav(path)
    n = int(sr * frame_s)
    frames = x[: len(x)//n*n].reshape(-1, n)
    rms = np.sqrt(np.mean(frames * frames, axis=1) + 1e-12)
    db = 20 * np.log10(rms + 1e-12)
    p20, p80 = np.percentile(db, [20, 80])
    threshold = float((p20 + p80) / 2.0)
    threshold = max(min(threshold, -23.0), -39.0)
    raw = db > threshold
    k = 5
    sm = np.convolve(raw.astype(np.float32), np.ones(k)/k, mode='same') >= 0.4
    mask = binary_close_open(sm, close_frames=18, min_run=5)
    centers = global_start + (np.arange(len(mask)) + 0.5) * frame_s
    active = centers[mask]
    duration = len(x)/sr
    return duration, active, threshold, float(mask.mean())


def parse_transcript(path: Path):
    turns = []
    for line in path.read_text(encoding='utf-8').splitlines():
        line=line.strip()
        if not line: continue
        m=re.match(r'^([MDT]):\s*(.*)$', line)
        if m:
            spk, txt=m.group(1), m.group(2).strip()
        else:
            spk='?'; txt=line
        words=re.findall(r"[\wÄÖÜäöüß'-]+", txt, flags=re.UNICODE)
        punct=len(re.findall(r'[,.?!;:…]', txt))
        weight=max(1.0, len(words) + 0.18*punct)
        turns.append({'speaker':spk,'text':txt,'words':len(words),'weight':weight})
    return turns


def sec_to_hms(s: float):
    s=max(0.0,float(s)); h=int(s//3600); s-=h*3600; m=int(s//60); s-=m*60
    return f'{h:02d}:{m:02d}:{s:05.2f}'

def sec_to_ms(s: float):
    s=max(0.0,float(s)); m=int(s//60); s-=m*60
    return f'{m:02d}:{s:05.2f}'


def part_for_time(parts, t):
    for i,p in enumerate(parts):
        end=p.global_start+p.duration
        if t < end or i==len(parts)-1:
            return p, max(0.0, min(p.duration, t-p.global_start))
    return parts[-1], parts[-1].duration


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--audio-dir', type=Path, default=Path('audio'))
    ap.add_argument('--transcript', type=Path, default=Path('reference_transcript.txt'))
    ap.add_argument('--out-dir', type=Path, default=Path('.'))
    args=ap.parse_args(); args.out_dir.mkdir(parents=True,exist_ok=True)

    parts=[]; g=0.0; all_active=[]
    for i in range(1,7):
        path=args.audio_dir/f'Meth_{i}.wav'
        dur, active, th, frac=vad_times(path,g)
        p=Part(f'Meth_{i}',path,dur,g,active,th,frac); parts.append(p)
        all_active.append(active); g+=dur
    active=np.concatenate(all_active)
    if len(active)<100: raise RuntimeError('VAD found too little speech')

    turns=parse_transcript(args.transcript)
    weights=np.array([t['weight'] for t in turns],dtype=float)
    edges=np.r_[0.0,np.cumsum(weights)]/weights.sum()
    idx=np.clip(np.round(edges*(len(active)-1)).astype(int),0,len(active)-1)

    rows=[]
    for j,t in enumerate(turns):
        start=float(active[idx[j]])
        end=float(active[idx[j+1]]) if j+1<len(idx) else g
        if end<start: end=start
        p,local=part_for_time(parts,start); pe,local_e=part_for_time(parts,end)
        rows.append({**t,'global_start_s':start,'global_end_s':end,
                     'part':p.name,'part_start_s':local,'end_part':pe.name,'part_end_s':local_e})

    tsv=args.out_dir/'meth-sixpart-1990-reference-assisted-transcript.tsv'
    with tsv.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['turn','speaker','part','part_start','end_part','part_end','global_start','global_end','words','text'],delimiter='\t')
        w.writeheader()
        for n,r in enumerate(rows,1):
            w.writerow({'turn':n,'speaker':r['speaker'],'part':r['part'],'part_start':sec_to_ms(r['part_start_s']),
                        'end_part':r['end_part'],'part_end':sec_to_ms(r['part_end_s']),
                        'global_start':sec_to_hms(r['global_start_s']),'global_end':sec_to_hms(r['global_end_s']),
                        'words':r['words'],'text':r['text']})

    md=args.out_dir/'meth-sixpart-1990-reference-assisted-transcript.md'
    with md.open('w',encoding='utf-8') as f:
        f.write('# Meth_1…Meth_6 — deutschsprachiges Referenz-Transkript mit Audio-Zeitausrichtung\n\n')
        f.write('**Status:** vollständiger textlicher Dialoginhalt aus einer älteren menschlichen Transkriptionsquelle, gegen die sechs vom Nutzer bereitgestellten Tonspuren als gleiche Aufnahmefamilie eingeordnet; Zeitmarken sind VAD-/Längen-basiert **ungefähr**, nicht wortakustisch erzwungen. Unklare Alttranskript-Stellen bleiben markiert.\n\n')
        f.write('**Wichtig:** Dies ist kein Beleg für die physikalische Richtigkeit der Aussagen. `M`, `D`, `T` sind die Sprecherrollen der historischen Transkriptionsquelle; `M` wird dort Luzi Cathomen zugeschrieben, diese Identität ist für die vorliegende Bitstream-Kopie quellenkritisch separat zu führen.\n\n')
        current=None
        for r in rows:
            if r['part']!=current:
                current=r['part']; f.write(f'\n## {current}\n\n')
            f.write(f"[{sec_to_ms(r['part_start_s'])} ~ | global {sec_to_hms(r['global_start_s'])}] **{r['speaker']}:** {r['text']}\n\n")
        f.write('\n---\n\n## Zeitmarken-Hinweis\n\n')
        f.write('Die Zuordnung wurde reproduzierbar aus Sprachaktivität (20-ms-RMS-VAD) und der relativen Textlänge erzeugt. Sie dient zum schnellen Auffinden einer Passage im Ton. Für Zitate ist die konkrete Audiostelle erneut anzuhören; die Markierungen sind keine forensische Forced-Alignment-Messung.\n')

    vad=args.out_dir/'vad_summary.tsv'
    with vad.open('w',encoding='utf-8',newline='') as f:
        w=csv.writer(f,delimiter='\t'); w.writerow(['part','duration_s','global_start_s','threshold_dbfs','active_fraction','active_seconds'])
        for p in parts:
            w.writerow([p.name,f'{p.duration:.3f}',f'{p.global_start:.3f}',f'{p.threshold_db:.2f}',f'{p.active_fraction:.4f}',f'{len(p.active_times)*0.02:.2f}'])

    print(f'parts={len(parts)} duration={g:.3f}s active={len(active)*0.02:.1f}s turns={len(turns)} words={sum(t["words"] for t in turns)}')
    print(md); print(tsv); print(vad)

if __name__=='__main__': main()
