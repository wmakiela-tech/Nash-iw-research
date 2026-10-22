# MT13 / Front B — exact single-history directional-rate nonidentifiability, two-excitation certificate
Date: 2026-10-23
RETURN_ID: MT13-FRONTB-DIRECTIONAL-RATES-SINGLE-TRAJECTORY-NONIDENTIFIABILITY-001_20261023
SCIENCE: classical finite-dimensional deterministic identifiability / source-native limitation of reduced neutron equation.
CLAIM CEILING: FOUNDATION / NO NEW JULIA SOURCE RUN / NO PHYSICAL PBH OR BBN ENDPOINT / NO NOVELTY / NO CANON / NO EXEC.
BW: PENDING. Manuscript owner LT5; executor owner MECH-S7; independent referee REC10.

## Existing results and source status
MECH-S6 four Wu-Xu law x charge-map numerical executor comparison:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s6/2026-10-19/mech_s6_frontb_wuxu_source_law_x_charge_map_2x2_dynamic_comparator_001.md
MECH-S7 ROT002 correct fixed-T conditional common-background source-off comparison:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s7/2026-10-22/mech_s7_frontb_common_background_target_gate_002.md
MECH-S7 ROT003 six signed directional channel rates and cancellation conditioning:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s7/2026-10-23/mech_s7_frontb_signed_channel_conditioning_terminal_gate_003.md
REC10 ROT08 source audit: fresh PBH emission OFF does not remove populations of hadrons produced earlier; hadron conversion can survive and source-off replay is CONDITIONAL:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/rec10/2026-10-23/rec10_rot08_mech_s7_hadron_memory_gate.md

New QUESTION: can even perfectly observed full X_n(t) identify separately hadronic proton->neutron (A) and neutron->proton (B) rates, or certify absence of post-emission memory? What extra legal observable would separate them?

## Exact typed carrier
Fix the common physical-time background and known source-neutral Standard Model contributions u(t),lambda(t). Consider the scalar neutron fraction X(t) in (0,1) with directional nonnegative external time-dependent rates A(t),B(t), obeying
 Xdot=u-lambda*X+(1-X)*A-X*B.                                            (1)
Rates A,B in this theorem are unrestricted nonnegative time functions, exogenous and SHARED ACROSS preparations. This broad class is NOT claimed to coincide with Wu-Xu's restrictive microscopic six-population kinetic source family. If actual hadron populations couple to X, the shared-rate second-experiment condition must be re-audited, not assumed.

## Theorem 1: complete non-identifiability of ONE neutron history
For any C1 observed x*(t) in (0,1), set
 F*=x*dot-u+lambda*x*.
All nonnegative rate pairs producing EXACTLY that x* at its initial condition are parametrized by arbitrary time function R(t) satisfying
 R >= R_min=max(0, F*/(1-x*), -F*/x*),                                   (2)
 A_R=F*+x*R,     B_R=(1-x*)R-F*.                                          (3)
If A,B is one such pair and k(t)>=0, the alternative
 Atilde=A+k*x*, Btilde=B+k*(1-x*), Rtilde=R+k                            (4)
has identical entire observed X(t)=x*(t), while changing A+B and generally q=A/(A+B).
Proof: F*=(1-x*)A-x*B=A-x*(A+B). Solve for A,B at fixed R; nonnegativity is precisely (2). Substitution in (1) verifies x*, and ODE uniqueness at fixed preparation gives the same whole trajectory. Eq (4) is the R->R+k special case. QED.
If R>0, q=x*+F*/R. Thus R->infinity drives q toward x* without changing the original record. A single X trajectory determines net signed forcing F, not R nor directional A,B; even continuous zero-noise observation is insufficient in this broad carrier.

## Exact post-emission memory counterexample
Take u=1/2, lambda=1, initial X(0)=1/2, no NEW hadron injection.
H0: A=B=0.
H1: A(t)=B(t)=(3/2)*exp(-t), modeling a purely SYNTHETIC decaying residual rate without fresh injection, NOT a reconstruction of the six Wu-Xu species.
BOTH give X(t)=1/2 for all times. But total hadronic directional reaction R differs: 0 versus 3 exp(-t). Hence 'source injection off + identical X history' does not logically imply 'hadron conversions off'.
For a distinct hypothetical initial X(0)=0.6 under the same exogenous rates,
 X_H0(t)=1/2+0.1 exp(-t),
 X_H1(t)=1/2+0.1 exp(-t-3*(1-exp(-t))).
At t=1 these are 0.536787944117 and 0.505522377696 respectively. Differing histories separate the models. This is NOT an asserted cosmologically legal state preparation.

## Theorem 2: two independently prepared initial neutron histories identify the rates if they share exogenous coefficients
Let x1,x2 be solutions of (1) for same u,lambda,A,B on one identical background, with x1(t0)!=x2(t0). Set d=x1-x2. Then
 ddot=-(lambda+R)*d and d(t)=d(t0)*exp[-integral_t0^t (lambda+R)].
Therefore exact recovery from two differentiable histories:
 R= -(dot d)/d-lambda,
 A=dot x1-u+lambda*x1+R*x1,    B=R-A.                                 (5)
No d crossing zero at finite t for integrable coefficients.
From TWO endpoint differences, even without derivatives, ONLY the integrated R is recovered:
 integral_t0^t1 R= -log(abs(d(t1)/d(t0))) - integral_t0^t1 lambda.         (6)
Proof: subtraction of common-coefficient equations, integration, algebra. QED.
Failure type: first theorem is single-history nonidentifiability; this second theorem is conditional two-excitation identifiability, not an unconditional physical instrument.

## Precision qualification of the second-history formula
Suppose exact |d|>=d_min>2eps, measured |hat x_i-x_i|<=eps and |hat x_i dot - xi dot|<=eps_prime; assume lambda known and |lambda+R|<=L. Taking Rhat= -(dhat dot)/dhat-lambda, direct quotient subtraction gives
 |Rhat-R| <= [2*eps_prime+2*L*eps]/[d_min-2*eps].                        (7)
The reconstruction becomes unstable as distinct preparations converge (d_min small). This is a deterministic sufficient bound, not a statistical or physical data error bar.

## Independent numerical witness
Local Python NumPy/SciPy, two genuinely different positive time-varying rate models:
 x*(t)=0.4+0.04*sin(t), u=0.3+0.02 sin(t), lambda=1.2+0.1*cos(t),
 R1=2+0.2*cos(t), F=x*dot-u+lambda*x*,
 A1=F+x*R1, B1=(1-x*)R1-F,
 k=0.9+0.2 sin(t), A2=A1+k*x*,B2=B1+k*(1-x*).
Positivity of all A1,B1,A2,B2 checked on 1500 points. Two independent solve_ivp solves from same x*(0) follow x*(t) with max deviations 1.824e-13 and 2.125e-13 on [0,2]; solve from x*(0)+0.03 yields different output, exact integrated sensitivity matches to 2e-10, two-preparation inversion R,A,B validated at 15 times. All tests PASS. Raw code in companion GitHub test and moderator local attachment. Neither source model is a real PBH run.

## Source/target science gate
- MECH-S7 recovered A,B,F and six channel contributions on saved ABOVE-TABLE samples. This is precisely the *extra information* the reduced neutron history alone cannot yield.
- To attribute endpoint sign interaction to pbar/nbar or pion/kaon sources in the unresolved M<1e9g window, a full accepted-step 10D trace must record rates, populations, source law/map branches, fixed background/time target, floor and solver controls. A four-cell endpoint without rates is NON-IDENTIFYING of the channel-level mechanism in the broad admissible rate class.
- Do not reinterpret the two-preparation thought experiment as a legal PBH intervention. When A,B depend on hadronic states, which in turn respond to X, rate sharing across preparations may fail; the actual alternative discriminator is source-native additional observables.
- REC10 showed 'PBH evaporation source OFF' is not 'postsource hadronic forcing OFF'; the exact H1 countermodel makes this nonimplication explicit without asserting Wu-Xu source validity.
- Source law under M<1e9g, source-to-hadronization mapping, publication-run genealogy, solver global accuracy, physical helium and deuterium likelihood remain open; no PBH exclusion bound is released.
- Existing MT13 source/proxy interaction numeric precision gate epsilon_X<6.3335656e-6 is a separate question from structural rate identifiability; solving one does not solve the other.

## Prior art subtraction
Mature hosts are standard two-state reversible reaction kinetics, inverse identification of linear time-varying ODEs, experimental excitation and structural identifiability.
Stanhope, Rubin and Swigon, Identifiability of Linear and Linear-in-Parameters Dynamical Systems from a Single Trajectory, SIAM J Applied Dynamical Systems, DOI 10.1137/130937913, https://epubs.siam.org/doi/10.1137/130937913.
Identifiability analysis of linear ordinary differential equation systems with a single trajectory, Applied Mathematics and Computation 430 (2022) 127260, DOI 10.1016/j.amc.2022.127260, https://www.sciencedirect.com/science/article/pii/S0096300322003344.
NO novelty of formula (2)-(7) claimed. Value is a narrowly scoped falsifier to source-mechanism attribution in the project, not a new physical law.

STATE: EXACT_CLASSICAL_THEOREM / SYNTHETIC_TEST_PASS / MECH-S7_SOURCE_EXECUTION_REQUIRED / BW_INGEST_NOT_ASSUMED / NO_CANON / NO_EXEC / NO_NOVELTY.
