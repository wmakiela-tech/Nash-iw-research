---
artifact_id: IW_GEEKY_S12_ROT010_FULL_45DIGIT_SOURCE_INTERVAL_REGEN_AND_CANONICAL_BLOB_GATE_001_20261112
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
created_at: 2026-11-12
exposure: PUBLIC
science_status: AUTHOR_ACTUAL_MPMATH_IV_SOURCE_REGEN_FULL_25_CANONICAL_GIT_BLOB_PASS / INDEPENDENT_REFEREE_PENDING / M14_ADOPTION_PENDING
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: M13_AUXILIARY_N41_FIVE_MASK_B_ONLY / HISTORIC_PRODUCER_MISSING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT010 — pełna 45-cyfrowa regeneracja 25 przedziałów B z identycznością Git blob

## A. Nowy wynik i jego precyzyjny status

Rzeczywiście przeprowadzono lokalną regenerację źródłowych 25 współczynników przedziałowych kwartycznych kanału B M13, N=41, maski k=2,..,6. Zrekonstruowany generator nie wczytuje oryginalnych współczynników jako danych; oblicza je od oryginalnej definicji C1, C2, h, E_lin, centralnego stencilu2, tensor Lie/bracket i płaskiej projekcji Fourier-TT. Dla każdego k regeneruje pełne pięć współczynników kwartycznych za pomocą skończonych modalnych sum iloczynów maskowanych w mpmath.iv przy 45 cyfrach dziesiętnych.

Original M13 direct_B.json Git blob: a6f50fbe5904e580e84c87ee87c5ad043cdec5d0, bajtów 7501.
Staged regenerated JSON with newline: Git blob ea650d8f398376fc9903ed27cb563a577ce8cc4b, bajtów 7502.
Staged generated JSON AFTER removing the terminal LF: Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0, bajtów 7501.

Ta jedyna różnica wynika z oryginalnego snapshot exportera M13, który na końcu zapisuje dodatkowy LF, podczas gdy opublikowany GitHub source direct_B.json kończy się znakiem '}', bez LF. 25 par przedziałowych mają identyczne teksty (weryfikacja 25/25 FNV per pair), a dokładne 7501 bajtów ma ten sam Git SHA1 blob co oryginał. Nie jest to tylko zgodność Float64; to pełna zgodność źródłowych interwałów zapisanych jako dziesiętne końce.

Test ACTUALLY RUN: Python3.13.5, mpmath1.3.0, iv.dps45, N41, pięć masek, 25 coeff, 41 mode keys for each U,V,W, około 7,15 sekund na pełną rekonstrukcję. Nie wykonywano skanów delta, nowego geometrycznego modelu ani fizycznych symulacji. Wcześniejsze ROT008/009 dawały niezależne testy Float64, obecnie luka regeneracji źródłowych 45-cyfrowych coefficient enclosures jest domknięta w zakresie wiernie transkrybowanego producenta pomocniczego.

## B. Dokładna podstawa i granica pierwszeństwa

M13 FIRST: rekonstrukcja funkcjonalnie dopasowanego pomocniczego producenta DTC0a, 99/99 historycznych RMS, 45-cyfrowa formuła źródłowych przedziałów i zapis direct_B; późniejsze M13 ROT35 shell covariance, ROT39/40 geometria najbliższych alternatyw, A/C radial. ROT010 nie jest odkryciem nowej formuły lub źródłowym first wykonania M13; jest osobnym weryfikowalnym REPLAY z pełnym bitowym testem wyjścia, rozstrzygającym wcześniejszą lukę reprodukowalności.

Source of truth (public originals):
- M13 ROT33 module research/m13/2026-10-24/verify_m13_rot33_interval.py, Git blob c6377cfbc9a0070abc34ffedc5871e719f6a4679.
- M13 ROT40 exporter research/m13/2026-10-26/source_snapshot_ch.py, Git blob c8ea76abd77f2186f868d5e16035b5fb0e0f6231.
- M13 original data research/m13/2026-10-26/direct_B.json, Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0.

Source links:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-24/verify_m13_rot33_interval.py
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/source_snapshot_ch.py
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json

LIMIT: No direct container network to download actual 8968-byte M13 ROT33 module. Instead source formulas were transcribed to a local independently authored Python file preserving computation order. This transcribed 7404-byte file is NOT byte-identical to original ROT33 code. The small M13 snapshot script was also copied manually, its canonical bytes identified with M13 exact source Git blob c8ea76... after removing only an appended local LF, and it was actually executed with the staged, functionally matching transcribed module through PYTHONPATH. This reproduction yielded the SAME canonical Git blob a6f50... . Thus original source output is REPRODUCED EXACTLY, but an unchanged ORIGINAL M13 ROT33 module has not been separately run byte-identically in the local container.

## C. Repair of ROT008 source import path

Original exporter source_snapshot_ch.py lives in 2026-10-26 and imports verify_m13_rot33_interval.py from an entirely separate 2026-10-24 directory. Under default Python path, direct invocation needs explicit PYTHONPATH. This rotation actually executed a staged copy with corrected PYTHONPATH and confirmed full output equality, without overwriting frozen original direct_B.json.

NEW PUBLIC SAFE STAGED WRAPPER for a checked-out repo performs fail-closed original 3 blob identity prechecks, copies original exporter into a temporary directory, fixes PYTHONPATH, executes UNCHANGED original M13 module and exporter, removes only trailing LF and compares canonical bytes to the M13 original file:
https://github.com/wmakiela-tech/Nash-iw-research/blob/4d5561d785e19d4c328586e9f32b53af3a3d9eab/research/geeky-s12/2026-11-12/geeky_s12_rot010_replay_original_M13_snapshot_safely.py

This standalone public wrapper was committed and read back exactly (Git blob d2eaa88a21a5adf0411b42cce4d3d7f982c38ee9). It was NOT itself executed from an actual full cloned repo in this rotation; the SOURCE ALGORITHM recreation and the original snapshot script with staged transcribed module DID run. Do not misstate the wrapper publication as its complete reexecution.

## D. Reproducible package and hashes

A local ZIP in the user conversation contains:
- actually executed faithful transcription of ROT33 sparse interval generator (7404 bytes),
- canonical 7501B regenerated direct_B source table,
- machine manifest including expected, raw, and canonical Git blobs,
- independent README of execution and limitations.

ZIP SHA256 57842de5dfb8a73f0987afbe3a3670aeaa694ed388718978855991f6d2be044f; ZIP CRC and all four member byte-replay comparisons PASS.

Script SHA256 dcb3e67db8886a1ad4cb9567ef46aca729a5c2543096153e659758ba6e7933a9.
Canonical regenerated source SHA256 0295116e364e28e67f0129bda1fc298d6e4bfdcb7aa8a6314f02a9ea37edca5f.

Full machine-readable regenerated source and execution certificate published in GitHub:
https://github.com/wmakiela-tech/Nash-iw-research/blob/776379ee6e46eaca07ab5be86cf5a9d6b7e2ae01/research/geeky-s12/2026-11-12/IW_GEEKY_S12_ROT010_M13_DIRECT_B_SOURCE_INTERVAL_REGEN_CERTIFICATE_001_20261112.json

## E. Impact, limits, next gate

This strengthens the source-origin validity of all earlier SOURCE-CONDITIONAL B statements, WITHOUT replacing their independently needed mathematical referee:
- ROT004 B ALL-delta nearest-only FALSE for delta=.035.
- ROT005 B fixed .01 nearest-only TRUE.
- ROT006 B all 0<delta<=.020 nearest-only TRUE and example FAIL .026.
- ROT007 B all 0<delta<=.025 nearest-only TRUE, example FAIL .02514, and reduction to at most THREE candidates among beta in {0, alpha-delta, alpha+delta}.
The downstream exact rational interval Bernstein/wedge code and its conclusions have NOT been newly independently referee-accepted by this source reconstruction; M13's original source remains first. Numeric helper alignment ROT009 remains distinct corroboration.

NO claim that original historical dtc0a_runtime_v0_3_1.py was recovered. NO confirmation of historic physical K/J3/TPE model, source operator outside functional auxiliary family, physical effects or mathematical novelty. No transfer to other N, masks, TT fields, covariance or empirical data. Validity of directed computations still relies on assumptions of mpmath.iv outward rounding and source formulas.

As checked in #iw-dispatch on 12XI, no independent REC11/AUD1 ROT007 endorsement or M14 formal owner adoption was found; KN13 earlier recognized ROT007 source-read only. BW custody remains pending. PUBLIC GitHub artifacts are evidence of publication, NOT owner or referee acceptance.

FINAL: SOURCE_B_FULL_25_45DPS_CANONICAL_EXACT_GIT_BLOB_PASS / REPRODUCER_DEPENDENCY_PATH_REPAIRED_BY_STAGING / HISTORIC_RUNTIME_NOT_FOUND / OWNER_PENDING / REFEREE_PENDING / BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
