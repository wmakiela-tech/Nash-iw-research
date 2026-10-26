---
artifact_id: GEEKY-S11-ROT022-PROJECTION-INDUCED-MEMORY-AND-PROJECTION-PRODUCT-LIMIT-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-26
problem_id: P3_DTC0A_FIXED_SMOOTH_TT_PROJECTED_EVOLUTION_VS_TRUE_OBSERVED_PROCESS_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
class: EXACT_FINITE_MORI_ZWANZIG_PLUS_FIXED_SMOOTH_NONMARKOV_WITNESS_AND_UNIFORM_PROJECTION_PRODUCT_LIMIT
status: MATHEMATICAL_PROOF_WITH_REUSED_EXACT_FRACTION_AND_146_EXECUTED_NUMPY_CONTROLS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: MATURE_FINITE_OPERATOR_THEORY / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT022 — TT projections between time steps create a distinct projected dynamics; discarded modes generate an exact memory kernel

## 0. Self-prior-art and primary literature subtraction

The **mathematical source** of this turn is S11 ROT021: for the same even-grid source raw-k full real-TT-compatible orthoprojector B, the fixed smooth input H=T cos(2x+y) and generator C=(0,cos x,0), the independent rational certificate established a nonzero coefficient of B L (I-B) L B, with exact continuum original-frequency norm ratio 1643/20000. ROT020's H2 threshold was *only* about scalar Nyquist guard G; ROT021 disproved extension to full B because non-Nyquist TT-normal modes matter. ROT015–017 supplied source-helper realness conventions. Those are PRIOR results, not rediscovered by ROT022. PRF12 owns quantum/process-memory questions; INT8 owns tensor-geometry/metric interface; M14 owns historical h=fI and masked K_A; XH owns external geometry and physical literature, separately.

The projected evolution/orthogonal dynamics/Volterra convolution identities and frequent-projection product limits are **mature mathematical hosts**. Primary reference: Widder, Zimmer & Schilling, *On the generalized Langevin equation and the Mori projection operator technique*, Journal of Physics A **58**, 405001 (2025), DOI 10.1088/1751-8121/ae02cc. Additional 2026 scope/limitations: Widder & Schilling, arXiv:2604.20453. These works provide the external host, **not validation of NASH or source DTC physical diagnostics**. ROT022's bounded new-to-cell increment is source-typed exact finite-time and finite-projection-number falsification on the ROT021 *already known fixed smooth* TT witness, plus a uniformly bounded single-ky band and numerical direct source checks. **No mathematical novelty/priority is asserted.**

Unchanged auxiliary source helper: `deepseek_python_20260627_a87249.py`, SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`. Historical production runner `dtc0a_runtime_v0_3_1.py` **not available byte-exact**, and is NOT claimed replayed.

## 1. Precisely scoped operator and three distinct evolution experiments

Even periodic N³ grid (N≥12 for the fixed low-band witness), h=2π/N, real symmetric 3×3 grid tensors, normalized full unmasked Frobenius L². Source raw-k FFT auxiliary projector A is real-cast and non-idempotent on mixed Nyquist modes. The strict orthogonal full-real TT-compatible projector B=G A from ROT017 **does** satisfy B=B*=B² and equals the usual raw-k TT P at all low non-Nyquist modes. Q=I−B. At zero raw frequency original source convention is traceless rank-5, irrelevant to the witness with ky=±1.

C(x)=(0,cos x,0) is fixed smooth and independent of N. With centered first differences D and original full symmetric covariant tensor Lie:

`(L H)_ij = C^m D_m H_ij + H_mj D_i C^m + H_im D_j C^m`.

Eα=I+αh²Δ₂ acts **once on initial data**, if selected; it commutes with B as Fourier diagonal, so its input multiplier is explicitly retained. For core α=0 put H0∈ran B. Define:

* `F_N(t)H0=B exp(t L_N) H0`: source-like unprojected internal evolution, TT observed only at the end.
* `Y_N(t)H0=exp(t B L_N B) H0`: dynamics whose generator remains in the projected TT sector.
* `S_(N,n)(t)H0=(B exp[(t/n)L_N] B)^n H0`: repeated finite-time steps with full TT projection after each step.

This is a deliberately **mathematical linear flow**, not the DTC historical production algorithm nor a physical time evolution model. Do not equate physical generator flow, gauge transformation or causal quantum memory to it.

## 2. R22.1: exact projection-induced memory/Volterra identity

For any FINITE N, split w(t)=exp(tL)H0 into x=B w and u=Q w, with u(0)=0 because BH0=H0. The exact coupled system is

`x'=B L B x+B L Q u`, `u'=Q L B x+Q L Q u`.

Variation of constants eliminates the unobserved u:

**`x'(t)=B L B x(t) + ∫_0^t K_N(t-s)x(s) ds`**,

where the **exact** operator-valued memory kernel is

**`K_N(τ)=B L Q exp(τ Q L Q) Q L B`**.

There is no added forcing term because QH0=0; for general initial H0 with QH0≠0 there would be an additional `B L Q exp(t Q L Q) QH0` forcing. The correct kernel at τ=0 is

**`K_N(0)=B L Q L B`**,

precisely the operator in ROT021. In Laplace variables for Re z large, the equivalent Schur resolvent on ran B is

`B(z−L)^(-1)B = [z−BLB−BLQ(z−QLQ)^(-1)QLB]^(-1)` (both sides on ran B).

These finite-dimensional identities are standard Mori–Zwanzig operator algebra. We numerically checked the actual integral and Schur resolvent separately, not merely a Taylor expansion.

## 3. R22.2: repeated projections converge to the WRONG evolution for this source-typed target

Set Δ=t/n. On ran B, expansion gives `B exp(Δ L) B = I_B + Δ BLB + O(Δ²)`. Therefore **for every finite grid N**, in operator norm on ran B,

**`lim_(n→∞) S_(N,n)(t) = exp(t BLB)B=Y_N(t)`**.

An explicit bounded-matrix telescoping estimate can be given. If ||L||≤M, then

`||B exp(ΔL)B−exp(Δ BLB)B|| ≤ Δ² M² exp(ΔM)`;

`||S_(N,n)(t)−Y_N(t)|| ≤ (t² M²/n) exp(2tM+ΔM)`.

This is NONSHARP but fully rigorous. For our source-typed C=(0,cos x,0), **the subspace of tensors with ky=±1 is invariant** under L and B. On that subspace centered D_y has norm |sin h/h|≤1; the tensor-gradient map K(H)=e_x(H e_y)^T+(H e_y)e_x^T has norm ≤2; thus **M=3 is UNIFORM IN N** on the actual tested frequency family. This upgrades the projection-product convergence to an N-uniform controlled statement on the declared invariant subspace, not the whole N³ tensor space.

This product limit is sometimes discussed in connection with quantum Zeno dynamics, but our B is a **classical tensor Fourier projector** and our finite L is not a quantum Hamiltonian. No experimental or quantum-Zeno effect is claimed.

## 4. R22.3: fixed-smooth nonzero continuum finite-time difference and rigorous error bar

Reuse the ROT021 *own prior* fixed, rational real TT witness:

`k=(2,1,0), T=[[-3/50,3/25,0],[3/25,-6/25,0],[0,0,3/10]]`, `H0=T cos(2x+y)`;

`k·T=0, tr T=0`, exact ||T||²=9/50. For every even N≥12 the input and all modes appearing at the second order are free of Nyquist, so the distinction is full TT geometry, NOT the artificial mixed-Nyquist correction G. Own prior exact Fraction certificate gives the **single returning Fourier-frequency** nonzero second derivative:

**`lim_(N→∞) ||(B_N L_N Q_N L_N B_N H0)_(±k)||/||H0||=1643/20000=.08215`.**

For every fixed α∈R, Eα on this input is the scalar

`e_N(α)=1−4α[sin²(2π/N)+sin²(π/N)]→1`, so the continuum limit of the observed projected evolution difference survives the stated initial filter.

For any finite matrix L,

`B exp(t L)B−exp(t BLB)B = (t²/2) B L Q L B + O(t³)`.

Sharper on **this return Fourier frequency k**: L shifts k_x only by ±1 at every application; any odd number of such shifts cannot return to k_x=2 when N is even. Hence all **ODD Taylor coefficients** of the k-return cancel. On ky=±1, ||L||≤3 and ||BLB||≤3, so direct tail estimates yield in the continuum

**`return_difference(t)/||H0|| ≥ (.08215/2)t² − (3t)^4 exp(3t)/12`.**

For t=.05, the leading part is .0001026875 and the maximum tail is .0000490148821151. Thus the total difference has the **rigorous strictly positive lower certificate**

**`liminf_(N even→∞) ||[F_N(.05)−Y_N(.05)]H0||/||H0|| ≥ 0.0000536726178849`.**

Here the N→∞ argument uses strong convergence on fixed Fourier polynomials plus the single-ky uniform operator bound M=3, which controls the exponential tails independently of N. The actual finite-N values exceed the lower certificate by a comfortable margin. The coefficient .08215 is NOT new to this turn; the **finite-time implication and uniform remainder** are ROT022's target-relative increment.

Projected observable semigroup also fails composition: `F(t+s)−F(t)F(s)=B exp(tL)Q exp(sL)B = t s BLQLB + O((t+s)³)`. This is a precise finite-dimensional failure of memoryless composition, not a claim about physical quantum non-Markovianity.

## 5. R22.4: actual executed falsification tests

Code A `geeky_s11_rot022_projection_memory_verify.py` independently constructs 6D Frobenius-orthonormal symmetric tensor matrices at each Fourier mode, banded nearest-neighbor x-shift sparse L matrices on ky=1, and true raw-k TT block projector B (zero on defective Nyquist face). Complex ky=1 is paired with conjugate ky=−1 when interpreted as a REAL cosine tensor. SciPy `expm_multiply` computes **genuine matrix exponentials**, not time-stepping based on the target Taylor claim.

Code B is INDEPENDENT full 3D real-space tensor source-style Lie, 7-point E, vectorized Fourier TT Praw+Nyquist guard, and a truncated **order-15 exponential Taylor** with small t=.1. These routes do not import one another; direct comparisons in nine cases give maximum absolute difference **2.24e−16** in the reported normalized observable norm.

On N=12,16,24,32,64,96,128, five times t=.005,.025,.05,.1,.25, multiple α∈{0,.05,−.2}, and repeated projection counts n=1,2,4,8,16,32,64:

| N | `||F(.05)H0−Y(.05)H0||/||H0||` | `||F(.2)H0−Y(.2)H0||/||H0||` | n=64 distance to Y(.2) |
|---:|---:|---:|---:|
| 12 | .000120895332 | .001940562598 | .000030261931 |
| 16 | .000125901298 | .002021183572 | .000031516623 |
| 24 | .000129577238 | .002080397768 | .000032438036 |
| 32 | .000130883891 | .002101448828 | .000032765578 |
| 64 | .000132153837 | .002121909905 | .000033083927 |
| 96 | .000132390091 | .002125716512 | .000033143152 |
| 128 | .000132472859 | .002127050122 | .000033163901 |

At N=128,t=.2 the *n=64 product* differs by 3.31639e−5 from Y, but remains 2.09389e−3 away from F. At that N the difference F−Y is 2.12705e−3. This makes the distinction between Zeno/product **convergence** and source-typed **correctness of the target** explicit.

**Additional mature-host identity checks**: six Gauss–Legendre 16-node integrations of exact Volterra memory identity at N12/16/24 and times .08/.2, maximum relative residual 2.65e−16; three Schur-Laplace projected resolvent checks z=5, maximum relative residual 2.01e−16; three semigroup-defect leading-curvature comparisons; reused independent standard-library Fraction checker confirms the exact .08215 ROT021 prior result. Two original unchanged helper checks at N12/16 directly compare `apply_P_TT` and `lie_derivative_tensor` with our independent full-grid implementation. 

**Count:** core script **146** explicitly typed checks: 7 second-order coefficient checks, 35 semigroup-time comparisons, 21 source E-factor tests, 49 repeated-product comparisons, 7 independently checked K(0) identities, 4 finite-time lower certificates, 6 Volterra integrals, 3 Schur resolvents, 3 semigroup-defect probes, 9 independent full-grid FFT comparisons and 2 native helper comparisons (sum = 146). plus **one reused prior exact Fraction certificate**, not claimed as new data. The machine-readable JSON provides 130 result rows and literal `checks=146`; count refers to assertions/typed controls, not independent physical datasets. The standalone report, both executable programs, 2 JSON outputs, frozen helper, stdout logs, README and SHA256 manifest are archived together and clean-rerun.

## 6. Strict limitations and scientific decision

1. This is a **fixed flat grid Fourier** mathematical experiment in the auxiliary helper operator family; historical DTC production runtime bytes unavailable; source h=fI K_A and masked RMS output are not recreated. No gauge invariance, NASH K/J3 physical meaning, GR/GW/PBH/BBN evidence.
2. Eα is placed **once at the input**, not after every Lie step. The repeated B projections do not automatically constitute the historical source algorithm. Alternative placements require separate calculations.
3. R22.1 and R22.2 are classical Mori–Zwanzig and product-limit facts. In the source-typed witness, intermediate TT-normal modes carry **mathematically observable future contribution**, but this alone is NOT a physical memory interpretation or proof of stochastic/quantum non-Markovianity.
4. The uniform-in-N bound M=3 is **only** for the ky=±1 invariant band of the fixed C; it is NOT a global unbounded-derivative estimate on arbitrary N³ tensor fields.
5. The finite-time lower bound uses **fixed smooth fields** and a prior exact independent Fraction coefficient; no novel theorem ownership or independent referee acceptance is asserted. All numerical controls are synthetic, deterministic except nonexistent measurement noise.
6. BW ingestion, scientific owner uptake and Moderator EXEC authorization are pending. No new task cascade.

`NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / INDEPENDENT_REFEREE_PENDING / BW_PENDING`.
