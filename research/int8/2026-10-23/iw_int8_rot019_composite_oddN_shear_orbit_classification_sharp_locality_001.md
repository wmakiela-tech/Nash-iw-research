---
artifact_id: IW_INT8_ROT019_COMPOSITE_ODDN_EQUIVARIANT_CONVOLUTION_ORBIT_AND_SHARP_LOCALITY_CLASSIFICATION_001_20261023
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
date: 2026-10-23
problem_id: P3_DTC0A_METRIC_NATURALITY_FILTER_OPERATOR_HOST_001
evidence: EXACT_FINITE_RING_PROOF / EXECUTED_ORBIT_ENUMERATION / RETAINED_SOURCE_HELPER_PASS
exposure: PUBLIC
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_KJ3_INVARIANT
---

# INT8 ROT019 — composite odd-grid universal fixed-stencil equivariance classification and exact locality threshold

## Source and mature-host subtraction

INT8 ROT018 proved prime-N scalar convolution rigidity. Historical DTC0a grids N=31,33,35,37,39,41 contain COMPOSITE 33,35,39; prime orbit proof alone was not applicable. Current Slack #iw-dispatch read on Oct23; XH-S4 ROT020–023 owns metric-natural York P_g, curved-host tests and filter-mismatch findings; M13 ROT023–027 owns actual historic source-family K_A replay, continuum and mask/stencil asymptotics; Geeky-S11 owns TT leakage/rigidity; PRF11 R24 owns mesoscopic centered-vs-spectral estimates. The following is a distinct elementary finite-ring classification, not a new physical NCDG or mathematical theorem family.

## Theorem 019.1 — all odd integer N, INCLUDING composites

Let N>=5 be odd, G=(Z/NZ)^3, H:G->Sym(3,R_real). Fixed componentwise scalar convolution T_c acts as (T_c H)(x)=sum_{v∈G} c(v)H(x+v). For every integral A∈SL(3,Z) let U_A H(x)=A^T H(Ax mod N) A. The following are equivalent:

(a) T_c U_A=U_A T_c for ALL integer determinant-one A, with THE SAME untransformed kernel c;
(b) c(v)=beta_d depends only on d=gcd(v1,v2,v3,N), indexed by positive divisors d|N;
(c) T_c belongs to the linear span of EXACTLY tau(N) subgroup-average operators
    Avg_d H(x)=(N/d)^(-3) sum_{u∈(Z/(N/d)Z)^3} H(x+d u),  d|N.

Avg_N=I; Avg_1=full spatial mean. Composite N admits additional subgroup comb projections. Their Fourier symbols are exactly 1 on k whose three coordinates are divisible by N/d and zero otherwise; they are not conventional isotropic lowpass Laplacians.

**Proof.** Direct tensor-index-preserving change of summation gives
T_c U_A H=A^T sum_w c(A^(-1)w)H(Ax+w)A,
U_A T_c H=A^T sum_w c(w)H(Ax+w)A.
Equality for all H iff c(A^(-1)w)=c(w). Elementary integer shears generate SL(3,Z/NZ). Its action on G has orbits precisely the coordinate-ideal classes (v1,v2,v3)=(d) in Z/NZ, labeled by d=gcd(v1,v2,v3,N). Indeed, v=d u with u a primitive vector mod q=N/d; over Z/qZ primitive vectors extend to determinant-one bases by Bezout/CRT/elementary row reduction, and elementary operations lift modulo N, mapping any such v to d e1. Invertible maps preserve the ideal, giving the converse. Thus (a) iff (b). Uniform subgroup kernels are invariant under all A. The indicators of subgroups dG are related to the exact gcd-orbit indicators by triangular divisor incidence, invertible by Möbius inversion, proving (b) iff (c). No physical or nonflat metric assertion.

Orbit cardinality for d is J3(N/d)=(N/d)^3 product_{prime ℓ|N/d}(1-ℓ^(-3)), the third Jordan totient. Dimension of equivariant kernel space = number of divisors tau(N).

## Theorem 019.2 — SHARP locality lower threshold

Define periodic-coordinate support radius R as maximum of min(v_i,N-v_i) for every kernel shift v with c(v) nonzero. Let p_min be the smallest prime divisor of N and d*=N/p_min. Set
    R*=(N-d*)/2=(N-N/p_min)/2.
If an equivariant kernel has support radius R<R*, it is necessarily a multiple of the identity T_c=gamma I. The bound is sharp: Avg_d* has exactly p_min^3 shifts and exact support radius R*, and is a NONIDENTITY universally invariant kernel.

Proof: For each proper divisor d|N, q=N/d is odd≥p_min, and w=(d(q-1)/2,0,0) has gcd(w,N)=d, since gcd((q-1)/2,q)=1. Therefore that entire orbit includes a shift with periodic radius (N-d)/2≥(N-d*)/2=R*. If R<R*, all orbit coefficients beta_d for d<N must vanish, leaving only v=0. Conversely shifts of Avg_d* are multiples of d* in each coordinate; their maximum centered coordinate is d*(p_min-1)/2=R*. QED.

In particular R*≥N/3 on ALL odd grids: no nontrivial universally unchanged small-radius 7-point E_lin can satisfy this strong condition, including N33/35/39. This DOES NOT preclude a correct metric-dependent transformed family E_(phi*g) U_phi=U_phi E_g, nonlinear/non-translation-invariant tensor operators, or a curved-spacetime physical Box.

## Source-matched executed verification

Independent BFS with six elementary shears, compared with Jordan-totient cardinalities, verified all gcd orbit classes with total N^3:

| N | gcd d : orbit cardinality | tau(N) | R* |
|---|---|---:|---:|
|9|1:702;3:26;9:1|3|3|
|15|1:3224;3:124;5:26;15:1|4|5|
|31|1:29790;31:1|2|15|
|33|1:34580;3:1330;11:26;33:1|4|11|
|35|1:42408;5:342;7:124;35:1|4|14|
|37|1:50652;37:1|2|18|
|39|1:57096;3:2196;13:26;39:1|4|13|
|41|1:68920;41:1|2|20|

With original unchanged axis-aligned E_lin at alpha=.05 and shear phi(x,y,z)=(x+y,y,z), random symmetric tensor discrepancy ||E_flat U-U E_flat||_RMS: N33 .34794721201, N35 .347247180878, N39 .345493027465. The genuinely equivariant Avg_d* commutator errors <=8.88e-16 and 0.7I+0.3Avg_d* errors <=1.78e-15, under the SAME random sample and shear. Independent full-grid tests N9 and N15 also PASS.

Literal retained helper 'deepseek_python_20260627_a87249.py', SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801, UNMODIFIED apply_E(.,'E_lin',2pi/N,order=2,alpha=.05), was imported and executed N33/35/39. Difference vs independent 7-point stencil <=8.88e-16. The original production dtc0a_runtime_v0_3_1.py, SHA256 2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084, remains byte-UNAVAILABLE; no original physical run is asserted.

Standalone full local report + independent Python verifier + executed ledger + README + SHA256SUMS have clean unzip/CRC PASS, SHA256 4/4 PASS, and clean-directory independent execution WITH and WITHOUT retained source helper PASS. GitHub source code publication is not assumed from this report link. Full local report SHA256 fec94cf2d34f07927be39ec9a1537350155a93692d5b58ee89d2832410477bac; reproducer SHA256 58ac507a43db8b63e8d97811edde7f3a8c9d69dddaa73cd6a1f0648b237ce16f.

**Disposition:** EXACT math and source-helper checks PASS. Owner/BW/referee/EXEC not claimed. This is NOT an explanation of historical DTC K_A plateau, TT physical gauge or a K/J3 invariant. No new task cascade.