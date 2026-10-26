artifact_id: MECH-S7-FRONTB-JOINT-TARGET-HELDOUT-THERMAL-TRANSFER-026_20261026
exposure: PUBLIC
claim_ceiling: EXECUTED_CONDITIONAL_10COMP_BRIDGE_PLUS_7D_JOINT_LINEAR_TARGET_NULLSPACE_AND_HELDOUT_CHIEM_BREAK_NO_PHYSICAL_ADMISSION
sync_state: GITHUB_PENDING_BW_INGEST

# Mech-S7 ROT026 — Jointly target-matched source moments fail to transfer unchanged to a held-out thermal background

**Date:** 2026-10-26. **Owner:** `IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7`.
**PROBLEM_ID:** `P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001`.
**RETURN_ID:** `MECH-S7-FRONTB-JOINT-TARGET-HELDOUT-THERMAL-TRANSFER-026_20261026`.
**Status:** executed conditional calculation; NO original Julia 10D; no physical PBH/BBN/Yp/DH inference; no canon/novelty/EXEC; GitHub is not BW ingestion.

## 1. Motivation, sources and prior-art subtraction

ROT013 corrected a wrongly transplanted edge initial state with the nine-source-tabulated-row preedge 10-component ODE; ROT020 established exact pointwise antinucleon pair-sum-preserving conditional sign sensitivity; ROT021 established the mass-dependent **target adjoint** for final neutron abundance; ROT022 localized most of the response to source-active neutron-state history; ROT023/024 exhibited two- and six-moment **nonidentification**; ROT025 established **cross-map nontransfer** of one target-matched source moment. Here we run a stricter **joint** (both maps) kernel-null construction at nominal EM Hawking deposition, then test an independent thermal allocation. No generic mathematical theorem novelty is claimed: linear nullspaces, target-specific statistical sufficiency, moment recovery and model-dependent transfer are mature mathematical host theory (MT13/NC/LT and general inverse problems).

Source Wu–Xu public pinned commit `d395183674cace6c9906a8911bdeb7234ba4040d`, table `arXiv-2509.05618/data/out/hadrons_from_PBH.dat`, source interpolation `tool_script-hadrons_from_PBH.jl`, original dynamical code `main-scan.jl`. Hadron rates are **tabulated only at M >= 10^9 g**. The entire perturbation at `7e7..9.2e8 g` lives **outside** the source-valid table and is deliberately nonphysical until source validation. Raw source four-way 2x2 archives and the previously validated conditional preedge/7D code are preserved in the bundle.

## 2. Exact controlled object and training/held-out separation

Let `u = M/(10^9g)`, `z=ln u`. At seven disjoint logarithmic mass bins `(u_i,u_{i+1})` spanning `u=.07..0.92`, take positive compact bump functions `b_i(z) = sin^4(pi (z-ln u_i)/(ln u_{i+1}-ln u_i))`, zero outside each bin, and `h(z)=sum_i c_i b_i(z)`.

Modify **only** the two source channels `Qpbar' = Qpbar + ε (Qpbar+Qnbar) h(z)`, `Qnbar' = Qnbar − ε (Qpbar+Qnbar) h(z)`. Hence pair sum is conserved **pointwise**, other four hadron channels unchanged, and source support excludes the Wu–Xu table edge; all edge derivatives through at least third order unchanged. Check positivity at `ε=±.15`.

Choose `c` from the seven-dimensional nullspace of FIVE nominal constraints:

- comoving species source fluence log-mass moments `L_j = ∫ u^3 (Qpbar+Qnbar) h(z) z^j dz = 0`, `j=0,1,2` (thus both individual species have identical 0,1,2 moments before/after);
- **both** independent nominal ROT021 response gradients `G_exec · c = 0` and `G_sym · c = 0` at `chi_EM=.5`, `eta_B` constant.

There are two remaining source-shape degrees of freedom. Select one deterministic vector by orthogonal projection of the independently specified smooth test vector `G_exec * sqrt(u_bin_low * u_bin_high)` into this nullspace; no held-out outcome was used in selecting it. Then normalize `max|c_i| = 1`.

Coefficient vector:
```
[+0.8257014742156576,
 -0.6912705334208665,
 -0.6350615599007463,
 +1.0000000000000000,
 -0.4619538457988034,
 +0.09076972514896188,
 -0.006504906397405212]
```

The normalized FIVE-constraint matrix is ill-conditioned, with 2-norm condition number approximately **8626**. This is an important stability/physical-inference caveat: errors in ROT021 gradients or source transport may perturb the apparent null directions. The nominal response cancellation is conditional upon those gradients.

All conditional simulations use the same Wu–Xu archived state plus ROT013 corrected source-active 10-component bridge, then active-source 7D plus postsource neutron/hadron kinetics. The two-temperature micro-EOS host allocates an arbitrary fraction `chi_EM` of PBH power into the EM bath; the complementary fraction enters an effective thermalized neutrino bath. This is a **stress parameter**, not a physically derived energy-partition prediction. Baryon prescription `eta_const` is held fixed.

**Training background:** `chi_EM=.5`, both `B_exec`,`B_sym` target adjoints used for the five linear constraints. **Held-out background:** `chi_EM=0`, *no recalibration of vector c*, same both maps; chi is changed consistently in both 10-component preedge bridge and 7D thermodynamic host. Attempted `chi_EM=1` full runs did **not** finish within execution limits and are **NOT counted**.

## 3. Executed full nonlinear ODE results

Conditional neutron endpoint `Xn(T_nuc)` differences against ε=0 within each corresponding chi/map. Native Julia 10D is **NOT executed**.

| chi_EM | map | epsilon=+0.15 ΔXn | epsilon=−0.15 ΔXn | centered ∂Xn/∂ε approx |
|---:|:---:|---:|---:|---:|
| .5 | B_exec | -3.39467454146813e-10 | -1.28651145292480e-10 | -7.02721029514445e-10 |
| .5 | B_sym  | -1.46259615529942e-10 | +1.05583319864877e-11 | -5.22726491721433e-10 |
| 0 | B_exec | -1.21268246555672e-8 | +1.16534831784421e-8 | -7.92676927800310e-8 |
| 0 | B_sym | -3.00496760807789e-9 | +2.86757173562080e-9 | -1.95751311456623e-8 |

**Local odd-response amplification at chi=0 versus training chi=.5:** `112.801x` exec and `37.448x` sym. The symmetric finite difference here at ε=.15 is an empirical local slope diagnostic (not a mathematically certified derivative). The nominal near-zero odd response confirms first-order target matching to numerical accuracy; nonzero even part confirms nonlinear remainder.

Even quadratic-response coefficients from `[(ΔX(+ε)+ΔX(−ε))/(2ε²)]`:

| map | chi=.5 | chi=0 |
|---|---:|---:|
| B_exec | -1.04026355431e-8 | -1.05186994917e-8 |
| B_sym | -3.01558407874e-9 | -3.05324161016e-9 |

The **quadratic remainder barely changes**, whereas the odd/first-order response becomes visible in the held-out host. This explicitly discriminates background-kernel transfer failure from simple quadratic growth.

**Important additional distinction:** at chi=.5, ε=.15, the source cut neutron state changes by `+1.64126772117523e−7` (exec) and `+8.20023683401061e−8` (sym), despite the much smaller final-state response. Matching one final target (even jointly across maps) is **not** sufficient to reconstruct the intermediary state/history.

## 4. Independent controls and numerical precision

The FIVE normalized training constraints have a max numerical residual `9.02e-17`. An independent 320-node Gauss–Legendre calculation, separate from 96-node coefficient formation and prior 256-node validation, gives relative signed-vs-total contribution residuals `4.46e-17`, `3.10e-16`, `4.27e-16` for moments j=0,1,2. Independent sample of 4000 logarithmic u points gives max pair-sum relative residual `2.2191e−16`, with minimum individual source fraction `0.3487746 > 0` for ε=+.15. For ε=−.15 positivity follows the same worst-case amplitude bound and is also checked by every integration's source positivity guard.

Tighter held-out `Radau` integrals `rtol=3e−10` for both maps and ε=±.15 (four additional independent 7D trajectories) reproduce the finite-difference slopes within `8.36e−13` (exec) and `3.01e−12` (sym), compared with the `rtol=3e−9` primary solves. These are **empirical precision stress results**, not mathematical global bounds. Their raw absolute endpoint differences versus non-tight solves include solver effects common to +/−ε, so the *centered* difference is the appropriate transfer diagnostic.

All executed ODE data and exact source constraints are in `nominal_026.csv`, `heldout_026.csv`, `heldout_negative_026.json`, `tight_heldout_026.json`, `static_controls_026.json`; scripts and original 2x2 archives are included. Source and intermediate raw ZIP snapshots are included, with per-entry SHA256 manifest and ZIP integrity test.

`chi_EM=1`: attempted twice (nominal/tighter settings) but **timed out before any confirmed state**; no value or PASS claimed, no numerical inference. For performance, a future Julia/native or optimized EOS evaluation could extend the grid, but no task is assigned to another cell without owner request.

## 5. Source status and decision

This is a **conditional source-to-target stress experiment**, not an exact new theorem or an original Wu–Xu simulation. A source moment calibrated to BOTH nominal reaction maps is locally predictive at that one nominal host but is **not transportable without correction to another thermal background**, even when species total yields and moments 0..2 are unchanged. The main observable mismatch stems from transfer of the **linear target sensitivity**, not from a suddenly growing quadratic effect. This supports NC/MT target-relative sufficiency and denies background-independent use without covariant/typed transport.

Priority is therefore an evidence-based **cross-background target-kernel validation** followed by the still-required original source-native accepted-step Julia 10D, observed hadron source spectra below 1e9g, precise event handling, and physical observable admission. These remain OPEN. Do not claim Yp, D/H, constraint curves, Hawking spectra validity, novelty or EXEC. Do not infer BW ingestion from GitHub publication.

**Status flags:** `EXECUTED_CONDITIONAL_JOINT_TARGET_NULLSPACE`; `HELDOUT_CHI0_TRANSFER_FAIL`; `CHI1_TIMEOUT`; `ORIGINAL_JULIA_10D_NOT_EXECUTED`; `SOURCE_VALID_E2B_OPEN`; `NO_CANON`; `NO_EXEC_SIGN`; `NO_NOVELTY`; `NO_PHYSICAL_Yp_DH`; `NO_PBH_BOUND`; `BW_PENDING`.