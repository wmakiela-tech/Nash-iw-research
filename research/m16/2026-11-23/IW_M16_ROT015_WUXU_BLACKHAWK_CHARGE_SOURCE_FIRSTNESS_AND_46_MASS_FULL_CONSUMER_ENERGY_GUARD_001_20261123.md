---
artifact_id: IW_M16_ROT015_WUXU_BLACKHAWK_CHARGE_SOURCE_FIRSTNESS_AND_46_MASS_FULL_CONSUMER_ENERGY_GUARD_001_20261123
cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_11 / M16
date: 2026-11-23 Europe/Warsaw
authorization: Moderator "Sam prowadź prace zamiast czekać na badacza"
type: INDEPENDENT_SOURCE_BOUND_FIRSTNESS_AND_CONSUMER_AUDIT
status: ORIGINAL_WUXU_NOTEBOOK_ACTUALLY_READ / BADACZ_REVIEW122_AND_PREREG121_ACTUALLY_READ / FIRSTNESS_CORRECTED / ORIGINAL_C_CONSUMER_AND_HIGGS_SOURCE_READ / 46_46_RECOMBINATION_ACTUALLY_EXECUTED_V8
claim_ceiling: NO_ORIGINAL_CHARGE_FINDING_BY_M16 / NO_ORIGINAL_HIGGS_FINDING_BY_M16 / NO_RAW_SECONDARY_ENERGY_TABLE_INDEPENDENT_REPLAY / NO_NATIVE_JULIA / NO_PBH_BOUND / NO_AUTHOR_ERROR_ESTABLISHED / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_NOT_WRITTEN
---

# ROT015: independent BlackHawk/Wu–Xu source-consumer energy check and mandatory priority correction

## A. Firstness correction — prior original source and actual native test

M16 initially characterized the charge-conjugate source-column mismatch as newly detected, but full NASH currentness and earlier source reports establish PRIORITY elsewhere. MT14 ROT022 1 Nov 2026 (source-literature conditional charge gate), BADACZ 2 Nov 2026 PREREG043 T1/T2 source PYTHIA 100×5 verification and native paired B_sym tests, subsequent SCOPE11/PRF13/INT9/KN14 15 Nov. BADACZ verified pi±, K±, p+pbar, n+nbar are combined species columns and K0L is the neutral anchor, and found under specific native counterfactual +0.27...+0.30 dex beta shifts. M16 does NOT claim discovery, source-firstness, novel beta result, or first physical test.

Original Badacz Slack 2 November:
https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1793615741021849

Current source-firstness: BADACZ PREREG121 Git blob b447de56620bd310143e8fd40498b769da6de556, native REVIEW122 Git blob efbfd2e7f6ed0e44bdb4c637c7e99d4bb79dbdc5 actually read FULL, released mass-level POSTHOC_121 machine JSON blob 4bb27a3271de1331ecef73ae629021c7b188a97b also actually read. 
https://github.com/wmakiela-tech/Nash-iw-research/blob/7ea5b91/research/badacz/2026-11-23/IW_BADACZ_B1_GEC_B_ENERGY_LEDGER_REVIEW_122_20261123.md

DAX-S10 ROT007 23 Nov first independently obtained byte-identified full BlackHawk2.3 fM mirror (source SHA256 5baaac375e5848584ec6cc852aeacc28edc4de3528c796f6aee1dd460ad943cc) and independently confirmed 371-point R approximately .581752. Prior M16 ROT011 BH-side I1 OPEN statement is now superseded by DAX. Firstness Badacz/DAX fully preserved.
https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1795426671066539

## B. Direct original upstream source

The actual complete original Wu–Xu notebook was read through GitHub blob, not merely filename or summary: Git blob 8a10396ae771b17059808fc2b91235dd194cba8d, ~1.675MB, original repo commit d395183674cace6c9906a8911bdeb7234ba4040d:
https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/valid_hadrons_from_BlackHawk.ipynb
Cells 8/9 set BlackHawk BBN PYTHIA and primary 5..100000GeV, 100 energies. Cells 12/13 compute actual secondary spectra, then trapezoid logE of E times rate to write exactly FIVE 100-row hadron-number rates. The saved number table loses particle-by-particle ENERGY distributions; matching five total count rates alone is insufficient for G_EC+(b) energy conservation.

Original author main-scan.jl blob b368ba55d5a493f7bc185909730f7fe5691f10d6, lines 103..128: SAME qpi feeds pi+ and pi- separately, qK feeds K-, qp feeds antiproton, qn antineutron and qK0L feeds K0L. Primary full source 100×5 tabulation blob 06d0883a27b108692720422294ba2baacd381a64 actually read. Independently recomputed 100-point instantaneous aggregate Q_code=2*qpi+qK+qK0+qp+qn against charge-split conditional Q_sym=qpi+qK/2+qK0+qp/2+qn/2. For all 100 masses from 1e9 to4e12g, Q_sym/Q_code ranges 0.5128033033702232..0.5160090643312839. M16 computed conditional integrated per one isolated PBH j22 Qcode≈8.39759e29 Qsym≈4.30614e29 and j62 Qcode≈6.12814e30 Qsym≈3.14278e30; these earlier preliminary aggregate integrals interpolate the aggregate Q rather than each original q separately, so indicate approximate scaling only. NO native BBN/Yp/beta values inferred. This is an INDEPENDENT CONFIRMATION of a known NASH source problem, not novel.

Independent source mirror BlackHawk code C at cewasiuk/Spin-and-Charge-BH-Evolution commit0bd531eb948bd11549535a563b55f0d23671589b, scripts/pythia_scripts/table_gluon.cc blob b52a1b0b70f5fce78cd8692dbcb0996c663fed8f PDG ±211, ±321, ±2212, ±2112 categories each aggregated, src/secondary.c blob9b544e7e2fa2bbf0f952eaf530cf4e29c2a0de5e no split. Exact selected BlackHawk v2.3 hardtable branch identity is not independently demonstrated merely by reading this 2025 mirror.

## C. Original Higgs factor-two C mechanism independently read, but first Badacz REVIEW122

Mirror full scripts/pythia_scripts/table_higgs.cc Git blob80ce8240d8d02db4db39bc3c81c4fb46963d516b: original e+e- to Higgs Monte Carlo generator sets Beams:eCM=2*beam_energy. Mirror original scripts/pythia_scripts/formatting.c Git blobf89bf329e3316ff472b61ac4f51c23084fbb6970, line69, Higgs l==2 column does NOT divide by2 although all other columns do. BlackHawk then consumes tabulated Higgs rate as if at energy E' per one primary. This is a CONDITIONAL source mechanics explanation for owner P_T1 Higgs epsilon=2.000 across 100GeV..14TeV. Independent first source statement remains BADACZ REVIEW122: M16 source code reads support but do not prove entire original historical v2.3 prepared table binary. No priority or publication novelty claimed.

Original author-modified BlackHawk_inst.c source Git blob f517b0a71a3c994e396600ce73cb9658e440d646, source lines 628..640 explicitly call add_photons_instantaneous and add_electrons_instantaneous AFTER integrated hadronized spectra, confirmed also in independent BlackHawk mirror src/secondary.c. A predicted all-channel energy-balance ratio that omits direct additions does NOT correspond to the actual consumer.

## D. Actual independent numerical algebra on ALL owner 46 physics source mass rows

DIRECT raw BADACZ actual posthoc_121.json Git blob 4bb27a3271de1331ecef73ae629021c7b188a97b, 186162chars, accessed via GitHub fetch_blob and parsed to 100 rows with per-channel primary power_share and energy_excess_over_Ptot. Select exactly 46 physical masses 2e9≤M≤1e11g (no manufactured cells). Independent V8 JS recombined:
r_nominal = 1 + sum_channel(energy_excess / primary Ptot),
r_full = r_nominal + primary_photon_power_share + primary_electron_power_share,
because original C consumer adds direct photon and electron.
Across ALL 46 independent recombinations:
r_nominal∈[1.014584134027137,1.0243845175059103] = Badacz prereg P_M1 nominal apparent PASS,
r_full∈[1.0613968769543713,1.0712812336460438],
omitted direct photon+electron∈[0.04681140104565418,0.04689671614013347] primary power.
Max internal algebraic/source original comparison residual 3.3306690738754696e-16; all 46/46 full ratios > nominal.

This is INDEPENDENT ALGEBRA and external-original-code consumer source guard, NOT raw secondary energy spectra independent integration; original Badacz POSTHOC121 provided input power fractions and found the basic 6–7% full excess FIRST. Crucial scientific warning: P_M1 PASS cannot certify full energy conservation in actual BlackHawk consumer when observed quantity excludes material positive secondary terms. Higgs original owner posthoc primary power excess fraction at these 46 masses .017104775.. .018189060, relative hadron count Higgs contribution mean4.72%..5.46% among five channels. E_Higgs remodelling per author source result -0.7% to -1.55% across 2e9–1e11g (owner paper focused 1e9–1e10g -0.4..-0.9%). These quantitative effects derive from owner source, not separately regenerated physical PYTHIA.

Stored actually computed independent source reaggregation JSON:
https://github.com/wmakiela-tech/Nash-iw-research/blob/282b9c39cfb845bb447dad53675b3b9adf012de7/research/m16/2026-11-23/data/m16_rot015_46mass_energy_consumer_certificate.json
Owner original raw 46 values used, not copied claim prose.

Self-contained standalone JS of same mathematically independent audit with 46 source mass rows embedded, commit 3b6f8085b261f663457087e9f0f42cb8add9f0ec, blob b0eec277203fcf979b6cb099eda5d9c4692089ef, full readback to verify:
https://github.com/wmakiela-tech/Nash-iw-research/blob/3b6f8085b261f663457087e9f0f42cb8add9f0ec/research/m16/2026-11-23/code/m16_rot015_46mass_energy_consumer_recombination_independent.js
One lexical variable typo from initial GitHub write was patched by explicit sequential update. Actual numeric function executed in functions.exec V8 during this turn; separately executing saved JS using Node has NOT been performed, so no Node claim.

## E. Hard scientific scope and next source-grounded step

BADACZ PREREG121 G_NUM PASS, P_T1 FAIL, P_T2 FAIL, P_M1 PASS due incomplete pre-registered consumer then corrected. Badacz posthoc G_EC+(b) qualified: source energy 2e9..1e11g hadronic dominant generators within ~1%, Higgs and other channels have source anomalies, FULL total consumer 1.061..1.071 cannot be called global energy-consistent. Below1e9g original mass rates not tabulated, j22 81.4% per-BH hadron NUMBER relies on lowmass extrapolation (M16 ROT014), j62~11.1%. G_DEP heat deposition to single radiation fluid remains separate physically unvalidated gate.

RECOMMENDED own next active physics challenge: identify actual old-vs-current BlackHawk2.3 BBN hardtable selected runtime, energy-resolved secondary invariant and G_DEP sectoral source. If a native BBN run is attempted independently, preannounce source-only variations (f_BH mass loss, conjugate q split, Higgs energy counter-control) and freeze original solver calibration and Tnuc; do not silently overwrite BADACZ native STD_A prereg or claim new physical beta constraints.

FINAL STATUS: M16_ROT015_OWNER_FIRSTNESS_CORRECTED / ORIGINAL_WUXU_NOTEBOOK_FULL_READ / BLACKHAWK_HIGGS_F2_C_SOURCE_GUARD_I1_CONDITIONAL / ALL46_FULL_CONSUMER_RATIO_INDEPENDENT_REAGGREGATION_PASS / OWNER_REVIEW122_P_T1_FAIL_AND_P_M1_FALSE_SCOPE_PRESERVED / NO_INDEPENDENT_HADRONIZATION_SPECTRUM_RUN / NO_NEW_PHYSICAL_BBN_BOUND / NO_AUTHOR_ERROR_ESTABLISHED / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_BW_NATIVE_WRITE.
