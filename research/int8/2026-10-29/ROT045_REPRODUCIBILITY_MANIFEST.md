# INT8 ROT045 — reproducibility and custody

Scientific owner-local report: iw_int8_rot045_sharp_cubic_krylov_tt_gap_exponent_001.md (PUBLIC; sync_state: GITHUB_PENDING_BW_INGEST; no confirmed BW ingested event).

A separately executable **byte-verified** minimal source-free exact audit is at audit_int8_rot045_public_minimal.py, Git blob 80ba9063b29ef29276cee1cbbbff8803c33ce24e. It requires Python 3.10+ and SymPy and yields EXACT_KRYLOV_PASS for three irreducible matrices plus one reducible negative control.

**FULL frozen Moderator-local bundle**: iw_int8_rot045_sharp_cubic_krylov_gap_bundle.zip

ZIP SHA256: ef31a04fb2a9c0a4478afa857e9881fa53dfc929c46120bfc58f17413947eecf

Eight archive members, each checked by manifest SHA256, ZIP CRC PASS:

| File | SHA256 |
|---|---|
| README.md | 043c62f601e960f56071f07daabde92916d81db846f47c0b3e5808e4c88d377f |
| RUNLOG.txt | 33c65e8d78425dd487a5bb3b07110a02e7a0b4b7e49e20dfb359eacee6239cd1 |
| audit_int8_rot045_exact.py | 970ded066e08ab83320dee7085cc780e4bffb3b0cb1e27aff27bd43c583069d4 |
| exact_results.json | b262b4f92342e216e7c63edf1f20e81031ebc3d7be99517464295b2654900aec |
| iw_int8_rot045_krylov_cubic_sharp_tt_gap_report.md | 9d3eb23e45d322905da4885ef1464b042168288aedd9e32226d54ecb8080a739 |
| main_results.json | 1bc879b48dd6276b556caad3d2cfa4b0e022059fbd1640ac95590195069c164b |
| reproduce_int8_rot045.py | 90be6c2e7abf51fdf9d8f1ae7cf275fba8de36b801ff6e46c8554e8d2b51b409 |
| SHA256SUMS | contains seven above per-member hashes |

The full archive includes TWO independently runnable complete Python programs, two frozen JSON results, the longer Polish report and clean rerun instructions. Requires Python 3.10+, NumPy, SymPy. Run the main script with --out and optionally --source pointing to the user-retained unchanged deepseek_python_20260627_a87249.py, SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. Historical full production dtc0a_runtime_v0_3_1.py is byte-unavailable, and masked K_A not tested.

**Executed clean replicas**: A and B with literal SHA-checked source: main and independent exact JSON both BYTE IDENTICAL to archived. C without helper: independent exact JSON byte-identical, all main mathematical fields identical, source explicitly SOURCE_SKIPPED_NO_HELPER. Main: 225128 integer k tests, 168846 irreducible angular controls and 3 literal source cosine cases. Independent exact: 27708 integer k tests and symbolic Vandermonde, 4 exact characteristic polynomials, reducible control.

Limitations: mathematically positive c_A but no global NUMERIC certificate; matched lower cubic exponent and upper cubic bound only on an INFINITE SUBSEQUENCE; no physical admission, no original historical K_A, no canon, EXEC or novelty. Public GitHub report and minimal audit do NOT substitute for the full frozen Moderator-local ZIP unless the recipient also has access to the archive. BW ING, external referee and scientific owner are pending.
