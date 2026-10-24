# Mech-S7 ROT015 — source-active mass-cube secant audit, branch invariance, and non-global clock defect

**DATE:** 2026-10-24.  **RETURN_ID:** `MECH-S7-FRONTB-ARCHIVED-MASS-CUBE-SECANT-AND-NONGLOBAL-CLOCK-DEFECT-015`.  **PROBLEM_ID:** `P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001`.

**CLASS:** `EXECUTED_FULL_SAVED_TRAJECTORY_EXACT_INVARIANT_AUDIT / BRANCH_IDENTICAL_ABOVE_SOURCE_TABLE_EDGE / LOCAL_SECANT_NONCONSTANT_RATE_DIAGNOSTIC / NEGATIVE_CLOCK_MECHANISM`.  **CLAIM CEILING:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_SOURCE_VALID_E2B / NO_MODERN_Yp_DH / NO_PBH_BOUND`.

## 1. Original sources and inherited constraints

- Original Wu–Xu code `Fenyutanchan/Primordial-Black-Hole` pinned SHA `d395183674cace6c9906a8911bdeb7234ba4040d`, `arXiv-2509.05618/main-scan.jl`: source `d_m_PBH_dt = -N_PBH * NU.m_Pl^4 / m_PBH^2` when `PBH_evaporated_flag == false`; `tool_script-parameters.jl`: `N_BH(T)=(27/4)*Nᵨ(T)/(30720π)`; `tool_script-N_relativistic_species.jl`: PDG tabular `Nᵨ` with **constant high-temperature extrapolation**; Hawking temperature is above PDG range throughout source-active archived range `M<=6e9g`. Source-native invariant: `d(M³)/dt = −Γ` with `Γ=4.207579833788249e27 g³/s` for the pinned unit/PDG inputs. Thus `M(t)=[(6e9g)³−Γ(t−t_i)]^(1/3)` until cutoff in the ideal continuum ODE, independent of the hadronic charge map or source-law selection. No claim this law is an exact quantum-gravity statement.
- Mech-S6 raw GitHub Actions trajectory archives: `mech_s6_public_2x2_raw.zip`, SHA256 `75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5`; `mech_s6_paper_2x2_raw.zip`, SHA256 `3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e`. Both checksums enforced at runtime; each source-law+map CSV has 1600 sampled rows and **1470 source-active sampled rows**, all above the hadron source table lower boundary `10^9 g`.
- Source-only references: Mech-S7 ROT004 established the pointwise exact mass discrepancy; ROT013 demonstrated state transport changes both endpoint contrasts by order 2; ROT014 proved that **an artificial consistent translation of all time coordinates** changes a reduced autonomous model's terminal result by zero. That time-origin identity must not be mistaken for a repair of a *nonconstant* residual in archived physical time/mass pairs. REC10 postsource-hadron guard, DAX-S7/PRF11 R21/R22 cooling/EOS priority and MT13/LT5 event-target global accuracy gates remain binding.

## 2. Independent all-sample diagnostic

For every archived source-active row define

`R_i = [M_i³ + Γ(t_i−t_0) − M_initial³]/Γ` (units of seconds; this is the exact **mass-cube clock defect**),

`e_M,i = M_arch(t_i)/M_exact(t_i) − 1`, and for each consecutive row pair,

`r_i = [(M_{i−1}−M_i)(M_{i−1}² + M_{i−1}M_i + M_i²)]/[Γ(t_i−t_{i−1})]`.

The factorized product reduces cancellation in adjacent mass cubes. The exact source continuum requires `R_i=0` and `r_i=1` for every interval prior to evaporation. A constant time shift cannot alter `r_i`. Nor can it turn a nonconstant `R_i` into a constant residual. The audit implements NumPy/Pandas Float64 and an **independent Decimal(65) arithmetic check from serialized CSV numbers** on selected late intervals. Max `|r_Decimal−r_Float64|` across the selected secants was `2.26e-14`, versus genuine observed secant deviations up to `0.0596241`.

Four trajectories were processed (1470 rows each). The original CSV field `i` starts at **1**; `iloc[1469]` is original **CSV i=1470**. `source_active` switches OFF at CSV i=1471, leaving **no source-active archived points below M=10^9g**; nothing here observes accepted Julia steps.

## 3. Main new result — sign-changing secant error

| Last CSV sample `i` of interval | `r_i` public/ paper, B_exec | `r_i` public/ paper, B_sym |
|---:|---:|---:|
| 1401 | 0.9997491333 | 0.9997252877 |
| 1441 | 0.9997143029 | 0.9995646661 |
| 1451 | 0.9996478933 | 0.9993619209 |
| 1461 | 0.9990116719 | 0.9984823202 |
| 1466 | 0.9970874074 | 0.9978454245 |
| 1467 | 1.0024015344 | 0.9900331185 |
| 1468 | 0.9867287723 | 0.9959403268 |
| 1469 | **0.9403758801** | 1.0008483282 |
| 1470 | **1.0346917070** | **0.9789475764** |

**Falsifier of a global clock/rate reinterpretation:** `B_exec` progresses from `r_1469−1=−0.0596241` (5.9624% shortfall) to `r_1470−1=+0.0346917` (3.4692% excess). A single different constant coefficient Γ' or a global time translation cannot simultaneously reproduce these two increments while satisfying the pinned continuum source equation. `B_sym` also exhibits late nonconstant secant deviations up to −2.10524%. The entire source-active archive has maximum |r−1| (for intervals ending after t>1s) **5.96241% B_exec / 2.10524% B_sym**. This is an inconsistency in **stored interpolated numeric outputs**; we cannot infer whether internal accepted steps, interpolant evaluations, cutoff handling, solver error control or another implementation detail is the cause without the actual Julia runtime.

## 4. Error development and nonmonotone clock-defect

| Last saved CSV i | B_exec: `R_i` [s] | B_sym: `R_i` [s] |
|---:|---:|---:|
| 1401 | +0.000396906 | +0.000409184 |
| 1441 | +0.002791354 | +0.003016834 |
| 1451 | +0.004987541 | +0.005486715 |
| 1461 | +0.010834532 | +0.012740553 |
| 1468 | +0.049302796 | +0.048214576 |
| **1469** | **+0.174651898** | **+0.046431188** |
| **1470** | **+0.098404926** | **+0.092695276** |

At CSV 1469, `B_exec` has the **largest** clock defect, 0.174651898 s; by the next row, it **decreases** by 0.076246972 s. This is a stronger, counter-directed local error than the earlier report's terminal 0.098404926 s. `B_sym` peaks at the terminal 0.092695276 s. The clock-defect difference between two reaction maps on CSV 1469 is **0.128220711 s**, dropping to **0.005709651 s** at CSV 1470. A mathematically map-independent mass-vs-time invariant exhibits map-correlated numerical discrepancies in two independently integrated trajectories. It must not be represented as a physical charge-map coupling in the PBH mass equation.

First stored point with mass relative error ≥0.01% is CSV i1456 (B_exec, `M=4.708353e9g`, `t=26.536541s`) and i1457 (B_sym, `M=4.629142e9g`, `t=27.768252s`); error ≥0.1% at i1468 (exec, `M=2.887783e9g`) and i1467 (sym, `M=3.191715e9g`); error ≥1% at i1469 (exec, `M=2.507380e9g`) and i1470 (sym, `M=1.835347e9g`). Terminal `M_arch/M_exact−1` remains +2.3324398% (exec) / +2.1959001% (sym) as ROT004 found. The new result is **nonmonotonicity and opposite-sign successive secant deviations**, not rediscovery of the endpoint value.

## 5. Spectral-law branches share exactly one recorded active history per map

For all 1470 source-active rows, `public_exec` is **bitwise-identical** to `paper_exec` in `a,t,T,M,X_n` AND the six hadron densities. Likewise `public_sym` is bitwise-identical to `paper_sym` for these fields. The two source spectra agree on the source-supported `M≥10^9g` region by construction. Consequently any recorded `paper−public` endpoint difference is mediated by the **unsampled sub-table source interval and postsource memory**, not by distinct **recorded preedge** histories for the same charge map. The map differs even above the table boundary and produces slightly distinct source-active numerical backgrounds; that does not license a physical map-to-background claim absent numerical validation.

This is important for attribution: previous ROT013 bridges improve inherited states separately for maps and alter source-law *sensitivity*, but cannot claim to observe paper-vs-public differences above the edge in original raw runs.

## 6. What this does, and does not, establish

**Established within archived-output host:**
1. Two independently simulated reaction-map backgrounds violate a mathematically constant rate-of-change invariant and exhibit a local sign switch in B_exec's secant error, much larger than Float64/csv serialization effects.
2. A global offset of the time labels (ROT014) can be invariant in a reduced ODE yet **cannot remove a varying** `R_i` of historical sampled masses.
3. No source-active saved data below table edge, so 10D end-run emission and hadronic memory require internal step capture, event-aligned sampling and explicit tolerance checks.

**Not established:** actual accepted Julia step accuracy; physical mass-loss uncertainty; any bound on `X_n` absolute/global error; guaranteed sign of B-exec/B-sym under source-valid spectra; revised `Y_p/D/H` or PBH exclusion; source-invalid E2b claim. Ratios `r_i` are **secants on saved/dense-interpolated sample points**, not direct derivatives of accepted numerical states. SciML docs distinguish adaptive time stepping, postsolution dense interpolation and output sampling; the source code uses `solve(evolution_problem, AutoTsit5(Rosenbrock23()))` with no explicit tolerances and evaluates `evolution_solution(log(a))` afterward on 1600 points.

**Decision for existing P1 executor:** request/source instrument *no new task cascade*: original 10D Julia run with logged ACCEPTED internal points / step states vs sampled dense-output points; exact analytical `M³(t)` monitor for both, source-on/off event detection (with no hidden step over `M=10^9 g`), explicit tolerance ladder, synchronized T event, `Q_species / n_h / A / B / X_n`. If future raw accepted-step diagnostic passes while dense-output monitor fails, classify as interpolation; if both fail, assess integration/threshold handling; no premature blame of any single solver component. DAX/PRF thermodynamics and independently validated hadronic sub-table source remain separate physical prerequisites. Independent REC10/M13 claim review desirable only when it yields actual material correction; no artificial owner handoff.

## 7. Reproducibility package

Full executed Python `reproduce_mass_cube_secant_audit_015.py` (NumPy, Pandas, standard Decimal/zip/hash) validates two ZIP SHA256 before loading, processes all source-active rows, computes factorized two-sample Γ, exact mass and per-point defect, Decimal verification, branch equality, threshold crossings. Outputs:
- `all_source_active_mass_clock_015.csv` — all **5880** branch-active rows and diagnostic columns;
- `selected_secants_decimal_controls_015.csv` — **36** high precision late sample checks;
- `secant_branch_summary_015.csv` — four branch summaries;
- `threshold_crossings_015.csv` — error boundaries;
- `result_015.json` — source pins, exact numbers and holds;
- `run015.log` — executed stdout;
- two original, exact SHA-checked, raw Mech-S6 archives, and `MANIFEST_015.json` with file checksums.

Permanence: save report plus code to public-safe GitHub with full readback; local complete ZIP for independent source audit; Slack scientific return to already relevant cells. `GITHUB_WRITE != BW_COMMITTED != OWNER_ACCEPTED != EXEC_SIGN`.

**Final status:** `EXECUTED_ARCHIVED_ALL_SAMPLES / EXACT_MASS_CUBE_SOURCE_CONTROLS / BITWISE_PREEDGE_SPECTRAL_INVARIANCE / SOURCE_VALID_E2B_OPEN / FULL_10D_JULIA_NOT_EXECUTED`.