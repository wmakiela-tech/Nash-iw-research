# REC9 — Chapter 7 single spectral multiplier quantifier referee

**RETURN_ID:** REC9-LT4-CH7-SINGLE-SPECTRAL-MULTIPLIER-QUANTIFIER-REFEREE-001_20261017  
**CELL:** IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_08 / Rec9  
**CLASS:** CLAIM-LOCAL STRESS / TYPE / HARDEN  
**VERDICT:** PASS_BOTH_WITH_QUANTIFIER_REPAIR  
**SEVERITY:** MEDIUM  
**AUTHORITY:** NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_NEW_TASK

## Objects reviewed

1. INT7: `INT7-MONOGRAPH-CH7-SAME-MULTIPLIER-VS-SPECTRAL-AND-CHAIN-TRANSPORT-001_20261017`  
   GitHub commit: `286f38ae32f57f19cc4df2dd2c2e6a04df430dd3`  
   blob: `59418ce8d2ca3f91eb922b09ff59a3bc5e2b8412`

2. MT13: `MT13-CH7-SINGLE-INJECTIVE-SPECTRAL-MULTIPLIER-GATE-001_20261017`  
   GitHub blob at review: `ddc0ba448bb9a1858adb362f00af04c5d4e4eda8`

## Core issue

INT7 correctly proves that:
- merely writing the same scalar multiplier on two operators defines no transport;
- a noninjective single multiplier can collapse distinct spectra;
- spectral transport and chain transport are separate contracts.

MT13 correctly observes that the phrase "one multiplier does not suffice" cannot be universal.

The exact distinction is not **one function versus many functions**.

The exact distinction is:

[
oxed{	ext{SPECTRALLY SEPARATING WITNESS} quad 	ext{vs} quad 	ext{NONSEPARATING WITNESS}.}
]

## Exact theorem

Let (Age 0) and (Bge 0) be self-adjoint on Hilbert spaces (H_1,H_2), let (Jinmathcal B(H_1,H_2)), and let (t_*>0).

If
[
J e^{-t_*A}=e^{-t_*B}J,
]
then for every bounded Borel (m:[0,infty)	omathbb C),
[
Jm(A)=m(B)J.
]

Reason:
- (h(lambda)=e^{-t_*lambda}) is injective on ([0,infty));
- (T=h(A)), (S=h(B)) are bounded self-adjoint contractions;
- (JT=SJ) implies intertwining of the bounded Borel functional calculi of (T,S);
- for bounded Borel (m), define (g(u)=m(-log u/t_*)) for (u>0), arbitrary at (u=0);
- (E_T({0})=E_S({0})=0), since exponentials of self-adjoint operators have trivial kernel;
- hence (m(A)=g(T)), (m(B)=g(S)).

More generally, one bounded real Borel function (h) suffices when it is injective on a Borel set containing
[
sigma(A)cupsigma(B)
]
(or, equivalently for the present purpose, when one common Borel inverse exists on the relevant spectral images).

The **union-spectrum** condition is load-bearing. Injectivity only separately on each spectrum is not enough if values can collide across the two spectra.

## What INT7's counterexample proves

INT7 uses
[
A=operatorname{diag}(0,1),quad
B=operatorname{diag}(0,3),quad
h(lambda)=cos(pilambda),
]
so
[
h(A)=h(B)=operatorname{diag}(1,-1)
]
while (A
e B).

This is correct and proves:

[
oxed{	ext{ARBITRARY / NONSEPARATING ONE-MULTIPLIER AGREEMENT}

otRightarrow
	ext{GENERATOR IDENTIFICATION}.}
]

It does **not** prove:

[
oxed{	ext{NO SINGLE MULTIPLIER CAN EVER DETERMINE THE SPECTRAL CALCULUS}.}
]

The latter is false.

## Required wording repair

The following absolute firewall is too broad if read literally:

> ONE MULTIPLIER AGREEMENT != GENERATOR EQUIVALENCE.

Replace by one of:

> ARBITRARY ONE-MULTIPLIER AGREEMENT DOES NOT IN GENERAL IMPLY GENERATOR EQUIVALENCE.

or, more sharply:

> NONSEPARATING ONE-MULTIPLIER AGREEMENT DOES NOT IDENTIFY THE GENERATORS.

Add the complementary positive statement:

> A SINGLE SPECTRALLY SEPARATING MULTIPLIER, together with a declared bounded intertwiner, can already determine the full bounded Borel spectral transport. For nonnegative self-adjoint generators, (e^{-tA}) at any one fixed (t>0) is such a witness.

## Important remaining nonimplications

Even after the MT13 strengthening:

[
	ext{ONE SEPARATING MULTIPLIER INTERTWINING}
Rightarrow
	ext{FULL BOUNDED BOREL SPECTRAL INTERTWINING},
]

but still:

[
	ext{FULL SPECTRAL INTERTWINING}

otRightarrow
	ext{CHAIN ISOMORPHISM},
]

[
	ext{FULL SPECTRAL INTERTWINING}

otRightarrow
	ext{EXACT-BOUNDARY TRANSPORT},
]

[
	ext{FULL SPECTRAL INTERTWINING}

otRightarrow
	ext{MULTI-TIME PROCESS EQUIVALENCE},
]

[
	ext{FULL SPECTRAL INTERTWINING}

otRightarrow
	ext{MICROSCOPIC CARRIER IDENTITY}.
]

For exact filtered-boundary transport, INT7's independent chain/domain/surjectivity requirements remain intact.

Also:
- bounded (J) is part of the present theorem;
- unbounded intertwiners require explicit domain control;
- full bounded Borel intertwining is an operator-transport statement, not automatically equality of unbounded generators unless stronger conditions on (J) and domains are imposed;
- if (J) is not bijective, "generator equivalence" remains too strong even though spectral intertwining holds.

## Recommended LT4 insertion

Suggested precision sentence:

> Liczba sprawdzonych mnożników nie jest sama w sobie kryterium siły transportu. Pojedynczy mnożnik nierozdzielający widma może utożsamiać różne generatory, natomiast pojedynczy mnożnik rozdzielający odpowiednie wspólne widmo — na przykład (e^{-tlambda}) dla (t>0) i nieujemnych operatorów samosprzężonych — wraz z ograniczonym splataczem wyznacza pełny ograniczony borelowski transport spektralny. Nie usuwa to osobnego wymogu transportu łańcuchowego, dziedzin i rzeczywistych przestrzeni brzegów.

## Final disposition

`INT7_CORE_TRANSPORT_ANALYSIS=PASS`  
`INT7_ABSOLUTE_ONE_MULTIPLIER_FIREWALL=REPAIR_QUANTIFIER`  
`MT13_INJECTIVE_MULTIPLIER_THEOREM=PASS_EXACT`  
`SPECTRAL_SEPARATION_NOT_MULTIPLIER_COUNT=CONTROLLING_DISTINCTION`  
`CHAIN_TRANSPORT_REQUIREMENT=UNCHANGED`  
`PROCESS_EQUIVALENCE_NONIMPLICATION=UNCHANGED`  
`BLOCKING_SCIENTIFIC_GAP=NONE`  
`NOVELTY_CANDIDATE=NONE`  
`NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK`

This closes the apparent INT7–MT13 tension as a quantifier/typing repair, not a scientific contradiction.
