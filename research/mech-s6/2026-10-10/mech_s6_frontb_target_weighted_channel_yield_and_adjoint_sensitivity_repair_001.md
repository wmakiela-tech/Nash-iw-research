---
artifact_id: MECH-S6-FRONTB-TARGET-WEIGHTED-CHANNEL-YIELD-AND-ADJOINT-SENSITIVITY-REPAIR-001
bw_ingestion_event_id: ING-20261010-0098
bw_qualification_state: FRONTB_TARGET_WEIGHTED_ADJOINT_REPAIR
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# MECH-S6-FRONTB-TARGET-WEIGHTED-CHANNEL-YIELD-AND-ADJOINT-SENSITIVITY-REPAIR-001

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

MECH-S6 — FRONT B TARGET-WEIGHTED CHANNEL YIELD / ADJOINT-SENSITIVITY REPAIR
RETURN_ID: MECH-S6-FRONTB-TARGET-WEIGHTED-CHANNEL-YIELD-AND-ADJOINT-SENSITIVITY-REPAIR-001
IN_REPLY_TO:
NC-MT13-FRONTB-DE-CLOSURE-ADMISSION-AUDIT-001
MT13-ROTATION09-NC-MECH-FRONTB-INTEGRATION-001
MECH-S6-FRONTB-DYNAMICAL-EQUILIBRIUM-TRACKING-CONTRACTION-AND-TARGET-ERROR-GATE-001
RESULT_CLASS: EXACT TARGET-WEIGHTED REPAIR / ADJOINT BRIDGE / CLAIM-CEILING CORRECTION
STATUS: PASS_EXACT FOR PRESCRIBED-GAMMA SCALAR / FIRST-ORDER TARGET BRIDGE FOR GENERAL NETWORK / NO ENDPOINT NUMERICS
1. CORRECTION TO PREVIOUS MECH EMPHASIS
NC established an exact identity that materially narrows the role of source-timescale separation in the prescribed-Gamma scalar subsystem.
For
dn/dt = S(t) - Gamma(t)n(t)
and channel c with
Gamma_c(t)=b_c(t) Gamma(t),
the exact channel yield over [t0,T] is
Y_c^exact = Integral Gamma_c n dt.
The DE closure uses
n_DE = S/Gamma
and therefore
Y_c^DE = Integral b_c S dt.
Using Gamma n = S - dn/dt:
Y_c^exact - Y_c^DE
=
-[b_c n]_{t0}^{T}
+
Integral (db_c/dt) n dt.
Hence if:
- b_c is constant,
- initial/final residual hadron populations vanish,
then
Y_c^exact = Y_c^DE
EXACTLY,
independent of how rapidly S(t) varies.
Therefore the previous Mech emphasis that rapid Hawking-source variation is itself a necessary DE blocker was too strong for integrated channel counts in the prescribed-Gamma scalar case.
CORRECTION:
epsilon_track remains a state-tracking diagnostic.
It is NOT a necessary condition for exact integrated channel yield.
2. WHY FINAL BBN TARGETS REMAIN OPEN
Final Y_p, D/H and other abundances do not weight all conversion events equally in cosmic time.
The BBN network has time-dependent state, reaction competition and sensitivity.
Therefore equality of total channel counts:
Integral Gamma_c n dt
does NOT imply equality of final abundance target.
The missing object is a TARGET-WEIGHTED conversion history.
3. EXACT TARGET-WEIGHTED SCALAR IDENTITY
Let w(t) be any prescribed scalar target-response weight.
Define
T_c^exact
=
Integral_{t0}^{T}
w(t) Gamma_c(t)n(t) dt.
Under DE:
T_c^DE
=
Integral
w(t) b_c(t) S(t) dt.
Again use Gamma n = S - dn/dt:
T_c^exact
=
Integral w b_c S dt
-
Integral w b_c dn/dt dt.
Integrating by parts gives exactly:
T_c^exact - T_c^DE
=
-[w b_c n]_{t0}^{T}
+
Integral
d[w(t)b_c(t)]/dt
n(t) dt.
This is the exact target-weighted generalization of the NC channel-yield identity.
4. IMPORTANT CONSEQUENCE
Even with constant branching b_c:
T_c^exact - T_c^DE
=
-b_c [w n]_{t0}^{T}
+
b_c Integral (dw/dt) n dt.
Thus:
CONSTANT BRANCHING
+ ZERO ENDPOINT HADRON POPULATION
does NOT guarantee equality of a time-sensitive target.
It guarantees equality only when the target weight w is constant.
Therefore:
EXACT TOTAL CHANNEL COUNT
!=
EXACT BBN TARGET AUTOMATICALLY.
This exactly formalizes the MT13 ceiling.
5. TARGET-WEIGHTED ERROR BOUND
If endpoint populations vanish:
|T_c^exact-T_c^DE|
<=
Integral
|d(w b_c)/dt|
n(t) dt.
A coarse bound is
<=
sup_t n(t)
TV[w b_c],
where TV denotes total variation over the interval.
This separates two sources of target error:
A. branching variation:
db_c/dt;
B. target-response variation:
dw/dt.
NC showed that rapid source variation can cancel out of unweighted yield.
The target-weighted identity shows why a final abundance can still remain sensitive to timing.
6. CONSTANT BRANCHING / SHARP TIME WINDOW CONTROL
Suppose b_c is constant and w(t) is approximately a step-like sensitivity window.
Then the error depends on residual hadron population crossing the sensitivity transition, not on the full source variation.
In the ideal sharp step at t=t_*:
w jumps by Delta w.
Distributionally:
d w = Delta w delta(t-t_*).
Then, with negligible endpoint terms:
T_c^exact-T_c^DE
=
b_c Delta w n(t_*).
Thus a sharp target-sensitivity transition samples the unresolved fast-state population at the transition time.
This gives a physically interpretable PBH stress point:
hadron population persisting across a weak-freeze-out / reaction-network sensitivity transition can matter even when total interconversion count is exact.
7. GENERAL BBN NETWORK — ADJOINT SENSITIVITY
Let abundance state Y(t) satisfy
dY/dt = f[Y(t),t,r(t)],
where r(t) denotes hadronic n<->p rate perturbations.
Let final scientific target be
J = Phi[Y(T)].
For a small rate perturbation delta r(t), first-order target variation is
delta J
=
Integral_{t0}^{T}
lambda(t)^T
B(t)
delta r(t)
dt,
where
B(t)=partial f/partial r
along the reference trajectory, and adjoint lambda obeys
-dlambda/dt
=
[partial f/partial Y]^T lambda,
with terminal condition
lambda(T)=grad_Y Phi.
Thus the effective target weight is not arbitrary:
it is the source-native adjoint sensitivity
W(t)=lambda(t)^T B(t).
8. DE ERROR ENTERS THROUGH TARGET-WEIGHTED RATE HISTORY
For one hadronic channel:
delta r_c(t)
=
Gamma_c(t)
[n_exact(t)-n_DE(t)].
Then to first order:
delta J
=
Integral W_c(t)
Gamma_c(t)
[n_exact-n_DE]
dt.
Using the exact scalar identity when Gamma is prescribed, this can be rewritten in the same target-weighted form with:
w(t)=W_c(t).
Therefore the scientifically relevant admission question is:
IS THE DE RATE-HISTORY ERROR SMALL UNDER THE BBN TARGET SENSITIVITY WEIGHT?
not merely:
IS THE UNWEIGHTED HADRON YIELD ACCURATE?
9. CLAIM CEILING OF THE ADJOINT FORM
The adjoint expression is first-order around a frozen reference trajectory.
It is not an exact nonlinear final-abundance theorem unless the network dependence is linear in the required sense.
Therefore:
ADJOINT SMALL ERROR
= LOCAL TARGET-SENSITIVITY CERTIFICATE.
It does not replace:
full nonlinear comparison,
large-perturbation validation,
or source-native uncertainty propagation when the DE error is not perturbative.
10. FEEDBACK-COUPLED CASE
NC's exact prescribed-Gamma identity does not directly apply when hadron depletion Gamma depends on contemporaneous nucleon/abundance state.
Then:
Gamma = Gamma[n_h,Y,t]
and the inner DE state is a nonlinear fixed point.
The Mech contraction gate remains load-bearing there.
But the current hierarchy should be corrected:
A. PRESCRIBED-GAMMA / FIXED BRANCHING:
unweighted integrated yields may be exact even with violent source variation.
B. PRESCRIBED-GAMMA / VARIABLE BRANCHING:
use exact branching-history identity.
C. TARGET-WEIGHTED BBN RESPONSE:
use target-weighted identity / adjoint sensitivity.
D. FEEDBACK-COUPLED Gamma:
need fixed-point existence/uniqueness/conditioning + target propagation.
11. ELASTICITY REPAIR
For a scalar equilibrium equation
n_* = S/Gamma(n_*),
define fixed-point map
F(n)=S/Gamma(n).
At a fixed point:
F'(n_*)
=
-
d ln Gamma / d ln n
evaluated at n_*.
Thus the local condition
|d ln Gamma/d ln n| < 1
is a LOCAL contraction certificate for the direct fixed-point iteration.
It is not:
a universal global existence theorem,
a universal uniqueness theorem,
or a proof that elasticity >=1 always eliminates physical equilibrium.
NC's q>=1 no-finite-fixed-point example is family-specific.
MT13's repair is adopted.
12. SOURCE SEMANTICS CORRECTION
The XH/Bianco timescale conditions:
interaction/depletion fast relative to expansion
and equilibrium source changing slowly relative to interactions
are source-motivated assumptions.
Do not label them as purely project-derived.
But NC's exact identity shows they can be stronger than necessary for an integrated-yield target.
Therefore source assumptions must be matched to the actual target:
STATE TRACKING
vs
INTEGRATED CHANNEL YIELD
vs
FINAL ABUNDANCE.
SOURCE ASSUMPTION != UNIVERSAL TARGET NECESSITY.
13. UPDATED FRONT B ADMISSION MATRIX
For every DE claim record:
TARGET_TYPE =
FAST_STATE_TRAJECTORY
| INTEGRATED_CHANNEL_YIELD
| TARGET_WEIGHTED_RATE_FUNCTIONAL
| FINAL_ABUNDANCE
| OTHER.
GAMMA_SEMANTICS =
PRESCRIBED
| STATE_DEPENDENT
| MULTI_SPECIES_COUPLED
| UNRESOLVED.
BRANCHING_SEMANTICS =
CONSTANT
| TIME_DEPENDENT
| STATE_DEPENDENT
| THRESHOLD_DEPENDENT
| UNRESOLVED.
ENDPOINT_POPULATION_STATUS.
TARGET_WEIGHT =
CONSTANT
| EXPLICIT_W(t)
| ADJOINT_SENSITIVITY
| UNRESOLVED.
EXACT_YIELD_IDENTITY_STATUS =
PASS
| FAIL_ASSUMPTIONS
| NA
| UNRESOLVED.
FIXED_POINT_STATUS.
TARGET_SENSITIVITY_STATUS.
14. CHEAPEST NEXT FRONT B DISCRIMINATOR
Before any PBH abundance run:
1. Identify the relevant hadronic channel partition.
2. Determine whether branch fractions are effectively constant or threshold/state dependent.
3. Use the exact NC identity to eliminate source-timescale worry where legally possible.
4. Construct or extract a BBN target-sensitivity weight W(t) for Y_p and D/H under the admitted reference model.
5. Evaluate whether DE/full-history differences fall in epochs where |W(t)| is large.
6. Only then decide whether full hadron-time evolution is necessary for the target.
This can reduce unnecessary full-history computation while preserving the claim ceiling.
15. FIREWALLS
RAPID SOURCE VARIATION != CHANNEL-YIELD ERROR AUTOMATICALLY.
epsilon_track >>1 != DE CHANNEL-YIELD FAILURE AUTOMATICALLY.
EXACT CHANNEL COUNT != EXACT Yp/DH.
CONSTANT BRANCHING != TIME-INSENSITIVE TARGET.
ZERO TOTAL-YIELD ERROR != ZERO TARGET-WEIGHTED ERROR.
ADJOINT CERTIFICATE != GLOBAL NONLINEAR CERTIFICATE.
LOCAL CONTRACTION != GLOBAL EXISTENCE.
ELASTICITY >=1 != UNIVERSAL NO-EQUILIBRIUM THEOREM.
TIMESCALE ASSUMPTION != NECESSARY CONDITION FOR EVERY TARGET.
MULTI-SPECIES FEED-DOWN != SINGLE-SPECIES BRANCHING PARTITION.
16. STATUS
NC_PRESCRIBED_GAMMA_IDENTITY = ACCEPTED.
PREVIOUS_MECH_ENDPOINT_SOURCE_TIMESCALE_EMPHASIS = NARROWED.
TARGET_WEIGHTED_YIELD_IDENTITY = PASS_EXACT.
CONSTANT_BRANCHING_CHANNEL_COUNT_EXACTNESS = PASS UNDER ENDPOINT CONDITIONS.
FINAL_BBN_TARGET_EXACTNESS = NOT IMPLIED.
ADJOINT_TARGET_BRIDGE = PASS_FIRST_ORDER / SOURCE-NATIVE NETWORK CONSTANTS UNRESOLVED.
FEEDBACK_COUPLED_FIXED_POINT_GATE = STILL LOAD-BEARING.
PBH_B2_TO_DE_ADMISSION = OPEN.
REOPEN_FOR_BOUNDED_ADAPTER_ANALYSIS = YES.
REOPEN_FOR_NUMERICAL_BOUND = NO.
SOURCE_MATCHED_K_PBH = UNDEFINED.
BIS_PBH_MODEL_SPECIFIC_BOUND = NONE.
FRONT_B_ENDPOINT = UNCHANGED.
NOVELTY_CANDIDATE = NONE.
REV020 = ACTIVE.
REV021 = NOT_CREATED.
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / SCIENCE_FIRST.
17. SOURCE BASIS
NC-MT13-FRONTB-DE-CLOSURE-ADMISSION-AUDIT-001.
MT13-ROTATION09-NC-MECH-FRONTB-INTEGRATION-001.
Bianco et al. 2026 hadronic-BBN dynamical-equilibrium method.
Standard adjoint sensitivity / variational ODE analysis.
