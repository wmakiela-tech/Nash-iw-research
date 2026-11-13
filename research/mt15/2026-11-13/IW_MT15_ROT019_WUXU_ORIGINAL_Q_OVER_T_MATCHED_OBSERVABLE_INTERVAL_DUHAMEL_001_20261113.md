---
artifact_id: IW_MT15_ROT019_WUXU_ORIGINAL_Q_OVER_T_MATCHED_OBSERVABLE_INTERVAL_DUHAMEL_001_20261113
created_at: 2026-11-13
origin_cell: IW_MT_SUCCESSOR_14 / MT15
exposure: PUBLIC
document_type: INDEPENDENT_ORIGINAL_NATIVE_ONE_TRACE_SOURCE_MATCHED_READOUT_MATHEMATICAL_INTERVAL_AUDIT
status: ORIGINAL_10000_SOURCE_SHA_PASS / Q_OVER_T_NATIVE_Y_REPLAY_PASS / MATCHED_SCALAR_DELTA_X_AND_Y_INTERVAL_PASS / INDEPENDENT_MPMATH70_PASS / CLEAN_OFFLINE_REPLAY_PASS
claim_ceiling: ONE_MECH_S9_ORIGINAL_10D_SAMPLED_J22_TRACE / POSTEV_FIXED_NATIVE_BACKGROUND_WEAK_ONLY_SCALAR_COMPARATOR / NOT_ORIGINAL_UNCLAMPED_10D_OR_PHYSICAL_Yp_OR_PBH / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# MT15 ROT019 — conditional source Q/T-matched Duhamel output intervals for original Wu–Xu

## 0. Exact source and priority

ORIGINAL Wu–Xu JCAP 02 (2026) 063, author frozen public repository Fenyutanchan/Primordial-Black-Hole commit d395183674cace6c9906a8911bdeb7234ba4040d; main-scan.jl source Git blob b368ba55d5a493f7bc185909730f7fe5691f10d6. At original source lines 206–211 the function magic computes the code output by linear interpolation of original neutron fraction Xn against Q/T, followed by Ycode=2X/(1-X). This is NOT identical to the published manuscript heuristic Yp≈2X and is not a PCHIP-interpolated time-evaluation.

FIRSTNESS: LT8 source log-six-hadron numerical floor; Mech-S9 ROT012/013 FIRST original Julia full10D one-input native 10000-sample six-hadron raw history; INT9 ROT022/024 first original signed floor-rate / on-path integral; MT15 ROT017 first separate same-native-background weak-only scalar Duhamel comparator; MT15 ROT018 first interpolation-free original-source sample D bounds; INT9 ROT025 FIRST sourced the Q/T readout-vs-PCHIP mismatch and first matched single-point D estimate. MT15 ROT019 independently extends those known results to a source-operator matched INTERVAL and formal code Y output INTERVAL. Classical linear positivity and monotone rational map, NO mathematical or physics novelty.

ORIGINAL exact native input: Mech-S9 Actions run 43436800793, artifact ID14045176436; untouched original 713794-byte GitHub ZIP SHA256 71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486; original 10000x19 source CSV SHA256 45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1; original source ZIP CRC and ALL 16 internal SHA256 manifest entries PASS. One original source-native j22 call at log10beta=-16.9974609375; beta is +0.586% above original author scan beta max 1e-17, so this is a real callable input but not an original published scan node. No source Julia code modified, no alternate 10D run.

## 1. Correctly typed model comparator and exact interval theorem

At first saved original nPBH-zero sample8545, all six native original hadron logarithms are below -100, and all six source floor flags remain ON through 1456 saved postev rows. Conditional on original SOURCE differential equations holding continuously and six logs remaining clipped after the sample, original clamped Xc obeys scalar forced weak equation on the original frozen native T(t):

    Xc_dot = aweak(T) - kappa(T) Xc + f_floor(T,Xc)

with kappa=Gamma_n(1+exp(-Q/T))+1/tau_n,
f_floor=k0*((1-X)A(T)-62.7X),
A(T)=1.5 Fc_pi(T)+31 Fc_K(T)+35,
k0=1.451486837240379e-19 sec^-1.

The DIFFERENT auxiliary weak-only comparator W is defined by W_dot=aweak(T)-kappa(T)W on exactly the same T(t), with W(start first zero sample)=Xc(start). Thus D=Xc-W satisfies D_dot=f_floor(T,Xc)-kappa D, D(start)=0. This is NOT the physical change produced by removing the floor in the full author 10D code; those six hadron states remain dynamically coupled in the true source.

MT15 ROT018 source-ODE-monotone postev sample calculus gives at all 1456 original native samples the separate numerical lower and upper node constraints L_i<=D(t_i)<=U_i, conditional on those actual saved numbers representing an original solution with source ODE restrictions. Those L/U arrays are RECOMPUTED in ROT019 from original native CSV, not imported from the published ROT018 JSON.

For an original source target Tstar between adjacent native sample temperatures T_i>Tstar>T_(i+1), the AUTHOR-Q/T-LINEAR interpolation weight is

    theta=(1/Tstar-1/T_i)/(1/T_(i+1)-1/T_i),  0<theta<1.

The common Q cancels. The source readout x=L_QT(Xc)=(1-theta)Xc_i+theta Xc_(i+1). If the weak-only comparator is read out by precisely THE SAME source Q/T operator L_QT, then its output difference d=L_QT(Xc)-L_QT(W)=(1-theta)D_i+theta D_(i+1). Therefore, because both weights are nonnegative, EXACT mathematically:

    d_lower=(1-theta)L_i+theta L_(i+1)
    d_upper=(1-theta)U_i+theta U_(i+1)
    d_lower<=d<=d_upper.

This is a strictly different bounded quantity than D at the UNKNOWN actual instant when T(t)=Tstar, which ROT018 correctly bounded by the broader [L_i,U_(i+1)]. A narrower code-output bracket is not an improved continuous true-trajectory error bound.

For actual code G(x)=2x/(1-x), the matched formal paired output difference is exactly

    G(x)-G(x-d)=2*d/((1-x)*(1-x+d)).

G is increasing on physical x<1, so substitute d_lower,d_upper in this exact identity for an interval. For the distinct manuscript-like 2X operator the paired interval is 2*d, not G interval and not physically corrected helium.

## 2. Recomputed ORIGINAL 10000-row native results, including code output verification

At Wu–Xu original code T0=.07818527068831994 MeV, native source sample Q/T bracket one-based 9401–9402, theta=.9007198835246876. Actual independently recomputed source x=.11205517576826313, Ycode=.25239220435845194, matching the actual original native Julia printed Ycode=.25239220435845267 within 7.3e-16, the expected finite output decimal discrepancy.

At Badacz corrected SBBN T1=.0996888512474581 MeV, native source bracket 9326–9327, theta=.26317486326243933. Recomputed x=.12588190883956388, formal G(x)=.28802037187549623. T1 is NOT an actual original code magic endpoint for this run; its formal G(x) is only an additional matched target.

EXACT conditional bound results from original source sample L/U recurrences:

target   matched d=L_QT(D) lower  matched upper        matched formal delta CODE Y lower       upper
T0       2.202762365163523e-15 2.2056827742579078e-15 5.587604819523828e-15   5.595012832384787e-15
T1       1.2216118477080871e-15 1.2231916290604223e-15 3.197591746865649e-15 3.2017268539567897e-15

Relative source matched X-difference interval widths: T0 .001324915702486514 or .13249%, T1 .00129235856161597 or .12924%. ROT018 unknown exact event-time interval widths were T0 ~.90158%, T1 ~.91896%: the source-matched discrete readout bracket is 6.8x / 7.1x narrower, ONLY because it bounds a more specific operator.

INT9 ROT025 independent prior matched point estimates d(T0)=2.204224813545911e-15 and d(T1)=1.2224031939080372e-15, along with code Y differences 5.5913145177459196e-15 / 3.1996631102718086e-15, are INSIDE the new ranges, 4/4 PASS, and retain original INT9 FIRSTNESS. At T0 an UNMATCHED PCHIP(time) original readout changes X by ~1.06e-8 versus native Q/T original interpolator and code Y by ~2.68e-8, i.e. >4 million times the floor comparator size; INT9 first identified those numerical operator-mismatch facts. It is a formal output-type mismatch, NOT a physical solver-error measurement; the matched paired readout algebra cancels the common interpolation discrepancy.

## 3. Actual executable reproducibility

Actually executed standalone Python mt15_rot019_source_matched_readout_bounds.py from ORIGINAL native 10000 samples, SHA256 97ebf11367e4debf147cd61f322615f8ae8a9dc4db284025f24af18fb2eb16d6; full actual JSON mt15_rot019_results.json SHA256 e35b1871d179ffb437fceafcf7b7fca34f2e8bf89bafed4afcbf7307a8a12dc4. Primary source ZIP SHA lock and original inner 16 SHA passed before arithmetic, full 1455 postev time nodes recomputed. A separate independently implemented 70-decimal-digit mpmath source loop took the original decimal CSV samples, recalc all 2910 endpoint recurrences, original Q/T weight and exact rational map; worst relative binary64 versus independent 70dps for tested twelve event scalar values 1.8832591139837284e-13. This is numerical crosscheck NOT formal output error enclosure.

Independent verifier mt15_rot019_verify.py SHA256 1cc495606565fcc224ba65c55eedb323cca1a2032c1d7f720fcabdbebc72e28f: complete reexecution original JSON byte-for-byte PASS; 1-byte mutation in source ZIP FAIL_CLOSED as desired; 4000 seeded independent 65-digit random source nodewise D choices constrained by L_i,U_i at actual two original event brackets, all 4000 resulting matched affine differences and nonlinear code-Y deltas strictly inside source brackets PASS, exact rational identity independently checked. Random probes are implementation falsifiers; positivity of source interpolation proves the inequalities.

FULL self-contained OFFLINE ZIP mt15_rot019_source_matched_qt_duhamel_bounds_20261113.zip, exactly 722388 bytes SHA256 d9576529a8696df542d501ad4cd05bd5766462d1776f77045196e0f5c6ff8940; contains UNTOUCHED source-native Mech-S9 original artifact ZIP (with its original 10000-row CSV and all hashes), producer Python, output JSON, verifier, README and SHA256_MANIFEST for all five payloads. Package ZIP CRC PASS, manifest five-of-five SHA256 PASS, original nested ZIP CRC and 16 original SHA256 PASS, extraction to a BRAND-NEW separate temporary folder and Python -I full verify run regenerates results JSON BYTE-IDENTICALLY with 4000 controlled falsifiers PASS. The full ZIP is conversation-local; NO claim GitHub or BW contains these native raw bytes.

## 4. Explicit negative knowledge

This is source-typed **operator-matched OUTPUT** for a separate forced clamped-vs-weak-only comparator, not the actual physical clamped-vs-unclamped original full 10D. The source original Julia numerical solver's absolute error at e-15 X scale is not independently certified. The original source B1 primary X(T0) remains proposed, not automatically frozen by MT15; Mech-S9/Badacz coowners and Moderator authorize original Julia per-run. The event 8544->8545 native X increases by +.001726674978829, so no monotonicity or D source comparison back-propagates across actual PBH cutoff bracket. All physical E4 unknown below 1e9g hadron generator, code-v2/source-paper helium and EOS issues remain. No physical corrected Yp, PBH excluded mass/beta, new physical mechanism or mathematical novelty, no I3 or BW receipt, no owner override/task cascade.

VERDICT: ORIGINAL_SOURCE_QT_CODE_READOUT_PASS / MATCHED_SCALAR_D_AND_G_INTERVAL_PASS / INDEPENDENT_70DPS_AND_4000_FALSIFIER_PASS / CLEAN_OFFLINE_REPLAY_PASS / E4_SOURCE_HOLD / NO_PHYSICAL_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / GITHUB_PENDING_BW_INGEST.
