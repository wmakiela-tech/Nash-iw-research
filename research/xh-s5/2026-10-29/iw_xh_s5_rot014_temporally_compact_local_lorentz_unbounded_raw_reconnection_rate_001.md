# XH-S5 ROT014 — temporally compact local Lorentz rotation makes raw reconnection integral arbitrarily large in flat spacetime

artifact_id: IW_XH_S5_ROT014_TEMPORAL_FRAME_COMPACTNESS_AND_UNBOUNDED_RATE_20261029
return_id: XH-S5-ROT014-TEMPORALLY_COMPACT_FRAME_UNBOUNDED_RECONNECTION_RATE_001_20261029
date: 2026-10-29
cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_MATURE_LOCAL_LORENTZ_FRAME_WITNESS / PARTIAL_SOURCE_EQ31_FUNCTIONAL / NO_GLOBAL_TOPOLOGY_PROOF / NO_NOVELTY / NO_NASH_PHYSICAL_CLAIM / NO_CANON / NO_EXEC_SIGN

## Original science and evidence custody

Comisso & Asenjo, Reconnection of Gravitational Fields, Physical Review D 114 084095 (2026-10-28), DOI https://doi.org/10.1103/lmqy-pf9k ; earlier source Frozen-In Gravitational Fields, PRL 136 161401 (2026), DOI 10.1103/6c4q-kx6f. PRIMARY APS METADATA AND ABSTRACT independently checked during this rotation. Full arXiv HTML access failed this rotation. Symbolic source contract F^a=de^a, R^a=i_u F^a, alternative transport w and line integral from previous full source-based XH-S5 ROT013 (Moderator locally archived). Do NOT claim full current article source re-read nor author code execution.

Source itself warns that local nonideal field or line integral does not independently prove the global change of field-sheet connectivity; strong topology and physical frame-selection assumptions remain. This XH mathematics audits only literal raw tetrad derivatives; no novelty or paper-level physics falsification.

PRECEDENT: ROT012 first Minkowski local rotated frame nonzero R and flux; ROT013 first full-rank F and positive exact along-field line integral, but not full separator/topological criterion. The new-to-cell ROT014 strengthens the countercontrol by ARBITRARILY SCALING the rate with a smooth frame rotation of COMPACT TIME SUPPORT, and independently testing magnetic field-line endpoint maps, with exactly identical asymptotic and initial coframes.

## Exact construction

Minkowski metric g=diag(-1,1,1,1), same physical observer u=partial_t. Let b(s)=exp(1-1/(1-s²)) for abs(s)<1 and 0 otherwise, smooth C_infty, b(0)=1. Define f(y)=b(y), h(t)=t*b(t), h(0)=0, hprime(0)=1, h=0 for abs(t)>=1.
beta(x,z)=.7*x+.11*x*z+.08*z².
In terms of alpha, A=cos(alpha)dx+sin(alpha)dy,
e0=dt,
e1=cos(beta)*A+sin(beta)dz,
e2=-sin(alpha)dx+cos(alpha)dy,
e3=-sin(beta)*A+cos(beta)dz.
CONTROL alpha=0 for all spacetime. ACTIVE alpha=kappa*h(t)*f(y) with arbitrary real kappa. This is a smooth time- and space-dependent SO(3) rotation of all spatial coframes. Therefore g and its Riemann curvature EXACTLY unchanged for ALL kappa,t. Both maintain e0=dt and same u. ACTIVE and CONTROL coframes are EXACTLY identical for all abs(t)>=1, all t=0 spatial points, and all abs(y)>=1 for every t.

Raw source-like F1=de1=cos(beta)*dalpha wedge e2 + dbeta wedge e3. At time zero:
F1_active=kappa*f(y)*cos(beta) dt wedge dy + B(x,z)dx wedge dz,
F1_control=B(x,z)dx wedge dz,
B=beta_x*cos(beta)+beta_z*sin(beta).
The instantaneous magnetic field curves defined by u_lambda *F^{1 mu lambda} are SAME in control/active, along y at fixed x,z for time t=0. At origin x=z=0, beta=0 and B=.7!=0. The curve Upsilon: y runs -infinity to +infinity at x=z=t=0 crosses compact nonideal bump, and BOTH ends abs(y)>=1 have exactly R^a=0 for all tetrad components.

Raw nonideality R1=i_u F1 is zero in CONTROL, and equals kappa*f(y)dy on Upsilon in ACTIVE. Therefore:
  abs(integral_Upsilon R1)=abs(kappa)*C, C=integral_-1^1 b(y)dy=1.2069003224378765>0.
For ANY M>0 choose abs(kappa)>M/C and the indicated source-like line integral exceeds M while metric, curvature, physical observer, initial full spatial coframe, pre- and post-time-support full coframe remain unchanged. This is a COMPLETE exact analytic unboundedness proof, not a numerical extrapolation.
At origin at t=0: F1_ty=kappa,F1_xz=.7, determinant F1=(.7*kappa)^2; for kappa=.4 determinant49/625, rank4. Local no-alternative-w condition of previous ROT013 continues to hold for every nonzero kappa in region where f,B,cos beta are nonzero.

IMPORTANT: This is a lower bound for any maximization functional containing this line/component, NOT a calculation of source global ALL-COMPONENT maximum or physical field-sheet reconnection rate. No rigorous proof of any topology change or experimental observer-invariant event. Bare coframe derivative de changes under local Lorentz rotation in standard geometry, no novelty. Source theory might physically restrict tetrad class; this null test does NOT settle that question.

## Independent executed computation

Symbolic test: SymPy exact E^T E=I3 and det(E)=1, derive F1, confirm rank4/det49/625, exact Minkowski metric, and compact support construction — PASS.

Independent numerical route uses raw tetrad functions and central differences without importing symbolic F; SciPy QUAD integrates i_uF1 along Upsilon for kappa=0,.1,.4,1,2,10. Numerical values respectively 0,.1206900322433041,.4827601289731822,1.2069003224324766,2.413800644872195,12.06900322437256, versus exact values 0,.1206900322437877,.4827601289751506,1.2069003224378765,2.413800644875753,12.069003224378765. Residuals below 1e-11 on these samples.

Independent spatial-field-line integration of B=curl(e1) from y=-1.5 to 1.5, initial (x,z)=(.25,.20), kappa=.4:
  at t=.3: endpoint (x,z)=(.2480006691578711,.22389999612570524), displacement .023983476366553135;
  at t=1.2 (after compact temporal support): endpoint exactly (.25,.20), displacement0. This describes transient coframe field-line ENDPOINT MAPPING only and is explicitly NOT proof of a change in topology.

Reproduction: local full Polish scientific report (9233 bytes), original independent SymPy and SciPy/NumPy executable scripts, two frozen JSON, SHA256 member manifest, README. ZIP CRC PASS; all six SHA256 PASS; both scripts executed in clean extracted ZIP with BOTH JSON BYTE-IDENTICAL PASS.
FULL LOCAL moderator ZIP: IW_XH_S5_ROT014_TEMPORALLY_COMPACT_FRAME_UNBOUNDED_RATE_REPRO_20261029.zip
ZIP SHA256 3d07a9c7f93c58abc107b3296499c295758f6cf3186daa70870f60a401038b35.
FULL local science report SHA256 e269c76c1855340deaef623ca9db76a672c7978fad7a5cc78d597b23e8e22bd6.
Exact symbolic script SHA256 700f952ecdbd3a573fa17fb5e5afdb68d8a4903cdafe96d4b4d10b38ed93c215.
Independent numeric script SHA256 88abb10db1b525382ca6bb325fd3b20baeb01d93b3a27fda2e8fb2b77683d3e0.

## SCIENCE / falsifier / caveats

Frame change is a classical local-SO3 gauge transformation preserving SAME Minkowski g,u. This proves raw proposed nonideal ingredients and one source-type integral do NOT by themselves uniquely determine a metric-only gravitational observable; indeed the integral can be arbitrarily scaled within this gauge class. Because raw de alone is coframe anholonomy and not gauge-covariant physical curvature, a proposed completion would need an operational physical tetrad selector or local-Lorentz-covariant construction (including any chosen spin connection). Covariant torsion-free completion de^a+omega^a_b wedge e^b=0 in this particular Minkowski case is a different diagnostic; do NOT silently replace the authors' F^a=de^a by torsion and call it a derivation of their theory.

A true paper-level refutation would require demonstrating that source admissible frames include these rotations under their complete physical conditions, that full separator/field-sheet connectivity tests are met, and that a proposed observable claims local Lorentz invariance. NOT DONE. This turn accesses current APS abstract but not full source text; exact equation interpretation must be independently reviewed. No GR gravitational-wave/PBH/NASH-KJ3 physical result, no author experiment reproduction, NO_MATHEMATICAL_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_CELL_TASK_CASCADE.
