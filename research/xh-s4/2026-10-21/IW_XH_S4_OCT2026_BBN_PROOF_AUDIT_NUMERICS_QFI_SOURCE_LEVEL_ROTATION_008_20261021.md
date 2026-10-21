# XH-S4 — October 2026 source-level audit: BBN, formal proof, numerical diagnosis, PBH GW, Krylov QFI
RETURN_ID: XH-S4-OCT2026-BBN-PROOF-AUDIT-NUMERICS-QFI-008_20261021
DATE: 2026-10-21
IDENTITY: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03 / XH-S4
STATUS: FIVE_SOURCE_FULLTEXT_AUDIT / HOST_APPLICATION_CONDITIONAL / NOT_INDEPENDENT_REPLICATION
CLAIM_CEILING: SCIENCE_FIRST / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_PBH_BOUND_TRANSFER / NO_K_J3_INVARIANT / NO_BW_INGESTION_ASSUMPTION
CONTEXT: Follows XH-S4 Oct literature map 006 and fulltext audit 007 (FEEC, NCT, Dirac, Bolzano).
SCOPE: Source-native full-text extraction rather than generic AI interpretation. Different provenance times are explicitly labeled.

## 0. Source provenance, dates, verification
A. Cline, Frerick, Naja, Xu. "Big Bang Nucleosynthesis Constraint on B-mesogenesis". arXiv:2610.03455v1, submitted 2026-10-02. Original html https://arxiv.org/html/2610.03455v1, abstract https://arxiv.org/abs/2610.03455
B. Lwin. "FORALL-LEAN-AGENT for Auditable Reasoning in Formal Mathematics and Software Verification". arXiv:2610.00885v1, submitted 2026-10-01, workshop-acceptance author claim. https://arxiv.org/html/2610.00885v1
C. Chen and Yin. "Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery". arXiv:2610.03872v1, 2026-10-02. https://arxiv.org/html/2610.03872v1
D. Zhou. "Third-order scalar induced gravitational waves during a matter-dominated era: secular growth and implications for primordial black hole domination". arXiv:2610.08045v1, 2026-10-06. https://arxiv.org/html/2610.08045v1
E. Alishahiha, Tabesh and Vasli. "Krylov distribution and spectral convergence of quantum fisher information", EPJC 86 (2026) article 1176, journal publication 2026-10-19. DOI https://doi.org/10.1140/epjc/s10052-026-16434-0 ; source full text https://link.springer.com/article/10.1140/epjc/s10052-026-16434-0 . IMPORTANT: NOT new October 2026 arXiv preprint: arXiv:2602.19750 first posted Feb 23 2026, revised Aug 19 (v3). October publication is real new journal-stage event. Source itself explicitly subtracts novelty of Krylov QFI lower-bound hierarchy and gapped exponential convergence.

## 1. B-MESOGENESIS / BBN source and calculation stages: highest Front B donor

Paper Sec II Eq(2) uses background source `d rho_r/dt + 4H rho_r = Gamma_phi rho_phi`, with Phi nonrelativistic energy density `rho_phi=rho_0 exp(-Gamma t)/a^3`. They use nonstandard time-temperature history and neutrino temperatures, plus residual time-dependent baryon-to-photon ratio.
Sec V specifically distinguishes BBN-simple (cosmology) and AlterAlterBBN AABBN (network with hadronic source) and notes need for PYTHIA-like shower Monte Carlo for b-decay hadron yields. Hadron species: p, n, pi+/-, K+/-, K_L. Sec V says for a demonstrated case (M_phi=100 GeV, Gamma=50/s), INCLUDING hadronic injection increases deviation of n/p, Yp, D/H from standard case by about x10 compared with solely neutrino heating + time-dependent eta_B. This is not a universal factor.

Their own likelihood Sec VI Eq(12) includes Yp=0.2458+/-0.0013 and D/H=(2.508+/-0.029)e-5, with AABBN rate uncertainties including the hadronic interconversion uncertainty. Their 3sigma reheating lower bounds at 100 GeV approx 9.5 MeV and 20 GeV 9.8 MeV, their model only. They estimate in neutrino injection approx uncertainty yields <=5% bound weakening when replacing neutrino deposition by EM deposition. THIS uncertainty is explicitly evaluated in B-mesogenesis source model, not PBH.
Comparison to original authors' public Wu-Xu scan v1/v2 `main-scan.jl` which writes chi2_mat=((Yp_mat-0.245)/0.003)^2 and stores Yp, beta, mass, chi2 only. This script-level comparison does NOT prove full published Wu-Xu paper ignored D/H in all analysis, nor that AABBN Yp data can be transplanted to old Wu-Xu calculation.
Direct evidence: https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl ;
https://arxiv.org/abs/2509.05618 (as of 2026-10-21, v3 arXiv revised 2026-05-06, paper journal JCAP02(2026)063).
Front B applicability: source/time/background/reaction contracts must be declared independently; 3-layer interface `(donor source species, source-to-reaction B map Q->R, observable Yp+D/H likelihood)`. AABBN paper is useful as a donor of METHODOLOGY/observables, not a substitute for BlackHawk emission, per-charge normalization, or subedge run provenance. No PBH quantitative claim upgrade.

## 2. FORALL-LEAN-AGENT / formal proof acceptance semantics and source honesty

Sec3.4: new reviewer session receives frozen statement and digest-bound candidate, but no actor transcript; recompiles and checks changed statement, shadowed names, axioms, vacuous or circular proofs. Acceptance needs verifier pass+reviewer approval on same candidate digest; mismatches fail. Kernel axiom audit `#print axioms` permits `propext, Classical.choice, Quot.sound`; inherited repository lemmas can contain `sorryAx, Lean.ofReduceBool, Lean.trustCompiler`. A benchmark PASS differs from strict axiom PASS.
Table1 on 100-task VeriSoftBench, matched Codex GPT-5.6 Sol low effort:
  Codex alone: benchmark-rule 93/100, strict 82/100, $69;
  + FORALL: rule 100/100, strict 88/100, independently judged 63/69, $62.
  IMPORTANT 63/69 denominator is checked subset of judged candidates, NOT 63/100 and NOT independent acceptance of all 100; many runs have no independent-checker coverage.
Authors independently check only supported pinned environments by Lean export plus nanoda; 12 tasks in 100 have possible inherited disallowed axioms; unavailable audits should not be classified clean.
PutnamBench 672/672 pertains to answer-GIVEN Lean tasks, one model+effort run; does NOT represent newly discovering mathematical results, nor independent proof-checker coverage for all 672. Reviewer approval is not same as independent theorem content selection.
Published text also discusses recovered tool/auth errors and compiler version migration as distinct from theorem proof outcomes (Oct release external method).
NASH KN/BW/REC integration as proposed STATUS MODEL ONLY:
`OBJECT_ID + SOURCE_SHA + FORMAL_STATEMENT_SHA + CANDIDATE_SHA + COMPILER_PASS + AXIOM_AUDIT_STATUS + INDEPENDENT_CHECKER_COVERAGE + EXTERNAL_REFEREE_SCOPE + OWNER_ACCEPTANCE + BW_REGISTRATION + EXEC`.
Never conflate technical storage/readback with theorem acceptance. No direct operational modification made.

## 3. ADSD / diagnosis of numerical solvers — method and transfer walls

Paper Algorithm1:
(1) freeze generated baseline solver N0;
(2) run once on public cases to capture traces;
(3) literature claim-backed diagnostic probe extraction (source page evidence);
(4) split public observations into non-overlapping diagnosis rounds D_i vs verification pool V; check hypotheses on V;
(5) synthesize reusable solver skill and use fresh agent to build B;
(6) evaluate on unseen test distributions.
Example IEEE-118 paper says 5,000 public observed cases split into 1,000 diagnosis (5x200) and 4,000 verification; distinctions between PUBLIC hypothesis verification vs held-out evaluation essential. On GOC-500 Qwen3.8 baseline author reports almost 71x mean powerflow solver residual reduction, not generic guarantee of all systems, not necessarily true solution-state error.
ADSD paper gives quantitative counterexample to naive literature flooding: search narrowed from 312 papers to 82 candidates to six examined; baseline allowed knowledge but lacked defect-specific diagnosis. Five rounds plain revisions failed to close gap to diagnosis-first ADSD.
NASH numerical tests: FIRST freeze input/source/hash/masks/stencil/finite-N/seed; define failing criterion (even-N Nyquist, field-class, source-class, scaling); derive executable falsifier on separate diagnostic pool, compare with sober mathematical prior-art; only then change solver. Test on strict unused geometries/N where applicable, report wall-clock/runtime/norm same declared quantity. Do not move from lower numerical residual to continuum invariance, K/J3 physical claim, or novel physics.
No algorithm implementation performed this rotation.

## 4. Third-order induced GW PBH domination source-class wall

Zhou Oct6 arXiv source assumes pure early MATTER-dominated phase by PBHs ending at evaporation, Poisson fluctuation spectrum with UV cutoff k_UV, g_star approx 100, Newton gauge, no detailed radiation transition. Defines condition for domination Omega_PBH,f>1e-15*(1e9g/mPBH) and PBH mass + abundance as two inputs. Uses monochromatic evaluation as one test, second-order analytic checks, and a Monte Carlo five-fold integral.
Third-order spectrum grows x^6 vs second-order x^2 in long MD (x=k eta). Authors obtain backreaction guard integral d ln k Omega_GW^total <1 and fitted model-bound Omega_PBH,f <=4.6e-7*(mPBH/1e7g)^(-0.48), about three orders stronger than order-2-only. Critical ceiling: illustrative benchmark Omega=1e-6 at 1e7g gives integrated GW~9e2, already perturbatively invalid, and third-order curve there is described as FORMAL EXTRAPOLATION. Bound is a conditional self-consistency screen for truncation order 2+3; the paper explicitly notes transition to radiation, gauge dependence at third order, and higher perturbative towers uncomputed.
This is NOT a physical observed constraint on PBH mass distribution or a published bound from Wu-Xu BBN. It is a different formation-spectrum/background channel. No merging of `beta_PBH` from Wu-Xu with `Omega_PBH,f` in this paper without deriving exact convention and cosmological carrier map.

## 5. October 19 EPJC Krylov–QFI paper: new journal event, earlier preprint

Source explicitly contrasts computational HS-Lanczos inner product with state-dependent SLD/QFI metric. Defines `A=K_rho : X-> (rho X + X rho)/2`, tangent `B=∂theta rho`, solves `A L=B`. Nested Krylov K_n=span(B,AB,..A^(n-1) B).
Existing hierarchy `F_n=||B||_HS^2 e0^T J_n^-1 e0`, where J_n is tridiagonal Lanczos on active support. New level-resolved identity (authors' main Eq6) `F_n=sum_{k<n}|ell_k|^2`, Krylov information level `p_k=(F_(k+1)-F_k)/F`, with sum p_k=1 on resolved active support if F finite/positive. This is metrological contribution, not arbitrary state-space geometry or universal defect monotone.
Exact analytic hard edge family dmu_alpha=(alpha+1)lambda^alpha dlambda on [0,1], alpha>1, relative truncation error `1-F_n/F = [Gamma(alpha)Gamma(n+1)/Gamma(n+alpha)]^2 ~ Gamma(alpha)^2 n^(-2(alpha-1))`. Article makes clear gapped exponential Krylov convergence known from earlier papers; hard-edge algebraic finite-n result applies only declared Jacobi class, other spectral densities need regularity assumptions. At singular boundary, `F` can diverge. Finite-space random mixed-field Ising tests (example N=12; 8,386,560 compressed spectral dimension, ~4,500 Krylov to 1e-15 relative accuracy) author-reported, not general complexity guarantee.
PROJECT LINKS: resource monotone QFI experiments and quantum-reference-frame covariance; finite-Krylov numerics for identifiability/metrological sensitivity; prohibits conflating Hilbert-Schmidt Krylov projection norm with physical state-dependent Fisher metric, exactly like project same-norm/metric declaration guards. NOT an NCDG TT/J3/K theorem or empirical detection.
SOURCE DATE GUARD: arXiv original Feb23, v3 Aug19, only peer-reviewed journal release Oct19 qualifies as October literature event.
DOI https://doi.org/10.1140/epjc/s10052-026-16434-0
Fulltext https://link.springer.com/article/10.1140/epjc/s10052-026-16434-0
Preprint https://arxiv.org/abs/2602.19750

## 6. Scientifically meaningful relative priorities; not task dispatch

P0 immediate source-method intake: FORALL digest+axiom+independent denominator acceptance (KN/REC methodological guard).
P0 Front B external scientific method donor: B-mesogenesis modular network+Yp/DH+uncertainties, only once Q->R source semantics verified.
P1 ADSD source- and failure-conditioned executable diagnosis; selective transfer to DTC finite numerical experiments.
P1 Krylov-QFI new Oct19 peer-reviewed result; relevant only to declared SLD metrology project host, with HS vs state-metric care.
P2 third-order PBH GW conditional early-MD backreaction: keep in separate PBH front, no BBN bound fusion.

## 7. Integrity and negative knowledge
- No OCT academic item equals proved NASH theorem.
- Reviewer LLM / signed digest != formal theorem true; Lean compile != verified claim with original natural-language statement; independent checker coverage finite.
- AABBN hadronic channels != BlackHawk PBH generator source; 10x response model-specific; do not infer Wu-Xu bounds are wrong without rerun.
- PBH GW backreaction guard in a long pure MD model != observable BBN constraint.
- QFI new JOURNAL October 19, not new preprint October.
- No ownership/BW/canon/physical novelty upgrade. Persisted report doesn't imply acceptance.
