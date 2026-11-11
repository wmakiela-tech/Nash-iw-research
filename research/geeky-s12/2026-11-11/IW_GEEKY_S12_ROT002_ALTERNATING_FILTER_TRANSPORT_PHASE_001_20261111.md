---
artifact_id: IW_GEEKY_S12_ROT002_ALTERNATING_FILTER_TRANSPORT_PHASE_001_20261111
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
date: 2026-11-11
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_CLASSICAL_TWO_MODE_PERIODIC_PRODUCT_PHASE / SYNTHETIC_SIGNED_GAIN_LOSS_ONLY / NO_SOURCE_DTC0A_KA_OR_TT_INFERENCE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
science_status: AUTHOR_EXACT_PROOF + LOCAL_EXACT_RATIONAL_REPRO / INDEPENDENT_REFEREE_PENDING / OWNER_ADOPTION_PENDING
---

# Geeky-S12 ROT002 — a reached amplifying mode does not imply instability of alternating filtered transport

## 0. Bounded question and why it matters

**Question.** ROT001 constructed a *different, scalar auxiliary* norm-preserving transport U that sends initially E-damped modes to E-amplified frequencies. There, **E^m U f** grows if a newly excited Fourier mode has |q|>1. Does that transfer logically establish instability of **(E U)^m f**, a different process which alternates filter and transport at each step?

**Answer: NO.** In a rigorously typed two-mode synthetic signed-gain/loss model, the first step may even expand a stable starting mode by 20%, while the repeated alternating operator decays exponentially. Merely reaching an expanding eigenspace of E is not sufficient for a repeated-product instability claim. A separate exact example using the SAME E and initial stable f but a different orthogonal mixing U grows exponentially. There is a sharp, elementary Schur–Jury phase boundary.

**Status:** conditional classical linear algebra / discrete-time stability, not novel mathematical priority, physics or actual DTC0a source replay.

## 1. Foundation and precedence

**Mature external foundations:** classical Jury (1962), Schur–Cohn quadratic stability and periodic/Floquet monodromy:
- E.I. Jury, *A Simplified Stability Criterion for Linear Discrete Systems*, Proceedings of the IRE 50(6), 1962, DOI 10.1109/JRPROC.1962.288193. https://doi.org/10.1109/JRPROC.1962.288193
- *Schur stability of polynomials and matrices*, Encyclopedia of Mathematics, https://encyclopediaofmath.org/wiki/Schur_stability_of_polynomials_and_matrices
- C. Gökçek, *Stability Analysis of Periodically Switched Linear Systems Using Floquet Theory*, 2004, DOI 10.1155/S1024123X04401069, https://doi.org/10.1155/S1024123X04401069
- For arbitrary, not fixed-period switching, the joint spectral radius (a different problem) is the classical appropriate object: https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/wirth/Publikationen/stability-switched.pdf

**Own IW/NASH subtraction:** Geeky-S11 ROT027/029/033 treated specified filter placement, source schedules and order; INT9 ROT009 and ROT010 proved respectively global E_lin noncontraction at alpha=0.2 and contraction of the *actual source auxiliary* generator's input supports for E_lin; S12 ROT001 only treated one transport then repeated E, **not** an alternating source runtime. Do not transfer those exact source claims to a synthetic 2x2 without a new carrier equivalence proof. Historical canonical masked dtc0a_runtime_v0_3_1.py bytes remain unrecovered, even though a related Colab notebook AST matches the auxiliary helper.

No new direct IWTO_GEEKY_S12 source/owner task was found in the latest 11-Nov #iw-dispatch check. This rotation is a separate autonomous branch-point falsifier, not a demand for new owner execution.

## 2. Explicit synthetic source type

Let H=R^2 with standard norm, a>1, 0<b<1 and **ab<1**. Let

E = diag(-a,b),  U_c = [[c,-sqrt(1-c^2)],[sqrt(1-c^2),c]],  0<=c<=1,
M_c = E U_c,   f=e_2=(0,1).

E has one *negative amplifying* eigenvalue -a and one positive attenuating eigenvalue b. The sign pattern resembles a possible alpha=.2 E_lin Fourier multiplier at different modes, but **the two numbers and U are chosen freely**; there is NO assertion of a source-legal invariant Fourier block, TT projector action, tensor Lie group or masked K_A. U_c is exactly orthogonal, so ||U_c||=1 and ||M_c||=||E||=a>1 for all c. Thus even operator norm >1 per alternating step does not settle long-time growth.

Define the fixed-process output M_c^m f, m>=0. This is not E^m U_c f or U_c E^m f.

## 3. Exact phase theorem (classical)

For every a>1, 0<b<1, ab<1 in this 2-mode model, let
c_star = (1-ab)/(a-b).

Because (a-b)-(1-ab)=(a-1)(1+b)>0, we have 0<c_star<1.

**Exact classification:**
- 0<=c<c_star: spectral radius rho(M_c)<1. Thus M_c^m f ->0 exponentially for *every* f, even though E amplifies one mode.
- c=c_star: M_c has simple eigenvalues -1 and ab in (0,1); all orbits are bounded. For 0<c<1, e2 has a nonzero -1 component, so it does not decay to zero.
- c_star<c<1: M_c has a real eigenvalue <-1. Because U_c mixes e2 into the first coordinate, e2 has a nonzero component on the corresponding eigenvector, hence ||M_c^m e2|| grows exponentially.
- c=1: M_1=diag(-a,b) is globally unstable but e2 *still decays* as b^m. This explicit endpoint is a reminder that **global instability does not guarantee instability of the source-specific target**.

**Proof.** The exact characteristic polynomial is
p(lambda)=lambda^2+(a-b)c lambda-ab.
The quadratic Schur–Jury conditions for both roots in the open unit disk are:
1-ab-(a-b)c>0, 1-ab+(a-b)c>0, 1+ab>0.
For 0<=c<=1 and ab<1, the middle two are automatic, and the first is equivalent to c<c_star. At equality p(-1)=0 and the other eigenvalue is ab (because det=-ab). For c>c_star, p(-1)<0 and p(lambda)->+infinity as lambda->-infinity, so one real root is <-1. The discriminant ((a-b)c)^2+4ab is strictly positive, hence both eigenvalues are simple. When 0<c<1, M_c e2=(a sqrt(1-c²), bc) has nonzero first coordinate, so e2 is not an eigenvector and must have nonzero projection on each of the two distinct eigenvectors. Thus it excites the unstable eigenvector whenever one exists. For c=1, e2 is an eigenvector of b, giving the exceptional decaying orbit.

**Sharpest positive/negative witness at c=0:** U_0 swaps the two modes up to a sign. Then
M_0 = [[0,a],[b,0]],   M_0^2 = ab I.
Therefore ||M_0 f||=a>1, but ||M_0^{2m} f||=(ab)^m ->0. A first-step amplified signal is compatible with exponential decay of the true repeated process.

This is the essential falsifier: no threshold on |q| of merely *reachable* modes, and no finite observed first-step gain, can replace the spectral/observability test on the correct periodic product.

## 4. Exact rational model and independently checked arithmetic

Fix **a=6/5, b=1/5**, so
E=diag(-6/5,1/5), c_star=(1-6/25)/(1)=19/25=0.76.

**Stable mix** c=3/5,s=4/5:
M=[[ -18/25,24/25],[4/25,3/25]],
eig=(-3 +/- sqrt(33))/10; rho=(3+sqrt(33))/10 ≈0.8744562646538028<1.
For f=e2, ||M^120 f||≈8.631873638063579e-8 and ||M^250 f||≈2.3017450470529735e-15.

**Unstable mix** c=4/5,s=3/5:
M=[[-24/25,18/25],[3/25,4/25]],
eig=(-2 +/- sqrt(10))/5; rho=(2+sqrt(10))/5≈1.032455532033676>1.
For SAME f=e2, ||M^120 f||≈26.425496516882887 and ||M^250 f||≈1679.9617248279924.

**Quarter swap** c=0,s=1:
M=[[0,6/5],[1/5,0]], M²=(6/25)I.
For f=e2, ||M f||=6/5=1.2 >1, but ||M² f||=6/25=0.24 and orbit decays exponentially.

All matrix entries, traces, determinants, powers up to m=250 and classification assertions were computed with **stdlib fractions.Fraction exact arithmetic**, with floats used solely for reported Euclidean norms/eigenvalue approximations. An independent SymPy symbolic characteristic-polynomial expansion and exact radicals agreed. These are mathematics/implementation checks, not empirical experiments or independent peer review.

**PUBLIC self-contained reproducer:** https://github.com/wmakiela-tech/Nash-iw-research/blob/f270cf2a202c83fc5d1b50ab3c7854a2312fb418/research/geeky-s12/2026-11-11/iw_geeky_s12_rot002_periodic_filter_transport_reproducer.py
Direct pinned Git readback PASS of exact authored source content. The local author test and independent algebra check were executed, but a separate execution of downloaded GitHub bytes is NOT claimed.

## 5. Consequence for the NASH source boundary

ROT001's valid exact claim is about **E^m U(t) f** for a different scalar advection source. It does NOT entail a growth theorem for **(E U(t))^m f**. ROT002 shows the inferential arrow is false in general even when U is an isometry, E is signed gain/loss, the initial f is strictly stable under E, and U reaches the amplified eigenspace in a single step.

The source generator from INT9 ROT010 has its own bounded 24-mode E-input support and is contractive there at alpha=.2. This model does not overthrow that result. Neither ROT001 nor ROT002 is a physical nonlinear evolution, historical K_A or a canonical E repair.

For any requested *actual* source transport, the correct next mathematical test depends on the declared process:
A. **E^m U f:** test nonzero f projection on |q|>1 after the one transport.
B. **(EU)^m f:** test eigenvalues/Jordan chains of M=EU on the exact source-cyclic subspace span{M^k f}, not merely E's full-grid operator norm. In finite dimension, use Cayley–Hamilton to close the test.
C. **Variable schedule E_j U_j:** one-period monodromy if periodic; no single-product criterion for unrestricted switching (joint spectral radius or input-constrained products may be needed).
D. **Actual DTC0a finite K_A expression:** source-authorized finite operator word and masks; no time evolution/stability inference from a finite diagnostic.

**Immediate change:** refine S12 ROT001 proposed TRANSPORT_REACHABILITY_SPECTRAL_GATE by adding PROCESS_WORD/ORDER and an input-cyclic-product spectral test. The old simpler test remains valid for E^mU, not for alternating dynamics.

**Falsifier of this application:** show the exact source process never contains alternated (EU)^m, or that its legal tensor/projection/mask algebra cannot realize this two-mode matrix. Then ROT002 remains mathematics but has NO source transfer. STOP any generic physics claim or unauthorised runtime program.

## 6. Custody and final state

Primary public science location is this GitHub artifact under research/geeky-s12/2026-11-11/. Full proof, negative conditions, prior-art references and source code link are inline. PUBLIC source script is a separately pinned public file. Both need exact post-write readback before declaring stored. Cross-surface KN/BW ingestion remains PENDING, no ING invented; no independent REC/AUD verdict or M14/INT9 adoption inferred. Slack dispatch if delivered is transport evidence only.

**RESULT: EXACT TWO_MODE_FILTER_TRANSPORT_PHASE_PASS / ROT001_TO_ALTERNATING_INFERENCE_FAIL / SOURCE_DTC0A_TRANSFER_HOLD / REFEREE_PENDING / BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.**
