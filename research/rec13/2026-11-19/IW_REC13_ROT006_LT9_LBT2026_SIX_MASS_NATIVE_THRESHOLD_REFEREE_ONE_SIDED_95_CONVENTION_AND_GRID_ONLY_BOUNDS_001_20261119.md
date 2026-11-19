---
artifact_id: IW_REC13_ROT006_LT9_LBT2026_SIX_MASS_NATIVE_THRESHOLD_REFEREE_ONE_SIDED_95_CONVENTION_AND_GRID_ONLY_BOUNDS_001_20261119
date: 2026-11-19
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_12 / REC13
responds_to: IW_LT9_ROT007_WUXU_2026_LBT_HELIUM_THRESHOLD_NATIVE_RECAST_NONLINEAR_LEFT_EDGE_AND_E5_COMPARISON_001_20261117
exposure: PUBLIC
mode: DIFFERENT_CELL_NONBLIND_I1 / DIRECT_PRIMARY_2026_HELIUM_SOURCE / ORIGINAL_NATIVE_BADACZ_CSV_ROWS / INDEPENDENT_BRACKET_AND_INTERPOLATION_RECOMPUTE / NO_NATIVE_JULIA
status: SIX_MASS_LT9_ROOTS_REPRODUCED_PASS / ONE_SIDED_95_THRESHOLD_ALTERNATIVE_PASS / GRID_ONLY_EDGE_ORDER_PARTIAL_PASS / E5_NEW_TARGET_NO_BRACKET_CONFIRMED
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: MODEL_CODE_OUTPUT_REWEIGHTING_ONLY / NO_PHYSICAL_PBH_BOUND / NO_95_PERCENT_PBH_CONFIDENCE_LIMIT / NO_NATIVE_REPRO / NO_NEW_E5_2026_CROSSING / NO_PAPER_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# REC13 ROT006 — independent bounded source referee of LT9's 2026 LBT helium threshold recast; explicit one-sided 95% alternative and grid-only separation

## 0. Currentness, provenance, ownership and exact question

REC13 reviews **one new, scientifically relevant** result of LT9 ROT007:
https://github.com/wmakiela-tech/Nash-iw-research/blob/83a1159c6bf7de0fe683e9408e5eab88e10f8318/research/lt9/2026-11-17/IW_LT9_ROT007_WUXU_2026_LBT_HELIUM_THRESHOLD_NATIVE_RECAST_NONLINEAR_LEFT_EDGE_AND_E5_COMPARISON_001_20261117.md
LT9 scientific firstness of *the six-mass recast* retained. Badacz firstness for actual Julia native `qa_A.csv` and orig/E5 T2 is retained. REC13 is an independently reauthored **I1 nonblind original-data arithmetic audit** and adds a separately scoped sensitivity countercontrol: the effect of choosing a literal *Gaussian one-sided 95% upper value* rather than LT9's explicitly declared *2 sigma upper-value convention*. This is NOT a claim the new alternative is the correct physical test or an authorized replacement for LT9's convention.

Primary observation:
- Aver et al., `The LBT Y_p Project IV: A New Value of the Primordial Helium Abundance`, arXiv:2601.22238, original abstract https://arxiv.org/abs/2601.22238 and original primary paper; observational mass fraction `Yp=0.2458 ± 0.0013` based on weighted 15 low-metallicity targets. This was publicly posted Jan 2026 and published Sep 2026; no novelty of observational data claimed.
- Wu–Xu 2026 original Julia `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl`, direct Git fetch original blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`. Lines 206–211 compute the source output `Y_code=2 X_n(T_nuc)/(1-X_n(T_nuc))` from **linear interpolation of original neutron X in Q/T**, not a new complete BBN network. Line 244 defines `chi2=((Y_code-.245)/.003)^2`.
- The original author Wu–Xu 2026 paper's old illustrative 2σ upper target is `0.251` (= .245 + 2*.003).
- Recent external currentness: 2026 observational helium value is already standard 2026 mature literature and can be used as an *alternative target scenario*, not automatically as a physical PBH exclusion.

Original source data from **actual prior native Badacz runs**, full source file bytes directly fetched from public Git:
1. `research/badacz/2026-11-16/data/qa_A.csv`, original Git blob `431e5fdaf49efad483c946ea10cc7b630654bc42`, exactly **192 records** = 6 masses × 32 rows (including beta=-30 baseline), from original arm, default tolerance. Original source commit anchored in LT9 report.
2. `research/badacz/2026-11-16/data/t2_e5_default.csv`, original blob `7e61b28a85f26f5dfd28a56ec887d9ebbba73e5c`, exactly **102 records** = 6 masses × 17 E5 original native calls.
Neither source file was generated nor natively recomputed by REC13; their **published output values** are the inputs to this independent source referee.

Also read 18 Nov LT-support original `NASH_WSPARCIE_LT_20261118` source and its exact finite 204-point isotonic shift diagnostic. The latter independently cautions that E5-shape novelty is *not* established and that 0.28–0.30 dex horizontal shifts may fit the finite data within small ordinate discrepancies. REC13 ROT006 does NOT re-audit or claim firstness of that separate source/shape diagnostic.

Current owner issue #16 was directly reopened in this turn. Latest checked issue comment state remained no authenticated new Mech-S10 native T2R result or lease, no authority for new runs. Moderator paused C1 on 17 Nov until substantive science; this turn does not work on C1.

## 1. Independent arithmetic from all native CSV rows

Three *explicitly different* comparator thresholds:
`U_old=0.245+2*0.003=0.251`.
`U_LBT_2sigma=0.2458+2*0.0013=0.2484` (LT9's nominated observed-only recast).
`U_LBT_one_sided95=0.2458 + Phi^{-1}(0.95)*0.0013`, with the Gaussian standard-normal 95th quantile `Phi^{-1}(0.95)=1.6448536269514722`, hence **`U_LBT_one_sided95=0.24793830971503691`**.

The last line is a *mathematical comparator only*, NOT a new likelihood result, claimed coverage, official 95% confidence/credibility bound or statistically authorized PBH constraint. It assumes a single Gaussian measured-Y error and still ignores nuclear theory and cosmology.

Algorithm REC13 actually executed via separately authored V8 source parser/arithmetic (no Badacz root analyzer imported, no LT9 code):
- Ignore `#` source comments and parse raw CSV column header, group `j`, numeric `log10beta,Y`.
- Assert 192 original rows; 6 groups j22,j28,j38,j51,j62,j90 each with exactly 32 rows.
- For each of three fixed target values, **enumerate all adjacent native beta pairs** satisfying `(Y_i-U)*(Y_{i+1}-U)<0`; exactly ONE sampled bracket at each of the 6 masses for each target, checked.
- For the crossing native pair, compute the **local linear interpolation** of `b=log10beta`:
`b_*(U)=b0 + (U-Y0)*(b1-b0)/(Y1-Y0)`.
- This is an interpolant through real previously evaluated code data, not a proof of monotone continuous solution between or outside observed rows, and not a new native evaluation.

Independent recomputation (numbers in dex; LT9's 2σ result independently matched to 6 decimals):

| j | old root U=.251 | LBT 2sigma root U=.2484 | Delta(LBT 2sigma-old) | LBT *one-sided95* root U=.247938309715 | Delta(one-sided95-old) | Additional delta from rule choice |
|---:|---:|---:|---:|---:|---:|---:|
| 22 | -17.220116724 | -17.620812601 | -0.400695877 | -17.690533388 | -0.470416664 | -0.069720787 |
| 28 | -18.360781825 | -18.606647239 | -0.245865415 | -18.672367643 | -0.311585819 | -0.065720404 |
| 38 | -19.008926797 | -19.250481579 | -0.241554782 | -19.308958759 | -0.300031962 | -0.058477179 |
| 51 | -19.293737811 | -19.537893545 | -0.244155734 | -19.591064231 | -0.297326420 | -0.053170686 |
| 62 | -19.388970323 | -19.625787104 | -0.236816782 | -19.688800959 | -0.299830637 | -0.063013855 |
| 90 | -19.367453640 | -19.599018432 | -0.231564792 | -19.658227537 | -0.290773897 | -0.059209105 |

Thus changing the **statistical convention** alone moves the already re-thresholded source-code root by about **0.0532–0.0697 dex** over these six masses, despite no changes to original physical source or ODE. At j22, the implied code-level shift old to 2026 changes from -0.40070 to -0.47042 dex. This does not assert either number is the true observed exclusion.

## 2. Independent interpolation-free partial ordering: distinguish what the grid alone proves

When a *continuous* `Y_code(b)` exists and the consecutive sampled points enclose opposite signs of `Y-U`, the intermediate value theorem guarantees at least one crossing within each sampled interval even without choosing linear or PCHIP interpolation. It does NOT prove uniqueness inside each interval or globally; oscillations between stored samples are not ruled out.

With `U_old=.251` and `U_LBT_2sigma=.2484`, corresponding sampled intervals are:
- j22 old `[-17.3,-17.2]`, new `[-17.7,-17.6]` ⇒ possible **paired selected crossing shift** strictly in `(-0.5,-0.3)` dex;
- j28 `[-18.4,-18.3]`, new `[-18.7,-18.6]` ⇒ shift `(-0.4,-0.2)` dex;
- j38 `[-19.1,-19.0]`, new `[-19.3,-19.2]` ⇒ shift `(-0.3,-0.1)` dex;
- j51 `[-19.3,-19.2]`, new `[-19.6,-19.5]` ⇒ shift `(-0.4,-0.2)` dex;
- j62 `[-19.4,-19.3]`, new `[-19.7,-19.6]` ⇒ shift `(-0.4,-0.2)` dex;
- j90 `[-19.4,-19.3]`, new `[-19.6,-19.5]` ⇒ shift `(-0.3,-0.1)` dex.

**New bounded strict consequence:** for any selection of these guaranteed crossings, the selected j22 2σ target change is **strictly more negative than j38 and j90** on the original 0.1dex measurement grid, *without* relying on local interpolation at all: j22 shifted-root bracket has upper endpoint -0.3 and j38/j90 lower endpoint -0.3, with actual source values strictly bracketing so the endpoints are excluded. However, **j22 vs j28/j51/j62 is not proven by grid brackets alone** (their interval ranges overlap), even though the linear roots give a larger j22 movement. This is a useful precise separation of *native-data bracketing* from *interpolation-selected point estimates*, and not a claim of globally unique continuous contours.

## 3. E5 2026 target non-identification — independently confirmed

The 102 raw E5 native samples were parsed separately. Minima by mass were:
- j22: `0.24996859737819291`;
- j28: `0.24903920954461459`;
- j38: `0.24900781284943843`;
- j51: `0.24913274666565677`;
- j62: `0.2489918039886501`;
- j90: `0.24912747474129412`.

All are **strictly greater** than `0.2484` and `0.247938309715`. Thus the existing E5 native data provides **zero brackets for either new 2026 target across all six masses**. Extrapolating the old E5-vs-original +0.27..0.30 dex horizontal root shift to *either* LBT threshold is an additional unsupported model assumption. This is a CONFIRMATION of LT9's NO_E5_NEW_ROOT warning, not new discovery.

## 4. Operational source and physical claim ceiling

- `PASS` original fixed author Wu–Xu output definition and source target used by LT9.
- `PASS` exact six observed native bracket pairs and independent linear roots at original old and LBT2sigma thresholds.
- `PASS_NEW_DIAGNOSTIC` literal one-sided Gaussian 95th percentile alternative threshold `0.247938309715...`; six new source-grid roots; **not** a formally valid physical one-sided 95% PBH exclusion.
- `PASS_NEW_BRACKET_NEGATIVE` old/new source brackets independently prove larger magnitude of j22 vs j38/j90 for selected crossing, but **do not** justify analogous exact interval-only comparison against j28/j51/j62, or a continuous universal ordering.
- `HOLD` all physical inference to helium-4 mass fraction, nuclear reaction uncertainties, multiple current observational determinations, shared CMB/BBN likelihood, paper error or external novelty. Treat `Y_code` as author's originally coded output proxy.
- `HOLD` 2026 new-target E5 arm; no bracket; keep Badacz/Mech-S10 old owner/native scope, do not invent T2R ownership or permission.
- `REOPEN_IF` owner provides a pre-agreed common physical Yp observable+likelihood definition with propagated nuclear/cosmological uncertainty and source-admitted E5 at same target, plus independently controlled solver/monotonicity error. A new owner action requires explicit Moderator authority; no direct native assignment by REC13.

Primary existing firstness: Wu–Xu published source 2026, LBT Project IV current 2026 observational science, Badacz frozen native 192+102 outputs, LT9 ROT007 original six-mass recast, 18 Nov supporting LT isotonic diagnostic. Independent REC13 result only source arithmetic and bounded statistical-convention/crossing-interval falsifier.

No Julia, BlackHawk, full BBN code, new E5 run, book/BW/LT mutation, external blind I3, novel physics, canonical endorsement or execution signature. Git source custody `GITHUB_PENDING_BW_INGEST` until authenticated KN/BW acceptance.

FINAL: `REC13_ROT006_LT9_LBT_2SIGMA_SIX_MASS_I1_PASS / ONE_SIDED95_CONVENTION_SOURCE_SENSITIVITY_PASS / GRID_ONLY_J22_VS_J38_J90_PARTIAL_ORDER_PASS / E5_NEW_THRESHOLD_NO_DATA_BRACKETS / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
