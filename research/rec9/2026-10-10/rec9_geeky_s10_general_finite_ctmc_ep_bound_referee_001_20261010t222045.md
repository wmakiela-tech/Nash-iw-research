---
artifact_id: REC9-GEEKY-S10-GENERAL-FINITE-CTMC-EP-BOUND-REFEREE-001@20261010T222045
bw_ingestion_event_id: ING-20261010-0111
bw_qualification_state: T3_CTMC_REFEREE_LATE_VARIANT
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: REFEREE_NO_OWNER_AUTHORITY
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# REC9-GEEKY-S10-GENERAL-FINITE-CTMC-EP-BOUND-REFEREE-001@20261010T222045

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

REC9 / GEEKY-S10 GENERAL FINITE-CTMC EP BOUND REFEREE
RETURN_ID: REC9-GEEKY-S10-GENERAL-CTMC-TRAFFIC-AFFINITY-EP-BOUND-REFEREE-001
TARGET: GEEKY-S10-T3-GENERAL-CTMC-TRAFFIC-AFFINITY-EP-BOUND-001
VERDICT: PASS_WITH_SHARPNESS_AND_AFFINITY-SEMANTICS_REPAIR
SEVERITY: MEDIUM.
1. CORE ALGEBRA — PASS EXACT
For active bidirectional edge e, with stationary directional fluxes f+ and f-, traffic a=f++f-, and stationary-flux affinity xi=ln(f+/f-):
f+-f-=a tanh(xi/2),
so sigma_e=a xi tanh(xi/2)=a g(|xi|), g(x)=x tanh(x/2).
g is increasing for x>=0.
Hence sum_e a_e<=A and |xi_e|<=L imply
0<=sigma<=A L tanh(L/2).
The derivation is exact
2. SHARPNESS REPAIR — GLOBAL CLASS, NOT EACH TOPOLOGY
The homogeneous ring construction correctly attains A L tanh(L/2). Therefore the bound is sharp over the broad admissible class of finite stationary CTMCs when topology is allowed to include such cycles.
But the same constant need not be sharp for a fixed carrier topology or a narrower physical subclass.
Exact control: on a finite connected tree with bidirectional edges, stationarity plus Kirchhoff current conservation forces every stationary edge current to vanish; equivalently the stationary chain is reversible on that support. Hence sigma=0 although the generic A,L upper bound may be positive.
Safe wording:
BOUND_VALIDITY = TOPOLOGY-INDEPENDENT UNDER DECLARED EDGE GUARDS.
GLOBAL_CLASS_SHARPNESS = PASS WHEN CYCLIC RING SUBCLASS IS ADMISSIBLE.
FIXED_TOPOLOGY_SHARPNESS = NOT AUTOMATIC.
RING_RESULT_NOT_TOPOLOGY-SPECIFIC should mean the inequality generalizes beyond rings, not that its saturation is topology-independent.
3. AFFINITY SEMANTICS REPAIR
The theorem uses exactly the stationary-flux affinity
xi_e = ln[(pi_i k_ij)/(pi_j k_ji)].
A source-native bound on some other quantity is not automatically a bound on xi_e.
In particular, a bound on bare rate ratio ln(k_ij/k_ji), reservoir force, energy gap, or local-detailed-balance contribution must be transported through the stationary distribution/state-potential term before being used as L.
Therefore add:
AFFINITY_OBJECT = STATIONARY_FLUX_AFFINITY / RATE_RATIO / RESERVOIR_FORCE / OTHER.
AFFINITY_TRANSPORT_TO_XI = PASS / FAIL / UNRESOLVED.
Only a legal bound on the theorem's xi_e (directly or through a proved bridge) supports A L tanh(L/2).
4. IDENTIFIED-SET CEILING
If the hidden carrier class is literally the broad class of finite stationary CTMCs constrained only by total traffic<=A and max stationary-flux affinity<=L, then the ring family realizes the upper endpoint and equilibrium realizes the lower endpoint; continuous scaling gives the full interval [0, A L tanh(L/2)].
For a fixed physical topology, rate architecture, state count, conservation law, or other carrier restriction, the same expression is always a valid outer upper bound when the edge guards hold, but it need not be the exact identified interval or attainable endpoint.
Thus:
UNIVERSAL_OUTER_BOUND = PASS.
EXACT_IDENTIFIED_INTERVAL = requires class-admissibility/saturation certificate.
GLOBAL_CLASS_SHARPNESS != SOURCE-SPECIFIC_SHARPNESS.
5. NECESSITY CLAIM CEILING
The ring subfamily correctly proves:
traffic-only does not yield a universal finite EP upper bound over the broad finite-CTMC class;
affinity-only does not yield one either.
This is a class-level impossibility result, not a statement that both controls are minimally necessary inside every narrower carrier family. Extra topology, conservation, fixed rates, reversibility, or source constraints can make one or both redundant.
Safe:
BOTH_CONTROLS_JOINTLY_SUFFICIENT = PASS.
EACH_ALONE_UNIVERSALLY_INSUFFICIENT_OVER_BROAD_CLASS = PASS.
MINIMAL_FOR_EVERY_SOURCE_CLASS = NOT EARNED.
6. COMPONENTWISE VERSION
sigma <= sum_e A_e L_e tanh(L_e/2) is a valid edgewise upper bound under the declared componentwise ceilings. However arbitrary simultaneous saturation can be blocked by stationarity/Kirchhoff constraints and topology. Therefore treat it as SAFE UPPER BOUND unless a source-specific saturation construction is supplied; do not infer componentwise sharpness automatically.
7. SUPPORT / ZERO-FLUX TYPING
Apply xi_e only on active support edges with positive stationary directional fluxes. If one direction is positive and the reverse stationary flux is zero, the finite-L certificate fails. Edges with zero flux in both directions are inactive for sigma and should not be assigned an artificial finite affinity from 0/0.
8. ADDITIVE HIDDEN COMPONENT — PASS WITH CLASS GUARD
For a genuinely independent product hidden CTMC, entropy-production additivity is legal and the visible detector law is unchanged. The total-EP interval statement is therefore valid under that product/additivity contract. Interacting hidden-visible sectors require a new decomposition/target proof, as Geeky already states.
9. SOURCE/HOST CHECK
The edge-current/affinity entropy-production form is standard Schnakenberg stochastic thermodynamics. The graph-theoretic host also supports the tree control: absent directed cycles, a stationary finite bidirectional chain is reversible on its support, so stationary edge currents and entropy production vanish.
10. FINAL STATUS
GENERAL_CTMC_EDGE_FACTORIZATION=PASS_EXACT.
UNIVERSAL_A_L_BOUND=PASS_EXACT.
GLOBAL_CLASS_SHARPNESS=PASS WHEN RING SUBCLASS IS ADMISSIBLE.
FIXED_TOPOLOGY_OR_SOURCE_SHARPNESS=NOT AUTOMATIC.
AFFINITY_OBJECT_SEMANTICS=REPAIR REQUIRED.
COMPONENTWISE_BOUND=PASS_SAFE; GENERIC SHARPNESS NOT EARNED.
TRAFFIC_ONLY_AND_AFFINITY_ONLY_CLASS_LEVEL_NO_GO=PASS.
EXACT_SOURCE_IDENTIFIED_INTERVAL=REQUIRES SOURCE-CLASS SATURATION CERTIFICATE.
MATURE_HOST_ABSORPTION=YES.
NOVELTY_CANDIDATE=NONE.
REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD.
NO CANON / NO EXEC_SIGN / NO NEW TASK / NO NEW FRONT.
STOP CONDITION
Stop after integration of: global-class vs fixed-topology sharpness; stationary-flux-affinity typing/transport; and outer-bound vs exact source-specific identified-set distinction. Reopen only for a concrete physical A,L certificate, stronger topology-specific sharpness claim, or contradiction.
.
