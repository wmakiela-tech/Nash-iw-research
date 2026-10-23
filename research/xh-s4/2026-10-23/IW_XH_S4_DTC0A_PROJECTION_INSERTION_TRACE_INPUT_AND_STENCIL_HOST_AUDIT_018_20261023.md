# XH-S4 — obrót 018: dokładna dekompozycja K_A−K_B, wejście czysto śladowe, zgodność P_TT/E i testy komutatora

RETURN_ID: XH-S4-MAYOCT2026-TT-PROJECTION-LEAKAGE-TRACE-INPUT-STENCIL-018_20261023
DATE: 2026-10-23
CELL: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03 / XH-S4
RESULT_CLASS: EXACT_FINITE_OPERATOR_IDENTITY / INDEPENDENT_NUMERIC_REPRO / NEW_SOURCE_TO_HOST_RESEARCH_QUESTIONS
SCOPE: finite periodic N=9,17,31, alpha=0,0.05,0.2; NumPy, unweighted Frobenius RMS /6 and inner mask slice(3,N-3). Pure mathematical/algorithmic; not a physical conclusion.
CLAIM_CEILING: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_K_J3 / NO_CONTINUUM_THEOREM / NO_BW_INGESTION_ASSUMPTION / NO_NEW_OWNER_TASKS

## 1. Grounded source and provenance
DTC verification runtime user-supplied local source `deepseek_python_20260627_a87249.py`, SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`.
Relevant source-defined functions: `apply_E`, `lie_derivative_tensor`, `apply_P_TT`, `projected_T`, `compute_K_C`, `compute_K_B`, `compute_K_A_out`, `generate_smooth_fields`, and `rms_norm`.
Frozen baseline CSV `dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv` used for **numeric same-definition comparison**, not a claim of full original production-run hash reconstruction.
Source `apply_P_TT` uses Fourier k multiplier Pij=deltaij−kikj/k² for nonzero modes, TT operator `P_i a H_ab P_b j − .5 P_ij (P_ab H_ab)`; at zero spatial frequency tracefree `H−tr(H)/3 I`. `E_lin` is componentwise `I+alpha*dx²*Delta_h`, centered second difference, and Lie tensor transport uses central first difference plus two stretching terms.
Independent reproduction: a standalone NumPy translation of exact finite algebra; checked N31 alpha=0,.05,.2 `K_A,K_B,K_C` match supplied archived CSV to roundoff. This is source-definition verification, not integration into original runtime.
Inputs: C1^x=.05 sin x, C1^y=.05 cos y, C2^x=.04 cos z, C2^z=.04 sin x; h_ij(x)=f(x,y) delta_ij, f=.1 sin x cos y.
Mask: used ONLY in final scalar RMS readout; no masking inside projection or T compositions.

## 2. Exact symbolic decomposition: what K_A actually measures
Write `P=P_TT`, `Q=I−P`, `L_i=Lie_Ci ∘ E`, `L_b=Lie_[C1,C2] ∘ E`, on the same finite symmetric tensor space. By code:
  K_C=[L1,L2]h − L_b h
  K_B=P K_C
  K_A=P L1 P L2 h − P L2 P L1 h − P L_b h.
Therefore exactly on each finite grid and each h, independently of alpha and the projection's idempotence:
  **K_A−K_B = P L2 Q L1 h − P L1 Q L2 h.**
This is an algebraic identity, not a new physical invariant, not a general Lie-representation theorem.
If QL1h=QL2h=0, then K_A=K_B on the selected h. Conversely, large K_A−K_B measures unretained intermediate components reentering P through the second transport, but does not prove the underlying continuum mathematical action should preserve TT.
At N31, alpha=.05, masked RMS:
  K_C = 2.1337231454168935e−6
  K_B = 4.4362003755635207e−7
  K_A = 3.76475685320836e−5
  exact difference ||K_A−K_B||_mask=3.744230361092206e−5
  RHS two leakage terms separately 2.4769648931e−5, 3.2457503901e−5 (these add as tensors with cancellation/interference; NOT scalar additive decomposition).
  identity residual RMS =2.77e−20; for alpha0,.2 also <3e−20. Ratio ||K_A−K_B||/||K_A|| approx .9945, but scalar RMS ratios are NOT attribution of signal energy fractions or proof of causality.
The ratio ||K_A||/||K_B||≈84.86 in this host. This computation DIRECTLY pins the excess above K_B to intermediate inserted P operations; does not determine physical legitimacy.

## 3. Crucial source input-class issue: h=f(x,y) I is pure trace, P_TT h=0
For nonzero k, TT(f I)= f P−.5*P*(tr P)f = fP−.5*2 fP=0. At k=0, tracefree projector of fI also zero. This is an exact algebraic result on every grid. Independent N31 FFT code gave `||P h||_RMS = 7.8e−34` (floating error; companion different implementation ~2.2e−18).
Thus the benchmark K_A is evaluated from an INITIAL H that contains NO transverse-traceless component. It measures the TT part generated and transformed by Lie actions on a pure-trace symmetric input. It cannot alone establish the defect restricted to TT initial states or a physical TT sector. IMPORTANT: zero P(h) does NOT imply P(L_C h)=0 for variable C.
New separate frozen nonzero-TT probe `h_alt=P_TT H_alt`, H_alt off-diagonal smooth three-mode sines/cosines, h_alt normalized to same GLOBAL symmetric Frobenius RMS as original h. NOT matched spectral support, same tensor class or source process:
  N31 alpha=.05: ||K_A||_mask original trace input=3.7647568532e−5;
  N31 alpha=.05: ||K_A||_mask new nonzero TT=3.2234720316e−5.
  alpha0: 3.7885297593e−5 vs 3.2833410042e−5.
  alpha.2: 3.6947235258e−5 vs 3.0716551332e−5.
So residual persists for one TT admissible test but its magnitude depends on field class. No operator-norm lower-to-upper transfer or continuum inference.

## 4. Exact commutation vs true source of noncommutation
Both P_TT and E_lin are PERIODIC Fourier multipliers. At each k, E(k)=e_alpha(k) I on tensor components; P(k) is a matrix (linear map on symmetric tensors). Therefore **[P_TT,E_lin]=0 exactly**, for all alpha including when E_lin is signed. Similarly the centered derivative D_j is a scalar Fourier multiplier and [P,D_j]=0 (both with the stated zero mode).
For spatially CONSTANT vector field C0, Lie_C0= C0·D and its stretching terms vanish, so **[P,L_C0]=0 exactly** as well.
For VARIABLE C, Lie_C has multiplication by C and by spatial derivative of C, which generically does NOT commute with nonlocal P: `[P,L_C]=[P,Lie_C]E`; no direct spectral-flattening simplification.
Independent finite-grid measured on an auxiliary smooth symmetric probe N31 alpha=.05:
 ||[P,E]probe||_RMS=1.93e−17
 ||[P,L_constant]probe||_RMS=2.35e−18
 ||[P,L_variable]probe||_RMS=1.6955628296e−3.
Last is only a probe response in a DIFFERENT input/normalization from original K_A; NOT a full commutator norm nor direct explanation of its magnitude. Mask not applied in these global commutator tests.
Mathematical implication: changing alpha cannot directly create a nonzero [P,E]; alpha can modify the transported signal and [P,Lie_C]E, while stencil-vs-continuum k only changes the P definition.

## 5. Stencil-compatible alternative P versus continuous-k P
Original P_TT uses k_i=2pi*fftfreq while centered derivative D has Fourier symbol i sin(k_i dx)/dx. Define a comparison projector P_sin with q_i=sin(k_i dx)/dx in TT formula (odd N avoids additional zero q-axis modes); handle q=0 with same tracefree zero mode.
At N31 alpha=.05, original trace input:
 - K_A(P_k)=3.76475685320836e−5
 - K_A(P_sin)=3.76830398966237e−5; relative +0.0942%.
 New nonzero TT input (prepared with P_k):
 - K_A(P_k)=3.22347203162382e−5
 - K_A(P_sin)=3.21684236037394e−5; relative −0.206%.
Thus replacing k by the centered stencil's effective wavevector does NOT eliminate plateau at this N and field: an empirical falsification of "almost all original K_A is caused solely by k-vs-sin(kdx) mismatch" in the tested setup.
Not a proof continuum P_k and P_sin have same convergence order or are gauge-equivalent, nor a proposal to silently replace accepted DTC projection. Mathematical exactness of P_sin under centered divergence differs from physical definition of transverse tensor and must be separately specified.

## 6. New 2026 literature and strictly typed links
PRIMARY SOURCE NEW, full HTML:
Elia Brué, Maria Colombo, Guido De Philippis, Carl Johan Peter Johansson, *Regularity estimates in transport equations via heat flow and quantitative differentiation*, arXiv:2607.13751v1 (15 Jul 2026), https://arxiv.org/html/2607.13751 . In a *SCALAR* transport equation and DiPerna–Lions/Ambrosio–Trevisan regularization, commutator `[b·∇,rho_eps*]u` is controlled under Sobolev/incompressible hypotheses. Theorem 1.1 involves symmetric gradient of b in a logarithmic scale estimate; this is a METHODOLOGY PRIOR ART showing how regularity of b enters commutators. It is NOT a theorem bounding [P_TT, tensor Lie_C].
RELATED 2026 JOURNAL publication (preprint 2024): Daniel Goodair, *High order smoothness for stochastic Navier-Stokes equations with transport and stretching noise on bounded domains*, Nonlinear Analysis 267 (June 2026) 114054, DOI https://doi.org/10.1016/j.na.2025.114054; accessible publisher ABSTRACT only (full theorem not audited). Studies cancellations and energy estimates with LERAY vector projection, Stokes operator and transport-stretching noise; different field rank, domain, stochastic assumptions. It confirms projector/transport interaction matters under suitable host but is NO DIRECT TT estimate.
2026 July JOURNAL version of preprint Jan: Hess-Childs, Rosenzweig, Serfaty, *Another look at regularity in transport-commutator estimates*, Comptes Rendus Math. 364 (published July 27 2026), DOI https://doi.org/10.5802/crmath.837 . RIESZ kernel commutators, authors show grad-velocity L∞ cannot generally be replaced by BMO except one endpoint; regularity requirements are source-kernel-dependent, preventing unjustified import of loose gradient assumptions to TT.
Cumulative link: Wittig Aug finite-range pseudospectral certificate needs controlled commutator with localization, while current TT is Fourier global; July transport commutator analysis gives research direction for *new host-specific estimate*, not an available certificate. FEEC Oct 2610.01501 operator-norm source independent, not a TT K_A theorem.

## 7. Explicit questions, competing hypotheses, discriminators
**Q32 / P0**: Can ||[P_TT,Lie_C]E|| be bounded (in what Sobolev/weighted operator norm) in terms of source-restricted gradients of C, with exact definitions of tensor field and boundary/zero mode? H_geometry: TT space not invariant for variable flow; H_numeric: stronger defect comes from stencil or numerical artifact; H_cancellation: structural cancellation for a restricted C/h sector. Test constant C controls, variable C amplitude/wavenumber class, nonzero TT/trace inputs, fixed h normalization, N scaling, inner vs global norm. Source commutator theorem HOST NOT YET PROVED.
**Q33 / P0**: Is project-observed K_A for trace-only h predictive for physical TT-initial h at all? H_trace depends on trace generation; H_TT independent target depends on TT sector. Already demonstrated one TT input differs but does not annihilate defect. Declare input restriction FIRST.
**Q34 / P1**: Does substituting P_sin for P_k remove defect? Falsified as DOMINANT explanation in N31 smooth-control, because change ~0.1% of K_A. Wider field and N class untested.
**Q35 / P1**: Can certified upper control of Q L_C P and P L_C Q over a specified smooth band translate exact leakage identity into target-specific bound on K_A−K_B? If yes, legal operator estimates and field Sobolev norms; sampled-field ratio alone insufficient. This asks for prior-art subtraction against commutator and pseudodifferential calculus rather than asserting new mathematical theorem.
No tasks sent to other cells; source science and test results routed informationally only.

## 8. Reproduction and numerical integrity
Self-contained NumPy script locally `xh_s4_dtc0a_projection_leakage_018_selfcontained.py`, SHA256 `534c1e548b4175de4b3929a8a8b82ce85098afa4cc39be36f4c3ffe26251826f`; JSON output SHA256 `97a3a6009e5f7caf29982be35f56b20f63284c076ab444fe88630737b6656991`.
Independent reproduction N=9,17,31, alpha=0,.05,.2; source finite Fourier h/fields, P/E/L, bracket, raw/masked norms and two input families. Identical original archive K_A/K_B/K_C at N31 alpha0,.05,.2 to machine precision. Numeric RHS residual 1e−20–3e−20. The source verifier SHA is recorded but actual project production runtime source elsewhere not audited. No original physical time evolution simulated.
STATUS: EXACT_IDENTITY_AND_FINITE_CONTROLS_VERIFIED / NO_CONTINUUM / NO_PHYSICAL_NASH / NO_CANON / NO_EXEC_SIGN / BW_PENDING.
