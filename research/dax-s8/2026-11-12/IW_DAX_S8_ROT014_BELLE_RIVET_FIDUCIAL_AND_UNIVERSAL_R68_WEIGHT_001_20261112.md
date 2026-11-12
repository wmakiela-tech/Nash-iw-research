---
artifact_id: IW_DAX_S8_ROT014_BELLE_RIVET_FIDUCIAL_AND_UNIVERSAL_R68_WEIGHT_001_20261112
created_at: 2026-11-12
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
document_type: SCIENTIFIC_RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_HEPDATA_RAW_NUMERIC_ROWS / NO_BELLE_EXPERIMENTAL_FIT / NO_FULL_QCD_PION_AMPLITUDE / NO_NEUTRINO_OR_DEPOSITION / NO_PBH_BBN_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX-S8 ROT014: original Belle/Rivet fiducial selector, universal thermal W-kernel and sharp bin-area bounds

**12 Nov 2026.** Source-typed mathematical science return. NO physical pion rate or QED differential result. DAX-S7 R68 FIRST limited photon first-muon probability to three channels. DAX-S8 ROT012 FIRST performed conditional point-pion Born fourth-channel test. ROT013 FIRST found only 19.557% of the declared Born-model collision hazard in Belle's joint measured W/angular window. Those results and strict ceilings remain in force. ROT014 is independent of pion Born except for a deliberately synthetic check.

## Primary original-source receipts

* Belle experimental HEPData https://www.hepdata.net/record/ins749358 , DOI https://doi.org/10.17182/hepdata.51842.v1 : record and original table inventory read; Table 1 labelled "Total cross section." Raw numeric CSV/YAML/JSON rows NOT OPENED: web cache miss and local container DNS blocker. Do NOT claim a Belle data fit, its measured numerical cross section or bin-error covariance.
* Rivet validated analysis original public C++ source https://heprivet.org/analyses/BELLE_2007_I749358/ READ. Defines 140 energy bins W=0.8..1.5 GeV, 12 angular bins |cos(theta*)|=0..0.6. Its cross-section histogram increments ONLY when |cos(theta*)|<=0.6. It is scaled by crossSection()/nanobarn/sumOfWeights(). Differential ANGULAR histograms separately get bin-width scaling, the energy-scan hist does not. This is a source-native implementation of the FIDUCIAL pion cross section at selected collision energies; it is not automatically the full-angular total cross section or dσ/dW. The Rivet executable and original YODA numerical reference data were NOT read.
* Belle Mori et al. 2007, DOI https://doi.org/10.1143/JPSJ.76.074102 , W=0.8..1.5GeV and angle acceptance |cosθ*|<0.6. No experiment numeric values in this study.
* Klevansky, Lemmer, Beygi 2025, DOI https://doi.org/10.1140/epja/s10050-025-01524-6 , original point-scalar pion Born Eq21/22 previously read. Used in ROT014 ONLY as synthetic nonnegative bin-area input, never true QCD/measurement.

Fiducial selector matters: HEPData field name Total does not mean uncut all-angle total. Source domain labels MUST be retained.

## Exact universal isotropic collision kernel

For fixed E_gamma=1436554 MeV and isotropic ideal Planck bath T=0.07818527068831995 MeV, x=epsilon/T, u=(1-cos theta_inc)/2, collision s=4ETxu and relative flux 2u, any unpolarized TOTAL gamma-gamma invariant-s cross section has unnormalised hazard

K[sigma] = integral_0^infinity dx x²/(e^x-1) integral_0^1 du (2u) sigma(4ETxu).

Positive Fubini, y=xu, and integral_y^infinity dx/(e^x-1)=-ln(1-e^-y) give

K = integral_0^infinity dy 2y[-ln(1-e^-y)] sigma(4ETy)
  = integral_0^infinity dW H(W) sigma(W²),

H(W) = [W³/(4 E² T²)] * [-ln(1-exp(-W²/(4ET)))].

For charged pion support sigma=0 at W<2m_pi. The H kernel depends on incident bath geometry and Planck spectrum, NOT on charged pion Born/QCD differential final-state distribution. This is not a universal law for anisotropic baths, polarized beams or outgoing-target energy deposition.

### The UNIQUE peak per linear dW has a rigorous proof

C=4ET, y=W²/C, L(y)=-ln(1-e^-y). Sign H'(W)=sign[3L(y)-2y/(e^y-1)]. Define D(y)=(e^y-1)L(y), g(y)=2y/D(y). Its derivative is positive: A(y)=(y-1)e^y+1>0, D-yD'=y-A(y)L(y). Since 0<L(y)<1/(e^y-1) and e^y-1>y, A(y)L(y)<A(y)/(e^y-1)=y+y/(e^y-1)-1<y. Thus g'(y)>0. Limits g(0+)=0, g(infty)=infty; g=3 has exactly one root, which is the global maximum of H.

72digit mpmath and separate SciPy root control:

y_peak=1.26500946957654603089825552256522863810...
W_peak=753.8767226372796806118457029181189703 MeV.
C=449269.4533935551098092 MeV².
H(W_peak)=0.00281567030696602736334416835113666 MeV^-1.
Belle lower edge=800MeV, 46.1232773627203MeV ABOVE kernel peak.

H(800)/H(peak)=0.99189825002656.
H(980)/H(peak)=0.83122248684291.
H(1500)/H(peak)=0.1592905939760.

This is NOT a measured event-spectrum mode. Event spectrum is H(W)*sigma(W²) and may peak elsewhere. MODE IS MEASURE-TYPED: with d ln W instead of dW it is W*H(W), with different peak.

## Source-agnostic positivity-only bin-area envelope

All 140 source analysis bins of width 5MeV in [800,1500] MeV lie to the right of the H peak, where H is strictly decreasing. For ACTUAL nonnegative measured BIN-INTEGRALS A_j=integral_[Wj,Wj+1] sigma_fid(W)dW, one can assert without interpolation or extra physics:

SUM_j H(Wj+1)*A_j <= K_fid <= SUM_j H(Wj)*A_j.

This is sharp under stated positivity-only functions. Max single bin H(left)/H(right)=1.0237057110370182 (2.3705711% bound width, relative to lower), but it is NOT an experimental or physical uncertainty, and does NOT apply to point-sampled cross sections unless bin-integral semantics are independently validated. The existing Rivet energy histogram uses cross section at a FIXED generated sqrt(s) and does NOT imply A_j values.

**Internal synthetic control only:** use point-scalar pion Born fiducial sigma to construct 140 exact numerical bin integrals, obtaining a weighted direct fixture 1.7792363780328816e-10 (consistent with ROT013), strictly between lower 1.771387282669995e-10 and upper 1.787048714096226e-10, total bracket width ~0.884% relative. These are Born source-model units, NOT Belle measurement.

If true measured bin integrals eventually become available and full pion σ_tot>=σ_fid, they can set a positivity lower bound on full charged-pion collision hazard without a full QCD amplitude for the measured support. However NO such numerical physical lower bound is currently computed; outside Belle source W/angles and complete hadronic dynamics remain unconstrained.

## Reproductions, failures, custody

Local author bundle contains three independent scripts: high precision mpmath closed-root+Planck formula; distinct SciPy root and direct-x vs direct-W constant σ check; SciPy 140-bin positivity bound harness with typed optional input schema, default Born-only synthetic fixture. 72digit first test and float SciPy second test agree. Independent constant-sigma x vs W integral relative difference ~3.23e-15 in SciPy. In initial source author test, comparing finite x<=120 with finite y<=120 omitted a tiny source-domain edge tail and FAILED overly tight 1e-60 threshold; corrected by extending BOTH integrals to infinity, now exact 72digit replay PASS. Failure retained in extended local report, no silent erasure. Local full original ZIP with 11 entries: CRC PASS; nine content SHA-256 checks PASS; THREE clean-extract script frozen JSON byte-identical replays PASS. This is author reproducibility, NOT external referee or native measurement replay.

No HEPData numeric rows or Rivet YODA data were obtained, and current XH-S6 is successor to acknowledged XH-S5 QED source contact but has NOT accepted a new pion retrieval task. Existing source owner custody is preserved; do not create new task cascade or imply BW ingestion. Reopen on raw Belle numerical rows and actual data-semantics proof (bins vs points), then appropriately sourced full-angular QCD amplitude or limited quantitative fiducial lower-bound question.

DISPOSITION: BELLE_RIVET_FIDUCIAL_SELECTOR_SOURCE_PASS / HEPDATA_NUMERIC_ACCESS_BLOCKED / UNIVERSAL_W_KERNEL_UNIQUE_MODE_PASS / CONDITIONAL_SHARP_POSITIVE_BIN_ENVELOPE_PASS / PHYSICAL_PION_RATE_OPEN / GITHUB_PENDING_BW_INGEST / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.
