---
artifact_id: IW_DAX_S9_ROT009_DAI_PENNINGTON_MATURE_PRIOR_ART_ANGULAR_TV_SOURCE_GATE_001_20261121
date: 2026-11-21
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
class: MATURE_PARTIAL_WAVE_PRIOR_ART_RECONCILIATION / AUTHENTIC_SECONDARY_SOURCE_SIX_BIN_TOTAL_VARIATION_FALSIFIER
claim_ceiling: NO_DAI_FIT_COEFFICIENTS / NO_CAUSAL_MU_CONTAMINATION / NO_EXPERIMENTAL_COMPATIBILITY_CI / NO_NEUTRINO_TRANSPORT / NO_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX9 ROT009 — mature Dai–Pennington partial-wave literature meets source-authenticated Mark II–Belle angular distributions

**New work only within DAX9 source-testing lineage. Not a first discovery of the Belle anomaly or a new hadronic amplitude.** Following ROT008 the user approved a shift away from arbitrary scale sensitivity experiments toward source-native amplitudes and real hadronic interpretation.

## A. Original 2014 partial-wave analysis directly read

Ling-Yun Dai and M.R. Pennington, *Comprehensive Amplitude Analysis of gamma gamma -> pi+ pi-, pi0 pi0 and Kbar K below 1.5 GeV*, Phys. Rev. D90, 036004 (2014), DOI 10.1103/PhysRevD.90.036004; full original arXiv 1404.7524v2 text at https://misportal.jlab.org/sti/publications/12980/attachments/9416/1404.7524v2.pdf , Sections 2.5, 3.2, Table 2, Figures 6 and 15.

**Established prior art, explicitly NOT new DAX discovery:** Dai–Pennington find a Belle pi+pi- discrepancy in W=0.8–0.9 GeV, particularly an anomalous rise in angular distribution around |cos(theta*)|=.5, and suggest it **MAY** reflect imperfect separation from the much larger gamma gamma -> mu+mu- QED background. They do not prove experimental misidentification. Their fitted hadronic partial-wave amplitude lies below Belle results in that region, and they rely on pi0pi0 and KK hadronic coupled-channel data, unitarity, analytic and crossing constraints. The same paper notes a separate Belle W=1.2–1.25 GeV residual. They explicitly allow normalization shifts for MarkII ~7% and Belle charged ~5% common dominant; Solution I Table2 lists mean chi2/data 1.55 for MarkII charged and 2.85 for Belle charged **inside their own weighted multi-dataset fit**, not a new significance calculation or standalone comparable experimental p-value.

The authors' Eq(27) specifies coupling functions alpha_i^{I,J,lambda}(s)=exp(b s) sum_n a_n X^n and uses separate fitted hadronic T-matrices. This DAX turn **did not obtain original numeric coefficient vectors or full T-matrices**; the plotted Solution I is NOT a verified machine-readable model and is NOT evaluated as a physical amplitude here. Full original PDF bytes are not in runtime; web PDF text read, web screenshot retrieval attempted but cache miss. No faux author-source numeric amplitude fit.

## B. Exact authenticated SECONDARY source bytes and units

MarkII original secondary packaged Rivet source MARKII_1990_I304882.yoda.gz SHA256 **ff9a573f34b469ef76b145913506dfa20774243332772c1f7ba2c31b8422986d**, extracted and authenticated in previous DAX9 ROT007–008, with 60 MarkII angular cells 10 broad W bands ×6 0.1-wide |z| cells. MarkII values are **nb PER ANGULAR BIN**.

Belle official secondary packaged Rivet BELLE_2007_I749358.yoda.gz SHA256 **28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403**, previously retrieved in DAX8 ROT017 and paper-verified in DAX9 ROT001, has 140×12 native entries: **nb PER UNIT |z|**, each multiplied by .05 before aggregation. Both source bytes independently SHA-checked in present local executable. Neither primary HEPData native export nor covariance recovered.

For SIX exactly matched MarkII/Belle W bands 0.85–1.45GeV (each 100MeV wide), directly sum MarkII six observed angular-bin contributions and positive Planck-H(W) weighted Belle twenty 5MeV rows per W band, pair Belle adjacent .05 angular cells into each MarkII .1 cell, independently normalize to probabilities pM_j,pB_j. The R68 H(W) and constants E_gamma=1436554MeV,T=.07818527068831995MeV are unchanged. This is conditional published-binned-source weighting, NOT a full QCD physical rate or muon background model.

## C. New DAX9 6-cell shape diagnostics

TVD6=.5 sum_j |pB_j-pM_j|; Delta_high=sum_{j:|z|>=.4}(pB_j-pM_j).

| W band GeV | TVD6 source central | Belle-MarkII high-angle 0.4..0.6 mass, percentage points | Belle-MarkII 0.5..0.6 mass, pp |
|---|---:|---:|---:|
| .85–.95 | **0.10279315** | **+10.279315** | **+6.533967** |
| .95–1.05 | .03664141 | +2.931301 | +2.048975 |
| 1.05–1.15 | .03273372 | +0.314151 | -.387994 |
| 1.15–1.25 | .02575733 | -.918733 | +.371144 |
| 1.25–1.35 | .03209324 | -2.007237 | -.243047 |
| 1.35–1.45 | .07201826 | +6.495386 | +4.863328 |

At W=0.85–0.95 GeV, pM(|z|≥.4)=.2923976608, pB(|z|≥.4)=.3951908125. This empirically SOURCE-CENTRAL localizes much of the broad anomaly towards high |z|, consistent with the published qualitative Dai/Pennington observation. **BUT** W.85..95 only partially overlaps their W.8..9 suspicious range; differences also occur at W=1.35–1.45. No claim this identifies muon contamination or significance.

**Exact standard coarse-graining statement:** for any continuous source angle laws P,Q having these FIXED six observed-bin central masses, TV(P,Q)≥TVD6 by the data-processing inequality for partition maps. The lower bound is mathematically sharp when within-bin conditional densities are equal. This is a **central numbers condition**, NOT a bound with experimental uncertainties, acceptance migration, true energy unfolding or correlated nuisance allowed. It does not conflict with ROT008: sign of one source E[z²] difference remains unidentified under within-bin variation, even when six-bin central TV is positive.

## D. Original execution and negative knowledge

Original independent 42-digit mpmath W quadrature over source 5MeV Belle rows and independently written YODA parsers, all genuine compressed source hashes PASS, six normalized distributions PASS and original ROT008 W=0.85–0.95 source q2 consistency PASS. A first code control failed because coarse rebinning .05→.1 prematurely changed Belle q2; repaired to use original .05 bins for q2 and coarsen only for TV. NOT promoted original failed result.

Local complete reproduction bundle contains both actual authentic secondary source assets, original executable, frozen JSON and CSV, full detailed report, manifest and log. ZIP SHA256 aea0f551498a6db765a3461bbfe55c238d58029d1dfd9823076c789551e18338; ZIP CRC PASS, all 8 SHA256 member hashes PASS, clean-directory replay JSON+CSV byte-identical PASS.

**Open material issue:** SOURCE-NATIVE NUMERIC Dai–Pennington fitted partial wave grid/coefficients and hadronic T matrices absent; full physical angular amplitude not reexecuted, detector muon leakage not tested causally, true joint experimental covariance unknown, original MarkII W=0.40–0.54 GeV PID gap, outside angles and full pion medium transport remain OPEN. No direct neutrino/BBN/PBH significance and no novelty inference; no BW write or external I3.

**DISPOSITION: MATURE_PRIOR_ART_BELLE_MU_MISID_HYPOTHESIS_FOUND / TWO_NATIVE_SECONDARY_SHA_PASS / SIX_BAND_SOURCE_CENTRAL_TV_PASS / SHARP_CONDITIONAL_REFINEMENT_BOUND_PASS / CAUSAL_AND_PHYSICAL_TRANSFER_HOLD / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.**
