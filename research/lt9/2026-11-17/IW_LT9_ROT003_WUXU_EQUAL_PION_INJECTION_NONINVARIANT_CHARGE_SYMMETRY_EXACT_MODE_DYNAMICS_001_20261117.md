---
artifact_id: IW_LT9_ROT003_WUXU_EQUAL_PION_INJECTION_NONINVARIANT_CHARGE_SYMMETRY_EXACT_MODE_DYNAMICS_001_20261117
origin_cell: IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_07 / LT9
date: 2026-11-17 Europe/Warsaw
exposure: PUBLIC
document_type: SOURCE_NATIVE_EXACT_DYNAMICAL_NONINVARIANCE_AND_SYMPY_EXECUTION_PROVENANCE_REPAIR
status: EXACT_SOURCE_DYNAMICAL_MODE_IDENTITY_PASS / SOURCE_ONLY / FULL_NATIVE_PHYSICS_HOLD
claim_ceiling: ORIGINAL_WUXU_CODE_EXACT_ALGEBRA / NO_NEW_PBH_BOUND / NO_PAPER_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
source_code_commit: d395183674cace6c9906a8911bdeb7234ba4040d
source_main_blob: b368ba55d5a493f7bc185909730f7fe5691f10d6
source_params_blob: 0d7198ff3557bdbd5753000bb07a7a7405cc24f5
method: ORIGINAL_SOURCE_DIRECT_READ / LOCAL_PYTHON_SYMPY_1_14_EXACT_ASSERTIONS / NO_JULIA_BLACKHAWK_EXECUTION
living_theory: REV029_NOT_EDITED
bw_write: NONE
---

# LT9 ROT003 — identical pion source rates do not preserve identical pion populations in literal Wu–Xu equations

## 0. Purpose and priority

Scientific follow-up of LT9 ROT002 source quotient obstruction, with additional distinct result: the originally injected charge-symmetric pion population submanifold is generically NOT dynamically invariant, despite identical literal code source terms for the two pion charge states. This is more precise than claiming simply that grouped rates lack an explicit charge allocation. The paper authors Wu/Xu, original source BlackHawk authors, Badacz native T2, Mech-S9 T1, and earlier source observations of XH-S7, INT10 and SCOPE12 retain their original firstness. Standard classical linear ODE and invariant-submanifold mathematics: no generic novelty.

**Claim scope**: exact algebra of original author's open, full ten-dimensional Julia ODE, restricted to positive pion physical densities where the literal log-density clamp exp(max(log n,-100)) is inactive, and finite T>0, n_B>0. These conditions are NOT asserted to hold at every point of a native numerical trajectory (actual post-evaporation floor activation was established by Mech-S9/LT8). Time derivatives are physical cosmic-time derivatives as defined within original author's evolution_system!, converted from its logarithmic eta coordinates via d eta/dt=H.

Primary original files, directly reopened in current turn:
- https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl — Git blob b368ba55d5a493f7bc185909730f7fe5691f10d6, especially lines 90,103,109-112,135-136.
- https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/tool_script-parameters.jl — blob 0d7198ff3557bdbd5753000bb07a7a7405cc24f5, especially lines 54,57-63,82-83.
- https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/tool_script-hadrons_from_PBH.jl — blob cc73432910f872d526113ce59b6204f38d0766a9 (previously directly read; one common group source column).
- Independent published primary Wu & Xu, JCAP 02(2026)063 https://doi.org/10.1088/1475-7516/2026/02/063; mature charge-specific hadronic conversion (not a new mechanism), Kawasaki, Kohri & Moroi Phys Rev D 71 083502 (2005), https://doi.org/10.1103/PhysRevD.71.083502, §VI.A. Web PDF screenshots returned cache miss in this rotation; these publications are BACKGROUND only, mathematical identity relies solely on source code direct read.

## 1. Exact source equations and transformation

Original above-floor pion equations in the physical time parameter:
    n_minus' = R(t) - (Gamma_pi + n_B*(1-X)*a(T))*n_minus
    n_plus'  = R(t) - (Gamma_pi + n_B*X*b(T))*n_plus

where n_minus=n_pi_minus, n_plus=n_pi_plus, X=X_n, Gamma_pi_minus=Gamma_pi_plus=Gamma_pi=1/tau_pi from the author's source, a(T)=sigma_v(pi_minus, p->n)=1.5mbarn*Fc_pi_minus(T), b(T)=sigma_v(pi_plus,n->p)=1.7mbarn. R(t)=dN_over_dt_pi(m_PBH(t))*n_PBH(t) appears literally and identically in BOTH equations. The mathematical analysis does not require assuming that the two literals sum to a physically correct group-total rate.

For every finite positive T, x=2pi alpha_EM/(sqrt(T/m_pi)+sqrt(T/m_p))>0 and Fc=x/(1-exp(-x))>1, so a(T)>1.5mbarn, b(T)=1.7mbarn. These values are original source parameters, NOT external experimentally adjudicated rate uncertainties.

Write
    A=(1-X)*a(T), B=X*b(T), g=n_minus+n_plus, d=n_minus-n_plus,
    L=(A+B)/2, D=(A-B)/2, k=Gamma_pi+n_B*L, h=n_B*D.

Then substitution gives the **exact** time-varying mode equations:
    g' = 2*R - k*g - h*d
    d' =       - k*d - h*g
    P_pi := (dX/dt)_pi = D*g + L*d.

This is a re-expression of the unchanged author's literal code, not a proposed physical perturbation. The coefficients depend on original fully coupled X(t),T(t),n_B(t). No assumption that these backgrounds are constant is needed for this identity.

## 2. Theorem: equal-rate injection does not preserve equal density

At any above-floor state with n_minus=n_plus=c>0, we have d=0, g=2c. Thus

    d' |_(d=0) = -n_B*c*((1-X)*a(T)-X*b(T)).

The equal-density submanifold is not invariant whenever the bracket differs from zero. Its local exceptional condition is

    X_*(T)=a(T)/(a(T)+b(T)),

and for constant T this is a single, special X; instantaneously reaching it does not prove that a full evolving trajectory remains on that manifold.

**Robust sign window:** for any 0<X<=15/32 and all finite T>0,

    (1-X)*a(T)-X*b(T)
      > (1-X)*1.5mbarn - X*1.7mbarn
       = (1.5-3.2 X) mbarn
      >= 0,

with strict inequality even at the endpoint X=15/32 due Fc>1. Consequently d'|_(d=0)<0 for n_B,c>0. The subinterval 0<X<=0.45 gives the simpler positive margin (A-B)>0.06 mbarn and d'|_(d=0)<-0.06mbarn*n_B*c. These are coefficient-level bounds in author's NaturalUnits convention, not direct physical measurements.

**Finite interval sign result (conditional, stronger than instantaneous noninvariance):** For an actual above-floor solution on [t0,t1] with 0<X(s)<=15/32, T(s)>0, n_B(s)>0, g(s)>0 and d(t0)=0, variation of constants yields

    d(t) =
      - integral_[t0,t] exp(-integral_[s,t] k(u) du) * h(s)*g(s) ds < 0

for all t in (t0,t1] where coefficients are continuous. This holds along the **fully coupled** original background, not only fixed-X approximation. The proof uses only k(t) finite and h(s)>0. It does NOT claim that native Wu-Xu solutions satisfy every hypothesis over their entire PBH/BBN trajectories; all-clamped postev segments are explicitly outside this version's above-floor scope.

Thus a symmetric injection and even symmetric INITIAL pion populations do NOT justify identifying pion charge populations over time. It is not enough to set one common n_pi variable. Neither group rate T1 nor a frozen g alone fixes P_pi dynamically.

## 3. Normalized charge imbalance — exact cancellation of common decay

For g>0, set phi=d/g. Direct quotient differentiation of the exact two-mode equations gives

    phi' = -h*(1-phi^2) - (2R/g)*phi.

Common pion lifetime decay Gamma_pi cancels **exactly** in this ratio equation. The two forcing terms have distinct meanings: charge-asymmetric p/n scattering generates an imbalance even from phi=0 via -h, while equal source R drives the existing imbalance toward zero through -2R*phi/g when R>=0. At phi=0 in the robust sign window, phi'=-h<0. This is an exact source-typed statement and does not supply charge-conditioned emission yields or a PBH observable.

For fixed exogenous X,T,n_B and R>0 only, the two linear densities have positive unique stationary values

    n_minus_QSS=R/(Gamma_pi+n_B*A),
    n_plus_QSS=R/(Gamma_pi+n_B*B),
    n_minus_QSS/n_plus_QSS=(Gamma_pi+n_B*B)/(Gamma_pi+n_B*A),
    (d/g)_QSS = -n_B*(A-B)/(2*Gamma_pi+n_B*(A+B)).

In the sign window X<=15/32, the stationary n_minus_QSS/n_plus_QSS<1. This frozen-background QSS is NOT an asserted measured native solution or a validated adiabatic approximation. If an external symmetry condition allocated group total R_group as R_group/2 to each state instead of literal R_group to each, the *frozen-background* QSS ratio would remain unchanged but densities change in scale; exact coupled full-10D X(t) and Yp do not follow an exact half-scaling law.

## 4. Actual independent symbolic execution and provenance correction

On 17 November 2026, after original ROT002 publication, LT9 actually executed **local Python + SymPy 1.14.0**. The earlier LT9 ROT002 contained an overstatement that SymPy had already been run when it had NOT. The original ROT002 text was corrected **in a separate dated Git commit 8be849882f3dca9c6a8db151546eecc005e92dec** before this report; history preserves the original error, and the new literal explicitly says the SymPy ROT002 check was retrospective. This is not silent retroactive attribution of an earlier execution.

ROT003 further performed and passed SIX exact algebraic asserts for the transformed equations, the pion P term, the equal-density derivative and the QSS formulas; a SEVENTH actual SymPy assert verified phi' including exact cancellation of Gamma_pi. The returned stdout independently confirmed:
- p(A)-p(B) = 2*epsilon*((1-X)*a+X*b);
- original equal-state derivative d' = c*n_B*(X*a+X*b-a);
- local exceptional X = a/(a+b);
- symbolic current ROT003 six transformed and stationary identities PASS;
- normalized imbalance equation PASS, Gamma_pi cancels;
- at X=15/32, b=17/10 mbarn, (A-B)=(17/64)*(2*a-3)>0 for a>3/2 mbarn.

The exact calculations did NOT run Julia, BlackHawk, network source physics or new BBN observable. Execution surface: current ROT003 local container, not claims of independent family I3, author implementation or validated scientific prediction.

## 5. Maturity subtraction, scope and legitimate next use

- Algebraic invariant-submanifold check, diagonal charge-mode equations and integrating factors are **mature classical ODE operations**, no generic novelty. Original model and rate coefficients are Wu/Xu; physical charged-pion n<->p conversion is mature, see Kawasaki/Kohri/Moroi 2005.
- This is distinct from LT9 ROT002's pointwise **same g, different d -> different P** counterexample; distinct from SCOPE12 ROT003's inverse **(g,P) -> (n_minus,n_plus)**; distinct from Mech-S10 ROT002's E5 x p12 SOURCE interaction. It adds a finite-time noninvariance result and normalized charge-imbalance balance law for exact original full-state trajectories under an explicitly bounded above-floor regime.
- Do NOT infer that the author 10D model is mathematically invalid; it is well-defined. Do NOT infer author paper error, physical charge asymmetry of PYTHIA emissions, published Yp error, beta shift, historical Fig5 producer identity, physical T2R replica, novelty or a new PBH bound. Only original-code mathematical representation is tested.
- **One material owner/reviewer use**: If one proposes reducing the source output to a charge-blind pion total while retaining accurate neutron conversion, the two-state charge-imbalance mode is generally dynamically generated even from zero; it cannot be eliminated simply by assuming initial charge equality or identical literal injection. True reduction needs externally validated charge-resolved rate/cross-section averaging and trajectory-level source contract. Owner Badacz/Mech-S10, auditor REC13/AUD3, Moderator retain all decisions.
- Avoid further synthetic repetitions of the same quotient counterexample. Reopen only with a source-native charge-separated yield law, a physical averaging definition, validated native conditional T2R, or a concrete REV029 claim requiring this precise invariant-submanifold boundary.

FINAL: SOURCE_NATIVE_EXACT_MODE_NONINVARIANCE_PASS / SYMPY_1_14_RUN_VERIFIED / RETROSPECTIVE_ROT002_PROVENANCE_CORRECTION_RECORDED / PHYSICS_HOLD / NO_NEW_NATIVE_RUN / BW_NO_WRITE / REV029_NO_EDIT / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
