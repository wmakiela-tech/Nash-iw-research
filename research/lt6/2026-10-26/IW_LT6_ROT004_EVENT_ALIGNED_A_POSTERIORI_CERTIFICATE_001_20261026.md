---
artifact_id: IW_LT6_ROT004_EVENT_ALIGNED_A_POSTERIORI_CERTIFICATE_001_20261026
created_at: 2026-10-26
origin_cell: IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_04 / LT6
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: MATURE_HOST_THEOREM_SYNTHESIS / SOURCE_TYPED_REPRO_PASS / REFEREE_PENDING
claim_ceiling: NO_MATHEMATICAL_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PBH_BBN_PHYSICS / NO_NATIVE_JULIA_10D / NO_PHYSICAL_SOURCE_CLOSURE
---

# LT6 ROT004 — From source-native ODE residual to event-aligned target uncertainty

**Scope:** finite smooth ODE, one certified crossing, no reset. First internal owner: LT5 §6.9a event-time adjoint (2026-10-23). LT6 ROT002–003 classical minimax LP and background transfer; MT14 ROT004 seven-window LP; Mech-S7 ROT026–028 conditional background-dependent source-target tests. This is NOT a theorem-priority or physical claim.

Let x'=f(t,x,theta), and xhat continuous piecewise C1 with certified residual r=xhat'-f(t,xhat,theta), error e0 at t0 and state Lipschitz L. Gronwall gives (for t0=0)

    ||x(t)-xhat(t)|| <= exp(L*t)*e0 + integral_0^t exp(L*(t-s))*||r(s)|| ds =: kappa(t).

For scalar guard phi(t,x)=0 let true H(t)=phi(t,x(t)), and suppose one TRUE isolated event tau in bracket I, |H'(t)|=|phi_t+phi_x f|>=m>0 WITH CONSTANT SIGN throughout I. If phi is L_phi-Lipschitz in x, root candidate tauhat lies in I and numerical guard residual r_ev=|phi(tauhat,xhat(tauhat))|, then

    |tauhat-tau| <= (r_ev+L_phi*sup_I kappa)/m.

For observable Q(t,x), true speed |f|<=F on I and Lipschitz constants L_Qx and L_Qt,

    |Q(tauhat,xhat(tauhat))-Q(tau,x(tau))|
      <= L_Qx*sup_I kappa + (L_Qt+F*L_Qx)*(r_ev+L_phi*sup_I kappa)/m.

Proof: Gronwall, state-guard Lipschitz, mean-value theorem for H, then triangle inequality on Q. These mature steps are exactly the missing *verification contract* for a source-native numerical claim. Accepted solver steps WITHOUT dense-output residual and root-isolation bounds do NOT satisfy the assumptions.

**Event derivative:** with z=partial_epsilon x, tau'=-(phi_x z+phi_epsilon)/(phi_t+phi_x f). For integral target J(epsilon)=integral_0^tau Ldt, derivative includes the boundary term L(tau)tau'. In the analytic 1D source x'=-x+epsilon, x(0)=1, event x=1/2, tau=log((1-epsilon)/(1/2-epsilon)), J=1/2+epsilon*tau. Hence J'(0)=log2; fixed-time derivative alone gives log2-1/2 and is WRONG for the event-aligned target.

**Executed synthetic verification**: with epsilon=.08 and surrogate xhat=x+.004 sin(5t), the exact event error is 0.00644835308246; direct certified upper bound 0.0118186166455; residual+Gronwall bound 0.1035494310814. For Q=x^2+t/2, actual target error 0.00322417654123 and direct specialized bound 0.00590930832274. Counterexample grazing guard (t-1)^2=epsilon gives tau=1-sqrt(epsilon), no uniform event-time Lipschitz bound at epsilon=0.

**Scientific stop:** this replay does not run the Wu–Xu source-native 10D Julia ODE, validate PBH emission below 1e9g, certify source event isolation and m, or derive physical Yp/DH. A nonlinear target bound additionally needs a source-valid Hessian remainder; the exact finite LP of ROT002 cannot substitute that.

Full Polish proof archived as five readback-verified parts in [Nash-Priv ROT004](https://github.com/wmakiela-tech/Nash-Priv/tree/main/living-theory/2026-10-26/ROT004). Updated [native REV024](https://docs.google.com/document/d/1ZwZSPGjiFrEgVoSDggNlvSSvmClVhEQUNg8lPscD6oc/edit) and its [full composite GitHub mirror](https://github.com/wmakiela-tech/Nash-Priv/tree/main/living-theory/2026-10-26/REV024). Exact tested script and JSON/manifest packaged in Moderator's checked ZIP.

**Mature literature:** verified residual a posteriori ODE error (2024) DOI 10.1007/s44207-024-00001-0; Kong et al. Saltation Matrices, Proceedings of IEEE 112 (2024), DOI 10.1109/JPROC.2024.3440211; Khan–Barton, IEEE TAC 2017 DOI 10.1109/TAC.2016.2644759. Internal priority stays with LT5 and owner cells. Public GitHub write and readback are NOT BW ingestion, referee acceptance or EXEC.
