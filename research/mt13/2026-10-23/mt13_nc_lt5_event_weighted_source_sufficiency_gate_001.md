# MT13 — NC × LT5: event-weighted source sufficiency, sharp information obstruction
**2026-10-23** | **RETURN_ID** MT13-NC-LT5-EVENT-WEIGHTED-SOURCE-SUFFICIENCY-GATE-001_20261023
**CLASS** exact classical sensitivity theorem + positive-source synthetic witness + independent ODE check. NO SOURCE-VALID PBH/BBN, NO NOVELTY, NO CANON/EXEC, BW and NC adoption pending.

## Source-first project integration, attribution and correction
**NC**, earlier October 10 DE-closure audit, first established for n'=S-Gamma*n the exact channel balance integral Gamma_c*n = integral b_c*S - [b_c*n] + integral b'_c*n, with explicit distinction between total reaction count and temporally weighted neutron target. MT13 ROT09 reviewed and preserved NC ownership:
https://docs.google.com/document/d/179IxBMID7ZjMwTjmDAjlR4J8mOmSlIn9H_4LthTidtk/edit
**MECH-S7 / Rec10** independently exposed surviving hadron reactions after injection off. MECH-S7 ROT008 source-mass window shows conditional 7D sign stress dependence, not original 10D:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s7/2026-10-23/mech_s7_rot008_mass_resolved_source_response_self_contained.md
**LT5 ROT09** owns exact event-aligned target/adjoint physics typing:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/2026-10-23/lt5_event_aligned_target_adjoint_exact_homotopy_and_fixed_temperature_source_gate_001.md
**MT13 previous NC-based theorem**: for a FIXED-TIME terminal linear target, emission + survivor moments suffice for all positive sources iff w in span{1,q}, with a three-rectangle witness (separate earlier deliverable):
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/2026-10-23/mt13_nc_active_research_weighted_yield_sufficiency_001.md
**PRF11 R22 + DAX ROT34-39**: source-pinned Wu-Xu thermal table encodes a two-temperature EOS/pressure host, not naive one-T entropy formula; never map this toy temperature to that EOS:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-23/prf11_r22_wuxu_two_temperature_eos_pressure_reconstruction_001.md
This note combines NC's moment adequacy with LT5's event derivative. None of the ingredients is novel general mathematics.

## Exact model and theorem
Fix scalar continuous dynamics on [0,1.2]:
 n'=S-gamma*n,  h'=S-mu*h,  X'=-lambda*X+kappa*gamma*n,  Theta'=-c+beta*h.
n(0)=h(0)=0, X(0)=.1, Theta(0)=2. Positive source S is exogenous. The synthetic heating reservoir h is NOT physical photons/neutrinos. The terminal event is Theta(tau[S])=1, crossing transversely Theta_dot(tau)!=0, and J[S]=X_S(tau[S]).

At a baseline S0 and tau0, linearize the four-state ODE to source perturbation f. If K_X(t,s), K_Theta(t,s) are fixed-time Green sensitivities to unit source at s, then by IFT:
 Dtau[S0]f= -(int_0^tau0 K_Theta(tau0,s)*f(s)ds)/Theta_dot0(tau0),
 DJ[S0]f=int_0^tau0 w_event(s)*f(s)ds,
 w_event(s)=K_X(tau0,s) - [X_dot0(tau0)/Theta_dot0(tau0)]*K_Theta(tau0,s).  (1)
Proof: differentiate the event constraint, then X(tau); eliminate time sensitivity. Valid as FIRST-ORDER local relation, not global linearity of event J[S]. For this constant coefficient carrier and s<tau:
 K_X=kappa*gamma/(gamma-lambda)*(exp[-lambda(tau-s)]-exp[-gamma(tau-s)]),
 K_Theta=beta/mu*(1-exp[-mu(tau-s)]).

Two logged source summaries at common reference t_ref=1 are E(S)=int_0^1 S(t)dt, n_S(1), with kernels 1 and q(s)=exp[-gamma(1-s)]. Restrict all perturbations f to J=[0,.7], strictly BEFORE tau0 and where baseline S0>0. Then:
**LOCAL MOMENT SUFFICIENCY IFF**: the first derivative DJ[S0] is determined by DE and Dn(1), for all bounded supported perturbations, iff w_event restricted to J is in span{1,q} a.e. (2)
If not, choose bounded signed f in joint kernel of both summary moments but with int w_event f!=0 (annihilator of finite-dimensional span). Sources S0 +/- epsilon*f remain positive for small enough epsilon, have EXACTLY equal E and n(1) because those summaries are affine, but J[S0+epsilon f]-J[S0-epsilon f]=2epsilon DJf+o(epsilon) !=0.
This is classical functional factorization and event-time differentiation. In the instantiated model w_event contains 1, exp(s),exp(2s),exp(.7s) on J with a nonzero exp(s) term; it cannot lie in span{1,exp(2s)}. Thus the two summaries are locally insufficient even with full linear-source accuracy, zero noise and a transversal event.

## Reproduced strictly positive three-pulse witness
Parameters gamma=2,mu=.7,lambda=1,kappa=.12,beta=.4,c=1.37; S0(t)=2. Three disjoint equal-area rectangles b_i(t)=12.5 on [a_i,a_i+.08], a=(.05,.30,.57). Let
 q_i=[exp{-2(1-a_i-.08)}-exp{-2(1-a_i)}]/(2*.08);
 v=(q2-q3,q3-q1,q1-q2)/max_i |...| =(-.6453557639085848,1,-.354644236091415).
Positive sources S_plus=2+.1*sum(v_i b_i), S_minus=2-.1*sum(v_i b_i); source minimum .75.

EXACTLY by linearity and sum_i v_i=sum_i q_i v_i=0:
 E_plus(1)=E_minus(1)=2;
 n_plus(1)=n_minus(1)=.8646647167633873;
 integral_0^1 gamma*n_plus = integral gamma*n_minus =2-n(1)=1.1353352832366128 (NC conservation);
but heating reservoir h differs and end event clock differs. Analytic closed-form values:
 tau_plus=.9378513082740388, tau_minus=.9405867484726412;
 X_plus(tau_plus)=.12845487256066163, X_minus(tau_minus)=.12779495181023773;
 event target difference +.000659920750423898.
At the SAME t=1 neutron values are .13309356544117723 and .13227899522210068; their difference .00081457021907655. Thus the event-clock correction to the DIFFERENCE equals -.00015464946865265; does not vanish although the two integrated emission/survivor summaries agree.
Baseline tau0=.939219864613131, Theta_dot(tau0)=-.819335958473488. The three effective source-kernel moments at that crossing are [.08222611676090004,.07733866027224719,.059140862108342344], and their dot product with v gives exact local slope .003299596012579266. Checked against +/- epsilon central differences for epsilon=.1,.01,.001. Both temperatures decrease strictly, X remains in (0,1), and pulses end before both events. This is mathematical witness, not BBN.

**Reproduction:** independent piecewise DOP853 solve_ivp integrations for S_plus,S_minus with explicit boundaries of all rectangular injections vs closed-form convolution and event-root calculation; agreement of event time and terminal X better than 4e-11, all checks PASS. Executable supplied as a separate code artifact and full 11k-character Polish report in Moderator conversation.

## Direct scientific effects and NC independence
- **NC**: active independent science role, not merely a final referee. Its old channel-yield theorem is a primary input to this stronger event-target obstruction. Bounded independent question: for actual multihadron source/kinetic and EOS carrier, do legal low-dimensional sufficient source moments exist for Xn(Tnuc), or is a full temporal reaction/source history indispensable? NC is free to develop a different better hypothesis/host; prior NC audit was NOT a blind check. No direct NC receipt or activation claimed.
- **MECH-S7**: existing original source-native accepted-step Julia 10D test should retain species/populations, A/B, emission time/mass, actual temperature clocks and full target output. Its conditional mass-fluence localization and integrated hadron event counts do not by themselves certify Xn(Tnuc). No new run asked beyond original Front B work.
- **LT5**: optional one short theorem and positive-source counterexample in Chapter 6/7 illustrating distinction: integrated yield sufficient for SOME source queries, but non-sufficient for event target; original editorial authority preserved.
- **PRF11/DAX**: thermodynamic two-temperature table and actual EOS clock remain necessary source-law gates. Synthetic Theta here cannot replace them.
- **KN11**: link NC source and MT13 consequence as separate events in existing BW after source validation; no inferred owner adoption.
**Host subtraction**: conventional IFT, linear systems Green kernels, functional linear dependence, event/saltation sensitivity (e.g. Nonlinear Analysis Hybrid Systems 31 (2019), DOI 10.1016/j.nahs.2018.07.003). No NASH mathematical priority, physical inference or closed Wu-Xu source model.

STATUS: EXACT_LOCAL_THEOREM / POSITIVE_SYNTHETIC_COUNTEREXAMPLE / INDEPENDENT_ODE_PASS / NC_AS_ACTIVE_RESEARCH_PARTNER / NC_ACK_PENDING / BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC / NO_PHYSICAL_UPGRADE.
