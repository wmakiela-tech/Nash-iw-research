# REC10 ROT08 — Mech-S7 Front B: post-evaporation hadron memory

Date: 2026-10-23. Status: PASS_WITH_SOURCE_GUARD. NO_CANON / NO_EXEC / NO_NOVELTY / NO_PBH_BOUND / NO_PHYSICAL_UPGRADE. BW ingestion PENDING.
Read exact primary Mech-S7 report research/mech-s7/2026-10-22/mech_s7_frontb_common_background_target_gate_002.md (blob 765906aeb88aaac995cbf4c76fae7db1cbd27c31), reproduction script (blob c746b7b1f7d6eaa79b85df0634540ba5bdc06838), and Wu-Xu upstream pinned public main-scan.jl commit d395183674cace6c9906a8911bdeb7234ba4040d.

SOURCE-VERIFIED: Actual code extracts X_n by linear interpolation at fixed x=Q/T_nuc, T_nuc=0.078185270688319950 MeV; raw fixed-a contrast is not the native endpoint. The source flag PBH_evaporated switches OFF fresh PBH emission, but six pre-existing hadron populations remain evolved, and the neutron ODE retains their interactions. Hence manually setting ALL post-source hadronic forcing to zero in the Mech-S7 conditional replay is a load-bearing simplification, not the exact post-evaporation source law. Mech-S7 itself correctly labels the replay CONDITIONAL.

INDEPENDENT EXACT GATE: on a single common background, each branch r has X_r'=u-lambda X_r+f_r, f_r=(1-X_r) A_r-X_r B_r, where A,B are the hadron-induced directional neutron-conversion rates. For delta=X_paper-X_public, delta0=delta(t0), and Lambda(t,v)=integral_v^t lambda(z)dz, exact variation-of-constants gives
 delta(t)=exp(-Lambda(t,t0))*delta0+integral_t0^t exp(-Lambda(t,v))*(f_paper(v)-f_public(v))dv.
This is exact, not linearized. Therefore
 |delta(t)-delta_hadron_off(t)| <= H_delta(t)
 :=integral_t0^t exp(-Lambda(t,v))*|f_paper(v)-f_public(v)|dv.
The shared-background source-off sign is certified for native hadron dynamics if H_delta(t)<|delta_hadron_off(t)|. Without a bound on surviving hadron interactions, source-off alone does NOT certify the actual native sign.

ARITHMETIC READBACK of Mech-S7 fixed-T tables:
B_exec raw -1.898857e-5, common -1.640731e-5, background -1.607742e-6, residual -9.735097e-7 (closure within 8.3e-12).
B_sym raw +1.266713e-5, common +1.083653e-5, background +2.251028e-6, residual -4.204293e-7 (closure within 1.3e-12).
Shared-background accounts for 86.406% and 85.548% of recorded contrast magnitudes. The first saved source-off deltas and shared-background endpoints imply survival factors ~0.799408 (exec) and ~0.799213 (sym), consistent with the source-free scalar damping.

SUFFICIENT NUMERIC SIGN GATES on that fixed-background, fixed-T replay: H_delta <1.640731e-5 for exec; H_delta <1.083653e-5 for sym. Neither H_delta is bounded by accessible original accepted Julia steps. Archive-minus-conditional-replay residual is NOT a rigorous estimator of H_delta.

STATUS: source code and table arithmetic independently examined; archived ZIP bytes and original Julia solve NOT rerun. This is classical ODE Duhamel mathematics, not a physical PBH result. No manuscript/BW mutation, no new tasks. Reopen on actual accepted-step hadron trace, convergence evidence or source-law revision.

## Delivery receipt (2026-10-23)
Slack #iw-dispatch reply to original Mech-S7 rotation 002 thread, SENT and THREAD READBACK PASS:
https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1792710109710459?thread_ts=1792655697.199669&cid=C0BV1J3SYLT
GitHub publication and Slack delivery do not establish BW ingestion, Mech-S7 owner acceptance, physics or EXEC authority.
