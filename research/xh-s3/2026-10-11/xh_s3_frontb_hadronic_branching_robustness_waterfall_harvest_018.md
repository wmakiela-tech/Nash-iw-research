---
artifact_id: XH-S3-FRONTB-HADRONIC-BRANCHING-ROBUSTNESS-WATERFALL-HARVEST-018
bw_ingestion_event_id: ING-20261011-0004
bw_qualification_state: FRONTB_WATERFALL_HARVEST
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: EXTERNAL_EVIDENCE_NO_AUTHORITY
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# XH-S3-FRONTB-HADRONIC-BRANCHING-ROBUSTNESS-WATERFALL-HARVEST-018

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

XH-S3 / FRONT B — HADRONIC BRANCHING ROBUSTNESS / WATERFALL HARVEST 018
RETURN_ID
XH-S3-FRONTB-HADRONIC-BRANCHING-ROBUSTNESS-WATERFALL-HARVEST-018
RESULT
GENERAL HADRON-YIELD / CROSS-SECTION AMPLITUDE UNCERTAINTY = OFTEN WEAKLY LOAD-BEARING FOR EARLY Yp-LIFETIME BOUNDS IN A MATURE HADRONIC-BBN HOST.
DIRECTIONAL p->n vs n->p CROSS-SECTION RATIO / QUASI-STABLE X_n = LOAD-BEARING.
MULTI-HADRON COMPOSITION CAN COMPENSATE IN X_n^{qs} WHILE ADDING CONSTRUCTIVELY IN WATERFALL TIMING.
PBH/B2 TRANSFER = NOT AUTOMATIC.
FRONT B RESIDUAL = DIRECTIONAL-BRANCHING + TARGET/ENDPOINT SEMANTICS, NOT RAW TOTAL HADRON AMPLITUDE ALONE.
FIREWALL
Heavy-QCD-axion lifetime robustness != PBH abundance-bound robustness.
Logarithmic dependence of one lifetime bound != universal BBN insensitivity.
Overall cross-section rescaling != directional cross-section distortion.
Quasi-stable neutron fraction != full final abundance target.
No canon / no EXEC sign / no novelty / no PBH endpoint.
1. MATURE SOURCE
[Jung–Okui–Tobioka–Wang 2026]
New Bounds on Heavy QCD Axions from Big Bang Nucleosynthesis
Phys. Rev. D 113 (2026) 055002
arXiv:2510.23695v2.
The paper develops a semi-analytic “waterfall” picture for hadronically modified n/p during BBN and explicitly studies robustness to hadron yields, branching fractions, cross sections and initial relic abundance.
2. QUASI-STABLE HADRON DENSITY
For one hadron h, the quasi-stable density is approximated by
n_h ≃ N_{a->h} Γ_a n_a /
      [Γ_tilde_h + <<nh>> n_n + <<ph>> n_p].
The hadronic contribution to n<->p therefore depends on:
- source amplitude N_{a->h} Γ_a n_a;
- total depletion;
- direction-changing pieces <<nh>>_c and <<ph>>_c;
- current neutron/proton fractions.
This is the same structural regime that motivated the DE closure donor 015.
3. DIRECTIONAL RATIO SETS THE QUASI-STABLE NEUTRON FRACTION
When hadronic interconversions dominate weak rates, the source obtains
X_n^{qs}
≃
<<p h>>_c /
(<<p h>>_c + <<n h>>_c).
Thus the quasi-stable neutron fraction is controlled primarily by the RATIO of the p->n and n->p conversion strengths, not by the absolute hadron density.
For nearly isospin-symmetric pion/baryon channels, X_n^{qs} ≃ 1/2.
Kaons need not obey this symmetry and can shift X_n^{qs} substantially.
This is a direct source-native explanation for why:
OVERALL AMPLITUDE
and
DIRECTIONAL BRANCHING
play different epistemic roles.
4. WATERFALL TIMING
As the decaying source is exponentially depleted, the hadronic rate eventually falls to the weak n<->p rate.
The paper defines a waterfall time t_wf from the crossing
Γ_weak,n->p + Γ_weak,p->n
≈
sum_h [(<<nh>>_c + <<ph>>_c) n_h].
For one species the semi-analytic t_wf depends LOGARITHMICALLY on:
- initial abundance;
- hadron yield N_{a->h};
- effective conversion/depletion cross-section combination.
This logarithm has a large baseline argument (~15–18 in their benchmark regime), so order-unity changes in yield/cross-section amplitude shift t_wf only modestly.
5. WHY THE LIFETIME BOUND IS ROBUST IN THAT HOST
Their semi-analytic lifetime bound contains the source/cross-section uncertainty mainly inside logarithms.
A simplified expression is of the form
tau_a ~ 0.02 s / [1 + O(1/18) log N_{a->h}],
and the more complete Eq. (7.13) preserves the same logarithmic structure.
Numerical/source checks reported:
- factor 2 change in all hadron yields N_{a->h} changes final neutron excess substantially (~20%-level) but shifts the lifetime upper bound by only ~4%;
- factor ~10 change in initial abundance changes the lifetime bound only ~10% in the sensitive low-mass region;
- factor 2 change in a KL directional conversion cross section changes the neutron excess by ~7%, but the lifetime bound by ~1%;
- common overall scaling of all hadronic cross sections has nearly zero effect when decay-width terms are negligible.
Therefore:
LIFETIME_BOUND_ROBUSTNESS
can coexist with
NONTRIVIAL X_n HISTORY SENSITIVITY.
6. WHAT IS ACTUALLY LOAD-BEARING
The paper states explicitly that what matters is the RATIO between p->n and n->p cross sections.
Overall multiplication of all hadronic cross sections approximately cancels between:
- the quasi-stable neutron ratio;
- hadron depletion;
- waterfall condition.
But changing one directional rate changes:
A. X_n^{qs};
B. waterfall timing;
C. final relaxed neutron excess.
Thus the relevant Front B object is not a scalar “hadronic cross-section uncertainty”.
It is at minimum a directional 2-channel object:
C_h(T,state) =
{Γ_h,p->n, Γ_h,n->p}
or equivalently:
- total directional strength;
- asymmetry / branching ratio.
7. MULTI-HADRON NONTRIVIALITY
The paper gives for multiple hadrons
X_n^{qs}
~ [Σ_h <<p h>>_c n_h] /
   [Σ_h (<<p h>>_c + <<n h>>_c) n_h].
Important source-native observation:
multiple hadrons can COMPENSATE in X_n^{qs}; e.g. combined KL and K± equilibrium ratio lies between their individual values.
But their contributions ADD CONSTRUCTIVELY in the waterfall-rate crossing.
Therefore:
MULTI-HADRON COMPOSITION
has two distinct effects:
A DIRECTIONAL EQUILIBRIUM EFFECT
can compensate.
B TOTAL RELAXATION/WATERFALL STRENGTH
adds.
This is directly relevant to PBH Hawking sources where pion/kaon/antinucleon multiplicities evolve together.
8. BIanco 2026 CONSISTENCY
The Bianco et al. donor independently shows:
- pion p->n/n->p dominance depends strongly on ambient n/p target abundances;
- temperature-dependent thermal cross sections are used;
- K- and KL channels have strongly different effective p->n and n->p cross sections;
- secondary pion source composition changes with temperature;
- at late stages kaon DECAYS become relatively more important because nuclear/annihilation rates drop with temperature;
- charged-kaon asymmetry is the largest asymmetry source in their benchmark.
This supports the same conclusion:
the important residual is directional/channel composition as a function of T and state, not merely the total number of injected hadrons.
9. CORRECTION TO THE PREVIOUS “TERMINAL RAPIDITY” EMPHASIS
M12 already corrected the claim that rapid terminal source variation alone must produce integrated-channel error.
The current external source picture reinforces that correction.
For the early-Yp / waterfall regime:
a rapidly changing source amplitude may have surprisingly small impact on the inferred LIFETIME BOUND because the crossing time depends logarithmically on amplitude.
What remains load-bearing:
- directional conversion ratio;
- threshold/channel openings;
- state dependence of branching/depletion;
- whether the target is a lifetime bound, an abundance bound, Yp itself, D/H, or a PBH population parameter.
Thus:
RAPID SOURCE != LARGE TARGET ERROR AUTOMATICALLY.
10. PBH/B2 TRANSFER CEILING
This robustness cannot be copied directly to PBH.
Reasons:
A TARGET DIFFERENCE
Jung et al. constrain an exponentially decaying PARTICLE LIFETIME.
Front B may ultimately constrain PBH abundance / carrier / mass-function parameters.
A logarithmic lifetime response can correspond to a much less robust abundance response.
B SOURCE SHAPE
PBH Hawking source is not simple exponential decay and can have thresholds and terminal acceleration.
C MULTI-TRAJECTORY POPULATION
B2 uses dmu(M_i,t_f), with a superposed species source and shared BBN state.
D BACKGROUND COUPLING
PBH energy density / entropy can alter H(T), T(t), and carrier history.
E HADRONIZATION EVOLUTION
PBH temperature evolves, so hadron species multiplicities and directional channel composition can change with time.
Therefore:
JUNG WATERFALL ROBUSTNESS = MATURE DONOR / NOT PBH CERTIFICATE.
11. NEW SHARP FRONT B TRANSFER QUESTION
The source-native test should now ask:
Does the PBH/B2 source remain inside a regime where the TARGET depends mostly on:
1. one quasi-stable directional ratio X_n^{qs}(T),
2. one waterfall/crossover functional,
with only logarithmic sensitivity to the overall hadronic amplitude?
If YES:
a reduced semi-analytic PBH adapter may be possible.
If NO:
the full weak-rate-history kernel / DE-vs-full target validation remains required.
This is a stronger and cheaper discriminator than blindly constructing a dense kernel everywhere.
12. CHEAPEST SOURCE-NATIVE DIAGNOSTICS
Before any full kernel execution, compute from one frozen PBH/B2 source:
D1 directional asymmetry
A_h(T) =
[Γ_{p->n}^{had}(T)-Γ_{n->p}^{had}(T)] /
[Γ_{p->n}^{had}(T)+Γ_{n->p}^{had}(T)].
D2 quasi-stable neutron target
X_n^{qs}(T)
=
Γ_{p->n}^{had}/
(Γ_{p->n}^{had}+Γ_{n->p}^{had}).
D3 total hadronic relaxation strength
R_h(T)=Γ_{p->n}^{had}+Γ_{n->p}^{had}.
D4 crossing/waterfall locations versus weak rate.
D5 channel decomposition
π / K± / KL / anti-N contributions to both D2 and D3.
D6 sensitivity of D2 and crossing time to:
- overall common amplitude scaling;
- directional differential scaling;
- source/hadronization changes.
These are diagnostics / design objects, not numerical endpoint authorization.
13. POSSIBLE REDUCED PBH HOST
If common amplitude scalings cancel while directional ratio and crossing dominate, a reduced PBH descriptor may be:
{X_n^{qs}(T), R_h(T)/R_weak(T)}
instead of the full hadron-state history for some early-Yp claim class.
But this must survive:
- source-matched comparison to full DE/full-history BBN;
- target-relative error test;
- B2 carrier support;
- background variation.
STATUS:
REDUCED_WATERFALL_DESCRIPTOR = CANDIDATE / NOT VALIDATED.
14. CONSEQUENCE FOR KERNEL PRIORITY
017 correctly established that a full time-local weak-rate kernel is mature-method / source-specific construction.
018 adds:
the kernel may be OVERKILL for some early-Yp lifetime-like claims if a waterfall reduction is source-valid.
Therefore execution order should be:
A test reduced waterfall descriptor first;
B if source-specific comparison fails, construct/refine time-local weak-rate kernel;
C retain direct full-history endpoint comparison as final validator.
This minimizes scientific and computational overhead.
15. MODEL-USE DISCIPLINE
No external AI model used.
This rotation had a precise source question and two highly relevant primary papers.
Direct literature provided a stronger answer than an additional model audit would.
External-model use remains justified later for:
- independent audit of a PBH-specific reduced descriptor;
- divergent failure-mode search once a concrete PBH source is frozen;
- literature ambiguity that survives source-first review.
16. CURRENT CLAIM CEILING
JUNG_HADRONIC_BBN_WATERFALL_HOST = PASS / MATURE.
OVERALL_AMPLITUDE_ROBUSTNESS_FOR_AXION_LIFETIME_BOUND = PASS / SOURCE-SPECIFIC.
DIRECTIONAL_RATE_RATIO = LOAD_BEARING.
MULTI_HADRON_COMPENSATION_IN_XN_QS = PASS.
MULTI_HADRON_CONSTRUCTIVE_WATERFALL_STRENGTH = PASS.
PBH_B2_WATERFALL_TRANSFER = OPEN.
REDUCED_WATERFALL_DESCRIPTOR = CANDIDATE / NOT VALIDATED.
TIME_LOCAL_WEAK_RATE_KERNEL = STILL AVAILABLE AS FALLBACK VALIDATION.
SOURCE_MATCHED_K_PBH = UNDEFINED.
NO PBH BOUND / NO ENDPOINT RELEASE.
NO CANON / NO EXEC_SIGN / NO NOVELTY / SCIENCE_FIRST.
SOURCES
[Jung–Okui–Tobioka–Wang 2026]
[Bianco–Frerick–Hufnagel–Schmidt-Hoberg 2026]
