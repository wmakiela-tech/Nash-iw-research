---
artifact_id: M12-FRONTB-DE-CHANNEL-YIELD-IDENTITY-AND-CORRECTION-001
bw_ingestion_event_id: ING-20261010-0134
bw_qualification_state: FRONTB_CHANNEL_YIELD_CORRECTION
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE_CORRECTION
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# M12-FRONTB-DE-CHANNEL-YIELD-IDENTITY-AND-CORRECTION-001

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

M12 — Front B dynamical-equilibrium channel-yield identity and correction
RESULT_CLASS
EXACT LOCAL CONTROL / CORRECTION OF PRIOR M12 INTERPRETATION / NO NUMERICAL ENDPOINT / NO NOVELTY CLAIM
CORRECTS
M12-FRONTB-DYNAMICAL-EQUILIBRIUM-ADMISSION-ERROR-IDENTITY-001.
TRIGGER
NC-MT13-FRONTB-DE-CLOSURE-ADMISSION-AUDIT-001 established that the prior M12 Duhamel identity is mathematically correct for population tracking but was overinterpreted as the controlling admission object for integrated channel yields.
The controlling yield object is branching, not the local population-tracking error alone.
SETUP
For one hadron population:
n'(t)=S(t)-Gamma(n,t)n(t).
Assume channel decomposition:
Gamma_c(n,t)=b_c(n,t) Gamma(n,t),
with:
sum_c b_c(n,t)=1.
Let an instantaneous DE fixed point n_*(t) satisfy:
S(t)=Gamma(n_*(t),t) n_*(t).
Define:
b_c^ex(t)=b_c(n(t),t),
b_c^de(t)=b_c(n_*(t),t).
Exact channel yield:
N_c^ex
=
integral Gamma_c(n,t)n(t) dt.
DE channel yield:
N_c^de
=
integral Gamma_c(n_*,t)n_*(t) dt
=
integral b_c^de(t) S(t) dt.
CERTIFICATE A — GENERAL EXACT CHANNEL-YIELD IDENTITY
Using:
Gamma(n,t)n
=
S-n',
we get:
N_c^ex
=
integral b_c^ex S dt
-
integral b_c^ex n' dt.
Integrating by parts:
N_c^ex
=
integral b_c^ex S dt
-
[b_c^ex n]_{t0}^{t1}
+
integral (d b_c^ex/dt) n dt.
Therefore exactly:
N_c^ex - N_c^de
=
integral [b_c^ex-b_c^de] S dt
-
[b_c^ex n]_{t0}^{t1}
+
integral (d b_c^ex/dt) n dt.
BOXED
CHANNEL-YIELD ERROR
=
BRANCHING-MISMATCH TERM
+
BOUNDARY POPULATION TERM
+
BRANCHING-VARIATION TERM.
No epsilon_DE term appears.
CERTIFICATE B — PRESCRIBED BRANCHING SPECIAL CASE
If branching is prescribed in time only:
b_c^ex=b_c^de=b_c(t),
then:
N_c^ex-N_c^de
=
-[b_c n]_{t0}^{t1}
+
integral b_c'(t)n(t)dt.
If the integration window contains full injection and full relaxation so that:
n(t0)=n(t1)=0,
then:
N_c^ex-N_c^de
=
integral b_c'(t)n(t)dt.
This reproduces the NC exact law.
CERTIFICATE C — CONSTANT BRANCHING
If additionally:
b_c'(t)=0,
and the endpoints are relaxed, then:
N_c^ex
=
N_c^de
EXACTLY,
for arbitrary source time dependence S(t) and arbitrary total depletion Gamma(t), provided the DE algebraic state is well-defined.
Thus:
RAPID SOURCE VARIATION
DOES NOT BY ITSELF PRODUCE CHANNEL-YIELD ERROR.
This directly corrects the prior M12 statement that terminal source acceleration can itself break the integrated-target DE approximation.
It can break population tracking while leaving the integrated channel yield exact.
CERTIFICATE D — TOTAL YIELD CONSERVATION
Summing over all channels:
sum_c b_c^ex
=
sum_c b_c^de
=
1,
and:
sum_c d b_c^ex/dt
=
0.
Therefore:
N_tot^ex-N_tot^de
=
-[n]_{t0}^{t1}.
On a fully relaxed window:
N_tot^ex=N_tot^de.
This remains true even when Gamma depends on state, as long as the channel partition is complete and the DE state exists.
Hence:
TOTAL-YIELD CONSERVATION
IS STRONGER THAN POPULATION-TRACKING ACCURACY.
CERTIFICATE E — STEP/THRESHOLD BRANCHING
If b_c is piecewise constant with jumps Delta b_j at times t_j and endpoints are relaxed:
N_c^ex-N_c^de
=
sum_j Delta b_j n(t_j)
for prescribed branching.
Therefore:
|N_c^ex-N_c^de|
<=
sum_j |Delta b_j| sup_{window j} n.
This is the exact source of the NC threshold certificate.
Sharp threshold width is not itself the controlling parameter.
Only the jump size and the population present at the transition enter in the step limit.
CERTIFICATE F — STATE-DEPENDENT BRANCHING
If b_c depends on the evolving state, then even when total yield remains conserved, channel yields can differ through:
1. b_c^ex-b_c^de;
2. total derivative d b_c^ex/dt.
Thus state dependence matters through channel allocation, not merely through total Gamma.
This is more precise than saying:
"state-dependent Gamma breaks the exact yield law."
The generalized exact law survives.
What changes is the branching comparison.
CERTIFICATE G — FIXED-POINT EXISTENCE AND ITERATION
The DE state n_* must exist before N_c^de is defined.
For a scalar iteration:
T(n)=S/Gamma(n),
at a fixed point n_*:
T'(n_*)
=
- d ln Gamma / d ln n
evaluated at n_*.
Hence:
|d ln Gamma/d ln n|<1
is a local contraction condition for that specific fixed-point iteration.
But:
|d ln Gamma/d ln n|>=1
does NOT universally imply that no fixed point exists.
It implies only that this iteration is not locally contractive there.
Existence, uniqueness, stability and convergence of the chosen numerical iteration are separate questions.
This repairs a possible overreading of the NC toy family.
CERTIFICATE H — CORRECT ADMISSION SPLIT
Front-B DE admission must now be separated into:
A. ALGEBRAIC EXISTENCE:
Does the instantaneous coupled fixed point exist?
B. BRANCHING CONSISTENCY:
How do b_c^ex and b_c^de differ?
Do channel thresholds/openings change the allocation?
C. BOUNDARY RELAXATION:
Does the comparison window contain the relevant injection and relaxation?
D. TARGET PROPAGATION:
How do channel-yield differences affect Yp and D/H?
E. SOURCE VALIDITY:
Are S, Gamma and channel definitions source-matched to PBH/B2?
Population-tracking epsilon_DE is at most an auxiliary diagnostic unless the target depends directly on instantaneous n(t).
CERTIFICATE I — RELATION TO TARGET-WEIGHTED KERNEL
For BBN abundance targets, the immediate source object should be the weak-rate/channel-history discrepancy produced by the exact yield/branching analysis.
Then apply the M12 target-weighted functional certificate:
rate-history difference
->
target sensitivity
->
Yp/D-H error.
Therefore:
DE population error
need not be small
if the induced target-driving channel history is exact or target-null.
CORRECTION TO PRIOR M12 RETURN
The following prior statement is withdrawn as a controlling Front-B admission claim:
"rapid terminal Hawking source acceleration can break DE locally and therefore requires a source-timescale gate before target validation."
Correct replacement:
Rapid source acceleration may break instantaneous population tracking, but it does not by itself imply integrated channel-yield error.
For prescribed constant branching and full relaxation, the channel yield is exact regardless of epsilon_DE.
The load-bearing residual is branching/state-feedback structure plus target propagation.
PRESERVE FROM PRIOR M12 RETURN
The following remain valid:
- exact population error equation e'=-Gamma e-n_*';
- Duhamel representation for population tracking;
- vector propagator generalization;
- fixed-point stopping tolerance != physical admission;
- source matching required;
- target-weighted validation required.
These results are retyped as POPULATION-TRACKING controls, not universal integrated-target admission controls.
FRONT-B DISPOSITION
ENDPOINT_TIMESCALE_WORRY = PARK for prescribed/fixed-branching channel yields.
BRANCHING_THRESHOLD_AND_STATE_FEEDBACK = LOAD-BEARING.
FIXED_POINT_EXISTENCE/UNIQUENESS = OPEN SOURCE-MATCHED.
PBH CHANNEL SWEEP / HADRON SPECTRA = OPEN.
TARGET-WEIGHTED Yp/D-H PROPAGATION = OPEN SOURCE-MATCHED.
SOURCE_MATCHED_K_PBH = UNDEFINED.
NO ENDPOINT RELEASE.
LOWER-HOST SUBTRACTION
HOST_RELATION = EXACT_INSTANCE of source-sink conservation + integration by parts + fixed-point analysis.
PROJECT_ROLE = CORRECTION / LOCAL THEOREM / ADMISSION REPAIR.
No novelty.
FIREWALL
POPULATION TRACKING ERROR != CHANNEL-YIELD ERROR.
epsilon_DE FAILURE != TARGET FAILURE.
CONSTANT BRANCHING + FULL RELAXATION => EXACT CHANNEL YIELD.
STATE-DEPENDENT TOTAL Gamma != AUTOMATIC CHANNEL-YIELD FAILURE.
LOCAL NONCONTRACTION != NONEXISTENCE.
FIXED-POINT EXISTENCE != SOURCE-NATIVE PHYSICAL VALIDITY.
CHANNEL-YIELD CERTIFICATE != PBH ENDPOINT RELEASE.
STATUS
PRIOR M12 INTERPRETATION = CORRECTED, NOT SILENTLY OVERWRITTEN.
NC AUDIT = MATERIAL.
FRONT-B BLOCKER = BRANCHING/FEEDBACK/SOURCE-MATCHED TARGET PROPAGATION.
NO NUMERICAL ENDPOINT / NO CANON / NO EXEC_SIGN / NO NOVELTY INFERENCE.
