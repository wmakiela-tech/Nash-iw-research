artifact_id: IW_XH_S6_ROT022_SYNTHETIC_FINITE_THIN_DISK_YUKAWA_GEOMETRY_INTEGRATION_AUDIT_001_20261116
date: 2026-11-16
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
to_cell_or_route: IWTO_MODERATOR
return_id: IW_XH_S6_ROT022_SYNTHETIC_FINITE_THIN_DISK_YUKAWA_GEOMETRY_INTEGRATION_AUDIT_001_20261116
result_class: ORIGINAL_AUTHOR_ABSTRACT_VERIFIED / ORIGINAL_FULL_TEXT_SI_RAW_TORQUE_HOLD / INVENTED_THIN_DISK_GEOMETRY_5_RADII / INDEPENDENT_3D_1D_QUADRATURE_60_CASES / POINT_TOY_OPTIMUM_NOT_GEOMETRY_INVARIANT
claim_ceiling: SYNTHETIC_UNIFORM_ZERO_THICKNESS_PARALLEL_COAXIAL_THIN_DISKS / NOT_AN_ET_AL_REAL_WAFERS / NOT_ORIGINAL_PAPER_ALPHA_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
guards: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_EXPERIMENTAL_ALPHA_LIMIT / NO_NASH_BRIDGE / NO_OWNER_TASK_CASCADE

# XH-S6 ROT022 — synthetic extended-mass geometry changes the point Yukawa shape-optimum

## Original source FIRST and source access

Original experiment: Zheng-Jie An, Wen-Hai Tan, Wen-Can Dong et al., Nature Communications, publication 7 October 2026, DOI https://doi.org/10.1038/s41467-026-78187-4 ; publisher https://www.nature.com/articles/s41467-026-78187-4 ; independent PubMed PMID42982831. Original publisher abstract supports two 7.6mg silicon masses, miniature rotating-source torsion pendulum, nominal separations0.654–1.554mm, Newtonian force agreement, maximum force UNCERTAINTY50aN (2sigma) and G=(6.67±0.35)e-11 SI (1sigma). The original authors retain science firstness; these are their measurements, not XH independently measured results.

This rotation repeatedly attempted access to original full publisher manuscript, supplementary file, PMC and scholarly full text. COMPLETE original scientific methods, numeric SI, actual three-dimensional wafer geometry and raw distance/torque/covariance were NOT retrieved. The abstract refers to Yukawa constraints but provides no independently retrieved numerical exclusion curve alpha(lambda). Hence original apparatus cannot be reconstructed from verified accessible source data. This is SOURCE_ACCESS_HOLD, not an assertion the full data do not exist. Classical milligram-force measurement is not an observation of quantized gravity or gravitationally induced entanglement.

## Frozen before data, distinctly artificial mathematical model

The finite geometry test protocol was GitHub pinned BEFORE computing results: https://github.com/wmakiela-tech/Nash-iw-research/blob/1c18bd2d3b2e4c656ad5ddfe9d3be02da1d88301/research/xh-s6/2026-11-16/iw_xh_s6_rot022_finite_thin_disk_yukawa_geometry_predeclared_test_001.md , git blob d8298979d0e8eedc3d86569856618431782f4e37.

ROT021 previously gave a point-mass toy optimum lambda=0.519942582943222mm and peak contrast0.44100476601722627 for two artificial distances numerically equal to published range endpoints, but NOT an actual original wafer experiment.

ROT022 introduces hypothetical MASS=7.6mg per disk, each a uniformly mass-loaded, infinitely THIN, parallel, coaxial circular disk, with INVENTED radii a in [0.02,0.10,0.50,1.00,2.00]mm, and two INVENTED face gaps d1=0.654mm,d2=1.554mm. The radii, zero thickness, alignment, absence of rotation and face-gap interpretation are deliberately invented. In particular, no source author wafer geometry, torsion lever arm or measured force was input to the simulation.

For uniform random surface points, radial square variables u1,u2 are uniform[0,1] and angular difference phi uniform[0,2pi], pair distance s²=d²+a²(u1+u2-2sqrt(u1u2)cos phi). The axial Newton force kernel is K=d/s³ and mature Yukawa point kernel factor q=(1+s/lambda)exp(-s/lambda). The synthetic disk response normalized to its own Newtonian force is Q_disk(d,a,lambda)=E[Kq]/E[K]. After nuisance-G cancellation, two-gap first-order shape contrast is DeltaQ=Q_disk(d1)-Q_disk(d2). Maximize DeltaQ(lambda) over the predeclared lambda range [0.02,20]mm. The a=0 limit is ROT021 point q(d1)-q(d2).

## Actual numeric results (nothing experimentally measured here)

| Invented radius a mm | Peak lambda mm | Peak DeltaQ | Shift lambda vs point | Peak DeltaQ change vs point |
|---:|---:|---:|---:|---:|
| POINT 0 | 0.519943 | 0.441005 | reference | reference |
| 0.02 | 0.520071 | 0.440832 | +0.025% | -0.039% |
| 0.10 | 0.523056 | 0.436862 | +0.599% | -0.939% |
| 0.50 | 0.567623 | 0.387093 | +9.170% | -12.225% |
| 1.00 | 0.623847 | 0.350091 | +19.984% | -20.615% |
| 2.00 | 0.702941 | 0.328882 | +35.196% | -25.424% |

Therefore, the hypothetical point toy optimum is NOT INVARIANT under finite disk radius in the five predefined model families. The invented 2mm-radius disk peak has 35.2% longer lambda and 25.4% smaller shape contrast compared with the point toy. This model-specific fact must NOT be mislabeled as actual experimental sensitivity of An et al. The toy Newton axial-force changes as well: at d=0.654mm, point ≈9.007fN, invented disks radius0.5mm ≈5.228fN, radius1mm ≈2.668fN, radius2mm ≈1.037fN. None are source-reported measured forces.

## Independent actual numerical evidence and adversarial controls

ACTUALLY EXECUTED Python NumPy quadrature integrated the source-independent 3-D pair kernel two ways at orders24×24×96 and48×48×192 (two radial-square variables and one azimuth difference). An INDEPENDENT ONE-DIMENSIONAL INTEGRAL uses the exact distance distribution of two random points in a circle:
 f(r)=4r/(pi a²)*[acos(r/(2a))-(r/(2a))*sqrt(1-(r/(2a))²)], 0<=r<=2a.
This dimension-reduced representation independently verified 5 radii ×2 gaps ×6 lambdas =60 cases: maximum absolute |Q_3D48-Q_1D256|=4.8516746e-14, |Q_24-Q_48|=4.8294702e-15; PDF mass normalization max error7.1254e-13, Newton baseline relative difference7.1187e-13. Independently differentiated FULL finite-disk Newton+Yukawa POTENTIAL numerically for ten cases: force relative agreement max error9.6133e-8. Point a=0 exactly matched q(d,lambda). Four different alpha/lambda pairs yield the SAME invented two-gap ratio with free G normalization, retaining the earlier identifiability warning.

Full synthetic numerical results are supplied as five-radius CSV, 60-case independent convergence CSV and a detailed numerical JSON with ten force-versus-potential checks and four synthetic nonidentifiability examples. The standalone locally executed complete source script and SHA/clean replay checker are in the attached user ZIP. Short independent 1D public reproducibility executable SHA-verified on GitHub:
https://github.com/wmakiela-tech/Nash-iw-research/blob/6ef97e9e6ad3f76b5772c9b2e19ddd426b939a9f/research/xh-s6/2026-11-16/xh_s6_rot022_independent_uniform_disk_1d_yukawa_replay.py
GitHub Actions workflow for that SAME code:
https://github.com/wmakiela-tech/Nash-iw-research/blob/6a8add570a101374c1e25da776c26fb4a1844755/.github/workflows/xh-s6-rot022-uniform-disk-1d-replay.yml
The local ZIP was CRC-tested, all SHA-256 member files verified, re-extracted clean and all three original numerical outputs replayed BYTE IDENTICALLY. Two intentionally corrupted archive-result files fail SHA verification closed. This is mathematical reproducibility, NOT independent experiment replication or peer review.

## NASH source-to-physics interface gating

To evaluate a NASH theory against the ACTUAL An apparatus, obtain the full source three-dimensional rotating mass distribution, torsion lever arm, angular-harmonic torque data, error covariance/background and an independently source-typed dimensionful prediction delta_tau(theta,d;NASH parameters) with a predeclared falsifier. The source abstract's 50aN quoted measurement uncertainty cannot be used as a proxy for a force residual or to divide toy point/disk force and manufacture an experimental alpha exclusion. Even the optimum lambda can change with finite model geometry, and the actual rotating torsion geometry is unknown here. The present two-gap shape still does not jointly identify alpha and lambda if G is a free nuisance parameter.

NO original An Yukawa alpha bounds computed, NO NASH physical bridge established, NO quantum-gravity discovery or novel theorem claimed; original authors and prior published short-range gravity literature retain firstness. BW GITHUB_PENDING_BW_INGEST is not BW ingestion receipt or Moderator acceptance. No AUD/REC signoff, CANON or EXEC_SIGN, no owner-task cascade.

ROT022_FINITE_THIN_DISK_GEOMETRY_TOY_PASS / ORIGINAL_AUTHOR_RAW_DATA_HOLD / POINT_TOY_GEOMETRY_INVARIANCE_FAIL / 60_1D_VS_3D_CHECKS_PASS / NO_EXPERIMENTAL_ALPHA_LIMIT / NO_NASH_BRIDGE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
