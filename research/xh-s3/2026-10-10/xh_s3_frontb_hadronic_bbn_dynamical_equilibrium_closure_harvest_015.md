---
artifact_id: XH-S3-FRONTB-HADRONIC-BBN-DYNAMICAL-EQUILIBRIUM-CLOSURE-HARVEST-015
bw_ingestion_event_id: ING-20261010-0083
bw_qualification_state: FRONTB_DYNAMICAL_EQUILIBRIUM_HARVEST
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: EXTERNAL_EVIDENCE_NO_AUTHORITY
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# XH-S3-FRONTB-HADRONIC-BBN-DYNAMICAL-EQUILIBRIUM-CLOSURE-HARVEST-015

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

XH-S3 / FRONT B — HADRONIC-BBN DYNAMICAL-EQUILIBRIUM CLOSURE HARVEST 015
RETURN_ID
XH-S3-FRONTB-HADRONIC-BBN-DYNAMICAL-EQUILIBRIUM-CLOSURE-HARVEST-015
RESULT
MODERN STATE-AWARE HADRONIC-BBN CLOSURE = FOUND
PBH/B2 TRANSFER = PLAUSIBLE BUT REQUIRES SOURCE-TIMESCALE + TARGET-ERROR CERTIFICATE
PUBLIC 2026 IMPLEMENTATION = NOT LOCATED
FRONT B ENDPOINT = NOT RELEASED
FIREWALL
External source/provenance harvest only.
DELAYED RELIC DECAY != PBH EVAPORATION automatically.
DYNAMICAL-EQUILIBRIUM VALIDATION != UNIVERSAL PBH ERROR BOUND.
GENERIC SOURCE TERM != VALIDATED B2 SOURCE ADAPTER.
PUBLIC PAPER != PUBLIC 2026 CODE.
SOURCE-LEVEL LINEARITY != SOLUTION/BODY-BOUND LINEARITY.
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
1. WHY THIS ROTATION WAS OPENED
Front B controlling blocker after XH-S3 return 014 + Rec9 + Mech-S6:
STATE_COUPLED_POPULATION_COMPOSITION.
Existing public pieces:
- Wu–Xu: direct early PBH pion/kaon/antinucleon n↔p coupling, but one-mass executor.
- BlackHawk: extended mass/population and Hawking spectra.
- PRIMAT: full BBN + custom background + exogenous n↔p seam.
- Wang/BURST: self-consistent thermal/neutrino/full-network treatment without direct hadron-plasma coupling.
Missing object:
legal B2 carrier dμ(M_i,t_f)
→ source histories Q_h(t)
→ state-aware hadronic interconversion
↔ same neutron/proton and BBN abundance state.
This rotation asks whether mature decaying-relic BBN literature already supplies a controlled approximation for exactly this state-aware composition.
2. FOUNDATION HOST — CLASSICAL HADRONIC BBN
SOURCES
[Kawasaki–Kohri–Moroi 2005]
[Jedamzik 2006]
[Kawasaki–Kohri–Moroi–Takaesu 2018]
Long-lived-particle BBN literature already treats injected pions, kaons, nucleons and antinucleons as modifying n/p and, at later times, inducing hadrodisintegration.
Kawasaki–Kohri–Moroi 2005 writes explicit nucleon interconversion terms and averaged per-decay transition numbers K_{N→N'} built from injected hadron multiplicities and interaction probabilities.
Jedamzik 2006 couples nonthermal processes to the thermonuclear fusion reactions.
The 2018 update explicitly includes pion/kaon/nucleon/antinucleon injection, thermalisation, n↔p interconversion and nonthermal nuclear effects.
ANTI-REDISCOVERY
“Hadronic injection modifies n/p and must be coupled to BBN” is mature prior art.
3. MAJOR CURRENTNESS DELTA — BIANCO ET AL. 2026
SOURCE
[Bianco–Frerick–Hufnagel–Schmidt-Hoberg 2026]
arXiv:2605.26824, May 2026:
Improved Big Bang Nucleosynthesis constraints on decaying massive relics.
The work substantially extends AlterAlterBBN and incorporates:
- updated p↔n interconversion rates;
- kaon-induced interconversions;
- pions and antinucleons;
- Pythia 8 hadronisation;
- hadrodisintegration while thermal BBN is still active;
- a dynamical-equilibrium treatment of injected hadron populations;
- matching to ACROPOLIS at late times.
This is the closest mature contemporary host found for the Front B missing state-coupled hadronic layer.
4. GENERIC DYNAMICAL-EQUILIBRIUM CLOSURE
The paper starts from a generic Boltzmann equation
dn/dt + 3H n = S - Γ n,
with arbitrary source S and fast depletion Γ.
When hadronic interaction/decay timescales are much shorter than cosmological evolution and source/background variation, they use
n_de ≈ S/Γ.
Source-native assumptions stated in the paper:
- relevant hadronic processes are much faster than H;
- the relic/background cosmology is essentially unaffected by the additional hadrons;
- source terms and baryon/background quantities vary slowly compared with hadron reactions.
This is important for PBH transfer because the mathematical closure is not intrinsically tied to an exponential relic-decay source.
The source symbol S is generic.
BUT:
generic mathematical source acceptance != PBH source validation.
5. STATE DEPENDENCE IS NOT THROWN AWAY — IT IS SOLVED BY AN INNER FIXED POINT
This directly repairs the concern from Front B return 014.
Bianco et al. do NOT simply pre-tabulate hadronic n↔p rates as functions of T.
At every AlterAlterBBN evolution step they:
1. take current/previous neutron and proton abundances as an initial guess;
2. calculate dynamical-equilibrium kaon and antinucleon densities using those nucleon abundances;
3. build secondary pion source terms and pion equilibrium densities;
4. recompute the nucleon equilibrium required by the total hadronic conversion rates;
5. iterate this map until the neutron/proton abundances converge;
6. use the original network nucleon state plus the converged meson/antinucleon equilibrium state to compute hadronic conversion rates;
7. feed those rates back into the main AlterAlterBBN time evolution.
They report a relative inner-iteration tolerance of 10^-6 in neutron/proton abundances.
Therefore:
EXOGENOUS RATE TABLE
!=
DYNAMICAL-EQUILIBRIUM FIXED-POINT CLOSURE.
The latter is state-aware.
6. VALIDATION AGAINST FULL-TIME HADRON EVOLUTION
Appendix B compares the dynamical-equilibrium approximation against a full time-evolution code for a controlled kaon-injection toy setup.
They match cross sections and disable other processes as needed for a like-for-like comparison.
Reported result:
- good agreement over the relevant BBN temperature window;
- largest asymptotic relative discrepancy a little above 1% for neutron abundance in the longest-lifetime benchmark;
- authors judge rate uncertainties larger than the systematic approximation error in that controlled comparison.
This is the first source located in this Front B chain that supplies an explicit state-aware closure AND a direct validation against full hadron-time evolution.
CLAIM CEILING
This is NOT a universal target-error bound.
It is a controlled implementation consistency check in a restricted decaying-relic setup.
7. WHY THIS MATTERS FOR PBH/B2
For a B2 PBH population, source-level hadron injection can be written schematically
Q_h(t)
=
a(t)^(-3)
∫ χ(t;M_i,t_f)
R_h(M(t;M_i,t_f))
dμ_B2(M_i,t_f).
Once Q_h(t) is constructed on a common self-consistent background, the Bianco et al. closure suggests a lower-dimensional alternative to explicitly evolving every short-lived meson state for every PBH mass bin:
B2 population
→ aggregate Q_h(t)
→ instantaneous/state-aware hadronic fixed point
→ Γ_had^{n→p}(t,Y)
  and Γ_had^{p→n}(t,Y)
→ full BBN network step.
This preserves the key contemporaneous dependence on neutron/proton state that stock PRIMAT weak-rate hooks lack.
IMPORTANT
This is an XH transfer hypothesis/inference.
The source paper does not validate this construction for PBHs or B2 carriers.
8. NEW SHARPER PBH TRANSFER CONDITION
The decaying-relic dynamical-equilibrium argument exposes the real load-bearing condition.
For each relevant injected hadron h, define a source/background variation timescale approximately by
τ_var,h
=
|d ln(S_h/Γ_h)/dt|^(-1)
where meaningful.
The quasi-steady closure requires at least qualitatively
Γ_h^(-1) << H^(-1)
and
Γ_h^(-1) << τ_var,h,
together with convergence of the state-dependent fixed point and legal thermalisation assumptions.
Operational dimensionless proxy:
ε_DE,h
=
Γ_h^(-1)
|d ln(S_h/Γ_h)/dt|.
A necessary adiabaticity-style gate is:
ε_DE,h << 1
over the target-relevant epoch.
This proxy is an XH-derived diagnostic from the source's timescale logic.
It is NOT quoted as a theorem from Bianco et al.
9. PBH-SPECIFIC RISK — END-OF-EVAPORATION SOURCE ACCELERATION
A decaying relic has a smooth exponential source controlled by τ_φ.
A Hawking source can change rapidly as M(t) decreases and T_BH rises, especially close to the final evaporation stage and across particle thresholds.
Therefore:
DECAY-RELIC DE CLOSURE VALID
does NOT automatically imply
PBH DE CLOSURE VALID.
For B2, one must test whether aggregate Q_h(t) remains slow relative to meson depletion throughout the n/p-sensitive window.
If the final Hawking burst occurs in a regime where Γ_h remains vastly faster than Q_h variation, DE may still be excellent.
If not, full hadron-time evolution or a controlled non-equilibrium correction is required.
This is now the CHEAPEST PHYSICS GATE.
10. POPULATION SUPERPOSITION REPAIR
The source-level map
dμ_B2 → Q_h(t)
is linear once the trajectory/background map is fixed.
The hadronic equilibrium/network response after Q_h is constructed is nonlinear/state-dependent.
Therefore the safe architecture is:
INTEGRATE SOURCES FIRST
THEN SOLVE ONE SHARED STATE-AWARE CLOSURE/NETWORK.
Do NOT:
solve each monochromatic PBH population independently through BBN
and average final abundances.
This preserves the Mech-S6 firewall:
LINEAR SOURCE SUPERPOSITION
!=
LINEAR SOLUTION SUPERPOSITION
!=
LINEAR BOUND SUPERPOSITION.
11. RELATION TO WU–XU
WU–XU
- public PBH-specific direct hadron equations;
- explicit meson/antinucleon states;
- exact state feedback within their declared simplified BBN observable;
- monochromatic PBH executor.
BIANCO ET AL. 2026
- generic heavy-decaying-relic injection;
- full AlterAlterBBN nuclear network;
- state-aware dynamical-equilibrium hadron closure;
- direct validation against full hadron-time evolution in a controlled test;
- not PBH/B2 specific.
COMPLEMENTARITY
Wu–Xu supplies PBH source semantics.
Bianco et al. supplies a modern full-network state-aware closure architecture.
This is a materially stronger composition prospect than:
Wu–Xu → pretabulated PRIMAT weak rates.
12. RELATION TO PRIMAT
PRIMAT remains valuable as an independent precision BBN backend and background/rate interface.
However for exact state-dependent hadronic feedback, the Bianco/AlterAlterBBN architecture is closer to the missing object because it performs an inner equilibrium solve using the current nucleon state.
Therefore current architecture ranking for this specific blocker:
A. PUBLIC SOURCE SEMANTICS:
Wu–Xu strongest PBH-specific donor.
B. STATE-AWARE HADRONIC FULL-BBN ARCHITECTURE:
Bianco et al. 2026 / AlterAlterBBN strongest donor found.
C. INDEPENDENT PRECISION FULL-BBN BACKEND:
PRIMAT useful for later cross-checking / background validation, not by itself the exact hadronic seam.
13. PUBLIC CODE STATUS — IMPORTANT NEGATIVE KNOWLEDGE
The public GitHub repository
hep-mh/alteralterbbn
exists and provides AlterAlterBBN v2 infrastructure.
Current GitHub audit:
- default branch: main;
- latest visible commit: 2025-02-27;
- searches on current default branch for meson, kaon, pion, antiproton, interconversion, hadrodisintegration, and dynamical equilibrium return no matching implementation.
The May 2026 PLANCK/EuCAPT conference description says the authors plan to publish the codes enabling the new bounds.
As of this currentness check:
PUBLIC 2026 HADRONIC EXTENSION CODE = NOT LOCATED.
Therefore:
PAPER_METHOD_PUBLIC = YES.
CURRENT PUBLIC EXECUTABLE IMPLEMENTATION OF 2026 EXTENSION = NOT VERIFIED.
SEARCH_NO_MATCH != NONEXISTENCE.
14. DOES THIS SATISFY THE FRONT B REOPEN CONDITION?
Mech-S6 said reopen on:
- source-validated coupled adapter;
- explicit approximation/closure theorem with target error bound;
- contradictory public implementation;
- owner/Moderator implementation authorization.
Current donor satisfies only PART of the second path.
PASS:
- explicit state-aware approximation/closure construction;
- source-native physical timescale rationale;
- full-network integration architecture;
- validation against full-time hadron evolution;
- quantified ~1% neutron-abundance discrepancy in one controlled comparison.
NOT PASS YET:
- PBH/B2-specific validation;
- universal or target-specific error bound for Y_p / D/H over legal B2 class;
- public 2026 executable code;
- proof that PBH Hawking source variation remains inside DE regime;
- source-matched PBH endpoint.
Therefore:
FRONT_B_REOPEN_STATUS =
REOPEN_FOR_BOUNDED_ADAPTER_ANALYSIS
NOT
REOPEN_FOR_NUMERICAL_BOUND.
15. SMALLEST SURVIVING OBJECT — UPDATED AGAIN
After 014:
STATE_COUPLED_POPULATION_COMPOSITION.
After 015:
the state-coupled hadronic closure itself has a mature source-native candidate.
The smallest surviving object is now:
PBH/B2-TO-DYNAMICAL-EQUILIBRIUM ADMISSION + TARGET-ERROR CERTIFICATE.
More explicitly:
1. construct source-valid aggregate PBH Q_h(t) from dμ_B2;
2. test hadron thermalisation/depletion assumptions;
3. test ε_DE,h across target-relevant epoch;
4. implement or reproduce the inner nucleon↔hadron fixed point;
5. compare against a direct PBH hadron-time evolution control at selected adversarial points;
6. propagate closure discrepancy to final target abundances;
7. only then allow source-matched K_PBH / endpoint analysis.
16. CHEAPEST FALSIFIERS
F1 SOURCE-TIMESCALE FAILURE
If ε_DE,h is not small for a load-bearing species/epoch, DE transfer is not certified.
F2 STATE-FIXED-POINT FAILURE
If the inner map does not converge uniquely/stably for legal PBH sources, closure fails or becomes branch-dependent.
F3 TARGET-ERROR FAILURE
If small neutron-history error produces unacceptable Y_p/D/H error, neutron-level validation is insufficient.
F4 POPULATION NONCOMMON-BACKGROUND ERROR
If Q_h is generated from independently evolved bins that do not share the actual common background, B2 source is inconsistent.
F5 PUBLIC-IMPLEMENTATION GAP
If reproduction requires unpublished 2026 code details not recoverable from paper, source closure remains partial.
17. EXTERNAL-MODEL USE POLICY FOR THIS OBJECT
No additional AI/model participant was invoked in this rotation.
Reason:
the source delta was strong, explicit, and directly checkable in primary literature + public repositories.
An extra model audit would currently add coordination burden without a clear unresolved interpretive fork.
A second model would become justified if:
- two plausible PBH transfer formulations survive;
- the DE/PBH timescale argument becomes ambiguous;
- independent code-architecture review is needed before implementation;
- or a claim approaches promotion and benefits from adversarial independent reconstruction.
Thus:
OTHER_MODELS = SELECTIVE HIGH-MARGINAL-VALUE TOOL,
not a routine step.
18. STATUS
CLASSICAL_HADRONIC_BBN_HOST = MATURE.
BIANCO_2026_STATE_AWARE_DE_CLOSURE = PASS / HIGH_RELEVANCE.
FULL_NETWORK_HADRONIC_ARCHITECTURE = SOURCE-DESCRIBED.
CONTROLLED_FULL-TIME_VALIDATION = PASS / RESTRICTED.
PBH_B2_TRANSFER = PLAUSIBLE / NOT VALIDATED.
PBH_SOURCE_ADIABATICITY_GATE = REQUIRED.
PUBLIC_2026_CODE = NOT LOCATED.
STATE_COUPLED_POPULATION_COMPOSITION = NARROWED.
NEW_CONTROLLING_BLOCKER =
PBH_B2_TO_DE_ADMISSION_PLUS_TARGET_ERROR_CERTIFICATE.
SOURCE_MATCHED_K_PBH = UNDEFINED.
BIS_PBH_MODEL_SPECIFIC_BOUND = NONE.
FRONT_B_ENDPOINT = UNCHANGED.
REOPEN = BOUNDED_ADAPTER_ANALYSIS ONLY.
NO NUMERICAL RELEASE.
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / SCIENCE_FIRST.
SOURCES
[Kawasaki–Kohri–Moroi 2005]
[Jedamzik 2006]
[Kawasaki–Kohri–Moroi–Takaesu 2018]
[Bianco–Frerick–Hufnagel–Schmidt-Hoberg 2026]
[PLANCK2026 Frerick presentation]
[AlterAlterBBN public GitHub]
[Wu–Xu PBH GitHub]
[PRIMAT public GitHub]
