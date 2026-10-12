---
artifact_id: MECH-S6-FRONTB-PRIMAT-ADDITIVE-WEAK-RATE-TARGET-KERNEL-CONSTRUCTION-CONTRACT-001
bw_ingestion_event_id: ING-20261010-0130
bw_qualification_state: FRONTB_PRIMAT_WEAK_RATE_KERNEL_CONTRACT
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# MECH-S6-FRONTB-PRIMAT-ADDITIVE-WEAK-RATE-TARGET-KERNEL-CONSTRUCTION-CONTRACT-001

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

MECH-S6 — FRONT B PRIMAT ADDITIVE WEAK-RATE TARGET-KERNEL CONSTRUCTION CONTRACT
RETURN_ID: MECH-S6-FRONTB-PRIMAT-ADDITIVE-WEAK-RATE-TARGET-KERNEL-CONSTRUCTION-CONTRACT-001
IN_REPLY_TO:
XH-S3-FRONTB-BBN-TARGET-SENSITIVITY-WINDOW-HARVEST-016
GEEKY-S10-DRAFT014-FRONTB-NONLINEAR-SECANT-ADJOINT-GRONWALL-TARGET-TRANSFER-CERTIFICATE-001
MECH-S6-FRONTB-TARGET-WEIGHTED-CHANNEL-YIELD-AND-ADJOINT-SENSITIVITY-REPAIR-001
LT3 DRAFT015
RESULT_CLASS: SOURCE-NATIVE KERNEL CONSTRUCTION CONTRACT / NO PBH ENDPOINT / NO NUMERICAL BOUND
STATUS: PUBLIC CONSTRUCTION SEAM PASS / KERNEL NOT YET EXECUTED
1. CONTROLLING GAP
Current Front B no longer lacks:
a full BBN network;
a custom weak-rate software seam;
a target-transfer host;
or a mature late-weak sensitivity motivation.
The remaining object is source-native and operational:
construct a time/temperature-local response kernel for final Y_p and D/H to additional hadronic n<->p rate histories, then validate that the kernel predicts held-out rate-history perturbations over the PBH/B2-relevant regime.
This is not the same as the existing global PRIMAT sensitivity table.
2. PUBLIC PRIMAT SEAM
Current PRIMAT exposes a custom Background interface with compulsory:
T_of_t;
t_of_T;
rhoB_BBN(t);
weak_nTOp(T_K);
weak_pTOn(T_K).
The custom background is a Python-only extension point.
PRIMAT also exposes ordinary sensitivity machinery for:
global multiplicative parameters;
whole nuclear reaction rates;
and additive scalar parameters.
That machinery is useful infrastructure but does not itself provide:
delta Y / delta Gamma_nTOp(T)
or
delta Y / delta Gamma_pTOn(T).
Therefore:
GLOBAL RATE SENSITIVITY != TIME-LOCAL WEAK-RATE FUNCTIONAL DERIVATIVE.
3. SOURCE-NATIVE PERTURBATION OBJECT
For the PBH early-hadronic problem the physical perturbation is additive:
Gamma_nTOp(T)
=
Gamma_nTOp^SM(T)
+
DeltaGamma_nTOp^had(T),
Gamma_pTOn(T)
=
Gamma_pTOn^SM(T)
+
DeltaGamma_pTOn^had(T),
with source-native hadronic increments nonnegative channel by channel when interpreted as additional transition rates.
Therefore the natural target kernel is additive, not fractional.
Define cooling coordinate
ell = ln(T_ref / T),
so ell increases with cosmic time during ordinary BBN cooling.
For target J in {Y_p, D/H}, define kernels K_J^np(ell), K_J^pn(ell) by the local linear-response relation
delta J
approximately
Integral K_J^np(ell) deltaGamma_nTOp(ell) d ell
+
Integral K_J^pn(ell) deltaGamma_pTOn(ell) d ell.
Units:
K has target-units times seconds because deltaGamma has s^-1 and d ell is dimensionless.
4. WHY LOG-RATE PERTURBATIONS ARE NOT THE PRIMARY PBH OBJECT
A multiplicative probe
Gamma -> Gamma exp(epsilon b_j)
measures response to delta ln Gamma.
For PBH hadronic injection, however, the physical object is an extra additive conversion rate.
Using a log-rate kernel would require
delta ln Gamma
approximately
deltaGamma_had / Gamma_SM
in the small-perturbation regime.
This can become badly conditioned where the baseline SM rate is small and also obscures the source semantics.
Therefore:
LOG-RATE KERNEL = useful numerical/diagnostic object.
ADDITIVE RATE KERNEL = preferred source-native PBH object.
5. PHYSICAL PERTURBATION CONE
At zero hadronic injection, physically legal added rates satisfy
deltaGamma_nTOp >= 0,
deltaGamma_pTOn >= 0.
Thus the physically admitted perturbations form a cone, not a symmetric vector space around zero.
A centered finite difference
J(+epsilon b)-J(-epsilon b)
can be mathematically convenient if total rates stay positive, but the negative branch is not a physical hadronic injection.
Therefore distinguish:
NUMERICAL_TANGENT_KERNEL
from
PHYSICAL_ONE_SIDED_RESPONSE.
Firewall:
SYMMETRIC NUMERICAL PROBE != PHYSICAL BIDIRECTIONAL INTERVENTION.
6. ONE-SIDED SOURCE-NATIVE DERIVATIVE
Choose a nonnegative localized basis function b_j(ell), normalized by
Integral b_j(ell) d ell = 1.
Choose a fixed positive rate scale A_ref in s^-1.
For one channel, define the physically legal perturbation
deltaGamma_j(ell)
=
epsilon A_ref b_j(ell),
epsilon > 0.
Let J0 be the unperturbed result.
Define forward response
D_j(epsilon)
=
[J(epsilon)-J0] / [epsilon A_ref].
Under sufficient smoothness,
D_j(epsilon)
=
D_j(0+) + O(epsilon).
A second-order one-sided Richardson estimate is
D_j^R(epsilon)
=
2 D_j(epsilon/2) - D_j(epsilon),
giving
D_j^R
=
D_j(0+) + O(epsilon^2).
This avoids an unphysical negative hadronic perturbation while retaining a convergence-controlled derivative estimate.
7. TWO CHANNELS MUST REMAIN SEPARATE
Construct independently:
K_J^np
for n -> p additions,
and
K_J^pn
for p -> n additions.
Do not impose:
K^pn = -K^np,
detailed-balance symmetry,
or one common weak-rate kernel.
Hadronic meson/antinucleon channels need not perturb both directions in a Standard-Model detailed-balance relation.
Therefore:
SM WEAK DETAILED BALANCE != HADRONIC INJECTION DETAILED BALANCE AUTOMATICALLY.
8. BASIS DESIGN
Use a smooth localized basis in ell=ln(T_ref/T).
Recommended properties:
nonnegative;
compact or rapidly decaying support;
partition-of-unity or explicitly known normalization;
overlapping enough to avoid blind gaps;
not narrower than the numerical/interpolation resolution without a separate convergence test.
Avoid delta-like spikes narrower than the BBN solver's effective temporal/temperature resolution.
A practical hierarchy:
LEVEL 0:
coarse full-BBN scan across the full weak-sensitive interval.
LEVEL 1:
refine where |response| is material.
LEVEL 2:
extra refinement across the late weak-sensitive window around roughly 0.3-0.1 MeV and any PBH terminal-source overlap.
The 0.3-0.1 MeV region is a stress region, not an assumption that sensitivity vanishes elsewhere.
9. WHY THE LATE WINDOW MATTERS
Mature BBN analysis shows that charged-current n<->p processes remain relevant well below the conventional approximately 0.7 MeV freeze-out scale, down near alpha-particle formation around 0.1 MeV.
Therefore:
CONVENTIONAL FREEZE-OUT TEMPERATURE != END OF TARGET SENSITIVITY.
This directly overlaps the Front B concern that Hawking source histories can become rapidly structured late in the relevant epoch.
10. TEMPERATURE-TIME MAP
The PBH source naturally exists as a function of cosmic time.
The PRIMAT weak-rate seam is queried as a function of photon temperature.
For monotonic cooling, the maps are related by:
ell(t)=ln[T_ref/T_gamma(t)].
If a kernel is defined in ell measure:
delta J
=
Integral K_ell(ell) deltaGamma[ell] d ell,
then the corresponding time kernel satisfies
K_t(t)
=
K_ell[ell(t)] d ell/dt,
for integration in increasing cosmic time.
Therefore the exact T(t) history used for the kernel must be the same admitted background used to map the PBH rate history.
BACKGROUND MAP MISMATCH != PURE RATE-HISTORY ERROR.
11. COMMON-BACKGROUND GUARD
A kernel built by perturbing weak rates while holding the cosmological background fixed certifies only the conditional response:
BBN target response GIVEN that background.
If the PBH/B2 model also changes:
H(t);
T_gamma(t);
T_nu(t);
rho_B(t);
entropy;
or the T(t) map,
then total target discrepancy has additional channels.
Thus:
WEAK-RATE KERNEL
!=
FULL PBH BACKGROUND RESPONSE.
A full source-matched error ledger must separate:
RATE_HISTORY_ERROR;
BACKGROUND_HISTORY_ERROR;
SOURCE_ACCOUNTING_ERROR;
NETWORK/MODEL_DISCREPANCY.
12. SAFE PRIMAT IMPLEMENTATION PATTERN
The public interface supports a wrapper Background that delegates:
T_of_t;
t_of_T;
rhoB_BBN;
and optional background quantities
to a frozen baseline background,
while overriding only:
weak_nTOp(T_K)
=
weak_nTOp_base(T_K)
+
deltaGamma_np(T_K),
weak_pTOn(T_K)
=
weak_pTOn_base(T_K)
+
deltaGamma_pn(T_K).
This makes the perturbation semantics explicit.
Important interface facts:
weak_nTOp and weak_pTOn consume photon temperature in Kelvin;
T_of_t and t_of_T use MeV.
The perturbation basis must therefore use an explicit, tested temperature-unit conversion.
CUSTOM BACKGROUND UNIT MISMATCH is a catastrophic silent error class.
13. IDENTITY-WRAPPER CONTROL
Before any kernel run:
construct the wrapper with
deltaGamma_np=deltaGamma_pn=0.
Require the wrapper result to reproduce the same Python-backend baseline within the frozen numerical tolerance.
This tests:
delegation;
units;
temperature mapping;
background semantics;
and output extraction.
Because background= is Python-only, this is the load-bearing local round-trip.
Do not treat C-vs-Python backend parity as a substitute for the wrapper identity test.
14. NUMERICAL FLOOR / STEP-SIZE GATE
For each basis location and target:
evaluate D_j(epsilon) on a decreasing positive epsilon sequence.
Require a stable Richardson plateau above the solver/noise floor.
Failure modes:
epsilon too large -> nonlinear secant contamination;
epsilon too small -> cancellation / solver noise;
basis too narrow -> interpolation/ODE-resolution artifact.
No universal epsilon is promoted here.
The accepted derivative interval must be frozen from convergence, not convenience.
15. BASIS-REFINEMENT GATE
Build the kernel on at least two basis resolutions.
Project the coarse result onto the fine representation or compare predicted responses for common smooth held-out perturbations.
Require target predictions to converge.
POINTWISE KERNEL PLOT CONVERGENCE
is less important than
HELD-OUT TARGET PREDICTION CONVERGENCE.
16. HELD-OUT RECONSTRUCTION TEST
A derivative atlas is not validated merely because each local finite difference converges.
Freeze one or more smooth held-out positive rate histories:
deltaGamma_hold^np(ell),
deltaGamma_hold^pn(ell),
not used in kernel construction.
Kernel prediction:
deltaJ_pred
=
Integral K_J^np deltaGamma_hold^np d ell
+
Integral K_J^pn deltaGamma_hold^pn d ell.
Direct result:
deltaJ_direct
=
J[Gamma_SM + deltaGamma_hold]
-
J0.
Compare:
deltaJ_pred
vs
deltaJ_direct.
This is the cheapest direct test of:
basis completeness;
linear-response regime;
channel combination;
and interpolation.
LOCAL DERIVATIVE CONVERGENCE != HELD-OUT HISTORY PREDICTION.
17. CROSS-CHANNEL NONLINEARITY TEST
To test whether n->p and p->n perturbations can be superposed at the chosen amplitude, define perturbations a and b and compute:
C_ab(epsilon)
=
J[epsilon(a+b)]
-
J[epsilon a]
-
J[epsilon b]
+
J0.
In a linear-response regime:
C_ab = O(epsilon^2).
Monitor:
|C_ab| / |deltaJ_a + deltaJ_b|
where denominator is safely nonzero.
If cross-term is not below the target-error budget:
the first-order kernel is not enough at that amplitude.
18. SOURCE-MATCHED PBH PROJECTION
Once a legal PBH/B2 adapter supplies:
deltaGamma_np^PBH(t),
deltaGamma_pn^PBH(t),
map them through the SAME admitted T_gamma(t) to ell.
Then first-order predicted target shift/error is:
deltaJ_kernel
=
Integral K_J^np(ell) deltaGamma_np^PBH(ell) d ell
+
Integral K_J^pn(ell) deltaGamma_pn^PBH(ell) d ell.
For DE-vs-full validation, use:
deltaGamma
=
Gamma_DE - Gamma_full,
not the total PBH rate itself.
This directly targets the approximation error.
19. LOCAL KERNEL VERSUS FINITE-ERROR CERTIFICATE
The kernel is local/first-order.
Geeky-S10 already supplies the mature finite-error continuation:
FIRST ORDER:
ordinary adjoint / local kernel.
FINITE EXACT TWO-TRAJECTORY:
secant adjoint, but trajectory-pair dependent.
NONPERTURBATIVE SUFFICIENT:
Gronwall envelope, often conservative.
Therefore the source-native workflow is:
local kernel
->
held-out reconstruction
->
if local failure, either reduce perturbation scale or move to secant/full comparison;
->
Gronwall only if its source-matched constants are usable.
No new generic theory is needed.
20. YP AND D/H MUST BE SEPARATE
Construct separate kernels for at least:
J=Y_p
and
J=D/H.
Do not infer D/H safety from a Y_p kernel.
The response can differ in:
temperature support;
sign;
channel weighting;
and nonlinear coupling to the network.
Y_P VALIDATION != D/H VALIDATION.
21. SOURCE ACCOUNTING GUARD
The weak-rate overlay must contain only the rate contribution not already represented elsewhere.
If a PBH module:
adds direct hadronic n<->p conversions
and
also modifies background/thermal state,
the rate perturbation and background perturbation must be partitioned without double counting.
Likewise:
secondary pions generated inside the hadronic-BBN model must not also be pre-included in Q_h if the downstream model regenerates them.
KERNEL LINEARITY DOES NOT REPAIR SOURCE DOUBLE COUNTING.
22. MINIMUM KERNEL RECORD
Record:
BASELINE_MODEL_VERSION;
BASELINE_CONFIG_HASH;
BACKEND=PYTHON;
BACKGROUND_ID;
T_TO_t_MAP_ID;
WEAK_RATE_BASELINE_ID;
TARGET={YP,DH};
RATE_CHANNEL={nTOp,pTOn};
PERTURBATION_TYPE=ADDITIVE;
PERTURBATION_CONE=NONNEGATIVE_PHYSICAL;
COOLING_COORDINATE=ell;
BASIS_FAMILY;
BASIS_WIDTH;
BASIS_NORMALIZATION;
STEP_SEQUENCE;
RICHARDSON_STATUS;
WRAPPER_IDENTITY_STATUS;
BASIS_REFINEMENT_STATUS;
HELDOUT_RECONSTRUCTION_STATUS;
CROSS_CHANNEL_NONLINEARITY_STATUS;
NUMERICAL_PRECISION;
TARGET_TOLERANCE;
SOURCE_MATCHING_STATUS.
23. CHEAPEST FIRST EXECUTION — IF LATER AUTHORIZED
This document does NOT authorize execution.
If execution is later authorized, the cheapest scientifically useful first run is:
A. standard Python baseline;
B. identity wrapper;
C. coarse additive one-sided kernel for Y_p and D/H over the whole weak-sensitive interval;
D. refinement around the response support, especially the late 0.3-0.1 MeV region;
E. one held-out smooth positive perturbation per direction plus one mixed perturbation;
F. stop if step/basis convergence or held-out reconstruction fails.
Do NOT begin with a full PBH/B2 endpoint.
24. CLAIM CEILING
If the kernel construction passes:
we gain a source-native LOCAL target-sensitivity map for the frozen PRIMAT background and declared network.
We do NOT yet gain:
PBH_B2_TO_DE_ADMISSION;
a finite-error PBH closure certificate;
a source-matched K_PBH;
a PBH abundance bound;
or a likelihood.
Those require:
actual PBH DE-vs-full rate-history error;
feedback validity;
source accounting;
background consistency;
and finite-error target validation.
25. FIREWALLS
GLOBAL SENSITIVITY != TIME-LOCAL KERNEL.
LOG-RATE KERNEL != ADDITIVE PBH RATE KERNEL.
SYMMETRIC NUMERICAL TANGENT != PHYSICAL HADRONIC INTERVENTION.
NEGATIVE HADRONIC RATE PERTURBATION != SOURCE-NATIVE PROBE.
CONVENTIONAL FREEZE-OUT != END OF TARGET SENSITIVITY.
TEMPERATURE KERNEL != TIME KERNEL WITHOUT JACOBIAN.
FIXED-BACKGROUND RATE RESPONSE != FULL PBH RESPONSE.
LOCAL DERIVATIVE != FINITE PBH ERROR CERTIFICATE.
LOCAL DERIVATIVE CONVERGENCE != HELD-OUT HISTORY PREDICTION.
Y_P KERNEL != D/H KERNEL.
KERNEL AGREEMENT != SOURCE ACCOUNTING VALIDITY.
PUBLIC SOFTWARE SEAM != SOURCE-MATCHED PHYSICAL ADAPTER.
26. STATUS
PRIMAT_CUSTOM_WEAK_RATE_SEAM = PUBLIC / PASS.
GLOBAL_BBN_SENSITIVITY_INFRASTRUCTURE = PUBLIC / PASS.
READY_MADE_TIME_LOCAL_WEAK_KERNEL = NOT LOCATED.
ADDITIVE_SOURCE_NATIVE_KERNEL_CONTRACT = PASS_DESIGN.
PHYSICAL_ONE_SIDED_RICHARDSON_ROUTE = PASS_DESIGN.
IDENTITY_WRAPPER_CONTROL = REQUIRED.
BASIS_REFINEMENT = REQUIRED.
HELDOUT_RECONSTRUCTION = REQUIRED.
PBH_B2_TO_DE_ADMISSION = OPEN.
TARGET_WEIGHTED_ERROR_CERTIFICATE = OPEN_SOURCE_MATCHED.
REOPEN_FOR_BOUNDED_ADAPTER_ANALYSIS = YES.
REOPEN_FOR_NUMERICAL_BOUND = NO.
SOURCE_MATCHED_K_PBH = UNDEFINED.
BIS_PBH_MODEL_SPECIFIC_BOUND = NONE.
FRONT_B_ENDPOINT = UNCHANGED.
NOVELTY_CANDIDATE = NONE.
REV020 = ACTIVE.
REV021 = NOT_CREATED.
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / SCIENCE_FIRST.
27. SOURCE BASIS
PRIMAT public repository, current 0.3.3 interface:
https://github.com/CyrilPitrou/primat
Custom Background documentation:
https://github.com/CyrilPitrou/primat/blob/master/docs/howto/backgrounds.md
PRIMAT sensitivity documentation:
https://github.com/CyrilPitrou/primat/blob/master/docs/howto/sensitivity.md
Grohs & Fuller 2016:
https://arxiv.org/abs/1607.02797
Burns 2026 BBN sensitivity atlas:
https://arxiv.org/abs/2603.22414
XH-S3-FRONTB-BBN-TARGET-SENSITIVITY-WINDOW-HARVEST-016.
GEEKY-S10-DRAFT014-FRONTB-NONLINEAR-SECANT-ADJOINT-GRONWALL-TARGET-TRANSFER-CERTIFICATE-001.
