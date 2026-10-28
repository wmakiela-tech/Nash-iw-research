---
artifact_id: GEEKY-S11-ROT030-SMOOTH-GENERATOR-SPECTRAL-TAIL-CERTIFICATION-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-28
problem_id: P3_DTC0A_SOURCE_RAW_TT_EXACT_SPECTRAL_SMOOTH_C_TAIL_H1_RESOURCE_GATE_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
class: EXACT_ALL_M_H1_TO_L2_GENERATOR_FOURIER_TRUNCATION_CERTIFICATE_AND_SHARP_L2_FALSIFIER
status: MATHEMATICAL_PROOF_AND_1489_EXECUTED_TYPED_CONTROLS_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT030 — certyfikowane obcinanie widma gładkiego generatora Liego w dokładnej średniej TT

## 0. Prior art, typowany zakres, motywacja

**Own-lineage first.** ROT015–017 Geeky-S11 established the even-grid raw-wavevector TT real-cast issue in the preserved auxiliary source and repaired it to the actual compatible real orthoprojector `B=GA`. ROT021–023 first built fixed-smooth source-TT memory and scalar observation carriers. ROT024–026 treated low-band E_alpha identification, repeated stable E and failure of swapping heat and Lie. ROT027 **first defined** `U_m=(m+1)^(-1) sum E^(m-l) B L_C B E^l` as a uniform insertion product derivative. ROT028 first derived positive integer 3-/5-node moment approximations to U_m. ROT029 first gave the **exact** all-m Fourier divided-difference formula for finitely supported C. ROT030 does not reassign any of these. New-to-cell question: can ROT029 be used with a smooth but non-finitely-supported generator C, with an a priori, resolution- and m-uniform truncation error gate? The answer is YES in the H^1->L² source-typed host, and NO with an unweighted L²->L² uniform guarantee.

**Mature external literature.** The Fourier coefficient decay/spectral accuracy and the importance of smoothness assumptions are standard (L. N. Trefethen, *Spectral Methods in MATLAB*, SIAM, 2000, Ch. 4, DOI `10.1137/1.9780898719598.ch4`, https://epubs.siam.org/doi/10.1137/1.9780898719598.ch4; Chapter 7 of Trefethen *Finite Difference and Spectral Methods for ODE/PDE*, online at https://people.maths.ox.ac.uk/trefethen/pdetext.html). Frequency-convolution/Young bounds and first-order differential loss are classical; **NO mathematical novelty or priority claim**. PRF12 process memory, INT8 geometric TT, M14 original masked pure-trace h=fI K_A and XH empirical fronts are separate hosts and owner claims.

**Only original source actually tested:** retained unmodified `deepseek_python_20260627_a87249.py`, SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`. Its `apply_E`, `lie_derivative_tensor`, `apply_P_TT` are independently checked. The historical production `dtc0a_runtime_v0_3_1.py` bytes are UNAVAILABLE; no production replay. No masked K_A data used or inferred. No source `A` realcast silently promoted into a projection: `B=GA` is the explicit ROT017 mathematical repair.

## 1. Host and exact source symbol

On the full periodic N³ even grid, `h=2π/N`, signed Fourier frequencies `k_j∈{-N/2,...,N/2-1}`, real symmetric covariant rank-two tensors with normalized grid Frobenius L², and discrete Sobolev norm

`||H||_(H_N^1)^2 = sum_k (1+|k|²) ||Hhat(k)||_F²`

(the discrete FFT has normalized coefficients). The source central derivative has `D_j exp(i kx)=i d_j(k) exp(i kx)`, where `d_j(k)=sin(h k_j)/h` and `|d(k)|<=|k|`. The exact source-style three-term Lie derivative is

`(L_C H)_ij= C^r D_r H_ij + H_rj D_i C^r + H_ir D_j C^r`.

Let `G` remove precisely mixed-Nyquist defective whole modes as in ROT016–017, and `B=GA` the compatible real raw-wavevector TT orthogonal projection, including rank-five tracefree k=0. B is a diagonal Fourier multiplier; `||B||_(L2->L2)<=1`, `||B||_(H1->H1)<=1` and it commutes with scalar source E. For any real stable `alpha∈[0,1/6]`, the source `E_alpha=I+alpha h² Delta_2` with `e_alpha(k)=1-4alpha sum_j sin²(pi k_j/N)` is contractive in both L² and H¹; its multipliers MAY BE NEGATIVE on high modes. Define the exact uniform `m+1` insertion mean from ROT027:

`U_m(C) = 1/(m+1) sum_(ell=0)^m E_alpha^(m-ell) B L_C B E_alpha^ell`.

The m-independent-sparse spectral evaluation is the already-established ROT029 divided-difference representation; here the focus is the effect of truncating C and proving a quantitative gate.

## 2. R30.1 exact full-grid Fourier-tail certificate

Expand **discrete sampled** C as `C(x)=sum_s c_s exp(i s·x)`, where vector `c_s` obeys conjugate symmetry for real C. Let S be any conjugate-invariant finite subset of modes and C_S retain exactly those modes (including any aliased constant part). Define the exactly computable nonnegative certificate

`eta_N(S;C) = sum_(s notin S) ||c_s||_2 sqrt(1+4|d(s)|²)`.

**THEOREM, all even N, all m≥0, all real stable alpha:**

`||U_m(C)-U_m(C_S)||_(H_N^1 -> L2) <= eta_N(S;C)`.

**Proof in source tensor geometry:** Put R=C−C_S. A single C Fourier transition `s` acts on any fibre V at wavevector k by

`[M_s(k)V]_ij = i(c_s·d(k))V_ij + i d_i(s) sum_r c_s^r V_rj + i d_j(s) sum_r c_s^r V_ir`.

By the Frobenius tensor inequalities `||u V^T + V u^T||_F <=2||u|| ||V||_F` (rank-one-index contraction here),

`||M_s(k)V||_F <= ||c_s|| (|d(k)|+2|d(s)|) ||V||_F`.

For a SINGLE transition s, translation in Fourier is unitary and the discrete norm of `|d(k)| Hhat` is at most the H¹ seminorm. Thus by Cauchy–Schwarz in the pair `( |||d| Hhat||₂, ||Hhat||₂ )`,

`||L_(c_s exp(is·x)) H||₂ <= ||c_s|| sqrt(1+4|d(s)|²) ||H||_(H_N^1)`.

Sum with triangle/Young ℓ¹ convolution. Pre- and postcomposition with B and powers of stable E cannot enlarge H¹ at input or L² at output. Average m+1 inequalities; they retain the SAME bound. QED. This is an operator bound, not a claim about floating point bit-exactness or arbitrary continuous/moving metric York projections. There is no factor of m. For arbitrary generator finite C, the exact eta_N is measured using full discrete C coefficient data and remains a mathematically valid certification; for fixed analytically specified C a closed upper bound may replace it.

**Computational resource:** if S contains at most M source Fourier modes, the exact ROT029 sparse implementation costs approximately O(N³log N + M N³) conventional floating-point operations, besides FFT tensor constants and power/log evaluations. An error tolerance can select S through eta, without requiring m+1 native Lie calls. This is not a universal speedup when M grows like N³ or when evaluating analytic C Fourier data costs more than the proposed shortcut.

## 3. R30.2 exactly summable analytic continuous source generator, sampled aliasing included

Set a FIXED analytic vector field, independent of N,

`C=(0,f(x),0),  f(x)=sum_(r>=1) 2^-r cos(rx)=(0.5 cos x-0.25)/(1.25-cos x)`.

Its sampled discrete Fourier coefficients at integer index j (in the x direction, y=z=0) are EXACT positive rational numbers:

`c_0=1/(2^N-1)` and, for 1<=j<=N−1,

`c_j=[2^(N-j)+2^j]/[2(2^N-1)]`.

This includes the nonzero **aliased constant mode** c_0, often missed if one naively assumes the continuous Fourier series zero-mean property transfers exactly to finite sampling. Let C_L retain all discrete |signed s_x|<=L with L<N/2, including c0. Because every excluded sampled Fourier mode can only originate from continuous Fourier harmonics r>L, and `|d(s)|<=|s|<=r` after aliasing, the explicit source-typed bound holds:

`eta_N(C−C_L) <= sum_(r=L+1)^infty 2^-r (1+2r) = (2L+5) 2^-L`.

Therefore the R30.1 error satisfies this **N- and m-independent exponential** bound for all stable alpha. To guarantee a target eps it suffices to choose L such that `(2L+5)2^-L <= eps` and `L<N/2`; such a choice has L=O(log(1/eps)+log log(1/eps)) and at most 2L+1 source modes independent of N. For coarse N with L>=N/2 the entire finite discrete spectrum can instead be retained, yielding ZERO truncation error. No physical interpretation attached.

Numerical benchmarks using the EXACT discrete coefficient tail eta, rather than the looser universal bound: at N24, alpha=.05, m4, low TT input H=diag(1,0,-1)cos(2y), the measured `||[U_m(C)-U_m(C_L)]H||₂/||H||H1` for L1,2,3,4 is `[.1154080432,.04915071245,.02175630333,.00986466426]`; the exact (full-discrete) certificate eta is `[2.54622265,1.55910937,.87239692,.45419708]`. These bounds are deliberately conservative, but all 168 full-tensor spectral test cases (including m20,000 and m20,001) satisfy them.

## 4. R30.3 unavoidable L² loss: explicit source-raw-TT high-band witness

A stronger, UNWEIGHTED `||U_m(C)-U_m(C_S)||_(L2->L2) <= const * sum_s ||c_s||(1+|s|)` with N-independent const is false even for a fixed, smooth omitted harmonic at stable alpha=0.

Take N divisible by four, K=N/4, `eps>0`, discarded `R(x)=(0,eps cos x,0)` and a REAL exactly source-raw TT input `H_N(x,y,z)=T cos(K y)`, where `T=(e_x e_x^T−e_z e_z^T)/sqrt(2)` has ||T||_F=1, tr T=0 and k·T=0 for k=(0,K,0). H_N varies with N, unlike the fixed-smooth coefficients C and R. Since H_yj=0, all gradient-on-C terms vanish and

`L_R H_N = -eps (sin(hK)/h) T cos x sin(Ky)`.

Both sidebands k'=(±1,K,0) are regular (not mixed Nyquist). Direct raw-k TT orthogonal projection gives the exact fibre survival factor

`r_K=||P_TT(±1,K,0)T||_F = 1−1/[2(K²+1)]`.

With alpha=0, E=I so U_m(R)=B L_R B for **every m**; normalized real-grid Fourier orthogonality yields

`||U_m(R)H_N||₂/||H_N||₂ = eps N/(2 pi sqrt(2)) [1−1/(2(K²+1))]`.

This grows as Theta(eps N). The H¹-normalized ratio is the above divided by sqrt(1+K²), and tends to `eps sqrt(2)/pi`. Thus derivative loss is real, not a proof artifact. This does NOT refute R30.1; it precisely explains the necessity of declaring H¹ input regularity. The example is a source-typed high-frequency adversary, not a fixed-smooth-input continuum counterexample or historic h=fI masked K_A output.

For eps=1/8, the source-native/fresh FFT measured L²-input ratios at N8,12,16,24,32,64 are `[.101285586,.160368844,.218459106,.333056205,.446695403,.898564728]`, all matching the exact formula (max 1.9e−15); the H¹ ratios approach 0.05627.

## 5. Independent performed falsification and complete reproducibility

**Four independent programs, not using ROT029 implementations for their main test:**

1. `geeky_s11_rot030_fourier_tail_certify.py`: fresh NumPy Fourier-raw-TT projector + scalar source E and exact finite insertion polynomial (with separate high-m divided-difference fallback), analytic sampled broadband C vs truncated C_L; 168 full tensor cases, N12/16/24, L1..4, alpha0/.05/1/6, m0/1/2/4/6/20,000/20,001, low and random symmetric H; source Fourier eta and exact operator linearity. **696/696 typed assertions PASS**. Max normalized difference in `U(C)-U(C_L)-U(C-C_L)` is 7.78e−15 (numerical rounding, not an upper-bound failure).
2. `geeky_s11_rot030_source_native_verify.py`: independent literal SHA-pinned unchanged source native `apply_P_TT`, `apply_E`, full three-term `lie_derivative_tensor`, full real N³, G guard, and all-position source loop; N8/12, L1/3, alpha0/.05/1/6, m0/1/2, fixed low TT H. **36/36 PASS**; max linearity/commutation 2.72e−15. An earlier significantly larger original-helper suite TIMED OUT and is excluded from passing counts.
3. `geeky_s11_rot030_highband_witness.py`: separate analytic raw TT sideband calculation for exactly transverse H, stdlib Fraction rational r_K, actual native source for N8/12/16 and self-implemented FFT TT for N24/32/64; alpha0 all m; **51/51 PASS**, max absolute difference 1.89e−15.
4. `geeky_s11_rot030_exact_alias_tail.py`: standalone stdlib **exact Fraction** rational DFT alias coefficients and all finite weighted-tail upper bounds for N8/12/16/24/32/48/64/96/128 and all allowed L<=20; independent direct real trigonometric FFT numerical check. **706/706 PASS**, max alias numerical discrepancy 1.27e−16. Fractions verify only algebra and spectral alias coefficients, not transcendent sine identities.

**TOTAL 1489/1489 independently executed typed checks PASS**. The first larger literal source helper test TIMED OUT; not counted. Local Moderator/user-conversation ZIP holds this full report, four executable original programs, four executed JSON results, original frozen helper byte-unchanged, README, four stdout logs, SHA256 manifest. Independently clean extraction, CRC, all manifest hashes and byte-identical JSON replay must be checked and recorded before assigning final archive PASS. GitHub SCIENCE record write and pinned readback independently tracked; publication does NOT imply the executable sources are separately public.

## 6. Negative knowledge and release gate

- **H¹->L²** source-typed truncation certificate is uniform in grid and number of source E applications for stable alpha, NOT an L²->L² uniform certificate; the latter has an explicit Theta(N) falsifier.
- Analytic C has a nonzero sampled aliased c0; truncate the DISCRETE coefficients, not a silently unaliased continuum approximation.
- The real source-raw-TT A does not project on even N, so use correctly repaired `B=GA` and keep the defect mask explicit. No automatic claim that the true original source or masked production operator uses B.
- The exact sparse ROT029 method may be faster for modest S; no generic black-box one-call claim, no exact arbitrary-broadband O(N³) complexity. A numerical result still has floating-point errors.
- No physical/moving metric theory, historic original `dtc0a_runtime_v0_3_1.py`, actual masked source h=fI K_A, K/J3/NCDG gravity, GR/GW/PBH/BBN, novelty, owner adoption, independent referee, BW ingestion, canon or Moderator EXEC claimed. No new tasks.

`NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / INDEPENDENT_REFEREE_PENDING / BW_PENDING`.
