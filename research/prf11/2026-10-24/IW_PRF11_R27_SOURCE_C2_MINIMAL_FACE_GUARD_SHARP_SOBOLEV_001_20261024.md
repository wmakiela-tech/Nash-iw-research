---
artifact_id: IW_PRF11_R27_SOURCE_C2_MINIMAL_FACE_GUARD_SHARP_SOBOLEV_001_20261024
created_at: 2026-10-24
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_10 / PRF11
problem_id: P3_DTC0A_Q39_FACE_GUARD_MINIMAL_SUPPORT_DEALIASING_AND_SHARP_SOBOLEV_RECOVERY
function: FOUNDATION_FIRST / OTHERS_FIRST / FALSIFICATION_FIRST / SOURCE_TYPED_MATURE_HOST_SUBTRACTION
exposure: PUBLIC_SAFE
document_type: EXACT_CLASSICAL_OPERATOR_THEOREM_AND_SOURCE_HELPER_NUMERIC_AUDIT
status: MATHEMATICAL_PROOF_SYMPY_NATIVE_SOURCE_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_K_J3 / NO_PRODUCTION_RUNTIME_IDENTITY
cross_surface_sync: GITHUB_PENDING_BW_INGEST
source_helper: deepseek_python_20260627_a87249.py
source_sha256: 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801
---

# PRF11 R27 — A source-minimal Fourier-face guard restores the sharp H^s consistency threshold to s>0

**Date:** 2026-10-24. Exact conditional mature mathematical result on the *unchanged retained DTC0a helper*, not a physical field equation, GR covariance claim, historical masked RMS result, or owner certification.

## 0. Prior project work / currentness before research

- **PRF11 R23:** continuum fixed-flat tensor TT/Lie commutator bound and explicit high-frequency source aliasing under centered collocation; original whole-grid failure witnesses.
- **REC10 ROT20:** independent PASS_WITH_EXACT_DEALIASING_GUARD for R23, including O(h²) when input bandwidth is FIXED and no frequencies fold. Its own source material was not claimed to have been copied into this proof.
- **PRF11 R24:** exact mesoscopic no-fold estimates for K_N=o(N) and a growing-frequency NO-FOLD witness with k=(m,0,m), N=8m+1 whose unnormalized error remains nonzero.
- **PRF11 R25:** undealiased whole-cube H^s->L² bound O(N^{-min(s,2)}+N^{1-s}), giving the regularity threshold s>1; R25 sharp at alpha=0.
- **PRF11 R26:** closed exceptional alpha=1/6, gave sharp whole-cube fixed-alpha rates for all alpha>=0 and a TWO-witness tuning no-go at s=1, independent of any SOURCE-NATIVE de-alias support guard. Full GitHub R26 report and six source-native code controls read before this rotation; Slack parent had no independent REC10 review yet.
- **INT8 ROT018–021:** exact distinct fixed-universal-shear-equivariant E-filter minimax (fullband L² and Sobolev weighted) and original source-stencil/TT alias checks. This theorem is about a SOURCE-C2-specific input-frequency passband, not universal shear covariance.
- **Geeky-S11 ROT004–005:** even-grid MATCHED centered-symbol TT projector Nyquist kernel/coercivity; R27 is ODD N and retains the historic RAW Fourier-k projector.
- **MT13 24 Oct:** exact metric-local *family* E_g for flat affine shears; distinct from this fixed Euclidean source-harmonic guard. **M13 ROT30:** five-mask sharp true-TT bandwidth threshold for RMS identifiability; unrelated data-target.
- **XH-S4 ROT020–025:** moving York, metric curvature, off-shell Noether/Duhamel and hyperbolicity/source-level safeguards; no lift from flat projector to gravity.
- **KN11/NC:** custody and independent science are not automatically elevated to owner science or EXEC. KN11’s 24 Oct BW ingest concerns a specified public comparison slice, not proof that R27 was ingested.

**NEW problem after subtraction:** Can one remove the *exact source-supported alias obstruction* with a passband discarding only O(N²) of N³ modes, without artificially assuming K_N=o(N)? If yes, is the resulting H^s threshold exactly s>0, and can scalar alpha_N tuning ever repair the remaining s=0 no-fold stencil error?

## 1. Typed operator and source symbols

For odd N>=17, h=2pi/N, M=(N-1)/2 and B_N={k∈Z³: |k_i|<=M}, identify full N³ source arrays with their trigonometric Fourier interpolants in B_N using normalized Parseval. Inputs are real symmetric rank-two covariant tensors; complex Fourier extensions used in calculations. Let

  ||F||_(H^s)² = sum_(k∈B_N) (1+|k|²)^s ||Fhat(k)||_F².

For k!=0, raw-k orthogonal TT multiplier is

  p(k)=I-kk^T/|k|²,
  Pi_k(H)=pHp-(p/2) tr(pH).

At k=0 use tracefree projection. P denotes continuum Fourier TT, P_N the retained source raw-k grid TT. NOT even-grid centered-symbol P_delta, NOT curved York P_g. Source Lie derivative:

  (L_C F)_ij=C^l partial_l F_ij + F_lj partial_i C^l+ F_il partial_j C^l.

L_(C,h) uses central first differences D_h symbol i sin(k_j h)/h, pointwise multiplication and FFT index wrap. E_(alpha,h)=I+alpha*h² Delta_h has symbol e_alpha(k)=1-4alpha sum_i sin²(k_i h/2), and commutes with source P_N. Fix alpha>=0 INDEPENDENT of N except in the separate all-alpha negative result. Exact source field:

  C2=(0.04 cos z,0,0.04 sin x).

Its ONLY Fourier support is Q={+e_x,-e_x,+e_z,-e_z}. Define H_N as the input Hilbert space on full B_N. The *continuum reference operator* is C=[P,L_C2] on trig inputs; continuum OUTPUT is kept in full continuum L², including source-generated modes outside B_N (not falsely resampled to hide alias).

## 2. The maximal alias-free passband for this particular source

Define an orthogonal Fourier-face projection G_N, acting on INPUT tensors by multiplication by

  g_N(k)=1_{|k_x|<=M-1 and |k_z|<=M-1},

with k_y UNRESTRICTED (|k_y|<=M). Since q∈Q shifts precisely x or z by one unit, the following statement is EXACT:

  k+q∈B_N for EVERY q∈Q  iff  g_N(k)=1.     (2.1)

Thus G_N is the unique maximal diagonal 0/1 passband guaranteeing that NO input source coefficient folds from any of the four retained source shifts. It is SOURCE-RELATIVE; not an all-fields or quadratic-Galerkin 2/3 rule. The retained count and discarded count are exactly

  kept = N(N-2)^2,
  removed = N³-N(N-2)^2 = 4N²-4N,
  removed_fraction=4/N-4/N²,
  kept_fraction=(1-2/N)².                           (2.2)

For example N=101: kept 96.07881580237232%, removed 3.92118419762768%; N=41: kept 90.481856% (calculated formula), removed 9.518144% (use exact formula if quoting). The asymptotically discarded proportion tends to zero even though EVERY source-relevant wrap is eliminated.

Define the *guarded source approximation on ALL original grid inputs*:

  A_(N,alpha)^guard = J_N [P_N,L_(C2,h) E_(alpha,h)] J_N^-1 G_N.   (2.3)

The difference against the original full continuum reference, WITHOUT changing its target, is

  R_(N,alpha)^guard = A_(N,alpha)^guard - [P,L_C2] |_(H_N).          (2.4)

Therefore if a Fourier mode is discarded by G_N, its numerical response is zero while its true continuum commutator need not be. This important truncation error is INCLUDED. G_N is applied to the input, not to the continuum target, and is not slipped past L_C2 as though it commuted with it.

## 3. Exact upper bound — full grid, shrinking boundary portion only

**Theorem R27.A.** For every fixed alpha>=0 and s>=0, there exists C_s,alpha,C2<infty independent of odd N such that

  ||R_(N,alpha)^guard||_(H^s(B_N)->L²(T³))
      <= C_s,alpha,C2 [ N^-min(s,2) + N^-s ]
      = O(N^-min(s,2)).                                  (3.1)

**Proof.** Split source input with orthogonal Fourier projections I=G_N+(I-G_N):

  R^guard F = [A^source_N - C] G_N F - C (I-G_N)F.

(a) Every k in the support of G_N and every q in Q have n=k+q in the grid B_N, so there is ZERO FFT-fold discrepancy. The modewise nonfold source estimate proved by PRF11 R24/R25 (not reattributed here) reads

  ||([P_N,L_(C2,h) E_alpha] - [P,L_C2])_(k,q)||
      <= c(alpha,C2) h² (1+|k|²),                       (3.2)

which uses the order-zero angular cancellation Pi_(k+q)-Pi_k=O(|q|/|k|), rather than the larger unprojected finite difference term O(h²|k|³). Since q is one of FOUR fixed frequency shifts, its Fourier translation is ℓ²-isometric on the nofold subset. Summing gives

  ||[A_N^source-C]G_N||_(H^s->L²)
      <= c h² sup_(k∈B_N)(1+|k|²)^(1-s/2)
      = O(N^-min(s,2)).                                 (3.3)

(b) If k is discarded then |k_x|=M or |k_z|=M, hence |k|>=M~N/2. The continuum commutator has already been shown in PRF11 R23 to be order zero:

  ||[P,L_C2]||_(L²->L²) <=20 D(C2) <infty.              (3.4)

Consequently

  ||C(I-G_N)||_(H^s->L²)
       <=20D(C2) (1+M²)^(-s/2) = O(N^-s).              (3.5)

Triangle proves (3.1), uniformly in arbitrarily high interior frequencies. The bound is for fixed alpha; its constant is not uniform when |alpha| grows without bound. QED.

**Positive meaning:** any s>0 suffices for FULL ORIGINAL INPUT CUBE consistency with the unchanged continuum operator. No hard K_N=o(N), no two-thirds bandwidth restriction, and no concealed comparison to a truncated continuum target are needed. This is a direct source-specific corollary of mature spectral truncation and smoothness-weighted Fourier approximation.

## 4. The NO-FOLD growing-band lower — s=0 is still impossible

Take N=8m+1 (m>=2), h=2pi/N, k=(m,0,m), n=k+e_x=(m+1,0,m). All q∈Q give in-band modes; G_N F=F for real exactly TT input

  F_(N,m)=sqrt(2) cos(mx+mz) H,
  H=(v v^T-e_y e_y^T)/sqrt(2), v=(-1,0,1)/sqrt(2).     (4.1)

It has L² norm 1 and ||F||_H^s=(1+2m²)^(s/2). Write

  S=e_x tensor (H e_z)+(H e_z) tensor e_x,
  U_m=(Pi_n-I)H,
  V_m=Pi_n S-S,
  d_m=sin(mh)/h, d_1=sin(h)/h,
  e_m(alpha)=1-8alpha sin²(mh/2).

The selected true output Fourier pair ±n (no folding anywhere) gives the EXACT discrepancy

  J_(N,m)(alpha)=0.02 || e_m(alpha)[d_m U_m+d_1 V_m]
                             -[m U_m+V_m] ||_F.        (4.2)

The other source Fourier term ±e_z does not overlap ±n, so Parseval gives

  ||R^guard_(N,alpha)||_(H^s->L²)
      >=J_(N,m)(alpha)/(1+2m²)^(s/2).                   (4.3)

As m→infty, h m→pi/4 and rho=sin(pi/4)/(pi/4)=2sqrt(2)/pi<1. The source E filter symbol tends to e_alpha=1-(4-2sqrt(2))alpha. The following *exact 3x3 matrices* are independently obtained by expanding raw-k Pi_n in powers of 1/m:

  A=lim m U_m=diag(-sqrt(2)/4,0,+sqrt(2)/4),
  B=lim V_m=(sqrt(2)/8)*[[3,0,-1],[0,2,0],[-1,0,-1]].

Their Frobenius Gram constants are exact:

  ||A||²=1/4, ||B||²=1/2, <A,B>=-1/4.                 (4.4)

Hence for any fixed alpha∈R the selected limit is

  J_infty(alpha)=.02|| (e_alpha*rho-1)A+(e_alpha-1)B ||_F.   (4.5)

**There is no alpha that makes this zero.** A and B are linearly independent (B has nonzero (y,y) component while A has zero), so the two coefficients would both have to be zero, requiring e_alpha=1 and e_alpha*rho=1, impossible since rho<1. For alpha=0 this recovers the earlier R24 exact 0.0009968368384289; here the NEW point is that it is valid with G_N and is positive for EVERY fixed alpha (even negative).

For each fixed alpha and 0<=s<=2, (4.3)-(4.5) yield the positive lower exponent Omega_alpha(N^-s). For s>=2, **R26's fixed nofold low-mode witness** k=(2,0,2), n=(3,0,2) lies within G_N for sufficiently large N; its independently SymPy-verified h² coefficient squared is

  (410112 alpha²-1056 alpha+727)/24336,

strictly positive for every real alpha (R26's full proof); therefore the lower exponent Omega_alpha(N^-2) holds. Combine with R27.A upper:

**Theorem R27.B (sharp source-relative guarded Sobolev rate).**
For every FIXED alpha>=0 and s>=0, odd N→infty,

  ||R_(N,alpha)^guard||_(H^s(B_N)->L²)
     = Theta_alpha,s,C2(N^-min(s,2)).                   (4.6)

Thus convergence holds **iff s>0**. This is an operator-approximation theorem, not a vanishing-continuum-TT-leakage theorem; C itself need not tend to zero.

## 5. Stronger tuning NONMAP at L²: no scalar alpha_N can fix source stencil dispersion

The high-band exact pair (4.2) is AFFINE in the real filter symbol e=e_m(alpha), and since sin(mh/2)!=0, optimizing over alpha∈R is exactly optimizing over e∈R.

For each N=8m+1, define X_m=d_m U_m+d_1 V_m, Y_m=m U_m+V_m. Then **at finite N**

  min_(alpha∈R) J_(N,m)(alpha)
    =.02 sqrt(||Y_m||_F² - <X_m,Y_m>_F²/||X_m||_F²),   (5.1)

with optimum e=<X_m,Y_m>/||X_m||², provided X_m!=0 (holds for all sufficiently large m). In the limit X_m→rho A+B, Y_m→A+B. From exact Gram (4.4):

  ||rho A+B||²=[1+(1-rho)²]/4,
  <rho A+B,A+B>=1/4,
  ||A+B||²=1/4.

Therefore

  lim_(m→infty) min_alpha J_(8m+1,m)(alpha)
    = 0.01(1-rho)/sqrt(1+(1-rho)²)
    = 0.0009919207435624083... >0.                (5.2)

For arbitrary odd N, replace m by floor((N-1)/8), which obeys m/N→1/8 and remains well inside G_N; the same finite-N argument and limit apply. Thus the uniform-in-alpha conclusion holds on ALL sufficiently large odd grids:

**Theorem R27.C:**

  liminf_(N odd→infty) inf_(alpha∈R)
    ||R_(N,alpha)^guard||_(L²(B_N)->L²(T³))
        >= 0.0009919207435624083... >0.               (5.3)

This no-go is for the singular one-scalar source E_alpha filtering family, not general de-aliasing or modified spectral differentiation. Even after perfect SOURCE-RELATIVE edge guarding, fixed-mesh-frequency modified-wavenumber dispersion remains an L² operator obstruction; varying alpha_N cannot erase its two independent tensor geometry components. This is a classical source specialization, not a novel theorem family.

## 6. Executed independent controls

**Original unmodified retained source:** `deepseek_python_20260627_a87249.py` independently SHA256-verified before import: `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`.

Reproduction source: `prf11_r27_guarded_source_tt.py`; output `prf11_r27_results.json`, executed on actual untouched helper with `generate_smooth_fields`, `apply_T` and `apply_P_TT` (not a substitute TT implementation). Six native full-grid checks N=17,25,33 for alpha=0,.05,.2,1/6; source vs independently calculated analytic selected Fourier coefficient agrees to maximum relative error **2.33e-15**. Source TT input projection/face-guard preserved to numerical rounding. Counts verified for every native N: removed 4N²-4N, retained N(N-2)². A source TT k=(M,0,r) is explicitly annihilated by G_N with numerical relative residual <1e-13; this is the R26 folded boundary type, here removed by a conscious passband contract.

Independent SymPy matrix check (exact radicals) verified ALL three Gram identities (4.4), the minimizing quadratic and exact floor (5.2). Separate 3x3 high-band calculations for m=2,4,...,512 and alpha=0,.05,1/6,.2 converged to J_infty:

| alpha | J_infty | J_N at N=4097 |
|---:|---:|---:|
| 0 | 0.0009968368384289 | 0.0009953887194316 |
| .05 | 0.0011062648558968 | 0.0011036276000347 |
| 1/6 | 0.0021109815510264 | 0.0021070560182646 |
| .2 | 0.0024643260913021 | 0.0024601394329680 |

At N=17,33,65,129,257,513,1025,2049,4097,8193, **finite-N** 1D minimization over all real scalar alpha (5.1) produced minima tending respectively from 0.000455299 toward 0.000991086, analytic limit 0.0009919207435624. Entries N>33 are analytic **3×3 Fourier computations**, NOT native N³ source runtime.

First attempt in new reproducer had an incorrect broadcast shape for the guard-count test; the test FAILED before any result was accepted. Corrected to a full (N,N,N) Fourier mask and fixed frequency rounding with `np.rint`; all complete validations then PASS. This is a documented script setup correction, not model-data alteration. Source helper untouched.

## 7. Mature-host subtractive literature

- Trefethen, *Spectral Methods in MATLAB*, SIAM 2000, Ch.3 (Periodic Grids: The DFT and FFT), DOI 10.1137/1.9780898719598.ch3 and Ch.4 (Smoothness and Spectral Accuracy), DOI 10.1137/1.9780898719598.ch4. Primary SIAM publisher page confirms Fourier regularity/alias decay, NOT exact source-C2 constants.
- Carnegie Mellon University, course notes on Fourier spectral methods, §4.1.6 “De-aliasing technique”: standard 3/2 zero padding; current specialized Q={±e_x,±e_z} faces are not the standard universal quadratic 3/2 theorem. Source: https://www.math.cmu.edu/~franzisw/files/NotesMCFD.pdf (author attribution in the web result not verified, so cite as CMU mathematical lecture notes rather than inventor proof).
- Iovieno, Cavazzoni, Tordella, “A new technique for a parallel dealiased pseudospectral Navier–Stokes code,” *Computer Physics Communications* 141 (2001) 365–374, DOI 10.1016/S0010-4655(01)00433-7: conventional full quadratic nonlinearity de-aliasing; separate numerical problem.
- Prior PRF11 R23–R26, REC10 fixed-mode referee, and INT8 discrete tensor source/operator families are the immediate owners for estimates used above. No mathematical priority novelty or physical sensor/wave interpretation is established by the targeted bibliography.

## 8. Scientific status and STOP guards

**Earned:** exact maximal source-supported zero-fold input Fourier passband; discard precisely 4N²-4N of N³ source modes; full-H_N *untruncated continuum target* convergence sharp iff s>0 at fixed alpha; an independent positive L² floor under arbitrary scalar alpha_N even after guarding; native helper FFT, exact SymPy and clean numerical controls.

**Not earned:** zero TT leakage itself; general source generators with unknown/high spectra; arbitrary tensor or nonlocal filters; exact v0.3.1 production bit identity; original historical source masked K_A plateau; even-grid P_delta; variable metric/York naturality; empirical physics, GR, PBH/BBN, NCDG J3/K or a canon upgrade. The guard G_N is source-specific and is NOT an integral-SL3(Z)-shear-natural family. No REC10 independent referee/owner acceptance or BW ingest has been established yet.

`NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_NEW_TASK / INDEPENDENT_REFEREE_PENDING / BW_PENDING`.
