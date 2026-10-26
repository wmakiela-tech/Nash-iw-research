artifact_id: MECH-S7-ROT025-TARGET-WEIGHTED-SOURCE-MOMENT-CROSS-MAP-NONTRANSFER-001_20261026
exposure: PUBLIC
claim_ceiling: EXECUTED_CONDITIONAL_SOURCE_TARGET_LINEAR_NONTRANSFER_AND_NONLINEAR_FALSIFIER_NOT_PHYSICAL
sync_state: GITHUB_PENDING_BW_INGEST
RETURN_ID: MECH-S7-FRONTB-TARGET-WEIGHTED-MOMENT-NONTRANSFER-AND-SYM-SIGN-ROOT-025_20261026
CLASS: SOURCE_PINNED_REDUCED_10COMP_BRIDGE_PLUS_7D / EXACT_PAIR_SUM / TARGET_ADJOINT_NULL / CROSS_MAP_FD_AND_ODE / NEGATIVE_KNOWLEDGE

# Mech-S7 ROT025 — a target-calibrated source statistic for B_exec fails to transfer to B_sym

**Date:** 2026-10-26. **Lineage:** `IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7`. **Authority:** Moderator only may issue EXEC. **Problem:** `P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001`.

## Source and prior art / ownership subtraction

Upstream Wu–Xu author source: [`Fenyutanchan/Primordial-Black-Hole`](https://github.com/Fenyutanchan/Primordial-Black-Hole/tree/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618) at commit `d395183674cace6c9906a8911bdeb7234ba4040d`. Source hadron table `data/out/hadrons_from_PBH.dat`, blob `06d0883a27b108692720422294ba2baacd381a64`; 100 source rows starting at `M=1e9 g`, *no source-validated hadronic production below this mass*. Source code `main-scan.jl` Julia 10D is **not executed** in ROT025. Our transport is source-informed reduced 10-component *preedge bridge* (ROT013) + a conditional active/postsource 7D neutron/six-hadron ODE at `chi_EM=.5`, `eta_const`, Radau. The active subedge source laws remain *unvalidated extrapolations*. There is no physical BBN helium/D/H/PBH-bound claim.

**Internal and external mature host, not novelty:** NC and MT13 established source-moment nonidentifiability, target-relative predictive sufficiency and exact finite-moment nullspace witnesses; LT5/LT6 own theory integration. Previous Mech-S7 ROT020 fixed-pair-sum ODE sign witness, ROT021 executed backward-adjoint mass kernel, ROT022 postsource memory, ROT023 first two moments non-sufficiency, ROT024 first six moments non-sufficiency with useful approximate contraction. DAX-S7 and PRF lineages own primary physical/thermodynamic controls, Rec referee status remains separate. ROT025 is **a newly executed, map-specific kinetic specialization**: transfer of a source target statistic between the two author-inspired charge maps and identification of its nonlinear limit. No general theorem novelty.

## Exact experiment and what is preserved

Let `u=M/(1e9 g)`, `z=ln u`, and let `Qp`, `Qn` denote the public first-cell log-log-extrapolated author rates feeding antiproton and antineutron populations. Seven disjoint C³ compact bump functions `b_i(z)=sin^4(pi*(z-z_i)/(z_(i+1)-z_i)))` are supported within `7e7 <= M <= 9.2e8 g` (no changes near the table boundary). Write `f_k(z)=sum_i c_i b_i(z)`, with

```
Qp_new(u) = Qp(u) + epsilon*(Qp(u)+Qn(u))*f_k(log u)
Qn_new(u) = Qn(u) - epsilon*(Qp(u)+Qn(u))*f_k(log u).
```

Thus the pointwise pair sum, all other four hadron production channels, and the upper tabulated spectra are unchanged. For each `k=0` or `k=2`, choose coefficients `c` in the numerical nullspace of:

* `A_j c=0` for `j=0,...,k`, where `A_(j,i)=∫ u³(Qp+Qn)b_i (ln u)^j d ln u`. This preserves exactly (up to float construction/independent quadrature accuracy) the respective *comoving emitted-particle log-mass moments* for each antinucleon. The factors `u³` arise from the exact mass-clock integration; the common comoving PBH count cancels in the relative constraints.
* `G_exec c=0`, where `G_exec` comes from the **executed ROT021 adjoint target derivative for `X_n(T_nuc)`**, with the exact transformation `d ln(Qp/Qn)/d epsilon=(Qp+Qn)² f/(Qp Qn)`. This preserves a **single B_exec target-weighted source moment to first order**, not the entire B_exec nonlinear observable.

Select the nullspace vector proportional to the projection of the ROT021 `G_sym` row on the same nullspace and normalize `max|c_i|=1` (fix sign so `G_sym c>0`). **Both target gradients are known in the construction: NOT a blinded prediction.** At `k=0` the nullspace has dimension 5; at `k=2` it has dimension 3. The two target gradients across seven bins have cosine `~0.9971472`: closely aligned but **not proportional**.

For both maps, the same `f_k` and same `epsilon=±0.15` are applied; the underlying inherited preedge states remain map-specific, as in ROT013. The model uses fixed source-total EM deposition `chi=.5`, conserved sum by mass and `eta_B=const`, with source-selected baryon coupling as defined by the conditional host. These are not physical-source uncertainty parameters.

## Quantitative direct nonlinear kinetic outputs

At fixed `epsilon=+0.15`, the entries are `X_nuc(public_modified)-X_nuc(public_native)` after full reduced bridged/active/postsource ODE, not just a kernel prediction.

| Matched source statistics | `B_exec` actual dX_nuc | `B_sym` actual dX_nuc | `B_sym` first-order adjoint prediction |
|---|---:|---:|---:|
| k=0 (source count per species + `B_exec` target moment) | **−1.73695696715e−9** | **+1.77120836941e−5** | +1.77134276572e−5 |
| k=2 (three source moments per species + `B_exec` target moment) | **−3.08799208426e−10** | **+3.05440422804e−6** | +3.05457241718e−6 |

At the exact linear level `G_exec c` is `+3.52e−18` for k=0 and `+1.48e−18` for k=2, hence linear prediction for `B_exec` dX is effectively zero. The **measured nonzero `B_exec` remainders are nonlinear**, not evidence that exact nonlinear sufficiency follows from the target statistic. For the opposite perturbation `epsilon=−0.15` the B_exec residuals are `−9.34239269279e−9` (k=0) and `−2.12136647137e−9` (k=2). This asymmetry exposes the nonlinear and higher-order response.

The `B_sym` responses for `epsilon=−0.15` are `−1.77148353398e−5` (k=0) and `−3.05501255404e−6` (k=2). The target-specific summary is not portable to a different reaction map, even though the maps' sensitivity gradients have high cosine similarity.

### Direct B_sym source-law sign root

The paper comparison source is held fixed. In the same `B_sym`, `chi_EM=.5`, `eta_const` model at solver `rtol=3e−9`, we recomputed independently:

* `X_nuc,public(native) = 0.400084966167165`
* `X_nuc,paper(fixed) = 0.40009624878548594`
* baseline `paper−public = +1.12826183209513e−5`
* `epsilon=+0.15` k=0 gives `X_nuc,public_modified = 0.4001026782508591`, and `paper−public_modified = −6.42946537315892e−6`.

A Brent root of **the actual full ODE result**, not the adjoint, occurs at `epsilon_* ≈ +0.09554773342`. Root evaluation numerical residual was at the `~1e−13` level; this root is *not* a rigorously certified interval. An additional attempt to recompute the entire root at `rtol=3e−10` timed out, but the two **executed stricter-tolerance bracketing cells** showed `paper−public(+0.094)=+1.82754511024e−7` and `paper−public(+0.097)=−1.71479946187e−7`. The sign-crossing bracket is therefore independently reproduced at tighter ODE tolerance, while the exact tight root itself remains unexecuted.

**Interpretation guard:** `epsilon` is the fraction of the **pair sum** shifted between channels (times a bounded shape), not a tiny relative ratio adjustment; at |epsilon|=.15 a channel may be altered by ~30% of its native magnitude in selected bins. Neither the source family nor the size of these transfers is physically validated. The result is a target-dependent **conditional non-transfer** counterexample.

## Independent tests, numerical uncertainty and failed checks

1. **Exact source algebra**: `Qp_new+Qn_new=Qp+Qn` for every `M` and all epsilon by definition. Verified on 4001 logarithmic mass points, max relative Float64 pair-sum residual `<2.22e−16`. Both new rates positive; minimum observed species fraction of the pair sum `>0.3486`. Other species untouched; all original source-table values and every derivative at `M=1e9g` unchanged because support stops at `9.2e8g`.
2. **Independent 256-node Gauss–Legendre quadrature**, versus 96-node source coefficient construction, gave max relative source-moment residue `≤1.51e−16` over j<=k; `G_exec c` remained `≤3.52e−18` (dimensionless source-weighted derivative units). These are numerical tolerances, not symbolic algebra exactness for stored floats.
3. **Full nonlinear ODE**: 12 completed nominal full active/postsource solutions (2 maps × 2 degrees × −.15/0/+.15). The two map runs were separated because a combined process timed out mid-run; no partial combined run is counted as completed.
4. **Tight solver** (`Radau rtol=3e−10`, vs `3e−9`): 8 further completed solutions for epsilon=0,+.15, both maps and both degrees. Max absolute change in computed dX between tolerances `9.99e−13`. Particularly, `B_exec` k=2 residual `−3.09e−10` remains well above the observed change across tolerances. Not a proven global error enclosure.
5. **Independent B_sym source-law root**: direct paper/native baseline replay, 8 Brent evaluations at nominal tolerance; 2 tighter bracketing evaluations completed, **entire tighter root search TIMEOUT**, not PASS.
6. **Clean isolated replay**: two `B_sym` k=0 ODE states at epsilon=0,+.15 were executed in a new temporary directory with *source archived ZIPs and code only, not earlier results*. All endpoint numeric fields matched original exactly at Float64 precision. `2/2 PASS`, not a full all-cell clean replay.
7. **A priori design and other models**: data-driven coefficient selection uses both already known adjoints, precluding new prediction/novel physics claims. We did not rerun all `chi_EM` and baryon host variants here; only nominal `chi=.5,eta_const` is tested. No accepted-step Julia 10D, event-localization certification, validated subedge hadronic source, admitted helium definition, Yp/D/H, actual PBH bound, or BW ingest.

## Independent significance and routing

ROT024's six undirected moments were only approximately sufficient in the tested family; here a *single target-weighted functional* is deliberately sufficient **only to linear order** for one observable, yet is insufficient for an alternative map. The two maps are sufficiently close that casual approximate-transfer reasoning is tempting, but the aligned kernels differ in their null directions. The near-zero `B_exec` residual and `B_sym` sign kill are source-inspired numerical demonstrations of target-relative information, not discoveries about Hawking emission.

No shared universal source summary or estimator has been certified. Valid future gates: independently admitted PBH antinucleon spectra below `1e9g` (including covariance of the two channels and total power), native Wu–Xu 10D solver and event data, and lawful BBN observable target. Route to REC referee, MT14/NC/LT for target-information geometry, DAX/PRF for microphysics; **no new owner task cascade**.

## Reproduction

Run Python 3 (NumPy/SciPy), from extracted ZIP directory with two pinned source archives:

```bash
OPENBLAS_NUM_THREADS=1 python reproduce_target_transfer_025.py --maps exec --degrees 0,2 --amp .15 --rtol 3e-9 --outprefix exec
OPENBLAS_NUM_THREADS=1 python reproduce_target_transfer_025.py --maps sym --degrees 0 --amp .15 --rtol 3e-9 --outprefix sym_k0
OPENBLAS_NUM_THREADS=1 python reproduce_target_transfer_025.py --maps sym --degrees 2 --amp .15 --rtol 3e-9 --outprefix sym_k2
OPENBLAS_NUM_THREADS=1 python independent_controls_025.py
OPENBLAS_NUM_THREADS=1 python solve_sym_contrast_root_025.py
OPENBLAS_NUM_THREADS=1 python clean_replay_025.py
```

Tighter ODE checks are recorded as `tight_{exec,sym}_k{0,2}_target_transfer_025.csv` with `--epsilons 0,.15 --rtol 3e-10`. One tight full-root timeout is explicitly preserved in `run_tight_root_025.log`; it did not produce a false success artifact.

**Claim ceiling:** `CONDITIONAL_SOURCE_TO_TARGET_NONTRANSFER / NONLINEAR_REMAINDER / NOT ORIGINAL SOURCE VALIDATED`. **Status:** `GITHUB_PENDING_BW_INGEST`, no reviewer/owner/EXEC acceptance. `NO_ORIGINAL_JULIA_10D / NO_SOURCE_VALID_E2B / NO_PHYSICAL_Yp_DH / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.