#!/usr/bin/env python3
"""Validate German/English README parity.

The checker cannot judge translation quality, but it enforces the repository contract:
- both language files exist;
- both expose the language switch at the top;
- synchronized sections use identical IDs and order;
- each paired section has the same structural payload (headings, list/table counts,
  link/image targets, code blocks and technical inline-code tokens);
- when requested, a Git range may not change only one README.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DE = ROOT / "README.md"
EN = ROOT / "README.en.md"
MARKER_RE = re.compile(r"<!--\s*README-SYNC:([a-z0-9-]+)\s*-->")
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"```([^\n]*)\n(.*?)```", re.DOTALL)
INLINE_RE = re.compile(r"`([^`\n]+)`")
HEADING_RE = re.compile(r"^(#{2,6})\s+", re.MULTILINE)
UNORDERED_RE = re.compile(r"^\s*[-*]\s+", re.MULTILINE)
ORDERED_RE = re.compile(r"^\s*\d+\.\s+", re.MULTILINE)
BLOCKQUOTE_RE = re.compile(r"^>\s?", re.MULTILINE)
TECH_SUFFIXES = (
    ".md", ".py", ".yaml", ".yml", ".tsv", ".json", ".zip", ".sha256",
    ".step", ".stl", ".glb", ".asf", ".wmv",
)


@dataclass(frozen=True)
class Signature:
    heading_levels: tuple[int, ...]
    unordered_items: int
    ordered_items: int
    table_lines: int
    blockquotes: int
    links: tuple[str, ...]
    code_blocks: tuple[tuple[str, str], ...]
    technical_inline: tuple[str, ...]


def read(path: Path) -> str:
    if not path.is_file():
        raise SystemExit(f"Missing required README: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def split_sections(text: str) -> tuple[list[str], dict[str, str]]:
    matches = list(MARKER_RE.finditer(text))
    if not matches:
        raise SystemExit("README contains no README-SYNC markers")
    ids = [m.group(1) for m in matches]
    if len(ids) != len(set(ids)):
        raise SystemExit(f"Duplicate README-SYNC marker(s): {ids}")
    sections: dict[str, str] = {}
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections[match.group(1)] = text[match.end():end]
    return ids, sections


def table_line_count(section: str) -> int:
    return sum(1 for line in section.splitlines() if line.lstrip().startswith("|"))


def technical_inline(section: str) -> tuple[str, ...]:
    values: list[str] = []
    for token in INLINE_RE.findall(section):
        if "/" in token or token.endswith(TECH_SUFFIXES) or token in {
            "ANOTHER language", "connected to nothing", "crystal", "Taster", "antenna keys"
        }:
            values.append(token)
    return tuple(values)


def signature(section: str) -> Signature:
    return Signature(
        heading_levels=tuple(len(h) for h in HEADING_RE.findall(section)),
        unordered_items=len(UNORDERED_RE.findall(section)),
        ordered_items=len(ORDERED_RE.findall(section)),
        table_lines=table_line_count(section),
        blockquotes=len(BLOCKQUOTE_RE.findall(section)),
        links=tuple(LINK_RE.findall(section)),
        code_blocks=tuple((lang.strip(), body.rstrip()) for lang, body in FENCE_RE.findall(section)),
        technical_inline=technical_inline(section),
    )


def validate_language_switch(de: str, en: str) -> None:
    de_prefix = de[:700]
    en_prefix = en[:700]
    if 'href="README.en.md">English</a>' not in de_prefix:
        raise SystemExit("README.md must link to README.en.md in the top language selector")
    if 'href="README.md">Deutsch</a>' not in en_prefix:
        raise SystemExit("README.en.md must link to README.md in the top language selector")
    if "<strong>Deutsch</strong>" not in de_prefix:
        raise SystemExit("README.md must mark Deutsch as the active language")
    if "<strong>English</strong>" not in en_prefix:
        raise SystemExit("README.en.md must mark English as the active language")


def validate_pair() -> None:
    de = read(DE)
    en = read(EN)
    validate_language_switch(de, en)
    de_ids, de_sections = split_sections(de)
    en_ids, en_sections = split_sections(en)
    if de_ids != en_ids:
        raise SystemExit(
            "README-SYNC section IDs/order differ:\n"
            f"German:  {de_ids}\nEnglish: {en_ids}"
        )

    errors: list[str] = []
    for section_id in de_ids:
        de_sig = signature(de_sections[section_id])
        en_sig = signature(en_sections[section_id])
        if de_sig != en_sig:
            errors.append(
                f"Section '{section_id}' differs structurally.\n"
                f"  German:  {de_sig}\n"
                f"  English: {en_sig}"
            )
    if errors:
        raise SystemExit("README language parity check failed:\n" + "\n".join(errors))


def changed_files(base: str, head: str) -> set[str]:
    proc = subprocess.run(
        ["git", "diff", "--name-only", base, head, "--", "README.md", "README.en.md"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        raise SystemExit(f"git diff failed for {base}..{head}: {proc.stderr.strip()}")
    return {line.strip() for line in proc.stdout.splitlines() if line.strip()}


def validate_changed_pair(base: str, head: str) -> None:
    changed = changed_files(base, head)
    if changed and changed != {"README.md", "README.en.md"}:
        raise SystemExit(
            "README language update is incomplete: a README change must modify both "
            f"README.md and README.en.md in the same change; changed={sorted(changed)}"
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--require-pair",
        nargs=2,
        metavar=("BASE", "HEAD"),
        help="also require that a Git range changes either both README files or neither",
    )
    args = parser.parse_args()

    validate_pair()
    if args.require_pair:
        validate_changed_pair(args.require_pair[0], args.require_pair[1])
    print("README German/English synchronization: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
