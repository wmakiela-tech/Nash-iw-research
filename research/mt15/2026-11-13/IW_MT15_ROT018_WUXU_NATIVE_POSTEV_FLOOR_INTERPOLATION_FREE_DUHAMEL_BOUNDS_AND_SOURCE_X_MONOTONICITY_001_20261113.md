---
artifact_id: IW_MT15_ROT018_WUXU_NATIVE_POSTEV_FLOOR_INTERPOLATION_FREE_DUHAMEL_BOUNDS_AND_SOURCE_X_MONOTONICITY_001_20261113
created_at: 2026-11-13
origin_cell: IW_MT_SUCCESSOR_14 / MT15
exposure: PUBLIC
document_type: INDEPENDENT_NATIVE_SOURCE_TRACE_CLASSICAL_COMPARISON_AUDIT_WITH_EXPLICIT_EPISTEMIC_INTERVAL
status: ORIGINAL_NATIVE_MECH_TRACE_SHA_AND_16_MEMBER_SHA_PASS / SOURCE_THERMAL_1000ROW_MONOTONICITY_PASS / 1455_SOURCE_ENDPOINT_X_BARRIERS_PASS / DAMPED_DUHAMEL_INTERVAL_55DIGIT_PASS / CLEAN_OFFLINE_REPLAY_PASS
claim_ceiling: SOURCE_NATIVE_ONE_J22_NUMERIC_TRACE_USED_AS_FIXED_SAMPLE_CONSTRAINTS / MONOTONE_POSTEV_SOURCE_ODE / SAME_BACKGROUND_SCALAR_WEAK_COMPARATOR / NO_ALTERNATE_10D / NO_PHYSICAL_Yp_OR_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# MT15 ROT018 — source-ODE conditional interpolation-free Duhamel brackets for the REAL Wu–Xu j22 native postevaporation floor

## 0. Firstness, source priority and exact data

ORIGINAL publication and physical source: Wu–Xu, JCAP 02 (2026) 063, frozen original public author Git source Fenyutanchan/Primordial-Black-Hole @ d395183674cace6c9906a8911bdeb7234ba4040d, code main-scan.jl Git blob b368ba55d5a493f7bc185909730f7fe5691f10d6. Original author thermodynamics 1000×3 N_around_m_e.csv Git blob 93f2494f026c5d0587ea40fe08bb938dd9d01fa8, interpolation source Git blob 0437c032bdc4bafca6cb634c0db4cd2c46fb7efc; original hadron conversion parameters blob 0d7198ff3557bdbd5753000bb07a7a7405cc24f5.

FIRST within project: LT8 ROT014/015 source floor discovery, raw/effective distinction and first analytic sensitivity warning; AUD2 ROT003 first conditional terminal no-floor criterion; INT9 ROT022 first signed dimensional pointwise floor bound and ROT024 independent on-path undamped integrals; Mech-S9 ROT012/013 FIRST actual original-author untouched 10D one-point Julia trajectory, 10000 samples and 6 raw hadrons, actual floor flags. MT15 ROT017 FIRST separate fixed-native-background weak-only SCALAR Duhamel comparator, LINEAR and PCHIP sampled trace interpolation to numerical D values. MT15 ROT018 improves the **epistemic** treatment of interpolation in that comparator and derives source-ODE restricted monotonicity; it does not take over physics ownership, redo native Julia or claim mathematical novelty.

ORIGINAL native source: Mech-S9 Actions run 43436800793, artifact 14045176436, UNMODIFIED downloadable 713794-byte ZIP SHA256 71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486. It contains original 2157565-byte 10000×19 native CSV SHA256 45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1, which this rotation ACTUALLY read. Outer ZIP CRC PASS, **all 16/16 original inner SHA256 manifest files PASS**. Original j22 Minit=1.1211744564709606e9g, log10(beta)=-16.9974609375, full native author 10D at one source input (NOT the original JCAP final figure producer). Original first PBH-zero one-based sample 8545, t0=.33751037021169s, T=1.48260941885709MeV, native X=.472697125696049. All six original raw log-hadron values far below -100 at first zero and all subsequent 1456 saved records; source effective RHS = exp(-100)GeV³ per species after the source switch; original native preev floor flags 0 and postev all 8736 of 8736 TRUE. This is the native finding of Mech-S9, not new to MT15.

## 1. Exact conditional mathematical question

After source first sampled zero-PBH index 8545, **if** the actual original source ODE branch has no new PBH injection and all six hadron logs stay below -100, the six effective hadron concentrations in the neutron RHS are identically the floor exp(-100)GeV³. The original Julia equations then give, for physical source time t:

    Xdot = a_w(T) - κ_w(T) X + f_floor(T,X),

    f_floor(T,X) = k0 [(1-X) A(T) - 62.7 X],
    A(T) = 1.5 Fc_pi(T) + 31 Fc_K(T) + 35,
    k0 = 1.451486837240379e-19 s^-1.

Weak birth rate a_w=Gamma_n exp(-Q/T), κ_w=Gamma_n(1+exp(-Q/T))+1/tau_n, Gamma_n=(255/tau_n)(12+6q+q²)/q^5, q=Q/T and source Q=m_n-m_p. This reproduces the source floor term exactly when every species is clipped. It is **not** the exact effective-minus-raw density correction, since raw densities remain mathematically positive, but in the original saved postev records they are exponentially negligible. For the comparator, only the effective floor term appears; no original source input has been changed.

Define a different, specified weak-only comparator W on the SAME externally frozen native T(t):

    Wdot = a_w(T_native(t)) - κ_w(T_native(t)) W,
    W(t_8545)=X_native(t_8545).

For the true clamped-native X trajectory (if it obeys the exact source ODE and this frozen background) the restricted difference D=X_native-W satisfies EXACTLY

    Ddot=f_floor(T_native,X_native)-κ_w(T_native)D,  D(t_8545)=0.

That is a classical Duhamel identity; it is NOT the result of solving alternate Wu–Xu 10D, removing a numerical floor from all ODE states, or calculating a physical helium error. The original native numerical CSV is treated as a constraint on a source-ODE branch; no solver-error certificate exists at the 1e-15 level.

## 2. Independent direct original thermodynamics makes temperature decrease

This rotation independently fetched the authentic **complete 1000-row** author N_around_m_e.csv directly from the connected original frozen GitHub source; author blob verified 93f2494. Exactly 723 piecewise-linear-in-logT source interpolation cells intersect the *recorded postev temperature range* T in [.00810973699892033, 1.48260941885709] MeV; the author source has CONSTANT extrapolation for g_rho and g_s below its first tabulated T=.01400298972685787 MeV. The fact that final native T is BELOW the first 1000-row thermodynamic node was handled explicitly, not extrapolated with a source-unjustified derivative.

Write q_rho=d ln g_rho/d ln T, q_s=d ln g_s/d ln T. Each source table cell has g(T) affine in ln T, so q=slope/g has derivative -slope²/g² with respect to ln T; extrema occur at cell endpoints. Exact original literal piecewise source endpoint checks produced global safe bounds over the covered range:

    -0.000789339557240243 <= q_rho <= .8291355487890821,
    -0.0007639987068695956 <= q_s <= .7110896673481276,
    4+q_rho >= 3.9992106604427597 >0.

The nPBH=0 author Julia line85 yields d ln rho_SM/d eta=-4+q_rho/(3+q_s), and these source-cell global q bounds give the mathematically conservative safe sign

    d ln rho_SM/d eta <= -3.723551081531564 <0.

Below the thermal table Tfirst, q_rho=q_s=0 and the derivative is exactly -4 in the frozen author's interpolation rule. Since source rho_SM(T) ∝ g_rho(T)T^4 has log derivative 4+q_rho>0 and the original author inverse T(rho) uses monotone log-rho/log-T interpolation (linear extrapolation below its constructed inverse boundary), the actual author code AFTER nPBH=0 has STRICTLY decreasing rho_SM and source temperature T(t). The 1000-row source result is preserved separately, with original Git SHA, source formula and calculated q extrema, in the pinned original-source certificate:

    research/mt15/2026-11-13/mt15_rot018_author_1000row_thermal_monotonicity_source_certificate.json

The thermodynamic 1000-row source JSON check was EXECUTED directly in the connected V8 environment on the original Git file. The 56KB original source thermodynamic table is NOT packaged in the offline 10D CSV replay ZIP, so the ZIP itself verifies the native original trace plus mathematical D bounds but does not reperform this separate connected source-table check. This is a mathematical source-recipe sign test, not a new original Julia run, not a formal directed rounding enclosure, and not an independent high-temperature physical EOS validation.

## 3. Source-neutron ODE plus recorded endpoints certify continuous X decline postev

The mere fact that all sampled X_i decrease does NOT prove intersample monotonicity. In fact a C-infinity bump supported in one tiny sample gap can preserve every source CSV endpoint but temporarily lift X to .9, changing the source floor forcing sign. Such arbitrary smooth bumps do NOT obey the fixed original Julia source ODE.

The key stronger source-aware guard avoids ASSUMING continuous X monotonicity without checking it. Define the actual postev neutron instantaneous relaxation rate and source equilibrium:

    K(T)=κ_w(T)+k0[A(T)+62.7] >0,
    B(T)=a_w(T)+k0 A(T) >0,
    h(T)=B(T)/K(T), so Xdot=-K(T)[X-h(T)].

Given original postev T monotonic in each native time slab [ti,ti+1], a_w(T) is increasing in T, κ_w(T) increasing in T and A(T) DECREASING in T due the two source Coulomb factors. Hence over slab i,

    h(T) <= Hi := [a_w(T_i)+k0 A(T_(i+1))]/κ_w(T_(i+1)).

The denominator drops the positive floor loss and hence is conservative. Now if the RECORDED source endpoint satisfies X_(i+1)>Hi, then no continuous solution of this exact source ODE could have X(t)≤Hi at an earlier time in the slab and return above Hi: the RHS at X=Hi always points nonpositively. Therefore X(t)>Hi>=h(T(t)), and **Xdot(t)<0 throughout the continuous slab**. This is a classical forward-invariance/backward endpoint barrier, not a numerical interpolation claim.

All **1455** consecutive ORIGINAL native postev source sample slabs passed X_(i+1)>Hi. Minimum ratio X_(i+1)/Hi is **1.1993856694751603**, native sample pair 8614–8615 (source T about 1.13928MeV; ending X=.296997422219669, source conservative Hi=.24762462131937282). Strict margin ~19.94%. This gives a source-ODE conditional proof of continuous X monotonicity on every covered slab, assuming true original solver trajectory is sufficiently close to the printed samples for the strict inequalities to remain true. The source log-hadron equations after production cutoff have nonpositive decay/collision RHS for every positive hadron and neutron fraction in [0,1], so raw hadrons once below -100 cannot spontaneously re-emerge above the floor on the true source branch. There is no external verified numerical ODE solution error certificate, hence no unqualified continuum-trajectory data claim.

**Crucial EVENT BRACKET negative guard:** between original last active-PBH sample 8544 and first zero-PBH sample 8545, native X actually INCREASES from **.47097045071722 to .472697125696049**, i.e. +.001726674978829, over .0025830184s. Thus the certified continuous postev monotonicity begins ONLY at the first sampled source zero index 8545. It is demonstrably false to extend it backward across that event bracket. That source jump includes earlier genuine hadron/weak dynamics and is NOT caused or explained by the tiny postev e^-100 floor estimate here. There is no full physical event-time or preev floor attribution.

## 4. New interpolation-FREE source-constrained Duhamel bounds

Along the postev source-ODE branch just certified conditional on original T and X source values, the floor source f(t)=f_floor[T(t),X(t)] is STRICTLY INCREASING: A rises as T falls, and X falls. Meanwhile the weak relaxation κ(t)=κ_w[T(t)] STRICTLY DECREASES. All 1455 consecutive source CSV node tests directly confirm f_(i+1)>f_i>0 and κ_(i+1)<κ_i.

For ANY continuous between-node rate functions satisfying the analytically established scalar order,

    f_i <= f(t) <= f_(i+1),
    κ_(i+1) <= κ(t) <= κ_i,

the classical scalar comparison principle yields the EXACT step-wise lower/upper recurrences with Δti=ti+1-ti:

    L0=U0=0,
    L_(i+1)=exp(-κ_i Δti)L_i + f_i * (1-exp(-κ_i Δti))/κ_i,
    U_(i+1)=exp(-κ_(i+1) Δti)U_i + f_(i+1)*(1-exp(-κ_(i+1) Δti))/κ_(i+1).

Then L_i<=D(t_i)<=U_i for all source postev sampled nodes. Because f/κ is increasing and D0=0, D(t) is NONDECREASING. For a target temperature T* reached somewhere in an unknown source sample gap ti-1..ti, the SOURCE-INTERPOLATION-INDEPENDENT event bracket is simply

    L_(i-1) <= D(t_T*) <= U_i.

No LINEAR, PCHIP, spline or event-time interpolation is used in these values. These bounds are **sharp enough for the provided sample spacing**, not claimed mathematically optimal over all original source-ODE trajectories. The underlying comparison inequalities are exact mathematical statements; endpoint numerical evaluations are binary64 cross-checked against 55-digit mpmath and have not been formally outward-rounded.

## 5. Actual original native trace numbers and honest uncertainty distinction

All values below are D for the separate source-defined SAME-T weak-only scalar comparator; **not delta Yp**, not actual error of native 10D, and not actual original author unclamped-vs-clamped physical difference. Target temperature is known to occur somewhere between listed sampled times.

| Target | Original source sample gap (1based) | Rigorous-under-assumptions D LOWER | Rigorous-under-assumptions D UPPER | relative width / midpoint |
| --- | --- | ---: | ---: | ---: |
| T1=.0996888512474581MeV | 9326–9327 | 1.2190680782154764e-15 | 1.2303224962027760e-15 | 0.91896% |
| T0=.07818527068831995MeV | 9401–9402 | 2.1875501714924986e-15 | 2.2073619854954410e-15 | 0.90158% |
| Last native sample10000, T=.00810973699892033MeV | exact recorded sample | 3.0926952009934006e-14 | 3.0977319018220719e-14 | 0.16273% |

The previous MT15 ROT017 PCHIP point estimates T1=1.2223991939725277e-15, T0=2.204222016560413e-15 and last=3.0952864265192953e-14 lie STRICTLY within these independent inequalities, 3/3 PASS. Previous LINEAR/PCHIP relative differences of 2.67e-6 near T0 (of D) are far smaller than the model-input-source monotonicity-only **0.0090158** width. Thus two interpolators agreeing closely IS NOT A CERTIFICATE for the true unknown continuous source trajectory.

This is a useful source-science **epistemic correction** without changing the meaning of ROT017: interpolation sensitivity and data-constrained continuum envelopes measure different uncertainties. Even our bracket is not an error bar on original Julia ODE accuracy or physical helium. In particular the very late D/X_native~.184% of a tiny X is NOT an absolute BBN effect, and T=.0081MeV is below native T0 where INT9's earlier T>=T0 pointwise source bound does not apply.

**Independent high precision:** A separately implemented 55 decimal-digit mpmath evaluation reads the original source 1456 time/T/X NUMERICAL DECIMAL TEXT independently of the binary64 arrays and recomputes EVERY lower and upper recursion (2910 values). Maximum relative difference against the first binary64 implementation is **1.0388743315215995e-13**. This is a rounding stability test, not an external reference to original solver truth. A different SciPy DOP853 synthetic-path evaluator tested 400 independently seeded nonlinear monotone T(t),X(t) histories against our source comparison recurrence: all 400 exact interval endpoints PASS. An adversarial one-byte original ZIP mutation was correctly rejected before analysis. The source-sample-only C-infinity interior bump negative test PASS: unless actual source ODE is invoked, the samples alone could conceal a nonmonotone X and a negative floor forcing; the bump is NOT an original Julia solution.

## 6. Reproducibility and stop

Independent executed code: mt15_rot018_native_duhamel_interpolation_free_brackets.py original SHA256 9a26224b64cc80b932e9da3e32c9d3befea72af84ff568943f7a7a32412d17ca; original full computed result JSON SHA256 c23251dbd7dcd651bb0d49bd5064fc33c0df7399a08647c95b959f673301e905. Separate verification code SHA256 4f2f979720068b6906d363838f0551fb1d84e3a1cc495df7be906bc4b0646f1d.

COMPLETE offline source-preserving ZIP mt15_rot018_original_native_monotone_duhamel_certificate_20261113.zip SHA256 85dc23c5d6a9517bfd1e0d84f9f4b1ff84c5f3e037f5d7907f4e4ee54894016c, size727295 bytes. It contains the **unmodified original Mech-S9 native Actions ZIP**, exact original code, result JSON, independent verifier, README and SHA256 manifest. ZIP CRC PASS, 5/5 payload SHA256 PASS, nested original ZIP CRC and original **16/16 SHA256 PASS**, and whole Python calculation re-executed from scratch in a NEW CLEAN temp directory producing JSON bytes identical to frozen result. Independent 400 synthetic continuous-path DOP853 controls and original-byte mutation rejection PASS in same clean replay. Archive is available in this conversation, NOT represented as already uploaded to public GitHub, BW or original authors.

SEPARATE original SOURCE THERMAL TABLE check is archived as GitHub JSON full source readback PASS, not part of this offline ZIP. The full original 56KB thermodynamic source CSV is accessible in the author's pinned Git repository. This separation is explicit; no false claim that the ZIP alone proves thermal source semantics.

This audit is a CLASSICAL scalar input-order comparison for ONE source-native 10D j22 output and an independent source-table monotonicity check. It does NOT execute another original author ODE, remove log floor, certify native ODE convergence, validate 100×100 original JCAP Fig5 producer, derive physical PBH beta or Yp correction, attribute the PBH event jump to floor, solve source E4 or propose new physics. No external novelty claim, canonical update, owner override, independent external I3 referee acceptance or BW writeback.

FINAL STATUS: ORIGINAL_NATIVE_TRACE_SHA_PASS / ORIGINAL_THERMO_1000ROW_SOURCE_SIGN_PASS / SOURCE_X_ENDPOINT_BARRIER_1455_PASS / DUHAMEL_INTERPOLATION_FREE_BRACKETS_PASS / MPMATH55_AND_400_SYNTHETIC_PASS / ORIGINAL_EVE_BRACKET_NEGATIVE_HOLD / NO_PHYSICAL_Yp_OR_PBH / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / GITHUB_PENDING_BW_INGEST / NO_NEW_TASK_CASCADE.
