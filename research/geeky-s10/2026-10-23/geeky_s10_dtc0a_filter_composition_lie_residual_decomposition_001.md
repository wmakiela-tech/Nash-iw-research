artifact_id: GEEKY-S10-DTC0A-FILTER-COMPOSITION-LIE-RESIDUAL-DECOMPOSITION-001
problem_id: P3-DTC0A-LIE-RESIDUAL-FILTER-COMPOSITION-001
origin_cell: MGPT-BUD-01-SUCCESSOR-10 / Geeky-S10
created_at: 2026-10-23
document_type: EXACT_SOURCE_LOCAL_OPERATOR_IDENTITY / INTERPRETATION_REPAIR
exposure: PUBLIC
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_FINITE_OPERATOR_MATH / NO_NOVELTY / NO_CANON / NO_EXEC / NO_PHYSICAL_KJ3_UPGRADE

# DTC0a filtered Lie residual: exact composition-defect decomposition

## 0. Trigger

XH-S4 ROT019 found a decisive negative control:

- with spectral derivatives and alpha=0, K_C falls to numerical zero;
- with spectral derivatives and alpha>0, K_C reappears;
- K_A remains large even when K_C is removed.

The source definitions are:

T_i := Lie_{C_i},

E := E_lin,

L_i := T_i E,

b := [C_1,C_2],

T_b := Lie_b,

and

K_C
=
[L_1,L_2]
-
T_b E.

When the derivative is spectrally exact on the tested low-band class, the unfiltered Lie operators satisfy

[T_1,T_2]=T_b

to numerical precision.

The question is then:

what exactly does nonzero K_C measure when E is not the identity?

## 1. Exact identity

Start from

K_C
=
T_1 E T_2 E
-
T_2 E T_1 E
-
T_b E.

Use

E T_i
=
T_i E
+
[E,T_i].

Then

T_1 E T_2 E
=
T_1 T_2 E^2
+
T_1 [E,T_2] E,

and similarly

T_2 E T_1 E
=
T_2 T_1 E^2
+
T_2 [E,T_1] E.

If

[T_1,T_2]=T_b,

then exactly

BOXED:

K_C
=
T_b(E^2-E)
+
T_1[E,T_2]E
-
T_2[E,T_1]E.

This separates three mechanisms.

A. insertion-count / composition mismatch:
T_b(E^2-E);

B. filter-versus-second-transport commutator:
T_1[E,T_2]E;

C. filter-versus-first-transport commutator:
-T_2[E,T_1]E.

Therefore even with an exact derivative and an exact Lie representation before filtering,

NONZERO K_C
does not imply
FAILURE OF [T_1,T_2]=T_[C1,C2].

## 2. Strong negative separator

Suppose E commutes with both T_1 and T_2.

Then the commutator terms vanish, but

K_C
=
T_b(E^2-E).

Therefore K_C can remain nonzero purely because the nested source expression contains TWO copies of E while the comparator T_b E contains only ONE.

Only if one of the following holds does this mechanism vanish automatically:

- E=I;
- E is idempotent, E^2=E;
- T_b(E^2-E) annihilates the selected input.

Hence:

FILTER COMMUTES WITH TRANSPORT
!=
SOURCE K_C VANISHES.

This is an exact source-definition effect.

## 3. Insertion-count-matched residual

Define an algebraic control residual with matched filter count:

K_C^(2)
:=
[T_1E,T_2E]
-
T_b E^2.

Then exactly

BOXED:

K_C^(2)
=
T_1[E,T_2]E
-
T_2[E,T_1]E.

Thus K_C^(2) isolates the failure of E to commute with variable-coefficient Lie transport, while the difference between the source K_C and this matched residual is

K_C-K_C^(2)
=
T_b(E^2-E).

This does NOT claim K_C^(2) is the intended physical observable.
It is an algebraic discriminator only.

## 4. Specialization to E=I+alpha A

In DTC0a,

E
=
I+alpha A,

where A is the dimensionless centered-Laplacian stencil

A = dx^2 Delta_h.

Then

E^2-E
=
alpha A
+
alpha^2 A^2,

and

[E,T_i]
=
alpha[A,T_i].

Therefore K_C is exactly quadratic in alpha as an operator:

K_C(alpha)
=
alpha K_1
+
alpha^2 K_2,

where

K_1
=
T_b A
+
T_1[A,T_2]
-
T_2[A,T_1],

and

K_2
=
T_b A^2
+
T_1[A,T_2]A
-
T_2[A,T_1]A.

Thus:

alpha=0
=> K_C=0

whenever the underlying unfiltered T_i satisfy the Lie representation identity.

At alpha!=0, nonzero K_C can arise even with exact spatial differentiation.

## 5. Constant-coefficient control

If C_1 and C_2 are spatially constant, then:

- b=[C_1,C_2]=0;
- T_i are constant-coefficient directional derivatives;
- E is a periodic Fourier multiplier and commutes with T_i.

Therefore every term vanishes:

K_C=0.

Hence the nonzero alpha>0 spectral K_C requires variable-coefficient transport geometry and/or a nonzero bracket together with the non-idempotent E composition.

## 6. Source-local numerical verification

Using the XH-S4 ROT019 spectral-derivative carrier on the original pure-trace benchmark at N=31:

### alpha=0

source K_C masked RMS:
1.6239016336884985e-18.

All three decomposition terms are exactly zero because E=I.

### alpha=0.05

source K_C masked RMS:
8.199267098820949e-7.

Decomposition sum:
8.199267098820942e-7.

identity residual:
1.4155256326836894e-18.

Individual term RMS values:

T_b(E^2-E):
2.714609336315411e-7.

T_1[E,T_2]E:
3.177480710171322e-7.

-T_2[E,T_1]E:
6.758465944656983e-7.

These are tensor terms with interference/cancellation.
Their scalar RMS values must NOT be added as energy fractions.

### alpha=0.20

source K_C masked RMS:
3.2392597737580425e-6.

decomposition sum:
3.239259773758036e-6.

identity residual:
1.923403830121315e-18.

Individual term RMS values:

T_b(E^2-E):
1.0724525397957845e-6.

T_1[E,T_2]E:
1.2553177402685205e-6.

-T_2[E,T_1]E:
2.670046798449684e-6.

Again these are interfering tensor contributions.

## 7. Consequence for XH Q38

Q38 asked which part of K_C comes from:

- discrete Leibniz failure;
- E_lin nonidentity.

The answer is now exactly stratified.

For the spectral low-band control where the unfiltered Lie identity holds:

CENTERED-DERIVATIVE LEIBNIZ DEFECT
= removed.

Remaining source K_C is generated by:

1. filter insertion-count mismatch E^2 versus E;
2. commutators [E,T_i].

Therefore:

SPECTRAL DERIVATIVE + NONZERO K_C
!=
DISCRETE LEIBNIZ FAILURE.

Likewise:

NONZERO K_C
!=
NONZERO K_A MECHANISM.

XH already showed alpha=0 spectral K_C~0 while K_A remains about 3.8e-5.

## 8. Relation to [P,E]=0

XH ROT018 proved

[P_TT,E]=0.

That does not remove the present defect because the relevant commutators are

[E,T_i],

not

[P,E].

So three different commutation questions must remain separate:

[P,E]=0,

[P,T_i] generally nonzero,

[E,T_i] generally nonzero.

The first concerns projection/filter compatibility.
The second controls TT cross-sector leakage.
The third controls filtered Lie-representation residual.

They are not interchangeable.

## 9. Interpretation ceiling

The source K_C is a computational residual for the chosen filtered operator definition.

Without an explicit theorem specifying the intended deformed algebra, one cannot interpret it uniquely as:

- a failure of the continuum Lie algebra;
- a physical curvature;
- a K/J3 invariant;
- a TT representation anomaly.

At minimum, one must state whether the intended comparator is:

[T_1E,T_2E] versus T_b E,

or an insertion-count-matched alternative such as T_b E^2,

or a differently normalized deformed bracket.

These are distinct mathematical contracts.

## 10. Mature-host subtraction

The algebra uses only:

- operator commutators;
- filtered differential operators;
- representation defects;
- standard product/composition identities.

The observation that filters generally do not commute with variable-coefficient transport is mature PDE/numerical-analysis territory.

No novelty claim.

Project-local value:
exactly type the alpha>0 spectral K_C observed in XH ROT019 and prevent attribution to the already-removed centered-difference Leibniz defect.

## 11. Firewalls

NONZERO K_C
!=
LIE ALGEBRA FAILURE AUTOMATICALLY.

[E,T_C]
!=
[P,T_C].

[P,E]=0
!=
[E,T_C]=0.

TWO FILTER INSERTIONS
!=
ONE FILTER INSERTION.

MATCHED FILTER COUNT
!=
PHYSICALLY CORRECT COMPARATOR AUTOMATICALLY.

TERM RMS RATIOS
!=
ENERGY ATTRIBUTION.

K_C MECHANISM
!=
K_A MECHANISM.

## 12. Disposition

EXACT FILTER-COMPOSITION DECOMPOSITION = PASS.

ALPHA-QUADRATIC OPERATOR LAW = PASS.

N31 spectral alpha=.05 and .20 numerical identity controls = PASS to ~1e-18 RMS.

XH Q38 source-local mechanism split = CLOSED_EXACT at finite-operator level.

INTENDED DEFORMED-LIE ALGEBRA / PHYSICAL MEANING = UNDEFINED.

PHYSICAL K/J3 INTERPRETATION = FORBIDDEN / UNESTABLISHED.

STOP this finite algebra seam unless:
- owner specifies the intended deformed bracket/comparator;
- a continuum host theorem for E and Lie_C is supplied;
- or referee finds an algebraic/source-definition error.

NO_CANON / NO_EXEC / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
NO_NEW_TASK.
