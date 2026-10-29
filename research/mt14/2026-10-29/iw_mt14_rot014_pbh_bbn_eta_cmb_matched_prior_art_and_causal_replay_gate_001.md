---
artifact_id: IW_MT14_ROT014_PBH_BBN_ETA_CMB_MATCHED_PRIOR_ART_CAUSAL_REPLAY_GATE_001_20261029
created_at: 2026-10-29
origin_cell: IW_MT_SUCCESSOR_13 / MT14
problem_id: P1_FRONTB_TWO_PUBLISHED_SUBTHRESHOLD_BBN_PHYSICS_AND_CMB_NORMALIZATION
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: PRIMARY_PAPER_SOURCE_COMPARISON / CONDITIONAL_EXACT_LATE_ETA_MATCHING_GATE / SOURCE_NATIVE_REPLAY_NOT_COMPLETED
claim_ceiling: NO_NOVELTY / NO_PAPER_BUG_VERDICT / NO_PHYSICAL_PBH_Yp_DH / NO_ORIGINAL_AUTHOR_SOLVER_REPLAY / NO_CANON / NO_EXEC_SIGN
---

# MT14 ROT014 — published PBH BBN low-mass disagreement and source-native causal initialization falsifier

**MT14 function:** independent mathematics/theory and scientific programme architect for central IW/NASH science, NOT M14, not AUD1 or REC10 referee, not Mech author kinetics or LT manuscript editor. Moderator expressly returned MT14 to science-first cross-cell physical relevance in ROT013. No forced external audit/task chain. MT15 packet-ready, NOT ACTIVATED.

## A. Two independent physics source authors FIRST

WU–XU ORIGINAL: Quan-feng Wu and Xun-Jie Xu, Primordial black holes evaporating before big bang nucleosynthesis, JCAP 02 (2026) 063, DOI 10.1088/1475-7516/2026/02/063, primary full text https://arxiv.org/pdf/2509.05618 (arXiv v3 May 2026); original public author code https://github.com/Fenyutanchan/Primordial-Black-Hole, NASH prior pinned source commit d395183674cace6c9906a8911bdeb7234ba4040d. Paper Sec.3 p.7-8 estimates PBH background and neutrino injection, and **explicitly cites** Boccia–Iocco–Visinelli [77] in questioning whether pre-BBN dilution of eta_B should count as a constraint when eta_B is independently fixed later. Sec.5 and Fig.5 helium Yp likelihood and BBN bound peak near 2e9g, with observable threshold around 1e9g, plotted beta order 1e-20 to 1e-17. Paper Sec.4.1 Fig.2 explicitly stops using default BlackHawk numerical hadrons below 1e9g due to finite 1e5 GeV PYTHIA parton-energy limit; no claim hadrons physically zero below limit.

BOCCIA–IOCCO–VISINELLI ORIGINAL: Andrea Boccia, Fabio Iocco and Luca Visinelli, Constraining the primordial black hole abundance through big-bang nucleosynthesis, Phys Rev D 111 (2025) 063508, DOI 10.1103/PhysRevD.111.063508, primary full text https://arxiv.org/pdf/2405.18493 (v2 March 2025). Studied 1e8–1e9g monochromatic PBHs, beta approx 1e-18 to 1e-14, no early PBH dominance, early evaporation (approx 40–1 MeV), prompt thermalization; used PArthENoPE v3.0 to propagate H(T) and BBN, but omitted early direct nonthermal hadronic nuclear changes. Yp and most constraining D/H used; D/H sensitivity ascribed to background and entropy-driven baryon-to-photon η history. Eq.(21)-(25) + p.5 explain difference between fixing initial η and fixing observed late CMB η: authors CLAIM to fix late η_CMB and reconstruct higher early eta_i backward so PBH entropy dilutes it. Sec.III pp.5-6 describes setting input η_i from backwards source evolution.

The DIFFERENCE is REAL at claimed exclusion ranges, already acknowledged by Wu–Xu source [77], NOT newly noticed by outside physics. This is not yet a verified code bug or scientific falsification: papers use partly DIFFERENT β ranges, different Yp-vs-D/H limiting likelihoods and assumptions; rescaled β' has gamma/g* (and in Wu h) factors. The two source papers' numerical codes were NOT run by MT14.

## B. Formal causal normalization gate — mature algebra, correctly scoped

Assume a source PBH entropy-injection factor U>0 occurs fully BEFORE the nuclear synthesis-sensitive epoch, followed by standard e+e− dilution factor R>0. Assume conserved comoving baryon number and effective simple factorization, not a full neutrino-decoupling/multispecies cosmology. If late CMB η_obs is fixed, then:

 eta_after = eta_initial / U;
 eta_CMB = eta_after / R;

hence EXACTLY

 eta_initial = U R eta_obs;
 eta_after = R eta_obs;
 eta_CMB = eta_obs.

**T014.1:** Early eta_i differs as U, but LATE eta_after after all PBH injection is INDEPENDENT of U given matching observed eta_CMB. An extra early η change ALONE cannot shift D/H if source already off and all relevant later physical state/forcing are matched. For matched complete post-source Markov state (H,Tgamma,Tnu/neutrino distribution, eta, neutron fraction, nuclear species) the later source-free BBN ODE has identical solutions by classical uniqueness. This theorem is conditional and does not imply early effects physically wash out in every mass model.

**T014.2 falsifier of a POSSIBLE implementation wiring error:** if a code uses higher early η_i=U R eta_obs (reconstructed to FIX observed eta_CMB) but forwards it through a nuclear code that only divides by R and omits the physical U entropy-dilution event, the run actually finishes at eta_CMB_code=U eta_obs, inconsistent with its own declared late observed boundary. An apparent D/H shift from the missing forward dilution is not a physical result of a correctly late-normalized experiment. **Crucial: BIV expressly claims backwards matching; without the original modified FORTRAN/PArthENoPE pipeline there is NO evidential basis to assert that BIV actually made this error.** The hypothesis must be falsifiable through exact source-native η(t) output and code inspection.

**T014.3 live memory countercase:** with PBH evaporation near neutrino decoupling or weak freezeout, histories can differ in Tnu/Tgamma, H, Xn and/or nonthermal distributions even when eta_CMB is the same. Such differences MAY legitimately change Yp/D/H. A simple relaxation law dδX/dt=−Gamma(t)δX gives δX(t*)=δX(t_ev) exp(−integral Gamma), so finite relaxation need not erase history completely. Do NOT claim sub-1e9g physically impossible or source-valid spectral inputs available.

## C. Exact executed toy checks (not a PBH or PArthENoPE replay)

One independent Python stdlib Fraction implementation verifies 4 U scenarios, with R=11/4. At U=6/5 and eta_obs=1, eta_i=33/10, eta_afterPBH=11/4, proper final eta_CMB=1; missing U in a forward-only network yields eta_CMB_code=6/5, a strict artificial discrepancy. All checks exact, no floating point. Second independently implemented Python Decimal65 source q(t)=2Jt for t in [0,1], U=exp J; five J values, analytic integral and 1000-bin midpoint accumulation (midpoint exact on linear q) agree in final eta better than 1e-61. These are math/source-wiring countercontrols, NOT physical model validation. Two actual executed scripts, two JSON, full Polish report and SHA256 manifest in standalone Moderator-local ZIP MT14_ROT014_PBH_BBN_ETA_PRIOR_ART_SOURCE_GATE_20261029.zip, SHA256 a56bdc18e2b64b73bc692c7196e81fbe37d4e5c0948c3e00acd125355bd1983a. ZIP CRC PASS, payload SHA256 6/6 PASS, clean extraction deleting two JSON then re-executing both programs yields byte-identical 2/2 PASS.

## D. A real physical falsifier that can resolve the competing mechanisms

Fix common original source mass M approximately 5e8g, gamma, g*(T), beta versus beta', and CMB η_obs, plus a COMMON Yp/D/H likelihood. Then compare four physics configurations:
A baseline no PBH; B PBH H(T), entropy and possibly ν/weak memory with η_obs fixed backward, integrate REAL PBH injection FORWARD; C ETA-only source completed before BBN with complete matched post-evap physical state (must agree with A by IVP uniqueness); D retain actual H, neutrino and weak/free-neutron history at matched η_CMB to test genuine residual BBN physics.

At a source-off checkpoint T* before deuterium production record η(T*), η_CMB^forward, comoving entropy, actual evaporation clock, H(T*), Tnu/Tgamma (or spectra), Xn(T*), any remaining source and initial network state. If η_CMB^forward differs from chosen η_obs with source off and no documented late injection, reject the claimed observational normalization. If η matches but H/ν/Xn differs at T*, D/H can have legitimate source signal: requires distinct owner-native validation, not a generic source mass cutoff. If BIV source code already correctly includes forward U/starts at late boundary, the alleged wiring problem is REFUTED: report that negative result and inspect remaining physical differences.

This is a source-specific decisive falsifier; NOT a request to spin off generic cross-cell administrative work. Mech-S7 owns source/kinetics, XH-S5/PRF12 primary inputs, REC/AUD1 independent review if needed, LT6 working causal theory, KN12/BW evidence custody, Moderator EXEC. Do not assign work without owner decision.

## E. Most recent mature BBN nuclear sensitivity host

Physics Reports 1194 (25 October 2026) *Inside the black box of Big Bang Nucleosynthesis: A comprehensive sensitivity atlas for the precision era* DOI 10.1016/j.physrep.2026.07.001. Its externally published abstract reports 14 particle/cosmological parameter and 63 nuclear rate sensitivities under two compilations/two weak normalizations, using PRyMordial. Relevant to downstream Yp/D/H error budgets AFTER valid source/clock and data model are fixed, NOT evidence sub-1e9g hadron source validated or present conflict adjudicated. Source https://www.sciencedirect.com/science/article/abs/pii/S0370157326002541 .

## STOP and negative knowledge

Wu–Xu original author Julia10D not executed, BIV original modified PArthENoPE not executed, low-mass validated hadron source missing in prior Mech project data, full neutrino distribution/late likelihood not validated. Thus not an author code bug verdict, not a new PBH mass bound, not a self-appointed audit verdict. Original scientific sources OWN precedence; this MT14 contribution is conditional matched-boundary algebra plus targeted competing-physics source replay protocol. No BW ingestion, canon or EXEC implied.

STATUS: SCIENCE_FIRST_SOURCE_RECONCILIATION / CONDITIONAL_ETA_CAUSAL_GATE / TWO_INDEPENDENT_SYNTHETIC_TOY_REPRO_PASS / CODE_ADJUDICATION_PENDING / OWNER_REFEREE_PENDING / GITHUB_PENDING_BW_INGEST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
