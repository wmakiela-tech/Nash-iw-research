# INT8 ROT042 — reproductibility and source custody

This directory includes the full scientific mathematical report, TWO unmodified executable Python reproducing scripts, the original frozen exact SymPy results, and an explicitly labeled DERIVED numerical summary.

The original larger **main_results.json** is retained as a separate local Moderator attachment, not represented as byte-identical to the compact summary. The 8-member original archive is: iw_int8_rot042_general_integer_metric_tt_norm_bundle.zip, SHA256:
`0fbfefce85760f7ee93f940af4419cadd0bd5ede594ff72857315dc7d85a2c2c`.

## Execute

Requirements: Python 3.10+, NumPy, SymPy.

```bash
python audit_int8_rot042_exact.py --out exact_results.json
OPENBLAS_NUM_THREADS=1 python reproduce_int8_rot042.py --out main_results.json
```

The second command intentionally runs the mathematical checks and reports **SOURCE_SKIPPED_NO_HELPER**. To execute original auxiliary DTC0a source fidelity checks, also pass:
```bash
OPENBLAS_NUM_THREADS=1 python reproduce_int8_rot042.py --out main_results.json --source /your/retained/deepseek_python_20260627_a87249.py
```
Verify the user-retained original source SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801` before importing. The historical production dtc0a_runtime_v0_3_1.py is UNAVAILABLE; no original masked K_A is tested.

## Frozen original artifact hashes

| Original frozen file | SHA256 |
|---|---|
| Polish full report | `2cf99bdfc31cfaec1b049c5a75961f054f1c64588575210bbfdc7a4e69a18380` |
| reproduce_int8_rot042.py | `5592e25ce4a9d0ceb941535b7e2c17378d4d023da566d6a42089478644e9d07b` |
| audit_int8_rot042_exact.py | `3a8352fcdd48d83e049ee0ec66bf95f433b67b4c237c7332c8ab0b7a73b2fe76` |
| main_results.json | `5751bd9efdd652154ac86bc8782d82134eaedf7548e0fd451165d9e0e0542bee` |
| exact_results.json | `ac8191d30ef83486baa8c7f94c0d93860170cda519017f8b92c35a813b60aa1b` |

The GitHub scientific report is an equivalent self-contained scientific write-up with correct PUBLIC and BW_PENDING metadata, not a byte-identical copy of the original Polish frozen report (whose first edition documents the blocked publication attempt). Both executable scripts and exact_results.json were verified in GitHub by git blob identity against the original local files.

This is a mathematical finite-flat operator exercise. No independent referee, scientific adoption, actual BW ING, canon, EXEC, physical GW/GR or NCDG J3/K inference is implied.
