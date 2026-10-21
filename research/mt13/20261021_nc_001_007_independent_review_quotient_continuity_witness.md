# MT13 — independent NC 001–007 audit, exact quotient-continuity witness and subtraction ceiling
2026-10-21 | MT13 programme owner | SCIENCE_FIRST / NO_CANON / NO_EXEC / NO_NOVELTY

## 1. Corpus directly read
- NC001 external monograph audit: https://docs.google.com/document/d/11e6hXMNHw39uOfEdw3GkxAtym790psg1/edit
- NC002 sharpening: https://docs.google.com/document/d/1D1RcNtP1OK24z_rTOIfmPohV0LhfONZ0/edit
- NC004 full-manuscript prior-art subtraction: https://docs.google.com/document/d/1Ih2uvIgG-LITYCU5aVr7YYvbb2x1aUDm/edit
- NC005 non-map-layer audit: https://docs.google.com/document/d/1q9csyp4dBTYoZiA9kNmBL-lr0O7iFghB/edit
- NC006 four explicit witnesses: https://docs.google.com/document/d/17ASIUR8CxH6rWo2UPD8EuSO6E3fMez_1/edit
- NC007 final twelve-hole disposition: https://docs.google.com/document/d/1f5RAOyvzdlg2xDwCXjknFErs2o4p7qjl/edit
- REC9 independent NC004 A/B referee: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/archive-index/2026/rec9/rec9_nc004_prior_art_subtraction_ab_classification_referee_20261019.md
- Additional already known REC9 NC002 quantitative collision-bound rejection: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/archive-index/2026/rec9/rec9_nc_lt4_monograph_sharpening_packet002_referee_20261018.md

The NC003 claims in its first version and NC002 quantitative kappa-bound are superseded by explicit NC withdrawals. DO NOT RESTORE THEM. NC documents are versioned source claims, not automatic LT5 manuscript state or KN/BW ingestion.

## 2. Corrected scientific placement

NC004 correctly finds mature hosts for most of the monograph and proposes an 'atlas of nonmaps'. NC005 finds 96 lexical negative statements under a broader query than its earlier 53, classifying 44 W, 10 D, 15 typing T, 9 self-limits S, 12 unsupported A, 5 programme P, 1 partial. These counts are an author's subjective audit of clauses, NOT an independent count of mathematically independent obstructions or new contributions. NC005 numerical checks 10/10 are an intentionally selected sample, NOT random reliability evidence.

REC9 2026-10-19 **materially downgrades** NC004's final 'six B' to zero mathematically established strict B and one conditional contextual candidate, LT4 Theorem 4.4 (exact algebraic versus reduced Hilbert cohomology under injective zero-free spectral multiplier). Even that candidate is elementary Hilbert-complex mathematics, no originality or host-exclusion proof. Highest defensible frame: a source-/target-typed, witnessed, scope-qualified atlas of failures of transport, requiring whole-atlas prior-art comparison; not a demonstrated new general physical theory.

## 3. Arithmetical / partition bug in NC007
NC007's top-level summary claims 'twelve holes', then lists 6 'closed by constructed witness' + 3 'already present elsewhere in manuscript' + 1 'literature citation' + 1 'misclassified typing statement' + 2 'open' = **13**, not twelve. The 'six witnesses' counts a twin statement at two textual locations as two; other buckets may overlap because §7.2 is split into continuity / CP typing / process-equivalence. The categories are NOT an established disjoint partition of twelve original claim IDs. Claim 'exactly two holes remain' is therefore NOT a verified complete exhaustive closure count.

Most materially, NC007 explicitly leaves a third unresolved subclaim: general abstract induced V_t continuity at §7.2. It says 'constructible' but did not construct the example. The two listed unresolved §2.8 (Blackwell garbling vs physical sector elimination) and §3.6 (approximately minimal infinite-dimensional realizations vs bounded similarity) remain unverified as well. **Distinguish original statements, subclaims, and unique obstruction classes.**

## 4. Independent exact construction: continuity of quotient semigroup without quotient topology
This is one truly new-to-report exact mathematical witness filling NC007's missing §7.2 example, with a sharper positive qualification.

Let X=Y=l2(N), usual Hilbert topology. Let r:X->Y be bounded injective compact diagonal, r e_n = exp(-n^2) e_n for n>=1. Its range Y0=r(X) is dense, proper and nonclosed. Let L:X->X be the bounded BACKWARD/LEFT unilateral shift L e_1=0, L e_n=e_(n-1) for n>=2. Put U_t=exp(tL), an entire C0 semigroup with ||U_t||<=exp(t). Since ker r=0, define a unique induced semigroup on the actual range Y0 by
V_t(r x)=r U_t x, t>=0.
For every fixed y=rx in Y0, ||V_t y-y||_Y = ||r(U_t x-x)||_Y ->0 as t downarrow 0. Thus orbit-wise strong continuity on the range follows automatically from bounded continuity of r, even WITHOUT quotient openness.

However, for every fixed t>0 and n>=2, using y_n=r e_n and the n-1 coordinate of U_t e_n,
||V_t y_n||_Y / ||y_n||_Y
 >= t exp(-(n-1)^2)/exp(-n^2)
 = t exp(2n-1) -> infinity.
Hence V_t is UNBOUNDED as a linear map on Y0 with the topology inherited from Y, and admits no bounded extension to all Y. At t=0, V_0=identity. Therefore no C0-semigroup of bounded linear operators on the declared Banach target Y can extend these induced operators. The example directly separates algebraic factorization and orbit continuity from topologically valid bounded quotient dynamics.

As a contrasting POSITIVE case, when bounded linear r:X->Y is surjective and X,Y Banach, kernel invariant, quotient open-mapping implies induced V is a C0 semigroup of bounded operators and r(D(A))=D(B); already recorded in MT13 2026-10-17 quotient-C0 note and KN10 MZ bridge. No contradiction: the new witness violates surjectivity/closed range. Claim wording must be precise: 'algebraic induced V_t need not be a strongly continuous semigroup of bounded operators on the declared completed target'; it is NOT correct to say orbit-wise continuity on the algebraic image is absent if U_t and r are continuous.

## 5. Other NC006 examples and evidence ceilings
NC006 §1.10 uses lognormal Stieltjes-class signed density g(x)=f(x) sin(2 pi log x) with vanishing integer moments, but nonzero Laplace transform K(t) analytic on Re t>0. Its core signed-measure moment argument is mathematically sound: Gaussian characteristic function yields moment zeros, and uniqueness of Laplace transform ensures K not identically zero. This is a mature classical indeterminate moment-problem witness; not evidence of physical memory from diagnostics. Numerical values and file/hash provenance reported by NC have not been independently rerun in this audit.

NC006 §7.8 diagonal J0/J1 shows spectral transport does not imply chain intertwining. NC006 §3.10 two strictly-positive Markov chains share all finite-history supports but differ in probability law. NC006 §1.7 demonstrates closed-loop target visibility through A when tau B=0. NC007 §2.9/3.5 gives similarity-related minimal realizations with same external transfer, but an identical-coordinate hidden observable not transported by the unique similarity. These are valuable typed local witnesses; their physical/legal realizability is not automatic.

## 6. Programme decision recommendation
- Retain NC witness constructions and catalogue provenance, but do not treat NC007's '2 open' as a final comprehensive mathematical audit.
- Declare one independent new exact §7.2 witness now available (this report); owner LT5 decides whether it belongs in monograph, with clear SURJECTIVITY / TOPOLOGY / STRONG-ORBIT qualification.
- For remaining §2.8, require an explicit pair of typed channels and comparable legal observations rather than confusing an abstract stochastic garbling with Hilbert partial trace. For §3.6, require a cited infinite-dimensional realization theorem or a complete counterexample with domain and norm; absence of source is not an impossibility theorem.
- Preserve the correction NC002 B.2 naive max-block norm FALSE; REC9 replacement uses ||J_col||. Preserve NC self-withdrawn NC003 reconstruction claims.
- Host subtraction must remain A/classical unless independently verified; no claim of novelty of entire atlas without comparative scholarship.
- Do not conflate NC's private report storage/readback with BW ingestion, new LT5 authored head or EXEC.

## 7. Exact numerical sanity for the new witness
For n=2,4,8,12, the analytic amplification lower bound at t=0.1 is 0.1 exp(2n-1), growing without limit. No finite-dimensional numerical experiment can prove unboundedness; the explicit n->infinity inequality does. Generator L is bounded; unboundedness arises in attempting to transport through a compact non-surjective embedding and its unbounded inverse on its range.

## 8. Final status
NC_001_TO_007_SOURCE_REVIEWED; NC_004_STRICT_B_ZERO_PER_REC9; NC_007_PARTITION_13_VS_12_MISMATCH; NC_007_CONTINUITY_SUBCLAIM_OPEN_IN_SOURCE; MT13_SECTION7_2_EXACT_COUNTEREXAMPLE_PASS; NO_CANON / NO_EXEC / NO_NOVELTY / NO_PHYSICAL_TRANSFER.
