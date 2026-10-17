# INT7 — Chapter 7 / Problem B: same spectral multiplier vs genuine transport

RETURN_ID: INT7-MONOGRAPH-CH7-SAME-MULTIPLIER-VS-SPECTRAL-AND-CHAIN-TRANSPORT-001_20261017

## Scope

Continuation of the direct LT4 Chapter 7 boundary-review request.

This rotation treats exactly one seam:

**Does using the same scalar spectral multiplier \(f\) in two theories define a transport between them, and what extra structure is required to transport exact boundary spaces rather than only spectral formulas?**

Relevant manuscript locations:
- Chapter 4: spectral multipliers, exact images, reduced quotients.
- Chapter 7.8: comparison of mature host theories.
- Chapter 7.9 Problem B: transport between Hilbert complexes with different metrics or boundary conditions.

## Verdict

PASS_WITH_EXPLICIT_CROSS-COMPLEX_TRANSPORT_CONTRACT.

The current manuscript is scientifically safe, but Problem B should make one distinction explicit:

\[
\boxed{\text{SAME SCALAR FUNCTION }f \neq \text{TRANSPORT OF }f(\Delta)}
\]

across different Hilbert complexes.

A legal transport of filtered exact images requires both:

1. a **spectral intertwiner**, and
2. a **chain-level transport** of exact boundaries.

Either one alone is insufficient.

---

## 1. Same formula \(f\) is only syntactic commonality

Let \(A\) on \(H_1\) and \(B\) on \(H_2\) be self-adjoint.

Writing
\[
f(A),\qquad f(B)
\]
with the same scalar Borel function \(f\) does not define a map
\[
H_1\to H_2
\]
and does not imply any relation between the two operators.

There is not even a well-typed equality unless an identification/intertwiner between \(H_1\) and \(H_2\) is supplied.

A one-function coincidence is also too weak to identify generators.

Example on the same carrier:
\[
A=\operatorname{diag}(0,1),\qquad
B=\operatorname{diag}(0,3),
\]
and
\[
f(\lambda)=\cos(\pi\lambda).
\]

Then
\[
f(A)=f(B)=\operatorname{diag}(1,-1),
\]
although
\[
A\neq B,\qquad \sigma(A)\neq\sigma(B).
\]

Hence:

\[
\boxed{\text{ONE MULTIPLIER AGREEMENT} \not\Rightarrow \text{GENERATOR EQUIVALENCE}.}
\]

This is stronger than the trivial constant-multiplier separator because \(f\) is nonconstant.

---

## 2. Spectral transport contract

Let \(A\) and \(B\) be self-adjoint on \(H_1,H_2\), and let
\[
J\in\mathcal B(H_1,H_2).
\]

A genuine spectral transport may be expressed by any standard equivalent strong form, for example:
\[
J E_A(\Omega)=E_B(\Omega)J
\]
for all Borel \(\Omega\), or by resolvent/semigroup intertwining under the usual hypotheses.

Then for every bounded Borel \(f\),
\[
Jf(A)=f(B)J.
\]

This is an operator-transport statement.

It is categorically stronger than merely writing the same function \(f\) on both spectra.

Thus:

\[
\boxed{\text{SAME }f \neq \text{SPECTRAL INTERTWINING}.}
\]

---

## 3. Spectral transport alone does not transport exact boundaries

Now let
\[
(H_1^\bullet,d_1),\qquad (H_2^\bullet,d_2)
\]
be Hilbert complexes with Laplacians
\[
\Delta_1^k,\qquad \Delta_2^k.
\]

Suppose \(J_k:H_1^k\to H_2^k\) spectrally intertwines:
\[
J_k f(\Delta_1^k)=f(\Delta_2^k)J_k.
\tag{S}
\]

This alone does not imply
\[
J_k(\operatorname{ran}d_1^{k-1})
=
\operatorname{ran}d_2^{k-1}.
\]

That is a separate chain-level statement.

To transport exact filtered images one needs a chain map relation:
\[
J_k d_1^{k-1}=d_2^{k-1}J_{k-1}
\tag{C}
\]
on the declared domains, together with enough surjectivity/invertibility to transport the full boundary space rather than only a subspace.

Therefore:

\[
\boxed{\text{SPECTRAL INTERTWINING} \neq \text{CHAIN ISOMORPHISM}.}
\]

and

\[
\boxed{\text{FILTER TRANSPORT} \neq \text{EXACT-IMAGE TRANSPORT}.}
\]

---

## 4. Exact filtered-boundary transport theorem

Assume degreewise bounded bijections
\[
J_k:H_1^k\to H_2^k
\]
such that:

1. \(J_k D(d_1^k)=D(d_2^k)\);
2. \(d_2^k J_k=J_{k+1}d_1^k\) on \(D(d_1^k)\);
3. for a bounded Borel multiplier \(f\),
\[
J_k f(\Delta_1^k)=f(\Delta_2^k)J_k.
\]

Let
\[
B_i^k=\operatorname{ran}d_i^{k-1}.
\]

Then
\[
J_k(B_1^k)=B_2^k,
\]
and moreover
\[
J_k\big(f(\Delta_1^k)B_1^k\big)
=
f(\Delta_2^k)B_2^k.
\tag{T}
\]

### Proof

From the chain-isomorphism relation and bijectivity of \(J_{k-1}\),
\[
J_k(\operatorname{ran}d_1^{k-1})
=
\operatorname{ran}d_2^{k-1}.
\]

Then
\[
\begin{aligned}
J_k\big(f(\Delta_1^k)B_1^k\big)
&=
f(\Delta_2^k)J_k(B_1^k)\\
&=
f(\Delta_2^k)B_2^k.
\end{aligned}
\]

No additional cohomological argument is needed.

This theorem is elementary transport once the two independent contracts — spectral and chain — are both present.

---

## 5. What weakens when bijectivity is removed?

If \(J_{k-1}\) is not onto the relevant source domain, one generally gets only
\[
J_k(B_1^k)\subseteq B_2^k.
\]

Then (S) gives only
\[
J_k\big(f(\Delta_1^k)B_1^k\big)
\subseteq
f(\Delta_2^k)B_2^k.
\]

Equality of filtered exact images therefore requires a surjectivity statement at the boundary level, not merely spectral intertwining.

If a map is only known to transport closures,
\[
J_k(\overline{B_1^k})=\overline{B_2^k},
\]
that certifies only closure-level transport.

It does not imply
\[
J_k(B_1^k)=B_2^k.
\]

Hence the Chapter 4 distinction survives cross-complex transport:

\[
\boxed{\text{CLOSED-RANGE TRANSPORT} \neq \text{EXACT-RANGE TRANSPORT}.}
\]

and

\[
\boxed{\text{REDUCED-COHOMOLOGY COMPATIBILITY} \neq \text{ALGEBRAIC-COHOMOLOGY COMPATIBILITY}.}
\]

---

## 6. Consequence for metric or boundary-condition changes

For two complexes built from different metrics or different boundary conditions, the phrase “apply the same multiplier \(f\)” is insufficient.

One must specify:

1. the carrier map \(J_k\);
2. domain transport for \(d_i\) and any adjoints used in the Laplacians;
3. chain compatibility \(d_2J=Jd_1\);
4. spectral compatibility \(Jf(\Delta_1)=f(\Delta_2)J\), preferably derived from an operator-level intertwining rather than checked for one \(f\);
5. whether \(J\) transports actual boundary ranges or only their closures;
6. whether \(J\) is bijective on the relevant exact sector.

This is especially load-bearing under changed boundary conditions, because the differential expression may be formally the same while operator domains and self-adjoint realizations are different.

Thus:

\[
\boxed{\text{SAME DIFFERENTIAL EXPRESSION} \neq \text{SAME OPERATOR REALIZATION}.}
\]

---

## 7. Recommended replacement for Chapter 7 Problem B

> **Problem B (transport spektralny i łańcuchowy).** Dla dwóch określonych kompleksów Hilberta \((H_1^\bullet,d_1)\), \((H_2^\bullet,d_2)\), związanych zmianą metryki lub warunków brzegowych, należy skonstruować jawne operatory transportu \(J_k\). Samo użycie tej samej funkcji \(f\) w \(f(\Delta_1)\) i \(f(\Delta_2)\) nie stanowi transportu. Trzeba osobno wykazać: (i) zgodność łańcuchową \(d_2J=Jd_1\) wraz z transportem dziedzin; (ii) intertwining odpowiednich realizacji spektralnych, np. \(Jf(\Delta_1)=f(\Delta_2)J\); oraz (iii) surjektywność na rzeczywistych przestrzeniach brzegów, jeśli celem jest zachowanie dokładnych obrazów, a nie jedynie ich domknięć. Dopiero wspólne spełnienie tych warunków pozwala porównywać filtrowane dokładne obrazy między teoriami.

---

## 8. Recommended compact insertion in §7.8

> Użycie tej samej funkcji spektralnej \(f\) w dwóch teoriach nie definiuje jeszcze transportu między nimi. Transport \(f(\Delta)\) wymaga jawnego intertwineru między realizacjami operatorów, a transport dokładnych obrazów dodatkowo wymaga zgodnej mapy łańcuchowej i odpowiedniej surjektywności na przestrzeni brzegów. Zgodność na poziomie domknięć nie może być automatycznie podniesiona do zgodności obrazów algebraicznych.

---

## Firewalls

SAME SCALAR MULTIPLIER != SPECTRAL TRANSPORT.

ONE MULTIPLIER AGREEMENT != GENERATOR EQUIVALENCE.

SPECTRAL INTERTWINING != CHAIN ISOMORPHISM.

FILTER TRANSPORT != EXACT-IMAGE TRANSPORT.

CLOSURE-LEVEL TRANSPORT != EXACT-RANGE TRANSPORT.

SAME DIFFERENTIAL EXPRESSION != SAME CLOSED/SELF-ADJOINT REALIZATION.

## Final status

CHAPTER7_PROBLEM_B = PASS_WITH_EXPLICIT_CROSS_COMPLEX_TRANSPORT_CONTRACT.

CHAPTER4_EXACT_VS_REDUCED_BOUNDARY = PRESERVED.

NO THEOREM REMOVAL.

BLOCKING_SCIENTIFIC_GAP = NONE.

NEW_RESEARCH_REQUIRED_NOW = NO.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_TASK.
