# KN10 — Mori–Zwanzig memory, quotient C0-semigroups and source-custody correction

```yaml
artifact_id: KN10_MZ_QUOTIENT_SEMIGROUP_SOURCE_LEGALITY_AND_LIBRARY_HOLD_001_20261017
date: 2026-10-17
origin_cell: KN10 / KCELL
kind: SOURCE_NATIVE_PRIOR_ART_INTEGRATION_AND_EXACT_FINITE_DIMENSIONAL_SANITY_TEST
exposure: PUBLIC
epistemic_class: STANDARD_LINEAR_SYSTEMS_IDENTITY / CONDITIONAL_BRIDGE / NO_NOVELTY
status: EVIDENCE_MEMO_WITH_UNREPAIRED_SCHOLAR_LIBRARY_SOURCE_HOLD
does_not_change: [LT_OWNER_HEAD, BW_SCIENCE_STATUS, EXEC, CANON, STOP, HOLD]
```

## 1. Scope and controlling sources

The five-paper Mori–Zwanzig (MZ) harvest is a prior-art/reference corpus, **not** five independent confirmations of one theorem. Different methods address strict estimates, kernel estimation, coarse-grained empirical kernels, neural closure and combinatorial constructions, respectively.

**Source quality exception:** the fifth item (Wang–Ripamonti–Hesthaven) returned from one Sider Scholar / Wisebase saved-file retrieval is an EPFL navigation/privacy-page body, not the scholarly article. Do not mark this saved file FULLTEXT_VERIFIED, and do not infer any mathematical claim from its Sider retrieval. The original paper was separately verified through public published/author textual sources:

- Wang, Q.; Ripamonti, N.; Hesthaven, J. S., *Recurrent neural network closure of parametric POD-Galerkin reduced-order models based on the Mori-Zwanzig formalism*, J. Comput. Phys. **410** (2020), 109402, DOI **10.1016/j.jcp.2020.109402**: https://doi.org/10.1016/j.jcp.2020.109402
- Author preprint full text (human-readable rendering): https://www.researchgate.net/publication/335230723_Recurrent_neural_network_closure_of_parametric_POD-Galerkin_reduced-order_models_based_on_the_Mori-Zwanzig_formalism
- EPFL public PDF endpoint (separate file URL, not the saved navigation-page URL): https://infoscience.epfl.ch/record/269133/files/MZ-LSTM%20Ver%201.pdf

The preprint's Sections 4–6 give a conditioned LSTM (POD history + physical/geometric parameters), IMEX integration of estimated memory, and **three numerical test systems**: 3D Stokes, 1D Kuramoto–Sivashinsky and 2D Rayleigh–Bénard. The experimental reports are finite-case generalization/effectiveness evidence, **not** an operator-theoretic proof of universal stability, correct hidden state reconstruction or all-horizon error bounds. Paper body read independently as public HTML; the bad Wisebase internal full-text object was *not overwritten* and remains an explicitly known retrieval-risk exception.

Other primary references:
1. Zhu, Y.; Dominy, J. M.; Venturi, D., *On the estimation of the Mori-Zwanzig memory integral*, J. Math. Phys. **59** (2018), 103501, DOI **10.1063/1.5003467**; preprint https://arxiv.org/abs/1708.02235.
2. Gouasmi, A.; Parish, E. J.; Duraisamy, K., *A priori estimation of memory effects in reduced-order models of nonlinear systems using the Mori–Zwanzig formalism*, https://arxiv.org/abs/1611.06277.
3. Li, Z.; Bian, X.; Li, X.; Karniadakis, G. E., *Incorporation of memory effects in coarse-grained modeling via the Mori-Zwanzig formalism*, J. Chem. Phys. **143** (2015), 243128; open body https://www.osti.gov/servlets/purl/1565466.
4. Zhu, Y., *Combinatorial Mori-Zwanzig Theory*, preprint https://arxiv.org/abs/2210.08395.

## 2. Exact elementary bridge: autonomous quotient vs hidden memory

Consider a finite-dimensional linear evolution with resolved and hidden coordinates:

```math
\dot x=Ax+By, \qquad \dot y=Cx+Dy,
\qquad r(x,y)=x.
```

Variation of constants in the hidden component yields exactly:

```math
y(t)=e^{Dt}y_0+\int_0^t e^{D(t-s)}Cx(s)\,ds.
```

Substituting in the resolved equation gives the *exact* MZ-like decomposition:

```math
\dot x(t)=Ax(t)+B e^{Dt}y_0+
\int_0^t \underbrace{B e^{D(t-s)}C}_{K(t-s)}x(s)\,ds.
```

The first added term retains dependence on the hidden *initial state*; the second is a convolution memory kernel. They must not be conflated.

Now apply the standard quotient C0-semigroup statement from the already authored 2026-10-17 MT13 return (see linked source below). For **all** initial states, the kernel of the projection (r) is invariant under the full linear evolution precisely when (B=0). Proof: (ker r=\{(0,y)\}). If invariant, any initial ((0,y_0)) must satisfy (dot x(0)=By_0=0) for every (y_0); hence (B=0). Conversely, when (B=0), (x(t)=e^{At}x_0) is autonomous, the kernel is invariant, and the induced semigroup (V_t=e^{At}) is exact. This is a finite-dimensional instance of the invariant-kernel quotient theorem, **not** a new general theorem.

Positive finding: nonzero (B) obstructs universal autonomous quotient semantics even if a particular memory approximation happens to look small. The MZ hidden-state forcing plus memory are one explicit exact representation of what the quotient fails to forget legally.

**Critical non-implication:** (K(t)=B e^{Dt} C\equiv0) does *not* imply a valid quotient semigroup for all initial states. For (B=1,C=0,D=-1), the memory kernel is zero while the hidden-initial-data term (e^{-t}y_0) is nonzero. A zero fitted memory kernel does not certify common-state identification, source-independent dynamics or invariant (ker r).

Current MT13 authored theorem (source-native): https://github.com/wmakiela-tech/Nash-iw-research/blob/565185c4edf/research/mt13/20261017_ch7_quotient_c0_semigroup_regularity.md. MT13 additionally requires *bounded surjective Banach-space reduction* and *invariance of its kernel* to obtain a quotient C0 semigroup and correct generator domains. A generic MZ projection need not satisfy these assumptions. No transfer from finite-dimensional block calculations to arbitrary unbounded (QL), its domain, or physical state is licensed without independent operator analysis.

## 3. Discriminating memory-truncation sanity test

Let (B=C=1), (D=-\gamma) ((\gamma>0)), with (y_0=0). Then (K(u)=e^{-\gamma u}). On ([0,t]), suppose (|x(s)|\le M). A truncated memory retaining only the last (\tau\) units ((0<\tau<t)) omits:

```math
E_{\tau}(t)=\int_0^{t-\tau}e^{-\gamma(t-s)}x(s)\,ds,
\qquad
|E_{\tau}(t)|\le \frac{M}{\gamma}
\bigl(e^{-\gamma\tau}-e^{-\gamma t}\bigr)
\le \frac{M}{\gamma}e^{-\gamma\tau}.
```

This is a true **source-local, data-conditional** norm estimate: it needs decay of (e^{Dt}) and an observable bound (M). It does *not* establish universal small-memory behavior.

Countercase: (A=D=0), (B=C=1), (y_0=0), (x_0=1). The exact solution is (x(t)=\cosh t), (y(t)=\sinh t), and (K(u)=1) has no decay. Discarding history before (t-\tau) removes **exactly** (\sinh(t-\tau)), which grows with time and is not bounded by an (e^{-\gamma\tau})-type estimate. Thus MZ decomposition alone does not license a short-memory or RNN fixed-window approximation.

This elementary calculation is **not** a test of the numerical algorithms or theorem constants in the five papers. It exposes the exact assumptions required before transferring their conclusions.

## 4. Paper-family separation and IW claim ceilings

| Source family | What can be transported after checking assumptions | What is not established automatically |
|---|---|---|
| Zhu–Dominy–Venturi | Semigroup/norm-based *conditional* MZ memory estimates, short-memory and hierarchical approximation bounds for admitted object/domains | Uniform long-time error control in arbitrary nonlinear models |
| Gouasmi–Parish–Duraisamy | A priori *numerical estimation* of unknown memory kernels from full-order snapshots using pseudo-orthogonal dynamics; published tests | Certified complete ROM closure under all regimes or general mathematical convergence |
| Li et al. | Coarse-grained model kernels and correlation relations in specified statistical ensembles | Unrestricted replacement of orthogonal projected dynamics by raw force correlation |
| Wang–Ripamonti–Hesthaven | Conditioned LSTM memory closure within parametric POD–Galerkin + IMEX; performance in three tested problems | Guaranteed hidden-source identifiability, arbitrary extrapolation or a theorem for every source carrier |
| Zhu, combinatorial MZ | Self-consistent/combinatorial kernel expansions with source-native operator and differentiability assumptions | Automatic analytic convergence or controlled numerical truncation for any system |

**Recommendation for actual scientific owners:** if an existing legal research front needs this machinery, first declare (i) resolved projection/range/kernel, (ii) generator domain and semigroup class, (iii) noise/initial-hidden-data treatment, (iv) memory-kernel norm and decay, (v) horizon and target functional, (vi) numerical or statistical error class. If any is absent, classify the result `ANALOGY_ONLY / NON_MAP / UNKNOWN`, not a new IW physical law.

This is a knowledge-custody and prior-art alignment note; it is **not** an owner-authored LT chapter, evidence of independent numerical reproduction, proof of admissibility in NCDG, or release of an active scientific HOLD.

## 5. Status and provenance

- Five bibliographic sources identified, four saved-file bodies yielded substantive science excerpts in targeted Sider Scholar reads.
- The fifth *saved-file body* was incorrectly resolved to EPFL site navigation; complete source was separately read as publicly accessible original preprint HTML, and its accurate DOI/publisher identity verified. Wisebase original not replaced; until readback of a corrected saved file, **source-custody repair is partial**.
- Independent exact finite-dimensional proof/counterexamples are supplied in this note, algebraically checkable without model training. No computational reproduction of published experiments.
- Project owner/MT13/INT7/referee findings after 2026-10-17 take precedence for theory currentness; this note is an optional source-facing semantic guard, not a new master head.
