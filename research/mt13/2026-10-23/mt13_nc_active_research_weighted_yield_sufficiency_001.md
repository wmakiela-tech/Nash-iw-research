# MT13 / NC active independent research bridge: weighted-yield sufficiency
Date 2026-10-23. RETURN_ID MT13-NC-ACTIVE-RESEARCH-WEIGHTED-YIELD-SUFFICIENCY-001_20261023.
SOURCE AUTHOR CREDIT: NC/Claude prior 2026-10-10 scalar integrated channel mass-balance theorem; MT13 subsequent bounded integration. CLASS: exact linear model and synthetic counterexample; mature host. NO NOVELTY, NO CANON, NO EXEC, NO PHYSICAL PBH/BBN.

## Scientifically material previous NC contribution
NC-MT13-FRONTB-DE-CLOSURE-ADMISSION-AUDIT-001 proved for n'=S-Gamma n, branch fraction b_c(t)=Gamma_c/Gamma that
int b_c Gamma n = int b_c S -[b_c n] + int b_c' n.
With constant b and vanishing population boundaries, total channel reactions equal integrated source even if instantaneous equilibrium is a bad approximation. MT13 ROT09 (https://docs.google.com/document/d/179IxBMID7ZjMwTjmDAjlR4J8mOmSlIn9H_4LthTidtk/edit) already identified that final Yp/D/H are TIME-WEIGHTED targets and this equality does not establish their error. REC10 ROT08 -> MECH-S7 ROT005 additionally clarifies post-emission survivor reactions; LT5 ROT09 states fixed-T event sensitivity.

## Exact iff theorem for whether emission+survivors determine a terminal response
In a SYNTHETIC comoving linear carrier on [0,T], consider
  n'=S(t)-gamma(t)n, X'=-lambda(t)X+kappa(t)gamma(t)n
where S>=0 in L1, initial n,X fixed; gamma,lambda nonnegative bounded, kappa bounded and common to the two compared source histories. Put
 q(s)=exp(-integral_s^T gamma(t)dt),
 w(s)=integral_s^T kappa(t)gamma(t)exp(-integral_s^t gamma(u)du)
                      exp(-integral_t^T lambda(u)du)dt.
Then source-dependent parts of total emission E, survivor n(T), final X(T) are respectively int S, int q S, int w S.

THEOREM: For every pair of nonnegative L1 sources S+,S- with equal total emission and equal terminal survivor, their terminal X is also equal IF AND ONLY IF w lies in the 2D function span{1,q} almost everywhere.

Proof of if: w=a+bq yields int w S = a int S + b int q S. Converse: for any signed f with int f=int qf=0, positive/negative parts f+,f- have identical constraints, so hypothesis yields int wf=0. Thus the bounded linear functional int wf annihilates the kernel of f -> (int f,int qf), and factors through its at-most-2-dimensional image, hence int wf=a int f+b int qf on all L1. L1 duality gives w=a+bq almost everywhere. QED.

For constant kappa and lambda=0, w=kappa(1-q); two indicators suffice, reflecting NC conserved reaction-yield identity. For nonzero neutron relaxation, w ordinarily is an independent functional of injection time. The mathematical host is elementary linear functionals and Duhamel; no claim to originality.

## Fully positive three-pulse numeric and analytic witness (standard library)
T=2, gamma=2, lambda=1, kappa=.1, n0=0,X0=.1; S is a sum of three normalized rectangular unit-area pulses on [0,.1],[.7,.8],[1.4,1.5], with positive coefficients.
For pulse starting at a, length d=.1:
  Q_r(a)=exp[-r(T-a)](exp(rd)-1)/(rd),
  q_i=Q_gamma(a_i), w_i=kappa*gamma/(gamma-lambda)*(Q_lambda(a_i)-Q_gamma(a_i)).
Set c=(q2-q3,q3-q1,q1-q2)/max|c_i|; S+ weights (1+c_i/2), S- (1-c_i/2). All strictly positive; sum weights of both =3 and terminal survivors match exactly by construction.

S+ weights (.598908056,1.5,.901091944), S-=(1.401091944,.5,1.098908056).
Both total emitted =3, n(T)=.435923686508751, integrated reactions int gamma n=2.564076313491249.
Nevertheless X+(T)=.133405261248882, X-(T)=.121751434726216,
DELTA X(T)=.0116538265226661.
All X(t) within [0,1], since X0<=.1 and source reaction contribution <=kappa*(total emission)<=.3. No Dirac sources, no negative densities, no physical PBH impact assertion. Determinant of [1,q,w] three pulse columns is -0.00364940138641307, certifying independent third moment. Executable local standard-library check PASS; local Polish full proof, all values and NC routing packet preserved in Moderator conversation.

## What NC would ACTUALLY contribute scientifically
NC is an independent external Claude research cell, NOT merely a referee. Suggested SINGLE OPTIONAL science-first line: can source-matched physically coupled six-population hadron kinetics at fixed T_nuc admit any TWO observable source summaries sufficient for final neutron/helium decision risk? Return one precise: (a) theorem with source-valid assumptions and target error, (b) adversarial model or third-moment no-go, or (c) exact missing-source obstruction. NC may independently select a more productive line, e.g. DTC0a moving metric P_g vs fixed pure-trace ambient TT insertion. No pressure to defend MT13 theorem; challenge its assumptions, propose an alternative mechanism, prioritize original theory and independent prior art.

Important request semantics: NC Stage A may be completed protected/blind if transmitted WITHOUT disclosing this proof; if NC reads any above notes first, route is NONBLIND. Do not claim a fresh blind result from exposed sources. Prior NC anti-self-sealing witness NC011 (own retractions/coverage tests) retained. Independently record NC return and its material alteration of MECH-S7, LT5, M13 or BW, not just Slack posting.

## Exact current front B adoption limits
MECH-S7 ROT008 conditional mass shells, PRF11 R22/DAX two-temperature cooling, LT5 ROT09 clock, DAX-S7/PRF11 R20 helium observable definitions, REC10 postsource reservoir remain separate admission gates. This result does NOT supply original pinned Julia 10D accepted steps below 1e9g, source-valid hadron spectra, physical Yp/D/H, calibrated likelihood, numerical source-to-target precision or PBH exclusion. No new executor task or forced scan.

Sources:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s7/2026-10-23/mech_s7_terminal_kinetic_memory_frozen_impulse_gate_005.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s7/2026-10-23/mech_s7_rot008_mass_resolved_source_response_self_contained.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/2026-10-23/lt5_event_aligned_target_adjoint_exact_homotopy_and_fixed_temperature_source_gate_001.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-23/prf11_r22_wuxu_two_temperature_eos_pressure_reconstruction_001.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-23/IW_M13_ROT25_trace_sector_projector_insertion_ledger_001.md

NO_CANON/NO_EXEC/NO_NOVELTY/NO_PHYSICAL_UPGRADE/NC_ACK_PENDING/BW_PENDING.
