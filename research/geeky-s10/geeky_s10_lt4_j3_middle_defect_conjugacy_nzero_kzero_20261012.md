# Geeky-S10 LT4 J3 middle-defect range-invisible conjugacy gate

RETURN_ID: GEEKY-S10-LT4-J3-MIDDLE-DEFECT-RANGE-INVISIBLE-CONJUGACY-AND-NZERO-KZERO-GATE-001  
DATE: 2026-10-12  
STATUS: PASS_EXACT_ALGEBRAIC / NO TENSOR-GRAVITY CLAIM / NO CANON / NO EXEC_SIGN

Durable native Google Doc:
https://docs.google.com/document/d/19tLSeBawl3eMbXsYwGVlS3T74-Fc5sXLA40RYIO6z3o/edit

## Exact middle-defect identity

Let rho be a Lie-algebra representation on D and let

T_x=rho_x F,
Q=F-I.

Then

J_F(x,y)
=
rho_x Q rho_y F
-
rho_y Q rho_x F.

Define

B_F(x,y)=rho_x Q T_y.

Then

J_F=0
iff
B_F(x,y)=B_F(y,x) for all x,y.

So exact closure is equivalent to symmetry of the operator-valued middle defect.

## Deformed one-step reachable range

Define

R_F=sum_y Ran(T_y)
   =sum_y Ran(rho_y F).

Because Ran(rho_yF) subseteq Ran(rho_y),

R_F subseteq R:=sum_y Ran(rho_y).

The exact defect probes Q only on R_F.

## Sharpened sufficient gate

Let

N=intersection_x ker rho_x.

If

Q(R_F) subseteq N,

then every middle-defect term vanishes and therefore J_F=0.

This is weaker than LT4 ROT03's sufficient criterion

Q(R) subseteq N,

because R_F subseteq R.

It remains sufficient, not necessary, since a nonzero B_F may still be symmetric.

## Three distinct closure mechanisms

A. Carrier-output invisibility:
Q(D) subseteq N.

B. Generator/ideal collapse:
K_F=ker(x->rho_xF) nonzero.

C. Middle-range invisibility:
Q(R_F) subseteq N,
possibly with Q(D) not subseteq N and K_F=0.

## Range-invisible conjugacy theorem

Assume F is invertible and acts as identity on the full original transport range R:

Q R=0,
equivalently
F rho_x=rho_x
for every x.

Then

T_x=rho_xF
=F^{-1}rho_xF.

Thus T is exactly conjugate to rho.

Consequences:
- J_F=0;
- ker T=ker rho;
- if rho is faithful, T is faithful;
- T may differ from rho while remaining representation-equivalent.

## Exact N=0, K_F=0 separator

Use LT4 ROT03's tensor-density weight lambda=1:

L_C^(1)u=(Cu)'.

Take

F=I+(c-1)P0,
c!=0,1.

Every L_C^(1)u has zero average, so F acts as identity on R and

T_C=F^{-1}L_C^(1)F.

The common carrier null sector is trivial:

N=0.

The original lambda=1 Witt representation is faithful, so by conjugacy

K_F=0.

Yet

F^2!=F

and, for u=1 and C=e^{ix},

[F,L_C^(1)]u=(1-c)i e^{ix} !=0.

Therefore simultaneously:

N=0;
K_F=0;
J_F=0;
F non-idempotent;
F noncommuting.

Hence N=0 plus K_F=0 still does NOT restore full-carrier idempotence/commutation necessity.

## Remaining algebraic residual

After the three zero-middle-defect mechanisms are removed, the exact residual is

B_F(x,y)=B_F(y,x) !=0.

So any universal necessity theorem must still classify or exclude nonzero symmetric middle-action cross-cancellation.

## Diagnostics

A numerical J3≈0 result should distinguish:
- carrier common-null sector;
- deformed generator rank/kernel ideal;
- F-I on R_F and R;
- representation conjugacy/equivalence;
- zero middle defect versus antisymmetry cancellation.

Firewall:

CLOSURE != UNDEFORMED ACTION != UNIQUE MULTIPLIER.

## Disposition

LT4_ROT03_MIDDLE-RANGE_MECHANISM = ABSTRACTED_AND_SHARPENED.  
N_ZERO_PLUS_K_ZERO_NECESSITY_HOPE = KILLED_BY_EXACT_CONJUGACY_COUNTEREXAMPLE.  
ZERO_MIDDLE_DEFECT_GATE = Q(R_F) subseteq N.  
RESIDUAL_AFTER_THREE_MECHANISMS = NONZERO_SYMMETRIC_B_F_CROSS-CANCELLATION.  
SPECIFIC_TENSOR_CARRIER_CLOSURE = OPEN_SOURCE_NATIVE.

NO physical inference / NO novelty / NO canon / NO EXEC_SIGN / NO NEW TASK.
