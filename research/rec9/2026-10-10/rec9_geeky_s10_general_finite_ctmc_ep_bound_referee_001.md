---
artifact_id: REC9-GEEKY-S10-GENERAL-FINITE-CTMC-EP-BOUND-REFEREE-001
bw_ingestion_event_id: ING-20261010-0082
bw_qualification_state: T3_GENERAL_CTMC_EP_REFEREE
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: REFEREE_NO_OWNER_AUTHORITY
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# REC9-GEEKY-S10-GENERAL-FINITE-CTMC-EP-BOUND-REFEREE-001

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

REC9 / GEEKY-S10 GENERAL FINITE-CTMC EP BOUND REFEREE
RETURN_ID: REC9-GEEKY-S10-GENERAL-FINITE-CTMC-EP-BOUND-REFEREE-001
TARGET: GEEKY-S10-T3-GENERAL-CTMC-TRAFFIC-AFFINITY-EP-BOUND-001
VERDICT: PASS_WITH_FORCE-SEMANTICS_AND-SHARPNESS-SCOPE_REPAIR
SEVERITY: LOW/MEDIUM.
1. EXACT MATHEMATICAL CORE — PASS
For bidirectional stationary edge fluxes f+=pi_i k_ij and f-=pi_j k_ji, with a=f++f- and xi=ln(f+/f-):
f+-f-=a tanh(xi/2), hence sigma_e=a xi tanh(xi/2)=a g(|xi|).
g(x)=x tanh(x/2) is increasing for x>=0.
Therefore sum_e a_e<=A and max_e |xi_e|<=L imply sigma<=A L tanh(L/2).
The homogeneous m-ring attains equality, so the bound is sharp over the unrestricted finite stationary CTMC class containing that subfamily
2. REPAIR A — AFFINITY SEMANTICS MUST MATCH THE PROOF
The bound uses exactly the stationary edge force
xi_e = ln[(pi_i k_ij)/(pi_j k_ji)].
Do not substitute a bound on the bare rate ratio ln(k_ij/k_ji), reservoir driving, energy gap, or cycle affinity unless a separate legal implication to |xi_e|<=L is proved.
The stationary probability ratio pi_i/pi_j is part of xi_e.
Therefore BOUND_SOURCE must record which quantity is actually bounded and the transport theorem/calculation to the stationary flux-ratio force.
Likewise A is a bound on stationary expected jump traffic sum_e(pi_i k_ij+pi_j k_ji), not automatically on an unweighted sum of raw rates.
Safe fields:
AFFINITY_OBJECT = STATIONARY_FLUX_RATIO / RATE_RATIO / CYCLE_AFFINITY / OTHER.
AFFINITY_TO_EDGE_FORCE_TRANSPORT = PASS / FAIL / UNRESOLVED / NA.
TRAFFIC_OBJECT = STATIONARY_EDGE_TRAFFIC / RAW_RATE_BUDGET / OTHER.
TRAFFIC_TO_STATIONARY_BOUND = PASS / FAIL / UNRESOLVED / NA.
3. REPAIR B — SHARPNESS IS CLASS-GLOBAL, NOT PER TOPOLOGY
The ring witness proves that no smaller universal bound follows from only A and L over the broad finite-CTMC class. It does NOT show the bound is tight for every fixed state graph, cardinality, or additional conservation structure.
Exact counter-control: for a connected bidirectional TREE at stationarity, divergence-free edge currents must vanish. A leaf has only one incident current, hence it is zero; remove the leaf and iterate. Thus every edge current is zero and sigma=0.
So:
TOPOLOGY-INDEPENDENT VALIDITY = PASS.
CLASS-GLOBAL SHARPNESS = PASS.
FIXED-TOPOLOGY SHARPNESS = NOT IMPLIED.
RING_RESULT_NOT_TOPOLOGY-SPECIFIC should mean the inequality applies beyond rings, not that every topology can saturate it.
If topology is legally known, use the strongest topology-specific certificate rather than automatically reporting the class-global envelope.
4. ACTIVE-EDGE / MICROREVERSIBILITY TYPING
For a_e=0 both stationary directional fluxes vanish and xi_e is undefined but irrelevant; exclude such zero-traffic edges from the max-affinity domain.
If one directional stationary flux is positive and the reverse is zero, the Schnakenberg flux-ratio force diverges and the finite-L certificate fails. This is consistent with the mature host's usual bidirectional/microreversible setting; unidirectional-transition thermodynamics needs separate treatment.
5. ADDITIVE HIDDEN-SECTOR REPAIR
The interval sigma_total=sigma_Y+sigma_Z is legal when the hidden sector is an appended dynamically decoupled/product component or when an additive EP decomposition is separately proved.
Marginal statistical independence at one time is not enough by itself to establish entropy-production additivity; shared reservoirs, coupled transition bookkeeping, or interaction currents can spoil the split.
Safe field:
EP_DECOMPOSITION_STATUS = PRODUCT_GENERATOR / PROVED_ADDITIVE / INTERACTING / UNRESOLVED.
Only the first two license direct interval addition.
6. IDENTIFIED-SET WORDING
Over the broad allowed class containing homogeneous rings, the full interval [0, A L tanh(L/2)] is attainable continuously by taking ring traffic A and varying |xi| from 0 to L. Hence the additive interval can be exact for that broad class.
For a fixed carrier topology or stronger structural restrictions it is generally only an outer envelope until attainability is rechecked. Record CLASS_SCOPE_FOR_SHARPNESS.
7. MATURE-HOST CHECK
Current stochastic-thermodynamics literature continues to formulate stationary Markov-jump entropy production through edge currents/forces and Schnakenberg network decomposition. The result here is an elementary consequence of that mature host plus a worst-case allocation argument, not a new thermodynamic principle.
FINAL STATUS
EDGE_FACTORIZATION=PASS_EXACT.
GENERAL_BOUND=PASS_EXACT.
TRAFFIC_ONLY_INSUFFICIENT=PASS.
AFFINITY_ONLY_INSUFFICIENT=PASS.
CLASS_GLOBAL_SHARPNESS=PASS.
FIXED_TOPOLOGY_SHARPNESS=NOT_IMPLIED.
AFFINITY_OBJECT_SEMANTICS=REPAIR_REQUIRED.
TRAFFIC_OBJECT_SEMANTICS=REPAIR_REQUIRED.
ADDITIVE_TOTAL_EP=PASS_ONLY_WITH_PRODUCT/PROVED_DECOMPOSITION.
MATURE_HOST_ABSORPTION=YES.
NOVELTY_CANDIDATE=NONE.
REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD.
NO CANON / NO EXEC_SIGN / NO NEW TASK / NO NEW FRONT.
STOP CONDITION
Stop this object after Geeky/LT3 record stationary-force semantics, class-vs-topology sharpness, and product/additivity typing. Reopen only for a source-native physical A,L certificate, a fixed-topology stronger bound, a nonstationary/non-Markov extension, or a promotion claim.
.
