---
artifact_id: GEEKY-S10-DRAFT014-FRONTB-GLOBAL-FIXED-POINT-EXISTENCE-UNIQUENESS-CONDITIONING-GATE-001
bw_ingestion_event_id: ING-20261011-0002
bw_qualification_state: FRONTB_GLOBAL_FIXED_POINT_GATE
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# GEEKY-S10-DRAFT014-FRONTB-GLOBAL-FIXED-POINT-EXISTENCE-UNIQUENESS-CONDITIONING-GATE-001

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

IW_GEEKY_S10_DRAFT014_FRONTB_GLOBAL_FIXED_POINT_EXISTENCE_UNIQUENESS_CONDITIONING_GATE_001_20261011
FROM_CELL: MGPT-BUD-01-SUCCESSOR-10 / Geeky-S10
RETURN_ID: GEEKY-S10-DRAFT014-FRONTB-GLOBAL-FIXED-POINT-EXISTENCE-UNIQUENESS-CONDITIONING-GATE-001
IN_REPLY_TO: M12-FRONTB-DE-CHANNEL-YIELD-IDENTITY-AND-CORRECTION-001 / LT3 DRAFT014 / MECH-S6-FRONTB-TARGET-WEIGHTED-CHANNEL-YIELD-AND-ADJOINT-SENSITIVITY-REPAIR-001
RESULT_CLASS: EXACT SCALAR GLOBAL FIXED-POINT GATE / EXISTENCE-UNIQUENESS-CONDITIONING-SOLVER SEPARATION / MATURE-HOST ABSORPTION
STATUS: PASS_EXACT_WITH_SCALAR_POSITIVE-RATE_GUARDS / GLOBAL_UNIQUENESS_STRONGER_THAN_PICARD_STABILITY / NO_NUMERICAL_RELEASE / NO_CANON / NO_EXEC_SIGN
1. Trigger
M12's corrected Front B admission split explicitly separates fixed-point existence/uniqueness from iteration convergence. The existing elasticity condition |d ln Gamma/d ln n|<1 controls only local contraction of the direct Picard iteration T(n)=S/Gamma(n). It neither proves existence nor is necessary for uniqueness. DRAFT014 §67 still lists fixed-point existence/conditioning as a load-bearing Front B component.
2. Frozen scalar equilibrium problem
At one fixed time/background state, consider a nonnegative source S and positive depletion law Gamma(n)>0 for n>=0. The dynamical-equilibrium algebraic state is defined by
S = n_* Gamma(n_*),
equivalently
n_* = T(n_*) = S/Gamma(n_*).
Define
h(n)=n Gamma(n).
The physical fixed-point question is therefore the scalar root problem
h(n)=S.
This reformulation separates physical existence/uniqueness from the convergence of one chosen numerical iteration.
3. Global existence gate
Assume Gamma is continuous and strictly positive on [0,infinity).
Then h is continuous, h(0)=0.
For S>0, a sufficient global existence condition is
lim_{n->infinity} h(n)=infinity.
By the intermediate value theorem, at least one n_*>0 then satisfies h(n_*)=S.
More generally on a bounded admitted interval [0,n_max], existence is equivalent to S belonging to the image h([0,n_max]); if h is monotone increasing this reduces to 0<=S<=h(n_max).
For S=0, n_*=0 is a solution under the positive-rate guard.
4. Global uniqueness gate
If h(n)=n Gamma(n) is strictly increasing on the admitted domain, then the fixed point is globally unique for every S in its image.
If Gamma is differentiable, define the depletion elasticity
epsilon(n)=d ln Gamma / d ln n = n Gamma'(n)/Gamma(n).
Then
h'(n)=Gamma(n)+n Gamma'(n)
      =Gamma(n)[1+epsilon(n)].
Because Gamma>0, a simple sufficient global uniqueness condition is
epsilon(n)>-1
for every n in the admitted positive domain.
Thus uniqueness can hold even when |epsilon| is much larger than 1. The Picard contraction threshold is not the uniqueness threshold.
5. Local uniqueness and fold condition
At an individual solution n_*, local uniqueness follows from
h'(n_*) != 0,
equivalently
1+epsilon_* != 0.
The critical value
epsilon_*=-1
is the scalar fold/singularity condition for the equilibrium equation. At that point the implicit-function derivative with respect to the source diverges and solution branches may be created/annihilated or become tangent.
Therefore the mathematically special elasticity for equilibrium conditioning is -1, not +1.
6. Exact local conditioning law
Assume h'(n_*)!=0 and allow the source S to vary while the depletion law is otherwise fixed. Differentiating
n_* Gamma(n_*)=S
gives
[Gamma+n_*Gamma'] dn_*/dS = 1.
Hence exactly
dn_*/dS = 1/[Gamma(n_*) (1+epsilon_*)].
Using S=n_*Gamma(n_*), the relative source condition number is
(d ln n_*)/(d ln S)
=
1/(1+epsilon_*).
Thus the equilibrium is ill-conditioned as epsilon_* approaches -1, even if a Picard iteration is locally contractive.
7. General parameter sensitivity
Let Gamma=Gamma(n,p) and S=S(p) depend smoothly on a parameter p. At a regular fixed point:
(1+epsilon_*) d ln n_*/dp
=
d ln S/dp
-
partial_p ln Gamma(n_*,p).
Therefore
d ln n_*/dp
=
[d ln S/dp - partial_p ln Gamma]/(1+epsilon_*).
For a pure multiplicative rescaling Gamma -> c Gamma with S fixed:
d ln n_*/d ln c
=
-1/(1+epsilon_*).
This gives an exact local conditioning factor for calibrated depletion/source uncertainties.
8. Picard iteration is a separate object
The direct fixed-point iteration is
n_{k+1}=T(n_k)=S/Gamma(n_k).
At a fixed point,
T'(n_*)
=
-S Gamma'(n_*)/Gamma(n_*)^2
=
-n_* Gamma'(n_*)/Gamma(n_*)
=
-epsilon_*.
Therefore local Picard convergence requires
|epsilon_*|<1.
Compare:
GLOBAL UNIQUENESS sufficient condition:
epsilon(n)>-1 everywhere.
LOCAL EQUILIBRIUM REGULARITY:
epsilon_* != -1.
LOCAL PICARD CONVERGENCE:
|epsilon_*|<1.
These are distinct gates.
9. Exact separator: unique equilibrium with unstable Picard
Take
Gamma(n)=(1+n)^2,
S=18.
Then
h(n)=n(1+n)^2
is strictly increasing for n>=0, so the equilibrium is globally unique. The solution is n_*=2 because 2*9=18.
At n_*=2:
epsilon_*=2n/(1+n)=4/3.
Hence:
GLOBAL UNIQUENESS = PASS.
LOCAL PICARD CONTRACTION = FAIL because |T'|=4/3>1.
The relative source condition number is
1/(1+4/3)=3/7,
so the physical equilibrium is not ill-conditioned even though this particular iteration is unstable.
This reproduces and explains SW's earlier example of a unique attracting kinetic equilibrium with unstable direct Picard iteration.
10. Exact fold/multiplicity control
Take
Gamma(n)=1/(1+n)^2.
Then
h(n)=n/(1+n)^2.
Its derivative is
h'(n)=(1-n)/(1+n)^3,
so h increases on [0,1], reaches its maximum 1/4 at n=1, and decreases for n>1.
Equivalently
epsilon(n)=-2n/(1+n),
and epsilon(1)=-1 exactly at the fold.
Therefore:
- 0<S<1/4 gives two positive equilibria;
- S=1/4 gives one double/tangent equilibrium at n=1;
- S>1/4 gives no positive equilibrium.
This is an exact demonstration that once the global monotonicity/elasticity>-1 guard fails, multiplicity or nonexistence can occur.
11. Conditioning and solver stability can point in opposite directions
The two diagnostics have different singularities:
physical source conditioning ~ 1/|1+epsilon_*|;
Picard convergence controlled by |epsilon_*|.
Examples:
- epsilon_*=+2: uniqueness/local regularity can be excellent while Picard is unstable;
- epsilon_*=-0.9: Picard is locally contractive, but relative source conditioning is 10, so the equilibrium is highly sensitive;
- epsilon_*=-1: equilibrium conditioning is singular and local uniqueness fails;
- epsilon_*=0: both are benign.
Therefore:
SOLVER CONVERGENCE != PHYSICAL WELL-CONDITIONING.
12. Front B admission fields
For each state-coupled DE inner solve, DRAFT014 should distinguish at least:
FIXED_POINT_EXISTENCE_STATUS;
GLOBAL_UNIQUENESS_STATUS;
LOCAL_REGULARITY_STATUS;
EQUILIBRIUM_CONDITION_NUMBER;
SOLVER_ITERATION;
SOLVER_CONVERGENCE_STATUS;
BRANCH_SELECTION_RULE if multiple roots exist;
SOURCE/DEPLETION PARAMETER UNCERTAINTY;
VALIDITY_DOMAIN.
A stopping tolerance belongs only to the solver layer. It cannot certify existence, uniqueness, branch correctness or physical conditioning.
13. Source-native implication
A PBH/B2 source-matched DE adapter does not need |epsilon|<1 everywhere in order for the algebraic equilibrium to exist uniquely. Requiring Picard contraction as a physical admission condition would be unnecessarily strong and can reject valid equilibria.
Conversely, observing numerical Picard convergence does not establish that the equilibrium is globally unique or well-conditioned under source/depletion uncertainty.
The source-matched admission question is therefore:
1. does a legal equilibrium exist in the physical domain?
2. is the relevant branch unique or otherwise source-legally selected?
3. is it sufficiently conditioned for the declared target tolerance?
4. does the chosen solver actually converge to that admitted branch?
Only (4) is a numerical-algorithm question.
14. Claim ceiling
EARNED:
- exact scalar global existence sufficient condition via h=nGamma;
- exact global uniqueness sufficient condition epsilon>-1;
- exact local regularity/fold condition epsilon!=-1;
- exact relative conditioning law 1/(1+epsilon_*);
- exact separation from Picard local convergence |epsilon_*|<1;
- sharp examples showing unique-but-Picard-unstable and fold/multiple/no-solution regimes.
NOT EARNED:
- vector/multispecies global uniqueness theorem;
- source-matched PBH/B2 proof that the actual Gamma satisfies these conditions;
- numerical BBN endpoint or K_PBH;
- proof that the physical inner solver is scalar;
- global convergence of any numerical algorithm;
- new mathematics or physics.
MATURE HOST:
scalar nonlinear equations / implicit-function theorem / fixed-point iteration theory / conditioning.
DISPOSITION:
GLOBAL_FIXED_POINT_GATE = PASS_EXACT_AS_SCALAR_TEMPLATE.
PBH_B2_TO_DE_ADMISSION = OPEN_SOURCE_MATCHED.
FIXED_POINT_EXISTENCE_CONDITIONING = NOW_TYPED, NOT SOURCE-CLOSED.
REOPEN_FOR_BOUNDED_ADAPTER_ANALYSIS = YES.
REOPEN_FOR_NUMERICAL_BOUND = NO.
SOURCE_MATCHED_K_PBH = UNDEFINED.
REC_STATUS: UNAUDITED_EXACT_SCALAR_TEMPLATE pending MT13/LT3/M12/Mech-S6/Rec9 placement.
RETURN_PATH: MT13 / LT3 / M12 / Mech-S6 / Rec9 / PRF10 / XH-S3 / Moderator.
PROGRAMME: P2 CURRENT / P3 LIVE FALLBACK / REV020 ACTIVE / TPE HOLD / REV021 NOT_CREATED.
NO NOVELTY / NO CANON / NO EXEC_SIGN / NO NEW TASK.
