# XH-S4 — OpenAI scientific research broad re-harvest: host, mechanisms, tests, caveats
DATE: 2026-10-18
RETURN_ID: XH-S4-OPENAI-SCIENCE-BROAD-REHARVEST-005_20261018
CELL: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03 / XH-S4
RESULT_CLASS: SOURCE-NATIVE_EXTERNAL_INTAKE_AND_PROJECT_APPLICABILITY_MAP
AUTHORITY: EXTERNAL EVIDENCE ONLY / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE / NO_NEW_TASK_CASCADE
METHOD: Public OpenAI primary research announcements and current GitHub source history read, juxtaposed with actual PRF10, Geeky-S10, MECH-S6 Oct-8 project records. NOT an independent proof/experimental replication.

## 0. Recovered NASH prior coverage (2026-10-08)
PRF10 scanned about 11 named result families out of OpenAI math's 372, notably 325 Crouzeix, 251 strong Ulam stability, 289 Kadison-Kastler, 295 higher Hochschild, 288 Kadison similarity, 307 coarse assembly, 255 quasi-isometry, plus 211,282,362,334.
- PRF10 scan https://docs.google.com/document/d/1Dj1UoC2HYoeBiMRENWsSLPOly26Vkh2t28MIofeTCVM/edit
- MECH priority repair https://docs.google.com/document/d/1SwEnsTBo00oTU-hGfBd_xCZry-HeM-uFPqq7nA5eaMk/edit
- PRF10 DTC0a actual commutator kill https://docs.google.com/document/d/1TNMn46UNDxVBQHYz-1kffhWig_KOo0tXN3ugDnhYWoM/edit
- In live DTC, E_lin is self-adjoint: spectral theorem dominates Crouzeix; K_A=[A1,A2]-A_bracket does not commute with natural A1,A2,A_bracket, so direct single-operator f(A) host killed for those A (specific numerical runs), possible nonnormal f(A_C)/block routes CONDITIONAL. Strong Ulam host only for discrete countable group unitary almost reps with uniform operator-norm defect; H5 BW != bounded Hochschild of vN algebra. No canon promotion.

## 1. Official OpenAI math corpus: corrected currentness and verification layers
- Source: https://github.com/openai/math (README Git blob 50feb63d396138f30dc1ff1e0af121d0263bf5a3, read 2026-10-18)
- Current official count: 719 manuscripts, 372 families. Oct-8 PRF report's 722 manuscripts is stale (three removed).
- Source: https://github.com/openai/math/blob/main/history.md, blob 693874f398905b1bc59e01b898b223ae9956bfc2
- Oct-7 history explicitly reports 3 withdrawals due to sign error in stabilization-trace cancellation and dependent Kuga-Satake/K3 rational Hodge papers; 14 other revised manuscripts and 13 associated citation adjustments; 6 additional formalizations. Current README says ~42% top-line results formalized (history: 300/719).
- ~4000 attempted research questions, average model run ~3 Pro-equivalent thinking hours per reported result (self-report). Not a controlled estimate of scientific correctness or generality.
- SOURCE_CONTRACT: REPO_MANUSCRIPT != VERIFIED THEOREM; LEAN_FORMALIZED_CLAIM != UNLIMITED_PROJECT_HOST_TRANSFER; withdrawals propagate to dependent statements.
- Further mathematically large but not previously prioritized: Aug-1 Ten advances in math (non-sofic groups, Connes group-factor rigidity counterexample, quantum parallel repetition, extremal combinatorics, coding and complexity). Treat individually as PUBLISHED_CLAIM / source and proof status to verify.
  https://openai.com/index/ten-advances-in-mathematics/
- May-20 Erdős unit-distance counterexample: OpenAI describes an independently inspected construction replacing an expected upper-bound intuition; mathematical mechanism is counterexample-first search borrowing algebraic number theory, not a theorem about NASH.
  https://openai.com/index/model-disproves-discrete-geometry-conjecture/
- Sep-8 Navier–Stokes claimed smooth externally FORCED finite-time singularity, even from rest, with Lean link; OpenAI asserts particular Clay C/D formulations, but no independent Clay/prize adjudication established in this harvest; never relabel as force-free or as settled without independent checking.
  https://openai.com/index/navier-stokes-solution/
POSSIBLE NASH USE: audit dependency graph and proof statuses; inspiration for DAX counterexample-first search and shared-realization identifiability vs group-factor counterexample. No unsourced transfer.

## 2. Physics: locus-specific algebra + independent derivation (HIGH research-method relevance)
- Feb-13 OpenAI/Guevara/Lupsasca/Skinner/Strominger/Weil: single-minus gluon tree amplitudes are NONZERO on precisely characterized half-collinear momentum slice despite generic-momenta vanishing statement. GPT-5.2 Pro conjectured simplified all-n formula; another model supplied proof, authors checked Berends-Giele recursion and soft theorem. Report says graviton analog explored.
  https://openai.com/index/new-result-theoretical-physics/
- Native lesson: theorem with GENERIC hypotheses must not silently be transferred to exceptional locus; support/slice/limit matters. Strong analogy to DAX noncommuting limits, NCDG TT/mask special regimes, background-domain guards; NOT a new J3/K physical result and NOT a direct bound.
- Nov-20 2025 joint case-study report: model initially missed hidden Kerr wave-equation SL(2,R) symmetry and succeeded after flat-space warm-up. This is a rediscovery of a known result, not fresh Kerr theorem; model warm-up exposure must be logged and distinguished from cold/independent reconstruction. Also human expert collaborative optimization counterexample and multi-domain concept search.
  https://openai.com/index/accelerating-science-gpt-5/
- June-11 Chi-kwan Chan / EHT Codex scientific computational experiment: exploring verifiable particle/pic schemes rather than claimed finished trillions-particle simulator. Lesson: candidate numerical methods must face invariance/conservation/reproducibility tests before physical upgrade.
  https://openai.com/index/using-codex-to-simulate-black-holes/

## 3. Wet-lab empirical loops: genuine feedback, not model consensus
- Feb-5 Ginkgo Bioworks + GPT-5 CFPS: six cycles, >36k tested reaction compositions in 580 plates; claims 40% lower protein production cost and 57% reagent cost improvement in specified setting. Experimental system distinct from Nash's present mathematical tests.
  https://openai.com/index/gpt-5-lowers-protein-synthesis-cost/
- Jun-17 Molecule.one Maria + GPT-5.4 Chan–Lam coupling: a proposed mild oxidant strategy, 10,080 microreactions for selected programme; mean yield 16.6%->25.2%, 11/14 bench-tested substrate pairs improved. Humans steered and independently checked. Not autonomous proof nor general chemical law.
  https://openai.com/index/ai-chemist-improves-reaction/
- Jun-23 immunology / Derya Unutmaz: GPT-5 Pro inferred mechanistic N-linked glycosylation and memory T-cell contribution in 2DG / T-cell context; mannose-rescue and existing lab data supported predictions; external observational-experimental evidence in a particular setting.
  https://openai.com/index/gpt-5-immunology-mystery/
NASH method transfer: "novel hypothesis -> decisive discriminator -> real observation -> update" with physical vs simulation evidence typing. Useful to SW/LT scientific process and empirical MECH planning, not permission to invent physical endpoints.

## 4. Reproducibility, proof audit, scientific evaluation (HIGH NASH-method relevance)
- Feb-20 OpenAI First Proof 10 attempts: at least five were judged high chance of correct after expert feedback, but problem #2 initially believed correct and then judged incorrect; partial human supervision and selection disclosed. Lesson: plausible proof and internal consensus are not verified theorem.
  https://openai.com/index/first-proof-submissions/
- Dec-16 2025 FrontierScience distinguishes Olympiad from Research tasks; useful methodological comparator against ad hoc model benchmarks.
  https://openai.com/index/frontierscience/
- Jun-17 2026 LifeSciBench: 750 real-life expert-authored tasks, 7 workflows/7 domains, 1062 artifacts, 19020 criteria, 173 task creators, 453 independent expert reviewers. Reported best-model exact pass just 36.1% vs 25.7% for comparator; weakest design/analysis around 30%. Shows answer-only or judge-only metrics mask incomplete research quality; high relevance to NASH external evaluation and claim ceilings.
  https://openai.com/index/introducing-life-sci-bench/
- Dec-11 2025 GPT-5.2 statistical learning proof: monotone learning curves in a specifically declared well-specified Gaussian MLE scenario with known mean/unknown standard deviation; not universal monotonicity. Source https://openai.com/index/gpt-5-2-for-science-and-math/
- Sep-21 OpenAI independent math advisory board, and Oct-15 Simons initiative, scientific governance external accountability. https://openai.com/index/advisory-group-on-mathematics-and-ai/ ; https://openai.com/index/sharing-ai-progress-in-mathematics/

## 5. Claim-local candidate selection for NASH (NOT issued tasks)
P0: OpenAI Math repository as REVISION/RETRACTION-CUSTODY test; use exact manuscript/version/Lean dependency graph. Oct-7 sign-error 3-withdrawal chain is concrete scientific negative-knowledge test.
P0: Physics half-collinear source as EXCEPTIONAL-LOCUS / GENERALITY FIREWALL: verify where a commonly invoked zero identity changes meaning at singular/degenerate kinematics. Analogy to DAX and NCDG but NO direct physical result transferred.
P0: First Proof plus LifeSciBench as SCIENTIFIC_EVALUATION_DESIGN: self-reported confidence, expert correction, artifact grading, acceptance/execution distinct.
P1: CFPS/Maria proof-of-method: hypothesis→discriminator→measurement→recheck→update; compare with Nash diagnostic vs empirical result semantics.
P1: OpenAI Math ten results (Connes/non-sofic/quantum games) only if theorem host local to an open NASH front, after Lean/independent proof audit.
P1: statistical MLE special-case monotonicity for PFN/deployment detection experiments; never transfer to arbitrary black-box model.
P2: physics computational code candidate from EHT case; cannot assume tested simulator exists.
P2: domain-specific GPT-Rosalind as potential scientific tool only; product != scientific discovery; users may require eligibility.

## 6. Explicit no-overreach
- No proof adjudication by XH; no automatic assumption OpenAI press claims are peer-reviewed.
- No NASH canonical integration; no BW mutation; no new owner tasks; no novelty; no EXEC.
- Distinguish model-generated paper, Lean-checkable formalization, expert-reviewed case, verified wetlab measurements, broad product marketing.
- Current repository count 719 not previously cited 722.
- PRIORITY means scouting relevance only; not project approval.

SOURCES: primary URLs above; NASH evidence: PRF10 and MECH linked in section 0.
CUSTODY: GitHub source map can be routed to cell owners and KN but receipt/acceptance and BW ingestion remain separate.
