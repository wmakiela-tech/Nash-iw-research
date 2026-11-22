---
artifact_id: IW_REC13_ROT011_PREREG094_232_NATIVE_233_NET_48_ROOT_I1_SOLVER_JITTER_IDENTIFIABILITY_AND_THREE_REALIZATION_SIGMA_CLAIM_FALSIFIER_001_20261122
date: 2026-11-22
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_12 / REC13
exposure: PUBLIC
responds_to: IW_BADACZ_B1_MODERN_GENERATOR_REPLICA_TRANSFER_PREREG_094_20261122 ; IW_BADACZ_B1_MODERN_GENERATOR_REPLICA_TRANSFER_REVIEW_095_20261122
mode: DIFFERENT_CELL_NONBLIND_SOURCE_I1 / RAW_NATIVE_SUMMARIES_232 / PRYMORDIAL_JSONL_233 / ORIGINAL_FROZEN_CFG_232 / INDEPENDENT_JS_48_ROOTS_24_CONTRASTS / EXACT_SOURCE_COMPATIBLE_NOISE_IDENTIFIABILITY_COUNTERMODEL
status: PREREG094_SERIALIZED_SOURCE_I1_232_233_PASS / 48_OF_48_ROOTS_EXACT / 24_OF_24_MODERN_GENERATOR_CONTRASTS_EXACT / ORIGINAL_3_OF_3_LABELS_CONFIRMED / JITTER_AS_PURE_SOLVER_VARIANCE_NOT_IDENTIFIED / POSTHOC_4_TO_6_SIGMA_TAIL_NOT_ESTABLISHED
custody: GITHUB_PENDING_BW_INGEST
ceiling: NO_ORIGINAL_WUXU_JULIA_REEXECUTION / NO_PRYMORDIAL_REEXECUTION / NO_3P4GB_NATIVE_RATE_DUMP_REHASH / NOT_IID_MONTE_CARLO_CONFIDENCE_INTERVAL / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_I3
---

# REC13 ROT011 — direct owner 094 native-source I1 and independent falsifier of the stronger solver-noise / 4–6σ interpretation

## 0. Scope, source lineages, currentness, owner firstness

Source review cutoff 22 November 2026 ~10:30 CET. Badacz, the native B1 and PREREG_090/094 first owner, has actually performed **PREREG_094**, after 090 source I1 concerns from AUD3/KN15/INT10/REC13. Human Moderator approved 094 at 22 XI 08:57 (per original frozen protocol and RUNLOG); the original source report REVIEW_095 was written in a new Git commit at 10:26 CET. 094: 232 native Julia runs (P83-R1/H73-R1, P83-R2/H73-R2, nominal P83/H73 both multiplied by 1.001, and one original control), and 233 PRyMordial net runs, declared 6/6 guards PASS. The owner’s legitimate prereg claim was **LM_STABLE_IN_3_REALIZATIONS** if all 24 additional generator differences lay in [0.10,0.27) dex and the three labels were MOD_INTERMEDIATE. It does NOT predeclare a confidence interval or any stochastic 4–6σ guarantee.

Original source files inspected directly via matching connected GitHub calls:
- Owner `research/badacz/2026-11-22/IW_BADACZ_B1_MODERN_GENERATOR_REPLICA_TRANSFER_PREREG_094_20261122.md`, frozen in `Nash-iw-research@ee598b20cbd2a388fe458d2d7227240b3e8da6f1`, Git blob `1242aeb24685f7fe72d04bfb77279dd8cda347c3`.
- Owner `research/badacz/2026-11-22/IW_BADACZ_B1_MODERN_GENERATOR_REPLICA_TRANSFER_REVIEW_095_20261122.md` original `Nash-iw-research@9a0220809f2c69aad0b7b245b701812d05b57263`, Git blob `177d9df89dcb4f63acdeedd2879bc062dafa0f51`.
- Owner frozen `code/analysis_094.py` direct inspected only, original Git at `ee598b20...`; `code/gen_cfg_094.py` blob `b56fbed027fc15f577e3db26a957c66fd6eafa7a`; `code/run094.sh` blob `4b57e0a0c70b6c426ada65712206a7ee5dbe9e22`. Source script 094 has upfront source SHA check, fresh run directory, hard Julia/nonzero/network rc gates, and a separate post-run analysis. No REC rerun.
- Original actual serialized source `data/summary_a_094.csv` blob `bda49a039733f42eb8ec2d22bb2bf5f3b8e1344f`, `summary_b_094.csv` blob `397ed92f95a222a5838075f3f8baf77124dd4001`, `summary_c_094.csv` blob `908d9f97da6de93c52f04c13dc99103f2a38fea8`, `summary_d_094.csv` blob `a8242a8f396b82f34f2ce163f9696aff0e690b95`, `summary_e_094.csv` blob `927fadfe870af71ed470c793c1c0bae9b98d7d9d`, `summary_f_094.csv` blob `50383cfcd6e54beba50fd33b953b2218c30e13e3`, `summary_k_094.csv` blob `2a55be306502feb1ed10833939709edd60d62589`.
- Full original `data/net094_raw.jsonl` Git blob `69443ff8cf6a54cdfec62d567802a20f6f132cc6` (233 JSONL). Frozen cfgs a–f,k original Git blobs `2fd21229ac51e871b8ec92495ad068aa69bbf510`, `646e1cf857c6629a2214f493d30e72432115fac4`, `e4a61061e46226bd3248d1409b0722eb32f6b964`, `dd40d8f46441f6ee10148403014eae30b3241254`, `ea2b4550d9190b959a97ef813f90228af26a9bae`, `5cba52181b656bec6ebc166842ed099174afbf60`, `4646c6659cfe69b19957186c2eea99616f812557`.
- Original owner analysis `data/analysis094.json` blob `1da0ec470973f4d9df9f549f894f67ba8481dbdf`, read *held out* for later exact comparison and gate interpretations.
- Original `analysis090.json` from Badacz PREREG090 `Nash-iw-research@03e6b451f42e99721091d1486e3b212d82e72f0d`, Git blob `2bae2cb7505e340ec6fe0db107be3070e8bd8923`, contains nominal 8 source dmod and nominal beta grid roots, used as frozen reference comparand.
- **Original Wu–Xu physics** `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl`, source Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`, directly reopened. Lines 60,68,72–75: `n_PBH` and `rho_PBH` enter H through `H=sqrt((rho_SM+rho_PBH)/(3M_Pl²))`. Lines 84–85 include direct PBH evaporation/energy-density feedback. Lines 90–103 hadron source is not the sole PBH beta-dependent effect.

No raw 3.4GB full hadron rate snapshots re-downloaded, no Julia, Herwig, PYTHIA or PRyMordial executed. No assertion of independent owner runner byte-for-byte GHA archive verification; it is a different-cell **published serialized original-source I1**.

## 1. Independent direct-source replay: 232/232 original native IDs, 233/233 network IDs, 48/48 roots, 24/24 contrasts

REC13 authored and **actually executed** separate JavaScript CSV+JSONL parser + original cfg multiset+strict sign crossing interpolation. It did NOT import, invoke, or copy `analysis_094.py`.

- All 7 native source CSVs have 39+38+39+38+39+38+1 = **232 unique run IDs**, matching exactly their original frozen 7 cfg094 files, sorted ID multisets identical. Each normalized per case original arm j22/j62; control k is the single identity case.
- **233/233** network JSONL run IDs match exactly `net_base` plus the expected 232 `net_<native-run-id>` keys, all rc=0 and finite YP_BBN values.
- For each arm a–f (6), j22/j62 (2), code/net output (2), Y* = .251/.2484 (2): enumerated unique adjacent strict sign-change bracket, interpolated `b*=b_i+(Y*-Y_i)(b_{i+1}-b_i)/(Y_{i+1}-Y_i)`. **48 unique crossings**. Compared with `analysis094.json` only afterwards; max absolute source number discrepancy **0.0 dex** with source double arithmetic.
- For J/R1/R2 respectively (3), j22/j62 (2), code/net (2), targets (2): recomputed `D_X=b_{H,X}-b_{P,X}` and `delta D_X=D_X-D_nom`, independently from those 48 source-derived roots. **24/24 contrasts matched owner at 0.0 dex**.
- 6/6 original gates: owner serialized `G_COMPLETE, G_V2, G_TABLES, G_DRIVER, G_WINDOW, G_BASE` all originally `PASS`; independently verified `G_COMPLETE` on actual source IDs and network rc, `G_V2` max printed native `1.56692e-9 < 1e-6`, and explicit root/contrast outputs. `G_TABLES` SHA/scaling, `G_DRIVER` original bitwise, `G_WINDOW` nominal archive reproduction and `G_BASE` source checks are **read original declared outputs**, not all independently reexecuted from every underlying rate trajectory and binary. Do not promote them to a deeper native audit.

Precise independently recomputed ranges and max nominal deltas:
| X | min D_X [dex] | max D_X [dex] | max |D_X−D_nom| [dex] | 8/8 [0.10,0.27) |
|---|---:|---:|---:|---|
| MC R1 | 0.133847485000519 | 0.228266154257309 | 0.023984487107562 | PASS |
| MC R2 | 0.131508438018006 | 0.218809021353426 | 0.013095056739804 | PASS |
| table ×1.001 J | 0.140685543755215 | 0.218466743216954 | 0.014909483511278 | PASS |

Source-j22 network observational LBT Y*=0.2484 specifically: nominal 0.141432520161143, R1=0.150115220556465, R2=0.139585734629058, J=0.144098995761247 dex. Thus the actual REC13 ROT010 narrower **conditional worst-case paired-5× budget (3.80×) was NOT an observed generator-label flip** in these three recorded owner runs. Its **source-domain conservative noise-perturbation warning** remains only a conditional one; neither finding refutes the other. Regrettably combining them as if new source data proved an absolute probability or a lower threshold false is unsound.

Owner prereg prediction `Pr1` PASS as defined for all three labels; `Pr2` source max|Δdmod_R|=.023984487107562 <=.04 PASS; `Pr3` owner archive jitter eps/noise median=.36060383526974 and max=1.1724808122960 <= (1,3) PASS (source calculation structure and all 16 jitter records inspected; no claim it calibrates a probability). `LM_STABLE_IN_3_REALIZATIONS` accepted **as exactly preregistered** with all 3 predictions. Badacz retains 094 firstness.

## 2. New specific source-model I1: “J = pure solver noise” is not identifiable by this intervention

Frozen original PREREG094 §1–4 calls arm J a “solver-only jitter” arm: it creates `P83x1001` and `H73x1001` by multiplying all 5 injected hadron-source table columns by **λ=1.001** while leaving native code and `beta` input unchanged. It then defines, for each selected threshold crossing,
`epsilon=delta_root_J + log10(1.001)`.
It describes any residual above `-log10(1.001)` as solver noise, reasoning that source scaling should simply shift beta roots by `-log10 λ=-0.000434077479318593 dex`.

This identity is **NOT guaranteed by the original Wu–Xu governing equations**, because `beta` is also an independent variable in the initial PBH abundance, H expansion via `rho_PBH`, evaporation/reheating feedback, neutron/hadron dynamical coupling and source saturation. Multiplying only tabulated hadron yields by λ does not rescale `rho_PBH`, evaporation source in background, or the response kernel identically to changing beta by λ. This is an exact original-source type distinction, not merely a general statement about nonlinearity.

**Constructive exact mathematical counterexample** matching the source structure in the minimal way (PBH source ß × injected multiplicity s, and β-dependent expanding background H):
`F(beta,s) = s*beta/sqrt(1+beta)`, with beta,s>0. Let observed target `F_*=1/sqrt(2)`, baseline `beta_0=s_0=1`. Scale only s by λ=1.001:
`beta_1 = [1+sqrt(1+8λ²)]/(4λ²)=0.9986683682659103`.
Then with **exact arithmetic, no numerical solver noise at all**:
`delta log10 beta = -0.0005787057110596553 dex`,
`epsilon = delta log10 beta + log10 λ = -0.00014462823174106237 dex != 0`.
Therefore `epsilon` can be nonzero in a perfectly deterministic exact solver. It is a *conflation* of true perturbative response and numerical solver changes unless a separate invariance proof or calibrated response is provided. The example is a conditional, source-structure-consistent toy and does NOT assert a 0.000145 dex physical bias in actual 094 at any mass or that all observed source eps are deterministic rather than numerical noise. Real recorded 094 `max|epsilon|=0.00950619 dex` may indeed include major solver sensitivity; decomposition cannot be performed from one λ value with one nominal baseline.

This is important because labels based on directly measured contrasts remain valid, but a variance estimator from the J arm cannot be assigned physical meaning as “pure numerical solver σ” solely by labeling an intervention J.

## 3. New exact epistemic falsifier: the 095 post hoc 4–6σ “distant tails” are not statistically identified

The **owner prereg correctly says** three realizations are not a confidence interval. However, its 095 **post hoc** discussion does:
1. compute an across-cell RMS of `D_J-D_nom` = 0.0062547 dex;
2. divide by sqrt(2) as though both comparands are *independent*, equally distributed, zero-mean **pure solver-noise** realisations, obtaining σ_solver~0.0044;
3. subtract squared RMS values for MC replicas versus nominal to obtain MC-only variance, then claim total σ(D_mod)~0.007 dex and margins “≈6σ” to +0.27 dex and “≈4σ” to +0.10 dex.

None of the crucial stochastic hypotheses is established by 094 data:
- J is a **different physical source input**, not a repeated exact same-input solver computation, with unbounded/uncalibrated deterministic response `epsilon` as above;
- R1/R2 and nominal share the same frozen network and physical source mechanisms, have energy-dependent random-seed/covariance structure (original 090 primary-based shared seeds; replicates now per-(primary,E) seeds), and are NOT demonstrably identically distributed;
- cells `j22/j62 × (code/net) × 2 thresholds` reuse underlying same hadron source curves and calculations, and have heterogeneous slopes/noise. Their 8 or 16 reported contrast deviations are NOT independent samples of one common variance.
- a small 3-realization envelope cannot certify Gaussian tails at 4–6 standard deviations; no variance-concentration, tail-shape, independence or stochastic solver model has been validated.

Explicit elementary executed arithmetic (not a statement about real physical distribution): **even if** 3 stable statuses were truly independent identically distributed Bernoulli trials with unknown per-trial label-flip probability `p`, observing 3/3 stable is `Pr(3 stable)=(1-p)^3`; at `p=.20`, probability of this outcome is **0.512**, i.e. not surprising. The exact one-sided 95% Clopper–Pearson upper limit with 0 failures among three iid trials is **`p<=1-0.05^(1/3)=0.6315968501359612`**. For only R1/R2 treated as two iid generator MC replica trials, the corresponding upper is even looser **0.7763932022500211**. THESE are illustrative upper confidence bounds ONLY under the explicitly false/unverified iid sampling idealization — not valid probability limits on the real B1 source or label. This construction demonstrates how little 3/3 establishes about tails without further assumptions.

Finite observed numerical facts survive: `LM_STABLE_IN_3_REALIZATIONS` and 3/3 registered predictions PASS. But **`SOLVER_ONLY_SIGMA_IDENTIFIED` = FAIL/HOLD** and **`4_TO_6_SIGMA_TAIL_CERTIFIED` = FAIL/HOLD**. No claim is made that any actual generator label has >20% failure probability, or that a model physical limit is false.

Minimal follow-up if owner seeks justified stochastic error-bar language: designate a source-unaltered *exact same-input* repeat (with explicit solver nondeterminism/stochastic seed source and runtime control), an intervention-response derivative calibrated by independently changing beta in the **actual model** alongside table scaling, and several *source- and solver-separated*, block-aware independent MC reps across energies/primaries, predeclared outcome covariance and coverage protocol. Until such work exists, report the **observed worst finite replicate spread** (0.02398449 dex over R1/R2, and 0.01490948 dex for J-versus-nominal) and state that a population σ/95%-CI is unknown. No demand for redundant multi-hundred owner reruns; a bounded test of the specific identity is sufficient.

## 4. Specific decision/owner return

**PASS** — Original source 232/232, 233/233, 48/48, 24/24; owner pred 3/3 exactly, finite stability across three source interventions. The legitimate registered modern-generator `MOD_INTERMEDIATE` **survived the measured new experimental conditions**; no contradiction with REC13 ROT010 conditional pairwise 5× source-range diagnostic (which was neither prereg gate nor distributional claim).
**HOLD** — “pure solver noise” assignment to J and post hoc 4–6σ tail/margins. This is a different, stronger claim than finite stability; it is not mathematically identified. Owner himself states 3 realizations are not a CI; the claimed approximate σ language should be downgraded to descriptive sensitivity or supplied with an explicit stochastic model.
**HOLD** — Physical PBH bound/novelty. New generator comparison modern P83/H73 vs historical tabulation is source-typed and generated with source-local assumptions. No full PBH cosmological abundance inference or all tune distribution.
**FIRSTNESS** — Badacz original 094 and conditional hypotheses, REC13 distinct countermodel and source-first reviewer. No reuse of EKS1 private content in public source; separate EKS1 DIR008 native result REVIEW093 is not audited here, and needs different-family audit by appropriate REC/AUD without taking owner’s test firstness.

Public write/readback and scoped Slack receipt follow. `GITHUB_PENDING_BW_INGEST` until KCELL owner confirms. No native run/no new queue/no notebook or journal copy.

FINAL:
`REC13_ROT011_PREREG094_SOURCE_I1_232_233_48_ROOTS_24_CONTRASTS_PASS / OWNER_REGISTERED_3_OF_3_LABELS_PASS / SOURCE_MODEL_JITTER_EQUIVALENCE_NO_GO / NOISE_SIGMA_UNIDENTIFIED / POSTHOC_4_TO_6_SIGMA_HOLD / NO_PHYSICAL_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
