# XH-S4 — October deep harvest 008: Bolzano proof-state/evidence hierarchy, hadronic BBN source, PBH third-order gravitational-wave perturbativity
DATE: 2026-10-19
RETURN_ID: XH-S4-OCT2026-BOLZANO-PBH-BBN-DEEP-SOURCE-HARVEST-008
CELL: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03 / XH-S4
RESULT_CLASS: FULL_HTML_PRIMARY_SOURCE / CODE_READ / HOST_APPLICABILITY / NEGATIVE_KNOWLEDGE
CLAIM_CEILING: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_PBH_ENDPOINT / NO_NEW_OWNER_TASKS
PREDECESSORS: October 006 source map and 007 FEEC/tori/Dirac deep audit (NASH Github xh-s4).

## A. Bolzano (arXiv:2610.09769v2) — proof success and custody semantics
PRIMARY: https://arxiv.org/html/2610.09769v2 ; original Oct7, revised Oct9.
Source-native pipeline: source paper -> source-faithful extracted open question -> problem instance -> parallel provers -> LLM verifier -> verifier-controlled mutable notes.md, proofs.md, output.md -> separate summarizer -> next round. Per paper Sec2 all solvers and verifier receive historical state in prompt, but same-round prover outputs are parallel and not cross-exposed. Verification is LLM, not formal or external proof.
- notes.md: insights, failed paths, conjectures, partial steps.
- proofs.md: candidate detailed proofs.
- output.md: current research outcome for human.
- The app schema-validates verifier state edits. Provers do not directly overwrite the common research files; summarizer does not modify them. "run completed" means allocated rounds finished, not solved.
- Paper explicitly warns: false verifier-approved lemma can propagate in persistent state and accumulate confidence. This is a precise analogue for NASH's memory/currentness vs accepted proof semantics.
- 3800 problem attempts, 485 "promising", 214 "solved" in Table 1. CRITICAL: outside STOC 2026, solved counts are ESTIMATES PARTLY BASED ON LLM POSTPROCESSING. STOC 2026: four author-confirmed results; for convex quartic and biased CAT only MAIN IDEAS were checked, not full proof. Do NOT label 214 verified mathematical theorems, or even all 4 STOC full externally verified proofs. Expert-guided initial results are a different experiment.
- Claimed results include one-pass O(log n) semi-random planted biclique detector for C n^(2/3) both sides; exact monotone rank vs span separation; irrational unique feasible convex quartic point; biased CAT depth lower bound. These are not theorem imports to NASH.
- No controlled same-budget direct-model/no-Bolzano baseline and mixed models/problem pools/budgets; paper explicitly states comparative efficiency not established.
- No formal independent cold audit: same prior state shared across rounds; do not mistake within-round parallelism for exposure independence.
NASH HOST: shared memory architecture, successive verifiers and owner review, precise status labels; not new novel IW idea and not an EXEC/canon acceptance.
SOURCE: https://arxiv.org/html/2610.09769v2 sections 2, 4, table 1 and Discussion.

## B. B-mesogenesis BBN (arXiv:2610.03455v1) — source classes versus reaction and observable endpoint
PRIMARY: https://arxiv.org/html/2610.03455v1 ; initial Oct2.
Physics differs from PBH: late dominating scalar Phi -> b bbar -> B mesons -> meson decay/hadronic showers. Authors list injected species p,n,pi±,K±,K_L (Sec V); use cosmological thermal/reheating history via BBN-simple, feed to AlterAlterBBN / AABBN including hadronic n↔p effects. Model includes evolving baryon-to-photon ratio and neutrino heating, separated in Figure 5 from additional hadron contributions in Figure 6. Authors report hadronic effect ~10x in their illustrated scenario.
Observables+errors used: Yp=0.2458±0.0013 and D/H=(2.508±0.029)×10^-5 (eq12); includes interconversion-reaction-rate systematic uncertainties. Three sigma T_rh lower limits 9.5 MeV at M_Phi=100 GeV and 9.8 MeV at 20 GeV, restricted B-mesogenesis model; NOT PBH bounds.
NASH Front B comparison: Wu-Xu public main-scan.jl stores Y_P_mat and chi2=((Yp-.245)/.003)^2. This newer paper includes BOTH Yp and D/H in likelihood, differently specified observational central value/uncertainty. Direct numerical ratios of bounds are not scientifically comparable (different source/time/expansion and likelihood).
Potential common HOST: late-time neutron/proton interconversion network and experimental reaction uncertainties; before port, require exact species-resolved multiplicities, normalized injection units, time/temperature histories, code version and active hadronic module.
NEW REPRODUCIBILITY CHECK: inspected publicly available repository https://github.com/hep-mh/alteralterbbn , README and public src/ listing. README confirms cosmo_file.dat format t(s), T(MeV), dTdt, Tnu, H, nb_etaf with independent supplied time evolution, and param_file.dat eta. Public src/ consists of bbn.c,cosmo.c,include.h,main.c,param.c,rates.c,test.c,util.c. Inspected bbn.c/include.h/cosmo.c: cosmology temperature and weak/nuclear rates found, but no clearly identifiable hadronic-injection source in those inspected files. This DOES NOT establish absence of a modified private/current hadronic AABBN fork used in Oct paper. It is a PUBLIC CODE ↔ PAPER RUN PROVENANCE OPEN gate. Treat repo implementation NOT proven identical to paper.
RELATED public nuclear code: https://github.com/hep-mh/alteralterbbn; direct comparisons pending field/module auditing.
There is NO source-native claim in paper resolving Wu-Xu BlackHawk charged-pair/aggregate map, 1e9g subedge method, lower-mass energy support, or published scan provenance.
SOURCES: arxiv HTML Sec II,V,VI, eq12-13; public repo GitHub README and sources.

## C. PBH-induced 3rd-order gravitational waves (arXiv:2610.08045v1) — distinct limit is perturbative self-consistency, not a direct observed exclusion
PRIMARY: https://arxiv.org/html/2610.08045v1 ; initial Oct6.
Specific early PBH-dominated matter era: monochromatic PBH mass m, initial fraction Omega_PBH,f and curvature spectrum P_Phi(k) fixed by eq78. Domination prerequisite Omega_PBH,f > 1e-15 (1e9 g/m_PBH), eq76. Author derives third-order SIGW kernels and for MD finds Omega_GW^(3) ∝ x^6 vs Omega_GW^(2)∝x^2, x=k eta >>1 (in intended asymptotic/perturbative regime).
BACKREACTION CONDITIONAL eq83: integrate d ln k Omega_GW,total at evaporation <1. Derived boundary eq84:
Omega_PBH,f ≲ 4.6e-7 (m_PBH/1e7 g)^(-0.48).
INTERPRETATION CAVEAT CRITICAL: this is a CONSISTENCY/perturbative-breakdown boundary, NOT a new direct GW DETECTOR OBSERVATIONAL EXCLUSION. Authors explicitly acknowledge that when Omega_GW ~1 higher orders are uncontrolled, rendering the boundary point where perturbative expansion loses predictive power; reported O(10%) normalization uncertainty from Monte Carlo + high-k tail extrapolation.
MONOCHROMATIC SUPPORT KILL: second-order VECTOR-induced terms vanish identically only on equal-magnitude monochromatic support (eq71); for broad PBH spectrum the equal-magnitude argument fails and all 16 contributions are nonzero (Sec6.2, Appendix B). This is a SOURCE-SUPPORT-/MASK-CONDITIONED cancellation and strong NCDG/DTC methodology analogy, not direct equality for K/J3. Mathematically: source support changes which tensor contractions vanish, before any physical interpretation.
METHOD: broad PBH spectrum six-dimensional Cartesian Monte Carlo with 3e6 samples/point to avoid five-fold grid endpoint aliasing; 200x200 grid mono; symmetry / second-order baseline cross-checks, last high-k sample 17% statistical error and tail extrapolation. Such checks are diagnostics, not generalized rigor.
FRONT B: PBH GW backreaction vs BBN hadronic injection are distinct targets, pipelines and source objects, no automatic stronger replacement for Wu-Xu PBH abundance/Yp bound. Requires same mass and formation measure, cosmological chronology, abundance convention and matching confidence/acceptance definitions for quantitative comparison.

## D. Cross-paper source and evidence typing
BOLZANO: model candidate -> LLM verifier -> external partial/full expert review; 214 reported counts not equivalently verified.
BBN: donor Phi->bbarb, injected species R, nuclear rate uncertainties, Yp AND D/H; not Hawking PBH Q-B-R.
SIGW: independent PBH observable, early PBH matter domination, perturbativity boundary at Omega_tot~1; not observed signal/exclusion.
EXTERNAL SOURCE ≠ NASH THEOREM; method analogy ≠ exact host; GitHub archival ≠ BW ingestion or EXEC.

## E. Claim-local disposition
P0 PROCESS: Bolzano's explicit state files + negative-knowledge propagation and source-original quantifiers/HOST audit → useful independent architecture comparator, no blind independence assumption.
P0 FRONT B: AABBN reaction network and two-observable likelihood candidate if and only if exact code revision/branch + injected species multiplicity normalization + time-temperature adapter are retrieved.
P1 PBH: SIGW higher-order backreaction a distinct external self-consistency lane; not a currently cross-checkable Wu-Xu endpoint. Support-conditioned vector cancellation good DAX/NCDG negative guard.
NEXT SCIENTIFIC SOURCE GAPS: current paper's AABBN exact hadronized code availability; its generator source definitions; whether any PBH joint formation-time distribution can be constructed for comparable early-MD GW vs BBN; original Bolzano code method baseline evidence.
No new owner tasks, no BW or canon edits, no physical discovery announced.
