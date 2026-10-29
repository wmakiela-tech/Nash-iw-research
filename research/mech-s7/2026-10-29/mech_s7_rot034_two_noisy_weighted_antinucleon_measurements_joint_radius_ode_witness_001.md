artifact_id: MECH-S7-FRONTB-JOINT-NOISY-SOURCE-MEASUREMENT-MINIMAX-GATE-034_20261029
exposure: PUBLIC
claim_ceiling: EXECUTED_CONDITIONAL_FINITE_H2_TWO_MEASUREMENT_BOUNDED_NOISE_RADIUS_AND_NONLINEAR_BINARY_WITNESS
sync_state: GITHUB_PENDING_BW_INGEST
result_class: TWO_MEASUREMENT_CONVEX_PRIMAL_DUAL / INDEPENDENT_SOURCE_AND_ODE_CHECKS / NO_PHYSICAL_PBH_CLAIM
owner_cell: IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7
problem_id: P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001
rotation: ROT034
report_date: 2026-10-29
scientific_admission: NO_SOURCE_VALID_SUBEDGE_EMISSION / NO_AUTHOR_NATIVE_JULIA_10D / NO_BBN_Yp_DH / NO_PBH_BOUND

# Mech-S7 ROT034 — Two imperfect weighted antinucleon measurements: joint bounded-noise information radius and nonlinear witness

## A. Executive scientific result

ROT033's noise analysis was limited to **one** additional weighted source measurement. ROT033's claimed two-measurement conditional improvements (5.05794% one versus 1.35013% two, at exact observations) were therefore **not yet noise-robust**. ROT034 fills that gap using *simultaneously bounded errors* in both ROT033 Gaussian-weighted anti-proton emission summaries, reconstructs positive source witnesses, tests nonlinear ODE trajectories, and independently verifies convex dual values with a direct primal optimization.

Within the same artificial, finite **11-dimensional C³ Legendre-envelope source family** and common fixed H² curvature budget R=11.4359607, original logmass comoving moments j=0,1,2 and pointwise antinucleon pair sum held fixed, the *worst across six conditional targets* (χ_EM=0.25,0.5,0.75 × B_exec,B_sym) is:

| Allowed symmetric absolute measurement error relative to source-class maximum | ONE source statistic remaining radius | TWO source statistics remaining radius |
|---|---:|---:|
| 0% | 5.0579% | 1.3501% |
| 0.1% | 5.1578% | 1.4940% |
| 1% | 6.0564% | 2.8397% |
| 2% | 7.0544% | 4.3241% |
| 5% | 10.0452% | 8.6759% |
| 10% | 15.0198% | 15.0198% |

At 1% maximum-range tolerance for EACH statistic, two measurements retain a 2.13× smaller worst linear information radius than one (2.8397% versus 6.0564% of the no-measurement baseline). At 5% the extra advantage is only 1.16×; at 10% the worst-target result for the chosen pair coincides numerically with using the first statistic alone. Do NOT mistake these error scenarios for a measured instrumental precision. The two Gaussian functionals have H²-dual normalized correlation 0.9817345571012799, explaining their information redundancy and attenuation of the second observation's usefulness as tolerance increases.

**Novelty scope:** the mathematical support-function argument and convex duality are classical. The new **executed scientific diagnostic** is a source-typed two-observation error budget in the conditional Wu–Xu-derived kinetic model, including a positive nonlinear two-source witness and out-of-calibration thermal controls; no theorem novelty or physical admission is claimed.

## B. Source and mathematical definitions

SOURCE: Wu–Xu GitHub `Fenyutanchan/Primordial-Black-Hole` commit `d395183674cace6c9906a8911bdeb7234ba4040d`; source `main-scan.jl` blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`. Its hadron table begins at M=10^9 g. All below-edge spectra here are **synthetic** continuations. The original author-native Julia 10D ODE has NOT been executed in this work. Executed kinetic equations are the separately sourced conditional Mech ROT013 preedge ten-component bridge plus 7D subedge/postsource transport, not a validated physical cosmology prediction.

Let u=M/10^9g, z=ln u ∈ [ln .07,ln .92], and h(z)=Σ_j c_j (1−x²)^4 P_j(x) with 11 coefficients; x is affine normalized z. Source redistributions:

    Q_pbar'(u)=Q_pbar(u)+(Q_pbar(u)+Q_nbar(u))h(z),
    Q_nbar'(u)=Q_nbar(u)−(Q_pbar(u)+Q_nbar(u))h(z).

They conserve total pair emission exactly pointwise (subject to floating point arithmetic), leave all other species unchanged and match all edge jets through order three. Impose j=0,1,2 comoving moments of each species via Cc=0, and H² curvature norm cᵀG2c ≤ R².

In the moment nullspace basis Z, H=ZᵀG2Z>0. For target gradient g=Zᵀℓ, and for two weighted Gaussian measurement rows a_i in Z-coordinates, assume both source measurements report their baseline values with **independently bounded absolute deviations** |a_iᵀβ|≤δ_i, δ_i=η R sqrt(a_iᵀH⁻¹a_i). η is a hypothetical tolerance fraction of each statistic's maximum possible source-induced deviation. The linear target information radius is

    rho_eta(g) = max_β |gᵀβ|
       subject to βᵀHβ≤R² and |a_iᵀβ|≤δ_i (i=1,2).

By finite-dimensional convex duality (and Slater for η>0), this equals

    min_(λ in R²) R sqrt((g−Aλ)ᵀ H⁻¹(g−Aλ)) + Σ_i δ_i |λ_i|,
    A=[a_1,a_2].

The η=0 result is the ordinary orthogonal projection onto the joint measurement nullspace. The two Gaussian weights are kept **UNCHANGED** from ROT033 (greedy exact-information finite scan): first centre 8.32396936244×10^8 g, σ_lnM=1.0; second centre 4.77318736294×10^8 g, σ_lnM=.65. We did NOT redesign their centres for noise and claim NO optimal noisy-instrument design.

## C. Independent numerical audit and error caveats

`analyze_joint_measurement_noise_034.py`: 6 targets × 10 error levels, L-BFGS-B in each of four dual sign orthants; stable normalized 2D optimization. `independent_primal_audit_034.py`: independent 8-variable convex primal SLSQP for 6 targets × 4 nonzero η values, direct H² ball+two linear slab constraints; 21/24 runs returned explicit optimiser SUCCESS. In all 24, maximum **numerical primal-dual objective difference** was 8.70664651e-13 normalized to the original target radius. Three runs terminated with a non-success flag despite ≤1e−12 objective discrepancy and ≤4e−12 measured constraint violation; therefore we do NOT label all 24 optimiser status flags PASS, nor treat a numerical primal/dual match as an exact interval-arithmetic theorem certificate.

The conditional adjoint kernel inputs were re-evaluated with inherited ROT028 tighter variants: worst relative radius change across all tested targets and η=(0,.01,.05) was 8.80056521e-08. This controls tested **numerical sensitivity**, NOT source theory error. The nontrivial rank/conditioning and source-model uncertainty gates remain as in ROT029.

## D. Executed nonlinear two-source witnesses

Construct a dual-supported maximizing perturbation in the three-moment nullspace for χ_EM=.5 targets B_exec/B_sym, at η=.01 or η=.05. Both its + and − variants are passed to the FULL conditional preedge/7D ODE; both are consistent with the SAME hypothetical source readings at the midpoint of the allowed error intervals, preserving each species' three comoving moments and pair total. Tiny finite-precision constraint excesses in the dual-generated source were explicitly removed by a documented conservative multiplicative shrink, then ODE sources rerun. There are **eight groups × three trajectories = 24 executed nominal ODE states**, η=.01 × χ_EM=0,.5,1 × exec/sym (18), and η=.05 × χ_EM=.5 × exec/sym (6).

For η=.01 at χ_EM=.5:

| Map | Numerical linear radius | Executed nonlinear half-gap [Xn(+)−Xn(−)]/2 | Largest individual end-point deviation from baseline |
|---|---:|---:|---:|
| B_exec | 1.34235616e-05 | 1.34234613e-05 | 1.34267393e-05 |
| B_sym | 6.13957506e-06 | 6.13971118e-06 | 6.14156618e-06 |

The half-gap is a **binary worst-case lower bound** for any target estimator that is given only these same noisy source measurements and original moments: either source+ or source−, compatible with one observed midpoint, must incur error >= half their conditional-model target difference. It is NOT a physical PBH/BBN bound or a uniform upper nonlinear bound across the source class.

The same **fixed two witnesses** were run at χ_EM=0 and χ_EM=1 as unseen thermal backgrounds (without shape refitting). The largest absolute executed response divided by the fixed nominal χ=.5 linear reference differed by at most 0.00921155747 fraction; this is the transfer performance of THESE witnesses, not the sharp noisy information radius re-optimized for the held-out backgrounds.

Independent Gauss1536 moment quadrature and two Gaussian constraint checks on all eight witness groups gave max source-moment normalized residual 6.12515119e-12 and minimum conservative continuum positivity lower bound 0.179637783. After feasibility shrink, max normalized measurement-bound violation was 0; all source cases meet the stated budgets within independently verified numerical tolerance. Their H² norms are ≤R.

The formal full 10D original Julia code, physically validated subedge spectra, original author accepted-step error and BBN Yp/DH or PBH bounds are NOT established. Additional attempted 10× tighter full-ODE rerun timed out; **NO TIGHT-ODE PASS is claimed in ROT034**. Isolated clean replay of the 6-target dual optimisation and independent 24-case primal audit reproduced three CSV files **byte-identically**; re-executed `B_exec`/η=.01/χ=.5 three-trajectory conditional ODE yielded all 11 selected numerical fields **identically** (absolute difference zero). The first replay attempt had omitted nested ROT009/ROT010 dependency directories; the corrected replay includes both dependencies and passed. This is computational reproducibility, not physical source certification. Earlier ROT033 tight ODE controls apply to the earlier witness shapes, not automatically to the new noisy witnesses.

## E. Reproducer / custody

1. `OPENBLAS_NUM_THREADS=1 python analyze_joint_measurement_noise_034.py` — exact finite-dimensional dual, six targets, 10 η values, outputs CSV+JSON.
2. `OPENBLAS_NUM_THREADS=1 python independent_primal_audit_034.py` — independent direct primal constraints and primal-dual comparisons.
3. `OPENBLAS_NUM_THREADS=1 python validate_joint_noise_ode_034.py --map exec --eta .01 --chi .5` — positive two-sided source witness and three nonlinear ODE trajectories. Repeat map sym, chi 0/1; and eta .05 for chi .5.
4. `OPENBLAS_NUM_THREADS=1 python kernel_precision_gate_034.py` — inherited tight kernel variants, new noise-radius comparison.
5. `python finalize_rotation_034.py` — regenerates recorded numerical summary and scientific report (excluding its own archive operation).

Self-contained reproducibility directory includes both Mech-S6 original raw archives, all executed ROT033 parent scripts/modules, exact constraint matrices/results, and the new ROT034 evidence. File SHA256s are manifest-checked, with CRC ZIP test. Python numpy/scipy dependencies are declared, not redistributed as wheels or binaries. GitHub write does NOT establish BW ingestion. No invented ING event or cross-cell task cascade.

**HARD STOP:** ORIGINAL_JULIA_10D_NOT_EXECUTED / SUBEDGE_HADRON_SPECTRA_NOT_SOURCE_VALIDATED / NO_INDEPENDENT_PHYSICAL_GRADIENT_ERROR_BOUND / NO_Yp_DH / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / GITHUB_PENDING_BW_INGEST.