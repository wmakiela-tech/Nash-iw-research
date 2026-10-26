artifact_id: MECH-S7-ROT024-HIGHER-LOG-MOMENT-TARGET-NONSUFFICIENCY-001_20261026
exposure: PUBLIC
claim_ceiling: EXECUTED_CONDITIONAL_FINITE_MOMENT_TARGET_INSUFFICIENCY_NOT_PHYSICAL
sync_state: GITHUB_PENDING_BW_INGEST
RETURN_ID: MECH-S7-FRONTB-SIX-SOURCE-MOMENT-TARGET-INSUFFICIENCY-GATE-024_20261026
CLASS: SOURCE_PINNED_REDUCED_10COMP_BRIDGE_PLUS_7D_FINITE_MOMENT_NULLSPACE_ADJOINT_FD

# Mech-S7 ROT024 — source moments 0–5 do not exactly determine a conditional neutron target, but increasingly constrain it

**Date:** 2026-10-26. **Cell:** `IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7`. **Owner:** Moderator / EXEC only.

**Source identity:** Wu–Xu pinned [`Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`](https://github.com/Fenyutanchan/Primordial-Black-Hole/tree/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618); author `hadrons_from_PBH.dat` Git blob `06d0883a27b108692720422294ba2baacd381a64`; original Julia `main-scan.jl` (not executed). Prior MECH-S7 ROT013 bridge repair; ROT020 pointwise pair-sum sign falsifier; ROT021 target adjoint; ROT022 postsource memory; ROT023 moment 0,1 non-sufficiency; MT13/NC/LT5 exact moment-host prior-art acknowledged. This work is a conditional **numerical specialization of the classical truncated moment problem**, not a novelty claim.

## Question / scope

Can first 3–6 *comoving logarithmic source moments* for each antinucleon species, combined with exact pair-sum at every mass, determine neutron fraction `X_n` at `T_nuc` in the existing source-inspired conditional transport model? **No, for this selected 7-bin family up to moment degree 5**, but residual sensitivity decreases substantially with stronger moment constraints. Crucially the result is NOT a statement about physically allowed Hawking spectral variations.

## Exact source/target construction

Let `u=M/(1e9 g)`, `z=ln u`; the supported variation lies in `7e7 g <= M <= 9.2e8 g`. Let `Q_p(u)` and `Q_n(u)` be the pinned code's separate first-cell log–log extrapolations from the **tabulated lower edge**. These rates are not validated below `1e9 g`. The common mass clock is `dt=-3*DT_EDGE*u^3 dz` (forward evaporation reverses `z`). Because the background is not changed by the controlled antinucleon split and the PBH number dilutes as `a^-3`, the *comoving particle fluence* has a common factor times `u^3 Q_i dz`. Its logarithmic moment of degree j is proportional to

`F_{i,j} = integral(u^3 Q_i(u) [ln u]^j d ln u)`, `j=0,...,k`.

Choose seven `b_i(z)=sin^4(pi (z-z_i)/(z_(i+1)-z_i))` on contiguous equal-log-width subintervals partitioning `u in [.07,.92]`, zero elsewhere. Each is C^3 after zero extension; the source equals pinned public spectrum identically outside these supports, including a neighborhood of table edge `u=1`. Let `f(z)=sum_i c_i b_i(z)`. Set

`Qp_new(u)=Qp_native(u)+epsilon*(Qp_native(u)+Qn_native(u))*f(ln u)`

`Qn_new(u)=Qn_native(u)-epsilon*(Qp_native(u)+Qn_native(u))*f(ln u)`.

Thus `Qp_new+Qn_new=Qp_native+Qn_native` **pointwise**; every *other* hadron emission channel is untouched; both changed channels remain positive for all tested amplitudes `|epsilon|<=.04`. Build the moment matrix with `A_(j,i)=integral u^3 (Qp+Qn)b_i(z) P_j(z) dz`, where `P_j(z)` is a linearly rescaled power `x(z)^j` (an invertible basis change in the polynomial space). For `k=2,3,4,5`, select `c` from `null(A_(0:k,:))`, maximizing its nonzero projection onto the archived ROT021 `B_exec` target sensitivity kernel, normalized so `max_i |c_i|=1`. **This is target-informed selection, not a blind held-out test.** The null direction preserves all moments j<=k for both species simultaneously. At k=5 the nullspace dimension is exactly 1.

The target derivative (linear adjoint response) uses

`d ln(Qp/Qn)/d epsilon = ((Qp+Qn)^2/(Qp*Qn))*f(z)`;

integrating the ROT021 mass kernel against this derivative predicts the final `X_n` response. We independently solve the **nonlinear** subedge 7D neutron+six-hadron ODE with original conditional 10-component preedge state bridge, two-temperature conditional thermal host (`chi_EM=.5`) and `eta_const`. It is NOT the source-native Wu–Xu Julia 10D solution.

## Executed results

A common amplitude `epsilon=±.04`; displayed numbers are `X_n(T_nuc, epsilon)-X_n(T_nuc, 0)`.

| Highest matched logarithmic moment `k` | Moments matched *per species* | `B_exec`, epsilon=−.04 | `B_sym`, epsilon=−.04 | `B_exec` linear-adjoint estimate |
|---:|---:|---:|---:|---:|
| 2 | 3 (`0..2`) | -3.04888030757e-05 | -1.21522506508e-05 | -3.04884154261e-05 |
| 3 | 4 (`0..3`) | -1.65108769762e-06 | -1.34324953738e-06 | -1.65093107035e-06 |
| 4 | 5 (`0..4`) | -4.53326466088e-07 | +7.17889834800e-08 | -4.53363841139e-07 |
| 5 | 6 (`0..5`) | -1.13020624803e-07 | -7.46815953523e-09 | -1.13028008588e-07 |

**Conditional sign kill (3 moments):** tight-solver paper reference `Xpaper=0.4009449678284942` vs native public `Xpublic=0.4009595189655935` gives baseline paper-minus-public `-1.45511370993e-05`. With k=2, epsilon=−.04, modified public `Xpublic_modified=0.4009290301625178` and paper-minus-modified `+1.59376659764e-05`: **sign reversal**, while source moment degrees 0,1,2 per species and pair-sum at every mass are invariant. This compares source-inspired `B_exec` models only; source-valid `Yp`/`D/H` and actual PBH limits remain UNKNOWN.

**Positive result about approximate sufficiency:** at fixed amplitude .04, the *maximal-direction-selected* `B_exec` response shrinks from ~3.05e-5 (k=2) through ~1.65e-6 (k=3), 4.53e-7 (k=4), to 1.13e-7 (k=5), a ~270-fold decline. `B_sym` shrinks from ~1.22e-5 to ~7.46e-9 (~1600-fold), with a sign change in the k=4 response. **Different target-optimized perturbation shapes are used at each k; this is a finite-family illustration, not a uniform stability theorem for all admissible spectra.**

## Numeric controls and uncertainty

1. **Source positivity/pointwise sum:** both new rates positive, exact pair-sum algebraically, checked on 2000 log-mass samples (Float64 relative residual at most ~4e-16); identical to native for `M>=9.2e8 g`, including all derivatives at `1e9 g`. Other four species untouched.
2. **Independent moment quadrature:** coefficients designed by 96-point Gauss–Legendre rule, checked independently by 256-point rule. Maximum `|moment residual|/sum_i |moment contribution_i|` over k=2..5, j<=k = **5.379e-16**; hence 0..5 source moments matched in the k=5 case to near double precision, not claimed exact as stored floats. The preservation holds analytically for exact nullspace coefficients.
3. **Nonlinear execution:** 24 ODE runs at rtol `3e-9`, both maps, four degree cases, both signs and zero controls; separate 12 ODE runs at rtol `3e-10` for k=4,5; max observed difference in their *differences* (`dX`) **9.5846e-13**. This is a tolerance comparison, not a rigorous global error bound.
4. **Adjoint vs ODE:** ROT021 kernel (itself finite-difference tested by mass shells) agrees with nonlinear response at order 1e-10 or better absolute for tested epsilon, with larger relative error where target derivatives are near zero. The global field/coupling is still conditional.
5. **Clean isolated replay:** copied 11 input files to a temporary empty working directory and reran k=5 `B_exec` with epsilon=−.04,0,+.04. Recomputed endpoint values agree with original exactly within Float64, max absolute error `0.0`. A complete 36-cell replay was **not** performed in that isolated run.
6. **Finite-class limitation:** 7 C³ windows and a target-optimized null direction; positivity checked only |epsilon|<=.04. Numerical target derivative nonzero at `k=5`; no claim of arbitrarily high k, no certified global minimax upper bound, and no constraint from physically correlated Hawking emission, thermal energy, or hadronic spectral covariance.

## Interpretation / cross-cell routing

This makes the ROT023 *two-source-moment non-sufficiency* more precise: even six moments per species do not exactly fix the conditional target, yet additional moments progressively damp the specifically optimized response in this family. The scientifically relevant object is the target-weighted moment beyond the constrained polynomial span (classic moment/functional analysis). Do not label any conditional k=5 residual as evidence of real particle emission uncertainty. Prior MT13/NC/LT source-moment and target-relative recovery is the **mature mathematical host**, and this is a concrete source-inspired diagnostic specialization.

**Next source-valid gates:** mass-resolved PBH antinucleon production below `1e9 g` with physically valid pbar/nbar ratio and correlated species yields; source-native full Julia 10D accepted-step/event/Q histories; admitted BBN observables and lawful helium target with uncertainty. Until then interpretation limited to bounded conditional source-to-target nonuniqueness.

## Reproduction

Run from the directory containing the packed dependencies and archived Wu–Xu trajectories (Python 3, NumPy, SciPy):

```bash
OPENBLAS_NUM_THREADS=1 python reproduce_high_order_moment_gate_024.py --maps exec,sym --degrees 2,3,4,5 --rtol 3e-9 --epsilon .04
OPENBLAS_NUM_THREADS=1 python independent_moment_checks_024.py
OPENBLAS_NUM_THREADS=1 python reproduce_high_order_moment_gate_024.py --maps exec,sym --degrees 4,5 --rtol 3e-10 --epsilon .04 --out tight
OPENBLAS_NUM_THREADS=1 python verify_clean_replay_024.py
```

The local archive contains original source-informed executable dependencies, source trajectory ZIPs, source kernel from ROT021, scripts, output tables, validation logs and SHA256 manifest. The public GitHub report is a complete methodological explanation; separate executable scripts and archived inputs are needed for exact replay.

**Claim/status guard:** `NO_ORIGINAL_JULIA_10D / NO_ADMITTED_SUBEDGE_HADRON_EMISSION / NO_PHYSICAL_HELIUM_DH_OR_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC / BW_PENDING`.