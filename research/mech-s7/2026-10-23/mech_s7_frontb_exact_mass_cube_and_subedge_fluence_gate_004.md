# MECH-S7 — Wu–Xu Front B: exact mass-cube numerical falsifier and subedge emitted-number control

```yaml
CELL: IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7
DATE: 2026-10-23
RETURN_ID: MECH-S7-FRONTB-EXACT-MASS-CUBE-SOLVER-ERROR-AND-SUBEDGE-FLUENCE-004
TYPE: EXACT_SOURCE_NATIVE_IDENTITY / EXECUTED_ARCHIVED_TRAJECTORY_VIOLATION / CONDITIONAL_SOURCE_INTEGRAL
EXPOSURE: PUBLIC
PROBLEM_ID: FRONTB_PBH_HADRON_BBN_SOURCE_VALIDATION
SOURCE: Wu-Xu JCAP02(2026)063; Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d
STATUS: CONDITIONAL_NUMERICAL_FALSIFIER_ON_ARCHIVED_2x2 / NOT_FULL_10D_REEXECUTION
NO_SOURCE_VALID_E2B: true
NO_MODERN_BBN_ENDPOINT: true
NO_PBH_BOUND_CORRECTION: true
NO_CANON: true
NO_EXEC_SIGN: true
NO_NOVELTY: true
BW_INGEST: NOT_VERIFIED
```

## 1. Research question, distinguishing contribution, and source basis

Question: Can one falsify numerical accuracy in the terminal mass regime **without first running the costly 10D Julia source solver**, and can the observed strong signed antinucleon cancellation be connected to the SPECIES-SPECIFIC paper-vs-public emission-law mismatch rather than guessed from its large condition number?

**Results:**

1. In the pinned Wu–Xu source model at M<=6e9 g, effective Hawking radiated degrees of freedom `N_BH(T_BH)` are exactly **constant** under the code's own saturated constant-extrapolation lookup table. Hence the ODE has an exact analytic invariant `M(t)^3 + Gamma (t-t_f) = M_i^3`, with Gamma numerically 4.207579833788249e27 g^3/s. At the last **source-active** saved point, the archived four-branch mass/time pairs violate this exact relation by **+2.33%** (`B_exec`) or **+2.20%** (`B_sym`) in M, corresponding to effective time lags 0.09840 / 0.09270 s. This diagnoses numerical inaccuracy in the frozen archived solver output without a new solve.
2. Source-native exact chronology for the archived M_i=6e9 g diagnostic: M=1e9 g at t=51.0982580232 s and ideal cutoff at t=51.3359243396 s (initial formation time ~7.7e-29 s). The **entire subedge** interval lasts only **0.2376663164 s**, whereas consecutive archived output samples span t≈49.96 to 52.26 s and have no saved source-active point within it. Thus the output save grid cannot trace the decisive injection period.
3. Below the edge, for species-specific public `Q_h~M^{s_h}` and paper-law `Q_h~M^{-1.3}`, the total **unweighted emitted particle count per PBH** integrated to the declared cutoff is computable in closed form under the SAME frozen source mass law. The paper-law relative increase is 5.60–6.08% across the five hadronic source channels. In the antinucleon pair, proton/pbar 5.629916% vs neutron/nbar 5.602173% is a differential of only **0.027743 percentage points**. Hence the enormous local condition number of signed antinucleon forcing does NOT itself establish that the particular source-law change reaches the unstable **differential** direction.

All three are about the **public reduced executor and its own source**. No independent source-valid hadronization below 1e9g or published figure genealogy, no full BBN and no new PBH abundance bound follow.

## 2. Source-local derivation: N_BH plateau and exact mass cube

Primary pinned paths:

- `arXiv-2509.05618/main-scan.jl`: `d_m_PBH_dt = -N_BH(T_PBH)*NU.m_Pl^4/m_PBH^2`, `T_BH(m_PBH)=NU.M_Pl^2/m_PBH` (from `tool_script-parameters.jl`). No hadron populations enter the mass derivative.
- `tool_script-parameters.jl`: `N_BH(T_BH)=(27/4)*Nᵨ(T_BH)/(30720π)`.
- `tool_script-N_relativistic_species.jl`: `Nᵨ` combines `N_s_from_PDG2024.csv` and `N_rho_OVER_N_s_from_PDG2024.csv` with **ExtrapolationType.Constant** at table ends.
- Last table temperature points are 279.783067 GeV (N_s) and 275.903656 GeV (rho/s), with respective values 104.896439 and 0.999701056, so **Nᵨ(hot)=104.86508083894**.
- `NaturalUnits.jl@4a9f007ff1df416c9fef28c4d83d8fe8846099cf`: `NU.M_Pl=1/sqrt(8π G_N)`, `NU.m_Pl=1/sqrt(G_N)`, `G_N=6.67430e-11 SI`, SI fundamental constants.

The source's Hawking temperature at M=1e9g is 10,572.612 GeV and at M_i=6e9g about 1,762.102 GeV: both ABOVE the maximum 279.783 GeV lookup temperature. Since mass only decreases until cutoff, Nᵨ(T_BH) remains at the same last-table constant along all source-active states. Thus:

    N_BH = (27/4)*104.86508083894/(30720π) = 0.007334382996056442
    dM/dt = -C/M²
    d(M³)/dt = -3C = -Gamma
    Gamma = 3*N_BH*hbar*c^4/G_N² * (1000g/kg)^3
          = 4.207579833788249e27 g³/s
    M_exact(t) = cbrt[M_i³ - Gamma*(t-t_i)]  until M_cut.

The mass-cube identity is source-native and independent of the details of hadron source, charge map, Xn, Hubble rate and choice of a as ODE independent variable; t is itself a solved state but its relationship with M must still satisfy this exact scalar law.

**SCOPE:** This identity does NOT apply across the source's evaporation cutoff branch where the derivative is artificially set to zero; only compare saved SOURCE-ACTIVE states at positive M significantly above the cutoff. No quantum-gravity mass-evolution statement is made.

## 3. Executed numerical comparison: archived, SHA-verified four cells

Original Mech-S6 GitHub Actions artifacts downloaded and hash-verified:

- public law `12116193467`, ZIP sha256 `75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5`;
- paper law `12192535869`, ZIP sha256 `3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e`.

Initial M_i=6e9 g, beta=1e-16 (deliberately strong *diagnostic*, not a PBH bound), 1600 sampled a points per branch; last saved source-active point zero-based 1469, first source-off 1470. Compare m_saved(t_saved) to exact m(t) with exact source initial t_f.

| Branch | Last saved t [s] | M_saved [10^9g] | M_exact [10^9g] | Relative mass discrepancy | Implied mass-cube time lag [s] |
|---|---:|---:|---:|---:|---:|
| public_exec | 49.961898627 | 1.836633086 | 1.794771130 | +2.33244% | +0.09840493 |
| public_sym | 49.959279260 | 1.835347300 | 1.795910890 | +2.19590% | +0.09269528 |
| paper_exec | 49.961898627 | 1.836633086 | 1.794771130 | +2.33244% | +0.09840493 |
| paper_sym | 49.959279260 | 1.835347300 | 1.795910890 | +2.19590% | +0.09269528 |

The identical rows for public/paper law within each reaction map up to this point are consistent with above-edge source-law equality. The differing `exec` and `sym` backgrounds should NOT reflect a physical coupling: the upstream mass/background block is triangular. Their difference and the absolute mass-cube error demonstrate why independent adaptive solves and bit-identical repeats do not certify O(1e-5) endpoint results.

**Evaporation interface:** the code sets `log_m_evap = max(log(M_i)-20,log(m_Pl))`, so the selected initial mass has intended cutoff `M_cut=12.3669217346 g`. First saved post-evap masses are about 8.446, 9.845, 11.152 and 7.457 g, respectively. They are *below* the specified nominal cutoff. This is consistent with solver step overshoot/interpolation around a discontinuous RHS but does not determine the accepted internal event-crossing step, and the mass-cube identity is not applied to these source-off states.

The exact source-native chronology is:

    t(M=1e9g) = 51.0982580232 s
    t(M_cut)   = 51.3359243396 s
    duration   = 0.2376663164 s

Saved adjacent output points cross this entire window: source-on 49.96 s -> source-off 52.26 s. It is a first-priority accepted-internal-step and tolerance/convergence gate.

**Numerical significance:** +2.2–2.3% last-active MASS discrepancies are detected against an exact scalar identity, NOT an asserted corresponding percentage error in Xn, hadron fluence or published beta bound. The latter remain unquantified. The signature is a source-native solver defect in this archived run, rather than evidence of physically different cosmological backgrounds.

## 4. Exact subedge emitted-number integral and limits

Pinned `data/out/hadrons_from_PBH.dat`, source blob SHA `06d0883a27b108692720422294ba2baacd381a64`: first two table entries yield log-slope s_h (public extrapolation). For M<M0, the code's public extrapolation has Q_h(M)=Q_h(M0)*(M/M0)^s_h. The paper-law comparator instead uses Q_h(M0)*(M/M0)^(-1.3). Under the **same constant N_BH**:

    |dt/dM| = M²/C, u=M/M0
    N_h^public = Q_h(M0)*M0³/C * [1-u_cut^(3+s_h)]/(3+s_h)
    N_h^paper  = Q_h(M0)*M0³/C * [1-u_cut^1.7]/1.7
    R_h = N_h^paper/N_h^public
        = (3+s_h)/1.7 * (1-u_cut^1.7)/(1-u_cut^(3+s_h)).

| Source species | public slope s_h | Paper minus public emitted number |
|---|---:|---:|
| charged pion pair (both tracked π channels) | -1.200486 | +5.853787% |
| charged kaon pair (tracked K-) | -1.196651 | +6.079332% |
| K0L | -1.196805 | +6.070303% |
| p+pbar (tracked pbar) | -1.204291 | +5.629916% |
| n+nbar (tracked nbar) | -1.204763 | +5.602173% |

The antinucleon pair's total rate enhancement is strongly **common-mode**: difference of enhancements 0.02774326 percentage points, about 20x less than the 0.54378 percentage-point `pbar+ε/nbar−ε` perturbation difference that reversed instantaneous F at the **last above-edge saved B_exec state** in Mech-S7 ROT003 (and ~48x less than the analogous 1.34721 pp B_sym threshold). This comparison is only a **directional scale analogy**: integrated production does not equal instantaneous abundance, true hadrons undergo fast losses, cosmological dilution and nonlinear Xn coupling, and the last-supported state is not the terminal one. It is **NOT a proven bound** on actual δF or δX.

For any u<1 the instantaneous paper/public source multiplier is `u^(-1.3-s_h)`, which becomes more species-differential at extremely small u. At u=0.1, ratio of p and n law changes differs by about 0.1087%; at u=0.01 by about 0.2174%. These are **relative source-rate ratios**, not population perturbations. A toy frozen-population mapping of these multipliers into last-supported channel coefficients may reverse F only very deep in the tail; its root, if computed, has no physical status absent a dynamical response kernel. This illustrates why the 6-channel high condition number of ROT003 cannot be promoted to an actual terminal reaction mechanism.

A useful purely emitted-number diagnostic: for paper exponent -1.3 the fraction of all subedge emitted hadron **counts** produced with M<εM0 is (approximately) ε^1.7. This is NOT an Xn response bound, because time-dependent reaction efficiency and sampling are not included.

## 5. Negative knowledge, cross-cell critical work, next discriminant

- **NEW EXACT CONTROL PASS:** the source-specific mass-cube identity exists due the pinned saturated N_BH table and is independently reconstructed from pinned SI constants. The archived output **fails numerical accuracy** of this exact source equation at late source-active points. Future Julia runs can apply a cheap exact-M monitor at every accepted state before studying sign(δXn).
- **NEW LIMITED CONTROL PASS:** subedge *integrated, unweighted emitted counts* for public vs paper source laws are exactly computable conditional on the pinned source-rate extrapolation. Nucleon total source-law differences are close to common scaling; no dynamic antinucleon mechanism is inferred.
- **PRESERVE:** Mech-S7 ROT003 measured instantaneous cancellation and directional condition-number stress; these are genuine local sensitivity diagnostics. MT13's global per-cell X(Tnuc) sufficient sign gate `epsilon_X<6.33356560558e-6` is an entirely different, endpoint accuracy requirement.
- **REC10 GUARD:** source-off is not zero hadron forcing by definition; carried hadrons can persist and the direct log-floor has a separate bound. One can use an exact Duhamel kernel and sign sufficient conditions only after integrating the actual residual source, not from the PBH source flag alone.
- **NEXT COST-EFFECTIVE SOURCE RUN:** maintain original frozen background equations but instrument mass-cube invariant at every **accepted internal step** and compare with exact analytic M(t) across 10^9 g->cutoff; set explicit 1e-3/1e-6/1e-8 tolerance tiers with source-native fixed-T interpolation, H(t)/T(t), all six log populations, source Q_h, A/B/F, floor flags and solver step stats. The exact-M(t) substitution can be used as a separate controlled comparator, not silently as a production code repair. Require replicate across 2x2 branches and same physical background.
- **SOURCE-VALIDITY STOP:** nothing above validates hadronization below 1e9 g, modern Yp/D/H, published scan genealogy, PBH beta bound, actual physical novelty or canonical theory. Rec10/M13 are appropriate independent scientific reviewers; MT13 program owner and KN11 BW owner may process without forced promotion. No new EXEC authorized.

## 6. Reproducibility contract

Local Python script `source_native_mass_cube_and_fluence_control_004.py`, original Actions ZIPs and checked SHA256 digests, computed JSON, four-branch mass-cube CSV, selected-row audit CSV and species fluence CSV are included in the accompanying ZIP. The script executes on original raw trajectories with numpy/pandas, compares source active rows ONLY for exact M(t), calculates the source-native Hawking temperature and derived gamma, asserts constant-table regime, validates terminal chronology and exports reproducible results. **Julia binary was not present; network install unavailable; no Julia solve was run.**

Storage: this full public scientific body intended for `research/mech-s7/2026-10-23/`; CI/GitHub readback and BW ingestion are distinct events. `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PBH_BOUND / NO_SOURCE_VALID_E2B`.