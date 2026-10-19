---
artifact_id: IW_PRF11_R12_ADAPTIVE_GAUSSIAN_SENSOR_BUDGET_KL_FISHER_VANTREES_MINIMAX_001_20261019
title: "PRF11 R12 — budget czułości w pomiarach adaptacyjnych: KL, Fisher, van Trees i minimaks"
created_at: 2026-10-19
as_of: 2026-10-19
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_10 / PRF11
function: FOUNDATION_FIRST / THEORY_COMPARISON / PRIOR_ART_SUBTRACTION / QUANTIFIER_REPAIR
document_type: REPORT
task_id: IW_PRF11_R12_GAUSSIAN_BUDGET_RISK_BRIDGE_001_20261019
exposure: PUBLIC
status: DRAFT
primary_location: GitHub/research/prf11/2026-10-19/IW_PRF11_R12_ADAPTIVE_GAUSSIAN_SENSOR_BUDGET_KL_FISHER_VANTREES_MINIMAX_001_20261019.md
content_sha256: NOT_AVAILABLE_USE_GITHUB_COMMIT_AND_BLOB_SHA_AFTER_READBACK
provenance: Public NASH-IW scientific source files and scholarly sources explicitly linked below; analytic calculations
derived_from:
  - IW_PRF11_R11_ACTIVE_SENSING_DUAL_CONTROL_RISK_TYPING_AND_PRIOR_ART_SUBTRACTION_001_20261019
  - GEEKY-S10-NC-GPT-TURA1-MATH-ATTRIBUTION-AUDIT-001
  - M13-ROT11-NC-GPT-TURA1-EXACT-NECESSITY-NONCOLLINEAR-AND-SOURCE-SUBTRACTION-001_20261019
supersedes: []
stale_if: Any change of actual legal Gaussian observation contract, independent-preparation resources, feedback coupling, or source-owner accepted claim scope
acceptance_owner: PRF scientific placement, LT4/MT13/NC own source claims; no local promotion
return_path: GitHub artifact plus explicit public-safe scientific dispatch when executed
claim_ceiling: MATURE_STATISTICAL_THEORY / EXACT_CONDITIONAL_BRIDGE / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC / NO_PHYSICAL_UPGRADE
github_check: USED_AS_PUBLIC_SAFE_PRIMARY
cross_surface_sync: GITHUB_PENDING_BW_INGEST
---

# PRF11 R12 — Co z ograniczenia czułości wyniknie dla dowolnego estymatora?

## 0. Currentness & others first

The public 19 Oct 2026 Geeky-S10 mathematical audit and independent M13 R11 mathematical return develop NC's *classical co-axial measurement* model. The relevant deterministic sensitivity statement is conditional:

- The instrument's readout and damping directions coincide, d=e.
- Each impulse with u=exp(-gamma*s) attenuates the readout component and emits sensitivity c=(1-u)(e·v)/gamma.
- Euclidean nonexpansivity of the between-impulse dynamics (mu_2(G)<=0) yields the pathwise budget gamma² Σ_j c_j² <= ||v_initial||².
- Geeky-S10 and M13 distinguish universal freely chosen sensor direction from a fixed apparatus direction. M13 proves a one-pulse violation of the 1/gamma ceiling for mu_2>0 when e is free; Geeky further provides a repeated reset-flow argument under that quantifier.
- For noncollinear e,d, a universal L² sensitivity ceiling may fail even with G=0.
- Neither claim includes automatic statistical interpretation, nor an admitted quantum apparatus. The external audits' own status is exploratory pending owner adjudication.

Public source:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s10/2026-10-19/geeky_s10_nc_gpt_tura1_math_attribution_audit_001.md
M13 R11 source verified on project Drive, but its private URL is intentionally not reproduced here; the public Geeky source covers the necessary mathematical scope.
NC public source and superseding caveats:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-18/IW_NC_BACKACTION_LEDGER_AND_ALIGNMENT_KNIFE_EDGE_010_20261018.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-18/IW_NC_MEASUREMENT_CEILING_IS_THE_LOGARITHMIC_NORM_011_20261018.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-18/README.md

R11 corrected a broad inference from "Fisher sensitivity ceiling" to a universal Gaussian minimax RMSE floor. It gave an explicit biased estimator with MSE 25/106 < 1/4 for R=gamma=1, sigma=1/2, c=0.9.
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-19/IW_PRF11_R11_ACTIVE_SENSING_DUAL_CONTROL_RISK_TYPING_AND_PRIOR_ART_SUBTRACTION_001_20261019.md

No R11 owner acceptance, BW ingestion, or reply on its original dispatch thread was confirmed during this rotation. This is not evidence of rejection.

## 1. Changed research question after mature-host review

Old, invalid upgrade: "If ||c||_2<=1/gamma then every Gaussian estimator has RMSE >= gamma*sigma."

Correct question: "Under an EXPLICIT law for one adaptively sampled, bounded scalar preparation, what unconditional information and minimax-risk LOWER BOUNDS survive for all estimators, including biased ones?"

The mature theorem families are:
- conditional relative-entropy chain rule and Gaussian KL formula;
- likelihood-score martingales in adaptive design;
- Fisher information and classical (unbiased-estimator) Cramér-Rao;
- van Trees Bayesian information inequality for *arbitrary* estimators, including biased;
- Young 2026 *augmented van Trees* preprint, potentially sharper in bounded-parameter minimax problems.
This is mature-host application, not a new law.

## 2. EXPLICIT observational contract; do not silently use this for NC without admission

Fix R>0, gamma>0, sigma>0, a scalar hidden preparation theta in [-R,R], and a FIXED finite number k of observations **of the same preparation**.

Let U be public/exogenous randomness independent of theta. At step j, after history H_(j-1)=(U,Y_1,...,Y_(j-1)), a legal feedback policy selects a real coefficient c_j(H_(j-1)), measurable before observing Y_j. The conditional measurement law is:

  Y_j | H_(j-1),theta ~ Normal(theta*c_j(H_(j-1)), sigma²).

Gaussian innovations are conditionally independent and of identical known variance sigma². The SAME policy (same measurable functions of past observations and exogenous seed) is used under every theta. The policy is not directly informed of the unknown theta.

Assume, for *every legal past observation path and the exogenous seed*:

  Σ_{j=1}^k c_j(H_(j-1))² <= gamma^(-2).      [PATHWISE SENSITIVITY BUDGET]

This is a HYPOTHESIS about a legal **Gaussian readout** equipped with a classical deterministic sensitivity budget. For an NC-style physical model it would follow only when the feedback changes the same collinear state component, the free flow is contractive in the SAME energy norm, the state is linear in the original preparation theta after fixing an observed policy history, and readout noise does not independently inject extra unmodeled dynamical disturbances.

It does NOT cover: parameter-dependent instrument policies, signal-dependent/non-Gaussian or correlated noise, uncontrolled stochastic state backaction, fresh independently re-prepared copies (each has a new energy budget), quantum noncommuting instruments, infinite uncontrolled measurement horizons or a policy-changing estimand.

## 3. Information inequality A: exact pairwise sequential KL

Write P_theta^pi for the law of (U,Y_1,...,Y_k). At each fixed admissible history h, the Gaussian conditional comparison between theta and theta' has equal variance and a shift (theta-theta')c_j(h), so

  KL(N(theta*c_j(h),sigma²) || N(theta'*c_j(h),sigma²))
  = (theta-theta')²*c_j(h)²/(2sigma²).

The sequential KL chain rule (with identical policy-seed law) gives the EXACT identity

  KL(P_theta^pi || P_theta'^pi)
  = (theta-theta')²/(2sigma²) * E_theta^pi Σ c_j(H_(j-1))².

Therefore, from the stated pathwise budget,

  KL(P_theta^pi || P_theta'^pi) <= (theta-theta')²/(2 gamma² sigma²).    (A)

By Pinsker (TV normalized as sup_event |P(event)-Q(event)|),

  TV(P_theta^pi,P_theta'^pi)
  <= min{1, |theta-theta'|/(2 gamma sigma)}.                            (B)

The same bounds hold for a common theta-independent postprocessing of the observed record by data processing.

These are standard KL/TV tools; no new family-independent process geometry is claimed. If the observations themselves change the hidden carrier beyond the declared conditional Gaussian law, (A) is not licensed.

## 4. Information inequality B: Fisher information under adaptive sensing

Conditional log likelihood:

  log p_theta(Y_1,...,Y_k | U)
    = -Σ_j (Y_j-theta*c_j(H_(j-1)))²/(2sigma²) + const.

Its score (differentiation with observed history FIXED) is:

  S_theta = sigma^(-2) Σ_j c_j(H_(j-1)) [Y_j-theta*c_j(H_(j-1))].

Each term is a martingale difference under P_theta. The cross terms vanish, and therefore

  I_pi(theta)=E_theta S_theta²
             =sigma^(-2) E_theta Σ c_j(H_(j-1))²
             <=1/(gamma² sigma²).                                      (C)

The adaptive coefficients may be random; treating them as fixed design values before data collection would be incorrect. The identity uses predictability and conditional Gaussian innovations, not independence of the selected coefficients.

Cramér-Rao yields an RMSE constraint for regular UNBIASED estimators but does not supply the same bound for all biased/minimax estimators on a bounded interval.

## 5. Arbitrary estimators: CLASSICAL van Trees bound

Take the smooth prior supported on [-R,R]:

  lambda_R(theta)=R^(-1) cos²(pi*theta/(2R)) for |theta|<=R,
                   0 outside.

It integrates to one, vanishes at ±R, and has finite prior Fisher information

  J(lambda_R)=int_{-R}^R [lambda_R'(theta)]²/lambda_R(theta)dtheta
              =pi²/R².

For any measurable estimator theta_hat(data) of finite second moment, integration by parts and Cauchy–Schwarz give the classical van Trees inequality:

  int E_theta[(theta_hat-theta)²] lambda_R(theta)dtheta
  >=1/[ int I_pi(theta)lambda_R(theta)dtheta +pi²/R² ].

The proof uses the joint score d_theta log(lambda_R(theta) p_theta(data)). The boundary term vanishes because lambda_R(±R)=0; its covariance with theta_hat-theta is 1; cross terms of prior and likelihood scores vanish by conditional mean-zero likelihood score.

Hence a valid LOWER bound on worst-parameter MSE over ALL (including biased and adaptive) estimators is

  sup_{|theta|<=R} E_theta[(theta_hat-theta)²]
  >= 1/[ 1/(gamma² sigma²)+pi²/R² ].                                   (D)

The right side is not an exact minimax value and can be conservative.

Original host: Gill & Levit (1995), Bernoulli 1(1-2), 59–79, DOI 10.2307/3318681. General form confirmed in Young (2026), sections 1.1–2 and in the mathematical literature.

## 6. BETTER finite-interval lower bound: Young (2026) augmented van Trees

Elliot H. Young, *The augmented van Trees inequality*, arXiv:2603.04686v1 (5 Mar 2026), HTML paper https://arxiv.org/html/2603.04686

The paper's Thm. 2 gives the variational lower bound for minimax MSE on a compact parameter interval:

  sup_t E_t[(hat t-t)²]
  >= sup_{alpha} [ int alpha(t)dt /
                   int sqrt(I(t)*alpha(t)²+alpha'(t)²) dt ]²,

with stated regularity on likelihood, Fisher information and admissible alpha. Example 3 (AVT1) derives the explicit constant-information bound 1/(sqrt(I)+1)² on [-1,1].

Application to the adaptive Gaussian contract:
let t=theta/R in [-1,1]. Its Fisher information is I_t=R² I_pi(Rt) and is uniformly bounded by

  J=R²/(gamma² sigma²).

The mathematical extension from an exact constant I to a UNIFORM UPPER BOUND J is legitimate under Young Thm. 2: for each admissible alpha,
integral sqrt(I_t alpha²+alpha'²) <= integral sqrt(J alpha²+alpha'²).
Young's triangular alpha_delta from Example 3, with plateau on [-1+delta,1-delta] and linear ramps to zero at endpoints, yields in the delta↓0 limit:

  sup_{|theta|<=R} E_theta[(theta_hat-theta)²]
  >= R²/(1+R/(gamma sigma))².                                           (E)

This requires the regularity assumptions of Young Thm. 2 (including the requisite absolute continuity of Fisher information), which hold for fixed-k regular conditional Gaussian models with bounded predictable c_j and a theta-independent policy under the standard dominated-derivative conditions. For more general policies, declare a REGULARITY_UNKNOWN status instead of automatically applying (E).

Combining (D) and (E):

  minmax_MSE >= R² max{
       [pi²+(R/(gamma sigma))²]^(-1),
       [1+R/(gamma sigma)]^(-2)
  }.

This does NOT imply minmax RMSE >= gamma sigma across all regimes; bounded-parameter shrinkage remains legal.

**Primary scholarly attribution:** Young's AVT1 result is a 2026 PREPRINT, not treated as a peer-reviewed theorem; the classic van Trees result is established. R12's algebra is an application and scaling of existing results, NO NOVELTY CLAIM.

## 7. Numeric exact-control brackets (one preparation, gamma=R=1, sigma=0.5)

Sensitivity cap 1/gamma=1; information cap 1/(gamma² sigma²)=4; scaled J=4.

Classical van Trees MSE floor =1/(4+pi²)=0.0721001097855; RMSE floor ≈0.268514636073.
Young AVT1 MSE floor =1/(sqrt(4)+1)²=1/9≈0.111111111111; RMSE floor =1/3≈0.333333333333.

For a single LEGAL finite-strength coaxial pulse at t=0 and s=ln(10), gamma=1, the source sensitivity is c=1-exp(-s)=0.9. Let measured Y=0.9 theta + noise, noise~N(0,0.25). Choosing theta_hat=(45/53)Y gives exactly

  sup_{|theta|<=1} MSE =25/106≈0.235849056604;
  sup RMSE =5/sqrt(106)≈0.485642931179.

Thus for the minimax RMSE over the declared admissible adaptive-policy class:

  1/3 <= minimax_RMSE <= 5/sqrt(106).

This is a rigorously compatible, non-exact bracket. It demonstrates why the old purported floor sigma=0.5 is NOT a universal all-estimator lower bound.

If arbitrary increasing finite s is allowed, c approaches 1 from below, and the same linear shrinkage construction provides the sharper infimum upper bound
  minimax_RMSE <=1/sqrt(5)≈0.447213595500;
that bound is an infimum over permitted finite strengths, not necessarily attained by a finite pulse and NOT a source-approved power/cost policy.

### Independent hand calculation

Given c, R=1 and sigma, estimator wY has worst risk (1-wc)²+w²sigma². Minimizing w gives w=c/(c²+sigma²); worst risk sigma²/(c²+sigma²). For c=9/10 and sigma=1/2 this is 25/106. No code or numerical optimization is needed.

## 8. NONMAPS / falsification gates

1. PATHWISE DETERMINISTIC C_SQUARED BUDGET != STOCHASTIC GAUSSIAN CONDITIONAL LIKELIHOOD AUTOMATICALLY.
2. FISHER INFORMATION CAP != UNIFORM RMSE FLOOR FOR ARBITRARY BIASED ESTIMATORS. Use van Trees and target-typed loss.
3. FIXED SINGLE-PREPARATION BUDGET != N FRESH-INDEPENDENT PREPARATIONS. Resetting the physics may legitimately replenish signal energy.
4. COAXIAL + EUCLIDEAN CONTRACTIVITY != GENERAL FIXED APPARATUS WITH MISALIGNMENT, NONNORMAL GROWTH, OR METRIC CHANGE.
5. ADAPTIVE HISTORY-BASED POLICY != THETA-DEPENDENT ORACLE POLICY. The policy's action rule must be the same under both parameters.
6. FIXED PARAMETER THETA != POLICY-DEPENDENT TARGET TAU_PI(THETA). Active measurement may change the estimand.
7. CLASSICAL DAMPING != QUANTUM MEASUREMENT BACKACTION; no CP instrument, uncertainty relation or physical realizability follows.
8. VAN TREES / YOUNG SCALAR REGULAR ESTIMATION != UNIVERSAL VECTOR, NONREGULAR OR ALTERNATIVE LOSS CONCLUSION.

## 9. Prior-art subtraction, host coverage and literature-provenance record

- Conditional KL and Gaussian conditional KL, Pinsker: classical probability/information theory.
- Fisher score martingale for adaptive Gaussian designs: mature sequential design theory, e.g. Adam Lane (2020), "Adaptive Designs for Optimal Observed Fisher Information", JRSS B 82(4):1029–1058, DOI 10.1111/rssb.12378, https://academic.oup.com/jrsssb/article/82/4/1029/7056028 .
- Classical Bayesian Cramér–Rao/van Trees: Gill & Levit (1995), "Applications of the van Trees Inequality: A Bayesian Cramér-Rao Bound", Bernoulli 1, 59–79, https://www.jstor.org/stable/3318681 .
- 2026 frontier refinement: Elliot H. Young (2026), "The augmented van Trees inequality", arXiv:2603.04686v1, https://arxiv.org/html/2603.04686 . This source HTML was opened and actual Theorem 2/Example 3 mathematical statements checked; preprint status retained.
- For adaptive observation design/likelihood martingale structure see also "Nonlinear Experiments: Optimal Design and Inference Based on Likelihood", Journal of the American Statistical Association 88(422) (1993), https://doi.org/10.1080/01621459.1993.10476305 .

Searches used on 19 Oct 2026 (targeted web, not exhaustive):
  * "van Trees inequality Bayesian Cramer Rao bound prior Fisher information sequential adaptive experimental design predictable Fisher information"
  * "van Trees inequality Gill Levit 1995 applications estimator bounded parameter smooth prior"
  * "Adaptive data collection sequential experiments van Trees inequality Fisher information adaptive sensing predictable regressors Gaussian"
  * "Bayesian Cramer Rao van Trees inequality cosine squared prior bounded interval minimax Gaussian location"
  * "Gill Levit Applications of the van Trees inequality 1995 Project Euclid Bernoulli 59 79 pdf"
  * "Adaptive sensing Fisher information martingale difference adaptive experimental design sequential gaussian regression van Trees minimax bound"
  * "2026 augmented van Trees inequality arxiv adaptive minimax lower bound cosine squared prior"
  * "sequential adaptive experiments KL divergence chain rule Gaussian predictable design Fisher information stochastic adaptive"
  * "chain rule relative entropy conditional distributions KL sequential experiments proof"

Retrieval: primary arXiv HTML Thm. 2 and Example 3 READ; 1995 Bernoulli/JSTOR bibliographic primary record verified, peer reviewed; Lane (2020) peer-reviewed journal article text/abstract read; targeted standard external theory descriptions, not a full monograph reading. Project sources full-text as linked above. Tool-specific search empty results do NOT establish absence of a project result. No code-run empirical experiment was performed; numeric rational/symbolic checks were done analytically and on independent calculator. No peer-review assertion for Young.

Scientific distinction: project-local assembly of classical conditional Gaussian design + an external 2026 statistical refinement is a **legible conditional theorem application**, not evidence of a new scientific discovery. An actual observation/readout law, stable same-preparation budget and loss must be certified by the appropriate source owner for any empirical application.

## 10. Return and freeze

RESULT: EXACT_CONDITIONAL_STATISTICAL_BRIDGE / MATURE_HOST_ABSORBED / FIXED_PREPARATION / GAUSSIAN / SEQUENTIAL.
REVIEW: source-owner audit of the sensor-to-Gaussian-law contract PENDING; GitHub readback must be checked; Slack delivery if attempted must be separately evidenced.
BOUNDARIES: NO_CANON / NO_EXEC / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE.
