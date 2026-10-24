---
artifact_id: GEEKY-S11-ROT005-EVEN-TT-PRESERVATION-QUANTITATIVE-DISTANCE-COERCIVITY-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-24
problem_id: P3_DTC0A_EVEN_N_MATCHED_TT_PRESERVATION_QUANTITATIVE_STABILITY_001
class: EXACT_COERCIVITY_TO_SIX_DIMENSIONAL_PRESERVATION_KERNEL_AND_24_PROBE_FRAME
exposure: PUBLIC
status: FINITE_GRID_MATHEMATICAL_PROOF_AND_INDEPENDENT_NUMPY_36_CASE_PASS / INDEPENDENT_REFEREE_PENDING
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: MATURE_CENTERED_SYMBOL_FOURIER_FRAME_AND_CONFORMAL_STRAIN_HOST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT005 — Quantitative stability of the exact even-N matched TT preservation kernel

## 0. Owner, currentness, subtraction, and scientific question

The prior Geeky-S11 ROT002 odd-grid twelve-probe exact trace frame gave TT preservation rigidity; ROT003 exhibited an even-grid Nyquist false negative of the axial frame; ROT004 proved the *correctly typed* even-N matched-symbol complete TT preservation family

`K_6={a+b*(-1)^(j_x+j_y+j_z): a,b in R^3}`

and an exact twelve oblique TT frame for the remaining corner modes. This rotation asks the missing **quantitative** question: if the full TT leakage is merely small rather than identically zero, must the generator be close to `K_6` in a computable norm with no vanishing grid-size penalty?

Other cells first: INT8 ROT020 supplies distinct sharp shear-equivariant scalar convolution minimax analysis; PRF11 R25/R26 own collocation Sobolev alias thresholds; M13 ROT027 owns masked vs unmasked source-specific KA asymptotics; XH-S4 owns metric-moving/curved York, non-Einstein counterexamples and Noether operator variations. None is superseded. The abstract setting and energy-frame argument are mature Fourier-multiplier, discrete Korn/conformal-strain and operator norm tools; **mathematical novelty not claimed**.

Public predecessor ROT004 (readback-verified): https://github.com/wmakiela-tech/Nash-iw-research/blob/a660eba871f58fae3d4ce2d1ec5351344fe27155/research/geeky-s11/2026-10-24/geeky_s11_rot004_even_nyquist_tt_kernel_and_finite_probe_classification_001.md

## 1. Source-style exact mathematical carrier

`N>=6` even, `h=2pi/N`, real periodic three-dimensional grid. The centered first difference D_j and componentwise E_alpha=I+alpha h^2 Delta_h (seven-point centered Laplacian), and covariant rank-two tensor Lie action are precisely those described in ROT004. Fix **matched centered-symbol** Fourier TT projector `P_delta` with delta_j(k)=sin(k_j h)/h, exactly zero at all Nyquist corners, with `P_delta=0` at all delta=0 corners; `Q_delta=I-P_delta`. This projector is NOT the archived original raw-wavevector DTC0a projector. All norms below are normalized *full-grid unmasked* L2 with Euclidean/Frobenius fiber norm.

Let:

- `chi(j)=(-1)^(j_x+j_y+j_z)` and `K_6={a+b*chi}`.
- `s_N=sin(h)/h>0`.
- `e_1=1-4alpha sin^2(pi/N)`, `e_2=1-8alpha sin^2(pi/N)`, assume `e_1*e_2 != 0`.
- `S_C^o=dev(sym D_h C)`, the discrete tracefree symmetric strain.
- `c_m` denote the eight orthonormal Fourier corner coefficients of C, `m in {0,1}^3` (binary index for frequency N/2 along each selected axis).
- `C_noncorner` the orthogonal sum of all Fourier modes with delta(k) != 0.
- `C_proper` the sum of the six proper Nyquist corner modes `m not in {000,111}`.

By Parseval, `dist(C,K_6)^2=||C_noncorner||²+||C_proper||²` exactly.

## 2. Theorem R5.1 — positive quantitative distance certificate

**Claim.** Under the above fixed carrier,

```
||Q_delta Lie_C E_alpha P_delta||_(L2 -> L2)
  >= c_(N,alpha) * dist_L2(C,K_6),

c_(N,alpha) = (s_N/sqrt(17))*min(sqrt(2/3)*|e_1|, sqrt(3)*|e_2|).
```

In particular for `alpha in {0, 0.05, 0.2}`, `c_(N,alpha)>0` on every even N>=6, and

```
lim_(N even -> infinity) c_(N,alpha) = sqrt(2/51) = 0.19802950859533486...
```

for any fixed alpha. This is a **nonsharp lower certificate**, not an upper bound on the leakage or an exact operator-norm computation.

### Proof: separated, rigorously noncancelling 24 probes

**2.1. Noncorner control by the ROT002 axial frame.** Its exact identity holds independently of N parity:

```
F_ax_trace(C):=sum_(12 axial H) ||tr(L_C E_alpha H)||²
             = 4 e_1² ||S_C^o||².
```

Since `P_delta F` is tracefree, `tr(Q_delta F)=tr(F)`. Pointwise tensor Cauchy-Schwarz gives `||Q_delta F||² >= |tr F|²/3`. Thus

```
sum_(12 axial H) ||Q_delta Lie_C E_alpha H||² >= (4/3)e_1²||S_C^o||².
```

At each noncorner Fourier wavevector delta(k)!=0, the linear strain symbol has singular values `|delta(k)|/sqrt(2)` (twice) and `sqrt(2/3)|delta(k)|` (once), by resolving C_hat into transverse and longitudinal components relative to delta. For even N>=6, the smallest nonzero `|delta(k)|` is `s_N` (including the near-Nyquist modes). Therefore

```
||S_C^o||² >= (s_N²/2)*||C_noncorner||².                 [R5.A]
```

**2.2. Proper Nyquist corner control from ROT004 oblique frame, with arbitrary other modes present.** ROT004 proved for corner-only C:

```
F_obl(C_corner):=sum_(12 oblique TT H) ||Q_delta Lie_C E_alpha H||²
                =3 e_2² s_N² W(C_corner),
W(C_corner)=sum_(m corner)sum_(a<b:m_a!=m_b)(|c_m,a|²+|c_m,b|²).
```

For each of six proper corners, the weight of the coordinate with minority bit is 2 and each other coordinate weight 1. Hence `W>=||C_proper||²`.

Crucial **new no-cancellation step**: this inequality survives addition of *arbitrary noncorner Fourier coefficients*. For a single complex exponential input H=T exp(i k.x), the source Lie action is linear in C, and a generator Fourier mode m produces output ONLY at `k+m (mod N)`, including both transport and `D C` contributions. Distinct m produce distinct output Fourier modes, and the diagonal Fourier projector Q_delta preserves their orthogonality. Pairing the real sine and cosine TT inputs recovers the sum of complex output energies with no cross terms. Consequently the contribution of the eight corner modes is an *orthogonal sub-sum* of the total 12-oblique energy:

```
F_obl(C) >= F_obl(C_corner)
         =3 e_2² s_N² W(C_corner)
         >=3 e_2² s_N² ||C_proper||².                     [R5.B]
```

No alias-free condition on C is assumed: Fourier folding is explicit and the map `m -> k+m mod N` remains bijective for each fixed k.

**2.3. Combine.** All 24 test inputs are exact `P_delta`-TT. The sums of their squared L2 norms are `5` (12 axial) and `12` (12 oblique), total `17`. By the definition of the L2 operator norm:

```
17||Q_delta Lie_C E_alpha P_delta||²
   >= sum_12axial ||Q_delta Lie_C E_alpha H||²
    + sum_12oblique ||Q_delta Lie_C E_alpha H||²
   >= (4/3)e_1²||S_C^o||² + 3e_2²s_N²||C_proper||²
   >= s_N²[(2/3)e_1²||C_noncorner||² + 3e_2²||C_proper||²]
   >= s_N² min((2/3)e_1²,3e_2²)dist(C,K_6)².
```

Taking square roots proves R5.1. At fixed alpha, `s_N,e_1,e_2 ->1`, giving the limit of the explicit coefficient.

**Interpretation:** an *upper measurement or estimate* `||Q_delta Lie_C E P_delta|| <= epsilon` implies the **inverse stability condition** `dist(C,K_6)<=epsilon/c_(N,alpha)` in the stated carrier; it is not a practical upper error estimate from merely measuring the 24 output probes. The latter provide a **lower** certificate only.

## 3. Independent executable control, full results

Self-contained NumPy code, separate from the ROT004 reproducer, evaluates the full centered source-style Lie tensor output, componentwise E, and independently defined Fourier `P_delta` on N={6,8,10,12}, alpha={0,0.05,0.2}, and three generator classes:

1. generic random grid field plus a+b chi,
2. almost-kernel field a+b chi+1e-4 noise,
3. exact six-dimensional kernel a+b chi.

36 cases. The code evaluates *all twelve axial traces* and *all twelve full projected oblique outputs*, reconstructs the eight Nyquist corner coefficients independently as signed grid averages and computes the exact orthogonal distance to `K_6` using FFT Parseval with modes 000 and Nyquist111 excluded. It checks both pointwise mathematical identities and the aggregate lower bounds.

Executed results:

- `case_count=36`, `all_pass=true`.
- Max absolute error in axial exact strain-frame identity: `1.1102230246251565e-16`.
- Max overestimate `F_obl(C_corner)-F_obl(C)` across 36 cases: `-2.2644001459962094e-32` (none positive).
- Minimum checked squared certificate margin: `1.3974288604377755e-33` (positive to floating precision).
- Representative N10 alpha=.05 generic: `dist=0.2126360963`, certified `c*dist=0.0386394739`, witnessed via 24-probe energy `sqrt(frame_energy/17)=0.3335645752` (not full norm).
- N10 alpha=.05 nearly in kernel: `dist=2.095022004e-5`, certified `3.806999348e-6`, witness `3.232090811e-5`.
- N10 alpha=.05 exact kernel: FFT-resolution `dist~5.06e-17`, 24-probe witness `~6.98e-17`, both floating-point zero.

For alpha=.05, the coefficient is c_N=0.1555806311 (N6), 0.1730672280 (N8), 0.1817164374 (N10), 0.1865707345 (N12), approaching 0.1980295. The executed code and JSON row ledger are provided as adjacent artifacts; original historical production code is byte-unavailable.

## 4. Claim boundary / STOP and follow-on scientific meaning

1. **Decision-changing repair:** ROT004's `leakage==0 iff C in K_6` has a quantitative stable inverse: `leakage >= c_N dist(C,K_6)`, where the lower coefficient remains positive as resolution increases at fixed alpha.
2. The 24-probe family supplies a *certified positive lower bound*, not an upper error bar or a sharp norm. No input perturbation/cutoff selection can be turned into a physical claim from it.
3. For even N, original raw-wavevector v0.3.1 TT projector failures are **not** repaired by the distinct `P_delta` host; historic `h=fI`, masked KA plateau, physical gravity/K/J3, moving York and nonlocal covariant E_g are all unrelated to this result.
4. e1*e2=0 cases, nonperiodic boundaries, non-centered stencils and alternate delta=0 projector policy are outside theorem. No automatic analytic continuation in alpha or N.
5. Mature-host frame stability mathematics, no novel-theorem priority inferred; independent referee, scientific owner adoption, BW ingestion and EXEC remain pending.

`NO_NEW_TASK / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / INDEPENDENT_REFEREE_PENDING / BW_PENDING`.
