---
artifact_id: GEEKY-S11-ROT012-UNIVERSAL-FOURIER-SHIFT-TT-KERNEL-AND-6R3-SINGLE-HOP-FAMILY-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-24
problem_id: P3_DTC0A_MATCHED_FOURIER_TT_DISCRETE_KERNEL_CLASSIFICATION_001
class: EXACT_FOURIER_SHIFT_LINEAR_ALGEBRA / ALL_ALPHA_SINGLE_HOP_KERNEL_AND_UNIFORM_STABILITY
exposure: PUBLIC_SAFE
status: PROOF_AND_THREE_INDEPENDENT_EXECUTED_NUMPY_CONTROLS_PASS / INDEPENDENT_REFEREE_PENDING
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: MATURE_DISCRETE_FOURIER_AND_NUMERICAL_NULLSPACE_HOST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT012 — universal Fourier-shift TT-preservation test, 6r³ kernel ladder, and uniform all-α stability

## 0. Currentness, owners-first, and novelty subtraction

Geeky-S11 ROT002 introduced an axial 12-probe trace frame; ROT003–006 isolated the even-grid Nyquist pathology and an exact K6 preserving family for central order-two; ROT007–010 showed that order-four standard/odd-offset/mixture hosts have very different ghost preservation; **ROT011 already proved** the parity criterion for arbitrary centered stencils and the 48-dimensional coarse-two-step preserving family for E=I. ROT012 does not reclaim those results. Its increments are: (i) a **general exact Fourier-shift rank formula** for any stencil on the subspace of generators annihilated by its derivative; (ii) a complete all-real-α infinite single-hop family r≥1, with exact dimension 6r³ and quantitative source-filter-independent coercivity; (iii) cross-checks against independently constructed 3D FFT code *and* a direct Fourier rank census.

INT8 owns filter equivariance/metric interface; PRF11 owns raw-k collocation and Sobolev sharpness; M13 owns historical h=fI source masked K_A; XH-S4 owns moving York and curved/Noether geometry; no priority displaced. Classical odd–even and decoupled-grid artifacts are extensively documented, including JCAM 333 (2018) DOI 10.1016/j.cam.2017.10.017 and mixed/staggered grid literature: https://academic.oup.com/gji/article/157/3/1269/568477. This is a special Fourier/TT calculation within a mature host, and **no original mathematical novelty is claimed**.

## 1. Precisely typed finite mathematical operator

The spatial domain is the **full unmasked** 3-torus sampled on an N³ periodic grid with h=2π/N. All norms are normalized real-grid L² with Frobenius tensor norm. Let D_j be a real, odd, translation-invariant grid derivative with Fourier symbol iδ_j(k); write δ(k)=(d(k_x),d(k_y),d(k_z)). Define the **matched-symbol** rank-two orthogonal Fourier tensor projector

- at δ(k)≠0: π(k)=I−δδᵀ/|δ|² and P(k)F=π F π−π tr(πF)/2;
- at δ(k)=0: P(k)=0, so Q=I−P.

Let E be **componentwise scalar Fourier-diagonal**, with multiplier e(k), in applications E_α=I+αh²Δ₂ where e_α(k)=1−4αΣ_j sin²(πk_j/N). Define the three-term source-style finite Lie action on symmetric covariant tensors:

(L_C F)_ij=C^m D_m F_ij+F_mj D_i C^m+F_im D_j C^m.

**Critical host typing:** P here is constructed from the *same modified derivative symbol*, NOT the historically archived DTC0a raw-wavevector projector; historical physical masked source h=fI is not a TT input. No moving metric-dependent York projector appears in this report.

## 2. Universal exact Fourier-shift criterion (Theorem R12.1)

Let Z={s∈(Z/N)³: δ(s)=0}, the zero-symbol generator spectrum. Suppose DC=0; Fourier expansion C(j)=Σ_(s∈Z) c_s exp(2πi s·j/N), with c_(-s)=conj(c_s) for a real C. Input H at one complex Fourier mode k can be chosen arbitrarily in P(k)'s TT fibre. Since DC=0, the tensor-gradient terms in L_C vanish and the **exact coefficient at output frequency k+s** is

  [Q L_C E P H]_(k+s) = i e(k) [c_s·δ(k)] Q(k+s)P(k) H_k.

For each s∈Z define its *failure-visible derivative-symbol span*

  W_s = span_R { δ(k) : e(k)≠0 and Q(k+s)P(k)≠0 },

where Q(k+s)P(k) is a matrix-to-matrix operator on symmetric tensors. The set excludes δ(k)=0 automatically (there P(k)=0). No cancellations among different generator frequencies occur for a fixed single-frequency input because their output frequencies k+s are distinct. Therefore

  **Q L_C E P=0 for a generator with DC=0 IFF c_s ∈ W_s^⊥ (complexified) for every s∈Z.**

For a *real* Fourier filter preserving conjugacy, ranks at s and −s agree. Consequently the exact **real** dimension of the preservation kernel *restricted to DC=0* is

  dim_R(K ∩ ker D) = Σ_(s∈Z) [3−rank_R(W_s)].

This is a finite, algorithmically checkable rank criterion, not a universal formula for the unconstrained kernel when a special filter annihilates every suitable axial trace probe. At active k, Q(k+s)P(k)=0 precisely when P(k+s)=P(k) (both rank two; if P(k+s)=0 then it is nonzero), i.e. when the derivative-symbol directions are parallel up to sign. Thus a geometry check reduces to comparing two **three-vectors** at k and k+s.

## 3. Closed-form single-hop theorem: K_(6r³) for EVERY real α (Theorem R12.2)

Fix a positive integer r and an even periodic N divisible by 2r with N≥6r. Define

  D_(r,h) f_j=[f_(j+r)−f_(j−r)]/(2rh),
  d_r(m)=sin(2πrm/N)/(rh),
  E_α=I+αh²Δ₂, α∈R arbitrary, including N/r-dependent tuning.

Let M=N/(2r)≥3. One-dimensional symbol zeros are exactly m=ℓM, ℓ=0,...,2r−1, so |Z|=(2r)³. Define the admissible shift set

  T_r={ M(ℓ_x,ℓ_y,ℓ_z) mod N : ℓ_i∈{0,...,2r−1}, ℓ_x≡ℓ_y≡ℓ_z (mod 2) }.

There are exactly 2r³ allowed shifts. Define K_r to be all real vector fields whose Fourier support is contained in T_r, with three arbitrary real-valued vector components subject only to the usual Fourier conjugation condition.

**THEOREM:** For each r≥1, N divisible by 2r with N≥6r, and **every α∈R**:

  **Q_r L_C^(r) E_α P_r = 0 on ALL symmetric tensors   IFF   C∈K_r,**
  **dim_R K_r = 3|T_r| = 6r³.**

The discrete conformal strain S°=dev sym(DC) has kernel dimension exactly 3(2r)³=24r³; thus only one-quarter of its real kernel vectors generate genuine preservation of the full TT sector.

*Proof necessity, 1: restrict to zero derivative support.* For q=1,2, define a_q=sin²(qπ/N), u_q=1−4αa_q. Since a_1<a_2, at least one u_q≠0 for every α. At that q the 12 real axial transverse-traceless sin/cos polarization carriers from Geeky ROT002 satisfy the **exact identity**

  Σ_12 ||tr(L_C E_α H)||² = 4u_q² ||dev sym(DC)||².

All P outputs are tracefree, so global QLEP=0 implies S°=0. Fourier mode by mode, the 3D algebraic map c↦dev sym(δ⊗c) is injective when δ≠0. Therefore C has Fourier support in Z (hence DC=0) — no other coefficients may survive.

*Proof necessity, 2: only same-parity shifts.* Write the zero-symbol shift s=Mℓ. Then d_r(k_j+s_j)=(-1)^(ℓ_j)d_r(k_j) exactly. At any mixed-parity ℓ choose a coordinate pair (a,b) with opposite parities and a frequency q(e_a±e_b). Its TT polarisation T=v vᵀ−e_c e_cᵀ, v=(e_a∓e_b)/sqrt2, has nonzero Q-output under the sign-mismatched shift. The e multiplier on that input is v_q=1−8αa_q. Again v_1,v_2 cannot simultaneously vanish, and d_r(q)≠0 for both q=1,2 since M≥3. For each opposite-parity pair, the + and − carriers require c_(s,a)+c_(s,b)=0 and c_(s,a)−c_(s,b)=0, so those two coefficients vanish. At least two opposite-parity pairs exist for every mixed-parity ℓ, killing all three components c_s. Thus only s∈T_r survive.

*Proof sufficiency.* If ℓ has all coordinates even, δ(k+s)=+δ(k); if all odd, δ(k+s)=−δ(k). Consequently P(k+s)=P(k) for every k, including zero-symbol conventions. Every allowed character χ_s commutes with P and is annihilated by all D_j; therefore Q L_(χ_s b) E_α P=0 for any constant vector b. Linear combinations preserve the identity. QED.

## 4. Quantitative uniform-in-(r,N,α) lower certificate (Corollary R12.3)

For general real C (not necessarily DC=0), the same 12 axial probes plus 12 oblique probes at adaptively selected q∈{1,2} yield a **constructive nonsharp** operator lower bound. Define

  d_1 = sin(rh)/(rh),
  a=sin²(π/N), b=sin²(2π/N), ρ_N=(b−a)/(b+a).

Since N≥6r, min_(m:d_r(m)≠0)|d_r(m)|=d_1 and d_r(2)≥d_1. The 12 axial trace frame controls the nonzero-derivative Fourier modes of C with squared coefficient (2/3)d_1² max_q|u_q|². The 12 oblique full-Q probes control the **forbidden** zero-symbol modes (those with mixed parity) by 3 max_q[d_r(q)|v_q|]² times a positive sum of their squared vector Fourier amplitudes. The latter lower bound still holds for arbitrary C because different C Fourier modes map one complex input k to distinct output k+s and sin/cos phase pairing cancels cross terms. These two orthogonal classes of C frequencies have squared distances adding by Parseval. The sum of 24 squared TT probe input norms is 17. Finally for 0<a<b,

  max(|1−ta|,|1−tb|)≥(b−a)/(b+a)=ρ_N for every t∈R.

It follows rigorously that

  **||Q_r L_C E_α P_r||_(L²→L²) ≥ c_(r,N) dist_L²(C,K_r)**,

  **c_(r,N)=d_1 ρ_N sqrt(2/51).**

This bound holds for all real α, even if a single axial or oblique first harmonic is erased. Moreover N≥6r implies rh≤π/3 and N≥6. Thus d_1≥sin(π/3)/(π/3), ρ_N≥1/2, giving the completely **uniform** lower floor

  **c_(r,N) ≥ c_* = [3sqrt3/(4π)]sqrt(2/51) = 0.08188454267608969**

for *all* positive integer r, all admissible N, and all real α. The coefficient is a certified LOWER bound, not the exact operator norm and not an upper error estimator. All fields, normalizations and projections remain full-grid mathematical.

## 5. Three complementary numerical controls (EXECUTED)

**Control A — full real-space 3D tensor action and FFT P.** `geeky_s11_rot012_zero_symbol_shift_kernel_verify.py`: 4 grids (r,N)=(1,12),(2,12),(3,18),(4,24), 4 α per grid including α tuned to erase one of the oblique harmonics q=1 or 2; 16 cases. For each, real random C whose Fourier support is the predicted T_r was tested against a *broadband random TT tensor*, and an explicitly forbidden generator at Fourier s=(M,0,0) against **two independently constructed oblique TT carriers**. Total 16 preserving controls plus 32 exact falsifier formula checks PASS. Max predicted-versus-measured two-probe leakage error 5.897871517101763e−15; max preservation relative leakage 1.0442738242917642e−15. The inputs use the full source-style Lie tensor, not only advection.

**Control B — independent complete shift-rank census.** `geeky_s11_rot012_shift_rank_census.py`: no tensor Lie and no special two-polarization witness construction. For each zero-symbol generator mode s, directly enumerates all Fourier input modes k, flags any change in the TT normal under k↦k+s, computes rank W_s by SVD of the flagged δ(k) 3-vectors, and totals Σ(3−rank W_s). Main 10 census cases cover the four single-hop r, plus odd-only fourth order, standard fourth order and 30% mixed fourth order. In each single-hop case all 2r³ allowed shifts have rank0 and all 6r³ forbidden shifts have rank3. Additional 8 exceptional-alpha census stress cases (q=1 and q=2 oblique filter roots) have the same dimensions. For r=1,2,3,4 preservation dimensions=6,48,162,384; full strain nullity=24,192,648,1536. Fourth-order external-host contrast at N12: odd-only→dimension6, standard and mixed fourth-order→dimension3. All 18 PASS.

**Control C — direct 24-carrier quantitative certificate (shares the core D/P implementation of A, uses independent probe constructions).** `geeky_s11_rot012_quantitative_frame_verify.py`: 5 genuinely random full-grid C instances at r=1,2,3,4, including one exceptional α for r=4. It explicitly constructs 12 axial+12 oblique real TT carrier fields, applies the full real Lie tensor and Fourier Q, sums their norms and compares with c_(r,N)dist(C,K_r). 5/5 PASS, sum TT input norms² =17 exactly up to 4e−15; maximum axial trace-frame error 6.94e−17. Example r4,N24,α=.05: distance .1206130825580; certified lower .0117424394017, witnessed 24-probe ratio .1345176427024. The witnessed ratio is **not** the true operator norm.

Thus **16 + 32 + 18 + 5 = 71 case-level or witness checks**; count them by type rather than suggest 71 distinct production datasets. Source code, JSON for each control, and SHA manifest are shipped in one locally executed package. Execution uses only Python/NumPy; no Julia DTC production code is available. The independent scripts do not import the historic helper.

## 6. Scope, limitations and negative knowledge

- R12.1's rank criterion is **conditional on DC=0**; only with an additional viable axial TT trace band can it classify the *entire* generator kernel. R12.2 establishes that extra condition for its stated single-hop family using q1/q2 and all α.
- R12.2 requires N divisible by 2r and N≥6r; r and N are finite positive integers. No assertion at untested alias/folding endpoints or generic nonperiodic boundaries.
- P_D is a matched-central-symbol flat Fourier projector, NOT the original raw-wavevector DTC0a P_TT, not geometric York P_g or Einstein-covariant tensor transport. The historic even-N N32 raw projector pathology is **not repaired**.
- The high-frequency subgrid-preserving generators depend on the grid; no fixed smooth continuum symmetry or continuum field nondecay follows from the growing dimension.
- This does NOT replay historic source h=fI masked K_A, does NOT establish physical K/J3 invariance, a gauge field, GR violation, observable GW, PBH/BBN bound or any other physical endpoint.
- Classical FD grid decoupling is mature prior art. No new mathematics priority, referee pass, independent scientific owner adoption, BW ingest or Moderator EXEC authorization is claimed.

NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / INDEPENDENT_REFEREE_PENDING / BW_PENDING.
