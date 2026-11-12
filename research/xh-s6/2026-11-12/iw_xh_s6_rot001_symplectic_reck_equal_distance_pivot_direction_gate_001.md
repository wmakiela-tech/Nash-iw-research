artifact_id: IW_XH_S6_ROT001_SYMPLECTIC_RECK_EQUAL_DISTANCE_PIVOT_DIRECTION_GATE_001_20261112
exposure: PUBLIC
claim_ceiling: EXACT_CLASSICAL_SOURCE_TYPED_LOCAL_PIVOT_DIRECTION_GATE__NO_NOVELTY_NO_GLOBAL_FACTORISATION_FALSIFICATION_NO_HARDWARE_NO_CANON_NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
to_cell_or_route: IWTO_MODERATOR
task_id: IW_XH_S6_ROT001_AUTONOMOUS_EXTERNAL_SCIENCE_20261112
return_id: IW_XH_S6_ROT001_SYMPLECTIC_RECK_EQUAL_DISTANCE_PIVOT_DIRECTION_GATE_001_20261112
result_class: RESULT + NEGATIVE_KNOWLEDGE
status: COMPLETE_SOURCE_TYPED_LOCAL_TEST
created_at: 2026-11-12
function: INDEPENDENT_EXTERNAL_SCIENCE_HARVEST / SOURCE_NATIVE_MATHEMATICAL_FALSIFIER
readback_claim: PENDING_UNTIL_VERIFIED
acceptance_owner: MODERATOR; scientific owner of the source paper remains its authors
guards: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_OWNER_TASK_CASCADE

# XH-S6 ROT001 — Equal-distance, unequal local symplectic pivot conditioning

## 0. Result in one sentence

For the **first fixed local two-mode nulling step in the public author implementation**, two exactly symplectic perturbations of the same original zero-pivot target can have **identical Frobenius distance from the target** while one has a finite local condition number and the other remains exactly singular. Consequently, closeness to a zero-pivot input **alone**, without perturbation direction / transversality, is not a sufficient regularization certificate. This is not a falsification of the paper's generic decomposition theorem, global existence under alternative pivot orders, or any physical measurement claim.

## 1. SOURCE FACTS / provenance and level of access

Original contemporary paper: Janet F. Zhong, Renwen Yu, Paul-Alexis Mor, Charles Roques-Carmes, Aviv Karnieli, David A. B. Miller and Shanhui Fan, *Symplectic Reck: In-Situ Learning of Gaussian Quantum Operations*, arXiv:2611.10206v1, submitted 6 Nov 2026, https://arxiv.org/abs/2611.10206 . Source abstract describes a **generic** real symplectic triangular factorization, in-situ local response-block nulling, finite-shot numerical study and a **local condition number**. The **full paper PDF/HTML was not obtained in this XH rotation** despite attempts; abstract-level paper access, not FULL_PAPER_READ. No claims about unpublished equation labels or empirical figure reproduction.

Original author code, actually retrieved/read through authenticated GitHub connector (not merely guessed):
- repository https://github.com/janetzhong/symplectic-reck
- PINNED commit `d2fc391d8081490168974c6302b53d36be4212ea` (3 Nov 2026).
- `symplectic_reck/targets.py` Git blob `ff46b37054af9989a7fbf04c348f7e95382610e4`: exact `isotropic_failure_target()` 6-by-6 numeric source matrix.
- `symplectic_reck/nulling_analytical.py` Git blob `a648fc45e045aa02de6a209b546acd511ecb37f4`: `local_condition_number(anchor,target) = max(1,sqrt(det(V.T@V))/abs(det(anchor)+det(target)))`, and **infinite / rejected singular pivot**.
- `symplectic_reck/nulling_gateorder.py` Git blob `05edc51657a04c24dcb905731707869a7079fb81`: for N=3, first step `probe=0,target=2,anchor=1`.
- `symplectic_reck/experiments/run_conditioning.py` Git blob `5d04aa9522c6204c83c54d86740ee3347922dda2`: one source-defined Hamiltonian perturbation path `exp(alpha*L)@S_iso` with a random generator; source code also tests different noises, Ns and squeezing.
- Source code was **READ, NOT EXECUTED**. No original author data or experimental device replay. Below is **XH independently authored/EXECUTED exact symbolic and numerical test** on one original source matrix.

Historical mature theoretical hosts, not XH originality: Reck et al., Phys. Rev. Lett. 73, 58 (1994), DOI 10.1103/PhysRevLett.73.58 (unitary mesh); Braunstein, Phys. Rev. A 71, 055801 (2005), DOI 10.1103/PhysRevA.71.055801 (Bloch–Messiah/squeezing). They provide context, not prior-art absence. Internal public code search `symplectic` and `Reck` within `wmakiela-tech/Nash-iw-research` returned zero hits at the queried time; **SEARCH_NO_MATCH != NOVELTY**. A comprehensive literature novelty audit was NOT performed.

## 2. Exact model and first pivot

Quadrature order: `(x1,p1,x2,p2,x3,p3)`. Original author 3-mode source target:

```text
S0 = [[1,0, 0,0, 0,-1],
      [0,1, 0,1, 0, 0],
      [1,0,-1,0, 0, 0],
      [0,0, 0,-1,0, 0],
      [0,0, 0,0, 0, 1],
      [0,1, 0,1,-1, 0]]
```

Let `J=diag(J2,J2,J2)`, `J2=[[0,1],[-1,0]]`, and `S0.T J S0 = J` exactly. First source schedule step uses columns `x1,p1` and rows of `anchor=mode2`, `target=mode3`:
```text
P0 = [[1,0],[0,0]],   E0 = [[0,0],[0,1]]
V0 = [P0;E0]  (4x2; rank 2)
Delta = det(P) + det(E) = 0
area^2 = det(V.T V) = 1
```
Here `Delta` is the symplectic area of the two probe-response columns, not a whole-device determinant or a measured sensitivity.

For invertible 3-by-3 Q define its **exact symplectic lift** `D(Q)` acting as `x->Qx, p->Q^(-T)p`, interleaved in the above order. Define (one-based E_ij matrix unit):
```text
Q_perp(a) = I + a E_12
Q_tan(b)  = I + b E_13
S_perp(a) = D(Q_perp(a)) S0
S_tan(b)  = D(Q_tan(b)) S0
a>0, b=2a/sqrt(3), b != 1.
```
Both families satisfy **`S.T J S=J` exactly** and have determinant +1. Both tend to the *same S0*.

## 3. Exact result (two independent routes: symbolic algebra and double precision)

Direct 2-by-2 first-pivot block evaluation:

```text
P_perp = [[1,0],[0,-a]]; E_perp=[[0,0],[0,1]]
Delta_perp = -a
area_perp = sqrt(1+a^2)
kappa_perp = sqrt(1+a^2)/a

P_tan = [[1,0],[0,0]]; E_tan=[[0,0],[0,1-b]]
Delta_tan = 0
area_tan = |1-b|
kappa_tan = +infinity for b!=1
```

Global target perturbation distances are **exactly**:
```text
||S_perp-S0||_F^2 = 4a^2
||S_tan -S0||_F^2 = 3b^2
b=2a/sqrt(3)  ==>  both distances = 2a
```
Thus the comparison **holds distance fixed**, not merely same perturbation coefficient. At `a=1/100`, each distance is `0.02`; kappa_perp = `sqrt(10001) approximately 100.004999875`; kappa_tan remains infinity.

Table from independently executed Python SymPy-exact + NumPy-double test:

| a | Both ||S-S0||F | kappa_perp | kappa_tan |
|---:|---:|---:|---|
| 1/10 | 0.2 | 10.049875621120888 | INF |
| 1/100 | 0.02 | 100.0049998750062 | INF |
| 1/1000 | 0.002 | 1000.0004999998748 | INF |
| 1/10000 | 0.0002 | 10000.000049999991 | INF |

For every row, numerical `||S.T J S-J||_F < 1e-11`. SymPy validated symbolic equalities before the float evaluations.

**Independent impossibility proof for the fixed first two-mode nuller at Delta=0.** The 4-by-2 local response frame V has full column rank two, but isotropic symplectic area `V.T J4 V=Delta J2=0`. A 4-by-4 symplectic left multiplier G preserves that area and rank. If the target 2-by-2 output block were zero, the remaining anchor block W must be rank two; hence `W.T J2 W=det(W)J2 !=0`, a contradiction. Thus **no exact local symplectic gate** can annihilate that target block on the tangent family for `b!=1`. This is about the stated fixed first pivot; reordering or using other primitives is not examined.

## 4. Mechanism, falsifier and science decision

A source paper's generic-factorization statement permits exceptional/singular cases; the official code already contains a zero-pivot target and a local condition number. XH has **not** discovered the general fact that pivoting matters. The independent material delta is a fully specified **equal-distance, distinct-direction source-target discriminator**. A scalar distance-to-zero-pivot stress sweep cannot replace a **local transversality / Delta check**. For the specific author `run_conditioning.py` experiment, a single random generator path is a sample of directions, not an all-directions certificate.

Cheapest next falsifier for anyone extending the numerical robustness claim: place **both** deterministic symplectic lifted paths at matched Frobenius distances into the original gate schedule, record `Delta`, `rank(V)`, `kappa`, `max_gate_db`, failure flags, and change order only as a separate control. Prior to gate creation guard `|Delta|` and report singularity separately from floating-point precision.

This **does not** establish hardware instability, an author's coding error, a violation of the generic decomposition theorem, universal impossibility of alternate symplectic meshes, or NASH physics.

## 5. Reproducibility and custody

Executed locally **12 Nov 2026** using Python 3, SymPy and NumPy; symbolic expressions and independent numeric values above were emitted and checked. Local executed files:

- `xh_s6_rot001_symplectic_equal_distance_gate.py` SHA-256 `6216d776b917f3c251ba1ca5cc7ce2934e0d8cbe236752606b5e79019fa711c9`.
- `xh_s6_rot001_symplectic_equal_distance_gate_results.json` SHA-256 `1cbfaa1cc195c6aa9a1b6dcf48624e307c8379df08ba326417d89ad066e29353`.
- `xh_s6_rot001_symplectic_equal_distance_gate_rows.csv` SHA-256 `aff52076c25bafdc0a6eb4d3b581b4f4a0564ee8337b2d82bc4bcfeb55b0721d`.

These local files are **not** claimed to be published as independent GitHub binary attachments by saving this Markdown body. Source matrix and all exact equations are reproduced in the report so the decisive result is auditable even without the local runner.

## 6. Negative knowledge, ownership and reopen conditions

- Paper FULL_TEXT: ACCESS_UNOBTAINED; abstract + author GitHub source READ. Avoid citing an uninspected paper equation number.
- AUTHOR_CODE_EXECUTED / ARTICLE_RESULT_REPLICATED / MEASUREMENT_REPRODUCED: NO.
- EXTERNAL_MATURE_HOST: Reck/Bloch–Messiah; no novelty claim.
- INTERNAL_NASH_PRECEDENCE: no exact public search hit, not a certified private BW no-match; no transfer of Schall M14 or DAX R68.
- CLAIM LIMIT: EXACT_CLASSICAL_LOCAL_FIXED_SCHEDULE / one original target matrix.
- NEXT_REOPEN_IF: (1) a source code/version update explicitly changes the first pivot or local condition; (2) a new guarantee of direction-uniform robust finite-shot nulling is made; (3) owner requests source-level deterministic stress rerun.
- OWNER DISPOSITION / independent referee / BW ingest: NOT ESTABLISHED.
- STORAGE != RECEIPT != ACCEPTANCE. NO_NEW_TASK_CASCADE.

**Return:** one independent external source-native mathematical test, with a negative universality bound, full source lineage, reproducibility numbers, and no physical or canonical claim.
