---
artifact_id: IW_DAX_S8_ROT018_REAL_BELLE_ERROR_COVARIANCE_IDENTIFIABILITY_AND_R68_FIDUCIAL_GATE_001_20261112
created_at: 2026-11-12
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
document_type: SCIENTIFIC_RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: ACTUAL_SHA_PINNED_RIVET_BELLE_MARGINAL_ERRORS / CONDITIONAL_SOURCE_INTERVAL_PROPAGATION / EXACT_PSD_COVARIANCE_NONIDENTIFIABILITY
claim_ceiling: NO_PRIMARY_HEPDATA_BYTE_IDENTITY / NO_SOURCE_ENERGY_BIN_SEMANTICS / NO_MEASURED_COVARIANCE / NO_EXPERIMENT_CONFIDENCE_INTERVAL / NO_FULL_PHYSICAL_PION_RATE / NO_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX-S8 ROT018 — Actual Belle/Rivet asymmetric errors and sharp covariance-unknown R68 gate

**12 November 2026.** Source-grounded scientific return. This computes mathematical sensitivity and covariance-identification limits on ACTUAL numeric Rivet-data Belle reference values. It does NOT compute a full physical pion rate or an experimental confidence interval.

## Firstness and source custody

DAX-S7 R68 FIRST restricted first-muon gamma-gamma probability to three channels only. DAX-S8 ROT012 FIRST evaluated point-charged-pion Born fourth-channel conditional sensitivity; ROT013-016 established Belle fiducial window, Planck kernel, source semantics and amplitude interference constraints. DAX-S8 ROT017 FIRST obtained real numeric Belle Rivet data in this DAX lineage, source verified by native GitHub Actions run https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43309487872. ROT018 FIRST uses their real asymmetric ERROR CHANNELS and tests UNKNOWN ENERGY COVARIANCE. No source-owner or science-acceptance inference and no additional external-source task.

Belle original Mori et al, J Phys Soc Japan 76, 074102 (2007), DOI https://doi.org/10.1143/JPSJ.76.074102 . Primary HEPData https://www.hepdata.net/record/ins749358 DOI https://doi.org/10.17182/hepdata.51842.v1 remained 6/6 HTTP403 for native numeric requests, so NO PRIMARY BYTE EQUALITY. Secondary source obtained from officially SHA-verified Rivet-data 4.1.2-2.1 RPM with whole package SHA256 8bed5d37a841e90ffaf1af8fd6f28fc2823c38af87e884d2b78a99a378fc489b. Actual compressed YODA BELLE_2007_I749358.yoda.gz is 29215 bytes SHA256 28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403, with 141 genuine numerical YODA V3 objects: Table1 140 positive fiducial y(W) and asymmetric stat/sys errors; Tables2-141 twelve angular y and stat/sys_1/sys_2 each. Rivet validated analysis https://heprivet.org/analyses/BELLE_2007_I749358/ cuts |cos(theta*)|<=0.6, normalises in nanobarn. Original reference bytes INCLUDED in local SHA-verified package; raw primary HEPData not included.

## Exact mathematical quantity and explicit source condition

Inherited fixed R68 E_gamma=1436554 MeV, ideal isotropic Planck T=0.07818527068831995 MeV, C=4ET, and source-invariant-W total cross section per angular fiducial acceptance. Thermal kernel per LINEAR dW is H(W)=4 W^3/C^2 [-ln(1-exp(-W^2/C))]. Convert 1 MeV^-2=389379371937.81984 nb. Under the CONDITIONAL assumption that each source Table1 y(W_i) represents a 5MeV bin-average value over [800+5i,805+5i]MeV, define strictly positive w_i = integral_bin H(W)dW / (nb per MeV^-2), and K_fid = sum_i w_i y_i. THIS primary bin-average semantics is not source-proven; if Table1 numbers are only point samples, ROT015 no-go for unbounded interpolation still applies.

Actual source-y central full-window K=3.88686466991478366418838581957044078e-10. The original real YODA has per-row signed down/up errors for stat and sys. Let d_stat_i,u_stat_i,d_sys_i,u_sys_i >=0 be magnitudes. Exact attainable LINEAR PROGRAM box extrema under the invented source-marginal simultaneous finite BOX constraint, y_i-d_stat_i-d_sys_i <= y_i' <= y_i+u_stat_i+u_sys_i, are:

K_box_LOW = 3.3943177950208697217474497225954059368e-10.
K_box_HIGH= 4.3907152771902658751674037576853869681e-10.
Relative to central: -12.67208706046% and +12.96290583965%. Source lower y_i' remain positive (minimum 21.52 nb).

This is a **conditional box sensitivity**, NOT Belle's 68%, 95%, or other joint confidence interval. It assumes every marginal reported error magnitude is a simultaneous hard interval and ignores error distribution correlations; it is therefore NOT a measured statistical uncertainty.

## Covariance identification theorem, rigorous but statistical-prior dependent

For one set of 140 hypothetically symmetric marginal standard deviations s_i interpreted from the respective positive source error magnitudes, with positive rate weights w_i, set a_i=w_i s_i. Independently fluctuating energy errors give SD_ind(K)=sqrt(sum a_i²); perfectly positively aligned energy errors give SD_coh(K)=sum a_i. With no knowledge of correlation but positive-semidefinite covariance and fixed diagonal, Gram representation C_ij=s_i s_j (u_i dot u_j), where u_i are unit vectors, gives the SHARP interval

max(0, 2 max_i a_i - sum_i a_i) <= SD(K) <= sum_i a_i.

Upper bound is the triangle inequality and attained by common u_i; lower is the polygon/triangle inequality and attained by closing a polygon of lengths a_i when max a_i<=sum others. For all four source error-magnitude proxies, largest a_i/total <2.75%, so the lower mathematical bound is ZERO. This does NOT mean Belle measurement error zero: arbitrary PSD correlations include contrived complete cancellation, and source covariance is unavailable.

| Error marginal | Independent RMS relative to central | Coherent positive alignment relative to central | PSD mathematical lower |
| --- | ---: | ---: | ---: |
| stat down/up | 0.0916560% | 0.9299734% | 0 |
| sys down | 1.1121796% | 11.7421137% | 0 |
| sys up | 1.1397415% | 12.0329324% | 0 |

Source asymmetric errors themselves are NOT a symmetric standard-deviation population. These figures are conditional PROXY scenarios, not true statistical variances, and stat/sys category independence is not presumed.

## Genuine angular error-table control, limited to WITHIN ONE energy

For each of 140 energies, independently summed real original 12 angular bins. Source central closure 140/140 at max relative mismatch 5.8637269849e-5. Angular statistical down-error quadrature 0.05 sqrt(sum_j stat_j^2) divided by Table1 corresponding stat down has median 0.990197 and range [0.977464, 0.998764]. Source common-like sys_2 angular linear addition 0.05 sum_j abs(sys_2,j) divided by Table1 combined sys down has median 0.996847, range [0.974265,1.000771]; upper median 0.997221, range [0.977273,0.999293]. This suggests a substantial angular common-like systematic COMPONENT, but does NOT identify the cross-W covariance. Do not double count sys_1 and sys_2 on top of Table1 already combined sys.

## Actual-source model implications with claim ceiling

- Restricted Belle fiducial point-pion Born toy K_Born=1.77923637803288135e-10. Source-value box ratios K_Belle/K_Born in [1.90773853150, 2.46775264456], central 2.1845690. These are NOT global physical QCD bounds or true measured systematic confidence ranges.
- Fix the R68 inherited scalar e+e-, mu+mu-, DPP denominators without changing them. Adding ONLY the conditional Belle-fiducial pion proxy yields P_first_mu(K) in [0.0861471737182, 0.0862256351312], central 0.0861868316264. NOT physically complete first muon rate, eventual muon yield or energy deposition.
- Real source weighting: W=0.8..1.15GeV accounts for 57.3265% of the declared fiducial K, W=1.15..1.5GeV accounts for 42.6735%. The upper experimental energy region is material despite the source primary HEPData abstract distinguishing total/differential table data there.

## Reproducibility and STOP

Actual local 11-member ZIP includes source YODA with pinned SHA, full report, source audit, README, 60-digit mpmath full 141-object parser, independently written SciPy first-object parser, two frozen JSON outputs, original 140-row error-weight CSV, a clean replay verifier, and SHA256 member manifest. All 10 payload SHA256 PASS; ZIP CRC PASS; two programs reexecuted cleanly, THREE derived files byte-identical to frozen outputs PASS. Source acquisition GitHub Actions was done in ROT017, not rerun as an original experimental measurement by ROT018. This is author reproducibility, no external referee.

Remaining gating facts: PRIMARY HEPData source byte identity OPEN, energy point-vs-bin semantics OPEN, actual Table1 cross-energy covariance or published systematic nuisance model OPEN, full charged-pion angular/energy/QCD amplitude OPEN, hadronic/neutrino transport and PBH/BBN OPEN. No new automatic XH-S6 source task; KN13 alone controls BW ingestion. Source concentration in same gamma-gamma source family remains flagged to Moderator, not automatic scientific closure.

DISPOSITION: REAL_RIVET_ASYMMETRIC_ERROR_SOURCE_PASS / ANGULAR_ERROR_INTERNAL_CONTROL_PASS / CONDITIONAL_BOX_SOURCE_PASS / EXACT_SHARP_PSD_COVARIANCE_NONIDENTIFICATION_PASS / EXPERIMENT_CI_NOT_CLAIMED / PHYSICAL_PION_RATE_OPEN / GITHUB_PENDING_BW_INGEST / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.
