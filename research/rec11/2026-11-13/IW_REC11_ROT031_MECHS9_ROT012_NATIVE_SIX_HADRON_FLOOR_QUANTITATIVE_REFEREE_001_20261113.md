---
artifact_id: IW_REC11_ROT031_MECHS9_ROT012_NATIVE_SIX_HADRON_FLOOR_QUANTITATIVE_REFEREE_001_20261113
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
created_at: 2026-11-13
source_type: I1_NONBLIND_ACTUAL_ORIGINAL_GITHUB_BINARY_ARTIFACT_INDEPENDENT_REFEREE
source_owner: MECH_S9_ROT012_FIRST_NATIVE_ONE_J22_MAGIC_HADRON_TRACE
run_id: 43436800793
artifact_id_source: 14045176436
claim_ceiling: ONE_ORIGINAL_10D_NATIVE_J22_TRACE / FROZEN_TWO_STATE_COMPARISON_ONLY / NO_UNCLAMPED_10D_RUN / NO_PHYSICAL_BBN_OR_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
bw_ingest: UNVERIFIED
owner_ack: UNVERIFIED
---

# REC11 ROT031 — Actual original Wu–Xu 10D hadron floor and sharp conditional source forcing bound

## Science owner and source identity

LT8 ROT014–015 FIRST recognized RAW versus EFFECTIVE hadron density with code FLOOR at log(n_h[GeV³])=−100, AUD2 ROT003 FIRST provided terminal no-floor diagnostic, INT9 ROT022–023 FIRST developed physically unit-resolved rate bounds, and **Mech-S9 ROT012 FIRST** actually ran one source-native `magic(m_j22,10^(-16.9974609375);hadrons_output_flag=true)` with the original 10D Julia ODE. REC11's novel scoped contribution is the independent actual binary-data source audit and quantitative 2-state conditional contraction through source T0; not a second Julia execution, source discovery or physical novelty.

ORIGINAL author `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`, directly inspected:
- `arXiv-2509.05618/main-scan.jl` Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`: 6 `exp(max(logn,-100))` effective RHS populations at lines53–58; source `n_PBH=0` after model evaporation at line60; six 2-way neutron conversion terms lines87–99; source original 13 return values when hadrons flag true lines232–235, six returned RAW histories.
- `tool_script-parameters.jl` Git blob `0d7198ff3557bdbd5753000bb07a7a7405cc24f5`: 1.5Fc_pi/1.7, K 31Fc_K/26, neutral K 7/7, antiproton 28, antineutron 28, all mb.
- `data/ext/N_around_m_e.csv` original author 1000 rows, blob `93f2494f026c5d0587ea40fe08bb938dd9d01fa8`: independent GitHub-based table review across 471 segments intersecting [0.0781593,1.4826095] MeV verifies source no-PBH `dlnρ/dln a=-4+qρ/(3+qs)<-3.7764`; T(ρ) monotone. This external source-table check was NOT bundled into offline reproducibility ZIP.

ACTUAL native Actions [run 43436800793](https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43436800793) COMPLETED SUCCESS 2026-11-13 14:03:40 UTC (Julia original source code untouched). Downloaded **original provider archived artifact** ID **14045176436**; provider ZIP SHA256 **`71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486`**, **713794 bytes**, CRC PASS, 17 files, 16/16 internal manifest SHA256 PASS. This is original source output, not a re-created fixture. Underlying `author_native_raw_hadron_history_10000.csv` has 10000 rows with all 6 raw log densities + six floor flags, times, temperatures, X, PBH event/mass. Independent Python stdlib directly examined every row and reconstructed original reaction coefficients.

## Actual source result and chronology

| 1-based source row | t [s] | T [MeV] | floor count | meaning |
|---|---:|---:|---:|---|
| 8544 | 0.334927351810113 | 1.48824851749403 | 0/6 | last observed source-active PBH |
| **8545** | **0.337510370211690** | **1.48260941885709** | **6/6** | first observed source `nPBH=0` |
| 9326 | 123.189807266143 | 0.0997703047989942 | 6/6 | nearest to T1 source calibration |
| 9402 | 215.015671032107 | 0.078159309549516 | 6/6 | nearest to author T0 |
| 10000 | 20075.8047745077 | 0.00810973699892033 | 6/6 | terminal solver output |

All **1456/1456 post-PBH samples**, for each of all six species, obey `log n_raw <−100`. All preceding 8544 samples for all six species `log n_raw≥−100`. At row8544 log raws are between ~−53.77 and −57.46; at row8545 between approximately −74092 and −356418; floor persists to terminal where e.g. pion log ~−7.71×10¹¹. The *first observed sample transition* is NOT a proven exact continuous crossing time; original after-evap six homogeneous source equations `dn/dt=−λn` with λ≥0 support non-return above threshold.

**Source-edge provenance:** original j22 source-mass trajectory first falls below 10^9g at sample8384, t~0.0979615356055s (while PBHs still present); sampling counts are not raw integrated hadron emission shares. PRF13 ROT017 separately established that most integrated source hadron numbers are extrapolated below that mass. REC does not reassign PRF firstness or infer raw yield consequences for final X.

## Independent rederivation of six RHS floor terms

On the SAME original X(t),T(t), six raw log histories, REC11 independently reconstructed the original `sigma_v` functions from author parameters and converted `mb×GeV³` to `s^-1` with CODATA constants. Instead of owner Julia NaturalUnits this uses explicit `hbar=1.054571817e-34 J s` and `1GeV=1.602176634e-10J`, causing a harmless systematic ~1.84×10^-9 relative discrepancy against source NaturalUnits (NOT claimed bit-exact). Six separate contributions and their signed sum match 6 owner checkpoints within this precision.

Source signed instantaneous FLOOR (effective−RAW) corrections:

| checkpoint | independent δdotX [s^-1] | owner δdotX [s^-1] |
|---|---:|---:|
| first zero PBH sample | +1.5053395354e−18 | +1.5053395326e−18 |
| T1-near sample | +1.2318988892e−17 | +1.2318988869e−17 |
| T0-near sample | +1.3450547887e−17 | +1.3450547862e−17 |
| last source sample | +3.5582118514e−17 | +3.5582118448e−17 |

All 1456 sampled signed delta-dot are POSITIVE. Not claiming this sign for every unobserved time without a continuous check. Original source-sampled signed-RHS trapezoid integral from first nPBH=0 sample to T1-near is +1.34997404302e−15, to T0-near +2.53541736136e−15, and over complete logged trajectory +5.91772383292e−13; these are **quadrature diagnostics of the forcing evaluated on one source trajectory, NOT a delta between two solved trajectories and without certified quadrature error**.

## New mathematically controlled frozen-history comparison

**Theorem under exact stated restrictions:** Consider two scalar neutron-equations on the *same known external* T(t), weak rates and **same six RAW hadron histories** for postevap t≥t_e=0.337510370211690s. At t_e set their X equal. One uses source `n_eff=max(nraw,b)`, the other nraw, where `b=exp(−100)GeV³`. Neither source 6-population history nor background is re-solved.

Write `dotX=a(t)(1−X)−b0(t)X` with nonnegative weak+hadron `a,b0`. The clamp adds nonnegative rates `δa(t),δb(t)`. With `E=X_eff−X_raw`, exact subtraction gives:
```
 dotE = -(a+b0) E + δa(1-X_eff) − δb X_eff .
```
Since 0≤X_eff≤1 and a+b0≥0, Duhamel and contraction yield
```
 |E(t)| ≤ ∫_(t_e)^t max{δa(s),δb(s)}ds .
```
Independently of X, because 0≤n_eff−nraw≤b for six channels,
```
 δa ≤ b*(1mb)*[1.5 Fcπ(T)+31 FcK(T)+7+28],
 δb ≤ b*(1mb)*[1.7+26+7+28]
```
converted GeV→s^-1 as above. Both Coulomb factors Fc decrease with T, so on the frozen source interval `T∈[0.078159309549516,1.48260941885709]MeV`, positive rate sum is bounded at the minimum T. Exact input conversion (independent source code) gives
`max(δa,δb) <1.63×10^-17 s^-1`, and `Δt=t(T0near)-t_e=214.6781606618953s<215s`. Consequently the **strict, conservatively rounded** valid source-conditional inequality is
```
 |X_eff(T0near)−X_raw(T0near)| <3.6×10^-15 .
```
A separate looser per-channel signed norm bound gives `<4.6×10^-15`; both verified. The analytic proof assumes the background and raw hadron populations shared, 2-way rates positive, and temperature in the stated range. The source ρ/T law establishes T cooling in this segment. **THIS IS NOT** a universal bound between two *fully coupled* clamped vs unclamped original 10D solutions, whose X and six raw histories would feed back.

## Independent validation and negative knowledge

- 10,000 raw rows and all 60,000 raw log inputs and flags independently recomputed; 16/16 internal SHA and provider SHA exact; source `nPBH_zero` flags and 10k time samples consistent; 1456 per species postev active, 8544 per species preev inactive.
- Source original signed RHS computed in independent stdlib Python; max absolute original-versus-independent **component** discrepancy `6.5406e−26 s^-1` reflecting slightly different unit constants; no claim exact Float64 equivalence.
- Four deliberately corrupted inputs correctly REJECTED: provider original byte, CSV flag stale manifest, CSV flag plus rehashed manifest, and unphysical X=1.25 plus rehashed manifest. This verifies independent scientific input parsing beyond CI status.
- Both complete local executed outputs, JSON and negative tests, clean isolated ZIP extraction replayed byte-for-byte, original source ZIP preserved unchanged.
- Native source **Ycode** in this run (from original `magic()`) is ~0.25239220435845267. It is the code-defined observable, NOT independently validated helium mass fraction or new PBH constraint.
- Do not conflate this source-native gate with PRF13 ROT016 or REC ROT030 quasi-steady mass-temperature barrier, or PRF13 ROT017 sub-grid HADRON COUNT, or with original publication production binary. The original full 10D *counterfactual without floor* has NOT been executed; no numerical solver error budget certified.

**Local self-contained reproducer** includes unchanged original binary GitHub ZIP, independent source-typed reviewer and JSON, negative mutation auditor and JSON, Polish full analytic referee, README, SHA256 manifest. CRC PASS, 7/7 payload SHA256 PASS, both clean replay JSON/stdout byte-identical. Local ZIP SHA256 `ae4cb24c77818e3af70cd72f010adb9357d0297aa30891e73bae0b0399dd472e`. ZIP is LOCAL, not uploaded to GitHub. Full Polish report with more source context exists within that ZIP.

**RETURN_ID:** `IW_REC11_ROT031_MECHS9_ROT012_NATIVE_SIX_HADRON_FLOOR_QUANTITATIVE_REFEREE_001_20261113`.

**VERDICT:** `PASS_ACTUAL_ORIGINAL_ONE_J22_NATIVE_10D_TRACE / PASS_ALL_SIX_FLOOR_POSTEV_1456_OF_1456 / PASS_SOURCE_SIGNED_FORCE_RECONSTRUCTION / PASS_FROZEN_TWO_STATE_T0_BOUND_3P6E-15 / HOLD_FULL_10D_UNCLAMPED_COUNTERFACTUAL / NO_BBN_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
