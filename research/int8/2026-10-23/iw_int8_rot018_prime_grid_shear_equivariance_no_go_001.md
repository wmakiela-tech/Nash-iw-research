# INT8 ROT018 — fixed scalar convolution versus universal lattice-shear equivariance

DATE 2026-10-23
CELL IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
RETURN_ID IW_INT8_ROT018_PRIME_GRID_SHEAR_EQUIVARIANCE_NO_GO_001_20261023
PROBLEM_ID P3_DTC0A_METRIC_NATURALITY_FILTER_OPERATOR_HOST_001
EVIDENCE EXACT ALGEBRA / EXECUTED NUMPY / RETAINED SOURCE-HELPER E_lin SHA CHECK
LIMITS NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / REFEREE_PENDING / BW_PENDING

## Currentness and subtraction

XH-S4 ROT020-022 owns geometric York P_g tests and the one-shear E_lin non-covariance; INT8 ROT017 already constructed a single exact lattice-shear defect and metric-transported stencil (local artifact; GitHub/Slack writes blocked). M13 ROT026 owns matched-source nonzero continuum K_A; Geeky-S11 ROT001 improved INT8 ROT016 fixed-smooth TT quantifier. This note does NOT claim those results anew.

## Exact classification theorem

Let p>=5 be ODD PRIME, G=F_p^3 and H:G->Sym(3,R) a covariant symmetric tensor array. Let a single translation-invariant COMPONENTWISE scalar convolution act as

 (T_c H)(x)=sum_{v in G} c(v) H(x+v).

For integer determinant-one 3x3 A, define U_A H(x)=A^T H(Ax) A where Ax is reduced mod p for the grid. Assume T_c U_A=U_A T_c for EVERY A in SL(3,Z); coefficients c stay UNCHANGED with A.

Then the following are equivalent:
(i) universal commutation as above;
(ii) c(0)=gamma and c(v)=beta for ALL v!=0;
(iii) T_c=a I+b M, where M H=p^-3 sum_x H(x) is global componentwise mean, a=gamma-beta and b=p^3 beta.

Proof: (T_c U_A H)(x)=A^T sum_w c(A^-1 w)H(Ax+w) A and (U_A T_c H)(x)=A^T sum_w c(w)H(Ax+w) A. Equality for all H iff c(A^-1w)=c(w). Integral elementary shears I+E_ij, i!=j, reduce to generators of SL(3,F_p). Their action is transitive on every nonzero w: complete any two nonzero vectors to oriented determinant-one bases and map one basis to the other. So c must be constant off origin. The converse follows because each A permutes G and constant A tensor-index factors commute with I and spatial averaging. QED.

LOCAL NO-GO: If c has periodic max-coordinate stencil radius R < (p-1)/2, at least one nonzero displacement has c=0. By transitivity beta=0, so T_c=gamma I. In particular the radius-one 7-point E_lin=I+alpha sum_j Delta_ej fails universal unchanged-stencil equivariance for alpha!=0 on p>=5.

Important NONMAP: This does NOT prohibit a geometrically natural FAMILY E_g transforming its coefficients with the metric. A deliberately A-transported local stencil obeys E_(phi*g) U_phi=U_phi E_g for a fixed integer shear, as INT8 ROT017 demonstrated. This theorem classifies only fixed componentwise SCALAR CONVOLUTIONS under all shears. It neither establishes NASH physical gravity covariance nor rules out tensor-coupled, non-translation-invariant, nonlinear, composite-grid, or nonlocal operators. Global mean M is a genuine nonlocal exception.

## Executed checks and provenance

Standalone NumPy orbit enumeration using only six elementary shears from e1:
p5 orbit 124/124, p7 342/342, p11 1330/1330.
Random real symmetric tensor, alpha=.05:
p5 fixed-axis E pullback commutator Frobenius RMS .315760948193; transported E error max 8.88e-16; aI+bM error 8.88e-16.
p7 fixed .353333563227; transported 8.88e-16; mean 8.88e-16.
p11 fixed .342357382444; transported 1.78e-15; mean 1.78e-15.
Unmodified retained deepseek_python_20260627_a87249.py SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801: apply_E E_lin versus independent 7-point stencil p5 max error 4.44e-16.
Local full Markdown report and standalone verifier bundled in a clean-room SHA256 3/3 ZIP, executed PASS; any GitHub write/readback of this shorter record must be verified separately.

Scientific host: elementary matrices generate SL(n,F), standard field linear algebra; not novel mathematics.
NO physical K/J3, continuum, historical DTC runtime byte reconstitution, owner adoption or new task cascade.
