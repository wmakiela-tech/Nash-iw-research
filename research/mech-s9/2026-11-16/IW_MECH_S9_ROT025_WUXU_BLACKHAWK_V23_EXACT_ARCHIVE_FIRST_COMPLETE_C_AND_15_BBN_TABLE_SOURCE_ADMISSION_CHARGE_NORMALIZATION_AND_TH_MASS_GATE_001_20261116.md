---
artifact_id: IW_MECH_S9_ROT025_WUXU_BLACKHAWK_V23_EXACT_ARCHIVE_FIRST_COMPLETE_C_AND_15_BBN_TABLE_SOURCE_ADMISSION_CHARGE_NORMALIZATION_AND_TH_MASS_GATE_001_20261116
created_at: 2026-11-16
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
document_type: ORIGINAL_AUTHOR_PINNED_EXTERNAL_SOURCE_BINARY_SHA_C_SEAM_15_TABLES_READ_ONLY_BOUNDED_AUDIT
claim_ceiling: ORIGINAL_V23_SOURCE_AND_ARCHIVE_IDENTITY_PASS / NOT_IDENTICAL_TO_PROVEN_WUXU_PUBLISHED_FINAL_FIG5_RUNTIME / NOT_COUPLED_N10_BBN / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE
---

# Mech-S9 ROT025 — direct original BlackHawk v2.3 archive readback closes tar-access gate, confirms charge-aggregating source counters and isolates still-unverified Wu–Xu build/data identity

## 0. FIRSTNESS / original and prior source evidence

Scientific original authors: **Alexandre Arbey & Jérémy Auffinger**, creators of BlackHawk, and **Quan-feng Wu & Xun-Jie Xu**, authors of the original PBH–BBN 10D model (JCAP 02 (2026) 063). NO new physics or prior-art priority is claimed for this audit.

Critical IW research precedence, corrected against original records:
- **MT14 ROT021 FIRST** downloaded the actual 161,495,983-byte BlackHawk v2.3 official tar via Wolfram on **2026-11-01** and verified archive SHA `dd148349304c158ed3509ea6935f2fd3d60ebe7cda4c34598aa99ea329c129a7`; his original `ExtractArchive` failed, so NO v2.3 primary C or BBN raw table source bytes were actually read. Original report Git blob `74c3d9132746401e74380693eaf5c70153b52886`, `research/mt14/2026-11-01/iw_mt14_rot021_blackhawk_v23_archive_charge_admission_001.md`.
- **Badacz FIRST** actually executed original Wu–Xu Julia conditional E5/E5b source-charge contour variants on 2026-10-31 (REVIEW038) and subsequent 2026-11-02 seven-row independent PYTHIA8.318.3 charge aggregation T1 (REVIEW044), with ratios near 1 for the AGGREGATE hypothesis. **INT9 ROT033** FIRST restored/replayed their full history independently on Nov15. These already existing native and pilot tests must NOT be labeled as Mech-S9 first or repeated as if untested.
- LT8 ROT025 FIRST located mature dual BBN PYTHIA0/HERWIG1 source support and generator prior-art; LT8 ROT026 FIRST read ten actual raw tables from a MODIFIED SUSY public fork, which was NOT official Wu–Xu v2.3; REC12 ROT005 FIRST independently reviewed those fork data. PRF13 ROT027 FIRST extracted the original 1.675MB producer notebook and related fork signed-PDG evidence; INT9 ROT031, REC12 ROT004 and SCOPE11 ROT009 previously independently reviewed exact Wu–Xu notebook. Mech-S9 ROT023 FIRST authored the bounded *frozen-source RHS* charge-halving conditional metric but not the underlying charge question; ROT024 FIRST added author native 100-energy node overlap 4/1 and 17/100 below-HERWIG branch, FORK only.
- **DISTINCT ROT025 FIRST**: original SHA-identical **official BlackHawk v2.3 archive was actually decompressed and used to read exact 10 C/source files and hash 15 original embedded raw BBN hadron tables** in the project, closing MT14's historic EXTRACT_FAIL. This is ORIGINAL SOURCE/PROVENANCE, not physics novelty or original software authorship.

## 1. Original archive identity verified twice by real standalone source-only GitHub Actions

Wu–Xu original repo `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`, `arXiv-2509.05618/Artifacts.toml` Git blob `324cb54a6d2d1beca970931534345f589eb68c56`, pins `https://blackhawk.hepforge.org/downloader?f=blackhawk_v2.3.tar.bz2`, byte SHA `dd148349304c158ed3509ea6935f2fd3d60ebe7cda4c34598aa99ea329c129a7` and extracted Julia git-tree `80511176a03378517e15b705713256f686ce9016`.

Three observed authenticated source-body events (first two are earlier/own):
1. MT14 FIRST Nov1 source downloaded and SHA PASS, extraction failed (prior owner).
2. Mech-S9 ROT025 Nov16 Wolfram independently redownloaded **161,495,983B** with EXACT pinned SHA PASS. A separate Wolfram retry returned a TRUNCATED 26,936,354B file with different hash and was correctly REJECTED, not accepted as source.
3. **TWO independent ACTUAL Github Actions source-only jobs** redownloaded exact full 161,495,983B via official link and checked the full exact SHA before any file read: stage1 Actions run `43773659154`, stage2 run `43774208631`. Both completed **SUCCESS**, all workflow steps SUCCESS, no BlackHawk compilation, no model execution or Julia run. Each did an original 1,024-byte truncated-archive negative fixture and correctly rejected it before creating any source JSON (PASS).

**Stage1 original official archive authenticated source extraction**: internal original TAR has 365 regular files; selectively read **10 exact source text files** and SHA-hashed **15 original raw hadron tables**. GHA artifact ID `14185446863`, archive ZIP SHA256 `68e9a09306021cf05aba44fcbdb1f325a97e7770316cac581c0a0a50de82efcf`; extracted `ORIGINAL_V23_SOURCE_ONLY_RESULT.json` SHA256 `2698bceb94b75192a29f6c5044da663c25f82136db70170ebdd6f46635ac7ade`. ZIP CRC+3/3 artifact member SHA PASS.

**Stage2 original source seam extraction**: same exact archived TAR, same 10 source and 15 raw table files; additional restricted context around *initial-parton /2 formatting*, original C `hadro_pythia.c` loader and original `secondary.c` convolution. GHA artifact ID `14185204381`, original evidence ZIP SHA256 `d1735c1a4123a7c17340fc18a76c218d532e3cd3a631eefd93106467316f2efc`; `ORIGINAL_V23_SOURCE_ONLY_RESULT.json` SHA256 `f8b2945b87360e186aeeda69c19b2aadce6b05726ac7de98bb9b14f20068e962`. ZIP CRC+3/3 artifact member SHA PASS, all step statuses SUCCESS and truncated-source FAIL_CLOSED PASS. These are actual connected-GitHub downloadable evidence bytes; no assumption from user descriptions.

Actual SHA256 of selected source code FROM exact original official TAR (not merely a related fork):
- `scripts/pythia_scripts/table_up.cc` `262c78fc41eb8440cc123329152eabade64bd0b9b35e80f063185f1c005667b6`;
- `scripts/pythia_scripts/table_gluon.cc` `7f8174652803e1144ffe9499eafdb55b4d8d2f1fb23938438727a8b04fd5b42b`;
- `scripts/pythia_scripts/formatting.c` `0baa942a9acfac2990f1ac03fc4f8eb56273ff8a7f922177368e4c8e6eb1d33e`;
- `scripts/herwig_scripts/MC_PARTICLE_COUNTS.cc` `e2314810c09e2b8fda9fa82651d0be06940bfac6f91fb289d6234ede6f9174ad`;
- `src/hadro_pythia.c` `64bdaa88564f15a615b385a10c17ca5294fe19343e51593a8345951e5e34c62a`;
- `src/secondary.c` `956bc2f0d2224627532ffd81248773cf328ac14ac3d7aed5cf450c950b521f30`;
- `src/tables/hadronization_tables/infos.txt` `bd6d2d2a240b4c8a56cf73e8d4119212f2c5a7e4657a71cd0a7199c566f2ef8c`.

EXACT original archive has 15 target raw tables: five HERWIG BBN, five current `pythia_tables/` and five distinct `pythia_tables/old/`. For example native raw `pythia_tables/pipm.txt` SHA256 `603f8b1a53efe316b4378da9a6242c1a1b3be026c17fbdaa917cb07f13850ac4` versus `pythia_tables/old/pipm.txt` SHA256 `39306be56e4feeeb361c23983e64b7c4f193c60be4ffa7211b745275cad679fa` (NOT equal); `herwig_tables/pipm.txt` `6ad10e894f0e323e33cbc777503b7bc2da902128434eb8912c0ef226eba86246`. The full 15 individual SHA identities are inside the actual validated stage2 JSON artifact, no content dump or false raw table upload.

## 2. SOURCE PROOF: original official BlackHawk has FINAL charge-aggregated counters, and its /2 is PER INITIAL parton

In the actual exact-original-source (not public modified fork) PYTHIA `table_up.cc` and `table_gluon.cc`, original C explicitly increments *one* `pipm` counter for PDG +211 or -211, one `Kpm` for +321 or -321, one `proton` for +2212 or -2212 and one `neutron` for +2112 or -2112. The `K0L` branch uses PDG130, a separate neutral species. **This is verified from the official v2.3 C text SHA, actual fixed official tar.** In original HERWIG `MC_PARTICLE_COUNTS.cc`, id is `abs(p.pdgId())`, and grouping includes PDG211,321,2212,2112; also actual official tar read.

In official exact PYTHIA `formatting.c`, lines 65–77 show the 1/2 divisor INSIDE THE **initial-parton type** loop over `l<nb_initial_particles` (else branch for all except initial Higgs index2); the exception says Higgs is produced without the two-primary-particle normalization. This confirms the 2019 Arbey–Auffinger published methodology per TWO initial partons and **DOES NOT HALVE individual final charge signs**. It would be a mathematical mistake to treat `/2` in this formatter as already dividing pi+,pi− or p,pbar into separate final physical species.

Original official `src/secondary.c` `contribution_instantaneous` sums primary Hawking parton spectra over all source channels into a **selected FINAL table particle_type**, without an additional generic final charge-sign half in the checked core, and official `src/hadro_pythia.c` has a **conditional** `#ifdef HARDTABLES` branch loading `hadronization_tables_pythia.h`. Because this branch is conditional, its presence alone does NOT certify the exact mode of compilation or whether the active precomputed header is equivalent to `pythia_tables/` or `pythia_tables/old/`. The original official binary/raw table payloads are present and SHA-pinned, but not yet replayed through the **specific Wu–Xu producer executable**.

The original Wu–Xu verified author notebook (Git blob `8a10396ae771b17059808fc2b91235dd194cba8d`) sets BBN mode0 PYTHIA for its 100 mass grid (no HERWIG in executed notebook), and writes the five integrated external rates `pipm,Kpm,K0L,proton,neutron` to `hadrons_from_PBH.dat` Git blob `06d0883a27b108692720422294ba2baacd381a64`. In author `main-scan.jl` source blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`, `dN_over_dt_π(m_PBH) n_PBH` goes to BOTH distinct `n_π-` and `n_π+` ODE species at full scalar, while the one group `Kpm` goes only to `K-`, `proton` scalar only to anti-proton, and `neutron` scalar only to anti-neutron. Five source rates are mapped to SIX ODE state species; source row/column order confirmed independently by REC12, KN14, PRF13 and others.

**New stronger but still bounded verdict:** Original upstream BlackHawk v2.3 **source code charge aggregation IS VERIFIED**, unlike the prior solely-fork conjecture. The **per-initial-parton /2** does not automatically perform a FINAL charge-state split. There is therefore a MATERIAL SOURCE-INTERFACE NORMALIZATION RISK if Wu–Xu's actual integrated `pipm`, `Kpm`, `proton`, `neutron` rate scalars inherited those original grouped finals *without further per-final-charge normalization*. This is stronger than the previous generic concern, but still **NOT a certificate of an error in the published Yp/PBH bound**, because exact author generator build, active compiled header/old table selection, full table output normalization, and self-consistent 10D corrected solver numerics have NOT been certified. In a conditional charge-symmetric model, source count for each charged sign would be half the grouped aggregate; without verified equality, only nonnegative 0…group individual bounds hold. No physical uncertainty bars or contour shifts are inferred by simple source arithmetic.

BADACZ prior original Oct31 E5/E5b 12-mass native contours and Nov2 independent original table/PYTHIA8 grouped T1 (all four medians ≈1 under aggregate hypothesis), remain material supporting prior evidence, NOT first discovered by Mech ROT025. They were prior to present exact official archive extraction; their pilot does not prove exact v2.3 binary identity.

## 3. Source support by Hawking temperature: original 100 mass grid, independent Decimal70

Actual original Wu–Xu BlackHawk producer source `valid_hadrons_from_BlackHawk.ipynb` mass table generator: `geomspace(1e9,4e12,100)` grams, distinct from original published 100×100 mass/beta scan. Original `tool_script-parameters.jl` Git blob `0d7198ff3557bdbd5753000bb07a7a7405cc24f5`: `T_BH(m)=NU.M_Pl^2/m`, standard Schwarzschild Hawking temperature. Related-fork BlackHawk dual energy minima (NOW corroborated by exact original v2.3 `infos.txt`): PYTHIA BBN source Emin5 GeV, HERWIG BBN Emin25 GeV, both source Emax100000 GeV; original producer uses a distinct 100-energy geometric grid from5 to100000 GeV.

Independent stdlib Decimal70 implementation using h exact, c exact, e exact, G CODATA6.67430e−11:
- `T_BH(1e9g)=10572.611958...GeV`, `T_BH(j22=1.12117445647e9g)=9429.943660...GeV`, `T_BH(4e12g)=2.6431529895...GeV`;
- `T_BH=25GeV` at `M=4.22904478322322e11g`, `T_BH=5GeV` at `M=2.11452239161161e12g`;
- on original mass table exactly **27/100** source masses have T_BH<=25GeV, and **8/100** T_BH<=5GeV. First zero-based mass grid index with T_BH<=25 is 73, first with <=5 is92.
- `25 GeV / T_BH(j22)=.00265112930683` (0.2651%); near largest 4e12g `25GeV/T_BH=9.4584`, `5GeV/T_BH=1.8917`.
- `17/100` of the Wu–Xu 100 PRIMARY ENERGIES are <HERWIG source table Emin25GeV (Mech ROT024 original result), not the same quantity as 27/100 BlackHawk mass nodes with T_BH<=25GeV. The latter says only source E_min is on/above characteristic thermal scale for many heavier masses; **neither metric quantifies the emitted particle or hadron contribution**. Need actual primary spectrum and kernel, proper generator source support and quadrature for a rate error bar.

Exact new local executed numerical script `mech_s9_rot025_hawking_energy_mass_support.py` SHA256 `73cda0565ae6bcfc5be5b37b36ac81ed0a8f09ec44d25b3148e11b5695c5c792`, JSON SHA256 `c376feb45245c737ae26a3b017c913cfcce0160b0115f78d5addd11cac83b548`. No original official source bytes included in script; source pins and constants exposed; no data provider API call.

## 4. Reproducibility and custody of results

Exact GHA source-only code source at `research/mech-s9/2026-11-16/code/mech_s9_rot025_original_v23_readonly_inspector.py` Git blob `4fb19c069843e56d7f5ad927cfc0292a7277ab4b`, as fetched and read from pinned GitHub. Runs have separate immutable source SHA gates and deliberately truncated negative fixtures PASS; official archive was NEVER shipped to public repo or user as unlicensed original source, and the original generator was never built/run. Stage2 official source artifact ZIP was downloaded directly from GitHub connector and independently inspected in the Moderator conversation: archive CRC PASS, all THREE result content SHA entries PASS, full final JSON directly parsed, 10 source files and 15 table SHA identities verified.

Combined self-contained user-conversation local evidence archive `mech_s9_rot025_original_v23_source_admission_COMPLETE.zip`, SHA256 `99416528eb86ea51d5b19f2928e001a7466ba65a3af043ef61ccb49e6e67f840`, contains BOTH actual original source-only GHA evidence ZIPs, independent Decimal70 source+JSON, README and 5/5 SHA manifest. Outer ZIP CRC PASS, 5/5 payload SHA PASS, BOTH nested evidence ZIP CRC+3/3 SHA PASS, isolated local Decimal70 replay produces **BYTE-IDENTICAL JSON PASS**. No original 161MB raw tar, no copyrighted C/table binary payload shared; original table byte digests and selected bounded source predicates only. Source original Wu–Xu author Pythia notebook/header/build history not yet reproduced as a single reference Figure5 executable identity.

## 5. B1 acceptance and next discriminating gate, not a new experiment request

1. **CLOSED with verified source:** original BlackHawk v2.3 tar availability and SHA, source CPP/C final charge aggregator, two-initial-parton formatter /2, exact selected BBN raw table file hashes, source PYTHIA-HERWIG energy domain minima. Stop claiming original v2.3 source bytes are unavailable or that group semantics is based only on modified public forks.
2. **STILL OPEN:** whether the precise `hadronization_tables_pythia.h` compile-time HARDTABLES branch or underlying direct raw `pythia_tables/old/` vs current version supplied the author Wu–Xu actual 100×5 produced rates; exact normalizations at representative energy/primary species matched to *their* checked-in `hadrons_from_PBH.dat` to numerical tolerance; official published JCAP figure-producing binary/Manifest; self-consistent corrected 10D source-to-six ODE with a recorded per-run Moderator authorization, source-grid beta, event localization and tolerance convergence. These are necessary before a physical BBN/PBH claim. No auto-dispatch of a new Julia or generator run.
3. Source-typed **non-claim**: charge aggregation in original v2.3 C is confirmed, but reinterpreting old published exclusion contours as wrong by ×2 or a numerical `Delta Yp` from frozen-source algebra is NOT authorized. The published original figure-code identity and reference E4 independent hadronization remain open.

**FINAL STATUS**: `ROT025_ORIGINAL_BLACKHAWK_V23_161MB_SHA_AND_ACTUAL_TAR_EXTRACTION_PASS / V23_OFFICIAL_PYTHIA_HERWIG_SIGNED_COUNTER_AND_INITIAL_PARTON_DIV2_SOURCE_PASS / 15_ACTUAL_ORIGINAL_BBN_TABLE_HASHES_PASS / 2_INDEPENDENT_GITHUB_SOURCE_ONLY_ACTIONS_PASS / 27_AND_8_MASS_THERMAL_SUPPORT_NODES_PASS / BADACZ_FIRSTNESS_RESTORED / WUXU_BUILD_SELECTION_AND_FULL_10D_PHYSICAL_EFFECT_HOLD / NO_NEW_JULIA / NO_BLACKHAWK_EXECUTED / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / GITHUB_PENDING_BW_INGEST`.
