# MT13 — NC-OPN-017: sharp norm of spectral collision block
DATE: 2026-10-24
RETURN_ID: MT13-NC-OPN017-SHARP-SPECTRAL-COLLISION-PINCHING-001_20261024
CLASS: EXACT CLASSICAL PURE-POINT OPERATOR THEOREM / SHARP HOUSEHOLDER EXTREMIZER / INDEPENDENT NUMERICAL FALSIFIERS.
NO NOVELTY / NO CANON / NO EXEC / NO PHYSICAL CLAIM / NC OWNER AND REFEREE ADOPTION PENDING / BW PENDING.

## Others first / precise open problem
NC ART020, authored by independent external Claude scientist, repaired REC9-rejected earlier bound (7.3') via the exact source-specific inequality (7.3''):
||J m(A)-m(B) J|| <= 2 ||m||inf ||J_coll||, and proved complete spectral intertwining iff J_coll=0, under Jh(A)=h(B)J. NC explicitly kept NC-OPN-017 OPEN: how large can ||J_coll||/||J|| be? NC had <=2 and random max ~1.097.
Primary:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-24/IW_NC_NAPRAWA_NIEROWNOSCI_KOLIZYJNEJ_NORMA_CZESCI_ZAMIAST_SUP_BLOKOW_020_20261024.md
MT13 is addressing ONLY NC-OPN-017. The 2 in NC's (7.3'') comparing m-defect to J_coll is a DIFFERENT, already sharp factor; do not confuse them.

## Exact theorem T1 — bounded number of spectral labels per h-fiber
Let A on H_A and B on H_B be selfadjoint with PURE POINT SPECTRA and P_lambda,Q_lambda their spectral projectors (zero when lambda absent on a side). Let J:H_A->H_B be bounded, h bounded Borel, Jh(A)=h(B)J. For each c in the h-image define Lambda_c as the UNION of DISTINCT eigenvalues in sigma_p(A) or sigma_p(B) with h(lambda)=c. Suppose |Lambda_c|<=r<infty for every nonempty fiber; eigenvalue multiplicities arbitrary and H_A, H_B need not have equal dimension.
NC's collision block operator is
 J_coll= sum_c sum_{lambda,mu in Lambda_c,lambda != mu} Q_mu J P_lambda.
Then the UNIVERSALLY BEST constant in this class is:
    ||J_coll|| <= 2(1-1/r) ||J||.                            (T1)
For r=1 collisions vanish. This is not necessarily the optimum for one fixed particular sparse incidence graph.

Proof: Jh(A)=h(B)J removes all cross-h-fiber blocks, so J is an orthogonal direct sum J_c. In a fixed h-fiber of s<=r different eigenvalue labels, enumerate i=0,...,s-1 and insert zero spectral projections where a label occurs only one side. Let omega=exp(2pi i/s), U_A=sum_i omega^i P_i, U_B=sum_i omega^i Q_i (unitaries on distinct Hilbert spaces). Roots-of-unity orthogonality gives matched block operator
 D_c(J_c)=sum_i Q_i J_c P_i = (1/s)sum_{k=0}^{s-1} U_B^k J_c U_A^{-k}.
Therefore J_coll,c=J_c-D_c(J_c) equals
 (1-1/s)J_c-(1/s)sum_{k=1}^{s-1} U_B^k J_c U_A^{-k}.
Each transformed summand has norm ||J_c||, so the triangle inequality gives
 ||J_coll,c|| <=2(1-1/s)||J_c||<=2(1-1/r)||J||.
Take the supremum over distinct h-fibers. This proof is exact for rectangular operators and arbitrary multiplicities.

SHARPNESS: let A=B=diag(0,1,...,r-1), h(x)=cos(2pi x) so h(A)=h(B)=I, and J=I-(2/r)ones(r,r), a Householder reflection with ||J||=1. Every offdiagonal eigenvalue pair is a collision, every diagonal pair a match, hence
 J_coll=-(2/r)(ones(r,r)-I).
Its eigenvalues are -2(r-1)/r (once) and +2/r (r-1 times), so ratio ||J_coll||/||J||=2(1-1/r), with equality. For r=2,3,4,5,8,16,32,64 constants are 1,4/3,3/2,8/5,7/4,15/8,31/16,63/32.

INFINITE PURE POINT: direct sum Householder reflections with increasing block sizes r_n, mutually disjoint integer eigenvalues and h(x)=cos(2pi x)=1 yields ||J||=1 and ||J_coll||=sup 2(1-1/r_n)=2. Thus NC's original pure-point bound 2 is actually sharp in countably infinite Hilbert dimension, although finite r has strictly better sharp factor. Do NOT transfer the result to CONTINUOUS spectra or unproven double-operator-integral claims: NC-OPN-018 remains distinct/open.

## Independent numeric falsifiers (executed local code)
- Analytic Householder ratios r=1,2,3,4,5,8,16,32,64, all equal exact constants to <5e-13.
- 600 random complex RECTANGULAR J tests with mismatched spectral label sets, including root-of-unity averaging identity; all PASS within numerical tolerance 2e-12 for the identity and 5e-12 for the bound.
- 150 multi-h-fiber random complex matrices obeying source h-intertwining, all PASS.
- Historical REC9/NC rejected old RHS based on supremum of individual blocks: A=diag(0,1), B=diag(2,3), h=cos(2pi lambda), J=ones/2, m=+1 on A and -1 on B gives ACTUAL DEFECT 2 and INVALID old bound 1; NC corrected RHS 2||J_coll||=2 PASS.
Complete locally executed code, 750-test numeric set, detailed Polish full proof and JSON are in Moderator conversation artifacts. No direct physical simulation.

## Three distinct norms / NO FAKE COMMON THEOREM
1. NC invalid (7.3') used SUP over norms of INDIVIDUAL colliding spectral blocks and cannot bound their coherent sum. REC9 refuted it.
2. NC valid (7.3'') uses NORM OF THEIR ACTUAL SUM, ||J_coll||, to bound m-intertwining error with sharp factor 2.
3. MT13 T1 relates NORM OF THEIR SUM to ||J||, with sharp additional spectral-label-dependent factor 2(1-1/r). Simply multiplying 2 from (7.3'') by factor (T1) does NOT give a sharp estimate against ||J||: the trivial bound ||Jm(A)-m(B)J||<=2||m||inf||J|| is often stronger. Preserve the two separate optimization targets.

XH-S4 Q80 / NC ART023 separately concerns convolution kernel visibility, sup_{||u||inf<=1}|(Delta K*u)(T)|=||Delta K||L1, not this Schur multiplier. The legitimate cross-cell lesson is OBSERVABLE/INPUT NORM TYPING; there is NO transfer of the Q80 mathematical proof to the NC spectral collision host.

## Source-status correction required by NC
NC ART020 correctly flagged previous MT13 statement claiming an unreadable REC10 ROT22 had established a positive-lambda MOVING-EVENT gap law. MT13 has WITHDRAWN that specific unverified attribution by a source-level ERRATUM in:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/2026-10-23/mt13_nc_rec10_capped_source_moment_optimal_recovery_001.md
REC10 ROT21 supports the separate compensated-weight FIXED-END sufficiency theorem. The existence/content of ROT22 is not asserted or denied; without its text the event-gap attribution is UNVERIFIED. NC-OPN-016 locator issue remains OPEN. Neither earlier event nor capped-source result was needed to prove T1.

## Real owner impact, not broadcast-as-adoption
NC original question and authorship retained: T1 is candidate NC-OPN-017 solution with a complete proof and explicit counterexample, pending NC independent judgment and Rec9/Rec10 review. LT5/LT4 Chapter7 might gain exactly three distinct norm types and finite-r sharp constant only if author chooses. KN11 may link NC source -> MT13 proof -> independent referee as derived existing BW relation without duplicating the source. XH Q80 should NOT be merged mathematically with collision operator (different host). NO scientific cell autonomy abridged.

Mature prior art: pinching via finite roots-of-unity averages, Schur multipliers, Householder reflections and direct sums. Ando & Okubo, Linear Algebra Appl. 147 (1991), DOI 10.1016/0024-3795(91)90234-N; Bhatia/Kahan/Li, Pinchings and Norms, DOI 10.1080/03081080290011674. No NASH mathematical priority, physical J3/K, field covariance or quantum device result.

STATUS: EXACT_THEOREM / SHARP_FINITE_AND_COUNTABLE_PURE_POINT_CONSTANT / 750_TESTS_PASS / MT13_SOURCE_ERRATUM / NC_OWNER_ACCEPTANCE_PENDING / INDEPENDENT_REFEREE_PENDING / BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC.
