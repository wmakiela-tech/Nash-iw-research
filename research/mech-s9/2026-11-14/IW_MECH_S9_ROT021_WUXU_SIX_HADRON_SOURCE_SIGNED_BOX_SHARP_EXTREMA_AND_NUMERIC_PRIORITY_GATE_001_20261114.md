---
artifact_id: IW_MECH_S9_ROT021_WUXU_SIX_HADRON_SOURCE_SIGNED_BOX_SHARP_EXTREMA_AND_NUMERIC_PRIORITY_GATE_001_20261114
date: 2026-11-14
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
scientific_status: SOURCE_NATIVE_FROZEN_10D_6_CHANNEL_POSTHOC_SHARP_WEIGHT_BOX_PASS / NO_NEW_JULIA / B1_HOLD
claim_ceiling: SOURCE_INTEGRAL_LINEAR_FRACTIONAL_BOX_ONLY / NO_CAUSAL_XN / NO_HELIUM_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# ROT021 — exact six-channel box conditioning of the frozen Wu–Xu signed hadronic neutron RHS share

## Source-first and precedence

Original authors Wu and Xu first authored the physical PBH/BBN model and 10D Julia ODE, frozen at Fenyutanchan/Primordial-Black-Hole commit d395183674cace6c9906a8911bdeb7234ba4040d, original main-scan.jl Git blob b368ba55d5a493f7bc185909730f7fe5691f10d6. Mech-S9 ROT012/013 FIRST executed one original unmodified 10D Julia trajectory (Actions run 43436800793, immutable original artifact 14045176436), and ROT016 FIRST reconstructed the six signed reaction source RHS integrals. Mech-S9 ROT019 FIRST compared native saved-time versus mass-cubic source coordinate. AUD2 ROT013 FIRST independently checked signed versus absolute reaction source cancellations and single-channel 1% perturbations. ROT021 is the DISTINCT mathematically sharp six-simultaneous-channel-weight conditioning check on the SAME native solution, not new physical kinetics or novel mathematics.

Original native 10,000-row source archive SHA-256 71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486; original RAW 10k CSV SHA-256 45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1. Original ZIP CRC and 16/16 internal SHA verified PASS. The original beta 1.005863531057e-17 is 0.586353% ABOVE the original beta scan maximum, although accepted by original magic() callable; do not imply original published scan node.

## Frozen mathematical object and proof

Six original reactions are ordered: pi_minus, pi_plus, K_minus, K0_L, pbar, nbar. For each reaction i, let a_i be its original signed on-path RHS integral while M_PBH >= 1e9 g and b_i its signed on-path integral while 0<M_PBH<1e9 g. Integrate ONLY the 8544 source PBH-active sampled rows and split at the mass node between original rows 8383 and 8384. Never integrate across the discontinuous row 8544-to-8545 evaporation switch. On each of the two numerical clocks (original saved time, exact source-law mass-cubic coordinate) define

F(w) = (sum_i w_i b_i)/(sum_i w_i(a_i+b_i)), with independent purely formal multipliers w_i in [1-epsilon,1+epsilon].

On every epsilon box checked, the affine denominator is strictly positive on the whole box: min_w D(w)=D(1)-epsilon*sum_i |a_i+b_i|. At epsilon=.01 this minimum is 1.0182192873435412 for native-time coefficients, 4.274023730981637 for mass-cubic coefficients. Holding all other weights fixed, partial_i F=(b_i D-(a_i+b_i)N)/D^2 is independent of w_i. Its sign is uniform at all 32 vertices of the OTHER five-weight box for each of six channels at epsilon=.01 and smaller, so extrema on the closed box occur at the 64 corners; the maximizing signs in channel order are (-,+,+,+,-,+) and the minimizing signs their opposites (+,-,-,-,+,-). This is SHARP with respect to these six fixed *numerically computed phase coefficients*, not a bound on true ODE trajectories or source uncertainties.

## Actual source-derived results

| Independent per-channel perturbation | Native saved-time sharp minimum | Native saved-time sharp maximum | Mass-cubic sharp minimum | Mass-cubic sharp maximum |
|---|---:|---:|---:|---:|
| 0 (original) | 73.2651736523% | 73.2651736523% | 73.2083375210% | 73.2083375210% |
| +/-0.01% | 73.2477869854% | 73.2825729023% | 73.1909310412% | 73.2257566215% |
| +/-0.05% | 73.1783658771% | 73.3522960077% | 73.1214310553% | 73.2955595056% |
| +/-0.1% | 73.0918709816% | 73.4397346564% | 73.0348383997% | 73.3830987306% |
| +/-1% | 71.5865974732% | 75.0697464006% | 71.5279554392% | 75.0150927476% |

The unperturbed native signed-net integral is 1.0856940909460764 while six-channel total absolute activity is 6.747480360253531; 16.0903631130% net-to-absolute and thus 83.9096368870% sign cancellation. The absolute-activity below-table share is 48.2688076369% native saved time and 48.1741875230% mass cubic. Original signed-source clock share shift is 0.0005683613129947584 as a fraction, i.e. 0.0568361312995 percentage points. Exact vertex extrema reach this maximum shift at epsilon=0.000326390905984797, which is a **formal +/-0.0326390905985% change to each independent reaction weight**, not a claimed physical rate error bar.

The signed ratio's original clock shift is consequently a weaker numerical effect than permitted by small hypothetical independent channel reweightings. AUD2's prior independently verified single pi_plus 1% (+0.824387 pp) and pi_minus 1% (-0.818056 pp) remain intact. A common factor applied to all six channels would leave F unchanged, which also illustrates that this is a *relative-channel-weight* condition number, not source total normalization.

## Execution, negative tests and custody

Executed Python3 standard-library source SHA-256 bd18c16ca4a42345a7b20d994cc169acdec6df4af26e2b58dbfe04f4d40d47e5, output JSON SHA-256 764565f6939b6afad9f3a5adc0220f6c07e8f40279565d6f83551adb81e083ea. It directly verified the original source ZIP, all 16 internal SHA, 10000 original source records, 8544 live records, all six native hadron source log-floor flags and reaction coefficients; enumerated all 64 vertices per epsilon/clock, and 729 inside-box grid cases; tested each source channel derivative sign at all 32 other-weight vertices, the strictly positive whole-box denominator lower bound and an independent synthetic mixed-sign and flat-direction control.

Separate actually executed independent DECIMAL70 verifier source SHA-256 62c3a2b07ecff08020856b0946a106450924dea58f9a68e9f18748edce54114a reproduced all 64 corners and all derivative-sign maps across both coordinates and four epsilons, plus independently checked the 0.000326390905984797 threshold. Full conversation-local self-contained original-Julia-source+producer+JSON+Decimal-verifier+README archive: mech_s9_rot021_sharp_channel_box_reproduction.zip SHA-256 819fad1aa04671d4a8f71ba7d0b0bc67fd2a3fd60f377491253afe3c99c81dab; CRC PASS, 5/5 outer payload SHA and 16/16 nested original source SHA PASS; isolated independent standard-library replay produced byte-identical JSON; a one-byte original Julia ZIP tamper failed before any result. Source scripts and local archive live in the Moderator conversation, not claimed independently GitHub/BW archived.

## Physical and research disposition

All weights are exploratory independent multiplicative *posthoc* changes to already archived per-channel source RHS areas with 10D native T, X and n_h FIXED. Real hadron production, species populations, weak rates, couplings and PBH mass evolution are NOT self-consistently recalculated, and the actual model does NOT supply +/-1% independent cross-section uncertainty. The result is neither a changed X_n(T_nuc), a physical Yp error, a PBH exclusion shift, nor proof of general robustness across source parameters.

B1 30-day Test S release remains blocked by original native sampled mass-cubic and evaporation-stop numerical inconsistencies, default solver convergence unverified, source-original generator uncertainty below the 1e9 g hadron table uncalibrated, independent E4 source and published Fig5 executable identity unknown. No Moderator approval of another native Julia simulation found; NONE performed. Do not issue new tasks from this exploratory source-only condition-number comparison. GITHUB_PENDING_BW_INGEST does not mean BW receipt.

FINAL: ROT021_FIXED_SOURCE_FRACTIONAL_BOX_64_VERTEX_SHARP_PASS / DECIMAL70_INDEPENDENT_REPLAY_PASS / THREE_LEVEL_SOURCE_CUSTODY_PASS / B1_NUMERIC_HOLD / B1_PHYSICAL_INPUT_HOLD / NO_JULIA / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.