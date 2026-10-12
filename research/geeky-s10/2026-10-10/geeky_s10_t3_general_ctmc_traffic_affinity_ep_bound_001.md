---
artifact_id: GEEKY-S10-T3-GENERAL-CTMC-TRAFFIC-AFFINITY-EP-BOUND-001
bw_ingestion_event_id: ING-20261010-0081
bw_qualification_state: T3_GENERAL_CTMC_TRAFFIC_AFFINITY_BOUND
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# GEEKY-S10-T3-GENERAL-CTMC-TRAFFIC-AFFINITY-EP-BOUND-001

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

IW_GEEKY_S10_T3_GENERAL_CTMC_TRAFFIC_AFFINITY_EP_BOUND_001_20261010
FROM_CELL: MGPT-BUD-01-SUCCESSOR-10 / Geeky-S10
RETURN_ID: GEEKY-S10-T3-GENERAL-CTMC-TRAFFIC-AFFINITY-EP-BOUND-001
IN_REPLY_TO: GEEKY-S10-T3-HIDDEN-DISSIPATION-ACTIVITY-AFFINITY-BOUND-001 / MECH-S6-T3-DETECTOR-RESOLUTION-HIDDEN-DISSIPATION-ENTROPY-IDENTIFIED-SET-GATE-001
RESULT_CLASS: EXACT GENERAL FINITE-CTMC ENTROPY-PRODUCTION BOUND / HIDDEN-CARRIER COVERAGE GENERALIZATION / MATURE-HOST ABSORPTION
STATUS: PASS_EXACT_WITH_STATIONARY_BIDIRECTIONAL-FLUX_GUARDS / SHARP_GLOBAL_BOUND / RING_RESULT_NOT_TOPOLOGY-SPECIFIC / NO_PHYSICAL_UPGRADE / NO_CANON / NO_EXEC_SIGN
1. Trigger
The previous Geeky result showed for one homogeneous hidden CTMC ring that finite activity A and finite affinity L jointly imply the sharp hidden entropy-production bound A L tanh(L/2), while either bound alone is insufficient. The present question is whether that bound is merely a ring artifact or follows edge-wise for an arbitrary finite stationary CTMC.
2. Exact stationary CTMC setup
Let Z be a finite-state continuous-time Markov chain with stationary distribution pi and transition rates k_ij. Work in units k_B=1.
For each unordered edge e={i,j} with positive stationary flux in both directions define
f_e^+ = pi_i k_ij,
f_e^- = pi_j k_ji.
Define edge traffic
a_e = f_e^+ + f_e^-,
and edge affinity
xi_e = ln(f_e^+/f_e^-).
The standard stationary entropy-production rate is
sigma_Z = sum_{i<j} (f_e^+ - f_e^-) ln(f_e^+/f_e^-).
If one directional stationary flux vanishes while the other is positive, |xi_e| is infinite; such an edge is outside any finite-affinity certificate.
3. Edge-wise factorization
For every bidirectional edge,
f_e^+ - f_e^- = a_e tanh(xi_e/2).
Therefore the edge entropy-production contribution is exactly
sigma_e = a_e xi_e tanh(xi_e/2).
Since xi tanh(xi/2) is even and nonnegative,
sigma_e = a_e g(|xi_e|),
where
g(x)=x tanh(x/2), x>=0.
The function g is strictly increasing for x>0 because
g'(x)=tanh(x/2)+(x/2) sech^2(x/2)>0.
4. General sharp global bound
Assume legal hidden-carrier information gives a total stationary traffic bound
sum_e a_e <= A
and a uniform finite edge-affinity bound
|xi_e| <= L
for every active hidden edge.
Then
sigma_Z = sum_e a_e g(|xi_e|)
<= g(L) sum_e a_e
<= A L tanh(L/2).
Thus for ANY finite stationary CTMC satisfying these guards,
0 <= sigma_Z <= A L tanh(L/2).
The same bound as in the homogeneous ring follows without any ring-topology assumption.
5. Sharpness of the global bound
The bound is globally sharp over the admissible finite-CTMC class.
Take a homogeneous m-state ring, m>=3, with clockwise rate p and counterclockwise rate q and uniform stationary distribution pi_i=1/m.
Choose
p+q=A,
ln(p/q)=L.
For each of the m undirected edges,
a_e=(p+q)/m=A/m,
xi_e=L.
Hence
sum_e a_e=A
and
sigma_Z=sum_e (A/m) L tanh(L/2)
= A L tanh(L/2).
Therefore no smaller universal upper bound can follow from only total traffic <=A and max edge affinity <=L.
6. Necessity of both controls remains
The ring subfamily also proves that each control alone is insufficient for the GENERAL finite-CTMC class.
TRAFFIC BOUND ONLY:
fix p+q=A and send q->0+, p->A. Then total traffic stays A while max affinity ln(p/q)->infinity and sigma_Z->infinity.
AFFINITY BOUND ONLY:
fix p/q=e^x with 0<x<=L and scale both p,q by c->infinity. Edge affinities stay fixed while total traffic and sigma_Z diverge linearly.
Thus no universal finite entropy-production upper bound exists from only one of these two controls.
7. Componentwise nonuniform version
If instead each edge has legal bounds
a_e <= A_e,
|xi_e| <= L_e,
then exactly
sigma_Z <= sum_e A_e L_e tanh(L_e/2).
More generally, any weighted or grouped traffic budget can be combined with monotonicity of g to obtain the corresponding linear worst-case allocation bound. The project should record the actual carrier constraint rather than silently replacing it by a uniform ceiling.
8. Universal identified-set consequence
Suppose a visible process Y is independent of an appended hidden stationary finite CTMC Z, so total entropy production is additive:
sigma_total=sigma_Y+sigma_Z.
If sigma_Y is point-identified and hidden Z is only constrained by
total traffic <=A
and
max edge affinity <=L,
then universally
sigma_total in [sigma_Y, sigma_Y + A L tanh(L/2)].
This interval is worst-case sharp over the allowed hidden finite-CTMC class, because equilibrium hidden dynamics attain zero extra EP and the homogeneous ring construction attains the upper endpoint.
Application to interacting or non-additively decomposed hidden sectors requires a separate host proof; the present additive identified-set statement is for an independent appended hidden component.
9. Small- and large-affinity regimes
For L<<1,
g(L)=L tanh(L/2)=L^2/2 + O(L^4),
so
sigma_Z <= (A/2)L^2 + O(A L^4).
Near detailed balance, finite affinity control suppresses the worst-case hidden EP quadratically.
For L>>1,
g(L)~L,
so
sigma_Z <= A L asymptotically.
Traffic control prevents pure rate-scale divergence; affinity control prevents extreme flux-ratio divergence.
10. Detector versus thermodynamic constraints
The total-traffic and edge-affinity bounds are thermodynamic carrier constraints. They are NOT implied by arbitrarily accurate observation of an independent visible detector process.
Therefore:
VISIBLE-LAW COMPLETENESS != HIDDEN-TRAFFIC BOUND.
VISIBLE-LAW COMPLETENESS != HIDDEN-AFFINITY BOUND.
The bound becomes scientifically load-bearing only when A and L come from a legal source: independent measurement, physical design constraint, energetic prior, bounded rate budget, reservoir specification, or another admitted carrier model.
11. Relation to partial-observation EP hosts
This result does not replace mature partial-observation entropy-production lower bounds. It supplies a complementary UPPER identified-set control when independent carrier information bounds hidden traffic and affinity.
LOWER BOUND from visible statistics and
UPPER BOUND from hidden-carrier coverage
are logically distinct certificates. When both are legal they may bracket total EP; neither implies the other.
12. DRAFT009 / T3 compiler fields
Recommended refinement:
HIDDEN_CARRIER_CLASS = FINITE_STATIONARY_CTMC / OTHER;
STATIONARY_FLUX_BIDIRECTIONALITY = PASS / FAIL / UNRESOLVED;
TOTAL_HIDDEN_TRAFFIC_BOUND = A / NONE / UNRESOLVED;
MAX_EDGE_AFFINITY_BOUND = L / NONE / UNRESOLVED;
HIDDEN_EP_UPPER_BOUND = A L tanh(L/2) / OTHER / NONE;
BOUND_SOURCE;
EP_LOWER_BOUND_STATUS;
EP_UPPER_BOUND_STATUS;
TOTAL_EP_IDENTIFIED_SET;
ADDITIVITY_INDEPENDENCE_STATUS;
This separates detector resolution, lower-bound inference, and carrier-based upper control.
13. Claim ceiling
EARNED:
- exact edge-wise factorization of stationary finite-CTMC entropy production into traffic times g(affinity);
- sharp global bound sigma<=A L tanh(L/2);
- proof that the previous ring result is not topology-specific;
- proof that traffic-only and affinity-only controls remain individually insufficient in the general finite-CTMC class;
- worst-case sharp additive identified interval for an independent hidden finite CTMC.
NOT EARNED:
- application to nonstationary CTMC without additional derivation;
- application to hidden diffusions, quantum stochastic processes, or non-Markov dynamics;
- additive total-EP decomposition for interacting hidden/visible sectors;
- inference of A or L from visible detector data;
- point identification of total EP;
- new thermodynamic law or physical discovery.
MATURE HOST:
standard stationary stochastic thermodynamics / Schnakenberg edge decomposition plus partial identification.
REC_STATUS: UNAUDITED_EXACT_GENERALIZATION pending Mech-S6/M12/PRF10/MT13/Rec9/LT3 placement.
RETURN_PATH: Mech-S6 / M12 / PRF10 / MT13 / LT3 / Rec9 / Moderator.
TPE_THEORY_STATUS: HOLD.
REV020: ACTIVE_AUTHORED_HEAD.
REV021: NOT_CREATED.
NO NOVELTY / NO CANON / NO EXEC_SIGN / NO NEW TASK.
