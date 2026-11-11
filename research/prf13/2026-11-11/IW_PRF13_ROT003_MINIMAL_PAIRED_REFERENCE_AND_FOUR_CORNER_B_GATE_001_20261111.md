---
artifact_id: IW_PRF13_ROT003_MINIMAL_PAIRED_REFERENCE_AND_FOUR_CORNER_B_GATE_001_20261111
created_at: 2026-11-11
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_12 / PRF13
source_type: SOURCE_TYPED_ANALYTIC_MODEL_THEOREM_WITH_REPRODUCED_NUMERICAL_FIXTURES
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: CONDITIONAL_FOUR_CORNER_B_GATE / ONE_SCALAR_THETA_IDENTIFIABILITY / FIXED_N_RESOURCE_FIXTURES / REFEREE_PENDING
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_HARDWARE / NO_EXPERIMENTAL_JOINT_REFERENCE / NO_ARBITRARY_COPULA_EXTENSION / NO_ORIGINAL_3Q_LOCC_CLOSURE
---

# PRF13 ROT003 — Minimal paired readout reference, exact four-corner B gate, and joint calibration overhead

**Scientific finding:** In the restricted correlated-detector family proposed in PRF13 ROT002, conditional on the unchanged PRF12 R31 source-B model, a single *source-independent prepared ideal (--)* two-shot reference identifies the mixing weight `theta`, even though all original one-shot detector references fail to identify it. When detector single-shot response probabilities `p0,p1` are uncertain in a simultaneous rectangular confidence set but COMMON to the two terminal readout shots of each science pair, the global source-B score is a convex function of `(p0,p1)`. Consequently, an EXACT robust conditional B upper bound is obtained from FOUR corners, and not from a crude additive error-budget split. Explicit fixed-design exact-binomial reference counts show a steep statistical cost near the admissible threshold. This is model-conditional mathematics, not an empirical instrument result.

## Primary source and mature-host inventory

- **PRF12 R31 source proof:** https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-03/IW_PRF12_R31_NINE_CLASS_COMPOSITE_E_OPTIMALITY_BRACKET_AND_FIXED_N_1666_001_20261103.md. Borrowed source-B Lindblad means and fixed score coefficients; source-A all-real-Xi global proof NOT rerun in ROT003.
- **PRF12 R34 nonstationary reference:** https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-10/IW_PRF12_R34_VARIANCE_ADAPTIVE_NONSTATIONARY_REFERENCE_ANYTIME_CERTIFICATE_001_20261110.md. Borrowed difference between reference confidence bounds, science readout conditional independence, and exogenous detector-drift requirement. Its 46055 reference readings are ONE SYNTHETIC FIXTURE, not a new empirical benchmark.
- **PRF13 ROT001 copula no-go:** https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf13/2026-11-11/IW_PRF13_ROT001_PAIR_READOUT_COPULA_SCORE_RESPONSE_GATE_001_20261111.md.
- **PRF13 ROT002 source-B copula falsifier:** https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf13/2026-11-11/IW_PRF13_ROT002_SOURCE_B_SHARED_LATCH_SHARP_MIXTURE_THRESHOLD_001_20261111.md; 70-dps independent Lindblad generator replay retained there; ROT003 code copies its 30-digit source-B means, without re-solving Lindblad.
- **Mature theory:** Frechet-Hoeffding bivariate Bernoulli coupling; Chernoff/Ville nonnegative supermartingales, Clopper-Pearson one-sided binomial inversion, [Howard et al. 2021](https://doi.org/10.1214/20-AOS1991) time-uniform confidence sequences; [Bravyi et al., PRA 103 042605 (2021)](https://doi.org/10.1103/PhysRevA.103.042605) correlated Markovian readout models. Analogous full assignment-matrix calibration is established. There is **no novelty or priority claim** for any of these mathematical hosts or for this application.

## 1. Frozen assumptions (essential for every subsequent statement)

1. PRF12 source B unchanged: two freshly prepared shots with source-ON finite controls, independent Cauchy-Levy increments, same private axis `j` per pair; the corresponding ideal-plus probability of either shot is `r_j=(1+m_B,j)/2`. The two ideal Z outcomes are independent conditional on relevant history.
2. The source-independent **classical terminal readout** has one-shot assignment probabilities `p0=P(R=+|ideal +)`, `p1=P(R=+|ideal -)`, with `0<p1<=p0<=1`. They are COMMON to both shots within each pair for the core four-corner theorem. Coherent joint POVMs, source-dependent readout and uncontrolled between-shot memory are outside scope.
3. Before the current ideal pair, a predictable Bernoulli selector with mixing probability `theta` independently selects (a) ordinary shotwise independent error uniforms, or (b) one common fresh uniform threshold variable `U` for both recorded signs. The selector, errors, and private scoring coin do not anticipate the current ideal quantum outcomes. Selector is fresh between science pairs. In calibration controls, the SAME detector family and temporal protocol apply.
4. PRF12 score: axes `w=(.18,.20,.62)`, score on registered `++`: `a=(.943,.907,.347)`, on `--`: `b=(1,1,.018)`, mixed: `0`; a fresh private coin converts score into Bernoulli Y. These coefficients belong to the R31 original source.
5. A reference labelled ideal `(--)` must actually implement two known ideal-minus detector inputs at matching readout timings, independently of the source and unknown Xi. The availability and validity of such a reference **are not established** by the archived R34 singleton reference. Detector state preparation error and timing differences are unmeasured obstructions.
6. Readout calibration errors and correlation are either constant or subjected to a separately warranted, time-uniform reference-to-science transfer law. Nothing is inferred about future science-window theta from past calibration without a nonanticipating transfer bound.

## 2. ROT003.1: identifiability through ONE joint prepared-minus reference in the restricted mixture family

Write `h(p,theta)=p^2+theta*p*(1-p)`. A prepared ideal `(--)` pair has observed `++` indicator `X`, satisfying

`P(X=1|past) = h(p1,theta)`.

In the independent component the probability is `p1^2`; in the common uniform latch it is `p1`. For `0<p1<1`, the reference pair's `++` probability uniquely determines

`theta=(t_minusminus - p1^2) / [p1*(1-p1)]`.

The entire one-shot reference outcome law is INDEPENDENT of theta: any number of singleton references has zero identification power for theta within this family. At `p1=0` or `1`, even the new `(--)` joint reference is completely uninformative, since `p1*(1-p1)=0`. For the nominal R31/R34 comparison, `p1=247/4600=0.05369565217` and sensitivity `p1*(1-p1)=0.0508124291115`.

**One-sided finite-sample certification with uncertain p1:** if the true p1 has a valid simultaneous lower confidence bound `ell in (0,1)`, and the prepared-minus joint ++ conditional mean has a valid upper confidence bound `u`, then on the joint coverage event

`theta <= min(1,(u-ell^2)/(ell*(1-ell)))`,

provided `u>=ell^2`. The derivative of `F(t,p)=(t-p^2)/(p*(1-p))` in `p` is

`dF/dp=-[(p-t)^2+t*(1-t)]/[p^2*(1-p)^2] <=0`

for `t in [0,1]`. Also F increases with t. If `u<ell^2`, the bounds are inconsistent with the declared model on the simultaneous coverage event: flag **MODEL/CONFIDENCE ABSTAIN**, not an arbitrary theta=0 estimate. If `ell=0` or no valid known preparation, flag **NOT_IDENTIFIABLE**. This inversion is only for the **restricted shared-latch mixture**, not for an unrestricted 4x4 correlated detector.

**Nonstationary/anytime version, conditional:** let `X_k` be the paired ++-reference indicators with predictable timestamps `tau_k`, and conditional means `t_k=h(p1(tau_k),theta(tau_k))`. A source-native R34-style time-uniform CS can upper bound `bar t_n=(sum_k t_k)/n` by `U_n`. If on a simultaneous event each p1(tau_k)>=ell>0, then because h increases in p and is affine in theta,

`bar theta_n <= (U_n-ell^2)/(ell*(1-ell))`.

One completely explicit, though usually conservative, CS is generated for each *predeclared* lambda>0 by the bounded-increment supermartingale

`M_n(lambda)=exp(lambda*sum_k(t_k-X_k)-n*lambda^2/8)`.

By Hoeffding's lemma and conditional expectation, `E[M_n|past]<=M_{n-1}` even for varying conditional means. With a finite predeclared lambda grid L and alpha allocation alpha_joint, Ville + union gives simultaneously at all n

`U_n=mean(X_1,...,X_n)+min_lambda { [log(|L|/alpha_joint)+n*lambda^2/8]/(lambda*n) }`.

If in addition an EXOGENOUS bound `|theta(t)-theta(s)|<=nu_theta*|t-s|` holds across reference and science, then for any future science time t:

`theta(t) <= (U_n-ell^2)/(ell*(1-ell)) + nu_theta*(sum_k |t-tau_k|)/n`.

Clip to [0,1] only after establishing the joint coverage event and model consistency. If p1 drifts, its lower ell must cover all relevant reference times, and science p0/p1 must separately be covered by their own time-transfer intervals. The full cross-source risk spends alpha_joint **in addition** to uncertainty allocated to p0,p1 and any needed drift assumptions; R34's 0.01 reference budget cannot be silently reused in full for each new arm. Optional stopping applies only to the stated e-process/CS, not to repeated fixed-n Clopper-Pearson intervals.

An alternative direct anytime e-test against a bad-detector reference `t_k>=t_crit` chooses a predeclared `s<t_crit` and multiplies `e(X_k)=(s/t_crit)^{X_k}[(1-s)/(1-t_crit)]^{1-X_k}`. Because its one-step conditional expectation is <=1 whenever the null `t_k>=t_crit` holds, Ville controls false rejection under arbitrary stopping. This is a **reference-time** conditional null; science-time transport again requires an external drift law. The code checks its one-step e-factor inequalities, not unprovided device data.

## 3. ROT003.2: exact FOUR-CORNER B gate, instead of separate pessimistic score margins

Use the R31/R34 actual source-B ideal-plus probabilities `r_j=(1+m_B,j)/2` from ROT002. Define

`q_j(p0,p1)=p1+(p0-p1)*r_j`,

`t_latch,j(p0,p1)=p1+(p0-p1)*r_j^2` (`p0>=p1`),

`G_ind,j=a_j*q_j^2+b_j*(1-q_j)^2`,

`G_latch,j=a_j*t_latch,j+b_j*(1-2*q_j+t_latch,j)`,

`G_B(p0,p1,theta)=sum_j w_j[(1-theta)*G_ind,j+theta*G_latch,j]`.

**Theorem (conditional four-corner source-B certificate).** Let simultaneous confidence intervals be `I0=[l0,u0]`, `I1=[l1,u1]`, with `0<l1<=u1<=l0<=u0<=1`. Assume a correctly transferred future-science upper bound `theta<=theta_U<=1`. Then for every `(p0,p1) in I0 x I1`:

`G_B(p0,p1,theta) <= max_{(x,y) in {(l0,l1),(l0,u1),(u0,l1),(u0,u1)}} G_B(x,y,theta_U)`.

**Proof:** `q_j` is affine. `G_ind,j` is convex, because its Hessian is `2*(a_j+b_j)*(grad q_j)(grad q_j)^T`, positive semidefinite. `G_latch,j` is affine in `(p0,p1)` on `p0>=p1`, since both `q_j` and `t_latch,j` are affine. For fixed theta, their nonnegative mixture `G_B` is convex; every point of a rectangle is a convex combination of the four corners, and Jensen bounds its value by their maximum. Monotonicity in theta follows *pointwise for each ideal pair*: `min(p_z1,p_z2)>=p_z1*p_z2`; recorded marginals are the same in both readout branches, so increasing common-latch mixing increases the score by `(a_j+b_j)*(t_latch-t_ind)>=0`. Thus replace theta by theta_U before taking the corners. QED.

**Sharp safe-theta formula for a rectangle:** for each of the four corners v, let `C_v=G_B(v,0)`, `D_v=G_B(v,1)-G_B(v,0)>=0`. The source-B threshold b=.2828 is retained whenever

`theta_U <= min_v[(b-C_v)/D_v]` (clip to [0,1], treat `D_v=0` separately and ABSTAIN if any `C_v>b`).

This formula treats uncertainty in p0,p1 and dependence theta **JOINTLY** rather than allocating the complete nominal score margin separately to each. For science pairs with unequal per-shot p0/p1, select a legitimate common-pair anchor `(p0,p1)` and separately bound the maximum per-shot deviation `eps_pair`. Coupling the two recorded signs using the same branch uniforms implies

`|G_B(actual)-G_B(common-pair-anchor)| <= 2*S*eps_pair`,

where `S=sum_j w_j*max(a_j,b_j)=0.59514`. Therefore a conservative unequal-shot gate is `max_corners G_B(corner,theta_U)+2*S*eps_pair<=b`. For R34's *exogenous* derivative nu_i=1e-8 and source-pair duration gamma*T_pair=1.82831853, an example bound using a pair-start anchor is `eps_pair<=1.82831853e-8`, giving score correction <=`2.177e-8`. Such use is conditional on the same detector coupling and the genuinely applicable temporal derivative; no experimental confirmation is claimed.

**Source-A boundary:** with identical detector marginals, latch mixing can only increase the pointwise signed score relative to product readout, for *any* ideal-pair source distribution, including Xi-dependent source A. Hence the original R31/R34 A lower score certificate remains available wherever its own calibration, reset-hazard and drift assumptions are met; apply the extra `2*S*eps_pair` penalty if needed. This is NOT a new proof of R31 all-real-Xi source A, and an unrestricted rectangle outside its prior calibration envelope does not inherit its A guarantee.

## 4. New numerical fixtures (synthetic, NOT data)

At exact nominal p0=.99, p1=247/4600:

- `G_B(ind)=0.27068308375498048`;
- `G_B(latch)=0.28292573266763738`;
- `theta_critical=0.98972994582019011`;
- paired reference `t_critical=h(p1,theta_critical)=0.053173805773929869`.

In **ILLUSTRATIVE symmetric rectangles** `[p0*-delta,p0*+delta] x [p1*-delta,p1*+delta]` (NOT the actual nonstationary R34 confidence rectangles), the exact four-corner thresholds are:

| delta | maximum safe theta |
|---:|---:|
| 0 | 0.989729945820 |
| 0.0001 | 0.986306207415 |
| 0.001 | 0.956768580109 |
| 0.002 | 0.926427698434 |
| 0.005 | 0.848324859188 |
| 0.009398133421 | 0.759786463355 |

That last delta has the same numeric magnitude as the R34 scalar drift budget, but this square must **NOT** be mistaken for R34's actual CP + exogenous drift confidence region. Source-B prior R31 upper CP bound `B0=0.271613589752...` differs from its nominal `G_B(ind)`; using `B0` as though it were the nominal mean would invalidate the displayed theta-critical calculation.

**Exact fixed-n design cost, conditional on KNOWN p1 and stationary theta, for one-sided bad-detector test H0: theta>=theta_critical.** For each predeclared n, reject H0 when the number K of pair-reference ++ observations is at most the largest integer c satisfying `P[Bin(n,t_critical)<=c] <= 0.005`. Then size is <=0.005 for the composite null by monotone binomial stochastic order. Under the indicated *hypothetical* theta, the table gives examples of n with >=90% power; they are not necessarily minimal n and do NOT license sequential repeated peeking.

| hypothetical theta | prepared -- ref pairs n | physical readouts 2n | c | exact type-I bound at edge | test power |
|---:|---:|---:|---:|---:|---:|
| 0 | 137 | 274 | 1 | 0.004878 | 0.9400 |
| 0.5 | 971 | 1942 | 34 | 0.004978 | 0.9097 |
| 0.9 | 34898 | 69796 | 1748 | 0.004987 | 0.9016 |
| 0.98 | 3053998 | 6107996 | 161383 | 0.00499986 | 0.9001 |

The steep rise near theta_critical follows from the tiny separation `p1*(1-p1)*(theta_critical-theta)`. The example at theta=.98 needs >6 million physical readouts, dwarfing R34's synthetic 46055 reference shots. This comparison does NOT claim an intrinsic lower bound for all correlated-readout calibration strategies; it concerns this specified prepared-minus/binomial design at this score threshold. Source preparation, SPAM, drift and p1 uncertainty would require **additional** work and risk budgets.

## 5. Exact obstruction beyond the one-parameter mixture model

ONE paired prepared-minus reference is not enough for **arbitrary** source-independent conditional correlated readout `Q(r1,r2|z1,z2)`. Construct two channels with the same p0,p1 singleton marginals and exactly the same full conditional readout law for prepared ideal `(--)`: let all input-pair joint laws be product except for ideal `(++)`, where replace its registered `++` joint probability from `p0^2=.9801` to `min(p0,p0)=p0=.99`, keeping its two plus marginals equal to p0 and adjusting the other three registered outcome probabilities by Frechet coupling. This is a valid conditional classical 4x4 channel.

For actual source B, ideal `(++)` has probability `r_j^2>0` in each axis; hence the two detectors, indistinguishable by ALL singleton references and the entire prepared-minus paired reference, induce a signed source-B score difference

`Delta_source_B=(p0-p0^2)*sum_j w_j*(a_j+b_j)*r_j^2=0.00356869730040287224`.

Thus the one-scalar theta model is a falsifiable family **assumption**, not a demonstration that one joint detector setting solves arbitrary readout correlation. Its source-native falsifier is a paired-reference second ideal input `++` (or richer 4x4 score-response controls) showing a joint law inconsistent with the fitted common theta. Full assignment-matrix calibration is a mature competing route; its fit to **sequential source-ON shots** must still be established.

## 6. Work/custody/readback and explicit next owners

Public reproducibility script: `IW_PRF13_ROT003_JOINT_CALIBRATION_CORNER_GATE_REPRO_001_20261111.py` (Python3 standard library Decimal+SciPy), executable in one command, no data downloads. Asserts source-B comparator agreement with ROT002, four-corner fixtures and monotonicity tests, exact finite-n binomial size/power, and a basic bad-detector e-factor conditional expectation check. Its numerical output is an **author calculation, not an independent referee or directed-interval proof**. Parent R31 source-B matrix generator was independently checked in ROT002, but R31 source-A all-real-Xi proof is inherited only conditionally. Local source/checksum must be tied to published GitHub blob after write; BW ingestion not assumed.

**Proposed source owner action, not evidence of receipt:** owner of experimental/reference protocol should establish whether prepared ideal `(--)` paired source-independent reference at science-like timing exists, record raw two-shot outcome counts and p1 marginals with timestamps, quantify p0/p1/selector drift or state a blocker. Deliver to KN13/BW only via existing provenance path; LT7 and referee AUD1/REC11 adjudicate scientific status. PRF13 does not self-upgrade canon or write directly to BW/LT.

**REOPEN_IF:** (a) real pair-reference preparation and timestamped outcomes become available, (b) scientific referee finds an invalid model/coupling/convexity assumption, (c) experimental theta is demonstrably axis-specific or source-dependent, or (d) a tighter model-agnostic score-response calibration outperforms the one-parameter channel. Do not continue deriving physically stronger statements from unmatched synthetic controls.

**RETURN:** PRF13_ROT003 / ONE_PAIRED_MINUS_REFERENCE_IDENTIFIES_LATCH_THETA_IF_MODEL / FOUR_CORNER_CONVEX_B_CERTIFICATE / EXOGENOUS_THETA_AND_P_DRIFT_REQUIRED / SOURCE_A_MONOTONICITY_CONDITIONAL / REAL_REFERENCE_UNVERIFIED / ARBITRARY_COPULA_NOT_IDENTIFIED / FIXED_N_ALPHA005_EXACT_BINOMIAL_FIXTURES / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / REFEREE_PENDING / GITHUB_PENDING_BW_INGEST / ORIGINAL_3Q_LOCC_OPEN.