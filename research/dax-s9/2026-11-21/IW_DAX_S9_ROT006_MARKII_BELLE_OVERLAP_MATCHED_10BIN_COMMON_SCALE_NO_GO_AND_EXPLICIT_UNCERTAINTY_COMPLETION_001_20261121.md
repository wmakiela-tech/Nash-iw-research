---
artifact_id: IW_DAX_S9_ROT006_MARKII_BELLE_OVERLAP_MATCHED_10BIN_COMMON_SCALE_NO_GO_AND_EXPLICIT_UNCERTAINTY_COMPLETION_001_20261121
date: 2026-11-21
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
document_type: ORIGINAL_SCIENTIFIC_SOURCE_RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: ORIGINAL_EXACT_MATCHED_SOURCE_OVERLAP_10BIN_COMPARISON / COMMON_SCALE_CENTRAL_VALUES_MINIMAX_NO_GO / ARTIFICIAL_MARGINAL_ERROR_INTERVAL_JOINT_COMPLETION_WITNESS
claim_ceiling: NO_NATIVE_MARKII_HEPDATA_BYTES / NO_JOINT_MARKII_BELLE_COVARIANCE / NO_EXPERIMENTAL_COMPATIBILITY_OR_TENSION_TEST / NO_PHYSICAL_ALL_W_PION_CROSS_SECTION / NO_NEUTRINO_PBH_BBN / NO_NOVELTY_INFERENCE / NO_CANON / NO_EXEC_SIGN
---

# DAX-S9 ROT006 — Mark II vs Belle in 0.80–0.90 GeV: one-scale central-shape no-go and explicit nuisance-box reconciliation

**21 November 2026.** Bounded successor source analysis following DAX-S9 ROT005, not a new particle-physics theory, not an independent experimental reanalysis, and not a validated statistical hypothesis test. This turn asks whether the **84.153% integrated source-weight ratio** in the same W and fiducial angular support can be attributed to a single common normalization versus experimental shape/systematics. The decisive epistemic distinction is between **unequal central shapes** and **incompatible experiments**.

## A. Direct source context, exact provenance and negative knowledge

1. **Mark II primary authors**: J. Boyer et al, *Two-photon production of pion pairs*, Phys. Rev. D **42** (1990) 1350–1367, DOI https://doi.org/10.1103/PhysRevD.42.1350. DAX9 ROT005 transcribed Mark II author Table III's ten σ(W) fiducial values in W=0.800–0.900 GeV, 10 MeV centers 0.805,0.815,…,0.895 GeV, together with published statistical and systematic error scales. Its primary-author data at W<0.8GeV had 17 valid low-W bins and a true no-pion-identification gap W=0.400–0.540GeV. Direct bytes of original HEPData Mark II record https://www.hepdata.net/record/ins304882 (DOI 10.17182/hepdata.22881.v1) are still **NOT** retrieved; only metadata and original paper transcription.
2. **Belle primary authors**: T. Mori et al, JPSJ **76** (2007) 074102, arXiv https://arxiv.org/abs/0704.3538, Appendix B: DAX9 ROT001 independently checked all 140 published fiducial σ/stat triples exactly (at printed decimal precision) against authenticated SECONDARY official Rivet-data reference source YODA. DAX-S8 ROT017 acquired reference package via original public GitHub Actions 43309487872; genuine bundled `BELLE_2007_I749358.yoda.gz` compressed source SHA256 **28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403**. Here source bytes are READ AGAIN from the actual original DAX8 ZIP. YODA Table1 contains asymmetric `stat` and `sys` fields; latter are authentic SECONDARY reference errors, **not** proven equal to unmodified HEPData original export.
3. Source provenance retained: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/dax-s9/2026-11-21/IW_DAX_S9_ROT005_MARKII_AUTHOR_TABLE_III_17_LOW_W_MEASURED_BINS_R68_FIDUCIAL_KERNEL_AND_SOURCE_OVERLAP_GATE_001_20261121.md ; source firstness belongs to Boyer/Mori and DAX-S8 ROT017/DAX9 ROT001/ROT005, not ROT006.
4. **Mature prior art**: Dai and Pennington, *Comprehensive amplitude analysis of gamma gamma -> pion pairs and K bar K below 1.5 GeV*, Phys. Rev. D **90** (2014) 036004, DOI https://doi.org/10.1103/PhysRevD.90.036004: interplay of Mark II, Belle, Crystal Ball and hadronic amplitudes with limited angular acceptance requires careful fitting; no amplitude fit is newly executed here.

## B. Exactly matched source operator and data processing, not a free 5-MeV interpolation

Both experiments publish fiducial |cos(theta*)|<0.6, but Mark II bins are 10 MeV whereas Belle bins are 5 MeV. For each Mark II 10-MeV interval I_j=[800+10j,810+10j] MeV, Belle has two complete subintervals I_{j,1},I_{j,2}. Use the identical **inherited R68** fixed-Planck positive kernel H(W)=4W³/C²[-log(1−exp(−W²/C))] with C=4 E_gamma T, E_gamma=1,436,554 MeV and T=0.07818527068831995 MeV.

Let h_{jk}=∫_{I_{jk}}H(W)dW and α_{jk}=h_{jk}/(h_{j1}+h_{j2}). Define the common-bin Belle central b_j=α_{j1} b_{j1}+α_{j2} b_{j2} and original Mark II author central m_j. All j=1…10 were recomputed: 45-digit mpmath integration and separately implemented Gauss-Legendre-16 source integrals agree to <5e−13 relative on every common bin. This is conditional source bin-constant reconstruction as inherited; no claim of exact underlying continuous σ(W) or detector unfolding.

The same calculation reproduces ROT005 weighted overlap:
- K_MarkII(W800–900) = **5.59239307311557935e−11**;
- K_Belle(W800–900) = **6.64550319081277118e−11**;
- their ratio **0.841530417267260** = 84.1530%.
All are R68 source-convolution numbers, not a physical branching ratio, neutrino yield or statistical effect size.

## C. Exact central-shape common-normalization no-go

The 10 original central pairs have extrema:
- m_j/b_j **min 0.7223062679155069** at W=0.805 GeV;
- m_j/b_j **max 0.9683933099925599** at W=0.855 GeV.

Consequently there exists **no** single positive scalar k such that k m_j=b_j for ALL j: necessary pair ratios are not constant. A stronger *exact simple minimax* diagnostic, defined per-bin as D(k)=max_j |k m_j/b_j−1|, gives
  min_{k>0}D(k) = (r_max−r_min)/(r_max+r_min) = **0.145553382335105**,
  k_opt = 2/(r_min+r_max) = **1.182942272023653**.
The proof follows by equalizing the maximum two extremal residuals 1−k r_min and k r_max−1 for k in their straddling range; the interior ratios lie between them. It is a source-central-**shape** statement only and NOT a measurement disagreement magnitude or sigma.

Under the *separate deliberately constrained hypothetical* shared calibration k∈[0.93,1.07], using Mark II paper's approximately 7% shared normalization scale as though it were a strict hard interval, optimum is at k=1.07 and min D(k) = **0.227132293330408**. Mark II published shared 7% is **NOT** literally an experimental hard cap or a confidence interval; this is a sensitivity scenario only. Shared normalization alone cannot reproduce each printed source central value.

## D. Constructive non-tension completion in an ARTIFICIAL uncertainty-box class

For each Mark II 10-MeV bin j, define a **hypothetical symmetric additive envelope** e_Mj = sqrt(stat_Mj²+sys_Mj²), using original Mark II Table III per-bin printed errors and excluding the separately published approximate 7% common normalization. No assertion that all 10 error components can fluctuate independently with hard ±e bounds is made.

For each Belle paired 10-MeV bin, independently from official SECONDARY YODA:
- e_B,stat,j = sqrt[(α_1 stat_1)²+(α_2 stat_2)²], *if* the two published 5-MeV stat errors may be treated independent;
- e_B,sys,j = α_1 max(|sysDn_1|,|sysUp_1|)+α_2 max(|sysDn_2|,|sysUp_2|), deliberately **full-correlated within each 10-MeV pair** as a conservative marginal amplitude;
- e_Bj = sqrt(e_B,stat,j²+e_B,sys,j²).

These are *modelled per-bin envelope half-widths* derived from published **marginal error scales**. Their shape is NOT a validated simultaneous 10-bin likelihood or source covariance. For each j require the artificial intervals
   [k(m_j−e_Mj), k(m_j+e_Mj)]
and
   [b_j−e_Bj, b_j+e_Bj]
to intersect. Algebraically (provided m_j>e_Mj) this is equivalent to
   (b_j−e_Bj)/(m_j+e_Mj) ≤ k ≤ (b_j+e_Bj)/(m_j−e_Mj).
Taking the intersection for all 10 j, independent code from the original two tables and SHA-pinned YODA finds:
  **k ∈ [1.066810037359867, 1.268416320936021]**.

Intersecting further with the arbitrary common Mark II k∈[0.93,1.07] yields
  **[1.066810037359867, 1.07]** (NONEMPTY).
The executing script constructs a **real numerical witness** at k=1.07 for **10/10 bins**: each chosen target c_j belongs to both declared intervals. Original frozen `paired_overlap_rows.csv` records each source central/error, exact Planck-weighted Belle pair, feasible k band and actual chosen c_j.

**What this DOES establish:** There exists one joint reconciliation in a mathematically defined per-bin uncertainty-box COMPLETION, whose marginal scales are anchored to source-reported errors. Therefore the apparent ~16% integrated central difference **alone does not imply logical incompatibility** of the source records.

**What it emphatically DOES NOT establish:** that such a full 10-bin assignment is allowed by the actual Mark II/Belle correlation matrices, that k=1.07 is an experimentally acceptable confidence threshold, that both experiments are statistically consistent, or that any physical calibration error occurred. In particular, arbitrary independent directions for systematics from ten bins may violate their true shared-detector nuisance structure. One must NOT attach a p-value, 1σ joint coverage, 95% confidence, or independent-I3 designation to this constructive box witness.

Optional transparent diagonal *heuristic* ∑[(k m_j−b_j)/sqrt((k e_Mj)²+e_Bj²)]² is 13.0972 at k=1 and 6.9541 at k=1.07. As covariance/likelihood is missing, **these are just sums of squared scaled deviations, not χ²-distribution test statistics or p-values**.

## E. Reproduction and controls

The originating conversation's downloadable complete archive `DAX9_ROT006_MarkII_Belle_overlap_source_calibration_repro.zip` has original human-readable CSV input source transcripts, the actually SHA-verified original DAX8 official-secondary Belle YODA ZIP, original Python source `verify_overlap.py`, frozen `results_rot006.json`, per-pair witness `paired_overlap_rows.csv`, README and member SHA256 manifest. ZIP SHA256 **844a46b8eea41d6c40d14566084fe59cf1997bc5e6d79692b7afd834cee69f74**; ZIP CRC PASS, 7/7 SHA256 member digests PASS; fresh directory replay reproduced both CSV and JSON BYTE-IDENTICAL PASS. The bundle deliberately does NOT include original Mark II HEPData native export or journal PDF, which are still not held by the runtime. Authors' original source transcriptions, secondary package source and modelling assumptions are explicit.

## F. Boundary and decision

The legitimate next scientific discriminator is **actual joint W-bin covariance or source-native original Mark II/HEPData Table1 values** combined with a joint detector/normalization likelihood; possibly the mature Dai–Pennington amplitude fit in a fully source-native way. No additional variation of arbitrary same-source weights without new original source contact would be useful. The Mark II W400–540MeV particle-identification gap, below-350MeV and outside-fiducial angles remain a separate original **support incompleteness** problem even if the ten overlap bins were calibrated. No inferred W<800 daughter-event fraction η, no complete pion production, full in-medium transport, BBN/PBH or new particle physics.

Original predecessor DAX8 ROT028–031 BW read-only check via KN15 resolved narrowly (exact Git blobs verified and no matched ING in specified ranges); DAX has not performed or requested any unauthorized BW ingestion. All present report outputs are GitHub public artifact only and **not automatically BW ingested**, independently refereed, canonized or owner accepted.

**RETURN: MARKII_BELLE_OVERLAP_10BIN_SOURCE_MATCH_PASS / CENTRAL_SHAPE_GLOBAL_SCALE_NO_GO / EXACT_SUP_NORM_MINIMAX_PASS / MATHEMATICAL_PER_BIN_ERROR_BOX_RECONCILIATION_EXISTS / NO_VALIDATED_EXPERIMENTAL_COMPATIBILITY_OR_TENSION_CLAIM / NO_PRIMARY_MARKII_HEPDATA_BYTES / NO_FULL_QCD_OR_NEUTRINO_PHYSICS / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.**
