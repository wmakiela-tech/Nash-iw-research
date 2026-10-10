# DAX-S6 DRAFT012 CAUSAL COMPOSITION GATE 001

FROM: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_05 / DAX-S6  
RESULT_CLASS: EXACT TOY / CLAIM-CEILING REPAIR / NO NEW FRONT

## Question

Does one-step commutation of intervention actions imply preservation of intervention composition?

## Answer

Not at the level of intervention labels when the high-level state action is nonfaithful.

## Exact toy

Low intervention monoid:

- L={e,a}
- a^2=e

Low state space X={0,1}.

Actions:

- rho_L(e)=id
- rho_L(a)=flip

High state space Z={0,1}, tau=id.

High intervention labels:

- H={E,B,C,D}
- B^2=C
- B^4=E

High state actions:

- rho_H(E)=id
- rho_H(C)=id
- rho_H(B)=flip
- rho_H(D)=flip

Define:

- phi(e)=E
- phi(a)=B

Then one-step commutation holds:

tau rho_L(e)=rho_H(phi(e)) tau

tau rho_L(a)=rho_H(phi(a)) tau

But relation preservation fails:

phi(a^2)=phi(e)=E

while

phi(a)^2=B^2=C

and C!=E as intervention labels.

Thus:

ONE-STEP STATE COMMUTATION != INTERVENTION RELATION PRESERVATION.

The discrepancy is invisible on state space because rho_H(C)=rho_H(E).

## Legal repair

For sequential claims, freeze an explicit intervention-equivalence relation ~ and require:

phi(l2 l1) ~ phi(l2)phi(l1)

for every legal composable pair.

For every defining source relation w1=w2 require:

phi(w1) ~ phi(w2).

If high-level identity is defined only modulo state action, quotient H by action-equivalence. Then E~C and the obstruction disappears. If intervention labels carry claim-relevant distinctions, that quotient is not legal.

## DRAFT012 patch

Keep separate:

- INTERVENTION_ACTION_DESCENT
- INTERVENTION_EQUIVALENCE_RELATION
- INTERVENTION_COMPOSITION_DESCENT
- RELATION_PRESERVATION_STATUS
- SEQUENTIAL_POLICY_DESCENT

## Cheap falsifier

1. Freeze generators and defining relations of the low intervention family.
2. Verify one-step state commutation.
3. Independently test mapped defining relations.
4. Test one held-out composite word.

## Mature host

Monoid/category actions; equivariant maps; homomorphism and relation preservation.

## Negative knowledge

ONE-STEP COMMUTATION != SEQUENTIAL COMPOSITION FAITHFULNESS.  
ACTION EQUALITY != INTERVENTION LABEL IDENTITY.  
GENERATOR COMMUTATION != RELATION PRESERVATION.

SCIENTIFIC_SURPLUS=NONE.  
TRUE_SURPLUS=NONE.  
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / SCIENCE_FIRST.
