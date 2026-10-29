# INT8 ROT047 — audyt źródłowy i kompletna reprodukcja

## Dostępne pliki GitHub — full readback verified
- iw_int8_rot047_commuting_z_shears_projection_inserted_KA_nogo_001.md — kompletny opis dowodu i zakresu.
- audit_int8_rot047_exact.py — **bajtowo identyczny** z pełnym niezależnym oryginalnym audytem w pakiecie (Git blob aaa39415b1ce532f25188d1553cf520d97a26a87).
- exact_results_rot047.json — **bajtowo identyczny** z zamrożonym oryginalnym JSON (Git blob bcbf3a710c56d41fa3ed4b3ebbd9de770e94cfa8).
- public_source_minimal_rot047.py — **bajtowo identyczny** z oddzielnie uruchomionym lokalnym minimalnym falsyfikatorem, Git blob 9d39553b49b62da33bd76c9d99cf3f449108c956. Nie jest zamiennikiem kompletnego oryginalnego reproduktora.

Run:
  python audit_int8_rot047_exact.py --out exact_results.json
  OPENBLAS_NUM_THREADS=1 python public_source_minimal_rot047.py --source /path/to/deepseek_python_20260627_a87249.py

Original auxiliary user source sha256: 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. It is NOT redistributed. Without source, exact SymPy can be rerun but direct actual helper K_A_out CANNOT be claimed as executed.

## Frozen complete Moderator-local 8-member ZIP
Name: iw_int8_rot047_projected_commuting_shears_exact_source_KA_bundle.zip
SHA256: cb59225ca96ea78352f215d559671f1720ef51636f68310c90036b0f2c6d057c
ZIP CRC PASS; 7/7 member SHA256 PASS.

Original payload hashes:
- README.md: 6a384a5b11a62811cd87f88180c3935e00bee59b4033db4aea838b59282b52b5
- RUNLOG.txt: b8e19e7a846c6fccd4e4345e1e0bc7d0c50f0c50c4a71c30039def564a465a9a
- audit_int8_rot047_exact.py: da0875e9c6f521fa2ee89b0e0c19fbfc055116f6ee53b2b409358b8f1f76012a
- exact_results.json: ff2218baeaa8319eb0a8a004dad069cbae1e5acbb7152acfda1e46ff32332dea
- iw_int8_rot047_projected_commutator_closure_report.md: 2f014fc28baa41343f21e531dfe5ed61ca1b93682f4c8d0ec6817c19047f11f5
- main_results.json: 0831590229be3ae20bcc797dc1037a3e2498fad631a551afb2c0a021a8f19944
- reproduce_int8_rot047.py: 26c29cc637484a658cbd0b8a43e18631ce37bd1671a8548d204c1f074592ec7f
- SHA256SUMS: manifest of 7 payload SHA256.

## Czyste reprodukcje, faktycznie wykonane
- CLEAN_A with original byte-verified helper — independent exact and numerical main JSON both BYTE IDENTICAL.
- CLEAN_B with original byte-verified helper — independent exact and numerical main JSON both BYTE IDENTICAL.
- CLEAN_C no helper — independent exact JSON BYTE IDENTICAL and all main mathematical fields equal; original source correctly SOURCE_SKIPPED_NO_HELPER.
- Initial full-replay batch attempt timed out; it is not called a PASS. The tests were run as three separate successful clean jobs.
- Initial exploratory main attempted huge N=1025 3D field and was OOM-KILLED. Final verified code uses only SCALAR asymptotic calculations for N>41, full native original source grid up to N31.

STRICT SCIENCE: Odd N>=7, two commuting z-independent e_z shears, constant H=I, E_mode=Identity, full unmasked auxiliary source compute_K_A_out only. E_lin negative control has K_C and K_B nonzero. Full historical dtc0a_runtime_v0_3_1.py and masked production K_A are UNAVAILABLE. No GR gauge/Noether/GW or NCDG J3/K physics; no novelty or EXEC.

PUBLIC report and code are NOT evidence of actual BW ingestion, independent referee, scientific source owner adoption or Moderator EXEC. Status GITHUB_PENDING_BW_INGEST / REFEREE_PENDING / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
