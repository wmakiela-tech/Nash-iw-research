---
artifact_id: IW_MECH_S9_ROT016_ORIGINAL_WUXU_NATIVE_SIX_HADRON_SIGNED_RHS_EXTRAPOLATED_MASS_EXPOSURE_AND_CONTROL_001_20261113
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
created_at: 2026-11-13
document_type: SOURCE_NATIVE_FROZEN_JULIA_TRAJECTORY_POSTHOC_HADRON_CONVERSION_FORCING_AUDIT
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
scientific_status: NATIVE_ORIGINAL_TRACE_POSTHOC_6RHS_DIRECT_SOURCE_4_QUADRATURE_PASS / NO_NEW_JULIA / B1_ORIGINAL_PHYSICS_HOLD / NO_CANON_NO_EXEC_SIGN
claim_ceiling: ON_PATH_SIGNED_HADRON_RHS_EXPOSURE_NOT_CAUSAL_DELTA_X / NO_NATIVE_ODE_ERROR_CERTIFICATE / NO_PHYSICAL_BBN_OR_PBH_BOUND / NO_FIG5_BUILD_ID / NO_EXTERNAL_E4 / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE
---

# ROT016 — original Wu–Xu 10D source trajectory: where the six native hadronic neutron-conversion terms accumulate

## 1. Original firstness and what is genuinely different

ORIGINAL SCIENTIFIC AUTHORS: Wu and Xu; original frozen Julia source `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`, `arXiv-2509.05618/main-scan.jl` Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`, original six cross-sections `tool_script-parameters.jl` Git blob `0d7198ff3557bdbd5753000bb07a7a7405cc24f5`; first five tabulated rate channels `hadrons_from_PBH.dat` Git blob `06d0883a27b108692720422294ba2baacd381a64`. The original 10D model is the authors' work, not ours, and its final published Fig5 producing environment is not authenticated.

Prior research firstness:
- PRF13 ROT017 FIRST showed **~81.36–81.44% of the original model integrated emitted HADRON NUMBER** at j22 arises from masses below the FIRST original emission table node 1e9 g; LT8 ROT017 FIRST independently checked.
- Mech-S9 ROT012/013 FIRST executed original 10D `magic(;hadrons_output_flag=true)` at j22 beta=10^-16.9974609375 to get one 10k-sample 6-RAW history, source authentic. Mech-S9 ROT015 FIRST identified actual source time-temperature at first table node: time linear between samples ~.09731184823146 s T~2.75681355 MeV; original PBH zero sample8545 time .33751037 s, table extrapolated ~71.17% of source active preev sample-clock and 87.588% of observed live mass decrement (ideal final zero 89.192% separate).
- LT8 FIRST exposed source raw-vs-effective numerical floor; INT9 FIRST derived physical-unit sharp on-path floor correction and then integrated its tiny postev contribution; MT15 and AUD2/REC11 FIRST supplied postev weak-only Duhamel/conditional counterfactual referees. No duplicate floor integration claimed here.

ROT016 DISTINCT QUESTION: on the actual original Wu–Xu **full 10D original SOURCE trajectory** with ALL six original effective hadron state histories and ORIGINAL source `σv(T)` and (X_n), **what fraction of the signed on-path six-hadron neutron-conversion RHS integral is accumulated below the original first 1e9g HADRON EMISSION TABLE node?** This is neither emitted hadron number nor the causal contribution to final neutron fraction. This is explicitly **POSTHOC exploratory**, not preregistered source discovery, and no solver error bounds inferred.

## 2. Exact original source and independent execution

Original native data is UNALTERED real GitHub Actions run `43436800793`, artifact ID `14045176436`, archive ZIP sha256 `71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486`, original raw 10000-row CSV sha256 `45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1`. The archived source source script `main-scan.jl` is frozen; original threshold RHS n_eff=exp(max(lograw,-100)) GeV^3, and original `magic()` return preserves six RAW hadron log profiles. Before PBH evaporation, all original 8544 saved live source history rows are above floor (independently reverified), so effective vs RAW equal there. At first PBH-zero source sample8545, six floor flags switch true and remain true for all 1456 postev rows; this report strictly **DOES NOT TRAPEZOID-INTEGRATE ACROSS THE 8544→8545 PHASE DISCONTINUITY**.

New independent executable **Python 3 STD-LIB ONLY**, public original-source result path
`research/mech-s9/2026-11-13/code/mech_s9_rot016_native_hadron_extrapolated_rhs_exposure_stdlib.py`
Git blob `3da33daf04a8337063a98115f22493b925ebe561`, commit `f54186a70c2ca22713d7dd14cf036187714ac57e`. It:
- pins original archive SHA256 and original native CSV SHA256, ZIP CRC + 16/16 original inner file digests, all 10000 states and six clamp flag columns, exact first PBH zero=8545 and 1e9g crossing bracket original source rows8383–8384;
- derives source GeV³×mbarn→s⁻¹ from defined exact SI `h=6.62607015e−34 Js`, `e=1.602176634e−19 C`, `c=299792458 m/s`, and original `NaturalUnits` reaction types; reproduces original INT9 k0=e^-100 GeV³×1mb = `1.45148683724038e−19 s⁻¹` within 4e−9 relative without importing INT9 code;
- recomputes all 6 native effective hadron conversion contributions independently on the full 10000-source-state grid:
  ```
  F_h(t) = n_pi_minus(1-X)*1.5 Fc_pi(T)
           -n_pi_plus*X*1.7
           +n_K_minus*((1-X)*31 Fc_K(T)-X*26)
           +n_K0L*7*(1-2X)
           -n_pbar*28 X + n_nbar*28*(1-X)
  ```
  where numbers multiply mbarn, native source number densities are GeV³ and SI-derived conversion is applied. No omitted charged/neutral reaction sign. `F_h` is a source on-path instantaneous derivative in s⁻¹; `F_h` computed positive at ALL 8544 original saved live samples but individual species signed pieces can be large and cancel;
- locates the first original mass-table node 1e9g between rows 8383/8384, LINEAR-interpolates time, T, X and `F_h` across that one recorded bracket. The linear bracket is descriptive, NOT exact continuous original ODE event.
- integrates over actual original time from first source row through table crossing, and from the crossing to last PBH-ACTIVE source row8544; separates the source 8544→8545 event jump instead of smearing through it.
- cross-checks left, right, trapezoid and independently coded shape-preserving PCHIP cubic Hermite on nonuniform original source time knots. This is discretization sensitivity, NOT source solver truncation error confidence interval.

ACTUAL Python-only GitHub Actions completed SUCCESS for ALL steps: `43468428634` job `132033663341`; original source ZIP automatically downloaded from GitHub API using same immutable artifact ID `14045176436`, original ZIP outer SHA PASSED. Workflow `.github/workflows/mech-s9-rot016-native-hadron-exposure-stdlib.yml` commit `84faece0ccd77322b3d6dd9d46e2d6c388232ff1`, blob `7648e018e2286504214fb0bcf617a8cf1a65c2d3`. Actual new source audit artifact ID `14058489900` ZIP SHA256 `c575a13c0b613e1a71f449297f68c4ee9b226db8d6956843a1cc950240e55856`, contains ORIGINAL unchanged author artifact ZIP + new result JSON + stdout/negative-control/manifest. Actual downloaded ZIP independently opened, CRC PASS, all FIVE new internal SHA256 source files PASS, original nested ZIP SHA256 PASSED. Original result JSON `ROT016_NATIVE_HADRON_RHS_EXPOSURE.json` was independently read from downloaded artifact in model-container; no unsupported result-copying. GitHub workflow itself executes a negative tampered-original-archive fixture, rejects source-mismatch prior to result, PASS.

## 3. Actual new numerical source results

Source original j22, `M_ini≈1.1211744564709606e9g`, beta=10^-16.9974609375. This `beta=1.0058635310570255e−17` is **0.586% ABOVE original author's original beta_max=1e−17**, valid original `magic()` callable but not original 100×100 scan node (ROT014 prior).

Original first table mass node crossing t≈`0.09731184823146294 s`, T≈`2.756813552886383 MeV`; last source active PBH t≈`.334927351810113 s`; first source zero PBH t=.33751037021169 s NOT integrated over.

| Source on-path six-hadron signed RHS `∫ F_h dt` | Above table mass≥1e9g | Below table mass<1e9g, PBH active | Below-source fraction of ∫ |
|---|---:|---:|---:|
| Left rectangle | +.2899252699709642 | +.7902854140161226 | **73.160303423%** |
| Right rectangle | +.29059158979343175 | +.8005859081116342 | **73.368989889%** |
| Trapezoid | +.29025842988219797 | +.7954356610638784 | **73.265173652%** |
| PCHIP cubic Hermite | +.29025950238602194 | +.7946595967432605 | **73.245977270%** |

This `~73.2–73.4%` observed quadrature family is a **discrete-source numerical sensitivity range only**, NOT a certified continuum range. In particular, do not conflate with PRF13 original-number-emission ~81.4%, original time ~71.17%, or observed mass decrease ~87.59%. Those are different denominators.

Original per-species signed trapezoid contributions above vs below table (dimensionless ∫dX/dt):
| species | ≥1e9g | <1e9g while PBH live |
|---|---:|---:|
| pi− | +1.69831862036225 | +1.24206505862234 |
| pi+ | −1.51610739391266 | −.88089943715763 |
| K− | +.06343949416246 | +.23419533080799 |
| K0_L | +.01134480134094 | +.04205552983213 |
| pbar | −.08403941356029 | −.34984689002314 |
| nbar | +.11730232148951 | +.50786606898219 |

Individual channel integrals exceed total signed net because proton→neutron and neutron→proton channels mostly cancel. Hence percent-of-net cannot be equated to a physically calibrated parameter sensitivity: derivative of final X to an individual rate coefficient needs an actual source-legal intervention and ODE variational/adjoint or new native run; no such run is authorized.

## 4. Independent equation-consistency check on subgrid source segment

Native original source frozen (Q=(939.5654205-938.27208816)) MeV, (	au_n=878.4) s and original weak rate:
```
Γ_n(T) = (255/τn)*(12+6q+q²)/q^5, q=Q/T
F_weak=−Γ_n*[X−(1-X)*exp(−q)] − X/τn .
```
Compute trapezoid on same original source segment from linear table crossing to last PBH-live saved row:
- ∫F_h dt=+0.795435661064,
- ∫F_weak dt=−0.721131799941,
- sum of source RHS trapezoid =+0.074303861123,
- native X last-active minus linearly interpolated table-crossing state =+0.072896920186,
- **RHS quadrature minus source sampled state change =+0.001406940937** (about 1.93% of recorded ΔX). This **nonzero diagnostic residual** is real and kept; does not prove a physical source bug, because interpolation/saved-grid quadrature/source native ODE errors are not fully bounded.
- In particular source table phase `X` can increase while weak part is negative, showing competing reaction terms. The +0.795 integral is NOT `ΔX` attributable to hadrons and not the perturbation derivative of final code Y.

## 5. What this discriminates, and why B1 holds

It shows, for **ONE** authentic old historical Wu–Xu native 10D point, most **signed on-path hadronic neutron-conversion RHS area**, not just emitted hadron *counts*, lies in the portion of author code that uses log-log rate extrapolation below its FIRST original tabulated mass. This is original-source reproducibility and a concrete question about external hadronization inputs, not a new physical constraint. It is not evidence that all beta/mass combinations share this ratio, nor a verified distribution of hadronization uncertainty.

30-day Moderator-accepted B1 Test S protocol `IW_NASH_30_DAY_EXTERNAL_RESULT_DECISION_PROTOCOL_001_20261113`, private commit `ffc0d011706617aeb38ea90abd62f40626353fad`, §E still requires Moderator per-native-Julia-run authorization. Mech-S9 ROT014 and Badacz separate receipt native co-owner verified; INT9 ROT025 recognizes original `q=Q/T` scalar output mapping (primary source `X_n(T0)`, code `Y_code=2X/(1-X)` secondary only) as proposed target, not frozen by Moderator. This ROT016 contains ZERO new Julia source solver calls, no source physical equation modifications, and makes NO direct B1 externally novel claim. No original independent BlackHawk/PYTHIA generator uncertainty/mass-downstream calibration provided; no meaningful physical rate perturbation envelope can be assigned simply from source extrapolation.

**Scientific status:** `ROT016_SOURCE_NATIVE_HADRON_SIGNED_RHS_73P3_PERCENT_POSTHOC_REPRO_PASS / ALL_6_RATE_CHANNELS_PRESENT / MASS_NODE_EVENT_BOUNDARY_EXCLUDED / LITERATURE_FIRSTNESS_PRESERVED / NO_NEW_JULIA / B1_INPUT_SOURCE_HOLD / NO_PHYSICAL_PBH_BOUND / NO_E4 / NO_FIG5_BUILD_ID / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`. This public GitHub report is not BW ingestion; `GITHUB_PENDING_BW_INGEST`.
