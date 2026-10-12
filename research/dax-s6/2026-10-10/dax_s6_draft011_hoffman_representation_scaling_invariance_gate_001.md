---
artifact_id: DAX-S6-DRAFT011-HOFFMAN-REPRESENTATION-SCALING-INVARIANCE-GATE-001
bw_ingestion_event_id: ING-20261010-0065
bw_qualification_state: HOFFMAN_REPRESENTATION_SCALING_GATE
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# DAX-S6-DRAFT011-HOFFMAN-REPRESENTATION-SCALING-INVARIANCE-GATE-001

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

DAX-S6-DRAFT011-HOFFMAN-REPRESENTATION-SCALING-INVARIANCE-GATE-001
STATUS
FROM: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_05 / DAX-S6
MODE: AUTONOMOUS FUNCTION-NATIVE CHEAP FALSIFIER / EXACT REPRESENTATION CONTROL / NO NEW FRONT
TARGET: DRAFT011 robustness layer / PRF10 polyhedral Hoffman certificate
CLAIM CEILING: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE
0. QUESTION
PRF10 correctly established the classical Hoffman host:
dist(x,P) <= H(A,C) ||r_{A,C}(x)||
for a fixed legal linear/polyhedral encoding and fixed norms.
Can the numerical size of H, the raw residual ||r||, or even the certificate H||r|| be compared across equivalent constraint representations as though it were an intrinsic robustness property of the scientific object?
ANSWER:
NO, not without a representation / normalization / preconditioning contract.
1. EXACT 1D SCALING CONTROL — H ALONE IS NOT INTRINSIC
Feasible set:
P={x in R : x=0}.
Representation alpha>0:
C_alpha=[alpha],
d=0.
Residual:
r_alpha(x)=alpha x.
With Euclidean norm:
dist(x,P)=|x|.
The optimal Hoffman constant is exactly:
H_alpha = 1/alpha,
because:
|x| <= H_alpha |alpha x|
for all x
requires and is achieved by H_alpha=1/alpha.
Thus the SAME feasible set has Hoffman constant ranging over every positive value merely by changing units/scaling.
Therefore:
SMALL H != INTRINSICALLY WELL-CONDITIONED
and
LARGE H != INTRINSICALLY ILL-CONDITIONED
unless the constraint representation and residual norm are normalized/frozen.
2. RAW RESIDUAL IS EQUALLY REPRESENTATION-DEPENDENT
At the same physical/model point x=1:
||r_alpha(1)||=alpha.
The same violation of the same feasible set can therefore be reported as arbitrarily small or arbitrarily large by equivalent row scaling.
Hence:
RAW RESIDUAL MAGNITUDE != REPRESENTATION-INVARIANT DISTANCE TO FEASIBILITY.
3. STRONGER 2D CONTROL — EVEN H||r|| CAN CHANGE ARBITRARILY
The simple 1D uniform scaling has exact compensation:
H_alpha ||r_alpha(x)|| = |x|.
That does NOT hold as a representation-invariant numerical certificate under general equivalent nonuniform row scaling.
Take:
P={(0,0)} subset R^2.
Representation A:
C_A = I_2.
Then optimal Hoffman constant in Euclidean norm:
H_A = ||I_2^{-1}||_2 = 1.
At x=e_2=(0,1):
||C_A x||_2 = 1,
so
H_A ||r_A(x)|| = 1.
Now use an equivalent equality encoding:
C_K = diag(1,K),
K>=1.
The feasible set is still exactly:
P={(0,0)}.
The smallest singular value of C_K is 1, so:
H_K = ||C_K^{-1}||_2 = 1.
At the SAME x=e_2:
||C_K x||_2 = K.
Therefore:
H_K ||r_K(x)|| = K.
Actual geometric distance:
dist(e_2,P)=1.
Thus the certified upper bound can be made arbitrarily loose by an equivalent row scaling even when the optimal global Hoffman constant is used.
The scientific/model object did not change.
Only the coordinate representation of constraints changed.
4. WHY THIS DOES NOT CONTRADICT HOFFMAN
Hoffman guarantees existence of a valid error bound for a fixed encoding and norm.
It does NOT state that:
- H is invariant under equivalent row scalings;
- raw residual norms are invariant;
- the numerical upper bound H||r|| is optimal pointwise;
- two different encodings can be compared by H or H||r|| without calibration.
Therefore PRF10 theorem remains PASS.
DAX result is a claim-ceiling / representation-legality repair.
5. UNITS / DIMENSIONAL ANALYSIS CONSEQUENCE
If constraints have different physical units, stacking raw residual components into one Euclidean norm is not even dimensionally meaningful without nondimensionalization or a declared weighting.
Equivalent changes of units can alter:
- residual magnitudes;
- row norms;
- apparent dominance of one constraint family;
- estimated robustness rankings.
Therefore a scientific robustness certificate must declare:
RESIDUAL_COORDINATE_SYSTEM
RESIDUAL_UNITS
ROW / BLOCK NORMALIZATION
WEIGHTING / COVARIANCE METRIC
WITNESS NORM
TARGET NORM
before numerical robustness comparisons are interpreted.
6. ROW NORMALIZATION HELPS BUT IS NOT A UNIVERSAL CURE
For simple scalar/equality row scaling, normalizing each nonzero row to unit norm removes the arbitrary multiplicative factor.
However:
- duplicated/redundant constraints can still alter aggregate residual norms;
- block weighting changes the geometry of the residual space;
- equality and inequality blocks may need different scaling;
- stochastic/noisy constraints naturally use covariance or likelihood geometry rather than row norms;
- transport into common coordinates can itself change conditioning.
So the correct requirement is not merely:
NORMALIZE ROWS.
It is:
FREEZE A LEGAL RESIDUAL GEOMETRY / PRECONDITIONING CONTRACT.
7. DUPLICATION CONTROL
Feasible set:
P={x in R : x<=0}.
One-row encoding:
x<=0.
m-duplicate encoding:
x<=0 repeated m times.
With Euclidean residual norm, at x>0:
single residual norm = x,
duplicate residual norm = sqrt(m) x.
The feasible set is unchanged.
The optimal Hoffman constant compensates globally by a factor 1/sqrt(m) in this simple case, but:
- raw residual size changes;
- any fixed external threshold on residual changes;
- nonoptimal certified constants can change practical acceptance;
- mixed redundant/nonredundant constraints can distort block contributions.
Therefore:
RESIDUAL_THRESHOLD must never be treated as representation-independent unless the encoding/weighting is frozen.
8. CROSS-CASE COMPARISON FIREWALL
Suppose two project cases A and B have identical geometric distance-to-feasibility and target sensitivity.
If one is encoded with different row scalings or residual weights, comparing:
H_A vs H_B,
||r_A|| vs ||r_B||,
or H_A||r_A|| vs H_B||r_B||
may rank them differently for purely representational reasons.
Thus:
ROBUSTNESS RANKING ACROSS CASES
requires a common normalization/metric convention
or an explicitly representation-invariant quantity.
9. SAFER INVARIANT TARGET
The intrinsically meaningful quantity is geometric:
dist(x,P)
in a declared witness metric.
For target claims:
dist_T(tau(x),tau(P))
or the target identified-set diameter in a declared target metric.
Hoffman is useful as a COMPUTABLE CERTIFICATE mapping residual coordinates to geometric distance.
Therefore:
Hoffman certificate = interface from representation-dependent residual to declared geometric quantity.
It is not itself automatically the scientific quantity.
10. REVISED DRAFT011 ROBUSTNESS CONTRACT
Current robust-gluing contract should be extended to include:
A. FEASIBLE SET / SCIENTIFIC OBJECT
exact P or W and source semantics.
B. WITNESS METRIC
metric/norm in which distance to feasibility is interpreted.
C. CONSTRAINT ENCODING
A,C,b,d or equivalent relation encoding.
D. RESIDUAL GEOMETRY
norm/weight/covariance on residual space.
E. NORMALIZATION / PRECONDITIONING
row/block scaling rule or declared preconditioner.
F. HOFFMAN CONSTANT / BOUND
for THIS encoding + THESE norms.
G. POINTWISE RESIDUAL
computed under the same contract.
H. GEOMETRIC CERTIFICATE
H||r|| or sharper bound.
I. TARGET MODULUS
omega_tau or exact image propagation.
J. DECISION THRESHOLD
in target/scientific units.
11. REPRESENTATION-EQUIVALENCE TEST
Before comparing robustness certificates from two encodings of the same model:
1. verify they define the same feasible set/scientific object;
2. identify the change of residual coordinates;
3. transport the residual metric accordingly;
4. recompute or transform the error-bound constant;
5. compare only the induced geometric/target bound.
If step 3 or 4 is missing:
CROSS-REPRESENTATION ROBUSTNESS COMPARISON = NOT CERTIFIED.
12. CHEAP FALSIFIER
Given any claimed robustness score S built from residuals / Hoffman constants:
Apply a legal positive diagonal row scaling D to the constraint system.
If:
- feasible set unchanged,
but
- S changes arbitrarily,
then S is not an intrinsic robustness observable.
Use:
C_K=diag(1,K)
for P={0} in R^2
as the smallest witness.
Any purported invariant robustness scalar should survive this control, or explicitly declare representation dependence.
13. IMPLICATION LEDGER
Valid:
fixed encoding + fixed norms + nonempty polyhedral P
=> finite Hoffman error bound.
Invalid:
small Hoffman constant
=> intrinsically robust scientific model.
Invalid:
small raw residual
=> intrinsically close to feasibility across representations.
Invalid:
H||r|| from one encoding
=> directly comparable to H'||r'|| from another encoding.
Valid after contract:
representation-specific residual
+ representation-specific error-bound constant
=> certified bound on declared geometric distance.
Scientific comparison should be made at the geometric/target level, not on raw representation coordinates.
14. MATURE-HOST PLACEMENT
Nearest host:
classical Hoffman error bounds / condition measures / preconditioning / error-bound conditioning.
No new mathematics claimed.
Project contribution:
representation-invariance firewall for DRAFT011 robustness compiler.
15. NEGATIVE KNOWLEDGE
HOFFMAN CONSTANT != INTRINSIC ROBUSTNESS SCALAR.
RAW RESIDUAL != INTRINSIC DISTANCE.
EQUIVALENT CONSTRAINT ENCODINGS != NUMERICALLY EQUIVALENT CERTIFICATES.
ROW SCALING CAN ARBITRARILY CHANGE REPORTED ROBUSTNESS BOUNDS.
ERROR-BOUND HOST LEGALITY != REPRESENTATION-INVARIANT SCIENTIFIC INTERPRETATION.
ROBUSTNESS CERTIFICATE REQUIRES METRIC + ENCODING + NORMALIZATION CONTRACT.
16. FINAL DISPOSITION
RESULT_CLASS:
EXACT REPRESENTATION COUNTEREXAMPLE / CLAIM-CEILING REPAIR / NO NEW FRONT.
PRF10 HOFFMAN HOST:
PRESERVED.
DRAFT011 PATCH:
add RESIDUAL_GEOMETRY + NORMALIZATION/PRECONDITIONING + REPRESENTATION_EQUIVALENCE fields.
SCIENTIFIC_SURPLUS:
NONE.
TRUE_SURPLUS:
NONE.
REOPEN:
only if a project claim proposes a representation-invariant condition number / metric-regularity modulus and supplies its legal relation to source-native observables.
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / SCIENCE_FIRST / NEGATIVE_KNOWLEDGE_PRESERVING.
