---
artifact_id: IW_PRF12_R33_DRIFT_INTERLEAVED_LOCAL_REFERENCES_AND_NONIID_SOURCE_GUARD_001_20261108
created_at: 2026-11-08
owner: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
source_type: SOURCE_TYPED_THEORETICAL_CONTINUATION_R31_R32
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: ANALYTIC_DRIFT_TRANSFER / NONSTATIONARY_REFERENCE_MARTINGALE / EXACT_RATIONAL_BINOMIAL / INDEPENDENT_DENSITY_AND_FALSIFIER_PASS / REFEREE_PENDING
claim_ceiling: NO_DRIFT_RATE_FROM_DATA / NO_PHYSICAL_HARDWARE / NO_NOVELTY / NO_CANON / NO_EXEC / ORIGINAL_SINGLE_COPY_3Q_LOCC_GAP_OPEN
---

# PRF12 R33 — Local interleaved references under bounded detector drift: valid source contrast and an unrestricted-drift no-go

Date: 2026-11-08. Owner PRF12. This note is a NEW mathematical continuation of PRF12 R31/R32 and DOES NOT claim a newly obtained quantum all-real-Xi certificate, a true quantum device measurement, or an answer to the original three-probe single-copy LOCC-closure question. The source-class definitions and source-ON driven instrument are inherited. The new problem is drift of the **effective terminal detector only**, measured by p0(t),p1(t), while the qubit driving and input source models remain unchanged.

## 0. Inputs, lineage, prior-art separation and precise contracts

- **Quantum comparator:** R31 full science owner https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-03/IW_PRF12_R31_NINE_CLASS_COMPOSITE_E_OPTIMALITY_BRACKET_AND_FIXED_N_1666_001_20261103.md ; reproducer present in R31 ZIP. The conditional same-signed-coin protocol using private axis J with w=(.18,.20,.62) and signed ++/-- weights alpha=(.943,.907,.347), beta=(1.,1.,.018), mixed=0, has for EVERY real Xi and R25's explicit conditional source-reset hazard a **fixed-detector** certificate: A0=0.3106993896688963, B0=0.27161358975207756. These were certified for every detector pair (c,d) inside the specified fixed-size 99% CP confidence region from SYNTHETIC reference counts. The nominal comparator p0*=.99, p1*=3705/69000 falls within this set, and thus inherits those deterministic source A/B bounds. NO re-proof of quantum interval nodes is performed in this note.
- **R32 owner and failure boundary:** https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-08/IW_PRF12_R32_ANYTIME_REFERENCE_CS_COUPLED_DETECTOR_GLOBAL_XI_001_20261108.md . R32 Beta-mixture test martingales require fixed conditional reference probabilities p0,p1. For arbitrary time variation they are NOT test martingales; R33 deliberately does not reuse stationary R32 confidence sequences.
- **Mature external work:** Howard, Ramdas, McAuliffe, Sekhon (2021), *Time-uniform, nonparametric, nonasymptotic confidence sequences*, Ann. Statist. 49, 1055–1080, DOI 10.1214/20-AOS1991; Waudby-Smith & Ramdas (2024 issue), *Estimating means of bounded random variables by betting*, JRSS B 86, DOI 10.1093/jrsssb/qkad009; Chugg & Ramdas (2025 preprint), *Closed-form empirical Bernstein confidence sequences for scalars and matrices*, arXiv:2512.21300, covers average conditional means that may vary with time. All concentration, optional stopping, alpha spending, bilinear sensitivity and stochastic domination used below are standard mature mathematical tools. No novelty/priority claim.
- **Inherited quantum assumptions:** Source A has a static hidden Xi within each intact two-shot pair but may have arbitrary dependence across pairs; B is Cauchy-Lévy independent-increment driven Lindblad dephasing during all preparation/analysis/free segments. Source A no-reset survival hazard remains >= exp(-.02*1.7783185307179588) even conditioned on CURRENT Xi, selected private axis, other hazard-relevant hidden variables and observable past. Readout signs and private score randomizations are conditionally independent given complete physical trajectories. Detector drift and reference scheduling are NONANTICIPATING with respect to future source-B Lévy increments: conditional on the information available before each source-B pulse, its quantum evolution is still the same independently incremented Lindblad channel; correlations that condition on future source-B increments are OUTSIDE the theorem. Finite X/Y controls Omega_max/gamma=10, free Delta*gamma=.5, terminal ideal Z projection are unchanged. One pair time T_pair*gamma=1.8283185307179588 including specified readout/reset overhead, excluding external unmodeled overhead.
- **NEW detector assumption:** Each terminal positive-label probability for reference state |0> or |1> is p0(t),p1(t), and for any incoming Bloch Z mean m in [-1,1], q_t(m)=(1+m)p0(t)/2+(1-m)p1(t)/2. No state dependence beyond this affine channel; the two detector uses are conditionally independent. For dimensionless clock tau=gamma*t, impose the externally supplied, PATHWISE Lipschitz bounds |p_i(tau)-p_i(sigma)|<=nu_i*|tau-sigma|. No data-derived or universally physical value for nu_i is claimed. The reference outcomes X_{i,k} obey E[X_{i,k}|full relevant past]=p_i(t_{i,k}) and are in {0,1}; their sampling times/which reference to prepare are chosen predictably. These assumptions may fail under correlated detector afterpulsing, changing qubit control, or unmodeled time-dependent measurement memory.

## 1. R33.1 — simultaneous nonstationary reference bounds across any number of completed blocks

For each reference epoch j=1,2,..., take a PREDECLARED fixed n_{i,j}>=1 of each reference type i in {0,1}, at predictable physical times tau_{i,j,k}. Write hat p_{i,j}=(1/n_{i,j}) sum_k X_{i,j,k}; bar p_{i,j}=(1/n_{i,j}) sum_k p_i(tau_{i,j,k}). Conditional Hoeffding's lemma applied to bounded martingale differences X_{i,j,k}-p_i(tau_{i,j,k}) gives, without identically distributed or independent-in-time p_i,

 Pr(|hat p_{i,j}-bar p_{i,j}|>epsilon_{i,j} | history before epoch j) <= 2 exp(-2 n_{i,j} epsilon_{i,j}^2).

Set alpha_cal=.01 and

 epsilon_{i,j} = sqrt{ log[4 j(j+1)/alpha_cal] / (2 n_{i,j}) }.                         (R33.1)

Then the above two-sided failure is <=alpha_cal/[2j(j+1)] for EACH reference stream. Union bound over both streams and **every** j>=1 yields a simultaneous event E_cal of probability at least 1-alpha_cal, since sum_{j>=1}1/[j(j+1)]=1. On that event, for any future detector readout at time tau,

 |p_i(tau)-hat p_{i,j}|
   <=epsilon_{i,j}+nu_i*(1/n_{i,j}) sum_k |tau-tau_{i,j,k}|.                         (R33.2)

This is the main robust calibration theorem, valid at ANY adaptively selected number of COMPLETED reference epochs. The allocation/ordering of the two streams within an epoch may be predictable, including deterministic interleaving. The within-epoch sample sizes n_{i,j} must be fixed before its samples are observed: (R33.1) is NOT a confidence sequence for unrestricted optional stopping at arbitrary intermediate reference count n. A separate extra alpha allocation over all n or a genuine moving-mean CS is needed to obtain that stronger property.

For an arbitrary fixed comparison detector pair p_i*, define

 delta_{j}(tau)=max_i [|hat p_{i,j}-p_i*|+epsilon_{i,j}+nu_i*(1/n_{i,j})sum_k |tau-tau_{i,j,k}|]. (R33.3)

Conditionally on E_cal, both effective detector channels at every declared science shot are within delta_j(tau) of the COMPARATOR in total variation for any ideal m in [-1,1]. This uses the convex combination q_tau(m) of p0(tau),p1(tau). For many epochs the comparison point may be chosen predictably from earlier data, but each choice MUST lie within a separately certified fixed-detector quantum-comparator domain; the explicit numerical example fixes the R31-valid nominal point p* before the current synthetic reference data and therefore avoids adaptive comparator selection.

## 2. R33.2 — exact signed-quartet perturbation and transfer of the ALL-Xi source bounds

For axis j let alpha_j,beta_j be the fixed R31 private-coin weights. Given recorded positive-label probabilities q_1,q_2 in the two shots, the probability that the private score bit equals 1 is

 F_j(q_1,q_2)=alpha_j*q_1*q_2+beta_j*(1-q_1)*(1-q_2).                            (R33.4)

The partial derivatives are alpha_j*q_2-beta_j*(1-q_2) and alpha_j*q_1-beta_j*(1-q_1), so |dF_j/dq_l|<=M_j:=max(alpha_j,beta_j). Thus for ANY source, INCLUDING an arbitrary broken pair with unrelated Bloch means in the two shots,

 |F_j(q_1,q_2)-F_j(q_1*,q_2*)|<=M_j (|q_1-q_1*|+|q_2-q_2*|). (R33.5)

Averaging over independent common private axis J gives axis sensitivity

 S=sum_j w_j M_j = .18*1+.20*1+.62*.347 = **.59514**.                       (R33.6)

If delta_j(tau) <=delta for BOTH science-shot times over all active epochs, apply (R33.5) and the fixed-comparator ALL-REAL-Xi and arbitrary-between-pair-memory source theorem from R31. For every allowed previous source-and-detector history, conditional on valid calibrations,

 P_A(bit=1|past) >= A0-2 S delta,
 P_B(bit=1|past) <= B0+2 S delta,                                  (R33.7)

with A0=.3106993896688963 and B0=.27161358975207756. The lower survival bound for Xi must remain conditional on CURRENT hidden Xi and axis. This bound cannot be replaced by a marginal/no-reset-average statement. The finite source B driven evolution and same-shot physical instrument are NOT retuned or replaced by static dephasing.

For a positive source gap (R33.7) it suffices that

 delta < (A0-B0)/(4 S)= **0.01641874177370819**.                          (R33.8)

This is a threshold for THIS conservative proof, not a necessary or hardware-universal physical limit. The bound holds for any drift trajectory within (R33.2), including an adversarial but pathwise Lipschitz detector history correlated with source Xi, provided the conditional independence and reset assumptions remain intact.

## 3. R33.3 — non-iid fixed-N test and optional science stopping with local calibration

The extra private coin makes each recorded science bit a TRUE Bernoulli variable. If for N science pairs, during all their actual physical readouts, the calibration-derived (R33.7) satisfies the **predictably** chosen bounds a<=A0-2Sdelta and b>=B0+2Sdelta with 0<b<a<1, even when Xi values are arbitrarily dependent between pairs the count K_N stochastically dominates Bin(N,a) under A and is dominated by Bin(N,b) under B. For a fixed decision threshold k, source-conditional errors are bounded by

 P_A(choose B)<=BinomCDF(k-1;N,a),
 P_B(choose A)<=BinomSF(k-1;N,b).                               (R33.9)

Add <=alpha_cal to the worst scientific error bound by the stopped-before-first-calibration-failure argument. Importantly, **one must not condition naively on the future event E_cal and then falsely assert a change of independent data distribution**. Instead the source-conditioned e-process is stopped theoretically immediately before the first failure of a true-parameter calibration enclosure; outside that event the error is paid for separately by alpha_cal. This yields the unconditional per-hypothesis wrong-declaration bound alpha_cal+alpha_science.

For genuinely adaptive science stopping after any number of completed local calibration blocks, choose a_t,b_t (or ABSTAIN if a_t<=b_t) from calibration information available BEFORE observing bit Y_t. Then define opposite-null e-factors

 G_A(Y_t)=(a_t/b_t)^{Y_t}[(1-a_t)/(1-b_t)]^{1-Y_t},
 G_B(Y_t)=(b_t/a_t)^{Y_t}[(1-b_t)/(1-a_t)]^{1-Y_t}.          (R33.10)

Under B, E[G_A|past]<=1; under A, E[G_B|past]<=1, since the relevant conditional Bernoulli success bounds are b_t,a_t. Their products are nonnegative test supermartingales until first calibration failure; Ville threshold 25 pays alpha_science=.04, while global epoch calibration alpha_cal=.01 pays the rest. Source Xi independence BETWEEN pairs is unnecessary. **If there is no current positive gap, set both factors to 1 and do not declare source.** The optional stopping is for science and completed epochs, NOT for arbitrary sample count within reference epoch, and never against unlimited detector drift.

## 4. R33.4 — physically ordered, explicitly synthetic two-epoch witness

Use two full calibration/science epochs. Per epoch acquire n0=46000 known |0> and n1=69000 known |1> reference reads, interleaved deterministically in a 2:3 ratio across a reference block lasting 11500/gamma. Each reference read is assigned duration 0.1/gamma, which is inherited from the R26 resource convention and does NOT prove realistic state preparation hardware. Use reference shot midpoint tau_k=.1(k+.5), k=0,...,114999; choose |0> via low-discrepancy floor((k+1)*2/5)-floor(k*2/5)=1. Therefore reference mean times are exactly approximately 5750.1 and 5749.9333333333 (units 1/gamma), respectively. Per epoch acquire 4750 science pairs AFTER that reference block; each costs 1.8283185307179588/gamma. Repeat this reference/science pair pattern in the second epoch. The number of reference blocks may be adaptively selected in the general algorithm, but the numerical witness declares two in advance.

Synthetic reference positive counts for EACH epoch: K0=45540 and K1=3705. Fixed comparison point p0*=.99,p1*=3705/69000 (strictly inside R31's certified CP detector domain). **These are example counts, not measured device performance.** The external detector drift hypothesis is |d p_i / d(gamma*t)|<=nu_i=10^-8 per unit gamma*time. Reference outcomes may be nonidentical Bernoulli across time, but must obey conditional means p_i(t) and predictable sampling.

Epoch j=1 has max delta_1=.008668358626139135. Epoch j=2, with its larger alpha-spending correction, has max delta_2=.009342184150949345, including the explicit maximum timestamp gap between science readout and the average reference time. Their respective safe conditional source bounds:

 j=1: A>=.3003816157633754, B<=.2819313636575985.
 j=2: A>=.2995795747177044, B<=.2827334047032695.

Use uniform weaker transparent a=.2995,b=.2828 for BOTH epochs. With N=9500 total pairs, select A iff K>=2765. The exact rational success probabilities a=599/2000,b=707/2500 allow a completely independent integer recurrence for the binomial CDF: t0=(Q-P)^N, t_{k+1}=t_k*(N-k)*P/[(k+1)(Q-P)], sum t_k/Q^N. Exact big-integer inequality checks prove both conditional errors <1/25=.04. Decimal reporting (cross-checked with SciPy):

  P_A(false B)<=.03497645807537805,
  P_B(false A)<=.03826512503259979.

Add global alpha_cal=.01: per hypothesis wrong decision <=.04497646 and <=.04826513. The total number of single sensor observations is **249000** (230000 references + 2*9500 science); wall time in this declared cost model is gamma*T<=**40369.02604182061** (23000 calibration +17369.02604182061 science). This is a resource INCREASE compared with R31 fixed-detector N1666; a realistic device may need vastly different time, calibration granularity and drift budget. No guarantee of experimental success follows from a nominal synthetic trajectory.

The maximum permissible whole-experiment detector tolerance at which the conservative gap still stays positive is delta <.01641874, but THIS particular a,b and N9500 need tighter delta <= min((A0-.2995)/(2S),(.2828-B0)/(2S)) = .00939813; the example .00934219 satisfies it. A naive all-n union Hoeffding boundary **inside** the first 46000-read reference block would have radius about .0174945, already exceeding the gap-positive limit with zero drift. Thus do NOT silently claim within-block optional stopping using (R33.1); it has a material resource penalty.

## 5. Independent falsification: detector drift without a bound destroys source identifiability

Assume calibration at any earlier finite set of times yields exactly the healthy detector p0=.99, p1=3705/69000, but let the detector be unconstrained between calibrations. During ALL science reads choose p0(t)=p1(t)=1/2. Then for every input Bloch mean m,

 q_t(m)=[(1+m)p0(t)+(1-m)p1(t)]/2=1/2.

Under either source A or B, each recorded sign is a fair independent bit, the complete quartet law is P(++|j)=P(+-|j)=P(-+|j)=P(--|j)=1/4 and the entire recorded observation law is EXACTLY source independent. Hence total variation equals zero and, for any FORCED BINARY classification rule based only on those observations, false-A plus false-B errors equal 1 (allowing an abstention changes the meaning of the two errors but cannot create information). The same detector drift can be confined to unobserved scientific gaps and reversed at later calibration reads if there is NO continuity/drift restriction. This counterexample proves that R32 stationary calibration cannot by itself imply uniform drift-robust discriminability. It does NOT disprove R31/R32 under their stationary-detector contracts, nor does it settle the original 3-qubit LOCC problem.

## 6. Reproducibility and source-type limits

Main standalone Python recalculates the explicitly timed reference interleaving, 1/[j(j+1)] reference error spending and Hoeffding radii, local detector drift budgets, source-score Lipschitz bound, epochwise A/B conditional inequalities, exact integer binomial tails and SciPy cross-check, and random numerical score perturbations. A wholly separate 2x2 unitary A / 4x4 Lindblad B audit independently reconstructs full signed-score probabilities at nine phase values and source B, verifies the drift Lipschitz inequality against 30000 random two-shot detector trajectories, and checks the unrestricted-drift no-go with source-independent recorded quartet probabilities. These are **fixture and analytic checks**, NOT independent rederivation of all-real-Xi R31. The all-Xi predecessor is explicitly cited in Section 0, with its own mpmath.iv verified code and source custody. This honest dependency is a required source guard.

**Negative knowledge:** The drift bound nu_i is EXOGENOUS and not identifiable from 115000 reference counts alone. The effective affine detector map is assumed valid for every scientific input state even while drifting. The reference probes cannot be measured simultaneously with the science terminal projectors using the same single sensor; scheduled reference blocks cost significant time. The source A hazard remains conditioned on the hidden Xi and axis; marginal or outcome-selective resets are excluded. No detector afterpulsing, anticipating drift correlated with FUTURE source-B increments, hidden source-to-detector crosstalk, gate drift, or adversarial bit assignment beyond p_i(t); these would require additional tests. No scientific priority, no hardware demonstration, no BW readback or external referee certification. No improvement of original 3-party LOCC one-shot closure, which remains OPEN after R09.

**Return:** PRF12_R33 / DRIFT_LIPSCHITZ_TWO_REFERENCE_EPOCHWISE_MARTINGALE / CONDITIONAL_SCORE_SENSITIVITY_0P59514 / NONIID_N9500_K2765_SYNTHETIC_INTERLEAVED_WITNESS / EXACT_INTEGER_BINOMIAL_PASS / UNRESTRICTED_DRIFT_IDENTIFIABILITY_NO_GO / INDEPENDENT_2X2_4X4_FIXTURE_PASS / R31_GLOBAL_XI_INHERITED_NOT_REPROVED / REFEREE_PENDING / NO_CANON / NO_EXEC / NO_NOVELTY / BW_INGEST_PENDING / ORIGINAL_3Q_LOCC_OPEN.

**R34 scientific target:** obtain time-uniform variance-adaptive confidence regions for changing conditional reference means with a local Lipschitz budget and adaptive within-block stopping, quantify whether this materially lowers the extremely expensive R33 reference burden; independently falsify the auxiliary detector pathwise drift and shot conditional-independence assumptions under a realistic T1+assignment switching model.
