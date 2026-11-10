# XH-S5 ROT009 — thermodynamic Mpemba computing: source-motivated slow-mode calibration gate

artifact_id: IW_XH_S5_ROT009_MPEMBA_CALIBRATION_PRECISION_GATE_20261110
date: 2026-11-10
cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
return_id: XH-S5-ROT009-MPEMBA_INITIALIZATION_CALIBRATION_PRECISION_GATE_20261110
source_type: PUBLIC_PEER_REVIEWED_2026 / INDEPENDENT_EXACT_AND_NUMERIC_TOY
claim_ceiling: NO_MATH_NOVELTY / NO_AUTHOR_ERROR / NO_SOURCE_DATA_OR_DEVICE_REPLAY / NO_NASH_PHYSICAL_BRIDGE / NO_CANON / NO_EXEC_SIGN / NO_BW_INGEST_ASSUMED

## Source and non-conflation
M. Moroder, F. C. Binder, J. Goold, "Digitally optimized initializations for fast thermodynamic computing", npj Unconventional Computing 3, 57, published Nov 2 2026, DOI https://doi.org/10.1038/s44335-026-00103-2, full publisher HTML https://www.nature.com/articles/s44335-026-00103-2, preprint arxiv:2603.24183. Source proposes preparing the K slow covariance modes with their equilibrium variance digitally, then using an overdamped Langevin OU thermodynamic computer for matrix inversion and determinant. Their Lyapunov equation Eq13: dSigma/dt=-mu(A Sigma+Sigma A)+2mu kBT I; Eq16 Sigma0(K)=sum_{k<=K}(kBT/lambda_k)u_k u_k^T; Eq18 **absolute Frobenius norm** error E(t)=||Sigma(t)-Sigmaeq||_F; Eq19 first hitting time; Eq21 ideal asymptotic speedup S -> lambda_(K+1)/lambda_1. Source explicitly warns that hardware-coupling calibration error renders initialization suboptimal and that multi-stage determinant total time cannot inherit just the thermalization speedup. No author's experiment, original code, device noise, actual LC circuits or source's 500D Wishart ensemble has been replayed.

## Mature host / priority subtract
Lu and Raz, PNAS 114, 5083-5088 (2017), DOI 10.1073/pnas.1701264114 already analyzed slow-mode suppression Mpemba; Klich/Raz/Hirschberg/Vucelja PRX9 021060 (2019) classical spectral theory; Nature Communications DOI 10.1038/s41467-025-59011-x (2025) already demonstrates thermodynamic matrix-inverse sampling; 'Robustness of the quantum Mpemba effect against state-preparation errors', NJP (2026), DOI 10.1088/1367-2630/ae5840 already establishes analogous sensitivity IN DISTINCT quantum systems. Source authors already know calibration limitations. No novelty claimed; this is a quantified diagnostic gate in their source-motivated six-dimensional mathematical host only. Public NASH GitHub queries "Mpemba optimized", "thermodynamic computing", "initial covariance" gave no matches, NOT evidence of absence from private NASH work.

## Executed exact test (model not author data)
SPD A eigenvalues (0.1,1,2,4,8,16); d=6, mu=kBT=1, K=1. Sigmaeq=A^-1. Standard Sigma0=0; ideal Sigma0=u1 u1^T/lambda1. Imperfect initial Sigma0=(1+r)u1 u1^T/lambda1, relative slow-mode initial variance error r>=0, with all other modal initial variances zero. Covariance propagates exactly Sigma(t)=Sigmaeq+exp(-At)(Sigma0-Sigmaeq)exp(-At).
Exact norm-square:
E_standard(t)^2=sum_{i=1..6} lambda_i^-2 exp(-4lambda_i t);
E_ideal(t)^2=sum_{i=2..6} lambda_i^-2 exp(-4lambda_i t);
E_r(t)^2=(r/lambda1)^2 exp(-4lambda1 t)+sum_{i=2..6} lambda_i^-2 exp(-4lambda_i t).
The first-hitting times t(eps) computed by monotone Brent root finding.
Ideal r=0 -> speedup limit lambda2/lambda1=10 as eps -> 0.
For ANY FIXED r>0, slow tail reappears, and t_standard~ln(1/(lambda1 eps))/(2lambda1), t_r~ln(r/(lambda1 eps))/(2lambda1), so speedup limit as eps ->0 equals ONE. Limits r->0 and eps->0 do not commute. This standard spectral-relaxation consequence is not a new theorem and does not contradict author's ideal formula.

Actual synthetic times / speedups, absolute covariance Frobenius:
eps 1e-2: t_std 34.5387764; t_ideal 2.3025913 S_ideal 14.999959; t_r1% 11.5129255 S_1% 3.000000.
eps 1e-4: t_std 57.5646273; t_ideal 4.6051702 S_ideal 12.500000; t_r1% 34.5387764 S_1% 1.666667.
eps 1e-6: t_std 80.5904783; t_ideal 6.9077553 S_ideal 11.666667; t_r1% 57.5646273 S_1% 1.400000.
eps 1e-8: t_std 103.6163292; t_ideal 9.2103404 S_ideal 11.250000; t_r1% 80.5904783 S_1% 1.285714.
eps 1e-12: t_std 149.6680310; t_ideal 13.8155106 S_ideal 10.833333; t_r1% 126.6421801 S_1% 1.181818.
For 0.1% residual and eps 1e-4, S 2.5; eps1e-8, S1.5. S_ideal >10 at finite target is consistent with asymptotic limit10 because modal prefactors matter.

## Quantified calibration-precision gate
Choose allowed thermalization time budget t_budget=(1+beta)t_ideal(eps). Then EXACT maximum allowable residual:
|r| <= lambda1 exp(2 lambda1 t_budget)*sqrt(eps² - sum_{i>=2}lambda_i^-2 exp(-4 lambda_i t_budget))
when radicand >=0. This controls how accurately the mode must be prethermalized to meet an operational deadline in this toy model, not real-world device tolerance. For beta=.2 (max 20% extra thermalization time over ideal):
eps1e-2 -> max r .00159415862248
eps1e-4 -> max r 2.98178162038e-5
eps1e-6 -> max r 5.23761770405e-7
eps1e-8 -> max r 9.11723073988e-9
eps1e-12 -> max r 2.75420687746e-12
eps1e-16 -> max r 8.31763605537e-16
The asymptotic exponent is 1-(1+beta)lambda1/lambda2=.88; independent finite-difference log-log slope between eps1e-12 and 1e-16 = .8799991612171945.

## Three independent executable checks
1. scipy.optimize.brentq of exact modal covariance formula over K0/K1 and r=0,.0001,.001,.01,.05, eps1e-2 through1e-12, including asymptotic analytic tail values.
2. Independent NumPy 6x6 orthogonally rotated matrix A and scipy.linalg.expm propagation vs reconstructed modes on 20 conditions; BDF 36-state integration of generic Lyapunov ODE for three additional conditions, differences max 2.44e-10. Independent *commuting model mismatch* A_actual=A_nominal+delta lambda1 u1 u1^T gives exact residual r=delta checked at -5%,-1%,0,+1%,+5%; noncommuting rotations NOT tested.
3. Independent pure Python math/bisection 18 precision gates over target eps and beta=.1,.2,.5, direct inequality, +0.1% and -0.1% around gate verify logical distinction. NO stochastic finite-sampling, digital preprocessing cost, energy budget, nonquadratic or source-device effects; NO claim full algorithm speedup.

## Custody receipts
Moderator-local complete 11-member ZIP, source scripts+three frozen deterministic JSON+full 10.9k-char Polish report+README+SHA256 manifest+standalone verify_rot009.py:
IW_XH_S5_ROT009_MPEMBA_CALIBRATION_PRECISION_REPRO_20261110.zip
ZIP bytes 17996; SHA256 202cb30dc49a837693929f62a78a882ac2a4ef8f8373e5ef6cdac50b9451fff1.
Full report SHA256 b03796d0ffa7b1bbffe9d3e904ec455cc0fe25542dee7268f396571ad41745f9.
Actual ZIP testzip() CRC PASS; 11 archive members checked; all manifest member SHA256 PASS; freshly extracted standalone verify_rot009.py reruns ALL THREE programs, frozen JSON BYTE IDENTICAL PASS. This GitHub research report is NOT the same as a GitHub-uploaded ZIP; source code has only been packaged in moderator-local ZIP unless separately transferred and verified.

## Strictly bounded source-native falsifier (not executed)
Freeze A, actual noise, device parameters and optical/voltage sampling scheme; vary prepared first-mode covariance error and eigenvector rotation; compare covariance errors vs times to the exact crossover and account separately for digital eigenpair computation, finite samples, hardware energy cost, multi-stage workloads. No physical experiment undertaken; do not treat this as task delegation or author flaw.

VERDICT: SOURCE_MOTIVATED_EXACT_SPECTRAL_GATE / PRIOR_ART_SUBTRACTED / NO_NOVELTY / NO_AUTHOR_FAULT / NO_CANON / NO_EXEC_SIGN / NO_BW_INGEST_VERIFIED / NO_TASK_CASCADE.