---
artifact_id: IW_PRF11_FOUNDATION_IDENTIFIABILITY_DECISION_MEMORY_REPORT_001_20261018
title: PRF11 — identifiability, target-relative reduction, decision risk and predictive memory
created_at: 2026-10-18
as_of: 2026-10-18
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_10 / PRF11
function: foundation-first theory comparison and prior-art subtraction
document_type: REPORT
task_id: IW_PRF11_ARTIFACT_RECOVERY_AND_RESULTS_ROUTING_001_20261018
exposure: PUBLIC
status: DRAFT
primary_location: GitHub canonical path of this report
content_sha256: NOT_AVAILABLE — connector write/readback identity by Git blob SHA
provenance: PRF11 rotations 4–7; public mathematical reconstructions
derived_from: [PRF11_ROTATION_4, PRF11_ROTATION_5, PRF11_ROTATION_6, PRF11_ROTATION_7]
supersedes: []
stale_if: Source-specific legal observation semantics or current LT/BW definitions change
acceptance_owner: PRF lineage; scientific integration only through appropriate owners
return_path: GitHub issue IW_PRF11_ARTIFACT_RECOVERY_AND_RESULTS_ROUTING_001_20261018
claim_ceiling: FOUNDATION / HOST_SUBTRACTION / NO_CANON / NO_EXEC / NO_NOVELTY_CLAIM
bw_ingestion: NOT_CONFIRMED
cross_surface_sync: GITHUB_PENDING_BW_INGEST
---

# PRF11 — Consolidated foundation return (rotations 4–7)

This is a **new synthesis**, not a byte-identical copy or proof of custody of the four predecessor rotation files. Source rotation 4 had a created-but-empty Drive document; rotations 5–7 existed as local Markdown files but GitHub publication was not verified at the time of consolidation. Do not label those originals as recovered or readback-verified.

## 1. Feasible behavior versus probability law versus one observation

Let Θ={a,b}, X={0,1}, P_a(X=1)=1/3 and P_b(X=1)=2/3. Both laws have support {0,1}, yet P_a != P_b. Thus equality of feasible supports does not imply equality of laws. The parameter is identifiable from the full probability law but no single outcome perfectly identifies it. Under an explicitly iid repeated-sampling protocol the empirical frequency distinguishes the two models asymptotically.

For set-valued behavior B(a)={0,1} and B(b)={1,2}, unequal behavior sets still overlap at observation 1, so unequal sets do not guarantee unique single-observation attribution. If the admitted observation object is the *full law*, then F(theta)=P_theta and B(theta)={P_theta}; do not silently replace that typed observation with its support.

## 2. Target-relative reduction

For θ=(u,v), full observation X=(u,v) and reduction R(X)=u, the target τ(θ)=u is exactly preserved although full parameter recovery is lost. Therefore loss of full-model information does not imply loss of information for a specified target. Preservation of one target is weaker than Blackwell equivalence for all decision problems.

## 3. Statistical identifiability versus finite-sample decision risk

Let u be equally likely 0 or 1. Conditional on u, Y and Z are independent binary reports, with P(Y=u|u)=0.6 and P(Z=u|u)=0.9. Observing only Y retains law-level identifiability of u but the optimal one-shot zero-one Bayes error is 0.4. Observing (Y,Z), optimal decision uses Z and the error is 0.1. Thus structural identifiability does not imply preservation of finite-sample decision quality. The reported risks depend on the declared prior, sampling protocol and loss.

## 4. Current observation versus intervention-conditioned predictive sufficiency

Let H~Bernoulli(1/2), Y_0=H, current visible X_1=0, action a∈{0,1}, and Y_2=H XOR a. A reduction retaining only X_1 loses the information in history Y_0: at fixed a, P(Y_2=1|X_1=0,do(a))=1/2, while conditioning on full history makes Y_2 deterministic.

For legal histories h,h' and policy class Π, predictive sufficiency of reduction R requires:
R(h)=R(h') => Law(Y_future|h,π)=Law(Y_future|h',π) for every π∈Π,
with legal domains, intervention semantics and conditioning specified. This is a criterion/definition, not a new theorem. Classical examples do not establish quantum process-tensor transfer.

## 5. Mature-theory absorption / nonmaps

- Willems-style behavioral systems and set-membership identification distinguish feasible trajectories and observations.
- Statistical identifiability, sufficient statistics and partial identification distinguish laws, estimands and realized data.
- Blackwell comparison concerns parameter-independent Markov randomization and decision order, not preservation of one estimand alone.
- Le Cam comparison is an experiment/risk approximation framework under declared assumptions.
- Controlled Markov aggregation, POMDP belief states and predictive-state representations address history-dependent prediction.
- Quantum comb/process tensor analogies require source-native instrument and intervention legality; classical counterexamples are not a quantum proof.

These distinctions are established foundations. **No novelty or project scientific adoption is claimed.**

## 6. Reusable check for actual NASH endpoints

Declare: (i) model and nuisance domain, (ii) legal observation/intervention channel, (iii) observation type (support, law, finite sample, history law), (iv) target τ, (v) loss/risk and sample budget if relevant, (vi) reduction map, (vii) precise preservation obligation and counterexample/kill test. Do not upgrade a G2/G3 identifiability statement to a G4 decision/robustness statement, or terminal-state equality to multitime process equivalence.

## 7. Scope and outstanding custody

The present report is a compact reproducible *mathematical synthesis* with finite models specified inline; it is not a complete literature-search record (no frozen query logs, database exports or checked bibliography), and not a claim that rotations 4–7 were separately committed. Original local Markdown files 5–7 remain separate source copies; no claim of BW ingestion, owner acceptance or cross-surface synchronization is made.

Project control: NASH/IW Cell Work, Artifact and Reproducibility Protocol (as of 2026-10-12); Storage and Cross-Surface Sync Policy (2026-10-12). Current LT source must be resolved via private BW/LT owner before source-specific promotion.
