---
artifact_id: GEEKY-S11-ROT014-ODD-RAW-TT-ALL-ALPHA-UNIFORM-RIGIDITY-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-25
problem_id: P3_DTC0A_ODD_N_SOURCE_RAW_K_TT_ALL_ALPHA_RIGIDITY_AND_COERCIVITY_001
class: EXACT_SOURCE_TYPED_RAW_K_FOURIER_TT_ALL_REAL_ALPHA_RIGIDITY_WITH_UNIFORM_LOWER_CERTIFICATE
exposure: PUBLIC_SAFE
status: ANALYTICAL_PROOF_AND_53_TYPED_NUMPY_CONTROLS_PASS / INDEPENDENT_REFEREE_PENDING
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: MATURE_DISCRETE_FOURIER_FRAME / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT014 — odd-N source-raw TT Lie-rigidity, including all exceptional scalar filters

## 0. Currentness, own claim subtraction, and test question

ROT002 already established a 12-axial-TT trace frame and rigidity on odd grids when the first-mode scalar filter multiplier is nonzero. ROT004–012 established distinct even-grid *matched derivative-symbol* TT projector preservation classes; these cannot be silently mapped onto the source's raw-wavevector projector. ROT013 clarified the **actual source-helper raw-k projector**, including its rank-five tracefree zero-mode convention, and showed a full-operator projector difference of norm 1 from the deliberately zero-at-k0 matched projector. INT8 owns separate shear-/metric-transport and TT principal-angle results; PRF11 owns continuum-vs-collocation Sobolev source commutator; M13 owns historical h=fI mask/source observables; XH-S4 owns geometric York. None is reattributed.

Question specific to ROT014: *can the actual retained source-helper raw-k projector on the odd grids support a uniform, all-real-alpha TT-preservation rigidity statement, despite ROT013's projector non-equivalence?* Answer yes, with an explicit positive resolution/alpha independent quantitative lower bound. This is an elementary finite Fourier/frame calculation within mature numerical analysis, NOT a priority or novelty claim.

## 1. Source-typed finite operator and exact original-helper semantics

On the 3-torus N³ grid with odd N>=7 and h=2π/N, use normalized full-grid vector and symmetric-tensor Frobenius L². Write

- D_j F(x)=[F(x+e_j)−F(x−e_j)]/(2h), centered second-order first difference.
- E_alpha=I+alpha h² Delta_2, scalar componentwise periodic 7-point filter, alpha ANY real number including negative, enormous, fine-tuned, or alpha_N varying with N.
- (L_C F)_ij=C^m D_m F_ij + F_mj D_i C^m + F_im D_j C^m, full 3-term source-style tensor Lie derivative.
- At each **nonzero** signed raw FFT wavevector k, `P_raw(k)` is the orthogonal symmetric traceless-transverse rank-2 tensor projector using direction k/|k|.
- At k=0 the original preserved helper defines **P_raw(0)F=F−tr(F)I/3** (rank FIVE). `Q_raw=I−P_raw`. Hence P_raw is tracefree at EVERY wavevector, including zero.

The exact retained file `/mnt/data/deepseek_python_20260627_a87249.py` was rehashed SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`. The present reproducer compares to its unchanged `apply_P_TT`, `apply_E` and `lie_derivative_tensor` at selected odd grids. This helper is NOT the still unavailable original `dtc0a_runtime_v0_3_1.py` production source. This note does NOT substitute the unmatched P_delta, nor change the source's k0 convention.

## 2. Theorem R14.1: exact ALL-alpha rigidity on odd grids

Let `Const={C(j)=a, a in R³}`. Then for every odd N>=7, every real alpha and every real grid vector field C,

**Q_raw L_C E_alpha P_raw = 0 on all real symmetric tensor grid fields IF AND ONLY IF C in Const.**

*Proof:* for any q=1,2 and each coordinate axis A choose two transverse traceless polarizations, with b,c the other axes:

`T_A^D=(e_b e_b^T−e_c e_c^T)/sqrt(3)` and
`T_A^O=(e_b e_c^T+e_c e_b^T)/sqrt(2)`.

For both phases cos(q h j_A), sin(q h j_A), these 12 real fields H are EXACT P_raw-TT, because their wavevectors are purely axial and nonzero. The sum of their squared normalized L² tensor norms is **5**, independent of N or q. Put `u_q=1−4 alpha sin²(qπ/N)` and `S°(DC)=dev sym(DC)`.

The trace of advection `C·D (E H)` vanishes since each input H is traceless; the remaining two Lie terms yield `tr(L_C E H)=2 u_q H_ij D_i C^j`. Orthogonality of the two real phases and the two orthogonal transverse polarizations gives the exact POINTWISE/Parseval axial identity

**sum_(12 axial H_q) || tr(L_C E_alpha H_q) ||² = 4 u_q² ||S°(DC)||².**

As P_raw always has traceless output (including k=0), `Q_raw L_C E P_raw=0` implies that identity's left side is 0. The two numbers `u_1,u_2` cannot both be 0: `sin²(π/N) != sin²(2π/N)` for odd N>=7. Therefore `S°(DC)=0`.

At Fourier k≠0, centered derivative vector `delta(k)=sin(hk)/h` is nonzero on ODD grids (there is no Nyquist zero). For any nonzero real 3-vector delta, the map `c -> dev sym(delta ⊗ c)` has singular values `|delta|/sqrt(2)` twice and `sqrt(2/3)|delta|` once, hence is injective. Thus every nonzero Fourier mode of C vanishes: C is constant.

Conversely, if C=a is constant, then `DC=0`, `L_a=a·D`, and E_alpha, D, P_raw are all Fourier-diagonal. They commute, hence `Q_raw L_a E_alpha P_raw=0`. Source k0 tracefree convention does not alter this. QED.

## 3. Theorem R14.2: uniform lower stability bound with no alpha exceptions

Define the full-grid constant-field distance

`d(C,Const)=sqrt(mean_grid |C(j)−mean_grid C|²)`.

For any odd N>=7 set `a_N=sin²(π/N)`, `b_N=sin²(2π/N)`, and `rho_N=(b_N−a_N)/(b_N+a_N)`. For any real alpha,

`max(|u_1|,|u_2|) >= rho_N` (sharp for the two scalar factors, at `alpha=1/[2(a_N+b_N)]`).

For each nonzero Fourier mode k, `|delta(k)|>=dmin_N=sin(π/N)/h`. The singular-value bound above therefore gives

`||S°(DC)||² >= (dmin_N²/2) d(C,Const)²`.

Since the source P_raw is a TRACEFREE orthogonal projector, `tr(Q_raw F)=tr(F)` and `||tr F||² <= 3||Q_raw F||²` pointwise. The exact 12-probe identity then gives

`sum_12 ||Q_raw L_C E_alpha H_q||² >= (2/3)u_q² dmin_N² d(C,Const)²`.

But all 12 input H_q lie in P_raw's range and have aggregate squared norm 5, so by the defining operator norm,

**||Q_raw L_C E_alpha P_raw||_(L²->L²) >= sqrt(2/15) dmin_N max(|u_1|,|u_2|) d(C,Const)**

**>= c_N d(C,Const), c_N=sqrt(2/15)*[sin(π/N)/(2π/N)]*[4cos²(π/N)−1]/[4cos²(π/N)+1].**

The functions `sin(x)/x` and `(4cos²x−1)/(4cos²x+1)` both grow as x=π/N decreases over N>=7. Consequently

**c_N >= c_7 = 0.09338559046080631 > 0**, uniformly for ALL odd N>=7 and real alpha, including alpha_N chosen adversarially. As N→∞, `c_N -> (3/10)*sqrt(2/15) = 0.10954451150103321`.

The certificate is NONSHARP for the full TT leakage operator. It bounds the absolute full-grid L² leakage, not the difference between two TT projectors, and not the continuum convergence rate. Specifically it does not contradict ROT013: the projectors may differ by norm 1 while each individually has a restricted rigidity statement.

## 4. Executed falsification controls and evidence

Standalone independently written NumPy implementation of **source-matching** P_raw including tracefree k0, centered D, source E_lin and full tensor Lie with both D(C) terms. Full 12 polarizations/phases were checked, rather than substituting the analytical inequality into a tautological test.

- **50 full 3D tensor cases:** odd N=7,9,11,15,31 crossed with seven alpha settings for generic seeded random C: 0, .05, .2, alpha_zero_q1, alpha_zero_q2, alpha_minimax_q1q2, -.7, plus two near-constant vector controls and one exactly constant control per grid (10 cases per N).
- **3 original-helper source-native comparison cases:** N=9,15,31, source C2=(.04cos z,0,.04sin x). Original unchanged `apply_P_TT` checked on both raw TT test input and its full Lie output, original `apply_E` and `lie_derivative_tensor` compared with independent implementation.
- Total 53 typed executed cases, **ALL PASS**. Maximum difference in the 12-field trace identity `3.1086244689504383e-15`, maximum non-TT contamination of TT probes `5.649205427211584e-16`, maximum original-helper versus independent discrepancy among P_raw/E/L comparisons `1.1784159000380967e-16`.
- Sample, N31 alpha=.05 generic field: `dist(C,Const)=0.07126121836511749`, witnessed 12-input lower bound on full operator norm `0.3838066742232649`, theoretical alpha-adaptive lower certificate `0.012961613562745144`, alpha-independent lower certificate `0.007750030028471321`. Witness itself is a LOWER operator bound, not the true operator norm.
- No historical mask, K_A measurement, underlying source vector C1/C2 experimental noise, curved metric, or original production runtime is reexecuted.

Code and JSON are in the user conversation archive. A clean copy of the original helper with independently checked SHA is included in the reproducibility ZIP. The package supports a clean re-execution via Python/NumPy; it is not a claim of having run a historical external lab or recovered unknown bytes.

## 5. Negative knowledge / exact transfer decisions

1. **Do not transfer** even-grid K6 or K_(6r³) results of ROT004–012 to the original source raw-k P; their projector family and grid parity differ.
2. **Do not infer** from ROT013 `||P_raw−P_delta||=1` that source P_raw lacks internal TT preservation rigidity. This turn proves a separate yes/no and lower certificate on odd grids.
3. **Do not claim** any exact result at even raw-k N where reality and Nyquist validation were historically problematic, or on different stencils/filters, masked norms, boundary conditions, or curved geometry.
4. Historical h=fI is pure trace and not a TT input; no identification of source K_A with the isolated leakage operator here. No gauge covariance, new physical K/J3 invariant, GR/GW, PBH/BBN or data discovery follows.
5. Classical Fourier multiplier frames and conformal-strain rigidity are mature hosts. No mathematical novelty/priority, independent referee acceptance, BW ingestion, owner scientific promotion or Moderator EXEC is asserted.

`NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / INDEPENDENT_REFEREE_PENDING / BW_PENDING`.
