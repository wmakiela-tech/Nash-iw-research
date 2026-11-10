# M14 ROT035 — Chebyshev–Lobatto sampling with polynomial temporal calibration drift: sharp minimax and Gaussian falsifier

artifact_id: IW_M14_ROT035_CHEBYSHEV_LOBATTO_TEMPORAL_DRIFT_SHARP_MINIMAX_AND_GAUSSIAN_FALSIFIER_001_20261110
date: 2026-11-10
origin: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09 / M14
return_id: M14-ROT035-XH5-AUD1-REC11-CHEB_LOBATTO_SHARP_TEMPORAL_SAMPLING_GAUSSIAN_NEGATIVE_CONTROL_001_20261110
exposure: PUBLIC
claim_ceiling: EXACT_CLASSICAL_CONDITIONAL / NO_NOVELTY / NO_REAL_NV_DEVICE_REPLAY / NO_PHYSICAL_SENSITIVITY / NO_NASH_PHYSICS / NO_CANON / NO_EXEC_SIGN
custody: public GitHub note only, separate local full proof+ZIP; no BW/REC11/AUD1 adoption assumed.

## Scientific precedence and boundaries

XH-S5 ROT007 first owns F. Schall, L. Lindner, Y. Rottstaedt et al., *Laser-enhanced quantum sensing boosts sensitivity and dynamic range*, Nature Communications 17:10825 (published 2026-10-22), DOI https://doi.org/10.1038/s41467-026-78386-z. Their actual four-orientation NV source (Fig. 2) and separate triplet 14N hyperfine NV sample (Fig. 3b) must NOT be fused into a validated single signed paired sensor. The 127 fT/sqrtHz reported in that work is a photon-shot-noise SENSITIVITY LIMIT, not achieved technical-noise sensitivity. No author-native paired time-series, polynomial sensor drift, delta bound, gamma calibration or Poisson temporal center errors replayed.

M14 ROT031 owns tetrahedral four-axis common-shift geometry; ROT032 owns bounded orientation drift/parity-dark sharp minimax; ROT033 owns conditional nonzero-parity sharp bound; **ROT034 (2026-11-08)** owns the polynomial calibration quotient and sharp 3/4-axis radius for EQUALLY SPACED times. ROT035 extends only to **nonuniform temporal node placement** and explicitly falsifies transferring its bound to Gaussian variance. NIST DLMF Chebyshev identities: https://dlmf.nist.gov/18.5. Classical polynomial interpolation / Chebyshev extremal duality, NO claim of mathematical priority.

## Frozen conditional observation model

m=p+1 >=1; m+1 known distinct times 0=t0<...<tm=L; tetrahedral axes a1=(1,1,1), a2=(1,-1,-1), a3=(-1,1,-1), a4=(-1,-1,1); A^T A=4I3 and A^T 1=0. Hypothetical paired half-center observations for each orientation:
g_i(t_k)=a_i·b(t_k)+eta_i(t_k)+xi_i,k; b=(gamma/sqrt(3))*physical_B.
Each eta_i is an arbitrary, independent polynomial of degree <=m-1 (calibration not shared across orientations). For the deterministic risk result only: separate simultaneous |xi_i,k|<=delta and exact timestamps. This error assumption is NOT established by the paper.

Define lambda_k=1 / product_{l != k}(t_k-t_l), z=sum_k lambda_k b(t_k), y_i=sum_k lambda_k g_i(t_k).
Lagrange identities: sum lambda_k t_k^r=0 for r<m; sum lambda_k t_k^m=1.
Therefore y_i=a_i·z+epsilon_i with epsilon_i=sum lambda_k xi_i,k and sharp kappa=delta*sum|lambda_k|.

R35.1 EXACT QUOTIENT AND SHARP FULL-DATA COMPATIBILITY: Each eta_i occupies precisely the m-dimensional polynomial subspace of m+1 observations; y_i is its one-dimensional quotient. Every epsilon_i in [-kappa,kappa] is attainable with lawful raw-time errors; conversely any z satisfying |y_i-a_i·z|<=kappa fits ALL raw observations after choosing a polynomial eta_i degree<=m-1. No hidden extra raw-data constraint for this MINIMAL time window. The vector gauge b(t)->b(t)+h(t), eta_i->eta_i-a_i·h(t), any vector polynomial degree<=p, remains exact (including the paired spectra if centers agree). Three axes identify z noiselessly; four add a parity consistency check.

For bounded center errors: the exact minimax uniform Euclidean radius is sqrt(3)*kappa with first three axes and kappa with all four. A3^-1(d1,d2,d3)=((d1+d2)/2,(d1+d3)/2,-(d2+d3)/2). Four-axis estimator zhat=A^T y/4 has ||zhat-z||<=kappa since AA^T=4I4-11^T, and equality is possible with balanced signs. Both lower bounds are reached by TWO distinct polynomial field worlds producing identically ZERO ALL RAW READINGS (m=3, delta=.01): z=+/-kappa*(1,1,-1) for three axes or +/-kappa*(1,0,0) for four. Independent polynomial calibration and errors remain legal. Conditional nonzero-parity refinement is inherited from ROT033, not newly proved.

For GENERAL b(t), z is the mth DIVIDED DIFFERENCE and changes if time nodes change; only under an additional b(t) polynomial degree<=m assumption is z the SAME t^m coefficient for every design. No fair field-coefficient design comparison otherwise. For equispaced h=L/m, z=Delta^m b/(m! h^m): this is a rescaling, not contradiction of ROT034.

## R35.2 GLOBAL OPTIMAL bounded-error time design (classical exact proof)

Among ALL distinct m+1 observation times in [0,L], the minimum of kappa is EXACTLY

kappa_star = 2^(2m-1) * delta/L^m,

uniquely attained by Chebyshev–Lobatto extrema t_j=L*(1-cos(j*pi/m))/2, j=0,...,m. Proof: P_m(t)=T_m(2t/L-1) has sup|P_m|<=1 and leading coefficient c=2^(2m-1)/L^m, so c=|sum lambda_j P_m(t_j)|<=sum|lambda_j|. The Cheb extrema attain equality with alternating signs. More precisely lambda_j=(-1)^(m-j)*[2^(2m-1)/(m L^m)]*(1/2 for endpoints, 1 for interior). Equality forces all nodes to be extrema of P_m, hence uniqueness of this node SET.

For equispaced t_j=jL/m, sum|lambda_j|=2^m*m^m/(m! L^m), hence kappa_equal/kappa_star=m^m/(2^(m-1)*m!). This equals 1 for m=1,2, 9/8 for m=3 (11 1/9% less worst-case error), 4/3 for m=4 (25% less), 625/384 for m=5 (38.56% less), 81/40 for m=6 (50.62% less). These percentages refer ONLY to the sharp worst-case bound for the SAME field-polynomial coefficient on a fixed time span; NOT physical fT precision.

## R35.3 STRONG EXACT NEGATIVE / Gaussian variance is a different objective

If one instead assumes independent homoscedastic Gaussian time errors of variance sigma^2, the quotient variance is sigma^2*sum(lambda_j^2), NOT sigma^2*(sum|lambda_j|)^2. EXACT RATIONAL COUNTEREXAMPLE for m=3,L=1:

- Cheb nodes (0,1/4,3/4,1): L1(lambda)=32, L2(lambda)^2=2560/9.
- Different nodes (0,7/30,23/30,1): L1(lambda)=225/7 >32, yet L2(lambda)^2=14630625/51842 <2560/9.
- The strict variance-factor improvement is 1039895/466578 >0, about 0.7835519% relative to Cheb.

For four independent equally noisy axes covariance of zhat=A^T y/4 is sigma^2*||lambda||2^2*I3/4, so Gaussian variance counterexample transfers to vector field readout. No claim that the alternative nodes are Gaussian-global optimum. Neither noise model is experimentally validated for Schall's paired centers.

## Certification / caveats

FULL OFFLINE PACKAGE contains a 12k-character Polish proof, SymPy exact script (23 groups PASS), independent mpmath 90 digit numeric code (2412 checks PASS, including 750 random node comparisons and 800 randomized multiaxis observations), exact rational FULL RAW DATA two-world witnesses for 3 and 4 orientations, a pure stdlib replay, both generated JSONs, hashes, README and intended cross-cell dispatch. 2412 synthetic checks are not independent experiments and do not certify globality. Local ZIP and integrity report are separate from the GitHub contents API.

No source-certified bounded delta, temporal clock accuracy, shot budget equality, source-native device data, global Lorentz inverse, physical NV field units, Nash J3/K/GR/GW/PBH result, accepted BW ingestion, referee sign-off, canon or execution sign-off.

NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NASH_PHYSICS / BW_PENDING / REC11_AUD1_PENDING / NO_NEW_TASK_CASCADE.
