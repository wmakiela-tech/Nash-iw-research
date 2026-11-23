---
artifact_id: IW_M16_ROT014_WUXU_ORIGINAL_100ROW_HADRON_TABLE_SUBGRID_EXPOSURE_500RATE_CROSSCHECK_AND_GEC_B_PARTIAL_GUARD_001_20261123
origin: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_11 / M16
date: 2026-11-23 Europe/Warsaw
authorization: Moderator 2026-11-23 direct instruction "Sam prowadź prace zamiast czekać na badacza"
science_type: INDEPENDENT_FIRST_PARTY_WU_XU_SOURCE_TABLE_READ / MASS_INTEGRATED_HADRON_NUMBER_EXPOSURE / ALTERNATE_LOG_SIMPSON_CONTROL / 500_RATE_CROSS_TABLE_UNIT_RECEIPT / G_EC_PLUS_B_PARTIAL
status: SOURCE_TABLES_DIRECT_READ / EXECUTED_V8_ARITHMETIC / EXECUTED_ALTERNATE_24000_PANEL_SIMPSON / EXACT_PIECEWISE_POWER_LAW_ALGEBRA / SELF_CONTAINED_EMBEDDED_SOURCE_REPRODUCER_READBACK_PENDING
claim_ceiling: NO_ENERGY_BUDGET_CLOSED / NO_AUTHOR_ERROR / NO_DIRECT_NEW_BBN_NUCLIDE_RESULT / NO_FIG5_NEW_BETA_BOUND / NO_EXTERNAL_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_BW_NATIVE_WRITE
---

# M16 ROT014: First independent physical-source progress on G_EC+(b) — entire author hadron table and sub-grid number fluence

## 1. Research mandate and original firstness

Moderator explicitly directed M16 to perform active research, instead of waiting for BADACZ. This supersedes M16's self-imposed passive HOLD after ROT011–013 in the limited scope of autonomous M16 research. It does NOT transfer BADACZ ownership of native Julia/PRyMordial BBN studies or allow a new physical PBH bound without evidence. M16 original contribution is a DIFFERENT-CELL direct read and a carefully controlled, previously unreported source-integral exposure diagnostic.

Direct ORIGINAL AUTHOR code and data, pinned 2025 original upstream commit `d395183674cace6c9906a8911bdeb7234ba4040d`:
- Original **complete** published Wu–Xu source table, exactly 100 rows × 5 positive emission rate columns in natural `GeV` time units, Git blob `06d0883a27b108692720422294ba2baacd381a64`:
https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/data/out/hadrons_from_PBH.dat
- Original **complete** prescription `tool_script-hadrons_from_PBH.jl` Git blob `cc73432910f872d526113ce59b6204f38d0766a9`: code reads columns by mass in GeV, log-log interpolates, and linearly EXTRAPOLATES outside the log-mass grid (ExtrapolationType.Linear).
https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/tool_script-hadrons_from_PBH.jl
- Original author `tool_script-parameters.jl`, blob `0d7198ff3557bdbd5753000bb07a7a7405cc24f5`, lines 101–106, fixes N_BH mass-loss coefficient.
- Original author `main-scan.jl`, blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`, lines 80 and 102–128, mass-loss rate and one-rate-per-mass hadron injection; line 167 nominal terminal cutoff `M_cut=max(M_start exp(-20),m_Pl)`.

Second complete different-cell archived SECONDARY integrated number rates, 100 × 5 per-second count entries, originally created by BADACZ for run 090 (NOT independent from BlackHawk physics, but independent file/protocol), Git blob `2ffa1720a45dcd52fcbd7b668416007d5f927eee`:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/badacz/2026-11-21/data/primary_spectra_090_secondary_totals.tsv

BADACZ original native REVIEW117 directly read (blob `98399b8565a5ba900f12e1c0fdc8cff6e080dad4`):
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/badacz/2026-11-23/IW_BADACZ_B1_SUBGRID_EXTRAPOLATION_NATIVE_CHECK_REVIEW_117_20261123.md
This team already established FIRST that j22 PBH **beta threshold** shifts ~-0.061 dex when replacing author code's low-M table extrapolation with a paper-inspired M^-1.3 slope and that an integrated exposure-only proxy FAILED (3/6). Preserve original native threshold firstness; ROT014 does not duplicate their native runs or pretend its total fluence predicts thresholds.

## 2. Entire first-party table and 500-unit crosscheck

100 original masses form a geometric grid from exactly `1e9g` to `4e12g`, ratio step `1.087387770584725`; five separate rate columns: charged pion, charged kaon, K_L0, proton, neutron. All 500 values strictly positive.

Independently verify Badacz run 090 `primary_spectra_090_secondary_totals.tsv`: there are exactly 100 aligned masses and exactly 500 positive number rates. Original author rates `q_i(M)` carry dimension energy in natural units (one per natural second); archived secondary rates `Q_i` are in 1/sec. For ALL 500 cells, `Q_i * hbar / q_i` differs from 1 by at most `7.7342022e-11` with CODATA `hbar=6.582119569e-25 GeV s`; implied hbar has median `6.58211956950907e-25 GeV s` with internal spread only rounding. All 100 masses match exactly under source mass GeV-to-gram normalization.

This is a strong quantitative **unit and number multiplicity ledger** between two source datasets. It does NOT assess whether secondary hadrons carry the energy specified by the primary Hawking flux; no G_EC+(b) energy test can be inferred from totals alone. The two datasets share a BlackHawk modelling family and are not independent physical measurements.

## 3. Independently integrated emitted HADRON NUMBERS, not energy

For each tabulated species column, at one isolated PBH start `M_i` and terminal `M_cut=M_i exp(-20)`, under Wu–Xu's code mass loss `dM/dt=-f_code/M²`, with code plateau `f_code=1.6295583423315782e74 GeV⁴` independently checked M16 ROT011, the integrated count is
  N_i^code(M_i) = 1/f_code * integral_{M_cut}^{M_i} q_i(M) M² dM.

On a log-log segment `q(M)=q_a (M/M_a)^s` and `s != -3`, integration is analytical:
  I(a,b) = q_a M_a³/(s+3) [ (b/M_a)^(s+3) - (a/M_a)^(s+3) ].
Below 1e9g the code extends the slope from the first two rows; first-row alpha=-s in the narrow range `1.19665...1.20476` across five species. Terminal cutoff 2.31g (j22) or 7.20g (j62), well above m_Pl, is the original **code** cutoff, not artificially M=0.

RESULTS: share of total *number per one PBH* emitted BELOW first original table mass M=1e9g:

| source column | j22 M0=1.121e9g | j62 M0=3.494e9g |
|---|---:|---:|
| q_charged_pion | **81.4231%** | **11.1584%** |
| q_charged_kaon | 81.3875% | 11.0959% |
| q_K_L0 | 81.3889% | 11.0999% |
| q_proton | 81.4585% | 11.2208% |
| q_neutron | 81.4629% | 11.2283% |

Concrete total source-column pion counts, under code f:
- j22: `3.6159515794300184e29` q_charged_pion particles per PBH;
- j62: `2.6385783243396705e30` per PBH.
These are ONE q_pion column, not automatically the sum of both charges; the native main-scan uses that same source q_pion in separate pi- and pi+ equations. Multiplicity semantics require careful handling.

If and ONLY IF BlackHawk has the previously BADACZ-reported constant `R=f_BH/f_code=0.58175` and the same native q(M) holds all along the trajectory, then N_i^(BH)=N_i^(code)/R. This correction changes all counts but NOT the shares below tabulated range if f-ratio is constant. M16 has not independently reopened original BlackHawk `fM.txt`, so **all such BH-adjusted values are strictly conditional**. No inference that Y_P or beta scales as 1/R.

Second FRESH numerical implementation uses direct 24000-panel composite Simpson quadrature in `log M`, independent of the exact per-segment power integral, reading identical original raw source array but computing literal `q_h(M)` by log interpolation and `q_h(M) M³ dln M`. For all TEN mass/species outputs, maximum relative discrepancy `1.6611360065255099e-9`; subgrid-share absolute discrepancy of similarly small magnitude. Two distinct integration paths PASS. No Java/Julia native BBN re-execution.

## 4. Extrapolation sensitivity — what it does and does NOT predict

Holding original tabulated `q_i(M=1e9g)` fixed and changing ONLY below-grid power `q_i(M) ∝ M^-alpha`:
- alpha=1.3 instead of actual ~1.20 boosts **j22 per-BH emitted numbers** by +4.56% to +4.95% across five species; **j62** by +0.629% to +0.675%;
- alpha=1.5 boosts j22 by +16.03% to +16.46%; j62 by +2.21% to +2.24%.
- alpha=1.0 lowers j22 by ~8.0%–8.34%; j62 by ~1.09%–1.15%.

The analytic derivative, if terminal cutoff negligible, is `d ln N_total / d alpha ≈ F_sub/(3-alpha)`. Near alpha~1.2, j22 gives ~0.45 per unit power index, j62 ~0.06. This correctly explains why same exponent change moves source-column number fluence much more at j22 than j62. **This DOES NOT predict native BBN beta threshold**: BADACZ REVIEW117 already falsified simple exposure transfer approximations because physical response kernels and nonlinear dynamics have unequal weighting over mass/temperature. Four-dimensional matter evolution cannot be replaced by a count-only single PBH integral.

## 5. Partial G_EC+(b) guard: easy necessary energy test is weak

A lower bound on energy associated with these five tracked hadrons is their rest-mass production power `P_rest_min(M)= Σ_h m_h q_h(M)` using original source masses from Wu–Xu parameters. Comparing to **CONDITIONAL** full BlackHawk power `P_BH=0.58175*f_code/M²`:
- at 1.000e9 g: `P_rest_min/P_BH≈5.8812e-4` (0.0588%);
- at j22 1.121e9 g: `6.4355e-4` (0.0644%);
- at j62 3.494e9 g: `1.4353e-3` (0.1435%).
This uses **one event per each of five tabulated column counts** as a conservative necessary floor; if charged pion column corresponds to separately injected pi+ AND pi- as in main-scan, the floor is somewhat higher. It CANNOT constrain the rest of the energy budget: emitted hadrons may carry kinetic energy and hadronization has many untracked secondaries. It is NOT a physical G_EC+(b) PASS, merely a demonstration that number totals plus masses by themselves provide far too weak a test. Even an exactly matched 500/500 count ledger cannot close energy conservation. This rest floor is not a claim of positivity in the full secondary model without verifying how categories are counted.

## 6. No scientific laundering; current decisions

PASS: direct original AUTHOR 100-row tabulation read; exact analytic full under-grid number shares; independent numerical full literal interpolation Simpson; 500/500 cross-table rates/units PASS. NEW quantified, source-rooted risk: ~81.4% source-column hadron counts at j22 rely on EXTRAPOLATION outside the tabulated mass region, while at j62 ~11.1%. This is not news that subgrid impacts limits (BADACZ FIRST); it quantifies *per-PBH hadron count dependency*, which is a different source-observation object.

HOLD: BlackHawk original full `fM.txt` M16 independent source read, full energy-resolved hadron spectra in G_EC+(b), true physical deposited energy G_DEP, coupled BBN native corrected Y and beta. A count ledger cannot substitute for any of these. No direct Julia, no PRyMordial run, no claim independent experiment, no author misconduct or definitive code defect. No new physical PBH constraint or novelty.

**NEXT substantive independent research step by M16**: acquire energy-resolved secondary species spectra or original generator output to compute channel energy-integrals with no primary+secondary double counting and rigorous E_max truncation. Failing that, build a source-based reduced coupled BBN falsifier with explicit model assumptions, NOT call it native Wu–Xu. No more passive waiting; no duplicate owner's prereg outputs mislabelled as M16.

## 7. Executed computation and publicly pinned reproducibility

All calculations were ACTUALLY RUN inside connected JavaScript V8 against directly fetched source bytes. A self-contained, offline JavaScript reproducer was generated from the same executed function source (`independentRecalc.toString()`) with both original raw table snapshots embedded unchanged as JSON literals, and saved to public GitHub. It requires no Internet after checkout; run using Node (`node filename.js`) for the same calculations. The saved code was NOT separately executed by Node in this turn; do not claim such a run. Full Github immutable readback confirmed both embedded complete input tables and copied function:

https://github.com/wmakiela-tech/Nash-iw-research/blob/1c63acfabbf2369aae43f7a04618ff4cbadab387/research/m16/2026-11-23/code/m16_rot014_author_original_subgrid_hadron_fluence_500count_embedded_selfcontained.js
Code Git blob `20d86ca3872d43d08c31351463781f4e0e098f03`, 30,795 UTF-8 characters.

Exact numeric machine certificate 10 rows and all ledgers:
https://github.com/wmakiela-tech/Nash-iw-research/blob/07d822dfc8d92b9a0eb3eba3ba83e7dfeb9fab14/research/m16/2026-11-23/data/m16_rot014_author_source_subgrid_hadron_fluence_certificate.json
Certificate Git blob `821732f18f372bbb63bf3e94504bf9e8d9568ce8`, 6,686 chars. A separately executed minimal physical rest-energy floor test was performed in V8 against original author table, and its values recorded above.

M16_ROT014_ORIGINAL_AUTHOR_HADRON_100ROW_SOURCE_READ / COMPLEMENTARY_SECONDARY_500_NUMBER_RATE_RECEIPTS_PASS / SUBGRID_J22_81P4_PERCENT_NUMBER / SUBGRID_J62_11P1_PERCENT_NUMBER / ANALYTIC_VS_NUMERIC_2ALG_PASS / SLOPE_SENSITIVITY_SOURCE_ONLY / REST_MASS_ENERGY_LOWER_BOUND_TOO_WEAK / G_EC_B_ENERGY_OPEN / NO_AUTHOR_ERROR / NO_NEW_BETA_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_NOT_WRITTEN.
