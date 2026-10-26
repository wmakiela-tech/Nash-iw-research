---
artifact_id: IW_PRF12_R11_NINE_EFFECT_PRODUCT_SIMPLEX_MINIMAL_HELSTROM_REFINEMENT_001_20261026
created_at: 2026-10-26
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
problem_id: PRF12_R10_MINIMAL_RANK_ONE_PRODUCT_REFINEMENT
exposure: PUBLIC
canonical_body_path: research/prf12/2026-10-26/IW_PRF12_R11_NINE_EFFECT_PRODUCT_SIMPLEX_MINIMAL_HELSTROM_REFINEMENT_001_20261026.md
sync_state: GITHUB_PENDING_BW_INGEST
status: ANALYTIC_EXACT_PRODUCT_9_FRAME_CONSTRUCTION / MINIMAL_RANK_ONE_PRODUCT_OUTCOME_PROOF_LOCAL / REPRODUCTION_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_GLOBAL_MINIMAL_POVM / NO_HIGHER_RANK_PRODUCT_MINIMALITY / NO_LOCC_IMPLEMENTABILITY / NO_FULL_BINARY_LOCC_GAP / NO_FINITE_PULSE_SOURCE_ACTIVE_TRANSFER / NO_NOVELTY_OR_PRIORITY_CLAIM / NO_CANON / NO_EXEC_SIGN
function: SCIENCE_FIRST / LITERATURE_FIRST / TWO_SURFACE_PRIOR_ART / NEGATIVE_KNOWLEDGE / FALSIFIER_FIRST
---

# PRF12 R11 — Nine product effects form an exact C8 simplex and are count-minimal in the rank-one product POVM class

**Date:** 26 October 2026. **Owner:** PRF12. **Scope:** exact ideal-source three-probe endpoint; scientific status local analytic proof plus numerical consistency tests, pending independent referee. **Strong result:** the R05 28-effect and R10 10-effect separable refinements can be sharpened to a **nine-effect separable POVM**, and nine is the **smallest possible number of rank-one PRODUCT effects** that can attain the endpoint Helstrom bound for this frozen source pair. **Critical boundary:** this does NOT prove any three-laboratory LOCC attainability, LOCC closure gap, or rank>1 effect minimality.

## 0. Scientific owners and mature external host

**Internal origin:** PRF11 R35 static Cauchy frequency vs independent Cauchy–Lévy increments and ideal SWAP: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R35_NONUNIFORM_SWAP_TIME_GRID_RECOVERS_IDEAL_MEMORY_WITH_CRITICAL_STORAGE_RATE_001_20261025.md .
PRF12 R04 exact n=3 8×8 spectral operator and fixed-local-X gap: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R04_THREE_PROBE_FINITE_SWAP_EXACT_X_READOUT_GAP_AND_SECTOR_DECOMPOSITION_001_20261026.md .
PRF12 R05 28 product effects: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R05_SEPARABLE_HELSTROM_POVM_PRODUCT_BASES_AND_ONE_CNOT_RESOURCE_AUDIT_001_20261026.md .
PRF12 R06 exact finite-round LOCC local-rigidity candidate: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R06_EXACT_SEP_VS_LOCC_NO_GO_LOCAL_ORTHOGONALITY_RIGIDITY_001_20261026.md .
PRF12 R09 correction of R07 coarse-graining, retaining LOCC closure gap OPEN: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R09_COARSE_GRAINING_COHEN_THEOREM_AUDIT_AND_CORRECTED_CLAIM_CEILING_001_20261026.md .
PRF12 R10 full ten-label refinement and corrected Cohen path scope: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R10_REFINED_LOCC_PROOF_SUPPLEMENT_001_20261026.md .

**Mature external mathematics, NOT PRF12 novelty:**
- L. Welch, "Lower bounds on the maximum cross correlation of signals" (1974), original Welch bound for unit vectors.
- Fickus, Jasper, King, Mixon, *Equiangular tight frames that contain regular simplices*, Linear Algebra and its Applications 555 (2018), 98–138, DOI https://doi.org/10.1016/j.laa.2018.06.004 . N=d+1 complex tight frames are regular simplices and the Welch-bound equality criterion is classical.
- Fickus, Lake, *Doubly Transitive Equiangular Tight Frames That Contain Regular Simplices* (2025), a later external treatment of simplex structures. https://scholar.afit.edu/facpub/2334/
- Cohen, *Local approximation of multipartite quantum measurements*, Phys. Rev. A 105, 022207 (2022), DOI https://doi.org/10.1103/PhysRevA.105.022207 . LOCC-vs-SEP outcome-refinement caveat from R09 is preserved. The Cohen theorem is **not needed** for the SEP9 existence/minimality result.

The origin of the novel-to-this-cell *specific parameterization* is an independent C3-orbit search, then analytic root-of-unity reconstruction. No claim of new general frame theory, unique frame, publication priority, or experimentally implemented measurement.

## 1. Frozen source contract and projectors

Exactly n=3 qubits initialized |+>³, two ideal instantaneous SWAPs, three equal exposure times T/3, and κ=0 (no storage dephasing). A = one global hidden Cauchy(0,γ) draw held constant during all exposure intervals. B = independent symmetric Cauchy–Lévy increments. Let q=γT/3>0.

The signed endpoint matrix difference in computational bits a,b∈{0,1}³:

 D(q)_{ab}=1/8[exp(−q|Σ_j(a_j−b_j)|)−exp(−qΣ_j|a_j−b_j|)].

Use normalized vectors
 W=(001+010+100)/√3, Wbar=(110+101+011)/√3, g=(000+111)/√2;
 P=|W><W|+|Wbar><Wbar|; K=|000><000|+|111><111|; Q=I−P−K.

As proved first in R04, the strictly positive eigenvalues of D are (1−e^(−2q))(2±e^(−q))/8 and P is its positive spectral support; Q is its strictly negative support and K its kernel. Endpoint Helstrom:

 V_H(q)=(1/2)||D(q)||_1=(1−e^(−2q))/2.                  (1)

No statement about optimal adaptive process testers or quantum devices.

## 2. Exact nine PRODUCT vectors from ninth roots of unity

Let η=exp(2πi/9), ω=η³=exp(2πi/3). Define the normalized equatorial single-qubit ket e(z)=(|0>+z|1>)/√2 for |z|=1, and the normalized three-qubit product ket

 v(r1,r2,r3)=e(η^r1)⊗e(η^r2)⊗e(η^r3),

where exponents are integers modulo 9.

Specify the nine triples of exponents IN FULL:

| Decision A: 3 symmetric rays | Decision B: 6 asymmetric rays |
|---|---|
| (0,0,0) | (1,4,7) |
| (3,3,3) | (4,7,1) |
| (6,6,6) | (7,1,4) |
| | (5,2,8) |
| | (8,5,2) |
| | (2,8,5) |

Let these unit vectors be v_1,...,v_9 in this order. Set every rank-one effect to the SAME weight:

 F_j=(8/9)|v_j><v_j|, j=1,...,9.                    (2)

They are positive rank-one PRODUCT effects. The first three decision labels are + (A), the remaining six − (B). All v_j are independent of q.

## 3. Theorem R11.1 — an exact equiangular tight frame, no rounding needed

**Claim:** for all j≠k, |<v_j|v_k>|=1/8. Proof:

For exponent triples a,b,
 <v(a)|v(b)>=1/8 ∏_{h=1}³(1+η^(b_h−a_h)).
 
There are just two nontrivial combinatorial cases:
- Within any one cyclic family, differences of each of the three exponents are ±3 mod 9, giving the product (1+ω)^3 or (1+ω²)^3, of absolute value 1.
- Between two distinct exponent families (A vs either B, or the two B opposite-parity families), the three exponent differences form one complete residue triple (r,r+3,r+6) mod 9, with r not divisible by 3. Therefore their factor product is
  ∏_{j=0}²(1+η^r ω^j)=1+η^(3r)=1+ω^r
  using 1+ω+ω²=0; its magnitude is 1.

These exhaust all 36 unordered pairs. Thus |<v_j|v_k>|²=1/64 for each j≠k.

Now apply the elementary frame-potential inequality for N=9 unit vectors in d=8:
 Tr[(VV†)²]=Σ_{j,k}|<v_j|v_k>|² ≥ N²/d=81/8,
 equality iff VV†=(N/d)I_8.
But the left side is exactly 9+9×8/64=81/8. Consequently equality holds and

 Σ_{j=1}^9|v_j><v_j|=(9/8)I_8,
 **Σ_{j=1}^9 F_j=I_8 exactly.**                   (3)

This is an N=d+1 equiangular tight frame, also called a complex regular simplex; it is NOT a 64-vector SIC POVM in d=8 and must not be misnamed as such.

## 4. Theorem R11.2 — the nine-effect POVM achieves exact Helstrom for ALL q>0

The first three vectors are symmetric powers e(ω^k)^{⊗3}; hence their support is contained in span(000,W,Wbar,111), the symmetric subspace orthogonal to Q. Explicit third-root averaging gives

 Eplus=Σ_{j=1}³ F_j=P+(2/3)|g><g|.                (4)

Proof: components of each v(3k,3k,3k) along (000,W,Wbar,111) are
 (1,√3 ω^k,√3 ω^(2k),1)/√8.
Averaging k=0,1,2 deletes offdiagonal terms between distinct mod-3 Fourier characters. The W and Wbar eigenweights are 3*(8/9)*(3/8)=1 each. The (000,111) block has coefficient 3*(8/9)/8=1/3 in all its four entries, exactly (2/3)|g><g|.

For every B-labeled product vector, its three local phase ratios are a permutation of z(1,ω,ω²), with z=η or η^5. Thus both
 Σ_j z_j=z(1+ω+ω²)=0
 and
 Σ_{i<j}z_i z_j=z²(ω+ω²+1)=0.
It is orthogonal to W and Wbar, so its effect has zero support in P. From the tight-frame identity (3):

 Eminus=Σ_{j=4}^9 F_j=I−Eplus
       =Q+K−(2/3)|g><g|.                             (5)

The kernel K contributes zero to Tr(Eplus D), so Eplus is a Helstrom-optimal binary decision effect. Therefore

 **V_SEP9(q)=Tr(Eplus D(q))=(1−e^(−2q))/2=V_H(q)**
 for all q>0.                                          (6)

No source-active finite-SWAP / fixed κ / cross-cell physical claims.

## 5. Theorem R11.3 — nine outcomes are MINIMAL among rank-one PRODUCT effects

Let a POVM with N nonzero effects F_l=w_l|a_l,b_l,c_l><a_l,b_l,c_l|, w_l>0, be complete on C²⊗³ and Helstrom-optimal for D(q) at a fixed q>0. Classical postprocessing may group fine outcomes into the two decisions; splitting an effect classically cannot improve the rank-count argument.

**Step 1:** completeness Σ_l F_l=I_8 implies N≥8, because a sum of N rank-one matrices has rank ≤N.

**Step 2:** if N=8, form the square 8×8 matrix whose columns are √w_l |a_l,b_l,c_l>. Then VV†=I_8 and V is unitary, so all eight effects are orthogonal unit-weight rank-one projectors onto a complete PRODUCT orthonormal basis.

**Step 3:** exact Helstrom equality forces each positive-decision vector to have zero overlap with Q. For product vectors, this is equivalent (R10 and independent elementary exchange-symmetry check) to being fully symmetric: |u>⊗³ for a single-qubit ket u. Two such product vectors are orthogonal iff their local qubit factors are orthogonal: <u³|v³>=<u|v>³. In C² at most TWO symmetric-cubic product vectors can be mutually orthogonal.

**Step 4:** however a positive Helstrom binary effect must act as identity on the rank-two positive eigenspace P. It cannot be made from one positive rank-one vector, nor from only TWO positive rank-one vectors: in the latter case their two-dimensional span must equal P, but P contains no nonzero product vector. Indeed a symmetric-cubic ket (a|0>+b|1>)⊗³ has amplitudes a³ on |000> and b³ on |111>; belonging to P requires both amplitudes zero, so a=b=0. Thus **AT LEAST THREE** distinct positive-labeled product vectors are necessary.

Contradiction with the two-vector orthogonality limit in any N=8 POVM. Therefore N≥9. The explicit N=9 construction of §2 saturates this bound.

**Quantifier/ceiling:** minimum is only within POVMs whose each nonzero fine effect is PRODUCT AND RANK ONE, even after optimized final classical decision. Does not prove minimum over positive higher-rank product effects, separable but nonproduct coarse effects, jointly measured entangled POVMs, LOCC, or auxiliary system constructions. Does not prove uniqueness of the 9-frame.

## 6. Numeric independent reproduction and falsifiers

Independent direct NumPy run, constructing all nine tensor products and source-state D(q) from characteristic functions:

- All 36 |Gram offdiagonal| lie in [0.12499999999999972,0.12499999999999996] vs exact 1/8.
- max matrix-entry |Σ_j F_j−I| ≈1.9984e−15.
- Gram spectrum: 0 once, 9/8 eight times, within machine precision.
- max |Eplus−P−(2/3)|g><g|| ≈6.11e−16.
- For q in {.05,1/3,.7,1.4,3}, direct spectral Helstrom TV and direct SEP9 TV equal the closed (1−exp(−2q))/2, discrepancies ≤7e−16.
- No random optimizer is used in final reproduction: fixed ninth-root exponents generate all rays, with no fitted runtime parameters.

Source:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R11_NINE_PRODUCT_SIMPLEX_REPRO_001_20261026.py

R11 future falsifiers/review:
1. Re-derive the classification of B rays from W/Wbar orthogonality and check that all listed B vectors satisfy it.
2. Verify all 36 exact pair cases (especially opposite-parity C3 orbit differences) and Welch/frame-potential equality.
3. Verify P+2/3|g><g| exactly from root filtering; κ=0 and equal exposure assumptions must stay fixed.
4. Check the N=8 argument allowing arbitrary classical postprocessing and possible kernel-only outcomes.
5. Search existing literature for *the same particular nine-product-vector simplex* before any novelty/priority claim. Present search supports only mature general ETF theory and does not establish original discovery.
6. Check mathematical full ten-label Cohen closure audit separately; N=9 outcome minimality is independent of Cohen's theorem and does not resurrect R07.
7. The operational asymptotic three-party binary LOCC gap remains OPEN after R09; no stable numerical positive lower bound is derived.
8. Independent referee still pending. No BW synchronization readback or EXEC; no physical validation.

## 7. Source-typed return

PRF12_R11 / EXACT_9_PRODUCT_EFFECT_COMPLETENESS / C8_EQUANGULAR_TIGHT_FRAME_9 / PRODUCT_RANKONE_OUTCOME_MINIMALITY_PROVED_LOCAL / EXACT_HELSTROM_FOR_ALL_Q_IDEAL_N3 / INDEPENDENT_NUMPY_MATRIX_REPRO_PASS / NO_LOCC_IMPLEMENTABILITY / BINARY_LOCC_CLOSURE_GAP_OPEN / INDEPENDENT_REFEREE_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC / GITHUB_PENDING_BW_INGEST.


## Later R12 strengthening — 2026-10-27

PRF12 R12 proved that, for the SAME frozen n=3 ideal SWAP Cauchy/Lévy source pair and exact endpoint Helstrom performance, **every nonzero PRODUCT positive operator effect in an exactly optimal fine-grained POVM is automatically rank one**, even if its local factor ranks were not initially restricted. The R11 nine-outcome minimality therefore holds among ALL individually PRODUCT PSD effects, not merely the initially assumed rank-one subfamily. Crucial proof: no two-dimensional product-factor slice lies in either Q-perp=Sym^3(C²) or P-perp, the latter following from the polynomial identity (b0+b1*t)(c0+c1*t)=0 implying a zero local ket. This does NOT imply minimum nine for general SEPARABLE summed effects, LOCC closure nonapproximability, or any real device cost. Full theorem and new equatorial adaptive LOCC witnesses: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-27/IW_PRF12_R12_RANKONE_RIGIDITY_PRODUCT_EFFECT_MINIMALITY_AND_EQUATORIAL_LOCC_001_20261027.md . Independent referee pending.
