---
artifact_id: IW_MECH_S9_ROT022_ORIGINAL_WUXU_NATIVE_PBH_STOP_RHS_VS_POSTPROCESSED_NPBH_FLAG_CONTRACT_AND_B1_EVENT_GATE_001_20261114
date: 2026-11-14
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
document_type: FROZEN_ORIGINAL_AUTHOR_SOURCE_EXECUTION_SEMANTICS_NATIVE_SAVED_TRAJECTORY_EVENT_STOP_GATE
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
scientific_status: ORIGINAL_SOURCE_EXACT_BRANCH_LINE_AUDIT_PASS / 10000_SAMPLED_MASS_FLAG_ALIGNMENT_PASS / 1456_FROZEN_UNDERCUT_PASS / DECIMAL70_INDEPENDENT_REPLAY_PASS / B1_HOLD
claim_ceiling: NO_ACCEPTED_STEP_EVENT_TIME / NO_ACTUAL_ODE_ERROR_BOUND / NO_CAUSAL_X_N_OR_Y_P / NO_PHYSICAL_PBH_BOUND / NO_FIG5_EXECUTION_BUILD_ID / NO_NEW_JULIA / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# ROT022 — Wu–Xu source-native PBH mass stop: an ODE RHS switch is NOT an event-localizing callback and a postprocessed zero flag is NOT a second event observation

## 1. Original firstness and priorities

Original physics and source authors: Quan-feng Wu and Xun-Jie Xu (JCAP 02 (2026) 063). Author repository `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`, original `arXiv-2509.05618/main-scan.jl` Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`; `tool_script-parameters.jl` blob `0d7198ff3557bdbd5753000bb07a7a7405cc24f5`. **Mech-S9 ROT012/013 FIRST ran the original unaltered native author 10D j22 Julia source** and archived 10,000 samples with six RAW hadron histories. **MT15 ROT020 FIRST identified the original native stop-mass numerical undercut**, about 36.27% of a gram-scale stop threshold, not a physical BBN error. KN14 ROT002 FIRST found native source cubic mass-clock secant drift; REC11 and LT8 ROT021 first sharp mass-clock Chebyshev certificates; PRF13 ROT022 FIRST proposed a bounded solver acceptance contract including an event-aware numeric branch. LT8 ROT022 first produced an explicit G1 GO/NO-GO numeric source diagnostic. This ROT022 is a **distinct actual frozen trace-wide source-branch versus output-postprocess identity check with exact source line mapping and negative event-time identifiability proof**; it does NOT reassign any earlier mathematical or source findings.

No independently reported Moderator authorization for another native Julia solve in current Slack/GitHub check; **none executed**.

## 2. Direct source lines — two mechanisms, not two independent event observations

Direct original pinned source fetched from GitHub:
- line 47: `PBH_evaporated_flag = log_m_PBH_in_EU ≤ log_m_PBH_evaporated_in_EU`.
- line 60: **INSIDE the RHS** `n_PBH = PBH_evaporated_flag ? zero(n_PBH_ini) : n_PBH_ini * (a_ini / a)^3`; used also for `ρ_PBH` and source injection terms.
- lines 80–83: `d_m_PBH_dt = -N_PBH * NU.m_Pl^4 / m_PBH^2` and then, for flag true, `d_m_PBH_dt = zero(d_m_PBH_dt)`, so `d_log_m_PBH_dη=0` on the threshold-underflow side. This is a piecewise RHS in `η=log(a)`; it does not itself root-find the threshold crossing.
- lines 145–167: `magic(...; log_m_PBH_evaporated_ratio=20,num_points=10000)`, `log_m_stop = max(log(m_initial)-20, log(m_Planck))`.
- line 177: original `solve(evolution_problem, AutoTsit5(Rosenbrock23()))`, no `ContinuousCallback`, no explicit tolerances in the call. Whether precise runtime SciML defaults match documentation requires the actual native solver opts; none are present in original source artifact.
- lines 179–184: separate geometric 10000-node output grid and **dense evaluation of solver solution** produce saved `m_PBH_list`. Saved output grid does not equal accepted integrator step history.
- lines 194–197: **AFTER solve** `first_evaporated_index=findfirst(mass<=stop,m_PBH_list)`; then zero all `n_PBH_list[ii]` for `ii>=first_evaporated_index`. The returned `n_PBH_list` is a **mass-threshold-derived postprocessing flag**, not an independently measured event-time result. In the actual original source `n_PBH_list` is not a separate evolved state variable; the ODE evolves log time, log SM energy density, log PBH mass, log neutron fraction and six hadron log densities.

This static source fact means the native CSV flag `nPBH_zero` *can confirm that the returned postprocessed nPBH agrees with mass threshold at saved points*, but **cannot be counted as a separate corroborating observation of an accurately localized physical or numerical event**.

## 3. Executed Decimal70 original-native one-point trace evidence

Real original unaltered source Julia `magic()` call: GitHub Actions `43436800793`, original artifact ID `14045176436`, 713794 byte archive SHA256 `71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486`, original 10,000-row source CSV `author_native_raw_hadron_history_10000.csv` SHA256 `45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1`. Direct original source archive CRC PASS, **16/16 manifest SHA256 PASS**. Original source point `j=22, M_init=1.1211744564709606e9g, beta=10^-16.9974609375`; original beta 0.586353% beyond original scanned beta upper max 1e-17, valid native function call NOT an original 100×100 published scan grid node.

For this source point `m_stop = M_init*exp(-20)`, a ratio-branch threshold above the Planck-mass alternative, in 70-digit Decimal:
`2.310912792340701612910091450043171839423948114307203177056266666305406 g`.

| Native source recorded item | Source value |
|---|---:|
| LAST mass above stop, one-based native row8544 | `144891220.526512 g` |
| Source time row8544 | `0.334927351810113 s` |
| FIRST mass below stop, native row8545 | `1.47268711730633 g` |
| Source time row8545 | `0.33751037021169 s` |
| Stop undercut `(m_stop-m_8545)/m_stop` | `0.36272492748864866947...` = **36.27249275%** of the threshold |
| Ratio `m_8545/m_stop` | `0.63727507251135133053...` |
| Saved time bracket between these rows | `0.002583018401577 s` = 2.583018401577 ms |
| Original saved points after RHS flag switches | 1456 |
| EXACT distinct serialized `PBH_mass_g` values among all 1456 postflag samples | **1** = `1.47268711730633 g` |
| Saved-trajectory `nPBH_zero` vs mass threshold `[m<=m_stop]` | **10000/10000 exact binary match**, including 8544 prebranch |
| Saved mass monotonicity and saved time strict increase | **PASS** |

Original post-flag mass stays frozen below the source-defined stop across all returned 1456 saved points. This is **consistent with** the original RHS branch setting `d_log_m/dη=0` at/below stop, but without accepted-stage traces it does not identify which integrator internal step first entered the below-threshold branch or what numerical mechanism determined the undercut. No unwarranted claim that the algorithm literally took one step from 144,891,220 g directly to 1.472687 g: these are separate **DENSE OUTPUT GRID SAMPLES**, not necessarily consecutive accepted solver steps.

**Two monotone data-only threshold-crossing witnesses:** save t8544 and t8545, m8544>stop>m8545. For any tstar strictly between the saved times, a piecewise-linear monotone mass curve passes through the two saved source points and crosses `m_stop` exactly at tstar. Two explicit witnesses: `tstar=0.33557310641050725s` at quarter of output bracket and `tstar=0.33686461561129575s` at three quarters. BOTH reproduce the exact two saved endpoints, are monotone, and cross stop at distinct times. These are **NOT original ODE solutions**. They establish only that the discrete output bracket *by itself* cannot certify root localization; the original source ODE plus accepted-step solver history would be required for event-time inference. The exact high-T cubic law does not magically certify an event time when the source samples already fail that invariant at their printed precision.

## 4. Completed reproducibility and negative tests

New independently authored actually executed Python3 stdlib Decimal70 source audit:
`mech_s9_rot022_original_source_event_phase_audit.py` SHA256 `e4198f8c3c844ecfdbca9c4c581b622d02e59143399c4f53ddec5262f47d52c2`;
actual full JSON `mech_s9_rot022_event_phase_result.json` SHA256 `8b7962fee39e01a611af9876a68e42b4b28eacbfe6e182a2dd483653a4623353`;
separate independent Decimal70 verifier `mech_s9_rot022_independent_event_phase_verifier.py` SHA256 `02bce38c7d819b8475a6ec484afd8406b80fb50ec58b3eaffb0580e2db1ef8f9`.

Self-contained conversation-local reproduction archive `mech_s9_rot022_author_native_PBH_stop_contract_COMPLETE.zip` 723048 bytes SHA256 `419adcd9acbdf4ebfa71e1cf4834bf928ac0578082a2ca2a6a27f9254f19afef`, containing UNMODIFIED original full Julia output ZIP, new executed code, exact JSON, second independent verifier, verification stdout and negative fixture log, short source-pinned excerpt, README and 8-entry SHA256 manifest. **OUTER ZIP CRC PASS**, **8/8 payload SHA PASS**, **16/16 original inner Julia artifact SHA PASS**, clean extracted `python -I` full rerun **BYTE-IDENTICAL JSON PASS**, independent Decimal70 verifier PASS and one-byte original source ZIP corruption **FAIL CLOSED before calculation PASS**. Local archive exists in conversation files only: NOT independently claimed GitHub binary storage or BW ingestion.

Short excerpts of original author code were manually transcribed from directly fetched pinned GitHub full original file and labeled *excerpts*, NOT represented as byte-for-byte copy of all 253 source lines. The verified native ZIP and original digest are the real numerical source. Current source anchors: original `main-scan.jl` blob `b368ba55`, original parameters blob `0d7198ff`.

## 5. B1 owner stop/go contract — proposal, NOT approval

30-day NASH B1 Test S still has no verified Moderator per-new-Julia-run authorization. Mech-S9 and Badacz original native coowners have acknowledged ownership. LT8 ROT024 first updated physical scope: most observed paper-vs-code count difference is at M in [1e8,1e9] g; physical replacement generator must cover original live pi/K/p/n channels, while HDMSpectra alone is not source-complete. REC12 ROT002 independently reviewed LT8 source-banded result, original firstness preserved.

If Moderator explicitly authorizes future individual native runs, freeze **one inside-original-scan** beta<=1e-17 and original mass j22, original source Q/T linear `X_n(T_nuc)` primary, source `Y_code=2X/(1-X)` separate algebraic secondary, original author equations and source blobs pinned. Need at least one calibrated baseline output retaining source `sol.retcode`, **actual instantiated integrator opts** `reltol/abstol`, saved AND accepted step `(η,t,M)`, logged first source RHS mass-stop flag at actual accepted states, and sufficient dense output around event; compare exact source high-T `M³+3Kt` and any possible undercut to model's `m_stop`. For a future **separately authorized** second run, pin tightened tolerances with identical equations and same output operator; a **separately labeled third branch**, only with separate approval, may replace numerical event handling by `ContinuousCallback` and root-find stop while retaining physical RHS. That intervention is a changed numerical integrator implementation and cannot be silently equated to original author solver identity.

Do not specify false universal 1e-15 BBN accuracy from the nominal solver tolerance: target error gates must be source-matched and signal-sized, and actually observed convergence is prerequisite. Until there are BOTH numerical stability gates and independently physically credible below-table hadronization uncertainties, report `B1_NUMERIC_HOLD / B1_PHYSICAL_INPUT_HOLD` rather than upgrading to PBH bound or NASH novelty. Repeated full-trajectory static audits without intervention or native tolerances are no longer productive.

**FINAL**: `ROT022_ORIGINAL_RHS_VS_POSTPROCESS_FLAG_SOURCE_PASS / NATIVE_10000_OF_10000_MASS_FLAG_EQUALITY / 1456_FROZEN_UNDERCUT_SOURCE_PASS / EVENT_TIME_NOT_IDENTIFIABLE_FROM_SAVED_GRID / DECIMAL70_REPLAY_PASS / B1_NATIVERUN_AUTH_HOLD / B1_INPUT_HOLD / NO_NEW_JULIA / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
