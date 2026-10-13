# MT13 — kontrola pierwszych rozdziałów monografii Żywej Teorii
Data: 2026-10-13
Status: BOOK_FIRST / EDITORIAL_MATHEMATICAL_REVIEW / NO_CANON / NO_EXEC / NO_NOVELTY
Active academic monograph: https://docs.google.com/document/d/1cn97_kO65BcJRRWQrvrL9fKlEYBT3PHg6BJItn1Q4FQ/edit
Distinct educator book: https://docs.google.com/document/d/10REMeEYIFneORSqYSea4kdZKJ6IyJn4-ptwGIps9TdE/edit

## Actual edit to the academic monograph (in-place, not a competing manuscript)
Inserted after the title and before Chapter 1: "WPROWADZENIE. CO DOKŁADNIE ZACHOWUJE OPIS EFEKTYWNY?" (~2,057 original characters), with HEADING_1 followed by normal body paragraphs.
Readback verified at native document indices: title 1–49; introduction heading 51–103; original Chapter 1 heading starts 2108; original Chapter 2 starts 25026; Chapter 3 starts 49271; Chapter 4 starts 64090. All 4 original chapter headings remain HEADING_1. Original proofs and chapter bodies untouched.
The new pedagogical-scientific bridge uses the same *one source-defined* 3-variable model throughout:
u'=-u, v'=h, h'=v-2h.
For x=(u,v), hidden h, A=diag(-1,0), B=(0,1)^T, C=(0,1), D=-2; K(t)=B exp(tD) C=diag(0,exp(-2t)) nonzero. Prepared h(0)=0 and v(0)!=0 yield v''(0)=v(0), so prepared v(t) differs from v'=0. With unrestricted hidden preparations, v'(0)=h(0) can vary at fixed x(0), blocking universal autonomy of x. Target tau(x)=u has exact autonomous evolution tau(x(t))=exp(-t)tau(x(0)) for all initial values. Reparametrization u_tilde=2u requires a declared measurement/calibration map if interpreted as a second physical readout. All assertions follow by direct finite linear ODE calculation; these are mature systems theory and not a new discovery.
The opening intentionally retains mathematical/physics content only, following LT4's authoring contract (academic monograph <=400 pages). This is distinct from SCOPE8's nine-part educational "Język świata".

## Reviewed material
Chapter 1: compression defect, exact memory elimination, Schur, prepared semigroup, target-specific autonomy, Kalman realization, Hilbert compression, and unbounded generator counterexamples.
Chapter 2: target factorization, quotient continuity, dynamical projectability vs target autonomy, bounded vs unstable inverse, quantitative target modulus, Bell correlations, observation law and common realization. Existing SW and INT7 Ch2 repairs are ALREADY in text; do not reapply.
Chapter 3: exact intertwining/representation/quotient/compression/quantum channel and statistical-experiment transport. INT7's latest §3.10 Blackwell dominance/target sufficiency correction is already delivered to LT4 and should be integrated by manuscript owner; do not overwrite a concurrent editor's live range.
Chapter 4: Hilbert complexes, bounded spectral multipliers, reduced vs algebraic cohomology, domain/graph norms, chain homotopy, heat action and spectral grids. This chapter is currently in the same manuscript but was not the primary user-selected "first chapters" edit.

## Two local, claim-safe checks for LT4, not silently applied
1. §4.10 "W unormowanej bazie sinusoidalnych postaci własnych e_n" is literally too broad for the whole exact 1-form space B on S^1, because both sine and cosine modes are present. Safe wording: "Wybierzmy ortonormalną rodzinę sinusoidalnych postaci własnych e_n należących do B"; the strict-image counterexample needs only an infinite orthonormal family, not a complete basis.
2. §4.2/4.3/4.5 explicitly permits non-closed d^f on original D(d). Calling H_red(d^f) a quotient is algebraically meaningful (ker d^f / closure ran d^f), but if the terminology is "closed Hilbert complex" readers need a one-sentence warning: the resulting operators need not be closed, and passage to their graph closures is a separate domain change. This is a terminology/domain audit suggestion, not an allegation the existing theorem is false.

## Preserve current review ownership
LT4: text and scientific architecture.
SW: proof checks (Ch2 PASS_WITH_LOCAL_PROOF_PATCH).
INT7: bridge checks (Ch2 integrated; Ch3 §3.10 ready-to-paste Blackwell repair).
MT13: programme-level coherence and bounded book-first edits, not independent referee.
No claim of peer review acceptance or scientific novelty. No project-process bureaucracy should be inserted into academic prose.

## Currentness
As of readback 2026-10-13 the native Google Doc contains Chapters 1–4. Earlier Slack announcement mentioned Chapters 1–3; do not regress on that stale stage. Next editorial work should track document revision to avoid overlap with LT4/SW/INT7.
