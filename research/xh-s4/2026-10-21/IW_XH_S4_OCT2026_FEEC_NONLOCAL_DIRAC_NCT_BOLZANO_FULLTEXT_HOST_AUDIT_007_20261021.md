# XH-S4 — October 2026 full-text host audit: FEEC, nonlocal Dirac, spectral truncations, Bolzano
RETURN_ID: XH-S4-OCT2026-FEEC-DIRAC-NCT-BOLZANO-FULLTEXT-HOST-AUDIT-007_20261021
DATE: 2026-10-21
CELL: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03 / XH-S4
MODE: SCIENCE_FIRST / CURRENTNESS_FIRST / EXTERNAL_SOURCE_NATIVE_INTAKE
RESULT_CLASS: SOURCE-LEVEL THEOREM_HYPOTHESIS_AND_METHOD_AUDIT / HOST_APPLICABILITY_SPLITTER
STATUS: FOUR_FULL_TEXTS_READ / INDEPENDENT_PROOF_CHECK_NOT_DONE / NASH_HOST_TRANSFER_CONDITIONAL
AUTHORITY: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE / NO_K_J3_CLAIM / NO_NEW_OWNER_TASKS / BW_INGESTION_NOT_IMPLIED

## I. Inputs, versioned primary full texts

A. Daniele Boffi, Kaibo Hu, Yizhou Liang, Umberto Zerbinati, "Finite element exterior calculus for spectra and pseudospectra of advection-diffusion of differential forms", arXiv:2610.01501v1 (submitted 2026-10-01).
https://arxiv.org/html/2610.01501
https://arxiv.org/abs/2610.01501

B. Paulo Jose Porfirio, Ramires Nascimento da Silva, "Nonlocal Dirac theory in curved spacetime and the Bunch-Davies vacuum", arXiv:2610.06390v1 (submitted 2026-10-05).
https://arxiv.org/html/2610.06390
https://arxiv.org/abs/2610.06390

C. Vibhor Bhatt, Satyajit Guin, Palash Sharma, "Gromov-Hausdorff Convergence of Spectral Truncations for Noncommutative Tori", arXiv:2610.01132v1 (2026-10-01).
https://arxiv.org/html/2610.01132

D. Adrian Zamecnik et al., "Bolzano: From Expert-Guided Proof Search to Automated Open-Problem Solving", arXiv:2610.09769v2 (2026-10-09; first posted 2026-10-07).
https://arxiv.org/html/2610.09769

This report replaces the earlier abstract-level classification of the named papers with narrower full-text source obligations. An arXiv full-text read does not constitute independent proof verification or expert referee acceptance.

## II. FEEC — exact mature transportable theorem and its nontransportable conditions

Paper Section 2, Assumption 2.2 requires bounded cochain projections `pi_h^k` commuting with the differential: `d^k pi_h^k = pi_h^{k+1} d^k`; approximation L2 error `<=C h^t |u|_{H^t}` for `1/2 < t <= 1`. This is a substantive chain-complex structural condition not satisfied by merely observing finite matrix convergence.

Paper Section 3, Theorem 3.5 (Kato-type standard perturbation estimate): bounded operators S,T on same complex Hilbert X obey, all epsilon>0,
`sigma_epsilon(T) subset sigma_{epsilon+||T-S||}(S)`
and vice versa.
Corollary 3.6 needs `||T_n-T||_{L(X,X)} -> 0` on the SAME X and SAME operator norm. It yields two-sided epsilon-enlarged pseudospectral inclusions. The claim is NOT mere empirical convergence of a single residual `K_A(h_base)` or visually stable eigenspectra. Corollary 3.7 uses compactness of limit operator T for spectral convergence.

FEEC Sections 4–5 prove operator norm convergence in a specific variational finite-element discretization of Hodge/advection-diffusion. They exploit source/solution operators and compact embeddings. For the full system, Theorem 5.3 explicitly demands u in L^infinity and a sufficiently large positive shifted `nu >= 4epsilon + 1/2||u||_inf + epsilon^-1||u||_inf^2 + 1`. `nu` is part of their shifted source resolvent construction. Their theorems are NOT unconditional for every tensor-transport discretization.

NASH DTC0a proposed legal route:
(i) freeze a bounded nonnormal target `A_C(N)` or a resolvent `R_N(z)` acting on declared Hilbert spaces;
(ii) furnish isometries/embedding and consistent norm to place the finite-N and continuum objects on same X, or instead derive an explicitly comparable finite-to-finite bound;
(iii) prove a robust `delta_N=||T_N-T||_{op}` (or `||T_N-~T_N||_{op}` for an explicit reference construction), not only RMS of a selected field;
(iv) only then claim `sigma_epsilon(T_N) subset sigma_{epsilon+delta_N}(T)`;
(v) eigenvalue lists, scalar control, or K residual amplitude alone are insufficient.
These are SOURCE-APPLICABILITY GATES, not derived DTC convergence. General K_A=[A1,A2]-Ab multioperator structure is untouched. FEEC discretizes differential forms with de Rham projections, while current DTC uses periodic spectral finite differences and TT projection, so their concrete convergence proof cannot simply be imported.

Independent illustrative control (not NASH): A=[[-1,100],[0,-2]], B=diag(-1,-2). Both have identical eigenvalues {-1,-2}, but at z=1, `||(zI-A)^-1||_2 = 16.677493...`, and `||(zI-B)^-1||_2=0.5`; with epsilon=0.1, z=1 lies in A's epsilon-pseudospectrum but not B's. Computed with numpy for explanatory purpose. Demonstrates eigenvalue agreement does NOT certify pseudospectral dynamics.

MATURE_PRIOR_ART: authors explicitly identify estimate as Kato-type (Thm 3.5) and their compact-operator spectral consequence as Osborn-type. No new theorem family inferred from its appearance in October.

## III. NCT spectral truncations — exactly what converges, not what might be assumed

Paper Theorem 4.18: states of truncated finite-dimensional operator systems `E_R` converge to states of the noncommutative torus C*-algebra `A_Theta` with respect to Connes' metric in Gromov-Hausdorff distance as R->infty.
Construction uses unital completely positive maps `rho_R:A_Theta->E_R` and `sigma_R:E_R->A_Theta`, their Lipschitz-norm contractivity, and a C^1-approximate order isomorphism, controlled by `gamma_R -> 0`. Proposition 4.16 has `||T-rho_R sigma_R(T)|| <= gamma_R ||[D_R,T tensor I]||`.
This certifies convergence of METRIC STATE SPACES in a specific noncommutative n-torus host, not convergence of arbitrary projected transport operators, de Rham cohomology, or DTC K/J3 residuals.
The representation/cutoff/metric type must be given explicitly for any legal comparison. It is a different convergence claim from FEEC's operator-norm source-resolvent approximation.

Source https://arxiv.org/html/2610.01132 Sections 3–4, Prop 4.16 and Thm 4.18.

## IV. Nonlocal Dirac — zero-free is not sufficient for no ghosts (model-host firewall)

Authors use covariant first-order spinor Dirac operator `slash nabla`, with Lichnerowicz `slash nabla^2 = Box - R/4` under their convention; even if entire form factor is zero-free, zeros of the FULL fermion kinetic operator in presence of m create new pole branches (Section II, after Eq 8). Spinor components do NOT generally satisfy independent scalar nonlocal equations. A nonlocal f(slash nabla) does NOT automatically represent our tensor E(Box) and does not supply a universal background covariant Box theorem.

In Section II, condition `f(slash nabla)^ddagger = f(slash nabla)` imposes reality `f(z)^* = f(-z^*)` independent of the entire/zero-free condition. Exponential model I f_1=exp(-slash nabla/Lambda) violates target Hermiticity; has generically complex principal pole. Model II f_2=exp(-i slash nabla/Lambda) satisfies reality condition in authors' framework.

For Model II Section IV.3:
`M_n e^{-M_n/Lambda}=m`, `M_n=-Lambda W_n(-m/Lambda)`.
If `0<m/Lambda<1/e`, two real branches n=0 and n=-1. Simple-pole residue scales as `exp(M_n/Lambda)/(1-M_n/Lambda)`.
n=0: `0<M_0<Lambda`, positive residue, treated as physical branch;
n=-1: `M_-1>Lambda`, negative residue, ghostlike;
at `m/Lambda=1/e` branches merge and simple-pole residue argument stops. Remaining branches complex.
Authors RETAIN only principal n=0 sector in physical BD quantization. They do NOT assign independent creation/annihilation operators to ghostlike/complex branches, and do not posit tensor-product Hilbert space across all branches.
Do NOT infer that selecting the positive-residue sector establishes ghost-free full fundamental quantum theory or erases other propagator poles. The nonlocal observable corrections are branch- and model-specific. Local limit Lambda->infinity is not global physical consistency certificate.

NASH use: negative control for zero-free E(Delta)/E(Box) discussions; require exact operator, adjoint/metric, reality, pole/residue, physical sector, full kinetic polynomial/spectrum, background. No claim about K/J3 or new auxiliary particles.

Source https://arxiv.org/html/2610.06390, Eqs 6–13, Sec IV.3 Table 1, Eqs 59–60.

## V. Bolzano — governance evidence, with exact independent-verification ceiling

Authors' v2 Table 1 across four automated experiments:
- 3,800 problems attempted;
- 485 outputs marked "promising";
- 214 classified "solved" (90+4+40+80) with "except for STOC 2026 solved counts are estimates"; LLM assessment contributes substantially and no exhaustive external check.
- four STOC 2026 paper-author confirmations, but paper footnote says for convex quartics and biased CAT states original authors examined the MAIN IDEA ONLY, NOT the full proof.
- no direct baseline to isolated underlying models; no established comparative efficiency gain.

Research states `notes.md`, `proofs.md`, `output.md`, plus past round summaries. Concurrent provers share initial state but cannot see other current-round prover outputs. Verifier assesses all and is the only stage to update three shared research docs; separate summarizer does not alter them. In the paper experiments, prover/verifier/summarizer use NO web, code execution, filesystem or tools (only prompt-passed text); an earlier external problem-extraction workflow did use papers/web. This crucial distinction prevents wrongly describing Bolzano as code-execution/formal-theorem tool.
Authors explicitly warn verifier is just another LLM, not formal; wrong lemma can recursively enter shared memory and acquire unwarranted certainty.
Postprocess explicitly compares extracted task with source paper's EXACT hypotheses, quantifiers, conventions, and asks whether source genuinely states the open problem and whether the candidate proof is correct; even correct answer to wrong extracted task is not completion.
"Completed" in orchestration means allocated rounds finished, NOT theorem solved.

NASH implementation/legal lessons, all already structurally anticipated by KN/BW:
A) preserve immutable question-as-asked and author-source span, not only reformulated task;
B) freeze separate note, proposed proof and verdict; isolated verifier may organize state but cannot bless independent truth;
C) record accepted/rejected source-with-version, assumptions, quantifiers, expert confirmation granularity (idea-only/full proof/formal checked), and human moderator EXEC separately;
D) protected negative knowledge and anti-self-sealing dependency graph across successor handoffs;
E) count results by receipt/checked levels, not self-asserted successes;
F) never equate a persisted state or source availability with owner/BW acceptance.
Not new theory. No new tasks issued.

Source https://arxiv.org/html/2610.09769, Sec 2, Table 1, Sec 4 screening and footnote 3, Sec 5.

## VI. Cross-paper comparison / candidate verdicts

| Paper | Evidence status | Exact likely host | Blocks / not admissible |
| --- | --- | --- | --- |
| FEEC 2610.01501 | Paper source read, proof not independently checked | Matched bounded-resolvent OPERATOR NORM -> epsilon-pseudospectrum | Raw K_A RMS, unmatched H_N, generic TT convergence |
| NCT 2610.01132 | Paper source read, proof not independently checked | Noncommutative torus state metric GH convergence, C^1 maps | Arbitrary operator error/K/J3, physical geometry |
| Dirac 2610.06390 | Paper source read, calculation not independently re-derived | Covariant spinor Dirac exponential form-factor pole/residue selection | Tensor E(Box), universal ghost-freedom, physical NASH bridge |
| Bolzano 2610.09769v2 | Paper methods and counts audited; no independent case-proof read | Research-state/claim-evidence architecture audit | 214 independent verified proofs; LLM verifier=proof checker |

Ranked source value: P0 Bolzano METHOD anti-self-sealing; P0 FEEC same-space norm/pseudospectrum; P0 nonlocal Dirac zero-free/pole firewall; P1 NCT metric-truncation distinction.
Owners for awareness: KN11/Rec10/LT5/PRF11 (method), DAX/Mech (operator counterexamples), NCDG owner (only conditional host), Scope9 (teaching).
READBACK/CROSS_SURFACE note: report saved to GitHub only initially; no Drive/BW accepted, no scientific upgrades.

## VII. Scientific claim ceiling

2026 October arXiv preprint metadata verified. Distinguish established cited Kato/Osborn host statements from new application and author's derivations. No proof adjudication. NO NASH endpoint, no claim of new mathematical invariant, no physical interpretation, no novelty, no EXEC.
