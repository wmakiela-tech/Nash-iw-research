# INT8 ROT049 — complete source reproducibility and integrity

**Public science**: iw_int8_rot049_nonconstant_puretrace_isospectral_z_shear_stability_001.md
**Owner**: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
**Date**: 2026-11-01
**Exposure**: PUBLIC
**Current sync**: GITHUB_PENDING_BW_INGEST (actual BW adoption is UNVERIFIED).

## FULL executable scripts on GitHub — actual bytes read back

Both below are BYTE-IDENTICAL to the locally executed, SHA-matched original files from the frozen ZIP, not truncated or paraphrased:
- reproduce_int8_rot049.py — git blob b48d778551c11a4d473dc0cdecca3d85b5d07ec8; SHA256 50b36b53b1c29f864855224d0f573706f9407a90adc61b50554c898426b55224.
- audit_int8_rot049_exact.py — git blob 4abac9bd26da247e31469352ba3720eda633cfa2; SHA256 22eb1c59a74aa90b0968153df8a3a5656fa9ccf9c4316172413b932820f473d7.
- exact_results_rot049.json — git blob 3a415a2145938f4ca0b909f99c1b2b4e35913cf9; SHA256 5d33ed61bde8b6d4232a44c8b644706abb732947968b7d512123c67b13492917. Exact frozen independent source-free result byte-identical.
- The FULL numerical main_results.json is in the Moderator-local original ZIP only; its SHA256 is 0aa6a6a71d44ba9229de4d2f9b71cc1c472494eebbeea9440a8f77feb2724ea7. Do not claim it is byte-identically present on GitHub.

## Replay

Requires Python >=3.10, NumPy (main) and stdlib only (independent).

python audit_int8_rot049_exact.py --out exact_results.json

OPENBLAS_NUM_THREADS=1 python reproduce_int8_rot049.py --out main_results.json

Last command performs only mathematical scalar baseline calculations and reports SOURCE_SKIPPED_NO_HELPER. To execute original SOURCE:
OPENBLAS_NUM_THREADS=1 python reproduce_int8_rot049.py --out main_results.json --source /your/retained/deepseek_python_20260627_a87249.py

Unmodified SOURCE SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801 is checked before import. The auxiliary original helper is NOT redistributed. Historic full production dtc0a_runtime_v0_3_1.py byte unavailable; no original masked K_A test.

## Frozen local complete 8-member ZIP
iw_int8_rot049_nonconstant_puretrace_isospectral_robustness_bundle.zip
SHA256 **a4e44f89f816b0ed44c3589c5866b940c0701f82596e88584ec528c652087aae**.
ZIP CRC PASS, payload SHA256 7/7 PASS.

| Member | SHA256 |
|---|---|
| README.md | 33ea07a5bcc716ba157691ea788248c0255c04271bb3e3a4c688fe4115b6a5c8 |
| RUNLOG.txt | 495da5dc429b6d88f27e1b05297e963e9e65bea52880bd2636fdfe55dc6eecf0 |
| audit_int8_rot049_exact.py | 22eb1c59a74aa90b0968153df8a3a5656fa9ccf9c4316172413b932820f473d7 |
| exact_results.json | 5d33ed61bde8b6d4232a44c8b644706abb732947968b7d512123c67b13492917 |
| iw_int8_rot049_nonconstant_puretrace_transverse_shell_report.md | 5e6faefce0f64a33f6301d864cb17b3adb35e9f29ed3cb37823f2fe855c2f3f4 |
| main_results.json | 0aa6a6a71d44ba9229de4d2f9b71cc1c472494eebbeea9440a8f77feb2724ea7 |
| reproduce_int8_rot049.py | 50b36b53b1c29f864855224d0f573706f9407a90adc61b50554c898426b55224 |
| SHA256SUMS | contains the seven above |

THREE separate actually executed clean extractions:
- CLEAN A with original byte-SHA-verified helper: main JSON and exact JSON BOTH BYTE IDENTICAL to frozen.
- CLEAN B with original byte-SHA-verified helper: main JSON and exact JSON BOTH BYTE IDENTICAL to frozen.
- CLEAN C without helper: exact JSON BYTE IDENTICAL; all mathematical scalar main values byte-equivalent; native original helper correctly SOURCE_SKIPPED_NO_HELPER (no false source pass).

## Exact result type and limitations
For a source-specific equal-E-eigenshell commuting z-shear pair: Identity K_C=0 for ANY symmetric tensor H; E_lin K_C=K_B=0 for ANY f(z)I; projected auxiliary K_A_out norm >= abs(mean f) times ROT048 positive constant baseline. Positive and nonconstant f(z) tested directly. Planar f(x)I E_lin KC/KB nonzero negative control. Fraction exact grid N=3 verifies source-independent algebra only, not original odd N>=7 TT projection.

No original masked historic h=fI K_A, even-N RAW cast, curved York, GR gauge, physical J3/K, Noether/GW, experimental claim, novel mathematics, canon or EXEC. BW ING, independent referee, scientific original-owner uptake ALL PENDING. NO_NEW_TASK_CASCADE.
