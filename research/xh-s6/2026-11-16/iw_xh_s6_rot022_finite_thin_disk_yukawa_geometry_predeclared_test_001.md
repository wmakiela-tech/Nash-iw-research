artifact_id: IW_XH_S6_ROT022_PREDECLARED_UNIFORM_THIN_DISK_YUKAWA_FINITE_GEOMETRY_NEGATIVE_CONTROL_001_20261116
date: 2026-11-16
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
status: FROZEN_BEFORE_FINITE_DISK_NUMERICAL_SCAN
return_id: IW_XH_S6_ROT022_PREDECLARED_UNIFORM_THIN_DISK_YUKAWA_FINITE_GEOMETRY_NEGATIVE_CONTROL_001_20261116
claim_ceiling: SYNTHETIC_FINITE_THIN_DISK_GEOMETRY_ONLY / NOT_ORIGINAL_AUTHOR_WAFERS_OR_TORSION_HARMONIC / NO_EXPERIMENTAL_YUKAWA_LIMIT / NO_NASH_BRIDGE
guards: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_EXPERIMENTAL_ALPHA_LIMIT / NO_NASH_BRIDGE / NO_OWNER_TASK_CASCADE

# ROT022 prereg: Does extended mass geometry change the ROT021 point-Yukawa shape optimum?

Author source FIRST: Zheng-Jie An, Wen-Hai Tan, Wen-Can Dong et al., Nature Communications published 2026-10-07 DOI 10.1038/s41467-026-78187-4. Original publisher/PubMed abstract verified (two 7.6 mg silicon wafers, separation 0.654 to 1.554 mm, Newton-compatible torque-derived gravitational forces, 50 aN maximum quoted 2sigma error). ORIGINAL full paper body, supplement, 3D wafer geometry, measured phase/torque and uncertainty covariance not readable via currently available tools. DO NOT claim full text or experimental geometry was used. Prior ROT021 point toy at ARTIFICIAL radii equal to reported distance endpoints yielded lambda_star=(r2-r1)/(2ln(r2/r1))=0.519942582943222 mm, point shape sensitivity q1-q2=0.44100476601722627. Original paper did NOT report this point toy optimum.

NEW independently falsifiable toy question: replace each original hypothetical POINT mass by a UNIFORMLY MASS LOADED, THIN, PARALLEL, COAXIAL CIRCULAR DISK of the same 7.6mg nominal total mass but with INVENTED disk radii a in {0.02,0.10,0.50,1.00,2.00} mm. Disk thickness exactly ZERO, masses normalized by their area; nominal face-plane separations d1=0.654 mm and d2=1.554 mm numerically copied from reported original source abstract, but are NOT validated original apparatus plane gap or wafer thickness. NO rotating source, torsion lever arm, wafer fabrication or measured data included.

For two random independent uniform disk surface points with normalized radial squared fraction u1,u2 in [0,1] and relative azimuth phi uniform [0,2pi], transverse separation rho²=a²(u1+u2-2sqrt(u1u2)cos phi), full gap s=sqrt(d²+rho²). Direct Newton axial force is G*m²*E[d/s³]. Hypothetical scalar Yukawa-alpha added axial force has factor (1+s/lambda)exp(-s/lambda), hence finite-disk relative kernel Q_disk(d,a,lambda)=E[(d/s³)(1+s/lambda)exp(-s/lambda)]/E[d/s³]. This is an EXACT geometric integral for the DEFINED thin-disk toy, not authors' experiment.
Analog of nuisance-G eliminated two-distance shape response S_disk(lambda)=Q_disk(d1,a,lambda)-Q_disk(d2,a,lambda). The corresponding point R=0 shape is q(d1,lambda)-q(d2,lambda). For each radius predeclare numeric optimization over lambda in [0.02,20]mm (one positive maximizing root), and compare optimum lambda, maximum shape amplitude and normalized Newton force to the point model. The hypothesis that all finite radii have the SAME optimum and same maximal shape as point masses is a NEGATIVE CONTROL and shall be explicitly checked/falsified; no outcome hardcoded as PASS.

Numerical verification BEFORE claiming any result:
- Deterministic tensor product Gauss-Legendre quadrature in u1,u2 plus uniform periodic azimuth phi; primary order radial24 x phi96, independently higher-order radial48 x phi192 on every radius and both distances at the maximum and at lambda grid {0.1,0.5,1,2,10}mm.
- Preserve actual max relative errors and report failures; do NOT promise exact convergence without computing.
- Independent quadrature check at radius a=0 is IDENTICAL to point Yukawa q(d,lambda) for each d.
- Independent direct finite-difference derivative of fully integrated point-pair Yukawa potential for selected geometry vs integrated axial force (requires numerical accuracy).
- Independent geometrical long-range limit Q→1 as lambda→infinity, short-range lambda→0 Q→0 for positive d.
- Test arbitrary G multiplier and mass scaling cancel in Q and S (by construction).
- Check at least a single synthetic finite-disk example with different (alpha,lambda) pairs same two-distance Newton normalized force ratio once a common amplitude G*m² is free, retain alpha-lambda nonidentifiability.

Source-fair interpretation: finite-disk geometry may shift the source Toy point optimum, but even a large shift is NOT the original An wafer experiment. No experimental Yukawa exclusion from the source 50aN single quoted uncertainty; no NASH force/torque prediction supplied, hence NO_PHYSICAL_BRIDGE. Source-first publication credit and exact scope needed.
