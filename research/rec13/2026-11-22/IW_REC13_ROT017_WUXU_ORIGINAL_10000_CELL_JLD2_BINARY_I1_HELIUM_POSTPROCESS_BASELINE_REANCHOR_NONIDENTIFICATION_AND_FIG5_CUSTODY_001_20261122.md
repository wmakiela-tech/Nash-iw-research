---
artifact_id: IW_REC13_ROT017_WUXU_ORIGINAL_10000_CELL_JLD2_BINARY_I1_HELIUM_POSTPROCESS_BASELINE_REANCHOR_NONIDENTIFICATION_AND_FIG5_CUSTODY_001_20261122
date: 2026-11-22
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_12 / REC13
exposure: PUBLIC
mode: ORIGINAL_AUTHOR_BINARY_SOURCE_DIRECT_READ / INDEPENDENT_100x100_HDF5_WOLFRAM_RECOMPUTATION / STRICT_SHA256_AND_CHI2_GATES / POSTPROCESSOR_ONLY_COUNTERFACTUALS / TWO_EXPLICIT_BASELINE_REANCHOR_FALSIFIERS / SCIENCE_FIRST_NONBLIND
firstness: EKS1_ROT016_FIRST_78_WUXU_ROOTS_AND_GAP006_CARR_G0_FAIL / REC13_ROT016_FIRST_THREE_WAY_V1V2V3_Yp_SOURCE_CONTRACT / REC13_ROT017_FIRST_IN_THIS_LINEAGE_EXACT_NATIVE_ORIGINAL_BINARY_JLD2_AND_10000_CELL_THREE_BASELINE_CONVENTION_REFEREE_RECOMPUTATION
status: EXACT_AUTHOR_JLD2_SHA256_PASS / NATIVE_SOURCE_100X100_HDF5_I1_PASS / SOURCE_78_OLD_ROOTS_REPRODUCED / CONDITIONAL_V3_73_ROOTS_AND_J62_PLUS_0P83369 / PHYSICAL_REBASE_NONIDENTIFIED / G0_PUBLICATION_LINK_NOT_CLEARED / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_I3
custody: GITHUB_PENDING_BW_INGEST
ceiling: REAL_RAW_AUTHENTIC_SOURCE_FILE_READ_AND_SOURCE_NUMERICS_PASS / ACTUAL_JLD2_PRODUCER_BINARY_NOT_LINKED_TO_GITHUB_MAINSCAN_EXEC_HISTORY / NOTE_V3_PAPER_CLAIMS_NETWORK_CROSSCHECK_NOT_REPRODUCED / NO_FIG5_IDENTICAL_PLOT_HASH / NO_ACTUAL_PHYSICAL_PBH_LIMIT / NO_GENERAL_LITERATURE_ENVELOPE_SIGNOFF / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# REC13 ROT017 — actual Wu–Xu original JLD2 read, 10,000 source-cell independent helium observable reprocessing, and constructive baseline non-identification

## 0. Why this was the necessary next I1; rigor and negative firstness

REC13 ROT016 identified an important **three-way discrepancy** under the *same declared neutron fraction* `X_n=n_n/(n_n+n_p)`: arXiv 2509.05618 **v1/v2** Eq(5.1) `2X_n/(1-2X_n)`; the public author Julia `main-scan.jl` (and its v1 retained source) `2X_n/(1-X_n)`; the peer-reviewed/public **v3** Eq(5.1) `2X_n`. EKS1 ROT016 was FIRST to compute the archived comparison of Wu–Xu's own contour with Carr/Keith/Kohri published digitizations and to identify G0 FAIL: no Carr2020-winning exception in the author archived curves. **REC13 ROT016 had then NOT independently opened the binary 100×100 JLD2** and explicitly placed source-to-archive contract under HOLD. ROT017 removes THAT narrower data-access limitation by opening the real author 151,089-byte original JLD2 byte array and recomputing the entire scan with a different mathematical runtime (Wolfram Language v15), not copying 78 roots from EKS1. The original research source and archived values are Wu–Xu's, first archival contour root replay is EKS1's; this ROT017 contributes the fully independent native-binary source test and explicit baseline-nonidentification falsifiers.

Primary publication, directly read full HTML, not a potentially stale review:
- Quan-feng Wu and Xun-Jie Xu, *Primordial Black Holes Evaporating before Big Bang Nucleosynthesis*, JCAP 02(2026)063, DOI `10.1088/1475-7516/2026/02/063`, preprint `https://arxiv.org/html/2509.05618v3` (6 May 2026), Sec 2.1 Eq(2.4) `X_n=n_n/(n_n+n_p)`, Sec 5 Eq(5.1) `Y_P≈2X_n`, Eq(5.2) `β'=√γ*[g*(T_i)/106.75]^(-1/4)*(h/.67)^(-2)*β`; v3 explicitly says `Y_P=.245±.003`, 2σ upper `.251`, and its *separate BBN-simple nuclear network check* agrees closely with its approximation. **That claimed native network cross-check is NOT replicated in this report.** Paper Fig.5 is not authenticated here as the exact public repo `plots/Y_P.png` asset, although REC13 opened that public image separately for limited visual source context.
- Earlier v1/v2 author publication Eq5.1 gave `2X/(1-2X)` despite declaring X to be neutron fraction; author current scan code `2X/(1-X)` was directly read and confirmed in REC13 ROT016.

Original **AUTHOR GITHUB** snapshot, commit `d395183674cace6c9906a8911bdeb7234ba4040d` (independent of NASH project):
- EXACT `arXiv-2509.05618/data/out/scanning.jld2`: original Git SHA1 blob `10cc9b3f078fcadb91b5e520e75845859ca00b74`, directly fetched entire binary in base64 via connected GitHub source, decoded as original HDF5/JLD2 (Julia runtime header 1.12.3; HDF5 signature at byte offset 512), **151,089 bytes**; independently Wolfram `Hash[BaseDecode[...],"SHA256","HexString"]` gives `51844a46ca904f57f941e0d0ebc3b5920c38bace76eea9e1d89cb5fd1f2c5786`. THIS EXACTLY MATCHES THE FULL SHA-256 EARLIER LOGGED BY EKS1 in ROT016! This is independent binary identity and resolves ROT016's direct-file access HOLD, not the source-program/executed-runtime lineage problem.
- EXACT author public `arXiv-2509.05618/main-scan.jl`: original Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`, line210 computes `2*X_nuc/(1-X_nuc)`, lines 243–249 write `Y_P_mat` and `chi2_mat=((Y_P_mat-.245)/.003)^2`. The source output array operator can be reconstructed conditional on this source being the actual binary producer; merely sharing a repo path does NOT establish production lineage.
- ORIGINAL separate *v1 archival JLD2* `arXiv-2509.05618/arXiv-2509.05618v1/data/out/scanning.jld2` SHA1 `ff08072449c4ef46144cb800778224acd9669a8f`, Wolfram computed SHA256 `7f8ebe6c6c7b380f20c725908d900c5508bb4f16519a7f17e10955a55e78ecf1`, 149,272 bytes (Julia 1.11.6). Direct independent HDF5 import shows 100×100, *exact same mass and β node grids* as current author snapshot, but different Y data: maximum absolute 10,000-cell difference `1.03484782797849`, mean absolute `0.08457321190599984`. These differences also include changed hadron/nucleon physics and code revisions; **NOT attributable causally to Eq5.1 revision alone**. Distinct archives verified, no conflation of “archive” with one unique time-invariant data state.
- Author source plot `arXiv-2509.05618/plots/Y_P.png`, direct image original Git blob `3b8bb8438660da9c1fb84a383b22dd1a6878a7b0`, actually visually inspected as source; paper v3 HTML references Fig.5. No assertion of byte identity between printed v3 figure and this repo graphic without a source asset match.

## 1. Direct independent ORIGINAL binary I1 — no EKS1 extracted original rows relied upon

Wolfram Language evaluator v15 opened **the actual GitHub original bytes** from `BaseDecode` in a temporary binary `.h5` with strict `Import[file,{"HDF5","Data","/..."}]`; author JLD2 HDF5 *userblock* begins with `HDF5-based Julia Data Format, version 0.2.0`; actual HDF5 superblock begins at byte 512. Dataset names include `/Y_P_mat`, `/chi2_mat`, `/m_PBH_list [gram]` and UTF-8 `/β_PBH_list`. **Warning**: one Wolfram list of dataset names renders UTF-8 β as mojibake `Î²`, but reading `/β_PBH_list` with the original exact Unicode succeeds. Import Y and chi2 are `[β, mass]`, and we explicitly **transpose** to `[mass, β]`, with independent axis gates; shape alone is blind because both are 100.

Direct measured:
- 100 mass entries from `6×10^8` to `10^10` grams; 100 β values from `10^-20` to `10^-17`; 10,000 archived Y cells and 10,000 archived chi² cells, now truly opened by REC13.
- Actual author original chi² 10,000-cell reconstructed residual `max|chi2_mat−((Y-.245)/.003)^2|=4.3655745685100555e-11` (PASS against `1e-9` tolerance). This confirms the archived stored statistic is algebraically typed to its stored Y observable.
- Root-estimator matches EKS1's ORIGINAL method: for each mass find the unique upward **sampled** neighboring β pair `Y(beta_k)<.251<=Y(beta_(k+1))` and linearly interpolate Y against `log10β`; do not claim strict between-grid monotonicity, significance calibration or an IV-certified continuum root. Uniqueness of upward pairs on the sampled 100×100 grid passes all 4 scenario matrices, but not a continuum theorem.
- Exact source original `n_old=78` masses with root; first mass index ZERO-BASED `j=22`, `1.1211744564709606×10^9g`; j22 root `-17.220222662721067`, j62 root `-19.389217861290064`. Matches the prior EKS1 firstness without copying his 78 roots.

This is **SOURCE_NATIVE_BINARY_I1_PASS**, not a BlackHawk/Julia physics-solver rerun. It specifically replaces the previous statement “the source JLD2 was not directly available” with a current verified true source read. NO claim original author ran the exact currently read `main-scan.jl` binary; remaining uncertainty is dataset creation provenance and the actual published v3 Fig5 producer.

## 2. Hypothesis stress test: if raw Y data were computed by the archived code postprocessor

Let `Y_code = 2X/(1-X)` be the public source formula. Its exact inverse is `X=Y_code/(2+Y_code)`. Under the v3 paper definition `Y_v3=2X`, the *conditional postprocessing-only* mapping of each actual 10,000-cell source datum is:

`F(Y_code)=2Y_code/(2+Y_code)`.

The source critical 2σ cutoff `Y_v3=.251` corresponds to `Y_code=2*.251/(2-.251)=.28702115494568325`; it is NOT equivalent to .251 in the archived code variable.

ACTUALLY independent computation on every source HDF5 cell (not a toy):
- **original archive:** 78 sampled-grid upper-root masses; earliest j22 at `1.1211744564709606e9g`;
- **hypothetical direct F without rebaselining:** only **73** upper-root masses; earliest j27 at `1.2923576786116033e9g`. Exactly five formerly root-bearing low masses j22–j26 lack an observed crossing inside the same **finite** beta scan `[1e-20,1e-17]`. Do NOT call this “no physical bound at those masses”; only scanned-domain no-crossing.
- j22 original `-17.220222662721067` → **no sampled-grid crossing** after F;
- j62 original `-19.389217861290064` → `-18.555528141997392`, conditional `Δlog10β=+0.8336897192926713` dex;
- 73 source masses possessing both old and F crossings show conditional `Δlog10β∈[+0.831685444385851,+1.1822393854848734]` dex. This is large **only for the naive and physically baseline-incompatible source postprocessor**.

**Critical scientifically NEGATIVE knowledge**: source baseline at Y_code=.245 maps to F(.245)=`0.21826280623608016`, a shift `-0.02673719376391984`, or about **8.9124** times the quoted observation `σ=.003`. Example first original data cell at lowest mass and beta `Y_code=.24494317949740632` → `F(Y)=.2182177096814038`. This is an algebraic scaling relative to the *paper's quoted observational uncertainty*, NOT a calibrated 8.9σ model rejection or validated new SBBN prediction. It demonstrates why a postprocessor-only .83369dex threshold shift **CANNOT BE A PHYSICAL LIMIT CLAIM** without reconsidering SBBN baseline calibration and agreement with BBN-simple.

## 3. Explicit NON-IDENTIFICATION: two alternative source-only baseline calibrations, identical original 100×100 data

To test (and reject) naive unique attribution of a new physical beta constraint from a postprocessor formula alone, REC13 constructed two **deliberately ad hoc, scientifically illustrative** baseline controls, not source paper claims and not proper reruns of BBN:
- GLOBAL anchor at observed source standard reference `Y0=.245`:
  `Y_A(Y)=.245+F(Y)-F(.245)`;
- MASS-LOCAL anchor at each mass's *first scanned β=1e-20*:
  `Y_B(j,β)=.245+F(Y_code(j,β))-F(Y_code(j,β_min))`.

The second has especially strong physical limitation: `β_min` need not be pure SBBN for all PBH masses; fixing it to observation is not validated. Both are **sensitivity witnesses** only, mathematically exposing a missing calibration condition.

All three alternative 100×100 counterfactuals read the same original archive and are searched with the same root operator:

| Scenario | masses with root | earliest mass | j22 root logβ | j62 root logβ | conditional Δj62 dex |
|---|---:|---:|---:|---:|---:|
| owner archived Y_code, no mapping | 78 | 1.12117445647e9 g (j22) | -17.2202226627 | -19.3892178613 | 0 |
| F(Y), NO baseline re-anchor | 73 | 1.29235767861e9 g (j27) | no scanned root | -18.5555281420 | +.8336897193 |
| global anchor YA | 77 | 1.15349336644e9 g (j23) | no scanned root | -19.2931906314 | +.0960272298 |
| mass β_min anchor YB | 78 | 1.12117445647e9 g (j22) | -17.0136349013 | -19.2241376426 | +.1650802187 |

Grid-common shift ranges respectively `+.8316854...+1.1822394` for F; `+.0918956...+.1465676` for YA; `+.0942178...+.2065878` for YB. The correct physical prescription cannot be selected from the source (Y_code) matrix, paper formula and observational anchor alone. It requires a defined SBBN/neutron-to-helium mapping and, where claimed, actual BBN-simple network output and producer lineage. There is **no unique physical corrected β** in this archival interface test.

Strong but bounded outcome: this is NOT a hypothetical 10-point mathematical counterexample; it operates on **every one of the 10,000 genuine author source values** under three explicit formulas and compares unchanged threshold/interpolation. What is conditional is the interpretation of those values as a v3 physical observable, not their numeric reprocessing or original-source identity.

## 4. Public reproducibility and separate actual-code execution

Actually executed on original source HDF5 bytes in the current rotation:
1. Wolfram source HDF5 dimensions/provenance and exact chi² check;
2. independent full old vs F(Y) 100×100 recomputation;
3. independent three-scenario source + global-anchored + per-mass-anchored recomputation;
4. independent reexecution of the **same published audit function body**, passing the exact source binary with native 151089 bytes and strict SHA, source axes, χ², and upcrossing gates, resulting in the same 78/73/77/78 source root counts and j22/j62 values; tested in Wolfram kernel v15.0.1. Output was interpreted from exact Wolfram Association, not guessed.
5. separate actual source v1 JLD2 imported: two SHA256 values, both axes/dimensions and quantitative matrix mismatch checked (see §0).

Portable PUBLIC Wolfram Language source program, which expects the ORIGINAL SHA-256 pinned downloaded file and stops on mismatch:
`research/rec13/2026-11-22/code/rec13_rot017_wuxu_original_jld2_Yp_three_way_postprocessing_falsifier.wl`.
Public machine result JSON:
`research/rec13/2026-11-22/data/rec13_rot017_wuxu_author_jld2_100x100_conditional_Yp_postprocessor_audit.json`.
No private EKS1 dataset is embedded in these PUBLIC files; all reconstructible inputs are the author's ORIGINAL public HDF5, source Julia, and arXiv papers.
Expected source original file link (not a user-generated new file):
`https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/data/out/scanning.jld2`

The author-provided paper v3 claims that its separate nuclear BBN network agrees with the `2X_n` approximation (v3 §5). We have **not** audited its BBN-simple native modules, its full authored notebook `main.ipynb` (the GitHub connector returned 0 UTF-8 characters for this large notebook), or the exact figure-image derivation. Do not silently replace these unknowns by the source Julia `main-scan.jl`. A reproducible code/data mismatch can coexist with an actually valid separately recalculated published v3 curve. Allegations that the published physics is wrong remain unjustified.

## 5. Strict reviewer verdict, source custody and next single gate

**PASS**: exact Wu–Xu author original Git JLD2 binary SHA256 (the same bytes as EKS1 original source), direct real 100×100 HDF5 datasets and 100×100 chi2, original 78 roots and j22/j62 numbers independently reassembled, four scenario root matrices independently computed; low-level provenance read and numerical controls completed.
**PASS conditional mathematics**: if this original JLD2 matrix really stores `2X/(1-X)`, exact F(Y) is required for paper v3 `2X`; naive 73-root +.83369dex results, *and* arbitrary but explicit baseline-renormalization procedures induce 77/78-root and only +.096/+165 dex j62. Therefore **a unique physical β bound is NOT IDENTIFIED by swapping the helium postprocessor alone**.
**HOLD**: actual code-to-HDF5 produce-call lineage; actual v3 published Figure5 source, its grid version and whether it uses `Y_code`, corrected `2X`, or full BBN-simple network; SBBN baseline calibration; continuum roots; actual physics corrected PBH limits; physical best literature envelope; claimed novelty. Preserve false-positive prevention: source numerical G0 failure for Carr remains true for the **archived source**, but does not automatically certify the publication v3 figure's physics.

SINGLE OWNER-PRIORITY GATE (READ ONLY): independently authenticate the notebook `main.ipynb` / actual plotted v3 Figure5 source and whether `2X_n` is applied consistently with its standard-SBBN baseline. If that producer is demonstrably the authored `main-scan.jl` line 210, request source-backed explanation of this observable mismatch; if the v3 producer is separate network and corrected, assess it as distinct source. Do not run a new PBH generator/nuclear network solely because the archive is inconsistent until the source lineage question is resolved. Owner EKS1/Badacz/Moderator; referee REC13 records bounded audit, no task cascade or covert author contact.

FINAL:
`IW_REC13_ROT017_WUXU_ORIGINAL_BINARY_SHA256_51844A46_I1_PASS / 10K_CHI2_CELL_PASS / SOURCE_78_ROOT_EXACT_AND_NATIVE_REBUILT / CONDITIONAL_V3_73_ROOT_J62_PLUS_0P83369 / ANCHORED_77_OR_78_ROOT_J62_PLUS_0P096_OR_PLUS_0P165 / ACTUAL_PHYSICAL_BETA_UNIDENTIFIED / ORIGINAL_FIG5_AND_NETWORK_PRODUCER_HOLD / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_I3`.
