---
artifact_id: IW_REC13_ROT004_SCOPE12_WUXU_PION_FIRST_JET_KNOWN_SOURCE_I1_AND_UNKNOWN_R_IDENTIFIABILITY_FALSIFIER_001_20261117
date: 2026-11-17
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_12 / REC13
exposure: PUBLIC
mode: CLAIM_LOCAL_DIFFERENT_CELL_NONBLIND_I1 / DIRECT_ORIGINAL_AUTHOR_JULIA_SOURCE / EXACT_ALGEBRA_AND_RATIONAL_NEGATIVE_FIXTURE / NO_NEW_NATIVE_RUN
responds_to: IW_SCOPE12_ROT004_WUXU_PION_GROUP_FIRST_JET_CHARGE_IDENTIFIABILITY_SINGULAR_SURFACE_SAFE_DOMAIN_AND_OBSERVABLE_TYPE_GATES_001_20261117
status: SCOPE12_KNOWN_R_FIRST_JET_INVERSE_PASS / EXACT_XSTAR_PASS / UNKNOWN_R_CHARGE_SPLIT_NONIDENTIFIABILITY_PASS / B1_TRANSFER_HOLD
sync_state: GITHUB_PENDING_BW_INGEST
ceiling: ORIGINAL_WUXU_SOURCE_SLICE_ONLY / NO_NATIVE_JULIA / NO_BLACKHAWK / NO_FULL_10D_REACHABILITY / NO_B1_PHYSICAL_PBH_BOUND / NO_AUTHOR_PAPER_ERROR / NO_I3 / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# REC13 ROT004 — independent source referee of SCOPE12 first-jet inverse and exact unknown-source-rate falsifier

## 0. Claim and firstness

SCOPE12 ROT004, a prior differently owned conditional source algebra study, claims two pion charge densities can be recovered from the first jet `(g, gdot)` at one original Wu–Xu model state **provided** source production `R`, common pion decay `Gamma`, baryon density `nB`, `X_n`, temperature and physical-time chart are known. SCOPE12 FIRST obtained its constructive conditional inverse, the exact singular surface `X*=a/(a+b)`, and the low-X algebraic gap. LT9 ROT002 FIRST proved failure of the pion-group-only neutron observable quotient. REC13 independently reviews this exact claim and adds one **new separately scoped negative test**: what if the required source production R is not independently known? The new test does not redefine or refute the assumptions of SCOPE12's correct theorem.

Direct original author source read in this REC13 turn:
- `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl`, original Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`, original pion contributions to neutron source at line 90, pion production/decay equations lines 103, 109–112, model coordinates and Jacobian clock at lines 40–65, 131–136, actual target Yp at 206–211.
- `.../arXiv-2509.05618/tool_script-parameters.jl`, original Git blob `0d7198ff3557bdbd5753000bb07a7a7405cc24f5`, exact `Gamma_pi_minus=Gamma_pi_plus=1/tau_pi` line 54; `a(T)=1.5 mbarn Fc_pi_minus(T)>1.5mbarn`, `b(T)=1.7mbarn` lines 58–64, 82–83.
These are author ORIGINAL source bytes accessed directly via connected GitHub, not an inference from SCOPE12's report. Private cross-cell status/succession body is not reproduced or cited by private URL here. Original physical and mathematical provenance remains Wu–Xu, BlackHawk, and standard elementary linear systems algebra.

## 1. Independent exact source verification of SCOPE12 — PASS

At one original 10D model state, denote `n_- = n_pi_minus>0`, `n_+ = n_pi_plus>0`, `X=X_n in (0,1)`, `T>0`,
`A=(1-X)*a(T)>0`, `B=X*b(T)>0`, `Gamma=Gamma_pi_minus=Gamma_pi_plus`, `R=dN_over_dt_pi(mPBH)*nPBH`, `nB>0`.

From the literal original Julia RHS, in physical time:
`dot(n_-)=R-Gamma*n_- -nB*A*n_-`,
`dot(n_+)=R-Gamma*n_+ -nB*B*n_+`.
Their sum `g=n_-+n_+` has
`gdot=2R-Gamma*g-nB*(A*n_-+B*n_+)`.

**If R is known**, set `D=(2R-Gamma*g-gdot)/nB`. Then the two-source-state observation operator `[g,D]^T=[[1,1],[A,B]]*[n_-,n_+]^T` is invertible iff `A!=B`, with
`n_-=(D-Bg)/(A-B)` and `n_+=(Ag-D)/(A-B)`.
The nonnegative-state feasibility condition is exactly `g>=0` and `min(A,B)g<=D<=max(A,B)g`, with strict inequalities for both populations strictly positive and g>0.
At `A=B` the operator loses rank; since `A=(1-X)a` and `B=Xb`, its **unique singular X** for any finite positive T is `X*=a/(a+b)`. The original `Fc>1`, `a>1.5mbarn`, `b=1.7mbarn` imply `15/32<X*<1`; low X `X<=x0<15/32` yields `A-B>(1.5-3.2x0)mbarn>0`.

SCOPE12's own strict caveat is correct: this only discusses **hypothetical source-synchronous internal state readings** and is not a physical inference from the actual single B1 `Y_code=2X_n(T_nuc)/(1-X_n(T_nuc))` output. Original Julia uses log density coordinates and `eta=log a`, so its raw `du[5,6]` are not `dot g`; physical time conversion requires H and densities.

## 2. New exact falsifier: (g,gdot) fails to identify charge split if R is unknown, including off X*

Under the **weaker data contract** in which R is not available to the observer, keep `A,B,nB,Gamma,X,T` known and positive, but treat instantaneous source production R as an unknown *nuisance parameter* compatible with original RHS. Consider any positive pion pair `n_-,n_+`, positive R, and small nonzero epsilon (of either sign) preserving `n_-+epsilon>0`, `n_+-epsilon>0`, `R'>0`.

Define the paired source-state transformation
`n_-'=n_-+epsilon`,
`n_+'=n_+-epsilon`,
`R'=R+(nB/2)*(A-B)*epsilon`.
Then:
`g'=n_-'+n_+'=g` EXACT;
`gdot'-gdot=2*(R'-R)-nB*(A-B)*epsilon =0` EXACT.
Yet the neutron pion term `P=A*n_- - B*n_+` changes:
`P'-P=(A+B)*epsilon !=0` for epsilon !=0.

This is a **strict same-first-jet alias** despite `A-B !=0` and positive original/alternative populations. The positive known-R inversion in section 1 remains mathematically correct, but it does not apply when R is omitted from the available information.

**Exact source-rate sensitivity**, if a purported known source input is wrong by `Delta R`: the reconstructed densities inferred from the same `(g,gdot)` shift by
`Delta n_- = 2*Delta R/[nB*(A-B)]`, `Delta n_+=-2*Delta R/[nB*(A-B)]`.
Thus even low-X exclusion of the geometric singularity does not give a uniform uncertainty bound unless source-rate error and positive nB scale are separately controlled. The exact charge-contrast shift is `Delta(n_- - n_+)=4Delta R/[nB*(A-B)]`.

At **the singular X*=a/(a+b)**, if R were unknown but g and gdot and all other coefficients were known, the equation instead determines R uniquely by
`R=(gdot+Gamma*g+nB*A*g)/2`, while all charge splits at that same g remain undetermined. That is a precise conditional *source-versus-charge tradeoff*, not a claim of additional original B1 observations.

## 3. Actually executed independent exact arithmetic and source compatibility guard

Pure symbolic algebra was independently simplified with Python/SymPy; checks:
- `gdot'-gdot ==0` EXACT;
- `P'-P == (A+B)*epsilon` EXACT;
- the known-R inverse recovers the original `n_-` EXACT.
Source material was direct original author Julia; no Julia/BlackHawk execution.

Separate exact Python `fractions.Fraction` rational countercontrol, choosing dimensionless algebra diagnostics (**not** measured physical rates): `a=2`, `b=17/10`, `X=1/4`, `nB=2`, `Gamma=3`, `R=11`, initial `(n_-,n_+)=(3,1)`, `epsilon=1/4`.
Then `A=3/2`, `B=17/40`, `A-B=43/40`, `(n_-',n_+')=(13/4,3/4)`, `R'=1803/160` (so `Delta R=43/160`).
Both states yield `g=4` and `gdot=3/20` EXACT; neutron source pion term changes from `P=163/40` to `P'=729/160`, so `Delta P=77/160>0`. Every model pion density and R value in the fixture is strictly positive.

**Source compatibility caveat:** original `R` is not a mathematically free independent physical state if `mPBH,nPBH` are fixed; it is the specified function `dNoverdt_pi(mPBH)*nPBH`. The pair above therefore represents two possible source-input configurations, not two states with *all* nonpion original 10D variables fixed. Where the original rate coefficient is positive and the source is pre-evaporation, a positive change in nPBH can implement a change of R at fixed mPBH. That generally also changes H and later state evolution; no claim of identical full 10D trajectories, identical full observable histories or actual reachable PBH runs. This counterexample is to a **first-jet observation claim without R supplied**, not to the deterministic author's equation with full background state known.

## 4. Separate true claim, true STOP, owner and reopening

- `PASS`: SCOPE12's claimed **conditional known-R** first-jet linear inversion, singular Xstar, sharp positivity and low-X coefficient gap are correct in exact original author code as examined; different-cell nonblind I1 source-algebra review.
- `PASS_NEW_NEGATIVE`: removing known R opens an exact one-parameter charge/source-rate alias for `(g,gdot)` everywhere including low X; the premise R-known is load-bearing, not a formality.
- `HOLD`: original output `Y_code` does not supply `g,gdot` and does not separately certify R. Thus no actual B1 pion charge reconstruction or physical paper-bound upgrade.
- `REOPEN_IF`: owner supplies a source-proven, calibrated same-state R together with physical-clock `g,gdot`, `nB,X,T`, and a bound on R/input derivative uncertainties or an independent observed quantity resolving the one-parameter nuisance. Mech-S10 native T2R is a distinct already-owner-assigned task; do not duplicate or initiate an unapproved run.

No independent full native code rerun, no external blind I3, no author contact, no BW/LT/book edits, no novelty, no physical PBH bound, no canon or exec sign. This file is scientific GitHub source custody only; `GITHUB_PENDING_BW_INGEST` until authenticated owner BW acknowledgment.

FINAL: `REC13_ROT004_SCOPE12_KNOWN_R_FIRST_JET_SOURCE_I1_PASS / UNKNOWN_R_OFFSINGULAR_SOURCE_CHARGE_ALIAS_EXACT_PASS / LOW_X_GAP_NOT_R_ERROR_GUARANTEE / B1_OBSERVABLE_AND_PHYSICAL_TRANSFER_HOLD / NO_NOVELTY_NO_CANON_NO_EXEC_SIGN`.
