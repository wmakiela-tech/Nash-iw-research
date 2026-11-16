---
artifact_id: IW_DAX_S9_ROT001_BELLE_AUTHOR_PAPER_140X_RIVET_SOURCE_IDENTITY_FIDUCIAL_REPRO_001_20261117
date: 2026-11-17
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: PRIMARY_AUTHOR_PAPER_NUMERIC_SOURCE_CONTACT / EXACT_PUBLISHED_140ROW_CENTRAL_STAT_SECONDARY_RIVET_IDENTITY / CONDITIONAL_R68_FIDUCIAL_QUADRATURE_REPRO
claim_ceiling: NO_PRIMARY_HEPDATA_EXPORT_BYTE_IDENTITY / NO_FULL_COVARIANCE / NO_EXPERIMENTAL_NEUTRINO_CI / NO_COMPLETE_PION_TRANSPORT / NO_BBN_PBH / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX-S9 ROT001 — original published Belle 140 W-bin numbers vs actual Rivet-data packaged source

**17 November 2026.** A strictly source/provenance-specific SUCCESSOR audit, inheriting DAX-S8 ROT015, ROT017, ROT018, ROT030 and ROT031. No firstness claimed for Belle measurements, source data acquisition or the QED calculations of prior DAX8; this result closes a narrower original-author-publication semantic and quantitative comparison gate.

## Sources

1. Original T. Mori et al. (Belle Collaboration), *High statistics measurement of the cross sections of gamma gamma -> pi+ pi- production*, J. Phys. Soc. Jpn. 76 (2007) 074102; arXiv:0704.3538, https://arxiv.org/abs/0704.3538 ; original author paper rendered at https://ar5iv.labs.arxiv.org/html/0704.3538 . §V, §VI.1, §VI.2 and **Appendix B** directly read.
2. Original HEPData record metadata https://www.hepdata.net/record/ins749358 (DOI 10.17182/hepdata.51842.v1); native numerical CSV/YAML/YODA **not** read in this DAX9 turn.
3. Rivet validated analysis https://www.heprivet.org/analyses/BELLE_2007_I749358/ . DAX-S8 source-native original GitHub Actions run https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43309487872 , artifact ID 13985880814 downloaded afresh by DAX9. Artifact ZIP published SHA256 666655df8b8534e45a4ca64bc91d4ad09b6f8a15336a4ca5b0c4200efeb8275c. Extracted BELLE_2007_I749358.yoda.gz compressed 29,215 bytes, independently measured SHA256 **28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403**; YODA V3 141 objects, first one source 140 W and asymmetric stat/sys columns.

## Actually executed new source check

The original author paper §V and §VI.1 state W measurement/efficiency bins of **5 MeV** and |cos(theta*)| bins of **0.05**; §VI.2 integrates differential cross section over |cos(theta*)| up to **0.6**. Its **Appendix B actually publishes fiducial total sigma(W) numbers for ALL 140 W positions** from 0.8025 to 1.4975 GeV. The paper has those total values throughout the higher-W region even though the original HEPData data abstract distinguishes low-W total-and-differential versus high-W differential submissions. Thus paper content, not inference from a secondary Rivet W-axis, establishes author-publication high-W total coverage.

DAX-S9 independently transcribed 140 original Appendix B published triples (W, sigma_fid, stat), decoded the exact downloaded YODA source /REF/BELLE_2007_I749358/d01-x01-y01, matched W, sigma and |stat_down| as exact decimals at two-digit nb publication precision. **140/140 exact matches, zero disagreements.** Five anchors:
- (0.8025 GeV, 109.74 nb, 2.77 nb stat)
- (1.1475 GeV, 185.23 nb, 1.15 nb stat)
- (1.1525 GeV, 190.32 nb, 1.15 nb stat)
- (1.2475 GeV, 308.21 nb, 1.24 nb stat)
- (1.4975 GeV, 25.07 nb, 0.83 nb stat)

This is **identity at original-publication decimal precision**, not raw HEPData byte-for-byte identity, error covariance confirmation, or source statistics independent of Belle.

## Independent source-matched R68 fiducial kernel replay

Under ONLY the inherited DAX-S8 ROT017 fixed isotropic Planck benchmark E_gamma=1436554 MeV, T=0.07818527068831995 MeV, C=4E_gamma T, H(W)=4W^3/C^2[-log(1-exp(-W²/C))] per LINEAR dW, 1 MeV^-2 = 389379371937.8198416 nb, and a **conditional** within-5MeV-bin constant cross section equal to the author-published value, the independently implemented 35-digit mpmath quadrature on author-paper Appendix B numbers gives

K_fid = sum_(i=0..139) sigma_i / nb_per_MeV2 * integral_[800+5i,805+5i] H(W)dW
= **3.88686466991478366418838582e-10**.

This matches predecessor ROT017 K_fid=3.8868646699147836641883858195704408e-10 to within 6.31e−36 relative under numerical working precision. This is **independent numerical verification of existing conditional computation**, NOT a new full charged-pion cross section, initial-muon physical probability, neutrino flux or PBH/BBN result. The primary paper explicitly uses finite W,z histogram bins, materially strengthens the previous conditional bin-origin premise; exact physical continuous σ(W) bin-average, resolution/migration handling and associated energy covariance still require separate modeling.

## Original paper systematics and conditional nuisance test

Original paper §VI.2 Table 1 lists tracking 2.4%, trigger 4–10%, muon separation 0–1%, pion separation 5–7%, two-photon luminosity function 5%, integrated luminosity 1.4%, total systematic 11.1–12.3%. It does **not** provide an identified full W-bin covariance matrix.

One explicit source-informed example, **NOT an unconditional uncertainty statement**: if both 5% and 1.4% quantities act as independent common multiplicative normalization nuisances across all W, and other nuisance variables are independent of them, the contribution to K_fid relative standard deviation is sqrt(0.05²+0.014²) = **5.1923%**. The completely arbitrary PSD covariance lower endpoint zero in DAX-S8 ROT018 need not remain physically admissible after specifying these shared nuisances, but there is no validated model of all cross-W correlations and no measured K-fid CI. Do not treat 5.1923% as a Belle experiment-derived uncertainty floor without its extra assumptions.

## Falsified transfer, retained limits and stop

FALSIFIED in author-published scope: "Rivet 140 high-W total values might have no original author paper counterpart." Actual Belle Appendix B supplies all of them and 140/140 central/stat agree.

STILL NOT PROVEN: actual original HEPData submission Table1 contains same 140 entries; exact original HEPData numerical bytes; joint stat/sys covariance or acceptance corrections; off-fiducial W/z production, genuine in-medium pion energy loss; any real neutrino-tail experimental confidence interval or firstness; full cosmological PBH/BBN transport. DAX-S8 ROT030/031 rare-tail and E2 remain restricted CSDA conditional results. No independent referee I3 or BW-ingestion receipt is claimed.

**DISPOSITION: PRIMARY_AUTHOR_PAPER_140_ROW_SOURCE_CONTACT_PASS / PUBLISHED_BIN_WIDTHS_READ_PASS / PAPER_TO_SECONDARY_RIVET_W_SIGMA_STAT_140OF140_PASS / AUTHOR_PAPER_CONDITIONAL_K_REPLAY_PASS / HEPDATA_EXPORT_BYTES_AND_COVARIANCE_OPEN / NEUTRINO_PHYSICAL_CEILING_UNCHANGED / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.**
