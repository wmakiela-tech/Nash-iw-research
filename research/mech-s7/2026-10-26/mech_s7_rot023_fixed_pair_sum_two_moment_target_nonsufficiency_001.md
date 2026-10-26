artifact_id: MECH-S7-FRONTB-FIXED-PAIR-SUM-TWO-MOMENT-TARGET-NONSUFFICIENCY-023_20261026
exposure: PUBLIC
claim_ceiling: EXECUTED_CONDITIONAL_BRIDGED_10_COMPONENT_PLUS_7D / MOMENT_CONSTRAINED_SOURCE_TARGET_COUNTEREXAMPLE / NO_PHYSICAL_UPGRADE
sync_state: GITHUB_PENDING_BW_INGEST

# Mech-S7 ROT023 — Equal total and first log-mass moment of each antinucleon source do not determine the conditional neutron endpoint

**Date:** 2026-10-26 (Europe/Warsaw). **Lineage:** `IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7`.  
**Problem:** `P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001`.  
**Return ID:** `MECH-S7-FRONTB-FIXED-PAIR-SUM-TWO-MOMENT-TARGET-NONSUFFICIENCY-023_20261026`.  
**Scientific classification:** completed source-informed **conditional** preedge 10-component bridge + active/postsource 7D Radau replay, moment-null source geometry, independent ROT021 adjoint consistency, numeric source-root and thermal controls. **Not original Julia Wu–Xu 10D and not physical BBN.**

## 1. Source-native facts, lineage and independent prior-art credit

Pinned author source: Wu–Xu, *Primordial black holes evaporating before Big Bang nucleosynthesis*, JCAP 02(2026)063, code `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`, `arXiv-2509.05618/main-scan.jl`, `tool_script-hadrons_from_PBH.jl`, `data/out/hadrons_from_PBH.dat` (source Git blob `06d0883a27b108692720422294ba2baacd381a64`). Original S6 public/paper 2×2 ZIP SHA256: `75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5` and `3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e`. The current 10-component bridge evolves the original **last saved active states** from about `1.8366e9g` to `1e9g`, uses the original hadron source table for that above-table interval and holds a stipulated micro two-temperature background, after Mech ROT013; it is **not** a source-native rerun of the 10 original Julia ODEs.

Others-first: Mech ROT019 showed that the boundary jet of `Qpbar/Qnbar` cannot determine its continuation; ROT020 exhibited **pointwise pair-sum**-conserving C² matched spectral alternatives that reverse a conditional sign; ROT021 supplied a source-to-target adjoint kernel validated by direct mass-shell finite differences; ROT022 separated active-source imprint in `X_cut` from survivor-population contributions and postsource weak/hadron integrals. The more general *time-weighted target vs aggregated source-moment insufficiency* is already structurally developed by NC (October 10 source mass balance), MT13 and LT5, including event-sensitivity hosts; this result is **a targeted source-informed numeric witness**, not a claim of new theorem-family novelty. REC10 hadron memory and DAX-S7/PRF11 R21/R22 source-cooling/thermodynamics are credited separately.

## 2. More restrictive question than ROT020

Can two **positive** source spectra yield a distinct endpoint even if (a) `Qpbar(M)+Qnbar(M)` is exactly identical *pointwise*, (b) the **comoving integrated emitted numbers** of pbar and nbar separately are identical, (c) their **first log-mass emission moments** are identical, and (d) the source laws are unchanged, with all derivatives, near and above the original `1e9 g` table edge? All other four hadron production channels, background and collision/weak coefficients are also identical. Answer: **YES in the executed conditional 10+7-dimensional model.** Even the signed PAPER–PUBLIC endpoint comparison can flip.

The moments are not moments of **surviving hadron populations** or already converted neutron fractions. Let `u=M/(1e9 g)`, `z=ln u`, `u_cut≈1.2366921734631341e−8`, and use the source-native hot-mass-cube law `dt=−3 Δt_edge u² du=−3 Δt_edge u³ dz` with common PBH history. Because `a³ n_PBH` is common and constant in the prescribed background, source emission into a comoving volume is proportional to `3Δt_edge ∫u³ Q_i(u) dz`. Define

`L_j[Qi]=3Δt_edge ∫_(ln ucut)^0 u³ Qi(u) (ln u)^j dz` for `j=0,1`.

This exact weighting distinguishes comoving emitted fluence from instantaneous source rates `Q_i`, current number densities, or postsource survivors. It does **not** claim that arbitrary mass-weighted source moments are physically measured.

## 3. Explicit smooth positive, two-moment-null source construction

Take **three compact nonoverlapping intervals** in `u`:

- LOW `u∈(0.07,0.20)` = `7e7`–`2e8 g`;
- MID `u∈(0.23,0.43)` = `2.3e8`–`4.3e8 g`;
- HIGH `u∈(0.50,0.85)` = `5e8`–`8.5e8 g`.

On each interval use `b_i(u)=sin^4(π (ln u−ln l_i)/(ln h_i−ln l_i))` and zero elsewhere. The pieces and their first three derivatives vanish on each boundary, so the altered spectra coincide with all derivatives of the original source near `u=1`. Their supports lie **entirely below** the validated first row of the author table.

Let `S(u)=Qpbar_native(u)+Qnbar_native(u)>0` and the `2×3` matrix `A_ji=∫u³ S(u)(ln u)^j b_i(u)dz` for `j=0,1`. Numerically the rows are

```
A0 = [ +614.1539437597633, +2069.421721880875, +6473.984914579834 ]
A1 = [-1286.6123712385847, -2364.8965480596603, -2704.3775147066003 ]
```

Take the null direction `c ∝ A0×A1`, orient it negative at LOW, and normalize `max|h|=1`, where `h(u)=Σ c_i b_i(u)`:

`c=[−1, +0.6865078710932105, −0.12457865867224774]`.

**At every mass**, set

`Qpbar_eps=Qpbar_native+eps*S*h`,  
`Qnbar_eps=Qnbar_native−eps*S*h`.

There is no change to any other hadron rate. Algebraically `Qpbar_eps+Qnbar_eps=S` *for all M*. Because `A c=0`, both `L0` and `L1` are unchanged **for each species** under exactly the same cosmological history, for every amplitude where both rates stay positive. The remaining **second** log-mass moment does change: `∫u³ S h z² dz = −987.5910917755671` in the same common source normalization. The construction is a simple three-window linear-algebra null vector of a rank-two measurement map, consistent with mature moment-problem hosts; novelty is not claimed.

**Independent direct quadrature of both species** at `eps=.005`, **without subtracting two large separate integration results first**, yields the original and modified `L0` (normalization includes `3Δt_edge`):

| Comoving source moment | Native source | Altered source | Relative difference |
|---|---:|---:|---:|
| `L0[pbar]` | `12672.129834873149` | `12672.129834873150` | `1.44e−16` |
| `L0[nbar]` | `12605.102432589025` | `12605.102432589023` | `1.44e−16` |
| `L1[pbar]` | `−6645.034334834182` | `−6645.034334834182` | `0` at displayed precision |
| `L1[nbar]` | `−6611.774767052367` | `−6611.774767052366` | `1.38e−16` |

These are **floating-point evidence for continuum moment constraints**, not arbitrary exact equality of binary floating-point integral outputs. The identities hold algebraically for the exact null-vector construction. All tested `eps∈[−.005,+.012]` rates remain positive. At the nominal sign root `eps≈.00734641`, the pointwise modified/native ratio `(Qpbar/Qnbar)_eps/(Qpbar/Qnbar)_native` varies between approximately `−2.896%` and `+2.038%` over the tested mass domain; **not** a subpermille physical uncertainty bound.

## 4. Executed dynamical target: nominal 7D kinetics, fixed T event

Common input from ROT013 bridge: original last-source-active archive for a given charge map, evolved through original tabulated (M≥1e9g) source segment under the specified micro-EOS/EM heating assumptions. Both native and altered source then propagate through identical active seven state variables `[Xn, nπ−, nπ+, nK−, nKL0, npbar, nnbar]` from `u=1` to source-off `u_cut`, including source-dependent populations, baryon collision loss, weak conversions, and postsource survivors to the common `T_nuc=0.07818527068831995 MeV` event. Numerical solver SciPy Radau, nominal `rtol3e−8, atol3e−11` (as defined in code). The source mass time law `M³` and thermal host are common. **No original Julia 10D execution.**

Primary result at `chi_EM=.5`, constant `eta_B`, difference `X_eps−X_native`:

| epsilon | B_exec target difference | B_sym target difference |
|:---:|---:|---:|
| `−.005` | `+9.9035366678e−6` | `+2.8957650589e−6` |
| `.000` | `0` | `0` |
| `+.005` | `−9.9035368805e−6` | `−2.8957678641e−6` |

Nominal source-off difference at `.005`: `δX_cut≈−1.2354005001e−5` (exec) and `≈−3.607419864e−6` (sym). Postsource weak and hadronic dynamics continue, so the event target differs from the source-off state. Baseline conditional native `Xnuc_exec=0.40095951896185816`, `Xnuc_sym=0.4000849662408279`.

The independently established ROT021 adjoint kernel gives `dXnuc/deps = −0.0019807080337802957` for exec and `−0.0005791537701141928` for sym. At `.005` this predicts `−9.9035401689e−6` / `−2.8957688506e−6`, agreeing with **fresh** full nonlinear ODE differences to relative `3.32e−7` / `3.41e−7`. The nonzero kernel projection on the two-moment null direction is the precise reason the `L0,L1` data are *not sufficient* for the endpoint **within this model**. Contributions to `dX_exec/deps` from LOW/MID/HIGH windows are `+0.00915150`, `−0.01938831`, `+0.00825610`; their cancellation leaves `−0.00198071`, not zero. Thus `K_target` is not a combination of the two source moment weights on this chosen three-dimensional source family.

## 5. Finite sign reversal while retaining individual source moments

Compare against the **unchanged** conditional PAPER (`−1.3` common five-channel exponent) endpoint. At `rtol3e−8`, paper `Xnuc_exec=0.40094496781788425`, native public `Xnuc_exec=0.40095951896185816`:

| eps of moment-null redistribution | PAPER−PUBLIC_modified target |
|---:|---:|
| `0` | `−1.4551143974e−5` |
| `.005` | `−4.6476070936e−6` |
| `.012` | `+9.2173586763e−6` |

The continuous root in the prescribed source family exists at `eps≈0.00734643423` (`rtol3e−8`) and `eps≈0.00734641461` (`rtol3e−9`), a shift of roughly `1.96e−8` in `eps`. At root, the numerical target residual is around `10^−14–10^−13`, but the nonlinear solver has jitter on this scale; **do not claim a 10-digit-accurate physical critical amplitude**. Both signs outside the root bracket are separated by orders of magnitude more than the solver-tolerance changes. `B_sym` endpoint responds materially to the moment-null deformation; no assertion of sign flip in B_sym is made.

The PAPER and native PUBLIC reference already differ in their mean spectral slopes. The existence of a sign reversal for this *additional* moment-preserving deformation does **not** establish a physical model of emission below `1e9g`, a bound on Hawking-source uncertainty, or an observational constraint.

## 6. Independent stress tests and errors

- Tighter nominal `Radau rtol=3e−9` executed for both charge maps at eps `{0,.005,.012}`; unchanged sign and source endpoint response. Max change in **differences** between the `rtol3e−8` and `3e−9` tests is on the order of `1e−10` in X (no certified global error interval).
- Four additional host/map series (each 3 amplitudes `0,.005,.01`) executed at `chi_EM=0` and `1`, with comoving baryon preservation. `B_exec` response at `.005` ranges from `−9.9198e−6` to `−1.0048e−5`; `B_sym` from `−2.9140e−6` to `−2.9545e−6`. Thus moment sufficiency fails across all **executed** stress axes. This is not a complete physical uncertainty envelope.
- Both moment controls were also checked by direct `scipy.integrate.quad` piecewise quadrature over the common exact mass-clock. `M0,M1` errors below `1.5e−16` relative are an integration check, not a proof of source-native species physics.
- Source rates positive and pair sum equal by construction for every u, not only sampled points. Exact boundary equality of all derivatives holds because perturbations have compact support a finite distance away from u=1.
- Root bracketed and evaluated independently at two `rtol`; no fully source-native SciML accepted-step/global-error certificate exists.

## 7. Scope, host subtraction, and decision impact

**Supported:** for the specified conditional source-informed bridged kinetic replay, *pointwise pair sum plus comoving emitted number and first log-mass moment for each species* still do **not** identify the fixed-temperature neutron endpoint or its signed comparison to another counterfactual source law. A three-bin moment-null direction has a nonzero target derivative and a full nonlinear sign-changing witness. This extends the **particular physical-source instantiation** beyond ROT020 but lies in the mature theory of positive moment inverse problems, target-relative sufficiency and adjoint-weighted causality (NC/MT13/LT5); **NO novelty claim**.

**Not supported:** that original Hawking spectra can vary arbitrarily between bins, that pointwise pair number conservation preserves physical energy allocation (proton/neutron masses slightly differ), that the original 10D Julia ever produced this witness, that generic finite source moments are insufficient in every restricted parametric source family, that a modern BBN helium/D/H likelihood has been reconstructed, or that paper Figure5 / PBH bounds are correct or modified. Wu–Xu source table remains **unvalidated below `1e9g`**; source effects, hadron kinetics and two-temperature background remain interdependent. An `Xn` target is not a directly validated mass fraction `Yp`.

**Actionable owner decision (not a new task cascade):** record that source verification must preserve a mass-resolved **correlated** pbar/nbar production history, not only total pair yield, species fluence and one emission moment. In a legal full original 10D replay capture accepted-step mass/time and event, `Q_i(M)`, all source-active hadron populations, `X_cut`, `X(Tnuc)`, postsource weak/hadron collision integrals and a justified global numerical error budget. Until independent source validation and referee acceptance, do not promote the sign or physically interpret the PBH constraints.

`NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_SOURCE_VALID_E2B / NO_ORIGINAL_JULIA_10D / NO_MODERN_Yp_DH / NO_PBH_BOUND / BW_INGEST_UNVERIFIED`.

## 8. Reproducibility and handoff

Complete reproducibility package includes the two new executable scripts `reproduce_two_moment_kernel_023.py` and `verify_two_moment_sign_root_023.py`, actual four original 10D archived source cells inside SHA-checked S6 ZIPs, inherited mathematical/kinetic dependencies from ROT013, ROT020 and ROT021, ROT021 causal sensitivity kernel, output CSV/JSON for nominal, tight and alternative backgrounds, and the exact root-search log. `numpy`/`scipy` available in Python 3.13. Source-table Git blob pinned as above; full data trace source disclosed in inherited code. Run from extracted ZIP root:

```bash
python reproduce_two_moment_kernel_023.py --amps=-.005,0,.005 --chis=.5 --baryons=eta --rtol=3e-8 --out .
python reproduce_two_moment_kernel_023.py --amps=0,.005,.012 --chis=.5 --baryons=eta --rtol=3e-9 --out tight
python reproduce_two_moment_kernel_023.py --amps=0,.005,.01 --chis=0,1 --baryons=comoving --rtol=3e-8 --out thermal_robustness
python verify_two_moment_sign_root_023.py
```

Check original source copyright/licensing independently before further redistribution. Public GitHub storage of the model report is **not** BW ingestion or scientific owner/referee approval. SYSS5 public source guard fields supplied explicitly above; `sync_state` remains pending until an independent actual BW ING record exists.