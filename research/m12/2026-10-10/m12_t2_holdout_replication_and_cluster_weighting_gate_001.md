---
artifact_id: M12-T2-HOLDOUT-REPLICATION-AND-CLUSTER-WEIGHTING-GATE-001
bw_ingestion_event_id: ING-20261010-0074
bw_qualification_state: T2_HOLDOUT_REPLICATION_CLUSTER_WEIGHTING
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE_PROTOCOL_REPAIR
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# M12-T2-HOLDOUT-REPLICATION-AND-CLUSTER-WEIGHTING-GATE-001

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

M12 - T2 holdout replication and cluster-weighting gate
RESULT_CLASS
EXACT PROTOCOL CONTROL / T2 BENCHMARK COMPOSITION / UNIT-OF-ANALYSIS GATE / NO HOLDOUT EXECUTION / NO NOVELTY CLAIM
TRIGGER
T2 now has:
- correctness-first paired evaluation;
- full frozen denominator;
- separate coverage/abstention/failure states;
- resource-vector cost semantics.
One remaining protocol risk is benchmark composition:
duplicating or oversampling one case family can change the aggregate verdict without adding a new scientific distinction.
SETUP
Let frozen cases i=1,...,N have paired correctness differences:
D_i = C_i - B_i in {-1,0,1}.
Unweighted paired full-set effect:
Delta = (1/N) sum_i D_i.
CERTIFICATE A - REPLICATION SENSITIVITY
Replicate case j exactly k additional times while keeping all outputs identical to the original case.
New effect:
Delta'
=
(sum_i D_i + k D_j)/(N+k).
Unless D_j equals the original mean Delta, replication changes the aggregate effect.
Thus exact duplicate rows can move the verdict even though no new scientific case type was added.
BOXED
ROW COUNT
!=
SCIENTIFIC COVERAGE.
CERTIFICATE B - SIGN FLIP BY DUPLICATION
Take three unique cases with paired differences:
D_1=+1,
D_2=-1,
D_3=-1.
Original:
Delta=(-1)/3 < 0.
Duplicate case 1 three additional times.
New dataset has:
four copies of +1,
one -1,
one -1.
Then:
Delta'=(4-2)/6=+1/3 > 0.
The benchmark winner flips from baseline to compiler purely by replicating one already-seen case.
Therefore:
UNWEIGHTED CASE-AVERAGE WIN
CAN BE A BENCHMARK-COMPOSITION ARTIFACT.
CERTIFICATE C - UNIQUE-UNIT WEIGHTING
Suppose cases belong to predeclared scientific units/groups g=1,...,G.
Let group g contain n_g rows and let:
Delta_g
=
(1/n_g) sum_{i in g} D_i.
If scientific intent is equal weight per group, use:
Delta_group
=
(1/G) sum_g Delta_g.
Exact duplication within a group leaves Delta_group unchanged when duplicated rows have the same group-level outcome average.
Thus group weighting can make evaluation invariant to arbitrary within-group replication.
CERTIFICATE D - WEIGHTS DEFINE THE ESTIMAND
More generally, with nonnegative frozen weights w_i:
Delta_w
=
sum_i w_i D_i / sum_i w_i.
Changing weights changes the scientific target distribution being estimated.
Therefore:
WEIGHTING RULE
IS PART OF THE CLAIM,
NOT A POST-HOC PRESENTATION CHOICE.
Examples of legal estimands:
- equal row weight;
- equal task-family weight;
- deployment-frequency weight;
- inverse-probability weight from a frozen sampling design.
No single weighting is universally correct.
CERTIFICATE E - POST-HOC REWEIGHTING CAN FLIP VERDICT
If there exist at least two cases/groups with opposite signs of D, then suitable positive weights can make Delta_w positive or negative.
Therefore:
RESOURCE/QUALITY TRADEOFFS ACROSS CASE FAMILIES
REQUIRE A PREDECLARED TARGET DISTRIBUTION OR WEIGHTING RULE.
Post-hoc weights can manufacture a win.
CERTIFICATE F - DUPLICATES DO NOT ADD INDEPENDENT EVIDENCE
Exact duplicated cases are perfectly dependent.
Treating k copies as k independent observations understates uncertainty.
Thus:
REPLICATED ROWS
!=
k NEW INDEPENDENT TESTS.
When cases are clustered by common template/source/family, uncertainty should respect that dependence structure.
CERTIFICATE G - CLUSTERED PAIRING
Let g index predeclared clusters and define cluster contribution:
S_g
=
sum_{i in g} w_i D_i.
The total paired effect is:
Delta_w
=
sum_g S_g / sum_i w_i.
If within-cluster outcomes are dependent, uncertainty should be based on cluster-level independent units or another declared dependence model.
The scientific unit and statistical independence unit need not be the row.
CERTIFICATE H - HOLDOUT HASH IS NECESSARY BUT NOT SUFFICIENT
A frozen CASE_SET_HASH prevents after-the-fact row edits.
It does not by itself certify:
- no near-duplicates;
- scientifically balanced coverage;
- correct family weights;
- independent evidence.
Therefore T2 should freeze both:
1. the literal row set;
2. the unit/cluster/weight semantics.
CERTIFICATE I - DEPLOYMENT DISTRIBUTION VERSION
If T2 claims deployment-average correctness, let pi_g be the prospectively declared deployment probability of family g.
Then:
Delta_deploy
=
sum_g pi_g Delta_g.
Equal-row average estimates this only when benchmark sampling frequencies match pi_g or are reweighted correctly.
Thus:
BENCHMARK AVERAGE
!=
DEPLOYMENT AVERAGE
without a sampling/weighting link.
CERTIFICATE J - RELATION TO PAIRED CORRECTNESS GATE
The prior paired theorem remains valid at any frozen weighting level:
Delta_w
=
sum_i w_i(C_i-B_i)/sum_i w_i.
This preserves within-case pairing.
The present gate adds a different question:
WHAT SCIENTIFIC POPULATION DO THE CASE WEIGHTS REPRESENT?
The two controls are orthogonal.
PROTOCOL FIELDS
CASE_SET_HASH
CASE_COUNT
SCIENTIFIC_UNIT_ID
CLUSTER_ID
DUPLICATE_OR_NEAR_DUPLICATE_POLICY
SAMPLING_DESIGN
TARGET_POPULATION
WEIGHTING_RULE
WEIGHTS_FROZEN_BEFORE_OUTCOMES
GROUP_COUNTS
PRIMARY_EFFECT=WEIGHTED_PAIRED_FULL_SET_CORRECT_YIELD
UNCERTAINTY_DEPENDENCE_MODEL
CLUSTER_ROBUST_OR_GROUP_LEVEL_METHOD_IF_USED
DEPLOYMENT_REWEIGHTING_RULE_IF_CLAIMED
CHEAP FALSIFIER
Ask:
Can duplicating an already-existing case family change the reported winner?
If YES under the intended scientific estimand:
the benchmark aggregation is not replication-robust.
Ask:
Were group/cluster/weight semantics frozen before outcomes?
If NO:
the aggregate quality claim is vulnerable to post-hoc composition choice.
ARCHITECTURE ROLE
HOST_RELATION = EXACT_INSTANCE of weighted means / clustered paired comparison / sampling-design semantics.
PROJECT_ROLE = T2 protocol legality rule.
ASSUMPTION_STATUS = claim-local.
SCOPE = benchmark aggregation, not model correctness itself.
FIREWALL
MORE ROWS != MORE SCIENTIFIC COVERAGE.
DUPLICATE CASE != INDEPENDENT EVIDENCE.
CASE_SET_HASH != VALID TARGET POPULATION.
UNWEIGHTED BENCHMARK AVERAGE != DEPLOYMENT AVERAGE.
POST-HOC WEIGHTS != PREDECLARED ESTIMAND.
PAIRED ANALYSIS != CORRECT POPULATION WEIGHTING.
T2 STATUS
NOT_RUN.
COMPILER_UTILITY remains UNMEASURED.
CLAIM CEILING
No holdout execution.
No compiler quality claim.
No novelty inference.
No CANON.
No EXEC_SIGN.
CORRECTNESS_FIRST / PROTOCOL_FIRST / SCIENCE_FIRST.
