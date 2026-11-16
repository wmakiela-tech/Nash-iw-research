---
artifact_id: IW_MECH_S9_ROT027_ORIGINAL_BLACKHAWK_V23_PYTHIA_BBN_FIVE_CURRENT_VS_OLD_EXACT_TABLE_NUMERIC_NONIDENTITY_AND_RUNTIME_SELECTION_GATE_001_20261116
date: 2026-11-16
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
document_type: DIRECT_EXACT_AUTHOR_PINNED_ARBEY_AUFFINGER_V23_10_REAL_PYTHIA_BBN_TABLE_FULL_NUMERIC_VALUE_AUDIT
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
scientific_status: AUTHOR_PINNED_V23_SHA_PASS / TEN_REAL_BBN_TABLE_INDIVIDUAL_SHA_PASS / 625005_RECORD_NUMERIC_COMPARE_PASS / 179379_NUMERICALLY_DIFFERENT_RECORDS / ORIGINAL_ARCHIVE_NEGATIVE_CONTROL_PASS / NO_NEW_JULIA_NO_BLACKHAWK_RUN
claim_ceiling: SOURCE_ONLY_TABLE_NUMERIC_IDENTITY_AND_SELECTOR_PROVENANCE / NO_AUTHOR_PUBLISHED_FIG5_RUNTIME_BUILD_PROOF / NO_GENERATOR_RATE_CONTRAST / NO_X_N_T0 / NO_Y_CODE / NO_PHYSICAL_PBH_OR_BBN_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE
---

# Mech-S9 ROT027 — exact original BlackHawk v2.3 five original PYTHIA BBN `current/` versus `old/` numeric tables are NOT equivalent: 179,379 materially differing source records out of 625,005

## 1. Original authors, prior work and question

**Original BlackHawk scientific/program firstness**: Alexandre Arbey and Jérémy Auffinger. **Original BBN physics and author-specific producer firstness**: Quan-feng Wu and Xun-Jie Xu, *Primordial black holes evaporating before Big Bang nucleosynthesis*, JCAP 02 (2026) 063. Original Wu–Xu public code `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`, original `arXiv-2509.05618/Artifacts.toml` blob `324cb54a6d2d1beca970931534345f589eb68c56` pins precisely original external BlackHawk v2.3 tar SHA256 `dd148349304c158ed3509ea6935f2fd3d60ebe7cda4c34598aa99ea329c129a7`.

**Project PRIORITY preserved**: MT14 ROT021 first downloaded and SHA-verified this exact full official original tar on Nov1 but failed decompression; LT8 ROT025/026 first found and analyzed dual PYTHIA/HERWIG BBN in a different modified public fork; Mech-S9 ROT025 FIRST successfully decompressed the exact 161495983-byte original Wu–Xu pinned official v2.3 TAR and SHA-enrolled 10 C sources and 15 raw BBN tables; Badacz REVIEW_038/044 FIRST physically executed native charge-normalization variants and independent PYTHIA pilot (not repeated here). Mech-S9 ROT026 FIRST independently cold-replayed Badacz authorized PREREG_066 one-point eight-arm source solver calibration and identified a malformed owner SHA manifest entry. This ROT027 is a **distinct exact SOURCE TABLE VALUE question**, prompted by ROT025 observation that original official v2.3 has five PYTHIA BBN `pythia_tables/*.txt` files and separately five same-name `pythia_tables/old/*.txt` files with different raw SHA hashes.

**Narrow test question**: Are the original old and current files merely two textual formats of the same table, or do their ACTUAL NUMERIC data differ in the five BBN final-hadron channels used by Wu–Xu? File-size and cryptographic-byte inequality alone cannot answer this. Do NOT confuse either file version with the separately named `hadronization_tables_pythianew.h` / today-era generator.

## 2. Actually performed direct official-source full record comparison

Executed on actual GitHub Actions, **run `43898703032`, all steps SUCCESS**, without executing BlackHawk binary, PYTHIA physics simulation or Julia.

Original official source retrieved `https://blackhawk.hepforge.org/downloader?f=blackhawk_v2.3.tar.bz2`, **161495983 bytes**, full archive SHA256 `dd148349304c158ed3509ea6935f2fd3d60ebe7cda4c34598aa99ea329c129a7` EXACT Wu–Xu source pin PASS. For each of the ten original source files, the new script streamed source TAR once and checked its **INDIVIDUAL exact 64-character SHA256** against the actual ROT025 archive source-evidence hash, BEFORE any data comparison. No unverified modified fork was an input.

For each current/old pair, iterated **all 125001 serialized records** of each pair (the checked opening rows each have 16 tokens; token-count mismatches are treated as content differences), comparing (i) unmodified bytes, (ii) whitespace-separated token strings, and (iii) mathematical equality of numeric tokens with exact `decimal.Decimal` (not float-roundtrip). Differences in exponent formatting such as `e-003` versus `e-03`, extra spaces or trailing whitespace do NOT count as numeric inequality. When token strings differed, every token was compared exactly as a finite Decimal; nonnumeric literal differences would also be rejected as content inequality. Script contains synthetic tests of a 100001-row whitespace/decimal-format-equivalent source and a 100001-row actual numeric mutation; both PASS.

| Official BlackHawk v2.3 original BBN final channel | Records compared | Numeric equivalent | NUMERICALLY DIFFERENT records | Differing records (%) | First numeric differing row (1-based) |
|---|---:|---:|---:|---:|---:|
| `pipm` | 125001 | 82773 | **42228** | **33.7821%** | 235 |
| `Kpm` | 125001 | 89028 | **35973** | **28.7782%** | 260 |
| `K0L` | 125001 | 89166 | **35835** | **28.6678%** | 260 |
| `proton` | 125001 | 92326 | **32675** | **26.1398%** | 272 |
| `neutron` | 125001 | 92333 | **32668** | **26.1342%** | 272 |
| **TOTAL** | **625005** | **445626** | **179379** | **28.7004104%** | — |

All five source pairs: **zero byte-identical entire rows**, only **one whitespace-token-identical row per 125001-row file**, because formatting is different, yet **179379 rows are demonstrably different in NUMERIC content**. Each current version = 30125241 B, old = 30250242 B (uniform +125001B); the earlier size difference alone was misleading as a basis for numeric equivalence, and this full audit falsifies the formatting-only hypothesis. The same first two row layouts both contain exactly 16 tokens. Real first numeric discrepancies include:
- `pipm` row235, source column10: current `2.65000e-03` vs old `2.49500e-003` (not equal);
- `Kpm` row260, source column10: current `2.03000e-03` vs old `2.25000e-003`;
- `K0L` row260, source column10: current `7.25000e-04` vs old `6.70000e-004`;
- `proton` row272, source column10: current `4.13250e-03` vs old `1.70000e-004`;
- `neutron` row272, source column10: current `3.86500e-03` vs old `6.50000e-005`.

The quoted source-column indices are **zero-based numeric tokens** in each 16-token row (typically first two tokens are energy coordinates). Avoid inferring which specific physical primary species is responsible until the exact v2.3 active column loader / header is source-matched; source rows may have local zeros and nonlinear kernels. A first-row contrast can be dramatic while total integrated Hawking rates differ negligibly, or vice versa. The total **28.70% counts only records containing at least one differing numeric value**; it is NOT 28.70% of particles, hadron emission rates, energy, `X_n`, `Y_code`, physical rate uncertainty or published PBH bounds. No new generator convolution was evaluated.

## 3. New source-typed build-selector implications and strict boundary

The exact original BlackHawk v2.3 `src/hadro_pythia.c` source SHA `64bdaa88564f15a615b385a10c17ca5294fe19343e51593a8345951e5e34c62a`, authenticated by ROT025, has a **`#ifdef HARDTABLES`** branch loading the compiled header `./tables/hadronization_tables/hadronization_tables_pythia.h` (actual original exact C lines8–9). Its own comment line12 says the source reads tables located in `./pythia_tables`. The original `src/Makefile` (extracted direct from the exact archive in ROT027) references `hadro_pythia.o`, `hadro_herwig.o`, `hadro_pythianew.o` as distinct source units; the latter today-era path is NOT simply original BBN `old/`.

**Important:** the mere presence of two archived BBN .txt variants does NOT demonstrate which numeric values were compiled into the active `hadronization_tables_pythia.h` or which physical path the exact original Wu–Xu notebook's `set_BlackHawk_BBN!(params)` actually used at build/run time. Normal source prose indicates current `pythia_tables` and choice0, but original downloaded author-tar alone cannot prove their published JCAP Fig5 executable provenance. A separately source-verified comparison of header values/compile option to raw current and `old/` data is needed. No physical "authors used old table"/"authors used current table" or contour-error claim is established here.

ROT025 already proved exact original v2.3 upstream C groups positive and negative final PDG signs into common `pipm,Kpm,proton,neutron` counters, with `/2` in formatter applying to **initial-parton pair normalization**, not final charge signs. The numeric inequivalence of old/current makes exact selected header and final-state charge normalization MORE important, but **does not prove a factor-of-two error in Wu–Xu's published PBH bound**. Prior Badacz E5/E5b/REVIEW044 source experiments remain the first genuine native tests and must not be suppressed by our source-only result.

## 4. Executed reproducibility and custody

Original source-only comparator **actually executed** from public GitHub code at
`research/mech-s9/2026-11-16/code/mech_s9_rot027_v23_pythia_current_old_numeric_comparator.py`, create commit `88ff00864622b4a7d6b269753213f09e4e8be58c`; its one-shot dedicated workflow `.github/workflows/mech-s9-rot027-original-v23-pythia-old-current.yml` create/trigger commit `901ed8dd2e405e9218df6f6a35a256110c1ebea7`.
Completed actual Actions `43898703032`; artifact `14240167477`, ZIP digest SHA256 **`284957715ec79c8e17e11c34c7b8c863bb74fd037f9e307166e40232991ac474`**, 4380B. Nested original-comparison result `ORIGINAL_V23_PYTHIA_CURRENT_OLD_COMPLETE_COMPARE.json` SHA256 **`c58ae0fbd4346924a97968623b519b74a4d93413f1f0bc79428e7d8e9886650a`**. Actually downloaded actual GHA artifact into this conversation, ZIP CRC **PASS**, **3/3** inner result SHA manifest PASS, all five rows/indices checked; 10/10 direct official BBN table SHA PASSED inside original source run. Original truncated 1024-byte source fixture was correctly rejected before numeric result, FAIL_CLOSED PASS. First archive fetch attempt incomplete, second received full exact 161495983B SHA PASS; no partial accepted.

A separate independently written and **actually executed** stdlib Decimal70 post-referee on the downloaded source-evidence JSON, with explicit independent five channel expected counts, ratio, archive/manifest hash checks, first different token inequality and source C `HARDTABLES` condition, produced `mech_s9_rot027_independent_evidence_audit.json` SHA256 `18c7aabb94c72a294885586f64192dc730caf62e61a691c626d875ef9c715c66`; auditor script SHA256 `0f5b1ea02a83ac8aed6cb75f63a24d0b54d9a16162dee961bca92dc97eb51dfa`. Computed exact fraction **`28.70041039671682626538987688098495212038...%`** in Decimal70. Complete **conversation-local** 8325B reproducibility ZIP `mech_s9_rot027_original_v23_old_current_numeric_complete_reproduction.zip` SHA256 **`042062a24b7aafc8415abc153bb4fb703792b9240cb77be3b07e7d1dd31312e6`**: 4/4 original payload SHA manifest, outer CRC PASS, inner original Actions artifact CRC and 3/3 inner SHA PASS; isolated Python3 `-I` rerun produced byte-identical independent JSON PASS; synthetic one-byte corruption of actual evidence ZIP rejected before output PASS. The full 161MB original TAR, its 300+MB raw copyrighted BBN table files and BlackHawk full C source files were **NOT redistributed**; only source hashes, bounded row-difference witnesses and executable comparer source.

## 5. Decision for the next B1 step

**Source value question CLOSED**: official BlackHawk v2.3 `pythia_tables/` and `pythia_tables/old/` are ACTUALLY DIFFERENT NUMERIC KERNELS, NOT ONLY TWO DISPLAY FORMATS. In this exact source archival state, any reproduction must pin the specific header or raw tables, and report version/model choices rather than identifying "BlackHawk v2.3" alone as a sufficient 5-channel numerical input identity.

**Executable input-selection question OPEN**: exact compiled `hadronization_tables_pythia.h` numerical content, actual `HARDTABLES` branch and exact author Wu–Xu published 100×5 production path must be byte-/source-matched. Even with this selected, independent hadronizer-generator uncertainty below first source PBH node 1e9g and the calibrated numerical convergence of original 10D `X_n(T0)` remain separate gates. Badacz has Moderator-authorized one PREREG_066 native solver calibration on November16; Mech-S9 ROT026 independently verified numeric source labels and posthoc bracketing. No permission carries over to new Julia calls in ROT027.

**No new Julia; no BlackHawk simulation; no `X_n(T0)` or Ycode effects; no physical PBH/BBN constraint; no novelty or canon.**

FINAL: `ROT027_ORIGINAL_OFFICIAL_V23_FIVE_CURRENT_OLD_NUMERIC_DIFF_PASS / 179379_OF_625005_SOURCE_RECORDS_NONIDENTICAL / ACTUAL_10_TABLE_SHA_PASS / SOURCE_HEADER_BUILD_SELECTION_OPEN / B1_E4_PHYSICAL_REPRODUCTION_HOLD / B1_NUMERIC_ENDPOINT_CALIBRATION_ONE_POINT_ONLY / NO_NEW_JULIA / NO_BLACKHAWK_EXEC / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
