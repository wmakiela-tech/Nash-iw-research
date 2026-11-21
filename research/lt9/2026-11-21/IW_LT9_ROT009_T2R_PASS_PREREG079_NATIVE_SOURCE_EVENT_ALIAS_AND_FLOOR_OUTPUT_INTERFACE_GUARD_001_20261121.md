---
artifact_id: IW_LT9_ROT009_T2R_PASS_PREREG079_NATIVE_SOURCE_EVENT_ALIAS_AND_FLOOR_OUTPUT_INTERFACE_GUARD_001_20261121
origin_cell: IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_07 / LT9
created_at: 2026-11-21 Europe/Warsaw
exposure: PUBLIC
document_type: ORIGINAL_WUXU_SOURCE_PHYSICAL_RATE_TRANSFER_FALSIFIER_AND_T2R_CURRENTNESS
claim_ceiling: T2R_NATIVE_J22_J62_PASS / PREREG079_EVENT_ALIAS_UNCERTIFIED / RAW_VS_FLOOR_SOURCE_OPERATOR_MISMATCH / PHYSICAL_IMPACT_UNKNOWN / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
bw_write: NONE
living_theory: REV029_UNCHANGED
c1: PAUSED_BY_MODERATOR_NOT_WORKED
---

# LT9 ROT009 — źródłowy audyt transferu hadronów po niezależnym T2R

## 0. Co naprawdę zmieniło się od ROT008

Mech-S10 ukończył autoryzowany T2R: 34 rzeczywiste oryginalne wywołania Julia Wu–Xu w GHA 44749222324 z 20 XI i odrębnie autoryzowane 34 E5 w GHA 44900663854 z 21 XI. Przebiegi, nie pojedynczy nieprzerwany job; pierwszy zakończył się techniczną awarią E5 przed jej wykonaniem, drugi był uzupełnieniem bez powtarzania orig. Oryginalny raport Mech-S10 (pełny odczyt bez oryginalnego ponownego pobrania ZIP przez LT9):
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s10/2026-11-21/IW_MECH_S10_T2R_E5_ONLY34_TECHNICAL_CONTINUATION_NATIVE_68_OF_68_TWO_RUNS_INDEPENDENT_REFEREE_PASS_001_20261121.md
Git blob 852f19c25abb68eeea5112cb639162efc4a226bd.

Native outcome: j22 D=+0.27229926091289514 dex, factor beta 1.8719716224845862, j62 D=+0.29812358518660886 dex, factor beta 1.986660171690752. Independent 17-node OLS7 matches Badacz earlier owner D within 3.6e-15 dex, all 68 printed native Y-code values match textwise at 17 significant figures. Real different GPT-family same original author numerical code, NOT independent physical implementation, not proof that E5 is physically correct, not new PBH bound. Original firstness Wu–Xu, then Badacz T2, then Mech-S10 reexecution.

Badacz REVIEW078 20 XI source independently read: PRyMordial-vs-Wu-Xu neutron-kick response gain is temperature dependent, 1.064 at 0.8MeV to 1.285 at 0.105MeV in the qualified core; code's numerical kick gain near 1.2–1.5MeV was not stable and does not yield a certified local kernel. Its solution to the missing physical readout was to freeze PREREG079, transferring actual author-solver two-way hadron per-nucleon rates directly to a full PRyMordial nuclear network.

Original PREREG079, source blob a957676ae3bf664a2967f0a85af7a4ad99dd33b3:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/badacz/2026-11-21/IW_BADACZ_B1_RATE_TRANSFER_PREREG_079_20261121.md
Actual Moderator authorization to execute was logged 21 XI 13:02 CET (owner RUNLOG). At checked snapshot about 13:07 owner directory held prereg, code and log, NO measurement results; absence of checked results is not a claim about anything executed afterwards.

## 1. Original native source and source-transfer code, direct read

Wu–Xu original author commit d395183674cace6c9906a8911bdeb7234ba4040d:
https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl
Git blob b368ba55d5a493f7bc185909730f7fe5691f10d6, lines39-60,90-112,179-195,206-210,232-235.
Original parameters blob 0d7198ff3557bdbd5753000bb07a7a7405cc24f5 define charged pion tau_pi = 2.6033e-8 seconds:
https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/tool_script-parameters.jl

The native rate-dump PREREG079 original read:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/badacz/2026-11-21/code/rate_dump_079.jl
Git blob dc9801825da2aa3a5a00dfb60f8fd3c498e144bb. The driver calls author magic with hadrons_output_flag=true, collects 10000 output samples of raw charged densities and computes per-proton r_p2n and per-neutron r_n2p by multiplying those densities by original charge-specific sigma-v.

The NET consumer original read:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/badacz/2026-11-21/code/net_rate_079.py
blob 6d5ae16e63f89c9f01f95c28294c89cbc14abe84. It orders source T and interpolates each rate LINEARLY IN log(T), zero outside data span; it is not event-aware and does not use source solver internal event times.

The NET patch original read:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/badacz/2026-11-21/code/prym_rate_patch_079.py
blob 15399fabc8186101342beaad9d8a03872e2b80b5. It adds r_n2p to the n→p forward and r_p2n to p→n backward rates for HT/MT/LT. The exact upstream PRyMordial source vallima/PRyMordial@725d8a8 PRyM/PRyM_main.py blob b407438ad056ef3a45b1c650b2d7da5dc620fa91 was reopened: its forward and reverse directions and NormWeakRates in s^-1 confirm the PATCH DIRECTION IS CORRECT. NO accidental allegation of a sign swap.

The actual native 10000-point prior source trace is Mech-S10 ROT006, blob a5bea87f11805b865f016d6f4b762172b11fcb1a, which independently downloaded and hashed Mech-S9 GHA 43436800793 archive:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s10/2026-11-19/IW_MECH_S10_ROT006_ORIGINAL_WUXU_NATIVE_TRACE_FROZEN_PION_SIGN_GATE_AND_QSS_FALSIFIER_001_20261119.md
LT9 reuses these exactly reported sourced native sample numbers, NOT a fresh original ZIP audit. The old Mech audit was for j22 beta about 1.005863531e-17, close but NOT identical to each new PREREG079 source-run beta; no 079 results yet to measure actual transferred errors.

## 2. Material physical question: time of evaporation is hidden between far-spaced samples

Actual native old j22 Mech sample 8544 last PBH active at t0=0.334927351810113s, T0=1.48824851749403MeV; first sampled no PBH 8545 at t1=0.337510370211690s, T1=1.48260941885709MeV. The true source-off event time was NOT recorded, only bracketed.

ACTUALLY EXECUTED fresh LT9 JavaScript arithmetic from those sourced numbers:
delta_t=0.0025830184015769864 seconds
delta_t/tau_pi=99220.92734517675
ln(T0/T1)=0.003796280758078493
delta_t/(2*tau_pi)=49610.463672588376.

PREREG079 interpolates the rate in log T from active to zero in this bracket, which corresponds to an artificially smooth tail across about 100000 charged-pion decay lifetimes unless the actual source timing was independently recovered. Physical positive post-source pion survival in original ODE decays at least on the pion decay timescale tau_pi (hadronic capture accelerates the loss).

**Carefully bounded arithmetic witness; NOT actual estimated PBH error:** Suppose at t0 there is normalized rate r0>0, and physical source is switched off just after t0 in a fixed-coefficient pion subsystem with only decay, so r_true(t)=r0 exp(-(t-t0)/tau_pi). Then r(t1) is effectively zero and the true area across gap is r0*tau_pi. TIME-linear interpolation through the identical samples yields r0*delta_t/2, 49610.46 TIMES the true area. The actual PREREG079 method interpolates linearly in log T, not in t, and true T(t) differs slightly; this exact factor is only the conditional time-linear example, not an error factor for PRyMordial. Alternatively a history that remains active until near t1 has the SAME recorded endpoints and a much larger true integral than instant source-off. The sample endpoints alone cannot identify the integral without additional native source and dynamical constraints. This is a standard sampling nonidentifiability fact, NOT a novel theorem or demonstration of real model error.

The old Mech actual 10k j22 source-off gap is a real source-data counterexample to assuming generic timescale resolution. Whether it biases actual 079 Yp upward/downward or substantially at all is UNKNOWN. Neutron weak-equilibrium relaxation at T~1.5MeV can erase early effects; full network response cannot be inferred from a raw rate area alone. This is precisely the T range where REVIEW078 could not determine a stable ratio G_code/G_net.

## 3. Separate exact source identity issue: log-floor native RHS versus exported raw densities

Original Wu–Xu author evolution_system at lines53–58 defines effective state density for neutron RHS as n_eff = EU(exp(max(u,-100)),3), for EACH hadron. In contrast, output arrays at lines187–192 are n_raw = EU(exp(u),3) WITHOUT lower clamp; hadrons_output_flag tuple at lines232–235 exports the RAW arrays. Badacz rate_dump_079 uses those exported RAW arrays in sigma-v conversion rate calculations. Thus for a channel with positive cross section sigma, if u < -100,

r_raw / r_source_rhs = exp(u+100) < 1,

and r_source_rhs - r_raw = sigma*(exp(-100)-exp(u)) > 0 in same source natural density units. This is an EXACT SOURCE-LEVEL DIFFERENCE of operators, not an assumption about dynamical evolution.

The Mech-S10 native old j22 10000-run identifies 1456 postev sampled states with both pion raw log densities under -100. Hence this distinction actually occurs in an authentic original 10D trajectory. It is NOT independently demonstrated yet for every new 079 run. The absolute floor contribution may be negligible and nothing here establishes a physical Yp error, especially since once no PBH is left both pion species rapidly become tiny.

Original PREREG079 V2 checks the rate–neutron derivative consistency only for PBH ACTIVE AND hadronic dominated points; it does NOT test source-off floor-active points. The scientific claim "the dumped r are literally the rates used by the Wu–Xu neutron RHS for all times" is too strong without either applying the same effective floor to exported densities or a quantitative absolute floor-error bound.

## 4. Why prereg 079 frozen gates do not resolve these two gaps

Original analysis_079.py, blob 0c29e863efaede4af9612c5ff0f3df1e6ffe96c1:
- V1 confirms repeated same author Y_code scalar; does not measure unsampled hadronic rate area.
- V2 checks a sampled derivative only for PBH alive with hadron-dominant magnitude; it excludes floor-active after source-off and cannot reconstruct the evaporation-event time within a 10000-grid bracket.
- V3 uses nearly-zero PBH beta baselines; not an event alias test.
- V4 tightens solver tolerance for two orig cases; not input source calibration.
- V5 compares full and every-second source sample for two original cases o22_n08 and o62_n08; it can test rate-grid sensitivity in this chosen interpolation family, but **agreement of two approximations is not proof that either reconstructs an unsampled discontinuity**. Neither V5 E5-case coverage nor an independent exact source-off event timestamp is frozen.

These checks are useful for their stated numeric purposes, and a PASS is NOT falsely reclassified as a failure. Instead, IF they PASS and report SHIFT_TRANSFERS, that label remains a *conditional numerical result under their sampled-rate transfer*; external physical inference still needs separately labeled source-event and floor-operator gates. Do not change frozen prereg after observing outcomes. This report is a distinct post-facto currentness/input challenge, not retroactive amendment or extra task command.

## 5. One decisive forward scientific falsifier

The next physics-important question after 079: does the target D_net and full-network DeltaYp remain stable when native event-aligned hadron conversion rates (rather than 10000-point snapshot interpolation) are used at the SAME Hawking source and cosmology?

Owner-dependent, not initiated by LT9:
- reconstruct the source-off event time and near-event pion kinetic response from the SAME native ODE solution, using source event-aware output or a rigorously bounded time integral; do not invent missing 10D native points;
- correct/quantify raw-vs-floor operator difference, preserving original source semantics;
- for j22 and j62, orig and E5, calculate uncertainty envelope on physical full-network DeltaYp and D_net arising solely from source transfer before making any PBH constraint;
- preregister a target-level significance gate, such as a material fraction of the expected E5 effect or |D_net(event-aware)-D_net(snapshot)| <=0.02dex; 0.02dex is merely the current prereg079 comparison tolerance and would require owner approval if reused as future stability threshold.
- If effect does not survive: a reproduction result remains valuable, but no new physical bound. If stable: source transfer certified, then pursue source hadronization/charge, full BBN theory, observational likelihood, mature host and referee.

The main scientific objective remains a defensible *physical* PBH helium constraint different from Wu–Xu 2026, not reporting a generic classical two-state ODE lemma. The 2026 Bianco et al. nuclear network for decaying relics is the modern physical comparator, but different injection source. No claim is made that any existing paper is in error, that the numerical recast by LT9 ROT007 is a final 95% CL bound, or that C1 is active.

FINAL: T2R_68_OF_68_NATIVE_TWO_RUN_PASS / RATE079_ORIGINAL_HOOK_DIRECTION_PASS / EVENT_SOURCE_TIMING_NOT_CERTIFIED / RAW_VS_FLOOR_OPERATOR_MISMATCH_EXACT_WHERE_FLOOR / REAL_079_PHYSICAL_ERROR_UNMEASURED / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_NATIVE / C1_PAUSED.
