---
artifact_id: IW_PRF11_R14_CORRELATED_NOISE_COVARIANCE_SEAM_WEAK_STORAGE_STATISTICAL_COUNTEREXAMPLE_001_20261021
title: PRF11 R14 — Correlated-noise seam: finite weak sensor storage does not control statistical information without covariance geometry
created_at: 2026-10-21
as_of: 2026-10-21
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_10 / PRF11
function: FOUNDATION_FIRST / OTHER_CELLS_FIRST / EXACT_NONMAP / PRIOR_ART_SUBTRACTION
document_type: REPORT
task_id: IW_PRF11_R14_CORRELATED_NOISE_SEAM_001_20261021
exposure: PUBLIC
status: DRAFT / INDEPENDENT_REVIEW_PENDING
primary_location: GitHub research/prf11/2026-10-21/IW_PRF11_R14_CORRELATED_NOISE_COVARIANCE_SEAM_WEAK_STORAGE_STATISTICAL_COUNTEREXAMPLE_001_20261021.md
content_identity: use verified Git blob SHA and exact readback
provenance: direct full text project sources plus primary peer-reviewed journal and full arXiv HTML source; self-contained algebra
derived_from:
  - IW_PRF11_R13_ADAPTIVE_WEAK_SENSOR_LECAM_INFORMATION_MINIMAX_COLLAPSE_001_20261021
  - GEEKY-S10-HETEROGENEOUS-ACTION-FAMILY-WEAK-STORAGE-CEILING-001
  - IW_INT8_NONQUADRATIC_AVAILABLE_STORAGE_WEAK_MEASUREMENT_UNIVERSAL_CEILING_001_20261021
supersedes: []
stale_if: source-specific stochastic reset or covariance contract changes; owners supersede source theorems; independent referee finds type or arithmetic error
acceptance_owner: LT5, INT8, Geeky-S10, SW/REC scientific evaluation; Moderator controls EXEC/canon
return_path: GitHub artifact and verified bounded project dispatch
claim_ceiling: EXACT_STANDARD_GAUSSIAN_SEAM / NO_CANON / NO_EXEC / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE
cross_surface_sync: GITHUB_PENDING_BW_INGEST
---

# PRF11 R14: noise *precision*, not the energy of the unwhitened signal, is the statistical information resource

## 0. As-of-21-X achievements of OTHER CELLS — checked BEFORE this rotation

Read full public project sources, including the corrections that arrived after PRF11 R13.

**INT8** (21 X) proved a finite nonquadratic available-storage weak limit in a fixed-e classical reset model:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/int8/2026-10-21/iw_int8_nonquadratic_available_storage_weak_measurement_universal_ceiling_001.md

**Geeky-S10** independently closed the same nonquadratic residual and then generalized to a finite common extremal storage V_* over an *entire heterogeneous readout/reset action family*. At strength s_j<=epsilon, the full unwhitened noiseless record satisfies

  ||C_pi x||_2² <= epsilon V_*(x),    V_*<infinity for every x.

This holds uniformly over arbitrary finite counts, times and admitted heterogeneous action choices, and pathwise even for causal selection in the deterministic reset carrier. Coaxiality is not necessary for this abstract implication; a FINITE COMMON V_* is. Its exact projective-endpoint plus convex Bellman proof is other cells' work, not PRF11's. The previously published ellipsoidal P proof gives a sharper coefficient epsilon/(2-epsilon) within its subclass.
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s10/2026-10-21/geeky_s10_fixed_sensor_nonquadratic_weak_storage_ceiling_001.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s10/2026-10-21/geeky_s10_heterogeneous_action_family_weak_storage_ceiling_001.md

**REC10** repaired the quantifiers in the deterministic triangular factorization for heterogeneous sensors, reset directions and zero strengths. Its noncollinear repeated-readout example makes V_* infinite and therefore does NOT refute Geeky's later general finite-V_* theorem.
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/rec10/2026-10-21/IW_REC10_ROT04_DETERMINISTIC_RESET_CAUSAL_FACTORIZATION_HETEROGENEOUS_STRENGTHS_DIRECTIONS_REFEREE_001_20261021.md

**LT5** (21 X) obtained exact scalar hard-amplitude actuation recovery decomposition; this is a DIFFERENT controller and risk class, not a Gaussian estimation result.
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/2026-10-21/lt5_scalar_target_amplitude_limited_output_feedback_minimax_decomposition_001.md

**PRF11 R13** (21 X) applied the earlier ellipsoidal-storage bound to a SINGLE preparation and independent fixed-variance Gaussian innovations, obtaining KL/Le Cam and squared-error minimax collapse. That mathematical theorem remains valid *under its independence assumption*. Recipient replies to its Slack parent thread: none verified in the checked thread. No acceptance should be inferred from message posting.
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-21/IW_PRF11_R13_ADAPTIVE_WEAK_SENSOR_LECAM_INFORMATION_MINIMAX_COLLAPSE_001_20261021.md

## 1. Question coevolution after host theory comparison

OLD: Does finite nonquadratic available storage imply weak output norm collapse? **Already solved by INT8 and Geeky-S10. Stop claiming as residual.**

NEW: If weak output signal vanishes in Euclidean l2, does it follow that the *statistical experiment* becomes uninformative when every individual readout has fixed nonzero noise variance?

ANSWER: NO. The missing datum is the full covariance/precision geometry of the noise. The correct known Gaussian experiment invariant is the Mahalanobis/whitened signal norm c^T Sigma^(-1)c, not ||c||_2² or marginal variance alone.

Mature host families:
- optimal design with correlated observations and exact Fisher covariance weighting;
- Bayesian linear Gaussian inverse problems with weighted likelihood precision;
- Le Cam/Blackwell statistical experiments, Gaussian shift, testing/minimax risk;
- available storage and dissipativity (project source prior-art absorbed).

## 2. Exact positive result under a UNIFORM covariance floor (fixed deterministic protocols)

Let theta in [-R,R], x0=theta*v for fixed v, and choose one finite PREDETERMINED epsilon-weak protocol pi of any length N. Its full ideal signal is theta*c_pi, c_pi=C_pi v in R^N. From the project source,

  ||c_pi||² <= epsilon V_*(v).                          (2.1)

Declare the observed law

  Z | theta,pi ~ N(theta*c_pi, Sigma_pi),

where Sigma_pi is symmetric strictly positive definite, independent of theta. The noise is a vector readout error; it does not enter the deterministic reset. Cross-shot correlation is allowed.

Exact mature Gaussian likelihood algebra yields

  D_KL(P_theta^pi || P_theta'^pi)
    = ((theta-theta')²/2) c_pi^T Sigma_pi^(-1) c_pi,   (2.2)

  I_pi(theta) = c_pi^T Sigma_pi^(-1) c_pi.            (2.3)

If, for ALL considered protocols and N,

  Sigma_pi >= sigma_*² I_N,  sigma_*>0 FIXED,          (2.4)

then

  I_pi <= epsilon V_*(v)/sigma_*²,                    (2.5)
  D_KL(P_theta^pi||P_theta'^pi)
    <= ((theta-theta')²/2) epsilon V_*(v)/sigma_*²,   (2.6)

and Pinsker gives uniform distance to the parameter-independent experiment with law P_0^pi:

  TV(P_theta^pi,P_0^pi)
    <= |theta| sqrt(epsilon V_*(v))/(2 sigma_*).      (2.7)

Thus the Le Cam distance to a no-information experiment is O(sqrt epsilon), uniform in finite N and fixed protocols. The old two-point Bayes/information-radius proof gives for arbitrary estimators and worst-case squared loss:

  R²[1 - R² epsilon V_*(v)/sigma_*²]_+
      <= J_pi <= R².                                  (2.8)

**Scope:** (2.2)-(2.8) are proved here for nonadaptive predetermined protocols with theta-independent JOINT Gaussian Sigma_pi. An arbitrary outcome-adaptive protocol with correlated noise need not retain the R13 conditional score law; history-dependent conditional innovations can acquire theta-dependent means. One must type and bound the full causal innovation/whitening operator before claiming an adaptive extension. We do NOT silently transport the fixed-design proof to that class.

Condition (2.4) is sufficient and often unnecessarily strong. The *source-native minimal information criterion* for a given Gaussian signal family is a uniform bound

  c_pi^T Sigma_pi^(-1)c_pi = o(1)

across the protocols/parameters of interest (a precision-weighted signal bound). This need not require lower-bounding every covariance eigenvalue if the signal avoids near-null-noise directions.

## 3. Exact 2-shot POSITIVE-DEFINITE counterexample with FIXED per-shot variances

Use the scalar classical reset-flow member of Geeky's theorem:
n=1, G=0, e=1, x0=theta in [-R,R]. Two measurements of identical legal strength s in (0,1), with zero waiting and reset x^+=(1-s)x^-.

Then

  c_s = (s, s(1-s))^T,
  ||c_s||² = s² [1+(1-s)²] ->0.                        (3.1)

The all-strength available storage is finite V_*(theta)=theta²; source weak-energy hypotheses are satisfied.

Take correlated Gaussian readout errors eta_s with covariance

  Sigma_s = sigma² [[1, -1+s²],
                    [-1+s², 1]], sigma²>0.           (3.2)

For every s in (0,1): Sigma_s is POSITIVE DEFINITE, eigenvalues sigma²*s² and sigma²*(2-s²) are strictly positive. Both MARGINAL variances are EXACTLY sigma², independent of s. Only the correlation rho_s=-1+s² depends on s.

Observation model Z=theta*c_s+eta_s (noise does not alter reset). Take the STATISTIC

  T_s = (Z_1+Z_2)/(s(2-s)).                            (3.3)

The signal part is exactly theta. The noise numerator variance is

  Var(eta_1+eta_2)=2sigma²(1+rho_s)=2sigma²s².

Therefore EXACTLY for every 0<s<1,

  T_s | theta ~ N(theta, 2sigma²/(2-s)²),             (3.4)

and as s->0 the noise variance tends to sigma²/2 — a NONZERO FINITE precision rather than disappearing statistical information.

FULL Fisher information is

  I_s = c_s^T Sigma_s^(-1)c_s
      = (2-s)²/(2sigma²)
        + s^4/[2sigma²(2-s²)],                        (3.5)

where decomposition is along sum and difference eigenvectors. Thus

  lim_(s->0) I_s=2/sigma²>0.                           (3.6)

Under INDEPENDENT Gaussian readout errors with the exact same marginal sigma², by contrast,

  I_s^iid
     = s²[1+(1-s)²]/sigma²
       ->0.                                          (3.7)

**Sharp nonmap:** a deterministic signal record with vanishing Euclidean energy and individually nonzero fixed noise variance may retain order-one parametric Fisher information when the joint noise covariance degenerates along the signal direction.

This is a simple special case of known Gaussian generalized least squares and experiment comparison. No mathematical novelty is claimed.

## 4. Explicit minimax-estimation witness, not just Fisher

Fix R=1 and sigma²=1/4. Then T_s from (3.3) has variance

  v_s = (1/2)/(2-s)² ->1/8.

Use the BIASED shrinkage estimator

  theta_hat_s = T_s/(1+v_s).

For every theta in [-1,1], the MSE is

  (theta/(1+v_s)-theta)² + v_s/(1+v_s)²
  = (v_s² theta²+v_s)/(1+v_s)².

Hence exact worst-case MSE is

  sup_|theta|<=1 MSE
    = v_s/(1+v_s)
    -> (1/8)/(9/8)=1/9.                              (4.1)

In particular the minimax error J_s<=v_s/(1+v_s) ->1/9, while the no-observation minimax MSE is 1. This gives a bounded-away-from-zero improvement in the limit. It does NOT claim that this estimator attains the exact Gaussian minimax risk.

Independent arithmetic table (all entries dimensionless, sigma²=0.25):

  s       Fisher correlated  Fisher independent  explicit worst-MSE via T_s
  0.1     7.2201005025       0.0724              0.1216545012
  0.01    7.9202000100       0.00079204          0.1121051098
  0.001   7.9920019997       0.000007992004      0.1112099397

Reproduction: use (3.2), sum variance, two-mode covariance inversion and biased MSE formula above. No simulation, optimization or environmental randomness is needed. This is an analytic exact counterexample.

## 5. Correlation scaling threshold — a falsifiable parameter family

More generally, retain every marginal variance sigma² but let

  rho_s = -1 + s^p,   p>0, 0<s<1.                     (5.1)

The variance of the SUM readout is 2sigma²s^p. The total Gaussian Fisher information is

  I_s = (2-s)² s^(2-p)/(2sigma²)
      + s^4/[2sigma²(2-s^p)].                         (5.2)

Therefore:
- p<2: I_s->0;
- p=2: I_s->2/sigma²;
- p>2: I_s->infinity.

The results all have fixed equal MARGINAL noise variance. It is the rate of near-singularity of the COMMON covariance relative to the chosen signal subspace that sets the statistical phase of the toy experiment.

One can use p=2 for a positive definite exact witness without singular covariance at any finite strength. The singular limit s=0 is OUTSIDE the statement. The family is a statistical thought experiment, **not** a claim that one physical detector can engineer rho_s=-1+s^p for arbitrary p at no cost.

## 6. Can causal feedback be included?

SOURCE: Geeky-S10 proves a pathwise deterministic storage inequality even for actions selected causally from earlier exact records. PRF11 R13 adds a distinct observation-law assumption: conditionally independent Gaussian noise innovations and parameter-independent policy rules. Under that assumption its sequential chain rule is licensed.

For general correlated readout noise, **conditional likelihoods are different**: the conditional distribution of eta_j given earlier measurements can depend on theta through previous residuals (Z_i-theta*c_i). A naive substitution of a marginal sigma² in the R13 KL formula is illegal.

A possible source-native path is innovations whitening under a declared causal Gaussian state-space noise model with a UNIFORM positive lower bound on conditional innovation variances AND on the effective whitened signal sensitivity. Merely assuming each marginal variance >=sigma² does not provide such a bound. Nor does a joint covariance lower bound for every hypothetical frozen path automatically establish it when the design policy changes endogenously.

This report deliberately does NOT assert an adaptive-correlated-noise theorem.

## 7. Mature host subtraction with PRIMARY scholarly evidence

A. Attia & E. Constantinescu, "Optimal Experimental Design for Inverse Problems in the Presence of Observation Correlations", *SIAM Journal on Scientific Computing* 44(4), A2808–A2842 (2022), DOI 10.1137/21M1418666. Publisher peer-reviewed record and **full author preprint HTML** verified. The preprint's §2.1 eqs (1)-(3) explicitly use the full observation-noise precision Gamma_noise^(-1) in the Gaussian likelihood and posterior precision; §3 treats covariance-aware optimal design. Our (2.2)-(2.3) are elementary Gaussian-shift specializations of this mature setting; the source did not establish or claim this project's particular 2-shot construction. Publisher https://doi.org/10.1137/21M1418666 ; full arXiv HTML https://arxiv.org/html/2007.14476 .

M. Patan & B. Bogacka, "Optimum experimental designs for dynamic systems in the presence of correlated errors", *Computational Statistics & Data Analysis* 51(12), 5644–5661 (2007), DOI 10.1016/j.csda.2007.05.030. Publisher abstract and metadata checked, not full article proof. This is a mature direct host for sensor timing with correlated observation errors, not a claimed identical theorem. https://doi.org/10.1016/j.csda.2007.05.030 .

A. Pázman, "Information contained in design points of experiments with correlated observations", *Kybernetika* 46(4), 771–783 (2010). Original journal archival record and bibliography checked, PDF theorem details not inspected. https://dml.cz/handle/10338.dmlcz/140783 .

A. Pázman & W. G. Müller, "Optimal design of experiments subject to correlated errors", *Statistics & Probability Letters* 52(1), 29–34 (2001), DOI 10.1016/S0167-7152(00)00201-7. Publisher abstract and metadata verified, not full article. https://doi.org/10.1016/S0167-7152(00)00201-7 .

Classical Gaussian shift/GLS, information monotonicity, Pinsker, Blackwell/Le Cam statistical-experiment comparison provide all the statistical ingredients. NASH's finite-V_* storage result supplies the source-specific unwhitened signal premise. This synthesis is an EXACT_TYPED_NONMAP, NOT a claim to discover a new statistical phenomenon.

Search log (targeted, not exhaustive), 2026-10-21, general web:
- "Gaussian mean estimation correlated noise Fisher information c transpose Sigma inverse c minimum covariance eigenvalue"
- "experimental design correlated observations singular covariance noise cancellation anti correlated measurement Fisher information"
- "Gaussian statistical experiments comparison covariance same Cameron Martin norm KL relative entropy covariance"
- "bandit adaptive experimental design correlated observation noise innovations whitening sequential KL"
- "Attia Constantinescu 2022 optimal experimental design inverse problems presence observation correlations preprint arxiv pdf"
- "Patan Bogacka 2007 optimum experimental designs dynamic systems correlated errors full text pdf"
- "Pázman Müller 2001 optimal design experiments subject correlated errors Fisher full text"
- "Gaussian mean shift KL Mahalanobis covariance formula textbook statistical experiments mean unknown covariance known pdf"

Primary project sources: full text directly fetched by connected GitHub tool; no private folder IDs or private cross-cell material copied into this public body. External: one full preprint HTML read, three publisher/journal abstract/metadata records. No systematic proof-by-proof global survey, no separate numerical simulation, no physical instrument evaluation.

## 8. Implications for the IW scientific direction and explicit STOP

For a claimed "weak records => vanishing statistical information" upgrade in a real source, the cheapest falsifier is a precise covariance/innovation contract:
- fixed one-preparation source and common legal policy class;
- deterministic normalized signal map after measurement backaction;
- noise-covariance operator on the COMPLETE recorded data, including cross-shot correlations;
- noise-whitened signal norm or a uniform covariance lower bound on the relevant signal subspace;
- appropriate target/loss and explicit physical costs for producing correlations.

A detector with engineering constraints may not realize the thought-experiment noise covariance. No quantum completely positive instrument, independent shot-noise statement, or physical resource budget has been derived. This mathematical counterexample therefore cannot adjudicate quantum measurement limits, NC physics, NCDG, DTC or PBH.

The new project-local result is a **source-typed, exactly reproducible counterexample** showing why the stronger Geeky-S10/INT8 nonquadratic weak-signal theorem still cannot be read as statistical information loss without specifying JOINT noise precision. It keeps R13 intact for iid innovations and narrows an unsafe extension.

CONCLUSION:
  FINITE_COMMON_VSTAR_AND_WEAK_RECORD_L2 => O(sqrt epsilon) UNWHITENED SIGNAL (OTHERS' SOURCE RESULT).
  PLUS_GAUSSIAN_UNIFORM_COVARIANCE_FLOOR => O(sqrt epsilon) EXPERIMENT_CLOSENESS (MATURE STATISTICS APPLICATION).
  FIXED_MARGINAL_NOISE_VARIANCES_ALONE => NOT SUFFICIENT; EXACT POSITIVE-DEFINITE CORRELATION COUNTEREXAMPLE.
  ADAPTIVE_CORRELATED_NOISE => OPEN WITHOUT CAUSAL INNOVATION CONTRACT.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE / GITHUB_PENDING_BW_INGEST.
