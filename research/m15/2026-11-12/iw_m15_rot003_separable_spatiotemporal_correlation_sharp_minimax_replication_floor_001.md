---
artifact_id: IW_M15_ROT003_TETRAHEDRAL_SEPARABLE_TEMPORAL_CORRELATION_SHARP_MINIMAX_001_20261112
return_id: M15-ROT003-SEPARABLE_UNKNOWN_TEMPORAL_CORRELATION_SHARP_MINIMAX_AND_REPLICATION_FLOOR_001_20261112
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-12
exposure: PUBLIC
result_class: EXACT_CLASSICAL_GAUSSIAN_MINIMAX / SOURCE_ADMISSION_GATE / NEGATIVE_KNOWLEDGE
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_SENSOR_NATIVE_TEMPORAL_NOISE / NO_NASH_PHYSICAL_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE / NO_NEW_TASK_CASCADE
---

# M15 ROT003 — sharp replication floor under separable unknown spatial and temporal noise correlations

## 0. Source and currentness / ownership / question

**Decision question.** M15 ROT002 established sharp robust total-vector Gaussian minimax risk 4 sigma²/N with UNKNOWN four-channel within-block correlations, but expressly assumed noise independence between separate four-channel groups. Is the 1/N improvement still guaranteed if the group noises are correlated and only an upper absolute pairwise correlation kappa is certified?

**Answer: NO except under a suitable vanishing temporal-dependence constraint.** For the exact separable spatiotemporal Gaussian covariance contract in §1, fixed m complete four-channel blocks, N=4m, and 0<=kappa<=1, the sharp global all-estimator minimax total squared Euclidean risk is

    R*(m,kappa)=sigma² [1+(m-1)kappa]/m
               =sigma² (kappa+(1-kappa)/m)
               =(4sigma²/N) [1+(N/4-1)kappa].               (R3.1)

At kappa=0 it reduces exactly to ROT002. For a fixed kappa>0, as m increases the robust risk approaches a **nonzero floor sigma²*kappa**. For kappa=1 it equals sigma² for all m: repeated perfectly correlated four-channel groups cannot be counted as independent evidence. This does not contradict better performance for other individual covariance matrices, including perfectly common spatial noise that the tetrahedral contrast projection eliminates.

**Original-first research lineage.** M14 ROT031 first source-typed tetrahedral geometry, M14 ROT039 first independent-Gaussian exact all-estimator four-axis common-mode minimax, M14 ROT041 original group-size/co-time graph and independence-limited static risk; M15 ROT001 Schall static-to-temporal nonidentifiability; M15 ROT002 exact UNKNOWN within-group covariance contrast minimax:
- M14 ROT039 original blob 80e678005d4a0edd0c6299d8b582e0199f464a8f: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m14/2026-11-11/iw_m14_rot039_common_mode_four_axis_sharp_gaussian_minimax_and_spatial_gauge_001.md
- M14 ROT041 original blob 357d823e604fabfc86b9fc3573743aa126001250: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m14/2026-11-11/iw_m14_rot041_group_size_static_field_graph_connectivity_and_sharp_gaussian_minimax_001.md
- M15 ROT002 original blob 480eeceb30c9169e1bb4800b68f4bbcaf5049761: https://github.com/wmakiela-tech/Nash-iw-research/blob/ee59ca188feabe34e460670a570d2e7cf187a9a7/research/m15/2026-11-12/iw_m15_rot002_tetrahedral_correlated_gaussian_sharp_robust_minimax_001.md
- Schall, Lindner, Rottstaedt et al., Nature Communications 17 (2026) 10825, published 22 October 2026: https://doi.org/10.1038/s41467-026-78386-z . It is the ORIGINAL authors' calculated photon-shot-noise sensitivity LIMIT, **NOT achieved technical-noise sensitivity**. XH-S5 inventory first audited the supplied Schall Source Data ZIP and reports no co-time repeat/correlation time series there; original XH source firstness preserved, no other external Schall raw-data claim. Source inventory https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s5/2026-11-10/iw_xh_s5_eks1_t1_schall_original_source_data_zip_complete_inventory_temporal_no_003.md
- Mature classical host: NIST Engineering Statistics Handbook autocorrelation/randomness independence standard-error caution https://www.itl.nist.gov/div898/handbook/eda/section3/eda331.htm ; University of Zurich clinical biostatistics longitudinal exchangeable repeated-measures design effect https://biostat.pages.uzh.ch/sta404/clin-biostats/14-Longitudinal.html ; Gauss-Markov/Aitken GLS, compound symmetry and Gaussian diffuse-prior mean estimation. **No novelty, source-typed classical special case**, no exhaustive literature search.

Recent #iw-dispatch bounded scan at 2026-11-12 22:35-22:36 CET: KN13 ROT021 forwarded M15 tag but did not task M15 to alter the sensor mathematics; it reviewed Wu-Xu original L1/native, an independent L2 owner script path failure, and PRF13 six-dimension Pauli source results. XH-S6 ROT009 executed original neural task, unrelated. Do not appropriate their firstness or start a new task cascade.

## 1. FROZEN observational and covariance contracts

Let known four tetrahedral directions be rows of A in R^(4x3):

    a0=(+1,+1,+1), a1=(+1,-1,-1),
    a2=(-1,+1,-1), a3=(-1,-1,+1).

Exact Gram properties:

    A^T A=4I3, A^T 1_4=0, AA^T=4I4-1_4 1_4^T.

The unknown **constant across every session** field is z in unrestricted R3. At each of m predeclared physically simultaneous four-orientation complete groups, observe

    Y_k=A z+h_k 1_4+epsilon_k,  k=1,...,m; N=4m.

Each h_k is an unrestricted real nuisance, independent in its value from other h_l (there is **no stochastic assumption** on h). Conditional on parameters the jointly centered errors are multivariate Gaussian with exact **separable** covariance

    Cov(epsilon_{k,i},epsilon_{l,j})=sigma² K_{kl} C_{ij}.

Sigma²>0 is known and each elemental marginal error has variance sigma². Both nuisance correlation matrices are UNKNOWN but shared through all blocks, and satisfy:

    C=C^T >=0, size 4, diagonal=1 (all within-group correlation matrices allowed);
    K=K^T >=0, size m, diagonal=1,
    |K_kl|<=kappa for all k!=l; kappa in [0,1] fixed and known.

Singular K,C are permitted; supremum/minimax unchanged if replaced by positive-definite approximations. The product form is crucial: the theorem is **NOT claimed for arbitrary nonseparable 4m×4m covariance**. No adaptive scheduling/groups, varying field, unknown axes, independent per-axis replication, unequal cost, calibrated real instrument Gaussian statistics, physical PSN transfer, or intervention. Any measurable estimator, including nonlinear/biased, may use all raw data. Loss is E||estimator-z||², supremum over z,h,C,K.

## 2. Uniform upper bound using the tetrahedral projector

Define the fixed four-channel contrast estimator and its repetition average

    w_k=(1/4) A^T Y_k,     z_hat=(1/m) sum_k w_k.

Since A^T1=0, every h_k cancels exactly, no assumption on its smoothness or value. E(z_hat)=z.

Its covariance and total squared risk are

    Cov(z_hat)= [sigma²/(16m²)] (1_m^T K 1_m) A^T C A,

    R(z_hat;K,C)
      = [sigma²/(16m²)] (1_m^T K1_m) tr(A^T C A)
      = [sigma²/m²] (1_m^T K1_m) [1-(1_4^T C1_4)/16].  (R3.2)

Proof uses tr(A^TCA)=tr(CAA^T)=4tr(C)-1^TC1=16-1^TC1.

By positive semidefiniteness, 1_4^T C1_4>=0, so spatial factor <=1. For K with diagonal 1 and all |K_kl|<=kappa,

    1_m^T K1_m = m + 2sum_{k<l}K_kl <=m+m(m-1)kappa.

Therefore for every admissible z,h,K,C, R(z_hat)<=sigma²[1+(m-1)kappa]/m. This immediately gives a uniform bound over ALL unknown correlations.

Notice **the bound is in contrast noise, not merely raw sample correlation**. A purely common spatial channel noise C=11^T has zero contrast risk for any K, even if temporally perfectly correlated. Thus it would be FALSE to claim that any positive temporal correlation necessarily destroys contrast averaging for a fixed real noise law.

## 3. Matching global all-estimator lower bound

Set P=I4-11^T/4 and choose lawful within-block C_*=(4/3)P, hence diag(C_*)=1 and eigenvalues 0,4/3,4/3,4/3. Its six pairwise spatial correlations are -1/3 and its channel sum is identically zero. Define lawful temporal equicorrelation K_*=(1-kappa)I_m+kappa 1_m1_m^T, which has diagonal 1, all offdiag kappa, eigenvalues 1-kappa (mult m-1) and D=1+(m-1)kappa (mult 1). For kappa<1, K_* is PD. Both achieve simultaneously equality in upper bound.

**Full original raw data has no extra z information at these witnesses.** Since col(A)=1_4^perp, each Y_k is invertibly reconstructed from w_k=A^TY_k/4 and s_k=1_4^TY_k/4 using Y_k=A w_k +1_4 s_k. Under C_*, s_k=h_k deterministically. Restrict the permitted nuisance to h_k=0. Then the complete raw experiment reduces EXACTLY to

    w_k=z+eta_k,  joint Cov(eta)= (sigma²/3) K_* ⊗ I3.   (R3.3)

No spatial common-coordinate data are informative for z; the sign/rank of C_* is legal, and temporal correlation is entirely in contrast coordinates. Because K_*1_m=D1_m, for each location component the Gaussian location Fisher precision is

    (3/sigma²) 1_m^T K_*^-1 1_m = (3m)/(sigma² D).

Put a proper diffuse Gaussian prior z~N3(0,tau² I3). For kappa<1, the posterior covariance based on ALL raw data at these legal witness parameters is

    V_tau=[tau^-2 + (3m)/(sigma² D)]^-1 I3.

Any estimator (biased/nonlinear included) has Bayes integrated vector loss at least

    tr V_tau = 3[tau^-2+(3m)/(sigma² D)]^-1.

Let tau→∞. The minimax loss over the entire admissible model is >=sigma² D/m, matching §2. For kappa=1, K_*=11^T; all m eta_k are exactly the same three-dimensional Gaussian vector, so the full experiment has precisely ONE effective Gaussian location observation with covariance (sigma²/3)I3, hence the same limit sigma². As kappa→1 from below the bound is continuous.

If positive-definite C and K are required, use C_eps=(1-eps)C_*+eps I4, and K_delta=(1-delta)K_*+delta I_m with eps,delta>0; the worst-case Bayes risk converges to the displayed value by the Gaussian covariance continuity, so the supremum over the strictly PD class has the same value. For kappa=1, use equicorrelation <1 approaching 1. This is still a proper Gaussian lower argument, not an isolated CRLB or ordinary unbiased-estimator assertion.

Therefore

    inf_all_estimators sup_z,h,C,K E||z_hat_est-z||²
      = sigma² D/m
      = sigma²[kappa+(1-kappa)/m].                         (R3.4)

## 4. Limiting cases and falsifiers

- kappa=0: K=I_m and the result reduces to M15 ROT002, namely sigma²/m=4sigma²/N. It is **not** the independent-CHANNEL M14 risk, which is 3sigma²/N and additionally fixes C=I.
- With C=I and K=I, the fixed estimator has total risk 3sigma²/(4m)=3sigma²/N, matching the M14 r4 static independent-Gaussian contract.
- At any fixed kappa>0, asymptotic minimax risk is sigma² kappa; repeating sessions no longer permits a source-independent zero error certificate.
- kappa=1: errors at distinct sessions can be perfectly identical in the contrast subspace; merely collecting more nominal samples provides no additional location information.
- For m=4, sigma²=1: kappa=0 risk 1/4; kappa=1/2 risk 5/8; kappa=1 risk 1. Same complete four-channel geometry, same elemental variances, different legal temporal correlation.
- C=11^T (fully common across channels) yields zero contrast-estimator risk despite arbitrary K. This is a rigorous **counter-control to an overbroad slogan** that any correlated noise causes a floor.
- No claim of a general effective-sample-size theorem is made; ONLY in this fixed separable, exchangeable worst family a convenient equivalent count of independent *four-channel groups* is m_eff=m/[1+(m-1)kappa]. This reparametrizes the displayed exact minimax risk; it is not an empirical measured m_eff.

## 5. Executable science and audit quality

The original 3414-byte Python3 standard-library Fraction checker was ACTUALLY EXECUTED locally with 98 distinct counted exact assertions PASS (20 m/kappa cases x four checks, 15 extra Gaussian precision crosschecks, three edge controls). It checks A Gram, C_* PSD structure by exact equicorrelation eigenvalue identities, legal temporal compound-symmetry eigenvalues, trace risk at explicit C/K, matching lower precision scalar, independent-channel and perfect-common controls. The dynamic all-estimator minimax lower argument is the separate analytic proof above; 98 exact assertions do not prove the global theorem by themselves.

The initial executed 3414-byte source (SHA256 6992406feb986279f25efad7034b6b0a477e8a12b320d27dba56d3fa38128d96) was published at pinned commit 9bc13b124825538bfedad58249fc56f7291902b4, blob 2c216ceb522709e1376fe705456e6ab411448b7f, and matched the locally executed original bytes. A **portability correction** replaced the absolute result JSON output directory with the sibling path derived from __file__; it did **NOT** change any of the mathematical statements or assertions. Corrected 3429-byte complete source was ACTUALLY REEXECUTED locally, 98 counted Fraction assertions PASS, and also executed in an independently created clean temporary directory. The resulting standalone JSON was BYTE-IDENTICAL to the initial valid JSON; CLEAN_TEMP_RERUN_RESULT_BYTE_IDENTICAL PASS. Corrected source local SHA256=e749c4a34c8b8affeb5c6d8921a27c9e3478deb91cdae6e2899e337047cd6c1a, git blob 18ead21a66707adf917aaeccfb31e701ddaf44c9. Updated GitHub exact source at commit f9f1af5323cfb5c194edfdb1a26eee9f67ddff8f, blob 18ead21a66707adf917aaeccfb31e701ddaf44c9, matching corrected EXECUTED local bytes exactly and full pinned GitHub readback:
https://github.com/wmakiela-tech/Nash-iw-research/blob/f9f1af5323cfb5c194edfdb1a26eee9f67ddff8f/research/m15/2026-11-12/m15_rot003_exact_temporal_correlation_checker.py

Original local machine JSON result SHA256=6b8219ace43631503db436713d6e3702ccef7e25ccf54fa1b1f776636c68e7e0 (3278 bytes); clean temp rerun same exact bytes, not claimed GitHub-hosted. No outside independent referee, observed hardware replication, sensor raw timestamp/correlation extraction, physical performance or NASH physics. The code only enumerates fixed legal test points; universal upper/lower proof is analytic.

## 6. Decision and source admission / stop

The new material delta relative to ROT002 is *not* an improved sensitivity claim: **even if exact spatial covariance is dealt with, 1/N statistical improvement requires certified cross-session independence or a quantitatively decaying temporal covariance condition**. A fixed upper κ that does not vanish across growing m admits a nonzero sharp robust floor in this separable class. The source archive inspected by XH does not supply the required co-time channel readings, timestamps, repeated technical-noise series, nor calibrated K/C structure to determine κ or justify independent groups. Do not substitute optical ODMR frequency sweeps or photon-shot-noise limit slopes for a noise time series.

**Reopen only** on true-same-sample paired multichannel time observations sufficient to estimate the temporal *contrast* covariance and its cross-session dependence, not just per-channel marginals, or on a stronger independently verified physical noise source/protocol that justifies covariance structure. A bound only on a few lags should NOT silently be promoted to a uniform all-pairs κ over an arbitrarily growing calendar. M14 independent conditional results stay valid. No cross-context theory merge, no BW status ownership, no new source task or task cascade.

**Ceiling:** NO_NOVELTY / NO_NATIVE_SCHALL_TIME_RECORD / NO_NASH_PHYSICAL_CLAIM / NO_CANON / NO_EXEC_SIGN / OWNER_ACK_PENDING / INDEPENDENT_REFEREE_PENDING / GITHUB_PENDING_BW_INGEST.
