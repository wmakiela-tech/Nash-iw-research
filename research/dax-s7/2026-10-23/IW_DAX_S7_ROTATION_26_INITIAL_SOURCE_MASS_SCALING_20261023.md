# DAX-S7 Rotation 26 — initial PBH source scaling

Source-code audit (Wu–Xu public main-scan.jl, magic): t_f=M_f/(gamma*m_Pl^2), H_f=1/(2t_f), rho_SM,f=3*M_Pl^2*H_f^2, rho_PBH,f=beta*rho_SM,f, n_PBH,f=rho_PBH,f/M_f. Hence n_PBH,f=3*beta*M_Pl^2*gamma^2*m_Pl^4/(4*M_f^3), i.e. n_PBH,f proportional to beta*M_f^-3 exactly for these initial conditions.

For per-PBH emission q_h(M_f) proportional to M_f^p_h in a specified mass branch, initial source S_h,f=n_PBH,f*q_h(M_f) proportional to beta*M_f^(p_h-3). Thus paper subedge p=-1.3 implies -4.3, public helper near -1.2 implies about -4.2. This is conditional and initial-time only, not a claim for source at common later cosmic time. A common M^-3 factor cancels from A/B and cannot by itself identify mass. Actual time-aligned trajectories require full executor; no Julia run, no Yp inference, no physical bound. Status EXACT SOURCE-CODE ALGEBRA / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY.
