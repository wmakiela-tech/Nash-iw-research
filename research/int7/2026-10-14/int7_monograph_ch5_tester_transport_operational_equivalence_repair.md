# INT7 — Chapter 5.11 tester-transport and operational-equivalence repair
RETURN_ID: INT7-MONOGRAPH-CH5-TESTER-TRANSPORT-OPERATIONAL-EQUIVALENCE-REPAIR-001_20261014

## Verdict

PASS_WITH_MAP_TYPING_REPAIR / NO THEOREM REMOVAL / BLOCKING_GAP=NONE.

The current §5.11 correctly states that equality of process laws is relative to a declared family of instruments and does not identify microscopic environments. One load-bearing map is still implicit: when two models have different legal tester spaces, their process laws cannot be compared until a transport between tester spaces is declared.

This repair makes that map explicit and turns the final open paragraph into a precise existence problem.

## 1. Typed process-law comparison

Let

- \(\mathcal E_1,\mathcal E_2\) be the legal tester/instrument classes of two models;
- \(\mathcal P\) be a common outcome-law space, e.g. probability distributions on a declared common outcome alphabet;
- \(\mathcal T_1:\mathcal E_1\to\mathcal P\);
- \(\mathcal T_2:\mathcal E_2\to\mathcal P\).

If \(\mathcal E_1=\mathcal E_2\), then the statement
\[
\mathcal T_1=\mathcal T_2
\]
is well typed.

If \(\mathcal E_1\neq\mathcal E_2\), one first needs a legal tester transport
\[
F:\mathcal E_1\to\mathcal E_2.
\]

The correct relative comparison is then
\[
\mathcal T_1=\mathcal T_2\circ F.
\]

Call this **\(F\)-relative operational equivalence**.

Without \(F\), writing \(\mathcal T_1=\mathcal T_2\) across different tester spaces is not a false statement; it is an ill-typed statement.

## 2. Fiber criterion

If \(F(e)=F(e')\), then any factorization
\[
\mathcal T_1=\mathcal T_2\circ F
\]
forces
\[
\mathcal T_1(e)=\mathcal T_1(e').
\]

Therefore a necessary condition for transport through \(F\) is:

\[
F(e)=F(e')\Longrightarrow \mathcal T_1(e)=\mathcal T_1(e').
\]

Equivalently, \(\mathcal T_1\) must be constant on fibers of \(F\).

Conversely, as a set-theoretic statement, if \(\mathcal T_1\) is constant on fibers of \(F\), then it factors uniquely through the image \(F(\mathcal E_1)\):
\[
\mathcal T_1=\widetilde{\mathcal T}_2\circ F,
\qquad
\widetilde{\mathcal T}_2:F(\mathcal E_1)\to\mathcal P.
\]

This does **not** yet prove that \(\widetilde{\mathcal T}_2\) extends to a legal quantum process on all of \(\mathcal E_2\). CP, normalization, causal-order and source-admission conditions remain separate.

Hence:

TESTER-FIBER CONSTANCY = SET-THEORETIC FACTORIZATION GATE.

TESTER-FIBER CONSTANCY != PHYSICAL PROCESS REALIZABILITY.

## 3. Minimal separator A — noninjective tester transport

Let
\[
\mathcal E_1=\{a,b\},\qquad \mathcal E_2=\{x\},
\]
and let \(F(a)=F(b)=x\).

If
\[
\mathcal T_1(a)\neq\mathcal T_1(b),
\]
then no law \(\mathcal T_2\) can satisfy
\[
\mathcal T_1=\mathcal T_2\circ F.
\]

Thus a proposed change of frame/reduction/tester map can fail before any CP or Choi condition is examined: it may identify testers that the source process distinguishes.

This is the exact process-law analogue of failure of projectability under a quotient.

## 4. Minimal separator B — nonsurjective tester transport

Let
\[
\mathcal E_1=\{a\},\qquad
\mathcal E_2=\{x,y\},
\]
with \(F(a)=x\).

Suppose
\[
\mathcal T_1(a)=\mathcal T_2(x).
\]

Then \(F\)-relative operational equivalence holds on the transported tester image, but \(\mathcal T_2(y)\) is unconstrained.

Therefore:
\[
\mathcal T_1=\mathcal T_2\circ F
\]
does not imply full operational equivalence when \(F\) is not surjective.

An additional legal tester in model 2 may distinguish realizations that are identical on the transported image.

Hence:

AGREEMENT ON TRANSPORTED TESTERS != FULL TESTER-CLASS EQUIVALENCE.

## 5. When does tester transport support full equivalence?

A sufficient clean case is a bijection
\[
F:\mathcal E_1\overset{\sim}{\to}\mathcal E_2
\]
together with
\[
\mathcal T_1=\mathcal T_2\circ F.
\]

Then the two process laws are operationally equivalent relative to the declared relabeling/transport of all legal testers.

Even this does not imply:
- identical environment Hilbert spaces;
- identical microscopic carriers;
- identical Hamiltonians;
- identical internal memory realization.

Thus:

BIJECTIVE TESTER-LAW EQUIVALENCE != MICROSCOPIC REALIZATION IDENTITY.

This is the Chapter 5 process analogue of Chapter 3's distinction between response equivalence, similarity, shared component and physical-carrier identity.

## 6. Interaction with §5.10

The correct order is:

1. declare the source and target process/tester types;
2. declare tester transport \(F\), if tester spaces differ;
3. test fiber constancy / linear-relation compatibility on transported data;
4. seek one linear or affine extension;
5. impose CP / Choi positivity;
6. impose the correct normalization and causal constraints for the selected higher-order map class;
7. only then call the map a legal physical transformation.

Therefore:
TYPE/MAP LEGALITY precedes CHOI FEASIBILITY.

A Choi feasibility problem cannot repair an undefined comparison between distinct tester spaces.

## 7. Ready-to-paste repair for §5.11

Suggested insertion after the first paragraph:

> Jeżeli dwa modele mają tę samą legalną klasę testerów \(\mathcal E\), równość ich funkcjonałów procesu \(\mathcal T_1,\mathcal T_2:\mathcal E\to\mathcal P\) jest dobrze typowanym pojęciem operacyjnej nierozróżnialności. Gdy klasy testerów są różne, \(\mathcal E_1\neq\mathcal E_2\), przed porównaniem trzeba zadeklarować legalny transport testerów \(F:\mathcal E_1\to\mathcal E_2\). Wtedy właściwym warunkiem jest \(\mathcal T_1=\mathcal T_2\circ F\). Warunek ten wymaga, aby \(\mathcal T_1\) było stałe na włóknach \(F\). Jeżeli \(F\) nie jest surjektywne, zgodność na obrazie \(F(\mathcal E_1)\) nie rozstrzyga odpowiedzi na dodatkowe testery modelu drugiego; jeżeli \(F\) nie jest iniektywne, może już na poziomie praw wyników identyfikować testery, które model pierwszy rozróżnia. Dopiero bijektywny transport całej klasy testerów wraz z równością praw daje pełną operacyjną równoważność względem tego transportu, nadal bez identyfikacji mikroskopowej realizacji.

Suggested replacement of the current open problem:

> **Problem otwarty.** Dla dwóch skonkretyzowanych modeli o legalnych klasach testerów \(\mathcal E_1,\mathcal E_2\) należy najpierw skonstruować lub wykluczyć legalny transport testerów \(F:\mathcal E_1\to\mathcal E_2\). Następnie trzeba sprawdzić, czy prawa źródłowe są stałe na włóknach \(F\), czy indukowana mapa na obrazie \(F(\mathcal E_1)\) dopuszcza liniowe przedłużenie oraz czy istnieje jedno przedłużenie spełniające całkowitą dodatniość, właściwą normalizację i warunki przyczynowe wybranej klasy transformacji. Jeżeli któryś etap zawodzi, należy wskazać pierwszy zawiedziony poziom: typ transportu testerów, projektowalność na włóknach, zgodność liniowa, CP, przyczynowość/normalizacja albo ograniczenie źródłowe klasy testerów.

## 8. Firewalls

SAME PROCESS SYMBOL != SAME TESTER DOMAIN.

DIFFERENT TESTER SPACES REQUIRE A DECLARED TESTER MAP.

FIBER CONSTANCY != CP REALIZABILITY.

AGREEMENT ON TRANSPORTED TESTERS != FULL OPERATIONAL EQUIVALENCE.

BIJECTIVE OPERATIONAL EQUIVALENCE != SAME MICROSCOPIC CARRIER.

PROCESS SUPERMAP != TESTER TRANSPORT BY DEFAULT.

## Status

CHAPTER5_5.11 = PASS_WITH_MAP_TYPING_REPAIR.

NEW_THEOREM_CLAIM = NONE; the factorization statements are elementary set/linear-map structure.

BLOCKING_SCIENTIFIC_GAP = NONE.

NEW_RESEARCH_REQUIRED_NOW = NO.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
