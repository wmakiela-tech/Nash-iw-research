---
artifact_id: XH-S3-FRONTB-BBN-FUNCTIONAL-RESPONSE-PRIOR-ART-HARVEST-017
bw_ingestion_event_id: ING-20261010-0127
bw_qualification_state: FRONTB_FUNCTIONAL_RESPONSE_PRIOR_ART
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: EXTERNAL_EVIDENCE_NO_AUTHORITY
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# XH-S3-FRONTB-BBN-FUNCTIONAL-RESPONSE-PRIOR-ART-HARVEST-017

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

XH-S3 / FRONT B — BBN FUNCTIONAL-RESPONSE PRIOR-ART HARVEST 017
RETURN_ID
XH-S3-FRONTB-BBN-FUNCTIONAL-RESPONSE-PRIOR-ART-HARVEST-017
RESULT
FUNCTIONAL-RESPONSE METHOD IN BBN = MATURE PRIOR ART.
TIME-LOCAL WEAK n↔p KERNEL = STILL NOT LOCATED AS READY-MADE PUBLIC OBJECT.
PROJECT NOVELTY CANNOT RESIDE IN “USE A FUNCTIONAL RESPONSE KERNEL”.
PROJECT RESIDUE = CHANNEL-SPECIFIC WEAK-RATE KERNEL + PBH/B2 SOURCE-MATCHED TARGET VALIDATION.
FIREWALL
External source/provenance harvest only.
EXISTENCE OF BBN RESPONSE FUNCTIONS != EXISTENCE OF THE REQUIRED WEAK-RATE KERNEL.
EXPANSION-RATE KERNEL != n↔p-RATE KERNEL.
NUCLEAR S-FACTOR KERNEL != HADRONIC INTERCONVERSION KERNEL.
LINEAR-RESPONSE METHOD != GLOBAL VALIDITY FOR LARGE PBH DEVIATIONS.
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO ENDPOINT.
1. 1998 LINEAR SENSITIVITY HOST
SOURCE
[Fiorentini–Lisi–Sarkar–Villante 1998]
They formulate linear propagation of BBN abundance uncertainties through reaction-rate sensitivities and emphasize that different reactions contribute differently to each elemental abundance.
This is a mature precursor for target-specific sensitivity analysis.
However their standard formulation treats energy-independent rate shifts, not an arbitrary local-in-temperature weak-rate perturbation.
2. 2000 FUNCTIONAL SENSITIVITY FUNCTIONS
SOURCE
[Nollett–Burles 2000]
This is direct prior art for the numerical construction proposed in 016.
For each nuclear reaction and nuclide, they define sensitivity functions by:
- perturbing the reaction S-factor in a narrow energy bin;
- rerunning BBN;
- measuring the fractional abundance change as a function of bin location.
They explicitly describe the narrow-bin limit as a functional derivative of the BBN yield with respect to the reaction S-factor.
Thus the generic method:
LOCALIZED INPUT PERTURBATION
-> FULL BBN RERUN
-> TARGET RESPONSE FUNCTION
is mature BBN practice.
3. 2005 FUNCTIONAL RESPONSE TO ARBITRARY TIME-DEPENDENT EXPANSION MODIFICATION
SOURCE
[Bambi–Giannotti–Villante 2005]
They numerically determine element-specific response functions rho_i(eta,T) satisfying, for small fractional expansion-rate perturbations,
delta Y_i
=
2 ∫ rho_i(eta,T) delta H(T) dT/T,
and interpret these as functional-response objects for arbitrary time-dependent changes in the early-universe expansion rate.
The response functions exhibit different time/temperature support for different elements.
Their results explicitly separate:
- weak-freeze-out-sensitive epoch;
- deuterium-bottleneck / synthesis epoch.
This is direct mature prior art for:
TIME-RESOLVED BBN TARGET RESPONSE.
4. CONSEQUENCE FOR 016
The construction proposed in 016:
Gamma_np(T)
-> localized basis perturbation
-> full BBN rerun
-> W_Y(T)
is NOT methodologically novel.
It is a straightforward channel transfer of already mature BBN functional-response practice.
Therefore:
GENERIC_FUNCTIONAL_KERNEL_IDEA = PRIOR_ART_ABSORBED.
The only source-specific question is whether the relevant input channel is:
Gamma_{n->p}(T)
and
Gamma_{p->n}(T),
with the exact background/network contract required for PBH hadronic transfer.
5. WHAT WAS NOT FOUND
Targeted search did NOT locate a published ready-made pair
W_Y^{n->p}(T),
W_Y^{p->n}(T)
for final Yp / D-H under arbitrary localized perturbations of the nucleon interconversion rate histories.
This is a bounded search result:
READY_MADE_WEAK_RATE_KERNEL = NOT LOCATED.
SEARCH_NO_MATCH != NONEXISTENCE.
6. CORRECT PROJECT OBJECT
For a frozen BBN receiver, define local functional response:
W_Y^-(T)
=
delta Y / delta ln Gamma_{n->p}(T),
W_Y^+(T)
=
delta Y / delta ln Gamma_{p->n}(T),
in the chosen baseline/network/normalization/background contract.
Then for small DE/full-history mismatch:
delta Y
≈
∫ [W_Y^-(T) delta lnGamma_-(T)
   + W_Y^+(T) delta lnGamma_+(T)] dlnT.
This object should be typed by:
- BBN code/backend;
- nuclear-rate compilation;
- weak-rate normalization;
- baseline cosmology;
- target Y;
- perturbation basis / binning;
- epsilon;
- local-linearity diagnostic.
7. IMPORTANT CROSS-CHANNEL GUARD
Bambi et al. expansion-response function can show which epochs matter under delta H(T), but cannot be numerically substituted for the weak-rate kernel.
Nollett–Burles nuclear-energy sensitivity functions show functional-derivative methodology, but cannot be substituted for n↔p response.
Therefore:
SAME TARGET
+
SAME TIME WINDOW
!=
SAME INPUT-CHANNEL RESPONSE FUNCTION.
8. TARGET-SPECIFIC EXPECTATION
Prior art strongly supports that:
- He-4 has major sensitivity to neutron-history / weak-processing epochs;
- D/H has substantial later nuclear-network dependence;
- different targets have distinct response supports.
Hence separate kernels remain mandatory:
W_Yp != W_DH.
9. FRONT B VALUE
The project-specific residue is now narrower than in 016.
Not:
“invent a BBN response-kernel method”.
Instead:
construct the MISSING CHANNEL-SPECIFIC kernels for weak n↔p histories,
then combine them with the source-matched DE/full-history PBH discrepancy.
This is exactly the target-transfer certificate required after 015.
10. CHEAPEST COMPUTATIONAL REALIZATION
Use existing mature method:
- log-temperature bins or smooth localized basis b_j;
- perturb one rate direction at a time;
- centered finite differences;
- convergence under epsilon reduction;
- convergence under bin refinement;
- compare linear prediction against a direct finite perturbation.
Need also test mixed perturbations because PBH hadronic physics changes both directions and state-dependent effects can generate nonlinear response.
11. NONLINEARITY / RANGE GUARD
Functional derivatives are local.
If PBH-induced rate changes are large:
- linear kernel becomes only first-order diagnostic;
- use secant/adjoint/nonperturbative target bounds already developed internally;
- direct full-history vs DE BBN comparison remains decisive.
Thus:
KERNEL PASS
!=
GLOBAL PBH TRANSFER PASS.
12. SCIENTIFIC PLACEMENT
MATURE HOSTS:
- linear BBN sensitivity propagation;
- localized nuclear-reaction sensitivity functions;
- arbitrary time-dependent expansion-rate response functions.
PROJECT RESIDUE:
- weak-interconversion-history channel;
- state-aware DE donor transfer;
- PBH/B2 source semantics;
- target-specific error certificate;
- terminal-Hawking overlap.
13. MODEL-USE DISCIPLINE
No external AI model invoked.
The main uncertainty was prior-art existence and was resolved directly by primary literature.
Another model would add little evidence value.
STATUS
BBN_FUNCTIONAL_RESPONSE_METHODOLOGY = MATURE / PRIOR_ART_ABSORBED.
TIME_LOCAL_WEAK_NP_KERNEL = NOT_LOCATED_READY_MADE.
CHANNEL_SPECIFIC_CONSTRUCTION = JUSTIFIED / NOT NOVEL.
FRONT_B_NEXT_OBJECT = SOURCE_MATCHED_WEAK_RATE_KERNEL + DE/FULL TARGET VALIDATION.
SOURCE_MATCHED_K_PBH = UNDEFINED.
NO ENDPOINT RELEASE.
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / SCIENCE_FIRST.
SOURCES
[Fiorentini–Lisi–Sarkar–Villante 1998]
[Nollett–Burles 2000]
[Bambi–Giannotti–Villante 2005]
[Grohs–Fuller 2016]
[Burns 2026 sensitivity atlas]
