---
artifact_id: IW_DAX_S9_ROT005_MARKII_AUTHOR_TABLE_III_17_LOW_W_MEASURED_BINS_R68_FIDUCIAL_KERNEL_AND_SOURCE_OVERLAP_GATE_001_20261121
date: 2026-11-21
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
document_type: ORIGINAL_SCIENTIFIC_SOURCE_RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: ORIGINAL_AUTHOR_PUBLISHED_MARKII_17_LOW_W_NUMERIC_ROWS / CONDITIONAL_FIDUCIAL_SOURCE_WEIGHTED_CONVOLUTION / EXPERIMENT_IDENTIFICATION_GAP / MARKII_BELLE_OVERLAP_CROSSCHECK
claim_ceiling: NO_HEPDATA_NATIVE_MARKII_BYTES / NO_JOURNAL_PDF_BYTE_OR_SCREENSHOT_CONFIRM / NO_FULL_MARKII_BELLE_COVARIANCE / NO_PHYSICAL_ALL_W_ALL_ANGLE_PION_SOURCE / NO_PHYSICAL_DAUGHTER_NEUTRINO_FLUX / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX9 ROT005 — Original Mark II paper Table III: 17 measured low-W charged-pion data bins folded against R68 and Belle cross-experiment overlap control

**21 November 2026.** New original-successor SOURCE acquisition and bounded quantitative check after DAX9 ROT004. ROT004 established that a charged point-scalar pion Born model can make W below 0.8GeV materially important, K_Born,fid(W<800MeV)=3.74617437682e−10 compared to DAX-S8 ROT017 / DAX9 ROT001 actual Belle author-paper W0.8–1.5GeV conditional K=3.88686466991e−10. It did **not** recover experimental Mark II numerical data. This ROT005 replaces that purely model-based suggestion **on the actually measured subintervals only** with 17 NUMERICAL VALUES PUBLISHED BY THE ORIGINAL EXPERIMENT, and identifies a critical source gap.

## 1. Original source, provenance and necessary correction of inherited source interpretation

**Primary-author publication:** J. Boyer et al. [Mark II Collaboration], *Two-photon production of pion pairs*, Phys. Rev. D 42 (1990), 1350–1367. DOI https://doi.org/10.1103/PhysRevD.42.1350. The original paper PDF is mirrored by two independent scholarly dissemination sites:
- https://escholarship.org/content/qt0vx433mf/qt0vx433mf.pdf (University of California eScholarship).
- https://scispace.com/pdf/two-photon-production-of-pion-pairs-4902mxt6d2.pdf .
In BOTH full-article PDF TEXT renderings, the original **Table III** was read and the 17 relevant LEFT COLUMN original author-published tuples (W[GeV], sigma[nb], statistical nb, systematic nb) for W<0.8GeV are identical at printed precision: five at 0.355, .365, .375, .385, .395GeV and twelve at .555, .585, .615, .645, .675, .705, .735, .755, .765, .775, .785, .795GeV. Example published anchors: W=.355GeV sigma=232.0±9.3(stat)±31.1(syst)nb; W=.555GeV sigma=99.2±4.2±12.9nb; W=.795GeV sigma=81.4±6.2±7.3nb. NOT a synthetic or Born-generated table. Paper says |cos(theta*)|<0.6 and an additional approximately 7% overall common normalization error (5% luminosity, 5% efficiency) is NOT included in per-bin systematic errors.

**Experimentally material discontinuity, previously underemphasized in ROT004:** the original paper's Sec.III explicitly says only TOF identified pion pairs W=.35..4GeV and LA identified W=.54..1.6GeV have credible pion identification; **between .40 and .54GeV NO reliable particle identification is available**. Hence the phrase “Mark II measured W=.35–1.6GeV” is a range-level abstract, NOT evidence of continuous valid measurement over every W in that range. Exact subinterval bins used below are 350–400 MeV and 540–800 MeV, with gap 400–540 MeV kept OPEN. The near-threshold TOF analysis explicitly assumes the Born angular shape within accepted |z|<.6 to determine corrected cross sections: those data are experimental counts with a model-dependent acceptance correction, NOT wholly theory-free.

**HEPData native status:** https://www.hepdata.net/record/ins304882 (DOI 10.17182/hepdata.22881.v1) identifies Table 1 as original paper T3 and Table 2 as T4. Web/native CSV/JSON attempted but no original numeric HEPData export bytes received in this turn; tools returned cache/access failures. Source reading is **ORIGINAL AUTHOR PAPER TABLE III TEXT**, not an authenticated native HEPData datafile. Web PDF screenshot calls for the readable PDFs failed due cache miss, so visual PDF screenshot verification and local full-PDF SHA could not be claimed. Textual 17-row verification against both mirrors is the actual obtained evidence. Crucial exposure negative knowledge: the unrelated right-side high-W table at 1.185GeV differs between the two PDF TEXT extractors (one reads 241.4nb, other 214.4nb); global full-paper text extraction is NOT certified. The 17 relevant low-W left-side entries agree across both. No journal manuscript PDF hash receipt claimed.

## 2. Declared conditional measured-source numerical convolution, not complete charged-pion physics

Reuse **exact R68 benchmark source operator** from DAX-S8 ROT012/017 and DAX9 ROT001/004: E_gamma=1436554MeV; ideal Planck T=.07818527068831995MeV, C=4 E_gamma T; and 1MeV^-2=389379371937.8198416 nb.

H(W)=4 W^3/C^2[-ln(1−exp(−W^2/C))], with W measured in MeV.

For every Mark II original Table III W center and its **contiguous reconstructed printed-bin interval** [a_i,b_i] inferred from 10MeV or 30MeV and then 10MeV adjacent point spacing, treat the author-published central sigma_i [nb] as CONSTANT in that bin for this explicit *numerical reconstruction* only:
K_mark,reported = Σ_i [sigma_i/(nb per MeV^-2)] ∫_[a_i,b_i] H(W) dW.

This is NOT a proof that the unknown continuous physical pion cross section is constant or that original detector migration/systematics are absent. The 400–540MeV identification gap has NO Mark II source integral inserted. Neither is W<350MeV extrapolated.

The underlying original 17-row dataset including published stat/systematic columns, 10 original paper Mark II overlap bins W0.8–0.9GeV, original Belle Appendix B 140-source rows, original author-written Python mpmath/SciPy code, frozen JSON, README and SHA256 manifest are supplied as a downloadable local reproduction ZIP in this originating conversation. Those files are **not represented as GitHub code uploads**.

## 3. Executed original author-data numerical values and independent controls

45-digit mpmath numerical per-bin integration, and a separately implemented binary64 SciPy integral independently recovered the SAME binned Mark II central K within relative 1e−13:

| Data source/actual support | Binned thermal K (R68 conditional, dimensionless) |
|---|---:|
| Mark II published 5 TOF bins, 350–400MeV | **3.6274292182998825e−11** |
| Mark II published 12 LA bins, 540–800MeV | **1.64410883421723495e−10** |
| Mark II **17 published source bins combined**, excluding gap | **2.00685175604722320e−10** |
| Belle original author paper 140 bins, W800–1500MeV (prior ROT001) | **3.88686466991478366e−10** |

Original author-data Mark II known-bin K / Belle 800–1500 K = **0.516316344013907 = 51.6316%**. This is a material actual-published-measurement **source-support comparison** at the same angular acceptance (|z|<.6); it is NOT a ratio of all physical pion production events, neutron yields, daughter neutrino multiplicities or cosmological source terms. Even the angular-accepted Mark II source and Belle are different experiments and source reconstruction models.

A separate **point-scalar Born MODEL** evaluation from the inherited Klevansky et al (2025) Eq21 and independently coded 36-point angular quadrature in the EXACT same two Mark II actually measured bands returns K_Born,matched=2.2803282716329693e−10, giving Mark II published/matched Born = **0.880071427001207**. This is NOT a lower/upper bound on hadronic amplitude. The strictly MODEL Born unmeasured 400–540MeV gap equals **1.04814137761e−10** and near threshold W(2m_pi,350MeV) equals **4.17704727579e−11**; neither is added as if it were Mark II DATA. ROT004's full low-W Born 3.74617437682e−10 is fully reproduced by partitioning threshold + Mark II-known bins + gap, and is not misrepresented as experimental.

**Cross-experiment overlapping source gate** independently uses original Mark II 10 printed 10MeV bins (.805..895GeV), and Belle original author-paper 20 5MeV bins (.8025..8975GeV), all at |z|<.6. Recomputed:
- K_mark(W800–900MeV) = **5.59239307311557935e−11**;
- K_Belle(W800–900MeV) = **6.64550319081277118e−11**;
- Mark II / Belle in SAME W support = **0.841530417267** (~84.15%), i.e. conditional ~15.85% lower central source-weighted reconstruction for Mark II.

**A source-consistency QUALIFICATION, NOT a statistical discrepancy claim:** different detector efficiencies, two-photon luminosity evaluations, common systematics and W-bin covariance; no actual joint experiment covariance or uncertainty profiling performed. An approximate 7% normalization nuisance in Mark II is separately listed by original authors, Belle reported distinct nuisance components and shared normalization. Do not compute naive p-value or treat Mark II and Belle as a single consistent observed cross-section function without a source-resolution control.

Original Mark II Table III per-bin published statistics provide, **only if bins are independent**, a diagonal-only statistical propagated scale sqrt(Σ (stat_i h_i)^2) = 2.54771626258140529e−12; the analogous diagonal *systematic* scale is 6.14678756121319424e−12, neither an experiment-certified covariance. The paper's 7% separate common normalization would correspond to 1.40479622923305624e−11 in K units *under common multiplier assumption*. These are diagnostics, NOT a confidence interval for a physical low-W rate.

## 4. Scientific interpretation and original negative knowledge

**FALSIFIED:** Mark II original 1990 paper contains only a generic 0.35–1.6GeV locator and no recoverable numeric low-W source for DAX. Table III gives 17 actual measured numeric tuples, directly suitable for restricted measured-source thermal folding. This eliminates Born dependence for the numerical SOURCE-WEIGHT test ON THOSE 17 BINS, not for TOF acceptance correction or unknown W intervals.

**ADDED CRITICAL LIMIT:** Mark II source has 400–540MeV experimental identification gap; ROT004's “350–800MeV coverage” must be qualified rather than promoted as continuous native measurement.

**FALSIFIER OF EASY MERGING:** Mark II and Belle overlap for W=.8..9GeV yields central K ratio 0.84153; before splicing original source arrays, an experimental covariance/normalization and detector-unfolding consistency audit is required. This is not evidence of a significant experimental contradiction.

**PRESERVED:** DAX-S8 ROT030/031 conclusions on rare E_nu>10GeV domination of second raw moment remain source/fiducial/hard-πe-CSDA-conditional. Even a 51.63% newly observed source-weight contribution CANNOT be translated to the fraction of daughter neutrino events eta (DAX9 ROT003) without deriving initial pion energy, medium stopping, decay/competing channels and full W/z angle support. Off-fiducial angles remain entirely open; no claimed new neutrino physics, PBH/BBN bounds, full generator, independent I3 or physics novelty. A binned-source comparison is not an experimental significance test of mathematical ratios.

## 5. Repro, custody, discrete next gate

Originating ZIP `DAX9_ROT005_MarkII_author_data_lowW_source_fold_repro.zip`: 17 source rows, overlap source comparison rows, 140 original Belle paper source rows, Python verifier, frozen JSON, README, SHA256 member manifest. CRC PASS, 6/6 member hashes PASS, clean same-script reexecution yields byte-identical frozen JSON PASS. Complete ZIP final SHA256 **21f7ec2696144fd46345332737d8adc34a4b6ad74f38d9f3298c8573f812c81d**. Original article full PDF bytes NOT bundled or independently hashed. All primary author data table values transcribed from accessible text extraction; two mirror crosschecks for 17 low-W rows PASS.

**Next legitimate falsifier (not automatic task cascade):** retrieve original HEPData Mark II Table1 CSV/YODA or SHA-verified MARKII_1990_I304882.yoda.gz reference; compare 17 rows including units, bin edges and asymmetric uncertainties, then model the 400–540MeV ID gap and original Mark II/Belle overlap acceptance/covariance rather than assuming Born there. This can materially test ROT004's model sensitivity and the source interface, without overclaiming a whole physical neutrino spectrum. No BW writes; prior DAX8 ROT028–031 KN15 READ-ONLY status was resolved separately but their ingestion remains unverified.

**RETURN: MARKII_ORIGINAL_AUTHOR_TABLE_III_17_LOW_W_NUMERIC_SOURCE_PASS / TWO_PDF_TEXT_MIRROR_LOW_W_MATCH_PASS / SOURCE_FOLD_INDEPENDENT_QUADRATURE_PASS / FIDUCIAL_MARKII_17BIN_TO_BELLE_K_RATIO_51P63PCT / MARKII_400_540_PID_GAP_RETAINED / MARKII_BELLE_OVERLAP_84P15PCT_CAUTION / NO_NATIVE_HEPDATA_BYTES / NO_PHYSICAL_UPGRADE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.**
