# PRF14 ROT025 — PUBLIC ERRATUM: nine zero source Fourier coefficients, not ten

**Date:** 2026-11-22 · **Cell:** PRF14 · **Status:** source correction, historical artifacts unmodified, independent referee pending.

The recurring textual assertion in historic PRF14 ROT016–ROT024 that the six-parameter two-time correlated classical Pauli source has **"ten ordinary Fourier coefficients equal to zero"** is WRONG.

A normalized classical source on sixteen paired Pauli histories `p(v,w)`, `v,w∈F₂²`, has exactly 16 Walsh coefficients:
- **1 constant coefficient = 1** (normalization, NEVER zero);
- **3** first-error marginal coefficients;
- **3** second-error marginal coefficients;
- **9** cross-error coefficients, comprising **6 offdiagonal** `(i≠j)` and **3 diagonal** `(i=j)`.

The original six-offdiagonal source definition is
`p(v,w)=[1+Σ_(i≠j) C_ij χ_j(v)χ_i(w)]/16`.
It has **SIX potentially nonzero cross-offdiagonal coefficients, NINE other nonconstant coefficients fixed zero, and ONE constant equal to 1**. Alternatively there are **ten remaining fixed coordinates, of which nine are zero and one is one**, NOT ten zeros.

I ACTUALLY executed an independent SymPy enumeration of all sixteen paired Pauli Walsh characters, confirming the full 16x16 Walsh matrix satisfies `W Wᵀ=16 I₁₆`, and the decomposition `1+3+3+6+3=16`.

**Custody:** This is an explicit textual correction; earlier pinned reports remain historic. The correction alone does not invalidate the original physical formula, CPTP Kraus or TV calculations, but their dependent claims require their own checks. No external peer review and no assertion that old files have been edited.

**Controlling science:** [PRF14 ROT025 source-first doctoral prior-art audit](https://github.com/wmakiela-tech/Nash-iw-research/blob/159144f543923d10a22957ed537dc0a74cfb1dff/research/prf14/2026-11-22/IW_PRF14_ROT025_DOCTORAL_PRIOR_ART_EXACT_THEOREM_AUDIT_WHITE_WANG_XU_LI_IST_AND_INSTRUMENT_TRANSPORT_DECISION_001_20261122.md).

NO_CANON / NO_EXEC_SIGN / NEGATIVE_KNOWLEDGE_PRESERVED.
