# INT7 audit — Chapter 2: Reduction, observables, and stability of effective description

RETURN_ID: INT7-MONOGRAPH-CHAPTER2-MAP-BOUNDARY-AND-TRANSITION-AUDIT-001
DATE: 2026-10-13
IN_REPLY_TO: LT4-MONOGRAPH-CHAPTER2-TARGET-FACTOR-CONTINUITY-AND-ROUTED-REVIEW-001_20261013
BW_STATUS: PENDING_INGEST
CLASS: BOOK AUDIT / SCIENTIFIC INTEGRATION / NO NEW RESEARCH
VERDICT: PASS_WITH_REPAIRS
STATUS: NO NOVELTY CLAIM / NO THEORY PROMOTION

## 1. Executive verdict

Chapter 2 is scientifically coherent and should remain directly after the exact elimination/memory chapter.

Its strongest feature is that it does not collapse the following into one operation:

- elimination of a hidden sector in one dynamical realization;
- set-theoretic reduction of realizations;
- dynamical projectability;
- target autonomy;
- bounded recovery of a target;
- quantum partial trace;
- stochastic garbling of observation laws;
- cross-context shared realization.

The current order is broadly correct:

exact elimination in Chapter 1
-> target factorization
-> process projectability
-> stability/robustness
-> quantum example
-> probability-law example
-> cross-context join
-> transition to transport of structures.

No blocking research is required.

The chapter should be accepted with local repairs that make the changes of object type explicit.

## 2. Section 2.1 — PASS, but add a scope-switch paragraph

The move from Chapter 1 to Chapter 2 is mathematically legitimate, but editorially abrupt.

Chapter 1 works with a specific linear realization and operators P,J,Q.
Chapter 2 starts with an arbitrary set map r:X->Y.

A reader may incorrectly infer that r is a generalization of the same physical compression mechanism.

Recommended insertion at the end of the opening paragraph of 2.1:

"Od tego miejsca symbol r nie oznacza już konkretnej kompresji operatorowej z rozdziału 1. Jest abstrakcyjną mapą redukcji zadeklarowanej klasy realizacji. Twierdzenia tego rozdziału określają, co wynika z samej struktury włókien, topologii i metryki; zastosowanie ich do konkretnej eliminacji fizycznej wymaga osobnego sprawdzenia, że dana konstrukcja rzeczywiście definiuje taki r."

This one paragraph prevents the strongest possible false identification between Chapters 1 and 2.

## 3. Sections 2.1–2.3 — PASS

Theorem 2.1 correctly separates target factorization from continuity, stability, dynamics, and measurement realizability.

The set-valued target object in 2.2 is the correct replacement when exact factorization fails.

The quotient-topology theorem in 2.3 is correctly scoped.

The example [0,2pi)->S1 is useful because it demonstrates:

algebraic uniqueness of the descended function
!=
continuity of the descended function.

No mechanism-level repair is needed here.

## 4. Section 2.4 — PASS_WITH_CLARIFYING_DISPLAY

This is the conceptual center of Chapter 2 and already contains the right distinctions.

Three different claims should be displayed explicitly as three different diagrams/conditions:

A. REDUCED-STATE PROJECTABILITY

r U_t = V_t r.

B. TARGET PREDICTABILITY FROM THE REDUCED STATE

tau U_t = g_t r.

C. AUTONOMY OF THE TARGET ITSELF

tau U_t = W_t tau.

These satisfy different fiber conditions.

The current prose explains this correctly, but a boxed three-level display would reduce later ambiguity.

Critical firewall to print once:

REDUCED STATE AUTONOMY
!=
TARGET PREDICTABILITY FROM REDUCED STATE
!=
TARGET AUTONOMY.

The examples 2.2 and 2.3 are well chosen and should remain.

The final reference back to K(t)=0 is also correctly scoped as a special criterion from Chapter 1, not a general definition.

## 5. Section 2.5 — PASS_WITH_PROOF-TYPING REPAIR

Theorem 2.4 is mathematically well placed and provides the exact transition from identifiability to stable bounded recovery.

The equivalence

T=SP with bounded S on closure(ran P)

iff

||Tx|| <= C ||Px||

is correct.

The closed-range corollary is also correct, but the proof should be typed more explicitly.

Current wording compresses two quotient operations into the phrase
"P:X/ker P -> ran P".

Recommended proof wording:

"Operator P induces a bounded bijection
P_tilde:X/ker P -> ran P.
Because ran P is closed, it is Banach; hence P_tilde^{-1} is bounded by the bounded inverse theorem. Since ker P subset ker T, T induces a bounded operator
T_tilde:X/ker P -> Z.
Therefore S_0=T_tilde P_tilde^{-1}:ran P->Z is bounded."

This is not a change of theorem, only a domain/codomain repair.

The diagonal l2 counterexample is exactly appropriate.

## 6. Section 2.6 — PASS

The modulus

omega(delta)=sup{d_Z(tau(x),tau(x')): d_Y(r(x),r(x'))<=delta}

is the right object for separating exact descent from robust descent.

The diameter bound by omega(2 epsilon) is exact.

The compactness theorem is correctly formulated for compact metric X and continuous r,tau.

The x^3 example correctly gives

omega(delta)=(4 delta)^(1/3)

for 0<=delta<=2.

The chapter already contains the essential warning that the metrics must correspond to the physical error contract.

Recommended editorial sentence:

"Moduł omega jest własnością trójki (r,tau,metryki), nie samej redukcji r."

This prevents omega from being read as an intrinsic quality number of the model.

## 7. Section 2.7 — QUANTUM EXAMPLE PASS, with a type firewall

The Bell-state example is correct and useful:

same reduced local state
does not determine
a nonlocal correlation observable.

The section also correctly states that partial trace is not the amplitude compression PTJ from Chapter 1.

This distinction should be elevated into a boxed type firewall:

AMPLITUDE COMPRESSION:
maps state-vector carriers / retained subspaces in the Chapter-1 setup.

PARTIAL TRACE:
maps density operators on a tensor-product system to density operators on a subsystem and is CPTP.

Neither operation is the generic set-theoretic reduction r merely by notation.

Recommended small notation repair:
avoid a bare D(H_A tensor H_B) if D may be confused with an operator domain elsewhere in the book; use an explicit symbol such as
S(H_A tensor H_B)
or
Dens(H_A tensor H_B)
and define it once.

No new quantum result is needed.

## 8. Section 2.8 — PASS, but separate statistical garbling from physical reduction

The law-versus-support distinction is correct.

The TV data-processing inequality under a parameter-independent Markov kernel is correctly used.

The prose already says stochastic information reduction and Hilbert-sector elimination are different operations.

Recommended stronger transition sentence before the Blackwell paragraph:

"Przechodzimy teraz do innego typu nośnika: obiektem redukowanym nie jest stan fizyczny ani jego współrzędna, lecz prawo obserwacji."

This prevents a reader from interpreting the Markov kernel K as the same kind of object as the memory kernel K(t) from Chapter 1.

Because the same letter K is used in two mature theories with unrelated typing, I recommend changing the Markov kernel symbol to M or mathcal K in Chapter 2.

This is a notation repair, not a scientific issue.

## 9. Section 2.9 — THREAD094 INTEGRATION PASS

The chapter correctly distinguishes:

FULL SHARED REALIZATION:
intersection only after a common full carrier has been established.

SHARED COMPONENT:
fiber product over the declared component maps.

EXTRA CROSS-CONTEXT LAW:
R intersect fiber product.

TARGET AGREEMENT:
weaker than either shared full realization or shared component.

This matches the corrected Thread094 scope.

Theorem 2.7 is intentionally elementary and should stay that way.
It is useful precisely because it prevents an illegitimate strengthening of the scientific claim.

One addition is now recommended from Thread096:

after Example 2.5, add a short realization-theory bridge:

"If two minimal state-space realizations are equivalent only up to a similarity T, this does not identify their raw internal coordinates. A declared shared component with maps s_1,s_2 is transported along that equivalence only when s_2 T=s_1. Thus uniqueness of a minimal realization up to similarity does not imply uniqueness of an internal physical variable."

Do not reproduce the full Thread096 section here; one paragraph and a forward reference are sufficient.

## 10. Section 2.10 — PASS_WITH_TRANSITION REPAIR

The direction toward a later chapter on transport of structures is correct.

However the phrase "legalny transport danych lub struktur" is still broader than the objects defined in Chapter 2.

Before the next chapter, define what a transport claim must specify.

Recommended closing template:

A transport claim between two descriptions must declare at least:

1. source carrier and target carrier;
2. legal source and target subsets;
3. map/relation between carriers;
4. structure required to be preserved
   (target, dynamics, algebra, probability law, intervention family, etc.);
5. level of equivalence required
   (full object, shared component, target-only, or transportable query).

Then state:

"Without these data, words such as equivalence, representation change, reduction, coarse-graining and duality are not interchangeable."

This creates the correct entry to the planned structural-transport part without asserting one universal category of physical maps.

## 11. Ordering audit: Chapter 1 -> Chapter 2 -> transport chapter

The present order is scientifically preferable to moving the transport material earlier.

Chapter 1 answers:
what exact hidden return is generated by eliminating degrees of freedom in one declared realization?

Chapter 2 answers:
which targets, dynamics and inference statements survive a declared reduction, and with what stability?

Only after these two questions are separated should the book ask:
when can structures be transported between distinct descriptions or contexts?

Therefore the recommended order is:

EXACT ELIMINATION
-> TARGET/PROCESS DESCENT
-> STABILITY
-> TYPE-SPECIFIC EXAMPLES
-> CLAIM-RELATIVE CROSS-CONTEXT JOIN
-> STRUCTURE TRANSPORT.

This order minimizes false analogy.

## 12. Mechanism non-isomorphism audit

The chapter currently passes the requested non-isomorphism audit provided the local repairs above are made.

The following must remain explicit:

SCHUR/FESHBACH ELIMINATION
!=
ABSTRACT FIBER QUOTIENT.

ABSTRACT REDUCTION r
!=
DYNAMICAL PROJECTABILITY.

DYNAMICAL PROJECTABILITY
!=
TARGET AUTONOMY.

BOUNDED TARGET RECOVERY
!=
ALGEBRAIC TARGET FACTORIZATION.

PARTIAL TRACE
!=
AMPLITUDE COMPRESSION.

PARTIAL TRACE
!=
MARKOV GARBLING OF MEASUREMENT LAWS.

LAW GARBLING
!=
HIDDEN-SECTOR ELIMINATION.

FULL SHARED REALIZATION
!=
SHARED COMPONENT FIBER PRODUCT.

SHARED COMPONENT
!=
TARGET AGREEMENT.

MINIMAL-REALIZATION SIMILARITY
!=
IDENTITY OF INTERNAL PHYSICAL VARIABLES.

These are not defects in the chapter; they are the boundaries the chapter is designed to teach.

## 13. Final disposition

CHAPTER2_OVERALL = PASS_WITH_REPAIRS.

BLOCKING_SCIENTIFIC_GAP = NONE.

NEW_RESEARCH_REQUIRED_NOW = NO.

REQUIRED_BEFORE_EDITORIAL_FREEZE:
- add Chapter1->Chapter2 scope-switch paragraph;
- box the three levels in 2.4;
- expand quotient typing in the closed-range part of 2.5;
- add omega depends on (r,tau,metrics);
- strengthen quantum type firewall in 2.7;
- rename/distinguish the Markov kernel in 2.8 from the Chapter-1 memory kernel;
- add one-paragraph Thread096 bridge in 2.9;
- make the transport-data contract explicit in 2.10.

No theorem in Chapter 2 needs to be removed on the basis of this INT7 audit.

No CANON / NO EXEC_SIGN / NO NOVELTY INFERENCE / NO THEORY PROMOTION / NO NEW SCIENCE CAMPAIGN.
