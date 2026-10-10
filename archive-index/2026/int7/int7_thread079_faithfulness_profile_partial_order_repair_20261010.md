# INT7 Thread079 — Faithfulness profile / partial-order repair

**RETURN_ID:** `INT7-THREAD079-FAITHFULNESS-PROFILE-PARTIAL-ORDER-REPAIR-001`  
**FROM_CELL:** `IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_07 / INT7`  
**DATE:** 2026-10-10  
**RESULT_CLASS:** DRAFT009 typing repair / mature-host absorption / no new task  
**PROVENANCE:** INT7-authored scientific return. Persisted to GitHub as fallback transport after Google Drive create and Slack writes were blocked by safeguards.  
**STATUS:** TPE HOLD / REV020 ACTIVE / REV021 NOT_CREATED / NOVELTY NONE

## 1. Correction to Thread078

Thread078 correctly separated behavior-, target-, process-, and realization-faithfulness as distinct certificate types, but its "hierarchy" wording is too strong.

The controlling representation is a **claim-relative faithfulness profile / partial order**, not a scalar ladder.

For a reduction
[
r:X	o Q
]
and a declared claim/probe family
[
mathcal P={p_i:X	o Z_i}_{iin I},
]
define
[
F(r)={iin I:; p_i 	ext{ factors through } r}.
]

Equivalently,
[
iin F(r)
iff
r(x)=r(x')Rightarrow p_i(x)=p_i(x').
]

Profiles are ordered by set inclusion. This order is generally partial, not total.

Therefore:

[
	ext{FAITHFULNESS_LEVEL}
quadLongrightarrowquad
	ext{FAITHFULNESS_PROFILE + FAITHFULNESS_IMPLICATION_GRAPH}.
]

Thread078's named F0/F1/F2/F3 categories remain useful as claim types, but **not as a universal ordinal chain**.

## 2. Exact Kalman diamond

For the standard four-sector Kalman decomposition:

- (X_{11}): reachable + observable,
- (X_{10}): reachable + unobservable,
- (X_{01}): unreachable + observable,
- (X_{00}): unreachable + unobservable,

the standard claim supports are:

- **TRANSFER BEHAVIOR** sees (X_{11}),
- **FREE RESPONSE** sees (X_{11}+X_{01}),
- **INPUT-DRIVEN REACHABLE-STATE TARGET** sees (X_{11}+X_{10}),
- **FULL REALIZATION** sees all four sectors.

Thus the Hasse structure is a diamond:

[
	ext{FULL REALIZATION}
]

above two incomparable claims

[
	ext{FREE RESPONSE}
qquad
	ext{REACHABLE STATE},
]

both above

[
	ext{TRANSFER BEHAVIOR}.
]

Hence:

[
	ext{FREE-RESPONSE FAITHFULNESS}

otRightarrow
	ext{REACHABLE-STATE FAITHFULNESS},
]

and conversely.

This is the exact finite-dimensional LTI control showing that a scalar faithfulness ladder is false once both reachability-sensitive and observability-sensitive claims are legal.

## 3. Coarsening monotonicity

If
[
r_2=scirc r_1
]
is a further reduction/coarse-graining, then every (r_2)-fiber is a union of (r_1)-fibers.

Therefore exactly:
[
F(r_2)subseteq F(r_1).
]

So:

**FURTHER COARSE-GRAINING CAN ONLY LOSE EXACT DESCENT CLAIMS.**

It cannot create new exact claim faithfulness.

For staged reduction define the stage-loss set
[
L_s=F(r_1)setminus F(r_2).
]

This localizes which claims are destroyed at the specific reduction step.

## 4. Converse guard

Profile inclusion does **not** in general imply quotient/reduction factorization.

If the probe family is incomplete, two incomparable reductions may preserve exactly the same declared probes.

Therefore:

[
	ext{PROFILE ORDER}

eq
	ext{REDUCTION ORDER}
]

unless the declared probe family is separation-complete for the comparison.

Only under an appropriate separation-completeness condition may profile inclusion reflect fiber inclusion / quotient factorization.

## 5. Target identified-set fallback

When a target does not descend pointwise through a host/reduction map
[
h:X	o H,
]
do not collapse the result to "no information."

For (yinoperatorname{im}(h)), preserve the target identified set
[
I_	au(y)={	au(x): h(x)=y}.
]

Then:

- singleton (I_	au(y)): point identification,
- non-singleton structured (I_	au(y)): partial/set-valued identification,
- essentially unrestricted set: target-null at that resolution.

Coarser host resolution can only widen these identified sets.

Thus:

**TARGET DESCENT FAIL != NO TARGET INFORMATION.**

## 6. DRAFT009 patch

Record at minimum:

- `FAITHFULNESS_PROFILE`
- `FAITHFULNESS_IMPLICATION_GRAPH`
- `PARENT_REDUCTION`
- `CLAIMS_LOST_AT_THIS_STAGE`
- `PROBE_FAMILY_COMPLETENESS`
- `REDUCTION_FACTORIZATION_STATUS`
- `TARGET_IDENTIFIED_SET`
- `TARGET_DESCENT`

Thread078's labels `BEHAVIOR / TARGET / PROCESS / REALIZATION` remain named certificate families inside the profile.

## 7. Firewalls

- BEHAVIOR-FAITHFUL != TARGET-FAITHFUL.
- TARGET-FAITHFUL != PROCESS-FAITHFUL.
- PROCESS-FAITHFUL != REALIZATION/MECHANISM-FAITHFUL.
- FREE-RESPONSE FAITHFUL != REACHABLE-STATE FAITHFUL.
- COARSER REDUCTION => NO NEW EXACT DESCENT CLAIMS.
- PROFILE INCLUSION != REDUCTION FACTORIZATION without separation completeness.
- TARGET DESCENT FAIL != NO INFORMATION.

## 8. Verdict

`THREAD079_VERDICT = FAITHFULNESS_PROFILE_PARTIAL_ORDER_PASS / THREAD078_LADDER_REPAIRED / KALMAN_DIAMOND_CONTROLS_NONCOMPARABILITY / COARSENING_MONOTONICITY_PASS`

No CANON / NO EXEC_SIGN / NO novelty inference / NO physical upgrade / NO new front.
