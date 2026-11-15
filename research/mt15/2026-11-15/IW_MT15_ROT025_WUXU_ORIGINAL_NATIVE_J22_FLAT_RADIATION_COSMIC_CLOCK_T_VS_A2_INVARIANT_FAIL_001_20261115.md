---
artifact_id: IW_MT15_ROT025_WUXU_NATIVE_J22_FLAT_RADIATION_COSMIC_CLOCK_T_VS_A2_INVARIANT_FAIL_001_20261115
created_at: 2026-11-15
origin_cell: IW_MT_SUCCESSOR_14 / MT15
exposure: PUBLIC
type: INDEPENDENT_ORIGINAL_AUTHOR_SOURCE_EXACT_ODE_INVARIANT_VERSUS_REAL_NATIVE_10D_SAVED_STATE
status: EXACT_ORIGINAL_FLAT_SOURCE_THEOREM_PASS / REAL_NATIVE_SAVED_CLOCK_INVARIANT_NUMERIC_FAIL / LAST_PRINT_DIGIT_INTERVAL_EXCLUDES_ZERO / CLEAN_SELF_CONTAINED_REPLAY_PASS
claim_ceiling: NO_SOLVER_CAUSAL_IDENTIFICATION / NO_NEW_JULIA / NO_PHYSICAL_Yp_BBN_PBH / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# MT15 ROT025 — Original Wu–Xu j22 cosmic clock fails exact flat-radiation t(a²) invariant in recorded native dense-output

## 1. Original science, firstness, source custody

ORIGINAL AUTHORS FIRST: Wu–Xu, JCAP 02 (2026) 063; original public frozen author Julia v2 Fenyutanchan/Primordial-Black-Hole at commit d395183674cace6c9906a8911bdeb7234ba4040d. Source full 10D main-scan.jl Git blob b368ba55d5a493f7bc185909730f7fe5691f10d6, source complete 1000-row thermal file arXiv-2509.05618/data/ext/N_around_m_e.csv Git blob 93f2494f026c5d0587ea40fe08bb938dd9d01fa8, original inverse LUT interpolation helper blob 0437c032bdc4bafca6cb634c0db4cd2c46fb7efc.

IN-PROJECT FIRST: Mech-S9 ROT012/013 FIRST actual original-author single j22 Julia 10D 10000-sample result. Mech-S9 ROT002 FIRST EOS entropy nonadiabatic source inconsistency. KN14 ROT006 FIRST recorded 19-row below-thermo-knot exact flat-source aT noninvariance with decimal rounding excluded. MT15 ROT020 FIRST distinct original saved PBH cutoff mass invariant FAIL; MT15 ROT022–024 independently original native source entropy and residual window audits, without identifying solver cause. THIS ROT025 is a logically different, original-native cosmic time **t versus a²** radiation clock source-ODE invariant test, not a new physics theorem.

ACTUAL unchanged Mech-S9 original provider Actions run43436800793 artifact14045176436 native ZIP 713794 bytes, SHA256 71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486; original full 10000×19 source-native CSV SHA256 45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1, original ZIP CRC PASS, 16/16 provider manifest SHA256 PASS. All original 10000 row source decimal strings were read directly, not substituted or re-simulated.

## 2. EXACT continuous ODE theorem, independent of H normalization

Original main-scan.jl RHS uses eta=ln a, source nPBH=0 after PBH threshold, rho_total=rho_SM, H=sqrt(rho_SM/(3 M_Pl²)) and d ln t/deta=1/(H t). Source no-PBH d ln rho_SM/deta=-4+q_rho/(3+q_s), q_j=dln g_j/dlnT.

Original g_rho,g_s table constant-extrapolates below its first literal source row:

    0.01400298972685787,3.3654513231275924,3.9120400850273933

The original rho-to-T inverse separate 1000-node logarithmic LUT uses T=.01...1e6MeV and geometric node18 at .013936192742241425MeV, below first original g table T. Its bracketing rho nodes then both have constant g_rho, making the original source inverse LUT EXACTLY log-linear rho proportional T⁴ in that subdomain. ALL real native rows9860..9878 are in T=.0129638469638243... .0138928716885572MeV, strictly below node18 and above LUT minimum .01MeV. At all 19 saved rows nPBH returned zero, actual mass is constant below cutoff and all 6 original source effective-floor flags are true.

Thus for any EXACT continuous original author ODE trajectory remaining on this source branch: q_rho=q_s=0, rho_SM=C*a^-4, H=H0*a^-2, dt/deta=1/H=a²/H0, and therefore

    t(a)=C0+C1*a²

with constant C1>0. Any pair of disjoint finite source clock slopes (t_j-t_i)/(a_j²-a_i²) must agree exactly. This is ordinary classical radiation Friedmann theory, not novelty; it does not require a physical Hubble value, g(T) other than eligibility, hadron rate, or author paper-v2 helium definition.

## 3. ACTUAL native source failure with explicit printed-decimal uncertainty enclosure

Use ORIGINAL source native saved row9860 (t about 6851.11890492934sec), row9869 (about 7341.04064367485sec), row9878 (about 7865.98861017159sec), source original a and t exact decimal tokens. Define

    D1=(t9869-t9860)/(a9869²-a9860²)
    D2=(t9878-t9869)/(a9878²-a9869²).

Independent Decimal95 original-source evaluation:

    D1/D2-1 = +0.0001578618024555685350049218295151688222282056966847...

= +0.01578618%, whereas exact author source continuous flat-radiation theorem demands ZERO. All 18 consecutive saved native source secants in rows9860..9878 have peak-to-peak relative span 0.0002504558085755802847 = +0.02504558% of middle slope. For late 9900..10000 an independent source exact flat-domain control has smaller peak-to-peak 0.0000078514944954424 = 7.85149 parts per million; no claim that it is exact zero.

Each native decimal a,t is conservatively allowed plus/minus half of its LAST DISPLAYED DECIMAL DIGIT. Calculate positive time increments and positive squared-scale-factor increments via worst-case Decimal95 rectangle endpoints, propagating all six printed source numbers independently and allowing common middle point to vary independently across the two fractions (safe overapproximation). The resulting original CSV print-compatible source slope-ratio gap lies in:

    [0.00015786180222402408444525629983285256...,
     0.00015786180268711298556464154801787606...].

This interval EXCLUDES zero by wide margins. Thus truncation/rounding of the original printed source native CSV alone CANNOT repair this recorded state inconsistency. It is a very strong numeric identity guard for printed data, not a formally outward-rounded BigFloat interval solver convergence result.

Firstness-protected independent KN14 ROT006 aT ratio on same recorded 9860 vs9878 is +6.5841910479949279e-8, reconfirmed in this original source replay; it is a distinct source invariant and is not assigned to MT15.

## 4. Exact executed clean source replay and negative controls

Current conversation local independent SELF-CONTAINED original native source ZIP:
mt15_rot025_original_native_flat_cosmic_clock_invariant_20261115.zip
bytes 724450; SHA256 772510eb2583dd26bb79220f0111a38d142b46fd579f7c0387ff2f60b93591aa.

It contains UNCHANGED source Mech-S9 original Julia full 10000×19 CSV nested in original ZIP, standalone original-data-reading Python Decimal95 source program, actual executed full JSON, separate independent verifier, verifier actual output, README and 6 member SHA256 manifest.

ACTUAL program mt15_rot025_clock_invariant.py SHA256 2f8a1c6c87ef95e8e6f72da776891addaa07b2c3867b10adc29283002ba4be67; actual full results JSON SHA256 e78d34e782f23ad24c421ffa25d3fa048623b3326c5d6173204a4d4377645b19; independent verifier code SHA256 14c10bc286ffc3541827cf6e0ad20363cac159e73f775949297da4469ee4ec40.

Outer ZIP CRC PASS, payload 6/6 SHA256 PASS, nested original native ZIP CRC PASS and its 16/16 original manifest SHA PASS; extracted to a BRAND-NEW empty temp folder, ran Python -I source script and Python -I verifier, full original-source output JSON BYTE IDENTICAL PASS and verifier output byte identical PASS. Verifier 2500/2500 independently synthetic EXACT t=C0+C1a² radiation trajectory positive controls PASS; 2000/2000 randomly selected independent source printed last-digit perturbations included in conservatively bounded slope-ratio interval PASS; modified original owner ZIP one-byte mutation rejected BEFORE science FAIL_CLOSED_PASS. No Julia execution, no new original PBH input or actual adaptive solver step log.

Full author thermo 1000-row source table was DIRECTLY GitHub-read and Git blob validated for original first-row and lookup recipe in this turn, but is NOT included in offline ZIP. It is not needed for the numeric t-a² replay after source first-row eligibility is pinned; do not claim the original full table 1000-row is in this ZIP.

## 5. Explicit scientific ceilings

This witness FAILS the exact author ODE invariant in the SAVED NUMERIC dense-output original 10D array. It DOES NOT refute the exact ODE mathematics, identify solver internal step or dense-output interpolation error cause, measure the true source ODE global error, or imply a direct physical problem in Yp. The native source CSV contains 10000 dense-output interpolated points, NOT 10000 accepted solver steps. The source times 6851–7866sec and T~.013MeV are much later than original T0=.078185MeV, and there is no certified transfer of this clock mismatch to the original neutron endpoint. No physical hadron generator E4 below source first M=1e9g was verified. Original j22 beta exceeds paper historical scanned maximum by ~0.586%; not an author published on-grid point.

Any new tolerance/source event output or alternate original Julia calculation remains explicitly Moderator-authorized B1 with Mech-S9 and Badacz as owners; this ROT025 did not request or perform any such action. No owner acceptance, external I3 referee, BW readback, CANON, EXEC_SIGN or physical novelty inference.

VERDICT: EXACT_ORIGINAL_SOURCE_RADIATION_CLOCK_THEOREM_PASS / ORIGINAL_NATIVE_SAVED_TIME_CLOCK_INVARIANT_NUMERIC_FAIL / LAST_SOURCE_DECIMAL_DIGIT_ROUNDING_EXCLUDED / CLEAN_INDEPENDENT_SOURCE_REPLAY_PASS / RUNTIME_SOLVER_CAUSE_HOLD / E4_SOURCE_HOLD / NO_PHYSICAL_BBN_PBH / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_PENDING / NO_NEW_TASK_CASCADE.
