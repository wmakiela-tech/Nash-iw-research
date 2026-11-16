---
artifact_id: IW_DAX_S8_ROT031_BELLE_ANGULAR_BIN_SUPPORT_RARE_NEUTRINO_TAIL_ROBUSTNESS_001_20261116
date: 2026-11-16
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
exposure: PUBLIC
bw: GITHUB_PENDING_BW_INGEST
class: ORIGINAL_RIVET_BELLE_140x12_SOURCE_ANGULAR_BIN_ADVERSARIAL_SUPPORT / FULL_NONHEADON_PLANCK / RARE_FIRST_NEUTRINO_E2_TAIL_SENSITIVITY
ceiling: NO_PRIMARY_HEPDATA_BYTE_EQUALITY / NO_SOURCE_ORIGINAL_BIN_SEMANTICS_OR_COVARIANCES / NO_COMPLETE_IN_MEDIUM_PION_STOPPING / NO_FULL_BBN_OR_PBH_NEUTRINO_PHYSICS / NO_NOVELTY_INFERENCE / NO_CANON / NO_EXEC_SIGN
---

# DAX-S8 ROT031 — original Belle fiducial angular-bin adversarial source control of rare first-neutrino second moment

**16 November 2026.** FIRST in this DAX-S8 R68 line to adversarially control the intra-angular-bin placement of 140x12 actual SECONDARY Rivet/Belle reference numerical data in the conditional first pion neutrino energy spectrum model. Mathematical/QED prior art is established; NO novel particle-physics claim or a real cosmological neutrino spectrum.

## Scientific precedence and material new question

DAX-S7 R68 original strictly 3 named gamma-gamma first-event source channels. DAX-S8 ROT017 first retrieved 140 W x12 |cos(theta*)| actual packaged Belle numerical sources; ROT019 real pion LAB energy second moment; ROT020 free-pion first-neutrino energy moments conditional on no collisions; ROT024 massive ideal FD e± bath; ROT026–027 chosen t-channel point-scalar one-photon πe± HARD Q² in [.001,.010]GeV² and its energy-updating restricted CSDA/500+200 discrete histories; ROT028 source-folded initial pion decay Jensen +13.014% while local πe loss changed ~-.07%; ROT029 full-source CSDA descendant median ~1.78244GeV and common-threshold transport factorization; ROT030 found conditional P(E_nu>10GeV)~.001887 but that tiny tail supplies ~97.94% of E_nu² and full source E2=13.40716117GeV² versus same source-mean initial E pion second moment 12.18357012GeV². ROT031 asks IF rare-tail effect can be explained by a hidden arbitrary uniform-z-bin distribution assumption, keeping the actual source each W/z BIN WEIGHT fixed. It can NOT: within defined model the rare-tail result persists under adversarial placements.

## Exact source receipt / not primary HEPData

Belle Mori et al 2007 JPSJ 76 074102 DOI https://doi.org/10.1143/JPSJ.76.074102 ; original arXiv https://arxiv.org/abs/0704.3538 ; official validated Rivet https://heprivet.org/analyses/BELLE_2007_I749358/ . Actually re-read and SHA-verified ORIGINAL SECONDARY packaged numerical YODA file **BELLE_2007_I749358.yoda.gz SHA256 28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403**, acquired original native ROT017 Actions https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43309487872 . 141 tables, 140 energy W in [.8,1.5]GeV x12 |z| COM [0,.6]. Full ZIP delivered in this chat includes this actual YODA, not synthetic source values.

**SOURCE LIMITS**: exact original HEPData primary numerical BYTE EQUALITY NOT established; 5MeV W and 0.05 z source entries modeled as BIN AVERAGES, not independently certified by original data. Experimental bin errors/covariance and off-W,z-fiducial pion production are unverified. All angular endpoint sensitivity results conditional on positive source values at their fixed W/z bin weights and this original numerical-source semantics.

## Exact mathematical model used, not complete medium plasma

Inherited R68 E_gamma=1436554MeV; ideal isotropic Planck bath T=.07818527068831995MeV, charged pion M=.13957039GeV, vacuum cτ=780.45cm, m_mu=.1056583755GeV. Ideal e± FD thermal bath original ROT024. Charged pion hard πe elastic loss uses original author chosen point-scalar VACUUM one-photon selected momentum transfer Q² in [.001,.010]GeV² only. This is NOT dynamic soft+hard finite-T matched physical pion stopping.

For pion with initial LAB energy E0, the restricted CSDA model obeys dE/dell=-b(E) and pion vacuum decay κ(E)=M/[cτ sqrt(E²−M²)]. Let h(E)=κ(E)/b(E), H'=h; survival S(E|E0)=exp[H(E)−H(E0)] for E≤E0, and daughter pion decay-energy density h(E)S(E|E0). For exact ideal free two-body scalar pion decay, f=(M²−m_mu²)/(2M²), p=sqrt(E²−M²), neutrino LAB energy f(E+p cosψ), cosψ uniform[-1,1]. Hence local neutrino second moment f²(4E²−M²)/3 and local contribution from Eν>t:
[(f(E+p))³−max(t,f(E−p))³]_+/(6 f p).
These are standard kinematics.

Method A independently re-parses all original source YODA data and integrates W with Gauss8. For EACH 0.05 angular source bin, preserving its fixed positive integral, select all weight at LEFT edge, CENTRE, RIGHT edge, or UNIFORM Gauss8. Evaluate a new 7501-point energy-dependent hard πe+decay CSDA kernel. HEADON pooled pion energies Eπ±=Eγ/2*(1±β_pi(W) z), βpi=sqrt(1−4M²/W²); the mean pooled Eπ does not change under angular re-placement.

Method B independently re-parses and integrates EXACT NONHEADON Planck geometry: W²=4Eγ T x u, u=(1−cosθ_inc)/2; pion energies Eπ±=(Eγ+T x ± βpi[(Eγ−T x)z+sqrt(4Eγ T x(1−u))*sqrt(1−z²)cosφ])/2 (units consistently MeV). Gauss4 W, Gauss4 z uniform, Laguerre12 photon x, 6 azimuth φ, 7501 energy-dependent πe CSDA grid. An 8W×8z×12001-E denser source model variation is run separately. Unlike a mistaken preliminary calculation, all thermal photon weights are normalized by their ACTUAL finite quadrature sum, and charge pooled source mean reverts to 718.27714439787GeV.

Method C: all 140 original W-centres and 121 z grid positions each, 12 Planck x and 12 azimuth angles. All **16,800 second-moment finite differences** positive for Eν², Eν² restricted >10GeV and >100GeV. All 16,800 tail-probability z differences negative for P(Eν>10) and P(Eν>100). This is a **FINITE NUMERICAL GRID MONOTONICITY TEST**, NOT a strict continuous analytic or interval-arithmetic proof.

Method D: independent 140-row per-W source table reproduces weighted headon source aggregate within ~1e-13. Strict original secondary YODA hash/141 object audit and original angular cross-section per-W closure at <6.1e−5 relative to rounded source table.

## New numeric results (source model conditional)

| assumed intra-z placement | headon second neutrino energy moment [GeV²] | FULL NONHEADON [GeV²] | fraction of E2 above10GeV | P(Eν>10GeV) |
| --- | ---: | ---: | ---: | ---: |
| ALL source mass at z-left | 13.2552776375 | **13.2552831751** | 97.9147% | 0.1892436% |
| MIDPOINT source mass | 13.4048665836 | not executed nonheadon | 97.9381% | 0.1887113% |
| UNIFORM inside each source angular bin | 13.4071559031 | **13.4071612048** | 97.9384% | 0.1887016% |
| ALL source mass at z-right | 13.5681911353 | **13.5681963656** | 97.9630% | 0.1881204% |

Original ROT030 full nonheadon uniform E2=**13.4071611702GeV²**; new independently coded full geometry baseline differs by only **3.46e−8GeV²**. Denser 8W×8z×12001E obtains 13.4071609775, a 2.27e−7GeV² shift from 4W×4z×7501E. No measured experimental confidence claim.

Relative to ROT030 fixed **source-mean** starting pion, Eν² one-mean=**12.1835701169GeV²**: the source E2 positive uplift is **+8.796%** with source mass z-left, **+10.043%** uniform, **+11.365%** z-right. Consequently the qualitative original +10% source-ensemble uplift is NOT eliminated by these strong within-angular-bin source-data rearrangements. Every full-nonheadon placement preserves starting pion source-ensemble mean 718.27714439787GeV from charge pooling.

>100GeV daughter neutrinos contribute 76.184%,76.569%,76.972% of Eν² in z-left,uniform,z-right scenarios respectively; P(Eν>100GeV) ~0.03290%, 0.03278%, 0.03265%. Thus energy-squared tail is highly sensitive to very RARE parent decays while median and mean need not be.

**CONSERVATIVE NUMERIC conditional robustness ratio**: MIN second-moment contribution from >10GeV over all assessed angular endpoint source placements 12.97887278GeV² and MAX total second moment 13.56819637GeV² give 12.97887278/13.56819637=**95.6566%**. Under numerically stressed monotonicity of both numerator and denominator, this is a deliberately LOOSE lower envelope for any within-z-bin redistribution of the fixed source weights. Not a formal universal interval theorem, not a 95% experimental CI, not a QCD physical bound. Each directly executed placement yields ~97.9% share.

## Reproduction, original negative knowledge, and scientific stop

Full local 25-member original package includes actual original 29,215B YODA; inherited ROT029 source kernel; original ROT030 frozen first-neutrino JSON and independent headon receipt; actual ROT020/ROT024 inputs; 6 executed author-written Python scripts; 6 frozen resulting JSON/CSV including 140 W-source rows; extended science report, README, source audit, environment, manifest and clean replay verifier. ZIP CRC PASS, SHA256 **24/24 PASS**, fresh temp-directory reexecution of SIX original scripts generates SIX frozen result files **BYTE-IDENTICAL PASS**, and original ROT030 benchmark replay comparisons PASS. ZIP SHA256 **e3454db4123ad968f821016226ba32f4c7f5fd72c2676a7e66ddb399023ad4f6**.

Original author-detected failures: initial tuple-unpacking and z-weight initialization mistakes failed immediately; most materially, a first full nonheadon method assumed finite 12 Laguerre-x photon weights sum EXACTLY to 1, yielding erroneous source mean 718.277075 instead of 718.2771444GeV. Fixed finite quadrature denominator to the actual sum; this source moment now recovers correct 718.27714439787GeV. No old incorrect runs promoted.

PHYSICAL NO-GO: source excludes W and angle outside Belle acceptance; source-data experimental covariance/primary bytes not established, point-pion Fpi=1 and arbitrary hard Q² range are NOT full real thermal πe electromagnetic stopping. Remaining finite-T dynamic screening and soft/hard matching, πγ and πN/piA strong channels, original BBN nuclei/temperature evolution, discrete multi-channel charged pion transport, muon decay, neutrino propagation and actual PBH/BBN all OPEN. No external referee approval or KN13 BW ingestion receipt. GITHUB_PENDING_BW_INGEST. NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.

**RETURN: ROT031_BELLE_ANGULAR_BIN_MODEL_ROBUSTNESS_PASS / RARE_NEUTRINO_E2_TAIL_PERSISTS_NUMERICALLY / NO_EXPERIMENTAL_CI_OR_FORMAL_CONTINUOUS_INTERVAL_PROOF / FULL_PHYSICAL_TRANSPORT_OPEN / GITHUB_PENDING_BW_INGEST / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.**
