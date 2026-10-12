---
artifact_id: REC9-NC-WATERFALL-DESCRIPTOR-ERROR-LAW-REFEREE-001
bw_ingestion_event_id: ING-20261011-0013
bw_qualification_state: WATERFALL_DESCRIPTOR_REFEREE_REPAIR
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: REFEREE_NO_OWNER_AUTHORITY
archive_mode: PUBLIC_ARTIFACT
sync_state: GITHUB_PENDING_BW_LINK_UPDATE
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# REC9-NC-WATERFALL-DESCRIPTOR-ERROR-LAW-REFEREE-001

> Public-safe mirror of the BW-linked Drive source. BW controls lifecycle/currentness; this GitHub body does not upgrade scientific authority.

REC9 / NC WATERFALL DESCRIPTOR ERROR-LAW REFEREE
RETURN_ID: REC9-NC-WATERFALL-DESCRIPTOR-ERROR-LAW-REFEREE-001
TARGET: NC-XHS3-WATERFALL-DESCRIPTOR-ERROR-LAW-001 + LT3 DRAFT017 §§91–95
VERDICT: PASS_GENERAL_SOURCE-SINK_IDENTITY / FAIL_EXACT_OBJECT_MATCH / REPAIR_DESCRIPTOR_CERTIFICATE
SEVERITY: HIGH for the object-map claim; MEDIUM for downstream DRAFT017 because owner wording already includes some guards.
1. GENERAL LINEAR SOURCE–SINK LAW — PASS WITH EXPLICIT BOUNDARY
For n' = S - D n and a prescribed channel fraction b(t), define
N_exact = integral b D n dt,
N_DE = integral b S dt.
Then exactly:
N_exact - N_DE = -[b n] + integral b' n dt.
Also:
integral D n dt = integral S dt - [n].
Therefore the zero-boundary/full-relaxation version used by NC is correct only when the relevant boundary terms vanish (or cancel). Attach the endpoint condition to BOTH the total-count and directional identities
2. EXACT OBJECT MATCH — FAIL / TYPE MISMATCH
NC's earlier theorem uses D = total destruction/depletion coefficient of the injected hadron population n_h in
n_h' = S_h - D_h n_h.
Its channel fractions b_c partition that same depletion coefficient: D_h = sum_c D_{h,c}.
XH-S3 harvest 018 defines different objects:
- n_h quasi-stable density has depletion denominator containing decay plus collisions weighted by ambient nucleon densities;
- X_n^qs is the equilibrium neutron fraction derived from the p->n / n->p conversion strengths;
- R_h in diagnostic D3 is Gamma_{p->n}^{had}+Gamma_{n->p}^{had}, the induced nucleon interconversion strength.
Therefore the identifications
D_h = R_h
and
b_{p->n} = X_n^qs
are NOT definitional from the cited XH objects.
Same physical dimension is insufficient.
Type firewall:
HADRON POPULATION DEPLETION RATE != NUCLEON INTERCONVERSION RATE.
HADRON-DESTRUCTION BRANCH FRACTION != NUCLEON EQUILIBRIUM FRACTION.
A correct bridge would have to declare separately:
D_h(t,state): total depletion coefficient in the hadron source–sink equation;
k_{p->n}^h, k_{n->p}^h: conversion coefficients;
lambda_{p->n}=k_{p->n}^h n_h and lambda_{n->p}=k_{n->p}^h n_h: induced nucleon rates;
X_n^qs=lambda_{p->n}/(lambda_{p->n}+lambda_{n->p}) for the declared one-species approximation;
and any decay/annihilation/other loss terms entering D_h.
Only after that typing can one ask whether the NC channel partition coincides with the XH reduced descriptor.
3. DESCRIPTOR-ONLY ADMISSION — CIRCULAR AS STATED
The exact error identity contains n_h^exact.
Replacing it by n_h^DE=S_h/D_h before DE is independently admitted cannot by itself certify DE accuracy.
Exact safe form:
|Delta N_c| <= |[b_c n_h]| + integral |dot b_c| n_h^exact dt.
If n_h=n_h^DE+e, then
|Delta N_c| <= |[b_c n_h]| + integral |dot b_c| n_h^DE dt + integral |dot b_c| |e| dt.
The last term requires an independent population-error bound (for example the existing Duhamel/DE error certificate) or an exact solve of the prescribed linear source–sink model.
Thus DESCRIPTOR VALUE + DE SUBSTITUTION != INDEPENDENT ADMISSION CERTIFICATE.
4. MULTI-SPECIES != FEEDBACK AUTOMATICALLY
Several species can produce an effective branching b_eff(t) that remains externally prescribed if their relative abundances/composition histories are externally specified functions of time.
The simple integration-by-parts law then still applies to that prescribed b_eff.
What breaks the simple law is ENDOGENOUS STATE DEPENDENCE / FEEDBACK, not species count itself.
Safe gate:
BRANCHING_PRESCRIBED vs BRANCHING_STATE_DEPENDENT.
Do not state that every multi-species case re-enters a fixed-point regime.
5. LOCAL CONTRACTION != FIXED-POINT EXISTENCE
For T(n)=S/Gamma(n), |d ln Gamma/d ln n|<1 at a fixed point is a local Picard-contraction condition.
Its failure does not imply absence of a finite equilibrium.
Exact counterexample:
Gamma(n)=n^2, S>0.
Then T(n)=S/n^2 has the finite positive fixed point n*=S^(1/3), while |d ln Gamma/d ln n|=2>1 and the naive Picard iteration is locally unstable.
Therefore:
ELASTICITY_GE_1 != NO_FINITE_EQUILIBRIUM.
NONCONTRACTION != NONEXISTENCE.
Existence, uniqueness, physical admissibility and iteration convergence must remain separate.
6. AMPLITUDE SEMANTICS
In the toy linear source–sink host, stronger prescribed depletion can reduce an occupancy-based error bound. But exact occupancy does not generally scale exactly as 1/lambda, and signed channel error need not be monotone when dot b changes sign.
The source-safe statement is only:
AMPLITUDE-INSENSITIVE EQUILIBRIUM RATIO != AMPLITUDE-INSENSITIVE CLOSURE ERROR.
Do not promote the toy near-1/lambda scaling to a source-native theorem.
7. DESCRIPTOR CONTENT GUARD
XH's candidate descriptor is {X_n^qs(T), R_h(T)/R_weak(T)}. It does not by itself supply the source amplitude S_h or the absolute hadron-depletion coefficient D_h needed for S_h/D_h. Those require separately admitted source/background maps.
8. SOURCE-CLASS TRANSFER
Decay-relic waterfall robustness does not automatically transfer to an accelerating PBH Hawking source. PBH_B2_WATERFALL_TRANSFER remains OPEN. The Jung waterfall result is a donor, not a PBH certificate.
9. DRAFT017 DISPOSITION
KEEP: set-membership repair; source-class transfer guard; amplitude-value vs closure-error distinction; BRANCHING_PRESCRIBED vs BRANCHING_STATE_DEPENDENT.
REPAIR §91: EXACT OBJECT MATCH -> CANDIDATE TYPED CORRESPONDENCE pending a source-to-source map.
REPAIR §92: endpoint condition must apply to the total-count equality as well.
REPAIR admission: use exact n_h or an independently bounded DE population error; S_h/D_h substitution alone is not an independent certificate.
REPAIR §94: multiple species do not imply feedback unless composition is endogenous/state-dependent.
REPAIR NC feedback ceiling: elasticity magnitude >=1 means failure of the local contraction certificate, not generic nonexistence of a finite equilibrium.
FINAL STATUS
GENERAL_SOURCE_SINK_ERROR_IDENTITY=PASS_EXACT_WITH_BOUNDARY.
NC_TO_XH_EXACT_OBJECT_MATCH=FAIL_AS_STATED / TYPED_MAP_REQUIRED.
DESCRIPTOR_ONLY_IFF_ADMISSION=FAIL / CIRCULAR_WITHOUT_INDEPENDENT_POPULATION_ERROR_BOUND.
MULTI_SPECIES_GATE=RETYPE_TO_ENDOGENOUS_STATE_DEPENDENCE.
ELASTICITY_LOCAL_CONTRACTION=PASS.
ELASTICITY_GE_1_IMPLIES_NO_EQUILIBRIUM=REJECTED_GENERICALLY.
AMPLITUDE_VALUE_VS_ERROR_DISTINCTION=PASS_WITH_SCALING_CEILING.
PBH_B2_WATERFALL_TRANSFER=OPEN.
REDUCED_WATERFALL_DESCRIPTOR=CANDIDATE / NOT VALIDATED.
NOVELTY_CANDIDATE=NONE.
REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD.
NO CANON / NO EXEC_SIGN / NO NEW TASK / NO NEW FRONT.
STOP after DRAFT017 repairs. Reopen only if a fully typed source-native bridge identifies the NC depletion/channel objects with the XH waterfall descriptor, or a source-matched PBH execution is proposed.
.
