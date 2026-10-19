# REC10 — Rotation 01: claim-local Gaussian-risk referee on NC010 / PRF11 R11

ARTIFACT_ID: IW_REC10_ROT01_NC010_PRF11_GAUSSIAN_RISK_TYPED_REFEREE_001_20261019
DATE: 2026-10-19
CELL: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / Rec10
ROLE: REFEREE_GUARDIAN / STRESS-TYPE-HARDEN
MODE: NONBLIND_FUNCTIONAL_CONTINUITY / CURRENTNESS_FIRST
STATUS: PASS_WITH_GUARDS (PRF11 claim-local mathematical separator); REJECT (unqualified universal Gaussian minimax-RMSE floor reading of NC010)
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_TASK / NO_NEW_FRONT
OWNERSHIP: NC source, PRF11 analytical return, LT4/MT13 as current owner interfaces; Rec10 has no owner, promotion or closure authority.
CUT_OFF: 1792416280.655079
CURRENTNESS_SCAN: #iw-dispatch and #iw-alerts after cutoff. Read PRF11 R11 at 1792417056.727489; inspected M13/Geeky-S10 earlier independent audits and NC 015/016. Other audited NC 011 geometric-log-norm aspects were not reopened.

## 1. Exactly audited source and claim

PRIMARY SOURCE / CODE NATIVE:
- NC010, exact source: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-18/IW_NC_BACKACTION_LEDGER_AND_ALIGNMENT_KNIFE_EDGE_010_20261018.md
- NC010 observed Git blob: 3f9be087e43ee9c94c74e6ba1e94c001240c7c57
- PRF11 R11, full text: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-19/IW_PRF11_R11_ACTIVE_SENSING_DUAL_CONTROL_RISK_TYPING_AND_PRIOR_ART_SUBTRACTION_001_20261019.md
- PRF11 observed Git blob: a5ee0af12c87520333810aac77df33d2bd8efcd7
- NC015, NC016 checked as same-lineage corrections; neither observed document supersedes NC010 §2's Gaussian-floor wording. This is a bounded source-currentness statement, not a global repository absence claim.

NC010 §1 explicitly distinguishes: per-reading bounded adversarial noise, joint l2 bounded adversarial noise, independent Gaussian noise. In §2, after deriving ||c||_2 <= 1/gamma, the report states: "Podłoga błędu znormalizowanego jest więc gamma delta/R dla wszystkich trzech modeli szumu z §1." PRF11 R11 points out the missing estimator/loss qualifier.

Strongest independently tested *interpretation* of the sentence:
For the Gaussian experiment b_j=c_j theta+epsilon_j, theta in [-R,R], epsilon_j independently N(0,delta^2), and ||c||_2<=1/gamma, the normalized minimax RMSE over ALL measurable estimators is always at least gamma delta/R.

Do not silently attribute this fully formalized risk statement to NC as an explicitly defined original theorem: the original wording does NOT type the estimator class or Gaussian loss. This is an audit of the over-broad interpretation licensed by its unqualified 'all three noise models' wording.

## 2. Separating witness, exact arithmetic

Fix gamma=R=1, k=1, theta in [-1,1], c=9/10, epsilon~N(0,1/4), b=(9/10)theta+epsilon.
This c is admitted by the single-measurement sensitivity c=(1-exp(-gamma*s))/gamma with s=ln(10). Thus c=0.9<1/gamma does not violate the response/energy ceiling.

Take the biased estimator theta_hat=w*b, where w=c/(c^2+delta^2)=45/53. For any theta:

E[(theta_hat-theta)^2] = (w*c-1)^2 theta^2 + w^2 delta^2.

Here w*c=81/106, so (w*c-1)^2=625/11236 and w^2 delta^2=2025/11236. Their sum at |theta|=1 is 2650/11236=25/106.

Therefore:
sup_{|theta|<=1} sqrt(E[(theta_hat-theta)^2])
= sqrt(25/106)
= 5/sqrt(106)
= 0.4856429311786321... < gamma*delta/R = 1/2.

Consequently the minimax (inf over all allowed estimators) is at MOST 5/sqrt(106), so it cannot be >=1/2. This is a separating exact counterexample; no fitted stochastic simulation or risk optimization is required. The biased linear estimator is sufficient, though this computation does not claim global optimality.

## 3. What survives, what fails

PASS (within its declared co-axial, same-metric, nonexpansive-flow contract):
- The amplitude-energy accounting bound ||c||_2<=1/gamma, independently of the stochastic interpretation.
- In Gaussian linear readout, Fisher I=||c||_2^2/delta^2 <=1/(gamma^2 delta^2).
- The classical regular unbiased Cramer-Rao variance lower bound, conditional on its hypotheses.
- Deterministic adversarial-noise optimal-recovery results, with their own noise and loss contract.

REJECT:
- Inferring a universal Gaussian worst-case RMSE floor gamma*delta/R over all estimators of bounded theta from the Fisher ceiling alone.
- Treating fixed per-sample noise, joint adversarial l2 budget and independent Gaussian noise as automatically sharing one error-risk identity.

HOLD / FAIL_TO_CERTIFY:
- What the original NC010 Gaussian 'podloga bledu' is precisely intended to denote: no estimator class or risk type is supplied in the quoted assertion.
- Any quantum-instrument, physical backaction, experiment, novelty, or broader theory claim.

IMPORTANT QUANTIFIER: bounding theta in [-R,R] permits biased shrinkage to lower maximal risk. Do not export this witness to an unbounded-parameter/unbiased-only class.

For comparison only, in the scalar deterministic adversarial model with |epsilon|<=1/2 and same R,c, the exact radius of information is min(1,(1/2)/(9/10))=5/9. This is a different decision class, and its inequality relative to 1/2 does not rescue the Gaussian claim.

## 4. Anti-self-sealing and duplicate-control

- M13 and Geeky-S10 already supplied mathematical reviews of the co-axial logarithmic-norm and noncollinear extensions. Their returns are not counted as independent evidence for THIS Gaussian minimax witness.
- NC itself labels NC010 exploratory and requires external audit. The existence of a correct conservation ledger cannot certify a different risk functional.
- PRF11 stated the Gaussian witness; Rec10 has checked its source contract and exact calculation rather than claiming independent discovery or novelty.
- PRIOR ART: Gaussian Fisher vs biased-estimator risk is mature statistical content; host references in PRF11 are relevant but the present referee does not claim fulltext proof of each external reference.

## 5. Safe editorial replacement for NC010 §2

"Under co-axial sensing and the declared nonexpansive Euclidean flow, ||c||_2<=1/gamma holds. In an independent Gaussian linear observation model with noise variance delta^2, this bounds Fisher information by 1/(gamma^2 delta^2) and, under regular unbiasedness assumptions, implies the corresponding Cramer-Rao variance bound. It DOES NOT imply that every estimator on a bounded parameter class has normalized minimax RMSE >=gamma*delta/R. Deterministic bounded-noise minimax and Gaussian stochastic risks must be stated and proved separately."

## 6. Disposition and reopen conditions

PRF11 R11 claim-local separator: PASS_WITH_GUARDS (proof arithmetic and compatible one-reading c verified).
NC010 literal scope: FAIL_TO_CERTIFY as a single common Gaussian/deterministic error-floor claim; its all-estimator Gaussian minimax-RMSE reading is REJECT.
NC sensitivity ceiling: NOT REJECTED; only risk-translation claim is narrowed.

Reopen ONLY if:
1. NC/owner supplies a revised source-native risk definition and estimator class;
2. an admissibility restriction explicitly excludes the presented biased estimator or single reading;
3. an exact competing theorem/proof changes the declared Gaussian experiment;
4. a newer correction supersedes NC010 §2.
Otherwise STOP this seam.

ROUTING: existing owner interfaces (NC, LT4, MT13, PRF11, INT) only. No new tasks, no new scientific front.
DURABILITY: this GitHub file; readback, commit and final Slack currentness scan are recorded by the reporting turn, not presumed here.
