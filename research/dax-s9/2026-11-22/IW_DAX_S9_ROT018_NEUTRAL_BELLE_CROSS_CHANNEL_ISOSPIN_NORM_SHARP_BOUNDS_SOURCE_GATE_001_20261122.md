---
artifact_id: IW_DAX_S9_ROT018_NEUTRAL_BELLE_CROSS_CHANNEL_ISOSPIN_NORM_SHARP_BOUNDS_SOURCE_GATE_001_20261122
date: 2026-11-22
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: OFFICIAL_SECONDARY_NEUTRAL_BELLE_BYTES_AUTHENTICATED / MATCHED_CHARGED_NEUTRAL_SOURCE_GEOMETRY / SHARP_PHASE_FREE_I2_NORM_FLOOR
claim_ceiling: NO_PRIMARY_HEPDATA_NATIVE_EXPORT / NO_EXPERIMENTAL_COVARIANCE_OR_PVALUE / NO_PHYSICAL_ISOSPIN_AMPLITUDE_FIT / NO_PION_NEUTRINOS_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX9 ROT018 — independent neutral Belle measurement yields phase-free source-central I=2 amplitude norm constraints

**22 November 2026.** Original bounded implementation of mature isospin/Hilbert geometry on newly source-authenticated neutral-pion data. Follows ROT017's proof of helicity underdetermination from ONE unpolarized Belle channel. This is not a discovery of physical I=2 pion production or a replacement for coupled-channel amplitude fits. It introduces independent final-state data, not another adjustable width/phase scan.

## Real original source receipt

Belle charged original author: T. Mori et al, JPSJ 76 (2007) 074102 DOI 10.1143/JPSJ.76.074102, official packaged SECONDARY compressed Rivet source BELLE_2007_I749358.yoda.gz original SHA256 **28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403**, 140×12 native angle .05 bins.

New Belle neutral original author: S. Uehara et al, PRD 79 (2009) 052009 DOI 10.1103/PhysRevD.79.052009, original arXiv 0903.3697 and earlier source 0810.0334. Native original HEPData record https://www.hepdata.net/record/ins815978 DOI 10.17182/hepdata.52161.v1 directly read: **Table 5** W=.85,.87,.89GeV; **Table 6** W=.91,.93,.95GeV; **Table31** independent integrated angular fiducial total. Author paper directly read; notes neighboring W bins after unfolding correlated, detector systematics substantial at low W. **Actual native primary HEPData CSV/YODA downloads HTTP403: NOT HELD**.

Original neutral packaged SECONDARY source new source-only reproducible GitHub Actions run https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/45025075860 from pinned workflow commit 20740d18654b2d1f382e99f6d98198b3ec086c0a. The original whole openSUSE Rivet-data 4.1.2-2.2 RPM 37,554,346B from original mirror passed independently published full SHA256 **a5ca114950e3a75240d3ed8e7af21f27a26713d95a8ecba6ce0885e2bf6dd090**. Extracted genuine official-secondary BELLE_2009_I815978.yoda.gz original compressed **18,555B SHA256 65ed96b71a3e03e5528c406c336aa07277bff3fd9cf1c6b9596a708f14c573dd**; 90 YODA source objects, 31 tables. Source-only GitHub Actions original artifact ID 14755331885 and artifact digest d621293e1b7b24168ed773d3485ccdcf4be38e5e52af078ac1a7113f399d4fb9. These are actual third-party bytes and original experimental table metadata, NOT synthetic/unreviewed numeric data.

**Independent neutral unit closure:** From each Table5/6 neutral angular density 12 bins ×.05, reconstruct original Table31 fiducial sigma(|z|<.6) from entirely separate source object, 5/5 PASS to 0.0045nb rounding. W centre .85: 6.4105 vs 6.41nb; .87:7.3555 vs7.36; .89:8.581 vs8.58; .91:9.207 vs9.21; .93:11.273 vs11.27. This proves exact source energy/angle alignment and avoids width-factor mistakes.

## Exact common source domains and declared approximations

Only W=[.84,.94]GeV and z=abs(cosθ*) in [0,.6]. Five FULL native 20-MeV neutral W bins paired with twenty FULL native 5-MeV charged W bins, each twelve native angular density bins of width .05. Data at native W centres are treated as piecewise constant across each measured bin for the SOURCE-weighted energy fold, not as known sub-bin physical W shape. Same positive inherited R68 photon-temperature H(W) for both, Egamma=1,436,554MeV,T=.07818527068831995MeV and C=4Egamma T, H(W)=4W³/C²[-ln(1−exp(−W²/C))]. No extrapolation into unknown MarkII W gap or |z|>.6.

Isospin rotation is strictly exact only in equal charged/neutral pion mass approximation. Nominal actual-mass phase-space correction to neutral source intensities betaCharged(Wcentre)/betaNeutral(Wcentre) uses charged m=139.57039MeV, neutral m=134.9768MeV, explicitly a small approximate correction and NOT full isospin breaking. Both equal-mass and flat-W-fold controls computed.

Source-centre R68 weighted neutral/charged cross-section ratio after mass correction **0.09448067326790723**, equal-mass 0.09481121741412421. The observed source angular share z=.4..6 within |z|<.6: charged **40.306087%**, independent neutral **28.692075%**, not identical source angular shapes. This is NOT proof of an experimental lepton-background cause. Neutral experiment uses distinct reconstruction corrections, source W binning and correlated errors.

## Exact phase-free geometrical isospin amplitudes, not a fitted physical complex amplitude

With normalized symmetric charged |C>=(|π+π−>+|π−π+>)/sqrt2 and normalized neutral |N>=|π0π0>, standard orthonormal I=0,I=2 channel rotation up to signs is:
 A_C = sqrt(2/3) A_0 + sqrt(1/3) A_2,
 A_N = sqrt(1/3) A_0 − sqrt(2/3) A_2.
A pure I0 gives cross-section ratio N/C=1/2 (as original 2009 Belle neutral paper itself discusses). Inverting A_2 = A_C/sqrt3−sqrt(2/3)A_N; and ||A_C||²+||A_N||²=||A0||²+||A2||² for common kinematics.

For observed fixed nonnegative binned source intensities C_j,N_j on exact shared angular/W supports, arbitrary complex phases and helicity decompositions imply the sharp source-binned Hilbert-norm constraints:
 LOWER f_I2 = Σ_j (sqrt(C_j)−sqrt(2N_j))² /[3 Σ_j(C_j+N_j)]
 UPPER f_I2 = Σ_j (sqrt(C_j)+sqrt(2N_j))² /[3 Σ_j(C_j+N_j)]
 where f_I2 = ||A2||²/(||A0||²+||A2||²). Endpoints attained by explicit aligned or anti-aligned source-cell amplitude witness, **not** asserted to satisfy physical analytic unitarity/phase dynamics. This is mature isospin/Hilbert triangle geometry, NOT a new theorem.

| Geometry of central source | Sharp lower f_I2 |
| -- | --: |
| Total combined intensity only | **0.09732702931802441** |
| Twelve angle bins retained, W aggregated | **0.09976679541180163** |
| Five W bins retained, angle aggregated | **0.09878291054839804** |
| All FIVE W × TWELVE angle cells | **0.10126203532642064** |

The full 60-cell phase-free upper geometry bound **0.6229544054480618**. Thus under declared approximations the entire source-central candidate range is **[10.1262%,62.2954%]** in mathematical norm fraction. This is *NOT an experimental statistical CI, unique amplitude, or daughter-neutrino fraction*. Source-central without mass correction fine-cell lower **0.1009737379877013**. Nominal mass correction with FLAT W bin weighting lower **0.10076380596281946**. Finer binning improves lower and decreases upper bounds; synthetic pure I0 C=2N gives exact lower=0.

**Independent source-code negative controls:** 5/5 neutral Table31 closure; different 20vs5MeV energy slicing, no double counting .05; two YODA SHA256 exact checks, actual original GitHub RPM SHA receipt. A wholly separate Python **standard-library-only** checker re-opens frozen 60-cell CSV and JSON (not YODA parser/scipy code), recreates exact lower/upper from 60 original source-cell masses to <1e-14 and explicitly reconstructs amplitudes satisfying the orthonormal isospin rotation cell by cell and saturating lower and upper bounds. Very important: none of these tests recovers the real photoamplitude phase or full physical source support.

## Reproduction and disposition

Complete original local package in DAX9 user conversation: original two authentic compressed packaged secondary YODA sources, source-receipt and first 160 original neutral source text lines, two independent Python scripts, original frozen JSON+two CSV, original full science report (12kb), README, original GitHub Actions receipt, runtime and clean replay logs, 13 SHA256 payload manifest. Local ZIP named DAX9_ROT018_Belle_Neutral_Charged_PhaseFree_Isospin_Bounds_Repro.zip, SHA256 **267edbbe0b2e34b70902710e946882289d706d415b138bbe9ebf6a836bd85212**, 14 members, ZIP CRC PASS, **13/13 payload SHA PASS**, two separate clean independent directories each replay 3/3 outputs byte-identical PASS. THIS public GitHub report is TEXT ONLY; complete executable not uploaded to GitHub. Source original record links remain valid independent audit handles.

**STOP**: source-only central mathematical norm constraint is not a physical source amplitude fit, statistical significance, resolution of the Belle charged angular anomaly, neutrino daughter fraction, transport/BBN/PBH effect or original novelty; true neutral+charged angular covariance, charged/neutral pion mass-splitting and helicity coupling, unitarity/analyticity, fit and physical phase are not recovered. Next valuable external evidence: source-backed numerical I0/I2 S,D0,D2 fit (Dai–Pennington or equivalent) jointly to BOTH channels or original detector covariance/polarization, not more freely chosen phases.

NO_I3 / NO_BW_WRITE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE.
