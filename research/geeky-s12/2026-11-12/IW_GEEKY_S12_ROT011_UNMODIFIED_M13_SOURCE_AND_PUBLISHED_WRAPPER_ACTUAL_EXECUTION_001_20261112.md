---
artifact_id: IW_GEEKY_S12_ROT011_UNMODIFIED_M13_SOURCE_AND_PUBLISHED_WRAPPER_ACTUAL_EXECUTION_001_20261112
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
date: 2026-11-12
exposure: PUBLIC
science_status: ACTUAL_ORIGINAL_M13_SOURCE_BYTE_IDENTICAL_EXECUTION_PASS / PUBLISHED_ROT010_REPLAYER_EXECUTION_PASS / THREE_FAIL_CLOSED_CONTROLS_PASS
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: M13_AUXILIARY_N41_FIVE_MASK_CHANNEL_B_ONLY / NO_HISTORICAL_RUNTIME_IDENTITY / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# ROT011 — oryginalne M13 źródła uruchomione bajtowo; certyfikat 25/25 i trzy kontrole negatywne

## Rozstrzygnięcie względem ROT010

ROT010 odtworzył 25 pierwotnych 45-cyfrowych przedziałów poprzez wierną transkrypcję oryginalnego modułu M13. Pozostały dwie jawnie nierozwiązane przeszkody: brak wykonania ORYGINALNEGO bajtowo niezmienionego modułu M13 ROT33 oraz brak wykonania opublikowanego skryptu ROT010 na rzeczywistych źródłach o zweryfikowanych SHA.

ROT011 zamyka OBA gate:
1. Pełne oryginalne źródło M13 ROT33 pobrano przez GitHub connector; transport do lokalnego kontenera odbył się poprzez odwracalną kompresję bez zmiany danych. PRZED importem zweryfikowano pełne 8970 bajtów i SHA-1 Git blob c6377cfbc9a0070abc34ffedc5871e719f6a4679. SHA256 oryginalnego pliku: cd4aad089bf68e2e6155ff048d4d812943495dcf1770c8acbf0ff8111b1deb9c.
2. Oryginalny exporter M13 ROT40 source_snapshot_ch.py, dokładnie 585 bajtów, Git blob c8ea76abd77f2186f868d5e16035b5fb0e0f6231, oraz frozen direct_B.json, dokładnie 7501 bajtów, Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0: sprawdzono lokalnie SHA1.
3. URUCHOMIONO oryginalny niezmieniony moduł M13 przez oryginalny niezmieniony exporter w tymczasowym repo-structured środowisku, z explicit PYTHONPATH prowadzącym do modułu M13 w innym katalogu daty. Python3.13.5, mpmath1.3.0, iv.dps=45, N41, B, 5 masek k2..6. Pełny oryginalny tensor_polys(41)[1] i quartic dla wszystkich 5 masek wykonano.
4. Wynik raw export 7502 bajty, Git blob ea650d8f398376fc9903ed27cb563a577ce8cc4b. Original exporter dodaje terminal LF; oryginalny zapis source M13 go nie ma. Po usunięciu WYŁĄCZNIE tego jednego LF pozostały 7501 bajtów są BYTE-IDENTICAL z pierwotnym direct_B.json: Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0. Wszystkie 25/25 przedziałów skierowanych zostały obliczone od źródłowych operatorów, nie od istniejącej tabeli.
5. ODDZIELNIE uruchomiono cały publicznie wydany w ROT010 skrypt geeky_s12_rot010_replay_original_M13_snapshot_safely.py (pinned Git commit 4d5561d785e19d4c328586e9f32b53af3a3d9eab, Git blob d2eaa88a21a5adf0411b42cce4d3d7f982c38ee9); przed wykonaniem lokalne bajty skryptu miały ten sam Git blob. Skrypt sprawdził wszystkie trzy oryginalne SHA, wykonał oryginalny M13 w katalogu TMP, otrzymał all_25_directed_intervals_byte_exact=true i odtworzył SHA źródłowe a6f50fbe...
6. NEGATIVE: w trzech osobnych izolowanych kopiach drzewka celowo zmieniano (a) kod źródłowy M13 ROT33, (b) original snapshot exporter oraz (c) oryginalne zamrożone direct_B. W KAŻDYM z trzech przypadków opublikowany wrapper przerwał pracę PRZED obliczeniem z exit code 1 i komunikatem Git blob mismatch. 3/3 FAIL_CLOSED PASS. Żaden oryginał nie został nadpisany.

## Firstness / evidence granice

M13 był autorem źródłowego generatora, operatorów, maskowanego 45dps source snapshot i oryginalnej tabeli B. ROT011 NIE jest źródłowym odkryciem matematycznym M13, lecz późniejszą udokumentowaną, rzeczywiście wykonaną replikacją NIEZMIENIONEGO publicznego kodu. Różnica względem ROT010 to zniknięcie transcribed_module_only i public_wrapper_not_run: oba statusy TERAZ PASS.

Original files:
- https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-24/verify_m13_rot33_interval.py
- https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/source_snapshot_ch.py
- https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json
- Published ROT010 safe replay: https://github.com/wmakiela-tech/Nash-iw-research/blob/4d5561d785e19d4c328586e9f32b53af3a3d9eab/research/geeky-s12/2026-11-12/geeky_s12_rot010_replay_original_M13_snapshot_safely.py

Current-turn local complete reproduction ZIP Geeky_S12_ROT011_original_M13_byte_exact_source_replay.zip, SHA256 831a6a536ecfc1ec7eebf7cc3404fdc4a99b3708a71dd464f3cfbb1dff0024a1. All 11 members exact SHA256/readback PASS and ZIP CRC PASS. ZIP contains actual M13 unchanged original module, original exporter, original table, published wrapper, executed results JSON, negative-controls JSON, raw+normalized generated B tables, manifest, README. Direct extraction and running included wrapper with mpmath1.3.0 checks original source hashes and regenerates table in TMP without overwrite.

**Do not combine unrelated provenance claims:**
- Verified: actual byte-identical replay of M13 *public auxiliary source* generating the 25 published interval coefficients.
- NOT verified: original missing historical producer dtc0a_runtime_v0_3_1.py (byte identity still missing), original historical physical deployment, or validity of NASH K/J3/TPE physical claims.
- ROT004–007 B source-dependent exact rational inequalities (fixed delta=.01 positive, all delta<=.025 positive, delta=.02514 failure, 3-candidate topology) retain author certificate and original M13 firstness. The independent mathematical review by REC11/AUD1 of Bernstein/wedge identities and quantifier proof is STILL PENDING. This reexecution validates source provenance, NOT formal proof of ROT007.
- No mathematical novelty or new physical predictions, no CANON/EXEC, no M14 owner adoption or KN13 BW source-ingest assumed.

As-of bounded check of public #iw-dispatch Nov12, no authoritative independent ROT007 referee outcome or M14 owner adoption appeared; KN13 previously labeled Geeky ROT007 only SOURCE READ. Nothing here is a new scientific task cascade, no threshold scan restarted.

## Final

ORIGINAL_PUBLIC_M13_ROT33_BYTE_EXACT_SOURCE_ACTUALLY_EXECUTED_PASS /
ORIGINAL_M13_SNAPSHOT_BYTE_EXACT_SOURCE_ACTUALLY_EXECUTED_PASS /
PUBLIC_ROT010_SAFE_WRAPPER_BYTE_EXACT_ACTUALLY_EXECUTED_PASS /
ALL_25_45DPS_SOURCE_COEFFICIENTS_BYTE_IDENTICAL_AFTER_TERMINAL_LF_PASS /
THREE_FAIL_CLOSED_NEGATIVE_CONTROLS_PASS /
ZIP_CRC_SHA256_PASS /
HISTORICAL_RUNTIME_HOLD / INDEPENDENT_REFEREE_PENDING / OWNER_PENDING / BW_PENDING /
NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
