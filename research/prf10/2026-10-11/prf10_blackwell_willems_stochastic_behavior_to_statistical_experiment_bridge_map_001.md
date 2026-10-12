---
artifact_id: PRF10-BLACKWELL-WILLEMS-STOCHASTIC-BEHAVIOR-TO-STATISTICAL-EXPERIMENT-BRIDGE-MAP-001
bw_ingestion_event_id: ING-20261011-0009
bw_qualification_state: BLACKWELL_WILLEMS_STOCHASTIC_BRIDGE
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE
archive_mode: PUBLIC_ARTIFACT
sync_state: SYNCED
source_surface: GOOGLE_DRIVE
source_revision: AHj4eMQLbEcjb6p-cFWNsXz0epl-ivKOT3a6z5ejlpjw6P-W3bCsJzJ5ujnoqLL_T_8VZ2aw5EMLk3fFTyJDyoZ0W4RlJfzg2nCQOb3vxMU
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# PRF10-BLACKWELL-WILLEMS-STOCHASTIC-BEHAVIOR-TO-STATISTICAL-EXPERIMENT-BRIDGE-MAP-001

> Public-safe mirror of the BW-linked Drive source. BW controls lifecycle/currentness; this GitHub body does not upgrade scientific authority. Private provider locators were redacted during mirroring.

BIBLIOGRAPHIC CORRECTION / SOURCE PRECISION — 2026-10-11
Willems “Open Stochastic Systems” has two source stages that must be distinguished:
- CDC-ECC 2011 conference version: “Open Stochastic Systems”, DOI 10.1109/CDC.2011.6160329;
- full journal article: J.C. Willems, “Open Stochastic Systems”, IEEE Transactions on Automatic Control 58(2), 406–421 (2013), DOI 10.1109/TAC.2012.2210836.
The probability-triple / coarse-event-sigma-algebra formulation is supported by both; the journal article is the preferred full source.
“Interconnection of Stochastic Systems” is the 2012 IFAC SYSID paper, IFAC Proceedings Volumes 45(16), 209–214, DOI 10.3182/20120711-3-BE-2027.00425.
This correction supersedes any shorthand below that cites “Willems 2011 Open Stochastic Systems” as though it were the only/final publication.
---
PRF10 — BLACKWELL ↔ WILLEMS DEEP FOUNDATION
Stochastic behavior → statistical experiment → decision
DATE: 2026-10-11
RETURN_ID: PRF10-BLACKWELL-WILLEMS-STOCHASTIC-BEHAVIOR-TO-STATISTICAL-EXPERIMENT-BRIDGE-MAP-001
0. METHOD
This rotation follows the recovered PRF phenotype:
FOUNDATION
→ THEOREM / THEORY FAMILY MAP
→ CURRENT LITERATURE
→ QUESTION COEVOLUTION
→ PRIOR-ART SUBTRACTION
→ SMALLEST SOURCE-NATIVE RESIDUAL.
No project-local gate was selected first.
1. FOUNDATION QUESTION
Initial question:
Is there a missing theoretical bridge between Willems-style behavior and Blackwell/Le Cam comparison of statistical experiments?
Question after deeper reading:
What extra structure turns a source-native stochastic process/behavior into a statistical experiment with a common parameter semantics, and when does reduction of the process induce a legal Blackwell/Le Cam randomization of the experiment?
This is a sharper and substantially more mature question.
2. BLACKWELL / LE CAM — THE RIGHT OBJECT
A statistical experiment is a measurable sample space together with a parameter-indexed family of probability measures:
E = (X, A, {P_theta : theta in Theta}).
Blackwell comparison is not an order on arbitrary models, deterministic maps or trajectory sets.
It is an information/decision order on experiments with a common state/parameter semantics.
Exact simulation / garbling:
E2 is less informative than E1 when there is a parameter-independent Markov kernel K such that
P2_theta = K P1_theta
for every theta.
Le Cam deficiency relaxes exact simulation.
For dominated Polish experiments, the one-sided deficiency is an infimum over Markov kernels of the worst-case total-variation discrepancy between the randomized P1_theta and P2_theta.
Decision meaning:
small deficiency means decision procedures in one experiment can be transferred to the other with uniformly small excess risk for bounded losses.
Primary / mature anchors:
David Blackwell, Comparison of Experiments, 1951.
David Blackwell, Equivalent Comparisons of Experiments, 1953.
Erik Torgersen, Comparison of Statistical Experiments, Cambridge, 1991.
Lucien Le Cam / Le Cam–Yang comparison and asymptotic-equivalence theory.
Ester Mariucci, Le Cam theory on the comparison of statistical models, 2016 survey.
3. WILLEMS STOCHASTIC BEHAVIOR — THE RIGHT OBJECT
Deterministic behavioral systems:
the primitive object is a behavior B, a set of admissible trajectories.
Representation is secondary.
Stochastic extension:
Willems explicitly proposed an open stochastic system as a probability triple.
The event sigma-algebra is part of the model and may be coarser than the full Borel sigma-algebra.
This is load-bearing:
STOCHASTIC SYSTEM
is not merely
DETERMINISTIC TRAJECTORY SET + NOISE LABEL.
The stochastic object includes:
- outcome/trajectory carrier;
- event sigma-algebra;
- probability law.
Later stochastic behavioral work develops:
- canonical representations of LTI stochastic processes;
- stochastic interconnection;
- random-variable / coefficient behavioral equivalences;
- stochastic versions of the fundamental lemma;
- data-driven stochastic control.
Anchors:
J.C. Willems, Open Stochastic Systems, 2011.
J.C. Willems, Interconnection of Stochastic Systems, 2012.
G. Baggio & R. Sepulchre, LTI Stochastic Processes: a Behavioral Perspective, 2017.
Behavioral theory for stochastic systems? A data-driven journey from Willems to Wiener and back again, Annual Reviews in Control 55 (2023).
4. FIRST DEEP RESULT — THE ABSTRACT BRIDGE IS ALREADY MATURE
Suppose Theta is a scientific parameter/state set and for every theta we have a stochastic process law P_theta on the SAME measurable trajectory/observation space (X,A).
Then
(X,A,{P_theta})
is already a statistical experiment.
Therefore there is no missing abstract bridge theorem at this level.
A parameterized family of stochastic behaviors / stochastic systems on a common measurable carrier is, after the parameter semantics are fixed, a statistical experiment in the standard decision-theoretic sense.
This is definitional/mature, not NASH novelty.
5. OBSERVATION AS RANDOMIZATION
Let the full process experiment be
E_full = (X,A,{P_theta}).
Let K be a parameter-independent observation/readout Markov kernel from X to an observation space Y.
Define:
Q_theta = K P_theta.
Then
E_obs = (Y,B,{Q_theta})
is a statistical experiment and is a garbling/randomization of E_full.
Therefore:
E_full >=_Blackwell E_obs.
For a deterministic measurable observation q:X→Y, K is the Dirac kernel associated with q and Q_theta=q_#P_theta.
This is the correct mature-theory statement behind the intuition that readout/coarsening cannot add universal decision information.
6. CRITICAL NON-MAPS
6.1 BEHAVIOR SET != STATISTICAL EXPERIMENT
A deterministic support/trajectory set B does not determine the family {P_theta}.
Two stochastic models may have the same support/behavior set and radically different likelihoods and decision values.
Hence:
SAME ADMISSIBLE TRAJECTORY SET
!=
SAME STATISTICAL EXPERIMENT.
6.2 PARAMETER-DEPENDENT POSTPROCESSING != BLACKWELL GARBLING
Blackwell/Le Cam randomization requires a common transition K that does not depend on the unknown theta.
If only
Q_theta = K_theta P_theta
with K_theta changing with theta,
ordinary Blackwell dominance is not established.
This distinction is highly relevant when apparatus, frame, nuisance, intervention or reduction semantics themselves depend on the candidate model.
6.3 VARYING EVENT ALGEBRA / CARRIER
If the candidate models do not live on one legally shared measurable observation space, they do not automatically form one standard statistical experiment.
A legal common carrier / measurable transport must be established first.
PAIRWISE COORDINATE RESEMBLANCE
!=
COMMON STATISTICAL SAMPLE SPACE.
6.4 PROCESS REDUCTION != OBSERVATION GARBLING
A behavioral reduction may change:
- admissible process law;
- state/history completion;
- event sigma-algebra;
- intervention semantics.
It is a Blackwell garbling only when the reduced observation law is induced by a single legal parameter-independent Markov kernel from the richer experiment.
6.5 INPUT/INTERVENTION CHANGE != GARBLING
Changing an excitation, intervention, policy or experimental design can change the family P_theta itself.
This is not ordinary postprocessing of an already fixed experiment.
Dynamic control and information-structure theory treat this separately.
7. SECOND DEEP RESULT — APPROXIMATE PROCESS-LAW REDUCTION HAS A DIRECT LE CAM BOUND
Let two parameterized process-law families share the same measurable sample space:
E1=(X,A,{P_theta}),
E2=(X,A,{Q_theta}).
Define
epsilon = sup_theta ||P_theta-Q_theta||_TV.
By choosing the identity Markov kernel in both directions:
Delta(E1,E2) <= epsilon.
Thus a UNIFORM TOTAL-VARIATION approximation of the full process-law family directly gives a Le Cam decision-theoretic approximation.
More generally, if a parameter-independent kernel K satisfies
sup_theta ||K P_theta - Q_theta||_TV <= epsilon,
then the one-sided deficiency of E1 relative to E2 is <= epsilon.
This is standard Le Cam machinery, not a new theorem.
Scientific meaning:
PROCESS-LAW APPROXIMATION
can imply
DECISION-RISK APPROXIMATION,
but only after the approximation is stated at the correct law/experiment level.
8. WHAT DOES NOT PROPAGATE AUTOMATICALLY
The following are not enough by themselves for a Le Cam / Blackwell conclusion:
- Hausdorff closeness of deterministic trajectory sets;
- closeness of one transfer function;
- small state-space matrix error;
- low prediction MSE under one input;
- matching finite moments;
- one nuisance-profiled target;
- representation similarity;
- equality of supports.
A legal inequality is needed from the native approximation object to a distance between parameter-indexed observation laws, or directly to deficiency/risk.
This is exactly where process-level approximation and decision-level approximation can separate.
9. PRIOR-ART SUBTRACTION — STOCHASTIC PROCESSES AS EXPERIMENTS ARE MATURE
Le Cam theory has long treated stochastic-process observation schemes as statistical experiments.
Mature examples include:
- discretely versus continuously observed diffusions;
- ergodic diffusion experiments versus Gaussian shift / white-noise experiments;
- jump-diffusion experiments;
- time series;
- spectral-density estimation;
- volatility experiments.
These works construct explicit Markov kernels or bound Le Cam distance between process-observation experiments.
Therefore:
STOCHASTIC PROCESS → STATISTICAL EXPERIMENT
is not an open conceptual frontier.
Likewise:
APPROXIMATE PROCESS OBSERVATION → DECISION-THEORETIC EQUIVALENCE
is a mature theorem family when the exact law-level hypotheses are available.
10. SYSTEM IDENTIFICATION NEIGHBORHOOD
System identification already intersects statistical experiment design:
- input design changes the information available for parameter identification;
- stochastic process observations induce parameterized likelihoods;
- Fisher/information criteria and optimal design are standard.
Behavioral identification adds a distinct representation-free question:
which behavior/model in a declared class is identified from finite trajectory data?
Markovsky–Dörfler 2023:
behavioral identifiability is model-class relative and requires structural prior information such as number of inputs, lag and order in the exact LTI setting.
Thus there are at least three different questions:
A. BEHAVIOR IDENTIFICATION:
which trajectory law/behavior is compatible and unique in the model class?
B. EXPERIMENT COMPARISON:
which observation structure contains more decision-relevant information about theta?
C. EXPERIMENT DESIGN:
which legal input/intervention/measurement should be chosen to generate an informative experiment?
Do not merge them.
11. DYNAMIC INFORMATION STRUCTURES
Classical stochastic-control/team theory already treats “who observes what” and the value/design of information structures.
Modern controlled-observation work also uses Blackwell-type comparisons of measurement channels.
Therefore:
BLACKWELL IN CONTROL
is mature prior art.
But the usual monotonicity requires the action/control semantics to stay legally comparable.
If the signal itself changes the feasible opportunity/action set, Blackwell’s simple “more information is always better” conclusion may fail.
Project relevance:
OBSERVATION IMPROVEMENT
and
CHANGE OF LEGAL INTERVENTION SET
must remain separately typed.
12. QUESTION COEVOLUTION
Initial candidate:
“Find a Blackwell–Willems bridge.”
After theory immersion:
too broad and largely absorbed.
Revised question:
For a source-native physical programme with parameter/hypothesis theta, when can its admissible stochastic process description be organized into ONE common experiment family {P_theta} and when does a proposed reduction/readout correspond to a theta-independent randomization K?
The residual is no longer abstract information theory.
It is SOURCE-NATIVE EXPERIMENT CONSTRUCTION.
Required objects:
PARAMETER_SEMANTICS
COMMON_MEASURABLE_CARRIER
PROCESS_LAW_FAMILY {P_theta}
LEGAL_OBSERVATION_KERNEL K
INTERVENTION / DESIGN CONTRACT
NUISANCE TYPING
TARGET / DECISION CLASS
13. SHARPER APPROXIMATE RESIDUAL
Potentially high-value project question:
Given a source-native approximation at the behavior/process level, can we prove a UNIFORM law-level bound strong enough to control Le Cam deficiency and therefore bounded decision risk?
The mature theorem chain is available once we establish:
PROCESS APPROXIMATION
→ UNIFORM DISTANCE BETWEEN {P_theta} AND {Q_theta}
→ LE CAM DEFICIENCY
→ TARGET/DECISION-RISK TRANSFER.
The open work is the FIRST ARROW for a concrete source-native model.
This is a much sharper research target than inventing a generic Blackwell–Willems “gate”.
14. IMPLICATION FOR LIVING THEORY / DRAFT016 LANGUAGE
Recommended conceptual decomposition:
P — PROCESS / BEHAVIOR LAYER
What source-native trajectories or process laws are admitted?
Hosts: behavioral systems, realization, stochastic processes, lumpability/process theory.
E — EXPERIMENT / OBSERVATION LAYER
What parameter-indexed law is actually observed?
Hosts: statistical experiments, observation channels, filtering, experimental design.
D — DECISION / TARGET LAYER
Which losses/targets are preserved or approximately preserved?
Hosts: Blackwell, Le Cam, target-specific sufficiency/partial identification.
Hence:
PROCESS-FAITHFUL
!=
EXPERIMENT-EQUIVALENT
!=
DECISION-EQUIVALENT.
But these are mature distinctions.
Do not promote them as a new TPE law.
15. WHAT THE LITERATURE KILLED / ABSORBED
Absorb as mature:
- generic “behavior-to-experiment” bridge at probability-law level;
- generic observation-as-garbling;
- generic decision-risk transfer from small deficiency;
- stochastic-process comparison as statistical experiments;
- Blackwell informativeness for fixed observation channels;
- model-class-relative behavioral identifiability.
Killed as over-broad project residual:
“Blackwell and Willems need a new unifying mathematical theory.”
No evidence supports that.
16. WHAT SURVIVES
Surviving PRF-worthy source questions:
R1 SOURCE-NATIVE EXPERIMENT CONSTRUCTION
Can the project’s candidate physical/source family be placed on one common measurable carrier with one parameter semantics?
R2 PARAMETER-INDEPENDENT READOUT
Is the proposed observation/reduction one common Markov kernel, or does it depend on the unknown candidate/state/history in a way that invalidates ordinary Blackwell comparison?
R3 LAW-LEVEL APPROXIMATION
Does the project approximation control the entire parameter-indexed observation law uniformly, not merely trajectories/moments/one target?
R4 INTERVENTION/DESIGN SEMANTICS
Does changing tester/input preserve the same experiment family, or create a new controlled experiment/design problem?
These are source-binding questions, not new general theory.
17. FOUNDATION STATUS
BLACKWELL/TORGERSON/LE_CAM = FOUNDATION SUFFICIENT FOR current comparison/deficiency decision class.
WILLEMS DETERMINISTIC + STOCHASTIC BEHAVIOR = FOUNDATION SUFFICIENT FOR current bridge-typing decision class.
SYSTEM IDENTIFICATION / EXPERIMENT DESIGN = INITIAL BRIDGE PASS.
DYNAMIC INFORMATION STRUCTURE / CONTROL = INITIAL BRIDGE PASS.
No claim of exhaustive field coverage.
18. NEXT THEORY-FIRST READING IF THIS LINE REMAINS PRIORITY
Priority backbone:
1. Torgersen — deficiency, equivalence, representations, comparison of linear models.
2. Le Cam & Yang — asymptotics and experiment comparison.
3. Polderman & Willems — behavioral systems foundations.
4. Willems — Open / Interconnected Stochastic Systems.
5. stochastic behavioral fundamental-lemma literature.
6. Ljung and classical optimal input/experiment-design literature.
7. stochastic control information-structure / observation-channel comparison literature.
Only after this:
select a concrete NASH source family and test R1–R4.
19. STATUS
BLACKWELL_WILLEMS_GENERIC_UNIFICATION = ABSORBED / NOT A NEW THEORY FRONT.
STOCHASTIC_BEHAVIOR_TO_STATISTICAL_EXPERIMENT =
MATURE DEFINITIONAL BRIDGE when common parameterized measurable law family exists.
OBSERVATION_TO_BLACKWELL_GARBLING =
MATURE when one theta-independent Markov kernel exists.
UNIFORM_TV_PROCESS_LAW_APPROXIMATION_TO_LE_CAM =
MATURE / EXACT UPPER BOUND.
SOURCE_NATIVE_EXPERIMENT_CONSTRUCTION =
CLAIM-LOCAL OPEN.
CROSS_LAYER_APPROXIMATION_FIRST_ARROW =
SOURCE-DEPENDENT OPEN.
NOVELTY_CANDIDATE = NONE.
NO CANON.
NO EXEC_SIGN.
NO PHYSICAL UPGRADE.
ROLE CHECK:
FOUNDATION_FIRST = PASS.
QUESTION_COEVOLUTION = MATERIAL.
LOCAL_GATE_FIRST = NOT USED.
PRF PHENOTYPE = RESTORED FOR THIS ROTATION.
