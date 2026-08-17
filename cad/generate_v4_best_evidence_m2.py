#!/usr/bin/env python3
"""Compatibility entry point.

The old V4 all-solid generator is preserved under cad/reference/ for visual/provenance
inspection. Running this canonical path now builds the M2 V5 real-material fabrication kit.
"""
from pathlib import Path
import runpy
print("NOTICE: M2 V4 all-solid CAD is reference-only; generating M2 V5 fabrication kit.")
runpy.run_path(str(Path(__file__).with_name("generate_m2_v5_fabrication_kit.py")), run_name="__main__")
