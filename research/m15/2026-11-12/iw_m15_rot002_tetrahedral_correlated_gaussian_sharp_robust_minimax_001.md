---
artifact_id: IW_M15_ROT002_TETRAHEDRAL_UNKNOWN_WITHIN_GROUP_CORRELATION_MINIMAX_001_20261112
return_id: M15-ROT002-CORRELATED_GAUSSIAN_FOUR_AXIS_SHARP_MINIMAX_001_20261112
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-12
exposure: PUBLIC
result_class: EXACT_CLASSICAL_CONDITIONAL_MINIMAX / ANTI_REDISCOVERY / SOURCE_TRANSFER_GATE
claim_ceiling: NO_NOVELTY / NO_NASH_PHYSICAL_CLAIM / NO_NATIVE_NV_CORRELATION_DATA / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE / NO_NEW_TASK_CASCADE
sync_state: GITHUB_PENDING_BW_INGEST
---

# M15 ROT002 — exact robust tetrahedral Gaussian risk under unknown within-group correlation

## 0. Question and prior ownership

Does M14 ROT039/ROT041's exactly sharp four-orientation independent-Gaussian risk 3 sigma²/N stay valid if each simultaneous orientation has the SAME known marginal variance sigma² but unrestricted admissible within-group correlation? **NO.** With N=4m predeclared readings from m complete four-axis simultaneous groups, block independent, static unknown z, arbitrary group-specific unbounded common scalar offset and one common unknown PSD correlation C with diag C=1, the **sharp all-estimator global minimax is 4 sigma²/N**. The ratio is 4/3, a 33⅓% increase over independent channels; the original M14 claims remain fully valid in their original independent model.

Firstness preserved: M14 ROT031 original tetrahedral geometry; M14 ROT039 independent Gaussian sharp four-axis common-mode risk (blob 80e678005d4a0edd0c6299d8b582e0199f464a8f), M14 ROT041 independent-Gaussian finite calendar graph and risk (blob 357d823e604fabfc86b9fc3573743aa126001250). Source Schall et al., Nature Communications 17:10825, 22 Oct 2026, https://doi.org/10.1038/s41467-026-78386-z ; measured static optical spectra and calculated photon-shot-noise **LIMIT**, not an attained technical-noise sensor sensitivity. XH-S5 original ZIP inventory reports no repeated time-indexed simultaneous noise/covariance data in the supplied published archive; this is not an assertion about all possible external unpublished data. No native four-co-time Gaussian model was observed in actual Schall hardware.

M14 prior exact originals:
- https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m14/2026-11-11/iw_m14_rot039_common_mode_four_axis_sharp_gaussian_minimax_and_spatial_gauge_001.md
- https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m14/2026-11-11/iw_m14_rot041_group_size_static_field_graph_connectivity_and_sharp_gaussian_minimax_001.md
- XH-S5 source archive inventory: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s5/2026-11-10/iw_xh_s5_eks1_t1_schall_original_source_data_zip_complete_inventory_temporal_no_003.md

General host is classical Gauss–Markov / Aitken GLS with correlated observation covariance, e.g. https://www.cs.cornell.edu/courses/cs6210/2025fa/lec/2025-09-24.html and https://sta721-f24.github.io/website/resources/slides/06-GLS.html . The particular sharp tetrahedral covariance-uncertainty calculation is an elementary local special case; **no mathematical novelty** is asserted.

## 1. Frozen observation contract

Let A be the 4x3 tetrahedral row matrix ((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)); AᵀA=4I₃, Aᵀ1₄=0, AAᵀ=4I₄−1₄1₄ᵀ. With static unknown unrestricted field vector z∈R³, unrestricted real h_k for each predetermined co-time block k=1,...,m, observe

    Y_k = A z + h_k 1₄ + ε_k,    N=4m.

The ε_k are independent between groups and jointly Gaussian within each group with identical distribution N₄(0,σ² C), σ²>0, **one shared but unknown** real correlation matrix C=Cᵀ≥0, C_ii=1. All groups cost four elementary shots, equal cost per channel. Singular C allowed (also prove nonsingular approximation). The exact target is global squared Euclidean risk over all unrestricted z,h,C and over all measurable estimators including biased/nonlinear. No adaptive creation of timestamps, no nonstatic b(t), temporal cross-group correlation, independent per-orientation shot allocation, unknown axes/σ², real optical Poisson law or physical claims.

## 2. Upper bound, sharp scalar covariance diagnostic

Define the contrast estimator

    z_hat = (1/m) Σₖ (AᵀY_k/4).

Every h_k cancels. For every C it is unbiased, and

    Cov(z_hat) = σ² Aᵀ C A / (16m).

Using AAᵀ=4I−11ᵀ and tr C=4, its total risk is

    R(z_hat;C) = σ²/m × (1 − (1ᵀC1)/16).                (R2.1)

PSD implies s:=1ᵀC1≥0; by Cauchy-Schwarz plus diag C=1, s≤16. Therefore 0≤R≤σ²/m. The single scalar s, i.e. normalized four-channel sum variance, fully determines the **trace risk of this estimator for this exact design only**; it is not a general likelihood sufficient statistic, and component errors still depend on the full covariance. Independent C=I gives s=4 and R=3σ²/(4m)=3σ²/N. Perfect common C=11ᵀ gives s=16 and zero projected noise, an exact algebraic *negative control*, not hardware performance.

## 3. Global all-estimator minimax lower certificate

Set P=I₄−11ᵀ/4, and admissible C_*=(4/3)P. Its diagonals equal 1, off-diagonals −1/3, eigenvalues 4/3 with multiplicity three on contrast space and zero on common vector; C_* is PSD, with s=0. Hence the same contrast estimator has risk σ²/m at this particular legal C_*.

For a lower bound over **all estimators**, restrict the model to C=C_* and h_k=0. The raw Y_k can be reconstructed from w_k=AᵀY_k/4 and u_k=1ᵀY_k/4 by Y_k=A w_k +1u_k. Under C_* each u_k=0 a.s. and w_k=z+η_k, η_k independent N₃(0,(σ²/3)I₃). Thus the full raw data contain **exactly** an ordinary three-dimensional Gaussian location experiment with m replicates, no further z-information.

Give z an independent proper Gaussian prior N₃(0,τ² I₃). The posterior covariance is V_τ=(τ^(−2)+3m/σ²)^(−1)I₃. The integrated squared risk of *any estimator* is at least tr V_τ=3/(τ^(−2)+3m/σ²). Let τ→∞, giving minimax lower σ²/m. The upper estimator in §2 meets it for every C,z,h. Therefore

    inf_estimator sup_{z,h,C} E||estimate−z||² = σ²/m = 4σ²/N.   (R2.2)

This is *not merely a Cramér–Rao lower bound* and includes biased and nonlinear estimators for the stated fixed complete design. If only strictly positive definite C is admitted, equicorrelations ρ>−1/3 tend to C_*. Their common and contrast eigenspaces remain separate; contrast covariance tends to σ²/3 I₃ and the same diffuse-prior lower bound approaches σ²/m. Thus the supremum value is unchanged.

## 4. Exact legal negative controls and local verification

For C_ρ=(1−ρ)I₄+ρ11ᵀ, PSD iff −1/3≤ρ≤1. The contrast estimator has

    R(z_hat;C_ρ)=3σ²(1−ρ)/(4m).

| ρ | Total risk per group /σ² | Meaning |
|---|---:|---|
| 1 | 0 | perfectly common noise canceled |
| 1/2 | 3/8 | positively correlated, improved contrast |
| 0 | 3/4 | M14 independent noise baseline |
| −1/6 | 7/8 | negative correlation worsens contrast |
| −1/3 | 1 | sharp PSD worst-case |

Example m=100, N=400, σ²=1: independent 3/400=0.0075; robust 1/100=0.01, factor4/3. In all five examples every channel marginal variance is *identical*.

Actually executed **local** pure Python 3 standard library Fraction verifier 30 assertions PASS; exact Gram, block C_* PSD/eigenvalue conditions, five rational equicorrelations, covariance matrices, risk identity and N400 budget. Local source SHA256: 32bc03e93f8a019771e7cfc05e3ad74533fba94e04b12f66d5e47f3df6c639af; local printed results SHA256: 03517fe128d94f39b5ac5d3bf84b89f5553539e786aabb5770fc4701051245d1. These local files have not been uploaded byte-exact to GitHub. Shorter **source-equivalent** public 30-check stdlib script, Git blob afd78565bb28b89c6b69895127f6348c85bfd3bd, creator write+full readback PASS:
https://github.com/wmakiela-tech/Nash-iw-research/blob/2257f815b34d2e99370e85a74c77827d707ff513/research/m15/2026-11-12/verify_m15_rot002_tetrahedral_correlated_gaussian.py . Its hosted exact bytes were not independently rerun in this turn. The finite controls do not substitute for the analytical Bayes lower proof in §3.

## 5. What changes, what does not; reopen gate

**Changed:** conditional transfer from M14's r4 independent noise to unknown correlated equal-marginal co-time groups requires a robust risk **4σ²/N**, not **3σ²/N**. To calculate the trace risk of the specific contrast estimator once actual assumptions are verified, measuring the same-sample true-co-time four-channel sum covariance scalar s suffices alongside measured marginal σ². It is *not* enough merely to know all individual channel marginal variances.

**Unchanged:** M14 independent noise theorems, REC11 scoped math referee, LT8 theory/author revision, XH source firstness, NASH physics and other fronts; no actual Schall covariance or same-sample true-co-time experiment has been established. PSN limit is NOT achieved technical-noise sensitivity; no device fT gain and no physical claim. No BW ING, owner uptake, separate referee, CANON, or EXEC sign.

**Reopen iff:** a verified original same-sample co-time multi-orientation raw acquisition with explicit true-time grouping, per-shot noise variances and cross-channel covariance plus independent replicate evidence is provided. XH-S6 handles source inventory; this paper makes no new owner task. Status GITHUB_PENDING_BW_INGEST / NO_NOVELTY / NO_NASH_PHYSICAL_CLAIM / NO_CANON / NO_EXEC_SIGN.

Literature search 2026-11-12: public web searches used exact strings “generalized least squares covariance matrix Gauss Markov correlated errors NIST handbook”, “generalized least squares correlated observation errors theorem”, “Schall Lindner Rottstaedt Laser-enhanced quantum sensing boosts sensitivity and dynamic range 2026”; primary Nature original and Cornell/Duke class notes inspected. This is a bounded source-typed host check, NOT an exhaustive novelty search.