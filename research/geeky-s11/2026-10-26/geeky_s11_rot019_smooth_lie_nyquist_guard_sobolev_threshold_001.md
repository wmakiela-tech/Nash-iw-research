---
artifact_id: GEEKY-S11-ROT019-SMOOTH-LIE-NYQUIST-GUARD-SOBOLEV-THRESHOLD-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-26
problem_id: P3_DTC0A_EVEN_RAW_TT_GUARD_LIE_COMPOSITION_SOBOLEV_RESOURCE_GATE_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
class: EXACT_ALL_ALPHA_TWO_FOURIER_BAND_LOWER_AND_FIXED_ALPHA_UPPER_SOBOLEV_THRESHOLD
status: ANALYTIC_PROOF_AND_108_EXECUTED_TYPES_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: MATURE_SPECTRAL_CALCULUS / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT019 — próg H¹ dla gładkiego transportu Liego przez strażnik Nyquista

## 0. Prior art first and scoped question

ROT015 Geeky-S11 proves non-idempotence of *retained auxiliary source* real-cast even-grid raw-k TT; ROT016 counts exact defective Fourier modes, shows isolated projector Sobolev error O(N^-s), and constructs the whole-mode selector G; ROT017 proves B=GA is maximal real source-raw-TT-compatible orthogonal projection; ROT018 exhibits non-closure for a fixed smooth C=(cos x,0,0), with a positive L2 effect at alpha=.05 but an exceptional alpha which kills its specific input. These are antecedents, not new ROT019 credits.

NEW SCIENTIFIC QUESTION: Does the frequency support guard G behave continuously in *composition* with a **first-order variable-coefficient finite Lie derivative**, and what exact regularity suffices for uniform convergence? This note gives matching two-sided order N^(1-s) in the operator H^s -> L2 norm for every fixed alpha, a positive ALL-REAL-ALPHA lower floor after two-band minimax, and an exact bounded-support (finite-step) positive guard. Source helper identity, FFT Nyquist, de-aliasing, Fourier Sobolev multipliers and finite-difference stability are mature mathematics; NO mathematical novelty claim. PRF11 owns source raw-k collocation/Sobolev, INT8 raw/matched TT principal angles, M13 historical h=fI masked K_A, XH-S4 geometric York; no ownership displacement.

Retained **unchanged** `deepseek_python_20260627_a87249.py`, SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`, is the helper checked numerically. Original `dtc0a_runtime_v0_3_1.py` production bytes are unavailable; no run of that program is claimed.

## 1. Finite host and exact commutator structure

Take a real symmetric (0,2) tensor H on the N³ discrete torus, N a multiple of eight at least 16, h=2pi/N, normalized full-grid Frobenius L2. Signed FFT indices k_i in {-N/2,...,N/2-1}. A=Re(ifft(P_raw fft(.))) is the unchanged source-helper map; G is the *scalar*, real orthogonal Fourier multiplier vanishing precisely on the mixed-Nyquist set from ROT016 (at least one Nyquist coordinate and at least one other ordinary nonzero coordinate); B=GA=AG is the orthogonal real compatible-TT projector from ROT017. G commutes with every scalar Fourier multiplier, including D and E_alpha. The discrete source-style Lie derivative is

    (L_C H)_ij = C^m D_m H_ij + H_mj D_i C^m + H_im D_j C^m,
    D_m f = [f(j+e_m)-f(j-e_m)]/(2h),
    E_alpha = I + alpha h² Delta_2, alpha real.

Fix one SMOOTH, N-independent periodic field C=(0,cos x,0). Let M_f be scalar multiplication and K the fibre operator K(H)_ij=delta_ix H_yj+delta_jx H_iy. Put d1=sin h/h <=1. Exactly:

    L_C = M_cos(x) D_y - d1 M_sin(x) K,
    [G,L_C E_alpha] = [G,M_cos(x)] D_y E_alpha - d1 [G,M_sin(x)] K E_alpha.

Note that commutator measures guard-support nonclosure, NOT the full TT leakage Q_B L_C E_alpha B: the latter also includes geometry and can be larger. Since B has range within G, an H in the B range satisfies

    ||(I-B)L_C E_alpha H|| >= ||(I-G)L_C E_alpha H||
    = ||[G,L_C E_alpha]H||.

## 2. Exact source-raw-TT two-band witness

Let K_N=N/2-1 and take m_A=N/4, m_B=N/8. Both are integers because 8 divides N. For m in this pair, k=(K_N,m,0), v=(-m,K_N,0)/R, R=sqrt(K_N²+m²), w=e_z, T=(v w^T+w v^T)/sqrt2. Thus ||T||_F=1, tr T=0 and k·T=0: H_N,m=T cos(h[K_N j_x+m j_y]) is a REAL genuine source-raw TT input. Since k has no Nyquist coordinate, B H=A H=H. In normalized L2, ||H||=1/sqrt2.

The unchanged scalar filter acts on H by the multiplier

    e_m(alpha)=1-4 alpha [cos²(pi/N)+sin²(pi m/N)].

After full THREE-TERM L_C action, Fourier k+e_x lies on the mixed-Nyquist defective face (N/2,m,0), and B must erase it. Let

    d_y=sin(2pi m/N)/h, d1=sin h/h,
    W=e_x (T e_y)^T+(T e_y)e_x^T,
    V=d_y T+d1 W.

Since <T,W>=-K_N m/(K_N²+m²) and ||W||²=K_N²/(K_N²+m²), the norm is EXACT:

    ||V||² = d_y² - 2 d_y d1 K_N m/(K_N²+m²) + d1² K_N²/(K_N²+m²).

For the real cosine input the two conjugate defective Fourier coefficients have exact relative L2 amplitude

    R_m(N,alpha) = |e_m(alpha)| ||V||/2.

No false claim is made that R_m is the entire strict (I-B) leakage; it is precisely its discarded-frequency contribution. This same analytic R_m was directly tested via independent real-space FFT.

The two scalar filter multipliers belong to different source bands. Write a_N=cos²(pi/N)+1/2, b_N=cos²(pi/N)+(2-sqrt2)/4. Then a_N>b_N>0 and, for ANY REAL alpha (negative, exceptional, N-dependent or unbounded),

    max(|1-4alpha a_N|, |1-4alpha b_N|)
    >= (a_N-b_N)/(a_N+b_N)
    >= sqrt2/(12-sqrt2) = 0.1335955123132193.

The minimax equality is attained at alpha_star=1/[2(a_N+b_N)]. Since d_y >=sqrt2 N/(4pi) on either carrier and d1<=1,

    ||V|| >= d_y-d1 >= N [sqrt2/(4pi)-1/16],  N>=16.

Therefore BOTH the scalar guard commutator operator and the strict repaired TT leakage on these TT input directions have the ALL-alpha nonsharp lower bound

    ||[G,L_C E_alpha]||_(L2->L2) >= c_* N,
    ||(I-B)L_C E_alpha B||_(L2->L2) >= c_* N,
    c_* = [sqrt2/(4pi)-1/16]*[sqrt2/(12-sqrt2)]/2
        = 0.0033425289590218294.

The proof does NOT rely on a fixed alpha. The two carriers are grid-dependent high-band H_N, while C is FIXED SMOOTH. This is a lower certificate, not the sharp norm.

## 3. Matching Sobolev upper for bounded filters; s=1 threshold

Define ||H||_(H_N^s)²=sum_k (1+|k|²)^s ||Hhat(k)||_F² on the original raw signed frequencies. For any s>=0, the two test carriers satisfy

    ||H_N,m||_(H_N^s)/||H_N,m||_2 = (1+K_N²+m²)^(s/2)
    <=(9N/16)^s  (N>=16; m<=N/4).

Hence the exact full real-grid operator inequality for ALL real alpha is

    ||[G,L_C E_alpha]||_(H_N^s->L2)
    >= c_* (16/9)^s N^(1-s).

The same lower floor applies to the strict B-composition leakage when the domain is B-TT input.

For an upper bound, all matrix entries of either commutator with M_cos or M_sin connect only grid-frequency neighbours straddling a defective-face boundary. Every **input** frequency contributing to [G,M_f] is at signed |k|>=N/2-1. Furthermore |D_y(k)|<=1/h=N/(2pi), ||K||<=2, ||[G,M_f]||<=2, and ||E_alpha||<=1+12|alpha|. Therefore, for every s>=0,

    ||[G,L_C E_alpha]||_(H_N^s->L2)
    <= (1+12|alpha|) [N/pi+4] [1+(N/2-1)²]^(-s/2).

This upper is deliberately nonsharp. For FIXED alpha or bounded sequence alpha_N, together with lower bound, the exact order is **Theta(N^(1-s))** along multiples of 8. Thus s>1 gives convergence to zero, s=1 has a nonzero lower limit, and 0<=s<1 diverges. If |alpha_N| tends to infinity, a uniform upper independent of alpha is NOT asserted; the lower remains valid. Unlike isolated projector ROT016 (order N^-s), the first-order Lie composition loses ONE derivative.

## 4. Positive finite-support / buffered-carrier theorem

Let C have finite Fourier support S and suppose H has support K. Centered D, E_alpha, original raw TT P_raw, A, G and B are diagonal Fourier multipliers; only multiplication by C and its derivatives can enlarge Fourier support. One Lie operation maps support K into K+S (discrete sum modulo N). Any finite composition of at most n Lie operations and arbitrary diagonal E/P operations stays in K+jS at stage j, j<=n. If **none** of these intermediate supports intersects the mixed-Nyquist forbidden set, then the guard acts as the IDENTITY throughout the entire finite sequence. In particular if coordinate bands obey |k_i|<=M_i for H, and C has coordinate degree <=L_i, then M_i+nL_i<N/2 in each coordinate suffices to stay wholly away from Nyquist and alias.

The positive guard is support-typed: it does NOT establish invariance of TT geometry under Lie transport, does NOT prove unbounded-time or bounded-band-in-N closure, and does NOT justify silently changing source masks. Direct low-band control numerically verified zero guard loss on random symmetric tensors for N16/24/32/40/48/64.

## 5. Independently executed numerical falsifiers

Original standalone NumPy reproducer in this package implements all three C_y-gradient Lie terms, source seven-point Eα symbol, scalar Nyquist G and exact raw-k TT cross-polarization. It does not import any ROT018 implementation. For N=16,24,32,40,48,64, TWO TT carriers m=N/8,N/4 and Eα settings {0,.05,.2,1/6,-.7,1/(4a_N),1/(4b_N),alpha_star} yield **96 full 3D real FFT equalities** R_m(analytic)==discarded sideband FFT, every case PASS (including two filter zeros and the globally worst two-band alpha_star).

Additionally SIX literal SHA-verified unchanged source-native helper tests: at N16/24, direct comparisons of source Lie, source E_lin and source apply_P_TT to an independent realization. SIX separately seeded random low-band support-preservation tests. Total **108/108 PASS**. All-alpha minimax worst two-witness coefficients [max(R_A,R_B)/N] on N16/24/32/40/48/64:

    0.00967163, 0.00983555, 0.00997496, 0.01007754, 0.01015388, 0.01025828.

Examples alpha=.05: N16 max discarded sideband ratio 0.79606385 (relative to input, unweighted), N24 1.22686535, N32 1.66491918, N40 2.10600228, N48 and N64 grow; because the operator is first-order, amplification is expected rather than a norm-bounded projector defect. For the m=N/4 carrier, H1-normalized source-typed ratios at N16/24/32/40 approximately .097989,.097604,.097767,.097980, confirming an O(1) critical H1 behaviour. Native checks max relative error <=2.22e-15 for source P_raw, <=3.73e-16 for Lie and <=4.59e-16 for E; buffered support residual <=5.2e-19.

Full Python, executed full JSON, unchanged source helper, this full report, README, logs and SHA256 manifest are collected in a local ZIP and clean-rerun. No original production runner recovery or physical output asserted.

## 6. Negative knowledge and decision

- `G` repairs the ISOLATED source raw-k real-TT projection but does not commute with variable-coefficient Lie composition; even a fixed-smooth generator can move high-band input into its forbidden support.
- The lower bound for all alpha does NOT extend the ROT018 one-band test at alpha=1/4. It is obtained from TWO NEW high-band carriers with independent scalar filter factors. The upper bound is only uniform for bounded alpha.
- All high-frequency witness tensors depend on N; there is NO fixed-smooth-TENSOR continuum nonconvergence or physical gauge claim.
- The result is for full unmasked normalized L2 source-helper-compatible TT and scalar G; NOT masked K_A, original DTC production runtime, covariant/moving York, genuine GR / GW / PBH / BBN, canonical NASH K/J3 or experimental evidence.
- Independent scientific referee, BW ingestion and Moderator EXEC not claimed. No new tasks or mathematical novelty/priority claimed.

NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / INDEPENDENT_REFEREE_PENDING / BW_PENDING.
