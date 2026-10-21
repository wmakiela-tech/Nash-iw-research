# XH-S4 — October 2026 operator/physics/inference source audit: Poisson-GENERIC, MM nonlocal gravity, DALI
RETURN_ID: XH-S4-OCT2026-POISSON-GENERIC-MM-NONLOCAL-DALI-SOURCE-AUDIT-009_20261021
DATE: 2026-10-21
CELL: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03 / XH-S4
PURPOSE: next independent science rotation after October literature map 006 and full-text audits 007/008.
RESULT_CLASS: THREE_PRIMARY_FULLTEXT_HYPOTHESIS_TESTS_AND_SOURCE_MAP / MATHEMATICAL_PRIOR_ART_AND_NEGATIVE_KNOWLEDGE
SOURCE_LEVEL: FULL PRIMARY ARXIV HTML READ + LITERAL FORMULAE/RESULTS; NOT independent proof reproduction or experiment.
AUTHORITY: NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_NOVELTY / NO_K_J3_TRANSFER / NO_BW_INGESTION_ASSUMPTION / NO_NEW_CELL_TASKS

## A. Primary paper 1 — October 12 v2 Poisson-GENERIC (structural exactness vs source-law validity)
Sulskis, Ravi, `Poisson-GENERIC Neural Operators: Exact Metriplectic Structure in Function Space via Casimir Entropies`, arXiv:2610.05570v2 [cs.LG] (Oct 12).
Primary full text: https://arxiv.org/html/2610.05570

Construction, source Sec 3 + Appendix C:
- z=(u,s), latent entropy density s, S=int s, delta S/delta z=(0,1); mechanical block L acts on u alone, so L delta S=0 identically; friction M=AA^T, M delta E=0 by pointwise design.
- For nonlinear scalar transport, L_u = alpha D + lambda P(uD + Du)P, D=sum partial_a, P 2/3-rule Fourier projector. Compatible Poisson pencil in CONTINUUM; L constant case Poisson everywhere.
- Source Appendix Proposition 2: the nonlinear DISCRETE Jacobi holds on a declared Fourier band where cubic products alias-free, NOT all full-spectrum fields. Tested full-spectrum Jacobi residual 0.17..0.78, alias-free band ~1e-16.
- Appendix Remark: generic learned multiplier a(k) inserted with uD+Du is NOT compatible; Jacobi residual order 1e-1 even on band-limited inputs. Explicit operator family matters, not just skewness.
- Data §4: wrong Euclidean scaling rather than proper variational/Riesz derivative causes transfer error on 64/128/256 grid ~0.011 -> 0.078 -> 0.125; corrected scaling gives ~0.0112 stable. These are authors' selected test values, not NASH data.
- Integration §5: split step exact only for the LINEAR reversible flow, NOT for full learned E; discrete-gradient method required for exact discrete E/S laws, and its nonlinear fixed-point solve failed for trained 2D heat Transolver. Authors report training cost 25–40x some baselines. No unrestricted efficient or universal structure certificate.
- Most important explicit negative control, authors' Broader Impact: learned-energy ablation conserved ITS OWN E at 1e-8 while PHYSICAL wave energy grew 6-fold within 10 frames and 30-fold within 40. This is a decisive separator: algebraic exactness of wrong modeled conserved quantity is not physical-law satisfaction. It does not refute their constrained approach; it constrains interpretation of model's own invariants.

Legally relevant NASH:
(i) DTC0a TT projection and field masks: proof of continuum Poisson/Jacobi in source host is NOT proof of discrete K/J3 vanishing. Need a precise identity, compatible projector and alias-free class.
(ii) Auxiliary/latent s is internal model coordinate; not independent physical entropy measurement. Metriplectic model class can be wrong for open/forced systems, yielding "perfect" residual by construction.
(iii) Two independently necessary checks: declared invariant algebraically exact on given discrete realization; target/readout physically calibrated to ground truth. These are different claim types. No physical import or discovery.

## B. Primary paper 2 — October 14 v1 Maggiore-Mancarella RR nonlocal gravity / full retarded prescription / restricted observational family
Amendola, Ayuso, Chakraborty, Rubio, Das, `Nonlocal Gravity, Restricted CPL Dynamics and DESI Constraints`, arXiv:2610.20720v1 [astro-ph.CO], Oct14.
Primary full text: https://arxiv.org/html/2610.20720

- Action: S=(M_Pl^2/2) integral sqrt(-g)[R-(m^2/6) R Box^{-2}R] + S_m. D'Alembertian Box=g^munu nabla_mu nabla_nu, Box^-1 explicitly RETARDED Green operator. Localized U,S equations Box U=-R; Box S=-U. General solutions U=U_hom-Box_ret^-1 R, S=S_hom-Box_ret^-1 U. Homogeneous pieces fixed by prescription+initial/boundary conditions; neither unconstrained propagating new physical field nor arbitrary choice after setting the model.
- Their cosmological realization: spatially flat FLRW, particular initialization N_ini=-20.7233 (a=1e-9), V_0=V'_0=U'_0=0, U_0 selected from H(N=0)=H0 normalization. Distinct path A/B depending on U0 vs threshold. Observable MCMC applies PATH B chosen prescription, not all model realizations.
- Parameter gamma=m^2/(9H0^2) and background effective CPL w_DE(a)=w0+wa(1-a). For fixed cosmological params, gamma -> one-dimensional trajectory of (w0,wa), NOT freely adjustable 2-parameter plane. Local relation near LambdaCDM-like endpoint wa=-alpha_NL(1+w0)+O((1+w0)^2), alpha_NL≈0.686 for fiducial params. This matching shares present value and first derivative near N=0, not whole redshift history.
- IMPORTANT subtlety gamma->0 in action reduces GR without explicit cosmological constant, but after imposing H(today)=H0 their required U0 diverges as gamma->0 while gamma U^2 remains finite. The resulting NORMALIZED BACKGROUND approaches LambdaCDM-like cosmology. Therefore "gamma->0 limit" and "fixed U0 limit" differ: noncommuting limiting procedure / singular realization scaling. Paper explicitly states it, equations (10) and prose after.
- Empirical authors' Planck 2018+DESI DR2 BAO+Pantheon+ for path B: gamma<0.00495 at 95% credibility; delta chi2_min=-2.654 relative to LambdaCDM for one extra parameter, delta AIC=-0.654; not statistically meaningful preference for nonlocal regime. Gamma prior Uniform [0.001,0.2]; posterior accumulates near lower prior boundary. Paper notes different inverse-operator prescriptions/homogeneous solutions still open, and full perturbation-sector validation not done.

Legally relevant NASH:
- A nonlocal action's Box^-1/Box^-2 is not complete physical model without Green kernel, domain/boundary data, retarded/advanced prescription and realization. A mathematical local auxiliary-field reformulation should never by itself create new physical degrees of freedom.
- A local (w0,wa) match is not exact cosmic-history equivalence; requires full observational likelihood from proper forward model. Important for identifiability and shared-realization discussions.
- Singular limit: limiting parameter to zero under adjusted auxiliary initial data need NOT equal holding auxiliary initialization fixed and setting parameter zero. Need declare what is held fixed for any claim of background/local limit.
- No direct NASH NCDG theory, J3/K, or PBH BBN transfer. This is Maggiore-Mancarella specific.

## C. Primary paper 3 — October 1 DALI non-Gaussian parameter bias / data mismatch direction
Sarcevic, van der Wild, Sellentin, `Non-Gaussian Parameter Bias: Formalism and Validation`, arXiv:2610.02104v1 [astro-ph.CO], Oct01.
Primary full text: https://arxiv.org/html/2610.02104

- Data systematic delta m_X = A s_X; covariance-weighted scalar magnitude d_data=sqrt(delta m^T C^-1 delta m). Unit covariance-direction s_hat_X=s_X/sqrt(s_X^T C^-1 s_X). Distinct directions with same scalar d_data probe different nonlinear model geometry.
- Two systematic templates alpha,beta have linearly additive SOURCE perturbations in data space, but induced parameter posterior shifts can be nonadditive. It is nonlinear inference, not source cross term.
- Specific controlled 2-parameter numerical case with amplitude A=20: Delta v numerical MAP=-0.15055, Gaussian Fisher +0.02600 (WRONG SIGN), DALI=-0.14985. Authors show corrected posterior deformation and nonadditivity. Source abstract reports d_data<=5 in tested examples; explicitly says this is not a universal validity threshold (depends on direction/model geometry).
- Interpretation: cannot treat size of model/data mismatch as complete prognostic of parameter bias; error DIRECTION, covariance, nonlinear map, and priors matter.
- No automatic use of DALI for arbitrary high-dimensional or time-dependent PBH likelihood: first identify actual likelihood, C, parameter map, systematic nuisance family and validate against full posterior simulation; target loss/residual is not same as inferred shift.

Legally relevant NASH:
- PRF11 identifiability/decision target: distinguish observability, scalar residual and direction-dependent posterior displacement.
- Front B if future BBN Yp+D/H likelihood: donor diagnostic that charge normalization/floor/systematics may move inferred bounds nonlinearly, not general additive/factor-two extrapolation. NOT an actual BBN computation. No NASH PBH bound.
- Important exact guard `SAME_SCALAR_RESIDUAL != SAME_INFERENCE`.

## D. Three-stage science-quality criterion from primary sources (source-aware synthesis, NOT new theorem)
1. MATHEMATICAL_LEGALITY: exact operator and Hilbert/domain/adjoint/type; for grid residual, original identity and alias-free or otherwise controlled class.
2. MODEL_REALIZATION: physical source/observable, Green prescription + homogeneous initial data, latent variable semantics, which quantity is actually conserved, and selection of limit.
3. EMPIRICAL_INFERENCE: source data, nuisance covariance/likelihood, geometry + direction of systematics, proper model comparison including degrees of freedom and observational uncertainty.

Strong link to NASH existing claim ceilings: algebraic exactness, numerically stable diagnostic, and empirical support are three noninterchangeable evidence classes. No new cross-cell task cascade or owner promotion.

## E. Provenance and date integrity
This rotation deep-reads previously SCOUTED October arXiv papers: it does not present them as newly discovered after report 006. Full texts source date checked Oct01, Oct12 v2, Oct14 respectively. No independent proof verification / data reanalysis.
KEEP_NEGATIVE:
- exact model E_theta does not imply exact physical energy or target dynamics;
- continuum Jacobi does not imply full-grid Jacobi;
- inverse Box is not defined by differential symbol alone;
- auxiliary fields with fixed retarded kernels are not automatically additional physical DoFs;
- gamma limit requires controlled initial-data prescription;
- same d_data can cause different posterior bias, including reversed sign.
STATUS: SOURCE_HOST_FULLTEXT_VERIFIED / NO_NEW_NASH_THEOREM / NO_PHYSICAL_CLAIM / NO_EXEC_SIGN / BW_PENDING / NO_NEW_TASK.
