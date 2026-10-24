# Mech-S7 ROT021 — Target-adjoint response to pointwise pair-sum-conserving antinucleon redistribution

**RETURN_ID:** `MECH-S7-FRONTB-ANTINUCLEON-ADJOINT-MASS-KERNEL-AND-C2-PLATEAU-KILL-021_20261025`  
**PROBLEM:** `P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001`  
**DATE:** 2026-10-25. **TYPE:** `EXECUTED_CONDITIONAL_7D_ADJOINT / SOURCE_LOCAL_MASS_KERNEL / INDEPENDENT_CENTRAL_FINITE_DIFFERENCE / NONLINEAR_C2_EXACT_PAIR_SUM_ROOT`.

## 1. Source/provenance and scientific motivation

Pinned author Wu–Xu `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`, original table `arXiv-2509.05618/data/out/hadrons_from_PBH.dat` blob `06d0883a27b108692720422294ba2baacd381a64`, public software `tool_script-hadrons_from_PBH.jl` separate log–log source interpolation/extrapolation. **Mech-S7 ROT020** already demonstrated conditional sign reversal when changing only subedge pbar/nbar partition of exactly preserved pair-sum production, with C² edge matching. ROT021 answers a different question: **which PBH mass windows contribute to that target response, and can a source-to-target adjoint predict the actual ODE outcome quantitatively?**

**Others first and theory host:** Mech ROT003 antinucleon sign cancellation; ROT004 exact hot-limit mass cubing; ROT006/007 original conditional 7D, source Shapley; ROT008 mass shells for switching *all* source species; ROT011–013 thermal and preedge bridge; ROT019 pinned p/n ratio edge continuation; ROT020 C² pair-sum-conserving full ODE counterexample. NC Oct10 integrated hadron yield and MT13/NC/LT5 event-weighted source functional sufficiency and moving-endpoint adjoints provide mature theoretical hosts. REC10 postsource-hadron-memory guard; DAX-S7/PRF11 two-temperature source thermodynamics and separate helium target genealogy. No new mathematical adjoint theorem or novelty is asserted.

Conditional model: last archival source-active state at `M≈1.8366e9 g` is *replayed* through source-tabulated mass `M≥1e9g` using a conditional ten-component preedge bridge, then 7D `[Xn,n_pi-,n_pi+,n_K-,n_K0L,n_pbar,n_nbar]` under exact `d(M³)/dt=-Γ` and a hypothetical two-temperature thermal host, then postsource memory until `Tnuc=.07818527068831995 MeV`. Nominal chi_EM=0.5, constant η_B, mass cutoff `6e9 e^-20 g`. Two alternative charge maps `B_exec/B_sym`. **Not original Julia 10D and all M<1e9g hadron spectra are unsupported extrapolations.**

## 2. Exact model intervention and adjoint identity

Let `u=M/1e9g`, `z=ln(u)`, `z_cut=ln(Mcut/1e9g)`. The baseline public ratio is `r_0(z)=ln(Qp/Qn)` with `Qp,Qn>0`. We alter only the ratio by `δr(z)`, fixing pointwise the pair sum `S(z)=Qp(z)+Qn(z)`:

`Qp_new = S exp(r_0+δr)/(1+exp(r_0+δr))`;  
`Qn_new = S /(1+exp(r_0+δr))`.

Thus `Qp_new+Qn_new=S` at every mass. At baseline, `∂Qp/∂r = Qp Qn/S = -∂Qn/∂r`. The preedge segment and both thermal/baryon histories are unchanged. This preserves the total **count rate of the pair**, not the total physical emitted energy or an independent underlying Hawking branching law.

Along the forward trajectory `dy/dt=F(y,t)` use the conventional terminal adjoint `dλ/dt=−(D_yF)^T λ` with final condition `λ_X(Tnuc)=1`, all six `λ_n=0`. Integrate backwards through postsource and active phases, retaining all kinetic memory. For the source-active mass coordinate `dt/du = −3 (M_edge³/Γ)u²`, the first variation of the final X is

`δXn(Tnuc) = ∫_[z_cut]^0 K(z) δr(z) dz + O(‖δr‖²)`,

`K(z) = 3 (M_edge³/Γ) e^(3z) [nPBH(z)/(ℏ NSCALE)] [Qp Qn/(Qp+Qn)] [c_p λ_pbar(z)−c_n λ_nbar(z)]`.

The `c_p,c_n` are both 1 for `B_exec`, both 0.5 for `B_sym`; the populations are numerically scaled by `NSCALE=1e16`. The full exact 7×7 Jacobian is implemented analytically in `reproduce_causal_kernel_021.py`, including ∂weak/∂X and the X dependence of *all six hadron-loss rates*. We did **not** freeze hadron populations or turn off postsource collisions. This is a **local tangent** identity at the conditional baseline, not a global nonlinear bound.

A compact C² bump in a mass shell `[z_a,z_b]` is `φ(z)=sin^4(π (z−z_a)/(z_b−z_a))` for interior z and 0 otherwise. Independent forward solves use `δr(z)=±2e-4 φ(z)`; Jacobian/adjoint calculation uses the derivative at ε=0. Shell-response coefficients are in `mass_shell_adjoint_fd_021.csv`, all mass-sampled kernel values (5201 log mass nodes) in `mass_sensitivity_kernel_021.csv`.

## 3. Executed adjoint vs full ODE results

Nominal conditional `chi_EM=.5`, fixed η_B, same bridged state and PAPER reference as ROT020. The tested nonlinear source-shape change is `δr(z)=s [λ tanh(z/λ)−z]`, with `s≈4.7163544457e−4` and `λ=.05`, and with **pointwise exact pair-sum** conservation.

| Source map | Actual `Xpublic_modified−Xpublic_native`, independently solved ODE | Linear prediction `∫K δr dz` | Difference prediction−actual |
|---|---:|---:|---:|
| B_exec | `−2.9627097342333e−5` | `−2.9627118991972e−5` | `−2.16496395e−11` |
| B_sym | `−1.6143379332756e−5` | `−1.6143389784215e−5` | `−1.04514591e−11` |

Tight nominal forward `Radau rtol=3e−9` gives actual changes `−2.9627099640384e−5` (exec), `−1.6143379705735e−5` (sym); corresponding linear predictions `−2.9627118992065e−5`, `−1.6143389791157e−5`. These small variations check numerical stability, **not certified global accuracy**.

For 4 compact mass-shell interventions per map, full `±2e−4` ODE central differences independently agree with adjoint shell coefficients. Maximum absolute discrepancy across all 8 tests is `4.1015e−9` in units `∂Xn/∂ε`, corresponding to an endpoint difference much smaller than the demonstrated `~1e−5` nonlinear shift. All 5201 sampled values of `K(z)` are negative in both nominal maps; this is a numerical sign observation, not a theorem for untested backgrounds or arbitrary source populations.

## 4. Conditional mass localization (this particular ratio-shape intervention)

Integrate signed `K(z) δr(z)` over mass. Contributions have the same sign for the tested shape, so the fractions below are positive. **Fractions are conditioned on a specific intervention and target; they are NOT source emission percentages or universal physical response fractions.**

| PBH mass at least | B_exec fraction | B_sym fraction |
|---|---:|---:|
| `2e7 g` | 99.0790% | 99.1543% |
| `5e7 g` | 96.2135% | 96.5218% |
| `1e8 g` | 89.4968% | 90.3326% |
| `2e8 g` | 72.9143% | 74.8940% |
| `3.5e8 g` | 47.2371% | 50.3241% |
| `5e8 g` | 25.7639% | 28.7640% |
| `7.5e8 g` | 4.6616% | 5.7335% |

Half the tested X shift comes from masses **below approximately 3.342e8 g in B_exec and 3.535e8 g in B_sym**. This is compatible with ROT008's broad localization of *whole-spectrum law changes*, but not interchangeable with ROT008 source-only fluence fractions.

## 5. Sharp first-order L-infinity obstruction and **executed nonlinear threshold**

First-order Hölder bound for each charge map:

`|δXn| ≤ ‖δr‖∞ ∫_[z_cut]^0 |K(z)| dz + O(‖δr‖²)`.

Computed `∫|K| dz`: **0.0998347382343** (exec) and **0.0602219590970** (sym). In the *local linearization*, changing the existing paper−native difference to zero would require at least `‖δr‖∞≈1.45752e−4` for exec and `≈1.87351e−4` for sym if the entire kernel can be exploited optimally. These are first-order necessity estimates, not globally certified lower bounds or allowable physical uncertainty.

A distinct **C²-edge-matched**, exactly pair-sum-preserving nonlinear intervention:

`δr(z)=ε [1−exp(−(z/0.15)^4)]` for `z≤0`, and 0 above the edge. Value and first three derivatives are zero at the edge; for `M=1e8g`, the multiplier is effectively saturated at ε. This is a controlled model probe; it is *not* an emitted Hawking spectrum.

Independently re-integrating preedge bridge, 7D source-on and 7D postsource dynamics with an unchanged PAPER comparator, numerical `Radau rtol=3e−9` gives:

| Source map | ε root of `Xpaper−Xpublic(ε)=0` | Relative p/n-ratio change at `1e8g` | Root residual in ΔX |
|---|---:|---:|---:|
| B_exec | **+0.00017176888993895** | **+0.01717836%** | `−2.31e−14` |
| B_sym | **−0.00022895072570425** | **−0.02289245%** | `−2.34e−13` |

At `rtol=3e−8`, the roots were +0.00017176935257755 and −0.00022895068903819; their shifts with tighter rtol are `−4.626e−10` and `−3.667e−11`. Tight solver consistency is not a global error certificate. The observed nonlinear roots lie above the respective first-order L∞ necessity estimates, as anticipated for a C² profile which cannot exert the full uniform perturbation at the boundary.

**Important distinct-root warning:** ROT020's root `λ≈0.578895` varies the *saturation width with amplitude dictated by `s`*. ROT021's roots above vary an independent *ratio amplitude ε at fixed width 0.15*. These are different controls and must not be conflated.

## 6. What is learned and what remains open

**Supported decision:** the conditional map `mass-resolved correlated ratio source → surviving pbar/nbar kinetic populations → signed n/p exchange → Xn(Tnuc)` has an explicit computed target-sensitivity kernel. Independent finite differences confirm that maintaining the total pair emission and all edge jets through second order does not identify the sign of B_exec. For the C² fixed-width family, a ratio change around 0.0172% at subedge masses is sufficient to flip this *conditional model* contrast; other shapes have different thresholds. The mass distribution identifies `1e8–~7e8g` as the most efficient first target for genuine correlated p/n source data **for this objective**.

**Not supported:** universal bounds from a finite-difference kernel, physical uncertainty on Hawking branching, true BBN helium or D/H response, original source-active Julia 10D numerical error or integrator accepted-step validation, source-valid rate below `1e9g`, actual PBH constraints. The thermal energy partition and baryon prescriptions are constructed stress axes, not measured physical ranges. Our source-only pair sum preserves particle counts, not necessarily full emitted energy spectra. The terminal target is `Xn`, NOT the article's contested `Yp` proxy. `NO_NOVELTY` for adjoint machinery.

A concrete next owner decision is to seek physically sourced mass-resolved **joint pbar/nbar branching** (with energy consistency), original source-native Julia accepted steps and correctly defined T event before promoting any BBN claim. Reuse existing MT13/REC10/KN11/LT5 impact pathways; do not create a new parallel registry/task cascade.

## 7. Reproducibility and custody

Executed scripts:

- `reproduce_causal_kernel_021.py` — builds original conditional state/host, forward 7D, analytic Jacobian, backwards adjoint through postsource, 5201-node mass kernel, 8 independent ± perturbation pairs, writes `causal_kernel_021.json`, `mass_sensitivity_kernel_021.csv`, `mass_shell_adjoint_fd_021.csv`.
- `reproduce_c2_plateau_kill_021.py` — independently solves full nonlinear ratio-amplitude root per map at two tolerances and writes `ratio_plateau_roots_021.csv` and `ratio_plateau_root_021.json`.
- Tight controls: `precision_kernel_021.json`, `precision_roots_021.json` plus `run_tight_021.log`, `run_roots_tight_021.log`.

All dependencies and *original* S6 public/paper trajectory archives copied exactly from the verified ROT020 bundle; manifest SHA256 covers all files (except itself and the outer ZIP). Original author source commit is pinned as above. Clean-directory reproducibility rerun and byte hashes are separately recorded in `clean_replay_021.json`.

`STATUS = EXECUTED_CONDITIONAL_ADJOINT_AND_FULL_ODE / EXACT_PAIR_SUM / 8_SHELL_FINITE_DIFFERENCE_CONTROLS / TIGHT_ROOT_NUMERIC_PASS / NO_SOURCE_VALID_E2B / ORIGINAL_JULIA_10D_NOT_EXECUTED / BW_INGEST_UNVERIFIED / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PBH_BOUND`.