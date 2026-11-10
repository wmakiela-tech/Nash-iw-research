---
artifact_id: IW_DAX_S8_ROT006_GAMMAGAMMA_4E_SOURCE_CONTACT_AND_OWNER_REOPEN_GATE_001_20261110
created_at: 2026-11-10
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
document_type: SCIENTIFIC_RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: SOURCE_CONTACT / EXTERNAL_PRIOR_ART / EXACT_COM_GATE / QUEUED_OWNER_ACTION_PROPOSAL
claim_ceiling: NO_NATIVE_MADGRAPH_RUN / NO_QED_OPERATOR_TRANSFER / NO_DEPOSITION / NO_PBH_BBN_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX-S8 ROT006 — gamma gamma to 4 electrons: primary-source route, source inventory and owner-reopen gate

10 November 2026. Object: two REAL incoming photons, gamma gamma -> e+e-e+e- with identical final electrons and positrons, and any downstream transport-dependent energy target. This is not gamma+nucleus Bethe-Heitler pair production, nor e+e- initial-state production. DAX-S7 R67/R68 first identified DPP rate versus differential-energy and cascade needs; DAX-S8 ROT001-005 already covered kinematic insufficiency, first-vs-eventual events, CRPropa equal-energy proxy, thinning variances, and hypothetical rate-table support. No full QED transport kernel was produced by DAX.

## Trigger: IW/NASH §9a amended 2026-11-10
Current public protocol docs/WORK_AND_REPRODUCIBILITY_PROTOCOL.md commit 745b926c27c3efb569759388151ed274620f519f requires resolving repeated source STOP through a discriminating source check or a bounded owner queue, and source code/data inventory by the fifth source-derived artifact. ROT003-005 rely on CRPropa. Focus check: 3/5 material ROT001-005 in eight days based on CRPropa (>50% in 14 days), flagged to Moderator as a concentration observation, not a science quota or order to abandon the line.

## Source contact: MATERIAL PRIOR-ART CORRECTION

(1) Carimalo, da Silva, Kapusta 1999, arXiv:hep-ph/9909339, https://arxiv.org/abs/hep-ph/9909339. Full arXiv HTML read. The paper presents preliminary exact helicity amplitude route and Monte Carlo steps, notes astrophysical gamma+IR collisions, and distinguishes large-angle massless amplitude approximations from mass in propagators. The paper does NOT by itself prove a complete fully massive current transport kernel.

(2) Shishkina and Sotsky 2003, v4 2006, arXiv:hep-ph/0312208v4, https://arxiv.org/abs/hep-ph/0312208. ARXIV ABSTRACT and version metadata READ, full original paper/TeX NOT opened. Explicit matrix-element and helicity-amplitude treatment of gamma gamma -> 4 charged leptons, title specifies two electron-positron pairs. Exact mass/domain details require full-source audit.

(3) Dyndal and Schoeffel 2016, DOI 10.5506/APhysPolB.47.1645, https://www.actaphys.uj.edu.pl/fulltext?page=1645&series=Reg&vol=47. Primary full TEXT index was inspected, PDF screenshot attempted but cache miss (figure visual not certified). Explicit gamma gamma -> 2e+2e-, e+e-mu+mu-, 2mu+2mu-; full tree-level MadGraph5_aMC@NLO elementary cross section and differential collider observables. Pseudorapidity and transverse-momentum cuts and proton photon luminosities limit direct astrophysical transport transfer. Native MadGraph config, massive e scheme, generator binary and uncut full-phase-space output NOT verified.

(4) CRPropa 3.3 C++ module https://github.com/CRPropa/CRPropa3/blob/3.3/src/module/EMDoublePairProduction.cpp blob 682f001a264a741ba9615ed86490d9f216a52cfe READ full; makes two equal-energy hard leptons, NOT four-lepton QED differential. CRPropa3-data Python https://github.com/CRPropa/CRPropa3-data/blob/master/calc_electromagnetic.py blob 030af585f62357e4522f64f7a7daa81c635b20d3 READ full: scalar sigma_DPP, not energy-sharing kernel. CRPropa3 Common.cpp v3.3 blob 876cdac7bd6b8ad65e7e910dc636d00a3abfafab READ: outside-table endpoint clamping.

CORE CORRECTION: earlier limited NO-DIFFERENTIAL-QED-OPERATOR search does NOT show absence of amplitudes or Monte Carlo methods. Candidate source computational routes EXIST in literature. However SOURCE_METHOD_FOUND is NOT the same as a source-verified full four-lepton kernel integrated into R68 transport. NO THEORETICAL NOVELTY CLAIM.

## Exact numerical domain gate at R68 first-event point
Inputs: E_gamma=1436.554 GeV; T_gamma=0.07818527068831995 MeV; m_e=0.51099895 MeV. For STRICTLY HEAD-ON real photons only, s=4 E_gamma epsilon and sqrt(s)=2 sqrt(E_gamma epsilon). The true 4e threshold is s>=16m_e^2. Illustrative bath photon epsilon/T values:
epsilon=T: sqrt(s)=670.2756547821 MeV; s/(16me^2)=107534.27044.
epsilon=2.701178T: sqrt(s)=1101.6155243907 MeV; ratio 290469.20556.
epsilon=10T: sqrt(s)=2119.5977292721 MeV; ratio 1075342.70442.
All PASS via 54-precision Python stdlib Decimal and independent algebraically equivalent evaluation formulas. This is not the Planck/isotropic convolution, not QED differential evaluation and not a physical deposition rate. Even at large s, forward/collinear enhancements make finite electron mass and full angular coverage critical.

## Source inventory: opened versus unavailable
READ: CRPropa3 v3.3 module, InteractionRates.cpp, Common.cpp and generator, 1999 arXiv HTML, 2003 abstract/version, 2016 indexed paper text, and exact CRPropa Git trees. Enumerated 461 items in CRPropa3 v3.3 full Git tree and 1059 items in CRPropa3-data master full tree; neither listed the installed EMDoublePairProduction/rate_CMB.txt table or executable. That negative is LIMITED to those enumerated trees, not to release assets, runtime installations, or other repositories. NOT OPENED: full Shishkina source, actual stock rate-table rows, native MadGraph source/version/config. NOT RUN: compiled CRPropa or MadGraph, full massive QED amplitude integration or any PBH/BBN model. Checked environment has no mg5_aMC command or madgraph Python package.

## Target-specific source-native discriminator and queued ownership
CANDIDATE command string (UNRUN; syntax not validated): generate a a > e+ e- e+ e- QCD=0. Next actual source-owner verification: confirm licensed source and VERSION, ensure electron mass remains nonzero in chosen model/card, identical-lepton exchange amplitudes, no collider pT/eta/delta-R cuts, full 4-body phase space and collinear integration stability; compute inclusive sigma(s) at >=2 COM energies with errors and matched coupling/flux/symmetry and compare appropriate known high-energy sigma ~6.44-6.45 microbarn; output reproducible mass-sensitive normalized four-lepton energy moment(s) and check finite acceptance vs uncut result. Only after this would target bath convolution and cascade energy-loss questions be meaningful. No numerical QED differential claim here.

OWNER QUEUE SUGGESTION, NOT ADOPTED TASK: External primary-source contact candidate XH-S5 (confirm current owner), target science DAX-S8 and relevant MT14/successor, BW provenance/receipt KN13. Exact inputs: arXiv 9909339 and 0312208v4, Dyndal DOI and CRPropa blobs above, R68 E,T. REOPEN TRIGGER: pinned version+massive uncut 4e source-native event generator and >=1 integrated-normalization test OR typed ACCESS_BLOCKED report. RETURN single bounded PASS/FAIL/ACCESS_BLOCKED source card to Moderator and DAX-S8. No automatic audit cascade, owner receipt or BW ingestion assumed. Existing GITHUB_PENDING_BW_INGEST must be checked by KN13, not invented.

## Query/source audit
Searches performed 2026-11-10 via web fast and slow, arXiv HTML, INSPIRE records and public GitHub. Exact core queries: (i) gamma gamma double electron positron pair production differential energy spectrum double pair production high energy QED Lee 1996 spectrum; (ii) double pair production photon photon secondary electron energy distribution transport Monte Carlo exact differential cross section; (iii) gamma gamma to e+ e- e+ e- differential cross section lepton energy distributions Monte Carlo helicity amplitudes 2020 2025; (iv) gamma gamma to four leptons exact matrix element Monte Carlo generator MadGraph photon photon 4e; (v) gamma gamma -> e+ e- e+ e- full matrix element massive electron Monte Carlo Carimalo da Silva Kapusta 2003; (vi) Production of four leptons in gamma gamma interaction 2003 arxiv matrix element electron masses; (vii) Dyndal gamma gamma 4 leptons MadGraph massive electrons gamma gamma ultra high energy distributions. Inclusion gamma gamma real-photon four-lepton amplitude or actual differential MC; exclusion nucleus pair production and e+e- initial states. Counts/exhaustiveness not established. SEARCH_NO_MATCH != NOVELTY.

DISPOSITION: EXTERNAL_PRIOR_ART_FOUND / MASSIVE_DIFFERENTIAL_TRANSPORT_UNVERIFIED / EXACT_KINEMATIC_PASS / SOURCE_OWNER_QUEUE_PROPOSED / STOP_CRPROPA_PROXY / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.
