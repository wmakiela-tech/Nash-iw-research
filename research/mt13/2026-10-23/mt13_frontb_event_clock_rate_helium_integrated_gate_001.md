# MT13 — Four-cell source/dynamics/event-clock/helium target integration
Date 2026-10-23. RETURN_ID MT13-FRONTB-EVENT-CLOCK-RATE-MEMORY-HELIUM-CHAIN-001_20261023.
CLASS: exact classical ODE composition + synthetic tests; NO NOVELTY, NO CANON, NO EXEC, NO source-valid PBH/BBN, BW pending.

**Prior:** MT13 2x2 dynamic rate ledger: research/mt13/2026-10-23/mt13_frontb_exact_dynamic_factorial_interaction_ledger_001.md; LT5 event adjoint: research/lt5/2026-10-23/lt5_event_aligned_target_adjoint_exact_homotopy_and_fixed_temperature_source_gate_001.md. REC10 -> MECH-S7 ROT005 surviving hadrons, PRF11 R20 credits DAX-S7 for distinct helium observables.

**A1 exact event identity.** For four differentiable neutron histories X_j(t), each reaching the same target Tstar at its own unique time tau_j, define w00=w11=+1,w10=w01=-1. At any common reference t_ref, with I(t)=sum w_j X_j(t), exactly
I_event=I(t_ref)+sum_j w_j int_(t_ref)^(tau_j) Xdot_j(t)dt.
Proof: FTC for each branch. Thus fixed-time interaction may be opposite in sign to fixed-temperature interaction. LT5 already proved the underlying two-branch event-secant/adjoint; this is a 4-way source-typed composition, not new maths.

**B1 exact temperature-coordinate dynamics.** If each T_j strictly decreases from the same start temperature, let xi=Tstart-T, t_j(xi)=inverse clock and v_j=dt_j/dxi>0. For equations Xdot_j=u_j+A_j-(lambda_j+A_j+B_j)X_j define y_j=X_j(t_j(xi)), f_j=v_j(u_j+A_j), q_j=v_j(lambda_j+A_j+B_j); then y'_j=f_j-q_j y_j. Put L=y10-y00,M=y01-y00,I=y11-y10-y01+y00,Delta f=f11-f10-f01+f00 (likewise q). Exactly
I'=-q11 I +(Delta f-y00 Delta q)-M(q11-q01)-L(q11-q10).
Proof: subtract four affine scalar ODEs and regroup. Integrating factor exp[-int q11] yields exact three-term ledger at one common temperature. Delta f/q combine clock Jacobians AND direction rates: not a unique microscopic source interaction. Do not add A1 and B1 ledgers together (same signal counted twice).

**Analytic sharp synthetic counterexample.** X(0)=.5, u=lambda=0; positive constant (A,B): 00=(.2,.4),10=(.3,.5),01=(.4,.2),11=(.5,.3), all mixed rate-level Delta A/B=0. Exact X_j(t)=A/R+(.5-A/R)exp(-Rt), R=A+B. Distinct synthetic T_j(t)=2-c_j t, c00=1,c10=.8,c01=1.2,c11=.7; common final Tstar=1. I_time(t=1)=-.012728362331296428, clock contribution +.03610382848714655, I_event=+.023375466155850122. **Sign reversal from the clock plus dynamics, WITHOUT mixed directional A/B rate changes.** In a second clock-only example X_j=.3+.1t for all j: I_time=0 but I_event=.034523809523809526.

DOP853 common-xi integration: direct effective-rate +.05735254994580060; feedback-M -.03439166771481804; feedback-L +.00041458392486765; sum +.02337546615585021. 101-point max ledger error 8.61e-16, all 4 closed-form trajectories match <2e-13. This is math-only synthetic, not Wu-Xu/Julia.

**NEW external currentness crucial to target:** PRF11 R20 source triage credits DAX-S7 ROT29–33: corrected author arXiv v3 (2026-05-06) gives approximate standard He4 mass fraction Ymass=2x (x=Xn at Tnuc); JCAP 2026-02-17/arXiv v2 prints R=2x/(1-2x) (helium mass to remaining hydrogen mass); pinned public code 2025-12-30 uses C=2x/(1-x) (helium mass to original proton mass). For simplified all-neutrons-in-He4 stoichiometry x<.5, Ymass=R/(1+R)=2C/(2+C). These output types MUST NOT share the same observational likelihood without conversion. Corrected v3 text does not establish published Figure5 JLD2/run ancestry. FULL BBN network still required. Source: research/prf11/2026-10-23/IW_PRF11_R20_WUXU_HELIUM_SOURCE_VERSION_STOICHIOMETRY_AND_LIKELIHOOD_NONMAP_001_20261023.md.

**Existing one-source-run physical gate:** MECH-S7 original Julia 10D accepted-step run with Qspecies, survivor n_i, six A_i/B_i, source floor/emission, M<1e9g, t/a/T and own event tau_j, common physical interpretation, numerical endpoint error/temperature crossing, model-version helium transform and nuclear likelihood. REC10->MECH-S7 ROT005 frozen kinetics explicitly FAILS to reproduce observed opposite signs; not a replacement. Existing MT13/LT5 per-cell certified global event X error threshold for the reported opposite contrasts is <6.33356560558e-6, NOT passed.

**Verified cross-cell uptake**: LT5 ROT09 already used MT13 fixed-T numerical admission to derive event adjoint; MECH-S7 ROT005 uses REC10 survivor warning; PRF11 R20 builds on DAX source triage. Receiver adoption of this NEW synthesis is only PROPOSED. LT5 REV021 staged but not issued. KN11 BW source ingest != scientific acceptance. No new task cascade; autonomy preserved.
