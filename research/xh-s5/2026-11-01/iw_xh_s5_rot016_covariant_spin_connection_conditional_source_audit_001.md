# XH-S5 ROT016 — covariance control for source-motivated gravitational-reconnection tetrad diagnostics
artifact_id: IW_XH_S5_ROT016_COVARIANT_SPIN_CONNECTION_SOURCE_LIMIT_AUDIT_20261101
return_id: XH-S5-ROT016-COVARIANT-SPIN-CONNECTION-COMPARISON-SOURCE-CLAIM-GATE_20261101
date: 2026-11-01
cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_MATURE_FRAME_GEOMETRY_AND_SPIN_CONNECTION / SOURCE_CONTRACT_PARTIAL / NO_FULL_ORIGINAL_EQ30_EQ31_REPLAY / NO_NOVELTY / NO_PHYSICAL_ADMISSION / NO_CANON / NO_EXEC_SIGN

## Original 2026 source — facts and access boundary FIRST
Luca Comisso, Felipe A. Asenjo, "Reconnection of gravitational fields", Physical Review D 114:084095 (28 October 2026), DOI https://doi.org/10.1103/lmqy-pf9k, preprint arXiv:2609.25241. APS author/date/abstract source RECHECKED 1 November. The authors define gravitational reconnection as changes to connectivity of gravitational FIELD SHEETS, not only raw tetrad flux or local nonideality. FULL APS and arXiv paper PDF/HTML could NOT be accessed this turn, despite multiple independent routes; scite fulltext connector denied without subscription. Thus the specific literal definitions F^a=de^a (earlier Eq3), R^a=i_uF^a (earlier Eq22), alternative transport Eq28, separator Eq30 and line-based rate Eq31 were inherited from earlier XH-S5 full-source-reviewed local ROT013/014 and later corrected ROT015 report. They were NOT independently reread in 2026-11-01. NO claim of author-equation audit COMPLETE. Source model already distinguishes local nonideality from true reconnection.

## PRIOR ART FIRST — no new mathematics
Krššák & Pereira, "Spin connection and renormalization of teleparallel action", Eur Phys J C 75:519 (2015), DOI https://doi.org/10.1140/epjc/s10052-015-3749-2 (verified open full article section 3, explicit simultaneous tetrad+spin connection transformation). Related independent 2026 EPJC "The field-theoretical formalism for the teleparallel equivalent of general relativity", DOI https://doi.org/10.1140/epjc/s10052-026-16382-9, eqs 4.8–4.10 (2026-10-29). These are classic DIFFERENT geometrical frameworks, NOT evidence that the GR reconnection article uses the same source physical field or should be silently redefined.

Known XH scope: ROT012–014 constructed exact raw coframe F and Eq31-LIKE line integrals changing under local frame rotations while Minkowski g and observer remained fixed. ROT015 additionally calculated entire smooth spatial field-line maps and IMPORTANT corrected false logical implication: smooth invertible 3D magnetic endpoint map DOES NOT imply absence of 3D reconnection (Priest/Demoulin JGR1995; Priest/Hornig/Pontin JGR2003). ROT016 is a DIFFERENT mathematical discriminating check: compare raw coframe derivative with an explicitly simultaneously transformed INERTIAL SPIN CONNECTION; DO NOT claim canonical replacement of authors' source fields.

## Two physically different comparison rules
Start from Cartesian Minkowski coframe e0^a=dx^a and omega0=0. For any smooth pointwise SO(3) spatial rotation E(t,x,y,z), transform tetrad e=E dx. This retains physical metric g EXACTLY but changes RAW F=de=dE wedge dx. A spatially varying E therefore changes the source-motivated raw F even in metric-flat spacetime.

In a separate COVARIANT pair comparison, transform omega=E d(E^-1)=-dE E^-1, and compute Cartan torsion T^a=de^a+omega^a_b wedge e^b, and spin curvature Omega=domega+omega wedge omega. Then T=0, Omega=0 IDENTICALLY. Local coframe rotations are gauge for the simultaneously transformed pair (e,omega). This does NOT prove F=de is equal to T or that Comisso/Asenjo permitted arbitrary changes of their fixed frame. Holding omega=0 AFTER rotating e is NOT a simultaneous gauge transformation of the same pair: it changes the connection.

## Exact inherited ROT015 coframe, now two-connection control
Coordinates (t,x,y,z), g=diag(-1,1,1,1), u=partial_t. Smooth b(s)=exp(1-1/(1-s²)) for abs(s)<1, else zero; h(t)=t*b(t), f(y)=b(y), alpha=kappa*h(t)*f(y), beta=(7/10)*x. Triad E as spatial matrix rows:
 E=[[cos(beta)cos(alpha), cos(beta)sin(alpha), sin(beta)],
    [-sin(alpha),cos(alpha),0],
    [-sin(beta)cos(alpha),-sin(beta)sin(alpha),cos(beta)]].
Full coframe e0=dt, spatial e=E dx. Metric eta, zero Riemann all t,kappa, observer unchanged. At spacetime origin h'(0)=f(0)=1, alpha=beta=0, so RAW source-like F1_ty=kappa, taking values 0,.4,2,10 for kappa=0,.4,2,10. For all these g remains exactly unchanged.

Define W_alpha=-partial_alpha E * E^T and W_beta=-partial_beta E * E^T:
W_alpha=[[0,-cos(beta),0],[cos(beta),0,-sin(beta)],[0,sin(beta),0]];
W_beta=[[0,0,-1],[0,0,0],[1,0,0]];
omega_mu=(partial_mu alpha)*W_alpha+(partial_mu beta)*W_beta.
Exact SymPy verifies E E^T=I, det E=1, both generators skew and:
partial_alpha E+W_alpha E=0;
partial_beta E+W_beta E=0;
partial_alpha W_beta-partial_beta W_alpha + [W_alpha,W_beta]=0.
IMPORTANT: the derivative term and commutator term of this last curvature identity are EACH NONZERO and cancel. Thus all Cartan torsion and inertial spin curvature vanish for arbitrary smooth alpha,beta (not only a single point). At origin raw F1_ty=+kappa; connection contribution=-kappa. This is precisely classical covariance, not experimental gravity or novel math.

## Independent executed tests
Route A standalone SymPy1.14 EXACT alpha,beta symbolic checks, full triad orthogonality, det, generator antisymmetry, derivative cancellations and NONTRIVIAL Maurer-Cartan commutator cancellation: PASS.
Route B separate NumPy2.3.5 with 5-point central differences of RAW triad e and independently coded analytic omega generator + bump derivatives, for 4 kappas (0,.4,2,10) and FIVE spacetime points (20 cases):
 max |T_covariant| =8.501643833369599e-12;
 max |Omega_spin|=2.9605947323337505e-12;
 max |g-eta|=2.220446049250313e-16.
 At origin raw F1_ty numerical values exactly within 9e-12 of 0,.4,2,10.
Math output is independent of the physical source's global reconnecting sheets or field energy.

## Immutable reproducibility and custody
Full Moderator local reproducible ZIP IW_XH_S5_ROT016_COVARIANT_TETRAD_FRAME_GATE_REPRO_20261101.zip
SHA256 ec5f15e7b4e0cddc174b5b200022fc96861df44b5c79ed126ce0db6eb95eadd4.
Full local Markdown audit SHA256 606453d8b93d31e963f22303f2d5e59264582722ffebb1e66d3d453171543843.
Contains 10 members: original full Polish report, standalone SymPy source, independent NumPy source, 2 deterministic JSON, verify.py, README, SHA256SUMS, UNCHANGED prior ROT014/ROT015 full reports.
ZIP CRC PASS, SHA256 all NINE content members PASS; clean isolated ZIP extraction, re-run both independent Python sources and verify.py -> BOTH frozen JSON BYTE_IDENTICAL PASS. Code/ZIP LOCAL, not included in this public GitHub report unless separately uploaded/readback.

## Referee gate and exact NO-CLAIM
What tetrad/connection class is PHYSICALLY SELECTED by authors, or how does their *final* Eq30/Eq31-based connectivity verdict transform when (e,omega) changes together? Need FULL SOURCE text and separator/field-sheet compatibility first. Simply substituting T=de+omega wedge e for their source F=de is UNAUTHORIZED; fixing spin connection to zero in both local frames is NOT gauge-equivalent in a covariant pair formalism. Do NOT conclude (i) authors' theory is refuted, (ii) actual gravitational field reconnection exists in Minkowski, (iii) no 3D reconnection from smooth line maps, (iv) new theorem, or (v) astrophysical NASH K/J3/GR/GW/PBH upgrade.
NO_NOVELTY / NO_PHYSICAL_CLAIM / NO_CANON / NO_EXEC_SIGN / BW_INGEST_UNVERIFIED / NO_CROSS_CELL_TASK_CASCADE.
