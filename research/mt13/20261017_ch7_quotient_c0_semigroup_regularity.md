# MT13 — Ch7 quotient C0 semigroup: automatic regularity under bounded surjective Banach reduction
Date: 2026-10-17 | RETURN_ID MT13-CH7-QUOTIENT-C0-SEMIGROUP-REGULARITY-001_20261017
Status: exact standard semigroup theorem / no novelty / no canon / no EXEC.

## Source placement
LT4 Chapter 7 §7.2 says abstract factorization rU_t=V_t r gives a semigroup V but does not itself guarantee continuity: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt4/2026-10-15/lt4_monograph_ch7_fidelity_synthesis_working_20261015.md
This is CORRECT for abstract set maps and without topological assumptions. The following supplementary positive case should be explicitly distinguished.

## Theorem
Let X,Y be Banach spaces. Let r in B(X,Y) be surjective, and let U=(U_t)_{t>=0} be a strongly continuous semigroup of bounded linear operators on X. Assume ker r is U_t-invariant for every t>=0 (equivalently: rU_t is constant on each fiber of r). Define V_t:Y->Y by V_t(rx)=rU_tx. Then V=(V_t)_{t>=0} is a strongly continuous semigroup of bounded linear operators on Y.

Proof: N=ker r is closed; quotient Q=X/N is Banach. The map ~r:Q->Y given by [x]->rx is a bounded bijection, hence bounded inverse by open mapping. Invariance of N yields well-defined quotient operators ~U_t[x]=[U_tx], with norm at most ||U_t||; each is linear bounded. The quotient map pi obeys pi U_t=~U_t pi. For any [x], ||~U_t[x]-[x]||_Q=||[U_tx-x]||_Q<=||U_tx-x||_X->0 as t downarrow 0. Therefore ~U is C0; V_t=~r ~U_t ~r^{-1} is a C0 semigroup. QED.

Even without explicit quotient notation, open mapping gives a lifting constant C such that each y has x with rx=y and ||x||<=C||y||. Consequently ||V_t||<=C||r|| ||U_t||. Note no bounded linear section Y->X is required (surjective maps need not split).

## Generator-domain bonus
Let A denote generator of U and B denote generator of V. Then r(D(A))=D(B), and B r x=r A x for every x in D(A). Inclusion rD(A) subset D(B) follows by differentiating rU_tx=V_t rx. Conversely choose lambda above growth bounds, y in D(B), set w=(lambda-B)y and choose z in X with rz=w. Put x=(lambda-A)^{-1} z. Resolvent intertwining gives rx=(lambda-B)^{-1}rz=y, so y belongs r(D(A)). Resolvent intertwining follows by integrating rU_t=V_t r against exp(-lambda t) for lambda large. The generator relation thus has an exact DOMAIN contract: only on D(A) / D(B), not all X/Y.

## Non-implications / typology
- In arbitrary sets or nonquotient topologies, a merely algebraic V may fail continuity.
- If r not surjective, its image may not be complete or topologically equivalent to declared Y; no automatic C0 on all of Y.
- Bounded operator r and complete Banach target are load-bearing.
- Strong continuity / quotient generator do not imply positivity, complete positivity, trace preservation, admissible tester transport, unitary equivalence, or microcarrier identity.
- A noninjective r can lose hidden-state information even with exact quotient dynamics.
- This is standard quotient C0-semigroup theory (Engel–Nagel host) and not a new universal principle.

## Local suggested paragraph near Ch7 §7.2
'Brak gwarancji ciągłości dotyczy ogólnej faktoryzacji zbiorowej. Jeśli jednak X i Y są przestrzeniami Banacha, r:X->Y jest ograniczoną liniową surjekcją, U_t jest półgrupą C0 operatorów ograniczonych, a ker r jest U_t-niezmiennicze, to indukowana V_t jest automatycznie półgrupą C0 na Y, ponieważ Y jest topologicznie izomorficzna z X/ker r. Dla generatorów A,B zachodzi r(D(A))=D(B) i Brx=rAx na D(A). Wniosek nie dotyczy fizycznej legalności mapy r.'

Placement only. LT4 owns chapter edits. P2/REV020 unchanged, no physical upgrade, no new tasks.
