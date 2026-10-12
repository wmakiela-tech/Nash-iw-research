---
artifact_id: MECH-S6-FRONTB-DYNAMICAL-EQUILIBRIUM-TRACKING-CONTRACTION-AND-TARGET-ERROR-GATE-001
bw_ingestion_event_id: ING-20261010-0093
bw_qualification_state: FRONTB_DE_TRACKING_CONTRACTION_TARGET_ERROR
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# MECH-S6-FRONTB-DYNAMICAL-EQUILIBRIUM-TRACKING-CONTRACTION-AND-TARGET-ERROR-GATE-001

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

MECH-S6 — FRONT B DYNAMICAL-EQUILIBRIUM TRACKING / CONTRACTION / TARGET-ERROR GATE
RETURN_ID: MECH-S6-FRONTB-DYNAMICAL-EQUILIBRIUM-TRACKING-CONTRACTION-AND-TARGET-ERROR-GATE-001
IN_REPLY_TO:
XH-S3-FRONTB-HADRONIC-BBN-DYNAMICAL-EQUILIBRIUM-CLOSURE-HARVEST-015
PRF10-FRONTB-STRUCTURED-POPULATION-FOUNDATION-SOURCE-MAP-001
MECH-S6-FRONTB-STATE-COUPLED-POPULATION-COMPOSITION-BLOCKER-UPDATE-001
RESULT_CLASS: BOUNDED ADAPTER ANALYSIS / EXACT FAST-SLOW ERROR GATE / FIXED-POINT ADMISSION / NO ENDPOINT NUMERICS
STATUS: PASS_EXACT_FOR_GENERIC_SCALAR_FAST_SUBSYSTEM / SOURCE-NATIVE PBH TRANSFER NOT YET VALIDATED
1. CONTROLLING DELTA
XH-S3 identified a highly relevant mature source-native closure:
Bianco, Frerick, Hufnagel, Schmidt-Hoberg (2026) use a state-aware dynamical-equilibrium treatment for hadronic BBN, retaining dependence on the nucleon state through an inner iterative equilibrium construction and validating it against full hadron-time evolution in controlled decay-relic benchmarks.
This materially reopens Front B for BOUNDED ADAPTER ANALYSIS.
It does NOT yet reopen:
PBH endpoint numerics,
source-matched K_PBH,
BIS PBH bound,
or likelihood construction.
The smallest question is now:
WHEN DOES A B2 PBH HADRON SOURCE TRACK THE DYNAMICAL-EQUILIBRIUM MANIFOLD WITH A TARGET-RELEVANT ERROR CERTIFICATE?
2. EXACT SCALAR FAST-SUBSYSTEM THEOREM
Consider one source-native fast hadron density n(t) satisfying
dn/dt = S(t) - Lambda(t) n(t),
with
Lambda(t) >= lambda_0 > 0.
Define the instantaneous dynamical-equilibrium value
n_*(t) = S(t)/Lambda(t).
Define the tracking error
e(t) = n(t)-n_*(t).
Then exactly:
de/dt + Lambda(t)e = -dn_*/dt.
Therefore, by variation of constants,
e(t)
=
exp[-Integral_{t0}^{t} Lambda(u)du] e(t0)
-
Integral_{t0}^{t}
exp[-Integral_{s}^{t} Lambda(u)du]
(dn_*/ds)
ds.
Hence the exact bound
|e(t)|
<=
exp[-lambda_0(t-t0)] |e(t0)|
+
Integral_{t0}^{t}
exp[-lambda_0(t-s)]
|dn_*/ds|
ds.
In particular,
|e(t)|
<=
exp[-lambda_0(t-t0)] |e(t0)|
+
(1/lambda_0)
sup_{s in [t0,t]} |dn_*/ds|.
This is a rigorous sufficient tracking certificate for the scalar linear fast subsystem.
3. DIMENSIONLESS DE TRACKING PARAMETER
When n_*(t)>0 on the target-relevant interval, define
epsilon_track(t)
=
|d ln n_*/dt| / Lambda(t)
=
Lambda(t)^(-1)
|d/dt ln[S(t)/Lambda(t)]|.
If
epsilon_track << 1
and the initial transient has decayed, the equilibrium point moves slowly compared with fast relaxation.
This is the correct local dimensionless object for the scalar equation.
It sharpens the XH diagnostic
Gamma_h^(-1) |d ln(S_h/Gamma_h)/dt|
by making explicit that the relevant relaxation coefficient and variable convention must be source-native.
4. PHYSICAL-DENSITY VERSUS COMOVING-DENSITY SEMANTICS
If the source-native equation for a PHYSICAL number density is
dn/dt + 3H n = S - Gamma n,
then
Lambda = Gamma + 3H
and the instantaneous algebraic equilibrium of that exact scalar equation is
n_* = S/(Gamma+3H).
If instead one evolves the COMOVING density
N=a^3 n,
then
dN/dt = a^3 S - Gamma N,
and the fast coefficient is Gamma.
Therefore:
DYNAMICAL-EQUILIBRIUM SMALL PARAMETER IS VARIABLE-CONVENTION DEPENDENT.
Using S/Gamma for a physical density requires an additional approximation such as Gamma >> H, or an equivalent quantified source-native argument.
Do not mix physical-density and comoving-density closures.
5. PBH-SPECIFIC SOURCE TIMESCALE
For B2:
Q_h(t)
=
a(t)^(-3)
Integral chi(t;M_i,t_f)
R_h[M(t;M_i,t_f)]
dmu_B2(M_i,t_f).
The DE admission variable is not merely the Hubble timescale.
The aggregate source can change rapidly because:
PBH mass evolves;
Hawking temperature accelerates near final evaporation;
species thresholds/hadronization kernels change with mass;
carrier nodes terminate at different evaporation times;
the active support chi changes.
Therefore define a source timescale, where legal:
tau_Q,h
=
|d ln Q_h/dt|^(-1).
A necessary practical stress test is whether
Lambda_h tau_Q,h >> 1
over the target-relevant epoch.
But the exact scalar certificate should use
d ln(Q_h/Lambda_h)/dt,
not Q_h alone.
SMOOTH MASS DISTRIBUTION != SLOW AGGREGATE SOURCE AUTOMATICALLY.
6. INITIAL-LAYER GUARD
Even with epsilon_track small later, a DE approximation can fail immediately after:
formation;
threshold activation;
sudden injection onset;
rapid source turn-off;
or a sharp evaporation feature.
The exact transient term is
exp[-Integral Lambda] e(t0).
Therefore any DE implementation must declare either:
A. INITIALIZED_ON_DE_MANIFOLD;
B. INITIAL_TRANSIENT_RESOLVED;
C. INITIAL_TRANSIENT_BOUNDED_BELOW_TARGET_TOLERANCE;
D. UNRESOLVED.
FAST LATE TRACKING != VALID INITIAL CONDITION.
7. INNER STATE-AWARE FIXED POINT
Bianco et al. do not merely pretabulate hadronic rates.
They iterate the hadron/nucleon equilibrium state until a consistent state is reached, then feed the resulting interconversion rates into the BBN evolution.
Abstract that inner step at fixed time t as
x_{m+1} = F_t(x_m),
where x can be the neutron fraction or a finite vector of equilibrium nucleon variables.
If F_t maps an admitted closed domain D into itself and is a contraction:
||F_t(x)-F_t(y)|| <= kappa ||x-y||
with
0 <= kappa < 1,
then Banach's fixed-point theorem gives:
a unique inner fixed point x_*(t);
convergence from every starting point in D;
and an exact iteration-error certificate.
8. ITERATION-TOLERANCE DOES NOT EQUAL FIXED-POINT ERROR AUTOMATICALLY
For a contraction with factor kappa:
||x_m-x_*||
<=
[kappa/(1-kappa)]
||x_m-x_{m-1}||.
Therefore a numerical stopping rule such as
relative iterate change < 1e-6
is NOT by itself a 1e-6 scientific fixed-point error certificate.
Its meaning depends on kappa.
If kappa is near 1, the error amplification
kappa/(1-kappa)
can be large.
Thus:
INNER TOLERANCE != PHYSICAL CLOSURE ERROR.
ITERATION CONVERGENCE OBSERVED != UNIFORM CONTRACTION CERTIFIED.
The 1e-6 criterion reported by Bianco et al. is a numerical convergence choice in their implementation; it should not be exported to PBH B2 as a universal target-error guarantee.
9. PERTURBED-MAP ERROR AMPLIFICATION
Suppose the exact source-native inner map is F and an approximate implementation uses F_tilde with
sup_{x in D} ||F_tilde(x)-F(x)|| <= delta,
while F is a contraction with factor kappa<1.
If x_* is the exact fixed point and x_tilde is a fixed point of F_tilde in D, then
||x_tilde-x_*||
<=
delta/(1-kappa).
Therefore:
source approximation error,
cross-section error,
population quadrature error,
or closure approximation
can be amplified by the fixed-point geometry.
SMALL LOCAL KERNEL ERROR != SMALL EQUILIBRIUM-STATE ERROR without a contraction margin.
10. MOVING FIXED-POINT CONDITIONING
If F_t is differentiable and
x_*(t)=F_t[x_*(t)],
then formally
[I-D_x F_t] dx_*/dt = partial_t F_t.
If
||D_x F_t|| <= kappa <1,
then
||dx_*/dt||
<=
||partial_t F_t||/(1-kappa).
Thus a PBH source whose forcing changes rapidly can make the consistent equilibrium state move rapidly even if the fixed point exists uniquely at each instant.
The same margin 1-kappa controls sensitivity to:
time variation;
source error;
and numerical map perturbations.
CONVERGENT INNER FIXED POINT != SLOWLY MOVING FIXED POINT.
11. TARGET-ERROR PROPAGATION TO n<->p RATES
Hadronic conversion rates have the source-native form
Gamma_had
=
sum_h c_h(t) n_h(t),
with c_h representing the relevant thermally averaged reaction coefficient.
If n_h^DE is used instead of full n_h, then
|delta Gamma_had|
<=
sum_h |c_h| |n_h-n_h^DE|.
The fast-subsystem bound therefore converts directly into an interconversion-rate error bound once source-native c_h are frozen.
This is the first required bridge from DE tracking to BBN target error.
12. TARGET ERROR REQUIRES A SECOND SENSITIVITY LAYER
Let Y denote the full abundance state with dynamics
dY/dt = f[Y,t,Gamma_had(t)].
For two histories differing by delta Gamma, suppose over the admitted regime:
||partial f/partial Y|| <= L_Y(t)
and
||partial f/partial Gamma|| <= L_Gamma(t).
Then a standard Gronwall perturbation bound gives schematically
||delta Y(T)||
<=
Integral_{t0}^{T}
exp[Integral_s^T L_Y(u)du]
L_Gamma(s)
|delta Gamma(s)|
ds.
Therefore a claim-grade PBH DE approximation needs TWO layers:
LAYER 1:
hadron-state tracking error.
LAYER 2:
target sensitivity of Y_p, D/H, or another declared abundance endpoint to the induced rate error.
A small hadron-density error is not automatically a small abundance error.
13. SOURCE PAPER VALIDATION CEILING
Bianco et al. report good DE agreement with full-time hadron evolution in controlled kaon toy benchmarks and find the largest asymptotic relative neutron-abundance discrepancy a little above 1% in the longest-lifetime case they show.
But their Appendix B comparison is explicitly a consistency check under matched simplified conditions; they disable weak/fusion processes for comparability and state that it is not a physical benchmark point.
Therefore:
BIANCO APPENDIX-B VALIDATION = HIGHLY RELEVANT DONOR.
BIANCO APPENDIX-B VALIDATION != UNIVERSAL PBH ERROR BOUND.
DECAY-RELIC VALIDATION != PBH FINAL-EVAPORATION VALIDATION.
The source itself supports state-aware DE as a serious mature method, not automatic B2 transfer. The paper describes iterative state-aware meson/nucleon equilibrium and validates it against direct hadron-time evolution in restricted benchmarks. 
14. FRONT B ADMISSION CONTRACT
For each load-bearing hadronic species h record:
FAST_VARIABLE_CONVENTION =
PHYSICAL_DENSITY
| COMOVING_DENSITY
| OTHER.
SOURCE_HISTORY =
Q_h(t) or legal equivalent.
RELAXATION_RATE =
Lambda_h(t).
DE_TARGET =
n_h^*(t).
TRACKING_PARAMETER =
epsilon_track,h(t).
INITIAL_LAYER_STATUS.
INNER_FIXED_POINT_MAP =
F_t.
CONTRACTION_FACTOR_BOUND =
kappa(t) or UNRESOLVED.
ITERATION_STOPPING_RULE.
FIXED_POINT_ERROR_BOUND.
RATE_ERROR_BOUND =
delta Gamma_n_to_p / delta Gamma_p_to_n.
TARGET_SENSITIVITY_BOUND =
delta Y_p / delta(D/H) / declared endpoint.
15. CHEAPEST B2 DE FALSIFIER
Before any full BBN endpoint run:
1. Construct the aggregate B2 Q_h(t) with no endpoint averaging.
2. Freeze physical/comoving density convention.
3. Compute or bound Lambda_h.
4. Evaluate epsilon_track,h across the target-relevant epoch.
5. Explicitly inspect evaporation endpoints and threshold crossings.
6. For the state-aware inner map, estimate a local/global contraction margin kappa.
7. Convert the stopping tolerance into a fixed-point-error bound.
8. Convert hadron-state error into n<->p rate error.
9. Only if that rate error is target-safe under a declared abundance sensitivity bound may DE be admitted for endpoint use.
Failure at steps 4-7 kills the approximation before an expensive abundance/likelihood pipeline.
16. RELATION TO PRF STRUCTURED-POPULATION FOUNDATION
PRF correctly reframes Front B as:
distributed PBH population
->
integrated source outputs
->
hadron kinetic state
<->
common neutron/baryon/abundance environment
->
light-element endpoint.
The present result does NOT supply the exact finite-dimensional structured-population closure sought by PRF.
Instead, it isolates a source-native approximate reduction route:
KEEP full B2 population integration in Q_h(t);
reduce only the fast hadron kinetic variables through a DE manifold;
retain one shared abundance environment;
certify target error.
This avoids the illegal shortcut:
independent monochromatic endpoint averaging.
17. WHAT WOULD COUNT AS A REAL FRONT B ADVANCE
A material advance now requires one of:
A. PBH B2 source histories Q_h with epsilon_track uniformly small in the relevant epoch plus an admitted initial-layer treatment;
B. a source-native contraction/error certificate for the Bianco-style inner map under PBH forcing;
C. a direct comparison of B2/PBH DE against full hadron-time evolution that covers the Hawking rapid-variation regime;
D. a source-supported target-sensitivity bound showing the residual DE error is below the declared Y_p / D/H tolerance.
Without one of A-D:
PBH_B2_TO_DYNAMICAL_EQUILIBRIUM_ADMISSION remains unresolved.
18. FIREWALLS
TIMESCALE SEPARATION != TARGET ERROR CERTIFICATE.
Gamma >> H != COMPLETE DE VALIDATION.
S/Gamma != UNIVERSAL EQUILIBRIUM FORM WITHOUT VARIABLE CONVENTION.
INNER ITERATION TOLERANCE != FIXED-POINT ERROR.
FIXED-POINT EXISTENCE != FAST TRACKING.
FIXED-POINT CONVERGENCE != UNIFORM CONTRACTION.
SMALL HADRON ERROR != SMALL ABUNDANCE ERROR.
DECAY-RELIC DE VALID != PBH DE VALID.
LINEAR B2 SOURCE INTEGRATION != LINEAR ABUNDANCE ENDPOINT.
MATURE QSSA HOST != SOURCE-NATIVE PBH ADMISSION.
PUBLIC PAPER METHOD != PUBLIC EXECUTABLE.
APPROXIMATION SUCCESS != SOURCE_MATCHED K_PBH.
19. STATUS
BIANCO_2026_STATE_AWARE_DE_CLOSURE = ACCEPTED AS HIGH-RELEVANCE MATURE HOST.
SCALAR_FAST_TRACKING_ERROR_BOUND = PASS_EXACT.
INNER_FIXED_POINT_CONTRACTION_GATE = PASS_EXACT.
ITERATION_TOLERANCE_TO_ERROR_CONVERSION = PASS_EXACT CONDITIONAL ON kappa.
TARGET_ERROR_PROPAGATION_FORM = PASS_GENERIC / SOURCE CONSTANTS UNRESOLVED.
PBH_B2_TO_DYNAMICAL_EQUILIBRIUM_ADMISSION = OPEN / NOT YET PASSED.
REOPEN_FOR_BOUNDED_ADAPTER_ANALYSIS = YES.
REOPEN_FOR_NUMERICAL_BOUND = NO.
SOURCE_MATCHED_K_PBH = UNDEFINED.
BIS_PBH_MODEL_SPECIFIC_BOUND = NONE.
FRONT_B_ENDPOINT = UNCHANGED.
NOVELTY_CANDIDATE = NONE.
REV020 = ACTIVE.
REV021 = NOT_CREATED.
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / SCIENCE_FIRST.
20. SOURCE BASIS
Bianco, Frerick, Hufnagel, Schmidt-Hoberg — Improved Big Bang Nucleosynthesis constraints on decaying massive relics — arXiv:2605.26824 (2026).
XH-S3-FRONTB-HADRONIC-BBN-DYNAMICAL-EQUILIBRIUM-CLOSURE-HARVEST-015.
PRF10-FRONTB-STRUCTURED-POPULATION-FOUNDATION-SOURCE-MAP-001.
MECH-S6-FRONTB-STATE-COUPLED-POPULATION-COMPOSITION-BLOCKER-UPDATE-001.
Generic mature host:
Tikhonov/Fenichel fast-slow reduction, quasi-steady-state approximation, contraction mapping, ODE perturbation/Gronwall stability.
