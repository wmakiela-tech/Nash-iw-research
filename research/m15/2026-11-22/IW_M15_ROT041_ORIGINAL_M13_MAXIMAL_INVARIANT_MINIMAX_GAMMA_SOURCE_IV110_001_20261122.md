---
artifact_id: IW_M15_ROT041_ORIGINAL_M13_MAXIMAL_INVARIANT_MINIMAX_GAMMA_SOURCE_IV110_001_20261122
return_id: IW_M15_ROT041_SIX_SOURCE_FOURIER_CALIBRATION_GROUP_MAXIMAL_INVARIANT_AND_SHARP_INVARIANT_RISK_001_20261122
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-22
exposure: PUBLIC
result_class: NEW_ORIGINAL_M13_SOURCE_SPECIFIC_GROUP_INVARIANT_MINIMAX_TEST_CHARACTERIZATION_PLUS_IV110_SAFE_FINITE_N
source_class: EXACT_ORIGINAL_M13_NATIVE_EXECUTED / DIFFERENT_ALGORITHM_FULL_41CUBED_SPATIAL_SVD_AND_EXACT_GAMMA_CF_NUMERIC
review_level: INTERNAL_NONBLIND / REC13_AUD3_INDEPENDENT_REVIEW_PENDING
sync_state: GITHUB_PENDING_BW_INGEST
ceiling: NO_GENERAL_NOVELTY / NO_PHYSICAL_SENSOR / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE
---

# M15 ROT041 — Six-mode maximal invariant, least-favorable log-Gamma location testing, and improved strict Gaussian sample gates

## 1. Claim and scientific attribution

**NEW SOURCE-BOUNDED RESULT.** In the EXACT six fixed source energy-mean-free M13 Fourier cosine/sine channels studied in M15 ROT036–040, FIVE independently unknown, unbounded site-noise calibration coefficients act as a five-dimensional positive scaling GROUP on the SIX observed mode energy sums. The unique one-dimensional null contrast already constructed for Gaussian Peano C5 calibration in M15 is a **MAXIMAL INVARIANT** of that group, not merely a convenient heuristic. Conditioning on mode pair energies loses no candidate information carried by their independent isotropic Gaussian phase/direction vectors. The remaining SIX-channel *group-invariant* composite testing problem is an EXACT one-dimensional **location-interval experiment** of one common, strictly log-concave log-Gamma noise distribution. This determines the exact minimax **MAX CONDITIONAL ERROR AMONG CALIBRATION-GROUP-INVARIANT TESTS** by a unique equal-tail threshold between least-favorable nuisance endpoints. It does not establish minimax among every conceivable non-invariant test, full 68,921-site observer or physical measurement design.

The sharp C5 deterministic log-variance gap remains the ORIGINAL M15 ROT040 theorem; there is NO new general mathematical novelty or owner-firstness seizure. Original M13 FIRST public 41-mode Fourier B N41 auxiliary source; Geeky-S12 ROT035 FIRST the exact source-legal rational synthetic Gaussian A/B spatial covariance witnesses; Geeky-S13 ROT001 FIRST unbounded C-infinity axial-only full-field alias; M15 ROT036 first six-mode cubic+FACE nuisance and Peano kernel, ROT037 bounded C5 restoration, ROT038 exact weighted log-Gamma concentration, ROT039 strict cubic Peano lower bound, ROT040 sharp GLOBAL C5 log-variance contrast infimum. AUD3 ROT009 and REC13 ROT014 earlier cross-cell improved Lipschitz/concentration science retained; ROT041 does NOT relabel their results.

Original M13 source COMPLETE 8,970 bytes SHA256 `cd4aad089bf68e2e6155ff048d4d812943495dcf1770c8acbf0ff8111b1deb9c`, original Git blob SHA1 `c6377cfbc9a0070abc34ffedc5871e719f6a4679`, both checked BEFORE actual native import and execution of `tensor_polys(41)[1]`, `calc(41,alpha=1/20)[1]` and `inner(B,B,41,k0)` in TWO different programs. Original native B tensor Fourier modes: 41, original B energy Fourier difference support: 221. Source original immutable:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py

The historic FULL original `dtc0a_runtime_v0_3_1.py` producer was NOT recovered. All Gaussian site noise and added Fourier measurements are SYNTHETIC, unrecorded mathematical models.

Full ORIGINAL ROT040 sharp source IV110 parent is SHA-frozen in this reproducer as `m15_rot040_native_sharp_C5_ramp_IV110.json` SHA256 `0d495d0d0d1c5e74eff7743717659540d849f02b9314f3512a62c6cbca7bbb9e`; original source-legal exact rational Gaussian candidate parent `m15_rot029_exact_rational_source_proof.json` SHA256 `00b8c93da96c9c92901555fd4c2db0af63978ecf735df3945e9ff42d218dee90`. Parents are identified and read, NOT falsely called freshly re-proved.

## 2. Exact observer and unrestricted calibration group

Original N41³=68,921-site periodic torus. New six Fourier k wavevectors are
`(20,20,20)`, `(20,20,0)`, `(20,0,0)`, `(7,0,0)`, `(12,12,13)`, `(3,13,7)`.
Each k and −k modulo 41 is ABSENT in original 221 B-energy Fourier source differences. Therefore all TWELVE normalized real cosine/sine energy projection source means are EXACT ZERO for every alpha (not a Gaussian modeling assumption). They are NOT the original coarse-region masks or observed experimental channels.

Two first-owner Geeky EXACT RATIONAL source Gaussian stationary site covariances are:
- A: beta0=1, theta_ax=3/25, theta_face=1/10, theta_body=2/25.
- B: beta0=99779719687217/10^14; theta_ax=316869474178226/2494492992180425, theta_face=93110637627687/997797196872170, theta_body=205860943554709/2494492992180425.

For k let cx,cy,cz=cos(2pi*k_j/41), a=(cx+cy+cz)/3, f=(cxcy+cxcz+cycz)/3. Candidate X variance v_X(k) is original rational stationary spectral polynomial times a positive model calibration exp(p_X(a)+tau_X*f+phi_X(a)). The first nuisance block is UNRESTRICTED real cubic p_X and UNRESTRICTED FACE slope tau_X, five unknown coefficients per candidate X; these coefficients may differ freely across A/B. The residual unknown phi_X is an arbitrary real C5 function over the SIX axial node interval with uniform per-candidate bounds |phi_X^(4)|<=16.5 and |phi_X^(5)|<=50. This is the EXACT same hypothetical calibration class as ROT040, not tightened.

Suppose n independent entire Gaussian RAW site spatial snapshots or n independently repeated direct Fourier pair readouts are measured. At frequency i we receive 2n real centered Gaussian components with common variance lambda_i. Define S_i=sum of their squared magnitudes across n snapshots. Then independently across six i:

  S_i/(2*lambda_i) ~ Gamma(n,1).

Equivalently, after dividing S_i by the baseline model-A v_A(k_i) and 2n, take six log energies ell_i. Put the 5-by-6 real nuisance matrix H with rows (1, a_i, a_i², a_i³, f_i). Under arbitrary p and tau its action is

  ell -> ell + H^T theta, theta in REAL^5.

The original source IV110 strictly verifies the 5x5 original H first-minor determinant excludes zero, so rank(H)=5. The one-dimensional null vector w (with w_6=1) satisfies H w=0. Its weighted sum

  T = w^T ell

is invariant under ALL unrestricted nuisance shifts. **MAXIMALITY PROOF:** If T(ell)=T(ell'), then w^T(ell−ell')=0, i.e. ell−ell' belongs to w^perp. Since rank H=5, w^perp=im H^T. Therefore ell'−ell=H^T theta for a unique group theta. The converse is immediate. This is exact linear algebra for ALL positive energy sextuples, not numeric rank heuristics.

Conditional on S_i, the independent Gaussian real direction vectors in R^(2n) are uniformly distributed on their unit spheres for both candidate hypotheses, independent of lambda_i. Hence phase/directional information is ancillary under this specified observer. Every test invariant under nuisance reparameterization can be represented by a possibly randomized function of T alone. This does NOT say other raw Fourier frequencies or physical sensor types cannot add information.

## 3. Sharp calibration shift intervals and log-Gamma distribution

Write Delta=w^T log(v_B/v_A), recomputed from ORIGINAL native public M13 geometry using strict IV110. New source IV110 gives

  Delta≈0.0035493505760477928107931245105931118298204257120.

The ORIGINAL ROT040 source sharp C5 theorem gives the exact log-score difference-nuisance supremum

  Sstar≈0.0027916055643630171574,
  Gsharp=Delta−Sstar in [0.00075774501168477565096020000637363556489237632383875,
                         0.00075774501168477565580745002956433489354556379071167].

Because the residual C5 class is centrally symmetric, convex, and includes scalar contractions, each model's calibrated shift xi_X=w^T phi_X is exactly the OPEN interval (−Sstar/2,+Sstar/2). Each endpoint is a SUPREMUM approached by explicitly source-legal smooth mollifications of ROT040's least-favorable clipped ramp, but is not attained by an admissible C5 function. The sharpness is DERIVED FROM THE AUTHOR'S ROT040 SOURCE CERTIFICATE; it is not a new numerical optimization result here.

Under A and B, respectively, the maximal invariant has EXACT distribution:

  T_A = xi_A + Z_n,
  T_B = Delta + xi_B + Z_n,
  Z_n = sum_{i=1}^6 w_i*log(X_i/n), X_i independent Gamma(n,1).

Its exact characteristic function, since sum_i w_i=0, is

  E[exp(it Z_n)] = product_{i=1}^6 Gamma(n+it*w_i)/Gamma(n).

Moreover, if X~Gamma(n,1), Y=log X has density f(y)=exp(n*y−exp(y))/Gamma(n); second derivative of log f is −exp(y)<0. Signed nonzero linear scalings and convolution preserve log concavity. Therefore Z_n has a positive, strictly log-concave density and its location shifts have MONOTONE LIKELIHOOD RATIO. This is standard probability/statistics, not a new general theorem.

The C5 class produces two location intervals:

  H_A: mu_A in (−s,+s),
  H_B: mu_B in (Delta−s,Delta+s),
  s=Sstar/2.

Their closest endpoints are mu_A=s and mu_B=Delta−s=s+Gsharp. Since they lie in the CLOSURE rather than the actual smooth C5 family, each is a least-favorable LIMIT, not a data-generating smooth attained endpoint. This distinction is essential for using the word sharp.

## 4. Exact minimax MAX CONDITIONAL ERROR in invariant tests

Let F_n be the CDF of the common Z_n, with positive strictly log-concave density f_n. The least-favorable simple pair of shifted laws Z_n+s and Z_n+s+Gsharp has the monotone likelihood ratio property. A one-sided threshold is Neyman–Pearson-optimal for each fixed type-I size. For the max of the two conditional errors, the optimal threshold equalizes the errors. Let u_n be the unique real solution

  1−F_n(u_n) = F_n(u_n−Gsharp).

Then the invariant test

  decide B if T > s+u_n, otherwise A,

has worst-case conditional error

  R_n^inv = 1−F_n(u_n) = F_n(u_n−Gsharp).

**Proof of minimax restriction:** For any calibration-invariant test, the supremum of its errors across the two original smooth nuisance classes is at least the minimax error of the two least-favorable LIMIT laws. The limit follows by continuity in total variation of the translated density. The monotone likelihood ratio/Neyman–Pearson frontier yields a threshold and equalized conditional errors for this endpoint simple pair. The same threshold's type-I error increases with mu_A and type-II error decreases with mu_B, so the worst admissible errors approach exactly those endpoint errors. It therefore achieves the lower bound and is minimax for MAX CONDITIONAL ERROR within the specified INVARIANT class. It is NOT a claim of optimality of the fixed six modes or of ALL non-invariant tests.

This exact source-specific characterization reduces the optimal invariant finite-n risk to ONE ordinary scalar CDF of a known log-Gamma convolution. It is stronger than merely applying a concentration inequality to an arbitrary contrast.

## 5. New STRICT finite-n Chernoff source IV110, and independent numerical optimal-risk evaluation

A second smaller but RIGOROUS improvement follows by retaining more of the exact ROT038 log-Gamma denominator. Main program recomputes the original source H,w,Delta,V and checks the original ROT040 sharp gap and SHA identities. Define deliberately rounded safe constants

  g0=0.00075774 < Gsharp,
  Vup=2.815 > V=sum_i w_i^2≈2.8147662920,
  Wup=1.001 > max_i |w_i|=1.

The exact weighted log-Gamma MGF satisfies, for |t|*Wup<n−1/2,

  Psi(t)=sum_i[log Gamma(n+t*w_i)−log Gamma(n)],
  Psi'(0)=0,
  Psi''(t)=sum_i w_i²*trigamma(n+t*w_i)
        <= Vup/(n−|t|Wup−1/2).

The trigamma midpoint bound trigamma(x)<=1/(x−1/2) for x>1/2 is a mature analytic inequality. Choose m=g0/2 and Chernoff tilt t=n*m/Vup. For all n>=55,000,000, IV110 strictly verifies eta=m*Wup/Vup+1/(2n)<0.001; then BOTH tails satisfy

  P(error|X) <= exp[−n*g0²/(8*Vup)*(998/999)]

uniformly over every admissible independently fitted C5 calibration, for BOTH candidate noise models. The fixed midpoint cutoff Delta/2 from original ROT040 is valid because the per-model calibration ranges are centrally symmetric and have half-width s. Thus strict sufficient original mathematical 68,921-site IID RAW snapshot counts:

| Conditional accuracy strictly above | ROT040 original strict count | NEW ROT041 strict count |
| ---: | ---: | ---: |
| 75% | 65,000,000 | 55,000,000 |
| 90% | 105,000,000 | 95,000,000 |
| 95% | 135,000,000 | 120,000,000 |
| 99% | 210,000,000 | 185,000,000 |
| 99.9% | Not established by ROT040 table | 275,000,000 |

The main source outward IV110 checks every inequality. These are SUFFICIENT mathematical n, not MINIMUM or physical measured sample requirements.

A second genuinely independent numerical program runs the untouched original M13, constructs all nine complex B tensor fields by FULL N41³ spatial inverse FFT, computes source cosine/sine Fourier means, evaluates direct site noise covariances by all source 6 axial/12 face/8 body signed periodic site rolls, derives w from an INDEPENDENT 5x6 SVD and verifies a nontrivial five-parameter scaling orbit and its inverse. It then numerically inverts the **EXACT analytical gamma characteristic function** with independent MP46 complex log Gamma and one-dimensional Gil–Pelaez Fourier quadrature, directly solving the equal-tail minimax equation. This is an EXACT DISTRIBUTION subjected to NUMERICAL inversion, not an interval-certified finite sample risk.

NUMERIC ONLY (not strict CDF certificates):

| n complete hypothetical spatial IID snapshots | numerical worst conditional error for optimal invariant equal-tail test |
| ---: | ---: |
| 65,000,000 | ~0.03432936 |
| 100,000,000 | ~0.01196506 |
| 106,000,000 | ~0.01003571 |
| 110,000,000 | ~0.00893087 |
| 120,000,000 | ~0.00668444 |
| 185,000,000 | ~0.00106475 |

The same numerical routine checks normal approximation values that agree within 4e−11 absolute, but does NOT turn the normal approximation or finite quadrature into a rigorous guarantee. In particular **110 million is a diagnostic indication of >99% under the modeled invariant endpoint experiment, while 185 million is the new defensible source-IV110 sufficient guarantee.** The normal-asymptotic n for 99% is about 106.12 million, but is not a nonasymptotic minimum claim.

## 6. Actual source reproduction and adversarial controls

All FULL original M13, two frozen parent result JSONs, BOTH independent ROT041 programs and COMPLETE raw machine JSONs are included in one user-local runnable ZIP. The primary is an independently reexecuted original M13+mpmath.iv.dps110 source and calibration group check, NOT just a copy of ROT040 data; the entire sharp C5 functional extremizer is inherited from the locked original ROT040 parent, and remains distinctly attributed. The independent second program constructs the full site math and evaluates exact log-Gamma characteristic functions via an entirely DIFFERENT numerical path.

Both scientific programs ACTUALLY reexecuted under isolated Python -I in new temporary directories, and their complete result machine JSON outputs were BYTE IDENTICAL (2/2). TEN disposable mutations actually run with expected fail-closed behavior: original native M13 corruption against each code path, original ROT040 certificate corruption, original ROT029 rational source corruption, current new IV110 JSON corruption before independent checker, false negative sharp gap, false positive source lower bound, false 99%-success at n=1 million, false 99%-success at n=65 million from independent Gamma CF, false assertion that group scaling alters the maximal invariant. All TEN were correctly rejected with identified guards; no original input files changed. One INITIAL independent script failed due to a missing source-V output field in the author's new JSON; the author corrected this and reran both programs and the complete cold replay prior to the final PASS. This preliminary implementation bug is disclosed, not counted as a PASS.

Custody: immutable full input SHA, actual source execution, actual complete machine outputs, independent byte-identical replays, negative fixtures, README, deterministic ZIP builder, archive SHA manifest and archive full reread are recorded in the attached user-local ZIP. GitHub report/curated JSON and Slack dispatch are NOT a public executable code mirror or native BW ingest receipt.

## 7. Specific review questions and strict STOP

Please ask REC13/AUD3 to audit specifically: (i) group rank and maximality against all six positive mode energies; (ii) why mode-pair Gaussian directions are ancillary but other modes are NOT included; (iii) exact shift image of smooth C5 constraints and closure endpoints from ROT040; (iv) log-concavity -> monotone likelihood ratio and minimax MAX conditional error among **invariant** tests only; (v) whether the original log-Gamma MGF and stronger 998/999 factor with g0,Vup,Wup is interval-safe; (vi) numerical Gil–Pelaez inversion versus rigorous guarantee, preventing the 110 million diagnostic from being presented as certified; (vii) priority of original M13, Geeky, AUD3, REC13 and M15 earlier claims.

**HARD SOURCE STOP:** Public original M13 AUXILIARY source only, historical complete DTC0a runtime not recovered; the two Gaussian site error covariances and all calibration derivative limits are synthetic and not measured; no physical site-field recorder, six frequency-pair sensors, IID repeated source data or measured astrophysical/quantum outcomes. No general novelty, global minimum sample resource, minimax over all non-invariant decision rules or alternative physical sensors, no alpha global inverse, no NASH K/J3/TPE/GW/GR mechanism. User-local replay I1 is NOT independent outside blind I3 review. KN15 native BW ING receipt not verified. GitHub/Slack posted != owner accepted/canon/execution signed.

STATUS: `ROT041_ORIGINAL_M13_NATIVE_PASS / FIVE_NUISANCE_GROUP_MAXIMAL_INVARIANT_PASS / C5_SHARP_LOCATION_INTERVAL_PASS / LOGCONCAVE_INVARIANT_MINIMAX_THEOREM_PASS / NEW_IV110_55M_95M_120M_185M_275M_PASS / FULL_41CUBED_INDEPENDENT_GAMMA_CF_NUMERIC_PASS / COLD_JSON_2_OF_2_PASS / TEN_ACTUAL_NEGATIVES_PASS / BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE`.
