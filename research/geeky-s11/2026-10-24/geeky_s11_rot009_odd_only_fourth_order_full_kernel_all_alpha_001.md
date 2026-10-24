---
artifact_id: GEEKY-S11-ROT009-ODD-STENCIL-FOURTH-ORDER-ALL-ALPHA-K6-QUANTITATIVE-TT-RIGIDITY-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-24
problem_id: P3_DTC0A_EVEN_N_MATCHED_TT_STENCIL_PARITY_FULL_KERNEL_AND_STABILITY_001
class: EXACT_FOURIER_OPERATOR_KERNEL_AND_UNIFORM_COERCIVITY_FOR_ODD_STEP_ORDER4
exposure: PUBLIC_SAFE
status: MATHEMATICAL_PROOF_AND_120_CASE_NUMPY_PASS / REFEREE_PENDING
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: MATURE_FINITE_FOURIER_OPERATOR_HOST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT009 — full even-grid TT preservation kernel of odd-offset fourth-order stencil, all alpha

## 0. Question, priority and precise host

ROT008 Geeky-S11 introduced an odd-offset fourth-order centered derivative that preserves the Nyquist full-checkerboard vector generator while the *standard* fourth-order derivative does not. ROT008 proved the full six-dimensional preserving-kernel claim only conditionally on nonzero first-band filter factors, and did **not** establish an all-alpha kernel/quantitative coercivity theorem. ROT006 independently established these conclusions for the **other** second-order derivative. This note fills the remaining exact all-real-alpha mathematical gap for the **odd-offset fourth-order** host. INT8 ROT018–023, PRF11 R23–R27, M13 historic h=fI masked K_A, and XH-S4 moving/curved York stay separately owned. Mature Fourier/TT projector mathematics, NOT a novelty claim.

On periodic even N>=6, spacing h=2pi/N, define

D_o4 f(j) = [ (9/8)*(f(j+1)-f(j-1)) -(1/24)*(f(j+3)-f(j-3)) ]/(2h),

d_o4(theta) = (sin(theta)/h)*(1+sin(theta)^2/6).

Use the unchanged componentwise DTC-like centered scalar filter E_alpha=I+alpha*h²*Delta_2, any **real** alpha including grid-dependent, and source-style symmetric covariant tensor action

(L_C F)_ij=C^m D_m F_ij +F_mj D_i C^m +F_im D_j C^m.

Define P=P_(TT,d_o4) by the raw orthogonal tensor TT multiplier constructed from **the matched derivative symbol** delta_i(k)=d_o4(k_i h): pi=I-delta delta^T/|delta|², P F=pi F pi -pi tr(pi F)/2 where delta!=0, and P=0 on all eight zero-symbol corners. Q=I-P. This is NOT the archived historically invalid even-N raw-wavevector DTC0a projector, nor a geometric moving York P_g. Full-grid normalized Frobenius L2 throughout.

## 1. Exact classification, no exceptional alpha

Let chi(j)=(-1)^(jx+jy+jz), K6={a+b chi : a,b in R³}.

THEOREM R9.1: For any even N>=6 and any real alpha,

**Q L_C E_alpha P=0 on all tensors if and only if C belongs to K6.**

Proof, necessity. d_o4(theta) vanishes exactly at theta=0,pi since its factor 1+sin²(theta)/6 is strictly positive. Thus discrete conformal strain dev sym(D C) has kernel precisely the 24 real coefficients c_m of the eight Fourier corners m in {0,1}³. For q=1,2 let a_q=sin²(q pi/N), u_q=1-4alpha*a_q and v_q=1-8alpha*a_q. Since a1<a2, u1 and u2 cannot both vanish, nor can v1 and v2.

For each q, 12 exactly TT axial cosine/sine polarization carriers (three axes times two standard transverse polarizations times two real phases) give the exact frame:

sum_12 axial ||tr(L_C E_alpha H)||² = 4 u_q² ||dev sym(D C)||².

Every P-output is tracefree; hence whole-TT preservation and some nonzero u_q imply dev sym(D C)=0. Then C=sum_(m corners) c_m chi_m, so D C=0. Consider 12 exactly TT oblique carriers (three coordinate pairs, two signs, two phases) at frequency q(e_a ± e_b), using T=v v^T-e_c e_c^T, v=(e_a∓e_b)/sqrt2. For corner-supported C, antipodal symbol under partial Nyquist shifts yields exact Parseval identity:

sum_12 oblique ||Q L_C E_alpha H||² = 3 v_q² d_q² W,
d_q = d_o4(qh),
W = sum_(m corners) sum_(a<b with m_a!=m_b) (|c_m,a|²+|c_m,b|²).

For each of six proper corners m not 000/111, its term W_m>=|c_m|². Choosing one q for which v_q!=0 and requiring whole-TT preservation forces proper corner coefficients to vanish. Thus C=a+b chi.

Sufficiency. D chi=0; multiplication by chi shifts all three coordinates by Nyquist, and d_o4(theta+pi)=-d_o4(theta), hence P(k+Nyquist_111)=P(k) for all k, including zero-symbol modes. Multiplication by chi commutes with P, and scalar E and D are diagonal Fourier multipliers that commute with P. Therefore Q L_(a+b chi) E P=0 for all alpha. QED.

## 2. Quantitative all-alpha stability

Let dist(C,K6) denote normalized full-grid vector L2 distance. Put

d1=sin(h)*(1+sin²(h)/6)/h,
d2=sin(2h)*(1+sin²(2h)/6)/h,
a=sin²(pi/N), b=sin²(2pi/N), rho=(b-a)/(b+a).

Here d1>0, d2>=d1 for even N>=6 and d1 is the smallest nonzero absolute discrete d_o4 symbol. Let q_a maximize |u_q| and q_o maximize d_q |v_q| over q∈{1,2}. These choose **24 exactly TT real probes** with sum of squared input Frobenius L2 norms=17. Axial trace frame and min singular value d1/sqrt2 of dev sym(delta⊗C) control the noncorner coefficients:

sum_axial ||Q L_C E H||² >= (2/3)*d1²*u_qa²*||C_noncorner||².

The 12 oblique Q energies, for any C, dominate the contribution from its six proper Nyquist corners: distinct generator Fourier modes map each complex probe k to distinct output modes, Q is Fourier-diagonal, and cos/sin phase pairing cancels opposite-carrier cross terms. Thus

sum_oblique ||Q L_C E H||² >= 3*d_qo²*v_qo²*||C_propercorner||².

Parseval gives dist(C,K6)²=||C_noncorner||²+||C_propercorner||². Therefore the full operator norm obeys the explicit nonsharp lower bound

**||Q L_C E_alpha P||_(L2->L2) >= c_adaptive(N,alpha) * dist(C,K6)**

c_adaptive = min(sqrt(2/3)*d1*max_q|u_q|, sqrt3*max_q(d_q*|v_q|))/sqrt17.

For any real t and 0<a<b: max(|1-ta|,|1-tb|)>=(b-a)/(b+a)=rho. Apply to 4alpha and 8alpha; since d2>=d1,

**||Q L_C E_alpha P|| >= d1 * rho * sqrt(2/51) * dist(C,K6)**

for ALL real alpha, including tuned, exceptional, negative, unbounded or N-dependent values. As N approaches infinity along even values, this uniformly positive coefficient tends (3/5)*sqrt(2/51)=0.118817705157. This is a lower certificate for *absolute fixed-projector leakage*, not a claim about discrete-to-continuum consistency or physical K/J3.

The same kernel reasoning extends conditionally to other **odd-offset-only centered first-derivative stencils** having no extra sampled Fourier zeros and nonzero first/second harmonic symbols, but the quantitative derivative-symbol constant then changes. ROT009 executes only the specific fourth-order stencil.

## 3. Standalone independent verification, provenance and limits

Standalone NumPy script implements ±1/±3 derivatives, unchanged ±1 E_alpha, full tensor Lie derivative, independently built Fourier matched P, phase-resolved 12+12 TT frames and direct norm comparisons. Four even N={6,8,10,12}, nine alpha values {0,.05,.2,1/(4a),1/(4b),1/(8a),1/(8b),-.7,-3}, three real generator classes {generic random, K6 plus 10^-4 perturbation, exact K6} yield **108/108 PASS**. Twelve additional broadband random TT K6 controls PASS.

Max absolute axial frame residual 5.329070518200751e-15; minimum oblique minus required proper-corner lower energy +9.898507838467054e-33; minimum witnessed norm² minus derived coercivity norm² -9.63841656239707e-30 (floating roundoff in exact K6 null cases); max broadband relative leakage from K6 5.129721274391709e-15. Local reproducibility files:
- geeky_s11_rot009_odd_only_fourth_order_full_kernel_all_alpha_001.md (full detail)
- geeky_s11_rot009_odd_stencil_all_alpha_kernel_verify.py (original independent executed source)
- geeky_s11_rot009_odd_stencil_all_alpha_kernel_results.json (108 rows plus 12 controls)
- geeky_s11_rot009_SHA256SUMS.json and ZIP.
All local SHA256 3/3, clean unzip, direct NumPy rerun and BYTE-IDENTICAL JSON replay PASS. Original historical DTC0a production runtime byte-unavailable; no false source-replay claim.

NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_REFEREE_PASS / GITHUB_SAVED != BW_INGESTED.
