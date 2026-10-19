# XH-S4 — October 2026 deep source audit 009: formal semantics, numerical diagnosis, and replication independence

DATE: 2026-10-19
RETURN_ID: XH-S4-OCT2026-FORMAL-SEMANTIC-NUMERICAL-DIAGNOSIS-INDEPENDENCE-AUDIT-009
CELL: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03 / XH-S4
RESULT_CLASS: FULL_TEXT_PRIMARY_SOURCE / EXACT_EVIDENCE_TYPES / HOST_TRANSFER_AND_FAILURE_GATES
AUTHORITY: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE / NO_NEW_OWNER_TASKS
PREDECESSORS: XH-S4 October 006–008 records on NASH GitHub.
SCOPE: three original Oct 2026 v1 manuscripts read full in HTML (plus AIProver abstract only; full HTML > accessible viewer limit): Forall-Lean-Agent arxiv 2610.00885, ADSD arxiv 2610.03872, electrochemical model guide arxiv 2610.10320; AIProver 2610.05367 abstract. NO third-party replication or independent proof of their claims.

## A. Forall-Lean-Agent (2610.00885v1, October 1) — benchmark success != strict proof != independent checker

PRIMARY: https://arxiv.org/html/2610.00885v1 , Sections 3–6, Table 1, Appendices.
AUTHOR: Naing Oo Lwin.

SOURCE-NATIVE acceptance chain:
1. FROZEN task theorem + accessible permitted definitions/statement-only retrieval, but no proof body;
2. Actor produces candidate in isolated workspace; verifier checks syntax, exact statement, shadowing, elaboration, forbidden bypasses;
3. Fresh reviewer has the task + candidate read-only, NOT actor transcript; it recompiles and gives explicit verdict plus proof digest;
4. Final acceptance requires verifier PASS + reviewer APPROVE for THE SAME hash-matched artifact; different SHA invalidates outcome;
5. #print axioms audit separates benchmark rule from strict policy (propext, Classical.choice, Quot.sound only); independent lean4export/nanoda kernel on eligible Lean Eval tracks; independent checker coverage has its own denominator.
6. The authors identify threatened validity from unauthorized reference access, filesystem leakage, artifact drift, outdated dependencies, scorer/infrastructure failures. They call OS/process-tree restrictions *runtime blindness*, explicitly not proof of no training exposure.

MATERIAL NUMBERS (VERISOFTBENCH 100-TASK SUBSET, NOT FULL 500):
Unaided Codex/GPT-5.6 Sol low: benchmark-rule 93 / strict 82 / cost $69.
Forall-Lean-Agent + Codex/GPT-5.6 Sol low: benchmark-rule 100 / strict 88 / independently checked 63/69 judged / cost $62.
Unaided Claude/Opus 5 xhigh: 100 rule / 89 strict / $135.
Forall-Lean-Agent + Claude/Opus 5 xhigh: 100 rule / 96 strict / 69/69 judged independent / $111.
Indep. 63/69 is NOT 63/100 and neither 100 rule nor 88 strict means 100 independent kernel-verified.
The study warns inference/review budgets differ across protocols and closed model comparisons are not fully controlled. Forall with Fable5 low increases cost $157 to $350 and strict remains 89; improvements are NOT universal cost reduction.
Important residual caveat: 12 tasks can inherit disallowed axioms via **repository lemmas**, not necessarily direct model admissions; benchmark rule PASS may still violate the strict chain-of-trust contract. Imported dependency is part of proof's trusted base.

NASH application: implement evidence classes STATEMENT_HASH_MATCH, KERNEL_COMPILES, AXIOM_POLICY_PASS, EXTERNAL_CHECKER_COVERAGE, EXTERNAL_REFEREE_AGREES, PHYSICAL_HOST_APPLICABLE. They are distinct. Do not relabel existing GitHub/Drive readback as science proof acceptance. A reviewer without actor transcript is reviewer-information-blind, NOT source-independent or training-blind.

## B. AIProver (2610.05367v1, October 4) — nontrivial NL-FL semantic fidelity

PRIMARY ABS: https://arxiv.org/abs/2610.05367
Full HTML source too large for current source viewer (~5.6MB); DO NOT claim full paper read.
Authors' abstract: autoformalization verifier examines type correctness, proof completeness, semantic correctness; LoCoBench 58.9k total examples and 771-instance validation without public Lean formalization; their reported pass@4 semantic correctness rises 15.7%->36.7% for base-vs-system. No claim that mere Lean compilation proves source-native intended NL theorem. Full semantic judge design not audited in this turn.
NASH APPLICATION: even exact Lean statement hash can prove the WRONG originally intended theorem if original-language-to-Lean translation was invalid. Need separate source-meaning↔formal-target mapping/referee independent of kernel check. HOST OPEN until exact claim is identified and formalized.

## C. ADSD (2610.03872v1, October 2) — diagnosis precedes code changes

PRIMARY: https://arxiv.org/html/2610.03872v1 sections 2–4, especially 3.1, 3.2, 4.5.
AUTHOR: Peter Chen, Wotao Yin.

Source-native pipeline:
- Fix a baseline numerical solver N0. Collect PUBLIC execution observations.
- Search scientific literature for precise symptom→numerical condition links, capture exact equation/assumptions, turn into deterministic diagnostic detectors.
- Split public data into separate diagnosis rounds and a *verification pool*. On IEEE-118 example: 5000 public traces, 1000 diagnosis (5×200), 4000 verification.
- Threshold >90% verification pool agreement admits a DIAGNOSTIC RELATION / 'illness' to internal hypothesis set. This is an empirical detector screen, not proof of numerical cause or physical law.
- Subsequent method search requires source-native assumptions, separate theory audit, implementation and empirical reproduction. A frozen solver skill includes executable code + instructions + claim dossier; new solver B uses frozen N0 plus skills under matched prompt/model budget.
- Data partition additionally keeps PRIVATE evaluation cases hidden throughout development. This is a separate split from the public diagnosis-vs-public verification partition.
- Authors explicitly bar importing off-the-shelf numerical solvers to isolate diagnosed numerical skill acquisition rather than generic black-box use.
- Ablation: direct solver self-edit (without diagnosed hypotheses/skills), under nominally fixed prompt/model/effort, improves 4 out of 9 error comparisons but worsens other 5; ADSD outperforms every direct edit. Five recursive self-improvement iterations also fail to match ADSD within tested budgets. Results are author reported and domain specific.
- Qwen3.8-2.4T on GOC-500 mean residual error ~1.0e-9 -> 1.4e-11 (about 71x). It is ONE baseline/case, not cross-domain factor or operator error certificate. Other model gain sizes differ.
- Critically, PF residual ||F(x)|| is NOT necessarily distance ||x-x*||, as paper explicitly states, and its PDE error uses discrete reference solution with known norm. This distinction maps to DTC: residual against one profile != operator norm / continuum accuracy.

NASH applicability: diagnostic-first workflow for DTC0a, PDE stiffness, PFN deployment; root-cause source evidence and hypothesis test first, then possible method change, then held-out validation. DO NOT confuse verified detector (>90% public verification) with causal mechanism proof or private heldout success.

## D. Electrochemical specification-driven multiphysics (2610.10320v1, October 7)

PRIMARY: https://arxiv.org/html/2610.10320v1 ; full text/Methods.
AUTHORS: Sebastian Castro et al.
SOURCE-NATIVE research artifact: single HUMAN-controlled machine-readable Markdown guide with governing equations, parameters, numerical methods, staged build, stop criteria and plots; reproducible Julia agents; COMSOL control; physical interpretation at each stop gate. Five build stages: 400 DOF liquid transport+reactions, boundary extensions, 1200 DOF gas phase, fit stage4 before stiffness, 1480 DOF final coupled electrochem. Predeclared checking: electroneutrality, mass, current, Newton residual, diagnostic curves.
Independent builds match each other at 0.04% of the relevant peak CO current and COMSOL at 0.7%. This is a numerical IMPLEMENTATION cross-check, NOT an empirical discovery or proof that the physics model describes reality.
CRITICAL PROVENANCE CAVEAT:
- Each of NINE reported builds had active persistent project memory indexed to earlier-version build results, including a specific fitted i0 and rough prior COMSOL agreement; the shared guide also included ~20 target stop-gate quantities established from first build.
- Authors disclose no direct other-build file/COMSOL output access, and perform an additional TENTH guide-only run without project memory that gives consistent fitted parameters.
- Accordingly 'nine independent builds' are independent file executions but are NOT genuinely exposure-free BLIND reproductions. Their own clean tenth run provides partial independent evidence. Compare with NASH PLANNED_COLD vs STATE_BASED modes and exposure logs.
PLANTED-SPEC ERROR TEST:
- Defects injected in GUIDE, not code. Faithful guide->implementation can propagate flawed PHYSICS perfectly.
- Agent instructed to follow wrong guide, stop for human gate; detects defect only when build log explicitly names wrong relation and proposed repair. Human inspects plots, not code; author uses guide-file checks.
- This differs from implementation bugs. Two independent codes implementing the SAME wrong scientific model can agree to 0.04% and still both be wrong.
- The paper makes explicit that the shared specification is a common-mode scientific failure source; cross-code agreement is evidence for implementation reproducibility, not for source-theory truth.

Source repository: https://github.com/Sebobbit/CO2R-Bulk-Scale-Model (linked directly by paper; not inspected beyond paper text here).
NASH use: versioned governing-equation contract + independent implementation + common-specification error injection + blind independent science referee. Protect against 'trusted guide -> unchallenged duplicate error'. No retrofit to existing physical conclusions.

## E. Taxonomy of three orthogonal audit obligations
PROOF: original meaning (NL) ↔ frozen formal theorem ↔ Lean kernel check ↔ axiom provenance ↔ same-file digest ↔ independent checker coverage.
NUMERICAL: fixed equation/instance ↔ frozen baseline ↔ measured residual/error ↔ diagnostic falsifier ↔ methods from correct source hosts ↔ code experiment ↔ private holdout.
PHYSICAL: source theory and equations ↔ specification contract ↔ independent code builds ↔ convergence/conservation ↔ experimental data and identifiability. Agreement between codes cannot adjudicate a common incorrect physics specification.

## F. Narrow NASH controls (recommendations, not tasks issued)
1. Attach hash of exactly the theorem statement, formalization and proof artifact, plus axiom dependency list. Separate VERIFIER_PASS / STRICT_AX_PASS / SEMANTIC_SOURCE_PASS / EXTERNAL_CHECKER_SCOPE.
2. For numerical DTC and PFN, keep DIAGNOSIS hypothesis distinct from FIX and from VALIDATION on independent/private distribution; preserve numerical method provenance and approximation/floor effects.
3. For source-driven multiphysics, build STOP_GATES with predeclared physics checks; add planted model-level faults to test review; disclose shared guide/memory exposures; at least one scientific auditor independently evaluates the base equations.
4. Tests are currently SOURCE-LEVEL applicability ideas, not EXEC, canon promotions, or new task delegation.

STATUS: READ_SOURCE_AND_DOCUMENT_METHOD_GUARDS / NO_CODE_REPRODUCTION / NO_SCIENTIFIC_CLOSURE / NO_BW_INGESTION.
