---
artifact_id: IW_PRF11_MOMENT_MATCHING_LE_CAM_DEFICIENCY_NONMAP_REPORT_001_20261018
title: Moment matching does not control Le Cam deficiency
created_at: 2026-10-18
as_of: 2026-10-18
origin_cell: PRF11
document_type: REPORT
function: foundation-first theory and exact counterexample
task_id: NOT_APPLICABLE
exposure: PUBLIC
status: DRAFT
primary_location: GitHub canonical path
content_sha256: NOT_AVAILABLE (Git blob SHA and readback recorded separately)
derived_from: [IW_PRF11_FOUNDATION_IDENTIFIABILITY_DECISION_MEMORY_REPORT_001_20261018]
supersedes: []
stale_if: A source-specific restriction changes the admitted law family or metric
acceptance_owner: PRF / appropriate scientific owner
return_path: GitHub canonical file
claim_ceiling: FOUNDATION / NEGATIVE_KNOWLEDGE / NO_CANON / NO_EXEC / NO_NOVELTY_CLAIM
cross_surface_sync: GITHUB_PENDING_BW_INGEST
---

# PRF11 rotation 8 — moment matching vs statistical-experiment comparison

## Foundation and question coevolution

PRF10's Blackwell–Willems deep foundation already establishes the mature implication: a uniform total-variation bound between parameterized observation-law families bounds Le Cam deficiency (via identity or another common Markov kernel). The remaining source-native question is the *first arrow*: does a given reduced process approximation imply a sufficiently strong **uniform law-level** bound?

This rotation supplies a precise obstruction to replacing that first arrow with a finite list of matched moments. It does not claim a new result or new general bridge.

## Exact Fourier-moment counterexample

Let the observation space be the unit circle S¹ with its Borel sigma-algebra. Let P be normalized Haar (continuous uniform) probability measure and let Q_n be uniform probability on the n roots of unity (n>=2).

For k=1,...,n-1, E_P[Z^k]=0=E_Qn[Z^k]. The same holds for negative integer k with 0<|k|<n, and k=0 equals 1 for both. Proof: Haar orthogonality and the geometric sum (1/n)Σ_{j=0}^{n-1} exp(2π i kj/n)=0 whenever n does not divide k.

Nevertheless TV(P,Q_n)=sup_A |P(A)-Q_n(A)|=1, taking A as the n-point support of Q_n. Hence no universal bound TV(P,Q)≤f(m) with f(m)<1 follows solely from matching the first m Fourier moments, even for arbitrarily large finite m.

Note: weak convergence Q_n⇒P as n→∞ is compatible with TV(P,Q_n)=1 for every n. This separates weak/finite-test-function convergence from TV convergence.

## Exact experiment-level obstruction

Fix parameter set Θ={0,1}. Define a source experiment E with P_0=P (Haar) and P_1=Q_n (roots). Define a compressed experiment F with R_0=R_1=P.

For each θ, the first n-1 nontrivial Fourier moments of P_θ and R_θ match exactly. Yet F carries no information about θ. For any θ-independent Markov kernel K mapping F observations to E observations, K R_0 = K R_1 = M. Triangle inequality yields
TV(P_0,P_1) ≤ TV(P_0,M)+TV(M,P_1) ≤ 2 max_θ TV(P_θ,K R_θ).
Therefore the one-sided deficiency δ(F,E)≥1/2 (TV normalization sup_A). Equality is attained by a kernel ignoring its input and outputting M=(P_0+P_1)/2, so δ(F,E)=1/2.

In the opposite direction δ(E,F)=0: simply ignore the E observation and output Haar P. Thus the symmetric Le Cam distance Δ(E,F)=1/2 under the max-of-deficiencies convention.

For equal prior and zero-one loss on θ, E perfectly discriminates the two parameters from one observation because the laws are mutually singular, whereas F's optimal error is 1/2. This gives an operational witness to the deficiency gap.

## Boundary and prior-art subtraction

- This is a standard finite-moment versus strong-probability-metric obstruction, not a novel NASH theorem.
- The construction changes discrete/continuous measure class. It does not prove an analogous lower bound for a source-native model restricted to smooth strictly positive densities, fixed finite-dimensional exponential families, or controlled diffusion laws.
- Moment convergence can imply weak convergence under appropriate compactness/determinacy hypotheses; it still does not generally imply TV convergence.
- Even TV closeness is a sufficient rather than universally necessary condition for small deficiency: an appropriate θ-independent randomization can give deficiency zero across different sample spaces.
- A source-specific bridge would need additional regularity, domination, noise smoothing, mixing, quantitative inversion or a direct randomization/risk bound. None is supplied here.

## Exact source relations

Foundation source: PRF10, *Blackwell–Willems deep foundation: stochastic behavior → statistical experiment → decision*, 2026-10-11, private project source. Mature host families: Blackwell comparison, Le Cam deficiency, Fourier analysis on compact groups, weak versus TV convergence. No new external literature search was performed in this rotation; this is an exact self-contained control, **not** a reproducible literature sweep.

## Reproduction instructions

For any n≥2: define P as normalized Lebesgue/Haar measure on [0,2π) and Q_n=(1/n)Σδ_{2πj/n}; compute Fourier coefficients for integer |k|<n by the geometric-series identity; take A={2πj/n} to witness TV=1. For the experiment-level bound, use the triangle inequality and the constant output kernel M=(P+Q_n)/2. Expected outputs: moment differences 0; TV=1; δ(F,E)=1/2; δ(E,F)=0.

## NASH scope

Before upgrading matched trajectories, observables, spectra or finitely many moments to experiment equivalence, demand a source-native theorem controlling the full parameter-indexed law family or a direct admissible decision-risk bound. In particular, do not infer G4 risk preservation from G2/G3 identifiability alone.

State: GITHUB_PENDING_BW_INGEST / NO_CANON / NO_EXEC / NO_NOVELTY_CLAIM.
