---
artifact_id: IW_PRF11_R27_ALL_SOBOLEV_UNIFORM_FILTER_TUNING_SHARP_RATE_001_20261024
created_at: 2026-10-24
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_10 / PRF11
problem_id: P3_DTC0A_Q39_ALL_S_OPTIMIZED_SCALAR_FILTER_SHARP_COLLOCATION_RATE
function: FOUNDATION_FIRST / CURRENTNESS_FIRST / OTHERS_FIRST / PRIOR_ART_SUBTRACTION / FALSIFIER
exposure: PUBLIC_SAFE
document_type: EXACT_SOURCE_TYPED_CLASSICAL_THEOREM_WITH_EXECUTED_REPRODUCTION
status: PROOF_AND_SYMPY_AND_SOURCE_HELPER_TEST_PASS / INDEPENDENT_REFEREE_PENDING
source_helper: deepseek_python_20260627_a87249.py
source_helper_sha256: 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_J3_K_INVARIANCE / NO_PRODUCTION_RUNTIME_BIT_IDENTITY
cross_surface_sync: GITHUB_PENDING_BW_INGEST
---

# PRF11 R27 — Globally optimized scalar filter cannot beat the sharp all-Sobolev collocation error rate

**Date:** 24 October 2026. **Scope:** original *retained* DTC0a helper's flat, raw-wavevector TT projection, covariant rank-two Lie stencil, fixed finite Fourier generator `C2`, and scalar 7-point filter. Classical source-typed Fourier analysis, **not** a physical NCDG or gravitational result.

## 0. Currentness, priority subtraction and actual new delta

Before computing, read current GitHub tree and latest bounded `#iw-dispatch`. The first relevant currentness correction was that R16 custody was RESTORED to GitHub on 23 Oct, and PRF11 R17–R26 already existed. This is R27, *not* another R17. R26 parent dispatch had no scientific reply visible during initial currentness check; absence of a reply does not imply scientific rejection.

**Results owned by OTHER cells:**
- **INT8 ROT021 (24 Oct):** exact attained Sobolev-weighted minimax approximation of the *source filter itself* by SHEAR-EQUIVARIANT scalar convolution, rate `Theta(N^-min(s,2))`. This is a different operator/problem from the current *Lie/TT commutator discrete-to-continuum error*. No claim of transferring INT8's optimal filter or priority: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/int8/2026-10-24/iw_int8_rot021_sharp_sobolev_weighted_equivariant_filter_minimax_001.md
- **Geeky-S11 ROT004:** correct six-dimensional matched-centered-symbol TT-preservation kernel on even grids, with exceptional checkerboard modes. Its `P_delta` is **not** the historical raw-k `P_TT`. https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s11/2026-10-24/geeky_s11_rot004_even_nyquist_tt_kernel_and_finite_probe_classification_001.md
- **M13 ROT029** and **REC10 ROT023:** five-mask identifiability/minimax and exact historical alpha/mask biases, respectively; not the same full-output Fourier operator norm. XH-S4 retains naturality/curved-metric York questions; KN11 independently ingests cited source objects but source delivery is not canon/EXEC.
- **PRF11 R25** supplied the UNIFORM positive upper bound for each *fixed* `alpha≥0`: `||R_(N,alpha)||_(H^s→L²) ≤ C_{s,C,alpha}[N^-min(s,2)+N^(1-s)]`. **PRF11 R26** supplied exact high-frequency alias certificates and positive minimax floor for ALL alpha_N at *critical s=1*, plus a low-frequency second-order coefficient known to be nonzero for every *fixed* alpha. The present report REUSES their tensors, formulae and helper; its **only scientific delta** is taking the infimum over **arbitrary grid-dependent alpha_N** in the **entire H^s scale**, with fully uniform finite-N bounds and sharp rates.
  - https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-23/IW_PRF11_R25_SHARP_SOBOLEV_THRESHOLD_FULL_COLLOCATION_TT_COMMUTATOR_AND_SOURCE_ALIAS_WITNESS_001_20261023.md
  - https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-24/IW_PRF11_R26_ALL_FILTER_CRITICAL_SOBOLEV_ALIAS_NONMAP_001_20261024.md

**Precise gap:** R26 expressly asserted all-alpha_N uniformity at `s=1` only, and all-s sharp rates for *fixed* alpha only. Does optimization over `alpha_N∈R` for every N change the best achievable rate for `s≠1`? A superficial reading of R26's low-mode *fixed-alpha* expansion could falsely suggest an `alpha_N` depending on N might cancel the `N^-2` term for `s≥3`. We prove it cannot.

## 1. Exact mathematical carrier (same as R26, no hidden change)

Let `T³=(R/2πZ)³`, `N` odd and large, `h=2π/N`, `M=(N-1)/2`, `B_N={k∈Z³:|k_j|≤M}`. Grid arrays are identified isometrically with trigonometric interpolants in `B_N`; Fourier coefficients use normalized Parseval. For symmetric rank-two covariant tensor `F`, use the *raw wavevector*, orthogonal Fourier TT projector

`Π_k F = p(k)F p(k) - (1/2) p(k)tr[p(k)F]`, `p(k)=I-kk^T/|k|²` for `k≠0`, and the tracefree projector at zero. The original `P_N` is NOT the centered-symbol projector used by Geeky-S11 ROT004.

Let `L_C F` be the rank-two covariant Lie derivative with component expression `C^l∂_l F_ij+F_lj∂_i C^l+F_il∂_j C^l`. `L_(C,h)` replaces all derivatives by centered `D_h`, with Fourier symbol `i sin(kh)/h` and source-grid pointwise multiplication/FFT folding. The filter is `E_(alpha,h)=I+alpha*h²*Delta_h`, symbol `1-4alpha sum_j sin²(k_j h/2)`, for arbitrary REAL alpha; E commutes with the flat raw-k projector. Fix the exact retained original source generator

`C2=(0.04 cos z, 0, 0.04 sin x)`.

Define the ERROR on input `F∈H^s(B_N)` and output in FULL continuum `L²(T³)`:

`R_(N,alpha)=J_N[P_N,L_(C2,h)E_(alpha,h)]J_N^-1 - [P,L_C2]`.

**Crucial output typing:** the discrete term is embedded on B_N, but the unwrapped continuum term retains every true mode k+q even if outside B_N. Never resample the continuum output onto the original grid before measuring this error. Normalize

`||F||_(H^s)^2=sum_{k∈B_N}(1+|k|²)^s ||Fhat(k)||_F²`, all fixed s≥0.

Let `D_N(s)=inf_{alpha∈R} ||R_(N,alpha)||_(H^s(B_N)→L²)`. The infimum is mathematical and does not assert that negative or unbounded alpha is a physically legal filter.

## 2. Main R27 theorem — optimal alpha_N sharp rate for EVERY s≥0

**Theorem R27.A.** For the above source carrier and each fixed real `s≥0`, there exist `0<c_s≤C_s<∞`, independent of odd N, such that for sufficiently large N:

`c_s [N^(1-s)+N^-2] ≤ D_N(s) ≤ C_s [N^(1-s)+N^-2]`.   **(2.1)**

Equivalently,

`inf_(alpha_N∈R) ||R_(N,alpha_N)||_(H^s→L²) = Θ_s(N^(1-s)+N^-2)`. **(2.2)**

Therefore: `0≤s<1` diverges as `N^(1-s)`; `s=1` has an order-one positive floor; `1<s<3` converges exactly as `N^-(s-1)`; `s≥3` converges exactly as `N^-2`. The conclusion includes arbitrary real `alpha_N` changing with N, even unbounded sequences. This concerns BEST RATE, not a closed expression for the minimizing full-operator alpha at finite N.

### 2.1. Upper estimate: a SINGLE candidate already achieves the claimed rate

Since the infimum includes `alpha=0`, and PRF11 R25 already established for that fixed admissible value

`||R_(N,0)||_(H^s→L²) ≤ A_s [N^-min(s,2)+N^(1-s)]`, (2.3)

we have `D_N(s)` bounded above by (2.3). For any s≥0, `N^-min(s,2) ≤ N^(1-s)+N^-2` for N≥1 (if s≤2, `N^-s≤N^(1-s)`; if s≥2, `N^-min(s,2)=N^-2`). This proves the upper half. **R25 owns the upper theorem; R27 does not reattribute it.**

### 2.2. Uniform HIGH-frequency lower at general Sobolev order

R26 constructed two exact real, normalized raw-TT Fourier waves on the SAME grid: input k=(M,0,r_A) with `r_A=nearest_integer(N/4)` and input k=(M,0,r_B) with `r_B=nearest_integer(N/6)`. The selected C2_z sine-source Fourier output k+e_x aliases from M+1 to -M. The continuum output at that folded index is ZERO, so the selected discrete output is an exact error lower bound. For either probe `r`, define

`H(k)=[v v^T−e_y e_y^T]/sqrt(2)`, `v=(-r,0,M)/sqrt(M²+r²)` (input TT),

`S=e_x⊗(H e_z)+(H e_z)⊗e_x`, `U=Π_(-M,0,r)H-H`, `V=Π_(-M,0,r)S-S`,

`a_(N,r)=4[sin²(Mh/2)+sin²(rh/2)]`, and

`w_(N,r,s)=0.02 ||[sin(rh)/h]U+[sin(h)/h]V||_F /(1+M²+r²)^(s/2)`.

For **every real alpha and every odd N** with valid carrier, Parseval gives

`||R_(N,alpha)||_(H^s→L²) ≥ w_(N,r,s)*|1-a_(N,r)alpha|`. (2.4)

For the two probes write `A_N=w_(N,r_A,s)`, `B_N=w_(N,r_B,s)`, `a_N=a_(N,r_A)`, `b_N=a_(N,r_B)`. For sufficiently large N, `a_N>b_N>0`, and `A_N,B_N>0`. Therefore for every alpha:

`||R_(N,alpha)|| ≥ max(A_N|1-a_N alpha|, B_N|1-b_N alpha|)`.

The EXACT minimax of these two absolute affine functions (not a heuristic least-squares fit) is

`H_N(s) := inf_alpha max(...) = A_N B_N (a_N-b_N)/(a_N A_N+b_N B_N)>0`, (2.5)

attained at `alpha_high=(A_N+B_N)/(a_N A_N+b_N B_N)`. The formula is valid for arbitrary real alpha before taking N→∞.

For each fixed s, the Sobolev scaling identity is EXACT:

`w_(N,r,s)=w_(N,r,1)*(1+M²+r²)^((1-s)/2)`.

R26's source-exact `s=1` limits were

`A_1=0.004174983337015688...`, `B_1=0.002993670211551709...`.

Since `|k_A|/N→sqrt(5)/4`, `|k_B|/N→sqrt(10)/6`, and `a_N→6`, `b_N→5`, define

`A_s=A_1 [sqrt(5)/4]^(1-s)>0`,

`B_s=B_1 [sqrt(10)/6]^(1-s)>0`,

`H_s := A_s B_s/(6 A_s+5 B_s)>0`.

Then

`N^(s-1) H_N(s) → H_s>0`. **(2.6)**

This proves, UNIFORMLY over all alpha_N, the non-cancellable high-frequency rate `Omega_s(N^(1-s))`. For `s=1`, (2.6) recovers R26's 0.00031232057654915964; the new content is the correct *entire Sobolev scaling*.

### 2.3. Uniform LOW-frequency second-order floor: noncollinearity defeats alpha_N tuning

The R26 source low wave `k=(2,0,2)`, `q=e_x`, `n=(3,0,2)` has no aliasing for sufficiently large odd N. With fixed normalized TT polarization `H0=(u u^T−e_y e_y^T)/sqrt(2)`, `u=(-1,0,1)/sqrt(2)`, define `S0=e_x⊗(H0 e_z)+(H0 e_z)⊗e_x`, `U=Π_n H0-H0`, `V=Π_n S0−S0`. The input has exact `||F||_(H^s)=3^s`.

The selected REAL Fourier-pair error (R26 exact source identity) is

`J_N(alpha)=0.02 || e_(alpha,h)(k) [δ_h(2)U+δ_h(1)V]−[2U+V]||_F`,

`e_(alpha,h)(k)=1−8alpha sin²(h)`, `δ_h(j)=sin(jh)/h`.

Put

`v_(0,h)=[δ_h(2)−2]U+[δ_h(1)−1]V`,

`v_(1,h)=−8sin²(h)[δ_h(2)U+δ_h(1)V]`.

The EXACT expression is `J_N(alpha)=0.02 ||v_(0,h)+alpha*v_(1,h)||`. Minimizing the squared Euclidean/Frobenius distance from a vector to the line spanned by another vector gives for each finite N (v1 nonzero)

`min_(alpha∈R) J_N(alpha) =0.02 sqrt(||v0||²−<v0,v1>²/||v1||²)`  **(2.7)**

and `alpha_low_opt=−<v0,v1>/||v1||²`. **No boundedness assumption on the optimizer is used**. The vectors are exactly source-defined 3×3 matrices.

Since `δ_h(2)=2−(4/3)h²+O(h⁴)`, `δ_h(1)=1−h²/6+O(h⁴)`, and `sin² h=h²+O(h⁴)`, as h→0

`v0/h²→X:=−(4/3)U−(1/6)V`,

`v1/h²→Y:=−8(2U+V)`.

R26's exact, independently checked SymPy algebra yielded

`||X+alpha Y||²=(410112 alpha²−1056 alpha+727)/24336`, (2.8)

with **strictly positive** global real minimum at `alpha=11/8544`:

`min_(alpha∈R)||X+alpha Y||²=85/2848>0`. (2.9)

In particular X and Y are linearly INDEPENDENT in the Frobenius inner-product space, so the squared-distance-to-span functional in (2.7), after division by h⁴, converges to the positive value `85/2848` by continuity of orthogonal projection onto a nonzero one-dimensional span. This is the crucial UNIFORMITY argument missing in R26's *fixed-alpha* Taylor statement:

`lim_(N odd→∞) min_(alpha∈R) [J_N(alpha)/h²] = 0.02 sqrt(85/2848)
                                                   =0.0034551703644235855...>0`. (2.10)

Thus for every fixed s≥0, uniformly over all alpha∈R,

`||R_(N,alpha)||_(H^s→L²) ≥ L_N(s):=min_alpha J_N(alpha)/3^s`  **(2.11)**

and the exactly normalized limit is

`lim_(N odd→∞) N² L_N(s) = [0.02(2pi)²/3^s] sqrt(85/2848)
                                     = 0.13640465854091416.../3^s >0`. (2.12)

This proves an alpha-uniform `Omega_s(N^-2)` low-frequency barrier, including choices alpha_N diverging with N. A scalar multiplier can shrink a component of the low-mode error but cannot make the stencil-error and filter-correction tensor directions simultaneously collinear. This is an exact classical finite-dimensional best-approximation obstruction.

### 2.4. Combine the two independent floor mechanisms

Both (2.5) and (2.11) hold for each same alpha, so for every real alpha,

`||R_(N,alpha)||_(H^s→L²) ≥ max{H_N(s),L_N(s)}`.

The RHS is independent of alpha; hence the identical lower bound holds for `D_N(s)=inf_alpha||R||`. Since `N^(s-1)H_N(s)→H_s>0` and `N² L_N(s)→L_s>0`, we get positive constants and

`D_N(s) ≥ (1/2)min(c_H,c_L)[N^(1-s)+N^-2]`

for all sufficiently large odd N. Combine with the R25 upper (2.3); Theorem R27.A follows. QED.

**Caution on optimal parameters:** `alpha_high_opt~0.179` and `alpha_low_opt→11/8544≈0.00128745` minimize DIFFERENT projected witness errors. They are **not** alleged to be global optimizers of the full operator norm. The different choices reinforce why a single scalar cannot remove both errors. The theorem establishes the optimal RATE, not a complete finite-N operator-norm minimax solution.

## 3. Executed source-native and exact-arithmetic falsification controls

The self-contained Python reproducer `prf11_r27_all_s_tuning_reproducer.py` and machine-readable `prf11_r27_numeric_results.json` were **ACTUALLY EXECUTED**. Reproducer includes *independent* 3×3 matrix construction, exact SymPy low-mode polynomial verification, finite high-pair minimax checks against an independent 100001-point scalar grid, and five FULL N³ field/FFT runs against the unmodified retained helper (`apply_T`, `apply_P_TT`) at N17,19,31,41, with multiple alpha values (0,1/6,.05,.2,near the low-mode optimum).

The source helper's byte SHA256 check MATCHED `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`. All **five** independently computed native-vs-analytic Fourier *tensor* residuals agree with relative difference at most `1.191e−13`; normalized input TT projection errors at most `6.74e−16`. This is a stronger object check than only comparing scalar norms. The SymPy identity (2.8) and minimizer (2.9) are exact.

The code evaluated finite exact high/low certificates on N in {17,31,61,101,201,401,801,1601,3201} and s in {0,.5,1,1.5,2,2.5,3,4,5}: **81** cases. No N>41 whole-grid source-helper run is claimed; later N use only small 3×3 mode algebra.

For s=1 the high-frequency lower at N3201 is 0.0003109249993, approaching the R26 limit 0.00031232057655. For the entire s range the rescaled high witnesses N^(s-1)H_N(s) approach the strictly positive predicted constants H_s. The rescaled low witnesses N²L_N(s) approach 0.13640465854/3^s. Example theoretical limits:

| s | H_s (high scaled) | L_s (low scaled) |
|---:|---:|---:|
| 0 | 0.00016820558324 | 0.13640465854 |
| 1 | 0.00031232057655 | 0.04546821951 |
| 2 | 0.00057943959895 | 0.01515607317 |
| 3 | 0.00107413322998 | 0.00505202439 |
| 4 | 0.00198950983185 | 0.00168400813 |
| 5 | 0.00368186693127 | 0.00056133604 |

Interpret these columns with DIFFERENT N normalizations; they are NOT competing values of the same operator norm. The high mechanism scales `N^(1-s)`, the low mechanism scales `N^-2`.

**Independent control of script provenance:** the ZIP bundle contains report, reproducer, machine-readable results, README, immutable retained helper, and SHA-256 manifest. Clean-room unzip, SHA verification and rerun with source helper present are required to claim reproducibility; code/package creation does not by itself prove consistency with an unavailable historical production runtime.

## 4. Mature host and scholarship (no mathematical priority claim)

- Lloyd N. Trefethen, *Spectral Methods in MATLAB*, SIAM 2000, Ch. 3 “Periodic Grids: The DFT and FFT”, DOI `10.1137/1.9780898719598.ch3`; publisher chapter page inspected for Fourier periodic DFT/FFT basis. Ch. 4 “Smoothness and Spectral Accuracy”, DOI `10.1137/1.9780898719598.ch4`; original publisher chapter abstract and book excerpt independently confirm aliasing and regularity-driven spectral accuracy. Neither source presents the exact source-C2 tensor constants or claims physical NCDG consequences.
  - https://epubs.siam.org/doi/10.1137/1.9780898719598.ch3
  - https://epubs.siam.org/doi/10.1137/1.9780898719598.ch4
- PRF11 R25–R26 mathematical host combines Fourier-collocation aliasing, modified wave numbers, orthogonal TT projection algebra and elementary two-function Chebyshev minimax. The added step in R27 is finite-N projection of a 3×3 source coefficient onto an alpha-generated line, so the lower estimate is UNIFORM in potentially unbounded alpha_N. The geometry is elementary best approximation, not a new general theorem.
- Canuto & Quarteroni (1982), “Error Estimates for Spectral and Pseudospectral Approximations of Hyperbolic Equations”, *SIAM Journal of Numerical Analysis* 19(3):629–642, DOI `10.1137/0719044`. R25 already scoped this as a mature regularity-dependent approximation host; it is not a verbatim theorem for flat TT rank-two C2 on this source helper.
- INT8 ROT021 is separately recognized as the first project-local exact weighted minimax of E_alpha to shear-equivariant **single-kernel scalar convolutions**. `BEST_APPROX(E, C_shear)` must not be conflated with `BEST_APPROX([P,L_h E], [P,L])`.

Literature examination was targeted, not an exhaustive mathematical novelty search. Mathematical originality and physical discovery are NOT claimed.

## 5. Negative knowledge, ownership and scientifically meaningful stop

**Established (and bounded):** `D_N(s)=Theta_s(N^(1-s)+N^-2)` with arbitrary real scalar-grid tuning alpha_N and the exact original C2, original raw-k TT projection, original centered covariant Lie operator, original E_alpha; both frequency mechanisms are certified by exact Fourier witnesses and native retained helper tests. In particular the H^1 obstruction from R26 was not the only uniform-tuning barrier.

**Not established:** closed form of true optimal alpha_N or exact leading constant of the full operator norm; any guarantee for frequency-dependent nonlocal/tensor filters, dealiased collocation, matched centered-symbol `P_delta` on even N, metric-dependent York `P_g`, a curved spacetime-covariant ∇/Box operator, any physical J3/K law, original byte-unavailable DTC0a production runtime, historical masked RMS or any physical detector. There is no owner acceptance, independent REC10 referee pass, BW ingestion or Moderator EXEC asserted.

**Return path:** GitHub exact public-safe report and optional reproducibility bundle; bounded nonblind cross-cell science dispatch. No cascading new owner tasks. `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE / GITHUB_PENDING_BW_INGEST`.
