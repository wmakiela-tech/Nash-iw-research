---
artifact_id: MECH-S6-FRONTB-STATE-COUPLED-POPULATION-COMPOSITION-BLOCKER-UPDATE-001
bw_ingestion_event_id: ING-20261010-0079
bw_qualification_state: FRONTB_STATE_COUPLED_POPULATION_BLOCKER
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# MECH-S6-FRONTB-STATE-COUPLED-POPULATION-COMPOSITION-BLOCKER-UPDATE-001

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

MECH-S6 — FRONT B STATE-COUPLED POPULATION COMPOSITION BLOCKER UPDATE
RETURN_ID: MECH-S6-FRONTB-STATE-COUPLED-POPULATION-COMPOSITION-BLOCKER-UPDATE-001
INTEGRATES:
IW_MECH_S5_MT12_B2_PBH_HAWKING_TO_MODULAR_BBN_ADAPTER_CONTRACT_001_20261006
XH-S3-FRONTB-PBH-EARLY-BBN-PRIMAT-ADAPTER-CURRENTNESS-014
REC9-XH-S3-FRONTB-PRIMAT-ADAPTER-REFEREE-001
RESULT_CLASS: EXISTING FRONT UPDATE / SOURCE-CURRENTNESS INTEGRATION / BLOCKER SHARPENING
STATUS: PASS_WITH_SHARPENED_BLOCKER / NO NUMERICAL ENDPOINT / NO NEW TASK
1. CONTROLLING FRONT B STATE
The old broad statement
"MISSING PUBLIC EARLY NONTHERMAL BBN ADAPTER"
is no longer the best description.
Public source landscape now separately provides:
A. direct early PBH hadron/meson/antinucleon n<->p coupling in Wu-Xu;
B. full precision BBN network + custom background + exogenous n<->p rate seam in PRIMAT 0.3.3;
C. extended PBH mass-distribution / Hawking-spectrum machinery at BlackHawk population/spectrum layer;
D. self-consistent PBH thermal/neutrino/full-network donor in Wang/BURST, but without direct meson/hadron plasma coupling.
The smallest surviving load-bearing object is:
STATE-COUPLED POPULATION COMPOSITION
meaning a source-validated composition in which a legal B2 joint carrier drives PBH hadron populations that remain dynamically coupled to the same neutron/proton and abundance state used by the full BBN network.
2. CONTROLLING CARRIER UNCHANGED
Keep the joint comoving-number carrier:
dmu_B2(M_i,t_f).
Do not collapse to a mass-only beta(M) marginal.
Do not impose the Wu-Xu one-mass relation t_f=f(M_i) on the general B2 carrier.
The legal population source remains structurally:
Q_h(t)
=
a(t)^(-3)
∫ chi(t;M_i,t_f)
R_h(M(t;M_i,t_f))
dmu_B2(M_i,t_f).
This source may be linear in dmu_B2 after the common background and trajectory map are fixed.
But:
LINEAR SOURCE SUPERPOSITION
!=
LINEAR SOLUTION SUPERPOSITION
!=
LINEAR BOUND SUPERPOSITION.
All mass bins share H(t), X_n(t), baryon state and hadron depletion feedback.
3. CURRENT WU-XU STATUS
Public Wu-Xu root code directly evolves:
X_n,
pion states,
kaon states,
antiproton,
antineutron,
together with the PBH sector.
Hadron depletion depends on contemporaneous X_n / baryon composition, and hadron densities feed back into dX_n/dt.
Therefore:
WU_XU_DIRECT_EARLY_HADRONIC_NP = PUBLIC / PASS.
But the coupled executor remains:
MONOCHROMATIC / ONE-MASS / MASS-TIED FORMATION.
Therefore:
WU_XU_COUPLED_EXECUTOR != GENERAL B2 JOINT-CARRIER EXECUTOR.
4. CURRENT PRIMAT STATUS
PRIMAT 0.3.3 publicly exposes a custom Background interface including:
T_of_t,
t_of_T,
rhoB_BBN(t),
weak_nTOp(T),
weak_pTOn(T).
Therefore:
PRIMAT_FULL_BBN_CUSTOM_BACKGROUND = PUBLIC / PASS.
PRIMAT_CUSTOM_NP_RATE_INTERFACE = PUBLIC / PASS.
This removes the old claim that there is no public precision-BBN seam for external n<->p rates.
But the stock seam consumes exogenous rate functions.
It does not expose hadron/meson states to the abundance-network RHS.
5. REC9 INTERFACE-SEMANTICS REPAIR
Do NOT argue that the PRIMAT rate hook fails merely because desired rates are time-dependent.
If T(t) is one-to-one on the relevant interval, an externally precomputed rate history r(t) can be reparameterized as r(T).
The exact blocker is STATE DEPENDENCE:
Wu-Xu hadron densities and conversion rates depend on contemporaneous X_n / baryon state.
PRIMAT's stock Background rate methods have no abundance-state argument.
Therefore stock rate injection cannot represent the exact coupled system
X_n
<->
hadron/meson densities
<->
PBH population/background
without:
A. a closure/error theorem that removes the state dependence safely; or
B. deeper network/RHS modification that evolves the hadron states jointly.
6. FALSE COMPOSITION FIREWALL
Do not compute a general B2 endpoint by solving monochromatic cases independently and averaging their final abundances.
Even if Q_h is linear in dmu_B2, the solved network is nonlinear/coupled through:
H(t),
X_n(t),
n_B(t),
meson depletion,
weak conversion,
reaction network evolution.
Therefore:
AVERAGE OF MONOCHROMATIC ENDPOINTS
!=
ENDPOINT OF EXTENDED POPULATION
without a separate theorem.
7. COMPONENT MAP AFTER CURRENTNESS 014
A full BBN network:
PUBLIC.
B custom cosmological background:
PUBLIC.
C external n<->p rate interface:
PUBLIC.
D direct monochromatic PBH hadronic n<->p physics:
PUBLIC.
E BlackHawk extended distribution support:
PUBLIC AT SPECTRUM/POPULATION LAYER.
F general B2 joint carrier inside coupled early-BBN executor:
NOT SOURCE-CLOSED.
G exact hadron-state <-> neutron-fraction feedback inside a full modern BBN network:
NOT SOURCE-CLOSED.
H source-validated no-double-counting composition across thermal / early hadronic / late nonthermal channels:
NOT CLOSED FOR A GENERAL B2 ENDPOINT.
8. LEGAL ENGINEERING ROUTES AND CLAIM CEILINGS
ROUTE A — MONOLITHIC ENLARGED STATE
Full BBN + PBH population + hadron states in one RHS.
Conceptually closest to the exact target.
PUBLIC SOURCE-VALIDATED IMPLEMENTATION = NOT FOUND.
ROUTE B — OUTER FIXED-POINT ITERATION
X_n^(k)(t) -> hadron sector -> effective rates -> BBN -> X_n^(k+1)(t).
Mathematically plausible.
SOURCE-VALIDATED CONVERGENCE / ERROR CERTIFICATE = NOT FOUND.
ROUTE C — PRIMAT EXOGENOUS RATE HOOK
Legal software seam.
Exact only if rate history is independent of evolving abundance state or a valid closure theorem controls the error.
CURRENT STATUS = PARTIAL ADAPTER / NOT EXACTLY CLOSED.
ROUTE D — DIRECT PRIMAT NETWORK MODIFICATION
Likely implementable.
But a new project implementation is not source validation.
It would require independent validation before endpoint use.
9. LATE MODULE STATUS UNCHANGED
Late ACROPOLIS/Xena modules remain support-and-target conditional.
Do not infer:
formal nonzero carrier tail -> late module necessary,
or
dominant mass neighborhood -> late module dispensable.
Late module may be dropped only with:
A. exact source support giving zero contribution; or
B. a target-weighted quantitative error certificate.
Current early state-coupled blocker remains primary.
10. UPDATED VALIDATION LADDER
V0 carrier conservation / unit / Jacobian tests.
V1 monochromatic reduction of B2 population source.
V2 source-energy ledger.
V3 background benchmark in donor-native regime.
V4 full-BBN standard-cosmology round trip.
V5 EM continuous-source benchmark.
V6 state-coupled PBH hadron <-> n/p benchmark against Wu-Xu in its monochromatic native regime.
V7 general B2 population composition benchmark / convergence and no-double-counting audit.
V8 late hadronic spectral-vs-compressed validation if target-relevant.
No B2 abundance vector is claim-grade before the state-coupled composition step is validated.
11. FRONT B STATUS
FORMATION_CARRIER = SOURCE-CLOSED AT dmu_B2 LEVEL.
POPULATION_HAWKING_SOURCE_FORMULA = SOURCE-CLOSED STRUCTURALLY.
WU_XU_DIRECT_EARLY_HADRONIC_NP = PUBLIC / PASS.
WU_XU_COUPLED_EXECUTOR = MONOCHROMATIC / MASS-TIED FORMATION.
PRIMAT_FULL_BBN_CUSTOM_BACKGROUND = PUBLIC / PASS.
PRIMAT_EXOGENOUS_NP_RATE_SEAM = PUBLIC / PASS.
BLACKHAWK_EXTENDED_MASS = PUBLIC AT SPECTRUM/POPULATION LAYER.
EXACT_STATE_COUPLED_PBH_MESON_TO_FULL_BBN = NOT SOURCE-CLOSED.
B2_JOINT_CARRIER_COUPLED_BBN = NOT SOURCE-CLOSED.
STATE_COUPLED_POPULATION_COMPOSITION = LOAD-BEARING BLOCKER.
SOURCE_MATCHED_K_PBH = UNDEFINED.
BIS_PBH_MODEL_SPECIFIC_BOUND = NONE.
FRONT_B_ENDPOINT = UNCHANGED.
NO NUMERICAL RELEASE.
12. PENDING-DEPENDENCY CLOSURE
The historical pending Front B referee dependency is now RESOLVED AS A REVIEW DEPENDENCY.
REC9-XH-S3-FRONTB-PRIMAT-ADAPTER-REFEREE-001:
PASS_WITH_INTERFACE-SEMANTICS_REPAIR.
This does NOT resolve the scientific adapter itself.
Therefore distinguish:
REFEREE_DEPENDENCY = CLOSED.
SCIENTIFIC_ADAPTER_DEPENDENCY = OPEN / BLOCKED.
NUMERICAL_ENDPOINT_DEPENDENCY = NOT ACTIVATED.
13. REOPEN CONDITIONS
STOP on this object unless one of the following appears:
A. source-validated state-coupled PBH hadron + full-BBN adapter;
B. explicit approximation/closure theorem with target-relevant error bound;
C. contradictory public implementation that already closes the coupling;
D. Moderator/owner explicitly authorizes a new implementation programme.
Absent A-D:
do not code a new endpoint,
do not run BBN numerics,
do not derive PBH bounds,
do not tune approximation choices.
14. FIREWALLS
PUBLIC COMPONENTS != VALIDATED COMPOSITION.
CUSTOM RATE HOOK != EXACT STATE-COUPLED FEEDBACK.
TIME DEPENDENCE != THE BLOCKER.
STATE DEPENDENCE = THE CURRENT EXACT INTERFACE BLOCKER.
LINEAR SOURCE SUPERPOSITION != LINEAR ENDPOINT SUPERPOSITION.
BLACKHAWK EXTENDED MASS != B2 COUPLED BBN.
WU-XU MONOCHROMATIC COUPLING != GENERAL B2 CARRIER.
SOFTWARE EXTENSIBILITY != PHYSICAL VALIDITY.
NEW PROJECT CODE != SOURCE VALIDATION.
SEARCH NO MATCH != NONEXISTENCE.
REFEREE PASS != SCIENTIFIC CLOSURE.
15. FINAL DISPOSITION
FRONT_B_BLOCKER_DESCRIPTION = SHARPENED.
OLD BROAD BLOCKER = SUPERSEDED.
NEW CONTROLLING BLOCKER = STATE_COUPLED_POPULATION_COMPOSITION.
REFEREE_DEPENDENCY = CLOSED.
FRONT_B_SCIENTIFIC_ENDPOINT = STILL BLOCKED.
SOURCE_MATCHED_K_PBH = UNDEFINED.
BIS_PBH_MODEL_SPECIFIC_BOUND = NONE.
REV020 = ACTIVE.
REV021 = NOT_CREATED.
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / SCIENCE_FIRST.
16. SOURCE BASIS
IW_MECH_S5_MT12_B2_PBH_HAWKING_TO_MODULAR_BBN_ADAPTER_CONTRACT_001_20261006.
XH-S3-FRONTB-PBH-EARLY-BBN-PRIMAT-ADAPTER-CURRENTNESS-014.
REC9-XH-S3-FRONTB-PRIMAT-ADAPTER-REFEREE-001.
