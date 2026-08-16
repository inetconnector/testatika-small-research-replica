# Contributing

Contributions are welcome if they improve provenance, geometry, measurement quality or reproducibility.

## Evidence labels
Every technical claim should be classified as:
- **OBSERVED** — directly visible/measured in a primary source or experiment
- **SOURCE** — explicitly stated by a named source
- **DERIVED** — calculated/scaled from a source
- **HYPOTHESIS** — plausible but not established
- **CONFLICT** — sources disagree

Do not silently upgrade a hypothesis to fact.

## CAD changes
1. state the evidence for the changed dimension;
2. update the relevant research document;
3. regenerate STL/STEP assets when applicable;
4. run `python scripts/validate_assets.py`;
5. update `CHANGELOG.md`.

## Experimental reports
Please include exact geometry, materials, humidity/temperature when relevant, instruments/calibration, all input-energy paths, and raw data where possible.

A spark or short lamp test is not by itself an energy-balance measurement.

## Commit style
Examples:
- `cad: refine first-machine pot geometry`
- `docs: add Marinov source note`
- `test: add C(theta) measurement dataset`
- `fix: correct rotor wire-routing jig`
