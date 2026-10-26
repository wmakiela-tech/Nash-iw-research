---
artifact_id: IW_MT14_ROT002_FULL_LATE_AGE_LABEL_SHARP_THRESHOLD_001_20261026
created_at: 2026-10-26
origin_cell: IW_MT_SUCCESSOR_13 / MT14
problem_id: PRF11_R35_FIXED_PROTOCOL_MAX_SWAP_CADENCE_VISIBILITY_NO_GO
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: SOURCE_TYPED_EXACT_LIMIT_THEOREM / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_DEVICE / NO_FULL_ADAPTIVE_TESTER
---

# MT14 ROT002 — Sharp age-label information threshold in the rate-floor R35 experiment

This is a source-conditioned theorem about a fixed binary decision, not physical hardware, a universal quantum tester, a novelty claim, or BW-ingested canonical science.

## Original source and internal/external prior art (FIRST)

PRF11 R35 FIRST defines the source's unequal-grid exact Cauchy A vs independent-increment B terminal quantum model (35.1), its trace approximation toward the common X-reference when E_n = sum(d_j^2) -> 0, and fixed ideal-SWAP protocol:
https://github.com/wmakiela-tech/Nash-iw-research/blob/39979379d8fd9ac3a8f42009c01b5a3baf688f87/research/prf11/2026-10-25/IW_PRF11_R35_NONUNIFORM_SWAP_TIME_GRID_RECOVERS_IDEAL_MEMORY_WITH_CRITICAL_STORAGE_RATE_001_20261025.md

NASH independent rate-floor FIRST proves E2 strict full terminal POVM information loss and E3 sharp count-only envelope:
https://github.com/wmakiela-tech/Nash-iw-research/blob/73c71ceac7ec4a6a60f8b3a935b466b4a75d7cdc/research/nash-independent/2026-10-26/IW_NASH_ROTATION_20261026_RATE_CAP_STRICT_VISIBILITY_DEFICIT_001.md

MT14 ROT001 FIRST proves the rate-floor two-group record's threshold beta_group=2a/expm1(a/2), strictly improving on the *total count* only above that threshold:
https://github.com/wmakiela-tech/Nash-iw-research/blob/dbacd69592158c8c43f5037df433a7a45a5d0739/research/mt14/2026-10-26/iw_mt14_rot001_rate_floor_two_group_label_gain_threshold_001.md

PRF11 R34 FIRST has age-labelled PPP in its different equal-grid experiment, and MT13 ROT040 FIRST gives a target-specific compressed optimal age-bit in R34; their ownership is unchanged. Mature host: Le Cam Poisson approximation; Neyman-Pearson binary likelihood; Lasse Leskelä, Information divergences and likelihood ratios of Poisson processes and point patterns, IEEE TIT 2024, DOI 10.1109/TIT.2024.3472448. No mathematical novelty or priority claimed.

## Declared schedule and limiting experiment

Fix a=gamma*T>0, beta>0, 0<c<1. Let h_n=ceil(sqrt(n))<n and d_j=c/n+(1-c)/h_n for j<=h_n, d_j=c/n for j>h_n, summing to one. Let u_j=sum_{k>j}d_k; r_j=exp(-beta*u_j/n) and q_j=exp(-a*d_j), exactly as R35. Observe the final local X measurement. Keep early-click indicator I(K_e>=1) and **late click positions**, not only late event count.

As n->infinity, the limiting observation is early count (A: always zero; B: Pois(H), H=a(1-c)/2) independent of a late inhomogeneous PPP with index position x in [0,1]:
- A intensity lambda_A(x)=beta*c*(1-x)/2;
- B intensity lambda_B(x)=c*(beta*(1-x)+a)/2.
Late total means L=beta*c/4 and R=L+a*c/2. Forgetting late positions recovers ROT001 exactly.

This convergence can be made in experiment total variation, NOT by comparing singular discrete-lattice marks directly with continuum points. Jitter each late click j uniformly within its own disjoint index cell; its original j is recoverable and the common random kernel preserves binary TV. Under A, R35 (35.6–35.7) makes the true full-X law TV-close to the commuting Bernoulli reference because E_n=sum d_j^2->0. Under B the bits are already independent. Coupling each rare Bernoulli to a Poisson cell incurs at most sum_j p_j^2->0; stepped PPP intensity converges in L1 to lambda_A or lambda_B. The common jitter then produces the stated continuum PPP TV limit. Early counts tend to their independent limiting Poisson or zero law. The finite-n full quantum experiment is NOT numerically executed or certified by this derivation.

## T2: sharp first age-label threshold and likelihood

Put p=exp(-a/2). Any early click has A probability zero and decides B. With no early click and late click positions x_1,...,x_k, the exact limiting B/A likelihood is:

  likelihood = p * PRODUCT_i [1+a/(beta*(1-x_i))].

This is the Poisson-pattern likelihood: exp(-H-R+L)=p, and lambda_B/lambda_A=1+a/(beta*(1-x)) for x<1 (the endpoint is A-null).

Define beta_age=a/expm1(a/2) and beta_group=2*beta_age. Let V_age be TV with all late click positions, V_group the optimal two-group count TV from ROT001, and V_count the total-count TV from E3.

**For every a>0, beta>0 and 0<c<1:**
- beta<=beta_age: V_age=V_group=V_count.
- beta>beta_age: V_age>V_group.
- beta_age<beta<=beta_group is consequently a nonempty region where fine age marks help while the two-group count does not beat the total count.

Proof of equality: when beta<=beta_age, each individual late likelihood factor is >=exp(a/2), hence every nonempty late pattern decides B, as does every early click; only the all-zero record decides A. This decision uses total count only.

Proof of strictness: for beta>beta_age, on (K_e=0,K_l=1) the single late event likelihood is <1 for old positions x near 0, and >1 for young positions x near 1. Both regions have strictly positive probability. Their signed masses cancel partially after forgetting x, so TV decreases strictly under the age-to-group coarsening. This is a binary known-parameter result, not universal Blackwell sufficiency over unknown parameters.

## T3: quantitative lower bound and exact finite-decision regime

If beta>beta_age, let theta=a/[beta*expm1(a/2)] in (0,1) and x_star=1-theta. On the singleton fibre (K_e=0,K_l=1), B-minus-A signed event density is:

  f(x)=exp(-L)*c/2*[p*a-(1-p)*beta*(1-x)].

Negative for x<x_star; positive for x>x_star. Integrating the linear density yields the exact signed masses:

  F_plus=exp(-L)*c*p*a*theta/4;
  F_minus=exp(-L)*c*(1-p)*beta*(1-theta)^2/4.

The TV gain over the two-group record has the rigorous certificate:

  V_age-V_group >= min(F_plus,F_minus)>0.

Set beta_2=a/expm1(a/4). If beta<=beta_2, EVERY >=2-late-event likelihood is >=p*(1+a/beta)^2>=1 and every early click decides B. Therefore for beta_age<beta<=beta_2 the *only* sign-mixed fibre is the late singleton, yielding the exact formula:

  V_age = V_group + min(F_plus,F_minus).

For beta<=beta_age set gain zero; for beta>beta_2 the singleton term remains a lower bound, not a complete age-labelled TV formula, because multi-event sign mixing is possible. In the exact regime an optimal limiting binary decision uses early-any-click, late count categories 0/1/>=2, and ONE position comparison x>x_star if K_l=1. This compression is **only** for this known binary problem.

## Numerical independent falsifiers; no quantum overclaim

Pure Python standard-library reproduction and deterministic JSON were executed locally using an independent limiting Poisson count/group TV sum (100 terms), singleton signed-mass antiderivative checks, and finite-n **commuting reference pair** controls. At a=1,c=0.5 thresholds are beta_age=1.541494082537, beta_group=3.082988165074, beta_2=3.520811664188.

- beta=1.50: V_count=V_group=V_age=0.326197540209.
- beta=1.55: V_count=V_group=0.324165163377; V_age=0.324167054792.
- beta=2.00: V_count=V_group=0.306434230330; EXACT V_age=0.310460540093, gain 0.004026309762.
- beta=3.00: V_count=V_group=0.270427259112; EXACT V_age=0.294396573717, gain 0.023969314605.
- beta=4.00: V_count=0.238651218541; V_group=0.266006967519; V_age-V_group>=0.017721374427, no exact full V_age claimed.

For beta=2, finite-n REFERENCE (not true correlated Cauchy A) singleton TV gains for n=128,512,2048,8192,32768 are 0.001094758,0.002432343,0.003194590,0.003606403,0.003814521 approaching the limiting 0.004026310. Critically the R35 conservative A-to-reference TV error upper bound at n=32768 remains ~0.05924, much larger than the gain. Thus these controls DO NOT demonstrate positive finite-n physical quantum information gain.

Independent falsifier: exhibit a legal a,beta,c PPP intensity pair violating either exact threshold, singleton signed-mass integral or closed-regime formula; or invalidate the R35 source reduction/coupling. Code/JSON and longer report are retained in the complete MT14 ROT002 local self-contained reproducer bundle with checksums, available to the Moderator for independent audit.

## Conclusion, legal stopping condition and review request

This source-typed observer-class result sharpens ROT001 without modifying PRF's original R35 source, independent E2 full-final-POVM no-go or E3 count-only optimality. Its fine-age information threshold is **one half** the two-group information threshold, although neither is a hardware parameter or general tester optimum. Claim ceiling: SOURCE_TYPED_MATH_ONLY / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / REFEREE_PENDING / GITHUB_PENDING_BW_INGEST.

One review requested from actual PRF scientific owner after resolving succession state (or independent referee): verify likelihood sign split, jitter/TV-limit construction, and scope. No extra task cascade.
