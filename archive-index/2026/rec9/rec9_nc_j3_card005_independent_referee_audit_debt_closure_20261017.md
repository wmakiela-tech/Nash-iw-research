# REC9 — NC J3 card 005 independent referee and audit-debt closure

RETURN_ID: REC9-NC-J3-CARD005-INDEPENDENT-REFEREE-AND-AUDIT-DEBT-CLOSURE-001_20261017
CELL: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_08 / Rec9
CLASS: CLAIM-LOCAL STRESS / TYPE / HARDEN
VERDICT: PASS_AFFINE_CLOSED_FORM / REJECT_NECESSITY_OVERCLAIM / ACCEPT_INT7_AUDIT_WITH_SCOPE
SEVERITY: HIGH
AUTHORITY: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_TASK

## Trigger

NC explicitly reported an anti-self-sealing dependency: its Dorau–Much NCDG nonmap section used NC card 005 §1.2 as an unaudited premise. The highest-leverage disputed statement was that J3 closure requires BOTH commutation of F with Lie transport and idempotence F^2=F.

A previously unrouted independent INT7 audit was found in Drive:

INT7-NC-J3-SEVEN-ARTIFACT-INDEPENDENT-AUDIT-001_20261017
Drive ID: 107hPjXTAp73uY710C0DP3fBt7kL7oefNCfSyzNwq5Vk
Revision at Rec9 readback:
AHj4eMRhZ32doFv4kwGoFAmPGrX21AIXvI7bCG93RsqqI9f7Usvquh1wYTf1RTsJ0_hfzTMUOEKoy522T0WwZCC1HJ-i6Y0I03-uMHgqkcQ

INT7 independently reconstructed the algebra, did not import NC code, and reports independent exact checks in SymPy and Wolfram Language.

Rec9 separately re-derived the load-bearing algebra below rather than treating INT7 as a second authority by assertion.

## 1. Definitions

Let

T_c = L_c F

and assume the undeformed generators form the declared representation

[L_1,L_2] = L_12.

Define

J_F = T_1 T_2 - T_2 T_1 - T_12.

Thus

J_F = L_1 F L_2 F - L_2 F L_1 F - L_12 F.

## 2. General exact identity

Using

F L_i = L_i F + [F,L_i],

we get

L_1 F L_2 F
= L_1 L_2 F^2 + L_1 [F,L_2] F,

and similarly

L_2 F L_1 F
= L_2 L_1 F^2 + L_2 [F,L_1] F.

Therefore

J_F
= (L_1[F,L_2] - L_2[F,L_1])F
  + L_12(F^2-F).

This is exact.

Equivalently, write Q=F-I. Then

L_1 F L_2 F
= L_1 L_2 F + L_1 Q L_2 F,

L_2 F L_1 F
= L_2 L_1 F + L_2 Q L_1 F,

hence the undeformed representation identity cancels the first pair and

J_F
= L_1 Q L_2 F - L_2 Q L_1 F.

Therefore closure is exactly the equality

L_1 Q L_2 F = L_2 Q L_1 F

for the declared generator family.

This can occur by commutation/idempotence, but also by cancellation, range invisibility, quotient collapse, generator collapse, or other representation-relative mechanisms.

## 3. Affine closed form

For the affine multiplier

E = I + a B,

take Q=aB. Then

J_E
= a (L_1 B L_2 - L_2 B L_1) E.

Define

M = L_1 B L_2 - L_2 B L_1.

Thus

J_E = a M E
    = a M + a^2 M B.

Applied to h:

J3(h) = a M (I+aB) h.

With B=Box this is exactly the NC/INT7 form

J3 = a M (1+a Box) h.

SIGN CHECK: PASS EXACT.

No higher powers of a occur for this affine E.

Therefore NC's strongest algebraic result 001 survives the independent audit.

## 4. Exact 2x2 counterexample to necessity

Take

A = [[1,0],[0,0]],
B = [[0,1],[0,0]],

so

[A,B] = B.

Let

F = diag(1,gamma),

with gamma != 0,1.

Then

T_A = A F = A,

T_B = B F = gamma B,

T_[A,B] = B F = gamma B.

Hence

[T_A,T_B]
= gamma [A,B]
= gamma B
= T_[A,B].

Therefore

J_F = 0 exactly.

But

F^2 != F

for gamma != 0,1,

and

[F,B] = (1-gamma) B != 0.

Thus closure occurs while BOTH proposed necessary conditions fail.

This is an exact algebraic falsifier.

Therefore:

CLOSURE REQUIRES [F,L_c]=0 AND F^2=F = REJECT.

The pair remains a strong sufficient mechanism, not a necessary one.

## 5. Zero-free entire strengthening

INT7 gives a stronger legal example on S1:

rho_C u = (C u)',
Delta = -d^2/dx^2,

s(z) = sin(pi sqrt(z))/(pi sqrt(z)),
with s(0)=1 and s(n^2)=0 for n != 0.

Hence s(Delta)=P0, projection onto constants.

For gamma>0, gamma!=1 define

f(z) = exp((log gamma) s(z)).

This is entire and zero-free, with

F=f(Delta)=I+(gamma-1)P0.

Because every rho_C u has zero mean,

F rho_C = rho_C.

For T_C=rho_C F,

T_C T_D
= rho_C F rho_D F
= rho_C rho_D F,

and therefore

[T_C,T_D]
= [rho_C,rho_D]F
= T_[C,D].

So J_F=0 exactly even though generally

F^2 != F
and
[F,rho_C] != 0.

Therefore the stronger universal statement

NO NONTRIVIAL ZERO-FREE ENTIRE f(Delta) CAN CLOSE

is also false.

This directly reinforces earlier Geeky-S10 closure mechanisms and is compatible with the existing negative knowledge:
ORIGINAL REPRESENTATION FAITHFUL != DEFORMED EXPERIMENT FAITHFUL;
carrier-null and generator-quotient mechanisms must be typed separately.

## 6. Consequence for NC card 005

Retain:
- affine closed form J3 = a M (I+a Box) h;
- general commutator identity;
- specific examples where exp(a Delta) gives nonclosure;
- full-dilation scaling law only under its declared path;
- Lorentzian/Gaussian threshold only under its declared two-insertion tail contract;
- spectral-blindness / bandwidth mechanism with its low-saturation scope.

Repair / reject:
- commutation + idempotence as NECESSARY closure conditions;
- class-wide claim that every nontrivial entire or zero-free-entire multiplier must break closure;
- any downstream argument using such a universal theorem.

Keep open:
- Paper-1 same-source N=41 reproduction;
- causal attribution of the observed sigma plateau to domain truncation;
- original sigma-only asymptotic question where not all scales are dilated.

## 7. Consequence for Dorau–Much / NCDG downstream use

INT7's downstream repair is correct and Rec9 accepts it:

DORAU_MUCH_TO_NCDG = NO_CURRENT_LEGAL_MAP

because the project currently lacks the typed bulk-to-horizon carrier map, deformation relation/intertwiner, state/algebra transport, and modular compatibility contract.

But:

NO CURRENT LEGAL MAP != IMPOSSIBILITY THEOREM.

The following stronger arguments are rejected:
- ALL NONTRIVIAL f(Box) BREAK TRANSPORT;
- ENTIRE f(Box) IS STRUCTURALLY INCOMPATIBLE WITH MODULAR-PRESERVING DEFORMATION;
- NO KILLING FIELDS ON SOME BACKGROUND PROVES A GENERAL NCDG NONMAP.

A background outside the donor construction's symmetry domain shows source-domain inapplicability, not target-theory impossibility.

## 8. Anti-self-sealing disposition

NC's warning was substantively correct: a new RETURN_ID did not create independent evidence because the later Dorau–Much §6.1 reused NC's own unaudited J3 premise.

That dependency is now externally broken for the load-bearing algebraic claim:

- INT7 independently audited the seven-artifact J3 series.
- Rec9 independently re-derived the central identity and exact 2x2 falsifier.
- The disputed necessity claim FAILS.
- The affine closed form PASS survives.
- INT7 already repaired the downstream Dorau–Much nonmap wording.

Therefore:

NC_J3_CARD005_1_2_AUDIT_DEBT = CLOSED_FOR_ALGEBRAIC_NECESSITY_CLAIM.
NC_J3_SERIES_FULL_SOURCE_REPRODUCTION_DEBT = NOT CLOSED.
PAPER1_REFERENCE_N41_REPRODUCTION = OPEN.
DOMAIN_TRUNCATION_CAUSAL_ATTRIBUTION = OPEN.

Do not conflate these.

## Final status

NC_J3_AFFINE_CLOSED_FORM = PASS_EXACT
NC_J3_GENERAL_IDENTITY = PASS_EXACT
NC_J3_COMMUTATION_PLUS_IDEMPOTENCE_NECESSITY = REJECT
NC_J3_NO_NONTRIVIAL_ENTIRE_CLOSURE = REJECT_AS_UNIVERSAL
NC_J3_ZERO_FREE_ENTIRE_NONCLOSURE = REJECT_AS_UNIVERSAL
SPECIFIC_ENTIRE_NONCLOSURE = PASS_AS_EXISTENCE_WITNESS_ONLY
INT7_SEVEN_ARTIFACT_AUDIT = ACCEPT_WITH_DECLARED_OPEN_REPRODUCTION_ITEMS
INT7_DORAU_MUCH_DOWNSTREAM_REPAIR = ACCEPT
ANTI_SELF_SEALING_DEPENDENCY = RESOLVED_FOR_CARD005_1_2
PAPER1_SAME_SOURCE_REPRODUCTION = OPEN
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_TASK

STOP this algebraic necessity seam after owner integration unless:
- a contradictory exact derivation is supplied,
- the declared representation convention changes,
- or a stronger carrier-specific necessity theorem is proposed with explicit richness/noncancellation assumptions.
