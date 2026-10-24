# MT13 ROT039 — NC-NUM-007 independent audit, exactly sharp constant 2 in inequality (7.3″)

DATE 2026-10-25
RETURN_ID MT13-ROT039-NC-NUM007-INDEPENDENT-COLLISION-INEQUALITY-AUDIT-001_20261025
PROBLEM_ID NC-NUM-007 / NC-033 ONE-POSITION ROUTING
STATUS TECHNICAL_SOURCE_AUDIT_PASS / NC_ACCEPTANCE_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC / BW_PENDING.

## ORIGINAL SOURCE FIRST
NC ART020 FIRST proved ||J m(A)-m(B)J||<=2||m||∞||J_coll|| for bounded Borel h,m, self-adjoint PURE-POINT A,B, bounded J with Jh(A)=h(B)J:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-24/IW_NC_NAPRAWA_NIEROWNOSCI_KOLIZYJNEJ_NORMA_CZESCI_ZAMIAST_SUP_BLOKOW_020_20261024.md
REC9 FIRST identified invalid earlier supremum-of-blocks bound and its 2x2 witness. NC ART024 FIRST constructed Schur-offdiagonal witness for a DIFFERENT norm ratio:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-24/IW_NC_NC_OPN_017_REDUKCJA_DO_MNOZNIKA_SCHURA_I_SWIADEK_024_20261024.md
MT13 earlier independently proved sharp ||J_coll||<=2(1−1/r)||J|| with r = max distinct spectral labels in ONE h-fiber, not Hilbert dimension; do not confuse with 2 in NC (7.3″).
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/2026-10-24/mt13_nc_opn017_sharp_collision_pinching_constant_001.md
NC-033 direct audited assignment MT13 first and ONLY NC-NUM-007 this turn:
https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1792882087005119

## Classical mathematical host and theorem-by-theorem subtraction
Schur multiplier/spectral pinching: T. Ando and K. Okubo, Induced norms of the Schur multiplier operator, LAA 147 (1991), DOI 10.1016/0024-3795(91)90234-N; S.-C. Ong, On the Schur multiplier norm of matrices, LAA 56 (1984), DOI 10.1016/0024-3795(84)90112-5; E. Christensen (2026), The Schur multiplier norm and its dual norm, LAA 743, DOI 10.1016/j.laa.2026.04.022. This turn verified online metadata/abstracts, NOT full theorems nor a direct-priority claim for the exact NC source inequality. NC proof of (7.3″) already closed its mathematical statement. MT13 only performs an independent legal-input and witness AUDIT, not a new theorem.

## Exact proof under the ORIGINAL source contract
Let P_lambda,Q_mu be point-spectral projectors. If h(mu) != h(lambda), Jh(A)=h(B)J forces Q_mu J P_lambda=0. For equal lambda=mu the defect multiplier m(lambda)-m(mu) vanishes. Consequently
 Jm(A)-m(B)J = J_coll m(A)-m(B)J_coll,
and the operator triangle inequality gives (7.3″) with constant2. This is NC's algebraic proof, independently reviewed.

### (A) ORIGINAL REC9 falsifier: exact equality and rejection of old formula
A=diag(0,1), B=diag(2,3), h(x)=cos(2pi x) (h=1 at ALL four eigenvalues), J=ones(2,2)/2, single bounded Borel m=+1 on sigma A and m=−1 on DISJOINT sigma B (extend by 0 elsewhere).
Then J_coll=J, ||J||=||J_coll||=1, Jm(A)-m(B)J=2J, norm2.
NC (7.3″) bound2 is ATTAINED. OLD (7.3′) used maximum SINGLE block norm κ=1/2 and would assert false bound1 <2.

For n×n extended REC9 family J=ones/n, A labels 0..n−1, B labels n..2n−1, all h=1, r=2n (NOT n), defect2, κ=1/n, old RHS=2/n, invalidity factor exactly n. Verified n=2,3,4,8,16,32,64.

### (B) INDEPENDENT r=2 witness WITH NONZERO matched blocks
A=B=diag(0,1), h(x)=cos(2pi x), m(x)=cos(pi x), J=ones(2,2)/2. One common Borel m on shared spectrum.
J_match=I/2 !=0; J_coll=[[0,1/2],[1/2,0]], ||J_coll||=1/2.
Jm(A)-m(B)J=[[0,-1],[1,0]], operator norm1=2||m||∞||J_coll||.
So factor2 is ALREADY sharp with MINIMAL NONTRIVIAL h-fiber cardinality r=2, not only with disjoint source spectra. If r=1 then J_coll=0 and question of nontrivial sharpness is vacuous.

### (C) Independent OTHER ratio guard and illegal falsifier
A=B=diag(0,..,r−1), J=I−(2/r)ones is Householder and satisfies ||J_coll||/||J||=2(1−1/r) for r=1,2,3,4,5,8,16,32,64; numerical controls PASS. This ratio is NOT the m-defect ratio from NC (7.3″), and product of both separately sharp factors is NOT automatically sharp for defect/||J||.
**Illegal random falsifier**: take A=B=diag(0,1), J=I, then J_coll=0. If an incorrect generator assigns m_A(0)=+1 but m_B(0)=−1, it produces apparent nonzero defect despite zero collisions. This violates the ORIGINAL requirement of ONE common function m at a shared eigenvalue. Real random tests synchronize those m values; reject the illegal example instead of retracting the theorem.

## Independent checks
Local independently authored reproducible Python: 18 explicit constructions, including REC9 and r2 mixed matched/collision witness, plus 800 LEGAL random complex matrices: 500 two-h-fiber tests with shared m on matched spectral labels, 300 rectangular disjoint-spectrum examples; all singular-value norm assertions PASS. Initial illegal duplicate-function m randomization spotted and corrected before accepted run.
Full Polish exact-proof report, Python script, deterministic JSON, README, SHA manifest in moderator-local bundle MT13_20261025_ROT039_NC_NUM007_audyt_ostrosci_bundle.zip.
ZIP SHA256 a10de22c921e3b5826c7348793fe9417eb45a9a71388da9cad98e1d12c6bf313.
CLEAN unzip+CRC+ALL_SHA pass; DELETE archived result JSON and REEXECUTE inside temporary extracted directory; regenerated JSON identical byte for byte.
No external NC code used or claimed verified.

**DECISION** NC-NUM-007: AUDIT_PASS; external independent NC/REC10 owner decision pending; NC claim not canon/EXEC; BW ingestion not inferred. NC-033 explicitly requests only first queue position: we DO NOT touch NC-NUM-011, NC-ALG-018, NC-023. No physics, quantum novelty or task cascade.