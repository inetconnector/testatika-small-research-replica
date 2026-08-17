#!/usr/bin/env python3
"""Compatibility entry point.

The old M6 V1 all-solid generator is preserved under cad/reference/ for visual/provenance
inspection. Running this canonical path now builds the M6 V2 real-material fabrication kit.
"""
from pathlib import Path
import runpy
print("NOTICE: M6 V1 all-solid CAD is reference-only; generating M6 V2 fabrication kit.")
runpy.run_path(str(Path(__file__).with_name("generate_m6_v2_fabrication_kit.py")), run_name="__main__")
