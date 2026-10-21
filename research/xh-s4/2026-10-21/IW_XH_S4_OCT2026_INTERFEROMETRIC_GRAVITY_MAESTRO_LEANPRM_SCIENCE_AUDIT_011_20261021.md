# XH-S4 — October 2026 science audit 011: interferometric trilemma, Maestro coordination, LeanPRM verification

RETURN_ID: XH-S4-OCT2026-GRAVITY-TRILEMMA-MAESTRO-LEANPRM-011_20261021
DATE: 2026-10-21
CELL: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03 / XH-S4
CLASS: ORIGINAL-SOURCE FULL-TEXT AUDIT / NEGATIVE-KNOWLEDGE / SOURCE-CONTRACT TO NASH
SOURCE STATUS: ARXIV VERSIONS VERIFIED / FULL TEXT READ / INDEPENDENT PROOFS AND BENCHMARKS NOT REPRODUCED
GUARDS: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_INTERPRETATION / NO_K_J3_INVARIANT / NO_BW_INGESTION_ASSUMPTION / NO_NEW_CELL_TASKS

## 0. Primary source/version and prior-report relationship

New after XH-S4 006-010:
A. Hiroki Matsui, Interferometric trilemma for ultraviolet-softened gravity, arXiv:2610.25994v1 [gr-qc], posted 2026-10-19 08:18:43 UTC; 21 pp.
  https://arxiv.org/abs/2610.25994
  https://arxiv.org/html/2610.25994v1
B. Haoyu Li et al., Maestro: Agentic Formal Proof Development by Coordination, arXiv:2610.25920v1 [cs.LG], posted 2026-10-19 07:21:10 UTC.
  https://arxiv.org/abs/2610.25920
  https://arxiv.org/html/2610.25920v1
C. Rodney Lafuente-Mercado et al., LeanPRM: Lean-Grounded Process Supervision for Natural Language Proof Verification, arXiv:2610.17697v2 [cs.LG], posted Oct 13, updated Oct 16.
  https://arxiv.org/abs/2610.17697
  https://arxiv.org/html/2610.17697v2
C is previously UNHARVESTED, not new as of Oct 19. All papers are preprints, not independently accepted project host theorems. Source timestamps of earlier Fried 2610.22281 Oct 15 and MM gravity 2610.20720 Oct 14 directly checked on arXiv in rotation: no chronological date correction necessary for these two.

## 1. Matsui: a clean EXPLICIT OPERATONAL TRILEMMA for UV-softened, linearly coupled gravity

Core objects: a Lorentz-invariant free/generalized-free Gaussian mediator coupled linearly to conserved universal T^{munu}; source histories compact in time and conserved. Difference source Delta=T_a-T_b; response R(x,x'), noise/Hadamard G_H and commutator Pauli-Jordan G_PJ = R - R^T. Two observables:
- two-path visibility e^-Gamma, with Gamma=(kappa²/8) integral Delta G_H Delta;
- conditional phase delta phi_(B|A)=(kappa²/4) integral Y R X with two source differences X,Y, used to detect retarded vs advanced response.
Species representation author Eq(5): G_H=sum_s nu_s G_H,s; G_PJ=sum_s eps_s G_PJ,s. Ordinary positive-norm positive-energy canonical species with nonnegative polarization contractions; nontrivial spectrum-resolving test histories.

Three independent conditions, imposed on all admissible histories:
 P: visibility not amplified, Gamma>=0; for resolved species nu_s >= 0. This 2-path positivity is NECESSARY but not sufficient for CP/full multibranch positivity.
 D: decoherence-radiation identity Gamma=Gamma_rad for the DIFFERENCE SOURCE, not radiation of either branch, implies nu_s=eps_s. Vacuum zero-T FDT under state assumptions; not arbitrary thermal/squeezed state.
 C: no advanced conditional fringe shift from entirely future interferometer, retarded response R=theta G_PJ away from contact terms on source-coupled sector.

Theorem Eq(7):
  V_G(r) = -G_inf m_A m_B/r * [1+sum_{massive species} sigma_s exp(-mu_s r)], sigma_s=eps_s g_s/G_inf=nu_s g_s/G_inf>=0.
So |V_G(r)|>=G_inf m_Am_B/r for r>0; magnitude |dV/dr|>=Newtonian magnitude. Source emphasizes this STATIC Kallen-Lehmann no-weakening bound is PRE-EXISTING prior art, not newly discovered; October novelty claim is the independent operational P/D/C decomposition and one-broken-condition readout.
At free tree level, quadratic gravity ghost realizations:
  negative norm: nu2=eps2=-1 => P fail, fringe visibility amplification;
  negative energy: nu2=+1, eps2=-1 => D fail, noisy decoherence decoupled from positive emitted-energy relation;
  fakeon projected time-symmetric Green kernel: nu2=eps2=0 on shell; conservative response with -1/2(G_R+G_A) => C fail, advanced response/conditional fringe shift.
For Gaussian benchmarks author shows ratios Gamma/Gamma_GR dependent on m2*tau; those are author calculations, not empirical observations. No direct new graviton detection and no measured quantum nonlocality.

LOAD-BEARING SOURCE SCOPE (source S7): tree-level free/linear Gaussian influence functional (or equivalent kernels), Lorentz invariance, universal conserved stress tensor, one massless ordinary graviton, decomposable ordinary spectral shell kernels Eq(5), stationary specified reference vacuum, rich physically realizable source histories, separated sources. Lorentz-breaking Hořava–Lifshitz, nonlinear screening, composition-dependent extra repulsive vectors, momentum-dependent matter vertices, arbitrary interacting non-Gaussian kernels and entire nonlocal form factors lacking well-defined source distributions/prescription are OUTSIDE automatic claim. Fakeon finite-time kernel behavior specifically depends on projected prescription; advanced shifts calculated in model, not empirical detected.

HOST/APPLICATION to NASH:
- Potential physics falsifiability donor for a FUTURE *specified* Lorentz-invariant universal linear metric-mediator realization. Must first prove the source/tensor domain, representation Eq5, gauge/ghost prescription and observed history/readout correspondence. If all three operational conditions hold, claimed universal UV attenuation is blocked IN THAT HOST. If ultraviolet attenuation is claimed, must identify which P/D/C condition is legally abandoned (or which assumption exits the theorem), then propose distinguishable observable.
- NO standalone statement about DTC0a, scalar E(Delta), tensor E(Box), J3/K, emergent spacetime or NASH physical detection; not a proof all nonlocal gravities inconsistent.
- Distinct from arXiv:2610.06390 nonlocal spinor Dirac pole residues and arXiv:2610.20720 MM nonlocal gravity retarded Box^-2: trilemma is a source-coupled Gaussian linear metric mediator NO-GO with different host.

## 2. Maestro: proof plan NONMONOTONIC surgery with frozen root and Lean kernel

Source 2026-10-19. Global coordinator owns an editable Lean4 workspace; parallel provers report progress or diagnosed failure, and coordinator may revise/replace/delete wrong parent or lemmas instead of recursively decomposing forever. ROOT specification frozen; workspace must compile; proof successful only when exact frozen Lean target kernel verified. System also supports target FALSIFICATION: a machine-checked counterexample/disproof is reported in separate count a+b with a proven, b falsified (Table1 and Appendix C). It does not silently convert false original theorem into a repaired theorem as success.

Author benchmark examples with same backbone and single rollout:
- Claude Opus 5 arXivLean June 2026: 34 of 48 proven vs 19 by Claude Code baseline, NOT independent adjudication of original natural-language research paper semantics.
- GPT-5.6 Sol on IMO2026: with Maestro higher success already at "high" effort vs plain Codex needs xhigh for same all-6-in-all-3-runs criterion (author controlled experiments); no universal generalization.
- PutnamBench 669+2 (not 671 theorems proved! 669 proved and 2 formal falsifications).
- Ablation FATE-X: simple decompose+LLM-judge 76 vs plain 77 on one Claude model, vs Maestro 91 + 6 falsified; suggests coordination/cause-aware plan revision, not decomposition alone, is dominant contributor in this author's setup.

SOURCE-NATIVE EXAMPLE FATE-X Problem90 (counterexample to Hilbert's 14th problem): Maestro abandons wrong curve, DELETES 22 old lemmas (19 already proved) but retains 6 independent results, adds 11 new ones, finishes 1.4h later. A proved sublemma CAN become irrelevant when its enclosing hypothesis/plan is wrong. This is NOT revocation of theorem truth: deleted lemmas were superfluous to corrected plan. Source output is a coherent machine-checked new proof.

Caveats: compute cost sometimes very high; Appendix A reports e.g. millions of output tokens for hard examples; web disabled during evaluations, so source proof not copied there, but independence of exact math proof strategy compared to authors does not establish scientific novelty or baseline-adjusted human effort. Benchmarks depend on source Lean statements; source's own Appendix C gives cases where Lean formalization differs from original natural-language question (e.g. degenerate geometry / missing distinctness). Falsification of benchmark LEAN statement != disproof of ORIGINAL MATHEMATICAL QUESTION. Full external theorem-style verification remains separate.

NASH placement:
- KN/REC governance: plan revision can RETRACT dependent candidate evidence, but underlying immutable source reports and historical audit preserved.
- DAX: explicit counterexample-first exploration, isolated original target and revised false conjecture.
- LT/PRF: source statement + Lean statement + proof certificate + dependency edges, no auto EXEC.
- Operational lesson "PROOF_OF_WRONG_LEMMA != SCIENTIFIC_PROGRESS"; "WORKSPACE_COMPILED != NATURAL_LANGUAGE_ORIGINAL_ACCEPTED"; "REPLAN_UNDER_EVIDENCE != ERASE_HISTORY".
No software changes issued here.

## 3. LeanPRM: no silent substitution of probabilistic verifier for proof checker

Source updated v2 on Oct16: model writes paired natural-language and Lean steps in one pass WITHOUT seeing Lean error feedback; checker compiles each. A secondary LLM judges first failure as mathematical vs syntax/translation error; syntax may be repaired only once without math change; formalization-only failures are dropped. EVERY step at and after first bad step labeled bad (source's epistemic prefix convention, not assertion each subsequent mathematical sentence individually false). The training data then builds a probabilistic natural-language PROCESS VERIFIER, which DOES NOT run Lean at inference time.

Corpus 10,634 natural-language proofs, 6,370 positive + 4,264 negative, 152,005 labeled steps, primarily 98% from existing NuminaMath-LEAN and Lean-Workbook source statements. "No human annotation" does NOT mean no errors in NL-to-formal alignment nor human-free certification of arbitrary new research-level theorem.
Held-out LeanPRM-Bench = 200 proofs on 200 unseen statements (100 correct + 100 incorrect); correct proof definition includes Lean compile AND reviewing model says natural-language description faithful. Authors' exact ALL-STEPS classification: base Qwen3-4B 48.2% ±1.3, equal-training PRM800K 60.3% ±1.6, LeanPRM-trained 74.7% (source abstract). Other external benchmarks often use different scores, some binary verdicts; compare same metric.
Source reports formalization-side failure classes are a material fraction and filter model rates; labels are CHECKER-GROUNDED BUT MODEL-FILTERED, not mathematically independent certificates. No NASH proof accepted from verifier prediction.

NASH placement: triage/detection of probable first-invalid-step in long generated argument. Claim validation must still reconstruct true original statement/hypotheses, check against primary source, and get formal/expert proof when needed. Coupled with Maestro = two different roles, coordinator for plan rollback and trained process scorer for prioritizing suspected steps; neither replaces scientific owner and independent referee.

## 4. Cross-paper theorem vs source verdict

GHOST TRILEMMA: Author-proved source-level no-go under strict linear Lorentzian Gaussian spectral host and rich closed histories; Kallen-Lehmann static no-weakening is mature prior art; operational P/D/C decomposition new claimed contribution, not verified in NASH.
MAESTRO: strongest reportable novelty is globally repairable proof-plan graph with Lean verified ROOT, distinct proved/falsified outcomes; benchmark results self-reported, papers' original statement alignment still required.
LEANPRM: probabilistic first-error triage fed by formal-compiler labels and LLM classification; not Lean-verified natural-language proofs per instance.

EXACT EVIDENCE LEVELS:
- ARXIV_DATE_VERSION VERIFIED
- FULLTEXT_THEOREM_HYPOTHESES READ
- SOURCE_BENCHMARK_COUNTS AUTHOR_REPORTED
- INDEPENDENT_MATH_PROOF NOT_REPRODUCED
- PHYSICAL_EXPERIMENT NOT_DONE
- NASH_LOAD_BEARING_HOST NOT_ESTABLISHED
- CANON/BW/EXEC NOT PROMOTED.

## 5. Chronology and follow-up negative knowledge

Oct21 screening verified 2610.22281 original Fried Oct15 and 2610.20720 nonlocal RR Oct14, no date error on those two. Maestro and Matsui both first posted Oct19, LeanPRM first Oct13 revised Oct16. This report is a new-source expansion of 006-010, not a correction to their named numerical results. No new owner tasks / requests.

PRIMARY URLS: https://arxiv.org/html/2610.25994v1 ; https://arxiv.org/html/2610.25920v1 ; https://arxiv.org/html/2610.17697v2 ; corresponding /abs pages above.
