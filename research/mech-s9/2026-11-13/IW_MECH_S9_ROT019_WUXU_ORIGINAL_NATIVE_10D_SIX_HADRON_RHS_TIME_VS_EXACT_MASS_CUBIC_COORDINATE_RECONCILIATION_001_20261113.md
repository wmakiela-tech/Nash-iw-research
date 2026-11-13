---
artifact_id: IW_MECH_S9_ROT019_WUXU_ORIGINAL_NATIVE_10D_SIX_HADRON_RHS_TIME_VS_EXACT_MASS_CUBIC_COORDINATE_RECONCILIATION_001_20261113
created_at: 2026-11-13
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
document_type: ACTUAL_WUXU_SOURCE_NATIVE_EXISTING_10D_RHS_REPARAMETRIZATION_REPRODUCIBLE_NUMERIC_AUDIT
claim_ceiling: FROZEN_SOURCE_ON_PATH_FORCE_MEASURE_ONLY / NO_NEW_JULIA / NO_NATIVE_ODE_ERROR_CERTIFICATE / NO_CAUSAL_DELTA_X / NO_PBH_BBN_BOUND / E4_BLOCK / NO_FIG5_BUILD_ID / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE
---

# ROT019 — six-hadron neutron RHS original saved time versus mass-cubic author-law measure, source native j22

## 1. Priority, source identity, and question

Scientific original firstness: Wu and Xu, *Primordial black holes evaporating before Big Bang nucleosynthesis* (JCAP 02 (2026) 063), original frozen source `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`, native `arXiv-2509.05618/main-scan.jl` Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`. The source mass equation in high-T `N_BH=constant` branch is exactly `dM/dt=-K/M²`, `M³+3Kt=constant`; independently source-checked first by PRF13 and INT9. Mech-S9 ROT012/013 FIRST executed original one j22 10D native Julia `magic()` with six actual raw hadron histories, 10000 time points. PRF13 ROT017 FIRST quantified ~81.36–81.44% original hadron-number production below lowest 1e9g emission table node; Mech-S9 ROT015 FIRST mapped that node onto native source time; ROT016 FIRST independently reconstructed source six-species signed neutron conversion RHS and found below-node native saved-time area fraction **73.265173652%**.

Independent materially newer source checks: KN14 ROT002 first measured ~0.610519% drift in original source high-T mass-cubic secant K; REC11 ROT034 first proved four-point Chebyshev sharp fixed-sample native timing misfit; LT8 ROT021 first determined full 8544-row source-Chebyshev misfit, MT15 ROT020 first found numerical cutoff stop mass undercut ~36.27% at gram-scale. Mech-S9 ROT018 FIRST compared paper-vs-code partial emission proxy on original saved time and analytic author exact mass-clock. This ROT019 is a **distinct comparison for the original SIX SIGNED ON-PATH neutron conversion RHS area fraction 73.3%**, not another proof of the cubic invariant or five per-BH emission counts. No re-attribution of others' scientific work.

## 2. Typed mathematical test and strict source evidence

Actual original **unaltered** one-point 10D Julia native Actions run `43436800793`, original artifact `14045176436`, ZIP SHA256 **`71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486`**, actual original `author_native_raw_hadron_history_10000.csv` SHA256 **`45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1`**, 16/16 archived internal file SHA256 and ZIP CRC PASS. Same original mass `j=22, M_init=1.1211744564709606e9g` and original callable beta `10^-16.9974609375≈1.005863531057e-17`, **+0.5863531% outside original author beta scanned maximum**; genuine original source callable, NOT a published 100x100 scan node.

Original live PBH rows one-based 1…8544; original first PBH zero row8545 is an abrupt model event, **NOT integrated over**. First 1e9g rate-table node crossing between original native rows8383 and8384, bracket linear t≈0.097311848231463s; last live PBH t≈0.334927351810113s, mass≈1.44891220526512e8g. Original saved active hadron densities never hit numerical floor, so original RHS-used and original RAW are identical in this entire phase.

At EVERY original source live time point, reconstruct the SIX original signed reaction contributions, in original native units GeV³ times mbarn converted using `ħ,c,e` SI constants:

```
F_h = n_pi- (1-X)*1.5 Fc_pi - n_pi+ X*1.7
    + n_K- ((1-X)*31 Fc_K - X*26)
    + n_K0L * 7*(1-2X) - n_pbar*28X + n_nbar*28(1-X).
```

All coefficients match original source; the SIX-RHS signed sum `F_h` is positive at all 8544 live saved samples. `F_h` is an original-solution pointwise RHS rate, **not** the net causal effect of six hadron channels on `X_n`. Independently using mass coordinate on the **SAME stored original X,T,raw hadrons**:

```
dM/dt = -K/M² (original high-T constant N_BH)
dt = -M² dM/K = -(1/3K)d(M³)
u=(M_init³ - M³)/10^27 g³
f_below = [integral_(M=1e9g..last_live_M) F_h(u) du] /
          [integral_(M=Minit..last_live_M) F_h(u) du].
```

`K` cancels exactly in `f_below`; this mass-clock comparison needs **no fitted K at all**. An early source sampled K secant (8200–8350) is used **only for secondary absolute scale**, explicitly not the author's exact physical K.

**Scientific caveat**: although the original cubic mass-clock follows mathematically from the author equation, the state profiles `X(u),T(u),n_h(u)` are still TAKEN FROM THE NUMERICALLY RECORDED RUN; reweighting their source RHS by a new measure is a *post hoc reparametrized on-trajectory diagnostic*, NOT a corrected coupled ODE solution or solver-convergence certificate.

## 3. Measured actual source results and negative knowledge

| Fraction of integrated six-hadron signed RHS `∫F_h dt` below first 1e9g table node | Original saved t | Exact source cubic mass-coordinate u | Shift cubic−native (percentage points) |
|---|---:|---:|---:|
| Left quadrature | 73.1603034233% | 73.1069763922% | −0.0533270311 |
| Right quadrature | 73.3689898892% | 73.3087076319% | −0.0602822573 |
| Trapezoid | **73.2651736523%** | **73.2083375210%** | **−0.0568361313** |
| PCHIP Hermite | **73.2459772697%** | **73.1894021736%** | **−0.0565750962** |
| Independent trapezoid directly in `3M²dM` | not applicable | **73.1809915298%** | distinct source-mass quadrature |

The directly `3M²dM` trapezoid and the cubic-coordinate trapezoid differ **0.027346 percentage points**; this is a data-interval quadrature sensitivity, not an ODE accuracy bound. The cubic-trapezoid and cubic-PCHIP fraction differ **0.018935 pp**. For 65-digit Decimal direct calculation on the ORIGINAL serialized mass tokens, cubic-coordinate below fraction is `0.73208337520952227123769304525532273211433894632350616048784376496`; difference from independent Float64 computed `0.7320833752095222` is only `7.12376930452553e-17` in the stored fraction.

Source mass sequence in the original 8544 live samples has **4932 equal adjacent saved-decimal mass pairs** (but **ZERO upward mass steps**): very early mass changes are beneath the precision of source CSV printing. An automatic naive PCHIP of *every saved mass sample* fails on duplicate abscissae. The independent script explicitly merges ties with the final observed sample, enabling source cubic-mass PCHIP without fabricating mass changes. Positivity, original mass ordering, source 10000-row count, 6 floor flags, event index, ZIP identity and 16/16 original manifest members separately checked. A synthetic exact mass-cubic clock and constant (F_h) test passes source-time-vs-mass fraction equality <1e−14.

For secondary scale only, using **fitted early source K=1.40221242473924e27 g³/s** gives the signed RHS integral from original source samples:
- above node saved-time trapezoid +0.290258429882198 versus cubic mass-scaled +0.290253103941394;
- below node saved-time trapezoid +0.795435661063878 versus cubic mass-scaled +0.793117904365330;
- full preev saved-time +1.085694090946076 versus cubic mass-scaled +1.083371008306724; difference −0.002323082639353 dimensionless.

**The last absolute difference is not `ΔX_n`** and must not be called a physical hadron effect. It reflects alternate integration measures on the same saved source states. Source six-channel signed contributions cancel strongly; different mechanisms and competing weak conversion prevent causal inference from the on-path RHS area.

Result: this specific `~73.2%` SOURCE-AREA statement is relatively robust to reparametrizing the integration clock on this recorded trace: approx −0.057pp shift, despite the independent mass-cubic invariant inconsistency of source samples. This does **not repair the source solver** or validate the author's extrapolated particle-production physics.

## 4. Actually executed self-contained reproducibility

Independent new Python 3 STANDARD LIBRARY script actually executed on exact original 713794-byte archival ZIP, no new Julia:
`mech_s9_rot019_mass_reparam_source_audit.py` local SHA256 **`bca8c609942e1c379a8c68936d9f3ecfeafbadd10a022df83ee5b8a1017b558d`**.
Actual full source-trace result `mech_s9_rot019_mass_reparam_source_audit.json` SHA256 **`865b4c53060f9db2b3ba8ce71490880da2e69b6ce46c63669978f43137f1d867`**.

Complete **conversation-local** ZIP `mech_s9_rot019_mass_clock_hadron_rhs_reproduction.zip` archive SHA256 **`5fbfef631c56d2604beeb327c4873e95a6436f3baae3bc68421db99e61db96d9`**, contains 4 original payload members (AUTHENTIC original native Julia source ZIP, EXACT executed script, EXACT produced JSON, README) and its SHA256 manifest. ZIP CRC PASS; all 4/4 payload SHA PASS; nested untouched original author ZIP has 16/16 native internal SHA PASS; extracted standalone python3 -I replay produced **BYTE-IDENTICAL JSON**; mutation of one byte in original native source ZIP caused fail-closed rejection before output, PASS.

The script and full local JSON are supplied in the conversation-local downloadable ZIP; they are **NOT falsely described as separately archived GitHub contents or BW ingestion**. GitHub science report is published separately with exact commit/blob readback.

## 5. B1 decision

30-day owner B1 Mech-S9 + Badacz ACK, original INT9 recommendation `X_n(T0=.07818527068831994MeV)` with original LINEAR `Q/T` output (not PCHIP/t), code `Y_code=2X/(1-X)` typed secondary only. Moderator **per new Julia run** authorization is still not verified. Main B1 obstacles remain stronger than 0.057pp on-path area sensitivity: numerical exact-author high-T cubic mass invariant failure on saved source (KN14/REC11/LT8), original terminal mass cutoff undercut (MT15/AUD2), source ODE default tolerance lack of endpoint certification (MT15 ROT021), unknown published JCAP figure-producing code, and independently calibrated BlackHawk/PYTHIA hadronization below 1e9g absent.

No extra scientific tasks automatically commissioned, no original equations changed, no new Julia run, no physical PBH bound. Current state:
`ROT019_ORIGINAL_NATIVE_SOURCE_REPARAM_RHS_SHARE_PASS / FRACTION_73P208_VS_73P265_DIFFERENCE_0P057PP / 4932_RECORDED_MASS_TIES_HANDLED / FULL_REPLAY_PASS / B1_NATIVE_NUMERIC_AND_INPUT_HOLD / NO_NEW_JULIA / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / GITHUB_PENDING_BW_INGEST`.
