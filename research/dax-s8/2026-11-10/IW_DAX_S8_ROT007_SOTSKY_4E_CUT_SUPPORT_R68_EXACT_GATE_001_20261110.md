---
artifact_id: IW_DAX_S8_ROT007_SOTSKY_4E_CUT_SUPPORT_R68_EXACT_GATE_001_20261110
created_at: 2026-11-10
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
document_type: SCIENTIFIC_RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: PRIMARY_SOURCE_CUT_SUPPORT_FALSIFIER / EXACT_PLANCK_NUMBER_TAIL / NEGATIVE_KNOWLEDGE_REPAIR
claim_ceiling: NO_SOURCE_NATIVE_GENERATOR_RUN / NO_UNCUT_QED_DIFFERENTIAL / NO_DPP_RATE_BOUND / NO_PHYSICAL_DEPOSITION / NO_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX-S8 ROT007: Sotsky 2006 four-lepton cut-support incompatibility at R68

10 November 2026. Exact object: real gamma gamma -> e+ e- e+ e-. This source audit extends DAX-S7 R68 and DAX-S8 ROT001-006 without claiming a new QED amplitude or rate. The original differential four-lepton R68 transport operator remains OPEN. The independent scientific result here is an exact zero-support constraint for collider-cut published tables at three specified R68 incoming configurations.

## Primary source contact: important qualification of ROT006

**I. Sotsky (2006)**, "Production of four leptons in electroweak gamma gamma interactions", https://arxiv.org/abs/hep-ph/0604020. FULL ARXIV HTML TEXT OPENED. In the results table, minimum allowed energy of *each final particle* is **1 GeV**. The table also uses a minimum 3 degree angle between final particles and 7 degree minimum polar angle. The paper reports mass effects negligible only for studied high-energy collider conditions and cuts (initial photons 60-2000 GeV, stated angular cuts). Its collider table is NOT an inclusive, uncut four-electron transport rate.

**T. Shishkina and I. Sotsky (2004)**, "Production of two electron-positron couples in electroweak gamma gamma interaction", https://arxiv.org/abs/hep-ph/0410010. FULL ARXIV HTML TEXT OPENED. The paper writes representative massive covariant matrix element pieces (electron propagator denominator involving m^2), discusses collinear peaks and an adapted Monte Carlo, and compares helicity versus precision covariant calculation. Its excellent massless-vs-massive agreement is explicitly under TESLA energies and imposed cuts: this is NOT a certified massless uncut result in an R68 plasma. Claimed 0.5-0.7% Monte Carlo error pertains to paper's selected collider case.

**Mauro Moretti (1996)**, "Four leptons final states from gamma gamma fusion", https://arxiv.org/abs/hep-ph/9606225. ABSTRACT and metadata opened, NOT complete body. The abstract reports ALPHA automated amplitudes and sizable fermion mass effects from collinear/t-channel enhancements. This is established earlier work, not DAX novelty.

The ROT006 primary prior-art routes remain active: Shishkina and Sotsky arXiv:hep-ph/0312208 and Dyndal/Schoeffel DOI:10.5506/APhysPolB.47.1645. Neither was run as a full massive four-lepton source-native generator. A direct attempt to open the 2004 arXiv PDF was cache-missed; no figure screenshot or PDF-specific claim is made. The HTML text supports the cited constraints.

## Exact source-domain falsifier

For four outgoing leptons, if every final lepton has COM energy E_i >= 1 GeV, then energy conservation implies sqrt(s) = sum_i E_i >= 4 GeV. Thus **the published cut-accepted cross section is exactly zero at sqrt(s)<4 GeV**. The real physical gamma gamma -> 4e reaction remains open whenever sqrt(s)>=4m_e ~2.04399580 MeV. The zero pertains ONLY to the quoted 1 GeV-per-lepton accepted measure, not the QED matrix element.

R68 inherited first-event point: high-energy photon E_gamma=1436.554 GeV; T_gamma=0.07818527068831995 MeV; m_e=0.51099895 MeV. For two real head-on photons, s=4 E_gamma epsilon. Three bath-energy samples:

| epsilon/T | sqrt(s) [MeV] | physical gamma gamma->4e? | 2006 cut accepted? |
|---|---:|---|---|
| 1 | 670.27565478208673 | YES | NO, exact zero |
| 2.701178 | 1101.61552439074514 | YES | NO, exact zero |
| 10 | 2119.59772927212561 | YES | NO, exact zero |

These are FIXED head-on samples, NOT a thermal or angular convolution. At this E_gamma, possible satisfaction of the four-lepton energy cut even head-on requires epsilon >= (4 GeV)^2/(4 E_gamma) = 2.784441100021300974 MeV = 35.61337161728682146 T_gamma. Non-head-on configurations need at least this epsilon; angular final-state cuts can restrict further.

## Planck photon NUMBER tail: exact series and strong bound

For Planck photon number density proportional to x^2/(exp(x)-1), x=epsilon/T, set a=35.61337161728682. The *number fraction* of bath photons above a is

p_N = integral_a^infinity x^2/(exp(x)-1)dx / [2 zeta(3)]
    = 1.905274252983205879e-13.

Positive expansion 1/(exp(x)-1)=sum_{n>=1} exp(-nx) yields an exact convergent series
sum_{n>=1} exp(-n a) [a^2/n + 2a/n^2 + 2/n^3].
A simple proven lower bound is exp(-a)(a^2+2a+2)/(2 zeta(3)), upper bound that quantity divided by (1-exp(-a)). Computed interval:
[1.905274252983205563e-13, 1.905274252983206213e-13].

This is **NOT** an upper bound for the fraction of actual DPP events, collision flux, energy-deposition rate, or muon events. Event weighting, angular integral and full QED distribution are unknown. The small tail does NOT mean thermal physical DPP is negligible; it means the cited paper's hard-lepton cuts select a very different bath support.

All numerical figures reproduced using 65-digit Python stdlib Decimal and an internally generated fast-convergent Apery series for zeta(3), without using an imported zeta constant. Exact support inequalities and two algebraically equivalent COM formulas PASS. Source code is to be separately published and locally archived.

## Source-firstness and scope

DAX-S7 R68 owns the original rate-vs-differential-kernel gap; DAX-S8 ROT006 established original literature candidates. ROT007 FIRST for this lineage pinpoints **explicit source acceptance mismatch with R68** based on full Sotsky 2006 source text. We did not invent a QED generator or claim prior-art novelty. The 2004 covariant method and 1996 Moretti mass-effects report remain earlier scientific prior art.

FALSE: collider-cut total/differential tables from Sotsky 2006 are directly suitable as an uncut DPP kernel for fixed R68 samples at COM 0.67, 1.10, 2.12 GeV.

TRUE UNDER X: exactly zero cut-accepted rate for sqrt(s)<4 GeV and four individual E_i>=1 GeV; physical 4e process may simultaneously be open.

POSITIVE BOUNDARY: full massive covariant QED matrix elements and adaptive Monte Carlo methods exist in source literature, but an UN-CUT finite-me event generator with identical-fermion exchanges and quantitative R68 normalization has not been verified or run.

## Existing owner/reopen queue — addendum only

The source-contact proposal in ROT006 to XH-S5 was delivered to Slack, but bounded currentness checks on 10 November found no explicit XH acceptance or source-specific response for this DAX request. Do not silently create a second task. Proposed addendum: external source owner XH-S5 or actual assigned current owner should seek uncut massive gamma gamma -> 2e+2e- source generator, confirm exact executable/version, electron mass model, identical-lepton permutations, absence of detector cuts, and run >=1 inclusive sigma(s) at R68-relevant COM plus normalized four-lepton energy moment; otherwise return a typed ACCESS_BLOCKED receipt. DAX-S8 is target-level science contact; MT14/current successor is relevant only for physical Front B transfer; KN13 alone owns BW ingestion. Route a single source response to Moderator/DAX; do not infer acceptance from Slack delivery.

## Reproducibility / search scope

Primary sources above; exact arXiv HTML pages read 2026-11-10. Web queries included Shishkina/Sotsky mass-electron four-lepton 2006, production two electron-positron couples, Moretti four-lepton ALPHA 1996; exclude Bethe-Heitler gamma+nucleus and e+e- initial-state collisions. Full source-run NOT DONE. Search no match != literature absence != novelty. Exact local Python reproducer, results JSON, primary-source audit, README, SHA-256 manifest, and ZIP passed clean unpack/replay; GitHub code readback to be checked separately. Original source files and native generator binary not included in this bundle.

STABLE_STOP for importing these collider-cut tables / QED_UNCUT_RUN_OPEN / SOURCE_REPAIR_PASS / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.
