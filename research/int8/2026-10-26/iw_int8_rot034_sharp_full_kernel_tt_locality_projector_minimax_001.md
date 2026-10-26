---
artifact_id: IW_INT8_ROT034_SHARP_ALL_SHIFT_NONLOCALITY_AND_SUBLINEAR_STENCIL_TT_GAP_001_20261026
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_SOURCE_TYPED_RAW_TT_PROJECTOR_LOCALITY_AND_METRIC_ORBIT_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_FINITE_LOCALITY_NO_GO / SHARP_L2_MINIMAX / MATURE_BERNSTEIN_HOST / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 ROT034 — exact all-offset TT kernel requirement and sharp bounded-stencil approximation dichotomy

## Precedence, currentness and mature prior-art subtraction

Slack #iw-dispatch checked 2026-10-26. MT13 FIRST established source-matched flat-affine metric-transported E_g and first exposed naive target raw-k TT alias fault. INT8 ROT023–028 ALREADY own its projector angles/singularities. INT8 ROT029–032 ALREADY own the fixed metric-INDEPENDENT full integral-shear operator commutant. INT8 ROT033 ALREADY owns the correctly metric-INDEXED transported family P_g=U_A P_I U_A^{-1} on odd finite flat integer-unimodular orbit, with 24-element stabilizer descent. M14 owns historical h=fI, masked K_A and source channel. Geeky-S11 owns even-grid real-cast source pathology, PRF12 the distinct Lie/TT problem, XH-S4/S5 curved York.

This ROT034 adds a distinct source-typed INTERFACE question: what spatial support is UNAVOIDABLE if a translationally invariant approximant is itself a projection, and how does the best bounded-stencil error change if idempotence is removed?

MATURE external host: discrete Fourier diagonalization, rank stability of finite projections, and classical Bernstein trigonometric inequality ||t'||∞ <= R||t||∞; Encyclopedia of Mathematics Markov–Bernstein-type inequalities https://encyclopediaofmath.org/wiki/Markov-Bernstein-type_inequalities . Original mathematical novelty or new physics is NOT claimed.

## Precisely fixed source

Odd N=2m+1>=3; G_N=(Z/NZ)^3, V_N=all real symmetric covariant 3x3 tensor fields with flat Frobenius L2. P is the ORIGINAL odd-grid raw-k source helper apply_P_TT, spectrally L2-orthogonal; Phat(k) rank2 for EVERY NONZERO Fourier k, and at k=0 the SOURCE rank5 tracefree projection. Therefore real rank(P)=2N^3+3. Retained original user helper deepseek_python_20260627_a87249.py SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. Historical entire production dtc0a_runtime_v0_3_1.py remains BYTE UNAVAILABLE.

A TRANSLATION-INVARIANT arbitrary linear F has convolution kernel K_F(d), one 6x6 endomorphism of symmetric tensors for EVERY lattice shift d. The support is supp(F)={d:K_F(d) != 0}; matrix entries may vanish. Stencil coordinate radius <=R if support is in signed cube [-R,R]^3. Unless specified, F need not be selfadjoint, orthogonal, scalar, local or metric-independent; IDENTITY of global P is fixed at source metric I. All approximation errors below are FULL input L2 operator norms, unmasked.

## EXACT THEOREM 034.1 — every one of N^3 spatial displacements is required

Suppose F is a real translation-invariant IDEMPOTENT F²=F (even oblique), and ||F-P||_(L2->L2) < 1. Discrete Fourier simultaneously block-diagonalizes F and P.

**RANK STABILITY LEMMA:** If two idempotents E,F on finite-dimensional normed vector space have ||E-F||<1 then rank E=rank F. Indeed if ranks differ, one of ran E intersect ker F or ran F intersect ker E has nonzero vector v, with (E-F)v=+v or -v and hence ||E-F||>=1. Apply this for EACH Fourier 6x6 block (complex matrices included).

Consequently tr Fhat(k) = rank Fhat(k) = rank Phat(k) = 2+3*1[k=0].

Take inverse discrete Fourier transformation of this SCALAR TRACE SYMBOL. The trace of spatial convolution kernel MUST satisfy FOR EVERY d in G_N:
   tr K_F(d) = 2*1[d=0] + 3/N^3.                    (T034.1)

For d!=0 this is 3/N^3>0; for d=0 it is 2+3/N^3>0. Therefore **K_F(d) is NONZERO for ALL N^3 shifts**, and supp F=G_N. This is STRONGER than a radius lower bound.

The SOURCE projector P has this exact identity too, so is itself a FULL-NONLOCAL convolution kernel; it cannot omit a single shift. Only its block TRACE is asserted nonzero, NOT all entries of each 6x6 block.

**SHARP UNIVERSAL BEST-ERROR STATEMENT**: for ANY proper subset S of G_N,
   inf{||P-F||: F²=F, F translation invariant, supp(F)⊆S} = 1.
Lower: a smaller error would force all shifts. Upper: F=0 has error ||P||=1 and empty support.
For full S=G_N exact F=P gives best error 0.
For the cubical signed radius R<=m, this gives **EXACT**
   inf_(F²=F, radius<=R) ||P-F|| = 1 if R<m, and 0 if R=m.
This is valid for ALL odd N and all idempotents including non-selfadjoint ones. It is not a claim about nonlinear algorithms, arbitrary nontranslation-invariant corrections, restricted source-TT inputs, typical random fields or the true historical masked K_A.

On N31,35,41 every exact/<1 projective approximant requires respectively ALL 29791, 42875, 68921 shifts. Exact sharp minimum radii m=15,17,20.

## EXACT THEOREM 034.2 — removal of idempotence changes the threshold from 1 to 1/2

Now F is ANY translationally invariant linear operator with spatial support in cube [-R,R]^3, NO F²=F requirement. For every fixed N the cheap onsite choice F=I/2 yields ||P-I/2||=1/2: P is an orthogonal projector.

Further, for ANY odd sequence N→∞ and any R_N=o(N),
   lim_N inf_(F linear translation-invariant, radius<=R_N) ||P-F|| = 1/2.
This is a SHARP asymptotic result but NOT a sharp finite-N formula for every R>0.

Proof lower: let T=diag(2,-1,-1)/sqrt6 with Frobenius norm1. The original P acts on this polarization along Fourier x-axis as Kronecker delta:
   Phat(0)T=T, Phat((j,0,0))T=0 for all j!=0.
For any candidate F, f_j=<T,Fhat((j,0,0))T> comes from a degree<=R trigonometric polynomial f(theta). With epsilon=||P-F||, |f(0)-1|<=epsilon, |f(2pi*j/N)|<=epsilon for j!=0.

Let M=max_theta |f(theta)|. Classical Bernstein: max|f'|<=R M. Nearest sample at angular distance at most pi/N gives for alpha=pi R/N<1:
   M <= (1+epsilon)/(1-alpha).
Compare theta0=0 and theta1=2pi/N:
   1-2epsilon <= |f(0)-f(theta1)| <= (2pi R/N)M.
With beta=(2pi R/N)/(1-pi R/N), derive the EXPLICIT lower certificate:
   epsilon >= max{0, (1-beta)/(2+beta)}.          (T034.2)
When R_N/N→0, beta→0, so lower tends 1/2. The onsite I/2 construction attains the upper 1/2. QED.

This contrasts with the idempotent full-support theorem: even when arbitrary LOCAL linear approximations can approach error1/2, a genuine local PROJECTION cannot improve below error1 until support equals the whole lattice. There is NO invented physical meaning to either number.

**Independent scalar witness LP:** because delta at j0 is reflection invariant, symmetrization yields an optimal real-even degree-R scalar trigonometric approximant. This 1D LP gives a numerical LOWER BOUND on best FULL TENSOR F, NOT the full operator optimum. SciPy HiGHS 28/28 separate LPs:
 N31: R0=0.5, R1=0.494869323392, R3=0.455912614251.
 N41: R0=0.5, R1=0.497065801184, R3=0.474340713357.
 N101: R0=0.5, R1=0.499516282292, R3=0.495666986172.
 N201: R0=0.5, R1=0.499877856941, R3=0.498901635780.
Every numerical LP optimum passes the independent certified Bernstein lower estimate (24 analytic lower-bound values additionally calculated for N101/201/401/1001).

## Transported metric orbit, no physical extension

By ROT033 for g=A^T A, P_g=U_A P U_A^-1 with U_A H(x)=A^T H(Ax mod N) A. Such conjugation permutes spatial displacements by bijection of G_N and conjugates six-component fiber kernels, preserving their matrix traces. Therefore **every transported P_g also has all N^3 shifts in its convolution kernel**. For consistently transported candidate families and geometric L2(g), the isometric operator-norm obstruction persists. A metric-dependent family can be exactly natural AND necessarily spatially nonlocal. No all-curved metric/physical gauge inference.

## Actually executed independent falsifiers and negative knowledge

- NumPy full THREE-DIMENSIONAL inverse FFT of 2+3 delta_{k0}, verifying tr K(d)=2 delta_{d0}+3/N^3 for every offset at N=5,7,9,15,31,35,41 (7/7), absolute max errors below 1e-15.
- Unmodified retained SHA-checked source helper apply_P_TT on six Frobenius-orthonormal impulse tensor fields at N=5,9,15: source REAL 6-column convolution trace agrees with theoretical entire spatial array, max deviation <=4.45e-16. Native helper constant puretrace/traceless and nonzero-axis polarization tests at N5/7/9/15 all PASS, and original E_lin componentwise alpha=.05 axis multiplier matches 1-4alpha sin²(pi/N). NO native six-column helper test at N31/35/41 is claimed (the original Python helper uses triple nested Fourier loops).
- Completely independent SymPy exact rational source-FREE calculation of projector matrices Phat(0), Phat(e1), invariance under scaling by each nonzero integer j, rank5/rank2 and polarization T. Exact rational 3/N^3 and 2+3/N^3 certificates for 8 grids N3/5/7/9/15/31/35/41. The source-free proof scales to all odd N, NOT only those checked.
- 28/28 real-even scalar witness LP executions, all bounded by the Bernstein certificate, plus 24 finite-grid analytic certificates. Native source and mathematics separately typed.

NEGATIVE KNOWLEDGE: An initial independent SymPy sanity test compared a 6x1 vector with a 6x6 zero matrix and FAILED. Fixed shape to 6x1 and reran PASS. Another preliminary per-mode brute-force exact rank audit needlessly exceeded runtime; replaced by a separately verified exact invariance of P(j e1) under j!=0 and analytical Fourier identity. A preliminary attempted native six-column N35 convolution also exceeded practical runtime; it was NOT counted, and native tests were bounded to N5/9/15. No negative control is hidden or marked PASS prematurely.

## Local replay custody

Full local Moderator ZIP: iw_int8_rot034_complete_kernel_locality_bundle.zip
SHA256 7d126fc2c7c40ce2caaece74ecc7d0befb792d0ffbd597e5df34b9c25d5c65b8, 8 members including full Polish proof, two independent complete Python sources, two output JSON, README, execution log and SHA256SUMS manifest. ZIP CRC PASS and SHA256 **7/7 PASS** for payloads. Two CLEAN EXTRACTIONS: with byte-SHA-checked original helper both JSONs reproduced BYTE-IDENTICAL to archived; without helper, SymPy exact audit JSON byte-identical and independent FFT/LP/Bernstein math equal, but source marked SKIPPED and main JSON correctly differs in source provenance. Source helper code not redistributed and not falsely claimed stored on GitHub; original historical production runtime unavailable.

## Strict epistemic stop

All results are finite odd-grid raw-wavevector tensor Fourier projector statements. Zero mode is TRACEFREE rank5. Does NOT transfer automatically to even-grid source real-cast (Geeky-S11), any mean-zero-only prior, different k0 projector, local approximants under different norms, arbitrary non-translational schemes, actual masked NCDG K_A, J3/K invariance, curved York, physical gauge, GW energy, PBH or experiments. NO mathematical novelty, NO physical upgrade, NO canon, NO EXEC. Independent referee/owner adoption/BW ingestion PENDING. NO new task cascade.
