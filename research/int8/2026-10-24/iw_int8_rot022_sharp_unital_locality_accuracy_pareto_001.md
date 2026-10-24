---
artifact_id: IW_INT8_ROT022_SHARP_UNITAL_SHEAR_EQUIVARIANT_FILTER_LOCALITY_ACCURACY_FRONTIER_001_20261024
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_METRIC_NATURALITY_FILTER_OPERATOR_HOST_001
exposure: PUBLIC_SAFE
science_status: FINITE_FOURIER_THEOREM_PRIMAL_DUAL_AND_SOURCE_HELPER_REPRO_PASS
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 ROT022 — exact unital locality versus minimax approximation frontier for the retained DTC E_lin

## Scientific currentness and attribution
INT8 ROT018/019 owns the universal fixed-kernel SL3 shear-equivariant scalar-convolution classification, sharp first allowable locality radius, and odd/composite arithmetic orbits. INT8 ROT020 owns the unconstrained **full-band** approximation distance of E_lin to that entire class. INT8 ROT021 owns regularity-weighted Hs approximation. New question: require the replacement to preserve constants, **T1=1**, as the original source E does, AND limit stencil radius R. Without T1=1, a scalar near-optimal filter aI is allowed but spoils constant fields. XH-S4 owns York/curved metric and source E covariant issues; MT13 has now independently verified a geometrically TRANSPORTED local filter family under affine metric and its precise alias stop; M13 ROT023–030 owns original h=fI source K_A/mask; Geeky-S11 and PRF11 own independent TT/alias/commutator questions. No owner novelty, CANON, physics or original production runtime assertion.

## Carrier and exact finite minimax linear program

Odd N>=5. Tensor Sym² on periodic G_N=(Z/NZ)^3, FULL normalized Frobenius L2 norm, no boundary mask. Source helper deepseek_python_20260627_a87249.py SHA256 **23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801**. Exact componentwise stencil

  E_alpha=I+alpha sum_(i=1 to 3)(tau_ei+tau_-ei-2I),
  e_alpha(k)=1-4alpha sum_i sin²(pi k_i/N).

Fix one REAL componentwise translation-invariant scalar convolution kernel, unchanged under ALL pullbacks U_A H(x)=A^T H(Ax)A, A∈SL3(Z). Require additionally **T1=1** and support periodic coordinate-radius ≤R. This is a FIXED KERNEL contract, not a metric-indexed family E_g.

For d|N let Avg_d be uniform average over subgroup d G_N, with Avg_N=I and Avg_1=global mean. The prior orbit theorem implies precisely
  T=sum_(d in D_R) a_d Avg_d,
  D_R={d|N : (N-d)/2<=R},
  sum_d a_d=1      [unital].
For Fourier gcd orbit f=gcd(k1,k2,k3,N), Avg_d has scalar multiplier 1 iff N/d divides f, hence
  t_f=sum_(d in D_R, (N/d)|f) a_d.
Let m_f=min_{gcd(k,N)=f}e(k), M_f=max_{gcd(k,N)=f}e(k).
Then the **EXACT attained** radius-constrained minimax is the finite LP:
  rho_N(R)= min_{sum a_d=1} max_{f|N} max(|m_f-t_f|,|M_f-t_f|).    (1)
This is not a regression, numerical interpolation or historical observable. A second LP constrains all a_d>=0, giving convex mixtures of positive constant-preserving subgroup averages.

## Explicit exact endpoints and primal/dual certificates

Write p_min for smallest prime divisor, R*=(N-N/p_min)/2, m=(N-1)/2.
For R<R*, the only universal fixed convolution is aI (ROT019), and T1=1 forces **T=I**. For alpha>=0 exact:
  rho_N(R)=||E-I||=12alpha cos²(pi/(2N)).                        (2)
At R=m, the scalar Markov kernel
  T_opt=aI+(1-a)Avg_1,
  a=(e_low+e_high)/2,
  e_low=1-4alpha sin²(pi/N), e_high=1-12alpha cos²(pi/(2N)),
has t=a on ALL nonzero modes, t(0)=1, and ATTAINS the ROT020 global distance
  rho_N(m)=2alpha[3cos²(pi/(2N))-sin²(pi/N)].                    (3)
At alpha=.05, 0<=a<=1, so both endpoints achieved by Markov mixtures, no negative coefficients.

For N=pq, DISTINCT odd primes p<q, the only intermediate radii are R_1=(N-q)/2 and R_2=(N-p)/2. Let m_f,M_f be orbit symbol extrema. At R_1 only Avg_q and I are available, so on gcd-p Fourier orbit the unital T multiplier is FORCED to be 1:
  rho_N(R_1)>=1-m_p.                                             (4)
This bound is ATTAINED by nonnegative coefficients for N=15,33,35,39 at alpha=.05 (verified by explicit LP primal witness).

At R_2 the two permitted averages Avg_p and Avg_q plus I give scalar multipliers x on primitive gcd1, y_p on gcd-p, y_q on gcd-q satisfying **x=y_p+y_q-1** by unitality. Three necessary LP inequalities are M_1-x<=rho, y_p-m_p<=rho, y_q-m_q<=rho. ADD them: the relation eliminates x,y_p,y_q and yields the exact **DUAL certificate**
  rho_N(R_2)>=(1+M_1-m_p-m_q)/3.                               (5)
For N=15,33,35,39, alpha=.05 this lower bound is attained by EXPLICIT nonnegative:
  rho=(1+M_1-m_p-m_q)/3,
  x=M_1-rho, y_p=m_p+rho, y_q=m_q+rho,
  a_I=x, a_Avg_p=y_q-x, a_Avg_q=y_p-x.
Substitution checks every e_min and e_max endpoint on all four Fourier orbits: max residual exactly rho. (5) is therefore **SHARP**, independently of numerical optimizer convergence.

This is a source-typed conditional exact sharp stagewise theorem for the stated alpha and semiprime N, not a claim of a universal alpha-independent closed formula for all rings.

## Executed Pareto frontier alpha=.05

|N|Below first allowable nonidentity radius: only T=I|First radius R1|Second radius R2|Full-global radius|
|--:|--:|--:|--:|--:|
|31|.598460797018|—|—|R15 .298206895571|
|33|.598641576772|R11 .587847892084|R15 .345346920604|R16 .298417223249|
|35|.598792288199|R14 .570290660371|R15 .370462905848|R17 .298592623529|
|37|.598919246563|—|—|R18 .298740418799|
|39|.599027192440|R13 .591282545228|R18 .346662523831|R19 .298866109352|
|41|.599119740355|—|—|R20 .298973891367|

N9 and N15 extra independent controls included in reproducibility JSON. Between displayed threshold radii, D_R does not change; optimum is exactly CONSTANT. For ALL displayed stages the positive-subgroup-average LP has the SAME optimum as signed coefficients, differences <1e-9. Markov positivity therefore costs nothing FOR THESE CASES, not asserted for all N/alpha/R.

## Executed independent tests and source provenance

Standalone script NumPy+SciPy HiGHS independently enumerated all gcd frequency orbits and source e minima/maxima on N9,15,31,33,35,37,39,41, solved BOTH signed and nonnegative exact finite LP formulations for every stage, directly substituted primal variables to verify realized sup norm, checked (2), (3), primal certificate (4) and analytic dual/primal sharp certificate (5) for four semiprime grids. ALL PASS.

Literal retained user source helper **byte SHA-checked** at runtime, SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. Unmodified apply_E E_lin on independent random symmetric tensors N31,33,35,39,41 matches direct seven-point stencil max absolute error 8.8818e-16. This does NOT authenticate unavailable historic dtc0a_runtime_v0_3_1.py, declared SHA256 2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084.

Local Moderator-conversation ZIP **iw_int8_rot022_unital_shear_locality_frontier_bundle.zip** SHA256 **141dd40ddda3fe3f836e020b254a9278075e86fbb976c5a9a0eb7df7b3fd4a9c** holds complete 9246-byte report, 6847-byte original executed verifier, 15513-byte JSON, README, SHA256SUMS. Clean unzip and CRC PASS, SHA256 manifest 4/4 PASS, independent clean-directory verification both WITHOUT helper (source-gate SKIPPED) and WITH SHA-checked helper PASS; JSON with-helper run BYTE-MATCHES archived JSON. Source script separately in local ZIP; GitHub code publication is NOT claimed unless separately read back.

## Distinctions / scientific disposition

Full-grid L2 filter approximation error ~.60->~.30 is a statement about mathematical operator norm, NOT percentages of historical K_A/K_B, energy conservation, k-invariant physics, gauge wave energy or original NCDG. Condition T1=1 preserves constant components on this lattice only; not a Noether law. A correct METRIC-ADAPTED LOCAL FAMILY E_(phi*g)U_phi=U_phi E_g is expressly ALLOWED, as shown by MT13 for affine maps, with its alias caveat. Original DTC0a uses same Euclidean grid and fixed E, no derived full covariant tensor □. BW/owner/referee/EXEC pending, NO_NEW_TASK, NO_NOVELTY.
