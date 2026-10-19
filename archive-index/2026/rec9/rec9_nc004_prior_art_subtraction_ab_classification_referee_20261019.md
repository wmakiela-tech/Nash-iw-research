# REC9 — independent audit of NC-004 prior-art subtraction and A/B classification

RETURN_ID: REC9-NC004-PRIOR-ART-SUBTRACTION-AB-CLASSIFICATION-REFEREE-001_20261019
CELL: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_08 / Rec9
TARGET: NC-LT4-PRIOR-ART-SUBTRACTION-FULL-MANUSCRIPT-004
NC ARTIFACT: IW_NC_LT4_PRIOR_ART_SUBTRACTION_FULL_MANUSCRIPT_004_20261018
NC DRIVE: 1Ih2uvIgG-LITYCU5aVr7YYvbb2x1aUDm
MANUSCRIPT: "Opisy efektywne w układach fizycznych — monografia robocza — rozdziały 1–7"
MANUSCRIPT DRIVE: 1cn97_kO65BcJRRWQrvrL9fKlEYBT3PHg6BJItn1Q4FQ
CLASS: INDEPENDENT PRIOR-ART / CLAIM-CEILING / A-B SUBTRACTION REFEREE
VERDICT: NC_DIRECTION_PASS / NC_FINAL_B_COUNT_TOO_HIGH / ONE_B_WITNESS_CANDIDATE_REMAINS
SEVERITY: HIGH
AUTHORITY: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_NEW_TASK

## 0. Scope and classification rule

NC explicitly marked its A/B classification as its own judgment and requested independent audit under ANTI-SELF-SEALING.

This audit uses the final corrected NC state, not the superseded eight- or seven-item counts.

NC's own hierarchy-B test is taken literally:
a B item must identify a hypothesis, conclusion, sharpness statement, or counterexample that is not merely a cited mature-host result.

Rec9 applies one additional guard already controlling in the project:

ELEMENTARY DEDUCTION FROM A MATURE HOST
!=
NEW MATHEMATICAL RESULT.

Therefore a useful exact witness can be valuable manuscript material while still remaining hierarchy A in strict mathematical subtraction.

The audited final NC list contains six items:

1. Chapter 1 Theorem 5 + Counterexample 3.
2. Example 2.4a.
3. Theorem 4.4.
4. Theorem 4.5.
5. Example 4.1.
6. Theorem 7.12 + Counterexample 7.4.

## 1. Executive result

NC's overall subtraction direction is correct:
most of the monograph is mature-host mathematics, standard functional analysis, or elementary deduction, and the manuscript itself often labels this honestly.

However, the final count of six B candidates is still too generous if B is read as "mathematical content surviving mature-host subtraction."

Independent classification:

- Theorem 5 + Counterexample 3: A_PLUS_CONTEXTUAL_SHARPNESS.
- Example 2.4a: A.
- Theorem 4.4: B_WITNESS_CANDIDATE / NOVELTY_NOT_ESTABLISHED.
- Theorem 4.5: A_PLUS_DOMAIN_HARDENING.
- Example 4.1: A_PLUS_SHARP_WITNESS.
- Theorem 7.12 + Counterexample 7.4: A_PLUS_SHARP_OPERATOR_WITNESS.

Thus:

STRICT_B_ESTABLISHED = 0.
B_WITNESS_CANDIDATE = 1 (Theorem 4.4).
USEFUL_PROJECT-LEVEL_SHARPNESS_WITNESSES = several.
MATHEMATICAL_NOVELTY_ESTABLISHED = NO.

This does NOT mean only one item is worth keeping. It means only one item remains a plausible B-class contextual counterexample after subtraction, and even that item has no novelty certificate.

---

## 2. Theorem 5 + Counterexample 3 — demote to A_PLUS_CONTEXTUAL_SHARPNESS

### Manuscript object

Theorem 5 states the selected-target exactness criterion

tau R(t)=tau exp(tA)

iff, for large z,

tau (zI-A)^(-1) B (zI-D)^(-1) C = 0.

With an induced target dynamics A_Z satisfying

tau A = A_Z tau,

this reduces to equivalent target-memory conditions

tau B exp(tD) C = 0

and

tau B D^k C = 0.

Counterexample 3 shows that the moment conditions alone fail if ker tau is not A-invariant:
all tau B D^k C vanish, while tau A B C is nonzero.

### Host subtraction

The underlying concepts are mature linear-systems notions:
- selected-output / functional observability,
- transfer-function cancellation for a chosen output,
- invariant-kernel / quotient dynamics,
- disturbance-decoupling logic.

Fernando, Trinh and Jennings (IEEE TAC 55(5), 2010, DOI 10.1109/TAC.2010.2042761) explicitly introduce functional observability/detectability and state that ordinary observability is a special case.

The manuscript theorem packages the hidden-sector memory realization into this selected-target language, but the proof is a resolvent identity plus the standard quotient/intertwining condition tau A=A_Z tau.

Counterexample 3 is a good sharpness witness:
it demonstrates that tau B D^k C=0 does not replace A-invariance of ker tau.

But the witness is an elementary nilpotent finite-dimensional construction, not evidence of a new theorem family.

### Verdict

CH1_THEOREM5 = A_PLUS_HOST_SPECIALIZATION.
CH1_COUNTEREXAMPLE3 = A_PLUS_SHARPNESS_WITNESS.

Do not count this pair as strict B mathematical content.

Editorial value remains HIGH because the example prevents a natural overtransfer error.

---

## 3. Example 2.4a — demote to A

### Manuscript object

For diagonal P,T and source ball K_R, the manuscript proves

||Th||^2 <= ||h|| ||Ph||

and hence

omega_KR(delta)
<=
min(2R, sqrt(2R delta)).

A sequence of basis-vector pairs attains the square-root branch at delta_n=2R/n, showing sharp exponent 1/2 and sharp constant on that sequence.

### Host subtraction

This is exactly the structure of a standard Hilbert-scale interpolation inequality.

A modern Hilbert-scale source states the general interpolation inequality

||f||_{H_r}
<=
||f||_{H_t}^{(s-r)/(s-t)}
||f||_{H_s}^{(r-t)/(s-t)}

and points to Engl–Hanke–Neubauer, Regularization of Inverse Problems, Chapter 8, as the standard host.

The manuscript's sqrt estimate is the elementary diagonal instance of that mechanism.

The attainment sequence is useful and clean, but is obtained immediately from the same diagonal basis.

### Verdict

EXAMPLE_2_4A = A / STANDARD_HILBERT-SCALE_INTERPOLATION_WITH_SHARP_DIAGONAL_WITNESS.

It is a good pedagogical sharpness control, not a surviving B item.

---

## 4. Theorem 4.4 — retain only as B_WITNESS_CANDIDATE

### Manuscript object

The theorem uses the two-step Hilbert complex

d x_n = n x_n

on its natural closed domain and the bounded injective zero-free multiplier

f(Delta)=exp(-Delta).

On the preserved original domain,

d^f x_n = n exp(-n^2) x_n.

The exact range becomes dense but proper.

Hence reduced H^1 remains zero while algebraic H^1 becomes nonzero.

The manuscript also correctly shows that d^f on the preserved domain is not closed, and distinguishes it from its bounded closure on all l2.

### Host subtraction

Brüning–Lesch is the mature host for Hilbert complexes, closed operators, Hodge decomposition, closed-range issues, and the distinction between exact ranges and their closures.

The ingredients used here are standard:
- a diagonal closed unbounded operator,
- multiplication by a bounded injective sequence tending to zero,
- dense nonclosed range,
- reduced quotient using closure versus algebraic quotient using the raw range.

What is not immediately absorbed by the host citation is the exact configuration chosen for the manuscript's question:
a bounded injective zero-free spectral multiplier preserves the reduced cohomology while changing the algebraic cohomology when the original domain is frozen.

I did not find a source in the targeted search giving this exact example/configuration.

But:

SEARCH FAILURE != NOVELTY.

The construction is elementary enough that a novelty claim would be unsafe.

### Verdict

THEOREM_4_4 = B_WITNESS_CANDIDATE / CONTEXTUAL_COUNTEREXAMPLE.

Allowed claim:
"an explicit sharp witness tailored to the monograph's spectral-multiplier question."

Not allowed:
"new theorem in Hilbert-complex theory" or "novel cohomological phenomenon."

This is the strongest survivor of NC's list.

---

## 5. Theorem 4.5 — demote to A_PLUS_DOMAIN_HARDENING

### Manuscript object

For bounded f,g with f(0)=g(0), let j=f-g and h(lambda)=j(lambda)/sqrt(lambda).

Assuming h(Delta_k) bounded, the manuscript defines the bounded homotopy

K_k
=
closure[d_{k-1}^* q(Delta_k)]
=
V_{k-1}^* h(Delta_k) P_clran(d_{k-1})

and proves

F-G = dK + Kd

on the correctly typed domains.

It therefore shows that f(Delta) and g(Delta) induce the same endomorphism on algebraic cohomology of the original complex.

### Host subtraction

The core identity is standard Hodge/Green chain homotopy.

In standard Hodge SDR language one has a Green operator G and homotopy K=d^*G satisfying

[d,K] = I-P_H

(or the corresponding twisted form).

The manuscript replaces the resolvent-like Green factor by a bounded spectral functional-calculus difference and uses the polar decomposition/bounded transform to keep the domain legal.

The normalization by sqrt(lambda) is exactly the half-order compensation expected from d^* relative to Delta.

This domain-safe formulation is careful and worthwhile.

But it is structurally a functional-calculus version of the standard Hodge homotopy mechanism, not a new homotopy principle.

### Verdict

THEOREM_4_5 = A_PLUS_DOMAIN_HARDENING.

Recommended description:
"standard Hodge chain-homotopy mechanism written in a domain-safe spectral multiplier form."

Do not count as strict B.

The manuscript's explicit warning

LITERAL d^* q(Delta) NEED NOT BE EVERYWHERE DEFINED

is valuable negative knowledge and should remain.

---

## 6. Example 4.1 — demote to A_PLUS_SHARP_WITNESS

### Manuscript object

On S^1 and the exact positive-mode sector B,

T_s=exp(-s Delta), T_t=exp(-t Delta), s>t,

the manuscript proves

T_s(B) proper subset T_t(B)

while both closures equal B.

The witness uses b_n=1/n and observes that a T_s preimage of T_t b would require exponentially growing coefficients.

### Host subtraction

This is a direct spectral-calculus consequence of the stronger smoothing at the later heat time.

The general analytic-semigroup/compact-resolvent literature already treats heat operators as immediately smoothing/compact and their range as lying in increasingly regular domains.

In the diagonal eigenbasis used by the manuscript, strictness follows in one line from the exponential weight ratio.

Therefore the mathematical mechanism is standard.

The example remains an excellent witness for the manuscript's exact-range versus closure distinction.

### Verdict

EXAMPLE_4_1 = A_PLUS_SHARP_WITNESS.

Useful to retain.
Not a strict B survivor.

---

## 7. Theorem 7.12 + Counterexample 7.4 — demote to A_PLUS_SHARP_OPERATOR_WITNESS

### Manuscript object

For finite pure-point self-adjoint A,B with

Jh(A)=h(B)J,

the theorem isolates the off-diagonal h-collision part

J_col
=
sum_{lambda_i != mu_j, h(lambda_i)=h(mu_j)}
Q_j J P_i.

It proves

Jm(A)-m(B)J
=
J_col m(A)-m(B)J_col,

hence

||Jm(A)-m(B)J||
<=
2 ||m||_inf ||J_col||,

and full bounded-Borel transport iff J_col=0.

Counterexample 7.4 attains the factor 2 and falsifies the previously proposed "largest single block" replacement.

### Host subtraction

The theorem is correct and the counterexample is strong.

But in finite pure-point form it follows directly from the spectral decomposition identity

Q_j[Jf(A)-f(B)J]P_i
=
[f(lambda_i)-f(mu_j)] Q_j J P_i

plus the operator triangle inequality.

Its conceptual host is the standard spectral theorem / intertwining of normal operators.

The classical Fuglede–Putnam theory is a major mature host for intertwining normal operators; standard treatments extend intertwining to spectral measures/Borel functional calculus.

Theorem 7.12 is a useful finite-dimensional refinement for a noninjective h and fixed J, but its proof is blockwise spectral bookkeeping.

Counterexample 7.4 is particularly valuable because it:
- independently falsifies NC's earlier wrong quantitative bound;
- shows why norm of the collision sum, not max block norm, is the right object;
- attains the constant 2.

That is manuscript hardening, not established mathematical novelty.

### Verdict

THEOREM_7_12 = A_PLUS_FINITE_SPECTRAL_REFINEMENT.
COUNTEREXAMPLE_7_4 = A_PLUS_SHARP_FALSIFIER.

No strict B status.

General continuous-spectrum extension remains OPEN and must not be inferred.

---

## 8. Corrected final A/B state

Using a strict mathematical subtraction standard:

| object | Rec9 classification |
|---|---|
| Ch1 Tw5 + CP3 | A_PLUS_CONTEXTUAL_SHARPNESS |
| Ex2.4a | A |
| Tw4.4 | B_WITNESS_CANDIDATE / novelty not established |
| Tw4.5 | A_PLUS_DOMAIN_HARDENING |
| Ex4.1 | A_PLUS_SHARP_WITNESS |
| Tw7.12 + CP7.4 | A_PLUS_SHARP_OPERATOR_WITNESS |

Therefore:

NC_FINAL_B_COUNT_6 = REJECT_AS_TOO_HIGH.

REC9_STRICT_B_ESTABLISHED_COUNT = 0.

REC9_B_WITNESS_CANDIDATE_COUNT = 1.

The distinction matters:
"candidate B witness" means a tailored counterexample not yet absorbed by a directly located host formulation.
It does NOT mean novel mathematics.

If the project's hierarchy B explicitly counts original contextual sharpness witnesses even when the theorem mechanism is elementary, then Tw4.4 can remain B.
If B is meant to mean mathematical surplus beyond mature hosts, even Tw4.4 should remain unpromoted.

---

## 9. Citation-gap currentness audit

A fresh read of the current monograph still gives zero literal occurrences for:

Douglas
Fernando
Trinh
Jennings
Dahlquist
Söderlind
Lozinskii
Fuglede
Putnam
Rosenblum
Liljegren
Heinkenschloss
Antoulas
Stinespring
Oden
Prudhomme

So NC's main citation-gap diagnosis remains current at this readback.

But citation absence must not be interpreted as novelty.

Recommended host placements by claim type:

- Tw2.4: Douglas factorization/majorization.
- Tw5/CP3: functional observability / output-specific observability.
- Ex2.4a: Hilbert-scale interpolation / inverse-problem conditional stability.
- Tw4.4–4.5: Brüning–Lesch Hilbert complexes + Hodge/Green homotopy/polar decomposition host.
- Tw6.7–6.8: model-error / adjoint representation host including Oden–Prudhomme; DWR bibliography where applicable.
- Tw7.12: Fuglede–Putnam / normal-operator intertwining and spectral measures.
- candidate history-Gramian additions: Heinkenschloss–Reis–Antoulas / Liljegren-Sailer.
- log-norm sharpening if retained: Dahlquist/Lozinskii/Söderlind.
- channel dilation context where needed: Stinespring.

No bibliography insertion is performed by Rec9; this report only fixes the scientific placement.

---

## 10. Audit of NC's frame-level conclusion

NC's larger conclusion survives with a repair.

PASS:
The monograph's strongest distinctive value is not a large set of mathematically new theorems.

PASS:
Its repeated strength is disciplined typing of non-maps, exact failure witnesses, and explicit boundaries between:
- state and target sufficiency,
- exact range and closed range,
- spectral transport and chain transport,
- state/channel equivalence and process equivalence,
- source-level and endpoint-level claims.

REPAIR:
The raw count "53 non-maps versus 6 B candidates" is not itself a scientific quality metric.
Counts depend on editorial granularity, duplicated formulations, and the lexical definition of a non-map.

Therefore the safe frame is not:

NONMAP COUNT >> THEOREM COUNT => ATLAS IS ORIGINAL.

The safe frame is:

A CLAIM-LOCAL ATLAS OF TRANSFER FAILURES MAY BE THE MANUSCRIPT'S MOST DEFENSIBLE DISTINCTIVE CONTRIBUTION,
provided each non-map has:
1. a typed source and target category,
2. an explicit witness or theorem,
3. a mature-host subtraction,
4. a scope statement,
5. no duplicated counting of the same obstruction under different vocabulary.

This is a strong manuscript strategy, but originality of the atlas as a whole still requires literature-level comparison against review/survey traditions.

---

## 11. Final status

NC004_SUBTRACTION_DIRECTION = PASS.

NC004_INITIAL_8_B = SUPERSEDED.
NC004_FINAL_6_B = TOO_HIGH UNDER STRICT MATHEMATICAL SUBTRACTION.

CH1_TW5_CP3 = A_PLUS_CONTEXTUAL_SHARPNESS.
EX2_4A = A.
TW4_4 = B_WITNESS_CANDIDATE / NOVELTY_NOT_ESTABLISHED.
TW4_5 = A_PLUS_DOMAIN_HARDENING.
EX4_1 = A_PLUS_SHARP_WITNESS.
TW7_12_CP7_4 = A_PLUS_SHARP_OPERATOR_WITNESS.

STRICT_NEW_MATHEMATICS_FROM_SIX = NOT_ESTABLISHED.
MATHEMATICAL_NOVELTY_CLAIM = HOLD/NO.

MANUSCRIPT_HARDENING_VALUE = HIGH.
NONMAP_ATLAS_FRAME = PLAUSIBLE / REQUIRES WHOLE-ATLAS PRIOR-ART COMPARISON BEFORE ORIGINALITY CLAIM.

ANTI_SELF_SEALING_OBLIGATION_FOR_NC004 = CLOSED_BY_REC9_FOR_THE_SIX-ITEM_FINAL_CLASSIFICATION.

NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK.

STOP this subtraction seam unless:
- LT4 changes the six objects materially,
- DS/MT13 supplies a contrary host classification with source evidence,
- or a direct prior-art match/nonmatch is found for the exact Theorem 4.4 witness.
