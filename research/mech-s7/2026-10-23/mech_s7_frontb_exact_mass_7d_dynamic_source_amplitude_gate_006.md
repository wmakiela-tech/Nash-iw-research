# IW/NASH MECH-S7 — ROT006: exact-mass terminal 7D kinetic comparator and source-amplitude sign switch

```yaml
RETURN_ID: MECH-S7-FRONTB-EXACT-MASS-7D-DYNAMIC-SOURCE-AMPLITUDE-AND-MEMORY-GATE-006_20261023
CELL: IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7
DATE: 2026-10-23
PROBLEM_ID: P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001
RESULT_CLASS: EXECUTED_INDEPENDENT_CONDITIONAL_7D_KINETIC_REPLAY / MASS_EVENT_CONTROL / EXPLICIT_TOLERANCE_AND_SOURCE_AMPLITUDE_COUNTERTEST
MODEL_STATUS: REDUCED_TERMINAL_COMPARATOR; NOT_SOURCE_NATIVE_FULL_10D
EXPOSURE: PUBLIC
PRIOR_ART: STANDARD_STIFF_ODE_SOLVING / MASS_VARIABLE_TRANSFORM / CONDITIONAL_RESPONSE / NO_NOVELTY
CLAIM_CEILING: NO_SOURCE_VALID_E2B / NO_MODERN_Yp_DH / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
BW_INGEST: UNVERIFIED
```

## 1. Scientific question

Mech-S7 ROT005 found that frozen-coefficient, signed INTEGRATED hadronic impulse of the Wu–Xu terminal sub-table segment had **positive** paper-minus-public change for BOTH reaction maps, unlike the opposite source-law signs in historical four full Wu–Xu trajectories at fixed nuclear temperature. Does **time-dependent coupled neutron and six hadron population dynamics**, isolated on one common numerical cosmological background and with the PBH mass evolved exactly, suffice to generate opposite signs? Does that sign survive numerical convergence, hadronic source amplitude interventions, and the fate of hadrons after Hawking source shutdown?

## 2. Source chain and exact type

- Primary public Wu–Xu code pinned at `Fenyutanchan/Primordial-Black-Hole` commit `d395183674cace6c9906a8911bdeb7234ba4040d`, especially `arXiv-2509.05618/main-scan.jl`, `tool_script-hadrons_from_PBH.jl`, and `tool_script-parameters.jl`. Five aggregate hadronic source columns, tracked six populations: π−, π+, K−, K0L, pbar, nbar.
- Original public and paper 2×2 archived Actions ZIPs, SHA256 `75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5`, `3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e`. Their mass errors and fixed-T diagnostics were audited in ROT001–ROT004.
- Hot-PBH source exact mass-cube from ROT004: `Γ = 4.207579833788249e27 g^3/s`, `M^3=M_edge^3-Γ(t-t_edge)`. Use `u=M/(1e9 g)` as independent variable, terminal u runs from 1 to cutoff `6exp(-20)=1.23669e-8`. Window is ≈0.2376663 seconds. This removes stiff/time-discretization dependence of the mass variable but **does not** validate subedge hadron emission.
- Hawking tables: all source rates identical at 1e9g and differ only below by (i) public first-two-row log slope around −1.20; (ii) paper −1.3; use source number per PBH from original first table rate in GeV divided by ħ [GeV s] multiplied by PBH number density cm⁻³. Charge mapping `B_exec` uses paired aggregate source into each tracked charge state; `B_sym` uses half for π−, π+, K−, pbar, nbar, K0L unchanged.
- Hadron collisions, decays and weak neutron rates are reconstructed from the pinned source formulas. `d n_i/dt=S_i−D_i(X,T)n_i`, `dX/dt=Γ_SM((1−X)e^(−Q/T)−X)−X/τ_n+Σ_i[(1−X)a_i(T)−X b_i(T)]σ_unit n_i`. All physical cm, seconds, mbarn·c conversions explicit in script. Source-native hadron equations themselves do NOT include an additional 3H dilution term.
- **Common background** T(t) and a(t) is a single PCHIP of the archived `public_exec` trajectory. PBH number source is rescaled from its archived last source-active density by `(a_ref/a(t))^3` with no independent source-law-specific background. The fixed-T nuclear target is the **root of this same PCHIP**, not a common-a readout and not a linear-in-time interpolation.
- **Crucial boundary caveat:** since no archived source-active samples exist at M<1e9g, the archive states X and n_i at LAST SOURCE-ACTIVE sample M≈1.83663e9g are **reassigned as a surrogate initial state at M=1e9g**. This is intentionally not a valid source-native preedge propagation. Tests use zero, archived, double hadron-population initialization; X initial per reaction map from archived respective supported cell. No external source-valid E2b is available. No original Julia 10-variable solve is claimed.

## 3. Material result: opposite source-law signs emerge in 7D dynamics

All entries below `paper - public` under the same map. Stiff Radau solver, `rtol=3e-9`, explicit `atol=rtol*1e-3` on the numerically scaled states, initial populations from last supported archive; terminal-source mass controlled analytically.

| Map | X_public at fixed T_nuc | X_paper at fixed T_nuc | ΔX at cutoff | ΔX at fixed T_nuc |
|---|---:|---:|---:|---:|
| B_exec | 0.397801320526 | 0.397794448864 | −7.99445206e−6 | **−6.87166123e−6** |
| B_sym | 0.396614045913 | 0.396636501549 | +2.76725208e−5 | **+2.24556358e−5** |

This recovers the **opposite signs** of the four originally archived fixed-temperature source-law contrasts (B_exec −1.89885666e−5, B_sym +1.26671312e−5) even when their independently integrated cosmological backgrounds are replaced by ONE prescribed background. Magnitudes differ materially; this conditional 7D model does not reproduce the original 10D numerical solution.

The frozen terminal impulse sign conclusion of ROT005 and this dynamic result are not logically inconsistent. ROT005 kept X and coefficients constant. Here X dynamically updates and feeds back into all six population losses and their signed conversion; furthermore the postsource weak response propagates nonlinearly around cell-specific histories.

## 4. Tolerance ladder and initial-data stability

| Radau rtol | B_exec ΔX target | B_sym ΔX target |
|---|---:|---:|
| 3e−5 | −4.26234738e−6 | +2.32048869e−5 |
| 3e−7 | −6.86860939e−6 | +2.24561085e−5 |
| 3e−9 | −6.87166123e−6 | +2.24556358e−5 |

Finite-tolerance drift is material at 3e−5; both signs stabilize at 3e−7 and 3e−9, without constituting a verified rigorous global error bound. At rtol 3e−7, replacing archived six starting populations by ZERO or twice the archive values changes the endpoint source-law contrast by less than ≈1e−9 in either map: conditional terminal production dominates their *initial population* memory. This does **not** validate the surrogate starting neutron X, background, or source extrapolation.

An attempted independent BDF reproduction at tight tolerances failed with `Required step size is less than spacing between numbers` in postsource stiff dynamics. **Do not count BDF as a PASS or cross-integrator validation**. Successful method was SciPy Radau alone.

## 5. Postsource memory: source-OFF is not forcing-OFF

With the same terminal 7D source solution, compare full postsource propagation with deliberately ZEROING all six hadronic densities immediately at PBH cutoff:

| map | Retain postsource n_i ΔX | Artificially discard n_i ΔX |
|---|---:|---:|
| B_exec | −6.87166123e−6 | −6.37847682e−6 |
| B_sym | +2.24556358e−5 | +2.20788781e−5 |

Postsource residual hadrons change the source-law contrast by around +7.73% in magnitude (exec) and +1.71% (sym), **but do not cause the sign difference** in this reduced setup. This concretely respects the Rec10 ROT08 source-off memory caveat and distinguishes memory of freshly emitted hadrons from memory of preedge initial conditions.

## 6. Counterexample/gating discovery: source amplitude changes the sign

Uniformly rescale all six source injection rates at fixed prescribed background and fixed starting X,n_i. **This is a causal model intervention, NOT a physically consistent variation of cosmological β**, since background mass/temperature are held fixed.

| Source multiplier vs archival n_PBH normalization | B_exec ΔX fixed T_nuc | B_sym ΔX fixed T_nuc |
|---|---:|---:|
| 0.5 | **+1.05428492e−6** | +1.54120471e−5 |
| 1.0 | **−6.87283267e−6** | +2.24563488e−5 |
| 2.0 | −3.05906073e−5 | +2.09457543e−5 |

The B_exec sign switches as source injection rises. A bracketing solve finds a **conditional zero at multiplier ≈0.5970**, checked at Radau rtol 3e−9. The root is local to the prescribed 7D model; it is *not* a confidence interval, source error estimate, universality result, or validated PBH parameter threshold. The B_sym contrast remains positive at 0.5/1/2 in this test.

This falsifies any overly broad claim that the mere source-law change or charge map **guarantees** opposite signs. The dynamics can generate them, but model normalization can also destroy them. The correct next experiment must control and independently justify the hadron source, mass and geometry together.

## 7. Where the sign is determined

Independent 7D Radau dense-output traces at u=M/(1e9g) in `mass_resolved_7d_trace_006.csv` show: for the reference (multiplier 1) B_exec `ΔX(u=0.5)` already negative (~−1.36445e−6), growing in magnitude by u=0.1 (~−7.544e−6), and reaching −7.994e−6 at cutoff. B_sym remains positive throughout sampled masses. At half source amplitude B_exec is positive from u=0.5 to cutoff. These event-aligned probes are on a **controlled exact mass coordinate**, not the sparse independent-a archived grid.

## 8. Recipient/source tests, handoff, STOP rules

- **REC10/M13:** independently attack whether source-native `Γ_h` and direction-specific `D_h` / baryon density / charge pairing reconstructed here correctly match the pinned code. The scientific claim stays conditional until that independent check. Review the target root vs linear Q/T archive readout and the explicitly approximate last-supported-state-at-edge initialization.
- **MT13:** preserve distinction between local channel cancellation (`ROT003`), state endpoint uniform global numerical error criterion (`MT13 <6.33356560558e−6` for source four-cell sign certification), and the **nonrigorous** integrator convergence of this new 7D problem; do not conflare numerical tolerance with a rigorous bound.
- **KN11/BW:** GitHub publication is not BW ingestion, scientific review, owner adoption or EXEC.
- **NEXT source-native decisive gate:** full original **10D Julia**, source-active internally accepted steps below 1e9g, exact mass event audit and step/tolerance ladder, shared cosmological background and correctly event-aligned fixed-T target. An independently legitimate subedge hadron emission model plus helium/deuterium likelihood would be required for physical interpretation; this test provides neither.
- **STOP:** stop any claim of physical Yp, D/H, PBH abundance bounds, or theorem/discovery attribution until those requirements pass. The pinned public code's `Yp=2X/(1−X)` is a reduced/source-public readout with known version differences (PRF11 currentness), not a certified true helium mass fraction.

## 9. Reproducibility

Main script `terminal_7d_exact_mass_common_background_006.py`; controls `test_controls_006.py`, `test_scale_and_mass_traces_006.py`, `locate_amplitude_root_006.py`; exact original SHA-verified Actions ZIPs, main result JSON, tolerance table CSV, mass-resolved event CSV, source-scale CSV, postsource-memory CSV/JSON, amplitude threshold JSON, saved log and version manifest. Source-native physical constants embedded. All inputs and model preconditions fail-closed where practicable. Scripts require Python + numpy, pandas, scipy and SciPy `Radau`.

`NO_SOURCE_VALID_E2B / NO_10D_JULIA_EXECUTION / NO_BOUND / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / BW_NOT_ASSUMED`.