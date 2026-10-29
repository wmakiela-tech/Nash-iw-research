---
artifact_id: IW_MT14_ROT012_B_SOURCE_INTERVAL_GLOBAL_STATISTICAL_SEPARATION_GAUSSIAN_RESOURCE_001_20261029
created_at: 2026-10-29
origin_cell: IW_MT_SUCCESSOR_13 / MT14
problem_id: P3_DTC0A_B_SOURCE_INTERVAL_GAUSSIAN_STATISTICAL_IDENTIFIABILITY_RESOURCE_GATE
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: SOURCE_INTERVAL_EXACT_FRACTION_GLOBAL_MINIMAX_BRACKET / INDEPENDENT_ENDPOINT_CHECK / CLEAN_REPRO_PASS / OWNER_REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_HISTORIC_NATIVE_DTC_RUNTIME / NO_PHYSICAL_J3_K / NO_EMPIRICAL_NOISE_CLAIM
---

# MT14 ROT012 — rigorous source-interval global separation of B, plus synthetic Gaussian resource lower bound

**Date 2026-10-29.** MT14 active (not distinct M14), MT15 successor NOT ACTIVATED. AUD1 is independently active, but no external reviewer has accepted this scientific report. This result is source-typed mathematical and synthetic-statistical only.

## Prior source first and external mature theory

ORIGINAL **M13 ROT040 FIRST** owns original source-direct N41 five-mask quartics B, mask/shell energy covariance, positive shared gain profile, and original A/C all-delta theorem. B special delta=.01 remained GRID_ONLY in M13. Original:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/IW_M13_ROT40_universal_AC_radial_mask_global_argmin_001.md

Original B quartic directed coefficient intervals first M13, direct_B.json pinned Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json

MT14 ROT008 FIRST disproved a stronger B universal ALL-delta nearest-boundary claim at delta=.1 (still stands). MT14 ROT011 FIRST certified global SAME-SIDE nearest-boundary at the SPECIAL delta=.01 for all alpha, original source interval box:
https://github.com/wmakiela-tech/Nash-iw-research/blob/db6b3f97665904e32e49834e26cff1248155a40e/research/mt14/2026-10-29/iw_mt14_rot011_source_direct_B_delta001_global_nearest_boundary_bernstein_001.md

External mathematics: mature Lagrange identity/weighted Gram minors (https://mathworld.wolfram.com/LagrangesIdentity.html), classical variable projection Golub/Pereyra (https://www.sciencedirect.com/science/article/pii/B9780125142502500123), Bernstein/de Casteljau positivity, classical Gaussian Neyman-Pearson + Le Cam/Pinsker (https://web.stanford.edu/~lindrew/stats311.pdf). NO new mathematical novelty.

## M13 frozen observation and all-source-interval guard

Masks interior k=2..6 on N=41 have n=(50653,42875,35937,29791,24389), nested. Disjoint shell weights w=(7778,6938,6146,5402,24389). M13 original B mask means g_i(alpha) are quartics, shell means s_i(alpha)=(n_i*g_i−n_(i+1)*g_(i+1))/w_i for i=0..3 and s_4=g_4. Original source-interval certified shell means >0 on alpha in [0,1/5]; positive common ENERGY gain is strictly interior. Synthetic iid voxel ENERGY noise induces shell covariance tau² W^−1, W=diag(w), NOT five independent RMS sensor observations or real calibrated instrument.

Original owner source checked DIRECT this turn: original Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0, 7501 chars. Exact DECIMAL-to-BigInt rational independent parser verified all 100 directed source interval endpoints (25 polynomial coefficients ×4 endpoints) lie within 25 conservative intervals

  10^14 * c_ij in [C_ij−10^(−8), C_ij+10^(−8)],

where C_ij is the exact NINE-DECIMAL coefficient center explicitly repeated in the proof scripts. The code uses pure rational source coefficient scaled integers C_ij*10^9 ±10, and outward interval arithmetic over the entire box. Original direct_B.json source belongs to M13; a link/sha is not a claim original author data were copied into MT14 ZIP.

For alpha,beta in [0,1/5], let a=s(alpha),b=s(beta), P=||a||_W²,Q=||b||_W²,p=<a,b>_W, with p,Q,P>0. Define

  rho²(alpha,beta) = min_(t>0) ||a−t*b||_W² / P = 1−p²/(P*Q).

## Exact quantitative global theorem and proof

For EVERY realization of all original M13 B coefficient intervals, let

  m_B = inf_{alpha,beta in [0,.2], |alpha−beta|>=.01} rho²(alpha,beta).

**CERTIFIED BRACKET: 4.87e−6 < m_B < 4.904e−6**.

Exact rational lower certificate (unrounded display) is 4.875616762075767e−6, and original-source-interval endpoint upper certificate at (alpha,beta)=(.2,.19) is 4.903774041472931e−6. The lower and upper are NOT probabilistic confidence intervals or empirical errors; they are strict real-algebraic bounds for every source coefficient realization included in M13 intervals. Exact rational numerators and denominators are in accompanying JSON.

**Lower proof:** Weighted Lagrange/Binet-Cauchy identity gives

  P*Q−p² = sum_{0<=i<j<=4} w_i*w_j * [s_i(alpha)s_j(beta)−s_j(alpha)s_i(beta)]².

Each bracket factors (beta−alpha) EXACTLY. If s_i(x)=sum_{k=0}^4 s_ik*x^k, then

  [s_i(alpha)s_j(beta)−s_j(alpha)s_i(beta)]/(beta−alpha)
  = sum_{0<=k<l<=4} (s_ik*s_jl−s_il*s_jk)
    * (alpha*beta)^k * sum_{r=0}^{l-k-1} alpha^r * beta^(l-k-1-r).

This algebraic divided-difference identity avoids false cancellation caused by interval-evaluating the difference of two near-equal quartic products. Positive Gram sum also avoids subtraction of P*Q and p².

From MT14 ROT011 original source-interval GLOBAL nearest boundary theorem at delta=.01, it suffices to bound nearest boundary observations for all alpha: right side alpha=19u/100,beta=(1+19u)/100 and left side alpha=(1+19u)/100,beta=19u/100, each 0<=u<=1. For BOTH sides, build pure stdlib Fraction interval coefficients of ALL TEN minor-quotient polynomials, as well as positive P and Q norm polynomials. Convert them to 1D Bernstein interval coefficients and use exactly **512 dyadic subintervals per side**. On every subinterval, take the strict signed lower enclosure for each minor (otherwise lower bound zero), square it and weight it; use upper Bernstein bounds of P and Q in the SAME subinterval. All 512+512=1024 segments have strictly positive Gram lower. The MIN over all segments and BOTH sides is the same exact positive rational lower ≈4.875616762075767e−6, STRICTLY >487/10^8 = 4.87e−6. Because P is fixed for each true alpha, the ROT011 inequality D²(alpha,far)>=D²(alpha,nearest-same-side) transfers to normalized rho². Thus the 1024-bound proof covers EVERY legal beta with |beta−alpha|>=.01, not only nearby beta or gridpoints. The proof depends on ROT011's already-certified source theorem; this is NOT independent ROT011 referee acceptance.

**Upper proof:** A DIFFERENT standalone Python Fraction implementation takes alpha=1/5,beta=19/100, independently evaluates all 10 weighted Gram minors at those rational points for each original coefficient outer box, and encloses the numerator and positive P,Q denominator in both directions. It proves

  4.903744074886575e−6 < rho²(.2,.19) < 4.903774041472931e−6 < 4.904e−6.

This is a legal particular pair, hence upper bounds global m_B. It is an independently implemented source-interval endpoint control, NOT an independent theorem on all-alpha nearest boundaries.

**Independent positive cross-control:** One-pair-only (shell 2 vs shell 4) separate certified 128-dyadic code gives a weaker but rigorous UNIFORM lower >6.0378094e−7, independent of full Gram-sum optimization. The first exploratory numeric scan incorrectly applied a factor of 100 in polynomial alpha powers and gave ~6.8e−8. That number was DISCARDed before proof; corrected source-scale central evaluation gives ~4.903759e−6 for the hard boundary. The exact source-interval code and endpoint independent code use the correct source α domain and establish the bracket above. No diagnostic float enters sign verification.

## Conditional Gaussian information resource theorem

Now ASSUME exactly the additional synthetic observation law: each replicate of all five energy shell averages is Gaussian with common covariance Sigma=tau² W^−1 independent of alpha,beta or gain, and n independent replicates. True mean is t*s(alpha), t>0, and per-replicate **integrated SNR²=t² P/tau²**.

For the legal hard pair alpha=.2, beta=.19, choose the ALLOWED competing gain t_alt=t*p/Q>0, minimizing Gaussian W distance. The two resulting simple Gaussian hypotheses have exact squared Mahalanobis mean separation per replicate SNR²*rho²(.2,.19). With equal priors and known pair, Neyman-Pearson gives optimal probability of correct classification

  P_correct = Phi( sqrt(n*SNR²*rho²(.2,.19))/2 ).

To obtain 75% success on this legal pair, necessarily

  n*SNR² >= 4*[Phi^(-1)(3/4)]²/rho²(.2,.19).

Since rho²(.2,.19)<4.904e−6, it is NECESSARY that

  **n*SNR² > 4*[Phi^(-1)(3/4)]²/(4.904e−6) ≈ 371073.75.**

Thus a five-shell Gaussian energy-profile strategy with lower combined information budget cannot uniformly obtain binary success >=75% across the requested separation class. It is a necessary NOT sufficient budget, and NOT a claim of physical DTC sample size, actual sensor noise calibration, PBH, K/J3, geometry, operator invariance or arbitrary synthetic/non-Gaussian experiment. Other genuine measurements, different nuisance covariances and original runtime are outside the model.

## Executed reproducibility

Moderator-local runnable package: MT14_ROT012_Source_Separation_Gaussian_Resource_20261029.zip. ZIP SHA256 def9b7fb206dbb2cc3753175e579d71629f95a8a3c9f7f18b4d24e1bb5ffc437. Contents: FULL Polish mathematical report (~13KB), four independent-purpose Python standard-library runnable scripts (full ten-minor proof, one-minor control, endpoint source-interval check, assertion checker), JSON exact rational results, run logs and SHA256SUMS. No NumPy, SciPy, SymPy or external network needed for proof. ZIP CRC PASS; **13/13** SHA256 file checks PASS; extracted into NEW temporary directory, checked all original entries, DELETED 3 stored JSON outputs and RERAN all 3 scripts, regenerated JSON BYTE-FOR-BYTE IDENTICAL 3/3 PASS; assertion script PASS. Source owner original B full directed endpoint file separately live-verified 100/100 against source conservative boxes, not claimed to be included in ZIP.

## Scientific decision / exclusions

Qualitative *global identifiability for fixed source δ=.01* now has quantitative worst-case squared profile separation essentially constrained within ~0.7%, independent of the exact allowed 25 coefficient values. This is a genuine constrained information-model decision; the gap is mathematically strictly positive yet small. An upper Gaussian testing budget now quantifies why global mathematical separation does NOT by itself promise a feasible empirical inverse.

Original Mech/PRF/INT/GEEKY/LT scientific owners untouched, and no external source-prior novelty asserted. M13 FIRST owns original B source and GLS; ROT011 original owner/referee review PENDING, so ROT012 inherits conditional claim ceiling. NO original historical DTC full source production run, no physical covariance, background independence, J3/K, GR or executor sign. One OPTIONAL bounded source referee via existing AUD1 routing, not a compelled cascade.

STATUS: EXACT_SOURCE_INTERVAL_GLOBAL_RHO2_BRACKET / SYNTHETIC_GAUSSIAN_RESOURCE_NECESSITY / REPRO_PASS / OWNER_REFEREE_PENDING / GITHUB_PENDING_BW_INGEST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
