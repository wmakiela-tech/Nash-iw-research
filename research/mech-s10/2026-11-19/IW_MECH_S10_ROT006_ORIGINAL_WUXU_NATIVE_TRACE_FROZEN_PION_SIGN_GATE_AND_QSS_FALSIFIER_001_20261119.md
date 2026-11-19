---
artifact_id: IW_MECH_S10_ROT006_ORIGINAL_WUXU_NATIVE_TRACE_FROZEN_PION_SIGN_GATE_AND_QSS_FALSIFIER_001_20261119
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10
date: 2026-11-19 Europe/Warsaw
mode: ORIGINAL_AUTHOR_SOURCE_AND_MECH_S9_ACTUAL_NATIVE_ARTIFACT_READ_ONLY / NO_NEW_NATIVE_EXECUTION
status: ZIP_SHA_CRC_AND_16_OF_16_MEMBER_SHA_PASS / NATIVE_10000_ROWS_VERIFIED / 277_PREEV_CHARGE_QSS_RATIO_CHECK_PASS / 1456_POSTEV_FROZEN_SIGN_GATE_MISSED
ceiling: SINGLE_ORIGINAL_J22_TRACE_ONLY / NOT_EXACT_EVENT_TIME / NO_FULL_10D_COUNTERFACTUAL / NO_PAPER_ERROR / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# Mech-S10 ROT006 — original Wu–Xu native trajectory falsifies transfer of the ROT005 5-MeV pion sign example at one j22 PBH cessation bracket

## New scientific question

ROT003–005 derived correct classical conditions for source-on/off pion conversion in a frozen-temperature, constant-X, constant-baryon-density model. Its source-off signed integrated tail can reverse relative to initial signed pion RHS only when A*B > gamma_pi^2, and the original Wu–Xu coefficient choice allows such a condition for some neutron fraction only for T>4.294807511761714 MeV.

This ROT006 tests whether those conditions are met in an ACTUAL existing original-author 10D trajectory around the PBH source shutdown, with no new native run. Original Wu–Xu and BlackHawk firstness, Mech-S9 ROT012–013 native execution/source-floor firstness, Badacz original native T2 and LT9 original source-mode theorem are not transferred.

## Primary source and actual original native data

Direct original upstream Wu–Xu code read at Fenyutanchan/Primordial-Black-Hole author commit d395183674cace6c9906a8911bdeb7234ba4040d:
- arXiv-2509.05618/main-scan.jl, original blob b368ba55d5a493f7bc185909730f7fe5691f10d6, PBH evaporation flag 47, PBH number density zero on flag 60, nB definition 65, pion neutron RHS 90, common pion source 103, charge-specific density ODE 109-112.
- arXiv-2509.05618/tool_script-parameters.jl, blob 0d7198ff3557bdbd5753000bb07a7a7405cc24f5, original tau_pi 2.6033e-8s, eta_B 6.1e-10, Fc(T), pion sigma-v 1.5mbarn Fc and 1.7mbarn.

Original Mech-S9 one-trajectory author-native Julia actual source result: GitHub Actions run 43436800793 / artifact 14045176436, file size 713794 bytes. This turn ACTUALLY downloaded it; actual ZIP outer SHA256 71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486, CRC PASS, 16/16 internal manifest member SHA PASS, original 10000-row author_native_raw_hadron_history_10000.csv SHA256 45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1. Original one-run j22 M_init=1.1211744564709606e9 gram, beta=1.0058635310570255e-17 (slightly outside original scanned beta maximum 1e-17), Ycode=0.25239220435845267. Not a validated historical author published Fig5 producer.

## Thermal gate on 10,000 source records

Define gamma=1/tau_pi; A=(1-X)nB(T)*(1.5mbarn Fc(T)), B=X nB(T)*1.7mbarn, with nB=eta_B*2zeta(3)/pi^2 * (T_MeV*MeV_J/(hbar*c))^3, sigma-v area times c. All coefficients calculated from saved native T and X by independent Python stdlib arithmetic. No Julia/BlackHawk/PYTHIA/ODE invoked.

| Original sampled native state | T MeV | X | A/gamma | B/gamma | AB/gamma² | ABmax(any X)/gamma² |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 8544, last PBH active, time .334927351810113s | 1.48824851749403 | .47097045071722 | .046141667959 | .039832684868 | .001837946519 | .001844162932 |
| 8545, first PBH zero, time .33751037021169s | 1.48260941885709 | .472697125696049 | .045483359220 | .039525991307 | .001797774861 | .001803151476 |

Local threshold Tcrit=4.294807511761714 MeV is bracketed by original source indices 8267 (T=4.30659020578605 MeV, t=.039885655561227s) and 8268 (T=4.29007361640141 MeV, t=.0401929966970184s), BOTH of which have PBH still active. The original actual first PBH-zero index is 8545. All **1456 actual SAVED PBH-zero rows** are below 1.482610 MeV and have maximal frozen coefficient ABmax/gamma² at most **.001803151476**, more than 500 times BELOW the conditional integrated-tail inversion threshold 1; max actual-X AB/gamma²=.001797774861. Thus the synthetic T=5MeV source-off negative integral is NOT a demonstrated mechanism at this one native PBH source cessation bracket. This is a sample-anchored LOCAL-condition negative test, not a full time-varying 10D sign theorem.

## A second actual native-data test: charged pion population QSS

At every original alive PBH sampled state the original returned pion logarithmic densities are above the source floor. The actual stored pi-/pi+ ratio is exp(lograw_pi_minus-lograw_pi_plus); the local constant equal-source QSS prediction is (gamma+B)/(gamma+A). Over all **277 original alive** rows 8268..8544 below Tcrit, maximum absolute relative ratio discrepancy is **5.187343022783342e-5** and mean absolute discrepancy **2.582285768458466e-5**.

At actual last native active source row 8544:
- true stored pion charge ratio: 0.9939692660116087;
- recomputed source-constant QSS ratio: 0.9939692841959409;
- direct relative error: -1.8294662007534157e-8.

IF one were to **artificially force the source OFF at this exact saved PBH-active row** and then hold T,X,nB fixed while using the SAVED pion populations, the integrated post-source positive/negative contribution ratio would be **1.1444573935653823**, a strictly positive counterfactual frozen tail. This is NOT the actual unknown source-off event, and no physical Yp, beta or full 10D perturbed trajectory follows.

Original saved postev 1456 rows have BOTH pion raw logs below -100 and floor-active flags, first demonstrated by Mech-S9 ROT013; do not interpret clamped raw postev densities as an equilibrated physical pion population.

## Temporal source and event bracket guard

The difference in SAVED output times from last PBH-active index8544 to first PBH-zero index8545 is:
  delta_t=0.0025830184015769864 s = 99220.92734517675 * tau_pi.

This is only the **width of a saved source-event bracket**, not a measurement of how long the pion population had been decaying since the actual evaporation event. The exact event could be anywhere between these saved rows and the numerical solver may have many internal steps. Original CSV cannot resolve nanosecond-scale after-source effect from this bracket; do not claim otherwise.

The independent nB(T) from original source constants agrees with original selected source snapshot nB in cm^-3 at 8544/8545 to relative ~1.84e-9; unit/interface sanity PASS.

## Actual read-only execution and negative control

This turn executed a new standard-library Python auditor on ACTUAL original native ZIP bytes, checks outer SHA256, ZIP CRC, 16/16 member checks, full 10000 row CSV SHA256 and source indices, one-way PBH_zero, 1456 postev row coefficient maxima, crossing at 8267/8268, 277 active source ratio QSS, and signed frozen forced-off ratio at 8544. A disposable one-byte corrupted copy of the ZIP was correctly rejected by source hash before result computation (FAIL_CLOSED PASS). Original native Julia source was NOT rerun.

Reusable code:
- mech_s10_rot006_original_native_trace_referee.py SHA256 b50ac4d538a460751211f52366a37c621cf313b32d40674f169b9ecba389cbf3
- its executed output mech_s10_rot006_original_native_trace_referee.json SHA256 936d6291b14eb94653eb938cde162ee5bb1718a82fd17e41d19b36f071e607a1
- small code/output/README/repro report bundle ZIP SHA256 09d73769d84460cf33aa1d080cdc04086c36ed524133253ac3f376fcfe0e808b, CRC+3/3 member SHA PASS. Original native ZIP is not duplicated inside bundle; source link is Actions run 43436800793, artifact 14045176436.

## B1 currentness, negative knowledge, stop/reopen

Direct B1 issue #16, Git commits and Slack on 19 November have not established Moderator replacement-executor approval for Mech-S10's previously authorized **one** native T2R 68-call (j22,j62, orig/E5); Badacz had consented but this did not replace Moderator's Mech-S9-specific lease. Hence T2R_HOLD_NO_EXEC, no duplicate run. LT9 ROT006 with AUD3/XH-S7 found the original Kohri/KY per-charge historical implementation NOT established (SEMANTICS_OPEN); LT9 ROT007 updated observational Yp target on existing native original rows but current E5 target root was not bracketed. These science questions are distinct from this source-only trace test. E4 and historical Fig5 runtime physical source remain open.

**Source-status conclusion**: for this single actual original author j22 native trajectory, the ROT004–005 frozen 5-MeV postev integrated inversion scenario is **not supported near source-off**. Local AB/gamma² at cessation is ~0.0018, all saved postev states miss the sharp algebraic gate, and save-time spacing is ~99,221 pion lifetimes. This does NOT falsify the general classical theorem, nor rule out actual time-varying kinetic sign behavior or a different PBH mass/beta trajectory. No physical PBH bound, paper error, novelty, CANON or EXEC_SIGN.

FINAL: ORIGINAL_NATIVE_ACTUAL_ARTIFACT_SHA_CRC_PASS / 16_OF_16_MANIFEST_PASS / 277_NATIVE_PREEV_CHARGE_QSS_PASS / ALL_1456_SAVED_POSTEV_AB_GAMMA_GATE_MISSED / EXACT_EVENT_HOLD / ONE_J22_ONLY / T2R_HOLD / NO_NEW_JULIA / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
