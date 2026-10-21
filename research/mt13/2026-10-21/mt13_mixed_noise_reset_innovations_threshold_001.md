# MT13 — Mixed readout-noise reset: exact information threshold and state variance
Date 2026-10-21 | RETURN_ID MT13-MIXED-NOISE-RESET-INNOVATIONS-THRESHOLD-001_20261021
CLASS: classical scalar Gaussian innovations, conditional exact theorem, standard hosts, NO NOVELTY / NO CANON / NO EXEC / NO PHYSICS.

Source subtraction: Geeky-S10 already proved the alpha=1 raw-noise reset isomorphic to passive sampling, and PRF11 R13 proved alpha=0 Gaussian collapse under finite storage. This note interpolates these distinct carriers, not a re-claim:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s10/2026-10-21/geeky_s10_noise_driven_reset_passive_innovation_equivalence_001.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-21/IW_PRF11_R13_ADAPTIVE_WEAK_SENSOR_LECAM_INFORMATION_MINIMAX_COLLAPSE_001_20261021.md

MODEL: one x1=theta in [-R,R], G=0, fixed 0<s<1, iid eta_j~N(0,sigma^2), Z_j=s*x_j+eta_j, x_(j+1)=x_j-[(1-alpha)*s*x_j+alpha*Z_j]=(1-s)x_j-alpha*eta_j, 0<=alpha<=1. The scalar alpha measures contemporaneous readout-noise injection, not a claim about any real detector.

EXACT FIXED-PROTOCOL INNOVATIONS: write kappa=1-alpha, rho=1-kappa*s. Conditional on the same registered past Z, x_j=rho^(j-1)*theta - alpha*sum_(k<j)rho^(j-1-k)Z_k. Thus the parameter-independent invertible unit lower-triangular record map
Y_j = Z_j + alpha*s*sum_(k<j)rho^(j-1-k)*Z_k
gives Y_j=s*rho^(j-1)*theta+eta_j. The statistical experiment is exactly equivalent to independent Gaussian samples with sensitivities c_j=s*rho^(j-1), not necessarily the same physical reset trajectory.

EXACT FISHER and KL:
I_N=(s^2/sigma^2)*sum_(j=0)^(N-1)rho^(2j).
If kappa>0, I_N=s*[1-(1-kappa*s)^(2N)]/[sigma^2*kappa*(2-kappa*s)].
If kappa=0, I_N=N*s^2/sigma^2.
KL(P_theta||P_theta')=(theta-theta')^2*I_N/2.
For fixed alpha<1, I_infty=s/[sigma^2*(1-alpha)*(2-(1-alpha)*s)]=O(s)->0 uniformly in arbitrary finite N. Therefore any nonzero noise injection alpha>0 does NOT automatically prevent information collapse.

PHASE TRANSITION: Let kappa(s)=c*s^p>0, alpha(s)=1-kappa(s), c>0, p>=0. I_infty ~ s^(1-p)/(2*c*sigma^2). For p<1 even arbitrary-N information vanishes. For p=1 it can remain nonzero finite, and p>1 can diverge with adequate N in bare mathematics. At N(s)=floor(t/s^2), t>0, I_N tends respectively to 0 (p<1), [1-exp(-2*c*t)]/(2*c*sigma^2) (p=1), t/sigma^2 (p>1). Full alpha=1 also yields t/sigma^2.

ADAPTIVE HETEROGENEOUS BOUND FOR SAME SCALAR G=0 MODEL: let predictable actions s_j(h)<=epsilon<1 and alpha_j(h)<=1-kappa for fixed kappa>0, with same theta-independent policy, iid current innovations independent of past. For every frozen observation history, a1=1, a_(j+1)=[1-(1-alpha_j)*s_j]*a_j, conditional coefficient c_j=s_j*a_j. Exact telescoping gives
sum_j c_j^2 <= epsilon/[kappa*(2-kappa*epsilon)].
Proof: a_j^2-a_(j+1)^2=(1-alpha_j)*s_j*[2-(1-alpha_j)*s_j]*a_j^2; each c_j^2 divided by that drop is s_j/[(1-alpha_j)*(2-(1-alpha_j)*s_j)] <=epsilon/[kappa*(2-kappa*epsilon)]. Summation telescope. Bound attained in N->infty supremum by constant alpha=1-kappa and s=epsilon.
Sequential Gaussian KL <=(theta-theta')^2*epsilon/[2*sigma^2*kappa*(2-kappa*epsilon)], Fisher <=epsilon/[sigma^2*kappa*(2-kappa*epsilon)], and Pinsker TV(P_theta,P_0)<= R*sqrt(epsilon/[kappa*(2-kappa*epsilon)])/(2*sigma). PRF11 R13 two-point Bayes yields minimax squared-error lower bound R^2*[1-R^2*epsilon/(sigma^2*kappa*(2-kappa*epsilon))]_+ and upper bound R^2. For varying kappa(epsilon), collapse follows when epsilon/kappa(epsilon)->0.

STATE-NOISE COST (separate from conditional sensitivity): actual x_(N+1)=(1-s)^N*theta-alpha*sum_(k=1)^N(1-s)^(N-k)*eta_k. Therefore
Var(x_(N+1)|theta)=alpha^2*sigma^2*[1-(1-s)^(2N)]/[s*(2-s)].
For N~t/s^2 and alpha(s)->1 this grows as sigma^2/(2*s), despite nontrivial preserved statistical information. IF an additional uniform source state-variance budget V is imposed, necessarily alpha=O(sqrt(s)), and the information collapses O(s) for the constant-strength family. V is an added assumption, not supplied by any actual physical sensor.

NUMERICAL: independent Gaussian raw-covariance inversion vs innovation FI, triangular inverse, direct simulation for 12 (N,alpha) combinations, plus heterogeneous fixed-history finite-difference test: PASS. Python code and full Polish 14.5k-character detailed proof are in MT13 local conversation attachments. At s=0.01,N=10000,sigma^2=1, Fisher(alpha=0)=0.005025126, Fisher(alpha=.5)=0.010025063, Fisher(alpha=1-s)=0.432360743, Fisher(alpha=1)=1. The state variance for alpha=1-s after 9999 resets is about 49.251256.

HOSTS: Anderson & Moore, Optimal Filtering (innovations chapter); PRF11 R13 Gaussian likelihood/Le Cam; Geeky-S10 raw-reset triangular isomorphism. Classical linear filtering and geometric sums, NO mathematical priority or physical upgrade.

FIREWALLS: α interpolating ideal and raw current noise is a HYPOTHETICAL interface; real-device access to the ideal/noisy components not established. G=0 scalar one-preparation no free flow, current innovations iid of FIXED variance; no bandwidth/time, state constraints except when explicitly added; no quantum instrument, NCDG, PBH/BBN, nor process equivalence. LT5 book integration at owner discretion; external referee and BW custody not claimed.
