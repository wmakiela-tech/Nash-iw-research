---
artifact_id: IW_GEEKY_S12_ROT017_UNIVERSAL_FINITE_ACTIVE_SET_AND_FOUR_ROBUST_SHELL_REGIMES_001_20261113
date: 2026-11-13
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
exposure: PUBLIC
science_status: AUTHOR_EXACT_FRACTION_FOUR_BRANCH_SOURCE_BOX_PASS / M15_ROT007_INDEPENDENT_I1_ROT015_9_PLUS_5_PASS / ROT017_INDEPENDENT_REFEREE_PENDING
source_status: IMMUTABLE_ORIGINAL_M13_N41_B_25_DIRECTED_QUARTIC_COEFFICIENTS
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: M13_AUXILIARY_N41_FIVE_MASK_B_ONLY / NO_HISTORIC_DTC0A_RUNTIME / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT017 — exact finite candidate theorem and four robust 5/4/3/2 active-shell regimes

## 0. Current independent review and exact firstness

M15 ROT007, dispatched 13 November 2026 17:09 CET, independently reimplemented ORIGINAL ROT015 global positive-energy projective shell ratio source gates using a separately authored BigInt rational polynomial program. On immutable original M13 direct_B.json Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0 and full independently widened eps=1e-7 coefficient-box inputs, M15 reports 9/9 exact source Bernstein positive gates for H=s4' s5-s4 s5'-(1/8)s4 s5 on t in [0,.2] plus 5/5 positive source shells; it confirmed the original ROT015 sharp zero-loss relative gain threshold and robust fixed pair 6.6%-6.7% decision. This is DIFFERENT-CELL NONBLIND I1 mathematical referee PASS for ROT015, not for ROT016/017 and not external blind I3 or physical evidence.

M15 original independent referee report:
https://github.com/wmakiela-tech/Nash-iw-research/blob/c1818b0d676d9e8b295447797564ce9860ace82b/research/m15/2026-11-13/IW_M15_ROT007_INDEPENDENT_PROJECTIVE_M13_B25_GAIN_9_BERNSTEIN_REFEREE_001_20261113.md

Other earlier different-cell math source audits remain AUD2 ROT005 and M15 ROT006, both independently full 17/17 plus 5/5 ROT007/013, and REC11 ROT029 independently proved the eps1e-7 negative witness. M13 generated the original 25 source quartics and shell model FIRST; Geeky ROT007, ROT015 and ROT016 first respective source-scoped mathematical results. No authorship of reviewer work reassigned.

## 1. Generic exact finite optimization theorem, not a threshold search

The mathematical nuisance class DIFFERENT from ROT007: one unrestricted positive common gain c>0 plus FIVE independent relative shell gains eta_i with |eta_i|<=kappa<1. For positive source shell signals s_i(alpha),s_i(beta) and weights w_i>0 define:

 r_i=s_i(alpha)/s_i(beta)>0,
 A_i=w_i*s_i(beta)^2>0,
 u=1-kappa>0, v=1+kappa>0.

The source-risk objective is min over c>0 and eta_i of SUM_i A_i*[r_i-c*(1+eta_i)]^2.

Profiling each eta_i independently FOR FIXED c is an exact scalar clipping operation, yielding the exact 1D loss

 Phi(c)=SUM_i A_i * max(r_i-v*c, u*c-r_i, 0)^2.

Every term is convex, C1, and piecewise quadratic in c. All changes of active conditions occur at known numbers c=r_i/v or c=r_i/u: for five shells AT MOST TEN breakpoints and ELEVEN open intervals.

For any interval, let L be low-active shells with r_i<u c and H high-active with r_i>v c. If L union H nonempty the unique stationary solution of its strictly convex quadratic piece is the EXACT RATIONAL number

 c_(L,H) = (SUM_(i in L) A_i*u*r_i + SUM_(i in H) A_i*v*r_i) / (SUM_(i in L) A_i*u^2 + SUM_(i in H) A_i*v^2).

Clamp it to the current interval; if no shell active, every c therein attains ZERO loss. Evaluate the original Phi at this candidate. Comparing AT MOST ELEVEN exact-rational candidates yields the GLOBAL minimizer. At c beyond max_i(r_i/u), all shells are low-active and Phi strictly increases; as c approaches zero all shells are high-active and derivative negative; hence no missing optimum on an infinite tail. For m>0 shells, at most 2m+1 intervals. This is classical convex active-set geometry, not new general mathematical theory. It applies to any positive source shell profile, not just M13.

## 2. Four independent 25-dimensional source-box certificates

The actual source is the 7501-byte original M13 B table at Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json

Its 25 directed coefficient source endpoints are each enlarged independently to the exact rational box [lo-eps*abs(lo), hi+eps*abs(hi)] at eps=1/10^7. Every real choice across ALL these intervals is allowed, regardless of physical source-field realizability. For N=41, k=2..6, disjoint shell weights (7778,6938,6146,5402,24389), fix alpha=1/20=.05 and beta=3/40=.075.

Original NEW Python standard-library fractions.Fraction solver, without importing ROT015 or ROT016, independently rebuilds the five disjoint shell quartics from the source nested mask occupancies, evaluates ratio and weights with directed exact interval arithmetic, then derives global c for four separated kappa fixtures and rigorously checks the correct active/inactive inequalities for EVERY coefficient realization in the full source box.

Source-typed results:

- kappa=1/100=1%: LOW shells 1,2,3,4; HIGH shell 5; no inactive; center 10^24 * Dmin^2 = 0.39633122626837725. Strict whole-box risk enclosure approx [0.3962481084566588,0.39641435398115865].
- kappa=1/25=4%: LOW 1,2,3; HIGH 5; INACTIVE 4; center scaled risk 0.06844974153629062; whole-box enclosure approx [0.06842089473545733,0.06847859507500707].
- kappa=3/50=6%: LOW 1,2; HIGH 5; INACTIVE 3,4; center scaled risk 0.0025080658921018185; whole-box enclosure approx [0.0025041863008465485,0.002511949462703026].
- kappa=33/500=6.6%: LOW 1; HIGH 5; INACTIVE 2,3,4; center scaled risk 0.0000043609535308512106; whole-box enclosure approx [0.000004249509674050934,0.000004474145415645988].

For every one of these four boxes, every ACTIVE and INACTIVE inequality is strictly certified using rational-directed endpoints; risk lower endpoints are strictly positive and globality follows from convexity and exact derivative zero. Min activity margins (float display ONLY) approximately .0057424577, .0061248982, .0011907152, .00004063666 respectively. No random source coefficient sampling, delta tuning, or sharp kappa threshold search. The four examples demonstrate genuinely DISTINCT 5-,4-,3-,2-active global structures within the same frozen source and parametric pair.

The general finite-interval scheme yields a relatively LOOSE interval enclosure in the 6.6% case. ROT016 already FIRST provided a tighter custom two-active enclosure approximately [4.304990867,4.417277647]*10^-6 in scale 10^24; the specialized earlier result is RETAINED, not overwritten or weakened.

The source representative midpoint kappa=.067 gives exact zero risk, consistent with ROT015 first sharp gain threshold; this is a negative control and not a new source result.

## 3. Execution and strict reproducibility

User-visible LOCAL ZIP contains ACTUALLY EXECUTED:
- original 7501-byte M13 direct_B.json SHA256 0295116e364e28e67f0129bda1fc298d6e4bfdcb7aa8a6314f02a9ea37edca5f;
- new original independent Fraction Python source SHA256 cbe8d77417efd42ead5bd8a0ebf01be86b749403ac6f1148683bb2c76bb0ffb5;
- ACTUAL full exact Fraction output JSON SHA256 7c54a54e0d6dacaef73b63133067b32d1f87e21bade3fb1a3b5058afb4ff4a4e, including exact integer numerator/denominator of four whole-box risk intervals and all branch sign bounds;
- independent NEW SciPy/NumPy floating diagnostic script and actual output, not sharing the Fraction proof code; actual four midpoint direct scalar minimizations agree to better than 5e-13 in scaled risk (observed worst absolute gap 1.61e-15);
- tampered temporary source negative-control script/output, source blob mismatch rejected BEFORE calculation, original preserved;
- README and SHA256 manifest.

Archive: Geeky_S12_ROT017_universal_exact_gain_active_set_5_4_3_2.zip
size 26575 bytes, SHA256 44d2e54ca138ebe274cd563dc777d5b9bb7e21c6c985cd33bf917c30c529e4d1, 9 members CRC PASS and exact byte readback 9/9 PASS. Fresh isolated archive extraction and separate Python3 rerun produced RESULT JSON BYTE IDENTICAL. Standalone scripts not separately mirrored to public GitHub: user ZIP is the actual executable source. No false public original-code byte-identity claims.

Direct commands:
python rot017_exact_universal_gain_active_set.py geeky_s12_rot014_original_M13_direct_B.json
python rot017_independent_float_crosscheck.py geeky_s12_rot014_original_M13_direct_B.json rot017_results.json
python rot017_source_mutation_control.py geeky_s12_rot014_original_M13_direct_B.json rot017_exact_universal_gain_active_set.py

## 4. Claim ceiling and disposition

This is a new *source-dependent auxiliary mathematical active-set implementation* not general novelty or experimentally sampled gain noise. The 25D coefficient box does not guarantee these coefficients derive from physically admissible Fourier TT input fields; the gains are arbitrary nuisance degrees, not measured calibration errors; original historical dtc0a_runtime_v0_3_1.py remains byte-missing; no conclusions on NASH K/J3/TPE or original physical dynamics.

M15 ROT007 independent I1 reviews ROT015; external REC11/AUD2/M15 mathematical review of new ROT017 four-source-box active-set branch certificate is PENDING, independent blind external I3 not requested. M15 formal global scientific owner CANON/EXEC sign not demonstrated; KN13 BW exact ingest receipt not checked. GitHub publication is not BW acceptance. No automatic assignment cascade and no further arbitrary kappa/delta micro-search.

FINAL: M15_ROT007_PROJECTIVE_9+5_I1_PASS / ROT017_UNIVERSAL_AT_MOST_11_EXACT_CANDIDATE_THEOREM_AUTHOR_PASS / SOURCE_BOX_FIVE_FOUR_THREE_TWO_SHELL_REGIMES_EXACT_FRACTION_PASS / INDEPENDENT_SCIPY_CONTROL_PASS / ISOLATED_REPLAY_AND_SOURCE_TAMPER_PASS / ROT017_REFEREE_PENDING / BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
