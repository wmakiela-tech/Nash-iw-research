---
artifact_id: M12-DRAFT014-TARGET-WEIGHTED-DE-EXACTNESS-AND-UNIVERSAL-PROTECTION-GATE-001
bw_ingestion_event_id: ING-20261010-0105
bw_qualification_state: DRAFT014_TARGET_WEIGHTED_UNIVERSAL_PROTECTION
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# M12-DRAFT014-TARGET-WEIGHTED-DE-EXACTNESS-AND-UNIVERSAL-PROTECTION-GATE-001

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

M12 - DRAFT014 target-weighted DE exactness and universal-protection gate
RESULT_CLASS
EXACT LOCAL CONTROL / FRONT-B TARGET-ERROR ADMISSION / NO NUMERICAL BOUND / NO NOVELTY CLAIM
TARGET
IW_LT3_LIVING_THEORY_WORKING_DRAFT_014_SOURCE_CONTRACT_ABSORPTION_AND_TARGET_WEIGHTING_20261010
TRIGGER
DRAFT014 correctly separates:
- exact total channel count;
- target-weighted abundance impact.
This return gives the exact target class for which dynamical-equilibrium (DE) history error is automatically invisible, and the corresponding quantitative bound when it is not.
SETUP
Consider one fast intermediate population n(t) obeying:
dn/dt = S(t) - Lambda(t)n(t).
Let the exact channel rate be:
r_exact(t)=b(t)Lambda(t)n(t),
and the DE-substituted channel rate be:
r_DE(t)=b(t)S(t).
Then:
r_exact-r_DE
=
-b(t) dn/dt.
Let a declared scalar target be a weighted channel functional:
T_psi
=
integral_{t0}^{tf} psi(t) r(t) dt.
For abundance-sensitive applications:
psi(t)=w(t),
or equivalently absorb branching into:
phi(t)=w(t)b(t).
CERTIFICATE A - EXACT TARGET-ERROR IDENTITY
For:
phi(t)=psi(t)b(t),
the exact target error is:
Delta T
=
T_exact-T_DE
=
-integral phi(t) dn/dt dt
=
-[phi(t)n(t)]_{t0}^{tf}
+
integral phi_dot(t)n(t) dt.
Therefore:
BOXED
TARGET ERROR IS CONTROLLED BY
BOUNDARY OCCUPANCY
PLUS
TIME VARIATION OF THE TARGET-BRANCH WEIGHT.
No timescale approximation was used in this identity.
CERTIFICATE B - TOTAL-COUNT PROTECTION
If:
1. b(t)=b0 is constant;
2. psi(t)=1;
3. endpoint population vanishes in the declared exact sense:
n(t0)=n(tf)=0
(or corresponding infinite-time limit),
then:
Delta T = 0
exactly.
Hence an arbitrarily non-DE intermediate history can still give the exact total channel count.
Therefore:
EXACT TOTAL CHANNEL COUNT
DOES NOT CERTIFY
POINTWISE DE TRACKING.
CERTIFICATE C - UNIVERSAL PROTECTION THEOREM
Assume endpoint occupancy vanishes and consider a legal class rich enough to contain arbitrary compactly supported nonnegative occupancy perturbations inside (t0,tf).
Then:
Delta T=0
for every legal occupancy history n
IFF
phi_dot(t)=0 almost everywhere.
Equivalently:
phi(t)=constant
on the target interval.
Thus:
BOXED
CONSTANT EFFECTIVE TARGET WEIGHT
IS THE UNIQUE UNIVERSALLY PROTECTED CLASS
UNDER ENDPOINT-ZERO HISTORY ERRORS.
Any genuinely time-varying effective weight phi can be made sensitive to some admissible occupancy history.
This is an exact functional-analytic statement.
CERTIFICATE D - ACCIDENTAL EXACTNESS IS WEAKER
For one specific history n(t), a nonconstant phi may still satisfy:
integral phi_dot n dt
=
[phi n]_{t0}^{tf},
so Delta T=0.
But this is trajectory-specific orthogonality/cancellation.
Therefore:
ONE TARGET-EXACT BENCHMARK
!=
UNIVERSAL TARGET-SAFE DE CLOSURE.
To claim target-safe closure over a source family, the cancellation must be certified uniformly over that family.
CERTIFICATE E - EXACT ZERO-ERROR CONDITION
For any fixed legal history:
Delta T=0
IFF
integral phi_dot(t)n(t) dt
=
[phi(t)n(t)]_{t0}^{tf}.
This is the exact necessary-and-sufficient condition for that target/history pair.
No stronger interpretation is earned.
CERTIFICATE F - SUP-NORM TARGET ERROR BOUND
Without endpoint cancellation:
|Delta T|
<=
|phi(tf)n(tf)|
+
|phi(t0)n(t0)|
+
||phi_dot||_infinity
integral_{t0}^{tf} |n(t)| dt.
Thus a bounded target-error certificate can be built from:
1. endpoint occupancy control;
2. an occupancy integral bound;
3. a bound on time variation of the effective target weight.
This is independent of a pointwise DE tracking theorem.
CERTIFICATE G - L2 VERSION
Also:
|Delta T|
<=
|boundary|
+
||phi_dot||_2 ||n||_2.
The norm pair should be chosen from the admitted source/target contract.
No norm is canonical.
CERTIFICATE H - CONNECTION TO DRAFT014 FRONT B
For a channel c with:
phi_c(t)=w(t)b_c(t),
DRAFT014's exact identity is recovered:
Delta T_c
=
-[w b_c n]
+
integral d(w b_c)/dt * n dt.
Consequences:
- constant branching with zero endpoints protects total channel count;
- time-dependent abundance sensitivity w(t) generally destroys that protection;
- exact count agreement can therefore coexist with nonzero Y_p/D/H-relevant error.
Hence:
EXACT TOTAL CHANNEL COUNT
!=
EXACT NUCLEOSYNTHESIS TARGET.
CERTIFICATE I - SOURCE-HISTORY FAMILY GATE
Let N_adm be the admitted family of possible intermediate histories generated by the PBH B2 source contract.
Define the target-error functional:
L_phi[n]
=
-[phi n]_{t0}^{tf}
+
integral phi_dot n dt.
A uniform target certificate of tolerance epsilon requires:
sup_{n in N_adm}
|L_phi[n]|
<= epsilon.
This is the correct family-level object.
Therefore:
ONE MONOCHROMATIC BENCHMARK
or
ONE SOURCE HISTORY
cannot certify a general B2 target bound unless N_adm is reduced by a theorem.
CERTIFICATE J - RELATION TO DE TRACKING
A pointwise tracking bound:
|n-n_DE| small
is sufficient for many targets, but not logically necessary for a protected constant-weight total count.
Conversely:
exact total count
does not imply
small pointwise tracking error.
Thus:
TRACKING ACCURACY
and
TARGET ACCURACY
are distinct claims.
The correct order is:
source-native DE admission
+
target-weighted error certificate.
CERTIFICATE K - ADJOINT INTERPRETATION
In a larger coupled network, the first-order target variation takes the form:
delta J
=
integral lambda(t)^T B(t) delta r(t) dt.
The scalar effective weight phi above is the one-channel analogue of:
lambda^T B.
Therefore the relevant question is not:
"Is delta r small everywhere?"
but:
"Is delta r small in the directions/times where the target sensitivity weight is large?"
This is consistent with DRAFT014's adjoint bridge.
CERTIFICATE L - CHEAP FRONT-B FALSIFIER
For any proposed DE closure:
1. freeze the exact target;
2. derive its effective weight phi(t) or adjoint sensitivity;
3. identify endpoint terms;
4. compute/estimate phi_dot or target sensitivity variation;
5. identify the admissible history family N_adm;
6. test whether a family-level bound on L_phi exists;
7. only then promote from total-count agreement to Y_p/D/H safety.
If no such bound exists:
TARGET_ERROR_CERTIFICATE = OPEN.
PROGRAMME CONSEQUENCE
DRAFT014 target-weighting repair is mathematically load-bearing.
The strongest safe statement is:
DE can be exact for a coarse integrated channel count even when its time-history approximation is poor.
Target safety requires a separate target-weighted certificate.
The only universally protected weighted-integral targets under endpoint-zero arbitrary history errors are those with constant effective weight.
LOWER-HOST SUBTRACTION
Mature hosts:
integration by parts;
linear functionals on trajectory space;
adjoint sensitivity;
ODE perturbation/error estimation.
PROJECT_ROLE:
claim-local Front-B admission gate.
No new general TPE mathematics.
CURRENT FRONT-B DISPOSITION
PBH_B2_TO_DE_ADMISSION = OPEN.
TARGET_WEIGHTED_ERROR_CERTIFICATE = OPEN.
REOPEN_FOR_BOUNDED_ADAPTER_ANALYSIS = YES.
REOPEN_FOR_NUMERICAL_BOUND = NO.
K_PBH = UNDEFINED.
BIS_PBH_BOUND = NONE.
FIREWALL
EXACT TOTAL COUNT != EXACT TARGET.
TARGET EXACTNESS != TRACKING EXACTNESS.
ONE HISTORY CANCELLATION != UNIFORM SOURCE-FAMILY SAFETY.
SMALL INTERMEDIATE ERROR != SMALL Y_p/D/H ERROR without sensitivity weighting.
NO NUMERICAL BOUND from this theorem alone.
CLAIM CEILING
Exact trajectory-functional theorem only.
No PBH abundance bound.
No BBN numerical endpoint.
No physical-law promotion.
No novelty claim.
REV020 active.
TPE HOLD.
REV021 not created.
NO CANON / NO EXEC_SIGN / SCIENCE_FIRST.
