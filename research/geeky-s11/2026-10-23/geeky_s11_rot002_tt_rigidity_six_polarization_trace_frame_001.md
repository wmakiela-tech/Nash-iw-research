---
artifact_id: GEEKY-S11-ROT002-SOURCE-TYPED-TT-RIGIDITY-SIX-POLARIZATION-TRACE-FRAME-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-23
problem_id: P3_DTC0A_FINITE_TT_PRESERVATION_RIGIDITY_AND_CHEAP_FALSIFIER_001
class: EXACT_FINITE_GRID_PROJECTOR_LEAKAGE_RIGIDITY_AND_TRACE_FRAME_CERTIFICATE
exposure: PUBLIC
status: SOURCE_TYPED_MATHEMATICAL_PROOF_PLUS_INDEPENDENT_NUMPY_VERIFICATION_PASS / REFEREE_PENDING
bw_ingestion_event_id: PENDING
claim_ceiling: MATURE_FOURIER_TT_AND_CONFORMAL_KILLING_HOST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT002 — Rigidity of whole-TT preservation and a twelve-probe exact trace-leakage frame

## 0. Currentness, exact scope, and others-first subtraction

**Question left after S11 ROT001:** Beyond a witness of positive fixed-smooth TT leakage, can we characterize *all* source-grid generators preserving the fixed full TT subspace? Can a small *a priori* family of exactly TT inputs certify nonpreservation without scanning the space of fields or solving a York elliptic equation?

**Answer:** Yes, for the **fixed flat raw-Fourier TT projector** and the specific **centered second-order DTC operator** on an **odd periodic grid**, provided the `E_lin` multiplier on the axial first harmonics is nonzero. In fact, six polarized tensors, each with sine and cosine phase, give an **exact strain-frame identity**, which is strictly positive for every *nonconstant* periodic generator and gives an explicit full-grid `L²` leakage lower bound. This is a deliberately narrow mature-host exact result, not a physical novelty claim.

Already owned elsewhere:
- INT8 ROT014 supplied a genuine TT-input fixed-P Lie nonclosure witness; INT8 ROT016 established the exact source-stencil formula and nonvanishing TT-sector leakage with one prescribed generator and high-mode input, including the general-q equation. S11 ROT001 extracted q=1 fixed-smooth consequence. No priority is taken for these.
- XH-S4 ROT018–022 owns the metric-dependent and moving York projection, elliptic solver and curved-metric/covariance checks; these are **not** superseded by any fixed-P certificate.
- M13 ROT023–026 owns historical source-field replay, the 18/18 trace-sector ledger and the exact nonzero pure-trace ambient `K_A` limit; that carrier is not the TT domain studied here.
- York (1973) orthogonal TT decomposition and the conformal Killing operator are mature foundations. This work is a finite-grid specialization/probe-frame construction within that framework; independent mathematical novelty review not performed.

Relevant sources:
- INT8: https://github.com/wmakiela-tech/Nash-iw-research/blob/d645a43ad0f2d5e4b34b40ef041786f57f9a8c3f/research/int8/2026-10-23/iw_int8_rot016_source_typed_tt_high_frequency_commutator_nondecay_001.md
- S11 ROT001: https://github.com/wmakiela-tech/Nash-iw-research/blob/e2c7d202abddb7ad159b01d7636bd8ef6861b7cd/research/geeky-s11/2026-10-23/geeky_s11_rot001_fixed_smooth_tt_sobolev_nondecay_001.md
- XH ROT022: https://github.com/wmakiela-tech/Nash-iw-research/blob/6d71b91f9e5966f7a1aa206c10197054c5153c65/research/xh-s4/2026-10-23/IW_XH_S4_NONZERO_CURVATURE_YORK_METRIC_ELIN_COVARIANCE_AND_2026_TT_SPECTRAL_PRIORART_AUDIT_022_20261023.md
- York 1973: https://doi.org/10.1063/1.1666338

## 1. Domain and operator conventions

`N >= 7` **odd**, `h=2π/N`, spatial domain `T_N³`; grid points at `h(n_x,n_y,n_z)` and full-grid normalized Hilbert-Schmidt/Frobenius `L²` norm. All fields are real and periodic, all tensors covariant symmetric rank 2. The derivative is `D_jf=[f(x+he_j)-f(x-he_j)]/(2h)`.

For tensor `F`, let `E_{α,h}F=F+α h² Δ_h F`, componentwise, with `Δ_h` the centered 7-point second-difference Laplacian. The Lie derivative is the retained source-style operator

```
(L_C F)_{ij}= C^m D_m F_{ij} + F_{mj} D_i C^m + F_{im} D_j C^m.
```

`P` is the fixed flat raw-wavevector Fourier TT projector (using the standard nonzero-wavevector rank-2 tensor multiplier); `Q=I-P`. The zero-wavevector convention in the independent reproducer is `P(0)=0`; **the theorem only uses** that P fixes the twelve nonzero first-mode TT probes, that `P` is idempotent and Fourier-diagonal, and that the output of `P` is tracefree. No claim about other zero-mode conventions is needed.

Let

```
e1 = 1 - 4 α sin²(π/N).
S_C = (D C + (D C)^T)/2.
S_C° = S_C - (tr S_C)I/3.
```

**Hypothesis:** `e1 != 0`. For the DTC diagnostic values α∈{0,0.05,0.2} and odd N≥7, this is automatically true.

## 2. Six polarizations and twelve test fields

Take Cartesian orthonormal coordinate vectors `e_x,e_y,e_z`, and define six constant *tracefree symmetric* matrices:

```
A_x = (e_y e_y^T - e_z e_z^T)/sqrt(3)
B_x = (e_y e_z^T + e_z e_y^T)/sqrt(2)
A_y = (e_z e_z^T - e_x e_x^T)/sqrt(3)
B_y = (e_z e_x^T + e_x e_z^T)/sqrt(2)
A_z = (e_x e_x^T - e_y e_y^T)/sqrt(3)
B_z = (e_x e_y^T + e_y e_x^T)/sqrt(2).
```

For each matrix `M` labeled by axis `a∈{x,y,z}`, take the two real fields

```
H_{M,c}(x)=M cos(x_a),    H_{M,s}(x)=M sin(x_a).
```

Each is exactly TT under raw Fourier P: `P H=H`; all have a fixed continuum smooth representative. These are the only twelve test fields used below. Diagonal matrices `A` have Frobenius squared norm `2/3`; shear matrices `B` have squared norm `1`.

## 3. Exact trace-frame identity (THEOREM 002.1)

For **any** real periodic grid vector field `C` and any alpha with `e1 != 0`,

```
Σ_{M∈{A_x,B_x,A_y,B_y,A_z,B_z}} Σ_{phase∈{cos,sin}}
       ||tr( L_C E_{α,h} H_{M,phase})||²_{L²}
       = 4 e1² ||S_C°||²_{L²,F} .                    [R2.1]
```

**Proof.** Every H has zero trace. Since E is scalar on its single first harmonic, `EH=e1 H`, and the advection contribution `C·D(EH)` has identically zero trace (with no discrete Leibniz assertion). Contracting the remaining symmetric-gradient terms gives

```
tr(L_C E H_{M,phase})(x)=2 e1 f_phase(x_a) (M:S_C°)(x).
```

At each point `cos²(x_a)+sin²(x_a)=1`. The diagonal triple obeys

```
[(S_yy-S_zz)²+(S_zz-S_xx)²+(S_xx-S_yy)²]/3
    = Σ_i (S_ii - tr(S)/3)²;
```

and the three shear contractions contribute `2 Σ_{i<j}S_ij²`. Hence the six polarisations satisfy `Σ_M(M:S)²=||S°||²_F` **pointwise**. Square, sum phases and polarisations, average over the grid. QED.

No projector evaluation is needed to calculate the left-hand side; it is a **trace-only oracle** for the conformal strain of C.

## 4. Full TT-subspace preservation is rigid (THEOREM 002.2)

For an odd grid N≥7 with `e1 != 0`,

```
Q L_C E_{α,h} P = 0 as an operator on all symmetric grid tensors
    ⇔ C is a constant periodic vector field.             [R2.2]
```

**Only if.** If the left-hand side vanishes, in particular `Q L_C E H=0` for all twelve TT probes. Every `P` output is tracefree, so `tr(QF)=tr(F)`; therefore all twelve traces vanish. By R2.1, `S_C°=0`. Taking the DFT of this discrete conformal Killing condition at nonzero Fourier mode `m` gives

```
δ_i(m) c_j(m)+δ_j(m)c_i(m) = 2φ(m) δ_{ij},
δ_j(m)=sin(m_j h)/h.
```

For odd N, the real vector `δ(m)` is nonzero whenever `m!=0`. Rotate a Euclidean algebraic basis to align its first axis with δ. The `(2,2)` component forces φ=0, then `(1,1),(1,2),(1,3)` force all coefficients `c_j(m)=0`. Hence only Fourier mode `m=0` survives: C is constant.

**If.** For constant C, `D_i C^m=0` and `L_C=C^mD_m`. Every centered D_m, E and P is a Fourier multiplier and they commute; therefore `Q L_C E P=Q P L_C E=0` because P²=P. QED.

**Important guard.** At even N, the centered derivative has additional Nyquist-zero symbols. The above injectivity step is invalid; *no claim* is made that every nonconstant generator is detected there. Likewise the case `e1=0` requires a different carrier; no unconditional alpha assertion is made.

## 5. Quantitative lower certificate (COROLLARY 002.3)

For every symmetric output F, the tracefree property of P gives `tr(QF)=tr(F)`, and the Frobenius Cauchy-Schwarz inequality gives `||QF||²_F≥|tr(F)|²/3` pointwise. Sum the twelve inputs and use R2.1:

```
Σ_{12 probes}||Q L_C E H_a||²_{L²,F}
    ≥ (4/3)e1² ||S_C°||²_{L²,F}.
```

The twelve squared TT-input L² norms sum to 5: three diagonal pairs contribute 2 and three shear pairs contribute 3. It follows that

```
||Q L_C E P||_{L²→L²}
    ≥ (2|e1|/sqrt(15)) ||S_C°||_{L²,F}.             [R2.3]
```

This is a finite source-grid **lower bound**, not a sharp operator norm. The right-hand side is nonzero whenever C is nonconstant (odd N, e1≠0). It uses no alias-free assumption on C because the trace identity is pointwise.

## 6. Numerical independent reproducibility

Standalone NumPy uses exactly the centered stencil and scalar E multiplier above, constructs the source-style Lie derivative, and independently implements Fourier P. It checks R2.1, each of the twelve pointwise trace identities, the TT status of every input, R2.3, and a constant-vector null control.

Source test C (separate from the real historical DTC frozen generator):

```
C=(0.15 sin(x)+0.10 cos(y), 0.08 cos(z), 0.06 sin(x+z)).
```

Thirteen evaluated cases: N∈{7,9,17,31} × α∈{0,.05,.2} plus N=9, α=.05, constant C.

- Maximum absolute R2.1 discrepancy: `1.3877787807814457e-17`.
- Maximum pointwise trace formula discrepancy: `1.1102230246251565e-16`.
- Maximum RMS test-input TT projector mismatch: `3.626771794874605e-16`.
- All 13 aggregate leakage lower-bound checks: PASS.
- For N=31, α=.05: certified lower bound `0.0599069408283852`, ratio for the twelve-probe aggregate `0.13978249753497354`. **The latter is not a certified supremum**, only a witnessed ratio; a true operator norm may be greater.
- Constant control: bound zero and observed aggregate ratio `1.5958035690560542e-17`.

Reproducer SHA256: `3539f1551813135b28e035012190da1c80a21354838d592e5941abbf2522f570`.
JSON results SHA256: `498d4631da7069584186afc3c7d9ccd843b472325185e71e9c39f9d02c119058`.
Reproducer file: `geeky_s11_rot002_verify.py`.
Results file: `geeky_s11_rot002_results.json`.

The **historical byte-exact DTC0a production runtime** remains unavailable. This is an independent source-mathematics reproducibility check, *not* a claim to have recovered that runner or certified its frozen historical source fields.

## 7. Branch decisions and STOP/claim guards

1. **STOP** searching for a nonconstant periodic C which globally preserves the fixed flat TT range under this exact odd-N central-stencil/E-linear carrier: R2.2 rules it out. This does *not* preclude individual TT states, selected subspaces, deformed/moving York projectors, or alternative geometrically natural transport.
2. For cheap adversarial diagnostics, twelve exactly TT real probes plus **trace-only** outputs suffice to catch any nonconstant generator within the stated carrier. This avoids expensive exact full P-output calculations for a *detection* task; it does not replace geometric accuracy tests or source-run provenance.
3. This does **not** explain the historical DTC0a `K_A` plateau (the frozen h=fI input lies in the ambient pure-trace sector), nor physical closure or a gauge-breaking invariant.
4. The certificate is **not** covariant under arbitrary coordinate transformations because it uses one fixed Euclidean background and centered coordinate derivatives; XH-S4 ROT021/022 are distinct geometric experiments.
5. Its mathematics is a discrete conformal Killing / TT-frame calculation on a mature host, and no claim of mathematical novelty is made. Independent referee and BW ingest: **PENDING**.

NO_NEW_TASK / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_K_J3 / NO_NOVELTY / NO_OWNER_ADOPTION_ASSUMED.