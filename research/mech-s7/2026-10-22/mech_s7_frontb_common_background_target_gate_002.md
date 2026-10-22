artifact_id: MECH-S7-FRONTB-COMMON-BACKGROUND-DECOMPOSITION-002_20261022
cell: IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7
date: 2026-10-22
exposure: PUBLIC
result_class: EXECUTED_POSTSOURCE_ARCHIVED_TRAJECTORY_REPLAY / EXACT_CONDITIONAL_SOURCE_FREE_DYNAMICS
status: SCIENTIFIC_DIAGNOSTIC / NOT_FULL_JULIA_RERUN
claim_ceiling: NO_SOURCE_VALID_E2B / NO_MODERN_BBN_ENDPOINT / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY
sync: GITHUB_COMMITTED / BW_INGEST_NOT_VERIFIED

# Mech-S7 rotation 002 — source-native target gate and common-background decomposition

## Executive result

**Revision/qualification of Mech-S7 rotation 001:** The source-law contrast (paper M^-1.3 minus public log-interpolation) at a **common saved scale factor** reverses sign after PBH evaporation; replay shows this reversal is explained predominantly by differences between independently integrated numerical cosmological backgrounds. **But this is not the published executor target.** In upstream Wu–Xu code, the reduced helium proxy uses linear interpolation of Xn in Q/T, evaluated at fixed T_nuc=0.07818527068831995 MeV. At this correctly typed **fixed-temperature readout**, the opposite signs for the two charge maps persist under propagation on the **same saved background**. Thus claiming the source-native endpoint signs are *solely* a post-source background numerical artifact is unsupported.

This restores an important piece of mechanistic interpretability but **does not certify source-valid physics or original Julia solver convergence**: the full unsaved terminal injection below M=1e9g has not been instrumented, the extrapolated hadron emission lacks source-valid E2b, and the reduced proxy Yp>1 for this deliberately strong diagnostic point is not a physical abundance.

## Provenance

- Primary Wu–Xu public code: Fenyutanchan/Primordial-Black-Hole, commit d395183674cace6c9906a8911bdeb7234ba4040d, arXiv-2509.05618/main-scan.jl, tool_script-parameters.jl, tool_script-hadrons_from_PBH.jl, data/out/hadrons_from_PBH.dat.
- Peer-reviewed publication: Wu & Xu, JCAP02(2026)063, DOI https://doi.org/10.1088/1475-7516/2026/02/063.
- Existing four trajectories (1600 points on a common a grid): GitHub Actions original artifacts 12116193467 and 12192535869. Downloaded and checked raw ZIP SHA256 respectively 75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5 and 3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e.
- Four cells: public_exec, public_sym, paper_exec, paper_sym. Inputs M_initial=6e9 g; beta=1e-16. First saved SOURCE OFF at zero-based index 1470. No saved active point below 1e9g. The internal terminal adaptive steps have not been retrieved.
- Python/NumPy/Pandas/SciPy post-source replay. **No new Julia 10-variable solve**. Full reproducibility package (original ZIPs, source, JSON, CSV and independent extended report) delivered to Moderator.

## Exact conditional source-off control

The source-native neutron equation in the post-source regime, setting effective hadronic forcing to zero, is

    dX/dt = u(t) - lambda(t) X
    x=Q/T
    Gamma_SM=(255/tau_n) (12+6x+x^2)/x^5
    u=Gamma_SM exp(-x)
    lambda=Gamma_SM [1+exp(-x)] + 1/tau_n
    Q=1.29333234 MeV, tau_n=878.4 s

For a shared exact T(t), two trajectories' difference is

    delta_X(t) = delta_X(t0) exp[-integral_(t0)^t lambda(s) ds]

and preserves its sign. This is standard scalar linear ODE algebra, not IW novelty.

Execution: build PCHIP interpolants of each archived t(eta), T(eta), eta=log(a). From the four archived X values at the first source-OFF common a, propagate each on each frozen saved background using SciPy solve_ivp, DOP853, rtol=2e-11, atol=2e-13, max_step=.01 in eta. The replay is a **conditional source-off control**, *not* a reproduction of unknown hadron forcing or evaporation history.

Define a three-way algebraic partition at the selected readout: actual paper-public delta X = common-bg difference + background-choice effect (own-bg replay minus common-bg replay) + archive-minus-replay residual. The latter is not a direct or rigorous estimate of the original Julia ODE global numerical error: saved-curve interpolation and conditional-model simplification contribute.

## A. Same saved-a result: numerical background determines sign reversal

At zero-based sample 1502 (near T≈0.07757 MeV):

| Delta X paper−public | Recorded | Shared-bg | Background effect | Replay residual |
|---|---:|---:|---:|---:|
| B_exec | +1.466526e-6 | −1.633229e-5 | +1.882755e-5 | −1.028740e-6 |
| B_sym | −1.945113e-5 | +1.078699e-5 | −2.984126e-5 | −3.968621e-7 |

The sign changes after restoring saved numerical background differences. Upstream background t,rho_SM,m_PBH differential equations are triangular/independent of neutron and hadron populations, so with identical initial background they should coincide exactly. The saved independent 10-variable solver results do not: temperature shifts at index 1502 versus public_exec are +71.40 ppm (public_sym), +104.81 ppm (paper_exec), −31.93 ppm (paper_sym); time shifts are −0.00908, −0.04349, and +0.06214 seconds respectively.

**Important:** source model does not physically require these different backgrounds. This test identifies a numerical comparison confound on common-a outputs.

## B. Source-native fixed Q/T target: sign persists on shared background

The actual upstream readout interpolates Xn linearly in x=Q/T at T_nuc=0.07818527068831995 MeV. Applying precisely this readout:

| Delta X at fixed T_nuc, paper−public | Recorded | Shared-bg | Background effect | Replay residual |
|---|---:|---:|---:|---:|
| B_exec | −1.898857e-5 | −1.640731e-5 | −1.607742e-6 | −9.735097e-7 |
| B_sym | +1.266713e-5 | +1.083653e-5 | +2.251028e-6 | −4.204293e-7 |

At the physical-coordinate readout, shared-background contributions preserve source-law sign in **both** reaction maps, and account for about 86.4% (exec) and 85.6% (sym) of recorded contrast magnitudes in this conditional decomposition. Signs already differ at the first saved point *after* unobserved evaporation: −2.052432e-5 (exec), +1.355900e-5 (sym). This implicates the unobserved terminal integration as the next mechanism test; it is not proof of physical hadron source validity.

## C. Stability tests and limits

1. Across all four alternative frozen saved backgrounds, common-background delta at sample 1502 lies near [-1.633229e-5,-1.632563e-5] for B_exec and [+1.078621e-5,+1.078918e-5] for B_sym. Signs unchanged.
2. RK45, DOP853, Radau × PCHIP, CubicSpline controls preserve the original archived *own-background* comparison's signs at common a. Replayed exec delta range approx +2.460e-6 to +2.500e-6; sym approx −1.90562e-5 to −1.90529e-5.
3. Replay minus raw saved X at sample 1502 for public_exec/public_sym/paper_exec/paper_sym respectively is approximately −9.55e-7, −5.38e-7, +7.4e-8, −1.41e-7. These are replay mismatch values, not global error bounds on upstream Julia.
4. Rotation 001 established that the *direct* post-source log-population-floor contribution to dX/dt is at most 3.55e-17 s^-1 in the saved temperature range, with integrated direct forcing <5.8e-15 to T_nuc. Structural source-code qualifier remains; direct floor contribution alone is too small to cause source-law 1e-5 contrasts. Internal source-active terminal floor not evaluated.

## D. Numerical convergence and source-validity gates

The pinned public main-scan.jl uses exactly `solve(evolution_problem, AutoTsit5(Rosenbrock23()))` with **no explicit reltol or abstol**. SciML documented common deterministic adaptive defaults are approximately reltol=1e-3 and abstol=1e-6; these govern *local error estimates*, not guaranteed global endpoint errors (https://docs.sciml.ai/DiffEqDocs/dev/basics/common_solver_opts/). Actual defaults in the installed pinned solver versions must be printed from the runtime rather than assumed. Bit-identical retries do not certify a 1e-5 effect.

**Next cheapest valid test (not yet executed):**
1. Freeze a single source-native cosmological solution for the exact t(a), T(a), H(a), m_PBH(a) background and document effective solver tolerances. Compare 1e-3 / 1e-6 / 1e-8 relative tolerance tiers with corresponding explicit absolute tolerance, accepted/rejected step stats and physically typed X(T_nuc) target.
2. On this frozen background integrate all six hadronic log populations + X for 2x2 source-law × charge-map branches, keeping S_h, decay, floor, A/B/F, cutoff, and actual Q/T target. Save **accepted internal states**, especially M=1e9g to evaporation.
3. Distinguish species contributions (charged pions, charged kaons, K0L, p/pbar, n/nbar); only then discuss whether source-law × charge-map interaction survives solver convergence.
4. Require independent Rec10/M13 source-local review and a source-valid low-mass hadronization replacement before any physical inference. Neither valid Yp/DH likelihood nor published figure genealogy is established.

## Mechanism and empirical map

**MECH-WX1:** Hawking PBH emission → hadronic source Q_h n_PBH → six populations → directional neutron conversion F=(1−X)A−XB → reduced X target. Explains why uniform positive source-law change does not imply uniform X shift. Does not establish low-mass source validity/BBN observable. Cheapest falsifier: frozen-background species-trace accepted-step full solve.

**EA-WX1:** physical anchor type primordial helium and deuterium abundances (Wu–Xu 2026 and modern BBN). The inspected code computes the reduced diagnostic `Y_P=2X/(1-X)` and a single helium-like `chi2=((Y_P-.245)/.003)^2`, not a verified joint modern helium+D/H endpoint. Empirical anchor is indirect and NOT EXECUTED for this diagnostic.

**NEGATIVE KNOWLEDGE:** sign reversal on a common-a grid is NOT evidence that the source-native fixed-T target sign is wrong; independent-background drift is NOT a physical source-map effect; default adaptive solver tolerances do NOT certify 1e-5 result; source-off tracer floor=0 is NOT an internal accepted-step floor audit; source-valid E2b remains OPEN.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_ENDPOINT / BW_INGEST_NOT_VERIFIED.
