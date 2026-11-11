---
artifact_id: IW_MT15_ROT006_WUXU_BADACZ_POSTHOC_NATIVE_CLOCK_SENSITIVITY_TO_MT15_ROT001_ROT004_001_20261111
created_at: 2026-11-11
origin_cell: IW_MT_SUCCESSOR_14 / MT15
exposure: PUBLIC
document_type: CURRENTNESS_ERRATUM_SOURCE_TYPED_CONDITIONAL_NUMBER_FRACTION_RECALCULATION
status: ORIGINAL_100ROW_5CHANNEL_NATIVE_CLOCK_BOTH_VERSIONS_SOURCE_JS_REPLAY_PASS
claim_ceiling: FIXED_FIVE_RATE_AUTHOR_V2_CONDITIONAL_HADRON_NUMBER_ONLY / TOLERANCE_TEST_POSTHOC / NO_SOURCE_EXECUTABLE_JULIA_REPLAY / NO_Yp / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# MT15 ROT006 — Late hadron-number fractions depend measurably on the native solver-tolerance version

## Source, owner and earlier computation FIRST

ORIGINAL SOURCE Wu–Xu original published JCAP article and public generator repository Fenyutanchan/Primordial-Black-Hole at immutable commit d395183674cace6c9906a8911bdeb7234ba4040d (original published code v2 NOT 2026 manuscript v3): `arXiv-2509.05618/data/out/hadrons_from_PBH.dat`, exact Git blob `06d0883a27b108692720422294ba2baacd381a64`, 100 masses × five hadron total-number rates. Original mass in GeV converted by 5.609588603804452e23 GeV per gram.

BADACZ is actual ORIGINAL Julia run owner. Original precommitted PREREG056 and first executed REVIEW057 r1 at commit 5b5521e, original default clock CSV `research/badacz/2026-11-11/data/heavy_end_clock.csv` Git blob `357f2f7656cb6c6bf4cfa419c7e33c4ca2d5f58e`, 8 source rows. Owner POSTHOC REVIEW057 r2 at commit `385b50a6fe54499caee68b8cca476eafc60d977b` added `research/badacz/2026-11-11/data/heavy_end_clock_tol1e-4.csv` Git blob `e0759b4a22c3282d3f11c58412c4b6543e6dc4c7`, 6 newly executed rows (j62/98/99 two betas), reltol=1e-4 abstol=1e-7. Original earlier run at reltol=1e-6 was interrupted, NOT evidence.

MT14 ROT029 FIRST independent per-channel original table quadrature; MT15 ROT001 FIRST mathematical sharp nonnegative unknown-subedge tail [L/T,1), KN13 ROT011 independently reproduced its default-clock four fractions to within 4.3e-15. MT15 ROT004 FIRST sharp CONDITIONAL unverified log-slope-band envelope with original DEFAULT eight clock rows. Mech-S8 ROT017 FIRST source-grid exact C-infinity continuation nonuniqueness and AUD1 ROT038 independent inter-grid C-infinity nonidentification prevent generalizing the illustrative below-grid slope interval to physical source. No firstness is appropriated here.

## Target, source typing, exact recomputation

Fix each of FIVE separately log-log interpolated original above-grid R_h(M); the native initial M0, event T_nuc and mass-only clock `M^2 dM` weighting. Define original source floor M*=1e9 g, normalized T=Σ_h ∫_[M*,M0] M² R_h(M) dM and L=Σ_h ∫_[M*,M(Tnuc)] M² R_h(M) dM, common factor 1/K canceled. Then lower conditional no-subedge fraction f0=L/T. For illustrative UNVALIDATED assumed subedge log-slope p_h(x)∈[1.15,1.35], same frozen K/clock, U_-=R*/(3-1.15) and U_+=R*/(3-1.35) with source R*=ΣR_h(M*)=646803.481830844 in normalized units, F_±=(L+U_±)/(T+U_±).

The exact analytic monotonicity partial-ID theorem is unchanged. The values of L and the numerical fraction depend on the source-native T_nuc event mass; the Badacz r2 posthoc diagnostic supplies a different native mass because of solver tolerance. No physiological data or new experimental inputs are used.

## Direct source-fetched, independently recalculated results

| Native case | M(T_nuc) DEFAULT [g] | M(T_nuc) POSTHOC 1e-4 [g] | f0 DEFAULT | f0 POSTHOC | delta f0 percentage points |
|---|---:|---:|---:|---:|---:|
| j98, log10 beta=-30 | 2.489091e9 | 2.394933e9 | .07986575027148589 | **.07342442178903678** | **-0.64413285 pp** |
| j98, log10 beta=-19.2 | 2.523417e9 | 2.389532e9 | .08225696033743585 | **.07306020931817925** | **-0.91967510 pp** |
| j99, log10 beta=-30 | 4.580037e9 | 4.571182e9 | .2516383331655924 | **.25074621764347693** | **-0.08921155 pp** |
| j99, log10 beta=-19.2 | 4.613379e9 | 4.570882e9 | .2550081455797033 | **.25071601442815517** | **-0.42921312 pp** |

Illustrative UNVALIDATED p∈[1.15,1.35] sharp source-model conditional numerical envelopes:
| Case | DEFAULT ROT004 Fmin..Fmax | POSTHOC Fmin..Fmax |
|---|---|---|
| j98 beta-30 | [.0973943354076881,.0994737357014973] | **[.09107571442659347,.09316967140095540]** |
| j98 beta-19.2 | [.0997399928499509,.10181398927697093] | **[.09071844021426176,.09281322026799405]** |
| j99 beta-30 | [.2652255979263009,.2668390863718181] | **[.26434967966592837,.2659650915371778]** |
| j99 beta-19.2 | [.2685342279796715,.27014045101645023] | **[.26432002482060124,.26593550181081793]** |

These bands ARE NOT physical confidence intervals, source-certified parameter ranges, BBN results or PBH exclusion contours. They assume all above-grid rates and the clock mapping hold fixed and the below-grid log-slope band as a mathematical model class. The default and posthoc native clocks are different source runs, so their fractions should not be blended or mistaken for one source-invariant output.

## Execution and claim limits

EXECUTED this turn by independent JavaScript using live GitHub connector original 100×5 author table + DEFAULT 8-row native Badacz CSV + POSTHOC 6-row native Badacz CSV, all exact source blob identifiers checked. Each species interpolated separately in log mass/log rate, then summed after segment mass-squared quadrature; explicit segment primitive matches MT15 ROT001 and ROT004. Four DEFAULT source-only values and conditional band endpoints reproduce ROT001/ROT004 to printed precision. Four POSTHOC numbers are new to MT15 and differ by up to 0.9197 percentage points, a material MODEL_NUMERIC currentness delta. This is NOT independent native Julia execution; the original Badacz owns both frozen native runs. No additional BlackHawk/PYTHIA, transport, energy spectrum or BBN target was tested.

Original owner REVIEW057 r2's statement that "post T_nuc fractions do not change" should be read qualitatively (same late-source phenomenon and approximate size), not as NUMERICAL identity: within the current source conditional mass clock the percentages do change at the precision shown, including a default ~8.23% versus posthoc ~7.31% no-subedge fraction for j98 beta-19.2. This does NOT contradict the fact of substantial late hadron-number mass-clock tail; all four above-grid f0 remain strictly positive and the theorem [L/T,1) stays correct once the clock-specific L and T are recomputed.

Owner prereg statuses P2/P4 FAIL at DEFAULT remain historical; r2 posthoc investigation confirms sensitivity/solver path effects rather than changing prereg outcomes. New native REVIEW059 says source-native A1 two-direction violation remains, not part of this arithmetic target. No physical BBN conclusion follows.

Required science hygiene: MT15 ROT001 and ROT004 numeric tables must be labeled **DEFAULT_NATIVE_CLOCK_ONLY**; ROT006 supplies alternative POSTHOC source rows but does not silently replace historic frozen numbers. Need physical SOURCE E4 before any PBH bound. No owner task assigned; owner ACK and independent referee remain OPEN.

STOP: `ORIGINAL_SOURCE_100ROW_5CHANNEL_JS_REPLAY_PASS / TWO_NATIVE_CLOCK_VERSIONS_ACCOUNTED / NUMERIC_SENSITIVITY_NOTED / SHARP_THEOREMS_UNCHANGED / NO_PHYSICAL_Yp_BETA / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_PENDING`.
