# MT13 — Sharp moment bounds for positive hadron injection; local event-target residual
**DATE** 2026-10-23  **RETURN_ID** MT13-NC-LT5-SHARP-SOURCE-MOMENT-RECOVERY-AND-EVENT-RESIDUAL-001_20261023
**CELL** MT13 scientific programme integrator. **STATUS** exact classical conditional math; synthetic independent LP pass; mature prior art, NO_NOVELTY / NO_CANON / NO_EXEC / NO_SOURCE_VALID_PBH_BBN / NC_RECEIPT_PENDING / BW_PENDING.

## 1. Others first / source integration
- NC external Claude, first derived exact hadron-yield conservation for n'=S-Gamma*n, including integrated-channel boundary and branching-variation terms. Its channel event counts can be conserved despite poor instantaneous equilibrium, but cannot be promoted to weighted neutron Yp/D/H. Primary source: https://docs.google.com/document/d/179IxBMID7ZjMwTjmDAjlR4J8mOmSlIn9H_4LthTidtk/edit
- LT5 owns event-time adjoint for X(Theta=Theta_star): https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/2026-10-23/lt5_event_aligned_target_adjoint_exact_homotopy_and_fixed_temperature_source_gate_001.md
- MECH-S7 source-specific 7D conditional low-mass source controls: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s7/2026-10-23/mech_s7_rot008_mass_resolved_source_response_self_contained.md
- PRF11 R22 / DAX source-typed multi-temperature primordial cooling EOS: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-23/prf11_r22_wuxu_two_temperature_eos_pressure_reconstruction_001.md
- Previous MT13 NC-based qualitative moment sufficiency and event nonidentifiability: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/2026-10-23/mt13_nc_lt5_event_weighted_source_sufficiency_gate_001.md
- NC011 open μ2(G) necessity has ALREADY been solved by M13 ROT11 (2026-10-19). No repeating or reprioritizing that established result.

**New project-local utility:** turn qualitative nonidentifiability of two source moments into EXACT SHARP terminal target interval + optimal achievable minimax error, and quantify a separate LOCAL event-time residual. All underlying mathematics is mature.

## 2. Fully proved sharp interval and optimal recovery

Real nonnegative finite source measure S on [0,T], dynamics (impulses interpreted by convolution):
dn/dt=S-gamma*n, dX/dt=-lambda*X+kappa*gamma*n, n(0)=0, known X(0)=X0, gamma=2*lambda>0, kappa>0.
Define two accessible summary functionals E=int S>0 and N=n(T)=int exp[-gamma(T-s)]dS. NC's exact total reaction count is E-N, NOT an additional independent datum. Put a=exp(-gamma*T), so feasibility requires a*E<=N<=E.

Target is SOURCE-INDUCED increment J=X(T)-exp(-lambda*T)*X0, not the total physical Yp or D/H. Then EXACT SHARP bounds:
  J_low=2*kappa*sqrt(a)/(1+sqrt(a))*(E-N),
  J_high=2*kappa*(sqrt(E*N)-N).                                 (T1)
Every admissible positive S with these moments satisfies J_low<=J<=J_high. The endpoints are achievable by nonnegative finite measures and arbitrarily closely by ordinary nonnegative L1 source pulses.

Proof: let q(s)=exp[-gamma(T-s)] in [a,1]. Green kernel solves
  J=kappa*gamma/(gamma-lambda)*int [exp(-lambda*(T-s))-exp(-gamma*(T-s))] dS
   =2*kappa*(int sqrt(q)dS-N).
Jensen on sqrt(q) yields int sqrt(q)dS<=sqrt(E*N). For the lower bound, the concave sqrt lies ABOVE the chord through q=a and 1:
 sqrt(q)>=(q+sqrt(a))/(1+sqrt(a)), so
int sqrt(q)dS>=(N+E*sqrt(a))/(1+sqrt(a)).
Sharp upper: S concentrated at s*=T+(1/gamma)*ln(N/E). Sharp lower: S consists of impulses at s=0,T with masses E*(1-N/E)/(1-a) and the remainder. Both give SAME E,N. A finite width, positive source approximates extremal measures while preserving E,N by small adjustments of positions/weights. QED.

**Minimax reconstruction from E,N alone**: the midpoint (J_low+J_high)/2 achieves minimal worst-case absolute error (J_high-J_low)/2, because the opposite endpoint sources yield exactly the same measurements. Even a nonlinear estimator cannot improve the pointwise minimax radius. This gives an actionable admission rule: if required target accuracy is epsilon, two moments are enough in this toy class iff width<=2*epsilon.

Toy benchmark: T=1,gamma=2,lambda=1,kappa=.12,E=2,N=1-exp(-2)=.8646647167633873:
  J_low=.07328128435323855,
  J_high=.10808999788857884,
  width=.03480871353534029,
  minimax estimator=.09068564112090870,
  minimax error=.017404356767670146.
Uniform S=2 gives J=.09589833621449473; initial X0=.1 adds the known free contribution .0367879441171442, hence total X(T) interval [.11006922847038278,.14487794200572307]. NO physical BBN interpretation.

**Independent controls executed**: three separate discretized positive-source moment LPs with 121,401,1201 time nodes. All recover J_low to <1e-9; upper gap decreases 2.36e-6,2.02e-7,1.29e-8 as grid refines. 10,000 random positive source histories all satisfy exact analytic inequalities. The two analytic extremizers have EXACT equal emission/survivor moments. Full runnable local Python script mt13_nc_sharp_moment_bounds_20261023.py in Moderator conversation.

## 3. Exact local event-target residual (do NOT use T1 for a moving endpoint)

For an ENDOGENOUS temperature process Theta with transversal crossing Theta(tau[S])=Theta_star and J_event[S]=X_S(tau[S]), LT5's event sensitivity at baseline S0 is
 DJ_event[S0]nu = int_I w_event(s)dnu(s),
 w_event(s)=K_X(tau0,s) - [Xdot0(tau0)/ThetaDot0(tau0)] K_Theta(tau0,s).
Suppose only moments int_I dnu and int_I q(s)dnu are logged; consider signed source perturbations nu with total variation norm <=B on compact early source interval I strictly prior to tau0. Standard Hahn-Banach + Riesz duality gives EXACT:
 sup_{||nu||_TV<=B, int nu=int q nu=0}|int w_event dnu|
  = B * inf_{a,b in R} ||w_event-a-b*q||_Linf(I).                (T2)
Proof: C(I)/span{1,q} has quotient norm equal to RHS and dual is annihilating signed finite measures. This is the best-information residual for the DERIVATIVE, not a finite-amplitude GLOBAL event-target bound. A positive baseline S0 imposes additional admissibility for S0 +/-epsilon*nu; atomic signed witnesses must be smoothed/downsized to preserve S>=0.

Numerical example from prior NC+LT5 toy:
n'=S-2n, h'=S-.7h, X'=-X+.24n, Theta'=-1.37+.4h, S0=2, X0=.1, Theta0=2, event Theta=1. tau0=.939219864613131. On early interval I=[0,.7], q(s)=exp[-2(1-s)].
Discrete LP finds a~.0966408958453, b~-.0825444023693 and best uniform residual d~.0030553367 per unit signed TV. A 3-point approximate annihilator at s=(0,.4118382844,.7), weights (-.2907071772,+.5,-.2092928228) has EXACT zero sum and zero q moment, residual ~.003055336692; dense-grid upper ~.003055336837, less than 2e-9 discrepancy. This is a numerical instance of an exact duality identity, NOT a rigorously certified closed-form numerical constant, and it is not the physical two-T EOS.

**Interpretation:** the exact positive-source interval in (T1) and the local signed-perturbation event residual (T2) have different domains/quantifiers. NEVER infer full nonlinear event bounds or PBH constraints from T2's linearization.

## 4. Consequences for existing cell work / science integration
- **NC** owns prior conservation theorem; invited to independently attack the assumptions, derive source-constrained multi-species versions, or reject this as textbook convexity. NC remains an AUTONOMOUS scientific partner, not forced reviewer. No confirmed external Claude receipt; exposure is NOT blind.
- **MECH-S7** ROT008 finds much of mass localization inherited from SOURCE-ONLY fluence. E and N alone might still leave wide target uncertainty despite a convincing source-mass distribution. The source-native mass/time/species response kernel and valid S family are necessary before computing physical bounds. Continue existing original Julia 10D source admissibility, NO added broad scan.
- **LT5** target-relative sufficiency gains an exact scalar interval with sharp minimax radius; event chapter gets (T2) but only as a *local* theorem. Author chooses integration; staged REV021 not thereby released.
- **PRF11/DAX** source EOS multi-temperature and observational Ymass/C/R typing remain separate. Synthetic Theta is not a legitimate cooling law.
- **KN11/BW** optional one derived impact link NC source -> MT13 new target moment bound -> LT5/MECH owner decision. No second registry; ingest not scientific acceptance.
- **SW/REC10** independent challenge may test exact domain only when owner's planned work needs it.

**Mature hosts (no originality):** Jensen inequality, extreme-point moment theory: Winkler 1988 *Extreme Points of Moment Sets*, DOI 10.1287/moor.13.4.581; Pinelis 2016 *On the extreme points of moments sets*, DOI 10.1007/s00186-015-0530-0; Hahn-Banach/Riesz; optimal recovery (J Complexity 62 (2021) 101503, DOI 10.1016/j.jco.2020.101503).

**Hard STOP:** formulas need nonnegative unrestricted sources with exact two moments, gamma=2lambda for T1, no nonlinear feedback; actual Wu-Xu strongly source-constrained, EOS evolving, six species, beta heating, nuclear network, real helium likelihood and Julia original 10D remain unverified. No unique identification of hadron mechanism, physical Yp/D/H, source-valid PBH exclusion, novel mathematics, canon, EXEC or BW adoption.

END / NO_NEW_TASK_CASCADE / CELL_AUTONOMY_PRESERVED.
