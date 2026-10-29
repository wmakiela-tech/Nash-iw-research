# INT8-046 — custody, replay and full scientific claim ceiling

**Science:** iw_int8_rot046_centered_lie_raw_tt_symbol_mismatch_source_001.md, PUBLIC; sync_state GITHUB_PENDING_BW_INGEST. No independent referee/owner uptake/EXEC.

**Public exact independently executed SymPy:** audit_int8_rot046_exact.py (Git blob SHA1 02bba88dac55f340751b726a48bc85177dbb520c, byte-identical to original full-package exact script). Python 3 + SymPy:
  python audit_int8_rot046_exact.py --out exact_results.json
Expected EXACT_SYMPY_PASS 240 rational checks, 5 symbolic tensor identities, 104 zero controls. This does NOT import original helper.

**Public minimal original-source replay:** reproduce_int8_rot046_public_native_minimal.py (Git blob SHA1 093593a0042d32ce540d3660de6dc2c787df6f30, byte-identical to separately locally executed mini script). Python 3 + NumPy. Without helper:
  OPENBLAS_NUM_THREADS=1 python reproduce_int8_rot046_public_native_minimal.py
It must print SOURCE_SKIPPED_NO_HELPER; math still PASS. With ORIGINAL source byte-SHA-checked:
  OPENBLAS_NUM_THREADS=1 python reproduce_int8_rot046_public_native_minimal.py --source /your/path/deepseek_python_20260627_a87249.py
Original helper SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. Native tests of 5 cosine witnesses including one exactly zero expected SOURCE_SHA_VERIFIED_PASS.

**Full frozen Moderator-local ZIP** iw_int8_rot046_native_centered_derivative_raw_tt_mismatch_bundle.zip
SHA256 04aae7443d4ed8166057db14c3067dbbbdf0b31c6b296cac15742729328d5b1d
ZIP CRC PASS, archive 8 members, original payload SHA256 7/7 PASS:

| member | SHA256 |
|---|---|
| README.md | 07f274c51651feebb044624de0766d1113e7511086a0790f3d9758e2277e014f |
| RUNLOG.txt | 5d1f728f13710823c28ac9e296c1ce0ffa399577e218756d797c66f890b20eab |
| audit_int8_rot046_exact.py | e2a8c85c6f35f9cbbad3fed323a5d3ddc13d505d38ea2698247fcd70e88a4224 |
| exact_results.json | 3991a6ca6fed0b225b22fda7d6bbf1fd1c23b52969337cfa5c06737ae8eee539 |
| iw_int8_rot046_native_centered_lie_raw_tt_compatibility_report.md | d0e5d9253bcad6e9d12728c49bbf79a118af021263f68d0be56337227f8fb831 |
| main_results.json | 2bec87a47ae7f2019bdf992163708f4c4e589eea2575f479d0dffad949fe8ff1 |
| reproduce_int8_rot046.py | 9acc2fa3578403a5183b84fdc5c1dbf8b9568d3de5a734170940672fae5c325c |

Two separate CLEAN original-helper-present extractions reproduced BOTH JSON files BYTE IDENTICAL; third CLEAN helper-absent extraction reproduced mathematical JSON and math components unchanged but marked SOURCE_SKIPPED_NO_HELPER. The full original native numerical script and both original frozen JSON are in the ZIP; public mini native script is a separate verified subset, not a byte-for-byte replacement for the full native script.

**Source-typed limits:** single projected_T for constant puretrace h=I on odd raw signed-k source; no masked historical K_A, no full historic runtime, no gravitational gauge or physical energy, no novelty, no canon, no EXEC. Any silent substitution of raw-k TT with s_N(k)-TT changes the original source object and requires independent owner decision. No new task cascade.
