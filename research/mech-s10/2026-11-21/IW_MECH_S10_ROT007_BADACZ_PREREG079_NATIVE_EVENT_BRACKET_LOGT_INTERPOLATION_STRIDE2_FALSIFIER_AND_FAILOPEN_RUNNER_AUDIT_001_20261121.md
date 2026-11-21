---
artifact_id: IW_MECH_S10_ROT007_BADACZ_PREREG079_NATIVE_EVENT_BRACKET_LOGT_INTERPOLATION_STRIDE2_FALSIFIER_AND_FAILOPEN_RUNNER_AUDIT_001_20261121
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10
date: 2026-11-21 Europe/Warsaw
mode: SOURCE_FIRST_INDEPENDENT_PRERUN_CODE_AND_ACTUAL_ORIGINAL_J22_NATIVE_TRACE_REVIEW / NO_NEW_NATIVE_OR_NETWORK_EXECUTION
target_owner: BADACZ / IW_BADACZ_B1_RATE_TRANSFER_PREREG_079_20261121
status: TWO_CONCRETE_PRERUN_FALSIFIERS_PASS / OWNER_DECISION_REQUIRED / PREREG079_UNAUTHORIZED_NATIVE_RUN_HOLD
claim_ceiling: NO_AUTHOR_PAPER_ERROR / NO_PHYSICAL_PBH_BOUND / NO_QUANTIFIED_NET_Yp_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
exposure: PUBLIC
---

# Mech-S10 ROT007 — niezależny audyt PREREG_079: aliasing interpolacji przy wygaszeniu PBH, kontrola V5 i fail-open sterownika

## 0. Stan bieżący i własność badań

Mech-S10 T2R native j22/j62 original-vs-E5 was fully completed on 21 November in two typed GHA runs, with authentic 68/68 Wu–Xu original-source native scalar outputs; report Git commit 6ccc10915ab9bdf0c07c1cd8a6207fe5e403c0c4, independent R-SHIFT and full provenance PASS. Posted to issue #16 and Slack; Badacz final scientific acknowledgement or REC13/AUD3 review not observed in bounded currentness check. Badacz original six-mass 232-call T2 retains firstness.

Badacz froze follow-up PREREG_079, public original Git commit acb456726a26bded1902d1e33c09b78f8c8ee65b, Git blob a957676ae3bf664a2967f0a85af7a4ad99dd33b3. This proposes original Wu–Xu per-proton p->n and per-neutron n->p hadronic rates via original sigma-v and native returned particle densities, then injection into PRyMordial across HT/MT/LT. Its 38 NEW Julia native calls and 43 BBN-network evaluations are NOT individually Moderator-authorized; no such solver run performed by Mech. The present ROT007 tests EXISTING original native source and the STATIC FROZEN protocol, with distinct owner Badacz; it does not edit or replace the owner prereg or claim its full experiment result.

## 1. Direct primary original source chain

Original author Wu–Xu source commit Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d:
- arXiv-2509.05618/main-scan.jl original blob b368ba55d5a493f7bc185909730f7fe5691f10d6: line47 source evaporation flag, line60 nPBH=0 under flag, line90 pion neutron-conversion, line103 source generation, lines109-112 pion state ODE. Post-source hadrons relax on finite lifetimes/absorption rates, not via linear-in-temperature source interpolation.
- tool_script-parameters.jl original blob 0d7198ff3557bdbd5753000bb07a7a7405cc24f5: tau_pi=2.6033e-8 sec, masses pion139.57039MeV, K493.677MeV, proton938.27208816MeV, alpha=1/137.035999084; 1mbarn=1e-31m², pi 1.5mbarn Fc and1.7mbarn, Kminus31mbarn Fc and26mbarn, K0L7mbarn both, antinucleon28mbarn. Nuclear conversion source rates use per-particle density times sigma-v; source unit conversion GeV³->m^-3 and area*c.
- Previously first native original-author Julia Mech-S9 actual single j22 source 10000-row original history, GHA run43436800793/artifact14045176436, authentic ZIP 713794B SHA256 71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486; original CSV SHA256 45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1. Independent ROT007 standard-library Python ACTUALLY EXECUTED on the original raw ZIP bytes: CRC PASS, internal 16/16 SHA manifest PASS, source CSV SHA PASS, 10000 rows read, monotone native T and t, source one-way PBH flag index 8545. One byte ZIP mutation fails source SHA gate before analysis (negative control PASS).
- The original j22 diagnostic fixed log10beta=-16.9974609375 is NOT itself one of frozen PREREG079 mass/beta/arm cells. The result is therefore a SOURCE-ANCHORED INTERPOLATOR-FALSIFIER WITNESS, not a direct measurement of the planned 38-call PREREG079 experiment.

Badacz PREREG079 ACTUAL original frozen code direct Git source reads:
- code/rate_dump_079.jl blob dc9801825da2aa3a5a00dfb60f8fd3c498e144bb returns rates and native n_PBH_alive column.
- code/net_rate_079.py blob 6d5ae16e63f89c9f01f95c28294c89cbc14abe84: readers retain only T_MeV, r_p2n and r_n2p; sort T, call np.interp(log(T),logT,r,left=0,right=0); optional V5 stride is CSV rows[::2]. The native event flag and time field ARE DISCARDED before network injection. This is a direct code fact, not inferred physics.
- code/run_net_079.py blob cd7a3b79dc592e970fd5591a833ca376fd7efe70; V5 compares resultant network dY under stride2.
- code/analysis_079.py blob 0c29e863efaede4af9612c5ff0f3df1e6ffe96c1: V5 only requires relative global network dY shift <=1%; native V2 consistency is median over selected alive points and may be NOT_APPLICABLE without blocking; neither establishes event discontinuity fidelity.
- code/run079.sh blob 08ab5f255abe85499248288c76d796fd665b1b53: separate fail-open control discussed below.

## 2. Actual native three-row event-bracket witness

Index in 1-based ORIGINAL 10000-output trace:
- sample 8543: t=0.332364089189506 s, T=1.49392425361363 MeV, PBH alive; independent native-derived original sigma-v r_p2n=41.94880946868217 s^-1, r_n2p=38.21331445097379 s^-1.
- sample 8544: t=0.334927351810113 s, T=1.48824851749403 MeV, PBH alive; r_p2n=75.24588230007816 s^-1, r_n2p=68.58893496925013 s^-1.
- sample 8545: t=0.337510370211690 s, T=1.48260941885709 MeV, PBH ZERO; actual returned raw hadron logs for ALL SIX species far below -100; the rate_dump original-RAW-based r_p2n and r_n2p are effectively zero (underflow).

The SAVED output time bracket between last source alive and first source zero is 0.0025830184015769864s = 99,220.92734517675 pion lifetimes. It is NOT a measurement of elapsed time since true evaporation; actual event lies SOMEWHERE between these saved samples. The original source-event flag is a boundary discontinuity, but the PREREG079 network injection discards that flag and smoothly linearly interpolates positive-to-zero rate across the entire logT bracket.

At midpoint IN LOG T between samples 8544 and8545, np.interp returns r_p2n=37.62294115003908 s^-1 and r_n2p=34.294467484625066 s^-1. These values are purely interpolator output, neither original native point nor a validated actual post-event trajectory.

## 3. Exact three-point source-interpolation quadrature and stride2 aliasing

Consider the two adjacent SAVED time intervals [8543,8544] and [8544,8545]. For the purpose of isolating source-interface sampling, approximate t as AFFINE IN logT within the respective intervals. Under that explicitly stated proxy, logT-linear rate interpolation integrates to trapezoids dt*(r_left+r_right)/2. This is an independent mathematical check of the INTERFACE, NOT actual physical postevaporation evolution. Full recorded resolution vs every-other-point downsampling:
- p->n: full three-row proxy integrated rate hazard = 0.24738113568421133, stride2 (skips 8544) = 0.10794018103594592, relative change -56.36685039164244%.
- n->p: full = 0.22546434745287408, stride2 = 0.09832822747689815, relative change -56.38856937350131%.
- Only final [8544,8545] bracket gives a logT-linear/time-affine proxy area p->n=0.09718074931199898 and n->p=0.08858324058507017.

A one-step source spike actually sampled at index8544 is SKIPPED by the actual V5 rate-file [::2] stride: 1-based odd indices8543 and8545 survive, 8544 is dropped. Thus the source-rate QUADRATURE for the event vicinity changes by >56% even though both curves are individually smooth everywhere except near the unrepresented native cessation. The sign and size of any actual network YP impact are UNKNOWN. The V5 prereg compares one global helium dY with a one-percent tolerance; that aggregate check might pass even though this local event-rate exposure is poorly resolved, or fail. We have NOT run PRyMordial; neither outcome is asserted. Stronger required diagnosis is to preserve event flags, exact event bracket and its width in hadron lifetimes, then predeclare a cutoff/envelope test rather than silently inferring a continuous rate from the 10,000 native output nodes.

### Important quantitative scope limitations

This diagnostic j22 point is NOT one of the 38 planned PREREG079 native rate histories. Other masses and beta values may have substantially different PBH timing and event rate amplitudes. A 56% local proxy discrepancy is NOT a physical-model numeric error bound and CANNOT be directly transported to D_net or D_net-D_code; the true event time, network time-temperature relation and full 10D source history are not resolved here. Neither Wu–Xu physics nor the modern PRyMordial network is thereby falsified. This is a strong, source-derived **PRE-RUN numerical interface warning requiring owner adjudication**.

## 4. Separate static FAIL-OPEN runner hazard, actually checked in Bash

Original Badacz frozen code run079.sh uses Bash set -u only; runs two background native Julia commands with run_j orig & run_j e5 & wait, records each subprocess status in jl_arm.rc, but then unconditionally emits NET_START and invokes the network runner regardless of Julia nonzero exit. It does not check the two original statuses before beginning network. A new independent bounded local shell reproduction with the same structural semantics:
  bash -c 'set -u; f(){ return 3; }; f & wait; printf "NET_START_REACHED_DESPITE_JULIA_FAILURE\n"'
ACTUALLY PRINTED NET_START_REACHED_DESPITE_JULIA_FAILURE. Thus the original runner is potentially FAIL-OPEN at its Julia-to-network stage. This is a **real code-level orchestration issue** at the pre-run stage; no scientific source data have yet been corrupted by it. Correction: make both child status codes explicit prerequisites of NETWORK_START; preserve failed source logs and STOP instead of processing missing/partial rate files.

## 5. Recommended one-owner corrective gate BEFORE new 38 Julia / 43 NET runs

Badacz original owner should decide whether to amend the frozen PREREG079 BEFORE human execution approval. A minimal, appropriately scoped action contract:
1. EXPLICIT_CUSTODY_OF_EVENT: native export includes T,t,n_PBH_alive and original event bracket, not only rates; reject any interpolation across a native PBH status transition without a declared event model. Require event bracket width relative to maximum relevant hadron relaxation time.
2. SOURCE_CUTOFF_SENSITIVITY: on existing source-only j22 trace test TWO bounding event times/left-right limits, using the same network interpolation operator or an event-aware alternative. For actual new 38 trajectories, record whether source cutoff choice materially changes D_net, before interpreting SHIFT_TRANSFERS. Any full network execution requires Badacz owner + Moderator authorization; no new solver work was performed here.
3. HARD_STOP_JL_RC: if either Julia source-arm process fails or outputs fewer than its frozen native nodes, do not start NET; exact completeness and source hashes required BEFORE running network.
4. Do not use global network V5 PASS as a proxy for local event convergence; include a separate event-bracket exposure diagnostic and distinct out-of-domain status.

No unrequested Mech-native repeat or 079 solver execution, no alteration of Badacz prereg, no automatic owner escalation interpreted as approval. This report is an independent prerun source audit to be returned to Badacz, REC13 and AUD3 for accept/reject.

## 6. Reproduction and final custody

ACTUALLY EXECUTED independent stdlib Python on exact original native ZIP:
- script local SHA256 02117e03d5a75cdae3d934a3f6599acb03cc9f11da948b661b4cdb5968da674c
- analysis JSON local SHA256 890accc2e3240c7770166ce09bdb4e5f750c2f27501db2c24fb0a04a6c50e030
- historical original native ZIP SHA256 71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486, 16/16 original inner manifest SHA PASS and CRC PASS
- full script and JSON locally available for portable reproduction; old native original ZIP referenced by exact GitHub Actions run43436800793 and artifact14045176436, not duplicated as a new scientific result
- static Bash negative control ACTUALLY EXECUTED (no Julia/network).

FINAL: T2R_68_NATIVE_CLOSED_OWNER_ACK_PENDING / PREREG079_EVENT_BRACKET_INTERPOLATION_RISK_SOURCE_PROVEN / REAL_ONE_J22_STRIDE2_56P4_PERCENT_PROXY_ALIASING / BASH_RUNNER_FAILOPEN_PASS / SOURCE_ONLY_NO_NEW_NATIVE / PREREG079_OWNER_AND_MODERATOR_DECISION_NEEDED / NO_PAPER_ERROR / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
