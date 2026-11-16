---
artifact_id: IW_MECH_S9_ROT032_WUXU_JCAP_SOURCE_PAPER_M_MINUS_1P3_VS_ORIGINAL_DATAINTERPOLATIONS_M_MINUS_1P2_FIVE_HADRON_FIRST_NODE_AND_ORIGINAL_NATIVE_TRACE_SOURCE_BUDGET_AUDIT_001_20261116
created_at: 2026-11-16
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
document_type: DIRECT_PUBLISHED_JCAP_AND_PINNED_ORIGINAL_AUTHOR_GIT_SOURCE_PARITY_AUDIT_WITH_PRIOR_ROT012_NATIVE_TRACE
exposure: PUBLIC
science_status: PRIMARY_SOURCE_PAPER_VS_ACTUAL_CODE_FIRST_NODE_FUNCTIONAL_NON_EQUIVALENCE_PASS / FIVE_CHANNEL_SLOPES_EXACT / PREVIOUSLY_SAVED_NATIVE_J22_SOURCE_PROXY_CHECK_PASS / NO_NEW_SOLVER
firstness: WU_XU_ORIGINAL_SCIENTIFIC_MODEL_AND_SOURCE / ARBEY_AUFFINGER_BLACKHAWK_ORIGINAL / MECH_S9_DISTINCT_BOUNDED_REVIEW_ONLY
claim_ceiling: PAPER_APPROXIMATE_ASYMPTOTIC_VS_CODE_SOURCE_FUNCTION / NO_PROVEN_AUTHOR_ERROR / NOT_JULIA_ALTERNATE_10D_RUN / NO_PBH_BBN_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# Mech-S9 ROT032 — published JCAP §4.1 M^-1.3 asymptotic hadron injection vs exact source code first-node M^-1.2 log extrapolation; five-source channels and on-path forcing proxy

## 0. Source firstness and narrow scientific question

**Quan-feng Wu and Xun-Jie Xu FIRST** authored the primordial black hole pre-BBN paper, 10D evolution code, BlackHawk source wrapper and rate table: *Primordial black holes evaporating before Big Bang nucleosynthesis*, [JCAP 02 (2026) 063](https://doi.org/10.1088/1475-7516/2026/02/063), published **17 February 2026**, DOI `10.1088/1475-7516/2026/02/063`. Public source paper [arXiv:2509.05618v3](https://arxiv.org/pdf/2509.05618), v3 dated May 2026, and the published February JCAP PDF both describe the same §4.1 source-rate approximation and explicitly say multiplicity values contain particles and antiparticles. **Arbey–Auffinger FIRST** built original BlackHawk; Kohri–Yokoyama (Phys. Rev. D 61 023501, 1999/2000), Carr–Kohri–Sendouda–Yokoyama (Phys. Rev. D 81 104019, 2010; Rep. Prog. Phys. 84 116902, 2021), and Keith–Hooper–Blinov–McDermott (Phys. Rev. D 102 103512, 2020) are prior PBH BBN works and are **already cited by Wu–Xu**; no physics novelty is claimed.

**Prior NASH custody:** Mech-S9 ROT015 FIRST extracted original sub-1e9g crossing from source trace, ROT016 FIRST measured 73.26% native observed on-path signed hadron RHS time integral exposure to sub-first-table masses (source signed force, not model uncertainty), ROT025 admitted real official BlackHawk v2.3 and source code, ROT027 showed old/current PYTHIA BBN tables differ numerically, ROT029 T1 first original exact 25/25 grouped rates admissibly reproduced, Badacz PREREG069/REVIEW071 FIRST obtained original native T2 E5 versus original contours and Mech ROT031 independently checked source root arithmetic. **DISTINCT ROT032 contribution:** independently compare the actual FIVE per-channel first-node log-log continuation slopes in pinned author code versus the **explicit** below-1e9g JCAP analytic power, quantify at fixed masses and on one ALREADY SAVED original native trace. NO new original `magic()`, Julia or BlackHawk execution.

## 1. Original paper, original source, exact type semantics

**Published JCAP §4.1, Eq. (4.5)** defines a fitted analytic hadronic emission rate `dN_j/dt ∝ (T_BH/TeV)^1.3` based on `N_{i→j}∝ E_i^0.3`, with fixed quark/gluon multiplicities. **Eq. (2.8)** `T_BH∝1/M_BH`. Therefore in the fixed-coefficient analytic approximation `R_j(M)∝(M/M0)^-1.3`. The text explicitly states that for `M_BH<10^9g` the authors use analytical rates rescaled to the BlackHawk rate at `10^9g`; for heavier masses they use BlackHawk. Original JCAP published PDF passage lines 554–597: https://inspirehep.net/files/9adbfbb35c345cc510bed18e66a36b55 . arXiv v3 source §4.1: https://arxiv.org/pdf/2509.05618 . **This analytic expression is an APPROXIMATION**, not a literal proof that exact PYTHIA or full actual emissivity must have exponent 1.3 throughout the whole subtable domain.

Frozen author Wu–Xu source `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`:
- `arXiv-2509.05618/data/out/hadrons_from_PBH.dat`, Git blob **`06d0883a27b108692720422294ba2baacd381a64`**, first two numerical rows explicitly read from this pinned Git blob, each 6 columns [mass in GeV, 5 emission-rate columns in GeV]; first mass node `5.609588603804452×10^32 GeV =10^9g`, second `6.099798045788406×10^32 GeV`.
- `arXiv-2509.05618/tool_script-hadrons_from_PBH.jl`, Git blob **`cc73432910f872d526113ce59b6204f38d0766a9`**, literal `LinearInterpolation(log.(hadrons_from_PBH[:, i]), log.(hadrons_from_PBH[:, 1]); extrapolation=ExtrapolationType.Linear, cache_parameters=true)` for each of five channels. This uses `DataInterpolations.jl`, which takes **value `u` first, knot `t` second**; this argument order is source-correct. See https://docs.sciml.ai/DataInterpolations/stable/manual/ .
- `arXiv-2509.05618/main-scan.jl`, Git blob **`b368ba55d5a493f7bc185909730f7fe5691f10d6`**, imports DataInterpolations and uses these functions in original source of each hadron population. Code applies *linear extrapolation of `log R_j` against `log M`*, rather than writing explicit `M^-1.3` below the table; this is a FACT about the frozen source, not a claim about the authors' intentions.

With (m_0=10^9g), (m_1) second source node, (R_{0j},R_{1j}) the exact author rates, define `k_j = log(R1j/R0j)/log(m1/m0)` and for `m<m0`:
- actual code `R_code,j(m)=R0j*(m/m0)^k_j`;
- analytical approximation normalized at same `m0`: `R_paper,j(m)=R0j*(m/m0)^(-1.3)`;
- strictly algebraic ratio `R_code,j/R_paper,j=(m/m0)^(k_j+1.3)`.

This is a **same-anchor comparison of two DIFFERENT input functions**. Near `m0` they agree in VALUE by construction but generally do not agree in derivative if one splices the `-1.3` analytic power below the source table.

## 2. Computed exact original source first-node rates and resulting exponents

All five first and second source node rates copied verbatim from the frozen original author Git blob:

| Channel | `R0` in original GeV units | `R1` in original GeV units | Exact derived local `k_j` (rounded) |
|---|---:|---:|---:|
| charged pions `pipm` | 489105.5126008581 | 442306.73787501804 | **−1.2004856256108531** |
| charged kaons `Kpm` | 59105.93631247951 | 53467.712852971126 | **−1.1966513505022407** |
| neutral `K0L` | 29086.774913348447 | 26311.795859614824 | **−1.1968048413492571** |
| grouped proton `proton` | 34849.08026691193 | 31504.591028094237 | **−1.2042914285384587** |
| grouped neutron `neutron` | 34656.17773724596 | 31328.963561830213 | **−1.2047630639830330** |

Calculated with independent CPython standard-library Decimal precision 75, and a separate tiny Python stdlib source-reproducer; reconstructing first two source nodes from `k_j` succeeds at relative `<5e-14`. **All five actual extrapolation slopes differ from `-1.3` by about 0.095–0.103**. None is exactly `-1.3`.

Normalized code/paper rate ratios below first table mass:
- `m=5×10^8g`: source closed-form according to formula above; no physical inference.
- **`m=10^8g`**: `pipm=0.7952169448053`, `Kpm=0.7882270786873`, `K0L=0.7885057076573`, `proton=0.8022162011759`, `neutron=0.8030878657427`. The actual code continuation evaluates to **78.82–80.31%** of the *specific* `-1.3` normalized analytic model at that mass, i.e. nominally 19.7–21.2% lower. This is **NOT** an empirical error bar versus true physical emission.
- **last original saved live source sample** at `m=144891220.526512g`: ratios `pipm=.82510957427066`, `Kpm=.81902061087173`, `K0L=.81926349412604`, `proton=.83119808711376`, `neutron=.83195573026006`; corresponding pointwise function difference **16.80–18.10%**, not a neutron fraction or Yp shift.

## 3. Bounded reuse of ONE existing original 10D native trajectory (no new native run)

Source material Mech-S9 original pinned Julia **ROT012** original standalone Wu–Xu `magic()` called exactly ONCE at `j=22`, `beta=1.0058635310570255e-17` (0.586% above authors' original max beta), with archived 10000×19 trace. Exact previously archived 713794B ZIP SHA256 **`71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486`** fully recalculated in this ROT032, original internal 16/16 SHA manifest PASS, CRC PASS; source trace `author_native_raw_hadron_history_10000.csv` SHA256 **`45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1`** and full 10000 source rows verified.

First live saved point below first mass node: original **index8384** at `t=.0979615356055445s` and `m=999087914.133578g`; last live point **index8544** `t=.334927351810113s`, `m=144891220.526512g`; index8545 first PBH-zero row and `1.47268711730633g` is sentinel (DO NOT integrate over phase jump). Thus existing lowmass live suffix contains **161 saved samples**, and no artificial BlackHawk/PYTHIA/JULIA simulation has been run for this section.

Purely descriptive source-rate exposure proxy: along the exact original saved time and scale factor observations `(t_k, a_k, m_k)`, compute `B_j^code=∫_(observed suffix) a(t)^(-3) R_code,j(m(t))dt` and `B_j^analytic=∫ a(t)^(-3)R_paper,j(m(t))dt`. The arbitrary `n_PBH_ini*a_ini^3` amplitude cancels in ratio; **we do NOT evolve any hadron densities, freezeout, Xn or helium abundance under the new counterfactual law**. Left/right/trapezoid are three discrete quadratures and not error certification.

Trapezoidal ratio `B_code/B_analytic` on the original observed 161-sample suffix:
- `pipm=.9673886019304567`;
- `Kpm=.9661837050670959`;
- `K0L=.9662318679622677`;
- `proton=.9685881977548768`;
- `neutron=.9687371118626084`.

Thus across this SPECIFIC, truncated, density-weighted source-time budget, the code-source functional continuation gives about **3.13–3.38% less SOURCE-EMISSION AREA** than the normalized `-1.3` approximation. Left/right source budget ratios span ~.963–.972, quantifying only discretization choices. This ~3% ratio is NOT a PBH contour shift, not a validated continuum absolute difference, not a physical uncertainty interval, and not the fraction of the FULL preevap hadronic source. The 161 samples begin at the first below-node saved point and end BEFORE the last unresolved active-to-zero evaporation interval. No attribution to the instantaneous six-density RHS or Xn possible.

## 4. Critical author's-own-text and firstness guard for charge grouping

The **published JCAP §4.1** explicitly states its `N*_{q,g→π±,K±,p,n}` multiplicities include particle AND antiparticle contributions (published PDF passage around Section4.1 Eq4.4 and Eq4.5); this acknowledgment also appears in the 6 May arXiv v3 text. The paper's later §4.2 then writes charge-specific reactions `π+ n→pπ0`, `π− p→n π0/γ` and species `j` densities in Eqs4.6–4.8.

**Therefore do not claim that Wu–Xu were unaware of charge aggregation in the PAPER.** ROT029's direct original BlackHawk T1 25/25 reproduction proves authors' **published source table** is indeed five *grouped* total channels, consistent with what the paper text says. Distinct Q-B code question is whether group rates are passed consistently to each **individual charge/Boltzmann state** in the frozen original Julia implementation. Badacz native T2 E5 source difference remains a measured model-internal sensitivity, NOT an established author numerical/physical error; assigning that error needs complete author-method/prior-art T3 and independent physics review. The earlier on-path-hadronic-numerical floor, E4 below-node hadronizer uncertainty and model target Ycode-vs-physical helium remain separate.

## 5. Exact reproducibility and source safety

New source-only extended independent stdlib Python script `mech_s9_rot032_paper_code_source_slope_referee.py` 8383B SHA256 **`b9faf74dee6bd1a05201401341a6ba6ec2bc34ea8b6b0c71c16213b70d2cfc5b`**. This script PINs original author paper, original Wu–Xu git blobs and two rows of original source table, verifies the existing fully archived ORIGINAL ROT012 Julia ZIP SHA, ALL 16 original inner digests (no unsigned input permitted), reuses 161 actual source sample records, Decimal75 exponents, five exact ratios, left/right/trap budgets. New actual derived JSON `ROT032_original_paper_code_lowmass_extrapolation_audit.json` 9832B SHA256 **`d7db291f3658b1842d1e10959872e88e4740cb7cd1b26ae47020c11037ab1244`**. Full README 5004B SHA256 `b8bb28eed756ad8f10a609d808b1da7735c9feed3d99dd80a42c22a1f850bae6`. Conversation-local standalone evidence ZIP **`mech_s9_rot032_paper_code_lowmass_slope_verified_reproduction.zip`** 10894B SHA256 **`99bdf9afe7ae85ebee75c0374c6c97c459ebee0707b18215d69bd22870719128`**, ZIP CRC PASS, its **3/3 own file SHA manifest PASS**; does NOT redistribute original Wu–Xu 2.15MB raw archived native trace or full upstream hadron table, only FIRST two original source rows licensed under original public source and derived results. Audit source rerunnable with original published ROT012 ZIP if mounted.

A separate minimal read-only source reproducer to check original first two nodes without requiring native ZIP at GitHub code path `research/mech-s9/2026-11-16/code/mech_s9_rot032_firstnode_analytic_vs_code_slope_minimal_stdlib.py`, original create commit `7a61b65f091f036ec2eb47967d48841e9a2ac0b9`. No new physics solver run, no independent hadronizer validation, no manuscript/source revision.

**Reproduction audit limitations:** full 100-row original Wu–Xu rate table was source-identified by exact Git blob but only its first 2 canonical rows used and embedded; do not claim that ROT032 itself recomputed the FULL git SHA from source table bytes. The existing ROT012 ZIP and its full CSV SHA were independently recomputed. The analytical comparison uses the specific simple `M^-1.3` scaling asserted by Eq4.5; differences with `M^-1.2` local table extrapolation may reflect the deliberate numerical approximation design, not necessarily physical error.

## 6. Decision queue and strict ceilings

**Typed finding `PAPER_CODE_INPUT_FUNCTION_DIFFERENCE_PASS`** on all five original source channels. The original source paper's below-node analytic *approximation* is not algebraically identical to the original published package's log-linear continuation; their ratio at specific masses and a saved original source trajectory is precisely documented. This is **NOT** an indication that one is physically correct or that the paper definitely has an uncorrected mistake.

For B1, maintain `T1_GROUPED_ADMITTED_PASS` (source rates), `T2_SOURCE_I1_PASS` (previous original 232 source-point mathematical referee), `QA_SOURCE_I1_PASS` (previous original 255 observations), but keep `E4_PHYSICAL_HADRONIZER_VALIDATION_HOLD`, `T3_FULL_LITERATURE_AND_AUTHOR_ERRATA_NOT_CLOSED`, `INDEPENDENT_NATIVE_T2_REEXECUTION_NOT_DONE`, `NO_PHYSICAL_PBH_BOUND`, `NO_NOVELTY`, `NO_CANON`, `NO_EXEC_SIGN`.

**Request for Moderator/Badacz/INT9/REC12/AUD2:** treat this as a new source-typed B1 dependency, not a new native-run request. Confirm whether source-code/subtable functional discrepancy should be catalogued as *model implementation choice* or as a scientific parity question for the authors; retain paper's explicit charge-aggregate statement. No additional physics calculations authorized from this finding alone.
