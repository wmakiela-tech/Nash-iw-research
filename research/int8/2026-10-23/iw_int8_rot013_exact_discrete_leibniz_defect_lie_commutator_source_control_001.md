---
artifact_id: IW_INT8_ROT013_EXACT_DISCRETE_LEIBNIZ_DEFECT_LIE_COMMUTATOR_SOURCE_CONTROL_001_20261023
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
date: 2026-10-23
problem_id: P3_DTC0A_DISCRETE_LIE_DERIVATION_PRODUCT_RULE_DEFECT_001
document_type: EXACT_ALGEBRAIC_SOURCE_LOCAL_COUNTEREXAMPLE_AND_NEGATIVE_CERTIFICATE
exposure: PUBLIC
canonical_path: research/int8/2026-10-23/iw_int8_rot013_exact_discrete_leibniz_defect_lie_commutator_source_control_001.md
status: MATHEMATICS_EXACT_AND_SOURCE_HELPER_REPRODUCED / REFEREE_PENDING
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_K_J3_INVARIANT_CLAIM
---

# INT8 ROT013 — nonzero DTC0a Lie closure residual from centered-difference Leibniz failure alone

## 0. Source currentness and host subtraction

Science-first currentness checked in Slack #iw-dispatch on 2026-10-23. New XH-S4 ROT018 explicitly source-reconstructed the DTC0a operators and established exact decomposition
  K_A-K_B = P L2 (I-P)L1 h - P L1 (I-P)L2 h,
with a pure-trace initial field, true [P,E_lin]=0, a matched nonzero TT test, and a NEGATIVE TEST: switching the Fourier TT k to stencil delta changed K_A by only ~0.094% for their smooth N31 trace-field probe. It is therefore INCORRECT to diagnose their KA plateau as exclusively k-vs-delta mismatch; INT8 ROT008/012 never earned such an interpretation.
XH-S4 ROT018:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s4/2026-10-23/IW_XH_S4_DTC0A_PROJECTION_INSERTION_TRACE_INPUT_AND_STENCIL_HOST_AUDIT_018_20261023.md

INT8 ROT008/012 separately characterized EXACT Fourier-vs-stencil transversality and operator norm geometry. M13 ROT18–22 separately classified moving RMS masks, amplitude-test dependence, alpha-scan non-identifiability, and masked projector noncontraction. This rotation does NOT reproduce those claims.

**NEW MATERIAL SOURCE-LOCAL GATE:** In the supplied DTC helper the central first-difference tensor Lie derivative uses pointwise products. Its centered stencil does not obey the exact Leibniz rule. Even with E=Identity and an initial constant pure-trace tensor H=I, the unprojected Lie commutator closure K_C can be strictly nonzero for two smooth, exactly band-resolved vector fields, while *both* projected K_B and K_A vanish by source helper calculation. This isolates a **third** cause/type of numerical residual, distinct from projective insertion and TT/stencil mismatch.

This is elementary finite-difference product-rule theory and elementary algebra of derivations on finite sets, not a new theorem family.

## 1. Precise carrier and source provenance

Inspected the retained user-provided file
  deepseek_python_20260627_a87249.py
  SHA256=23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801.

Relevant functions and calls are literally:
  derivative(field, axis, dx, order=2):
       (roll(field,-1,axis)-roll(field,+1,axis))/(2 dx)
  lie_derivative_tensor(C,H,dx,order=2):
       C^k D_k H_ij + H_kj D_i C^k + H_ik D_j C^k
  lie_bracket(C1,C2): C1^m D_m C2 - C2^m D_m C1
  compute_K_C(C1,C2,H,E_mode='Identity',dx,order=2,alpha=0):
       L_C1 L_C2 H - L_C2 L_C1 H - L_[C1,C2] H
  K_B=P_TT K_C
  K_A=P L_C1 P L_C2 H - P L_C2 P L_C1 H - P L_[C1,C2]H.

This artifact considers ONLY `E_mode='Identity',order=2`. The E_lin(alpha!=0) branch inserts additional scalar Fourier multipliers and is NOT covered by the closed formula below. The original historical source `dtc0a_runtime_v0_3_1.py`, with manifest-declared SHA256 2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084, was NOT byte-reconstructed. The source helper is distinct from that historical production runner.

Periodic cubic grid N³, L=2pi, dx=h=2pi/N, odd N≥9; all fields are smooth single-coordinate samples, no aliasing of involved modes k=1,l=2 (and products up to k+l=3). Initial constant H_ij=delta_ij, exactly pure trace and with P_TT(H)=0.

Vector fields:
  C1=(f(x),0,0), f(x)=sin x,
  C2=(g(x),0,0), g(x)=cos(2x).

Thus only xx component is nontrivial in the Lie-closure residual, and source `compute_K_C` agrees exactly with a scalar 1D calculation on each spatial x-line.

**Normalization:** all numerical RMS below are `sqrt(mean_grid sum_ij |K_ij|²)` for the FULL periodic grid. The historical DTC0a `rms_norm` divides further by sqrt(6) and uses an interior mask. NEVER compare their numbers as if they were same units or a physical residual of same input amplitude.

## 2. Exact centered Leibniz defect and source-level commutator identity

Define D=D_h, the centered periodic first derivative, and
  E_h(f,g)=D(fg)-f Dg-g Df.                  (2.1)

For any discrete f,g,
  E_h(f,g)[x]
   =[(f(x+h)-f(x))(g(x+h)-g(x))
    -(f(x-h)-f(x))(g(x-h)-g(x))]/(2h).     (2.2)
This exact identity follows by expanding the products in the centered difference formula.

In the 1D metric-tensor restriction H_xx=b(x), C=f(x)∂_x, the source's tensor Lie action is
  L_f b = f Db + 2(Df)b.                    (2.3)
For constant b=1 and the code's bracket [f,g]_D=fDg-gDf:
  K_C,xx :=[L_f,L_g]1 - L_[f,g]_D 1
  =2[f D²g-g D²f-D(fDg-gDf)]
  =2[E_h(g,Df)-E_h(f,Dg)].                 (2.4)

This holds as an EXACT finite-grid algebraic identity independent of any TT projection. It does NOT assume a Leibniz rule. All other tensor components vanish in our concrete H=I and single-axis C class.

For continuum D=∂_x, E≡0 and K_C,xx≡0. For the central stencil, E generally does NOT vanish.

Smooth Taylor expansion gives
  E_h(f,g)=h²/2[f''g'+f'g'']+O(h⁴),        (2.5)
whence
  K_C,xx=h²(g' f'''-f' g''')+O(h⁴).        (2.6)
For f=sin x, g=cos 2x:
  K_C,xx=-6h² cos x sin(2x)+O(h⁴),        (2.7)
and its full periodic x-grid RMS is
  RMS(K_C,xx)=3h²+O(h⁴).                 (2.8)
The RMS leading constant 3 follows from exact orthogonality of trig modes and mean(cos²x sin²2x)=1/4 on these grids.

## 3. Exact Fourier-multiplier identity, full-band obstruction

For complex Fourier modes f=A e^{ikx}, g=B e^{ilx}, define delta(k)=sin(kh)/h. Then
  K_C,xx=
    2AB [delta(l)-delta(k)]
         [delta(k+l)-delta(k)-delta(l)] e^{i(k+l)x}. (3.1)

That is the EXACT difference between `delta(k+l)` and the sum `delta(k)+delta(l)`, caused by non-Leibniz multiplication. For f=sin x, g=cos2x, superpose k=±1 and l=±2 with standard complex coefficients; all x-grid K_C outputs from the helper agree with this spectral formula to <3e-12.

Nonuniformity: with k_N=floor(N/7), l_N=floor(N/5) and N=31,61,121,241, no product mode is outside Nyquist. Their physical frequencies grow proportionally to N, so
  ||K_C||_RMS = Theta(h^-2)
in the observed and asymptotic sequence, notwithstanding smooth low-fixed-mode error O(h²). This is an EXACT finite grid symbol effect, not a physical high-frequency source or a convergence counterexample under a declared Sobolev band/regularity hypothesis.

All functions are periodic grid samples and the test does NOT use a moving physical mask.

## 4. General algebraic no-go: no nonzero exact derivation on the pointwise finite-grid function algebra

Let A=R^M, finite M≥1, with pointwise multiplication. If a linear map D:A→A obeys D(fg)=fDg+gDf for ALL f,g∈A, then D=0.

Proof: For each coordinate idempotent e_j (1 at j, 0 otherwise), e_j²=e_j. Leibniz yields
  D e_j=2 e_j D e_j.
At coordinate i≠j, RHS=0, so (De_j)_i=0. At i=j, equation gives (De_j)_j=2(De_j)_j, hence zero. Thus De_j=0 for every j. Since the e_j form an A vector-space basis, D=0. QED.

Therefore NO nonzero stencil on the whole pointwise finite-grid algebra can satisfy a universal exact ordinary Leibniz rule. This does NOT rule out carefully designed mimetic/FEEC calculus with DIFFERENT products/spaces, discrete exterior derivative, or exact identities on narrower selected function classes. It also does not prove every conceivable commutator closure must be nonzero for every input.

## 5. Direct numerical reproduction in supplied source-helper implementation

A stand-alone NumPy verifier tested the scalar product-defect formula, the exact spectral-mode expression and SOURCE HELPER's `compute_K_C/K_B/K_A_out` with H=I, f=sin x, g=cos 2x, `Identity`, stencil order2.

| N | dx | KC_xx full-grid RMS | KC_RMS/dx² | max_abs KB | max_abs KA |
|---:|---:|---:|---:|---:|---:|
| 9  | .69813170 | .804490616445 | 1.650616815 | 5.32e-17 | 1.06e-16 |
| 17 | .36959914 | .345568481473 | 2.529718697 | 9.17e-17 | 6.10e-16 |
| 31 | .20268340 | .117073925677 | 2.849862011 | 1.02e-16 | 1.73e-15 |

Scalar-vs-helper max component discrepancies were ≤1.1e-15, spectral formula reconstruction ≤2.4e-15, and all non-xx K_C components were zero.

Why do projected channels vanish? Since every generated tensor mode is purely H_xx and wavevector parallel e_x, the Fourier TT projector kills it. Moreover P_TT(L_C H)=0 already at the intermediate first application for each C. Therefore both KB and KA vanish. This is a *specific source-local input-class witness*; it does NOT imply every discrete Leibniz defect is harmless after other projections or for spatially varying generators.

Low/high frequency test in stand-alone scalar exact calculation:
| N | fixed k=(1,2) KC_RMS/dx² | growing k=(floor N/7,floor N/5) KC_RMS | high KC_RMS*dx² |
|---:|---:|---:|---:|
|31|2.849862011|5.89954196|.24235648|
|61|2.960477532|23.99436663|.25457125|
|121|2.989905463|90.65629827|.24444828|
|241|2.997452161|364.09211727|.24747819|

The source-local check thus validates the exact product-rule mechanism independently of geometric/projector mismatches. The helper printed its own metadata banner; hash of its read source was verified. Local reproduction code file
  int8_rot013_discrete_leibniz_commutator.py
  SHA256=3616ef2fab0c1964a2251b2a09c08da178f205c38594fbc945f70d7dfe0e088d.

## 6. Interaction with current DTC0a science and negative knowledge

XH-S4 ROT018 proved original smooth-source N31 alpha=.05 K_A-K_B mostly intermediate P insertion, with an exact tensor decomposition and stencil-mismatch swap tiny. This new witness does NOT compete with that: here h=I constant, C are one-coordinate fields, E=Identity; KA=KB=0 although KC≠0. So it is a genuine **negative control** showing why raw KC alone cannot diagnose physical geometric nonclosure, not an explanation of XH's actual K_A.

Three separable defect classes now have explicitly named controls:
(A) Lie product-rule / discrete Leibniz closure defect: exact `E_h`, present even without P.
(B) Fourier-k versus derivative-symbol-delta TT incompatibility: INT8 ROT008/012, depends on spectrum and tensor polarization.
(C) Intermediate projector insertion/commutator with variable C: XH-S4 ROT018, exact K_A-K_B identity.
These can coexist in general fields. Neither their coefficients nor residual RMS combine additively without source-level tensor decomposition; any physical mechanism assignment needs original provenance, fixed physical domain and source-valid continuum/regularity contract.

CHEAPEST DISCRIMINATOR for DTC validation owners (not new task assignment):
- Use one H=I, one-coordinate f and g test with E=Identity to assert K_C=2(E(g,Df)-E(f,Dg)) and KB=KA≈0;
- Pair with the existing XH ROT018 source h=fI and independent nonzero TT h case; keep actual E alpha settings and Fourier/mask conventions distinct;
- Only then test field-specific decomposition and compare with archived production, which is NOT done here.

The universal finite-grid derivation no-go gives no continuum anomaly, no K/J3 invariant, no “failure of Lie geometry” in physical spacetime, no FEEC host import, and no 4th-order historical run. E_lin(alpha!=0) and physical field class are NOT analyzed in (2.4).

## 7. One problem one state

problem_id: P3_DTC0A_DISCRETE_LIE_DERIVATION_PRODUCT_RULE_DEFECT_001
best_result: exact finite-grid Leibniz / Lie closure identity with source-helper verified pure-trace tensor witness and low-band O(h²) versus high-band O(h^-2) asymptotic.
prior_hosts: textbook finite differences, algebra of derivations on R^M, DTC source helper; M13 ROT18–22, XH-S4 ROT018, INT8 ROT008/012.
owner: M13 numerical validation, LT5 theoretical synthesis, KN11 source/BW; INT8 only a sourced analytic discriminator.
independent_referee: NOT_VERIFIED.
blocker: byte-identical historical DTC runner absent; full original K_A channels involve spatially varying f, E_lin and masks, so negative example cannot explain archived plateau.
cheapest_test: compare identity E=0-alpha source-helper scalar defect vs projected states in one matched scope; no demand of new owner run.
decision: PASS for exact source-helper conditional mathematical statement; HOLD any physical, continuum, original-runner or K_A explanation.
canonical_path: research/int8/2026-10-23/iw_int8_rot013_exact_discrete_leibniz_defect_lie_commutator_source_control_001.md
bw_state: GITHUB_PENDING_BW_INGEST / NO_OWNER_ACCEPTANCE_ASSUMED.

NO_NEW_TASK_CASCADE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
