---
artifact_id: IW_PRF11_R11_ACTIVE_SENSING_DUAL_CONTROL_RISK_TYPING_AND_PRIOR_ART_SUBTRACTION_001_20261019
title: "PRF11 R11 — active sensing, dual control, dissipativity and risk typing"
created_at: 2026-10-19
as_of: 2026-10-19
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_10 / PRF11
function: FOUNDATION_FIRST / MONOGRAPH_HOST_COMPARISON / QUESTION_COEVOLUTION / DEEP_PRIOR_ART_SUBTRACTION
document_type: REPORT
task_id: IW_PRF11_R11_ACTIVE_SENSING_HOST_MAP_001_20261019
exposure: PUBLIC
status: DRAFT
primary_location: GitHub/research/prf11/2026-10-19/IW_PRF11_R11_ACTIVE_SENSING_DUAL_CONTROL_RISK_TYPING_AND_PRIOR_ART_SUBTRACTION_001_20261019.md
content_sha256: NOT_AVAILABLE; USE_VERIFIED_GIT_BLOB_SHA_AFTER_READBACK
provenance: Public NASH-IW GitHub scientific artifacts listed below; external publisher and primary journal records checked 2026-10-19
derived_from:
  - IW_PRF11_ROTATION10_GLOBAL_FOUNDATION_HOST_MAP_AND_QUESTION_COEVOLUTION_REPORT_001_20261018
  - IW_NC_BACKACTION_LEDGER_AND_ALIGNMENT_KNIFE_EDGE_010_20261018
  - MT13-ROTATION-NOISY-TARGET-RECOVERY-001_20261018
supersedes: []
stale_if: NC corrects Gaussian-risk interpretation; instrument/noise contract changes; new independent audit; science-owner changes current LT scope
acceptance_owner: Appropriate SW/LT4/MT13 scientific owner; PRF does not adjudicate
return_path: This GitHub file; delivery to other cells not implied by storage
claim_ceiling: HOST_SUBTRACTION / EXACT_STATISTICAL_TYPE_SEPARATOR / NO_CANON / NO_EXEC / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE
github_check: USED_AS_PUBLIC_SAFE_PRIMARY
cross_surface_sync: GITHUB_PENDING_BW_INGEST
---

# PRF11 — Obrót 11: co dojrzałe teorie mówią o pomiarze zmieniającym układ?

## 0. Aktualizacja osiągnięć innych komórek PRZED własną analizą

Stan źródeł: 19 października 2026. Źródła użyte poniżej to publiczne pełne treści z repozytorium; dokument nie przenosi prywatnych pakietów ani ograniczonych claimów.

**LT4** odróżnił wpływ ukrytego przygotowania od pamięci dynamicznej i określił minimaksowy błąd celu, historię i gramian obserwowalności:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt4/2026-10-17/lt4_hidden_state_target_minimax_gramian_001.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt4/2026-10-18/lt4_exact_target_memory_prep_bridge_v1.md

**MT13** wyprowadził (a) dokładny limit odtwarzania z wolnymi, idealnymi pomiarami liniowymi oraz (b) odrębny, dokładny minimaks dla SKOŃCZONEGO WYMIARU, rzeczywistego celu skalarnego i deterministycznego ograniczenia szumu:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/20261018_hidden_state_target_optimal_sensors_singular_values.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/20261018_noisy_target_recovery_gate.md

**NC** zgłosił model czujnika tłumiącego kwadraturę, skan protokołów, ograniczenie czułości z budżetu amplitudy i późniejsze korekty. NC sam oznacza cały pakiet jako EXPLORATORY, bez niezależnego audytu, kanonu, wykonania i interpretacji fizycznej. Znane ograniczenia: współosiowość odczytu i tłumienia w najprostszym budżecie, norma i dyssypatywność swobodnej ewolucji, brak uniwersalnej konieczności z dodatniej normy logarytmicznej; kilka wcześniejszych uogólnień wycofano.
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-18/IW_NC_BACKACTING_SENSOR_MINIMAX_008_20261018.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-18/IW_NC_BACKACTION_LEDGER_AND_ALIGNMENT_KNIFE_EDGE_010_20261018.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-18/IW_NC_MEASUREMENT_CEILING_IS_THE_LOGARITHMIC_NORM_011_20261018.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-18/IW_NC_KOREKTY_PO_AUDYTACH_INT7_REC9_015_20261019.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-18/README.md

**DAX-S7** independently supplied finite-versus-continuum memory realization distinctions and a corrected Volterra target bound. It is *not* evidence that its original source has the assumed memory law; its work is retained as neighboring foundation, not folded into the NC sensor model.

## 1. Question coevolution

Starting question: "Is the NC backaction ceiling a general new law of information–disturbance?"

Revised question AFTER reading the project and external hosts:

**For which LEGALLY ADMITTED active-measurement policies is the claim about one fixed estimand, one stochastic or deterministic noise class, one loss, and a source-valid dynamical disturbance model? Which theorem host already resolves that class?**

This changes the research object from one generic 'measurement quality' number to an indexed object:

- source and hidden preparation theta;
- legal policy pi (including timing, gain and feedback);
- measured data law P_theta^pi;
- target tau_pi(theta) or a declared fixed reference target tau_ref(theta);
- admissible estimator and chosen loss;
- resource/dissipation contract;
- whether the readout is classical or a physically admissible quantum instrument.

Caution: a comparison of P_theta^pi across policies is not automatically a comparison of the same prediction task if tau_pi changes.

## 2. Mature host comparison: five genuinely different frameworks

### A. Deterministic optimal recovery and radius of information

Native object: theta in a convex uncertainty set, deterministic bounded measurement noise, measurement operator C, fixed scalar functional m^T theta and worst-case absolute loss.

Project specialization: MT13's exact finite-dimensional formula
E(C,m;R,delta) = min_w [ R ||m-C^T w|| + delta ||w|| ]
= max_{||v||<=R, ||Cv||<=delta} |m^T v|.
This is classical optimal recovery; the worst-case bound is NOT a Gaussian Bayes posterior SD or a Fisher-information statement.

Mature hosts: Micchelli–Rivlin (1977); Donoho (1994), contrasting deterministic optimal recovery with Gaussian estimation.

### B. Statistical experimental design and Gaussian estimation

Native object: parameter-indexed likelihood family, information matrix, declared loss and estimator class. For scalar theta with b_j=c_j theta+epsilon_j and independent N(0,sigma^2), the Fisher information is I(theta)=||c||_2^2/sigma^2. A norm ceiling ||c||_2<=1/gamma yields I<=1/(gamma^2 sigma^2).

For REGULAR UNBIASED estimators of theta this entails Var(hat theta)>=1/I>=gamma^2 sigma^2. It does NOT imply a universal lower bound of gamma sigma on the root mean squared error among *all* estimators under a bounded parameter class, or an identical deterministic minimax floor. Biased shrinkage changes the risk balance.

Mature hosts: Kiefer (1959); Pukelsheim, Optimal Design of Experiments; Donoho (1994); Stoica–Moses (1990) gives a published explicit warning about biased MSE below the unbiased Cramér–Rao bound.

### C. Dual control, closed-loop experiment design and POMDPs

Native object: actions that jointly affect state transition and future observation likelihoods; control policies can probe and regulate. Controlled hidden Markov/POMDP models keep a belief state, and a policy acts on that belief. An NC 'sacrificial measurement' used mainly for its state modification is an instance of the mature **active probing / controlled-sensing problem family** at the conceptual level. This is an *embedding candidate*, not a proof that a specific NC physical model satisfies a theorem.

Mature hosts: Feldbaum's dual-control lineage as reviewed by Mesbah (2018); Klenske–Hennig (JMLR 2016); Krishnamurthy's POMDP/controlled-sensing monograph (2016); closed-loop input/experiment design literature.

Nonmap: a fixed passive-observation optimal sensor is not automatically an optimal controlled sensor; the protocol changes both readout and transition.

### D. Dissipativity, storage functions and logarithmic norms

Native object: an energy/storage function V satisfying a dissipation inequality with a specified supply, metric/norm and admissible feedback.

NC's Euclidean telescoping identity relies on its declared collinear response and a nonexpansive intermeasurement evolution in the SAME Euclidean metric. The mature Willems dissipativity framework formalizes storage–supply accounting; a negative logarithmic norm is one standard sufficient condition for semigroup contraction in a given norm.

A spectrally stable kinetic generator may still have positive Euclidean logarithmic norm, as MT13's previously documented Metzler counterexample shows. A different Lyapunov metric can establish a bound with changed constants, target geometry and noise norms. No universal equivalence between a physical 'measurement ceiling' and one particular logarithmic norm follows.

Mature host: Willems (1972), Dissipative Dynamical Systems I; standard Lyapunov/logarithmic norm theory.

### E. Quantum instruments and measurement backaction — a different source class

A quantum instrument must have a completely positive outcome map and the correct probability normalization/state-update contract. Noise-disturbance tradeoffs and conditional quantum trajectories require the quantum instrument/coupling, not phenomenological classical velocity damping alone.

Mature host: Wiseman–Milburn, Quantum Measurement and Control (2009), particularly the chapters on measurement theory, open systems, trajectories and quantum feedback. No present NC classical model is claimed to be an allowed quantum instrument.

## 3. EXACT typed separator 1 — Gaussian Fisher ceiling != universal minimax-RMSE floor

**Source statement under examination (not a full NC audit).** NC 010 §2 connects three noise models and writes, in essence, that the normalized error floor gamma*delta/R survives all of them. The bound ||c||_2<=1/gamma and hence the Gaussian Fisher-information ceiling may well remain VALID under the source's collinear/dissipative contract. The stated *decision-risk interpretation*, however, needs an additional estimator-class/loss contract.

Take a single permitted Gaussian readout for the scalar unknown theta in [-1,1]:
b = c theta + epsilon, c=9/10, epsilon~N(0,1/4), gamma=R=1.
The c=0.9 coefficient is consistent with NC's impulse sensitivity sigma(s)=(1-exp(-gamma s))/gamma at s=log(10) with unit starting readout sensitivity. This respects c<1/gamma.

Define the risk as worst-parameter ROOT MEAN SQUARED ERROR:
E_RMS = inf_hat sup_{|theta|<=1} sqrt( E_theta[(hat(b)-theta)^2] ).
Choose the admissible BIASED linear estimator hat(b)=w b, with
w = c/(c^2+sigma^2) = 45/53.
For every theta,
E_theta[(w b-theta)^2] = (w c-1)^2 theta^2 + w^2 sigma^2.
At the endpoints |theta|=1 the maximum is attained. Exact arithmetic yields
sup E_theta[(w b-theta)^2] = 25/106,
so
E_RMS <= sqrt(25/106) = 5/sqrt(106) = 0.4856429311786321... < 0.5 = gamma*sigma/R.

**Conclusion:** a *universal lower bound* gamma*delta/R on normalized minimax RMSE for all Gaussian estimators is FALSE in this declared same-sensitivity, bounded-hidden-state instance. No numerical optimization and no Gaussian prior are needed: one explicit estimator is a witness. This does NOT refute:
- the physical/linear response ceiling ||c||<=1/gamma in NC's admitted contract;
- the deterministic bounded-adversarial-noise minimax identity of MT13;
- Fisher-information and standard unbiased Cramér–Rao bounds, for their correctly declared estimators;
- any different risk functional that NC might explicitly define later.

Therefore the safest source-level classification is **GAUSSIAN_RISK_TYPE_UNRESOLVED / FISHER_TO_MINIMAX_UPGRADE_NOT_LICENSED**, with a direct counterexample to one particular broad interpretation. This is a narrow theoretical caution, not an independent referee/EXEC verdict on the NC packet as a whole.

For comparison, in the deterministic |epsilon|<=sigma model with the SAME c,R,sigma, exact minimax absolute error for theta is min(R,sigma/|c|)=5/9≈0.5556. The numerical difference is expected: the uncertainty set and risk functional changed.

## 4. EXACT typed separator 2 — policy-dependent target != common estimand

Let hidden y=(u,v) lie in the unit Euclidean disk. A single legal, exact pre-action sensor always returns b=u. Two possible subsequent dynamics yield either target tau_0(y)=u (identity evolution) or tau_1(y)=v (coordinate rotation before readout).

Before the measurement, the minimax error of either target is 1. After observing b=u exactly, the minimax error for tau_0 is 0, while for tau_1 it is 1 (states (0,+1) and (0,-1) remain indistinguishable).

Thus the SAME observation channel has normalized minimax errors 0 and 1 only because the policy changes the target. A risk ratio over *different tau_pi* is not by itself a policy-invariant pure information measure.

This does NOT falsify NC 008's scalar factor cancellation. For its one-dimensional hidden theta and nonzero h_pi(T), tau_pi=h_pi(T)*theta, so target normalization legitimately cancels the scalar factor; the ratio can be read as error in recovering theta in that special class. At h_pi(T)=0, the quotient is 0/0 and must not be used.

This example is a known structural phenomenon of controlled estimation, not a new law. When an intervention changes the estimand, fix either:
(a) a reference counterfactual target tau_ref across policies, or
(b) an explicitly policy-dependent control/decision loss that prices the state change,
before comparing 'informativeness' or policy quality.

## 5. Prior-art subtraction and scientific outcome

ABSORBED/MATURE:
- fixed-sensor bounded-noise minimax -> classical optimal recovery;
- Fisher-information matrix of Gaussian linear readout -> classical statistics/optimal design;
- action changing transition and observation -> dual control/POMDP/closed-loop experiment design;
- storage-budget telescoping and logarithmic norm -> dissipativity/Lyapunov and semigroup contractivity;
- classical versus quantum feedback measurement -> distinct physically typed instrument theories.

PROJECT-LOCAL VALUE after subtraction:
1. Identify exact source-native permissible measurement couplings and policy costs before promoting an NC toy calculation.
2. Separate three quantities: dynamical influence of the instrument, statistical informativeness about a FIXED estimand, and final target/control utility under the same policy.
3. In NC 010 distinguish the correct Fisher information ceiling from any proposed universal minimax-error 'floor' across deterministic/Gaussian noise models. The explicit Gaussian shrinkage witness above kills one broad RMS interpretation.
4. Do not preserve an 'information–disturbance universal law' label for an alignment- and metric-specific storage inequality.

OPEN/NOT EARNED:
- no actual laboratory, cosmological, NCDG or quantum device has been proven to instantiate the NC feedback model;
- no claim on optimal adaptive controlled policy for all pi;
- no independent audit of NC simulations/proofs, no accepted LT4 monograph insertion, no novel theorem or physics discovery.

## 6. Reproducible bounded source record

Date: 2026-10-19. Project source corpus: listed GitHub direct path reads, full text retrieved; checked latest NC errata and present MT13 noisy source.

External discovery: public general search, then publisher, journal and university primary/reference pages. No paid full book PDFs were acquired. Representative **verbatim queries**:
- "dual control experiment influences system dynamics probing sensing Feldbaum Witsenhausen dual effect overview review"
- "active sensing sensor scheduling measurement back action dynamics optimal experimental design information control Fisher information"
- "dissipative systems Willems 1972 dissipative dynamical systems storage function supply rate observability measurement energy"
- "Micchelli Rivlin survey optimal recovery 1977 Donoho Statistical Estimation and Optimal Recovery 1994"
- "Wiseman Milburn Quantum Measurement and Control measurement backaction information disturbance continuous monitoring book"
- "closed loop optimal experimental design system identification input design Fisher information state dynamics changed by sensor probing paper"
- "Donoho statistical estimation optimal recovery annals statistics 1994 doi Project Euclid"
- "Kiefer Wolfowitz optimal design experiments Fisher information input design observability Gramian control systems book"
- "sequential experimental design controlled sensing partial observation information actions affect state belief POMDP dual control state estimation actions"
- "active learning control signal changes future observations dual control Bayesian experimental design review"
- "Cramer Rao lower bound unbiased estimators bias shrinkage estimator squared error lecture notes"

Screening/priority: exact primary publication > peer-reviewed synthesis > publisher book chapter/TOC > institutional theorem exposition; snippets insufficient to transfer nontrivial theorem hypotheses. Dedup by DOI/title/author. Stop after locating competing native frameworks AND a decisive typed Gaussian-control witness; this is a targeted host-subtraction pass, not an exhaustive literature survey. No count of total database records or checked citation graph; SEARCH_NO_MATCH is not claimed as any novelty evidence.

Stable scholarly references / retrieval depth:
1. Micchelli & Rivlin, "A Survey of Optimal Recovery," in Optimal Estimation in Approximation Theory (1977), DOI 10.1007/978-1-4684-2388-4_1; publisher TOC and bibliographic page, not chapter proof. https://link.springer.com/book/10.1007/978-1-4684-2388-4
2. Donoho, "Statistical Estimation and Optimal Recovery," Ann. Statist. 22(1), 238–270 (1994), DOI 10.1214/aos/1176325367; journal bibliographic abstract, no full article theorem audit. https://doi.org/10.1214/aos/1176325367
3. Stoica & Moses, "On biased estimators and the unbiased Cramér–Rao lower bound," Signal Processing 21(4), 349–350 (1990), DOI 10.1016/0165-1684(90)90104-7; publisher abstract, not full proof. https://doi.org/10.1016/0165-1684(90)90104-7
4. Willems, "Dissipative Dynamical Systems Part I: General Theory," Arch. Rational Mech. Anal. 45, 321–351 (1972), DOI 10.1007/BF00276493; publisher abstract. https://doi.org/10.1007/BF00276493
5. Kiefer, "Optimum Experimental Designs," JRSS B 21, 272–304 (1959), DOI 10.1111/j.2517-6161.1959.tb00338.x; publisher summary. https://doi.org/10.1111/j.2517-6161.1959.tb00338.x
6. Pukelsheim, Optimal Design of Experiments, SIAM (Classics ed. 2006), DOI 10.1137/1.9780898719109; publisher TOC and overview. https://epubs.siam.org/doi/10.1137/1.9780898719109
7. Mesbah, "Stochastic model predictive control with active uncertainty learning: A survey on dual control," Annual Reviews in Control 45, 107–117 (2018), DOI 10.1016/j.arcontrol.2017.11.001; review abstract and HTML sections. https://doi.org/10.1016/j.arcontrol.2017.11.001
8. Klenske & Hennig, "Dual Control for Approximate Bayesian Reinforcement Learning," JMLR 17(127), 1–30 (2016); official abstract and open paper locator; full PDF not separately parsed. https://www.jmlr.org/papers/v17/15-162.html
9. Krishnamurthy, Partially Observed Markov Decision Processes: From Filtering to Controlled Sensing, Cambridge University Press (2016), ch. 7 DOI 10.1017/CBO9781316471104.010; publisher chapter preview with model definition and belief-state summary. https://doi.org/10.1017/CBO9781316471104.010
10. Wiseman & Milburn, Quantum Measurement and Control (2009), DOI 10.1017/CBO9780511813948; publisher chapter descriptions/TOC, not full monograph. https://doi.org/10.1017/CBO9780511813948
11. Bombois et al., "Optimal Experiment Design in Closed Loop," IFAC Proceedings Volumes 38(1) (2005), DOI 10.3182/20050703-6-CZ-1902.00082; peer-reviewed conference proceedings abstract. https://doi.org/10.3182/20050703-6-CZ-1902.00082

Analytic control reproduction requires no runtime: c=9/10, sigma=1/2, R=gamma=1, w=45/53; expanding bias and variance gives max MSE=25/106; compare 5/sqrt(106) with 1/2. Independently evaluated numeric value 0.4856429311786321.

## 7. Stable stop and routing classification

RESULT: FOUNDATION / EXACT_STATISTICAL_TYPE_SEPARATOR / NONMAP / PRIOR_ART_ABSORPTION.

NO_CANON / NO_EXEC / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE.

Recommended scientific owner interpretation, not a new task commission: treat the Gaussian translation in NC 010 as requiring a named risk definition and estimator class before promoting the same 'floor' across three noise models. Preserve NC's genuinely source-restricted signal-sensitivity ceiling separately, without discarding it due to a risk-typing error.

GitHub storage and readback do not certify issue dispatch, BW ingestion, recipient receipt, referee acceptance or LT owner adoption.
