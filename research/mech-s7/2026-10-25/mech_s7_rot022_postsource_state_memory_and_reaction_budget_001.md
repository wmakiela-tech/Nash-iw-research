# Mech-S7 ROT022 — Post-source state-memory contribution to the exact-pair-sum antinucleon sign witness

**RETURN_ID:** `MECH-S7-FRONTB-POSTSOURCE-STATE-MEMORY-SHAPLEY-WEAK-SCATTERING-BUDGET-022_20261025`  
**PROBLEM_ID:** `P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001`  
**CLASS:** `EXECUTED_CONDITIONAL_BRIDGED_10COMP_PLUS_7D / EXACT_NONLINEAR_POSTSOURCE_STATE_SWAP / 4GROUP_SHAPLEY / INDEPENDENT_WEAK_HADRON_INTEGRAL_BUDGET / ROT021_CUTOFF_ADJOINT_VALIDATION`  
**DATE:** 2026-10-25. **Scientific authority:** NONE (`NO_CANON / NO_EXEC_SIGN`).

## 1. Source, preceding results and question

Original Wu–Xu primordial-black-hole solver pinned to `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`; the source-table Git blob is `06d0883a27b108692720422294ba2baacd381a64`. Original S6 archival source cells are retained byte-for-byte (`mech_s6_public_2x2_raw.zip` SHA256 `75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5`, and paper equivalent `3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e`). Current model is the same **conditional** 10-component tabulated preedge bridge → seven-dimensional active subedge kinetics → postsource kinetics evaluated at common `Tnuc=.07818527068831995 MeV` as Mech ROT013, ROT020 and ROT021. The original Julia 10D was **not** run.

**Already known elsewhere, no priority claim:** Mech ROT003–005 (signed source channels vs residual postsource hadron populations), ROT013 preedge state repair, ROT019 C² spectral-shape insufficient information, ROT020 full 7D sign falsifier with fixed pair-sum and ROT021 source-to-target mass adjoint and finite-difference validations. REC10 hadron memory and MT13/NC/LT5 target-weighting are mature hosts. DAX-S7/PRF11 R21/R22 resolve source-table versus physical two-temperature cooling issues under specified assumptions. Here the targeted question is **what fraction of a particular change of final Xn derives from the neutron state at source-off versus the modified hadron populations surviving at that same boundary?**

## 2. Exact intervention and nonlinear state-swap definition

Under the **public** subedge source continuation, let `r0(u)=ln(Qpbar(u)/Qnbar(u))` at `u=M/1e9g`. Compare the native continuation with the positive `C²`-matched ROT020 modification `r1=r0+s[λ tanh(ln u/λ)−ln u]`, where `s≈4.7163544457e−4` and `λ=.05`. At **each mass**, enforce exact pair-sum `S=Qpbar+Qnbar` through the logistic replacement

`Qpbar_new=S exp(r1)/(1+exp(r1))`, `Qnbar_new=S/(1+exp(r1))`.

All other source channels, the initial preedge archived state, thermal host and baryon prescription are fixed *within each paired comparison*. The two resulting seven-vectors at source-off are `y0=(X0,n0)` (native) and `y1=(X1,n1)` (modified). Evolve either vector under the same source-OFF nonlinear ODE flow `Φ(y)` to the shared `Tnuc` event.

Exact two-group permutation-average (finite, **not** linear) of the source-off state:

```
F00 = Φ(X0, n0), F10 = Φ(X1, n0),
F01 = Φ(X0, n1), F11 = Φ(X1, n1).
D_X = 1/2[(F10−F00) + (F11−F01)];
D_n = 1/2[(F01−F00) + (F11−F10)].
Identity: F11−F00 = D_X+D_n.
```

This answers a **model intervention accounting** question, not a unique physical decomposition into independent realizable universes. Grouped source-off initial conditions are counterfactual. A second 4-group Shapley game splits `[X_cut, 4 mesons, pbar, nbar]` and computes all `2^4=16` hybrid postsource solves per map, using factorial Shapley weights; their contributions sum exactly to the finite target difference. **DO NOT confuse those state Shapley contributions with source Shapley (ROT007) or time-resolved source/target kernel (ROT021).**

## 3. Primary executed results, nominal chi_EM=.5, constant eta_B; Radau rtol=3e−9

All X differences below are `PUBLIC_modified − PUBLIC_native`, *not* the PAPER−PUBLIC contrasts reported in ROT020/021. All hadron populations remain present and reacting after source-off; neither baseline postsource nor its weak dynamics are frozen.

| Quantity | `B_exec` | `B_sym` |
|---|---:|---:|
| `δX_cut` (at source-off) | `−3.599791151498444e−5` | `−1.963062775939273e−5` |
| `δX_nuc` (full nonlinear model) | `−2.962709860260260e−5` | `−1.614337907523966e−5` |
| **2-group `X_cut` contribution** | `−2.886384015635124e−5` | `−1.576029864619466e−5` |
| **2-group inherited six-hadron-population contribution** | `−7.632584462513581e−7` | `−3.830804290450018e−7` |
| `X_cut` fraction of finite `δX_nuc` | **97.42378268%** | **97.62701212%** |
| Surviving-hadron population fraction | **2.57621732%** | **2.37298788%** |

**Four-group Shapley of full finite response:**

| Source-off state group | B_exec | B_sym |
|---|---:|---:|
| `X_cut` | `−2.886384023478850e−5` | `−1.576029874106784e−5` |
| Four meson populations | `−7.5689e−14` | `+3.7030e−13` |
| `pbar` surviving population | `−3.804882528305834e−7` | `−1.904689701191324e−7` |
| `nbar` surviving population | `−3.827700392940632e−7` | `−1.926117343536981e−7` |

The numbers show an important **negative control**: for this **particular pbar/nbar-ratio modification**, the final contrast is **NOT driven predominantly by late differences in surviving hadron populations**. Approximately 97.4–97.6% of the finite endpoint response is attributable to the neutron fraction already imprinted when the PBH source switches off, after postsource propagation of that boundary condition. This **does not say** that postsource evolution or reactions are negligible for the absolute neutron abundance, or for different source interventions, maps or physically admissible dynamics.

## 4. Independent fundamental-theorem-of-calculus dynamic budget

Independently integrated two accumulated postsource reaction channels as additional state variables `I_weak=∫_{tcut}^{tnuc}f_weak(t)dt`, where `f_weak` includes standard weak interconversion and neutron beta decay, and `I_hadron=∫ f_hadron(t)dt`, where `f_hadron=Σ n_i σv_i[(1−X)a_i−Xb_i]`, along each independently solved public native/modified postsource trajectory. Mathematically exact identity on each solve:

`δX_nuc = δX_cut + δI_weak + δI_hadron`.

| Term | `B_exec` | `B_sym` |
|---|---:|---:|
| `δX_cut` | `−3.599791151498444e−5` | `−1.963062775939273e−5` |
| `δI_weak` | `+7.228668658237902e−6` | `+3.938797300317987e−6` |
| `δI_hadron` | `−8.578564901045910e−7` | `−4.515485961486991e−7` |
| `δX_nuc`, independently integrated | `−2.962709937232022e−5` | `−1.614337903393937e−5` |
| Identity residual | `−2.55e−14` | `+2.13e−14` |

**Do not conflate the two budgets:** `δI_hadron` is the change in **all postsource hadronic reaction integrals**, including changes induced by a modified X even at fixed hadron populations; the 2-group `D_n` isolates **the contribution from changing the source-off hadron populations**, conditional on X and averaging orderings. That they differ is expected. `δI_weak` compensates approximately **20%** of the earlier neutron imprint; hadron integral adds a smaller signed term to the observed final difference. Postsource dynamics is thus essential to transporting source-on differences into the fixed-temperature target despite small population-memory attribution.

## 5. Adjoint cross-check (independently established ROT021)

Use ROT021's backward-integrated cutoff adjoint with `λ_Xcut≈0.80181985516` (`exec`) and `≈0.80284230761` (`sym`). The first-order prediction is `λ(tcut)^T δycut`; it is not assumed exact for finite δy. The independent ROT021 linear predictions and ROT022 **nonlinear** results differ by only `−1.879e−13` (`exec`) and `−1.289e−13` (`sym`). Componentwise, the predicted direct-X and 6-population contributions match exact state Shapley to better than `8e−12` each. This is model-local concordance between three *different* numerical routes: state-swap nonlinear ODE, postsource reaction-integral bookkeeping, and ROT021 tangent adjoint. No certified absolute global ODE error follows.

## 6. Independent thermal/baryon counter-controls

All six combinations were **independently executed**; `rtol=3e−9` for nominal `.5/constant_eta`, `rtol=3e−8` for additional thermal extremes with conserved comoving barions from edge.

| chi_EM, baryons | B_exec inherited-population contribution | B_sym inherited-population contribution |
|---|---:|---:|
| 0.5, constant eta_B | 2.5762173% | 2.3729879% |
| 0.0, comoving barions | 2.5924531% | 2.3869992% |
| 1.0, comoving barions | 2.5824395% | 2.3787786% |

All signs and fractions persist in these tested counterfactual axes. **This does not certify all χ/baryon combinations** and does not make χ physically sourced Hawking branching.

## 7. Interpretation, guardrails, and concrete owner decision

**Supported**:
1. The first-order source-to-target sensitivity already observed in ROT021 is mechanistically dominated by the **active-source imprint on X** rather than by later changes in survivors for the fixed-pair-sum C² intervention.
2. There remains substantial postsource *weak-rate evolution*, whose differential contribution modifies the earlier imprint by about one fifth. Therefore `source_OFF ≠ collisions_OFF` and `small inherited-population Shapley ≠ postsource physics irrelevant`.
3. Four-group split finds the inherited meson perturbation below numerical resolution for this **antinucleon-only** shape manipulation; pbar and nbar change-survivor influences have similar magnitudes and the same sign for the chosen redistribution.
4. Temporal full-source data are required for the target, as demonstrated independently by MT13/NC/LT5; one source moment or edge-jet is insufficient. The observed numerical 97% imprint in this specific model does not allow a universal reduced physical theory.

**Not supported**: that the true Wu–Xu full Julia 10D solver has these percentages; that altered Qpbar/Qnbar ratios are physically possible with a fixed total Hawking luminosity; modern BBN Yp/DH; the paper's source-map/target Figure 5; real PBH exclusion limits; certified global numerical truncation errors; novelty or adoption by owner/referee/BW. Earlier controls ROT013 and ROT016–018 do not remove these gaps.

**Owner-useful decision:** when a source-valid original Julia run is available, capture `X_n` and each hadron population **at true source-off and at fixed Tnuc**, along with the integrated weak and hadronic terms and accepted-step/event fidelity. A ref/cell can then test whether the large active-source imprint and small survivor-population differential persist, instead of mistaking late postsource survivors for the sole origin of the final contrast.

`STATUS: EXECUTED_CONDITIONAL_STATE_SHAPLEY / 16_SOURCE_OFF_HYBRID_STATES_PER_MAP / 6_THERMAL_BARYON_CONTROLS / INDEPENDENT_FTOC_REACTION_BUDGET / ADJOINT_CROSSCHECK_PASS / ORIGINAL_JULIA_10D_NOT_EXECUTED / NO_SOURCE_VALID_E2B / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PBH_BOUND / BW_INGEST_UNVERIFIED`.