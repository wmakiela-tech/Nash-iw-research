---
artifact_id: IW_REC11_ROT019_M14_ROT041_MINIMAL_OPTIMAL_SESSION_SUPPORT_REFEREE_001_20261111
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
date: 2026-11-11
kind: I1_NONBLIND_EXACT_SOURCE_TYPED_MATH_REFEREE
source_first: M14_ROT041_STATIC_FIELD_SHARP_GAUSSIAN_MINIMAX_AND_GRAPH_IDENTIFIABILITY
source_pin_commit: 760a9dabb886a2f400b887de264add08b75684a0
source_pin_blob: 357d823e604fabfc86b9fc3573743aa126001250
claim_ceiling: CLASSICAL_STATIC_SYNTHETIC_TETRAHEDRAL_GAUSSIAN_DESIGN / NO_NOVELTY / NO_NATIVE_NV_SOURCE / NO_CANON / NO_EXEC_SIGN
bw: UNVERIFIED
---

# REC11 ROT019 — Necessity of all six pair / four triple co-time groups for exact global Gaussian minimax

## 0. Source and priority

Directly inspected the original public M14 ROT041 source, commit `760a9dabb886a2f400b887de264add08b75684a0`, Git blob `357d823e604fabfc86b9fc3573743aa126001250`: [source report](https://github.com/wmakiela-tech/Nash-iw-research/blob/760a9dabb886a2f400b887de264add08b75684a0/research/m14/2026-11-11/iw_m14_rot041_group_size_static_field_graph_connectivity_and_sharp_gaussian_minimax_001.md).

M14 **FIRST** established exact risk `R_r*=9r sigma²/[4(r−1)N]` for r=2/3/4 simultaneous tetrahedral orientations, unbounded per-session common calibration nuisance, static vector field, independent equal-cost Gaussian shots, continuous N resources, general biased estimators/adaptive replications of a fixed predeclared calendar. M14 FIRST proved co-time connectivity iff full source-field rank and provided the all-subsets optimal designs, but explicitly **did NOT claim** that all six pairs/four triples were needed. REC11 independently closes **only that support-minimality question**. This is classical A-optimal balanced incomplete-block/graph-Laplacian design geometry, not novelty; nearest mature examples: [optimal incomplete-block graphs](https://link.springer.com/article/10.1007/s42519-021-00215-x), [graph Laplacian designs](https://pmc.ncbi.nlm.nih.gov/articles/PMC12274245/). No implication for actual NV instrument readout.

## 1. New sharp support theorem (continuous-resource exact)

Let `a0=(1,1,1), a1=(1,−1,−1), a2=(−1,1,−1), a3=(−1,−1,1)`. The original M14 model has **static** `z∈R³`, finite predetermined distinct session timestamps `t_k`, at most `r∈{2,3,4}` axes per session, arbitrary common `h(t_k)` with no amplitude/derivative bound (independent across finite sessions through smooth interpolation), independent equal-cost `N(0,sigma²)` noise and total shots `N`.

**Theorem REC11:** Any attaining design for M14's global minimum risk `R_r^*` with positive N must employ every one of the `binom(4,r)` DISTINCT r-axis subsets at least once, with the SAME positive *total group budget* for each subset and equal channel allocations within each group. Repeated sessions for the SAME subset can be aggregated. Thus the sharp minimum number of distinct co-time groups/physical sessions (if one group per time) is:
- r=2: **six different pairs**, `R_2^*=9sigma²/(2N)`;
- r=3: **four different triples**, `R_3^*=27sigma²/(8N)`;
- r=4: **one quadruple**, `R_4^*=3sigma²/N`.

In contrast, a connected graph with only THREE pair sessions identifies the field but is strictly risk-suboptimal. The source model's exact all-pairs/all-triples designs ATTAIN the lower bound. For arbitrary integer N, divisibility/rounding constraints may prevent exact attainment; these minimal-support statements concern the continuous relaxation and divisible integer budgets only.

## 2. Complete necessity proof

For a group `S` with exactly r axes, define
`G_S=Σ_(i∈S) a_i a_i^T − (1/r)(Σ_(i∈S)a_i)(Σ_(i∈S)a_i)^T`.
Then `tr G_S=4(r−1)`. If the total shots in this session are `n_S` and divided evenly, its profiled Fisher contribution is `n_S G_S/(r sigma²)`.

M14's sharp lower bound is the two-step chain
`tr I ≤4N(r−1)/(r sigma²)`,
`tr I^(−1)≥9/tr I`,
with a Bayesian lower argument extending it beyond unbiased/nonadaptive estimators. **Attaining the global number forces equality in BOTH links.** Equality in the first inequality is strict unless EVERY active group has exactly r positive channel counts all equal (`Σ n_i² ≥n_S²/r`); equality in the second requires `I=c I_3` (identical positive eigenvalues).

Aggregate any repeated identical group; write `w_S=n_S/r≥0`. Then the sole remaining requirement is that `F=Σ_(|S|=r) w_S G_S` be isotropic. This imposes precisely 5 linear zero-anisotropy equations:
`F12=F13=F23=0`, `F11−F22=0`, `F22−F33=0`.

REC11 independently constructed the exact rational 3×3 G matrices. The five-equation coefficient matrix has:
- r=2, all 6 pairs: rank **5**, nullspace exactly span{(1,1,1,1,1,1)};
- r=3, all 4 triples: rank **3**, nullspace exactly span{(1,1,1,1)};
- r=4, unique quadruple: nullspace span{1}.

Hence every isotropic feasible weight vector is a multiple of the all-ones vector, and positive N makes that multiple strictly positive. Omitting ANY distinct group forces the entire weight vector zero, contradicting N>0. Conversely uniform positive weights yield
`Σ_(|S|=r) G_S = [4(r−1)/3] binom(4,r) I_3`,
therefore `I=4(r−1)N/(3r sigma²) I_3` and exact owner risk. **Necessity and sufficiency are both established**. The argument uses strict equality in the global minimax lower proof, so it also excludes adaptive fixed-calendar allocations with fewer available group types from attaining the global value; this is not a theorem about dynamically introduced new timestamps.

## 3. Independent exact source controls and a new three-triple negative

Two standalone independent implementations executed locally:
1. Python SymPy (separate from all M14 source code): all r=2/3/4 exact G matrices, anisotropy nullspaces/ranks, owner N=240 Fisher/risk, 64 labeled co-time graphs, star/path/three-triple controls.
2. Pure Python standard-library `Fraction` and independent rational Gaussian elimination: separate derivation of each anisotropy matrix, nullity=1, each of 11 one-subset deletions defeats isotropy, exact isotropic FI.

Both PASS. Reproduced M14's **38 connected versus 26 disconnected** 4-vertex graphs and equivalence `graph connected ⇔ Fisher rank=3`. At `N=240,sigma²=1`, exact owner minima r2=`3/160`, r3=`9/640`, r4=`1/80`.

A **new** strict but not necessarily optimal three-triple countercontrol: use only (013),(023),(123), equal resource per channel. Its exact trace-inverse risk is `567 sigma²/(160 N)=(21/20) R_3^*`, **5% above** the owner r3 minimax. For N=720, the 9 channel-session cells can each receive exactly 80 integer shots. No claim that 5% is the sharp restriction gap under all unequal allocations among three triples. Existing M14 connected pair trees (star/path) stay only rank-positive, not globally optimal.

## 4. Reproducibility and claim ceiling

Complete independent LOCAL reproducer ZIP: `IW_REC11_ROT019_M14_MINIMAL_OPTIMAL_SESSION_SUPPORT_REPRO_001_20261111.zip`, SHA256 `481dca62c2dd5b6c75c89e17c8b4dba462401a7c50d923fa5a36a1423c217a07`. Nine files: full Polish report, README, two independent Python scripts, two deterministic JSON results, two stdout logs and SHA256 manifest. ZIP CRC PASS, 8/8 payload SHA256 PASS, isolated clean extraction/reexecution reproduced **both** JSON and stdout byte-for-byte. This ZIP is LOCAL conversation material, not claimed to be on GitHub.

Source controls are **synthetic and classical**. No original Schall NV four-orientation simultaneous timestamps, source-specific readout statistics, actual common calibration process, native sensor sensitivity/fT gain, non-static field, non-Gaussian noise, unequal instrument costs, large-scale NASH physical claim, mathematical novelty, REV029 source edit, BW receipt, owner M14 or AUD1 endorsement, CANON or EXEC_SIGN. Posting != owner acceptance.

RETURN_ID: `IW_REC11_ROT019_M14_ROT041_MINIMAL_OPTIMAL_SESSION_SUPPORT_REFEREE_001_20261111`.
FINAL: `PASS_M14_SCOPED / PASS_SHARP_MINIMAL_OPTIMAL_SESSION_SUPPORT_6_4_1 / PASS_TWO_INDEPENDENT_RATIONAL_IMPLEMENTATIONS / HOLD_NATIVE_NV / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
