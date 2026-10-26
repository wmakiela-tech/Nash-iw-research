---
artifact_id: GEEKY-S11-ROT021-FULL-REAL-RAW-TT-TWO-STEP-CONTINUUM-NONCLOSURE-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-26
problem_id: P3_DTC0A_FULL_B_VS_G_TWO_STEP_LIE_REGULARITY_AND_CONTINUUM_HOST_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_RATIONAL_COUNTEREXAMPLE_AND_SOURCE_NUMPY_REPRO_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: MATURE_FOURIER_LERAY_TT_HOST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT021 — full repaired TT projection invalidates extension of the Nyquist-only H2 threshold

## 0. Owners-first and falsification target

ROT015 quantified even raw-k real-cast nonprojection, ROT016 the scalar bad-frequency guard G, ROT017 the real-raw-TT orthogonal projection B=GA, ROT018–019 the one-step guard/smooth-Lie loss of one Sobolev derivative; **ROT020 already proved the H2 threshold ONLY for scalar G** in the two-step expression. This result does not reattribute those discoveries. INT8 owns broader tensor TT/sheer/metric interfaces, PRF11 raw-k source Sobolev/commutator, M13 original h=fI K_A and mask, XH moving York. Standard Leray projection, Fourier multiplier calculus and projected fluid transport are mature hosts (e.g. classical Leray projection literature and JCP 2010 work on projection methods); no mathematics priority or novelty claim. The first attempted extension "replace G by the full B and retain the same H2 convergence" was explicitly treated as a potential FALSE statement.

Same unmodified helper `deepseek_python_20260627_a87249.py`, SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`. This is an available auxiliary DTC0a helper, **NOT** recovered byte-exact historic `dtc0a_runtime_v0_3_1.py`. Spatial domain is the full unmasked 3D periodic real symmetric tensor grid, h=2pi/N, even N, second-order central D. `A=Re(ifft(Praw fft(.)))`, `G` removes precisely bad mixed-Nyquist full modes, `B=GA` (a true orthogonal projector). At non-Nyquist k≠0 it is the raw integer-wavevector symmetric rank-two TT Fourier projector; k0 follows original helper tracefree rank-five convention. Scalar E_alpha=I+alpha*h²*Delta2, alpha real; source-style three-term Lie derivative for the FIXED smooth C=(0,cos x,0).

## 1. Exact algebraic distinction

Compare end-only full-TT projection versus a full-TT projection between two Lie steps, using **one scalar E_alpha before the first step**:

`D_B(N,alpha) = B L_C^2 E_alpha B - (B L_C B)^2 E_alpha B = B L_C (I-B) L_C E_alpha B`.

Since G commutes with A and B, `I-B=(I-G)+G(I-A)`, so

`D_B = B L_C (I-G) L_C E_alpha B + B L_C G (I-A) L_C E_alpha B`.

The first summand is the *Nyquist-frequency excursion* studied at the G-only level in ROT020. The second is an **ordinary TT-normal excursion**, potentially even at fixed low Fourier frequency where G acts identically. Consequently the positive buffered-support lemma from ROT020 applies only to the first summand; it is NOT a full B closure theorem.

## 2. A FIXED SMOOTH real TT tensor prevents Hs convergence for ANY finite s

Set k=(2,1,0), and choose the fixed real symmetric tracefree rank-two TT polarization

```
T = [ [-3/50,   3/25,  0],
      [ 3/25,  -6/25,  0],
      [ 0,       0,    3/10] ];
H(x,y,z) = T cos(2x+y).
```

Directly, `k*T=0`, `tr(T)=0`, `||T||_F²=9/50`. All frequencies reached in TWO Lie steps are k, k±2e_x, their negatives, so at N≥12 none lies on a Nyquist face; **G is identically 1 on the entire experiment**. The scalar-G two-step mismatch is exactly ZERO, for every alpha. Meanwhile the TT projector Praw varies with the ordinary Fourier direction, so `(I-B)L H` need not vanish.

Write the continuum +/- Lie Fourier shift at frequency q=(qx,qy,qz) as

`L_±(F) = i/2 [ qy F ± K(F) ],  K(F)= e_x (F e_y)^T + (F e_y)e_x^T`.

For fixed k with qy=1, let `P_q` be the exact rank-two symmetric TT projector at nonzero integer q. Define

`F_plus  = (I-P_(k+ex)) (T+K(T))`,
`F_minus = (I-P_(k-ex)) (T-K(T))`.

The exact returned k-frequency **TT** matrix (before the factor -1/4) is

`Z=P_k[(I-K)F_plus+(I+K)F_minus]`.

A completely independent standard-library Fraction calculation gives EXACT

```
Z = [ [ 4929/250000, -4929/125000,       0],
      [-4929/125000,  4929/62500,       0],
      [          0,            0, -4929/50000] ].
```

For complex input `T exp(i k·x)`, returned k-amplitude is `-Z/4`; for real input cosine it is `-Z/8`, including the conjugate. Therefore the ratio of the k-pair output norm to the input tensor norm is EXACT

`||Z||_F/(4||T||_F) = 1643/20000 = 0.08215`.

For the discrete central derivative at finite N, qy is replaced by `sin(2pi/N)/h` and K by `(sin h/h)K`; the scalar E multiplier on this fixed input is `e_N(alpha)=1-4alpha[sin²(2pi/N)+sin²(pi/N)]`. For EVERY FIXED alpha, `e_N(alpha)->1`, and the exact matrix formula converges to rational Z. Thus

`lim_(N->infty) ||(D_B H)_(±k)||_2/||H||_2 = 1643/20000`, for fixed alpha,

and the global operator has the RIGOROUS fixed-low-band lower bound for all s≥0:

`liminf_(N->infty) ||D_B||_(H_N^s -> L²) >= (1643/20000)/6^(s/2) > 0`.

Here `||H||_(H_N^s)/||H||_2=(1+|k|²)^(s/2)=6^(s/2)` under the raw signed-wavevector Sobolev convention. This refutes the blanket claim that s>2 suffices for full B two-step convergence, and indeed shows failure for ANY finite s. Crucially BOTH C and H are fixed smooth trigonometric functions; this is a continuum TT geometry effect, not moving grid-edge data or an artefact of Nyquist.

## 3. Distinct high-band all-real-alpha growth, rigorous for N>=160

The low-band obstruction and Nyquist amplification COEXIST. For 8|N, N≥16, take ROT019 genuine source raw-TT high-band test carriers `k=(N/2-1,m,0)`, m=N/8 or N/4, with cross-polarized unit Frobenius tensor `T=(v e_z^T+e_z v^T)/sqrt2`, v=(-m,N/2-1,0)/sqrt(m²+(N/2-1)²). They lie in ranB. The original scalar source filter has factors e_m(alpha) in two different bands. Their EXACT minimax obeys

`max_m |e_m(alpha)| >= rho=sqrt(2)/(12-sqrt(2)) = 0.133595512313...` for ALL real alpha including alpha_N.

Let `z=||(I-B)L_C H||_2/||H||_2`. Since ranB⊂ranG, the removed Nyquist sideband from ROT019 gives `z>=kappa N` with

`kappa = [sqrt(2)/(4pi) - 1/16]/2 = 0.025019769759819...`.

The transport part `cos(x)D_y` is skew-adjoint. The symmetric part of full tensor Lie comes ONLY from the lower-order tensor-gradient term: `L+L*=-(sin h/h)sin(x)(K+K*)`. On six-dimensional symmetric Frobenius tensors, the eigenvalues of K+K* are `{-2,-1,0,0,1,2}`, so `||L+L*||<=2`.

For any unit H in ranB, putting W=(I-B)LH, Parseval/adjointness yields the exact quadratic identity

`<H, B L (I-B) L H> = -||W||² + <(L+L*)H,W>`.

Consequently, at the selected carrier and with a scalar source multiplier e_m(alpha), the full B two-step norm obeys

`||D_B H||/||H|| >= |e_m(alpha)| * z(z-2)`.

For N>=160 divisible by eight, `kappa N >=4`, hence `z(z-2)>= z²/2>=kappa² N²/2`. Therefore, for ALL REAL alpha,

`||D_B(N,alpha)||_(L²(B-TT)->L²) >= c_* N²`,

`c_* = rho*kappa²/2 = 0.00004181465248512705...`.

By the ROT019 carrier weight bound `||H||_(H^s)/||H||_2 <=(9N/16)^s`, the all-alpha high-band lower generalizes to

`||D_B||_(H^s->L²) >= c_* (16/9)^s N^(2-s)` for N≥160, 8|N and any s≥0.

A NONSHARP certificate, not exact full B norm. This **does not contradict** fixed low-band nondecay at high s: the high-band lower can tend to zero even though the low-band obstruction remains.

For bounded |alpha| the two Lie operations have uniform discrete H^s→L² upper estimates `O(N^(max(2-s,0)))`, since derivatives have order one, fixed trigonometric multipliers shift Fourier indices by ±1, and B/E are bounded Fourier multipliers. Combining the two independent lower mechanisms yields for each FIXED alpha and every s≥0, along 8|N:

`||D_B||_(H^s->L²) = Theta(N^(max(2-s,0)))`.

In particular s<2 diverges, s=2 stays order one, and s>2 ALSO stays order one (because of the fixed low-frequency TT leakage). The upper is NOT uniform for unbounded |alpha_N|; the high-band lower is.

## 4. Executed independent computational evidence

**Control A (full direct 3D real tensors, independent vectorized Fourier Praw and B):** for N12/16/24/32/40, a fixed real T cos(2x+y) input and alpha 0/.05/-.2/.25, independently construct 7-point E, 3-term centered Lie (including D_i C^m terms), full B and direct-then-intermediate projection comparison. All 20 low-band cases have exactly negligible G-only mismatch (<2e-15) but nonzero full B discrepancy. Exact finite-grid algebraic return coefficient agrees to <2e-12. Four larger N produce growing high-band full-B discrepancy. Four native auxiliary SHA-fixed Praw/E/Lie source replay checks at N12/16. Total Control A output reports **69 typed subchecks**, not 69 independent physical datasets.

At alpha=.05:

N | fixed low k-return/||H|| | fixed low full-B discrepancy/||H|| | scalar-G-only discrepancy/||H|| | moving high-band full-B discrepancy/N²
12 | .0701625982 | .0905651057 | ~5e-16 | .005700645
16 | .0751342375 | .0969824427 | ~4e-16 | .005645787
24 | .0789409760 | .1018961386 | ~8e-16 | .005568215
32 | .0803265329 | .1036846001 | ~9e-16 | .005522031
40 | .0809774764 | .1045248308 | ~2e-15 | .005492264

**Control B (independent exact rational stdlib):** compute T and Z, norm ratio-square exactly `2699449/400000000`, hence ratio `1643/20000`. No FFT, NumPy, or historical source import. **1 exact certificate PASS**.

**Control C (independent sparse complex Fourier route, arbitrary huge N):** apply full B, central Lie shifts, scalar E, two TT carriers, and form B L(I-B)L E B without ever materializing real-space N³. For N16/24/32/40/64/128/160/256/512/1024 times six alpha values including two filter roots, alpha minimax and negative alpha, **120 carrier scenarios PASS**. In tested N>=160, witness bound exceeds independent analytic uniform `c_*N²` at every alpha. At N1024 the smallest tested two-carrier witness ratio is `0.001000312672 N²`, against certified lower `0.00004181465 N²`.

**Cross-route controls:** N16/24/32/40 high carrier at alpha .05, independently computed full-grid vs sparse full B norms match to ≤3.56e-15 in absolute units. **4 PASS**.

Combined explicitly counted controls 69+1+120+4=194 typed conditions/cases, not 194 independent instruments or datasets. The full package has separate executable Python files, frozen result JSONs, source helper SHA-verified unchanged, report, manifest and README. NumPy and Python stdlib only.

## 5. Scope, negative knowledge and decision

- **ROT020 not erroneous:** its H² statement was expressly and correctly limited to scalar Nyquist `G`, not B. ROT021 invalidates a transfer to B, not that earlier mathematical claim.
- Source original `apply_P_TT` on even N is NOT idempotent, but B is a genuine full real-compatible TT orthoprojection. The fixed-low test lives entirely on non-Nyquist modes, where source A=Praw=B; the counterexample is not caused by even-N nonprojection.
- The fixed-low obstruction comes from projecting away geometric TT-normal components **between** two Lie steps, analogous to projected fluid transport and pressure correction in mature Leray calculus. It is not a physical gauge or a new spacetime curvature result.
- E is applied ONCE before the pair of Lie derivatives; source DTC historical K_A involves different operator placements and input h=fI, so one MUST NOT equate this full-B two-step discrepancy to the original source K_A or physical NCDG K/J3.
- No source runtime dtc0a_runtime_v0_3_1.py byte replay, original experimental data, source masked RMS validation, moving metric York, GR/GW/PBH/BBN or independent referee, BW ingestion and Moderator EXEC.
- The spectral witness exact Fraction result is mathematical deduction from host assumptions; independent execution validates the derivation but does not establish mathematical novelty.

`NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / REFEREE_PENDING / BW_PENDING`.
