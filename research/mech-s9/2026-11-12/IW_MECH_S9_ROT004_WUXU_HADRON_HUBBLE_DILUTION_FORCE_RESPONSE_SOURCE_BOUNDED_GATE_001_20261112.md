---
artifact_id: IW_MECH_S9_ROT004_WUXU_HADRON_HUBBLE_DILUTION_FORCE_RESPONSE_SOURCE_BOUNDED_GATE_001_20261112
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
date: 2026-11-12
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
document_type: SCIENCE_FIRST_SOURCE_BOUNDED_SCALAR_MECHANISM_GUARD
claim_ceiling: NO_NATIVE_JULIA_RUN / NO_JCAP_EXEC_BUILD_ID / NO_NATIVE_HADRON_EFFECT_Yp / NO_PBH_BOUND / NO_PHYSICAL_UPGRADE / E4_SOURCE_BLOCK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE
---

# ROT004 — source-native Wu–Xu hadron dilution: prove what is small, and what is not

## 0. Currentness, firstness, and scientific decision

Latest independently read primary IW evidence: REC11 ROT021 actually rechecked the Mech-S9 ROT002 original **1000-row** zero-PBH rho/entropy mismatch, including exact-decimal 776 positive / 223 negative local source intervals and a separate source inverse interpolation test (journal build and physical sector semantics remain open). KN13 ROT017 independently compared original 1000-row EoS via knot-Simpson and 100-row original hadron number table; original five rate channels have 495/495 decreasing adjacent pairs (not a full spectrum validation). INT9 ROT016 source-typed mapping of earlier Mech-S9 ROT002/003 entropy and comoving nB issues into conditional native nPBH dilution at historical T0 and calibrated T1. Credit earliest work to its owners. Badacz PREREG062 original C1–C4 Julia S1 still last verified failed on points-file '#' parser **before magic/ODE**; do not infer D1 results. No independent referee, source E4 or final journal Fig5 identity has been established for ROT004.

New question (raised as material open possibility in Mech-S9 ROT003): the original 10D code evolves **physical** emitted hadron density states without a `-3H n_h` dilution sink. Is expansion of the same order as source nuclear collision/decay sinks at late BBN, or quantitatively much slower under a well-specified control background? The correct disposition is a conditional **positive timescale bound and exact forced scalar response**, NOT an unsupported physical bug or Yp effect.

## 1. Author and independent-source anchors

Authors Wu–Xu original Git repo `Fenyutanchan/Primordial-Black-Hole` at original frozen commit `d395183674cace6c9906a8911bdeb7234ba4040d`. Original `arXiv-2509.05618/main-scan.jl`, Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`:
- lines 39–60 define physical `n_PBH=n_PBH_ini*(a_ini/a)^3` and all 10D logs of hadron number densities;
- lines 64–65 `n_gamma=2 zeta(3) T_SM^3/pi^2` and `n_B=eta_B n_gamma`;
- lines 72–75 `H=sqrt((rho_SM+rho_PBH)/(3*NU.M_Pl^2))`;
- lines 102–128 original 6 physical hadron source/loss ODEs, **without a separate `-3H*n_h`**;
- lines 131–140 source ODE implementation `du[5:10]=d n_h/dt / (H n_h)` with log physical-density coordinates and `eta=ln a`.
Original `tool_script-parameters.jl` blob `0d7198ff3557bdbd5753000bb07a7a7405cc24f5`: `eta_B=6.1e-10`; `Gamma_pi=1/(2.6033e-8s)`, `Gamma_Kminus=8.1e7s^-1`, `Gamma_K0L=2.0e7s^-1`, `sigma_v_antiN=28` or `37 mbarn` for proton/neutron target depending on X, with `barn=1e-28m^2` and `mbarn=1e-31m^2`. Requires physically admissible `0<=X_n<=1`.
Original `tool_script-N_relativistic_species.jl` blob `0437c032bdc4bafca6cb634c0db4cd2c46fb7efc`: low-energy source `g_rho(T)` linear in `ln T`; original 1000-row CSV `data/ext/N_around_m_e.csv`, Git blob `93f2494f026c5d0587ea40fe08bb938dd9d01fa8`.

Independent dimensional conversion is from NIST/CODATA2022 (not a claim that we executed `NU.M_Pl` in Julia): `G_N=6.70883e-39 GeV^-2`, `hbar=6.582119569e-25 GeV s`, `hbar*c=197.3269804 MeV fm`, `c=299792458 m/s`. Primary <https://physics.nist.gov/cuu/pdf/JPCRD2022CODATA.pdf> and <https://physics.nist.gov/cgi-bin/cuu/Value?hbcmevf%7Csearch_for=vacuum>. Standard reduced Planck convention `Mred=(8*pi*G_N)^(-1/2)`. We use exact-in-source radiation-only `rho_rad=(pi^2/30) g_rho T^4` as a **controlled approximate physical background**, not a literal 10D Julia-run `H`.

## 2. Correct forced equations and exact kernel

For any one hadron species `h` treated as **physical number density** and under the same predeclared `T(t),H(t),X_n(t),m_PBH(t),n_B(t),J_h(t)` in BOTH comparators, original source reads:
```
SOURCE:   d n0/dt = J(t) - lambda(t) n0
DILUTED:  d n3/dt = J(t) - [lambda(t)+3H(t)] n3
```
Here `lambda(t)>=0` is the source collision/decay sink (source pions/kaons/antibaryons), `J>=0` the source injection, with identical nonnegative initial density. Source code omits exactly the standard `-3H n_h` physical-volume dilution term; if `n_h` were intended comoving instead, the explicit native injection, scattering and thermodynamic units must be reconciled first, not inferred.

Subtracting gives the **exact forced identity**:
```
Delta(t)=n0(t)-n3(t)
        =integral_[ti,t] 3H(s)*n3(s)*exp[-integral_[s,t]lambda(u)du] ds  >=0.
```
Consequently if `H(s)<=Hmax` and `lambda(s)>=lambdaMin>0` for every s in the entire chosen interval:
```
0 <= Delta(t) <= [3Hmax/lambdaMin]*sup_[ti,t] n3.
```
This is an **absolute error relative to the maximum density in the past interval**, NOT a general percent error relative to instantaneous `n3(t)`, nor any full coupled Yp/BBN result. It holds even with rapidly time-varying nonnegative injections, provided all other trajectories are forced equal.

Constant coefficients, constant `J`, zero initial density give exact:
```
n0=J*(1-exp(-lambda*t))/lambda
n3=J*(1-exp(-(lambda+3H)*t))/(lambda+3H)
steady fractional reduction  [n0-n3]/n0 =3H/(lambda+3H).
```
The familiar `3H/lambda` is a **local steady / rate ratio**, not an unrestricted trajectory perturbation theorem. Counterexample to a misleading relative-transfer claim: if source injects only near `t_i`, after lapse `tau` the ratio is `n3/n0=exp(-3H*tau)` regardless of how large lambda/H is, although both surviving densities are exponentially small when lambda*tau is large.

## 3. Frozen actual 1000-row source numeric ratio — no PBH domination

Under `rho_PBH=0`, `Hrad(T)=(pi/sqrt(90))*sqrt(g_rho(T))*T^2/Mred` in natural units. Independent SI rate `lambda_anti_min=28 mbarn*c*n_B(T)`, source `n_B=6.1e-10*(2zeta3/pi^2)*(T/hbarc)^3`. The original six RHS have:
- pion `lambda_pi>=Gamma_pi`;
- charged K `lambda_Kminus>=8.1e7 s^-1`;
- K0L `lambda_K0L>=2e7 s^-1`;
- two antibaryon types `lambda_antinucleon>=28mbarn*c*n_B` **if** `0<=X_n<=1`.

The source original `g_rho(T)` was DIRECTLY read and interpolated in JS; grid count 1000. The temperatures below are source-dependent static rate ratios, NOT author-native Julia output:

| `T` MeV | `Hrad` s^-1 | `lambda_anti_min` s^-1 | `3Hrad/lambda_anti_min` |
|---:|---:|---:|---:|
| 1.0 | 0.671291 | 1.6233211e7 | 1.240588e-7 |
| 0.5 | 0.163374 | 2.0291514e6 | 2.415406e-7 |
| 0.2 | 0.0223441 | 1.2986569e5 | 5.161667e-7 |
| 0.1 | 0.00428507 | 1.6233211e4 | 7.919075e-7 |
| 0.099688851247 (Badacz native T1 reported in prior cell) | 0.00425369 | 1.6082154e4 | 7.934918e-7 |
| 0.0781852706883 (historical code T0) | 0.00243646 | 7.7585269e3 | 9.421089e-7 |
| 0.05 | 0.000950368 | 2.0291514e3 | 1.405071e-6 |
| 0.03 | 0.000341110 | 4.3829670e2 | 2.334786e-6 |

**GLOBAL SOURCE INTERVAL GATE** for every `T in [0.03,1] MeV` under these same source-defined radiation-only assumptions: native log-T piecewise interpolation has `g_rho(T)<=10.55866630203338` on that interval (including both endpoints and all knots), from source CSV. Since `3Hrad/lambda_anti_min=C sqrt(g_rho(T))/T`, a rigorous conservative continuous-interval upper bound is:
```
3Hrad/lambda_anti_min <= 4.13529284849e-6     (all T in [0.03,1] MeV).
3Hrad/Gamma_pi <= 5.2427141531e-8.
3Hrad/Gamma_K0L <= 1.0069362258e-7.
```
A distinct, valid-for-forced-histories **absolute memory bound** uses extrema `Hmax=0.6712908172 s^-1` and `lambda_anti_min_over_interval=438.2966994 s^-1`, so
```
0 <= n_source_no_dil(t) - n_corrected_3H(t)
   <= 0.004594769832 * sup_[ti,t] n_corrected_3H(s)
```
for any time interval whose forced `T(s)` remains in [0.03,1] MeV, if `H=Hrad(T)`, `0<=X_n<=1`, and injection nonnegative, and the sources/initial conditions are matched. **0.46% of historical supremum does not bound the fraction of the current density, the exact full 10D nonlinear difference, or Yp.** The bound covers the full continuous interpolation domain; the maximum over 557 knots is about 2.334786e-6 at 0.03MeV, NOT advertised as a proof of continuous true maximum.

When the original author's PBH component `f=rho_PBH/rho_SM>=0` is present, **at the same T with source n_B unchanged**:
```
H=Hrad*sqrt(1+f),  3H/lambda = (3Hrad/lambda)*sqrt(1+f).
```
For example at historical `T0`, the pointwise 3H/lambda_anti_min reaches unity only at `f≈1.1266727e12`, a **pure dimensionless conditional threshold**. No claim that original benchmark PBH solutions reach or fail to reach it; original `f(T)` must come from actual 10D output. The source `rho_SM` EOS and `n_B` mean earlier Mech-S9 ROT002/003 corrections can modify this comparison. No extrapolation to earlier high-temperature / extreme-PBH epochs is authorized.

## 4. Scientific disposition and falsifiers

**Bounded result:** omission of `-3H n_h` is a SOURCE-LEVEL bookkeeping distinction; at late 0.03–1MeV under radiation domination, original source rates imply a strong fast-interaction timescale separation. It is therefore **not justified to classify this as an O(1) helium/PBH defect** on the evidence in hand. In fact the closed forced scalar comparator gives a small conservative supremum-relative effect under stated assumptions. This is a *genuine partial negative result*, not a full physics rescue.

Falsifying applicability: any actual native 10D interval with `rho_PBH/rho_SM` large enough, `T` outside declared band, `n_B` physically redefined, `X_n` outside physical range, slow source memory, negative/nonmonotone effective sink, or coupled `J,lambda,H` changes violates the numeric gate's assumptions. To assess genuine Yp effects, first compare the six collision sinks with actual original source effective rates at matched native T/hadron histories; then an owner-authorized full nonlinear source replay including Hubble dilution (NOT automatically scheduled) is required. The original S1 Julia parser blocker and physical E4 validation remain independently open.

The **material higher-priority candidate** remains ROT002/003 background/entropy and baryon-number normalization: earlier source n_B differs by factors up to 2.85 at 1MeV under late calibration, while ROT004 shows that neglecting 3H alone is parametrically much smaller than baryon collision removal rates under radiation-only late BBN. This is a *comparison of conditional source controls*, not an ordering of verified physical Yp correction effects.

## 5. Execution and custody

Actual executed computations: original-author 1000-row `N_around_m_e.csv` fetched from pinned source and numerically evaluated in connected JavaScript in this rotation; all 557 relevant original knots/endpoints checked for global g_rho interval bound; exact formula comparison for all 6 source channels; separate container SymPy constant-source forced solution: source and diluted ODE residual PASS and stationary reduction identity PASS. This is NOT native Julia; no full 10D solution, original physical hadron spectra replay, author NPZ/JLD2 evaluation, no new BlackHawk/PYTHIA E4 and no PBH beta limit.

Public, source-Git-blob-locked Node reproducibility companion:
`research/mech-s9/2026-11-12/mech_s9_rot004_source_hadron_dilution_gate.mjs`. It checks Git blob SHA1, 1000-row source structure, values, all 557 original source knots/endpoints, conservative continuum source g_rho envelope, exact constant-J synthetic gate; **companion Node CLI itself not executed in this rotation**. This report and code are awaiting BW source-only ingestion if separate custodian elects to ingest. GitHub write and pinned readback must be checked; CI outcomes are not scientific peer review.

`ROT004 = SOURCE_HADRON_3H_MISSING_CONFIRMED_CONDITIONAL / RADIATION_BACKGROUND_FAST_HADRON_RATE_POSITIVE_GATE / EXACT_FORCED_COMPARISON_PROVED / RIGOROUS_WHOLE_INTERVAL_ENVELOPE / NO_FULL_10D_Yp / REFEREE_PENDING / GITHUB_PENDING_BW_INGEST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
