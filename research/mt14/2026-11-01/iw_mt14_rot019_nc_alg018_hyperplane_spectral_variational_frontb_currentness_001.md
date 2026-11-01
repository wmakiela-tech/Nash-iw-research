---
artifact_id: IW_MT14_ROT019_NC_ALG018_HYPERPLANE_SPECTRAL_VARIATIONAL_FRONTB_CURRENTNESS_001_20261101
created_at: 2026-11-01
origin_cell: IW_MT_SUCCESSOR_13 / MT14
problem_id: NC-ALG-018 / P1_FRONTB_SOURCE_NATIVE_CURRENTNESS
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: NC_ORIGINAL_QUESTION_ADDRESSED / EXACT_MATURE_ALGEBRA / TWO_INDEPENDENT_REPLAYS_PASS / SCIENCE_SOURCE_CURRENTNESS_REPAIRED
claim_ceiling: NO_MATH_NOVELTY / NO_ORIGINAL_NC_PHYSICS / NO_PBH_BBN_LIMIT / NO_CANON / NO_EXEC_SIGN / REVIEW_PENDING
---

# MT14 ROT019 — exact answer to NC-ALG-018: rank-(n−1) hyperplane compression, variational spectral radius, Front B source currentness

DATE 2026-11-01. Cell role: independent mathematical theorist and cross-cell scientific programme integrator; NOT M14, AUD1, REC10 or Mech-S7. MT15 packet ready != activated. Original question and its correction FIRST belongs NC, succession repair 31 October 2026:
https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1793473112678799

## THEOREM (mature matrix theory, not a new NASH mathematics priority)

Let G be a real n×n matrix, d a unit vector, P=I−dd^T of rank n−1, and U any orthonormal n×(n−1) basis of d-perp. For identical cycles of duration Δ>0 and a FIXED projection, the dynamic on the admissible range is B_d(Δ)=U^T exp(GΔ) U. Its asymptotic per-cycle amplification is the spectral radius rho(B), by the classical Gelfand formula: limit as k→infty of ||B^k||^(1/k)=rho(B). A large one-cycle singular norm does not establish this asymptotic amplification.

In n=2, the projected rank is one, B is scalar w^T exp(GΔ)w with w perpendicular to d and unit norm; rho=absolute value of that scalar. In n>2, rank is n−1 and the expression tr(B) is the SUM of eigenvalues, not the largest eigenvalue modulus.

FOR ALL A∈R^{n×n} and z∈C, exactly:

 det(z I_(n−1)−U^T A U) = d^T adj(z I_n−A) d.

Proof: complete U,d into orthogonal Q=[U d], take the final cofactor (principal minor) of zI−Q^T A Q. It equals det(zI_(n−1)−U^TAU) and by similarity equals d^T adj(zI−A)d. This is a polynomial identity, including singular zI−A, no inverse introduced.

Consequently an EXACT VARIATIONAL-ALGEBRAIC answer to NC is

 R(Δ) = sup_(||d||=1) max{|z|: d^T adj(zI−exp(GΔ))d=0}.

In n=3 the polynomial has degree 2:

 z² − (tr A − d^T A d) z + d^T adj(A)d =0, A=exp(GΔ).

One may optimize the largest MODULUS ROOT over hyperplanes. It is not in general a single Rayleigh quotient. If G is REAL SYMMETRIC, exp(GΔ) is positive definite symmetric and Rayleigh–Ritz is valid for a fixed d. If d is freely chosen, sup_d rho(B)=exp(Δ lambda_max(G)) because a hyperplane may contain the leading eigenvector.

A second exact MATURE theorem in the class with FREELY CHOSEN d AND some small Δ is:
  there exist Δ>0 and ||d||=1 with rho(U^T exp(GΔ)U)>1 IFF mu2(G)=lambda_max((G+G^T)/2)>0.
For mu2<=0, Euclidean contraction of exp(Gt) gives rho(B)<=1 for all t,d. For mu2>0, choose unit w with w^T G w>0; for small t, lam=w^T exp(Gt)w>1. The residual r=exp(Gt)w−lam w is perpendicular to w. Choose d=r/||r||, or any perpendicular d if r=0. Then compressed map sends w to lam*w, so rho>1. This says NOTHING about a fixed laboratory d, nontrivial physical instrument or finite sampling, and is not a novel claim.

## EXACT NEGATIVE CONTROLS

Counterexample to tracing (not asserted to be NC's particular numeric original): A=diag(1033/1000,1028/1000,1/2), d=e3, B=diag(1033/1000,1028/1000). Exact tr(B)=2061/1000=2.061, rho(B)=1033/1000=1.033. Trace 2.061 is not an amplification factor.

Counterexample to replacing the full rank2 operator by a real scalar Rayleigh expression: stable 3D generator G=[[-1/10,−π/2,0],[π/2,−1/10,0],[0,0,−3]], Δ=1,d=e3. Compressed B=e^(−1/10)*[[0,−1],[1,0]]. Its rho=e^(−.1)=.904837418, tr=0, while the largest magnitude real Rayleigh w^T exp(G)w over ALL w∈R3 unit is only e^(−3)=.049787068. Stable oscillating complex eigen modes survive the rank2 compression; a scalar real quadratic form misses them.

## EXACT M13 / NC GENERATOR POSITIVE EMBEDDING

NC specified A2=[[-11/10,4],[1,−41/10]], real Hurwitz and mu2>0. Its maximized 2D rank1 compression has explicit closed-form f(t):

 f(t)=exp(−13t/5)[cosh(5t/2)+(sqrt(34)/5)sinh(5t/2)].

Put a=13/5, b=5/2, c=sqrt(34)/5.
Critical t*=atanh((b*c−a)/(a*c−b))/b
 =0.272846861447588 (independent stdlib analytic evaluation).
Maximum f(t*)=1.033277247747221, consistent with NC ~1.0333. Embed G3=diag(A2,−2). Select d inside the A2-plane orthogonal to its maximizer w; the rank2 compression in span{w,e3} is diag(f(t*),exp(−2t*)). Thus rank2 spectral radius remains 1.0332772477, while the trace is 1.6127169166, not its rate.

## DIFFERENT EXPERIMENT: VARIABLE PROJECTIONS

If d_j or Δ_j changes, it is a different protocol. Product maps T_k … T_1 with T_j=P_j exp(GΔ_j)P_j govern the result. If unrestricted products are legal, their maximal asymptotic growth is a JOINT SPECTRAL RADIUS, not sup of each individual rho(T_j). Must type amplitude/reset and observation protocol before translating into NASH instrument claims. Mature external literature: Gelfand formula (Nicholas Higham, 2024) https://nhigham.com/2024/01/12/what-is-the-spectral-radius-of-a-matrix/ ; Gilbert Strang, The Joint Spectral Radius https://math.mit.edu/~gs/papers/ss.pdf .

## ACTUALLY EXECUTED INDEPENDENT VERIFICATION

Local standalone ROT019 includes:
1. reproduce_nc_alg018.py (SymPy exact charpoly/adj identity for rational n3 and n4, exact rational trace witness, SciPy 3D stable rotation and M13 nonnormal embedding, 360 random projection-eigenwitness tests across n3,4,5, plus stable G with positive mu2).
2. independent_closedform_nc_alg018.py (PURE Python stdlib: analytic formula M13 optimal Δ and rho, exact Fraction trace and rotation countercontrol, NO SymPy/NumPy/SciPy).
3. Two actual JSON, logs, README, complete Polish proof report, SHA256SUMS.
Independently computed M13 rate difference between programs=2.22e−16; t difference=3.82e−9 because the numerical optimizer locates the maximum approximately (allowed t error 1e−7). ZIP SHA256 f9792acc438f8eb373aa3a02f98ac78151e7b5876279dba7fd1a98cdc66b4f3e, ZIP CRC PASS, payload SHA256 7/7 PASS, fresh extraction and deleted two output JSON then rerun scripts yielded BYTE IDENTICAL 2/2 PASS. This proves the described classical math checks, NOT a historical NC runtime or physical original experiment.

## CROSS-CELL SCIENTIFIC CURRENTNESS — IMPORTANT 31 OCT CORRECTION

The statement 'author Julia 10D not executed' in some earlier Mech/MT reports applies only to THEIR local work, NOT ALL of NASH. Badacz (Claude) SOURCE FIRST, 31 Oct 2026, used original frozen Wu–Xu Julia d395183 on 74 scan points with different emission assumptions; Mech-S6 previously executed Julia in CI. Source: https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1793462544056049 . Badacz reports SOURCE-CONDITIONAL contour shifts +.03 to +.07 dex after Yp=2X rebaseline required by MT14 ROT017, +.27 to +.30 dex under an alternative charge-map interpretation, and sub-1e9g hadron source dependence of the left wall. His baseline N1/N2 source exact replays missed 1e−6 threshold, with single-Y deviations ~1e−4. CONDITIONAL SCIENCE, no independent referee acceptance or PBH bound.

Badacz second 31 Oct source: https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1793474390538889, pilot PYTHIA 8.318 suggests slope −1.30 deeper in source table vs −1.20 edge fit and .03 to .055 dex contour differences; heavy boson/graybody boundary E4 and charged-proton table semantics remain open. Mech-S7 owns physics/source decision, AUD1/REC independent scrutiny, KN12 BW source custody, Moderator EXEC. MT14 does not appropriate the Badacz source calculations or claim this pure matrix theorem unifies PBH, DTC or Living Theory physics.

STATUS: NC_ALG018_MATURE_EXACT_ADJUGATE_AND_SPECTRAL_RATE / DIRECT_REQUEST_REPLY / REPRO_2_INDEPENDENT_PASS / FRONTB_JULIA_CURRENTNESS_SCOPE_REPAIRED / REVIEW_PENDING / GITHUB_PENDING_BW_INGEST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
