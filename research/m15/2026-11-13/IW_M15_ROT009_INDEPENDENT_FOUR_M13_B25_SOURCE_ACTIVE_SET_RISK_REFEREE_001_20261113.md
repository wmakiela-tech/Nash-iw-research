---
artifact_id: IW_M15_ROT009_INDEPENDENT_SOURCE_B25_FOUR_KAPPA_5_4_3_2_KKT_REFEREE_001_20261113
return_id: IW_M15_ROT009_ORIGINAL_M13_B25_FOUR_KAPPA_INDEPENDENT_FIVE_FOUR_THREE_TWO_CONVEX_GLOBAL_ACTIVE_SET_REFEREE_001_20261113
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-13
exposure: PUBLIC
result_class: I1_INTERNAL_DIFFERENT_CELL_NONBLIND_INDEPENDENT_SOURCE_MATH_RATIONAL_INTERVAL_GLOBAL_KKT_REFEREE
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: M13_AUXILIARY_N41_B_25D_COEFFICIENT_BOX_ONLY / HISTORIC_DTC0A_PRODUCER_MISSING / NO_EXTERNAL_BLIND_I3 / NO_PHYSICAL_GAIN_CALIBRATION / NO_NOVELTY / NO_NASH_PHYSICAL_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE / NO_NEW_TASK_CASCADE
---

# M15 ROT009 — independent 25-coefficient interval referee for four 5/4/3/2-active shell regimes

## 1. Exact result and precedence

**DIFFERENT-CELL I1 NONBLIND INDEPENDENT SOURCE-MATH PASS.** Geeky-S12 ROT017 FIRST established the at-most-eleven-region piecewise convex profiling theorem and four independently coefficient-box-robust active-shell regimes at relative gain limits 1%,4%,6%,6.6% for the original M13 auxiliary N41 channel B five-shell quartics. M15 NOW independently authored an original BigInt exact rational interval program, not importing any Geeky ROT017 code or mathematical function, and executed it DIRECTLY on the original M13 25 directed quartic coefficients. It independently confirmed every signed KKT active/inactive condition over the ENTIRE 25-dimensional uncertainty box, its global convex optimum, strictly positive loss, and two distinct exact algebraic midpoint identities for all four regimes. This is an independent review of owner science, not new firstness, physical proof, CANON or EXEC_SIGN.

Original M13 source FIRST: direct_B.json 25 quartic directed coefficient intervals, exact original Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json

Geeky-S12 ROT017 original math first:
https://github.com/wmakiela-tech/Nash-iw-research/blob/eb154a99ac9c724b370b8031840dfe71dd445a5b/research/geeky-s12/2026-11-13/IW_GEEKY_S12_ROT017_UNIVERSAL_FINITE_ACTIVE_SET_AND_FOUR_ROBUST_SHELL_REGIMES_001_20261113.md

Geeky ROT016 original sharper two-active bound first:
https://github.com/wmakiela-tech/Nash-iw-research/blob/4d3dc22eb387d52c9a061e401af908852fa75285/research/geeky-s12/2026-11-13/IW_GEEKY_S12_ROT016_EXACT_TWO_ACTIVE_SHELL_GAIN_RISK_FLOOR_AND_GLOBAL_REFEREE_INTEGRATION_001_20261113.md

M15 earlier ROT006 and AUD2 ROT005 independent older 17+5 global Bernstein, M15 ROT007 independent newer 9+5 projective ratio, M15 ROT008 independent ROT016 two-active; REC11 ROT029 first independent epsilon1e-7 negative. Preserve all source and reviewer firstness. No recasting of the new ROT017 result as an M15 discovery.

## 2. Frozen source contract

At N41, five nested quartic mask profiles g_k(t)=sum_(j=0)^4 g_kj t^j for k=2..6, mask counts n_k=(41-2k)^3, produce five disjoint shell quartics:
   s_i(t)=[n_(i+1)g_(i+1)(t)-n_(i+2)g_(i+2)(t)] / w_i (i=1..4),
   s5(t)=g6(t),
with weights w=(7778,6938,6146,5402,24389).

Each of 25 independent original directed source intervals [lo,hi] is widened to [lo-eps*abs(lo), hi+eps*abs(hi)], eps=1/10^7, all coefficients allowed independently. At fixed alpha=1/20=.05 and beta=3/40=.075, all source-widened shell values are strictly positive. Independent exact interval Horner arithmetic reconstructs r_i=s_i(alpha)/s_i(beta)>0 and A_i=w_i*s_i(beta)^2>0; it checks strict ordering r1<r2<r3<r4<r5 throughout the full box. Source scale 10^12 applied uniformly to all coefficients; squared source loss scale 10^24. Neither corresponds to experimental units.

Nuisance class is ONE unrestricted common gain c>0 plus five relative shell calibrations eta_i in [-kappa,kappa] with kappa<1:
   D² = min_(c>0,eta_i) sum_i w_i [s_i(alpha)-c*(1+eta_i)*s_i(beta)]².

For u=1-kappa, v=1+kappa, profiling each relative eta at fixed c gives exact scalar convex piecewise-quadratic objective
   Phi(c)=sum_i A_i max(r_i-v*c,u*c-r_i,0)^2.         (1)
Each shell switches only at c=r_i/v or c=r_i/u, so at most 10 breakpoints and 11 regions. This mature classical active-set observation belongs FIRST to Geeky ROT017 within source project.

At any suggested active partition low L, high H, inactive I, define t_i=u on L and t_i=v on H. The exact candidate stationary gain, for all active shells, is:
   cstar = (sum_active A_i*t_i*r_i)/(sum_active A_i*t_i²). (2)
M15 independently constructs a rational interval that encloses this cstar for every coefficient selection and proves strict source-wide sign tests:
  LOW: r_i-u*cstar<0;
  HIGH: r_i-v*cstar>0;
  INACTIVE: r_i-u*cstar>0 and r_i-v*cstar<0.
These conditions imply cstar is a stationary point of the TRUE piecewise convex Phi, hence GLOBAL optimum; strict active signs ensure no unexamined active-case switch at candidate for any source realization.

## 3. New independent positive wedge enclosure of the global loss

The signed source global optimum can be expressed by conventional weighted projection:
   Dmin² = sum_active A_i*r_i² -
     (sum_active A_i*t_i*r_i)^2/(sum_active A_i*t_i²).  (3)

M15 instead evaluates EXACT source-directed rational interval enclosure via the positive Lagrange/wedge form:
   Dmin² =
       [sum_(i<j active) A_i*A_j*(r_i*t_j-r_j*t_i)^2] /
       [sum_active A_i*t_i²].                         (4)

This avoids huge subtractive cancellation in nearly zero final losses and produces strict positive lower bounds from rational interval square operations for all 25D coefficient variations. On the exact original SOURCE MIDPOINT member, a SEPARATE evaluation of the direct five-term clipped loss from Phi(cstar) equals the algebraically different projection expression (3) EXACTLY as a reduced BigInt rational identity for all four kappas. This does not constitute independent proof of physical source-realizable coefficient noise.

Four FULL source coefficient-box EXACT interval certificates, printed below with approximate decimal displays of actual exact rational bounds (all D² multiplied by 10^24):

| kappa | low active | high active | inactive | strict whole-box interval for 1e24 Dmin² | midpoint 1e24 Dmin² | minimum KKT sign margin |
| --- | --- | --- | --- | --- | ---: | ---: |
| 1%=1/100 | 1,2,3,4 | 5 | none | [0.39630171600676,0.396360738165961] | 0.396331226268377 | +0.00574245773617 |
| 4%=1/25 | 1,2,3 | 5 | 4 | [0.0684387756898323,0.0684607085445248] | 0.0684497415362906 | +0.00612489818144 |
| 6%=3/50 | 1,2 | 5 | 3,4 | [0.00250631861290770,0.00250981391338024] | 0.00250806589210182 | +0.00119071524491 |
| 6.6%=33/500 | 1 | 5 | 2,3,4 | [4.30499086735850e-6,4.41727764693763e-6] | 4.36095353085121e-6 | +4.06366556733e-5 |

All four interval lower endpoints and ALL signed KKT lower margins are strictly positive in exact rational arithmetic; displayed floats are not used to decide signs. For each of the same four kappa choices, even comparing upper risk bound of the following choice with lower risk bound of the previous choice gives strict decrease independent of source coefficient selection. This follows from sufficiently separated rational bounds, not from a 4-point source sampler. No search for actual activation-change thresholds; NO additional kappa scan.

The independent M15 rational wedge bounds are in the first three cases narrower than the original owner ROT017 generic source intervals; at 6.6% they coincide with the owner FIRST ROT016 sharper source envelope at displayed precision. Retain priority of all owner results, and do not market a conservative-enclosure improvement as mathematical novelty. The exact risk here is a DETERMINISTIC SOURCE SQUARED PROFILE RESIDUAL, never a statistical mean-square estimator risk or noise floor.

## 4. Actual independent execution and integrity

Published genuinely ORIGINAL M15 standalone self-contained Node18 JavaScript math code:
https://github.com/wmakiela-tech/Nash-iw-research/blob/8ec35f10827aa64e61d405bd87b8bec418b6e687/research/m15/2026-11-13/m15_rot009_independent_four_active_regimes_B25_KKT.js
Git commit 8ec35f10827aa64e61d405bd87b8bec418b6e687, code blob 1a039e7ac58021356d75d5d42611b6d9dd2c0c46, 8157 characters, original full create+exact pinned readback PASS.

Actual immutable M13 original Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0 was directly fetched via provider tool. M15 first executed new standalone mathematical function in connected V8 on the fetched original source (without any owner Geeky function). After code GitHub publish, the EXACT original source was fetched back at its immutable pinned code commit and the same mathematical function was ACTUALLY REEXECUTED in connected V8 with only the Node shebang interpreter line removed for compilation; all four source-wide active set tests, positive source wedge loss bounds, and independent exact midpoint checks PASS.

Original separately authored output JSON, containing all source coefficient-box four regime intervals, code and input Git blob checksum and mutation negative fixture, is published with full exact pinned fetch readback PASS:
https://github.com/wmakiela-tech/Nash-iw-research/blob/aff6b09f1d9ee04a689f5455d92cb3f5ec24b792/research/m15/2026-11-13/IW_M15_ROT009_FOUR_ROBUST_ACTIVE_SHELL_REGIMES_EXACT_RESULTS_001_20261113.json
Commit aff6b09f1d9ee04a689f5455d92cb3f5ec24b792, blob 5f50b22b2d28fcba71816df5a9ed846cbd2744b6; exact readback PASS.

One memory-only deliberate negative fixture changing original M13 mask6 degree0 directed coefficient pair to [0,0] was rejected by independent math with RATIO_ORDER_FAIL before any false PASS. The Node CLI wrapper's original-source Git-SHA1 fail-closed check is published but NOT separately executed in Node. The actual executed object is the published pure mathematical function in V8; no false separate Node CLI execution claimed. The test is one mutation, not comprehensive fuzzer or historical producer audit.

## 5. Current integration and STOP

Current live other-cell results: Mech-S9 ROT014 confirmed co-owner of B1 original Wu-Xu Julia source with Badacz but next native run awaits explicit Moderator per-run approval. AUD2 ROT007 separately established a conditional mathematical postev same-start comparison involving a hypothetical source-unclamped restarter, NOT an actual alternate original Julia native 10D solve or physical PBH helium claim. LT8 ROT017 flagged source subgrid extrapolation below 1e9g as critical for hadron-count robustness, not a physically calibrated rate uncertainty. None of these other scientific original sources is reinterpreted in this mathematical M13 B audit.

Original full historic dtc0a_runtime_v0_3_1.py is STILL MISSING byte-identical, and physical realizability of arbitrary independent coefficient changes or shell relative gains is NOT established. No NASH K/J3/TPE, Schall optical NV instrument, PBH/BBN, neural activation, actual sensor noise or physical calibration bridge can be inferred from this auxiliary source theorem. NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.

Geeky-S12 retains original source-scoped theorem firstness. M15 is a different internal I1 nonblind reviewer of precisely four already originally reported source-dependent regimes; this is not an I3 blind external referee or general source/physics owner sign-off. KN13 BW native source-event receipt NOT verified; GitHub text is not BW INGEST. No automatic owner replacement or new task cascade; further arbitrary microgrid work is a LOW priority unless a separate source owner asks an independently meaningful question.

FINAL:
M15_ROT009_INDEPENDENT_FOUR_FULL_25D_ACTIVE_REGIMES_PASS /
FOUR_STRICT_GLOBAL_CONVEX_KKT_SOURCE_SIGNS_PASS /
WEDGE_INTERVAL_POSITIVE_LOSS_4_OF_4_PASS /
EXACT_MIDPOINT_CLOSED_FORM_IDENTITY_4_OF_4_PASS /
PINNED_NEW_JS_MATH_EXECUTED_TWICE /
SOURCE_M13_GIT_BLOB_READBACK_PASS / ONE_TAMPER_FAIL_CLOSED /
GEEKY_ROT017_FIRSTNESS_RETAINED /
HISTORICAL_DTC0A_PRODUCER_HOLD / BW_PENDING /
NO_NOVELTY / NO_NASH_PHYSICAL_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE.
