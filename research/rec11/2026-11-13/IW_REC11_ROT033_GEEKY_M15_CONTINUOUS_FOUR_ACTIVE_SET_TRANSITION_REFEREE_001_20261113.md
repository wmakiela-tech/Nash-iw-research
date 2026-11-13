---
artifact_id: IW_REC11_ROT033_GEEKY_M15_CONTINUOUS_FOUR_ACTIVE_SET_TRANSITION_REFEREE_001_20261113
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
date: 2026-11-13
review_type: I1_NONBLIND_INDEPENDENT_EXACT_25D_COEFFICIENT_BOX_RATIONAL_REFEREE
status: PASS_ALL_FOUR_SOURCE_WIDE_PHASE_THRESHOLDS / PASS_NO_HIDDEN_ACTIVE_REACTIVATIONS
claim_ceiling: M13_N41_B_AUXILIARY_QUARTIC_ONLY / NO_HISTORICAL_RUNTIME_BYTE_ID / NO_FIELD_REALIZABILITY / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
bw_receipt: UNVERIFIED
---

# REC11 ROT033 — complete source-robust continuous active-shell gain-calibration phase diagram

## 1. Sources and firstness

- **M13 ORIGINAL SOURCE FIRST:** `research/m13/2026-10-26/direct_B.json` from `wmakiela-tech/Nash-iw-research`, Git blob `a6f50fbe5904e580e84c87ee87c5ad043cdec5d0`, five masks, 25 directed quartic coefficient pairs.
- **Geeky-S12 ROT015/016/017 ORIGINAL THEOREM FIRST:** projective zero-fit threshold (ROT015), exact positive two-shell risk at 6.6% (ROT016), classical convex finite active-set solver and four discrete 5/4/3/2 regimes (ROT017). Original ROT017 pinned: https://github.com/wmakiela-tech/Nash-iw-research/blob/eb154a99ac9c724b370b8031840dfe71dd445a5b/research/geeky-s12/2026-11-13/IW_GEEKY_S12_ROT017_UNIVERSAL_FINITE_ACTIVE_SET_AND_FOUR_ROBUST_SHELL_REGIMES_001_20261113.md , original blob `6b5238defd8c6b6fc0ee1fad3e6d0dc1f5e882bf`.
- **M15 ROT009 FIRST INDEPENDENT FOUR-DISCRETE-SOURCE-BOX REVIEW** with native original rational BigInt implementation, pinned https://github.com/wmakiela-tech/Nash-iw-research/blob/7ce1f923dd98e080af245f7ded9550abd7bff30d/research/m15/2026-11-13/IW_M15_ROT009_INDEPENDENT_FOUR_M13_B25_SOURCE_ACTIVE_SET_RISK_REFEREE_001_20261113.md , blob `fb063558929610c6c029c4dc87c6c06d0a1dabae`.
- **REC11 NEW IN THIS ROTATION:** exact quadratic equations for every possible active-shell dropout, rigorously certified positions of ALL transitions for EVERY choice of 25 source-box coefficients, and a theorem forbidding any other transition along the continuous `kappa` axis. This is a classical mathematics result scoped only to the source model, no general novelty claim.

The source extraction CSV 25-row original decimal interval endpoints is byte-for-byte equal to the original source, pinned existing REC11 ROT029 CSV Git blob `09824281d5e4b3c87446be97b0e52ace3b33edae`, SHA256 `fb82f6d4b7554791836c026aacaad28040f0c92cbf211023b89011764632f8f2`. Original M13 source directly fetched and verified this ROT; no synthetic replacement or historical producer substitution.

## 2. Frozen mathematical contract

M13 N41 B, masks k=2,3,4,5,6; disjoint shell weights
`W=(7778,6938,6146,5402,24389)`; `alpha=1/20`, `beta=3/40`. All 25 independent source coefficient perturbations lie in `[lo−eps*max(|lo|,|hi|), hi+eps*max(|lo|,|hi|)]`, `eps=1/10000000`. For shell signals `s_i` define `r_i=s_i(alpha)/s_i(beta)>0`, `A_i=W_i s_i(beta)^2>0`. Gain nuisance: one common positive `c>0` plus five independent relative gains `eta_i∈[-kappa,kappa]`, `0<=kappa<1`.

Exactly profiled convex loss (owner Geeky ROT017 original)
```
Phi_kappa(c)=SUM_i A_i max( r_i−(1+kappa)c, (1−kappa)c−r_i, 0 )².
```

Independent SOURCE-WIDE exact Fraction interval signs show `0<r1<r2<r3<r4<r5<2r1`, and at kappa=0 the positive optimum `c0` obeys `r4<c0<r5`.

## 3. New global continuous phase theorem and four source-wide brackets

For EVERY simultaneous selection of all 25 coefficients from their independent source intervals, there are strictly ordered thresholds
```
0 < kappa4 < kappa3 < kappa2 < kappa_crit < 1,
kappa_crit=(r5−r1)/(r5+r1).
```
As kappa grows from 0, the **strictly nonzero-residual active set** changes in this and ONLY this order:
```
[0,kappa4):   LOW 1,2,3,4 ; HIGH 5   (five active)
(kappa4,kappa3): LOW 1,2,3 ; HIGH 5 (four active)
(kappa3,kappa2): LOW 1,2 ; HIGH 5  (three active)
(kappa2,kappa_crit): LOW 1 ; HIGH 5 (two active)
[kappa_crit,1): all zero residual (zero optimized risk).
```
At the three leaving-shell boundaries the newly inactive shell has zero residual, so the change is continuous. At kappa_crit exact zero becomes feasible.

All four thresholds have **EXACT source-wide RATIONAL strict certificates**: at each asserted lower threshold the complete interval evaluation gives F_j<0, and at each asserted upper F_j>0. The corresponding rigorously conservative numeric displays are

| Source event | strict lower kappa | strict upper kappa | source midpoint strict decimal bracket |
|---|---:|---:|---|
| Shell 4 becomes inactive | .0191773556 | .0191825400 | [.0191799477,.0191799478] |
| Shell 3 becomes inactive | .0484029543 | .0484073978 | [.0484051760,.0484051761] |
| Shell 2 becomes inactive | .0616428704 | .0616468486 | [.0616448594,.0616448595] |
| Zero-risk fit | .0662678476 | .0662713468 | source-dependent rational formula |

**The endpoints are robust enclosures, not claimed attainable global extrema** across the 25-dimensional box. All original source intervals exact decimal-to-Fraction, no binary64 sign decision.

## 4. Analytic proof — no missed transitions

Set `t=(1+kappa)/(1−kappa)`. At the transition of low shell j∈{4,3,2}, its residual becomes `r_j=(1−kappa)c*`. All lower-index shells 1,...,j−1 are low active, and only shell5 high active. The exact global convex stationary equation leads to the quadratic:
```
F_j(t)=r_j*t²−r5*t+ SUM_(i<j)[ A_i(r_j−r_i)/A5 ]=0.
```
On `1<=t<=r5/r1`, `F'_j(t)=2r_j*t−r5>0` since `r5<2r1<=2r_j`; thus there is precisely one root for each leaving shell. The fully source-box-certified negative-to-positive rational threshold signs above identify the roots and their **strict order** (shell4, shell3, shell2) before the zero-loss threshold.

For any nonempty low active prefix L and the sole high shell5, let `B=Σ_(i∈L)A_i`, `S=Σ_(i∈L)A_i r_i`, `V=A5`, `R=r5`. The exact optimized source band's left/right fitted edges are:
```
Ledge=(1−kappa)c* = (S+t V R)/(B+t² V),
Redge=(1+kappa)c* = t*Ledge.
```
Differentiate exactly:
```
dLedge/dt= V*(R*B−2t*S−t²*V*R)/(B+t²*V)² < 0,
dRedge/dt=[S*B+t*V*(2R*B−t*S)]/(B+t²*V)² >0.
```
The first is strict from `S>=B*r1`, `r5<2r1`, `t>=1`. The second is strict from `S<=B*r5` and `t<=r5/r1<2`. Thus the zero-residual band grows monotonically, without reactivation of any departed shell. Shell1 low and shell5 high remain necessary until their feasible intervals first meet exactly at `kappa_crit`. No other sequence is possible.

Within every nonzero-risk phase, the exact minimized cost is the piecewise rational expression, with `u=1−kappa,v=1+kappa`:
```
c*_L=(u Σ_L A_i r_i+v A5 r5)/(u² Σ_L A_i+v² A5),
Dmin²=(Σ_L A_i r_i² +A5 r5²)−(u Σ_L A_i r_i+v A5 r5)²/(u² Σ_L A_i+v² A5).
```
At kappa>=kcrit take any `c∈[r5/(1+kappa),r1/(1−kappa)]` to get exact zero cost. Floating cancellation in the near-critical risk formula is NOT a proof; use exact fractions / positive wedge formulas.

## 5. Actually executed independent checks and reproducibility

**New independent stdlib Python Fraction interval proof** `verify_phase_transitions.py` authenticates original 25 source CSV bytes SHA256 first; proves source-wide strict shell positivity/order/r5<2r1/initial active branch; three strict lower/upper F_j signs at rational thresholds; strict threshold order and global zero loss. Its output original `result.json` is exact source-typed data, not sampled Monte Carlo.

**SECOND independent exact global optimizer**, previous REC11 author code `independent_hinge_enumerator.py`, enumerates all finite hinge breakpoints and local quadratic minima without using the threshold formula. New `crosscheck_transition_boundaries.py` performed **56/56 exact rational global optimality checks** at lower/upper sides of all four transitions for 7 honest source corner/midpoint configurations. Those checks support the analytic proof; **not** a substitute for the full source-box certificate.

Original midpoint numeric risk displays (units `10^24 Dmin²`): kappa=0 =>.5777405816626439 five; .01=>.3963312262683772 five; .03=>.1451241289101239 four; .04=>.06844974153629062 four; .05=>.02278507747688921 three; .06=>.002508065892101818 three; .066=>4.360953530851211e−6 two; .067=>0 zero. Original Geeky/M15 branches verified, with no claim of physical gain noise.

**Six mutation tests**: three distinct source CSV edits (one digit, missing trailing newline, swapping source lines) tested against BOTH separately source-locked validators; **6/6 rejected before mathematical computation**.

Complete executed LOCAL standalone ZIP `IW_REC11_ROT033_GEEKY_M15_CONTINUOUS_FOUR_PHASE_TRANSITIONS_REPRO_001_20261113.zip`: 14 members (13 payloads and SHA manifest), **20,583 bytes**, SHA256 `ff27ff9cc7094da8677bf676f23ffc57bc3a8e39f9717124ebe9d52bc612ac64`, CRC PASS; payload SHA256 **13/13 PASS**; clean isolated extraction and rerun of three programs reproduced BOTH JSON and run banners **byte-identically** 3/3 PASS. ZIP is LOCAL ONLY, not uploaded to GitHub. Complete original proof and all executed scripts are INSIDE local ZIP; this public GitHub report has equivalent mathematical claims, not falsely claimed byte-for-byte identical to its full local `REPORT.md`.

## 6. Strict guards and disposition

This is a CLASSICAL conditional result about original M13 N41 B auxiliary five-shell source quartics under arbitrary 25 independent coefficient and five relative shell gain nuisance variables. The actual historical `dtc0a_runtime_v0_3_1.py` producer bytes remain unverified; physical realizability of arbitrary 25-dimensional source coefficients and five independent gains is unproven. No original Fourier field, sensor measurement/PSN, GN, GR, TPE, J3/K, Wu–Xu, BBN or PBH implications are established. No mathematical/general novelty claim, no external blind I3; original M13/Geeky/M15 priority preserved. Owner Geeky and M15 adoption and BW receipt unconfirmed. No owner source modified; no task cascade.

**RETURN_ID:** `IW_REC11_ROT033_GEEKY_M15_CONTINUOUS_FOUR_ACTIVE_SET_TRANSITION_REFEREE_001_20261113`.

**VERDICT:** `PASS_25D_SOURCE_CONTINUOUS_5_4_3_2_0_PHASE_DIAGRAM / PASS_STRICT_RATIONAL_FOUR_THRESHOLD_BRACKETS / PASS_56_INDEPENDENT_GLOBAL_HINGE_CASES / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_PENDING`.
