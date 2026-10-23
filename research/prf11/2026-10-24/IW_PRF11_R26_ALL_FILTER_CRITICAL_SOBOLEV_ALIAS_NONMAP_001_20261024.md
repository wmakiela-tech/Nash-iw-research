---
artifact_id: IW_PRF11_R26_ALL_FILTER_CRITICAL_SOBOLEV_ALIAS_NONMAP_001_20261024
created_at: 2026-10-24
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_10 / PRF11
problem_id: P3_DTC0A_Q39_SHARP_FULL_BAND_SOBOLEV_COLLLOCATION_ALL_ALPHA_AND_TUNING_NO_GO
function: FOUNDATION_FIRST / SCIENCE_FIRST / CURRENTNESS_FIRST / OTHERS_FIRST / MATURE_HOST_SUBTRACTION / EXACT_NEGATIVE_KNOWLEDGE
document_type: EXACT_CONDITIONAL_THEOREM_AND_SOURCE_HELPER_REPRODUCTION
exposure: PUBLIC_SAFE
source_operator: deepseek_python_20260627_a87249.py
source_operator_sha256: 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801
status: MATHEMATICAL_PROOF_AND_INDEPENDENT_SYMBOLIC_NUMERIC_CHECK_PASS / EXTERNAL_REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_SOURCE_PRODUCTION_BIT_IDENTITY / NO_PHYSICAL_K_J3
owner_roles: XH-S4 asks Q39; INT8 source-grid operator; M13 original tests; REC10 referee; LT5 theory; KN11 BW; Moderator EXEC
cross_surface_sync: GITHUB_PENDING_BW_INGEST
---

# PRF11 R26 — All-filter sharp Sobolev threshold and a uniform tuning no-go for the source TT/collocation commutator

**24 October 2026.** Mathematical comparison theorem, not physical NCDG. Fixed flat 3-torus, ORIGINAL retained *raw-wavevector* Fourier TT projector, covariant symmetric rank-two Lie derivative implemented with centered differences, scalar 7-point grid filter E_alpha. Historical v0.3.1 production runtime is NOT available byte-for-byte; this report uses the *unchanged retained helper* identified above.

## 0. State of science / ownership / fresh subtraction before the R26 calculation

1. **PRF11 R25 (2026-10-23)** proved an H^s(B_N)->L² full-output operator-error ceiling for fixed source finite-band C and fixed alpha: O(N^{-min(s,2)}+N^{1-s}). With original C2 and alpha=0 it proved exact rates. Its folded TT example cancels *at alpha=1/6*, and R25 explicitly declined a matching lower claim there. **R26 addresses exactly that open exception and the general scalar-filter tuning question; it does not re-prove R25's upper estimate as new.** https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-23/IW_PRF11_R25_SHARP_SOBOLEV_THRESHOLD_FULL_COLLOCATION_TT_COMMUTATOR_AND_SOURCE_ALIAS_WITNESS_001_20261023.md
2. **REC10 ROT20** independently reviewed PRF11 R23 (`PASS_WITH_EXACT_DEALIASING_GUARD`) and proved fixed no-fold bandwidth O(h²). **PRF11 R24** already extended this to K_N=o(N), and R25 to the full regularity-weighted grid; none of these is credited to R26. https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-23/IW_PRF11_R24_MESOSCOPIC_TT_COMMUTATOR_CONSISTENCY_BANDWIDTH_SHARPNESS_NO_ALIAS_WITNESS_001_20261023.md
3. **INT8 ROT013–020** owns the original source-grid centered Leibniz/TT/aliasing controls and, most recently, the sharp operator-norm distance from fixed E_alpha to shear-invariant scalar convolution filters. This is a DIFFERENT filter naturality question, and R26 does not claim INT8's minimax value. https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/int8/2026-10-24/iw_int8_rot020_sharp_minimax_distance_to_shear_equivariant_dtc_filter_001.md
4. **Geeky-S11 ROT001–004** owns fixed-smooth TT leakage, odd-grid rigidity, and the even-grid matched-symbol P_delta Nyquist classification. R26 retains RAW-k P, only ODD grids, and estimates discrete-to-continuum ERROR, not absolute leakage. https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s11/2026-10-24/geeky_s11_rot004_even_nyquist_tt_kernel_and_finite_probe_classification_001.md
5. **M13 ROT026–029** owns the historical sparse pure-trace source plateau, mask/stencil asymptotic and mask minimax context. **REC10 ROT23** independently strengthened mask/alpha parameter-difference tests. They concern the retained historical source family and local RMS, not this whole-grid operator H^s norm. **XH-S4** owns moving metric York/curved geometric checks, not transferred to a flat raw-k P.
6. **PRF11 R16–R25** already exist and R16's previously blocked Github custody was restored. This note is **R26**, not a duplicate R17. Currentness read GitHub tree and dispatch through 24 October 2026; no owner/REC10 acceptance of R26 is implied.

**Question after host subtraction:** can the exceptional filter alpha=1/6, or even a tuned *grid-dependent* alpha_N, remove the critical-H¹ full-collocation alias obstruction for the original source field C2? Also, is the fixed-frequency second-order lower estimate nonzero for *all* fixed alpha? These are exact finite-grid operator questions; mature host is Fourier-collocation/aliasing, modified wavenumbers, and order-zero pseudodifferential commutators.

## 1. Precisely typed source model

Let T³=(R/2πZ)³ and H=L²(T³;Sym²(C³)), with normalized Haar measure and Frobenius tensor norms. For odd N≥13, h=2π/N, M=(N−1)/2, B_N={k∈Z³: |k_j|≤M}. Identify source arrays and trigonometric polynomials by the normalized-isometric Fourier interpolant J_N. Use periodic

`||F||_(H^s)^2 = sum_{k in B_N}(1+|k|²)^s ||Fhat(k)||_F²`, s≥0.

For k≠0, `p(k)=I−kk^T/|k|²` and the **raw-k** TT projector is

`Π_k H = p(k) H p(k) − [1/2]p(k) tr(p(k)H)`;

at k=0, use tracefree projection. The original retained Lie derivative of a covariant symmetric tensor is

`(L_C F)_ij = C^l ∂_l F_ij + F_lj ∂_i C^l + F_il ∂_j C^l`;

on the grid replace each derivative with centered `D_h` (symbol `i δ_h(k_j)=i sin(k_j h)/h`), multiply pointwise and **fold** FFT modes modulo N. The scalar filter is

`E_(alpha,h)=I+alpha h² Δ_h`, Fourier symbol `e_(alpha,h)(k)=1−4alpha sum_j sin²(k_j h/2)`.

It commutes with raw-k P. The source generator is the exact historical

`C2=(0.04 cos z,0,0.04 sin x)`.

Define operator error, comparing both outputs in the SAME continuum L², **without sampling continuum output back into B_N**:

`R_(N,alpha)=J_N[P_N,L_(C2,h) E_(alpha,h)]J_N^{-1} − [P,L_C2]` on H^s(B_N).

**NB**: This is NOT `[P_N,L_(C2,h)]` alone, NOT absolute Q L_C E P leakage, NOT a moving York P_g, NOT historical masked RMS. The continuum term can have real Fourier modes OUTSIDE B_N, kept as genuine continuum modes in the target L².

## 2. New R26 lower carrier: a complete continuum family of wrapped TT waves

For ANY odd N≥13, M=(N−1)/2, choose any integer `1≤r≤M−2`. Set

`k=(M,0,r)`, `n_true=k+e_x=(M+1,0,r)` (OUTSIDE B_N),

`n_fold=(-M,0,r)` (the DFT representative modulo N),

`v=(-r,0,M)/sqrt(M²+r²)`, `H(k)=[v v^T−e_y e_y^T]/sqrt(2)`,

`F_(N,r)(x)=sqrt(2)cos(Mx+r z) H(k)`.

Then `||F||_L²=1`, `Π_k H=H` and the real field is exactly raw-k TT on the source grid. Let

`S=e_x ⊗ (H e_z)+(H e_z)⊗e_x`,

`A=Π_(n_fold)H−H`, `B=Π_(n_fold)S−S`,

`e_(N,r)(alpha)=1−a_(N,r)alpha`, where

`a_(N,r)=4[sin²(Mh/2)+sin²(rh/2)]`.

Because `C2_z=0.04 sin x` has the Fourier coefficient `0.04/(2i)` at q=e_x, the folded *pair* of source discrete Fourier modes ±n_fold in `[P_N,L_(C2,h) E]F` has the EXACT L² norm

`L_(N,r)(alpha) = 0.02 |1−a_(N,r)alpha| * || δ_h(r)A+δ_h(1)B ||_F`.   (2.1)

The full continuum `[P,L_C2]F` has NO coefficient at ±n_fold: its source-generated Fourier modes are true ±k±e_x and ±k±e_z, and `n_true=(M+1,0,r)` is unwrapped. Therefore by Parseval the source operator error obeys the EXACT selective inequality

`||R_(N,alpha)||_(H¹→L²) >= w_(N,r) |1−a_(N,r)alpha|`,   (2.2)

where

`w_(N,r)=0.02 ||δ_h(r)A+δ_h(1)B||_F/sqrt(1+M²+r²)`.

No assumption about boundedness, sign, or N-independence of alpha is required for (2.2). The second historical generator mode `C2_x=0.04 cos z` shifts in z, so cannot cancel this selected Fourier pair. Real ±k normalizations and exact TT projection are included in the factor 0.02; this identity was independently checked against native full-grid helper outputs (section 6).

### Closed angular geometry

Write `d=(M²−r²)/(M²+r²)`. The incoming TT H polarizes along v and e_y. The outgoing transverse vector is `v'= (r,0,M)/sqrt(M²+r²)`. Their inner product equals d. Orthogonal TT projection obeys

`||Π_(n_fold) H||_F²=(1+d²)²/4`,

`||A||_F= ||(I−Π_(n_fold))H||_F = (1/2)sqrt[(1−d²)(3+d²)]`.  (2.3)

This identity uses only the 3×3 rank-two TT projector and its self-adjoint idempotence. It is independent of any source history, physics, or numerical regression.

## 3. Exact resolution of the alpha=1/6 exception

Take the subsequence `N=6m+1` and `r=m` (m≥2), so `M=3m`, `r/M→1/3`, `d→4/5`. Then by (2.3)

`||A||_F→3 sqrt(91)/50` and `δ_h(r)/N→sin(pi/3)/(2pi)`.

The filter symbol tends to `e_alpha(k)→1−5alpha`. Thus the exact leading folded norm is

`lim_(m→∞) L_(6m+1,m)(alpha)/N = [3 sqrt(273)/(10000 pi)] |1−5alpha|`.  (3.1)

For alpha=1/6 (precisely the filter value that kills the *old* R25 r/M=1/2 witness), (3.1) gives

`lim L_N/N = sqrt(273)/(20000 pi) = 0.0002629671231083755... >0`. (3.2)

Because `||F||_H¹=sqrt(1+10m²)` and `N/m→6`,

`liminf_(N=6m+1) ||R_(N,1/6)||_(H¹→L²)
  >= [sqrt(273)/(20000 pi)]*(6/sqrt(10))
  = 0.0004989450352586183... >0`.                      (3.3)

Consequently alpha=1/6 is **NOT** an operator-consistency exception at critical H¹. Its cancellation is directional: one special high-frequency ratio, not every alias direction. There is no claim of an exact operator norm or of a physical detector violation.

## 4. Stronger theorem: NO scalar alpha_N tuning can remove the H¹ alias floor

Use TWO exact source TT waves on EACH sufficiently large odd N:

`r_A(N)=nearest_integer(N/4)`, `r_B(N)=nearest_integer(N/6)`,

with both integer r in 1..M−2; let

`A_N=w_(N,r_A)`, `B_N=w_(N,r_B)`,

`a_N=a_(N,r_A)`, `b_N=a_(N,r_B)`.

For large N, `a_N>b_N>0`, A_N,B_N>0. Each probe individually supplies (2.2). Therefore for **any alpha∈R** (including arbitrary alpha=alpha_N depending on N and unbounded as N grows):

`||R_(N,alpha)||_(H¹→L²) >= max( A_N |1−a_N alpha|, B_N |1−b_N alpha| ).` (4.1)

The exact 1D minimax of TWO affine absolute values is elementary and ATTAINED between their distinct roots:

`min_(alpha∈R) max(A_N|1−a_N alpha|,B_N|1−b_N alpha|)
    = A_N B_N (a_N−b_N)/(a_N A_N+b_N B_N) =: delta_N >0`, (4.2)

with minimizer `alpha_N^opt=(A_N+B_N)/(a_N A_N+b_N B_N)`.

As N→∞ across ALL odd N,

`A_N→ A_* := [0.02/(2pi)]*[4 sqrt(21)/25]*[4/sqrt(5)]
              =0.004174983337015689...`,

`B_N→ B_* := [3 sqrt(273)/(10000pi)]*[6/sqrt(10)]
              =0.002993670211551709...`,

`a_N→6` and `b_N→5`.

Thus

`delta_N→delta_*:=A_*B_*/(6A_*+5B_*)
                      =0.00031232057654915964... >0`; (4.3)

`alpha_N^opt→(A_*+B_*)/(6A_*+5B_*)=0.17913460371526535...`.

**Theorem R26.A (fixed-source, any scalar-filter-tuning critical obstruction).**
For the original C2 and raw-k TT centered-collocation operator above,

`liminf_(N odd→∞) inf_(alpha∈R) ||R_(N,alpha)||_(H¹(B_N)→L²(T³))
           >=delta_*>0`.                          (4.4)

In particular NO sequence of real scalar filter parameters alpha_N—constant, optimally tuned, oscillating or even unbounded—makes this source full-band H¹ operator approximation converge to zero. The source polynomial filter has one real scalar parameter; two independent alias directions impose incompatible cancellation roots 1/6 and 1/5. **This does not exclude spatially varying, tensor-valued, frequency-specific, dealiased, geometrically natural or nonlocal filter families.**

Proof is self-contained: exact Fourier lower (2.2), explicit 2-variable minimax (4.2), ordinary trigonometric limits for (4.3). There is NO unjustified passage of an N-dependent alpha through a fixed-alpha asymptotic expansion: the finite-N inequality (4.1) is valid for every alpha before taking the limit.

## 5. Uniformly nonzero fixed-low-band second-order coefficient for ALL alpha

R25 supplied a low-band no-fold (k=(2,0,2), q=e_x, n=(3,0,2)) witness for alpha=0. Its exact 3×3 source algebra also determines its **ENTIRE dependence on alpha**, strengthening the s≥3 rate claim.

Take `H0=(u u^T−e_y e_y^T)/sqrt(2)` with `u=(-1,0,1)/sqrt(2)`, `S0=e_x⊗(H0 e_z)+(H0 e_z)⊗e_x`, and

`U=(Π_n−I)H0`, `V=Π_n S0−S0`.

For fixed alpha, the selected REAL Fourier pair of the discrete-continuum error is exactly

`J_N(alpha)=0.02 || e_(alpha,h)(k)[δ_h(2) U+δ_h(1)V]−[2U+V] ||_F`, (5.1)

where `e_(alpha,h)(k)=1−8alpha sin²(h)`.

The Taylor expansion as h→0 gives

`lim_(N→∞) J_N(alpha)/h² = 0.02 ||M_alpha||_F`,

`M_alpha = −(4/3)U−(1/6)V−8alpha(2U+V)`.         (5.2)

**Independent exact SymPy calculation** (all rational matrix entries after cancelling common square roots) gives

`||M_alpha||_F² = (410112 alpha² −1056 alpha +727)/24336`. (5.3)

The quadratic is **strictly positive for every real alpha**; completing the square:

`alpha_min=11/8544`,

`min_(alpha∈R) ||M_alpha||_F² =85/2848 >0`.       (5.4)

Consequently, for any FIXED real alpha and fixed Sobolev exponent s≥0,

`liminf_(N odd→∞) h^(−2) ||R_(N,alpha)||_(H^s→L²)
    >= (0.02/3^s) sqrt[(410112 alpha²−1056 alpha+727)/24336] >0`. (5.5)

This low-band second-order witness is NEVER canceled by a scalar filter alpha. For alpha=0, (5.2) recovers R25's exactly published `sqrt(727)/7800`; for alpha=1/6 it gives 0.014010773538528448... for J_N/h². This calculation is an extension in filter parameter, not a new source witness.

## 6. Complete fixed-alpha full-band rate after solving the gap

Combine (i) the already-proved R25 **upper** rate with (ii) the TWO folded lower witnesses from section 4 and (iii) the universal low-band lower from section 5. For the exact original C2 and EVERY fixed alpha≥0 and s≥0:

`||R_(N,alpha)||_(H^s(B_N)→L²(T³))
     = Θ_(alpha,s,C2)[ N^(1−s)+N^(−2) ]`   (N odd→∞). (6.1)

Equivalently:
- `0≤s<1`: grows at exact rate Θ(N^(1−s));
- `s=1`: Θ(1), nonconvergence;
- `1<s<3`: converges at exact rate Θ(N^(−(s−1)));
- `s≥3`: converges at exact centered-stencil rate Θ(N^(−2)).

No exceptional alpha=1/6 or alpha=1/5 survives. The statement is for **fixed** alpha; the uniform any-alpha_N statement is separately and fully proved only at the critical s=1 (4.4). R25 already owns the upper ceiling; R26's delta is the sharpness/completeness and the stronger nonstationary-scalar-filter no-go.

**Important point:** a nonzero continuum `[P,L_C]` is consistent with the discrete operator converging to it for s>1. `R_N→0` does NOT mean the physical TT leakage itself disappears. R26 proves a statement about matching operators, not vanishing operators.

## 7. Source-native independent tests ACTUALLY EXECUTED

Reproducer: `prf11_r26_complete_alpha_sobolev_reproducer.py` (Python3, NumPy, SymPy). Machine-readable output: `prf11_r26_exact_results.json`. The Python script verifies SHA256 of untouched helper before importing, verifies formula (5.3) and its minimizer symbolically, uses DIRECT 3×3 mode matrix computation, checks finite-N exact affine minimax (4.2), and, independently, constructs FULL N³ fields and calls the original helper `apply_T`, `apply_P_TT` (NOT a replacement projector).

Retained helper actual SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801` MATCH; native full-grid N=13/19/31, alpha=1/6, plus alpha=.05,.2 at N19. The five source-helper selected-pair relative gaps are all below **3.3e−15**; genuine input TT projection relative errors below **2.7e−15**. Sample:

| N | alpha | Native selected folded L² | Exact 3×3 L² | Relative gap |
|---:|---:|---:|---:|---:|
| 13 | 1/6 | values in JSON | exact | < 4e-15 |
| 19 | 1/6 | 0.002717293790925044 | 0.0027172937909250433 | 3.2e−16 |
| 31 | 1/6 | 0.005664813813628248 | 0.005664813813628251 | 6.2e−16 |
| 19 | .05 | 0.010994372527528285 | 0.010994372527528279 | 6.4e−16 |
| 19 | .2 | 0.0003524141518955453 | 0.0003524141518955464 | 3.3e−15 |

High-frequency folded analytic N from N=13 to N=961 (m up to 160) confirms (3.1) for alpha 0, .05, 1/6; for alpha=.2 new-family leading coefficient vanishes, as predicted, and the original-family certificate remains positive.

For the **universal tuning minimax** (4.2), direct unrounded integer k grid computations:

| Odd N | delta_N lower, minimized over all real alpha | minimizing alpha |
|---:|---:|---:|
| 31 | 0.000262412331 | 0.176273 |
| 61 | 0.000263848797 | 0.179866 |
| 101 | 0.000276682885 | 0.179311 |
| 201 | 0.000290519106 | 0.179068 |
| 401 | 0.000303090242 | 0.179172 |
| 801 | 0.000306764681 | 0.179116 |
| 1601 | 0.000309993196 | 0.179144 |
| 3201 | 0.000310925000 | 0.179130 |
| analytic limit | **0.000312320576549...** | **0.179134603715...** |

Here N≥61 tests are 3×3 Fourier calculations only; **NOT** N³ helper runs. For the fixed lowband second-order formula J_N(alpha)/h² at N1281: alpha=0 gives 0.00345676582 vs exact 0.00345678686; alpha=1/6 gives 0.01401064661 vs 0.01401077354; alpha=.2 gives 0.01667651564 vs 0.01667666367. All symbolic identities and array checks PASS. No historical production runtime or masked RMS simulation is claimed.

## 8. Mature mathematical literature / novelty subtraction

- Lloyd N. Trefethen, *Spectral Methods in MATLAB* (SIAM, 2000), Ch. 3 "Periodic Grids: The DFT and FFT" DOI **10.1137/1.9780898719598.ch3**, and Ch. 4 "Smoothness and Spectral Accuracy" DOI **10.1137/1.9780898719598.ch4**. Primary SIAM publisher abstracts examined. These explicitly connect Fourier DFT/FFT periodic grids and smoothness/aliasing; they do NOT present R26's exact C2 raw-k TT constants as a verbatim literature theorem.
- R. Coifman & Y. Meyer, "Commutateurs d'intégrales singulières et opérateurs multilinéaires", *Annales de l'Institut Fourier* 28 (1978), 177–202, DOI **10.5802/aif.708**, original journal entry examined; classical order-one pseudodifferential commutator L² regularity family. Not a source for a specific source-helper TT Fourier witness.
- Canuto & Quarteroni, *SIAM J. Numer. Anal.* 19 (1982), 629–642, DOI **10.1137/0719044**, mature regularity-dependent spectral approximation host already correctly scoped in PRF11 R25.
- Internal PRF11 R23–R25, INT8 source-grid Lie/projector/stencil, XH-S4 projection insertion, M13 original helper field family, Geeky-S11 TT-rigidity controls; author-source host hierarchy preserved.

**Literature caveat:** a targeted primary-source review is NOT exhaustive mathematical priority research; all the ingredients are mature linear Fourier analysis, elementary minimax of two affine moduli, and exact 3×3 orthogonal projection algebra. No novelty claim is established or needed.

## 9. Guardrails and exact disposition

EARNED:
1. Counterexample certifies nonconvergence at alpha=1/6, the explicit open exception in R25.
2. Exact sharp H^s rate for ALL fixed scalar alpha≥0 on the exact C2 full-band source grid.
3. Stronger positive universal obstruction for EVERY real grid-dependent alpha_N in critical H¹: `liminf inf_alpha ||R_N|| ≥0.0003123205765...`, with TWO source-internal folded witnesses on EACH sufficiently large odd N.
4. Independent rational/SymPy, whole-helper/NumPy and finite-grid minimax checks with exact source SHA match.

NOT EARNED:
- Scientific novelty/theorem-family discovery; owner or REC10 acceptance; BW ingestion; any EXEC_SIGN.
- Claims about matched-centered-symbol P_delta on EVEN N (Geeky-S11 scope), moving York P_g, covariant physical ∇/□, general filter matrices, dealiased pseudospectral codes, variable geometry, alternative sampling or all tensor classes.
- Claims about original byte-UNAVAILABLE DTC0a v0.3.1 runner, historical masked K_A, J3/K invariance, gravitational field equations or physical observational data.

`EXACT_CLASSICAL_SOURCE_TYPED / MATHEMATICAL_PASS / INDEPENDENT_REFEREE_PENDING / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE / GITHUB_PENDING_BW_INGEST`.