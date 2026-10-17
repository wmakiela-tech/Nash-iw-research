---
artifact_id: IW_PRF11_HEAT_SMOOTHING_FOURIER_MOMENT_TO_TV_BRIDGE_REPORT_001_20261018
title: Common heat smoothing converts finite Fourier-moment matching into a quantitative TV bound
created_at: 2026-10-18
as_of: 2026-10-18
origin_cell: PRF11
document_type: REPORT
function: foundation-first theorem-family reconstruction and exact discriminator
task_id: NOT_APPLICABLE
exposure: PUBLIC
status: DRAFT
primary_location: GitHub research/prf11/2026-10-18
content_sha256: NOT_AVAILABLE (immutable commit and blob SHA after readback)
derived_from: [IW_PRF11_MOMENT_MATCHING_LE_CAM_DEFICIENCY_NONMAP_REPORT_001_20261018]
supersedes: []
stale_if: Observation noise is not common, theta-independent heat convolution or sample space is not the circle
acceptance_owner: PRF / appropriate scientific owner
return_path: GitHub artifact
claim_ceiling: MATURE_FOURIER_ANALYSIS / EXACT_CONTROL / NO_CANON / NO_EXEC / NO_NOVELTY_CLAIM
cross_surface_sync: GITHUB_PENDING_BW_INGEST
---

# PRF11 rotation 9 — a conditional moment-to-law bridge

## Foundation and precise question

Rotation 8 established that matching arbitrarily many *finite* Fourier coefficients does not control total variation for raw measures on the circle. The next source-native question is whether a **specified legal common observation kernel** can supply the missing strong-metric bound.

This report treats one exact mature example: circular heat smoothing. It is not a new general theory, and no physical NASH endpoint has been shown to obey the assumptions.

## Statement

Let P,Q be Borel probability measures on the circle T=R/(2πZ). Define Fourier coefficients p̂(k)=∫exp(-ikx)dP(x), q̂(k)=∫exp(-ikx)dQ(x). Assume p̂(k)=q̂(k) for every integer |k|≤m, where m≥0.

Let H_t be the circular heat probability kernel with Fourier multiplier exp(-t k²), t>0. Then

TV(P*H_t,Q*H_t) ≤ Σ_{k=m+1}^∞ exp(-t k²).

TV is normalized as sup over measurable sets of the absolute probability difference (half of the L1 density difference).

## Proof

Both convolutions have continuous densities with uniformly absolutely convergent Fourier series. The difference density is

f_t(x)=(1/(2π)) Σ_{k∈Z} exp(-t k²) (p̂(k)-q̂(k)) exp(ikx).

By moment matching, the summands vanish for |k|≤m. For probability measures, |p̂(k)-q̂(k)|≤2. Therefore

|f_t(x)| ≤ (1/(2π)) · 2 · Σ_{|k|>m} exp(-t k²)
         = (2/π) Σ_{k=m+1}^∞ exp(-t k²).

Consequently

TV(P*H_t,Q*H_t)
= (1/2) ∫_0^{2π}|f_t(x)|dx
≤ (1/2)·2π·(2/π) Σ_{k=m+1}^∞ exp(-t k²)
= 2 Σ_{k=m+1}^∞ exp(-t k²).

**Correct constant is 2**, not 1, under this elementary triangle-inequality proof. A sharper bound might be available by different arguments; none is claimed here. The safe bound used in this report is:

TV(P*H_t,Q*H_t) ≤ min{1, 2 Σ_{k=m+1}^∞ exp(-t k²)}.

The Gaussian tail vanishes as m→∞ for fixed t>0.

## Uniform experiment-level implication

Suppose Θ is any parameter set and families {P_θ}, {Q_θ} satisfy the same coefficient-matching condition through m for all θ, with the same H_t. Define smoothed experiments E_t={P_θ*H_t}, F_t={Q_θ*H_t} on the same circle observation space. The identity kernel gives

Δ(E_t,F_t) ≤ sup_θ TV(P_θ*H_t,Q_θ*H_t)
          ≤ min{1, 2 Σ_{k=m+1}^∞ exp(-t k²)}

for the max-of-one-sided-deficiencies convention.

This is a sufficient experiment comparison bound for **smoothed** experiments. It does not imply the corresponding unsmoothed experiments are close. Heat convolution can destroy discrimination.

## Approximate low-frequency matching

If sup_θ |p̂_θ(k)-q̂_θ(k)|≤ε_k for |k|≤m, then by the same Fourier series argument,

TV(P_θ*H_t,Q_θ*H_t) ≤ (1/2)Σ_{|k|≤m}exp(-t k²) ε_k + 2Σ_{k=m+1}∞exp(-t k²),

capped at 1. This separates controlled low-frequency mismatch from the smoothing-suppressed high-frequency tail.

## Kill conditions / nonmaps

1. The kernel must be common and parameter-independent; theta-dependent readout does not establish the same Blackwell/Le Cam relation.
2. Exact Fourier moments and the circle geometry are essential to this statement. Generic finite moments or arbitrary observation spaces require another approximation theorem.
3. t>0 is essential for the tail decay. As t↓0 the uniform bound becomes useless, matching the rotation-8 obstruction.
4. This is a claim about observation laws, not equality of hidden processes, legal interventions or full multitime process tensors.
5. The noise channel is itself information-losing. A good approximation of noisy experiments is not a guarantee of preserving the original noiseless decision power.

## Source/prior-art scope

This is standard Fourier harmonic analysis and the classical heat semigroup, combined with the elementary identity-kernel upper bound for Le Cam deficiency already recognized in PRF10. No live literature search or novelty claim was performed. A project-specific scientific residual would require proving that a native instrument has this common smoothing property and supplies uniform moment bounds.

## Reproduction

For m≥0 and t>0, compute the positive Gaussian tail T(m,t)=2Σ_{k=m+1}∞exp(-t k²). Verify by geometric/Fourier-series orthogonality and triangle inequality. Expected inequality TV≤min(1,T(m,t)). For the approximate case, add the weighted finite-coefficient error term. Reproduction type: analytic derivation, not an empirical run.

Status: GITHUB_PENDING_BW_INGEST / NO_CANON / NO_EXEC / NO_NOVELTY_CLAIM.
