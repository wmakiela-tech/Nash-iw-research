---
artifact_id: IW_MECH_S9_ROT018_WUXU_AUTHOR_HIGH_T_EXACT_MASS_CLOCK_VERSUS_NATIVE_SAVED_TIME_PAPER_CODE_EMISSION_RATIO_SOURCE_CERT_001_20261113
created_at: 2026-11-13
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
document_type: ORIGINAL_SOURCE_EXACT_MASS_ODE_REPARAMETERIZATION_VERSUS_ORIGINAL_NATIVE_10D_DENSE_OUTPUT
scientific_status: ANALYTIC_SOURCE_MASS_REPARAM_PASS / 80DIGIT_DECIMAL_REPLAY_PASS / 5RATE_NATIVE_CLOCK_DISCREPANCY_MEASURED / NO_NEW_JULIA / B1_NUMERIC_HOLD
claim_ceiling: FROZEN_SOURCE_PER_PBH_EMISSION_NUMBER_INTEGRAL_ONLY / NOT_REACTION_RHS / NOT_ALTERNATE_10D / NOT_HELIUM_OR_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# Mech-S9 ROT018 — exact source PBH mass-clock reparameterization quantifies numerical clock dependence in ROT017

## Source, firstness, negative knowledge preserved

ORIGINAL Wu & Xu public JCAP source `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`: original `arXiv-2509.05618/main-scan.jl` blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`, lines around80 define `dM/dt=-N_BH(T_BH) m_Pl^4/M^2`. Original `tool_script-parameters.jl` blob `0d7198ff3557bdbd5753000bb07a7a7405cc24f5`, `N_BH=(27/4)N_rho(T_BH)/(30720π)`, original high-T PDG degree-of-freedom interpolation `tool_script-N_relativistic_species.jl` blob `0437c032bdc4bafca6cb634c0db4cd2c46fb7efc` has **constant** out-of-table values. Original j22 source PBH T_BH starts ≈9.4 TeV, high above last ≈280 GeV PDG table; so `N_BH` constant throughout PBH-live branch under frozen original source; `dM/dt=-K/M²` and `M³+3Kt` exact for source continuum before cutoff.

FIRSTNESS:
- Wu/Xu FIRST scientific source and original published §4.1 Eq4.5 analytic edge-matched `R_h∝M^-1.3` and original tabulated Julia source first-two-node log-log extrapolation p≈-1.20.
- PRF13 ROT017 FIRST exact integrated source-model hadron emission NUMBER below the first table node; LT8 ROT017 independent count and LT8 ROT018 FIRST source PAPER-vs-CODE correction with whole-evaporation author analytic count comparison, ROT019 FIRST verified v1/v2 historical source prescription.
- Mech-S9 ROT012/013 FIRST executed actual 10D Julia one-point six-hadron 10k source run (original native Actions 43436800793). Mech-S9 ROT015 FIRST native first-rate-node time, ROT016 FIRST on-path six-source SIGNED HADRON RHS integral fraction below rate table, ROT017 FIRST native *saved-time* AUTHOR PAPER/CODE five-source-rate comparison over the frozen observed subgrid mass interval.
- KN14 ROT002 FIRST detected real native mass-cubic `C` source secant drift ≈-0.610519%; REC11 ROT034 independently source-reviewed and gave sharp 4-node minimax time residual 0.197855ms; INT9 ROT027 independently verified original constant N_BH model branch. MT15 ROT020 FIRST proved the original numerical 10D trajectory's saved cutoff M=1.472687g undercuts source exact forward-invariant Mstop=2.310913g by ≈36.27%; this is numerical source-end boundary, not a 36% BBN error.
- Mech-S9 ROT018 DISTINCT exact analytic mass-*reparameterization* of the PREVIOUS native-clock ROT017 five-rate observable over the **SAME frozen mass endpoints**. It quantifies sensitivity of that reported 5% rate contrast to use of native saved dense-output time rather than the exact author mass-time law. NO physics novelty firstness claimed.

## Exact source formula / matched endpoints

At each of five author source hadron rates h, original first-two table nodes from `arXiv-2509.05618/data/out/hadrons_from_PBH.dat` blob `06d0883a27b108692720422294ba2baacd381a64` give source code exponent
```
p_h = log(R_h(M2)/R_h(M1)) / log(M2/M1)
R_code,h(M)=R0,h*(M/M0)^p_h,          M<=M0=1e9 g
R_paper,h(M)=R0,h*(M/M0)^(-1.3),       same anchor R0,h at M0.
```
Under frozen original high-T constant `K` author equation, exact continuum time:
```
dt = -M² dM/K
J(p) = ∫_{t(M0)}^{t(Mlast)} R0 (M(t)/M0)^p dt
     = (R0 M0³/K) * (1-r^{3+p})/(3+p), r=Mlast/M0.
J_paper/J_code = [(3+p)/(3-1.3)] [(1-r^(3-1.3))/(1-r^(3+p))].
```
Cancel absolute `K` and source rate anchor `R0` EXACTLY. This **does not depend on the native saved-time clock**, but uses the same actual last recorded live mass: `Mlast=144891220.526512 g` (native original one-based index8544). Upper source mass endpoint the same `M0=1e9 g`, first rate table node. Do not integrate past last native live mass or across observed PBH cutoff rows8544–8545; source Mstop not applied to this separate matched-endpoint comparison.

## Actually computed new source result: native saved-time estimates are systematically HIGHER

REUSED original unchanged native 10D Julia author ZIP artifact `14045176436` from Action `43436800793`, SHA256 `71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486`, original `author_native_raw_hadron_history_10000.csv` SHA256 `45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1`. Original native saved source M first crosses M0 between rows8383–8384. RETROSPECTIVE ROT017 actually executed original sampled-time comparison source JSON SHA256 `323e09e522882252823e0d428a398e88649c317e1341f06b2b3f0a051d5ed2d1`. Source-authentic one j22 beta=1.005863531057e-17 is +0.586% outside original author scan upper beta1e-17, but callable, NOT a published grid node.

Actual ROT018 executable used **80-decimal precision** independent source exponent and exact analytic formula, crosschecked vs float64 math.expm1, and separately independent mass-axis trapezoids on ACTUAL original native recorded mass output knots. Results, percentage change in PAPER versus CODE source-model PARTIAL emitted hadron NUMBER:
| hadron source channel | exact source mass-law (80D) | source native-mass-node trapezoid | previous native-time trapezoid ROT017 | previous native-time PCHIP ROT017 | time trapezoid minus source exact (percentage points) |
|---|---:|---:|---:|---:|---:|
| pi± | +5.137832% | +5.129413% | +5.319587% | +5.239828% | +0.181755 |
| K± | +5.337047% | +5.328273% | +5.525618% | +5.442877% | +0.188571 |
| K0L | +5.329070% | +5.320310% | +5.517369% | +5.434747% | +0.188299 |
| proton | +4.940185% | +4.932117% | +5.115161% | +5.038369% | +0.174976 |
| neutron | +4.915698% | +4.907674% | +5.089833% | +5.013409% | +0.174135 |

Mass-knots trapezoid departs from source exact by **<0.00878 percentage points**, whereas native saved-time trapezoid departs by **+0.1741..0.1886 percentage points**. Prior native-time PCHIP differs by **+0.0977..0.1058 percentage points**. The extra discrepancy is too large to be attributed solely to observed mass-axis trapezoid integration error. It diagnoses *saved-time versus exact source mass-time law, plus interpolation quadrature* on this particular archived computation. KN14 / REC11 independently demonstrated numerical native mass-clock inconsistency. This is NOT by itself a bound on source solver error, Xn endpoint bias, or physical emission-rate uncertainty. The sign and channel-dependence are historical source diagnostics only.

## Reproducibility, exact original source bytes and fail-closed tests

Local ACTUALLY EXECUTED `mech_s9_rot018_exact_cubic_mass_reparam.py` source SHA256 `06fae9332d19db4aeb88ac24017722fc5279a0c8c3fd8b15a4a4549650e24ba2`. It verifies original ZIP *outer* SHA256 and ZIP CRC, **all 16 original original artifact payload SHA256**, original 10000-point source CSV SHA256 and original ROT017 result JSON SHA256, exact source rate first-two-node decimal literals pinned to author Git blob, matches native 8383/8384 mass crossing and row8544 last PBH-live mass, and independently evaluates five source exponents and exact 80D ratios. It does **NOT** run Julia, change a PBH input, or solve any alternative neutron ODE.

Actual full result `mech_s9_rot018_exact_mass_axis_vs_native_clock.json` SHA256 `372a0c048ee0f6f522d74f13873e130c1900241b47e52f0430634dd250d3978a`. New complete **conversation-local** reproduction archive `mech_s9_rot018_exact_mass_clock_source_reproduction.zip` SHA256 **`f0fcd16691f6de0a96ec635e590e339de18b8fe36a66587def93122c3d3acde7`**, 723240 bytes; includes the unchanged original Julia author ZIP, the exact original ROT017 JSON, new actually executed Python, new complete 5-channel JSON, README, manifest. Verified ZIP CRC PASS, all **5/5** SHA256 manifest payload PASS, fresh extract+isolated `python3 -I` replay generated JSON **BYTE-IDENTICALLY PASS**, tampered original author ZIP rejected before numerical output and tampered ROT017 input JSON rejected, 2 negative controls PASS. This full package is LOCAL conversation artifact; its bytes are NOT claimed to reside on GitHub/BW. Repo scientific body does not substitute local package custody.

## Science disposition, B1 next gate

Mech-S9+Badacz B1 source owners ACKED 30-day (2026-11-13..2026-12-13) Moderator-accepted original-source question; no currently verified per-Julia-run Moderator authorization, no original new solver in ROT018. Proposed B1 primary source `X_n(T_nuc)` with author exact Q/T linear output and author algebraic `Ycode=2X/(1-X)` secondary remains Moderator decision. There is NOW a serious numeric original branch prerequisite: KN14 native constant-K cubic CLOCK drift, REC11 sharp proof, MT15 under-cut original source forward-invariant event cutoff. Before source-method 2x2 Julia arms could be interpreted, numeric mass-clock and cutoff event refinement must be preregistered with accepted convergence metrics, ORIGINAL source producer and original correct output map. Published M^-1.3 vs code M^-1.2 is AUTHORS' two mathematical prescriptions, not independently measured PYTHIA/HERWIG physical uncertainty; physical E4 below table remains unresolved.

**Verdict** `EXACT_ANALYTIC_MASS_CLOCK_5_OF_5_PASS / ORIGINAL_NATIVE_TIME_RATE_FRACTION_BIAS_DIAGNOSTIC / NO_NEW_JULIA / B1_NUMERIC_VALIDITY_HOLD / B1_INPUT_SOURCE_HOLD / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE`. GitHub source-report write/readback is distinct from BW ingest; `GITHUB_PENDING_BW_INGEST`.
