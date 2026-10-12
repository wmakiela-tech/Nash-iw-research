---
artifact_id: MECH-S6-FRONTB-WU-XU-EDGE-SLOPE-STRESS-AMPLIFICATION-AND-REGENERATION-ACCEPTANCE-GATE-001
bw_ingestion_event_id: ING-20261012-0013
bw_qualification_state: FRONTB_EDGE_SLOPE_STRESS
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE
archive_mode: PUBLIC_ARTIFACT
sync_state: GITHUB_PENDING_BW_LINK_UPDATE
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# MECH-S6-FRONTB-WU-XU-EDGE-SLOPE-STRESS-AMPLIFICATION-AND-REGENERATION-ACCEPTANCE-GATE-001

> Public-safe mirror of the BW-linked Drive source. BW controls lifecycle/currentness; this GitHub body does not upgrade scientific authority.

MECH-S6 — FRONT B WU–XU EDGE-SLOPE STRESS AMPLIFICATION / REGENERATION ACCEPTANCE GATE
RETURN_ID: MECH-S6-FRONTB-WU-XU-EDGE-SLOPE-STRESS-AMPLIFICATION-AND-REGENERATION-ACCEPTANCE-GATE-001
IN_REPLY_TO:
MECH-S6-FRONTB-WU-XU-TERMINAL-SOURCE-EXTRAPOLATION-EVAPORATION-WEIGHTED-YIELD-AND-DISCREPANCY-GATE-001
XH-S3-FRONTB-WU-XU-TERMINAL-HADRON-SOURCE-EXTRAPOLATION-HARVEST-022
LT3 DRAFT018 / MT13 temporary living-theory coverage
RESULT_CLASS: SOURCE-STRESS GEOMETRY / REGENERATION ACCEPTANCE CONTRACT / NO PHYSICAL ERROR BAR
STATUS: PASS_EXACT_FOR_DECLARED_POWER-STRESS FAMILY / E2 DIRECT SOURCE VALIDATION NOT RUN
1. CONTROLLING GAP
The current public executor uses the first log-log table secant as a power-law extrapolation below the approximately 1e9 g source-table edge.
The prior Mech gate showed:
a. this is code semantics, not physical validation;
b. the deepest terminal region is not automatically dominant after evaporation-time weighting;
c. direct lower-mass regeneration is the highest-value next validation.
The remaining bounded question is:
before E2 regeneration exists, how should a declared perturbation of the edge slope propagate into source rates and integrated sub-edge count without pretending to be a physical uncertainty bar?
2. DIRECT LOW-EDGE SLOPE AUDIT
Using the first 13 directly tabulated rows of the public hadron-source table, the first 12 local log-log slopes are monotone toward more-negative values as mass increases away from the low edge.
Species:
charged pion:
first slope -1.200486;
12th slope -1.303073.
charged kaon:
first -1.196651;
12th -1.296992.
K0L:
first -1.196805;
12th -1.297834.
proton:
first -1.204291;
12th -1.308939.
neutron:
first -1.204763;
12th -1.309602.
Thus the within-table excursion over these 12 intervals is approximately:
|Delta p| ~ 0.100 to 0.105.
This is an observed local-table fact.
It is NOT evidence that the same slope excursion continues below the table.
3. IMPORTANT CURVATURE GUARD
The local slopes become more negative as mass increases from the lower edge.
Therefore extrapolating the observed curvature backward to smaller mass would not even point in the same direction as simply replacing the edge slope by the 12th in-table slope.
Hence:
12TH IN-TABLE SLOPE != LOWER-MASS ASYMPTOTE.
The first-to-12th slope excursion may be used only as a convenient stress amplitude.
It is not a one-sided physical uncertainty direction.
4. DECLARED POWER-STRESS FAMILY
Let the E0 source below the edge be:
q_0(M)
=
q_e x^(p_0),
where:
x=M/M_e <1.
Declare a stress slope:
p=p_0+delta p.
Then:
q_delta(M)
=
q_e x^(p_0+delta p).
The exact instantaneous source ratio is:
q_delta/q_0
=
x^(delta p).
This is the fundamental amplification law.
5. LOG-SENSITIVITY
Taking logs:
delta ln q
=
delta p ln x.
Therefore:
|delta ln q|
=
|delta p| ln(M_e/M).
The source sensitivity to slope error grows linearly with extrapolation depth in log mass.
This is exact for the declared power family.
6. NUMERICAL STRESS AT THREE VALIDATION MASSES
Use representative extrapolation ratios:
x=0.6  corresponding to 6e8 g;
x=0.3  corresponding to 3e8 g;
x=0.106 corresponding approximately to 1.06e8 g.
Using the observed first-to-12th in-table slope excursion as stress amplitude:
charged pion:
delta p=-0.102587.
q_stress/q_E0:
1.0538 at 6e8 g;
1.1315 at 3e8 g;
1.2589 at 1.06e8 g.
charged kaon:
delta p=-0.100340.
ratios:
1.0526;
1.1284;
1.2526.
K0L:
delta p=-0.101029.
ratios:
1.0530;
1.1293;
1.2545.
proton:
delta p=-0.104647.
ratios:
1.0549;
1.1343;
1.2647.
neutron:
delta p=-0.104839.
ratios:
1.0550;
1.1345;
1.2653.
Thus a slope shift of order 0.10 changes the source by only about:
5.3–5.5% at 6e8 g;
12.8–13.5% at 3e8 g;
25.3–26.5% at 1.06e8 g.
Again:
these are STRESS NUMBERS, not physical confidence intervals.
7. GENERAL REQUIRED SLOPE ACCURACY FOR A SOURCE TOLERANCE
Suppose a direct regeneration is to constrain the source ratio at mass ratio x to within a multiplicative factor 1+tau.
For a one-sided logarithmic tolerance:
|delta p|
<=
ln(1+tau)/|ln x|.
This is the exact slope-accuracy requirement for the power family.
Examples:
at x=0.6:
a 10% source tolerance corresponds to |delta p| <= approximately 0.187.
at x=0.3:
10% corresponds to <= approximately 0.079.
at x=0.106:
10% corresponds to <= approximately 0.0425.
Therefore a regeneration point near 1e8 g is much more discriminating about extrapolation law than one at 6e8 g.
8. EVAPORATION-WEIGHTED SUB-EDGE COUNT
Inside current executor high-T constant-N_BH semantics, for power slope p:
N_sub(p)
proportional to
1/(p+3),
when integrated from a negligible terminal lower mass to M_e and normalized to the same edge value q_e.
Hence relative to E0:
N_sub(p_0+delta p)/N_sub(p_0)
=
(p_0+3)/(p_0+delta p+3).
This is exact for the declared power family.
9. NUMERICAL INTEGRATED-COUNT STRESS
Using the same first-to-12th slope stress:
charged pion:
integrated sub-edge count ratio = 1.06045.
charged kaon:
1.05892.
K0L:
1.05935.
proton:
1.06188.
neutron:
1.06202.
Thus the entire E0 sub-edge unweighted hadron count shifts by only about:
5.9–6.2%
under this particular constant-slope stress.
This is much smaller than the local source-rate effect at the deepest validation mass because rapid terminal evaporation suppresses the deep tail.
10. LOCAL SOURCE SENSITIVITY != INTEGRATED SOURCE SENSITIVITY
At x approximately 0.106:
instantaneous source stress is approximately +25%.
Yet total sub-edge unweighted count stress is approximately +6%.
Therefore:
POINTWISE SOURCE ERROR
!=
INTEGRATED SOURCE ERROR.
The mass-loss clock acts as a physical weighting before any BBN target weighting is applied.
11. TARGET WEIGHT REMAINS SEPARATE
For target kernel W(M):
C_W(p)
proportional to
Integral_0^1
W(x) x^(p+2) dx.
No universal closed ratio follows without W.
If W strongly enhances the terminal endpoint, target sensitivity can exceed unweighted count sensitivity.
Therefore:
6% UNWEIGHTED COUNT STRESS
!=
6% Yp/DH STRESS.
12. REGENERATION ACCEPTANCE AS LOCAL EFFECTIVE SLOPE
Given a direct regenerated point q_reg(M_i), define the edge-anchored effective slope:
p_eff(M_i)
=
ln[q_reg(M_i)/q_e] /
ln[M_i/M_e].
This is not assumed to be an asymptotic slope.
It is simply the unique edge-anchored power that passes through the regenerated point.
Compare:
delta p_eff
=
p_eff-p_0.
Then the current E0 extrapolator passes a declared local acceptance tolerance tau_i iff:
|ln(q_reg/q_E0)| <= ln(1+tau_i)
or equivalently:
|delta p_eff|
<=
ln(1+tau_i)/|ln x_i|.
13. MULTIPOINT CURVATURE TEST
With direct regenerated points at:
6e8,
3e8,
approximately 1e8 g,
compute p_eff at each point.
If:
p_eff(6e8)
approximately
p_eff(3e8)
approximately
p_eff(1e8),
then a single edge-anchored power remains empirically adequate over that interval.
If p_eff drifts systematically with x:
the source requires curvature in log q versus log M.
Then replace E0 by a lower-mass interpolation or another physically validated source representation.
Do NOT fit a terminal asymptote merely because three points admit a polynomial.
14. DIRECT CURVATURE OBSERVABLE
For two regenerated masses x_i,x_j, define:
C_ij
=
[p_eff(x_i)-p_eff(x_j)] /
[ln x_i-ln x_j].
C_ij=0 for an exact single power.
Nonzero C_ij measures edge-anchored log-curvature over the regenerated interval.
This is a diagnostic, not a fundamental physical parameter.
15. SPECIES-COMPOSITION STRESS
The five source species have slightly different edge slopes and different in-table slope evolution.
Even if a common multiplicative source normalization were uncertain, species-relative source ratios can change.
For species h,k:
q_h/q_k
proportional to
x^(p_h-p_k).
Thus:
delta ln(q_h/q_k)
=
delta(p_h-p_k) ln x.
This matters because:
A and B receive different species/directional contributions.
Therefore source-shape uncertainty can alter:
total source magnitude
AND
conversion-direction composition.
TOTAL HADRON COUNT AGREEMENT
!=
A/B AGREEMENT.
16. E0 SOURCE-COMPOSITION STABILITY AT THE EDGE
The first-edge slopes differ across the five tabulated source columns only at roughly the 0.008 level.
Under E0 this means species ratios evolve relatively slowly with extrapolation depth compared with total source amplitude.
But a regenerated E2 source can change that conclusion.
Hence direct regeneration must retain species-resolved outputs.
Do not validate only total hadronic multiplicity.
17. ACCEPTANCE OUTPUT FOR EACH REGENERATED POINT
Record:
M_i;
T_BH(M_i);
q_h^E0;
q_h^reg;
ratio q_reg/q_E0;
p_eff,h;
delta p_eff,h;
species ratio changes;
BlackHawk version;
hadronization mode;
Emin/Emax;
primary/secondary settings;
PYTHIA/HERWIG contract;
random seed or deterministic configuration if applicable;
table-generation script hash;
runtime warnings.
18. MINIMUM PASS STRUCTURE
For source-contract purposes, a near-edge E2 validation may be declared PASS over a finite mass interval only if:
A. same physical hadronization contract is used;
B. regenerated species-resolved q_h are available;
C. declared source tolerance is passed at all validation points;
D. no unresolved energy-range warning invalidates the hadronization output;
E. interpolation between regenerated points is typed separately from extrapolation below the lowest regenerated point.
Passing these does NOT validate the deep terminal tail automatically.
19. FAILURE STRUCTURE
If direct q_reg differs materially from E0:
do not interpret this first as a DE failure.
The correct order is:
SOURCE CONTRACT FAILURE
before
POPULATION CLOSURE FAILURE.
Update q_h(M) first.
Then re-run downstream floor/DE/A-B/X/target checks.
20. NO DIRECT E2 FOUND IN CURRENT PUBLIC REPO
Current GitHub source search found:
6e8 only as part of scan-parameter configuration.
No direct q_h regeneration artifact was located for:
3e8 g
or
1e8 g.
Thus:
E2_DIRECT_SOURCE_VALIDATION
remains genuinely NOT RUN / NOT LOCATED in the public project repository.
21. RELATION TO FLOOR GATE
The source-stress question is upstream of floor semantics.
Changing q_h changes:
S_h;
n_h trajectory;
floor-entry/reentry timing;
and floor residual magnitude.
Therefore floor materiality cannot be finalized before the source model is admitted.
SOURCE VALIDITY
precedes
SOURCE-ACTIVE FLOOR MATERIALITY.
22. RELATION TO A/B GEOMETRY
A source perturbation is first propagated species-wise into n_h.
Then:
deltaA
=
sum delta n_h k_h^pn,
deltaB
=
sum delta n_h k_h^np.
Because source slope perturbations can be species dependent, A/B composition is load-bearing.
Do not collapse E1/E2 validation to one scalar total hadron source.
23. CLAIM CEILING
PASS EXACT:
first-12-interval slope audit;
declared power-stress amplification law;
source-tolerance to slope-tolerance map;
evaporation-weighted integrated count ratio;
effective-slope regeneration diagnostic;
species-ratio sensitivity identity.
STRESS ONLY:
using first-to-12th in-table slope excursion as lower-mass slope perturbation.
NOT ESTABLISHED:
physical source uncertainty;
terminal asymptotic law;
E2 source values below 1e9 g;
high-energy metastable-hadron validation;
target-weighted Yp/DH effect;
PBH bound.
24. FIREWALLS
IN-TABLE SLOPE EVOLUTION != OUT-OF-TABLE ASYMPTOTE.
STRESS AMPLITUDE != ERROR BAR.
EDGE-ANCHORED p_eff != FUNDAMENTAL POWER LAW.
ONE REGENERATION POINT != CURVATURE VALIDATION.
TOTAL SOURCE AGREEMENT != SPECIES-COMPOSITION AGREEMENT.
TOTAL SOURCE AGREEMENT != A/B AGREEMENT.
POINTWISE SOURCE ERROR != INTEGRATED SOURCE ERROR.
UNWEIGHTED COUNT STRESS != TARGET STRESS.
SOURCE CONTRACT FAILURE != DE FAILURE.
25. STATUS
LOW_EDGE_FIRST12_SLOPE_AUDIT=PASS_EXACT.
OBSERVED_FIRST12_SLOPE_EXCURSION=~0.100_TO_0.105.
POWER_STRESS_SOURCE_AMPLIFICATION=x^delta_p=PASS_EXACT.
POWER_STRESS_INTEGRATED_COUNT_RATIO=(p0+3)/(p+3)=PASS_EXACT.
REPRESENTATIVE_STRESS_AT_6E8G=~5.3_TO_5.5_PERCENT.
REPRESENTATIVE_STRESS_AT_3E8G=~12.8_TO_13.5_PERCENT.
REPRESENTATIVE_STRESS_AT_1P06E8G=~25.3_TO_26.5_PERCENT.
REPRESENTATIVE_TOTAL_SUBEDGE_COUNT_STRESS=~5.9_TO_6.2_PERCENT.
E1_SLOPE_STRESS=DIAGNOSTIC_ONLY.
E2_DIRECT_REGENERATION=NOT_LOCATED.
TERMINAL_SOURCE_PHYSICAL_VALIDATION=OPEN.
PBH_DE_DYNAMIC_ACCURACY=OPEN.
PBH_Yp_DH_TARGET_VALIDATION=OPEN.
SOURCE_MATCHED_K_PBH=UNDEFINED.
NO PBH BOUND / NO ENDPOINT / NO CANON / NO EXEC_SIGN / NO NOVELTY.
REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD.
26. SOURCE BASIS
Current public Wu–Xu repository:
https://github.com/Fenyutanchan/Primordial-Black-Hole
Directly inspected:
arXiv-2509.05618/data/out/hadrons_from_PBH.dat
arXiv-2509.05618/tool_script-hadrons_from_PBH.jl
arXiv-2509.05618/main-scan-parameters.jl
Project inputs:
MECH-S6-FRONTB-WU-XU-TERMINAL-SOURCE-EXTRAPOLATION-EVAPORATION-WEIGHTED-YIELD-AND-DISCREPANCY-GATE-001.
XH-S3-FRONTB-WU-XU-TERMINAL-HADRON-SOURCE-EXTRAPOLATION-HARVEST-022.
