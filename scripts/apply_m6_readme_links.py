#!/usr/bin/env python3
"""Compatibility wrapper for the bilingual primary-build README updater.

The old M6-only updater modified README.md alone and is intentionally retired because
README.md and README.en.md must always remain synchronized.
"""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name("apply_buildkit_readme_links.py")), run_name="__main__")
