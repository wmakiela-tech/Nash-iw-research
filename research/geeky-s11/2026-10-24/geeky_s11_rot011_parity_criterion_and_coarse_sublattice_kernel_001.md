---
artifact_id: GEEKY-S11-ROT011-PARITY-CRITERION-AND-COARSE-SUBLATTICE-TT-KERNEL-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-24
problem_id: P3_DTC0A_FINITE_CENTERED_STENCIL_PARITY_AND_TT_GHOST_DEGENERACY_001
exposure: PUBLIC_SAFE
class: EXACT_FINITE_FOURIER_STENCIL_CLASSIFICATION_AND_EXPLICIT_48D_COARSE_GRID_TT_KERNEL
status: SOURCE_TYPED_MATHEMATICAL_PROOF_AND_INDEPENDENT_NUMPY_PASS / REFEREE_PENDING
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: MATURE_FOURIER_AND_ODD_EVEN_DECOUPLING_HOST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT011 — parity of arbitrary centered stencils and growth of spurious TT-preserving subspace

## 0. Research question and owners-first

Geeky-S11 ROT007–010 previously compared fixed second- and fourth-order stencils and showed an exact checkerboard-preservation vs nonpreservation bifurcation in one order-four interpolating family. This rotation *classifies every nonzero finite centered scalar first-derivative stencil* (under a strict no-spatial-alias radius) for the specific full-checkerboard TT symmetry, then gives an independent, more degenerate even-offset example with 48 real TT-preserving generator directions. It does **not** generalize historical DTC0a raw-k projector physics. INT8 (shear filter), PRF11 (original raw-k collocation), M13 (historical source h=fI masked RMS), XH-S4 (curved York), and MT13 (transported metric operators) remain separate owners.

External mature-host subtraction: odd/even decoupling and checkerboarding in centered finite differences are classical. A generic mature mathematical source is *A phenomenon of artificial odd–even grid oscillation ...*, Journal of Computational and Applied Mathematics 333 (2018), DOI 10.1016/j.cam.2017.10.017. The fluid collocated-grid literature also treats checkerboard pressure modes and odd/even grid decoupling, e.g. *A symmetry-preserving second-order time-accurate PISO-based method* (2021), https://www.sciencedirect.com/science/article/pii/S0045793021001468 . Neither source establishes the present special TT-subspace theorem; **no original-mathematics novelty is claimed**.

## 1. Precisely typed carrier

Let N be even and N>2R, h=2π/N. Define the same one-dimensional nonzero centered translation-invariant first derivative in each of three coordinate directions by

D_j F(n) = (1/(2h)) sum_{r=1}^R a_r [F(n+r e_j)-F(n-r e_j)],

with real a_r not all zero. Its Fourier symbol is i d_m where

d_m=(1/h) sum_{r=1}^R a_r sin(2π r m/N).

Set δ(k)=(d_{k_x},d_{k_y},d_{k_z}). At δ!=0 define the *matched-symbol* orthogonal rank-two tensor Fourier TT projector P_D by π=I-δδᵀ/|δ|², P_DF=πFπ−(π/2)tr(πF). Set P_D=0 at δ=0 (all such modes); Q_D=I-P_D. Work in the real symmetric covariant 2-tensor grid Hilbert space with full-grid unmasked L2/Frobenius norm.

Let (L_C^D F)_ij=C^m D_m F_ij+F_mj D_i C^m+F_im D_j C^m. Define χ(n)=(-1)^{n_x+n_y+n_z}, C=χ e_x. Every centered antisymmetric derivative annihilates χ, hence L_C^D F=χ D_xF. Scalar translation-invariant Fourier filters E commute with both D and P_D. The theorem below first fixes E=I; preservation for *all* E is then a direct corollary of parity purity.

## 2. General exact parity classification (Theorem R11.1)

For N even, N>2R, nonzero stencil a, E=I:

  **Q_D L_{χ e_x}^D P_D=0 on all symmetric tensors IF AND ONLY IF every r with a_r≠0 has the same parity.**

In particular, odd-only and even-only stencils both preserve the full TT range under the χ e_x action. Mixed parity stencils fail to preserve TT, even though Dχ=0.

**Proof, sufficiency.** Fourier multiplication by χ shifts every coordinate frequency by N/2. The shifted first-derivative symbol obeys

d_{m+N/2}=(1/h) sum_r (-1)^r a_r sin(2πrm/N).

If all contributing shifts r are odd, d_{m+N/2}=−d_m; if all are even, d_{m+N/2}=+d_m. Thus δ(k+ν)=±δ(k), ν=(N/2,N/2,N/2), with the same global sign in all three directions. Hence P_D(k+ν)=P_D(k) at every k including δ=0. Multiplication by χ commutes with P_D. Therefore Q_D χ D_x E P_D=0 for **every scalar Fourier multiplier E**, whether invertible or not, on this exact host.

**Proof, necessity for E=I.** Denote d'_m=d_{m+N/2}. At any input mode k with d_{k_x}≠0, χD_x has a nonzero Fourier scalar factor and shifts output to k+ν. If full-TT preservation holds, the two-dimensional symmetric transverse-traceless fibre P_D(k) must be contained in P_D(k+ν). At nonzero symbols both have rank two, so their equality demands δ(k+ν) parallel to δ(k); if δ(k+ν)=0, the output projector is zero and the nonzero input fibre leaks entirely. Axial modes k=(m,0,0) force d'_m≠0 whenever d_m≠0. If d_m=0 and d'_m≠0, choose k=(s,m,0) with d_s≠0: the shifted symbol gains a component transverse to the input symbol, contradicting preservation. Thus d and d' have identical zeros. Oblique k=(m,n,0), d_m,d_n≠0, force d'_m/d_m=d'_n/d_n. Consequently d'_m=c d_m for all m and some c≠0. Applying the half-grid shift twice gives c²=1, so c=+1 or −1. Because R<N/2, discrete sine harmonics sin(2πrm/N), r=1..R are linearly independent. The relation d_{m+N/2}=c d_m therefore implies [(-1)^r−c]a_r=0 for each r. Thus all nonzero offsets have exactly one parity. QED.

No statement is made about **one specially tuned nonidentity E** potentially masking a mixed-stencil witness. The universal statement “preserved for every scalar E iff parity-pure” follows immediately since E=I is included.

## 3. Exact symbol parity-gap identities (Theorem R11.2)

Let a_even and a_odd denote the subvectors of stencil coefficients at even and odd offsets. For R<N/2, discrete Fourier sine orthogonality yields the exact finite-N identities

  sum_{m=0}^{N−1}|d_{m+N/2}−d_m|² = (2N/h²) sum_{r odd} a_r²;
  sum_{m=0}^{N−1}|d_{m+N/2}+d_m|² = (2N/h²) sum_{r even} a_r².

Thus a preflight test requiring no tensor computation distinguishes parity-pure cases from mixed cases. The nearest ± periodic/antiperiodic discrete symbol mismatch is exactly

  min_{σ=±1}||d_shift−σd||_{ℓ²}=(√(2N)/h) min(||a_odd||₂,||a_even||₂).

This is a sharp **symbol-domain** mismatch, not an operator-norm lower bound for Q L_C P. The latter additionally depends on transverse angular defects and the input derivative amplitude.

## 4. Coarse two-step derivative: exact 48-dimensional preserving kernel (Theorem R11.3)

Let N≥8 be divisible by four and choose only a₂=1/2, so D=(T_{+2}−T_{−2})/(4h), with symbol d(θ)=sin(2θ)/(2h). Its one-dimensional zeros on the N-grid are exactly m∈{0,N/4,N/2,3N/4}, four values. The discrete conformal-strain operator C↦dev(sym DC) has **exactly 3·4³=192 real kernel dimensions**: any component C has arbitrary Fourier data on the 64 zero-symbol grid corners (all real degrees counted with conjugate symmetry).

For E=I, the **actual full TT preservation kernel** of C↦Q_D L_C^D P_D is exactly **48 real dimensions**, namely all real vector fields with Fourier support restricted to the 16 zero-symbol corners indexed r∈(Z₄)³ such that **r_x,r_y,r_z have identical parity** (all even or all odd):

  K₄₈ = span_real {e_j χ_r : r∈{0,2}³ ∪ {1,3}³, j=x,y,z},
  χ_r(n)=exp[(πi/2)r·n].

Here span_real means real-valued vector fields, respecting conjugate Fourier pairing. Eight all-even corners are individually real and contribute 24 real component degrees; eight all-odd corners form four conjugate pairs and contribute 24 additional real degrees.

**Necessity.** The original twelve axial sine/cosine exactly TT probes at first harmonic still give the ROT002 tight trace frame (E=I), which forces dev(sym DC)=0; the Fourier symbol injectivity of conformal strain at δ≠0 then restricts C to the 64 zero-symbol corners. At one such character χ_r, the output derivative symbol shifts component j by factor (−1)^{r_j}. The 12 oblique TT tests at k=±(e_a±e_b) (three pairs, signs ± and real phases sin/cos) detect the 48 corners where parity is not shared by all r components: for a pair (a,b) with opposite parity, the TT direction changes and the Q-rejected polarization squared Frobenius norm is 3/2, while the input squared norm is 2. Writing the Fourier vector coefficients c_r (real field: conjugacy enforced), the exact summed oblique frame has form

  sum_{12 oblique probes}||Q_D L_C^D H||² = 3 d_1² W(C),
  W(C)=sum_{r∈(Z₄)³} sum_{a<b:r_a mod2 !=r_b mod2}(|c_{r,a}|²+|c_{r,b}|²).

The sine/cosine phase pairing kills any overlaps of the ± input/output modes; Fourier orthogonality separates different r. For each of the 48 forbidden r (not all-even and not all-odd), at least two coordinate pairs have opposite parity, and W_r≥|c_r|². Hence vanishing whole-TT leakage forces all those coefficients to zero.

**Sufficiency.** If all r_j are even then δ(k+ r N/4)=+δ(k); if all are odd then δ(k+r N/4)=−δ(k). In both cases P_D stays identical under the Fourier shift χ_r. All such C also obey DC=0. Thus χ_r D commutes with P_D and Q_D L_C^D P_D=0 by linearity. QED.

**Consequence.** More null modes in DC (192 rather than 24) do *not* mean all of those 192 modes preserve the full TT range. However, coarse stencils can produce many extra *genuine discrete TT-preserving generators*, not only the three full-checkerboard directions of ROT004–006. The 48D statement is for E=I; all 48 remain sufficient preservers with any scalar Fourier E. An iff for every exceptional E is NOT claimed.

## 5. Independent executed numerical controls

The standalone NumPy source file `geeky_s11_rot011_stencil_parity_kernel_verify.py` implements all grid-space centered derivatives, the scalar seven-point E_alpha filter, the complete three-term tensor Lie action (including DC gradient), and the matched-symbol Fourier TT projector. It is independent of archived historical DTC production bytes.

- 36 full-grid tests: N∈{12,16,20} × 6 coefficients stencils × α∈{0,.05}. For each row a broadband random P_D-TT field and a deterministic oblique TT carrier are tested. All 36 PASS. Maximum false-positive ghost preserver leakage is 1.11e−15; every mixed stencil has a true TT witness with relative leakage >=0.10248.
- 18 independent scalar Fourier parity-gap identities tested, all PASS (maximum absolute residual 1.14e−13 versus quantities reaching ≈562, relative rounding-level).
- 6 coarse-step full 3D random TT tests: N∈{8,12,16} × α∈{0,.05} on a randomly generated real field with all 16 allowed Fourier corners versus another with all 48 disallowed Fourier corners. All 6 PASS. Allowed leakage ≤5.24e−16; forbidden leakage >=0.05473. Every test recovers exactly four sampled one-dimensional derivative zeros and the dimension counts 192 and 48.

Total **60 PASS checks**, organized as 36 whole-TT parity probes, 18 exact symbol identities, 6 coarse-grid controls. No global operator-norm numerical optimization was required. The 48D classification itself is an exact Fourier/frame proof, not inferred from random experiments.

## 6. Claim ceiling and next decision

- The projector P_D is *specifically matched to this finite-difference derivative*. These claims are not valid if one silently substitutes the historical DTC0a raw wavevector P_TT or a curved, metric-dependent York projector.
- These are unmasked spatial-grid operator claims only, not source historical h=fI K_A plateau, nor a physical observable, gauge-invariance or NCDG J3/K diagnostic.
- All checkboard generators are grid-scale, with no fixed smooth N→∞ representative.
- Odd/even decoupling is classic numerical-analysis prior art; no novelty claim for the abstract mathematical operator theorem.
- STOP expanding the ROT007–010 finite examples as though they were a physical sequence. The only new scope is the *generic structural classification and the explicit 48D degeneracy counterexample*. Independent referee, BW and scientific owner uptake pending; no EXEC authorization.

NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / INDEPENDENT_REFEREE_PENDING / BW_PENDING.
