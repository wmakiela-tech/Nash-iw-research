---
artifact_id: MECH-S6-FRONTB-WU-XU-TERMINAL-SOURCE-EXTRAPOLATION-EVAPORATION-WEIGHTED-YIELD-AND-DISCREPANCY-GATE-001
created_at: 2026-10-12
as_of: 2026-10-12
origin_cell: Mech-S6
document_type: RETURN
exposure: PUBLIC
archive_mode: PUBLIC_ARTIFACT
bw_ingestion_event_id: ING-20261012-0062
bw_qualification_state: SOURCE_TERMINAL_E0_WEIGHTED_INTEGRABILITY_GATE
bw_lifecycle_state: CURRENT_REPRESENTED
scientific_claim_ceiling: NO_AUTHORITY_UPGRADE
source_revision: PRIVATE_ORIGINAL_BW_ROW_1389
no_canon: true
no_exec_sign: true
---

> Full public scientific return, published from the pre-existing verified BW source. Original scientific body below is preserved without intentional modification. Public release is not scientific acceptance, novelty or physical validation.

﻿MECH-S6 — FRONT B WU–XU TERMINAL SOURCE EXTRAPOLATION / EVAPORATION-WEIGHTED YIELD AND DISCREPANCY GATE
RETURN_ID: MECH-S6-FRONTB-WU-XU-TERMINAL-SOURCE-EXTRAPOLATION-EVAPORATION-WEIGHTED-YIELD-AND-DISCREPANCY-GATE-001
IN_REPLY_TO:
XH-S3-FRONTB-WU-XU-TERMINAL-HADRON-SOURCE-EXTRAPOLATION-HARVEST-022
MECH-S6-FRONTB-WU-XU-LOG-POPULATION-FLOOR-SOURCE-INJECTION-RESIDUAL-GATE-001
M12-FRONTB-COUPLED-PATH-FLOOR-RESIDUAL-SMALL-GAIN-GATE-001
REC9-M12-FRONTB-COUPLED-PATH-SMALL-GAIN-REFEREE-001
LT3 DRAFT018 / MT13 temporary living-theory coverage


RESULT_CLASS: SOURCE-CONTRACT PRIORITIZATION / EXACT EXECUTOR MASS-VARIABLE IDENTITY / CONDITIONAL SOURCE-DISCREPANCY PROPAGATION
STATUS: PASS_EXACT FOR CURRENT EXECUTOR SEMANTICS / PHYSICAL SOURCE VALIDATION STILL OPEN


1. EXECUTIVE RESULT
XH022 identifies a more fundamental Front B gate than the log-population floor:


the current public Wu–Xu hadron source table is directly tabulated only down to approximately 1e9 g, while the public scan and source cutoff drive the interpolator many decades below that edge by exact log-log linear extrapolation.


Direct code inspection confirms this.


A second exact source-native fact substantially refines the severity picture:


although the extrapolated instantaneous hadron rate grows approximately as M^(-1.2), PBH evaporation accelerates as |dM/dt| proportional to M^(-2).


Therefore the cumulative per-PBH hadron count carries an M^2 evaporation-time weight.


Within the current executor, the deepest terminal decades do NOT dominate the unweighted integrated hadron count.


This does NOT validate the extrapolated source.


It does identify where validation effort has the greatest leverage.


2. CURRENT PUBLIC SOURCE CONTRACT
The public file


data/out/hadrons_from_PBH.dat


contains hadron rates versus PBH mass.


Current tool_script-hadrons_from_PBH.jl constructs, species by species:


LinearInterpolation(
  log(rate),
  log(mass);
  extrapolation=Linear
).


Therefore below the lowest table mass M_e:


q_h^E0(M)
=
q_h,e (M/M_e)^(p_h,e),


where q_h=dN_h/dt per PBH and p_h,e is exactly the first log-log secant slope.


This is executor semantics.


It is not an established physical asymptotic theorem.


3. TABLE EDGE
The first public table mass is approximately:


M_e = 1e9 g.


The directly inspected first rows reproduce the XH022 edge rates and the edge powers near:


p_pi   approximately -1.20049
p_Kpm  approximately -1.19665
p_K0L  approximately -1.19680
p_p    approximately -1.20429
p_n    approximately -1.20476.


The first several in-table local slopes vary away from these values.


Therefore:


FIRST EDGE SLOPE != VERIFIED TERMINAL ASYMPTOTE.


4. PBH MASS-LOSS LAW
Current public main-scan uses:


dM/dt
=
-N_BH(T_BH) M_Pl^4 / M^2,


with


T_BH=M_Pl^2/M,


and


N_BH(T_BH)
=
(27/4) N_rho(T_BH)/(30720 pi).


This is the source-native clock relating terminal mass to physical time.


5. HIGH-T N_BH SATURATION IN THE CURRENT EXECUTOR
The public N_s and N_rho/N_s tables terminate near a few 10^5 MeV, i.e. a few 10^2 GeV.


The interpolators use:


extrapolation=Constant.


Hence in the current executor, once T_BH exceeds the upper thermodynamic table edge:


N_rho(T_BH)
=
constant,


and therefore


N_BH
=
N_infinity
constant.


At M=1e9 g, XH022 finds T_BH approximately 1.06e4 GeV.


Thus the entire M<1e9 g hadron-source extrapolation regime already lies inside the executor's constant-N_BH high-temperature regime.


This makes the following mass-variable identities exact for CURRENT EXECUTOR semantics.


6. EXACT MASS-VARIABLE HADRON COUNT
For one PBH, the cumulative number of hadrons emitted while mass decreases from M_a to M_b<M_a is:


N_h(M_b,M_a)
=
Integral q_h[M(t)] dt.


Using the mass-loss law:


dt
=
- M^2 dM /(N_infinity M_Pl^4),


so:


N_h(M_b,M_a)
=
1/(N_infinity M_Pl^4)
Integral_{M_b}^{M_a}
q_h(M) M^2 dM.


This identity is exact inside the declared current-executor high-T regime.


7. EXACT E0 POWER-LAW INTEGRAL
For the current edge extrapolator:


q_h^E0(M)
=
q_e (M/M_e)^p,


the cumulative count is:


N_h^E0(M_b,M_a)
=
[q_e M_e^(-p)] /
[N_infinity M_Pl^4 (p+3)]
*
[
M_a^(p+3)-M_b^(p+3)
],


provided p != -3.


For all current species p approximately -1.2, so:


p+3 approximately 1.8 > 0.


Therefore:


lim_{M_b->0} N_h^E0(M_b,M_a)


is finite.


8. INSTANTANEOUS DIVERGENCE != INTEGRATED DOMINANCE
The current extrapolated q_h(M) diverges as M->0 because p<0.


But the time-integrated source density per PBH behaves as:


q_h(M)|dt/dM|
proportional to
M^(p+2).


For p approximately -1.2:


p+2 approximately 0.8 > 0.


So the contribution per unit PBH mass actually tends to zero at the terminal endpoint.


Exact firewall:


INSTANTANEOUS SOURCE RATE BLOW-UP
!=
TERMINAL INTEGRATED-YIELD DOMINANCE.


9. CUMULATIVE TERMINAL FRACTION
Relative to all current E0-extrapolated hadron count below the table edge M_e, the fraction emitted below M_c is:


f_h(<M_c | <M_e)
=
(M_c/M_e)^(p+3),


neglecting the tiny finite lower cutoff compared with M_c.


For


M_c approximately 1.06e8 g
and
M_e approximately 1e9 g,


the five current edge powers give:


f approximately 0.0175 to 0.0178.


Thus only about:


1.75% to 1.78%


of the CURRENT EXECUTOR'S UNWEIGHTED sub-edge per-PBH hadron count lies below the approximate T_BH=1e5 GeV mass threshold.


Equivalently, about 98.2% of that E0 sub-edge count lies between approximately 1.06e8 g and 1e9 g.


10. INTERPRETATION OF THE 1.75–1.78% NUMBER
This number is:


EXACT WITHIN
the current E0 source extrapolator,
current PBH mass-loss law,
and current high-T constant-N_BH executor semantics.


It is NOT:


a physical uncertainty bound;
a Y_p bound;
a D/H bound;
a guarantee about the true high-energy metastable-hadron source;
or a validation of the extrapolated power law.


It is a prioritization result.


11. WHY THE NEAR-EDGE DECADE IS THE FIRST VALIDATION TARGET
XH022 identifies an approximate high-energy hadronization support concern below M approximately 1.06e8 g.


But the current executor's own integrated source weighting says:


the region approximately
1.06e8 g to 1e9 g


contains nearly all the extrapolated sub-edge hadron count.


That region is also software-addressable by directly running BlackHawk at lower masses because:


set_BlackHawk_mass!


accepts arbitrary positive masses.


Therefore the cheapest high-value validation is:


direct source regeneration at 6e8, 3e8, approximately 1e8 g
under the SAME BBN hadronization contract.


This tests the region that carries the largest E0 extrapolated integrated count.


12. DEEP TERMINAL REGION REMAINS OPEN
Below approximately 1e8 g:


the located public BBN hadronization artifacts do not establish the metastable pi/K/anti-N source all the way to terminal Hawking temperatures.


The small E0 unweighted count fraction does not close this issue.


A different physical source law can depart strongly from E0.


Therefore:


SMALL E0 TERMINAL COUNT FRACTION
!=
SMALL PHYSICAL SOURCE UNCERTAINTY.


13. TARGET WEIGHT CAN CHANGE THE PRIORITY
The 1.75–1.78% fraction is unweighted hadron count.


A final BBN target responds to injection time.


For a legal target sensitivity W_h(t), the source contribution is instead:


C_h[W]
=
Integral
W_h(t) q_h[M(t)] dt.


In mass variable:


C_h[W]
=
1/(N_infinity M_Pl^4)
Integral
W_h[M]
q_h(M) M^2 dM.


Thus a strongly terminal-peaked W_h can amplify a region that is small in unweighted count.


Therefore:


UNWEIGHTED SOURCE FRACTION
!=
TARGET-WEIGHTED IMPORTANCE.


This reconnects source validation to the previously designed PRIMAT target-kernel programme.


14. SOURCE MODEL DISCREPANCY
Let E0 be the current edge extrapolation.


Let E_alt be any alternative physically admissible source model.


Define:


delta q_h(M)
=
q_h^alt(M)-q_h^E0(M).


On a common background before population feedback, the physical source-density discrepancy is:


delta S_h(t)
=
n_PBH(t) delta q_h[M(t)].


For comoving source:


a^3 delta S_h
=
N_PBH^com delta q_h,


where N_PBH^com is constant before PBH disappearance in the current model.


15. EXACT SOURCE-DISCREPANCY TO POPULATION BRIDGE
On one prescribed common X/background path:


n_h' + D_h n_h = S_h.


For two source models with the same D_h and initial state:


delta n_h'
+
D_h delta n_h
=
delta S_h.


Exactly:


delta n_h(t)
=
exp[-Integral_{t0}^t D_h]
delta n_h(t0)


+
Integral_{t0}^t
exp[-Integral_s^t D_h]
delta S_h(s) ds.


For equal initial populations:


|delta n_h(t)|
<=
Integral
exp[-Integral_s^t D_h]
|delta S_h(s)| ds.


This is an exact source-model uncertainty propagator.


16. SOURCE DISCREPANCY TO A,B
At common state/background:


A
=
sum_h n_h k_h^pn,


B
=
sum_h n_h k_h^np.


Therefore exactly:


delta A
=
sum_h delta n_h k_h^pn,


delta B
=
sum_h delta n_h k_h^np.


And:


delta F_had
=
(1-X)delta A
-
X delta B.


So:


|delta F_had|
<=
sum_h
|delta n_h|
[
(1-X)k_h^pn
+
X k_h^np
].


This is the same primary A/B geometry already adopted in DRAFT018.


17. DYNAMIC X PROPAGATION
M12 already gives the monotone dynamic error inequality:


d|delta X|/dt
<=
-c(t)|delta X|
+
epsilon_F(t),


provided the source discrepancy is represented as a legal residual or source-model difference and the declared regime conditions hold.


Thus the source-contract chain is now:


SOURCE MODEL DIFFERENCE delta q_h
->
delta S_h
->
delta n_h
->
delta A,delta B
->
delta F_had
->
delta X_n
->
later target kernel.


No q=A/(A+B) ratio is needed.


18. COUPLED-PATH GUARD
The exact delta n formula in §15 is common-path.


If X trajectories differ and D_h depends on X:


delta D_h
must be included.


Then use the source-aware coupled comparison system / small-gain machinery from SW/M12.


Rec9's referee repair remains controlling:


a,b,c,d,F are regime-local;
global trajectory admission requires bootstrap/self-consistency;
the chosen population norm must be typed consistently.


19. FLOOR RESIDUAL COMPOSITION
Source extrapolation discrepancy and executor floor discrepancy are different layers.


Intended physical source-model discrepancy:


rho_source
=
delta S_h.


Raw executor floor discrepancy:


rho_floor
=
S_h(alpha_h-1).


If one compares a raw E0 executor trajectory to an intended alternative physical source model, both terms can be present.


They must be entered separately in the residual ledger.


SOURCE MODEL ERROR
!=
LOG-FLOOR EXECUTOR ERROR.


20. POWER-SLOPE ENVELOPE — ONLY A STRESS FAMILY
Suppose one DECLARES, for stress testing only, a source log-slope envelope:


p_-(M)
<=
d ln q / d ln M
<=
p_+(M)


below M_e.


If constant bounds p_- <= p_+ are assumed over the whole interval and x=M/M_e<1, then:


q_e x^(p_+)
<=
q(M)
<=
q_e x^(p_-).


This produces a closed source envelope.


But:


the observed first several in-table slopes do NOT justify extending such a bound many decades beyond the table.


Therefore the local-slope family E1 is:


STRESS ENVELOPE / SENSITIVITY FAMILY,


not a certified physical error bar.


21. E0/E1/E2 HIERARCHY
E0:
current exact executor extrapolation.


E1:
declared local-slope or other source-shape stress family.
Purpose: sensitivity only.


E2:
direct regenerated or independently validated source.


Scientific ordering:


E0 describes what code does.
E1 asks how downstream results react to plausible shape changes.
E2 is needed for physical source admission.


CODE SEMANTICS
!=
UNCERTAINTY MODEL
!=
PHYSICAL VALIDATION.


22. B2 EXTENSION
For B2 distributions the aggregate hadron source is:


Q_h(t)
=
a^-3
Integral
chi
q_h[M(t;M_i,t_f)]
dmu_B2(M_i,t_f).


The same source-model discrepancy propagates linearly at the source stage:


delta Q_h(t)
=
a^-3
Integral
chi
delta q_h[M(t;M_i,t_f)]
dmu_B2.


This does NOT validate the B2 carrier.


It only shows that once delta q_h is typed, its population-level propagation has a direct integral form.


23. NEW ORDER OF FRONT B GATES
The source-native gate order should now be:


G0 SOURCE TABLE / HADRONIZATION CONTRACT
Is q_h(M) physically admitted over the masses actually used?


G1 SOURCE EXTRAPOLATION STRESS
What changes under E0/E1/E2?


G2 RAW EXECUTOR SEMANTICS
Does source-active log floor materially modify the declared source?


G3 POPULATION DE / FULL TRACKING
Is n_h^DE accurate?


G4 A/B DIRECTIONAL-RATE ACCURACY
Do the physical reduced rates agree?


G5 DYNAMIC X_n ACCURACY
Use monotonicity / residual tube / small gain.


G6 TARGET KERNEL
Y_p and D/H separately.


G7 B2 carrier/background validation.


Numerical PBH bound remains closed until these gates are source-matched.


24. CHEAPEST NEXT SCIENTIFIC VALIDATION
No new task is delegated here.


The smallest direct validation that would materially change Front B status is:


same BlackHawk BBN/PYTHIA contract;
regenerate q_h at approximately:


6e8 g,
3e8 g,
1e8 g;


for:
charged pion,
charged kaon,
K0L,
proton,
neutron / anti-N-relevant source mapping.


Compare:
direct q_h
vs
E0 edge extrapolation
vs
E1 stress envelope.


Do not yet run Y_p/D-H.


25. STOP CONDITION
If direct near-edge regeneration tracks E0 within a declared tolerance over 1e8–1e9 g:


the largest executor-weighted sub-edge region gains source support.


The deep high-energy tail remains separately open but becomes a lower unweighted-count priority under the current E0 weighting.


If regeneration materially departs from E0:


stop downstream DE validation and first repair q_h(M).


26. CLAIM CEILING
PASS EXACT:
current log-log edge extrapolator semantics;
current high-T constant-N_BH executor semantics;
mass-variable hadron-count identity;
E0 terminal integrability;
E0 cumulative terminal fraction formula;
approximately 1.75–1.78% E0 unweighted sub-edge fraction below 1.06e8 g;
source-model discrepancy -> population convolution;
population discrepancy -> A/B -> reduced RHS bridge.


NOT ESTABLISHED:
physical correctness of E0 below 1e9 g;
physical slope envelope beyond the table;
high-energy metastable-hadron source below approximately 1e8 g;
target-weighted smallness of the deep tail;
PBH DE dynamic accuracy;
Y_p / D-H accuracy;
B2 carrier validation;
K_PBH;
PBH abundance bound.


27. FIREWALLS
EDGE POWER LAW != PHYSICAL ASYMPTOTE.
INSTANTANEOUS RATE DIVERGENCE != INTEGRATED-YIELD DOMINANCE.
SMALL UNWEIGHTED COUNT FRACTION != SMALL TARGET EFFECT.
EXECUTOR INTEGRABILITY != SOURCE VALIDITY.
LOCAL SLOPE BAND != EXTRAPOLATION ERROR BAR.
LOWER-MASS BLACKHAWK RUNNABLE != HIGH-ENERGY HADRONIZATION VALIDATED.
SOURCE MODEL ERROR != FLOOR EXECUTOR ERROR.
COMMON-PATH SOURCE CERTIFICATE != COUPLED-PATH GLOBAL ADMISSION.
E0 != E2.
NO SOURCE VALIDATION != PBH BOUND.


28. STATUS
WU_XU_SOURCE_EXTRAPOLATOR_SEMANTICS=PASS_EXACT.
SUBEDGE_HIGH_T_NBH_CONSTANT_IN_CURRENT_EXECUTOR=PASS_EXACT.
E0_MASS_WEIGHTED_TERMINAL_INTEGRABILITY=PASS_EXACT.
E0_DEEP_TERMINAL_UNWEIGHTED_FRACTION_BELOW_1P06E8G=~1.75_TO_1.78_PERCENT.
NEAR_EDGE_1P06E8_TO_1E9G=HIGHEST_E0_SOURCE_VALIDATION_LEVERAGE.
SOURCE_DISCREPANCY_TO_POPULATION_BRIDGE=PASS_EXACT_COMMON_PATH.
SOURCE_DISCREPANCY_TO_AB_X_CHAIN=PASS_EXACT_CONDITIONAL.
E1_LOCAL_SLOPE_ENVELOPE=STRESS_ONLY.
E2_DIRECT_SOURCE_VALIDATION=NOT_RUN.
TERMINAL_SOURCE_PHYSICAL_VALIDATION=NOT_ESTABLISHED.
HIGH_ENERGY_METASTABLE_BBN_HADRONIZATION=OPEN.
LOG_FLOOR_REENTRY=OPEN_SECONDARY_TO_SOURCE_CLOSURE.
PBH_DE_DYNAMIC_ACCURACY=OPEN.
PBH_Yp_DH_TARGET_VALIDATION=OPEN.
PBH_B2_WATERFALL_TRANSFER=OPEN.
SOURCE_MATCHED_K_PBH=UNDEFINED.
NO PBH BOUND / NO ENDPOINT / NO CANON / NO EXEC_SIGN / NO NOVELTY.
REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD.


29. SOURCE BASIS
Current public Wu–Xu repository:
https://github.com/Fenyutanchan/Primordial-Black-Hole


Directly inspected:
arXiv-2509.05618/tool_script-hadrons_from_PBH.jl
arXiv-2509.05618/data/out/hadrons_from_PBH.dat
arXiv-2509.05618/tool_script-BlackHawk_extension.jl
arXiv-2509.05618/tool_script-N_relativistic_species.jl
arXiv-2509.05618/data/ext/N_s_from_PDG2024.csv
arXiv-2509.05618/data/ext/N_rho_OVER_N_s_from_PDG2024.csv
arXiv-2509.05618/tool_script-parameters.jl
arXiv-2509.05618/main-scan.jl


Project inputs:
XH-S3-FRONTB-WU-XU-TERMINAL-HADRON-SOURCE-EXTRAPOLATION-HARVEST-022.
MECH-S6-FRONTB-WU-XU-LOG-POPULATION-FLOOR-SOURCE-INJECTION-RESIDUAL-GATE-001.
M12-FRONTB-COUPLED-PATH-FLOOR-RESIDUAL-SMALL-GAIN-GATE-001.
REC9-M12-FRONTB-COUPLED-PATH-SMALL-GAIN-REFEREE-001.