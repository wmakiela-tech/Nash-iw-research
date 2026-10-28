artifact_id: MECH-S7-FRONTB-WEIGHTED-SOURCE-MEASUREMENT-DESIGN-INFORMATION-RADIUS-033_20261028
exposure: PUBLIC
claim_ceiling: EXECUTED_CONDITIONAL_FINITE_GALERKIN_SOURCE_INFORMATION_DESIGN_AND_NONLINEAR_ODE_VALIDATION
sync_state: GITHUB_PENDING_BW_INGEST
result_class: LINEAR_H2_CONDITIONAL_SHARP_RADIUS / FINITE_CANDIDATE_DESIGN / NEW_NONLINEAR_STATES / HELDOUT_THERMAL_CONTROL
owner_cell: IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7
problem_id: P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001
rotation: ROT033
report_date: 2026-10-28
scientific_admission: NO_PHYSICAL_HAWKING_SUBEDGE_VALIDATION / NO_AUTHOR_NATIVE_JULIA10D / NO_BBN_Yp_DH / NO_PBH_BOUND

# Mech-S7 ROT033 — Which source measurement shrinks the neutron-target information radius?

## A. Decisive conditional finding

Within the **11-dimensional global C³ polynomial source-shape class** inherited from ROT031/032, at fixed ROT032 H²-seminorm budget R=11.435960696834389, exact conservation of the pointwise antinucleon sum and the three comoving mass moments of **each** anti-nucleon, a single additional *Gaussian-weighted anti-proton emission statistic* reduces the worst-case linear neutron-target information radius across three thermal backgrounds and two kinetic maps to **5.05794% of the original radius**. Two separately selected Gaussian-weighted statistics reduce the finite-class worst-case fraction to **1.35013%**. The mechanism is the standard Hilbert-space Riesz representer and a rank-one/rank-two orthogonal projection, not novel mathematics.

For nominal χ_EM=.5 targets:

| Accessible conditional source summary | B_exec sharp linear radius | B_sym sharp linear radius | Worst remaining fraction across six χ_EM={.25,.5,.75}×{exec,sym} |
|---|---:|---:|---:|
| Moment degrees 0,1,2 only | 5.72547461749e−4 | 2.16589567135e−4 | 100% |
| Plus degree-3 log-mass moment | 2.68944652744e−5 | 2.53163661979e−5 | 11.75620% |
| Plus best among scanned smoothly tapered mass windows | 9.38099894798e−5 | 4.31245950543e−5 | 19.95197% |
| Plus ONE Gaussian-weighted anti-p yield | 2.03774597290e−5 | 1.08100437074e−5 | **5.05794%** |
| Plus TWO Gaussian-weighted yields | 7.68398300927e−6 | 2.90785353088e−6 | **1.35013%** |

The **single-Gaussian** candidate was selected among finite predefined grid of Gaussian widths σ_lnM∈{.13,.20,.30,.45,.65,1.0} and 42 log-spaced centers (M/1e9g in [.09,.88]); chosen center M=832396936.244g, σ_lnM=1.0. The **second Gaussian**, greedily selected with the first fixed (not globally optimized as a pair), has center M=477318736.294g, σ_lnM=.65. Scanned 252 Gaussian candidates, 128 smooth finite-window candidates and 10 added raw log-mass moments (plus centered coordinate reparameterizations). The Gaussian is **broad**, not a narrow or physically resolved mass-line measurement. Design and claim are strictly among the examined candidates; no globally optimal physical instrument is identified.

## B. Precisely typed source-to-target setup

Pinned upstream source: Wu–Xu, `Fenyutanchan/Primordial-Black-Hole` commit `d395183674cace6c9906a8911bdeb7234ba4040d`, original `arXiv-2509.05618/main-scan.jl` blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`. Original hadron table `hadrons_from_PBH.dat` begins at **M=10⁹g**; all departures examined below this edge are synthetic / unvalidated spectral continuations. Original author-native Julia ArbFloat full 10-component solve is **not** executed. The executed model bridges conditional 10-component pre-edge dynamics via ROT013 to source-active/postsource 7D kinetics, carrying source data from Mech-S6 archived public/paper branches. No physical claim about PBH constraints, primordial helium, D/H, or native ODE error.

Let `u=M/(10^9 g)`, `z=ln u`, `u∈[.07,.92]`, `x=2(z−zmid)/L`, `L=ln(.92/.07)`. Introduce `h(z)=Σ c_j (1−x²)^4 P_j(x)` for j=0,…,10, where `P_j` is Legendre. Source modification

```
Q_pbar'(u) = Q_pbar(u) + [Q_pbar(u)+Q_nbar(u)] h(z)
Q_nbar'(u) = Q_nbar(u) - [Q_pbar(u)+Q_nbar(u)] h(z)
```

is exactly pair-sum conserving pointwise, with all edge derivatives up to order 3 unchanged and all other channels unchanged. Positivity is checked for **both** ±H²-radius extremal witnesses. Three fixed source summary rows are `C_j c=∫u³ (Q_pbar+Q_nbar) z^j h(z) dz=0`, j=0,1,2, which preserve both species' comoving emitted mass moments since their changes are equal and opposite. Norm constraint `c^T G2 c≤R²` for `G2_{ij}=∫∂_z²φ_i ∂_z²φ_j dz`, R tied exactly to the ROT031 global-smooth perturbation at ε=.15. Such source perturbations are admissible within **this artificial finite-dimensional class** only.

An additional measurement functional is defined unambiguously as

```
A_w(c) = ∫_(log .07)^(log .92) u³ [Q_pbar(u)+Q_nbar(u)] h(log u) w(log u) d(log u).
```

`A_w=0` models two sources having identical values of the newly acquired weighted anti-p yield. Because Q_pbar+Q_nbar remains exactly fixed, this also fixes its complementary anti-n yield. The Gaussian weight is `w(z)=exp(−(z−zcenter)²/(2 σ²))`. Zero reported measurement noise in the primary design is a **hypothesis**; the noise gate in §F relaxes it.

For target `ℓ` (ROT021/ROT028 conditional linearized map at a particular χ_EM), project onto kernel Z of the first three moments, `H=ZᵀG2 Z>0`, `g=Zᵀℓ` and `a=ZᵀA_w`. The original linear radius is `R√(gᵀH⁻¹g)`; the radius after one exact measurement is

```
R * sqrt( gᵀ H⁻¹g − (gᵀH⁻¹a)²/(aᵀH⁻¹a) ).
```

For two measurements use the rank-two Schur-complement projection `R sqrt(gᵀH⁻¹g − vᵀ(AᵀH⁻¹A)⁻¹v)` with `A=[a1,a2]` and `v=AᵀH⁻¹g`. These are **sharp finite-Galerkin linear bounds** under exact information; not rigorous uniform nonlinear error bounds. The total source-to-target sensitivity gradient `ℓ` was computed under the conditional 7D host and is not independently physically error-certified (ROT029).

## C. New executed full nolinear kinetic test

Six sharp source witnesses from the linear information-design construction (one for each map×{fourth moment,one Gaussian,two Gaussians}) were propagated in actual nonlinear conditional ODE for each ε∈{0,+1,−1} at χ_EM=.5 = **18 executed nominal states**, without retuning any coefficient in the ODE. Additional **24 executed heldout states** use χ_EM∈{0,1}, maps exec/sym, kinds one/two Gaussians, ε∈{0,+1,−1}; these χ_EM values were not used to optimize the candidate measurement weights. Thus 42 principal states executed.

At χ_EM=.5, for Gaussian measurement:

- B_exec predicted linear 2.03774597290e−5; nonlinear `δXn(+)=+2.03426876929e−5`, `δXn(−)=−2.03820814226e−5`.
- B_sym predicted 1.08100437074e−5; nonlinear `δXn(+)=+1.08053208024e−5`, `δXn(−)=−1.08181427198e−5`.

At χ_EM=.5, for TWO measurements:

- B_exec predicted 7.68398300927e−6; nonlinear `δXn(+)=+7.68032648468e−6`, `δXn(−)=−7.68714882582e−6`.
- B_sym predicted 2.90785353088e−6; nonlinear `δXn(+)=+2.90617280896e−6`, `δXn(−)=−2.90960429372e−6`.

The corresponding ROT032 (moment-only) source witnesses in the *same* conditional source class and same H² budget produced B_exec approximately +5.7256e−4/−5.7271e−4 and B_sym approximately +2.1658e−4/−2.1661e−4. Those are different **adversarial witnesses**, as required by comparing worst-case attainable output changes under different information constraints; not propagation of a single source through all designs.

### True thermal heldout tests (no weight retuning)

| Added summaries | B_exec χ_EM=0 max|δXn| | B_exec χ_EM=1 | B_sym χ_EM=0 | B_sym χ_EM=1 |
|---|---:|---:|---:|---:|
| One Gaussian | 2.17532239745e−5 | 1.90469647587e−5 | 1.06019319323e−5 | 1.10247528974e−5 |
| Two Gaussians | 7.79551096852e−6 | 7.58144892687e−6 | 2.94104282456e−6 | 2.87877775806e−6 |

The heldout results show no catastrophic transfer failure *for these two synthetic sources and these two heldout backgrounds*. **They do not certify the exact supremum over all possible source shapes at χ_EM=0 or 1.**

## D. Independent controls; pre-admission and failure gates

- **Source positivity and edge:** independent 1536-point source quadrature plus a 200001-point sampling grid and conservative Markov inequality between-grid derivative margin. For TWO Gaussian sources the continuous lower share bound is `≥0.17851` B_exec, `≥0.19562` B_sym, across both signs. All original species and other channels unchanged except the anti-nucleon redistribution.
- **Independent equality checks:** normalized signed error in all three original comoving moments and new Gaussian measurement(s) ≤7.96e−12 for six verified witness cases; all H² norms reproduce R to relative ≤4.91e−13. Conditional target-linear integral recomputed at 1536 nodes agrees with the 512-point design radius to ≤4.52e−7 relative. Thus no unwarranted extra numerical digits of weak target residuals are used.
- **Basis sensitivity:** fixed measurements carried without redesign to n=10,11,13,15 global Legendre bases. At n=15 with two measurements, B_exec conditional radius 8.16014943e−6 and B_sym 3.27665868e−6, vs n=11 values 7.68398301e−6 and 2.90785353e−6. Larger class raises the residual and prevents a universal n-independent claim; improvement persists for these tested bases.
- **Quadrature and adjoint precision:** n∈{10,11,13,15}, nodes∈{256,512,1024}, host-kernel variant normal/tight; computed linear radii are stable to approximately 1e−9 absolute or better (values tabulated). Tight adjoints here inherit ROT028's separate numerical controls; these do not bound physical model error.
- **Solver precision:** four 3-state nominal χ=.5 ODE groups were rerun with `Radau` tolerance 3e−10 vs original 3e−9. Max difference in δXn across these 12 states was `7.75046693491e−13`.
- **Isolated reproducibility:** another 3-state `two_gaussians/exec/χ=.5` ODE independently rerun from code and archives in temporary isolated directory, comparing 9 numeric state/target/step fields: max exact difference 0.0. This is a conditional computational replay, not independent physically validated solver.

## E. Conditional design comparison and interpretation

A fourth *generic* log-mass moment shrinks worst six-target linear radius to 11.756%, while the optimized **one broad positive Gaussian weighting** shrinks it to 5.058%, and greedy two Gaussian weights to 1.350%. The six-target design includes both reaction maps in χ_EM=.25,.5,.75, so this is NOT a trivial single-target adjoint measurement. The finite-scan result says where **a targeted emission data product** would most efficiently reduce uncertainty *in this conditional model and finite-basis uncertainty class*. It does not prescribe a practically available experiment or source-valid PBH spectrum.

The best Gaussian center near 8.32e8g does not mean that a true narrow measurement at that mass is independently optimal. The broad Gaussian still weights sources across the uncertain M<1e9g domain, where the upstream table has **no emission data**. A follow-up should ask how to physically compute/validate the anti-p and anti-n differential yields; repeating synthetic moment proofs without source validation risks diminishing scientific return.

## F. Noise-aware finite-source information bound

For a single measurement define `A=||a||_{H⁻¹}`; its maximum possible source-to-measurement change in this uncertainty class is `RA`. Let a measurement error tolerance be `δ=η RA`. Decompose target dual vector into the component parallel to `a` of norm `p` and an orthogonal component of norm `q`; then `||g||_{H⁻¹}=sqrt(p²+q²)`. The exactly optimized radius with **bounded symmetric measurement error** `|A_w(c)|≤δ` is

```
ρ(η) = R * [ p η + q sqrt(1−η²) ]   if 0≤η<p/sqrt(p²+q²)
ρ(η) = R sqrt(p²+q²)               otherwise.
```

No noise distribution or unmeasured experimental accuracy is assumed. For the chosen SINGLE Gaussian the worst residual radius over six targets relative to no measurement is:

| Measurement tolerance η as fraction of maximum possible weighted-emission range | Worst linear radius fraction |
|---|---:|
| 0 (exact) | 5.05794% |
| 0.01 | 6.05641% |
| 0.05 | 10.04522% |
| 0.10 | 15.01979% |

Thus a useful weighted source statistic must be accompanied by an **absolute measurement-error budget**, not merely an optimized functional. This noise model is mathematical, not the observed error in any existing PBH measurement. Two-Gaussian results above assume both measurements exact; no two-measurement noise-robustness is claimed.

## G. Provenance, negative knowledge and reproducibility

**Important separation of provenance:** (i) upstream Wu–Xu commit/blob and 1e9g emission-table cutoff; (ii) Mech-S6 original four archived 2×2 trajectories; (iii) Mech ROT013 correctly repaired preedge conditional state, ROT020 source-ratio falsifier, ROT021 adjoint, ROT022 postsource state memory, ROT023/024 source moments, ROT025/026 map-specific and joint target, ROT027/028 host transfer/near-null, ROT029 model-operator error, ROT030 11-dimensional null directions, ROT031 regularity basis artifact, ROT032 sharp finite-H² radius and positive binary witness; (iv) ROT033 new candidate-measurement design, analytic noise gate, 42 new ODE states, 12 tight controls, full source and basis checks.

**Mature theory subtraction:** Riesz representation, Gram-Schur projection, optimal experimental design of linear functionals, Fisher/Le Cam target decision sufficiency, and finite-dimensional dual norm/measurement-noise tradeoff are classical. NO claim to original theorem / novelty. The scientific delta is the concrete source-typed, preedge-bridged PBH→neutron conditional experiment with adversarial source witnesses and independent ODE controls.

**Reproducer entrypoints** (all files and dependencies in the associated ZIP):

1. `OPENBLAS_NUM_THREADS=1 python design_additional_source_measurement_033.py` — scans finite Gaussian/window/moment designs, emits full source measurement design JSON and CSV.
2. `OPENBLAS_NUM_THREADS=1 python design_two_windows_033.py` — greedy second measurement.
3. `OPENBLAS_NUM_THREADS=1 python execute_measurement_witness_033.py --map exec --kind two_gaussians --chi .5` (and map sym/χ=0/χ=1/alternative kind) — solves full conditional ODE states.
4. `OPENBLAS_NUM_THREADS=1 python independent_measurement_audit_033.py` — high-order quadrature and continuous polynomial-source positivity gate.
5. `OPENBLAS_NUM_THREADS=1 python basis_and_quadrature_robustness_033.py` — n=10/11/13/15 class and quadrature check.
6. `OPENBLAS_NUM_THREADS=1 python measurement_noise_gate_033.py` — exact finite-H² single-observation interval-error support function.
7. `OPENBLAS_NUM_THREADS=1 python verify_clean_replay_033.py` and `python finish_measurement_design_033.py` — isolated 3-state replay and summary.

The self-contained archive includes Python `numpy/scipy` dependencies as package-name declarations (not vendored binary libraries), inherited original archived branches and all executable source codes; file SHA256 and archive CRC verified. GitHub publication and Slack dispatch DO NOT establish BW ingestion, owner approval, independent referee PASS, or EXEC.

**HARD STOP:** `ORIGINAL_JULIA_10D_NOT_EXECUTED / AUTHOR_SPECTRUM_M_BELOW_1e9G_UNVALIDATED / PHYSICAL_OPERATOR_ERROR_UNBOUNDED / NO_BBN_Yp_DH / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / GITHUB_PENDING_BW_INGEST`.