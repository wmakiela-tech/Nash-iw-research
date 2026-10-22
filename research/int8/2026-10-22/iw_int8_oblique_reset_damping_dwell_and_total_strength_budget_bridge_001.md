# INT8 ROT006 — oblique reset: exact damping–spacing threshold and finite-dose weak-readout guard
Date 2026-10-22. Cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8.
Class: cross-front exact finite-dimensional classical specialization; conditional proofs and numerical controls.
Authority: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
Owner/independent referee acceptance and BW ingestion: UNKNOWN.
Source interfaces: INT8 ROT005 oblique 2-sensor threshold (2026-10-21); INT8 ROT004 finite-T co-aligned ceiling; Geeky-S10 heterogeneous common-V* storage and noise-reset exact factoring; M13 ROT12 fixed-aligned nonnormal long-horizon instability; PRF11 R14-R15 noise precision nonmaps.

## 1. Frozen two-sensor carrier
Let e1=(1,0), e2=(0,1), d1=(1,-a), d2=(-b,1) with a,b>0.
At each shot, b_j=s e_i^T x^- and x^+=(I-s d_i e_i^T)x^- for a common 0<s<1. Both own-channel overlaps e_i^T d_i equal one; neither jump is necessarily Euclidean contractive.
Q1=[[1-s,0],[as,1]], Q2=[[1,bs],[0,1-s]].
Replace G=0 of ROT005 by G=-g I with g>0, waiting time h>0 between every two consecutive shots. An alternating pair has post-pair map
  B_g=e^(-2gh) B_0, B_0=Q2 Q1.
Set r=1-s, z=e^(2gh)>1. The polynomial of B_0 obeys
  det(z I-B_0)=(z-r)^2-ab*s^2*z,
  det B_0=r^2,
  tr B_0=2r+ab*s^2.

## 2. Theorem A: exact periodic damping/spacing threshold
Define
  Acrit(s,g,h)=(z-r)^2/(z*s^2)
               =(exp(2gh)-1+s)^2/(s^2 exp(2gh)).
For the prescribed equal-strength, equal-spacing, alternating *periodic* protocol:
  ab<Acrit => spectral radius B_g <1, asymptotically Schur stable;
  ab=Acrit => simple Perron eigenvalue 1, nonzero repeated records on its positive eigenvector;
  ab>Acrit => Perron eigenvalue >1, exponentially growing records on its positive eigenvector.
Proof: B_0 has strictly positive entries and determinant r^2<1. Its positive Perron eigenvalue lambda_+ exceeds r. For z>1, the polynomial det(zI-B_0) is positive exactly for z>lambda_+, since the other eigenvalue r^2/lambda_+<1. Hence lambda_+/z compares to one with the sign of ab-Acrit. The Perron vector has positive components, so both measured coefficients are nonzero. Repeated pairs produce l2 record divergence when lambda_+/z>=1. QED.
IMPORTANT: Stability of this one periodic cycle is NOT a proof of arbitrary-switching stability for a general action family.

As s->0+, lambda_+(s)=1+(sqrt(ab)-1)s+O(s^2).
Consequently:
- fixed h>0,g>0: Acrit~4*sinh(gh)^2/s^2 -> infinity; every fixed a,b eventually gives stable period;
- if h=kappa*s+o(s), kappa>=0: Acrit->(1+2g*kappa)^2;
- for ab>1 and fixed s, the critical gap is hcrit(s)=log(lambda_+(s))/(2g), asymptotically [(sqrt(ab)-1)/(2g)]s.
At equality of the leading asymptotic threshold, second-order terms decide finite-s behavior: no automatic equality assertion.

## 3. Theorem B: common finite TOTAL STRENGTH recovers weak collapse even for oblique changing actions
Take an arbitrary finite-dimensional real G, and arbitrary actions (e_j,d_j) with ||e_j||<=E and ||d_j||<=D. Allow arbitrary action order and times 0<=t_j<=T. Set Q_j=I-s_j d_j e_j^T, b_j=s_j e_j^T x_j^-, with 0<=s_j<=epsilon and total dose S=sum_j s_j<=B<infinity. Define mu_+=max(0,lambda_max((G+G^T)/2)).
Then for every finite protocol,
  sum_j b_j^2
    <= epsilon*B*E^2 * exp(2*mu_+*T+2*D*E*B) ||x0||^2.    (T-B)
In particular this is O(epsilon), UNIFORMLY over all finite counts, directions and timings when E,D,T,B are frozen. No finite V* or common quadratic P needed, and resets may be oblique or individually expansive.

Proof: Between shots ||exp(G*tau)||<=exp(mu_+*tau). Each jump has ||Q_j||<=1+s_j D E<=exp(s_j D E). Therefore each pre-shot state obeys
  ||x_j^-||<=exp(mu_+ T+D E B)||x0||.
Summing b_j^2<=s_j^2 E^2||x_j^-||^2 and using sum s_j^2<=epsilon sum s_j<=epsilon B gives (T-B). QED.
This is a *dose* condition, not a frequency/hardware law. Pointwise proof also permits causally selected deterministic actions, provided each realized trajectory obeys the same bounds. Does NOT cover stochastic current-noise-driven resets as an instrument law.

## 4. Logarithmic total-dose threshold: explicit counterexample to dropping B
Set G=0 and a=b=q>1 in the two-sensor family, take equal strengths s=epsilon and alternate. Starting on the normalized positive Perron eigenvector v_s of B_0,
  lambda_+(s)=1+(q-1)s+O(s^2),
  A_s=(first-pair record energy)=s^2(1+O(s)).
The total record energy of k pairs is EXACTLY
  E_k=A_s*(lambda_+(s)^(2k)-1)/(lambda_+(s)^2-1).
Choose k(s)=floor(c*log(1/s)/(2s)) for c>0, so total dose 2k s ~c log(1/s). Then
  E_k ~[1/(2(q-1))] s^(1-c(q-1)) as s->0.
Hence c<1/(q-1): output energy ->0;
c=1/(q-1): output energy ->1/[2(q-1)];
c>1/(q-1): output energy ->infinity.
This is achieved with *arbitrarily many finite shots in any fixed T>0* by packing gaps sufficiently tightly since G=0. It does not involve an actual infinite protocol, and does not establish that such an unbounded-rate hardware schedule is physically legal.
PROOF of asymptotic: per-cycle readouts are s*v_1 and s*(v_2+q s v_1), and v_s->(1,1)/sqrt2. Use log(lambda_+)= (q-1)s+O(s^2); k*s^2=O(s log(1/s))->0, giving geometric-series asymptotics.

## 5. Controls, host subtraction and typed interfaces
SymPy verified det(zI-Q2Q1)=(z-1+s)^2-ab*s^2*z. Numerical comparisons:
a=b=1.44,g=.4 give hcrit/s = 0.57854 at s=.1, 0.55694 at s=.025, 0.55138 at s=.005; limit is 0.55.
At q=1.5, c=2=1/(q-1) the exact energy from Perron eigenvectors approaches 1: s=.03 ->1.01128, s=.01 ->1.01309, s=.003 ->1.00611.
A random 2D oblique protocol of 32 shots under T=1.7, epsilon=.03, total dose .5311<=B=1 gave total squared record .0071604 <= theoretical generic cap .51066.

Prior-art hosts, not novelty: switched/impulsive Lyapunov and average-dwell-time theory, e.g. *Stability and L2-gain analysis for impulsive switched systems*, CNSNS 78 (2019), 104854, DOI 10.1016/j.cnsns.2019.104854; *Switching systems with dwell time: Computing the maximal Lyapunov exponent*, Systems & Control Letters (2021), doi lookup via publisher; classical Gronwall, 2x2 Perron-Frobenius and Schur/Jury criteria. Exact special-family arithmetic is a project synthesis, not a claim to discovery.

Nonmaps: UNIT OWN-CHANNEL ATTENUATION != EUCLIDEAN CONTRACTIVITY; FINITE T ALONE != WEAK CEILING FOR OBLIQUE UNBOUNDED-EVENT-PROTOCOLS; PERIODIC STABILITY != ALL-SWITCHING STABILITY; TOTAL DOSE FINITE != GLOBAL FINITE V*; READOUT SIGNAL BUDGET != STATISTICAL FISHER WITHOUT NOISE PRECISION; CLASSICAL RESET != QUANTUM MEASUREMENT; NO DTC/NCDG/J3/PBH transfer.

Claim ceiling: EXACT CONDITIONAL_FINITE_DIMENSIONAL / MATURE_HOST_SPECIALIZATION / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_NEW_TASK_CASCADE.
