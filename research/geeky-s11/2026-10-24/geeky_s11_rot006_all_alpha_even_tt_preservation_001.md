---
artifact_id: GEEKY-S11-ROT006-ALL-ALPHA-EVEN-TT-RIGIDITY-AND-UNIFORM-COERCIVITY-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-24
problem_id: P3_DTC0A_MATCHED_EVEN_N_TT_FILTER_BLINDSPOT_COMPLETION_001
class: EXACT_FINITE_FOURIER_ALL_REAL_FILTER_PARAMETER_THEOREM_AND_ADAPTIVE_PROBE_CERTIFICATE
exposure: PUBLIC_SAFE
status: MATHEMATICAL_PROOF_AND_108_CASE_NUMPY_CHECK_PASS / REFEREE_PENDING
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: MATCHED_CENTERED_SYMBOL_PDELTA / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT006 — No scalar E-linear filter tuning can enlarge the even-grid TT-preservation kernel

## 0. Scientific context, source audit, and subtraction

Geeky-S11 ROT002 proved exact axial TT trace-frame rigidity on ODD grids. ROT003 found an EVEN-grid checkerboard field whose full projected axial probe output vanishes despite genuine TT leakage on oblique inputs. ROT004 characterized the full EVEN-grid matched-symbol TT preservation kernel as K6={a+b χ111}, but assumed BOTH e1 and e2 nonzero, leaving exceptional scalar filters unclassified. ROT005 proved a quantitative lower bound on distance to K6 under the SAME nonzero-filter assumption. The present work removes that assumption for every REAL alpha and obtains a uniform-in-alpha positive lower certificate. It does not replace S11 ROT002-005 but strengthens the precise exception they left.

2026-10-24 source currentness: PRF11 R26/R27 have the original ODD-N RAW-wavevector projector source commutator Sobolev/alias and face-guard sharp results; INT8 ROT020-022 has shear-invariant filter locality and all-grid Fourier minimax; M13 controls the historical pure-trace DTC h=fI masks and asymptotics; XH-S4 owns moving York, non-Einstein TT and metric covariance. No transfer of novelty or result ownership between operator hosts. Original byte-exact DTC production runtime remains unavailable. Older matched-symbol proof: https://github.com/wmakiela-tech/Nash-iw-research/blob/a660eba871f58fae3d4ce2d1ec5351344fe27155/research/geeky-s11/2026-10-24/geeky_s11_rot004_even_nyquist_tt_kernel_and_finite_probe_classification_001.md . Quantitative previous report: https://github.com/wmakiela-tech/Nash-iw-research/blob/3b787afcad078b1f056091ce38c451e63dd3e506/research/geeky-s11/2026-10-24/geeky_s11_rot005_even_tt_distance_coercivity_001.md .

## 1. Exact mathematical host

Even periodic N>=6, h=2π/N. Let D_i be the centered first difference and Δ_h the seven-point centered scalar Laplacian. Define E_{α,h}=I+αh²Δ_h acting componentwise on rank-two symmetric tensors, with ANY α in REAL numbers (including negative and N-dependent). Define (L_{C,h}F)_ij=C^m D_m F_ij+F_mj D_i C^m+F_im D_j C^m. Matched TT Fourier projector P_delta uses δ_j(k)=sin(k_j h)/h and its orthogonal TT projector at δ!=0, while P_delta(k)=0 at the eight δ=0 Fourier corners. This is NOT the historic source raw-wavevector projector; Q_delta=I-P_delta. Unmasked full-grid L² Frobenius norms throughout.

Let χ111(j)=(-1)^(j_x+j_y+j_z) and K6={a+b χ111 | a,b∈R³}. For q=1,2 define the axial and oblique scalar E multipliers

u_q(α)=1−4α sin²(qπ/N),  v_q(α)=1−8α sin²(qπ/N),  s_q=sin(2π q/N)/(2π/N).

Let a_N=sin²(π/N), b_N=sin²(2π/N), with 0<a_N<b_N for EVEN N>=6. Let ρ_N=(b_N−a_N)/(b_N+a_N)>0. Note s_2>=s_1>0 for N>=6.

## 2. Complete all-alpha exact preservation classification — Theorem 006.1

For ALL α∈R, even N>=6 and arbitrary real periodic vector fields C,

    Q_delta L_{C,h} E_{α,h} P_delta = 0
        iff  C∈K6.

**Proof.** At frequency q e_axis and polarization orthogonal to that axis, the 12 axial sine/cos TT fields are exactly in ran P_delta and the E multiplier is u_q. Repeating the elementary trace-frame identity ROT002 at ANY q∈{1,2} yields

    sum_(12 axial at q) ||tr(L_C Eα H)||² = 4u_q(α)² ||dev sym(D C)||².

Since a_N≠b_N, u_1 and u_2 cannot vanish simultaneously for any real α. If whole-TT is preserved, choosing q with u_q≠0 proves dev sym(D C)=0, hence all C modes lie in the eight centered-symbol Nyquist corners, by the same symbol injectivity as ROT004.

For C supported on those eight corners, the 12 oblique TT probes at carrier (q, ±q, 0), for any q∈{1,2}, yield an exact Parseval identity

    sum_(12 oblique at q)||Q_delta L_C Eα H||² = 3 v_q(α)² s_q² W(C),
    W(C)=sum_(m corners)sum_(i<j:m_i≠m_j)(|c_{m,i}|²+|c_{m,j}|²).

Here χ_m are the eight corner Fourier characters and c_m their real vector coefficients. The formula is obtained exactly as ROT004, with s_q replacing s_1; sine/cos phase pairing cancels possible ±k spectral interference. For each proper corner m not 000 or 111, W_m≥|c_m|². Since v_1 and v_2 cannot vanish simultaneously, zero whole-TT leakage forces W=0 and C∈K6.

Conversely, every C=a+bχ111 satisfies D C=0. χ111 shifts each frequency by all-three-coordinate Nyquist, under which δ→−δ and P_delta is unchanged. Thus multiplication by χ111 commutes with P_delta, and centered D and E are Fourier multipliers commuting with P_delta. Q_delta L_C E P_delta=0. QED.

This removes BOTH exceptional e1=0 and e2=0 cases from ROT004 without introducing a new projector.

## 3. Quantitative all-alpha coercivity and constructive finite tests — Theorem 006.2

Choose q_a∈{1,2} maximizing |u_q(α)| and q_o∈{1,2} maximizing |s_q v_q(α)|. Use 12 axial TT fields at q_a and 12 oblique TT fields at q_o. These are 24 real fields, each with appropriate sine/cos phases. Their total squared full-grid input L² norms remain 5+12=17.

Decompose C=C_noncorners + sum_m χ_m c_m. The axial trace frame plus tr(QF)=tr F and |tr F|²≤3||QF||² gives

    sum_axial ||Q L_C E H||² >= (4/3)|u_qa|² ||dev sym D C||²
      >= (2/3)s_1² |u_qa|² ||C_noncorners||².

The second inequality follows from Fourier singular values of dev sym(δ⊗v): the smallest is |δ|/√2 and the smallest nonzero |δ| is s_1. For the oblique fields, **even for arbitrary C**, distinct generator Fourier modes map each fixed complex probe carrier k to distinct k+m modulo N and P_delta is frequency-diagonal. Pairing cos and sin removes opposite-carrier interference. Therefore the sum of projected output energies is at least the contribution of C's six proper Nyquist corners:

    sum_oblique ||Q L_C E H||² >= 3 |v_qo|² s_qo² W(C)
        >= 3 |v_qo|² s_qo² ||C_proper_corners||².

All 24 TT probe outputs together are bounded above by 17||Q L_C E P||². By Parseval orthogonality dist(C,K6)²=||C_noncorners||²+||C_proper_corners||². Thus

    ||Q_delta L_C E_alpha P_delta||_(L²→L²)
      >= c_N(α) dist_L²(C,K6),

    c_N(α) = [ min( sqrt(2/3)*s_1*max_q|u_q(α)|,
                        sqrt(3)*max_q |s_q v_q(α)| ) ]/sqrt(17).

Here the 24 probes are **adaptive** in alpha, but the 48-probe union of q=1 and q=2 bands is a fixed complete suite for every real alpha.

**Uniform alpha-independent coefficient.** For any 0<a<b and ANY real t,

    max(|1−ta|,|1−tb|) >= (b−a)/(b+a),

with equality only at t=2/(a+b). Apply once at t=4alpha, once at t=8alpha. Also s_2>=s_1>0. Then

    c_N(α) >= c_N,unif
      := [sin(2π/N)/(2π/N)] * ρ_N * sqrt(2/51) > 0,

for **ALL real alpha, even if alpha depends on N or diverges**. On the even-grid refinement sequence N→∞, ρ_N→3/5, s_1→1, and

    c_N,unif -> (3/5)*sqrt(2/51) ≈ 0.118817705157.

The absolute TT leakage cannot be driven to zero for a family of generators at uniformly nonzero distance to K6 merely by scalar E_lin tuning. This statement is within the matched-symbol host, NOT a claim that source historical KA or continuum commutator errors are alpha-untunable; PRF11 R26, INT8 ROT020-022 study distinct carriers.

## 4. Reproducibility / adversarial verification

Executable Python `geeky_s11_rot006_all_alpha_two_band_verify.py` imports *the independent publicly archived ROT005 NumPy module* in the same folder, specifically `geeky_s11_rot005_quantitative_tt_distance_verify.py`; both source files are included in the local ZIP with a SHA256 manifest. The reproducer computes full tensor Lie, finite difference, E, Fourier P_delta and all 24 selected TT fields, without supplying the analytic answer to the operator outputs.

For even N=6,8,10,12 and 9 filter values (0, .05, .2, q1/q2 axial zero, q1/q2 oblique zero, axial/oblique two-band minimax), test each of three generator classes (generic random, within 0.001 random error of K6, EXACT K6). Total **108 executed cases**; all exact trace-frame identities, TT probe status, proper-corner energy lower bounds, alpha-independent coefficient, and 24-probe witnessed operator bound PASS. Recorded summary:

- max axial trace-frame absolute error 2.6645352591003757e-15;
- max proper-corner energy excess over actual oblique output −6.974240428780175e−33;
- max TT-input relative P_delta error 8.325901660779925e−16;
- min witnessed-minus-certified norm −9.08525419980466e−16, due solely to floating roundoff in exact-K6 controls; numerical pass tolerance explicit (3e−10 on energies).

The test includes specially tuned alpha values where the ORIGINAL ROT004 q=1 argument breaks. It does NOT test original even-N historic raw-k production runtime or a physical model. The proof, not finite numeric tests, licenses all even N and every real alpha.

## 5. Branch decision and claim guards

STOP treating special e1=0 or e2=0 filter values as plausible paths to nontrivial TT-preserving generators beyond K6. The two-band algebra rules them out. A near-preserving TT generator has quantitative proximity to K6 under a strictly positive alpha-independent finite-grid coefficient (as N→∞, the lower coefficient remains positive). The result is model-specific and a mature linear Fourier/frame argument. No novelty, mathematical independent referee PASS, BW ingress, EXEC, historical original-source projector validation, physical K/J3 invariance or physical gauge upgrade claimed.

NO_NEW_TASK / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / INDEPENDENT_REFEREE_PENDING / BW_PENDING.
