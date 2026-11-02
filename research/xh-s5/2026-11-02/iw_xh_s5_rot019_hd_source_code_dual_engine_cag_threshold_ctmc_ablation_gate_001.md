# XH-S5 ROT019 — Original 2026 Huntington CAG model: dual engine thresholds and independent CTMC ablation

artifact_id: IW_XH_S5_ROT019_HD_CAG_DUAL_ENGINE_THRESHOLD_AUDIT_20261102
return_id: XH-S5-ROT019-HD_CAG_SOURCE_CODE_ENGINE_THRESHOLD_SENSITIVITY_20261102
date: 2026-11-02
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
exposure: PUBLIC
claim_ceiling: ORIGINAL_PUBLISHED_FULL_HTML_AND_AUTHOR_GITHUB_READ / EXACT_INDEPENDENT_MARKOV_GENERATOR_ANALYSIS / INDEPENDENT_UNIFORMIZATION_SPARSE_ODE_GILLESPIE_REPLAY / NO_AUTHOR_R_SHINY_EXECUTION / NO_AUTHOR_CLINICAL_OUTCOME_REPRODUCTION / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST

## Source first, authors' findings not ours

Bryan P. Simpson, Paul T. Ranum, David E. Leib and coauthors, "Computational modeling and preclinical evaluation support targeting somatic instability for Huntington's disease treatment", Nature Communications 17, 11036, PUBLISHED 2026-10-28, DOI https://doi.org/10.1038/s41467-026-78769-2 . Original Nature full HTML, including Methods "Simulating CAG repeat expansion in MSNs", checked this rotation. Authors report therapeutic AAV-MSH3 preclinical knockdown in nonhuman primates and mice and MODEL-PREDICTED changes in progression. They have NOT shown clinical human efficacy; n=2 NHP per dose group limits assessment of variability. The authors' README explicitly says the tool is for research, not for individual medical prognosis or care decisions. This XH work evaluates an independent mathematical parameter ablation, not therapeutic safety, human course, dose response, progression, or efficacy.

Author ORIGINAL software GitHub: https://github.com/LatusBio/HD_Model_NatComm_Publication/tree/b9de42ac6f634d137f68e57b059caf08f9ef4d05
Verified pinned commit b9de42ac6f634d137f68e57b059caf08f9ef4d05 (2026-10-28). Read README, global.r, ui.r and server.r source code (not only abstracts):
README Git blob 7172479e7ce11576b8f6145022c84373f00d3685;
server.r Git blob 5e60890235717e67b629d061cf122e4c539bd0f6;
ui.r Git blob 227bbc246075148cce48fd048d681719e1f1c185.
README explicitly announces TWO simulation engines:
- event-sampling model T2=55 repeat CAG;
- recommended Handsaker CTMC model T2=72.2 repeat CAG.
Both share T1=33.5; separate algorithmic differences beyond phase threshold. Authors ALREADY DOCUMENT this choice, so do NOT assert a discovered hidden code defect or a published figure inconsistency. Source full code and its restricted terms were not redistributed; no original R/Shiny engine executed.

Mature prior: Handsaker et al., Cell 2025 DOI 10.1016/j.cell.2024.11.038 for two-phase repeat expansion, standard birth-death CTMC, uniformization and ODE methods all predate XH. Public NASH code search "Huntington CAG", "LatusBio", "CTMC 72.2", "MSH3" yielded no indexed hit, not evidence that private BW lacks prior art.

## Pre-specified control: change ONLY T2, keep same CTMC family

From ORIGINAL Nature Methods, mean net rate mu(x)=r1*max(x-33.5,0)+r2*max(x-T2,0), r1=.035, r2=.576. From ORIGINAL source R code server.r (around lines 53-93), use p_exp=.676 and derive CTMC jump intensities:
net_factor = 2*p_exp - 1 = .352;
q_up(x)=[mu(x)/.352]*.676;
q_down(x)=[mu(x)/.352]*.324.
Apply in exactly the SAME continuous-time Markov birth-death engine with two counterfactual thresholds T2=55 and T2=72.2, keeping all other parameters fixed, NO therapy, no transduction, no patient-specific covariates. A unit of CTMC time is one year under model assumptions. Initial CAG x0=50,55,60; reported t=5,8,12. Upper state capped/absorbing at 240, with explicit cap checks 180/240/300/500. The evaluated endpoint is model marginal Pr[X(t)>=150] (NOT the probability of EVER crossing and NOT clinical risk). Upper cap materially affects EXPECTED capped CAG at long times; do not interpret expectation as a source physical observable without additional cap checks.

## Exact analytical local sensitivity, including at matched starting drift

At x=60:
 mu_55(60)=3.8075 net repeats/year, mu_72.2(60)=.9275 net repeats/year; ratio 4.1051212938.
At x=55 BOTH phase alternatives have identical initial mu(55)=.7525. But when the first +1 jump occurs, x=56 immediately enters the rapid term only for T2=55. Exact Fraction generator calculation:
 d² E[X(t)]_55/dt² at t=0 MINUS d² E[X(t)]_72.2/dt² at t=0 = 457821/550000 = .8324018181818181.
The derivative check is EXACT for source-like CTMC rates; no stochastic uncertainty, no novelty.

## Actual independent numerical results
Each number below comes from reimplementation of the source-defined mathematical generator, NOT original R application run or source-clinical prediction:

START CAG | YEARS | Pr[X>=150] if CTMC T2=55 | if CTMC T2=72.2
50 | 8 | .031710089078 | .000000125424
50 | 12 | .260163564810 | .000267970117
55 | 5 | .067177353511 | .000000002381
55 | 8 | .507464072325 | .0000581312214
55 | 12 | .823206832010 | .0117716135562
60 | 5 | .605399312431 | .000003881646
60 | 8 | .956645292191 | .004982922600.
These orders of magnitude are SOURCE-MOTIVATED model sensitivity, not a claim that 50% of real human neurons cross 150 repeats after eight years. The first alternative at T2=55 is a COUNTERFACTUAL in the recommended CTMC family; author event-sampling with T2=55 has different jump process and its predictions are NOT these numbers.

## At least three separate executed verification paths
1. Standalone Python stdlib Fraction script performs exact rates, local drift and second derivative at x55, and an independently coded Poisson UNIFORMIZATION of finite-state CTMC (x0=60, t=.5/1.0). Its computed probabilities match the separately implemented SciPy matrix exponential with max error 1.13e-12.
2. Separate script constructs sparse generator using NumPy and evaluates scipy.sparse.linalg.expm_multiply. Independently integrates forward Kolmogorov ODE with DOP853 at 4 settings. Maximum difference of individual state probabilities 5.30e-13.
3. Separate path in second script directly draws 7000 Gillespie event trajectories per chosen setting from the CTMC intensities. At x0=55,t=8,T2=55: 3571/7000=.510143 vs exact .507464, within .45 model binomial SE. At x0=55,t=12,T2=72.2: 81/7000=.011571 vs exact .011772. At x0=60,t=5,T2=55: 4222/7000=.603143 vs exact .605399.
4. Upper-bound convergence: at x0=55,t=8,12, two thresholds, varying cap 180/240/300/500 changes Pr[X>=150] by at most 6.81e-13. Mass conservation PASS.
5. Reproducibility: SciPy adaptive trace estimation can vary in 13th–15th numerical digits. Freeze computed FLOAT diagnostic JSON at 9 meaningful decimal digits, with residues <1e-11 canonically zero; core computations, internal checks and exact Fraction results are NOT approximated. Two scripts after CLEAN extracted ZIP produce 2 frozen JSON BYTE IDENTICAL. ZIP CRC PASS; all 7 scientific archive-member SHA256 PASS.

## Custody, original rights and scientific boundary

Moderator-local complete ZIP with full 10.4 KB Polish report, two ORIGINAL independently written runnable Python sources, two frozen JSON results, README, verify_replay.py, sha256 manifest:
IW_XH_S5_ROT019_HD_CAG_THRESHOLD_ABLATION_REPRO_20261102.zip
ZIP SHA256 00b1a5e87c2d91163a8d2ae372a06a4085b1d7bb28d4a666af95b443b1a5a774
Full local report SHA256 a64483d65ce1946b89b69030fc7ae5f47bbf14b936a5cea636bafde736d01942.
The author-owned R/Shiny source is NOT included in ZIP (reference only). Source code read/used for formula provenance, not executed/republished. The public GitHub artifact is detailed science, NOT the entire local ZIP/code, unless independently deposited and read back.

NARROW suggested real referee gate: when citing a specific treatment prediction from the authors, require the figure's EXACT engine name, commit, T2 threshold, mutation bias, transduction and knockdown, sample N/RNG, and data calibration. This mathematical ablation is insufficient to infer clinical benefit or model validation against observed progression. No task cascade and no external medical recommendations.

NO_NOVELTY / NO_SOURCE_R_REPLAY / NO_CLINICAL_EFFICACY_INFERENCE / NO_NASH_PHYSICAL / NO_CANON / NO_EXEC_SIGN / NO_BW_INGESTION_ASSUMED.