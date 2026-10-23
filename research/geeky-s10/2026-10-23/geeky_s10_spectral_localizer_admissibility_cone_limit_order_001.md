artifact_id: GEEKY-S10-SPECTRAL-LOCALIZER-ADMISSIBILITY-CONE-LIMIT-ORDER-001
problem_id: P2-P3-SPECTRAL-LOCALIZER-CUTOFF-TUNING-LIMIT-ORDER-001
origin_cell: MGPT-BUD-01-SUCCESSOR-10 / Geeky-S10
created_at: 2026-10-23
document_type: SOURCE_DERIVED_EXACT_CONSEQUENCE / LIMIT_ORDER_GUARD
exposure: PUBLIC
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: SOURCE_DERIVED_MATH / NO_NOVELTY / NO_CANON / NO_EXEC / NO_KJ3_PHYSICS

# Spectral localizer admissibility cone and cutoff/tuning limit order

## 0. Source

Matt Verhoeven, arXiv:2610.19791v1, Theorem 5.6 / Proposition 5.9.

For an invertible X with spectral gap

g = ||X^{-1}||^{-1},

the cited spectral-localizer theorem requires

kappa <= A
:= g^3 / [12 ||X|| ||[D,X]||],

and

rho >= 2g/kappa.

Under these sufficient conditions the localizer is uniformly gapped and its signature computes the index.

This note derives only elementary consequences of those source inequalities.

NO novelty claim.

## 1. Exact admissibility interval at fixed cutoff

For fixed finite rho>0, the second inequality is equivalent to

kappa >= 2g/rho.

Therefore theorem-certified kappa values are exactly confined to

[ 2g/rho , A ]

provided this interval is nonempty.

Hence:

BOXED:

THEOREM-CERTIFIED FIXED-rho REGION
=
{ kappa :
2g/rho <= kappa <= A }.

In particular, at fixed finite rho there is a strictly positive theorem-certified lower bound on kappa.

Thus:

kappa -> 0 at fixed rho
leaves the theorem's admissible region.

This is a theorem-applicability statement only.
It does NOT imply that the numerical signature must be wrong outside the region.

## 2. Exact minimum cutoff for any theorem-certified kappa

The fixed-rho interval is nonempty iff

2g/rho <= A.

Equivalently,

rho >= rho_min,

with

rho_min
=
2g/A
=
24 ||X|| ||[D,X]|| / g^2.

Therefore:

BOXED:

rho < 24 ||X|| ||[D,X]|| / g^2

implies that Theorem 5.6 / Proposition 5.9 certifies NO value of kappa at all.

At equality rho=rho_min there is exactly one certified tuning value:

kappa=A.

For rho>rho_min the certified interval has positive width.

## 3. Dimensionless admissibility ratio

Define

Q
=
rho / rho_min
=
rho g^2 / [24 ||X|| ||[D,X]||].

Then:

Q<1:
no theorem-certified kappa.

Q=1:
one boundary value kappa=A.

Q>1:
certified interval

kappa/A in [1/Q, 1].

Thus the source theorem has a simple dimensionless cone geometry.

## 4. Double-limit classification

Consider a path

kappa_epsilon -> 0,
rho_epsilon -> possibly infinity.

The theorem's second condition is

rho_epsilon kappa_epsilon >= 2g.

Therefore any theorem-certified small-kappa path must satisfy

rho_epsilon -> infinity

at least as fast as 1/kappa_epsilon.

More precisely, if

rho_epsilon ~ C kappa_epsilon^{-p},

then:

p<1:
rho*kappa ->0, so theorem certification eventually FAILS.

p=1:
certification of the cutoff condition requires C>=2g.

p>1:
the cutoff condition eventually PASSES.

The upper tuning condition kappa<=A is automatically satisfied eventually along every kappa->0 path.

Hence the exact source-theorem limit-order separator is:

BOXED:

SMALL kappa
requires
DIVERGING rho
with
liminf rho*kappa >= 2g.

FIXED CUTOFF LIMIT
and
SMALL-TUNING LIMIT
do not commute inside the sufficient theorem region.

Again:
THEOREM REGION FAILURE != INDEX FAILURE.

## 5. Representation-size scaling

If a truncation family is parameterized by n with

rho_n ~ C_r n^beta,

and one chooses

kappa_n ~ C_k n^{-alpha},

then source-theorem cutoff admissibility requires asymptotically:

beta > alpha:
cutoff inequality eventually passes;

beta < alpha:
cutoff inequality eventually fails;

beta=alpha:
requires C_r C_k >= 2g.

This gives a clean finite-cutoff scaling rule before any numerical extrapolation.

## 6. SU(2) specialization from Verhoeven

For the irreducible SU(2) unitary pi_j:

g=1,
||pi_j||=1,

so Proposition 5.9 gives

kappa <= 1 / [12 C_j],

rho >= 2/kappa,

where

C_j
=
||[D^{oplus(2j+1)}, pi_j]||.

Hence any theorem-certified kappa requires

rho >= 24 C_j.

Verhoeven derives the lower bound

C_j
>=
c_j
:=
sqrt(4j^2+6j+2)
sqrt(2j/(2j+1)).

Therefore a NECESSARY condition for the general theorem to certify any kappa is

rho >= 24 c_j.

As j->infinity,

c_j = 2j + O(1),

so this necessary theorem-cutoff scale satisfies

rho = Omega(j),

with leading lower-bound scale approximately

rho >= 48 j.

Since in the SU(2) parameterization

rho = 3/2 + 2J,

the corresponding truncation-label scale is at least

J >= 24j + O(1)

for certification through this general bound.

This is not claimed sharp.

## 7. Quantitative comparison with the paper's observed working range

Using the paper's commutator lower bound:

j=1/2:
c_j=sqrt(3)≈1.732,
rho theorem-necessary >=41.57.

j=1:
c_j=sqrt(8)≈2.828,
rho theorem-necessary >=67.88.

j=3/2:
c_j=sqrt(15)≈3.873,
rho theorem-necessary >=92.95.

j=2:
c_j=sqrt(24)≈4.899,
rho theorem-necessary >=117.58.

These reproduce and systematize the paper's observation that the general theorem predicts far larger truncations than numerically appear necessary.

The paper reports that, for the tested low-j cases, the index appears already at truncation roughly

rho >= 3/2 + 2(j-1/2)
=
2j + 1/2.

Thus the general sufficient theorem and the observed SU(2)-specific working region are very different objects.

GENERAL SUFFICIENT CERTIFICATE
!=
EMPIRICAL MINIMAL WORKING CUTOFF.

## 8. Low-kappa observations

The paper reports nontrivial low-kappa behaviour at fixed rho for several SU(2) cases.

The source theorem itself already explains why kappa->0 at fixed rho is outside its certified region:

2/kappa <= rho

cannot hold.

But this alone does NOT prove the numerical index must fail there.

The paper's plots are additional case-specific evidence.

Therefore the correct logic is:

THEOREM CONDITIONS FAIL
+
NUMERICAL WRONG SIGNATURE IN SELECTED CASES
=
SOURCE-SPECIFIC NEGATIVE EVIDENCE,

not a universal theorem that fixed-rho kappa->0 always fails.

## 9. Relation to finite truncation claims

For any finite-cutoff index computation based on this theorem, report at least:

g,
||X||,
||[D,X]||,
rho,
kappa,
rho*kappa,
A,
and whether

2g <= rho*kappa
and
kappa <= A.

Reporting kappa alone is insufficient.

Likewise increasing matrix size alone is insufficient unless the cutoff/tuning path is declared.

## 10. Relation to NASH DTC/NCDG

No source-legal map has been established from:

SU(2) spectral triple localizer,
K1 index pairing,
or propagation number

to DTC0a TT residuals, K_A, J3, or any physical NASH observable.

Therefore:

SPECTRAL-LOCALIZER LIMIT ORDER
!=
DTC K_A LIMIT ORDER AUTOMATICALLY.

The project value is methodological:
finite-cutoff and tuning limits must be typed jointly when theorem conditions couple them.

No K/J3 invariant claim follows.

## 11. Mature-host subtraction

The inequalities are from the cited spectral-localizer theorem.
The admissibility interval, rho_min formula and scaling phase are elementary algebraic consequences.

No novelty claim.

Project-local value:
turn XH-S4 Q20 into a compact theorem-applicability gate and a reusable finite-cutoff/tuning reporting contract.

## 12. STOP / reopen

STOP this spectral-localizer branch unless:

1. an independent reproduction of Verhoeven's SU(2) signature grid is needed;
2. a source-local exact commutator norm C_j is obtained;
3. an owner has a legal operator-system embedding requiring a certified localizer;
4. a referee finds an algebraic/source-typing error.

NO_CANON / NO_EXEC / NO_NOVELTY / NO_KJ3_PHYSICS / NO_PHYSICAL_UPGRADE.
NO_NEW_TASK.
