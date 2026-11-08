---
artifact_id: IW_DAX_S8_ROT004_CRPROPA_DPP_THINNING_TARGET_SUFFICIENCY_GATE_001_20261108
created_at: 2026-11-08
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
document_type: SCIENTIFIC_RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: EXACT_SOURCE_TYPED_TWO_BERNOULLI_TARGET_GATE / NEGATIVE_KNOWLEDGE / POSITIVE_BOUNDARY
claim_ceiling: NO_FULL_FOUR_LEPTON_QED / NO_NATIVE_CPP_EXECUTION / NO_DEPOSITION / NO_PBH_BBN_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX-S8 ROT004 — CRPropa DPP thinning: target-relative sufficiency and stochastic event-observable bias

8 November 2026. Science-first exact source-model audit; not a native C++ run and not a new physics result.

## Precedence and verified sources
DAX-S7 R68 identified total DPP rate versus full differential operator; DAX-S8 ROT001 identified exact on-shell kinematic insufficiency, ROT002 first-event versus eventual-event typing, ROT003 source-identified the two-hard-lepton CRPropa surrogate and its weighted mean. This ROT004 derives the exact sampling variance and raw event-indicator discrepancy for the same fixed source model. A bounded currentness search through 8 November found no new direct task to DAX and no verified physical differential-QED four-lepton operator; absence of match is not novelty.

Original C++ file https://github.com/CRPropa/CRPropa3/blob/3.3/src/module/EMDoublePairProduction.cpp (Git blob 682f001a264a741ba9615ed86490d9f216a52cfe). Current upstream master has this same checked blob. Documentation https://crpropa.github.io/CRPropa3/api/classcrpropa_1_1EMDoublePairProduction.html demands carrying the weights column in thinning post-processing; accepted thinning t is described as 0..1.

C++ performInteraction removes primary photon and, conditional on haveElectrons=true, calls addSecondary twice for represented e-/e+ hard leptons of equal energy Eh=(Egamma-2me c²)/2. It makes TWO separate random draws, with acceptance p_e=(1-f)^t, p_p=f^t, f=Eh/Egamma, and assigns inverse weights 1/p_e, 1/p_p. It does not generate a complete four-lepton QED event. The second soft pair is not fully represented by outgoing 4-momenta in that module.

## Exact result
Condition on one DPP event at fixed Egamma>2me c² with haveElectrons=true, and two independent Bernoulli draws I_e,I_p of probabilities p_e,p_p. Units: me c². Let q=Egamma/(me c²), Eh=(q-2)/2, f=Eh/q.

Hhat = Eh*(I_e/p_e + I_p/p_p).
E[Hhat]=2Eh.
Var(Hhat)=Eh²*(1/p_e+1/p_p-2).
Relative Var(Hhat)=[1/p_e+1/p_p-2]/4.
P(zero represented secondary records | a DPP event)=(1-p_e)(1-p_p).
E[unweighted indicator >=1 record]=1-(1-p_e)(1-p_p).
E[unweighted indicator both represented leptons present]=p_e*p_p.
Explicit Horvitz-Thompson joint indicator Jhat=I_e I_p/(p_e*p_p) has mean 1, but variance 1/(p_e*p_p)-1.

The energy result proves unbiased expectation only of this source-model additive hard-lepton functional, under correct use of weights and independent sampling. The event indicators require their own inclusion-probability corrections; otherwise thinning changes their mean. A corrected joint indicator need not be low variance.

At exact q=12,t=1: Eh=5, f=5/12, p_e=7/12,p_p=5/12. Then mean raw records=1; P0=35/144 (~24.31%), probability both represented leptons recorded=35/144, probability >=1 record=109/144; mean weighted number=2 and mean weighted hard-lepton energy=10; relative variance weighted hard-lepton energy=37/70; corrected joint-indicator variance=109/35. At t=0 all represented records are present and weighted-energy relative variance is zero.

Independent exact four-outcome rational enumeration of (I_e,I_p)=(0,0),(0,1),(1,0),(1,1), plus closed-form equality checks, passed in local standard-library Python. No Monte Carlo error. At q=12,t=1, one-event relative weighted-energy coefficient of variation sqrt(37/70) ~0.727; achieving 1% relative one-sigma standard error of a mean would require N>=5286 independent identical events. This is NOT a confidence guarantee or astrophysical event budget. High-q limit at t=1: p_e,p_p ->1/2, P0->1/4, relative weighted-energy variance->1/2, joint-corrected indicator variance->3.

Reproduction minimal formula: for each i,j in {0,1}, weight its observable by probability (p_e if i else 1-p_e)*(p_p if j else 1-p_p), sum the four terms; compute its variance by sum probability*(observable - mean)^2. Full report and a standalone exact Fraction program plus JSON/manifest were produced locally as DAX-S8 ROT004 package, but do not assume an independent GitHub copy of the code.

## Sharp falsifier and boundary
FALSE GENERICALLY: unweighted event occupancy/coincidence is preserved merely because the particle-energy estimator is unbiased. The exact P0=35/144 and both-record probability 35/144 falsify this for q=12,t=1.

TRUE UNDER X: source-model linear weighted expectations of the two represented high-energy leptons with correct weights, fixed input and independent thinning. Explicit joint corrections can restore particular nonlinear source-model observables but have distinct variance.

OPEN OUTSIDE X: physical QED differential 2->4, full four-lepton spectrum, transport and neutrino/EM deposition, evolving bath, PBH/BBN predictions, or CRPropa version-specific installed runtime. This test does not establish a CRPropa bug and does not extrapolate to astrophysical bounds.

No mandatory downstream audit cascade. BW private qualification and receipt remain pending. GitHub public body and source control are distinct from scientific acceptance.

STABLE_STOP / NO_AUTO_R69 / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.
