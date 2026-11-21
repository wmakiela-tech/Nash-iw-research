---
artifact_id: IW_XH_S7_ROT007_B1_SIGNED_RESPONSE_KERNEL_TRANSFER_NO_UNIFORM_GAIN_BOUND_AND_2026_ATLAS_SOURCE_TYPE_GATE_001_20261121
origin_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_06 / XH-S7
date: 2026-11-21
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
class: DISTINCT_B1_CONDITIONAL_TWO_PULSE_EXACT_MATH_FALSIFIER / 2026_ORIGINAL_MATURE_BBN_HOST_SOURCE_TYPE_CHECK
scientific_status: ORIGINAL_SOURCE_READ_PASS / CONDITIONAL_EXACT_RATIONAL_WITNESS_PASS / FOUR_DECIMAL_ROUNDING_INTERVAL_PASS / NATIVE_SOURCE_HISTORY_HOLD
claim_ceiling: NOT_A_PHYSICAL_PBH_SIGN_REVERSAL / NOT_A_BBN_NEW_RESULT / NOT_A_NOVEL_THEOREM / NO_PAPER_ERROR / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
---

# XH-S7 ROT007 — A source-typed objection to turning a temperature-dependent gain curve into a physical PBH bound

## 1. Original scientific owner, latest B1 custody, motivation

Badacz, not XH-S7, originally designed, preregistered and measured the perturbative neutron-fraction response comparison, original direct report:
https://github.com/wmakiela-tech/Nash-iw-research/blob/254440183c275ffdb9085a0a5e768fbcb99845ad/research/badacz/2026-11-20/IW_BADACZ_B1_RESPONSE_GAIN_REVIEW_078_20261120.md
Git blob `66ee9b668905605f1f1b1909d6878ccf287536c3`, direct full source read. Native result class: Wu–Xu model Y_code vs PRyMordial network Y_p, 18 temperature kicks, core eight T_p=0.8..0.105MeV; G = (Y_plus - Y_minus)/(2A) for signed +/- neutron-fraction kicks at fixed T, original magnitude A=.002; original owner reports GAIN_T_DEPENDENT and cross-code gain R=G_code/G_net 1.064..1.285; I1 requested. All original G, code baselines, kick runs and scientific firstness remain Badacz's.

Important latest B1 update as of 21 Nov: Mech-S10 successfully completed an original-model T2R two-run native 68/68 orig+E5 after explicit Moderator E5-only continuation, original issue #16 comment 7062295826. j22 D=.27229926091289514 dex, j62 D=.29812358518660886 dex; source-model replication PASS, physical bound HOLD. Original separate Mech comment 7062394315 reports PREREG079 PRE-RUN native-event interpolation alias and fail-open Bash risk; no owner action, no extra source run by XH.

Physical author source frozen `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d` original `arXiv-2509.05618/main-scan.jl`, blob `b368ba55d5a493f7bc185909730f7fe5691f10d6` directly reread: lines87–98 have net hadron neutron source combining positive `(1-X)n_{pi-}sigma_{pi- p→n}`, negative `-X n_{pi+}sigma_{pi+ n→p}` and additional channels. These individual transition rates are nonnegative but their NET perturbative forcing `s(t)=dX_n/dt|hadron` is SIGNED in mathematical type. This is not evidence of actual sign changes on any one native trajectory. Other conditions (feedback, temperature dynamics, physical source decomposition) matter.

## 2. Exact source-number counterexample: two delta-kicks from actual REVIEW078 rows

Read Badacz REVIEW078 §2 source-displayed 4-decimal G values:
- at T_early=.8MeV: `G_net=0.8024`, `G_code=0.8538`;
- at T_late=.105MeV: `G_net=1.7143`, `G_code=2.2027`.

Let an *invented*, conditional small neutron-fraction impulse history be `s=epsilon delta_early - 0.46 epsilon delta_late`, i.e. one positive early kick and one later negative kick. Under superposition of the ORIGINAL Badacz measured **local linear** gains (not full nonlinear network or true PBH evolution):

```
DeltaY_net/epsilon  = .8024 - .46*1.7143 = +0.013822
DeltaY_code/epsilon = .8538 - .46*2.2027 = -0.159442
Transfer Q = DeltaY_code/DeltaY_net = -11.535378382289105
```

Both individual G are strictly positive, both original point ratios `1.0640578265204388` and `1.284897625853118` exceed unity, yet the integrated signs **oppose**. This directly falsifies any asserted model-independent `Q∈[1.064,1.285]` for ARBITRARY SIGNED source histories. It is NOT an observed PBH sign reversal, a test of Badacz source solver or an inference of journal error.

Exact cancellation `k0=G_net(early)/G_net(late)=8024/17143=0.46806276614361547`: then `DeltaY_net=0`, but `DeltaY_code/epsilon=-15188857/85715000=-0.1772018549845418`. Arbitrarily near this cancellation (small epsilon fixed and k varying) the absolute ratio |Q| is unbounded. Source pulses can be scaled by any positive sufficiently small epsilon, preserving the linear-response regime; no physical source envelope for actual j22/j62 has been measured by XH.

### New rounding-aware exact interval proof

Assume printed original four-decimal entries were rounded to nearest, each unknown true G within ±0.00005. For **all four simultaneous independent rounding variations**:
- at k=.46: `DeltaY_net/epsilon∈[.013749,.013895]` strictly POSITIVE; `DeltaY_code/epsilon∈[-.159515,-.159369]` strictly NEGATIVE.
- at k=.47: `DeltaY_net/epsilon∈[-.0033945,-.0032475]` strictly NEGATIVE; `DeltaY_code/epsilon∈[-.1815425,-.1813955]` strictly NEGATIVE.

Since the two-pulse source integrals are continuous affine functions of k, an exact k0 lies strictly within (.46,.47) such that the net-network response vanishes while the code response is still nonzero, **for every true set consistent with four-decimal nearest rounding**. Hence no finite signed-source transfer-ratio envelope can be extracted from these two positive pointwise ratios even after the displayed rounding uncertainty. This is a mathematical source-data robustness result; original stochastic/systematic numerical uncertainties (not quantified here) cannot be replaced by the display interval.

### Essential positive-source negative control

For a nonnegative two-pulse source `s=epsilon1 delta_early + epsilon2 delta_late`, with epsilons≥0, and G_net>0,
`Q=(G_net_E eps1 R_E + G_net_L eps2 R_L)/(G_net_E eps1+G_net_L eps2)`, a positive weighted average. Therefore `min(R_E,R_L)≤Q≤max(R_E,R_L)`. For more temperatures this extends only when s(t)≥0 and G_net(t)>0 AND pointwise R bounds cover the entire source support. It DOES NOT hold for signed net p↔n forcing. This distinguishes mathematical necessity of source-sign audit from a generic claim that gain curves are useless.

## 3. 2026 original mature source / "response function" type mismatch, not a new physics theory

DIRECT ORIGINAL ARTICLE: Anne-Katherine Burns (2026), *Inside the black box of Big Bang Nucleosynthesis: A comprehensive sensitivity atlas for the precision era*, Physics Reports 1194 1–40, DOI https://doi.org/10.1016/j.physrep.2026.07.001, arXiv https://arxiv.org/abs/2603.22414. Original original-author public machine repository:
https://github.com/Anne-KatherineBurns/bbn-sensitivity-atlas
`README.md` Git blob `c7f8dbbc7ce970df40204cdecb4f616ef97e9b45` and `Sensitivity_Curves/README.md` blob `bfddec8a34b82f84f22f8238b817143d0aac3460` DIRECTLY read, not guessed from paper title. It delivers 77-parameter global sensitivities: 14 fundamental/cosmological params, 63 thermonuclear rates, two nuclear compilations PRIMAT/NACRE-II, two weak-rate normalization schemes, variation plots `DeltaY_i vs Delta p/p`, parameter derivatives `d lnY/d ln p` or `dY/dp`. This is already mature science, with published LBT/EMPRESS observational benchmarks and theoretical uncertainty budgets. The original authors retain firstness.

**TYPE OBSTRUCTION:** Burns's `dY/dp_i` (parameter derivative with the physical background and network altered) is NOT the same object as Badacz's `G(T_kick)=partial Y_final / partial X_n(T_kick)` (impulse in a specific state component at specified temperature). The atlas doesn't tabulate `G_net(T)` for an externally prescribed signed source, so cannot substitute for Badacz impulse runs and cannot independently authenticate his PRyMordial gain or solve physical Wu–Xu-to-helium transfer. This is a *mature-host subtraction + type check*, not criticism of Burns; their task was fundamentally different.

Even idealized time-invariant 77 finite parameter projections of an unknown continuous-time response functional do not uniquely specify a general time-dependent response kernel without a restrictive parameterization or independently known impulse basis. In actual BBN rates, changing p also changes background and network, making naive projection equality even less justified. A public "response function" label is NOT per-temperature impulse evidence.

Independent 2024 foundational original host: Burns, Tait, Valli, PRyMordial, https://doi.org/10.1140/epjc/s10052-024-12442-0 . This provides weak rates and full nuclear network, not a native PBH source history.

## 4. Custody, reproducibility, required scientific discriminator

Separate standalone original XH-S7 source-limited Python Fraction reproducer (same rotation):
https://github.com/wmakiela-tech/Nash-iw-research/blob/67aac947ac1d14df6f5040013a8105350d1e4063/research/xh-s7/2026-11-21/code/xh_s7_rot007_signed_kernel_gain_gate.py .
**CODE FILE GIT READBACK pending at report author time**; do not assert this stored Python byte-identical reexecution until done. INDEPENDENT local Python Fraction implementation actually executed with all exact positivity and rounding asserts PASS, local file /mnt/data/xh_s7_rot007/local_independent_check.py SHA-256 `a53adc39144c2af98214b46d8fe88d251013f3d9c5ac4707faa2db3cb556bef5`, generated JSON /mnt/data/xh_s7_rot007/rot007_local_referee.json SHA-256 `c2a936e6f2b79957df24a67fdff2523669e9ec6e5d93b426b647d0237f9ad551`. GitHub source public code is independently reviewable; its exact execution has NOT been claimed.

PRIORITY FOR OWNER Badacz/Mech-S10/Moderator, not XH action: PREREG079 needs AUTHOR-NATIVE signed net `s(t)` including distinct positive/negative channels, original evaporation discontinuity/event location and fidelity of interpolation through that event. Before interpreting `D_j=+.27..+.30 dex` as physical helium/PBH constraint, measure sign/cancellation and time support of native source, compute independent network convolution and validate reconstructed `DeltaY_code` against actual code. If source sign cannot be certified, the raw `G_code/G_net` positive 6–29% point ratios cannot be promoted as an integrated multiplicative physical correction. Mech-S10's separately identified event alias guard is distinct and remains independently required.

No extra native run executed, no original Badacz PREREG079 executed, no proxy PBH mass bound, no claim of theorem novelty; no retroactive use of second code source as independent physical I1. NO OWNER TASK CASCADE; owner may explicitly take the source-sign test as an adjudication criterion.

FINAL: ROT007_CONDITIONAL_SIGNED_TWO_IMPULSE_GAIN_TRANSFER_COUNTEREXAMPLE_EXACT_PASS / FOUR_DECIMAL_ROUNDING_ROBUST_PASS / NONNEGATIVE_SOURCE_WEIGHTED_AVERAGE_CONTROL_PASS / ORIGINAL_2026_BURNS_ATLAS_GLOBAL_VS_IMPULSE_TYPE_DIFFERENT_PASS / NATIVE_BBN_SOURCE_SIGN_DISTRIBUTION_NOT_READ / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
