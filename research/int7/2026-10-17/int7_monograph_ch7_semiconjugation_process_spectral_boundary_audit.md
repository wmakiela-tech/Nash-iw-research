# INT7 — Chapter 7 semiconjugation / process / spectral-calculus boundary audit

RETURN_ID: INT7-MONOGRAPH-CH7-SEMICONJUGATION-PROCESS-SPECTRAL-BOUNDARY-AUDIT-001_20261017

## Scope

Direct LT4 request: verify coherence of the boundaries between semiconjugation, process equivalence and spectral calculus in Chapter 7.

Audited LT4 Chapter 7 source at commit d1b7da1f6485ca17a4d941a90db8329bd0fd5821.

This rotation treats exactly one seam: when state-level semiconjugation justifies spectral transport, and whether either level justifies process equivalence.

## Verdict

PASS_WITH_ONE_BOUNDARY_LEMMA_AND_TWO_EXPLICIT_NONIMPLICATIONS.

No removal of Theorems 7.1–7.3 is required.

The missing load-bearing statement is an explicit spectral transport gate. Without it, the transition from §7.1 semiconjugation to §7.8 / Problem B can be read too loosely.

## 1. Three distinct levels

### S — abstract semiconjugation

Chapter 7.1 uses
\[
rU_t=V_t r,
\]
with a surjective reduction r.

This concerns projectability of trajectories. It does not require Hilbert carriers, linearity of r, boundedness, self-adjoint generators, spectral measures, CP, or tester spaces.

Therefore it cannot by itself imply a Borel functional-calculus statement.

### F — spectral functional-calculus intertwining

Let H1,H2 be Hilbert spaces, A>=0 and B>=0 self-adjoint, and J a bounded linear operator H1->H2.

Assume for every t>=0:
\[
J e^{-tA}=e^{-tB}J.
\tag{F1}
\]

Then for every lambda>0,
\[
J(A+\lambda I)^{-1}=(B+\lambda I)^{-1}J,
\tag{F2}
\]
because resolvents are Laplace transforms of the heat semigroups.

By the standard spectral theorem / functional calculus this yields, for every bounded Borel m,
\[
Jm(A)=m(B)J,
\tag{F3}
\]
and in particular intertwining of spectral projections.

This is the spectral-intertwining gate.

### P — process equivalence

Let
\[
\mathcal T_1:\mathcal E_1\to\mathcal P,\qquad
\mathcal T_2:\mathcal E_2\to\mathcal P
\]
be process laws on legal tester classes.

If the tester domains differ, comparison requires a legal tester transport
\[
F_{\rm test}:\mathcal E_1\to\mathcal E_2,
\]
and the typed condition is
\[
\mathcal T_1=\mathcal T_2\circ F_{\rm test}.
\]

This is a different contract from (F1)–(F3).

## 2. Boundary 1: semiconjugation does not imply spectral transport

From general
\[
rU_t=V_t r
\]
one cannot infer
\[
r\,m(A)=m(B)\,r,
\]
because A,B and their calculi may not even be defined.

To pass from §7.1 to spectral calculus one must add at least:
- Hilbert carriers;
- nonnegative self-adjoint generators;
- bounded linear intertwiner;
- semigroup intertwining for all t>=0, or an equivalent resolvent/spectral-measure condition.

Therefore:

ABSTRACT SEMICONJUGATION != SPECTRAL INTERTWINING.

Also, one matching multiplier is insufficient. The constant multiplier m=1 intertwines through every bounded linear J and carries no generator information.

ONE MULTIPLIER INTERTWINES != GENERATOR/SEMIGROUP INTERTWINES.

## 3. Boundary 2: spectral transport does not imply process equivalence

Even full (F3) concerns the spectral representation of one declared self-adjoint generator.

A multi-time process additionally depends on preparations, intermediate interventions, environment/memory state, causal composition and tester class.

Those are not determined by the spectral measure of one reduced generator.

The project counterexample in §5.5a supplies the correct nearby separator: two models have identical full reduced endpoint channels at the two inspected times for every initial system state, yet a legal intermediate reset and final X measurement distinguish them perfectly.

The current source proves this only for the two declared endpoint times and preparation. Chapter 7 should retain that exact scope and not upgrade it to equality of a full continuous-time semigroup.

Hence:

ENDPOINT CHANNEL EQUIVALENCE != PROCESS EQUIVALENCE.

More generally:

SPECTRAL INTERTWINING OF A REDUCED GENERATOR != TESTER-COMPLETE PROCESS EQUIVALENCE

unless an additional physical realization maps interventions into the generator-level description.

## 4. Boundary 3: process equivalence does not identify spectral realization

Even equality of all declared tester laws under a bijective legal tester transport does not identify:
- microscopic environment Hilbert spaces;
- Hamiltonians;
- self-adjoint generators;
- spectral multiplicities;
- invisible spectator sectors.

Therefore:

PROCESS EQUIVALENCE != SAME GENERATOR / SAME SPECTRUM / SAME MICROSCOPIC CARRIER.

This is consistent with the Chapter 3 firewall response equivalence != shared physical carrier.

## 5. Recommended three-level diagram

STATE / DYNAMICAL LEVEL:
\[
rU_t=V_t r
\]
projectability / semiconjugation.

Only with linear Hilbert + self-adjoint-generator intertwining:

SPECTRAL LEVEL:
\[
Jm(A)=m(B)J.
\]

No implication to process level without preparation/intervention/tester realization:

PROCESS LEVEL:
\[
\mathcal T_1=\mathcal T_2\circ F_{\rm test}.
\]

There is no universal implication triangle among these three levels.

## 6. Ready-to-paste lemma

**Lemat (bramka transportu spektralnego).** Niech A>=0 i B>=0 będą operatorami samosprzężonymi odpowiednio na przestrzeniach Hilberta H1,H2, a J będzie ograniczonym operatorem liniowym H1->H2. Jeśli dla każdego t>=0
\[
J e^{-tA}=e^{-tB}J,
\]
to dla każdego lambda>0
\[
J(A+\lambda I)^{-1}=(B+\lambda I)^{-1}J,
\]
a w konsekwencji dla każdego ograniczonego borelowskiego mnożnika m
\[
Jm(A)=m(B)J.
\]
Jest to twierdzenie o rachunku funkcyjnym operatorów samosprzężonych. Nie wynika ono z abstrakcyjnej semikonjugacji rU_t=V_tr z §7.1 bez dodatkowych założeń liniowych, dziedzinowych i spektralnych. Również pełny transport rachunku spektralnego nie implikuje równoważności procesu wieloczasowego: ta wymaga osobnego kontraktu przygotowań, interwencji i testerów.

Proof note: use
\[
(A+\lambda I)^{-1}=\int_0^\infty e^{-\lambda t}e^{-tA}\,dt
\]
and the analogous formula for B; boundedness of J allows moving J through the Bochner integral. Standard spectral calculus then extends resolvent intertwining to bounded Borel functions.

## 7. Recommended sharpening of §7.8

Add:

Semikonjugacja dynamiki, intertwining rachunku spektralnego i operacyjna równoważność procesu są trzema różnymi kontraktami. Pierwszy dotyczy projektowalności trajektorii, drugi wymaga operatorowego transportu samosprzężonych generatorów lub ich miar spektralnych, a trzeci — legalnego transportu całej zadanej klasy testerów. Żaden z tych poziomów nie zastępuje pozostałych bez dodatkowego twierdzenia o wspólnej realizacji.

## 8. Theorems 7.1–7.3

Theorem 7.1: PASS.
For fixed t, a point-separating family on Y reconstructs projectability of rU_t through r. Algebraic semigroup descent for all t is also correct. Continuity does not follow automatically.

Theorem 7.2: PASS.
The defect-composition identity only uses linearity of s. It does not promote reductions to physical channels.

Theorem 7.3: PASS_WITH_DECLARED_SCOPE.
It is a classical Banach-space Grönwall estimate. The existing warning correctly blocks direct substitution of unbounded spectral operators, quantum supermaps or history-space relations.

## Firewalls

ABSTRACT SEMICONJUGATION != SPECTRAL INTERTWINING.

ONE SPECTRAL MULTIPLIER != FULL FUNCTIONAL-CALCULUS TRANSPORT.

SPECTRAL INTERTWINING != PROCESS EQUIVALENCE.

ENDPOINT CHANNEL EQUIVALENCE != MULTI-TIME PROCESS EQUIVALENCE.

PROCESS EQUIVALENCE != SAME GENERATOR / SAME SPECTRUM / SAME MICROSCOPIC CARRIER.

COMMON FORM OF A COMMUTING DIAGRAM != COMMON PHYSICAL MECHANISM.

## Final status

CHAPTER7_SEMICONJUGATION_BOUNDARY = PASS_WITH_EXPLICIT_SPECTRAL_GATE.

CHAPTER7_PROCESS_BOUNDARY = PASS_WITH_CURRENT_TWO-ENDPOINT_SCOPE.

CHAPTER7_SPECTRAL_BOUNDARY = PASS_AFTER_OPERATOR-HYPOTHESIS_INSERTION.

THEOREMS_7_1_TO_7_3 = RETAIN.

BLOCKING_SCIENTIFIC_GAP = NONE.

NEW_RESEARCH_REQUIRED_NOW = NO.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_TASK.
