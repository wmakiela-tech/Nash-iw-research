# XH-S5 ROT022 — Pandora 2026: phase bookkeeping in SQL quantum-circuit rewrites and externally controlled subcircuits

artifact_id: IW_XH_S5_ROT022_PANDORA_GLOBAL_PHASE_CONTROLLED_COMPOSITION_GATE_20261103
return_id: XH-S5-ROT022-PANDORA-GLOBAL-SHIFT-REWRITE-CONTROLLED-COMPOSITION-GATE-20261103
date: 2026-11-03
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: PUBLISHER_2026_ABSTRACT_AND_ORIGINAL_GITHUB_SOURCE_REVIEW / EXACT_SOURCE_TYPED_ZPOW_GATE_AND_REWRITE_SEMANTICS / TWO_INDEPENDENT_EXECUTED_TESTS / NO_AUTHOR_POSTGRES_SQL_EXECUTION / NO_PANDORA_PERFORMANCE_REPRO / NO_COMPILER_BUG_PROVEN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN

## ORIGINAL SOURCE and precedence first
Ioana Moflic and Alexandru Paler, "Ultra-large-scale compilation and manipulation of quantum circuits with Pandora", npj Quantum Information, PUBLISHED 30 Oct 2026, DOI https://doi.org/10.1038/s41534-026-01402-z . Authors demonstrate open-source declarative multithreaded quantum circuit manipulation and report very large-scale compilation, equivalence checking and benchmarks. These findings and benchmarks belong to AUTHORS and were NOT independently replayed or benchmarked here.

Pinned public SOURCE CODE ioanamoflic/pandora commit 51b21d62b9199275e214684896a908d1584a8442 (2026-10-30). Exact live GitHub source content was READ through app, not merely README snippets:
1. src/pandora/db/generic_procedures/replace_two_sq_with_one.sql, source blob Git SHA1 1c402acc48bddf8d09148efe6997434e5e18ca04, defines fuse_single_qubit(type_1,type_2,type_replace,param1,param2,param_replace,...). It updates first-row type, next_q1, param to fused type/param, deletes second-row gate, but does NOT change first-row global_shift. ORIGINAL COMMENT expressly states it does not include replacement of global_phase. Thus omission is DOCUMENTED and no claim to newly discovered hidden source bug.
2. src/pandora/db/generic_procedures/cancel_single_qubit.sql, blob c67b3985ca7432aa9b0499140ee2a6bf67758326: checks type/param and adjacency, then removes both; no global_shift guard.
3. src/pandora/translation/gates.py, blob b3fe30a982eef9804c5597fa6c5ee6ae0de2ae3b: PandoraGate has stored global_shift and to_cirq_operation returns gate constructor with global_shift.
4. src/pandora/translation/cirq_translator.py blob e0ad82947a2f011c6464f1eec683d471cd319223: imports gate.global_shift.
5. src/pandora/optimisation/optimiser.py blob 7e95caa5d6f9f7f2041dd10d78b0d61796478704: user can supply gate types/params for templates.
6. tests/procedures_test.py blob 1886d6f031664b6f5bd0d8de94db6896d8c0cc8b: source positive test standard T*T -> S with the same global shift.

All original Git blob values are Git SHA1 object hashes, not archive member SHA256. Full source bytes and original SQL code are NOT republished in the separate local ZIP. Full compiled Pandora, PostgreSQL stored procedure, Cirq, and all performance benchmarks NOT executed. No assertion of an observed end-to-end author software failure.

MATURE prior: Google's OFFICIAL Cirq ZPowGate definition https://quantumai.google/reference/python/cirq/ZPowGate specifies Z(t,s)=exp(i pi s t) diag(1,exp(i pi t)). Standard quantum circuit equivalence checking modulo physically invisible GLOBAL phase is documented by Munich Quantum Toolkit QCEC https://github.com/munich-quantum-toolkit/qcec/blob/main/docs/equivalence_checking.md . Neither the phase algebra nor its promotion to relative phase when a subroutine is coherently CONTROLLED is a new theorem or author-specific novelty.

## EXACT source-typed proof: two distinct equivalence contracts
Let initial consecutive gates be ZPow(e1,s1) then ZPow(e2,s2). Under a specifically enabled source procedure call with type_replace=ZPow and param_replace=e1+e2, SQL keeps the FIRST global_shift s1; thus
U_before=Z(e2,s2) Z(e1,s1);
U_SQL=Z(e1+e2,s1).
The exact operator identity is
  U_before = exp(i*pi*e2*(s2-s1)) * U_SQL.
This holds for any real input params and makes UNCONTROLLED probabilities identical. Exact matrix equality, however, holds only if e2*(s2-s1) is an EVEN INTEGER. For any other choice there is a physical obstruction to treating U_before and U_SQL as identical operators in contexts that compare or coherently control their branches. The conventional circuit-equivalence contract modulo global phase is still satisfied.

SOURCE-NATIVE concrete witness, well within allowed Cirq API:
  first ZPow(exponent=1/4,global_shift=0)
  second ZPow(exponent=1/4,global_shift=-1/2)
  SQL-style fused ZPow(exponent=1/2,global_shift=0)=S.
Then U_before=exp(-i*pi/8)*S, not S. Input to EXTERNAL controlled whole subroutine C(U) is |+>_control tensor |0>_target; X-minus measurement of control:
   before P_minus=sin(pi/16)^2=0.038060233744356624,
   SQL fused without phase P_minus=0.
State fidelity before vs after cos(pi/16)^2=0.9619397662556434;
pure-state trace distance sin(pi/16)=0.19509032201612828.
Single-qubit state fidelity is EXACT 1 for all target inputs since this is global phase there. Thus controlled composition, not isolated-circuit semantics, is the necessary observable discriminator.

CORRECTION: after fusing, multiply the CONTROLLED-one branch by exp(-i*pi/8), e.g. through a conditional phase ledger on the control qubit, NOT by adding an unobservable scalar global factor to the full controlled circuit.

SECOND actual SOURCE PROCEDURE cancellation witness:
 first ZPow(e1=1/4,s1=0);
 second ZPow(e2=-1/4,s2=-1/2).
It matches parametrized cancel_single_qubit gates but its full unitary is exp(i*pi/8) * Identity, not Identity. Deleting both is projectively correct but fails EXACTLY on a coherently controlled use of the block, again P_minus=sin(pi/16)^2 vs0. When e1+e2=0, changing global_shift of a replacement ZPow(0,s) CANNOT encode the phase, thus a separate phase register is essential for strict operator equivalence; otherwise restrict the rule to phases congruent0 mod 2pi.

## EXECUTED independent checks, original code not invoked
Route A rot022_exact.py: Python3.13, fractions.Fraction and SymPy exact rational/complex 2x2 and controlled4x4 matrices. Exhaustive 4 exponents e=1/4,1/2,-1/4,1 with shifts s1,s2 each in -1/2,0,1/2 gives 36 source-call-compatible ZPow fusion patterns. 12 EXACT-unitary PASS, 24 only phase-equivalent, exactly as formula predicts. For all 36 symbolic check U_before=exp(i phi) U_fused exact, and exact witness/cancellation observables PASS. Standard source author T*T->S, s1=s2=0, is exact positive control.
Route B rot022_independent.py: entirely separate NumPy dense matrices and independently coded ctrl-block; 36 original patterns plus 288 randomly prepared full 2-qubit input/context tests with random 4x4 QR unitaries before/after. All projective gate equalities PASS and all phase-compensated controlled operators equal numerically to 2e-14. Without correction randomized minimum state fidelity 0.000961908174 and average0.859461058248. WITNESS controlled gate operator spectral distance 0.390180644032; controlled P_minus 0.038060233744 and fidelity 0.961939766256; source cancellation witness independently reproduced. These context numbers are SYNTHETIC algorithmic tests, NOT physical experiments or full Pandora compilation.

The scientific issue is the EXPLICIT contract between equivalence UP_TO_GLOBAL_PHASE vs exact operator equality when a compiled fragment becomes a conditionally applied, coherently controlled subroutine. The full Pandora paper or code may intentionally choose projective equivalence, which is standard. Therefore NO hidden compiler BUG or performance falsification is claimed.

## Reproducible custody and negative knowledge
Complete Moderator-local ORIGINAL XH scripts, a Polish self-contained scientific report, two deterministic frozen JSON, source_locator.json with 6 original Git blob identifiers, README, verify_replay.py, SHA256SUMS.json: 9 ZIP members. ZIP CRC PASS; all 8 member SHA256 PASS; clean EXTRACTION and both script runs yield two JSON BYTE_IDENTICAL PASS. Original Pandora SQL not included or executed.
LOCAL FULL ZIP: IW_XH_S5_ROT022_PANDORA_GLOBAL_PHASE_REWRITE_GATE_REPRO_20261103.zip
ZIP SHA256 c1cca9b594bafdd6590791ea5d96aa0fd91de4a584d11ae6e26d06685aa850a1
Full Polish report SHA256 4441832989988e678ce4d5adc72b4afc880739d6f8311f25e682fa5d588d7322
Exact script SHA256 72a1ce2c96eaaeb76e802319b446e41836dc7b89289ce1ba4769de86e4b2053d
Independent NumPy script SHA256 eb9c2eb12a5fe10e23296d7547e0fec7bafbcf142776fbf03c750dc2b219cd9f
The GitHub REPORT is NOT a bytewise copy of the complete local ZIP or source code. No remote ZIP custody implied.

Referee question only: specify output API contract. If STRICT equality is needed, enforce e2(s2-s1) in 2*integers, or preserve a phase ledger and pass it as a CONTROLLED relative phase; if only UP_TO_GLOBAL_PHASE is advertised, retain explicit caveat on composability and no new defect assertion. No cross-cell task cascade, BW/REFEREE/OWNER/EXEC adoption not assumed. No NASH physical K/J3/GR/GW inference.
NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PANDORA_POSTGRES_EXECUTION / BW_INGEST_UNVERIFIED.
