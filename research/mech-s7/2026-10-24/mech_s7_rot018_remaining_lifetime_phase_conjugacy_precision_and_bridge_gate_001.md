# MECH-S7 ROT018 — exact remaining-lifetime phase coordinate, high-precision cutoff representation and independent conditional bridge equivalence

**Date:** 2026-10-24  
**CELL:** `IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7`  
**RETURN_ID:** `MECH-S7-FRONTB-REMAINING-LIFETIME-PHASE-COORDINATE-AND-REPRESENTATION-GATE-018_20261024`  
**PROBLEM:** `P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001`  
**RESULT CLASS:** EXECUTED_ANALYTIC_COORDINATE_CONJUGACY / EXECUTED_FINITE_PRECISION_NEGATIVE_CONTROL / EXECUTED_10_COMPONENT_CONDITIONAL_PREEDGE_EQUIVALENCE / NOT_NATIVE_JULIA_10D.  
**Source type:** original primary Wu–Xu Julia at pinned commit for model structure; earlier ROT013 conditional independent SciPy system for the bridge; ROT017 source precision argument. Not a new physical law, not a PBH bound.

## 1. Why this question and others first

ROT004/015 derived and audited the exact constant-`N_BH` mass cube; ROT016 demonstrated archive-output event undersampling and inability to infer accepted-step error from dense-output samples; ROT017 corrected a native monitor that had prematurely cast time and mass to Float64. DAX-S7 and PRF11's independent thermal/EOS audits, Rec10's surviving-hadron rule and MT13/LT5's event-target reasoning remain separate credits. **ROT018 changes the event coordinate itself as an independent computational control.** It neither claims priority over standard event-adapted coordinates nor claims to have executed source Julia.

Pinned source: `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`, `arXiv-2509.05618/main-scan.jl` and `tool_script-parameters.jl`. Verified by GitHub source `evolution_system!` coordinates `η=ln a`, `u[1]=ln t`, `u[3]=ln M`, code `d_m_PBH_dt = -N_PBH * NU.m_Pl^4 / m_PBH^2`, and evaporated flag `log_m_PBH_in_EU ≤ log_m_PBH_evaporated_in_EU`. The source code enforces the right-hand-side switch, not a documented explicit `ContinuousCallback`. Initial mass in source Actions branch is 6e9 g; cutoff set by `ln M_cut = ln M_initial−20`. The numerical coefficient `Γ=4.207579833788249e27 g³/s` here is the *display precision value* verified in ROT004 and ROT017, **not an exact native ArbFloat source Γ**. Results about perfect 100-bit conservation still require the source-native coefficient.

## 2. Exact phase conjugacy

On the **verified constant-`N_BH` plateau, before source-off only**:

\[
\frac{dM}{dt}=-\frac{\Gamma}{3M^2},\qquad\tau(M)=\frac{M^3}{\Gamma},\qquad\frac{d\tau}{dt}=-1.
\]

Use the positive normalized remaining-life coordinate

\[
z=\ln\!\frac{\tau(M)}{\tau_{\rm cut}}=3\ln\frac{M}{M_{\rm cut}},\qquad
M(z)=M_{\rm cut}e^{z/3},\quad \frac{dt}{dz}=-\tau_{\rm cut}e^z.
\]

The source-supported cutoff is `z=0`; source start is exactly `z=60`, without an arbitrarily precise subtraction of 51.3359 s and 51.3359 s. On the subtable source interval `M=10^9 g → M_cut`, `z=54.6247215923 → 0`. For any nonmass subsystem `\dot y=F(y,t,M,T,...)`, its phase reparameterization is `dy/dz=−τ_cut exp(z) F`. The full ODE can be integrated **in source-on phase only**, with the end state transferred to a separate postsource time evolution. The original 10D `ln t` variable need not be estimated from a double-precision difference; if absolute time is required for output, retain high precision or an offset/split-clock representation.

This is a coordinate conjugacy of an assumed autonomous pre-off mass law, not a proof that original SciML integration, events or hydrodynamic EOS actually preserve the invariant at requested tolerances. It does not apply unchanged to mass-dependent `N_BH(M)`, nor to postsource frozen M.

## 3. Direct numerical representation control

`reproduce_remaining_lifetime_clock_018.py`: mpmath 90 decimal digits, binary significand precision ladder, diagnostic checkpoints from 6e9g to cutoff. `M_cut = 12.3669217346313469678 g`, `τ_cut=4.49523573992306442695e−25 s`, `τ_initial=51.335924...s`. Float64 absolute time ULP at 51 seconds `7.105427357601002e−15 s`. The mass whose remaining lifetime equals one ULP is 31,036.603609986 g. The Float64 representations of `t_zero` and `t_cut` coincide, even though the exact events differ by `τ_cut`.

| Binary significand bits | Recover τ_cut by subtracting rounded absolute times | Relative remaining-life error |
|---:|:---:|---:|
| 53 | NO | 100% |
| 64 | NO | 100% |
| 80 | NO | 100% |
| 87 | YES | 7.9936% |
| 90 | YES | 3.5072% |
| 94 | YES | 0.08684% |
| 100 | YES | **0.0030134%** |
| 113 | YES | 4.61685×10⁻¹⁰ |

**New correction to ROT017:** source-declared 100-bit inputs offer approximately 8,904 representational ULPs over `τ_cut`; the subtraction of absolute times can still lose ~3×10⁻⁵ *relative lifetime information* in a particular rounded simulation. “Cutoff distinguishable” is categorically weaker than “cutoff clock accurately recovered”. This is *not* a measured defect in the original Wu–Xu Julia solver; that solver explicitly evolves `ln t`, `ln M` and high-precision input types and could preserve phase information otherwise.

The normalized phase coordinate carries `z=0` exactly at the cutoff, without subtracting those times. Algebraically and with 90-digit mpmath we verified `dM/dz ÷ (dt/dz) = −Γ/(3M²)` at ten mass checkpoints to relative error below 1e−85. Float64 evaluates `M(z)` and `τ(z)` over the tested positive range and represents cutoff without the time-difference alias; ODE tolerance still must be established.

## 4. Independent 10-component conditional transport equivalence

**Actually executed** an independent numerical change-of-variable on the earlier `ROT013` **reduced** ten-component source-supported bridge `M≈1.8366e9g → 1e9g`, state `(T_gamma, ln a, ln rho_nu, X_n, six hadron populations)`; this is NOT original Wu–Xu 10D Julia (which integrates `ln t,ln rho_SM,ln M,ln X, six ln n`). Physics assumptions copied unchanged from ROT013: original 9 rows of source hadron table, common interpolated source `Q(M)`, conditional source energy split χ_EM=.5, source-inherited initial X/hadrons, original `B_exec` and `B_sym` maps. Both `Radau`, `rtol=3e−9`; a numerical step bound is set in both parameterizations.

Variant A integrates `dy/du` with `u=M/M_last`; B integrates identical equations `dy/dz=(u/3)dy/du`, with `z=3ln u` (this z differs from normalized z above only by a constant, so is the same remaining-life clock). The full state was independently solved twice for each map.

| Map | X_edge, original mass variable | X_edge, log remaining-life variable | Absolute X difference |
|---|---:|---:|---:|
| B_exec | 0.498443725372788 | 0.498443725287173 | 8.5615×10⁻¹¹ |
| B_sym | 0.497135264087447 | 0.497135264108543 | 2.1096×10⁻¹¹ |

Across **22 endpoint component comparisons** (11 per map including T, ln a, rho_nu, X and six populations), maximum relative difference `1.7176421063×10⁻¹⁰`. Original mass-coordinate solve: 122/124 points; phase solve: 258/264 points, two *independent* adaptive discretizations. The test establishes coordinate equivalence at the specified tolerances within the conditional bridge; it is neither an independent physics validation nor a global-error theorem.

The bridge is supported by the original hadron *table above 1e9g* but initial conditions remain from saved archive trajectories. Below 1e9g the law is extrapolated and source-valid E2b remains blocked. NO original source-typed 10D accepted steps were collected.

## 5. Independent source-only fluence invariance control

Under *counterfactual* `Q(M)∝M^{-p}` and source plateau `dt=−3M²/Γ dM`, the fluence normalized to `Q(M_edge) τ(M_edge)` is

\[
\mathcal F_p=\frac{3}{3-p}\left[1-\left(\frac{M_{cut}}{M_{edge}}\right)^{3-p}\right].
\]

Mass-coordinate quadrature and Gaussian 480-node log-remaining-time quadrature agree with this expression for `p=1.2,1.3,1.4,2.99`, with maximum absolute quadrature deviation `4.992e−13`. In particular `F_1.3≈1.76470588235`. This checks Jacobians and a source-only quantity; it is **not** a signed X_n response guarantee because anti-baryon contribution cancellation, survival and moving temperature events remain active.

## 6. Implications, falsifiers and future original 10D acceptance gate

1. **Approved as a conditional test design:** use `z=3 ln(M/M_cut)` during a source-active high-temperature plateau and stop at `z=0`, propagate all nonmass equations with `dt/dz=−τ_cut exp z`; add a separate postsource integrator with surviving hadrons. If `N_BH` is not constant, replace with the exact quadrature `τ(M)=∫_0^M m²/[N_BH(m)m_Pl⁴] dm`; no global linear lifetime claim without validation.
2. **Exact mass-coordinate local unit test:** mass reconstruction `M_cut exp(z/3)` and Jacobian, source fluence power-law analytical integral; test mass-edge continuity from high-temperature, tabulated source into subedge source law. Do not use this transform to assert that the unsupported subedge source is physical.
3. **Native original source comparison remains necessary:** original 10D accepted-step logs and dense samples, at source-native precision, tolerances, `destats`, `retcode`, event boundary and all six hadrons; compare with independent phase-coordinate 10D counterfactual using *the same physical EOS and emission table*. The 90-digit analytic test and reduced 10-component SciPy bridge are not that comparison.
4. **Precision/dynamics must remain typed separately:** exact phase resolves representational cancellation but cannot cure a low-order/interpolant error, wrong X reaction channels, inconsistent entropy or mismatched helium proxy. The signed source-law test from ROT007/012/013 stays fragile to ~1e−4 antinucleon exponent antisymmetry; source evidence below 1e9g is absent.

**SOURCE-CLAIM CEILING:** `EXECUTED_CLASSICAL_COORDINATE_IDENTITY_PLUS_CONDITIONAL_NUMERIC_CONTROL`. `NO_ORIGINAL_JULIA_10D / NO_SOURCE_VALID_E2B / NO_BBN_Yp_DH / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY`. GitHub persistence and Slack notice are not equivalent to BW ingest, owner adoption or referee approval.

## 7. Reproducibility

Pure executable files in the associated ZIP: `reproduce_remaining_lifetime_clock_018.py`, `validate_conditional_bridge_coordinate_018.py`, `edge_bridge_013.py`, source modules from predecessor packages, two original raw source-run archive ZIPs, results `*.csv` and `*.json`, `MANIFEST_018.json`. Python 3; `numpy`, `scipy`, `mpmath`. Command: `python reproduce_remaining_lifetime_clock_018.py` and `python validate_conditional_bridge_coordinate_018.py` from the extracted folder. `validate_conditional_bridge_coordinate_018.py` uses full source-file-level RT013 wrapper imported locally and does not need the Github connector after the package has been acquired.