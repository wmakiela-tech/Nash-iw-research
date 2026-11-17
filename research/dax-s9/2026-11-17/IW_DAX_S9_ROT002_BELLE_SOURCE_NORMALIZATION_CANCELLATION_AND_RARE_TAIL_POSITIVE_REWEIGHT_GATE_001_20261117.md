---
artifact_id: IW_DAX_S9_ROT002_BELLE_SOURCE_NORMALIZATION_CANCELLATION_AND_RARE_TAIL_POSITIVE_REWEIGHT_GATE_001_20261117
date: 2026-11-17
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: ORIGINAL_SUCCESSOR_EXACT_POSITIVE_RATIO_REWEIGHT_THEOREM / AUTHOR_PAPER_W_STAT_ENVELOPE / CONDITIONAL_NEUTRINO_E2_TAIL_FALSIFIER
source_class: DAX_S9_ROT001_PAPER_140_ROW_PUBLICATION_PRECISION + DAX_S8_ROT030_031_CONDITIONAL_CSDA_NUMBERS
claim_ceiling: NO_PRIMARY_HEPDATA_BYTES / NO_SOURCE_COVARIANCE / NO_BELLE_CONFIDENCE_INTERVAL / NO_FULL_PION_MEDIUM_TRANSPORT / NO_EXPERIMENTAL_NEUTRINO_FLUX / NO_PBH_BBN / NO_NOVELTY_INFERENCE / NO_CANON / NO_EXEC_SIGN
---

# DAX9 ROT002 — Positive source-shape reweighting: rare-neutrino E2 tail persists, but +10% uplift is less robust

Date: 17 November 2026. This is a narrowly bounded mathematical follow-up of **DAX-S9 ROT001** and predecessor **DAX-S8 ROT030/031**. It is NOT independent reproduction of DAX8's CSDA transport, nor a new Belle experiment. Preserve source firstness, all predecessor negative knowledge and scope.

## 1. Exact source and precedence

- Original Belle authors' publication: T. Mori et al. (2007), JPSJ 76, 074102, arXiv:0704.3538, Appendix B; https://arxiv.org/abs/0704.3538 ; original HEPData record https://www.hepdata.net/record/ins749358 .
- DAX9 ROT001 already compared **140/140** original published (W, fiducial sigma, stat) triples to the original SHA-pinned official SECONDARY packaged Rivet YODA (SHA256 28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403), and reexecuted the ROT017 conditional K_fid. That result remains the first DAX9 source-contact reconciliation, not an original discovery of Belle data.
- https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/dax-s9/2026-11-17/IW_DAX_S9_ROT001_BELLE_AUTHOR_PAPER_140X_RIVET_SOURCE_IDENTITY_FIDUCIAL_REPRO_001_20261117.md
- Predecessor original model inputs: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/dax-s8/2026-11-16/IW_DAX_S8_ROT030_REAL_BELLE_SOURCE_CONDITIONAL_FIRST_NEUTRINO_ENERGY_TAIL_AND_MOMENTS_001_20261116.md and https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/dax-s8/2026-11-16/IW_DAX_S8_ROT031_BELLE_ANGULAR_BIN_SUPPORT_RARE_NEUTRINO_TAIL_ROBUSTNESS_001_20261116.md .
- DAX9 ROT001 direct original paper source reading identified Belle systematic component ranges tracking 2.4%, trigger 4–10%, muon separation 0–1%, pion separation 5–7%, two-photon luminosity 5%, integrated luminosity 1.4% and total reported systematic 11.1–12.3%. These **are not** a measured full 140 x 12 covariance matrix or bounds on every angular data cell.

## 2. Exact mathematical result, with assumptions

Given *fixed nonnegative conditional observable responses* in source cells indexed i, let d_i >= n_i >= 0 be the contribution of cell i to the raw daughter second moment and to the same second moment restricted to a neutrino energy tail. Original source cell weights are w_i>=0. Then q = sum(w_i n_i)/sum(w_i d_i), for a positive denominator.

Suppose the ONLY source alteration is w'_i = a_i w_i, for all i, with pointwise multipliers **1-eps <= a_i <= 1+eps**, 0<=eps<1; pion stopping/decay kernels d_i, n_i and support remain fixed. With A=sum w_i n_i and B=sum w_i(d_i-n_i), monotone nonnegativity gives:

A' >= (1-eps)A, A' <= (1+eps)A;
B' >= (1-eps)B, B' <= (1+eps)B.

Consequently the following **rigorous universal but generally not sharp** envelope holds, regardless of correlations among the a_i:

q_low = (1-eps)*q / [(1-eps)*q + (1+eps)*(1-q)]
<= q' <=
q_high = (1+eps)*q / [(1+eps)*q + (1-eps)*(1-q)].

The same envelope applies to an EVENT TAIL PROBABILITY p = P(E_nu>t) if the per-cell conditional event probabilities lie in [0,1]. The ratio upper/lower may not be simultaneously attainable because each physical W,z bin contributes jointly to tail and non-tail; these are *guaranteed outer envelopes*, NOT exact profile likelihood or experimental confidence bounds.

**Common-mode normalization cancels exactly**: for a_i identically k>0, q'=q, all normalized source-tail probabilities unchanged and source-averaged E2 unchanged, while the unnormalized cross-section kernel K_fid scales by k. Thus a common 5% luminosity normalization uncertainty alone DOES NOT perturb the conditional normalized-neutrino observables in this fixed-model normalization.

For any fixed nonnegative source conditional observable g_i, its normalized mean m'=sum a_i w_i g_i / sum a_i w_i has the general envelope [(1-eps)/(1+eps)]m <= m' <= [(1+eps)/(1-eps)]m. This coarse mean envelope need not be optimal for a particular known source.

## 3. Source-derived inputs and actually executed arithmetic

DAX8 ROT031 assessed z-left, uniform and z-right placements. The smallest observed E2 share above 10GeV is **97.9147%** (left), and above 100GeV **76.184%** (left); uniform cases approximately 97.9384% and 76.569%. These are conditional to DAX8's specific source-restricted pion hard-Q2 vacuum point-scalar pi-e CSDA + two-body decay.

From original author-paper **W-INTEGRATED** table at published precision, independently transcribed and checked in DAX9 ROT001, maximal across 140 W-bin **statistical error / central** = **0.83/25.07 = 0.033107299561228556** at W=1.4975GeV. This DOES NOT identify maximum error for all 140×12 ANGULAR source cells or a simultaneous ±1sigma box; applying it to every required source cell below is an intentionally hypothetical bounded test.

The paper's 11.1–12.3% reported total-systematic *scale* is used in a second deliberately adversarial scenario **ASSUMING** all source cells have positive multiplicative reweightings within ±12.3%. This assumption is NOT what the Belle paper measured about source-wide joint angular/energy correlations. It is NOT a simultaneous experimental confidence band.

| Assumed per-cell cap eps | Conservative q>10GeV E2 share (z-left model) | Conservative q>100GeV E2 share (z-left model) | Baseline E2=13.4071611702GeV^2 coarse normalized-mean envelope |
| --- | --- | --- | --- |
| eps=0 (original DAX8 z-left q only) | 97.9147% | 76.184% | 13.4071611702 (ROT030 uniform baseline, different scenario) |
| eps=0.03310729956 hypothetical applied across all cells | >=**97.7750721%** | >=**74.9614067%** | [**12.54786049**, **14.32530835**] GeV^2 |
| eps=0.123 hypothetical applied across all cells | >=**97.3452979%** | >=**71.4132863%** | [**10.47024074**, **17.16789281**] GeV^2 |

For fixed full nonheadon ROT030 uniform q10~0.979384, at eps=.123 the bounded range is [0.973752959, 0.983827022]; P(E_nu>10GeV) baseline ~.001887016 would be in [~.001474263,~.002415049] **under this exact artificial positive-weight model**.

**Sharp conceptual distinction:**
- Conditional qualitative **rare-tail E2 dominance** is strongly robust under such uniform *upper caps* on all admitted source-cell multipliers. For conservative z-left q10=.979147, even eps as high as .423847 is sufficient for q10'>=.95 by the derived inequality; this is NOT a Belle experimental uncertainty number.
- Conditional **source-wide E2 uplift over mean-initial-energy approximation** is weaker. DAX8 ROT030 baseline source E2=13.4071611702 GeV^2 versus fixed mean-initial-E comparator 12.1835701169 GeV^2 (~+10.043%). By the coarse mean envelope, positive uplift is SUFFICIENTLY guaranteed only if eps < **0.04781383695** (4.7814%). Thus at the hypothetical eps=3.31073% level its positive sign is certified relative to the **held-fixed** comparator (minimal E2 12.54786049 >12.18357012), but at eps=12.3% THIS BOUND CANNOT CERTIFY the positive sign. This is absence of proof, NOT evidence for actual sign reversal. If source-dependent comparator changes under reweighting, recompute comparator too before a physical comparison.
- Common normalization-only nuisance cancels exactly in *both* normalized model observables and cannot by itself turn +10% into a sign reversal. Source **shape** or **physics kernel** changes are different.

## 4. Reproduction, limitations and backlog gate

Actually executed Python standard-library code in DAX9 originating runtime reads the 140 original author-published triples from DAX9 ROT001, verifies max stat ratio=0.83/25.07 (W=1.4975), rederives exact ratios and conservative absolute bounds for both tails and source E2, and tests common-mode cancellation. The replay produced frozen JSON and CSV-provenance reproduction, full ZIP CRC PASS. This is an elementary independent analytic bound, not replay of full original DAX8 CSDA nor an external referee. Source transcription at *publication decimal precision*; paper full HTML bytes were not SHA locked. The source table is not a native original HEPData export.

**NO EXPERIMENTAL CI, NO FULL PHYSICAL SOURCE SUPPORT:** a real W/z correlated covariance or detector acceptance response may not obey an assumed uniform cell multiplier cap; omitted production outside Belle restricted fiducial range, complete pion plasma stopping (soft+hard finite-T and hadronic), secondary muon/neutrino physics or nonlinear changes in the conditional response kernels can change everything. This result does not cover those changes.

**BACKLOG:** Earlier DAX9 posted read-only BW receipt request for predecessor ROT028–031 to current KN successor; latest bounded Slack parent thread read found NO THREAD REPLY. No duplicate request or BW write. Direct native HEPData export remains ACCESS_HOLD. No action to commandeer B1/B2 or source owner.

**RETURN: POSITIVE_REWEIGHT_UNIVERSAL_RATIO_ENVELOPE_PASS / COMMON_NORMALIZATION_EXACT_CANCELLATION_PASS / CONDITIONAL_TAIL_E2_DOMINANCE_BOUNDED_ROBUST / TEN_PERCENT_UPLIFT_IN_WIDE_SOURCE_SHAPE_BOX_NOT_CERTIFIED / ORIGINAL_SOURCE_COVARIANCE_MISSING / NO_EXPERIMENTAL_CI / NO_PHYSICAL_UPGRADE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.**
