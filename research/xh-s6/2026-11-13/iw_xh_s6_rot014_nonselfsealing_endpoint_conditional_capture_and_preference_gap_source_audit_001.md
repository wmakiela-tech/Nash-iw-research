artifact_id: IW_XH_S6_ROT014_NONSELFSEALING_ENDPOINT_CONDITIONAL_CAPTURE_AND_PREFERENCE_GAP_SOURCE_AUDIT_001_20261113
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
to_cell_or_route: IWTO_MODERATOR
return_id: IW_XH_S6_ROT014_NONSELFSEALING_ENDPOINT_CONDITIONAL_CAPTURE_AND_PREFERENCE_GAP_SOURCE_AUDIT_001_20261113
result_class: NEGATIVE_SELF_SEALING_DIAGNOSTIC_AUDIT + ACTUAL_ORIGINAL_AUTHOR_SOURCE_MODEL_11520_ROW_INDEPENDENT_REANALYSIS + SEED_BLOCK_BOOTSTRAP + EXACT_PREFERENCE_GAP
status: ROT014_SELF_SEALING_FALSIFIER_PASS / PREVIOUS_XH_ENDPOINT_5OF5_OVERCLAIM_WITHDRAWN / CORRECTED_CONDITIONAL_3OF5 / SOURCE_GAP_5OF5 / REPRODUCIBLE_LOCAL_PASS
date: 2026-11-13
claim_ceiling: MATHEMATICAL_IDENTITY_AND_FINITE_ORIGINAL_AUTHOR_TRAINED_SOURCE_MODEL_OUTPUT_POSTPROCESS / NO_NEW_AUTHOR_RNN_EXECUTION / NO_MONKEY_DATA / NO_NEUROSCIENCE_DISCOVERY / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
guards: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_OWNER_TASK_CASCADE

# XH-S6 ROT014 — A self-sealing diagnostic falsified: five dlPFC unconditional endpoint majorities become only three conditional majority captures; distinct original model preference gap retained

## 0. Critical scientific correction — anti-self-sealing first

ROT013 reported 5/5 source-selected dlPFC original-model units crossing a *home-made* endpoint-majority diagnostic:
E(B,S,P) = 1{S=B or S=P},
where B is final no-stimulation (SHAM) direction, S is the same-source-noise stimulated choice, P the specific stimulated original model unit's preferred direction.

This is logically SELF-SEALING as a criterion for actual preferred-direction capture: under the NULL "stimulus changes nothing", S=B on all trials, so E=1 on 100% of observations regardless of any neuronal or model perturbation mechanism. Exactly,
E = 1{S=B} + 1{S!=B and S=P}.
Thus the ROT013 5/5 endpoint-majority verdict is NOT a defensible standalone falsifier of an absent stimulation effect. This is a documented XH-S6 analysis error, NOT an error attributed to the authors.

**NEW CORRECTED descriptive diagnostic**: restrict to genuinely changed selected model decisions S!=B; report P(S=P | S!=B) = changed-and-captured / all-changed. Under a perfect no-op, the denominator is zero, so the conditional statistic is UNDEFINED rather than falsely positive. IMPORTANT: conditioning on a post-stimulation outcome is not a causal effect estimator; it describes the outcome mix, and should not be used as formal neuronal-inference evidence or a claim about an unobservable biological counterfactual.

## 1. Original source priority and primary biological evidence are separate

First authors: Douglas A. Ruff, Sol K. Markman, Jason Z. Kim and Marlene R. Cohen, *Information formatting in neuronal populations predicts differential functional contributions to behavior*, *Nature Neuroscience*, published 10 November 2026, DOI https://doi.org/10.1038/s41593-026-02514-7 . The original OPEN-ACCESS article already states that their dlPFC-like source model sometimes selected the motion direction and sometimes selected the stimulated-unit preferred direction, with essentially no intermediate choices. It also reports experimental monkey data, a DISTINCT evidentiary class, and explicitly says the model-data correspondence is qualitative rather than quantitative. Therefore the XH-S6 source geometric-gap observation is NOT a novel winner-take-all discovery and is NOT a challenge to the authors' scientific claims.

Original author repo https://github.com/solkm/formattingRNN exact frozen commit **7889a81e298c01532a313e02971c11dbc9db8eb0**. ROT013 used the actual author DotsTasks and vendored PsychRNN original classes, original actual trained MT and dlPFC NPZ weights (original MT source Git blob c5e701740f8ab1d19ca07415c0de2d6e7f88c37f and dlPFC blob 47142e3dee920a759406136449f0b12f9ce752ee), original 5 MT and 5 dlPFC stimulated unit/strength selections parsed from the authors' own source generator, original reward_rel180 and nonzero source input/recurrent noise. Each original unit had sixteen 72-direction seed-blocks with common-random-number sham/stim matching, not the authors' 250 repetitions per direction.

**NO AUTHOR MODEL REEXECUTION OCCURRED IN ROT014.** The entire numerical audit processes real previously observed ROT013 original-author native model outputs. The actual source model run is GitHub Actions **43430223171**, job 131901564479, COMPLETED SUCCESS:
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43430223171
Source native model data 11,520 sham/stim paired rows, from 23,040 executed source author Task+Simulator arm trials in ROT013; the original 2,018,806-byte source-runner CSV exactly SHA256 **e6717506d9d2f1a7d65fd7b25741e01d54d3c75f53145e97541c98933274db84** and 29,555-byte source-runner JSON SHA256 **d55f5db10890f67435ea4b46b119d4aa53db78f367f66ee05cc791fdfa71b4ef**. Both were read from current container-backed original source archive and independently SHA-locked before any processing.

Original upstream ROT013 source science report PINNED:
https://github.com/wmakiela-tech/Nash-iw-research/blob/011a3649b9c0a6974c6b2f0635af179a773e9c3e/research/xh-s6/2026-11-13/iw_xh_s6_rot013_all_ten_original_model_units_reward180_geometry_falsifier_001.md

## 2. Corrected numerical table — original dlPFC source units, n=1,152 each

| Author source dlPFC unit | Original strength | ROT013 old E positive (all 1152) | Genuinely changed decisions | Exactly P among CHANGED | Corrected capture | Whole-16-seed-block 95% descriptive interval |
|---|---:|---:|---:|---:|---:|---|
| 53 | 45 | 686/1152 = 59.55% | 827 | 361 | **43.65%** | 41.99–45.33% |
| 25 | 45 | 892/1152 = 77.43% | 821 | 561 | **68.33%** | 66.20–70.33% |
| 54 | 45 | 954/1152 = 82.81% | 668 | 470 | **70.36%** | 68.16–72.78% |
| 8 | 45 | 986/1152 = 85.59% | 646 | 480 | **74.30%** | 72.30–76.46% |
| 9 | 48 | 593/1152 = 51.48% | 1034 | 475 | **45.94%** | 44.74–47.04% |

Observed finite changed-choice preferred-capture majority >50% is thus **3/5**, not the previous unconditional endpoint-majority 5/5. Both unit53 and unit9 fall BELOW 50%, and their descriptive whole-seed-block bootstrap ranges also lie fully below 50%. The 3 others have descriptive intervals wholly above 50%. These intervals are 10,000 deterministic bootstrap resamples of WHOLE original sixteen seed-blocks, NOT thousands of independent monkey/neuron trials and NOT population inference.

The exact algebraic decomposition reconciles ALL five old counts with the corrected source counts. E.g. dlPFC53: 325 unchanged +361 changed-and-preference =686 old endpoint-positive; dlPFC9: 118 unchanged +475 changed-and-preference =593. It is inappropriate to erase the old recorded observations, but old numbers cannot be promoted as evidence of preferred choice capture by the same criterion.

MT comparisons remain distinct: all five author-source MT units still have more than half of ACTUALLY CHANGED choices strictly in the unique circular shorter arc toward stimulated preference. The corrected changed-only numerator conditional rates are MT37 978/1150, MT4 990/1070, MT42 1075/1130, MT25 993/1121 and MT34 937/1094. Each genuinely changed source-model choice is distinguished from an unchanged final bin. MT25 still provides a real original-source counterexample to a sweeping "MT NEVER chooses EXACT preferred direction": seventeen changed MT25 source outputs equal its preference at source reward_rel180. This is a finite single-network source model, not biological population evidence.

## 3. Separate positive finite geometry: exact stimulated P OR a source output at least 70deg away

Independently of the defective unconditional endpoint threshold, the ACTUAL original author RNN source-stimulated dlPFC output distribution has an unusually clean source-model angular gap:
For each of the five dlPFC source-author selected units and all 1,152 actually simulated source task pairs, S is either EXACTLY at that original stimulated unit's preferred output 5deg bin, or d(S,P)>=70 degrees on the circle. In particular, **ZERO of 5,760 stimulated dlPFC source choices lie within the nonpreferred 5deg–65deg annulus**:
- Original source stimulated selected P exactly: 2,347/5,760 across these five units;
- All other stimulated selected bins: 3,413/5,760, all at least 70deg away from P.
- Minimum nonpreferred stimulated choice angular distances: dlPFC53 70deg, dlPFC25 100deg, dlPFC54 100deg, dlPFC8 100deg, dlPFC9 80deg.
- By contrast, the corresponding 5,760 source NON-STIMULATED sham choices in precisely the same selected author-unit/noise conditions occupy the 5deg–65deg annulus **1,067** times.
- For MT, nonpreferred stimulated choices occur in that same angular annulus 2,236 times across 5,760 selected original source MT unit trials.

This finite-run directional **preference-gap** diagnostic is more narrowly defined and does NOT count no-change output as automatic support. It is qualitatively consonant with the original authors' own source-model "winner-take-all, essentially never in between" observation. The chosen gap radius of 65deg is DATA-OBSERVED, NOT preregistered, so neither the zero count nor a nominal "5/5" is a confirmatory statistical test. It is a DESCRIPTIVE SOURCE MODEL FINITE OUTPUT SIGNATURE, not an attractor-mechanism theorem, biological law or novel scientific result. Without other seeds, strengths, full published 250-per-angle simulations and actual neural data this is not universal.

## 4. True source-model sham-only negative comparator

Within each of the original five dlPFC selected units, the original source-model SHAM outputs for adjacent independent original seed blocks were compared at the same shown motion direction. Exactly 15 x72 =1080 independent-seed-pair comparisons per unit, total 5,400 (dependent reuse of individual seed blocks). No stimulation in either sham arm. Across five units, 2,903/5,400 sham-to-sham choices differ due to BOTH changed source noise and random onset times; 0 of these changed sham-to-sham choices land exactly at the selected unit's P in the source data (corresponding original selected sham P count is zero). These are not 5400 independent experimental observations or pure noise-only draws. They show why a raw choice mismatch is not equivalent to preferred-direction capture nor stimulation response.

## 5. Actual independent code execution and falsification controls

Standalone independent Python3 standard-library script, source SHA256 **a65296cf437681d4ac2d1a7bd46b68f868368d2600dd89535af21d315329928f**, executes on the ORIGINAL ROT013 source output files. It verifies every original 11,520 source model row against the actual source summary, source model stimulus unit+strength, original timing grids, all 10x16x72 source unit/seed/direction identities, circular geometry and exact source output flags, and argmax margin preservation theorem. It calculates the old endpoint logic, decomposes it into unchanged+changed-and-P, changed-choice conditional capture, nonpreferred annulus, comparison to sham-only, and fixed deterministic bootstrap of whole original seed blocks.

IMPORTANT methodological safeguard: Script FAILS on SOURCE or numerical integrity errors but **does NOT require any scientific hypothesis to PASS**. An actual source-model counterexample is reportable instead of triggering a program failure. This avoids another circular/self-sealing "unit must fit" test.

Actual isolated clean reexecution into a fresh empty directory regenerated the THREE derived numerical products BYTE IDENTICALLY:
- complete independently audited numerical JSON source SHA256 **59c5188037ea1e65fd19203e7dbf750f1bb7551f7a1c675eeb85b56f4f11151b**;
- 10-unit corrected conditional CSV SHA256 **b7b3a3921daeec8ef54e5bbc43515f752bc49076413cbb6c5656c0df1c186846**;
- 160 seed-block corrected audit CSV SHA256 **abda5f06d0931b13ca15256be3927409de66999d24c3492ad268637d4b3cd2ca**.

Two material independent NEGATIVE mutation controls actually executed:
- truncating original model CSV violates pinned SHA and fails closed with SOURCE_IDENTITY_FAIL: PASS;
- changing original model runner summary JSON violates pinned SHA and fails closed with SOURCE_IDENTITY_FAIL: PASS.

Full user-local archive *ACTUALLY CREATED AND VERIFIED*, contains entire original author-model 11,520-row CSV, actual original-runner JSON, complete independently executed analysis script, full independent JSON, corrected 10-unit CSV, 160-block CSV, full stdout, execution receipt, README and SHA256 manifest:
IW_XH_S6_ROT014_NONSELFSEALING_ENDPOINT_GEOMETRY_REPRO_20261113.zip;
**467,446 bytes**, SHA256 **9ac161ea2439f7ca780bf2840b656d177ee79a7201c4f62cc6a47ced95d67211**. ZIP CRC PASS, 9 of 9 file payload SHA256 PASS, SHA manifest PASS. Original author trained binary NPZ source models are referenced by immutable author Git commit and not redistributed.

PUBLIC machine-readable numerical certificate, exact GitHub write and FULL pinned byte-identical readback PASS:
https://github.com/wmakiela-tech/Nash-iw-research/blob/0857e28af55fab809e7914e2ee02c1ca50be8434/research/xh-s6/2026-11-13/xh_s6_rot014_conditional_capture_source_falsifier_certificate_001.json
Git blob 8869990e648ec8290755897494cb689e07d657e1, source unit counts, original SHA and local evidence SHA identities, descriptive bootstrap and guards.

## 6. Verdict and implications for predecessor claims

- **WITHDRAW as diagnostic** the ROT013 assertion that 5/5 unconditional dlPFC endpoint-majority is independently informative about actual stimulation, because an absolute no-op produces E=100%.
- **REPLACE** its preferred-choice-capture component with changed-choice conditional measure. For the five source author-selected dlPFC units it is only 3/5 majority, with 2/5 robust descriptive below-majority units (53,9). Do not falsely claim a 5/5 majority after conditioning.
- **RETAIN** the underlying actual 11,520 source model rows and original author priority unchanged. ROT013 is not numerically invalid; one home-made scientific criterion was logically insufficient.
- **RETAIN separately** the finite original source model geometric exclusion gap, no nonpreferred stimulated dlPFC final direction 5deg-65deg from P for these 5 x1152 source rows. It supports only qualitative source-model description already present in the original paper, not a biological mechanism inference.
- Recognize conditioning on a changed choice is POST-INTERVENTION SELECTION: the corrected proportion is not automatically a valid causal estimand. More meaningful tests would model full choice distributions under stimulation versus sham and source paper's original estimation procedures.
- BW GITHUB_PENDING_BW_INGEST, NOT ingest receipt. No independent referee acceptance, Moderator canonical adoption, external paper novelty or EXEC_SIGN. No PBH/BBN, no clinical/biological inference and no new owner task cascade.

STATE: XH_S6_ROT014_SOURCE_DATAROWS_11520_PASS / SELF_SEALING_DIAGNOSTIC_FAIL_AND_CORRECTED_3OF5 / FINITE_PREFERENCE_GAP_5OF5_DESCRIPTIVE / CLEAN_REPRO_PASS / GITHUB_PENDING_BW_INGEST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
