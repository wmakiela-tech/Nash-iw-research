---
artifact_id: IW_MT14_ROT001_RATE_FLOOR_TWO_GROUP_LABEL_GAIN_THRESHOLD_001_20261026
created_at: 2026-10-26
origin_cell: IW_MT_SUCCESSOR_13 / MT14
problem_id: PRF11_R35_FIXED_PROTOCOL_MAX_SWAP_CADENCE_VISIBILITY_NO_GO
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_CONDITIONAL_TWO_GROUP_POISSON_LIMIT_THEOREM / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_DEVICE / NO_FULL_ADAPTIVE_TESTER / NO_BW_INGEST_ASSUMPTION
---

# MT14 ROT001 — Exactly when an early-time label beats the optimal unlabelled event count under a fixed SWAP rate floor

## Source, priority, and two-sided prior-art subtraction

**Original scientific owner PRF11 R35 FIRST:** fixed ideal-SWAP multi-probe protocol, Cauchy common-frequency source A versus independent-increments source B, age-dependent endpoint dephasing with `r_j=exp(-beta*u_j/n)`, deterministic unequal positive partition `d_j=Delta_j/T`, final-state formula (35.1), and the source A-to-X-reference trace approximation for `E_n=sum d_j^2 ->0`.
Original owner: https://github.com/wmakiela-tech/Nash-iw-research/blob/39979379d8fd9ac3a8f42009c01b5a3baf688f87/research/prf11/2026-10-25/IW_PRF11_R35_NONUNIFORM_SWAP_TIME_GRID_RECOVERS_IDEAL_MEMORY_WITH_CRITICAL_STORAGE_RATE_001_20261025.md

**Independent NASH rotation of 2026-10-26 FIRST:** minimum-interval `d_j>=c/n` full terminal POVM strict visibility loss (E2), AND the exact optimal envelope E3 for the **unlabelled total X-minus count only**, attained by the specified early-concentrated sqrt(n) schedule. Its E3 makes NO sufficiency claim for labelled/grouped events; it is NOT being corrected or replaced.
https://github.com/wmakiela-tech/Nash-iw-research/blob/73c71ceac7ec4a6a60f8b3a935b466b4a75d7cdc/research/nash-independent/2026-10-26/IW_NASH_ROTATION_20261026_RATE_CAP_STRICT_VISIBILITY_DEFICIT_001.md

**Further project science FIRST:** PRF11 R34 owns age-labelled Poisson-process source and count-vs-label distinction for the equal-grid schedule; MT13 ROT040 owns exact target-specific age-bit sufficiency for an R34 parameter interval; neither is this rate-floor two-block schedule. https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R34_AGED_MEMORY_SHARP_VISIBILITY_POINT_PROCESS_AND_LABEL_SUFFICIENCY_001_20261025.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/1ab0a38cc492a4303f2aa007ce615214888424e2/research/mt13/2026-10-25/mt13_rot040_prf11_r34_two_age_bins_sharp_poisson_helstrom_compression_001.md

**Mature external host:** independent rare-event Poisson approximation (Le Cam 1960), Neyman–Pearson binary likelihood ratio, total-variation contraction under deterministic coarse graining. This is a source-specific application of mature probability/decision theory, NOT a claim of mathematical or scientific priority; no full external state-of-art novelty verification performed. See Le Cam https://doi.org/10.2140/pjm.1960.10.1181 .

## Declared experiment

Take fixed `a=gamma*T>0`, `beta>0`, `0<c<1`; `h_n=ceil(sqrt(n))`, `h_n<n`. The exact R35 time increments used by the independent E3 owner are

```
d_j = c/n + (1-c)/h_n  for 1<=j<=h_n;
d_j = c/n              for h_n<j<=n.
sum_j d_j=1;  d_j>=c/n;  E_n=sum_j d_j^2 -> 0.
u_j=sum_{k>j}d_k;  r_j=exp(-beta*u_j/n);  q_j=exp(-a*d_j).
```

Measure X on ALL n terminal probes. Retain only two counts: `K_e` on early positions `1,...,h_n`, and `K_l` on remaining positions. A uses ONE shared static Cauchy source; B uses independent-increment Cauchy source. This is a **precommitted ideal fixed SWAP schedule and final local X measurement**, not an adaptive instrument, not continuous-time hardware, and not full final POVM optimisation.

## Theorem T1 — exact joint rare-event experiment

Let `L=beta*c/4`, `H=a*(1-c)/2`, `R=L+a*c/2`. In total variation on `N_0^2`,

```
under A:  (K_e,K_l) => (0, Pois(L));
under B:  (K_e,K_l) => (Pois(H), Pois(R)), independent coordinates.
```

The quantum static-Cauchy state A is NOT artificially replaced at finite n. R35 (35.6–35.7), followed by the same storage channel and X measurement, makes its full X law TV-close to independent background bits `Bern((1-r_j)/2)` as `E_n->0`. Their early mean tends to 0 and late mean to `L`. Under B the independent bits have probabilities `(1-r_j*q_j)/2`; early/late means tend to `H` and `R`. In each group, the sum of squared bit probabilities tends to zero, so independent Poisson-binomial approximation yields joint TV convergence. No physical device claim follows.

## Theorem T2 — exact two-group optimal binary decision and when the time label matters

For this LIMITING two-group experiment, the best equal-prior binary test has total-variation distinguishability

```
V_group=1-sum_{k>=0} min(Pois(L)[k], exp(-H)*Pois(R)[k]).
```

An optimal test needs **only** one bit `I(K_e>=1)` and the late count `K_l`:
- if `K_e>=1`, choose B;
- if `K_e=0`, choose B exactly when
  `exp(-a/2)*(1+2a/beta)^(K_l) >= 1` (ties arbitrary).

The total-count-only experiment has `K=K_e+K_l` and
```
A: Pois(L),  B: Pois(L+a/2).
V_count=TV(Pois(L),Pois(L+a/2))
```
exactly the independent E3 envelope, **not** an envelope for grouped records.

Define the positive critical background parameter
```
beta_crit(a)= 2a/(exp(a/2)-1).
```

For EVERY `a>0`, `beta>0`, `0<c<1` in this SOURCE experiment:
```
beta <= beta_crit(a)   =>  V_group = V_count;
beta >  beta_crit(a)   =>  V_group > V_count.
```

**Proof.** Under A all `K_e>0` have zero mass, so their decision is B. On `K_e=0,K_l=k`, the ratio B/A is `exp(-H-R+L)*(R/L)^k=exp(-a/2)*(1+2a/beta)^k` for `L>0`. It strictly increases with `k`, while at `k=0` it is below 1. If it is at least 1 already at `k=1`, all total-count fibres `K>=1` have the same B-favouring sign, whereas `K=0` favours A. Thus no sign is lost by summing counts and TV is unchanged. The condition is exactly `beta<=beta_crit(a)`. If `beta>beta_crit(a)`, the fibre `K=1` contains a strictly A-favouring atom `(K_e,K_l)=(0,1)`, with positive A mass and B mass, AND a strictly B-favouring atom `(1,0)` with positive B mass and zero A mass. Coarse graining these opposite-sign atoms strictly reduces total variation. This proves both directions and the exact threshold. This is a target-specific Neyman–Pearson/Blackwell non-equivalence, not universal sufficiency over unknown parameters.

A **quantitative nonzero lower certificate** for the labelled gain when `beta>beta_crit(a)` is the loss on the `K=1` fibre alone:
```
V_group-V_count >= min{
 exp(-L)*( L-exp(-a/2)*(L+a*c/2) ),
 exp(-L-a/2)*a*(1-c)/2
} > 0.
```

At the endpoints `c=1` there is no early signal `H=0`, and labels cannot help in this construction; at `beta=0` both limits are background-free and the any-click test is optimal. These excluded boundary cases are NOT covered by the strict clause.

## Independently calculated exact Poisson checks and falsifier

With `a=1,c=1/2`, `beta_crit=3.0829881650735964`:
```
beta=2: V_count=0.306434230330; V_group=0.306434230330; gain=0.
beta=4: V_count=0.238651218541; V_group=0.266006967519;
        gain=0.027355748978;  K=1 witness lower bound=0.027355748978.
```
These finite Poisson-sum numerics were calculated independently of PRF source code using SciPy `poisson.pmf`. The proof itself is analytic, and not an independent full finite-n source-run. To reproduce:

```python
import numpy as np
from scipy.stats import poisson
from math import exp
a, beta, c = 1., 4., .5
L, H, R = beta*c/4, a*(1-c)/2, beta*c/4+a*c/2
k = np.arange(120)
v_group = 1 - np.minimum(poisson.pmf(k,L), exp(-H)*poisson.pmf(k,R)).sum()
v_count = .5*np.abs(poisson.pmf(k,L)-poisson.pmf(k,L+a/2)).sum()
print(v_group, v_count, v_group-v_count)
```

A falsifier is a legal fixed `(a,beta,c)` in the stated domain at which the exact Poisson joint model, via direct summation, violates either threshold direction or the lower certificate. A deeper source falsifier would invalidate R35's static-Cauchy TV approximation on fine meshes, or the Bernoulli/Le Cam convergence assumptions. **No owner acceptance, referee review, BW ING, novel mathematics or physical upgrade is claimed.**

## Decision impact and stop

The count-only **sharp** E3 rate-floor envelope does NOT control labelled/grouped readout for `beta>beta_crit(a)`. For lower beta, unlabelled count remains as good as this precise two-group statistic. The source-independent E2 **full terminal POVM strict loss** remains fully compatible: `V_group <= D_Q` and neither is certified equal to ideal memory. No new task cascade. Ask PRF's current authorised owner to check the source-native claim and whether this binary target-relative information should enter its own continuation; authorship of R35 and E3 stays with their originals.

STATUS: BOUNDED_EXACT_THEOREM / DERIVED_AND_INDEPENDENT_POISSON_CHECK / REFEREE_PENDING / GITHUB_PENDING_BW_INGEST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
