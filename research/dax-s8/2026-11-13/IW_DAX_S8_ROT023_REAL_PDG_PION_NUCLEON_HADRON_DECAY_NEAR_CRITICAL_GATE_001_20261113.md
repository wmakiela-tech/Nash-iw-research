---
artifact_id: IW_DAX_S8_ROT023_REAL_PDG_PION_NUCLEON_HADRON_DECAY_NEAR_CRITICAL_GATE_001_20261113
created_at: 2026-11-13
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
document_type: SCIENTIFIC_RETURN
exposure: PUBLIC
result_class: PDG_COMPAS_FOUR_ORIGINAL_NUMERIC_FILES / FREE_NUCLEON_DECAY_FIRST_EVENT_CRITICAL_SIGMA / DIRECT_VS_INFERRED_PROVENANCE_REPAIR
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_MEASURED_PIN_AT_718GEV / NO_BBN_FREE_NUCLEON_FRACTION / NO_NUCLEAR_TRANSPORT / NO_PION_INELASTIC_ENERGY_MAP / NO_ESCAPED_NEUTRINO_OR_PBH_BBN / NO_NOVELTY_INFERENCE / NO_CANON / NO_EXEC_SIGN
---

# DAX-S8 ROT023 — original PDG/COMPAS charged-pion nucleon data, hadronic first encounter vs free decay in R68

13 November 2026. FIRST in this DAX-S8 R68 lineage to move independently beyond scalar-Born pion-photon proxies and use original numeric pion–nucleon hadronic source data. Classical rate threshold, not a new physical Standard Model prediction or cosmic PBH/BBN constraint.

## Source native receipt

Native Ubuntu GitHub Actions 43464338879 (SUCCESS): https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43464338879 . Four original HTTP200 files from Particle Data Group COMPAS source index https://pdg.lbl.gov/2024/hadronic-xsections/ . Original raw artifact ID 14057731215, ZIP SHA256 afe9074d08a7ec9a994b6b2c98f81fb5dcad5733c93ec6d1869abcc9a7c7b9ce. File hashes:

- pi-p total (605 records): fa5bc4b5a1efbc80b0f258b7e16a97f8795b803143ca60ca93fd398a187576b3
- pi+p total (428 records): 439a76fe69ecfc13ac624ae7e0c77be31b1915620b2433140a654b16d2e4031a
- pi-p elastic (277 records): 5f9af000adc836c11a905adb9e43b41537ed77282ff37963ae6f6bce0bf3406f
- pi+p elastic (129 records): e068a871cc329be780ce1023ad9a98419c94b31222f6e3f7b9d509daef69cd11

Source negative control: header of pi+p total says 412 points but complete ORIGINAL .dat contains 428 numbered rows. The 16 appended later entries include PETROV 2010, RYUTIN 2017, KHOZE_VA 2017, not automatically directly measured pi+p at the energy of interest. Exact primary source bytes have been preserved, not silently truncated or reclassified.

## Original experimental provenance and two indispensable distinctions

1. Carroll et al, Phys Lett B80 (1979) p423, DOI https://doi.org/10.1016/0370-2693(79)91205-X , original paper https://www.mv.helsinki.fi/home/osterber/files/low_energy_sigmatot/Carroll_PL_80B_1979.pdf . DIRECT pi+p and pi-p total at the SAME momentum 340GeV/c: 24.62 +/-0.14 mb and 25.08 +/-0.08 mb. Their charge-average 24.85mb is measured at 340GeV/c, NOT at R68.
2. Firestone et al, Phys Rev D14 (1976) 2902, DOI https://doi.org/10.1103/PhysRevD.14.2902 . DIRECT same-experiment pi-p at 360GeV/c: total 25.25 +/-0.35mb, elastic 3.61 +/-0.11mb, hence nonelastic 21.64mb. This nonelastic remainder does NOT equal pion destruction, and no covariance uncertainty for difference is claimed.
3. Dersch et al/SELEX, Nucl Phys B579 (2000) p277, https://arxiv.org/abs/hep-ex/9910052 . 27.1 +/-1.5mb for pi- nucleon at 640GeV/c is INFERRED from pion-NUCLEUS measurements and ratio modeling, NOT direct pi-p on free proton despite compiled heading. Their combined 26.6 +/-0.9mb at ~610GeV/c is likewise inferred.
4. At R68 mean pion p_lab=718.277GeV/c (sqrt(s_pi p) about 36.726GeV for stationary proton), NO DIRECT original sigma(pi+ p,pi- p) measurements at exactly 718GeV/c were read. Direct pi+p reliable source coverage here ends at 340GeV/c, whereas even the pi- 640GeV/c number is nuclear-derived. No source-native 718GeV/c cross-section interpolation is claimed.

## Exact R68 free-nucleon first-event threshold

Source PDG 2025 Big Bang Nucleosynthesis https://pdg.lbl.gov/2025/reviews/rpp2025-rev-bbang-nucleosynthesis.pdf gives cosmic baryon-to-photon eta=(6.12 +/-0.04)e-10. In inherited R68 ideal Planck bath T=0.07818527068831995MeV, n_gamma=1.5152025724753423e28cm^-3, baryon NUMBER density n_b=9.2730397435490948e18cm^-3. This is NOT automatically FREE proton+neutron target density while primordial nuclei form.

Inherited ROT020 actual Belle/Rivet source-conditional MEAN pion energy E_pi=718277.144397855197MeV, pion m=139.57039MeV, c*tau=7.8045m: gamma=5146.3433210859065, beta near one, vacuum mean decay flight ell_dec=40.1646356911581km. Let f_free in [0,1] be BARYON NUMBER fraction in free nucleons, and assume stationary target nucleons plus an energy-fixed effective total piN cross section sigma (mb) governing the FIRST encounter independently of vacuum decay. Then

Gamma(piN)/Gamma(decay) = n_b*f_free*sigma*ell_dec,
P(decay BEFORE first piN encounter) = 1/[1+n_b*f_free*sigma*ell_dec].

When f_free=1, FIRST collision/decay equality occurs at exactly
sigma_critical = 1/(n_b ell_dec) = 26.8493667231222182746 mb.
PDG eta error +/-0.04e-10 alone gives [26.67502018596,27.02600729367]mb. For f_free>0, threshold is 26.8493667/f_free mb. Bound nuclei contribute DIFFERENT pion-nucleus reactions not addressed here; f_free<1 is NOT an upper bound on all hadronic interactions.

Strictly HYPOTHETICAL SOURCE-ANCHORED fixed-cross-section variants at 718GeV (all from measurements at OTHER momenta, or arbitrary chosen):

| sigma_eff (mb) | external source at other momentum | f_free | first piN MFP km | P decay-before-piN |
|---|---|---|---|---|
| 24.85 | Carroll DIRECT pi+ and pi- p charge mean at 340GeV/c | 1 | 43.396 | 0.519336 |
| 25.00 | rounded scenario | 1 | 43.136 | 0.517834 |
| 27.10 | Dersch NUCLEAR-DERIVED pi-N 640GeV/c | 1 | 39.793 | 0.497677 |
| 21.64 | Firestone DIRECT pi-p 360GeV/c NONELASTIC=total-elastic | 1 | 49.833 | 0.553717 |
| 25.00 | rounded scenario | 0.5 | 86.272 | 0.682333 |
| 25.00 | rounded scenario | 0.25 | 172.543 | 0.811175 |

Empirical/inferred source scales at different beam momenta STRADDLE sigma_critical, but whether the TRUE R68 hadronic first encounter dominates free decay remains UNKNOWN. Source total sigma includes elastic; none of these numbers yields absorption, final pion spectrum, or escaped neutrino flux.

Conditional source-charge identity: for initial equal pi+ and pi- pair with equal fixed energy on a mixture of FREE p/n, strong isospin approx sigma(pi+n)=sigma(pi-p), sigma(pi-n)=sigma(pi+p) makes the charge-averaged total (sigma_pi+p+sigma_pi-p)/2 independent of initial proton fraction. Fails for bound nuclei, isospin/QED breaking or subsequent charge/energy changes; does not determine sigma at R68.

Auxiliary FIRST three-clock source check at sigma=25mb, f_free=1 and earlier POINT-SCALAR RESTRICTED low-rest-photon Compton mean free path 479.365m (ROT021): P(first soft gamma)=0.9774713, P(first piN)=0.0108626, P(first decay)=0.0116661. Not a physical cascade: pion survives elastic scatter and rate changes; pion may survive hadronic event or generate secondaries.

## Original scientific source negative knowledge and reproduction

Independent author source-data-verified algorithms: 52-digit mpmath and independently coded stdlib-only regex parsing/floating precision both re-read FOUR original SHA-pinned source files, accurately recover Carroll charge mean 24.85mb, Firestone nonelastic 21.64mb, SELEX indirect 27.1mb and same threshold sigma_critical to ~1e-15 relative. Full ORIGINAL local ROT023 ZIP stores all 4 raw .dat files, native Action original artifact, source receipt, inherited ROT020 frozen source result, two programs, two frozen JSON outputs, one scenario CSV, science report, audit and SHA manifest. ZIP CRC PASS / 18 of 18 original member SHA256 PASS / independent clean-extract replay of both programs and CSV produces 3 byte-identical data outputs PASS. ZIP SHA256 1fa1b6c17900582a51151f269423e8d872235138813f5d80b1af8de719090dd2. This is author reproduction, not independent external audit.

Source-typed open science: no source-proven piN total at R68 718GeV; unknown free nucleon fraction, nuclei, actual pion LAB energy distribution and thermal baryon motion, charge exchange, true inelastic final-state transfer, repeated collision/decay with changing energy, pion/muon decay and neutrino transport. No PBH/BBN physical bound or novel physics. XH-S6 no task assignment. KN13 BW native ingestion not verified; GITHUB_PENDING_BW_INGEST. NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.

DISPOSITION: ORIGINAL_PDG_COMPAS_FOUR_FILE_SOURCE_PASS / DIRECT_VS_INFERRED_PROVENANCE_REPAIRED / NEAR_CRITICAL_FREE_NUCLEON_FIRST_EVENT_PASS / TRUE_HADRONIC_R68_RATE_OPEN / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.
