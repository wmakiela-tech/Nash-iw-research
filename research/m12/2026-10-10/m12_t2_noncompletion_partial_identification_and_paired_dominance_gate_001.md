---
artifact_id: M12-T2-NONCOMPLETION-PARTIAL-IDENTIFICATION-AND-PAIRED-DOMINANCE-GATE-001
bw_ingestion_event_id: ING-20261010-0072
bw_qualification_state: T2_NONCOMPLETION_PARTIAL_IDENTIFICATION
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE_PROTOCOL_REPAIR
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# M12-T2-NONCOMPLETION-PARTIAL-IDENTIFICATION-AND-PAIRED-DOMINANCE-GATE-001

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

M12 - T2 noncompletion bounds and paired dominance gate
RESULT_CLASS
EXACT PROTOCOL CONTROL / PARTIAL IDENTIFICATION / NO HOLDOUT EXECUTION / NO NOVELTY CLAIM
TRIGGER
DAX-S6 showed:
ACCURACY_AMONG_COMPLETED != FULL_HOLDOUT_PERFORMANCE.
Selective noncompletion can create a spurious quality win.
This return gives exact worst/best-case bounds when some frozen cases do not return a valid answer.
SETUP
Freeze N holdout cases for each arm.
For one arm define:
C = number of completed-correct cases,
I = number of completed-incorrect cases,
M = number of noncompleted/unresolved cases for a hypothetical forced-answer correctness claim.
N=C+I+M.
Let U be the unknown number of those M cases that would have been correct under a declared forced-completion counterfactual.
Then:
0 <= U <= M.
The latent full-set forced-answer accuracy is:
A* = (C+U)/N.
CERTIFICATE A - EXACT NONCOMPLETION BOUNDS
Without further assumptions:
C/N
<=
A*
<=
(C+M)/N.
These bounds are sharp.
Therefore:
completed-case accuracy
C/(C+I)
does not identify full-set forced-answer accuracy when M>0.
CERTIFICATE B - PAIRED ARM DIFFERENCE
For compiler arm c and baseline arm b:
A_c* in [C_c/N, (C_c+M_c)/N],
A_b* in [C_b/N, (C_b+M_b)/N].
Therefore the paired accuracy difference:
Delta*=A_c*-A_b*
is sharply bounded by:
LOWER =
(C_c - C_b - M_b)/N,
UPPER =
(C_c + M_c - C_b)/N.
Decision:
- if LOWER > 0: compiler is better under every completion of missing correctness;
- if UPPER < 0: baseline is better under every completion;
- otherwise: latent forced-answer superiority is UNRESOLVED.
CERTIFICATE C - DAX TOY
Baseline:
N=10,
C_b=8,
I_b=2,
M_b=0.
Compiler:
C_c=6,
I_c=0,
M_c=4.
Compiler completed-case accuracy = 1.0.
Baseline completed-case accuracy = 0.8.
But:
A_c* in [0.6,1.0],
A_b*=0.8.
Thus:
Delta* in [-0.2,+0.2].
So even the forced-answer latent accuracy ordering is unresolved.
The complete-case 1.0>0.8 statement is not a full-holdout win.
CERTIFICATE D - VALID ABSTENTION IS NOT MISSINGNESS
If VALID_ABSTENTION is an allowed terminal protocol outcome, do not hide it inside M.
It must be evaluated under a predeclared selective-prediction contract:
- coverage;
- correctness/risk conditional on answering;
- abstention rate;
- abstention loss or utility if one is scientifically justified.
A timeout or invalid output cannot be reclassified post hoc as valid abstention.
Thus two distinct objects exist:
1. CENSORING / UNRESOLVED FORCED-ANSWER OUTCOME:
use partial-identification bounds.
2. DECLARED ABSTENTION POLICY:
use selective-prediction utility/coverage semantics.
CERTIFICATE E - FULL-SET CORRECT YIELD
If the operational scientific question is simply:
"how many frozen cases received a correct usable answer within budget?"
then the exact primary quantity is:
Y = C/N.
No imputation is needed.
This quantity penalizes nonreturn through zero delivered correct answers, while resource costs of timeouts remain separately counted.
Therefore:
FULL_SET_CORRECT_YIELD
is exact operational performance,
whereas
LATENT_FORCED_ACCURACY
is a partially identified counterfactual.
Do not mix them.
CERTIFICATE F - MONOTONE ASSUMPTION OPTIONAL
If a predeclared scientific assumption implies noncompleted cases are no easier than completed ones, one may derive tighter one-sided bounds only if that assumption is independently justified.
Do not infer it merely because the system timed out.
TIMEOUT_DIFFICULTY_CORRELATION
is a selection mechanism, not a free theorem.
PROTOCOL PATCH
Freeze before T2:
CASE_SET_HASH
CASE_COUNT
BUDGET_PER_CASE
OUTCOME_STATE_DEFINITION
PRIMARY_OPERATIONAL_METRIC
VALID_ABSTENTION_RULE
FORCED_ANSWER_COUNTERFACTUAL_USED? YES/NO
MISSINGNESS_BOUND_RULE
PAIRED_DOMINANCE_RULE
RESOURCE_COST_FOR_NONRETURN.
Recommended default:
Primary = FULL_SET_CORRECT_YIELD + SAFETY + RESOURCE_PROFILE.
Secondary = coverage + conditional correctness.
Only report latent forced-answer accuracy as an identified interval unless extra assumptions close it.
FIREWALL
COMPLETED_CASE_ACCURACY != FULL_SET_YIELD.
NONCOMPLETION != INCORRECTNESS automatically.
NONCOMPLETION != VALID_ABSTENTION automatically.
FORCED_ANSWER_ACCURACY != OPERATIONAL DELIVERED UTILITY.
OVERLAPPING SHARP BOUNDS != QUALITY WIN.
STATUS
T2 NOT RUN.
COMPILER_UTILITY UNMEASURED.
This is a protocol gate only.
No holdout execution.
No CANON / NO EXEC_SIGN / NO NOVELTY.
