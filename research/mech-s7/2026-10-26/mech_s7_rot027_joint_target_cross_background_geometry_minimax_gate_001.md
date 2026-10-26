artifact_id: MECH-S7-FRONTB-JOINT-TARGET-CROSS-BACKGROUND-GEOMETRY-AND-MINIMAX-GATE-027_20261026
exposure: PUBLIC
claim_ceiling: EXECUTED_CONDITIONAL_JOINT_TARGET_CROSS_BACKGROUND_TWO_POINT_INFORMATION_LOWER_BOUND_NO_PHYSICAL_ADMISSION
sync_state: GITHUB_PENDING_BW_INGEST

# Mech-S7 ROT027 — Two-target nominal moment compression fails at **intermediate** thermodynamic backgrounds; geometry, finite-amplitude control and two-point minimax witness

**2026-10-26 | Lineage:** `IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7`  
**PROBLEM_ID:** `P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001`  
**RETURN_ID:** `MECH-S7-FRONTB-JOINT-TARGET-CROSS-BACKGROUND-GEOMETRY-AND-MINIMAX-GATE-027_20261026`  
**Scientific status:** executed conditional source-transport kinetic test; not the author's Julia 10D. BW ingestion pending, no scientific approval/EXEC, no physical inference, no novelty claim.

## 1. Prior-art subtraction and exact source scope

Prior Mech ROT013 recovered a missing nine-tabulated-row source-active preedge 10-component bridge; ROT020 established source-shape-driven conditional sign reversal with pointwise antinucleon pair-sum conserved; ROT021 computed a mass-dependent target adjoint; ROT022 decomposed postsource neutron memory; ROT023/024 showed ordinary source moments insufficient for the endpoint; ROT025 showed one-map target-calibrated moment did not transfer to another map; ROT026 constructed a **joint** nullspace for both nominal maps at `chi_EM=0.5` and established failure for extreme `chi_EM=0`. ROT026 recorded a poorly conditioned constraint matrix (~8626), and `chi_EM=1` timed out.

**Incremental ROT027:** independently execute both maps for intermediate held-out `chi_EM=0.25` **and** `chi_EM=0.75` (not used in construction), with both signs of epsilon and the unchanged coefficients; additionally execute half-amplitude controls and independently tighter Radau controls; compute geometric dependence and a sharp *binary-witness*, not physical/global, error lower bound for any estimator restricted to the same nominal compression. These are **source-to-target numerical falsifiers**, not a new general theorem. Linear algebra, moment nullspaces, minimax two-point arguments, and target-relative sufficiency are classical and were already recognized in MT/NC/LT work.

Upstream reference: Wu–Xu public code repository [Fenyutanchan/Primordial-Black-Hole](https://github.com/Fenyutanchan/Primordial-Black-Hole/tree/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618) at commit `d395183674cace6c9906a8911bdeb7234ba4040d`, original `main-scan.jl`, source interpolation `tool_script-hadrons_from_PBH.jl`, table `data/out/hadrons_from_PBH.dat`. **No source-valid charged hadron / antinucleon emission rates below `M=10^9g`** are established by this published table. The artificially constructed source variations live wholly below that boundary and are not interpreted as physical Hawking spectra.

## 2. Preserved source data and training information

Dimensionless mass `u=M/(10^9 g)`, log coordinate `z=ln(u)`. Seven disjoint intervals in `u∈[.07,.92]`; smooth compact shape `h(z)=Σ_i c_i sin^4(π(z−z_i)/(z_{i+1}−z_i))` on each interval and zero elsewhere.

At each mass vary only

`Q_pbar^(epsilon) = Q_pbar + epsilon (Q_pbar+Q_nbar) h(z)`;
`Q_nbar^(epsilon) = Q_nbar − epsilon (Q_pbar+Q_nbar) h(z)`.

Therefore `Q_pbar + Q_nbar` remains exactly the same function of mass; other hadronic sources do not change. Both antinucleon species preserve comoving fluence moments `j=0,1,2` weighted by `u^3 (ln u)^j`; both retain all near-table-edge derivatives. The two additional *nominal* statistics are ROT021 final-`X_n` linear response functionals for `B_exec` and `B_sym` at `chi_EM=.5`. These are **linearized observables**, not the full nonlinear endpoints. The vector `c` was fixed in ROT026 **before** any ROT027 held-out integrations; it is not refit here:

```
[+0.8257014742156576,
 -0.6912705334208665,
 -0.6350615599007463,
 +1.0000000000000000,
 -0.4619538457988034,
 +0.09076972514896188,
 -0.006504906397405212]
```

The moment constraints and both nominal linearized targets remain identical for `epsilon=−0.15` and `+0.15`; the pointwise pair sum remains identical as a **function**, a stronger invariant than one scalar moment.

All executed kinetic runs use the existing ROT013 source-active bridge and a **conditional** 7D active/postsource evolution with idealized micro-EOS and constant baryon-to-photon prescription `eta_const`. Hawking deposited EM-energy share `chi_EM` changes consistently in the bridge and thermal host, but this share is an artificial sensitivity parameter; it does not follow from a validated microscopic spectrum. The original author's source-native 10D Julia solver **has not been run**.

## 3. Exact nominal geometry (not independent observations)

Form the 5×7 matrix `A` of row-normalized constraints: three comoving log-mass moments plus two nominal target adjoint rows. Singular values:

```
2.19558555, 0.41778655, 0.06962138, 0.00335739, 0.000254523367
```

Full 2-norm condition number `κ₂(A)=8626.263211`. In the four-dimensional subspace orthogonal to the three source moments, the two target gradient rows have cosine **0.9967678426734934** and principal angle **4.6078774622°** (projected 2×4 row matrix condition ≈36.1). Thus the two nominal target constraints are almost collinear after moment subtraction. Nominal joint matching should **not** be described as two robust, orthogonal measurements. This geometry does not by itself set an uncertainty in physical emission or ODE correctness.

The 320-node independent Gaussian quadrature gives maximum normalized moment residual `5.3632e−16`; five nominal row constraints `max |A·c| = 9.0206e−17`. Independent 4000-point source controls at epsilon ±.15 give max pair-sum relative residual `2.2196e−16`, minimum individual antinucleon fraction of the pair `0.348776 > 0`, and unchanged source outside compact support.

## 4. NEW: nonlinear held-out kinetic experiment at intermediate backgrounds

Same source perturbations `epsilon=±0.15` and **same unmodified c**. The tabulated gradients are centered `(Xnuc(+.15)−Xnuc(−.15))/.30` in `X_n` per unit epsilon. The original extreme and nominal data from ROT026 are retained solely as anchors.

| `chi_EM` | map | centered response slope (epsilon±.15) | half-gap lower bound for any same-summary prediction |
|---:|:---:|---:|---:|
| 0.00 (prior ROT026) | `B_exec` | `−7.9267692780e−8` | `1.1890153917e−8` |
| 0.00 (prior ROT026) | `B_sym` | `−1.9575131146e−8` | `2.9362696718e−9` |
| **0.25 (NEW)** | `B_exec` | **`−3.9509390019e−8`** | **`5.9264085028e−9`** |
| **0.25 (NEW)** | `B_sym` | **`−9.9301757558e−9`** | **`1.4895263634e−9`** |
| 0.50 (training, prior ROT026) | `B_exec` | `−7.0272102951e−10` | `1.0540815443e−10` |
| 0.50 (training, prior ROT026) | `B_sym` | `−5.2272649172e−10` | `7.8408973758e−11` |
| **0.75 (NEW)** | `B_exec` | **`+3.7172134630e−8`** | **`5.5758201944e−9`** |
| **0.75 (NEW)** | `B_sym` | **`+8.6444222151e−9`** | **`1.2966633323e−9`** |

At `chi=.25` the magnitude of the empirical centered slope is about **56×** larger than the training `B_exec` slope and **19×** larger than the training `B_sym` slope. Signs reverse at `chi=.75`. The training centered slope is small but not mathematically zero because the full ODE response includes higher odd orders and numerical error, whereas nominal **adjoint** first derivatives were constrained to zero.

The approximately antisymmetric first-order loss around chi=.5 is consistent with host-dependence of the target kernel. It is **not** a claim of an exact affine dependence over the full chi range or of background covariance.

**Actual intermediate ODE endpoints (for audit):**

| `chi_EM` | map | baseline `X_nuc` | `ΔX_nuc(+.15)` | `ΔX_nuc(−.15)` |
|---:|:---:|---:|---:|---:|
| .25 | exec | 0.40127293210690995 | −6.1613154578e−9 | +5.6915015478e−9 |
| .25 | sym | 0.4003986713704224 | −1.5575775669e−9 | +1.4214751598e−9 |
| .75 | exec | 0.40064708999329063 | +5.3449925042e−9 | −5.8066478847e−9 |
| .75 | sym | 0.3997722478875832 | +1.2295985896e−9 | −1.3637280749e−9 |

## 5. NEW: sharp two-source information lower bound, limited to this experiment

For a chosen background and map, **both** source alternatives `ε=±0.15` have the *same* 3 species moments, 2 nominal target-linear moments, and entire pointwise antinucleon pair-sum function. An estimator receiving **only this unchanged summary** must return the same predicted scalar `\hat X` for both. For any two endpoint values `X_+`, `X_-`, elementary triangle inequality yields:

`max(|\hat X−X_+|, |\hat X−X_-|) >= |X_+−X_-|/2`.

The bound is attained for the binary source pair by predicting the midpoint. For the held-out chi=.25 and chi=.75, the measured lower bounds are given in the table above. In particular at chi=.25 they are `5.9264085e−9` (`B_exec`) and `1.4895264e−9` (`B_sym`). **Only a binary-witness minimax bound:** does not constrain an algorithm supplied with the full source spectrum, cannot be extended to a global uncertainty class without additional assumptions, and does not give a physical BBN/`Y_p` error bar.

## 6. Stress tests, source checks, replay

- **Higher solver precision:** four held-out cases each at epsilon ±.15, chi=.25 and chi=.75, two maps; rerun with `Radau rtol=3e−10` vs primary `3e−9`. Max absolute centered slope difference `2.65621e−12`, smaller than the measured slopes. Empirical tolerance comparison only, no certified global bound.
- **Halved perturbation:** additionally execute chi=.25 and .75 with epsilon ±.075 and same baselines. Centered slope changes relative to the ε±.075 value by **0.2951% exec / 0.0753% sym** at chi=.25 and **0.3217% exec / 0.0968% sym** at chi=.75. Thus nonzero transferred response is consistent with a first-order kernel change; only finite-amplitude numerical evidence, not an analytic differentiability proof.
- **Clean independent replay:** rerun all **12 primary states** (chi=.25/.75 × two maps × epsilon `0,+.15,−.15`) from the same original source bundles: numerical fields `chi`, `ε`, `X_nuc`, `X_cut`, `ΔX_nuc`, `ΔX_cut` agree **exactly at displayed float precision**, maximum absolute difference 0.0. Runtime/formatting excluded.
- **Moment/source checks:** independent 320-node quadrature and 4000-point positivity, unchanged edge and pair-sum PASS.

Scripts to reproduce are in the archive; existing `reproduce_joint_target_heldout_026.py` is the full ODE executable driver (reused unmodified), while `reproduce_heldout_geometry_minimax_027.py`, `independent_source_checks_027.py`, `analyze_amplitude_transfer_027.py` recompute controls and bounds; all raw CSVs and JSONs are included with a hash manifest. Conditions `.25` and `.75` are independently executed new science data; `.0` and `.5` are explicitly inherited ROT026 results.

## 7. Scientific decision and STOP guards

**DECISION:** Reopen any suggestion that 3 moments plus nominal `B_exec/B_sym` target calibration suffice *across backgrounds*. Nominal map agreement at chi=.5 provides almost redundant geometry after moment subtraction; the same compressed source yields distinct target values at intermediate held-out hosts, even when positivity, pair-sum, and source moments are retained. If future use requires cross-host prediction, the source summary must include admissible **host-family sensitivity information** or explicit error bounds under a specified host/source uncertainty class. Do not elevate a two-source lower bound to an absolute physical error estimate.

`EXECUTED_CONDITIONAL_INTERMEDIATE_CHI025_CHI075 = PASS`; `AMPLITUDE_HALVING = PASS`; `SOLVER_TIGHTENING = PASS`; `12_STATE_CLEAN_REPLAY = PASS`; `UNMODIFIED_PAIR_SUM_SOURCE_AND_MOMENTS = PASS`; `TWO_POINT_MINIMAX_WITHIN_TESTED_FAMILY = EXACT`; `NOMINAL_TWO_KERNELS_NEAR_COLLINEAR = VERIFIED`; `NATIVE_JULIA_10D = NOT_EXECUTED`; `LOW_M_HADRON_EMISSION = SOURCE_INVALID_UNDER_CURRENT_TABLE`; `Y_P_D_H_PBH_BOUNDS = NOT_ADMITTED`; `NOVELTY = NOT_CLAIMED`; `CANON = NO`; `EXEC_SIGN = NO`; `BW_INGEST = PENDING`.

No further action assigned to another cell. Moderator authority remains final. GitHub public report is not BW ingestion, owner approval, referee PASS, or EXEC.