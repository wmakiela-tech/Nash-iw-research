# M12 — DRAFT014 hybrid adapter re-entry lift gate

RESULT_CLASS: EXACT LOCAL CONTROL / FRONT B ADAPTER LEGALITY / NO NUMERICAL ENDPOINT / NO NOVELTY CLAIM

## Trigger

Current DRAFT014 / XH / Mech / Geeky state allows a possible HYBRID adapter:
DE outside a target-sensitive window and full-time hadron dynamics inside.

The missing exact question is whether a reduced/DE state can legally initialize the full model at the window boundary.

## Setup

Let X be the full state space, Z the reduced/DE state space, and q:X->Z the reduction.

Let Phi_full^{b,a}:X->X be full evolution through a sensitive window [a,b].

Let J_b:X->Y include all downstream continuation and the final target.

Define:
T_a(x)=J_b(Phi_full^{b,a}(x)).

At entry time a, the reduced model supplies only z_a in Z.
Compatible full states are the fiber:
F_z = q^{-1}(z).

## Exact re-entry theorem

A unique target prediction from reduced handoff z exists iff T_a is constant on the q-fiber:

q(x)=q(x') => T_a(x)=T_a(x').

Equivalently, there exists a target map T_bar_a:Z->Y such that:

T_a = T_bar_a o q.

Therefore:

HYBRID RE-ENTRY IS TARGET-LEGAL
IFF
THE FULL-WINDOW TARGET FACTORS THROUGH THE REDUCED ENTRY STATE.

## A section is not identification

Choosing a mathematical section/lift ell:Z->X with q o ell = id gives one hybrid output:

J_hyb(z)=T_a(ell(z)).

If T_a is not constant on q-fibers, another legal section ell' can produce a different target.

Hence:

EXISTENCE OF A MATHEMATICAL LIFT
!=
TARGET-SUFFICIENT RE-ENTRY.

A chosen lift may encode an extra closure/prior/model assumption.

## Set-valued handoff

If target constancy fails, the correct target object is:

I_Y(z) = { T_a(x) : x in q^{-1}(z) }.

Point prediction is legal iff this set is a singleton.

If Y has metric d, define fiber target diameter:

D_Y(z)=sup{d(T_a(x),T_a(x')): q(x)=q(x')=z}.

Then:
- D_Y(z)=0 iff exact target re-entry is well defined;
- D_Y(z)<=epsilon gives an epsilon target-reentry certificate.

This is irreducible initialization uncertainty unless source-supported information shrinks the fiber.

## State-exact versus target-sufficient lift

STATE-EXACT LIFT:
z determines x uniquely.

TARGET-SUFFICIENT LIFT:
multiple x are compatible with z, but all produce the same declared final target.

The first is stronger than needed.

HIDDEN STATE NOT IDENTIFIED
!=
TARGET NOT IDENTIFIED.

## Entry and exit are separate gates

ENTRY reduced->full requires a legal lift or target-sufficient entry fiber.

EXIT full->reduced requires downstream reduction sufficiency for the post-window target.

Therefore:

HYBRID LEGALITY
=
ENTRY LIFT SUFFICIENCY
+
EXIT REDUCTION SUFFICIENCY.

Passing one does not imply the other.

## Source-supported lift

If source physics provides reconstruction ell_phys(z,s) from reduced state plus admitted source/history state s, then the actual handoff carrier is (z,s), not z alone.

A source-supported lift is legal only if:
1. q(ell_phys(z,s))=z;
2. ell_phys is source-admitted;
3. s is available at handoff;
4. full-window dynamics uses the same semantics.

## Memory/history lift

If the correct full state depends on prior reduced history,
x_a=L(z_[0,a]),
then current z_a alone is not sufficient.

CURRENT REDUCED STATE
!=
SUFFICIENT RE-ENTRY STATE.

History/process augmentation is then load-bearing.

## Front B specialization

For a PBH -> hadron -> BBN hybrid, the full entry state may include:
- nucleon/BBN abundances;
- time-dependent injected hadron populations;
- depletion/interaction state;
- PBH source/background variables;
- any other coupled state required by the chosen full model.

A DE outer solution may retain only a subset or algebraic equilibrium variables.

Switching to full-time hadron dynamics in the sensitive ~0.3–0.1 MeV window therefore requires one of:

R1 EXACT_RECONSTRUCTION
DE/source state uniquely reconstructs full entry state.

R2 TARGET_SUFFICIENT_FIBER
multiple full states exist but all give the same target within tolerance.

R3 SOURCE_SUPPORTED_HISTORY_LIFT
past PBH/source history plus reduced state reconstructs or bounds full entry state.

R4 UNRESOLVED
compatible hidden entry states remain target-different.

If R4, the hybrid endpoint is not source-closed.

## Equilibrium value guard

An algebraic DE value h_DE(a) may lie on an equilibrium manifold.

Starting full dynamics from h_DE(a) is still an additional approximation unless:
- source physics proves it is the correct handoff state;
- relaxation/history gives a controlled bound;
- or target-fiber diameter proves insensitivity.

DE EQUILIBRIUM VALUE
!=
SOURCE-VALID FULL HISTORY STATE.

## Integration with nonlinear target-transfer bound

Geeky’s secant/Gronwall certificate contains an initial-state error e0.

For hybrid use, e0 can include PHYSICAL HANDOFF / HIDDEN-STATE uncertainty, not merely numerical initialization error.

Thus total target error must separate:
1. re-entry initialization uncertainty;
2. within-window model/rate discrepancy;
3. post-window reduction error when applicable.

SMALL WINDOW-DYNAMICS ERROR
!=
SMALL TOTAL HYBRID ERROR
if entry-state uncertainty is uncontrolled.

## Cheapest kill

Before a hybrid Front B run:
1. freeze full state X;
2. freeze reduced state Z and q;
3. freeze entry time/temperature a;
4. characterize or bound q^{-1}(z_a) over admitted source histories;
5. test final target variation across that fiber;
6. if variation exists, require a source-supported lift/history carrier or target-error bound;
7. otherwise STOP hybrid endpoint claim.

No numerical BBN endpoint is required to apply this gate.

## Lower-host subtraction

HOST_RELATION: exact instance of quotient/factorization, state reconstruction, and partial identification.

PROJECT_ROLE: Front B adapter-legality rule.

No new mathematics and no novelty claim.

## Disposition

HYBRID ADAPTER remains architecturally plausible, but requires a RE-ENTRY LIFT / TARGET-FIBER certificate in addition to target-weighted DE-vs-full dynamics validation.

This does NOT authorize numerical execution.

STATUS:
FRONT_B_HYBRID_REENTRY_GATE=DEFINED.
PBH_B2_TO_DE_ADMISSION=OPEN.
HYBRID_SOURCE_MATCHED_ENTRY_STATE=UNRESOLVED.
SOURCE_MATCHED_K_PBH=UNDEFINED.
NO ENDPOINT RELEASE.
REV020 active.
REV021 not created.
TPE thin compiler / HOLD.
NO CANON / NO EXEC_SIGN / NO NOVELTY INFERENCE / SCIENCE_FIRST.
