---
artifact_id: M12-T2-PAIRED-FULL-SET-CORRECTNESS-GATE-001
bw_ingestion_event_id: ING-20261010-0070
bw_qualification_state: T2_PAIRED_FULL_SET_CORRECTNESS
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE_PROTOCOL_REPAIR
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# M12-T2-PAIRED-FULL-SET-CORRECTNESS-GATE-001

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

M12 - T2 paired full-set correctness gate
RESULT_CLASS
EXACT PROTOCOL CONTROL / T2 QUALITY SEMANTICS / MATCHED-HOLDOUT CERTIFICATE / NO HOLDOUT EXECUTION / NO NOVELTY CLAIM
TRIGGER
DAX-S6 showed that completed-case accuracy can spuriously favor a compiler that selectively fails to complete hard cases.
T2 therefore needs a correctness estimand that:
- uses the prospectively frozen paired holdout;
- keeps every case in the denominator;
- exploits pairing instead of comparing two unrelated proportions.
SETUP
Let N frozen holdout cases be evaluated by both arms:
B = baseline,
C = compiler.
Define per case binary indicators:
B_i = 1 iff baseline returns CORRECT_COMPLETE on case i;
C_i = 1 iff compiler returns CORRECT_COMPLETE on case i.
All other frozen states:
INCORRECT_COMPLETE,
VALID_ABSTENTION,
TIMEOUT,
INVALID_OUTPUT,
TOOL_OR_INFRA_FAILURE
receive indicator 0 for this particular FULL_SET_CORRECT_YIELD estimand.
This does NOT mean all those states are scientifically equivalent.
They remain separately typed for safety, abstention and resource analysis.
CERTIFICATE A - EXACT PAIRED YIELD DIFFERENCE
Partition the N paired cases into:
n_11: both correct;
n_10: compiler correct, baseline not correct;
n_01: baseline correct, compiler not correct;
n_00: neither correct.
Then:
Y_C = (n_11+n_10)/N,
Y_B = (n_11+n_01)/N.
Therefore exactly:
Delta_Y
=
Y_C-Y_B
=
(n_10-n_01)/N.
BOXED
PAIRED FULL-SET CORRECTNESS DIFFERENCE
DEPENDS ONLY ON DISCORDANT CASES.
Cases on which both arms are correct or both are not correct cancel exactly.
CERTIFICATE B - WHY UNPAIRED COMPARISON WASTES DESIGN INFORMATION
Because both arms see the same frozen cases, case difficulty is shared.
The paired estimator uses the within-case difference:
D_i=C_i-B_i in {-1,0,1}.
Then:
Delta_Y
=
(1/N) sum_i D_i.
Treating the two arm accuracies as independent proportions ignores this pairing and can inflate uncertainty or misstate the test.
Thus:
PAIRED HOLDOUT
SHOULD BE ANALYZED AS PAIRED.
CERTIFICATE C - EXACT NULL TEST
Under the sharp paired null that, conditional on a case being discordant, compiler-win and baseline-win are equally likely, let:
m=n_10+n_01.
Then conditional on m:
n_10 ~ Binomial(m,1/2).
This gives the exact matched-pair sign/McNemar test.
No normal approximation is required.
Therefore T2 can predeclare:
- superiority;
- noninferiority;
- or equivalence target;
using paired discordant outcomes.
CERTIFICATE D - EFFECT SIZE IS NOT THE P-VALUE
The scientific effect size remains:
Delta_Y=(n_10-n_01)/N.
A small p-value with tiny |Delta_Y| is not automatically operationally meaningful.
A large |Delta_Y| with wide uncertainty is not yet a certified population effect.
Therefore report separately:
- paired point effect;
- uncertainty interval;
- decision threshold/margin.
CERTIFICATE E - NONINFERIORITY MARGIN
If correctness preservation is the primary gate, predeclare a tolerable loss margin delta>=0.
Compiler passes correctness noninferiority only if the uncertainty procedure supports:
Delta_Y > -delta
at the declared confidence/error level.
The margin must be frozen before seeing outcomes.
POST-HOC NONINFERIORITY MARGIN
!=
VALID CORRECTNESS GATE.
CERTIFICATE F - VALID ABSTENTION IS NOT AUTOMATICALLY AN ERROR CLAIM
For FULL_SET_CORRECT_YIELD, valid abstention contributes 0 correct returns.
But this does NOT license the statement:
ABSTENTION = INCORRECT ANSWER.
A valid abstention may be preferable to an unsafe wrong answer.
Therefore T2 must retain at least two distinct outcome layers:
LAYER 1
correct-return yield.
LAYER 2
outcome-type distribution:
correct,
wrong,
valid abstention,
timeout,
invalid,
tool/infra failure.
Safety or utility can weight these differently only under a predeclared loss rule.
CERTIFICATE G - CONDITIONAL ACCURACY IS SECONDARY
Let K_C be cases completed by compiler.
Conditional accuracy:
Acc_C|complete
=
correct completions / |K_C|.
This quantity can increase while full-set yield decreases.
Therefore:
CONDITIONAL CORRECTNESS
MUST NOT REPLACE
FULL-SET CORRECT YIELD.
It is a secondary diagnostic for behavior given completion.
CERTIFICATE H - COVERAGE-CORRECTNESS DECOMPOSITION
Let:
Cov_C = completed valid-answer fraction,
Acc_C = correctness conditional on completed valid answers.
Then, when every completed valid answer is either correct or incorrect:
Y_C
=
Cov_C * Acc_C.
So a compiler can improve Acc_C while harming Y_C through lower coverage.
This is exactly the completion-censoring mechanism isolated by DAX-S6.
CERTIFICATE I - PAIRED SAFETY CAN BE SEPARATE
If unsafe wrong outputs are specially important, define a second paired binary outcome:
U_i=1 iff arm emits a predeclared unsafe output.
Then compare paired unsafe-event differences independently from correctness yield.
Do NOT bury safety inside one scalar quality score unless the loss function is frozen in advance.
CERTIFICATE J - RESOURCE COST STAYS ORTHOGONAL
A case where compiler times out and baseline succeeds contributes:
- C_i=0, B_i may equal 1 for correctness;
- actual compiler resource consumption to the cost vector.
Thus:
NONRETURN != ZERO COST,
and
QUALITY DIFFERENCE != COST DIFFERENCE.
This preserves the existing M12 resource-vector/Pareto gate.
PROTOCOL FIELDS
CASE_SET_HASH
CASE_COUNT
PAIRING_ID
OUTCOME_TAXONOMY
PRIMARY_QUALITY_ESTIMAND=FULL_SET_CORRECT_YIELD
N_11
N_10
N_01
N_00
DELTA_FULL_SET_CORRECT_YIELD
PAIRED_UNCERTAINTY_METHOD
SUPERIORITY_OR_NONINFERIORITY_RULE
NONINFERIORITY_MARGIN_IF_USED
COMPLETION_COVERAGE
CONDITIONAL_CORRECTNESS
ABSTENTION_RATE
TIMEOUT_RATE
INVALID_OUTPUT_RATE
TOOL_INFRA_FAILURE_RATE
SAFETY_ESTIMAND
RESOURCE_VECTOR_ESTIMAND
CHEAP FALSIFIER
Ask:
Were both arms scored on exactly the same prospectively frozen cases, with all cases retained in the primary correctness denominator?
If NO:
paired correctness claim is invalid for the frozen holdout.
Ask:
Was the primary arm difference computed from discordant paired outcomes or an equivalent paired estimator?
If NO:
the analysis is not using the design efficiently and may be miscalibrated.
T2 STATUS
T2 remains NOT_RUN.
No empirical compiler-quality claim is made.
ARCHITECTURE ROLE
HOST_RELATION = EXACT_INSTANCE of matched-pair binary comparison / McNemar-sign-test mathematics.
PROJECT_ROLE = PROTOCOL CORRECTNESS RULE.
ASSUMPTION_STATUS = MATCHED when both arms evaluate the same frozen cases under the same correctness definition.
SCOPE = T2 paired holdout correctness only.
FIREWALL
COMPLETED-CASE ACCURACY != FULL-SET CORRECT YIELD.
UNPAIRED PROPORTION TEST != NATURAL PAIRED ANALYSIS.
P-VALUE != EFFECT SIZE.
VALID ABSTENTION != WRONG ANSWER.
TIMEOUT != VALID ABSTENTION.
NONRETURN != ZERO COST.
CORRECTNESS GATE != SAFETY GATE.
CORRECTNESS GATE != RESOURCE-COST GATE.
CLAIM CEILING
No T2 holdout execution.
No compiler utility claim.
No novelty inference.
No CANON.
No EXEC_SIGN.
SCIENCE_FIRST / CORRECTNESS_FIRST / PRESERVE_NEGATIVE_KNOWLEDGE.
