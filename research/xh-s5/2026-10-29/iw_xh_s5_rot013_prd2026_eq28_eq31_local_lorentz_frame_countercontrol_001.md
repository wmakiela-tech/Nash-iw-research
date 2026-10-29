# XH-S5 ROT013 — Exact Eq.(28) + Eq.(31) local Lorentz frame countercontrol in flat Minkowski

artifact_id: IW_XH_S5_ROT013_FULL_RECONNECTION_RATE_FRAME_AUDIT_20261029
return_id: XH-S5-ROT013-SOURCE_EQ28_EQ31_FLAT_METRIC_FRAME_FALSE_POSITIVE_001_20261029
date: 2026-10-29
cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_SOURCE_TYPED_EQ28_EQ31_FRAME_DEPENDENCE / NO_FIELD_SHEET_TOPOLOGY_PROOF / NO_PHYSICAL_RECONNECTION / NO_MATHEMATICAL_NOVELTY / NO_NASH_PHYSICAL_UPGRADE / NO_CANON / NO_EXEC_SIGN

## Original paper and ownership FIRST

Comisso and Asenjo, "Reconnection of Gravitational Fields", Physical Review D 114, 084095, 28 Oct 2026, DOI https://doi.org/10.1103/lmqy-pf9k ; FULL original source https://arxiv.org/abs/2609.25241 verified against literal Eqs.(3),(12),(22),(23-25),(26-28),(29-31). Prior author source Asenjo/Winkler/Comisso, PRL 136 161401 (2026), Frozen-In Gravitational Fields. ORIGINAL AUTHORS expressly say i_u F != 0 and dR != 0 ALONE do NOT imply reconnection. A regular alternative field w=u-zeta with i_w F=0 can implement mere slippage (26-28). Eq.(31) is a proposed integral maximization along field lines from ideal to nonideal to ideal and further field-sheet connectivity/physical frame requirements remain. This XH special case is NOT original article model replication, NOT claim paper proves gravitational reconnection occurs.

Mature prior art: local Lorentz frame changes alter bare de through de' = Lambda de + dLambda wedge e; tetrad coframe anholonomy includes inertial frame effects. Krssak & Pereira, Spin connection and renormalization of teleparallel action, EPJC 75:519 (2015), DOI 10.1140/epjc/s10052-015-3749-2. Different gravity theory, used only as classical frame-covariance host, not proof about PRD author's reconnection. ROT012 in XH-S5 FIRST showed nonzero local R/dR/flux in flat rotating tetrad but explicitly DID NOT calculate Eq.(28) and Eq.(31). ROT013 performs these NEW source-typed checks; no theorem priority.

## Exact witness, two tetrads the SAME on entire t=0 slice

Take Cartesian Minkowski metric g=-dt²+dx²+dy²+dz² and SAME observer u=partial_t. Define positive smooth compact-support C-infinity bump f(y)=exp(1-1/(1-y²)) for abs(y)<1 and exactly0 otherwise. f(0)=1. beta(x,z)=lambda*x+mu*x*z+nu*z², with constants kappa=.4 lambda=.7 mu=.11 nu=.08. Parameter alpha is 0 in CONTROL tetrad C for all time, or kappa*t*f(y) in ACTIVE tetrad D.

Both coframes (a=0,1,2,3):
e0=dt;
e1=cos(beta)*(cos(alpha)dx+sin(alpha)dy)+sin(beta)dz;
e2=-sin(alpha)dx+cos(alpha)dy;
e3=-sin(beta)*(cos(alpha)dx+sin(alpha)dy)+cos(beta)dz.
These are smooth SO(3) frame rotations, g EXACTLY Minkowski at all spacetime points; Riemann ZERO; e0=dt keeps SAME observer. At t=0 alpha=0 for BOTH, so e^a_C(x,y,z)=e^a_D(x,y,z) as entire initial spatial coframes, including all spatial F_ij and magnetic field curves. Only time derivatives differ.

## Source Eq.(3),(22): exact components
F1 = d e1 = cos(beta)*dalpha wedge e2 + dbeta wedge e3.
At t=0 for ACTIVE:
F1_D = kappa*f(y)*cos(beta) dt wedge dy + B(x,z) dx wedge dz,
B=beta_x*cos(beta)+beta_z*sin(beta).
For CONTROL: F1_C=B dx wedge dz, so R1_C=i_uF1_C=0 exactly.
For ACTIVE: R1_D=kappa*f(y)*cos(beta)dy.
At x=z=0, B=.7 and cos(beta)=1. In the active nonideal region f>0, cos(beta)*B!=0, the exact Pfaffian of the antisymmetric 4x4 F1_D is -kappa*f*cos(beta)*B; determinant equals its square, so F1_D has rank4 and KERNEL0. No nonzero smooth alternative transport w with i_wF1_D=0 exists on such an open region. Thus Eq.(28) nonslippage NECESSARY GATE cannot eliminate the active nonideality there. Point (t,x,y,z)=(0,0,0,0): F1_ty=2/5, F1_xz=7/10, det=(2/5*7/10)^2=49/625 exactly; rank4. CONTROL field same spatial B but rank2 and u regular ideal.

## Source Eq.(31) SOURCE-ADMISSIBLE INTEGRAL

At t=0, spatial F1_ij has solely F1_xz=B(x,z), so field vector u_lower*Fdual has only y component, along constant (x,z) and variable y; this holds in BOTH tetrads. Set x=z=0. Field curve Upsilon: y from -infty to +infty. Since bump f vanishes exactly when abs(y)>=1, the curve extends from a fully ideal region (all i_uF^a=0) through a compact nonideal region back to the ideal region, as required in the source's Eq.(31) curves. Along SAME curve: CONTROL absolute line integral0. ACTIVE:
abs integral_Upsilon R1_D = kappa * integral(-1,1) f(y)dy
=0.4 *1.2069003224378765
=0.48276012897515064.
For other fixed (x,z), source-like line integral magnitude kappa*abs(cos(beta))*integral f <=0.48276012897515064; origin attains bound with B nonzero. Thus the exact supremum of this source-typed line-integral functional in the class of t=0 magnetic-field curves is the displayed positive value, versus zero for CONTROL, even though both represent IDENTICAL flat spacetime and have identical t=0 spatial tetrad and instantaneous magnetic lines.

## Reproduction and fidelity gates
Route A Python SymPy1.14 symbolic matrix coframe orthonormality, all F1 derivatives, control equivalence, exact determinant49/625 and rank4: PASS.
Route B entirely independent NumPy2.3.5 / SciPy1.17 finite differences of raw e1, independent quadrature QUAD+composite Simpson, source contour integral for several (x,z), ideal-region checks and same metric at several spacetime points: PASS.
QUAD bump=1.2069003224378765; Simpson=1.2069003224378763; finite-difference-based integral=0.48276012897423803, analytic=0.48276012897515064, error9.13e-13. Metric numerical orthonormality max1.11e-16.
Local Python scripts both replayed in CLEAN ZIP extraction; frozen exact_results.json and numeric_results.json BYTE IDENTICAL to reruns; six file SHA256 matches and ZIP CRC PASS.
Full Moderator local report (10,251 bytes), 2 scripts, 2 frozen JSON, README, SHA manifest ZIP:
IW_XH_S5_ROT013_FULL_RECONNECTION_RATE_FRAME_AUDIT_REPRO_20261029.zip
ZIP SHA256 2b2cbdcbb11f2ebfc869f6f1d9479180acd1471257ad36abfa32222f35e5fcbd.
Report SHA256 37eb9c28d7b4430191d2745482eadc124a5817f26df1bc1101e30e1ae6d1f7b6.
Exact script SHA256 137c9a237132237071814dba0d1f8875f4bcb8f6af9a8a121126379eacd14f4d.
Independent NumPy code SHA256 57aa081748e97cfa556344a1daa60b1eda18f27040db8c2120a4a490cf26e39f.
This GitHub science artifact is NOT the whole standalone ZIP. Remote script/data custody requires separate uploads and readback. Local extraction/source replay proved.

## What this does and does NOT establish
EXECUTED EXACT: literal nonideal Eqs.(3),(22), necessary absence-of-slippage Eq.(28), and nonzero along-curve integral Eq.(31) can be satisfied by PURE smooth inertial local frame rotations in exactly flat Minkowski geometry and with the same u. This creates a serious *frame/observable* physical interpretation gate, not new gravitational physics.

NOT PROVEN: actual 2D field-sheet global connectivity changes, physical reconnection in Minkowski, source's separator Eq.(30) for a real nonflat configuration, source's entire global Eq.(31) physical sufficiency without its topology assumptions, any Einstein-equation failure, or gravitational wave/PBH/GR/K/J3 NASH new discovery. In the rank4 region F1 has no local 2D kernel, therefore extrapolation to reconnecting ideal-region sheets requires separate global topology work. Original authors already recognize local nonideality alone is insufficient; this work cannot simply be called a refutation.

Proposed referee question only: what precise physically selected tetrad class or local-Lorentz-invariant field-sheet construction makes the same metric+same observer give the same final reconnection verdict? If a fixed frame is an extra datum, what operational condition fixes it and how are eqs28,31 transferred? Alternative physical frame fixing, spin-connection completion or curvature-based invariant requires new proof and is NOT supplied here. NO_NEW_CELL_TASK_CASCADE, no acceptance by BW/referee/owner/EXEC.
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_NASH_PHYSICAL_UPGRADE / BW_PENDING.
