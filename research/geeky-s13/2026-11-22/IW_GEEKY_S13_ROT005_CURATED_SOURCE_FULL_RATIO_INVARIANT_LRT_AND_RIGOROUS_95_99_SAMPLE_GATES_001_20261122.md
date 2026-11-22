---
artifact_id: IW_GEEKY_S13_ROT005_CURATED_SOURCE_FULL_RATIO_INVARIANT_LRT_AND_RIGOROUS_95_99_SAMPLE_GATES_001_20261122
origin_cell: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
date: 2026-11-22 Europe/Warsaw
class: SOURCE_CONDITIONAL_N41_ROT038_ANISOTROPIC_GAUSSIAN_LATENT / MAXIMAL_INVARIANT_FULL_RATIO_OPTIMAL_TEST / RIGOROUS_IV55_FINITE_N
status: AUTHOR_MATH_AND_ACTUALLY_EXECUTED_INTERVAL_SOURCE / SAME_CELL_SCIPY_CHECK / DIFFERENT_CELL_I1_PENDING
source_execution: ORIGINAL_M13_HELPER_READ_NOT_NATIVE_EXECUTED_IN_THIS_ROTATION / HISTORICAL_FULL_DTC0A_MISSING
claim_ceiling: NO_GENERAL_NOVELTY / NO_PHYSICAL_RAW_SENSOR / NO_CANON / NO_EXEC_SIGN / BW_PENDING
---

# Geeky-S13 ROT005 — exact full-ratio likelihood test under arbitrary time-varying common gain

## Exact source and firstness

Original M13 N41 B Fourier auxiliary source Git blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679`; original Geeky-S12 ROT038 exact rational synthetic anisotropic Gaussian RAW-site noise models Git blob `28576dbb0649c1f0fbd4d926896813eac946e6d8`; Geeky-S13 ROT003 first chose permutation-related Fourier kx=(20,0,0), ky=(0,20,0); ROT004 first proved exact binary-sign robustness and sample counts 5825/11653 (Git blob `9d144f0bae3f78ab6d3bb38d424de9cc64ab4992`). ROT001/002 are distinct isotropic hypotheses and not reinterpreted. This report introduces a source-specific test, NOT any general probability novelty or measured experiment.

For t=cos(40*pi/41)=-cos(pi/41),
```text
vA_x=vA_y=167/150+14*t/75
vB_x=82/75+31*t/150
vB_y=17/15+t/6
q_A=1; q_B=vB_x/vB_y=exp(-D)
D=log(vB_y/vB_x)=0.08620670538230474999589005237625...
```

The original B-energy deterministic Fourier mean vanishes at these HYPOTHETICAL RAW-site projected modes by upstream M15 original-source support. No direct original M13 helper execution or hardware claim is made here.

## Nuisance contract, optimal invariant and exact score law

Under X=A/B, each hypothetical snapshot j has independent latent Exp(1) Fourier energies E_xj,E_yj; the pairs are IID across j. The observed energies are `P_xj=g_Xj vX_x E_xj, P_yj=g_Xj vX_y E_yj`. Any positive *common within-snapshot* multiplier g_Xj is allowed, including unbounded, temporally dependent or chosen adaptively as a function of latent data; directional or additive nuisance is NOT allowed.

The ratio `R_j=P_xj/P_yj=q_X E_xj/E_yj` eliminates gain PATHWISE and is a maximal invariant under the samplewise positive scale group. Its density is `f_q(r)=q/(q+r)^2` for r>0. The equal-prior Neyman–Pearson statistic is
```text
ell(r)=log q+2*log[(1+r)/(q+r)]
Decide B iff sum_{j=1}^n ell(R_j)>0.
```
The involution `r -> q/r` interchanges source laws and sends ell to -ell, giving exactly equal type-I and type-II errors. LRT is optimal among tests measurable in these complete ratios for the TWO FIXED source hypotheses; it is NOT globally optimal over other physical sensors or unrestricted latent noise.

Under A, `U=R/(1+R)` is Uniform(0,1) and `ell=-D-2log[q+(1-q)U]`. Thus:
```text
p_A(ell)=exp(-ell/2)/(4sinh(D/2))
p_B(ell)=exp(+ell/2)/(4sinh(D/2)), -D<ell<D.
h=D/(2sinh(D/2))=0.9996904172694321426129149...
e_n=h^n/(2*pi) * integral_0^infinity
       sinc(D*s)^n/(s^2+1/4) ds,  n>=2.
```
This last identity comes from exponentially tilting the log-likelihood score to the uniform law on [-D,D] and applying Fourier inversion. It is exact, no Monte Carlo or central limit approximation.

## Four decisive strict interval enclosures

Actually executed primary 55-digit outward `mpmath.iv` arithmetic, using original ROT038 exact rational source coefficients plus interval cos(pi/41). Composite trapezoid for s in [0,8], 32000 subintervals, step 1/4000; analytic absolute quadrature remainder <1/80000. Proof: for `g(s)=sinc(Ds)`, on this interval `0<g<=exp(-D^2s^2/6)`, `|g'|<=D^2s/3`, `|g''|<=D^2/3`. For n=4368..8740, `|d²/ds² [g(s)^n/(s²+1/4)]|<300`, giving `8(1/4000)^2*300/12=1/80000`. The separately bounded oscillatory infinite tail after s=8 has absolute value <1e-100 using the Gaussian sinc bound up to pi/D, then |sinc(Ds)|<=1/(Ds).

| n | Certified lower error | Certified upper error | Verdict |
|---:|---:|---:|---|
| 4368 | 0.0500166713065641 | 0.0500177002495319 | NOT >95% |
| **4369** | **0.0499972538282707** | **0.0499982824526956** | **>95%** |
| 8739 | 0.0100004846623038 | 0.0100007505015237 | NOT >99% |
| **8740** | **0.00999693779888760** | **0.00999720355580820** | **>99%** |

Since optimal Bayes risk e_n cannot increase when one observation is added (ignore the extra observation), these bracketed neighboring sample counts certify the FIRST admissible n for the chosen full ratio experiment. Against ROT004 one-bit majority n=5825 and n=11653, the improvement is about 25% for both levels. These source-conditional *hypothetical* counts do not imply experimental feasibility.

Independent second SAME-CELL SciPy algorithm recomputed the four point values: 0.05001718577806243, 0.04999776814049758, 0.010000617581919741, 0.00999707067735387, all strictly within directed interval certificates. Separate pathwise tests checked adaptive shared gain and source score involution. The former pooled F-test loses validity when one snapshot is given overwhelming gain; separate directional gains can alias A and B; arbitrary non-Gaussian *latent* energy laws do not meet the assumed beta-prime model.

## Actual reproducibility and review boundaries

The **user-local** full report and reproducibility ZIP contain TWO original scripts, COMPLETE two JSON outputs, executable cold replay, five actual fail-closed adversarial controls, README, SHA-256 manifest; no public code-byte mirror is claimed. Archive SHA256 `1d26a97b3c02a2d361a0fd8d63bf5fff6fc78d338fb9dbcc06b92b38891d1005`, 18,128 bytes, 9 archive members CRC PASS, eight file SHA256 PASS. The standalone initial archive extraction-and-replay orchestration TIMED OUT and was NOT counted pass. Subsequent individual runs FROM A FRESH EXTRACTED ARCHIVE both produced FULL JSON byte-identical, and a separate extracted cold replay repeated 5/5 expected negative rejections and an identical receipt. This distinguishes a timeout from an actually confirmed scientific check.

No original historical dtc0a producer, source-native physical 41^3 RAW site acquisition, measured Gaussian site noise, independently acquired sample collection, or physical gain-symmetry was established. REC13/AUD3 different-cell I1 specifically for ROT005 still PENDING, native BW ingestion receipt PENDING. No scientific owner ACK or CANON/EXEC_SIGN implied by publication.

**Bounded outside I1 requested:** Independently rederive exact q, truncated exponential loglikelihood distribution, Fourier factor h^n/(2pi), trapezoid |F''|<300 and oscillatory tail estimate, four strict n gate intervals, the nested NP minimax/balanced claim restricted to ratio observations and the pathwise gain-varying counterexamples.

`AUTHOR_EXACT_SOURCE_MATH / IV55_FOUR_GATES_PASS / EXTRACTION_TWO_JSON_IDENTICAL / FIVE_NEGATIVE_CONTROLS_PASS / OUTSIDE_I1_PENDING / BW_PENDING / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE`
