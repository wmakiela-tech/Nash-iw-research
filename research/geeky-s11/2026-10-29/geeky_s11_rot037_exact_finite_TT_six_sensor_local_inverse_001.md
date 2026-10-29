---
artifact_id: GEEKY-S11-ROT037-EXACT-FINITE-TT-LOCAL-INVERSE-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-29
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
class: SOURCE-COMPATIBLE-EXACT-FINITE-SIX-TT-JACOBIAN-LOCAL-INVERSE
status: FOUR-DIRECTED-INTERVAL-DET-CERTS-AND-10404-EXECUTED-CONTROLS-PASS
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# ROT037 — finite-grid local TT inverse without the ROT036 continuum-model bias

## Source, own science and epistemic contract

Geeky ROT015–017 first identified source even raw-k TT realcast defect and corrected orthogonal real compatible B=GA; ROT027 exact averaged one-Lie insertion; ROT033 variable-source-filter schedules; ROT034 exact non-identifiability for arbitrary schedules observed through two TT output fields; ROT035 limited six-level five-TT known-gain inversion; ROT036 six-TT UNKNOWN-gain continuum inverse and its LARGE noiseless finite-N model-bias falsifier. ROT037 does NOT reassign those results. It replaces only the continuum forward model by the exact SOURCE-FINITE product for the same RESTRICTED six-known-level schedule and proves a LOCAL inverse at four finite grids. Classical inverse-function theorem and interval arithmetic, not mathematical novelty.

UNCHANGED preserved auxiliary helper: deepseek_python_20260627_a87249.py SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. Original production dtc0a_runtime_v0_3_1.py is NOT available. Full unmasked even N³ flat symmetric tensors with genuine B=GA, C=(0,cos x,0), original centered THREE-term Lie and Ealpha=I+alpha h²Delta2; not historic h=fI/masked KA, not physical NCDG.

## Exact finite source law and analytic Jacobian

Fix A=.009, beta=.12, known six cumulative dose levels x_j=jA/5, known ramp velocity v=.012, and six unknown positive plateau durations d_j with sum D=.25; 5 ramps last A/v=.75. Unknowns theta=(gain t>0,d0,..,d4), d5=D-sum0..4 d_j>0. Let a_d(u) be the continuous nondecreasing piecewise-linear cumulative dose, constant on each plateau and slope v on each ramp. For N even set m=round(beta N²), and for j=1..m
alpha_j=N²[a_d(j/m)-a_d((j-1)/m)] in [0,1/6], sum_j alpha_j=N² A.

For the SIX source TT sidebands (p,s)=(2,-),(2,+),(3,-),(3,+),(4,-),(4,+), with a_in=sin²(pi p/N)+sin²(pi/N), a_out=sin²(pi(p+s)/N)+sin²(pi/N), let qi_j=1-4alpha_j*a_in and qo_j=1-4alpha_j*a_out. Then exact observed scalar amplitude
y_(p,s)=t*Omega_(p,s),
Omega_(p,s)=(m+1)^(-1) SUM_(ell=0)^m [PROD_(j<=ell)qi_j]*[PROD_(j>ell)qo_j].
There is NO approximation by continuum heat kernels or the ROT036 affine matrix.

Analytic derivative: at any temporal mesh node u=k/m strictly inside ramp r=0..4, partial a_d(u)/partial d_l=-v for l<=r and zero for l>r; on a plateau it is zero. Partial alpha_j/partial d_l=N²[partial a_d(j/m)-partial a_d((j-1)/m)]. Differentiate the above full product exactly; J_N(theta)=[Omega | t*partial_d Omega] is a 6x6 Jacobian. The map is differentiable on parameter chambers where NO time-mesh point hits a ramp endpoint. Do not apply this unqualified at kink coincidences.

## R37.1 four strict local inverse certs

At source true values t=1.07, all d_j=1/24, the time mesh avoids breakpoints at N24,32,48,64. Independent Python stdlib Fraction represents all schedule knots and derivatives EXACTLY; mpmath.iv at 84 decimal digits encloses sin² functions; an independently differentiated recurrence constructs the full Jacobian, and an explicit 720-term Leibniz determinant (NOT numpy.linalg) encloses:
N24 det about -1.9817116343447e-14;
N32 about -1.6551761948728e-15;
N48 about -3.0086110540453e-16;
N64 about -1.1408739085938e-15.
Every complete interval has a STRICT negative upper endpoint and excludes zero. By classical inverse function theorem, exact source-finite 6-TT data locally determine six unknown parameters in an open neighborhood for THESE four finite cases. This is software-directed interval certification CONDITIONAL on the experimental mpmath.iv backend, not Lean/Coq proof and NOT global injectivity or an all-N theorem.

## R37.2 finite-model repair of ROT036 bias

For source EXACT noiseless data y=1.07 Omega(N,d_true) with all d_true=1/24, solve the SOURCE-FINITE nonlinear equations using safeguarded Newton started deliberately away from truth: t_start=1.0701, d_start=d_true+(.00003,-.00002,.00001,-.00002,.00003). In 12 tested even N=24..1024 this procedure recovers all six parameters with L2 error <5e-11. It was NOT initialized at the true solution.

N | prior continuum inverse dwell L2 BIAS | source-finite local 6-parameter L2 ERROR
128 | .5042699246 | 4.187364e-11
256 | .1224648772 | 2.166066e-11
512 | .0303951609 | 4.987768e-11
1024 | .0075850470 | 2.783986e-11

A larger starting perturbation (~1e-3 in plateaux) failed some development-stage Newton checks, excluded from reported PASS. Therefore no guarantee of global Newton convergence, global injectivity or a broad basin.

## R37.3 numerical local noise sensitivity remains

For numerical Jacobians N32..1024, smallest singular remains positive but condition numbers are O(10^5), e.g. N1024 sigma_min=1.26283513675e-6, kappa2=490841.6999. Linearized amplification 1/sigma_min~791869 can magnify small readout errors. The local source-correct inverse avoids deterministic model mismatch but does not itself solve noisy identification. No measured noise or statistical confidence guarantee.

## Reproduction/provenance

FIVE original independent scripts executed and reexecuted:
(1) rot037_exact_discrete_inverse.py: 91 NumPy Fourier source-product/analytic derivative/central finite-difference tests through N1024 PASS;
(2) rot037_interval_discrete_jacobian.py: 8 strict interval determinant sign tests for N24/32/48/64 PASS, using stdlib Fraction exact knots;
(3) rot037_perturbed_inverse.py: 60 safeguarded displaced-start exact finite nonlinear Newton tests on 12 grids PASS;
(4) rot037_independent_source_native.py: 21 literal unchanged source full real N³ apply_E, three-term Lie and apply_P_TT checks for nonconstant sampled schedule, N12/16, max source Fourier gap 1.20915552913e-16 PASS;
(5) rot037_rational_schedule_audit.py: 10224 separate stdlib Fraction checks of legal sampled dose, mass and exact piecewise derivatives, across 12 profile+grid combinations PASS (not exact trigonometric checks).
TOTAL 10404/10404 actually typed tests PASS, not external peer review.

ONE Moderator-local self-contained user-conversation ZIP has full expanded Polish proof, 5 runnable programs, 5 original JSON, 5 stdout, README, unchanged helper, manifest; ZIP SHA256 2f64c10efaa1e52270643d1b1566922d719208c44c5fed418cb966311ea95909. Clean independent extraction ZIP CRC PASS, SHA256 18/18 PASS, all FIVE scripts reexecuted and five JSON BYTE IDENTICAL PASS. Source ZIP/code LOCAL, NOT falsely claimed separately GitHub-hosted.

No historic original DTC production, no masked h=fI KA or physical J3/K/GR/GW/PBH, no full-N or global nonlinear inverse, independent referee, BW ingestion, CANON or EXEC. NO_NEW_TASK / NO_NOVELTY / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
