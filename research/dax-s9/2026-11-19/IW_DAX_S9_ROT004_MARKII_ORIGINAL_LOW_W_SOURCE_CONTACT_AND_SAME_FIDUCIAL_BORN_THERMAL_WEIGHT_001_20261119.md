---
artifact_id: IW_DAX_S9_ROT004_MARKII_ORIGINAL_LOW_W_SOURCE_CONTACT_AND_SAME_FIDUCIAL_BORN_THERMAL_WEIGHT_001_20261119
date: 2026-11-19
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
document_type: SCIENTIFIC_RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: ORIGINAL_MARKII_PRIMARY_SOURCE_AND_HEPDATA_RECORD_LOCATOR / SOURCE_MATCHED_BORN_LOW_W_THERMAL_KERNEL_FALSIFIER / PION_SUPPORT_INCOMPLETENESS
claim_ceiling: NO_ORIGINAL_MARKII_NUMERIC_ROWS_INGESTED / NO_PHYSICAL_LOW_W_CROSS_SECTION_LOWER_BOUND / NO_EXPERIMENTAL_NEUTRINO_CI / NO_FULL_QCD_AMPLITUDE / NO_FULL_MEDIUM_TRANSPORT / NO_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX9 ROT004 — Mark II original low-W charged-pion source contact and same-fiducial Born countermodel under R68 thermal weighting

**19 November 2026.** Bounded divergent-search scientific turn after DAX9 ROT001 original Belle paper->Rivet reconciliation, ROT002 same-cell positive source-reweight theorem, ROT003 off-support mixture identifiability no-go. A missing-W original-source locator and one physically motivated **toy** support test; not a numerical extraction of Mark II experimental cross sections, not an experiment and not a full physical pion/BBN model.

## 1. Primary literature and source-native identification, without manufactured measurements

**ORIGINAL MARK II SOURCE:** J. Boyer et al. [Mark II Collaboration], *Two-photon production of pion pairs*, Physical Review D **42**, 1350–1367 (1990), DOI **10.1103/PhysRevD.42.1350**. Original journal abstract confirms charged-pion-pair invariant masses between **350 MeV and 1.6 GeV**. The corresponding original HEPData record was directly opened and READ at https://www.hepdata.net/record/ins304882 ; canonical DOI **10.17182/hepdata.22881.v1**. Original table inventory shows **two tables** (Table 1: from T3; Table 2: from T4, statistical errors only). Attempted original HEPData JSON and full CSV access yielded cache misses in the available web tools; local container outbound DNS also failed. **NO NATIVE MARK II NUMERIC TABLE ROWS WERE READ**. This is an access limitation, not provider downtime or proof of missing source.

**Validated numerical source locator:** original Rivet analysis https://heprivet.org/analyses/MARKII_1990_I304882/ . Its publicly displayed source code explicitly uses cTheta = abs(p_z/|p|), 0.1-sized cTheta slots and veto if floor(cTheta/0.1)>5, hence a restricted support **|cos(theta*)|<0.6** (boundary convention not a material numerical measurement). The 0.35..1.6GeV range is in its init guard. The independently published openSUSE Rivet-data **package inventory** confirms a file named /usr/share/Rivet/MARKII_1990_I304882.yoda.gz in Rivet-data-4.1.2-2.1.noarch.rpm. Its file name is VERIFIED IN INVENTORY ONLY; the numeric payload SHA, byte equality to original HEPData and data contents are **NOT** verified.

**MATURE PRIOR ART:** L.-Y. Dai and M. R. Pennington, *Comprehensive Amplitude Analysis ... below 1.5GeV*, Phys Rev D90 036004 (2014), arXiv:1404.7524, DOI https://doi.org/10.1103/PhysRevD.90.036004, explicitly describes Mark II as the unique charged-pion data source below 700MeV in their analysis, with sparse near-threshold points and sizeable uncertainties. It constrains amplitudes using unitarity, analyticity, crossing, and hadronic ππ/KK information; Born alone is inadequate. ORIGINAL math source: S.P. Klevansky, R.H. Lemmer, A. Beygi, *EPJA* (2025), DOI https://doi.org/10.1140/epja/s10050-025-01524-6, exact charged point-pion Born angular differential Eq.(21) and total Eq.(22). These sources pre-exist NASH; NO novelty claim.

**PREDECESSOR EVIDENCE:** DAX-S8 ROT012 already calculated the full-angle all-W charged point-Born R68 term 9.097617621183627e-10, and DAX-S8 ROT017 already calculated Born Belle-W/fiducial K=1.77923637803288135e-10 and actual secondary Belle fiducial K=3.88686466991478366418838581957e-10. DAX9 ROT001 independently tied the Belle 140 W σ/stat values to the original 2007 author paper at publication precision. These original firstnesses are preserved. New ROT004 question: **is a physically motivated missing-W support model potentially material at the SAME angular acceptance?**

## 2. Exactly defined conditional scalar Born benchmark and thermal source fold

Hold fixed the R68 benchmark E_gamma=1,436,554 MeV, T=0.07818527068831995 MeV, alpha=1/137.035999084, m_pi=139.57039 MeV. For W=sqrt(s)≥2m_pi and beta=sqrt(1-4m_pi²/W²), the original published charged-pion scalar point-Born differential formula (Klevansky et al Eq21) is

dσ_B/dΩ = alpha² beta /(2W²) * [ ((1-beta²)/(1-beta² z²))² + ((beta²(1-z²))/(1-beta² z²))² ],

with z=cosθ*. For a symmetric |z|≤zmax fiducial cross section,

σ_B,fid(W;zmax) = (2π alpha² beta/W²) ∫_0^zmax dz [ ((1-beta²)/(1-beta² z²))² + ((beta²(1-z²))/(1-beta² z²))² ].

For zmax=1 this integrates exactly to Klevansky et al Eq22:

σ_B,total(W)=(2π alpha² beta/W²) [2-beta² - ((1-beta⁴)/(2 beta)) log((1+beta)/(1-beta))].

The original DAX8 R68 positive Planck+angle kernel PER LINEAR dW is unchanged:

H(W) = 4 W³/C² [-log(1-exp(-W²/C))], C=4 E_gamma T.

Define K_Born(a,b;zmax)=∫_a^b H(W) σ_B,fid(W;zmax) dW. This is unnormalized source *model* rate weight, NOT a measured charged pion rate.

Exactly matching the Belle fiducial **zmax=0.6** is necessary: all-angle Born [2m,0.8] / Belle fiducial [.8,1.5] is a mismatched-acceptance comparison, so it is shown only as a separate sensitivity.

## 3. Actually executed quantitative source-support stress test

Two independent numerical integration routes executed in Python/SciPy/NumPy:
A. adaptive angular and energy quadrature with W=2m_pi+u² regularizing the threshold;
B. tensor-product Gauss-Legendre 160 W-nodes × 64 z-nodes with the same threshold transform.
All band integrations agree to declared relative 1e−9; 8-energy-point Eq21 angular integral versus independent closed Eq22 all-angle cross section PASS. Inherited ROT012 exact full-angle Born result and ROT017 same-window fiducial Born result are reproduced within numerical integration tolerance.

| W interval MeV | Point-scalar Born K, |z|<0.6 | Point-scalar Born K, full-angle |
| --- | ---: | ---: |
| 279.14078–350 | 4.17704727578775e−11 | 7.59454178945600e−11 |
| 350–600 | 1.86734607414294e−10 | 3.23517740736597e−10 |
| 600–800 | 1.46112357509980e−10 | 2.27317716357315e−10 |
| 800–1500 | 1.77923637803288e−10 | 2.74283972221896e−10 |
| 1500–3000 | 5.50814557059706e−12 | 8.69691207510182e−12 |

This is **entirely Born-model-only** across the table; **Mark II measured values have not been inserted**.

The **conditional hybrid comparison** is:
- **Born, missing W below 0.8GeV, same Belle angular support** K_Born,low,fid = **3.74617437682152e−10**;
- **Original Belle author-paper conditional W0.8–1.5GeV, same angular support** K_Belle,fid = **3.88686466991478e−10**;
- ratio **K_Born,low,fid / K_Belle,fid = 0.9638036553775** (96.3804%);
- illustrative hybrid low-W share K_Born,low,fid/(K_Born,low,fid+K_Belle,fid) = **0.4907841233202** (~49.08%). This hybrid mixes a Born assumption with Belle measured values and is **not a physical branching ratio**, lower bound, upper bound, or inference on missing daughter event fraction η.
- restricting modeled low-W band to Mark II documented coverage **350–800 MeV**: K_Born,MarkIIrange,fid = **3.32846964924275e−10**, ratio to Belle = **0.8563379309308** (85.63%); the unmeasured-by-this-Rivet subset 2m_pi–350 contributes Born-model 4.1770472758e−11.
- full-angle low-W Born = **6.26780874988473e−10**, but dividing that by Belle fiducial would mix angular acceptance and is NOT the primary apples-to-apples result.
- **Model-only Born total support partition:** ~68.8951% of the all-angle full-W Born K occurs below W=800 MeV (total from ROT012 9.097617621183627e−10). Does NOT imply physically real pion reaction partition.

## 4. Scientific falsifier and prior-art correction

The implication **"Belle W=0.8–1.5GeV source is likely complete enough for this R68 kernel because it includes a high-statistics measured charged-pion signal"** is NOT warranted: a directly source-matched physically motivated Born alternative assigns comparable kernel mass to the completely omitted **W<0.8GeV** interval at IDENTICAL angular acceptance.

This is a strong *model-support* test, but not a proof the true low-W hadronic rate is ≥ Born. As Dai/Pennington (2014) and Klevansky et al (2025) show, pion final-state interactions, analyticity/unitarity and resonance amplitudes can modify/interfere with the Born term. The 1990 Mark II experimental rows or a source-pinned dispersive amplitude are required to substitute the model low-W curve by measured/qualified hadronic source. Nothing here computes the full outside-Belle daughter neutrino distribution or eta from ROT003; **do NOT substitute Born source rate ratio for daughter event fraction**. Full pion electromagnetic/hadronic medium transport and PBH/BBN remain unmodeled.

The immediate source-native next discriminator is unusually precise: read **HEPData Mark II ins304882 Table1/2**, or original **MARKII_1990_I304882.yoda.gz** with verified package/archive SHA; inspect W,z bins and units and errors, impose same angular cut, and independently integrate 350..800MeV against H(W). If bytes stay inaccessible, the correct owner-bound status is **MARKII_NATIVE_SOURCE_ACCESS_HOLD**, not automatically another synthetic bound or unapproved task cascade. Existing original Dai–Pennington 2014 coupled-channel amplitude can serve only with actual numeric amplitude representation and stated fit uncertainties, not by reading an abstract or digitizing graph without disclosure.

## 5. Reproducibility and custody

Full standalone script in originating deliverable `DAX9_ROT004_MarkII_lowW_Born_source_audit_repro.zip`, including SciPy+NumPy executed code, JSON result, README and SHA256 manifest. Clean repeated execution byte-identical results JSON PASS, ZIP CRC PASS, all three manifest member SHA256 PASS. Local ZIP SHA256 **8f486a1378ca0dac6637add772709b91b8cd9f9085f4339ed196fa1314d458ad**. No Mark II original YODA included, and the package is not falsely represented as primary Mark II source data.

BW ingestion for DAX8 ROT028–031 was already independently checked by KN15 and unresolved as source-only receipt; do not issue a duplicate KN15 request. ROT004 is GITHUB_PUBLIC_PENDING_BW, not KN or referee acceptance. No claim of original QED novelty.

**RETURN: MARKII_1990_PRIMARY_PAPER_AND_HEPDATA_TWO_TABLE_LOCATOR_PASS / MARKII_RIVET_VALIDATED_FIDUCIAL_SOURCE_CODE_READ / POINT_BORN_SAME_FID_LOW_W_CONTRIBUTION_MATERIAL / INDEPENDENT_QUADRATURE_AND_PREDECESSOR_REPRO_PASS / MARKII_NATIVE_NUMERIC_BYTES_NOT_READ / NO_PHYSICAL_HADRONIC_RATE_OR_DAUGHTER_ETA / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY.**
