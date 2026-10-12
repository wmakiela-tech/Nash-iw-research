---
artifact_id: M12-T2-RETRY-CANDIDATE-COVERAGE-AND-SELECTOR-GATE-001
bw_ingestion_event_id: ING-20261010-0076
bw_qualification_state: T2_RETRY_SELECTOR_GATE
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE_PROTOCOL_REPAIR
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# M12-T2-RETRY-CANDIDATE-COVERAGE-AND-SELECTOR-GATE-001

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

M12 - T2 retry candidate-coverage and selector gate
RESULT_CLASS
EXACT PROTOCOL CONTROL / T2 RETRY SEMANTICS / END-TO-END QUALITY GATE / NO HOLDOUT EXECUTION / NO NOVELTY CLAIM
TRIGGER
T2 correctness evaluation can still be distorted when one arm:
- gets more retries;
- generates multiple candidates;
- uses a selector after generation;
- or reports best-of-k candidate coverage instead of final returned-answer correctness.
The scientific object must be the full end-to-end policy.
SETUP
For one frozen case, suppose an arm produces k candidate outputs.
Let:
X_j=1 iff candidate j is correct.
Define candidate-set coverage event:
G
=
{at least one generated candidate is correct}.
Let S be the event:
the final output actually returned by the legal selection policy is correct.
CERTIFICATE A - SELECTED SUCCESS IS BOUNDED BY CANDIDATE COVERAGE
If the final output must be selected from the generated candidates, then:
S subseteq G.
Therefore:
P(S)
<=
P(G).
BOXED
AT-LEAST-ONE-CORRECT CANDIDATE
!=
CORRECT FINAL RETURN.
The gap:
P(G)-P(S)
is selector loss.
A benchmark reporting P(G) as final accuracy gives an oracle upper bound unless the legal selector is proven to achieve it.
CERTIFICATE B - EXACT ORACLE BEST-OF-k UNDER INDEPENDENCE
If candidate correctness events are independent with per-attempt success probability p, then:
P(G)
=
1-(1-p)^k.
For 0<p<1 this increases strictly with k.
Therefore giving one arm more attempts mechanically increases oracle candidate coverage even if its single-attempt capability is unchanged.
Example:
p=0.6.
k=1:
P(G)=0.6.
k=3:
P(G)=1-0.4^3=0.936.
Nothing about the underlying single-attempt p improved.
Thus:
MORE ATTEMPTS
CAN CREATE A LARGE BEST-OF-k QUALITY GAIN
WITHOUT ANY SINGLE-ATTEMPT QUALITY GAIN.
CERTIFICATE C - INDEPENDENCE IS NOT REQUIRED FOR THE MAIN FIREWALL
Without any independence assumption:
P(G)
=
P(union_j {X_j=1}).
Always:
max_j P(X_j=1)
<=
P(G)
<=
min(1, sum_j P(X_j=1)).
So candidate coverage depends on:
- number of attempts;
- dependence among attempts;
- generation policy.
It is not an intrinsic property of one attempt.
CERTIFICATE D - ORACLE SELECTION IS A DIFFERENT ALGORITHM
Suppose evaluation chooses a correct candidate whenever one exists by consulting ground truth.
Then final correctness equals P(G).
But this uses an oracle selector unavailable at deployment unless the same information is legally available there.
Therefore:
GROUND-TRUTH BEST-OF-k SELECTION
!=
DEPLOYABLE END-TO-END POLICY.
Oracle selection may be reported only as:
CANDIDATE_COVERAGE_UPPER_BOUND.
CERTIFICATE E - LEGAL SELECTOR MUST BE PART OF THE ARM
Let L be the actual selector:
L(candidates, legal metadata) -> one final output or abstention.
Then the evaluated compiler arm is not merely the generator.
It is:
GENERATOR
+
RETRY POLICY
+
SELECTOR
+
STOPPING RULE
+
ABSTENTION RULE.
All must be frozen before holdout evaluation.
Changing only the selector after seeing reference answers is test leakage.
CERTIFICATE F - ATTEMPT BUDGET DEFINES THE ALGORITHM
Let A_k denote the same generator with maximum k attempts.
A_1 and A_5 are different end-to-end policies.
Therefore:
SAME BASE MODEL
!=
SAME EVALUATED ALGORITHM
when retry budget differs.
A fair scientific comparison can use different attempt budgets only if:
- those budgets are prospectively part of each policy;
- all resource use is charged;
- the claim is about those full policies.
It cannot support:
"compiler reasoning is intrinsically more accurate per attempt"
unless attempt-normalized evidence is separately shown.
CERTIFICATE G - STOPPING RULE MATTERS
Examples of distinct policies:
- fixed k attempts then select;
- stop at first internally valid output;
- stop at confidence threshold;
- retry only after tool failure;
- retry after self-check failure.
These policies induce different output distributions and costs.
Therefore:
MAX_ATTEMPTS ALONE
DOES NOT FULLY SPECIFY RETRY SEMANTICS.
The stopping rule is load-bearing.
CERTIFICATE H - RETRY AFTER INFRA FAILURE VS RETRY AFTER SCIENTIFIC FAILURE
A retry triggered by:
TOOL_OR_INFRA_FAILURE
is not the same scientific event as a retry triggered by:
candidate judged scientifically inadequate.
T2 should keep these causes separate.
Infra retries can preserve the intended algorithm under transient execution failure.
Scientific retries enlarge the inference/search policy.
Mixing them obscures both quality and cost.
CERTIFICATE I - COST OF ALL ATTEMPTS
Let attempt j consume resource vector R_j.
Total per-case resource use is:
R_total
=
sum_{j actually executed} R_j
+
selector/verification overhead.
Only charging the final successful attempt undercounts policy cost.
Therefore:
BEST-OF-k QUALITY
MUST BE PAIRED WITH
ALL-ATTEMPT RESOURCE ACCOUNTING.
This connects directly to the existing M12 resource-vector and amortization gates.
CERTIFICATE J - SELECTOR FAILURE CAN DOMINATE
Suppose exactly one of two candidates is correct on every case, so:
P(G)=1.
If the legal selector chooses randomly between them:
P(S)=1/2.
Thus perfect candidate coverage can coexist with mediocre final correctness.
Therefore generation and selection quality are different estimands.
CERTIFICATE K - SELECTOR CAN ADD SCIENTIFIC VALUE
Conversely, a legal selector may improve end-to-end quality if it uses admissible evidence unavailable to a single candidate.
That improvement is real for the full policy.
But attribution must be:
SELECTOR/VERIFICATION PIPELINE VALUE,
not generator-only value.
CERTIFICATE L - PAIRED HOLDOUT INTEGRATION
For each case and arm, score only the final policy output under the frozen retry/selector contract.
Then apply the prior paired full-set correctness gate to those final outputs.
Candidate-level statistics remain diagnostics:
ATTEMPT_1_CORRECTNESS;
CANDIDATE_COVERAGE;
SELECTOR_SUCCESS_GIVEN_COVERAGE;
FINAL_CORRECT_YIELD.
Do not replace final yield with candidate coverage.
CERTIFICATE M - COVERAGE DECOMPOSITION
Define:
q
=
P(G),
s
=
P(S | G).
Because S subseteq G:
P(S)
=
q s.
Thus final correctness decomposes exactly into:
candidate coverage
times
selector success conditional on a correct candidate existing.
This separates two failure modes:
- generator never produced a correct option;
- selector failed to choose it.
PROTOCOL FIELDS
MAX_ATTEMPTS_PER_CASE
ATTEMPT_TRIGGER
STOPPING_RULE
RANDOMNESS_POLICY
CANDIDATE_GENERATION_POLICY
SELECTOR_POLICY
SELECTOR_LEGAL_INFORMATION
GROUND_TRUTH_AVAILABLE_TO_SELECTOR=NO/YES
ABSTENTION_RULE
INFRA_RETRY_RULE
SCIENTIFIC_RETRY_RULE
ATTEMPT_1_CORRECTNESS
CANDIDATE_COVERAGE
SELECTOR_SUCCESS_GIVEN_COVERAGE
FINAL_FULL_SET_CORRECT_YIELD
TOTAL_ATTEMPTS
ALL_ATTEMPT_RESOURCE_VECTOR
SELECTOR_RESOURCE_COST
CHEAP FALSIFIERS
1. Is reported "accuracy" actually at-least-one-correct among k candidates?
If YES:
it is not deployable final accuracy unless selector achieves it legally.
2. Did arms receive different retry budgets without treating them as different end-to-end policies and charging cost?
If YES:
quality attribution is invalid.
3. Was output selection changed after viewing holdout truth?
If YES:
holdout contamination.
4. Are failed attempts omitted from resource accounting?
If YES:
cost estimate is censored downward.
ARCHITECTURE ROLE
HOST_RELATION = EXACT_INSTANCE of repeated-trial probability / selective prediction / decision pipeline semantics.
PROJECT_ROLE = T2 protocol legality rule.
ASSUMPTION_STATUS = claim-local.
SCOPE = stochastic or multi-attempt evaluation policies.
FIREWALL
CANDIDATE COVERAGE != FINAL CORRECTNESS.
BEST-OF-k != SINGLE-ATTEMPT QUALITY.
ORACLE SELECTION != DEPLOYABLE SELECTION.
SAME BASE MODEL != SAME POLICY UNDER DIFFERENT RETRY BUDGETS.
MAX ATTEMPTS != FULL STOPPING RULE.
INFRA RETRY != SCIENTIFIC RETRY.
FINAL SUCCESS != COST OF ONE ATTEMPT.
GENERATOR VALUE != SELECTOR VALUE.
T2 STATUS
NOT_RUN.
COMPILER_UTILITY remains UNMEASURED.
CLAIM CEILING
No holdout execution.
No compiler utility claim.
No novelty inference.
No CANON.
No EXEC_SIGN.
CORRECTNESS_FIRST / END_TO_END_POLICY_FIRST / SCIENCE_FIRST.
