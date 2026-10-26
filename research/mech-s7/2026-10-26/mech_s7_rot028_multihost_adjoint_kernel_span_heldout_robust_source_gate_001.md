artifact_id: MECH-S7-FRONTB-MULTIHOST-KERNEL-SPAN-HELDOUT-ROBUST-REDUCTION-GATE-028_20261026
exposure: PUBLIC
claim_ceiling: EXECUTED_CONDITIONAL_10COMP_PREEDGE_PLUS_7D_TARGET_ADJOINT_NUMERICAL_SPAN_AND_HELDOUT_ONLY
sync_state: GITHUB_PENDING_BW_INGEST
source_type: PINNED_EXTERNAL_WU_XU_PLUS_LOCAL_CONDITIONAL_RECONSTRUCTION
lineage: IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7
RETURN_ID: MECH-S7-FRONTB-MULTIHOST-KERNEL-SPAN-HELDOUT-ROBUST-REDUCTION-GATE-028_20261026
status: SCIENTIFIC_DIAGNOSTIC_NOT_OWNER_ADMITTED

# Mech-S7 — ROT028: multi-background source-to-target kernel span and nonlinear held-out robustness

## 0. Source, priority, negative knowledge, and original question

Source pinned to `Fenyutanchan/Primordial-Black-Hole` commit `d395183674cace6c9906a8911bdeb7234ba4040d`, `arXiv-2509.05618/main-scan.jl`, author's `hadrons_from_PBH.dat` first mass `M=1e9 g`. The **full author-native Julia 10D has never been executed or validated** in this lineage. Below 1e9g, hadronic rates are software extrapolations/controlled positive synthetic counterfactuals, not admitted physical Hawking spectra. Current test uses conditional ROT013 10-component source-active bridge to M=1e9g, conditional source-on/postsource 7D ODE, idealized micro-EOS and constant eta_B; chi_EM is a user-chosen deposition parameter, not microscopic physics.

Predecessor science: ROT020 sum-preserving pbar/nbar conditional sign counterexample, ROT021 target adjoint kernels independently FD-validated, ROT022 postsource state/reaction budget, ROT023–024 source-moment nonidentifiability, ROT025 cross-map transfer FAIL, ROT026 common nominal kernel null and chiEM=0 FAIL, ROT027 *new* chi=.25/.75 cross-host transfer FAIL and sharp binary-witness information bounds. Classical host: inverse problem / observation-operator row span, singular vectors, moment problems, host-relative information and Le Cam binary witnesses; earlier IW MT/NC/PRF/LT work already contains the mathematical principles. NO theorem novelty claim. New local contribution = fresh host-specific adjoints for both maps at chi=.25/.75, explicit six-gradient geometry, synthetic robustness direction, and independent heldout ODE at chi=0/1, with admitted numeric limits.

Question: when three comoving zero/first/second log-mass moments of each anti-nucleon species remain fixed, can a single nonzero source redistribution also make both map targets insensitive across several thermal backgrounds? And does an **approximate** multi-background direction transfer to thermal backgrounds NOT used for source design?

## 1. Exactly controlled source family and target

Let `u=M/(1e9g)`, `z=lnu`, seven non-overlapping C³ compact windows `b_i(z)=sin^4(pi (z-zlo)/(zhi-zlo))` over 7 equal-log-spaced bins in `u in [.07,.92]`, zero outside. For a coefficient vector `c` with `max|c_i|=1`, set

```
Qp'(u) = Qp(u) + epsilon [Qp(u)+Qn(u)] * sum_i c_i b_i(logu)
Qn'(u) = Qn(u) - epsilon [Qp(u)+Qn(u)] * sum_i c_i b_i(logu)
```

This preserves `Qp+Qn` **pointwise**, leaves the original source rates at/above 1e9g and their jets unchanged, and preserves exact source moments for both species when

```
M_j c = 0,   (M_j)_i = integral_bin_i u^3 [Qp(u)+Qn(u)] b_i(logu) (lnu)^j dlnu, j=0,1,2.
```

The source moment definition is the previously used comoving-emission source clock `dt ∝ u²du`. All source comparisons are at `epsilon=0, ±0.15`. This is a seven-dimensional *controlled construction*, not all admissible functions or physical source uncertainty set. The final target is X_n at conditional T_nuc, not Yp/DH or PBH bound.

## 2. Newly executed host-specific target-adjoint kernels, projected operator, rank

Use the ROT021 forward 7D + backward adjoint algorithm (same analytic reaction Jacobian) separately at chiEM=.25 and .75, maps B_exec/B_sym, including each corresponding preedge 10-component bridge and thermal host. For chiEM=.5 use saved, independently FD-checked ROT021 kernel, not a newly claimed run. At each host, project the continuous adjoint K_chi,map(lnu) against the *same* seven source redistributions using the exact Qp+Qn ratio Jacobian; source quadrature 96 nodes per bin, independently audited at 256. Let G_chi,map be the resulting row. Remove three source moments with an orthonormal basis W of ker(M) (dimension 4), and normalize each of six target rows to unit norm. The 6×4 matrix of normalized G_chi,map W has numerical singular values:

```
sigma1 = 2.44750857189671
sigma2 = 0.0984976246068213
sigma3 = 9.18266111928351e-05
sigma4 = 2.60705147828171e-06
```

The 4-th singular value is nonzero at displayed precision, hence sample-specific **numerical row rank 4**. The condition number is 938803.315656. In THIS seven-bin family, after preserving three source moments, six gradient conditions for three backgrounds and two maps do not have an exact nonzero common first-order null direction at numerical precision. Because the smallest singular value is tiny, this is **not** a machine-independent proof of full rank. New 4×2 host-adjoint integrations and a 256-node, tighter-adjoint control (see §5) bound the numerical instability in this computed setup.

By contrast, after projecting out the three moments, the nominal chi=.5 two maps have cosine 0.996767842673; their near collinearity/nominal 5-row condition κ≈8626 came from ROT027, not newly discovered. Six-dimensional row stacking improves span but still remains severely ill-conditioned; use it for diagnostics, not physical inverse accuracy.

## 3. New approx-robust direction, calibrated on chi=.25/.5/.75

Choose the **unit right-singular direction corresponding to the smallest singular value** of the row-normalized six-target matrix in the 4D source-moment null space. Push it to seven source bins and renormalize max|c_i|=1. This minimizes the Euclidean norm of six normalized first-order source-to-target responses **among source directions of fixed Euclidean norm in the 4D moment-null space**; final max-component rescaling does not change the direction. It does NOT solve a uniform supnorm minimax over all chi or exact nonlinear source inversion. No heldout chi=0 or 1 values enter source construction.

Seven source coefficients (ordered ascending source-mass bins):

```
01: -0.4387325732014372
02: +1
03: -0.9254132458872889
04: +0.4444329818926249
05: -0.1169283785971901
06: +0.01606709522649518
07: -0.0009120188544406453
```

Source moment res. verified with independent Gauss-Legendre 320 nodes. Pointwise Qp+Qn identity and positivity verified on a 20k-point grid. The source perturbation is synthetic but comparable to ROT026's direction: both have max|c|=1 and epsilon±.15 over exactly the same bins; no trivial zero-amplitude shortcut.

## 4. *New* fully nonlinear ODE results vs nominal direction

Both target maps and all 5 chi backgrounds are independently re-integrated with fixed coefficients, at epsilon ±.15 and baseline 0. Training backgrounds for the robust singular vector: .25, .50, .75. Genuine heldout backgrounds: .00, 1.00. Same model parameters, source-pinned original archives, chi consistently in source-active bridge and thermal host. Below is the L∞ over the two epsilon endpoints for each map.

| chiEM | Map | Maximum absolute delta Xnuc: previous direction | Maximum absolute delta Xnuc: ROT028 | Reduction |
|---:|:---:|---:|---:|---:|
| 0.00 | B_exec | 1.2126348e-08 | 2.5642860e-10 | 47.29× |
| 0.00 | B_sym | 3.0038288e-09 | 1.3717061e-10 | 21.90× |
| 0.25 | B_exec | 6.1613155e-09 | 1.6407908e-10 | 37.55× |
| 0.25 | B_sym | 1.5575776e-09 | 7.6556428e-11 | 20.35× |
| 0.50 | B_exec | 3.3946745e-10 | 7.3369977e-11 | 4.63× |
| 0.50 | B_sym | 1.4625962e-10 | 3.3852920e-11 | 4.32× |
| 0.75 | B_exec | 5.8066479e-09 | 1.4683776e-10 | 39.54× |
| 0.75 | B_sym | 1.3637281e-09 | 9.2372943e-11 | 14.76× |
| 1.00 | B_exec | 1.1350190e-08 | 2.3382668e-10 | 48.54× |
| 1.00 | B_sym | 2.7042645e-09 | 1.4877966e-10 | 18.18× |

Across training backgrounds, the largest new source-induced absolute Xnuc change is 1.64079084e-10. For unseen chiEM=0 and 1, the largest is 2.56428601e-10, with heldout improvement by **at least 18.18×** among all four heldout map cases. This is an executed *bounded-family numerical* robustness result, not proof for continuous chiEM in [0,1] or general physical halos.

The new source direction is NOT exactly target invisible: even when six adjoint first derivatives are small, full ODE has nonzero odd higher-order slopes and even-in-epsilon nonlinear remnants, of order 1e-11–1e-10 here. Never call this exact sufficiency.

## 5. Independent controls, precise PASS ceiling

- Source controls: max normalized independent three-moment mismatch = 1.1861e-15; max relative pointwise pair-sum mismatch = 2.2204e-16; minimum single-channel share of its positive pair = 0.348860866 at epsilon+0.15.
- Four completely independent χ=.25/.75 target-adjoint ODEs at rtol3e-8, each repeated at rtol3e-9. Results stored as full-res 5201-point kernels. Compare 96-point and 256-point projection quadrature across all 4 combinations; singular value sigma4 ranges **2.6068e-6 to 2.6081e-6** and κ about 938.4k–938.9k. The small singular value is numerically resolvable within this implementation, although the precision of tiny individual projected target slopes is sensitive to quadrature.
- Host-specific adjoint diagnostic compare the derivative of log-ratio flattening with full conditional nonlinear ODE: within ~2e-11 in Xn for the finite flattening stress; as in prior ROT021 this is *not* a certified global error bound for arbitrary changes.
- All four heldout map/source cases (chi=0/1, maps exec/sym) rerun at Radau rtol3e-10 vs 3e-9. Maximum difference of a paired epsilon endpoint response = 1.33238e-12, well below observed nonzero heldout changes ~1e-10. Precision is empirical and far from a formal proof of bounded error.
- New negative control: the previous **nominal** direction was independently re-integrated at unseen chi=0 AND chi=1 to form equivalent head-to-head comparisons. Chi=0 prior ROT026 is also present, but refreshed in this rotation; chi=1 first fully completed for this nominal direction here. It shows much larger responses than the new direction.
- Reproducibility package contains original Wu–Xu-inspired S6 raw trajectory archives (public + paper), exact ROT013/020/021/024/026/027 algorithm dependencies, new host adjoint kernels, new ODE CSV/JSON, SVD and quadrature tests, independent nominal unseen benchmark, scripts and per-file SHA256 manifest. ZIP integrity and manifest are verified separately. No claim that independent external replication has occurred.

## 6. Negative knowledge, changes to scientific decisions, next cheapest falsifier

The old blanket statement that nominally two-map-matched moments solve inter-background robustness remains false (ROT027). The new positive result is narrower: when **background-dependent adjoint rows themselves are included** in the calibration, a near-null direction can be found in a bounded seven-window source family whose nonlinear effects remain small also on the two unseen χ endpoints. This is not a universal low-dimensional summary of the source, and a carefully chosen worst-case source direction from the smallest singular vector should not be treated as representative of all possible source errors. In particular no upper bound for all perturbations follows from this witness alone.

The quantitative obstacle is that full row rank at the evaluated sample points leaves no exact nonzero common kernel, but the 4th singular direction is very weak; recovering that direction from noisy, source-valid kernel measurements would be delicate. A natural future falsifier, NOT assigned as a new task here, is to scan intermediate χ points, change thermal/baryon prescriptions, perturb the source-window basis, and run author-native Julia 10D accepted-step physical emission tables. Such a scan is required before claiming any continuous family error bar or physical transfer.

**STOP** `ORIGINAL_JULIA_10D=NOT_EXECUTED`; `LOWM_HADRON_SOURCE_VALIDITY=OPEN`; `SOURCE_VALID_E2B=OPEN`; `BBN_Yp_DH=NOT_CLAIMED`; `PBH_BOUND=NONE`; `PHYSICAL_INTERPRETATION=NOT_ADMITTED`; `NOVELTY=NOT_CLAIMED`; `BW_INGEST=PENDING`; `OWNER_REVIEW=NOT_CONFIRMED`; `CANON=NO`; `EXEC_SIGN=NO`. No new owner task and no time-dependent hidden work.