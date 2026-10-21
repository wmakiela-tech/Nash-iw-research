---
artifact_id: IW_PRF11_R15_FIXED_STATIONARY_DIFFERENCED_NOISE_RECOVERS_INFORMATION_FROM_VANISHING_WEAK_SIGNAL_001_20261021
title: "PRF11 R15 — fixed stationary MA(1) noise can enable consistent inference despite vanishing weak-record energy"
created_at: 2026-10-21
as_of: 2026-10-21
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_10 / PRF11
function: FOUNDATION_FIRST / OTHERS_FIRST / MATHEMATICAL_NONMAP / EXACT_PRIOR_ART_SUBTRACTION
document_type: REPORT
task_id: IW_PRF11_R15_FIXED_STATIONARY_NOISE_SPECTRAL_ZERO_NONMAP_001_20261021
exposure: PUBLIC
status: DRAFT / INDEPENDENT_REFEREE_PENDING
primary_location: GitHub/research/prf11/2026-10-21/IW_PRF11_R15_FIXED_STATIONARY_DIFFERENCED_NOISE_RECOVERS_INFORMATION_FROM_VANISHING_WEAK_SIGNAL_001_20261021.md
content_identity: VERIFY_GIT_BLOB_SHA_AND_FULL_READBACK
derived_from:
  - IW_PRF11_R14_CORRELATED_NOISE_COVARIANCE_SEAM_WEAK_STORAGE_STATISTICAL_COUNTEREXAMPLE_001_20261021
  - GEEKY-S10-PRF11-COMMON-STORAGE-ADAPTIVE-GAUSSIAN-LECAM-COLLAPSE-001
supersedes: []
stale_if: project source corrections or physical noise/instrument/timing contract changes
acceptance_owner: source owners Geeky-S10/INT8/LT5; suitable referee; Moderator holds EXEC
return_path: this GitHub file; exact science dispatch if delivered
claim_ceiling: EXACT_STANDARD_STATIONARY_GAUSSIAN_NONMAP / PRIOR_ART_ABSORBED / NO_CANON / NO_EXEC / NO_NOVELTY / NO_PHYSICAL_UPGRADE
cross_surface_sync: GITHUB_PENDING_BW_INGEST
---

# PRF11 R15 — Fixed stationary noise, weak resets and the low-frequency information loophole

## 0. Achievements by OTHERS and latest currentness, before PRF work

Read full current project GitHub texts and bounded #iw-dispatch. No owner answer on the R14 parent Slack thread was verified at this rotation. Lack of thread reply is not scientific rejection.

**Geeky-S10 (new after R14):** PRF11 R13's adaptive Gaussian Le Cam/van Trees-style minimax collapse is valid beyond a fixed sensor and a quadratic P. The deterministic donor assumption is a *finite common extremal storage* V_* for the entire heterogeneous action family; if every action has strength at most epsilon, one obtains the pathwise squared sensitivity budget Σ c_j² <= epsilon V_*(v). With *independent fixed-variance Gaussian innovations*, sequential KL, Fisher and Le Cam collapse follow uniformly even for noisy-history adaptive policies. This is Geeky's exact generalization, not a PRF11 theorem:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s10/2026-10-21/geeky_s10_prf11_common_storage_adaptive_gaussian_lecam_collapse_001.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s10/2026-10-21/geeky_s10_heterogeneous_action_family_weak_storage_ceiling_001.md

**INT8 (new after R14):** within a *fixed physical time horizon* T, co-aligned varying-direction weak reset readouts satisfy Σ b_j² <= [epsilon/(2-epsilon)] exp(2 max(mu_2(G),0) T) ||x0||² uniformly over arbitrary finite sample counts. It needs neither global V_* nor free Hurwitz stability. It is a deterministic statement; Gaussian inference remains a distinct conditional port.
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/int8/2026-10-21/iw_int8_finite_horizon_weak_readout_sharp_ceiling_without_global_storage_001.md

**MT13/M13, LT5 and REC10:** recent work separates weak readout size, exact noiseless observability, vector target Chebyshev geometry and source-valid actuation. In particular REC10 tightened LT5's finite witness-support bound d+2 to the sharp d+1 by Danskin/KKT/Carathéodory. These objects do not alter the present statistical noise question.
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/2026-10-21/lt5_vector_target_constrained_chebyshev_dual_and_nonseparable_actuation_001.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/rec10/2026-10-21/rec10_rot05_lt5_vector_chebyshev_dplus1_001.md

**PRF11 R14** already supplied a 2-shot correlated-Gaussian counterexample with fixed marginal variances, but its correlation coefficient rho_s=-1+s² was *tuned to the measurement strength*. That is mathematically valid but makes the source-noise seam less discriminating:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-21/IW_PRF11_R14_CORRELATED_NOISE_COVARIANCE_SEAM_WEAK_STORAGE_STATISTICAL_COUNTEREXAMPLE_001_20261021.md

R15 strengthens this exact NONMAP without introducing any s-dependent noise covariance rule.

## 1. New precise question and mature theory families

After currentness and prior-art subtraction, the proper question is:

**Can one fixed, stationary, short-range correlated Gaussian observation-noise process yield asymptotically perfect estimation from a single preparation whose entire UNWHITENED weak-readout energy tends to zero, when sample count grows?**

Yes, in a classical model with a spectral zero at frequency 0.

MATURE HOSTS:
- stationary Gaussian MA(1) with a moving-average unit root: differenced white noise eta_j=xi_j-xi_(j-1);
- spectral density f(omega)=sigma² |1-exp(-i omega)|² = 4 sigma² sin²(omega/2);
- Toeplitz/discrete Dirichlet Laplacian covariance, with lambda_min(T_N)~pi²/(N+1)²;
- generalized least squares and Gaussian shift information c^T Sigma^(-1)c;
- smooth taper/low-frequency projection and classical time-series signal processing;
- Le Cam comparison and minimax testing.

No claim that the mathematical phenomenon or these theorem families are new. The project-local value is an exact typed witness that separates the new **INT8/Geeky deterministic weak-record bound** from statistical inference under **fixed** non-independent noise.

## 2. Declared, one-preparation, all-finite classical reset carrier

Take n=1, G=0, e=d=1, hidden initial state x0=theta with theta in [-R,R], R>0. For each integer N>=2 set s_N=1/N. Use precisely N observations of the SAME state, with co-aligned deterministic resets and no noise-driven state update. The sample times can be chosen at nondecreasing times in a common finite [0,T]; since G=0 only the order matters.

At shot j=1,...,N:

  x_j^-=theta(1-s_N)^(j-1),
  b_j=s_N*x_j^-=theta*c_(j,N),
  c_(j,N)=s_N (1-s_N)^(j-1),
  x_j^+=(1-s_N)x_j^-.

For every finite N this is legal in the same classical weak-reset model as the Geeky and INT8 theorems. Its all-strength common V_*(theta)=theta² is FINITE; hence their stronger general results apply.

Exact deterministic record energy:

  ||c_N||²
   = s_N² sum_{j=0}^{N-1} (1-s_N)^(2j)
   = [s_N/(2-s_N)] [1-(1-s_N)^(2N)]
   <= s_N/(2-s_N)
   = O(1/N) -> 0.                                      (2.1)

This is **others' deterministic theorem**, specialized here to an exact scalar instance.

## 3. ONE fixed stationary Gaussian observation-noise process

On one probability space take iid xi_j~N(0,sigma²) for all integer j, sigma²>0 FIXED. Define the stationary Gaussian sequence:

  eta_j=xi_j-xi_(j-1),   j>=1.                         (3.1)

Use observations

  Z_j=theta*c_(j,N)+eta_j,   j=1,...,N.               (3.2)

No dependence on s_N or N enters (3.1); every finite observation record is a prefix of ONE fixed stationary Gaussian MA(1) noise law indexed by measurement number.

The covariance of the first N noise values is

  Sigma_N = sigma² L_N,
  L_N = tridiag(-1,2,-1).                              (3.3)

Thus:
- each marginal variance Var(eta_j)=2sigma², independent of j,N,s;
- adjacent covariance Cov(eta_j,eta_(j+1))=-sigma², lag ≥2 covariance =0;
- every finite Sigma_N is strictly positive definite;
- the covariance operator norm is uniformly bounded by 4sigma²;
- BUT the smallest eigenvalue decreases as N^-2, not uniformly bounded below:

  eigenvalues(L_N)=2-2cos(k pi/(N+1)), k=1,...,N;
  lambda_min(Sigma_N)
   =sigma²[2-2cos(pi/(N+1))]
   ~sigma²*pi²/(N+1)².                                (3.4)

The stationary spectral density (normalization convention omits 1/(2pi)) is

  f(omega)=sigma²|1-exp(-i omega)|²
          =4sigma² sin²(omega/2), f(0)=0.             (3.5)

No nontrivial *finite* observation record has a singular covariance; the zero occurs in the infinite-process spectral density and is approached as N grows.

The result goes beyond R14's tuned 2x2 covariance: here **all lag covariances and the entire noise-generating law are independent of strength and N**.

## 4. An explicit estimator with vanishing squared error

Let

  alpha_N=pi/(N+1),
  w_(j,N)=sin(j alpha_N), j=1,...,N,
  w_(0,N)=w_(N+1,N)=0.                                 (4.1)

Define the positive signal response

  A_N=sum_{j=1}^N w_(j,N) c_(j,N)
      =(1/N) sum_{j=1}^N
          (1-1/N)^(j-1) sin(pi*j/(N+1)).               (4.2)

Riemann convergence yields:

  A_N -> a = integral_0^1 exp(-t)sin(pi*t)dt
              = pi(1+exp(-1))/(1+pi²)
              ≈0.3953520151064591 >0.                 (4.3)

The estimator is

  theta_hat_N = [sum_j w_(j,N) Z_j] / A_N.             (4.4)

It is unbiased for EVERY theta because the mean of numerator is theta*A_N.

Its NOISE part telescopes exactly:

  sum_{j=1}^N w_j eta_j
    = -w_1 xi_0 + sum_{j=1}^{N-1}(w_j-w_(j+1))xi_j
      +w_N xi_N.                                       (4.5)

Therefore

  Var(sum_j w_j eta_j)
    =sigma²[ w_1²+sum_(j=1)^(N-1)(w_j-w_(j+1))²+w_N² ]
    =sigma²*w^T L_N w.                                (4.6)

The sine vector w is the first normalized-in-shape eigenvector of L_N, with

  L_N w =lambda_1 w,
  lambda_1=2-2cos(alpha_N),
  ||w||²=(N+1)/2.

Hence EXACTLY:

  Var(sum_j w_j eta_j)
    =sigma² (N+1) [1-cos(alpha_N)],                    (4.7)

  Var(theta_hat_N)
    =sigma² (N+1)[1-cos(pi/(N+1))]/A_N²
    ~ [sigma²*pi²/(2*a²)] * 1/N                        (4.8)
    ≈31.5719812529022 * sigma²/N.

The variance is constant across theta, so both worst-case and pointwise MSE equal (4.8). Thus

  inf_all_estimators sup_|theta|<=R MSE
    <=Var(theta_hat_N) ->0.                            (4.9)

One original hidden preparation is enough for **statistically consistent** estimation in this *declared* fixed-MA(1)-noise model, despite vanishing unwhitened signal energy.

No claim is made that this estimator is exactly finite-N minimax, or that the source can physically supply that many samples without resource cost.

## 5. Whole experiment does not collapse to a no-information experiment

For each N the likelihood family is a Gaussian shift:

  P_theta^N = N(theta*c_N, Sigma_N).

Its Fisher information is

  I_N = c_N^T Sigma_N^(-1) c_N.                        (5.1)

By Cauchy–Schwarz in the covariance metric, for any fixed weight w,

  I_N >= (w^T c_N)²/(w^T Sigma_N w)
       = A_N²/
         [sigma² (N+1)(1-cos(pi/(N+1)))]
       ~ [2a²/(sigma²*pi²)]N ->infinity.              (5.2)

Since theta_hat_N is Gaussian with variance tending to zero, any two fixed distinct theta values are asymptotically distinguishable with vanishing testing error. In particular for the binary subexperiment theta in {-R,+R}, testing the sign of theta_hat_N gives error

  Phi(-R/sqrt(Var(theta_hat_N))) ->0.

Therefore TV(P_+R^N,P_-R^N)->1. Let F_N be ANY theta-independent comparison experiment (one constant law for both parameters). It carries no binary distinction. Exact binary deficiency satisfies

  delta(F_N,E_N)=0.5*TV(P_+R^N,P_-R^N)->1/2,          (5.3)

using triangle inequality for the lower bound and the midpoint output law for attainment. In contrast delta(E_N,F_N)=0 by discarding observations. Thus Le Cam distance to a no-information experiment does NOT go to zero. This is the precise opposite of PRF11 R13 and Geeky's independent-noise conditional theorem, with NO logical contradiction because the noise contracts differ.

## 6. Independent-noise floor restores collapse (one-variable kill test)

Add to each readout an **independent** Gaussian component zeta_j~N(0,tau²), tau>0 FIXED, independent of xi and all else. The noise covariance is

  Sigma'_N=sigma²L_N+tau² I_N >=tau²I_N.              (6.1)

Then standard Gaussian information gives

  I'_N=c_N^T(Sigma'_N)^(-1)c_N
      <=||c_N||²/tau²
      <=s_N/[tau²(2-s_N)] ->0.                         (6.2)

Hence uniform fixed-parameter KL and TV collapse to the no-information experiment; for bounded theta the minimax advantage vanishes by elementary binary prior argument, as in PRF11 R14.

This ONE exact noise-control change makes the statistical conclusion reverse. The critical object is a uniform bound on precision in the signal direction, not stationarity, short-range dependence, positive definiteness at each finite N, or fixed marginal variance.

## 7. Numerical reproduction — independently checked

For sigma²=1 and s_N=1/N, direct tridiagonal-solver controls and exact sine-estimator formula gave:

  N      A_N         ||c_N||²     Var(theta_hat_N)    Full Fisher I_N
  10     0.44642552  0.04623281  2.23575917          0.464349
  30     0.41260864  0.01473222  0.93424268          1.108798
  100    0.40055910  0.00435186  0.30449499          3.398189
  300    0.39709077  0.00144427  0.10397279          9.948392
  1000   0.39587397  0.00043262  0.03145730          32.877218

The calculated I_N values use the full covariance solve L_N u=c_N, then I_N=c_N^T u/sigma²; exact variance formula uses (4.7)-(4.8). Tables are diagnostic checks, not the proof.

Regeneration snippet (Python/NumPy/SciPy, NOT needed for exact derivation):

    import numpy as np
    from scipy.linalg import solve_banded
    for N in [10,30,100,300,1000]:
        s=1/N; j=np.arange(1,N+1)
        c=s*(1-s)**(j-1)
        w=np.sin(np.pi*j/(N+1))
        A=w@c
        noise_var=(N+1)*(1-np.cos(np.pi/(N+1)))
        est_var=noise_var/A**2   # sigma²=1
        ab=np.zeros((3,N))
        ab[0,1:]=-1; ab[1,:]=2; ab[2,:-1]=-1
        precision_c=solve_banded((1,1),ab,c)
        fisher=c@precision_c
        print(N,A,c@c,est_var,fisher)

The snippet uses no user files, private project data or physical parameters; only a self-contained exact Gaussian counterexample.

## 8. Mature prior art and source-reproducibility log

Literature examined on 21 Oct 2026, targeted, non-exhaustive. Search families included:
- "differenced white noise MA(1) spectral density zero frequency tridiagonal covariance eigenvalues discrete Laplacian time series"
- "Gaussian observation correlated errors Fisher information inverse covariance generalized least squares stationary time series spectral density zeros"
- "Brockwell Davis Introduction to Time Series and Forecasting MA(1) noninvertible theta -1 first difference white noise spectral density"
- "Grenander Szego Toeplitz forms applications spectral density zeros minimum eigenvalue"
- "differenced white noise MA(1) covariance lag 0 2 lag 1 -1 spectrum 4 sin squared half"
- "covariance matrix second difference Toeplitz tridiagonal eigenvalues 2-2cos k pi/(n+1)"
- "estimation mean MA(1) theta -1 differenced white noise Gaussian likelihood superconsistency mean estimator spectral density zero zero frequency"
- "tridiagonal Toeplitz covariance difference white noise GLS estimate constant mean variance n cubed"

HIGH-CONFIDENCE HOST SOURCES:
1. Grenander & Szegő, *Toeplitz Forms and Their Applications*, University of California Press (1958), DOI 10.1525/9780520355408 (publisher contents, relevant chapters on eigenvalues and applications to probability/statistics inspected; **not full book proof-by-proof**). https://www.degruyterbrill.com/document/doi/10.1525/9780520355408/html
2. Published university/academic time-series lecture notes on differencing and MA(1): spectral multiplier |1-exp(-i omega)|² and zero at DC; exact content consulted in public course notes, no monograph exhaustiveness. https://www.barigozzi.eu/MB_time_series_lecture_notes.pdf
3. University lecture notes (NTNU) on tridiagonal Toeplitz eigenvalues lambda_k=2-2cos(k pi/(N+1)), direct derivation of discrete-Laplacian sine eigenvectors. https://www.math.ntnu.no/emner/TMA4205/2015h/notes/tridiag.pdf
4. "New exact ML estimation and inference for a Gaussian MA(1) process", *Economics Letters* 99(1), 172–176 (2008), DOI 10.1016/j.econlet.2007.06.021; publisher excerpt documents Gaussian MA(1) lag covariance and finite Toeplitz likelihood. The paper principally estimates the MA parameter, NOT the exact hidden preparation target in this note. https://doi.org/10.1016/j.econlet.2007.06.021
5. Attia & Constantinescu, *Optimal Experimental Design for Inverse Problems in the Presence of Observation Correlations*, *SIAM J. Scientific Computing* 44 (2022), DOI 10.1137/21M1418666; full author/preprint HTML inspected in PRF11 R14, Gaussian covariance-weighted inverse problem host. https://doi.org/10.1137/21M1418666

The objects used in this mathematical witness belong to the mature MA/Toeplitz/GLS/time-series families; a priority claim cannot be inferred from not locating an identical NASH-reset + tapered-MA toy example. The public scholarly searches were *targeted*, not systematic, and no external theorem author is claimed to have written this exact source-native example.

## 9. Physics, causality and scientific STOP

This statistical experiment is deliberately CLASSICAL. All state resets are deterministic and independent of the realized readout noise. The fixed stationary noise is indexed by shot number; when N grows in a bounded physical horizon, assuming this exact index-stationary covariance across arbitrary sampling rates would itself require hardware/source justification (bandwidth, sampling/filter electronics, energy, spectral cutoffs, time-cost and environmental correlations). **One physical sensor realizing all N at no additional cost is NOT established.**

Consequently:
- no quantum CP instrument;
- no noise–disturbance quantum tradeoff;
- no fixed-covariance continuous-time realization;
- no NCDG/DTC, PBH, Front B or gravitational physics transfer;
- no source-matched likelihood from any actual apparatus;
- no statement that a hardware device can exploit a stationary spectral zero at arbitrary sampling rates.

What R15 does establish is an EXACT source-typed NEGATIVE KNOWLEDGE firewall:

  FINITE COMMON AVAILABLE STORAGE
  + ARBITRARILY WEAK RESET RECORDS
  + FIXED NONZERO NOISE VARIANCE PER SHOT
  + STATIONARY SHORT-RANGE CORRELATED NOISE
      !=
  STATISTICAL INFORMATION COLLAPSE.

A sufficient repair is UNIFORM NOISE PRECISION CONTROL in the actual signal subspace, e.g. a strictly positive all-dimension covariance floor. The appropriate physical follow-up, if a source owner ever admits a real instrument, is to measure/model the full joint/causal noise spectrum and its resource scaling, not to add another abstract generic information-preservation gate.

This is a standard-mathematics exact counterexample inserted into the IW type lattice; theorems of Geeky-S10/INT8 and the iid-Gaussian extensions remain correct.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE / GITHUB_PENDING_BW_INGEST.
