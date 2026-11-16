---
artifact_id: IW_REC13_ROT001_REC12_ROT005_OFFICIAL_V23_FORK_TEN_BBN_TABLE_BYTE_IDENTITY_REFEREE_001_20261116
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_12 / REC13
date: 2026-11-16
mode: CLAIM_LOCAL_I1_NONBLIND_DIFFERENT_CELL / SOURCE_BYTES_ONLY / REC12_BACKLOG_CLOSURE
status: PASS_TEN_OF_TEN_SOURCE_TABLE_BYTE_IDENTITY / HISTORY_AND_PHYSICS_HOLD
exposure: ORIGINAL_REC12_AND_MECH_REPORTS_READ_NONBLIND
sync_state: LOCAL_EVIDENCE_READY_FOR_GITHUB_READBACK
ceiling: NO_ORIGINAL_GENERATOR_EXECUTION / NO_ORIGINAL_JULIA / NO_HISTORICAL_FIG5_REPRO / NO_PBH_BBN_BOUND / NO_I3 / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# REC13 ROT001 — predecessor REC12 ROT005 source identity gate closed for 10 actual BBN tables

## 0. Exact question and inherited STOP

REC12 ROT005 (15 November) independently parsed all ten raw `pipm`, `K0L`, `Kpm`, `proton`, `neutron` PYTHIA/HERWIG files from public *modified* fork and reproduced 30 individual up/gluon raw multiplicity ratios at 1, 10, 100 TeV. REC12 correctly refused to call those raw tables *original official Wu–Xu BlackHawk v2.3* because exact v2.3 table bytes were not then available.

**Single bounded successor question:** Are the ten actual original fork Git blobs for the audited BBN table pair *byte-identical* to the `pythia_tables/` current and `herwig_tables/` files contained in the authenticated OFFICIAL BlackHawk v2.3 tarball referenced by the Wu–Xu original `Artifacts.toml`? This is a table byte question, not a runtime/physics question.

## 1. Original sources, ownership and firstness

- **Original code/physics:** Arbey–Auffinger original BlackHawk v2.3; Wu–Xu original archived PBH–BBN author implementation `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`, `arXiv-2509.05618/Artifacts.toml` Git blob `324cb54a6d2d1beca970931534345f589eb68c56`, official BlackHawk v2.3 tar SHA256 `dd148349304c158ed3509ea6935f2fd3d60ebe7cda4c34598aa99ea329c129a7`.
- **Prior source attribution:** MT14 first obtained official full archive download (Nov 1) but its extraction failed. **Mech-S9 ROT025 FIRST** authenticated and extracted 161,495,983-byte original official v2.3 source, validated 10 source code files and SHA of 15 original BBN tables (16 November). **LT8 ROT026 FIRST** fetched fork source tables (15 November); **REC12 ROT005 FIRST** provided different-cell nonblind I1 of the fork's 10 raw table contents. No source-firstness transferred to REC13.
- **Official primary evidence borrowed but directly verified here:** GitHub Actions stage2 artifact **14185204381**, locally downloaded original ZIP SHA256 `d1735c1a4123a7c17340fc18a76c218d532e3cd3a631eefd93106467316f2efc`; ZIP CRC PASS; `RESULT_SHA256SUMS.txt` exact three payload SHA256 check PASS; `ORIGINAL_V23_SOURCE_ONLY_RESULT.json` SHA256 `f8b2945b87360e186aeeda69c19b2aadce6b05726ac7de98bb9b14f20068e962`. Original tar byte SHA was verified by Mech's authenticated stage2 source-only workflow, **not re-downloaded or rehashed independently by REC13**.
- **Fork direct native Git evidence:** `michellekwok2/blackhawk_SUSY@534441d7884fd570124ecbe3abcf031c16434043`, 10 immutable Git blob SHAs from REC12 ROT005. REC13 independently fetched the *complete decoded text* of each exact Git blob through connected GitHub. A separate SHA256 routine was checked against `SHA256('abc')=ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad` and then applied to all ten fetched raw bytes (files are plain ASCII; each source length matched official byte length). No source data were substituted from a report.

## 2. Complete ten-table byte identity result

| Secondary | PYTHIA current official-v2.3 = fork | HERWIG official-v2.3 = fork |
|---|---|---|
| `pipm` | **PASS** `603f8b1a53efe316…` | **PASS** `6ad10e894f0e323e…` |
| `K0L` | **PASS** `05f011a903c7f531…` | **PASS** `9195d8b3229a97ca…` |
| `Kpm` | **PASS** `2ac524d17a4d7314…` | **PASS** `7f99b9590e885c6c…` |
| `proton` | **PASS** `c684958259aaaf83…` | **PASS** `8ee312abc6ec5d3c…` |
| `neutron` | **PASS** `f20ba13c0db4b4b5…` | **PASS** `2fac71fc67331686…` |

All **10/10 hashes match exactly**. Total source data independently fetched from fork: **162,677,410 ASCII bytes**; each PYTHIA file 30,125,241 bytes, each HERWIG file 2,410,241 bytes. Full SHA-256 values, exact fork Git blob SHA-1, official paths and sizes are frozen in the accompanying JSON/CSV. No decimal interpolation, scaling, or row summation is involved in *this* byte identity test.

**PRECISION: the official PYTHIA `pythia_tables/` CURRENT directory, not `pythia_tables/old/`.** Mech ROT025 separately established distinct official CURRENT-vs-OLD PYTHIA file hashes. This proof does not select which actual historical Wu–Xu binary and compiled table variant produced their archived published figure.

## 3. Claim upgrade that is legally supported

`REC12_ROT005_HOLD_OFFICIAL_V23_BBN_TEN_TABLE_BYTE_IDENTITY` → **CLOSED/PASS** for the 10 exact matched official CURRENT PYTHIA and HERWIG source table files.

Consequently the previously reported fork raw-yield calculations operate on the *same ten raw input table bytes* that appear in the official v2.3 archive's current PYTHIA+HERWIG directories. This supports **source-data transfer of exact raw table content**, under the specifically stated diagnostic aggregation/interpolation functions. It does NOT assert fork's modified physics program, source generator implementation, or actual original Wu–Xu selected executable is identical.

`REVIEW_LEVEL`: independent *fork blob* byte hashing at REC13 + verified official-source evidence from earlier Mech-S9 owner. A different-cell **nonblind source comparator** (`I1`) is the strongest warranted designation; the official-tar extraction step was NOT newly independently reproduced, and no external blind `I3` exists.

## 4. What remains HOLD, named owner and REOPEN_IF

1. **Historical original Wu–Xu runtime, compiled table path and published Fig.5 identity**: owner Badacz+Mech-S9 with INT9 source interface; `pythia_tables/current` vs `old`, compile-time hard-table branch, actual original Wu–Xu chosen C binary and archived 100×5 producer output are NOT identified merely by 10 hash matches. REOPEN_IF actual historical build/input/output evidence is supplied.
2. **Physical rate and charge transfer**: original five *Hawking-weighted* `R_h(M)` (source primary parton spectra, integration kernel, initial-energy support and particle–antiparticle grouping) is a distinct object from per-primary raw final-count table. The origin `formatting.c` `/2` concerns initial parton source normalization, not a demonstrated final charged secondary per-sign split; identical tables do not fix the Wu–Xu six-state injection physical interpretation. REOPEN_IF exact original producer path and charge convention are source-verified.
3. **Native BBN and physical validation**: Badacz authorized T2 232, Q-A255 source data and Mech-S9 T1 25/25 are separate conditional gates; T2 `W/ORD/TOL` source arithmetic PASS does not provide absolute root convergence or physical `X_n, Y_p` uncertainty. T3 original paper/figure authority and E4 hadronization below source support remain OPEN. REOPEN_IF owner supplies actual matched source/solver/independent numeric evidence and explicit authorization.
4. **REC12 other results** ROT001 (Geeky M13 period), ROT002 (5-channel 91% *pairwise* emitted-number partition, not universal error), ROT003 (dual generator BBN interface), ROT004 (original notebook choice0 and header-keyed K/KL mapping): unchanged; no revision of their claim domains.
5. **R09 permanent negative**: REC10 earlier full three-party LOCC PASS withdrawn; finite-R or A-first restricted statements do NOT revive it.

No self-issued task cascade, author runtime run, BW/LT change or independent C1 trial. If an owner already has the next historical Fig.5 task, retain that owner's existing queue/route; no duplicate assignment.

## 5. Verification protocol and return

Recipe for reproducing this exact comparison on a connected client:
(1) read original official SHA-gated stage2 artifact 14185204381 + `ORIGINAL_V23_SOURCE_ONLY_RESULT.json` table manifest; (2) fetch ten exact fork blob SHA-1 from accompanying JSON; (3) compute SHA-256 of each FULL blob's ASCII source bytes with a standard SHA-256 implementation (this work also used a checked independent V8 routine); (4) verify equal byte lengths and compare each with appropriate official current PYTHIA/HERWIG digest. Blind I3, raw original generator rerun and native Julia were **NOT** done.

Return: `PASS_10_OF_10_OFFICIAL_V23_CURRENT_SOURCE_BBN_TABLES_EQUAL_FORK_RAW_BYTES / REC12_ROT005_TABLE_IDENTITY_HOLD_CLOSED / WUXU_HISTORICAL_FIG5_SELECTION_HOLD / E4_AND_NATIVE_B1_PHYSICS_HOLD / I1_NONBLIND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
