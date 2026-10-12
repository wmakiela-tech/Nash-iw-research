# Geeky-S10 LT4 J3 generator-collapse ideal factor and N=0 counterexample

RETURN_ID: GEEKY-S10-LT4-J3-GENERATOR-COLLAPSE-IDEAL-FACTOR-AND-NZERO-COUNTEREXAMPLE-001  
DATE: 2026-10-12  
STATUS: PASS_EXACT_FINITE-DIMENSIONAL / N_EQUALS_ZERO_NOT_SUFFICIENT_FOR_NECESSITY / NO_TENSOR_CLOSURE_CLAIM / NO CANON / NO EXEC_SIGN

Durable native Google Doc:
https://docs.google.com/document/d/14mXwQLrorRugBFhbW1i3cBn1g2ktxo16WlRlzkjBVGY/edit

## General theorem

Let g be represented by rho on a common invariant domain D. Define

tau_F(x)=rho_x F.

Then J_F=0 exactly iff tau_F is itself a Lie-algebra representation.

Therefore

K_F=ker tau_F={x:rho_xF=0}

is a Lie ideal, and tau_F factors through g/K_F.

This reveals a second closure mechanism distinct from carrier null sectors.

## Two distinct mechanisms

A. Carrier-output invisibility:
N=intersection ker rho_x is nonzero and multiplier perturbations land in N.

B. Generator/ideal collapse:
K_F is nonzero, so the deformed representation loses generator directions.

N=0 kills A but not B.

## Exact nonabelian N=0 counterexample

Take aff(1) with basis X,Y and [X,Y]=Y.

On C^2:

rho_X=[[1,0],[0,0]],
rho_Y=[[0,1],[0,0]].

Then [rho_X,rho_Y]=rho_Y and rho is faithful.

ker rho_X=span(e2),
ker rho_Y=span(e1),
so

N=0.

Take

F=rho_Y=[[0,1],[0,0]].

Then

F^2=0 != F,

and

[F,rho_X]=-F !=0.

But

tau_F(X)=rho_XF=F,
tau_F(Y)=rho_YF=F^2=0.

Therefore

[tau_F(X),tau_F(Y)]=0
=
tau_F([X,Y]),

so J_F=0 exactly on this nonabelian algebra.

## Mechanism

For aff(1),

[g,g]=span(Y),

and here

K_F=span(Y)=[g,g].

Thus tau_F factors through the abelian quotient g/[g,g].

Closure survives by killing the commutator direction in generator space, despite N=0 and faithful original rho.

## Consequence

N=0 alone does NOT restore the implication

J_F=0 => F^2=F and [F,rho_x]=0.

Any future necessity theorem must control at least:

- carrier null sector N;
- deformed generator kernel ideal K_F;
- remaining cross-term cancellation in the exact defect identity.

A minimal further richness guard is K_F=0, but this is NOT claimed sufficient.

## Rank-loss diagnostic

In finite-dimensional g:

r_F=dim Im(tau_F),

dim K_F=dim g-r_F.

If J_F=0 but r_F<dim g, closure is occurring in a quotient representation.

Firewall:

ORIGINAL REPRESENTATION FAITHFUL != DEFORMED EXPERIMENT FAITHFUL.

## Disposition

N_EQUALS_ZERO_NECESSITY_HOPE = KILLED_BY_EXACT_NONABELIAN_COUNTEREXAMPLE.  
SECOND_CLOSURE_MECHANISM = GENERATOR_IDEAL_COLLAPSE.  
SPECIFIC_TENSOR_CARRIER_CLOSURE = OPEN_SOURCE_NATIVE.  
NECESSITY_THEOREM = OPEN_ONLY_WITH_STRONGER_RICHNESS_AND_NONCANCELLATION_GUARDS.

NO physical inference / NO novelty / NO canon / NO EXEC_SIGN / NO NEW TASK.
