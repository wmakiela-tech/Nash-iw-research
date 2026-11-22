---
artifact_id: IW_DAX_S9_ROT024_MARKII_INDEPENDENT_BELLE_ANGULAR_SHAPE_HOLDOUT_AND_ERROR_PROVENANCE_GATE_001_20261122
date: 2026-11-22
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
exposure: PUBLIC
sync_state: GITHUB_REPORT_ONLY_PENDING_BW_INGEST
result_class: ORIGINAL_MARKII_1990_EXPERIMENT_INDEPENDENT_CONTROL / TRUE_SIX_BIN_QUARTIC_PRIMAL_DUAL / ERROR_PROVENANCE_TYPE_GUARD
claim_ceiling: NO_PRIMARY_HEPDATA_NATIVE_BYTES / NO_ORIGINAL_EXP_COVARIANCE / NO_JOINT_PVALUE_OR_CHI2 / NO_TRUE_AMP_FIT / NO_NEUTRINO_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX9 ROT024 — Original Mark II independent charged-pion angular holdout versus Belle and statistical-v-total error source guard

**22 Nov 2026.** Bounded source-first independent detector/control study after DAX9 ROT021–023. Historical prior art in 2014 Dai–Pennington already identified the unusual Belle high-angle source central behavior around W=0.8–0.9GeV and discussed possible incomplete muon/pion separation without proving cause. DAX9 ROT009 already quantified six-bin INTEREXPERIMENT TV. ROT024 adds independent Mark II *original author Table IV*, source-exact coarse six-bin quartic S+D0+D2 LP/dual checks and an explicit statistical-only versus YODA-total-error receipt. Not firstness physics claim.

## Authentic sources actually inspected

1. **J. Boyer et al, Mark II Collaboration**, *Two-photon production of pion pairs*, PRD42 (1990) 1350, DOI https://doi.org/10.1103/PhysRevD.42.1350 , full primary paper text https://escholarship.org/content/qt0vx433mf/qt0vx433mf.pdf directly read using web original PDF source, Table IV and original separate angular detector efficiency discussion. Table IV publishes 6 angular **partial cross sections nb per 0.1-wide cos bin** per 100MeV W, and **ONLY STATISTICAL uncertainties**. All 36 author-printed native central values from 0.85 to 1.45GeV were independently transcribed and compared to actual official-secondary YODA: **36/36 identical PASS**. Source PDF screenshot attempted twice but web screenshot CACHE MISS, so NO visual-PDF inspection or native PDF-byte identity is claimed.
2. **T. Mori et al, Belle Collaboration**, JPSJ76 074102 (2007), DOI https://doi.org/10.1143/JPSJ.76.074102 , primary original https://arxiv.org/abs/0704.3538 ; source has unpolarized ordinary S+D0+D2 angular form, and original author already noted possible large-angle angular-source systematic. The raw experimental HEPData native export, detector response and angular systematic covariance are not possessed.
3. **AUTHENTIC PACKAGED SECONDARY official Rivet reference bytes** SHA256 reread: MarkII_1990_I304882.yoda.gz SHA256 ff9a573f34b469ef76b145913506dfa20774243332772c1f7ba2c31b8422986d (2,237 bytes), and BELLE_2007_I749358.yoda.gz SHA256 28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403 (29,215 bytes). Belle angular source stores **DENSITY nb per UNIT |cosθ|**, multiply each 0.05 native angular bin once by 0.05. Mark II stores **partial nb per already-integrated 0.1 bin**, no factor 0.1. These authentic bytes are still SECONDARY, not experiment's original HEPData event/covariance.
4. The Mark II secondary YODA publishes one blank error label with totalDn,totalUp fields; those numerical errors **are not Table IV original stat-only numbers**. In the source W=.85..95 band, original author Table IV **stat** errors nb = (0.9,1.0,1.2,1.3,1.5,1.8); official packaged YODA total errors nb = (1.431352,1.491052,1.580772,1.632228,1.733039,2.004476). They MUST NOT be conflated. Original paper also documents ~5% angular-dependent efficiency systematic when |cosθ|>.5; experiment full nuisance matrix not reconstructed.

## Source-exact equal W/angle supports and controls

Six published Mark II full W bands: [.85,.95], [.95,1.05], [1.05,1.15], [1.15,1.25], [1.25,1.35], [1.35,1.45] GeV. Do not invent within-100MeV Mark II energy spectrum. In each W band, Belle **twenty native 5MeV bins × twelve native 0.05 angle densities**, summed in pairs to EXACTLY the six original Mark II 0.1 angle bins, z=|cosθ*| in [0,.6]. Original previous source-conditional positive R68 Planck W kernel **unchanged**, Eγ=1,436,554MeV and T=.07818527068831995MeV. Independent FLAT Belle W-bin weighting control also executed. The support is matched, but the true within-band Mark II events have UNKNOWN W distribution; this is not event-level identical reweighting. Belle flat-W versus R68 difference in original W=.85–.95 high-z fraction is only **0.06661049 percentage points** (within this reconstructed source object).

## New exact LP primal/dual source central quartic test

The author published ordinary unpolarized spin J≤2 class with S,D0,D2 gives I(z)=|S Y00 + D0 Y20|²+|D2Y22|²=a+b z²+c z⁴. For 6 EXACT 0.1-wide angular bins, G_jk = integral over bin j of z^(2k)dz, k=0,1,2. Normalize experimental six-bin source central probabilities p_j and minimize TV6=.5 sum_j |p_j−(Gθ)_j| subject to sum (Gθ)_j=1 and (Gθ)_j≥0. An INDEPENDENT LP dual with |λ_j|≤1 and Gᵀ(λ−μ1)=0 gives the SHARP lower certificate .5(λ·p−μ). Primal vs dual <1e−12 in ALL **18** variants (6 W × MarkII/Belle R68/Belle flat). Independent pure Python standard-library verifier reconstructs every moment, source auth SHA, actual author 36/36 centres, LP dual and conditional formula without NumPy/SciPy.

In W=.85–.95 original MarkII and Belle relaxed LP optimum quartics each have a>0,c>0,4ac−b²>0, hence EXACT physically acceptable complex **S+D0, D2=0** squares |u+v z²|² with no optimization slack; for THIS W band the TV minimum is sharp over actual ordinary angular wave-class. Caution: Mark II optimum for W=.95–1.05, 1.15–1.25, 1.25–1.35, 1.35–1.45 is **not verified as physically attainable**. Those numbers below are merely relaxed polynomial lower bounds, not a full unconstrained physical amplitude fit. Belle all W cases had explicit S+D0 witnesses.

| W GeV | Mark II 6-bin relaxed min TV | Belle 6-bin relaxed min TV | Mark II ↔ Belle central TV | Belle−MarkII high z=.4..6 (pp) |
|:--|--:|--:|--:|--:|
| .85–.95 | **0.715121%** | **1.855650%** | **10.279315%** | **+10.279315** |
| .95–1.05 | .500303% | 1.347188% | 3.664141% | +2.931301 |
| 1.05–1.15 | 1.906183% | .564849% | 3.273372% | +.314151 |
| 1.15–1.25 | .761341% | .439316% | 2.575733% | −.918733 |
| 1.25–1.35 | 1.549847% | .341679% | 3.209324% | −2.007237 |
| 1.35–1.45 | 3.509286% | .268490% | 7.201826% | +6.495386 |

At .85–.95GeV original Mark II printed source central nb=(15.9,15.8,14.7,14.1,12.4,12.6), sum 85.5nb; Mark II high angle .4–.6 fraction **29.23976608%**, Belle source R68-weighted **39.51908125%**; central interexperiment 6-bin TV **10.279315%** independently reproduces DAX9 ROT009. Belle original 12×.05 resolution source minimal TV=4.4806145% (ROT017 W=.85–.95); coarse six×.1 low resolution TV=1.85565%. Do NOT compare source-central TV across angular bin resolutions as though identical data likelihood.

## Source-type conditional statistical-only comparison, NOT a joint experiment test

Original Mark II author Table IV first-band stat-only errors .9,1.0,1.2,1.3,1.5,1.8 nb. In a **DELIBERATELY NONPHYSICAL conditional exercise**: hold Belle published central six-bin fractions exactly fixed without ANY Belle uncertainty, assume Mark II six reported STAT errors are mutually independent Gaussian, fit only one normalization α to Mark II original six measured angular nb. Explicit analytic weighted least squares gives **χ²_conditional = 30.31504718** at 5 nominal degrees of freedom and α=**90.61273701 nb**. If instead the *distinct secondary YODA total* error numbers are incorrectly treated as independent Gaussian, χ² changes to **20.16079199**. THESE ARE NOT combined MarkII/Belle χ², p-values or real experimental significances. Belle angular systematic and statistical covariance, Mark II efficiency and global errors, and Mark II within-bin W distribution remain unknown. Under the equally conditional independent original MarkII *stat* assumption, delta-method high-z fraction SD=**2.08279 percentage points**, NOT a two-experiment confidence interval. No causality of lepton-background or hadronic resonances inferred.

## Repro, custody, research ceiling

Local complete ORIGINAL executable archive in originating user chat: **DAX9_ROT024_MarkII_Belle_Independent_Quartic_Holdout_Repro.zip** 58,669 bytes, SHA256 **9975fbec12b76728490756b10cff23cf6b9115d9cc034114e2e251b5d2066ffb**, ZIP CRC PASS, **13/13 source+report+code+outputs member SHA PASS**, 15 ZIP members including hash manifest. Two fresh independent temp directories each complete execution of main Python+separate pure standard-library verifier PASS, frozen JSON+2 CSV **2×3/3 byte-identical PASS**. Original Mark II TableIV 36/36 central values and native source two compressed SHA inputs repeatedly checked, 18/18 primal-dual pair PASS. THIS GitHub Markdown is the science REPORT ONLY, not hosted source ZIP, and no BW ingestion is inferred.

Disposition: independent original MarkII controlled central shape does NOT show Belle high angle rise at .85–.95GeV, but the observation is mature prior art and cannot be promoted to statistical experimental conflict with absent correlated angular nuisance and original measurement uncertainty. Next scientifically material gate: source-native original correlated detector response or independent non-recycled higher-resolution angular measurement or a transparent fitted multichannel S,D0,D2 amplitude with experimental nuisance covariance. No further artificial marginal uncertainty-box proliferation.

**RETURN: ORIGINAL_MARKII_AUTHOR_TABLE_IV_36OF36_PASS / AUTHENTIC_SECONDARY_TWO_SHA_PASS / EXACT_COMMON_6ANGLE_W_BANDS_PASS / 18OF18_PRIMAL_DUAL_PASS / FIRST_W_PHYSICAL_S_D0_ATTAINABILITY_PASS / PRIMARY_STAT_VS_SECONDARY_TOTAL_ERROR_GUARD_PASS / REAL_JOINT_EXP_LIKELIHOOD_HOLD / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.**