---
artifact_id: GEEKY-S11-ROT003-EVEN-NYQUIST-AXIAL-TT-PROBE-BLIND-SPOT-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-23
problem_id: P3_DTC0A_EVEN_GRID_NYQUIST_TRACE_FRAME_BLINDNESS_AND_OBLIQUE_TT_FALSIFIER_001
exposure: PUBLIC
status: EXACT_ALGEBRA_PLUS_INDEPENDENT_NUMPY_EVEN_GRID_CHECK_PASS / REFEREE_PENDING
claim_ceiling: DISCRETE_CENTERED_SYMBOL_TT_MATURE_HOST / NO_NOVELTY / NO_PHYSICAL_K_J3 / NO_EXEC_SIGN / NO_CANON
bw_ingestion_event_id: PENDING
---

# Geeky-S11 ROT003 — A 21-dimensional Nyquist trace blind space and an exact oblique TT leakage witness on even grids

## 0. Currentness and exact subtraction

**Question.** Geeky-S11 ROT002 gave an exact twelve-probe strain-frame and a rigidity result for **odd** N using centered differences and a fixed flat TT projector. ROT002 explicitly left even N outside its proof because the centered derivative has Nyquist zeros. Does the same twelve-probe detector become merely *unproved*, or can it give an actual **false negative**, even when all twelve **fully projected** TT outputs are examined?

**Result.** There is a constructive exact false negative for all even N >=6 in a **different, correctly specified even-grid projector convention**. A nonconstant Nyquist checkerboard generator has zero centered gradient and hence zero output leakage on **each of the 12 axial probes** used in ROT002, yet has strictly positive exact TT leakage on an oblique low-mode input. Its explicit formula is independently reproduced using a Fourier TT projector based on the centered derivative symbol. This is a mathematical stress test of extrapolating ROT002 beyond its declared odd-N domain, **not** a replay or correction of the historical even-N DTC0a runtime.

Already owned, not rediscovered: Geeky-S11 ROT002 original odd-grid twelve-probe exact identity/rigidity; INT8 ROT012-016 centered-derivative symbol, aliasing and genuine TT witnesses; M13 ROT023-027 historical trace-sector source calibration and mask limits; XH-S4 ROT018-023 curved/moving York and non-Einstein TT geometry; PRF11 R24 mesoscopic spectral bandwidth theorem. This note does not reproduce nor supersede those results. Standard finite-difference Fourier symbols, Nyquist null modes and Fourier-TT algebra are mature mathematical hosts. No novelty claim.

## 1. Precisely typed even-grid carrier

Let N>=6 be even and h=2π/N on periodic T_N^3. On grid functions use centered first derivative

```
D_{i,h}F(n)=[F(n+e_i)-F(n-e_i)]/(2h)
```

and componentwise source-shaped E_lin

```
E_{alpha,h}=I+alpha*h^2*Delta_h,
Delta_h=sum_i [F(n+e_i)-2F(n)+F(n-e_i)]/h^2.
```

For symmetric covariant rank-2 tensor F define the centered source-style Lie action

```
(L_C F)_ij = C^m D_m F_ij + F_mj D_i C^m + F_im D_j C^m.
```

**Crucial projector convention.** Define a *matched centered-symbol* real Fourier TT projector P_delta, NOT the historically archived raw-wavevector P_TT, by the vector

```
delta_N(k)_j = sin(2π k_j/N)/h.
```

At each Fourier mode with delta !=0 use the orthogonal rank-2 TT projector formed from pi=I-delta delta^T/|delta|², `P_delta F=pi F pi-(pi/2) tr(pi F)`; set P_delta=0 on the entire delta=0 set, and Q_delta=I-P_delta. Set the centered sine symbol at every Nyquist mode **exactly zero** to preserve Hermitian symmetry. This P_delta is real, orthogonal and exactly idempotent. The alternative P_delta=0 zero-symbol convention is declared and is not imposed on the original production code. All witnessed input/output modes below have delta !=0, so the choice at delta=0 does not create the counterexample.

The projectors and norms are full-grid unmasked; tracefree property holds for every P_delta output.

## 2. Exact nullspace dimension and why ROT002's odd-N step fails (THEOREM 003.1)

For even N, the centered Fourier symbol delta_N(k) is zero exactly when each k_i is **either 0 or N/2** (mod N): eight self-conjugate Fourier corners in three dimensions. Let `S_C^o=dev(sym D_h C)` be the discrete conformal-Killing strain.

For every nonzero delta(k), the Fourier equation `dev(sym(delta(k)⊗C_hat(k)))=0` forces C_hat(k)=0 by the same finite-dimensional algebra as ROT002. At delta(k)=0 all three components C_hat(k) are unrestricted. Each of the eight corners is self-conjugate and has three real coefficients. Consequently

```
dim_R ker( C -> dev sym(D_h C)) = 3*2^3 = 24   (even N),
```

compared with dimension 3 for odd N. The 21 nonconstant checkerboard degrees of freedom are invisible to the exact **trace-frame** of ROT002 (the algebraic twelve-probe trace identity itself still holds when probes exist and e1 !=0). This theorem does not assert that every one of those 21 directions has zero *full Q output* on the twelve probes: that stronger statement is demonstrated below for one concrete nonconstant generator.

## 3. Stronger actual twelve-probe FULL-Q false negative (THEOREM 003.2)

Fix the Nyquist checkerboard

```
C_N(j_x,j_y,j_z) = ((-1)^j_x,0,0).
```

It is nonconstant but `D_{i,h} C_N^m=0` for all i,m **exactly**. Thus for all symmetric tensors F,

```
L_{C_N}F = (-1)^j_x D_x F.
```

Consider precisely the twelve axial TT probes `M cos(x_a)` and `M sin(x_a)` from ROT002, with two transverse tracefree polarizations M on each of the x,y,z axes. Their E multiplication on axial wavevectors is `e1=1-4 alpha sin²(π/N)`.

- For all eight probes depending on y or z, `D_x H=0`, so `L_C E H=0`.
- For all four x-axis probes, `D_x H` has only x-axis Fourier support; multiplication by `(-1)^j_x` shifts this support by the x-Nyquist harmonic, but the centered derivative symbol of the resulting nonzero output mode still points **along x**. Their transverse tracefree constant M remains TT. Hence `Q_delta L_C E H=0`.

Therefore

```
Q_delta L_{C_N} E_alpha H_a = 0  for EVERY one of the twelve ROT002 probes,
```

with no approximation, whether the detector records only the trace or the entire projected Q norm. Yet `Q_delta L_{C_N} E_alpha P_delta` is a **nonzero** operator, as an additional oblique probe demonstrates.

## 4. Exact oblique TT positive witness (THEOREM 003.3)

Put

```
v=(1,-1,0)/sqrt(2),  w=(0,0,1),  T=vv^T-ww^T,
H(j)=T cos(x+y),  x=h*j_x, y=h*j_y.
```

For the input Fourier mode k=(1,1,0), `delta(k)=(s_h,s_h,0)` with `s_h=sin(h)/h`. Therefore v and w are transverse and T is tracefree, so `P_delta H=H` and `||H||_L2,F=1` exactly (||T||_F²=2 and <cos²>=1/2).

The componentwise E multiplier is

```
e2=1-8 alpha sin²(h/2).
```

Since `D C=0`, the exact tensor output is

```
L_{C_N} E H = -s_h*e2 * (-1)^j_x * T * sin(x+y).
```

The checkerboard multiplies each input Fourier mode by x-Nyquist, producing output modes with centered symbol parallel to `(-1,1,0)` (up to overall sign). At such an output mode v becomes longitudinal and the transverse plane is spanned by `u=(1,1,0)/sqrt(2)` and w. The orthogonal TT projection sends

```
P_delta T = (uu^T-ww^T)/2;
||P_delta T||_F² = 1/2;
||Q_delta T||_F² = ||T||_F²-||P_delta T||_F² = 3/2.
```

This gives the **exact nonzero** finite-grid leakage ratio

```
||Q_delta L_{C_N} E_alpha P_delta H||_L2,F / ||H||_L2,F
  = (sqrt(3)/2) * abs(sin(h)/h) * abs(1-8alpha sin²(h/2)).    [R3.1]
```

For alpha in {0,.05,.2} and N even>=6, this is strictly positive. The N-even sequence tends to sqrt(3)/2 as N increases for fixed alpha, **but the checkerboard field C_N itself changes with N, has no fixed smooth continuum representative, and no continuum-field nondecay claim is made**. The distinct fixed-smooth nondecay from Geeky-S11 ROT001 belongs to INT8's source formula and is not inferred from this witness.

R3.1 also yields a constructive lower bound on the full `Q_delta L_C E P_delta` norm because H is an exact TT input.

## 5. Independent executable verification

Self-contained NumPy script runs centered finite differences, the componentwise 7-point E_lin, the complete source-form Lie tensor expression, and an independently defined 3D FFT matched-symbol TT projector. It directly checks all twelve TT axial probes and the oblique witness (not merely analytic scalars).

Tests: 4 even sizes N∈{8,12,20,32} times alpha∈{0,.05,.2}, plus a constant-generator null control: **13 cases total**. Results:

- Max absolute oblique predicted-versus-actual norm discrepancy: `5.658861638958419e-16`.
- Max full-Q relative output across all 12 axial probes and 13 cases: `4.952376001952659e-16`.
- Max axial input TT projection error: `4.598383593795097e-16`.
- Max centered derivative of the Nyquist generator: `0.0` exactly.
- Max imaginary FFT-projector residue: `3.114704750440158e-16`.
- All 12 nonconstant cases give oblique leakage >0.5, while the constant generator null control is zero within roundoff.

For alpha=.05, oblique norm ratios: N8 `0.7340232200712993`, N12 `0.8048341232888564`, N20 `0.8435114896470218`, N32 `0.8571647104153078`.

Executed code: `geeky_s11_rot003_even_grid_nyquist_blind_spot_reproduce.py`.
Executed row-level JSON: `geeky_s11_rot003_even_grid_nyquist_results.json`.

## 6. Decision-changing boundary and STOP

**STOP:** treating absence of ROT002's twelve-probe signal as a certificate that *even-N* `Q L_C E P` globally vanishes. A specific even-grid nonconstant C has all twelve full-Q outputs zero, yet positive oblique leakage. This counterexample is not covered by ROT002's explicitly odd-N theorem and does not contradict it.

**Admissible next distinction:** one may augment first axial probes with oblique carriers for targeted Nyquist falsification, but the present result does **not** prove that a fixed finite set detects *all* nonconstant generators on even grids.

**Nontransportability:** the projector P_delta is defined with the centered derivative symbol, not the archived raw-wavevector TT projector. The original v0.3.1 even-N realness/idempotence failure has already been documented by the DTC teams; this construction does not repair that source implementation, replay historic `K_A`, or validate even-N experiments. The checked positive leakage belongs to a distinct, well-typed mathematical host. M13 historical source `h=fI` is an ambient trace input, not the TT input used here.

**Negative knowledge:** full-grid mathematical TT leakage does not imply a K/J3 physical invariant, gauge breaking, Einstein-covariant transport, nor a GW observable. No referee pass, BW ingestion, owner adoption, EXEC or novelty is implied by GitHub publication or internal numeric match.

`NO_NEW_TASK / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_K_J3 / NO_NOVELTY / INDEPENDENT_REFEREE_PENDING / BW_PENDING`.