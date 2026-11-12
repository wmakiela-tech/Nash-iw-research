---
artifact_id: IW_DAX_S8_ROT015_BELLE_TABLE_SEMANTICS_ANGULAR_RECOVERY_AND_POINTDATA_NO_GO_001_20261112
created_at: 2026-11-12
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
document_type: SCIENTIFIC_RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: EXPERIMENTAL_TABLE_SEMANTICS_REPAIR / CONDITIONAL_ANGULAR_BIN_CLOSURE / SHARP_POINT_SAMPLE_LIPSCHITZ_ENVELOPE / SMOOTH_NONIDENTIFIABILITY
claim_ceiling: NO_RAW_BELLE_HEPDATA_OR_YODA / NO_EXPERIMENTAL_CROSS_SECTION_FIT / NO_FULL_QCD_PION_RATE / NO_NEUTRINO_TRANSPORT_OR_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX-S8 ROT015 — Belle table semantics, angular recovery, and finite-point thermal-rate no-go

**12 November 2026.** The new findings are source/semantic and mathematical gates, NOT experimental results and NOT a new physics amplitude. Science lineage: DAX-S7 R68 FIRST three-channel conditional gamma gamma first-muon probability; DAX-S8 ROT012 FIRST point-scalar Born charged-pion fourth channel; ROT013 FIRST point-Born Belle joint fiducial support fraction 19.557%; ROT014 FIRST general R68 linear-W Planck kernel, mode and sharp BIN-INTEGRAL positivity bound. All earlier source-typed results retained at their prior claim ceilings.

## Source semantic correction: 140 Rivet W slots are NOT proven 140 Belle measured total cross sections

Read the original HEPData Belle 2007 record https://www.hepdata.net/record/ins749358 DOI https://doi.org/10.17182/hepdata.51842.v1 . Its original data abstract distinguishes:
- source part reporting TOTAL AND DIFFERENTIAL cross sections for energy positions 0.8025 to 1.1475 GeV;
- source part reporting DIFFERENTIAL cross sections for positions 1.1525 to 1.4975 GeV.

The record enumerates 141 tables; Table 1 is titled "Total cross section". The complete original numeric table rows, including units and uncertainties, were NOT OPENED because HEPData raw CSV/JSON endpoints produced cache misses and container networking failed. Do not infer all 140 numeric total-cross-section measurements from the 140 W slots in Rivet or assume that Table 1 has any particular row count without direct inspection.

Original Rivet validated source https://heprivet.org/analyses/BELLE_2007_I749358/ was READ: _energyAxis 140 W slots over 0.8..1.5 GeV, _thetaAxis 12 |cos theta*| slots over 0..0.6, energy histogram fiducial condition |cos theta*|<=0.6, angular histogram scaled by physical crossSection()/nanobarn/sumOfWeights and 1/angle-bin width. Thus a displayed "Total" is not proof of FULL ANGULAR total; angular acceptance and source data observable must be typed precisely. The C++ defines the observation, not the measured numerical payload. Belle original Mori et al JPSJ 76(2007) 074102 DOI 10.1143/JPSJ.76.074102.

**Specific alternative source locator:** Official openSUSE/Rivet-data archive inventory lists /usr/share/Rivet/BELLE_2007_I749358.yoda in Rivet-data-3.1.11-bp160.1.17.noarch.rpm. Package index (but not payload) was searched: https://www.rpmfind.net/linux/RPM/opensuse/16.0/noarch/Rivet-data-3.1.11-bp160.1.17.noarch.html . Actual openSUSE mirror lists ~31.4MB RPM https://ftp.fau.de/opensuse/distribution/leap/16.0/repo/oss/noarch/ . File download ATTEMPTED but failed. Presence in index != original YODA read, file integrity receipt, or numerical source-currentness.

## Result 1: EXACT conditional 12-angle histogram closure

Let z=|cos(theta*)| and for each fixed invariant W let d sigma_fid/dz be measured over z in [0,0.6]. If 12 original angular values y_j(W) are truly bin AVERAGES of this same differential cross section, in identical units and with no hidden acceptance extrapolation, then

sigma_fid(W)=sum_{j=0}^{11} delta_z_j * y_j(W),  delta_z_j=0.05.

This is an exact bin-integral identity and a viable recovery route to fiducial cross sections at the higher W positions where source abstract describes differential-only tables. But first actual table rows/units/bin semantics must be recovered. The 140 angular positions do not themselves solve interpolation in W.

Independent source-model test, NOT Belle measured data: evaluated point-pion scalar Born differential Eq.21 (Klevansky/Lemmer/Beygi 2025 DOI 10.1140/epja/s10050-025-01524-6) over exactly 12 bins and compared their sum to separate analytic angular primitive for W=900, 1200, 1450 MeV. Relative closure residuals ~2.0e-56,4.1e-56,2.0e-56 in 55dps mpmath. PASS_SOURCE_BORN_12_ANGULAR_BIN_CLOSURE. The data are synthetic physics-model controls only, NOT experimental numerical validation.

## Result 2: exact positive smooth point-data identifiability no-go

Inherited R68 universal positive kernel for a fixed E_gamma=1436554 MeV and ideal isotropic thermal T=0.07818527068831995 MeV, PER LINEAR dW:

H(W) = W^3 / (4 E_gamma^2 T^2) * [-ln(1-exp(-W^2/(4 E_gamma T)))], H(W)>0 on W=[800,1500] MeV.

Under ONLY a finite set of exact POINT observations sigma(W_i)=s_i>=0, the class of nonnegative C-infinity functions interpolating all observations yields
  inf_sigma ∫_[800,1500] H(W) sigma(W) dW = 0
and
  sup_sigma ∫_[800,1500] H(W) sigma(W) dW = infinity.
Proof: separated smooth nonnegative compact bumps centered at each W_i with heights s_i and widths delta->0 drive integral to0 while preserving all data. Add an arbitrarily high nonnegative smooth bump supported strictly between two sample nodes to drive integral to infinity with all data fixed. This is a classical weak-model theorem, NOT a physically admissible arbitrary QCD scattering amplitude: true hadronic unitarity/analyticity may prohibit this class. Point samples MAY differ from true source energy-bin averages: theorem only applies if point interpretation is source verified.

Purely synthetic explicit C-infinity test for 140 data positions each s_i=1 arbitrary unit: with bump radii 1.0,0.2,0.04 MeV the positive thermal integrals are 0.2771854834,0.05543710082,0.01108742020, versus constant-interpolation K=1.148335183. An additional bump strictly between sample points leaves ALL 140 synthetic observed values unchanged while increasing K. No physical rate inference.

## Result 3: sharp conditional Lipschitz envelopes

IF independent physics sources supply a validated quantitative L>=0 satisfying |sigma(W)-sigma(V)|<=L|W-V| and the exact point data are jointly consistent with it, the sharp lower/upper admissible interpolants are

sigma_lower(W)=max{0, max_i[s_i-L|W-W_i|]},
sigma_upper(W)=min_i[s_i+L|W-W_i|].

Both are feasible nonnegative L-Lipschitz interpolants satisfying every sample because pairwise consistency |s_i-s_j|<=L|W_i-W_j| holds. Therefore these two extremes ATTAIN the sharp integrated bounds ∫H sigma_lower <= K <= ∫H sigma_upper. Measurement errors and interval-valued observations require a separate feasibility problem and were not assumed absent in real Belle measurements: this is a *noiseless mathematical gate*.

Synthetic SciPy fixture ONLY: 140 exactly equal point samples s_i=1 over 800..1500MeV, assumed arbitrary L=0.1 arbitrary sigma-units/MeV. Nominal constant K=1.1483351829725756; lower=1.0047933587489197, upper=1.2918770071962316, relative ±12.4999935865%. This is not a Belle uncertainty or bound and L is NOT identified physically. Shows that ROT014 ~2.371% maximum variation of H within one 5MeV slot is a different uncertainty source from interpolation of sigma.

Actual hadronic amplitudes may contain resonances near 980 or 1270MeV and strong final-state interactions; neither a finite L nor complete angular/invariant-energy extension was verified. Dai/Pennington 2014 DOI 10.1103/PhysRevD.90.036004 is relevant earlier unitary/dispersive prior art, NOT executed.

## Custody and next source-native discriminator

The original HEPData table inventory and Rivet code are SOURCE READ; raw numerical CSV/JSON/YODA = ACCESS_BLOCKED, no experimental fit or true pi cross section. Recovery should use exact HEPData primary version or provenance-checked packaged YODA; verify per-table 5MeV W-center/bins, units, angular acceptance, error/covariance and bin-average semantics. Then compute sigma_fid(W) from correct angular bin AREAS for differential-only positions and compare in overlap with Table 1 wherever actual data allow. Only then source-model amplitude or justified W smoothness permits a full Planck convolution. The 4e massive QED source task was separately acknowledged by XH-S5; XH-S6 is currently active successor, with NO acknowledged pion task. No duplicate source-owner cascade.

Author local full bundle: 11 members, CRC PASS, SHA256 10/10 PASS, three distinct clean-extract Python programs reexecuted byte-identically to frozen JSON PASS. Source raw data not included. Reproducibility controls are author-generated and not external physics referee.

**DISPOSITION: HEPDATA_ABSTRACT_SPLIT_SOURCE_READ / RIVET_140_SLOT_NONIDENTITY_GUARD / ANGULAR_12_BIN_CONDITIONAL_CLOSURE_PASS / CINF_POINT_DATA_NONIDENTIFIABILITY_PASS / SHARP_CONDITIONAL_LIPSCHITZ_ENVELOPE_PASS / EXPERIMENT_NUMERIC_ACCESS_BLOCKED / BW_GITHUB_PENDING_BW_INGEST / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.**
