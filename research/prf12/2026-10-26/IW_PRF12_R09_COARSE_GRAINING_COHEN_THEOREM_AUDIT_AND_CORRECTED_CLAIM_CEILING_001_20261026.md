---
artifact_id: IW_PRF12_R09_COARSE_GRAINING_COHEN_THEOREM_AUDIT_AND_CORRECTED_CLAIM_CEILING_001_20261026
created_at: 2026-10-26
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
problem_id: PRF12_R07_R09_COARSE_GRAINED_DECISION_EFFECT_CUSTODY_AND_SOURCE_AUDIT
exposure: PUBLIC
canonical_body_path: research/prf12/2026-10-26/IW_PRF12_R09_COARSE_GRAINING_COHEN_THEOREM_AUDIT_AND_CORRECTED_CLAIM_CEILING_001_20261026.md
sync_state: GITHUB_PENDING_BW_INGEST
status: CRITICAL_SELF_CORRECTION / VALID_RESTRICTED_MATRIX_MINOR_LEMMA / R07_FULL_LOCC_GAP_CLAIM_WITHDRAWN / R08_LOCC_WITNESS_PRESERVED / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_POSITIVE_FULL_LOCC_CLOSURE_GAP_PROOF / NO_CERTIFIED_NUMERICAL_LOCC_GAP_LOWER_BOUND / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_DEVICE / NO_NOVELTY / NO_FULL_SUCCESSION_HANDOFF_READBACK
function: SCIENCE_FIRST / FOUNDATION_FIRST / LITERATURE_VERIFICATION / NEGATIVE_KNOWLEDGE_PRESERVING / FALSIFIER_FIRST
---

# PRF12 R09 — Krytyczna audytowa korekta R07–R08: coarse-graining blokuje pozorny certyfikat ilościowej luki LOCC

**Data:** 26.10.2026. **Funkcja:** PRF12. **Werdykt:** pierwotnie zaproponowane oszacowanie \(\delta_{\mathrm{LOCC}}(q)\ge\mu(q)/72\) NIE zostało udowodnione. Poprawny jest wyłącznie lemat o operatorach produktowych zawartych w *zonotopie dwóch zagregowanych efektów decyzyjnych*. Użycie warunku ścieżek Cohena bez zachowania pełnego rozdrobnienia wyników pomiaru było nieuprawnione. Ten błąd dotyczy także wcześniejszego twierdzenia R07 o dodatniej luce w closure(LOCC). Niniejszy raport jawnie wycofuje oba mocne roszczenia, zachowując poprawne węższe wyniki i ścieżkę dalszego dowodu.

## 0. Źródła, status właścicieli i genealogia samokorekty

**Internal host:**
- PRF11 R35, właściciel modelu static Cauchy vs independent Cauchy–Lévy i SWAP: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R35_NONUNIFORM_SWAP_TIME_GRID_RECOVERS_IDEAL_MEMORY_WITH_CRITICAL_STORAGE_RATE_001_20261025.md .
- PRF12 R04, exact n=3 equal-grid matrix, Helstrom, locally measured X: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R04_THREE_PROBE_FINITE_SWAP_EXACT_X_READOUT_GAP_AND_SECTOR_DECOMPOSITION_001_20261026.md .
- PRF12 R05, dokładny 28-efektowy separowalny POVM achieving Helstrom, **bez dowodu implementowalności LOCC**: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R05_SEPARABLE_HELSTROM_POVM_PRODUCT_BASES_AND_ONE_CNOT_RESOURCE_AUDIT_001_20261026.md .
- PRF12 R06, bezpośredni argument o **niemożliwości dokładnego FINITE-ROUND** protokołu LOCC na podstawie lokalnej nieredukowalności P/Q: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R06_EXACT_SEP_VS_LOCC_NO_GO_LOCAL_ORTHOGONALITY_RIGIDITY_001_20261026.md . R09 NIE obala samego lokalnego argumentu R06; niezależna recenzja nadal oczekiwana.
- PRF12 R07, wcześniej błędnie użyty necessary condition o zonotopach do **zagregowanego** binary POVM: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R07_POSITIVE_ASYMPTOTIC_LOCC_GAP_VIA_ZONOTOPE_PRODUCT_PATH_OBSTRUCTION_001_20261026.md . **Główny claim R07 został oznaczony w samym pliku jako WITHDRAWN / NOT PROVED.**
- PRF12 R08, dokładny konstruktywny 3-party LOCC witness X→conditional X/Y→last-qubit Helstrom: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R08_EXACT_ADAPTIVE_LOCC_WITNESS_AND_DELTA_UPPER_BRACKET_001_20261026.md . **Jego osiągalność i wzór przetrwały**, ale ścisła dodatniość δ jako zależność od R07 została oznaczona jako NIEUDOWODNIONA.

**External mature mathematical host, checked in full text:**
- S. M. Cohen, *Local approximation of multipartite quantum measurements*, *Phys. Rev. A* **105**, 022207 (2022), https://doi.org/10.1103/PhysRevA.105.022207 ; full text https://arxiv.org/html/1912.02330v2 . Theorem 1 and discussions of measurement outcomes, individual leaves and proportionality in sections II–III are essential. Its product-path criterion relates the zonotope to the particular measured **POVM outcome structure**. We MUST NOT silently substitute the coarser two-decision operator pair obtained AFTER arbitrary classical outcome postprocessing.
- Cohen, *Local approximation for perfect discrimination of quantum states*, *Phys. Rev. A* **107**, 012401 (2023), https://doi.org/10.1103/PhysRevA.107.012401 , published erratum *PRA* 108, 029902 (2023). It treats a different pure-state perfect-discrimination context.
- General prior art: Helstrom optimal binary measurement, separable vs LOCC, LOCC measurement refinement, and classical coarse-graining. Our result in R09 is SOURCE-AUDIT and a restricted matrix-minor lemma, NOT a claim of universal novelty.

## 1. The fatal logical gap: binary classical decisions are not fine-grained measurement outcomes

An LOCC protocol may yield a family of product-positive leaf effects \(F_\ell=A_\ell\otimes B_\ell\otimes C_\ell\ge0\) satisfying \(\sum_\ell F_\ell=I\). After all local outcomes are recorded and classically communicated, the experimenter groups leaf labels into hypotheses A and B:

 \(E_A=\sum_{\ell\in{\cal L}_A}F_\ell,\quad E_B=\sum_{\ell\in{\cal L}_B}F_\ell=I-E_A.\)

The binary effects \(E_A,E_B\) are generally NOT themselves product operators. More importantly, their two-generator zonotope
 \(Z_{\rm binary}=\{\alpha E_A+\beta E_B:0\le\alpha,\beta\le1\}\)
need not contain all the intermediate operators encountered by the full refined LOCC tree.

**Elementary falsifier, no quantum sophistication:** local projective Z measurements on TWO separate qubits, followed by classical even/odd parity decision, implement a genuine LOCC instrument. Yet the coarse even-parity binary effect is

 \(E_{\rm even}=|00\rangle\langle00|+|11\rangle\langle11|
   =\mathrm{diag}(1,0,0,1),\)

which is NOT product: if it equalled \(A\otimes B\ge0\), the diagonal requirements \(a_0b_0>0\), \(a_1b_1>0\), \(a_0b_1=0\), \(a_1b_0=0\) would contradict positivity. Cohen's product-path criterion cannot be used to reject this obvious local protocol merely because the *coarsened* E_even is not product.

This is a problem in our *use* of the published theorem; the paper itself need not be pronounced invalid. The necessary refinement-preserving hypothesis has not been supplied. Any rigorous full-LOCC deduction would need to quantify over all admissible refinements and their intermediate product-operator paths, not just Z_binary.

**Immediate scientific consequence:** R07's assertion \(\delta(q)>0\) for the operational LOCC supremum does not follow from its binary-zonotope argument. R07's statement of **LOCC-closure nonmembership is withdrawn pending replacement proof**. R08's bound \(\delta(q)\le V_H-\max(V_X,V_{\rm adaptive})\) remains a valid upper bound because it has a concrete achievable LOCC protocol; lower bound from this lineage is only the tautological \(\delta(q)\ge0\).

## 2. What is ACTUALLY proved: a quantitative restricted binary-zonotope product-minor lemma

The original 3-probe source model remains unchanged: \(q=\gamma T/3>0\), \(x=e^{-q}\), \(b=1-x^2\). Its endpoint difference \(D(q)=\rho_A-\rho_B\) has positive spectral subspace P=span\{|W>,|\bar W>\}, negative subspace Q, and zero subspace K0. The least nonzero absolute eigenvalue is

 \(\mu(q)=b(1-x)/8=((1-e^{-2q})(1-e^{-q}))/8>0.\)

Helstrom \(\mathrm{TV}_H=b/2\). For any candidate binary decision POVM \(\{E,I-E\}\), orient the labels so \(\mathrm{TV}(E)=\mathrm{Tr}(ED)\ge0\), and let \(\Delta=\mathrm{TV}_H-\mathrm{TV}(E)\ge0\).

### Elementary spectral stability estimate

Because all positive and negative eigenvalues of D have magnitude ≥μ and \(0\le E\le I\):

 \(\Delta=\mathrm{Tr}[(I-E)D_+]+\mathrm{Tr}[E(-D_-)]\)
 \(\quad\ge\mu(\mathrm{Tr}[P(I-E)]+\mathrm{Tr}[QE]).\)                    (1)

Set \(e=\Delta/\mu\). Since \(E\) and \(I-E\) are contractions, for any vector p∈P and v∈Q:

 \(\|(I-E)p\|\le\sqrt e\,\|p\|,\quad\|E v\|\le\sqrt e\,\|v\|.\)       (2)

For a computational-basis string of weight one or two, its projections obey \(\|P|z\rangle\|=1/\sqrt3\), \(\|Q|z\rangle\|=\sqrt{2/3}\), with no kernel component. Consequently,

 \(\|(E-P)|z\rangle\|\le\sqrt e\,(1+\sqrt2)/\sqrt3<\sqrt{2e}.\)       (3)

Put \(\varepsilon=\sqrt{2e}\). For the indices (001,010,011) of the 8×8 matrix, the exact ideal P entries are:
 \(P_{001,010}=1/3,\;P_{011,011}=1/3,\;
 P_{001,011}=0,\;P_{011,010}=0.\)

Thus:
 \[
 |E_{001,010}-1/3|\le\varepsilon,\quad
 |E_{011,011}-1/3|\le\varepsilon,\quad
 |E_{001,011}|,|E_{011,010}|\le\varepsilon. \tag{4}
 \]

### An exact product minor and its quantitative consequence

Any nonnegative product \(F=A\otimes B\otimes C\) obeys the matrix identity

 \[
 \boxed{F_{001,010}\,F_{011,011}
        =F_{001,011}\,F_{011,010}.} \tag{5}
 \]

This follows by factoring each matrix element into the corresponding 2×2 local entries. Tested independently for 300 randomly generated PSD product triples (machine precision); the algebra is exact.

Now restrict to the **BINARY decision zonotope**, not the full fine-grained LOCC process:

 \(F=\alpha E+\beta(I-E)=\beta I+dE,\quad
  0\le\alpha,\beta\le1,\quad d=\alpha-\beta.\)

If d≠0 and ε<1/6, then:
- \(|F_{001,010}|\ge |d|(1/3-\varepsilon)\);
- \(F_{011,011}=\alpha E_{011,011}+\beta(1-E_{011,011})
               \ge(\alpha+\beta)(1/3-\varepsilon)\);
- \(|F_{001,011}|,|F_{011,010}|\le |d|\varepsilon\).

Substitute into (5), using \(|d|\le\alpha+\beta\). It would require
 \((1/3-\varepsilon)^2\le\varepsilon^2\),
contradicting \(\varepsilon<1/6\).

Therefore the rigorously correct statement is:

 \[
 \boxed{
 \Delta<\mu(q)/72 \implies
 \text{every positive PRODUCT }F\in Z_{\rm binary}
 \text{ is proportional to } I.
 } \tag{6}
 \]

This is a sharp-enough **restricted algebraic obstruction to a product path inside two aggregated decision effects**; it is NOT the operational discrimination no-go. The word LOCC does not belong in the consequent of (6).

At q=1/3:
 \(\mu(1/3)=0.01724137644563263\);
 \(\mu(1/3)/72=0.00023946356174489765.\)

The latter is a proven threshold for the RESTRICTED binary-zonotope statement (6), **NOT** a certified numerical lower bound on \(\delta_{\rm LOCC}\). A formerly created R09 Python code artifact had a misleading title and initial printed status; its header and output have been UPDATED with the explicit correction. Do not quote its filename as a result.

## 3. Exactly what survives, what is withdrawn

**Still supported (within frozen model and review ceiling):**
- PRF11 R35: original correlated-Cauchy/Lévy synthetic states.
- PRF12 R03: exact n=2 local X parity sufficiency in its special source contract.
- PRF12 R04: exact n=3 positive Helstrom vs local X gap, explicit source-active finite-gate numerical controls.
- PRF12 R05: explicit separable 28-product-effect endpoint POVM reaches Helstrom mathematically. SEP ≠ automatically LOCC.
- PRF12 R06: direct first-local-step orthogonality-preservation argument rules out an exactly Helstrom-optimal FINITE-ROUND three-party LOCC protocol, pending independent referee. This argument does not invoke Cohen's coarse-binary zonotope and is not automatically invalidated here.
- PRF12 R08: exact three-lab adaptive LOCC X→conditional X/Y→last-qubit Helstrom witness with TV=0.198464903476238 at q=1/3; this is an admissible LOCC lower witness for achievable distinguishability.

**WITHDRAWN / not proved:**
- PRF12 R07 asserted full \(\overline{\rm LOCC}\) exclusion and \(\delta(q)>0\), because binary decision grouping was treated as if it preserved product-POVM leaf structure.
- R08 inherited \(\delta>0\) from R07; remove that inherited positivity but keep constructive upper bound.
- The initially conjectured R09 numerical \(\delta(q)\ge\mu(q)/72\) for unrestricted closure LOCC.

**Current honest interval at q=1/3:**
 \[
 \boxed{0\le\delta_{\rm LOCC}(1/3)
     \le0.243291440483704-0.198464903476238
     =0.044826537007466.}
 \]
Our mathematical understanding makes strict positive δ plausible but this is now **an OPEN inference** for the unrestricted LOCC closure, not a theorem. No physical resource cost or universal device limitation follows.

## 4. Falsifiers, future correction route and custodian instructions

1. Show an explicit refined LOCC family whose binary decision E lies near the optimal family, such that refined product-paths escape the binary Z despite absence of product paths therein — the parity construction already shows this mechanism generically.
2. To revive positive \(\delta_{\rm LOCC}\), prove a no-approximation theorem quantifying over ALL fine-grained leaf decompositions and conditional communications, not simply \(\{E,I-E\}\). Candidate: a refined-outcome version of Cohen's necessary path constraint, or a direct quantitative version of orthogonality-preserving first local measurements with a bound across arbitrary rounds.
3. R06 finite-round proof needs a separate referee of its induction when outcomes are arbitrarily weak, and cannot be silently extended to closure LOCC.
4. Independently check (1)–(6), especially weight-one/two spectral overlaps and the 2×2 product minor identity. The code tests specific dimensions and the exact 8×8 D; it is not a full enumeration of LOCC.
5. Reassess 2022 Cohen paper under precise distinction between a measurement with fully specified classical label distribution and the binary *discrimination strategy* after postprocessing. Do not ascribe a false theorem to the author; record the extra hypothesis needed in this project.
6. No background-dependent, physical gravitational, NCDG K/J3, publication-priority, CANON or EXEC claims.
7. All outputs are in GitHub scientific corpus, not demonstrated in BW (status GITHUB_PENDING_BW_INGEST). Review independent remains pending.

### Source code and audit custody

Corrected restricted-matrix reproducer (legacy, misleading filename preserved so external links do not break):
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R09_EXPLICIT_POSITIVE_LOCC_GAP_MATRIX_MINOR_REPRO_001_20261026.py

R07 and R08 original reports have been patched *in place* with prominently displayed correction notices and changed status metadata; original reasoning remains visible below, only as an **audited historical claim**. A report without correction notice must not be treated as current.

## 5. RETURN

PRF12_R09 / CRITICAL_SOURCE_VALIDATION / COARSE_GRAINING_COUNTEREXAMPLE / RESTRICTED_PRODUCT_MINOR_LEMMA_PROVEN / FULL_ASYMPTOTIC_LOCC_POSITIVE_GAP_NOT_ESTABLISHED / R07_CLAIM_WITHDRAWN / R08_LOCC_ACHIEVABLE_WITNESS_PRESERVED / NO_NUMERIC_LOCC_LOWER_GAP_BOUND / INDEPENDENT_REFEREE_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC / GITHUB_PENDING_BW_INGEST / PRF12_SUCCESSION_PACKET_UNREAD.
