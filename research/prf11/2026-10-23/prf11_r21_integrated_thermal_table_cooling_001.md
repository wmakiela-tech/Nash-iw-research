# PRF11 R21 — source-table integral of Wu–Xu cooling (23 Oct 2026)

CLASS: exact conditional source-table diagnostic; NO_CANON / NO_EXEC / NO_NOVELTY / NO_PBH_BOUND. BW/owner acceptance unknown. Source: Wu–Xu commit d395183674cace6c9906a8911bdeb7234ba4040d, data/ext/N_around_m_e.csv 1000 rows, Git blob 93f2494f026c5d0587ea40fe08bb938dd9d01fa8. Same-table no-PBH comparison, NOT source 10D Julia execution.

OTHERS FIRST: DAX-S7 ROT34–35 discovered code vs adiabatic cooling mismatch and evaluated local r-s on 999 source cells; these findings belong to DAX. LT5 ROT09 established event-aligned adjoints. MECH-S7 ROT004–005 and MT13 diagnosed distinct mass and hadron source/kinetic errors. PRF11 R20 reconciled author's later arXiv-v3 helium-formula correction, unrelated to cooling.

Source main-scan.jl computes r=dln(g_rho)/dlnT, s=dln(g_s)/dlnT, and C_code=dln(rho)/dln(a)=-4+r/(3+s)-dM_PBH/dt*n_PBH/(H*rho). In PBH-FREE limit C_code=-4+r/(3+s). The source thermodynamic table N_around_m_e.csv is interpolated linearly as g_rho,g_s against ln(T/MeV); source T_nuc=0.07818527068831995 MeV. Ideal source rho=(pi²/30)g_rho*T^4.

Mature adiabatic comparator: S_tab=g_s*T^3*a^3 conserved, hence C_ad=-3(4+r)/(3+s). DAX exact local residual: C_code-C_ad=4(r-s)/(3+s). Exact source-table differential identities:
  dln(a_code)/dlnT=(4+r)/[-4+r/(3+s)]
  dln(a_ad)/dlnT=-(3+s)/3
  dln(S_tab)_code/dln(a)=4(r-s)/(4+r).
Only the tabular PROXY S_tab is described; this is not a proof of genuine physical entropy production, in particular near neutrino decoupling.

SOURCE-TABLE INTEGRATION: normalize a at T_i=1MeV, integrate along fixed original 1000-row table to T_f=T_nuc with per-knot quadratures:
 ln[a_code(T_f)/a_i]=2.8982739261612003
 ln[a_ad(T_f)/a_i]=2.8526907830819157
 Delta_ln_a=0.04558314307928457
 a_code(T_f)/a_ad(T_f)=1.046638021704485
 S_tab_code(T_f)/S_tab_code(T_i)=exp(3*Delta_ln_a)=1.146540822916374.
Starting at 0.5MeV instead yields a_ratio=1.0458075261646624, S_tab_ratio=1.1438136861353014. None of these is an inferred actual percent error in Yp, Xn, physical entropy, PBH beta or solver output.

Independent numerical controls: directly integrate the difference of the two dln(a)/dlnT functions; at T_i=1MeV Delta agrees with separate integrals to 6e-16. The adiabatic independent endpoint identity ln[a_ad(T_f)/a_i]=ln(T_i/T_f)+ln[g_s(T_i)/g_s(T_f)]/3 agrees to <9e-16. Per-knot Gauss-Legendre and Simpson integration agree ~1e-15. Each quadrature cell avoids derivative jumps at original log-interpolation knots.

DISTINCT BARYON PROXY: the same public source uses n_B=eta_B*n_gamma with constant eta_B=6.1e-10 and n_gamma proportional to T^3. Across e+e- annihilation, photon comoving number changes. If n_B is intended to represent conserved baryon number, then n_B*a^3 should stay constant but the SOURCE PROXY instead gives
  [n_B*a^3]_f/[n_B*a^3]_i = (T_f/T_i)^3 exp(3*2.8982739261612003) = 2.854223330835094.
With adiabatic a(T) but same constant eta_B prescription the factor is g_s(T_i)/g_s(T_f)=2.489421461303821. Their ratio 1.146540822916374 isolates the extra cooling-law factor. This is two separate normalization obligations, NOT baryon creation. A conserved-baryon ratio eta_B(T) must scale as [a(T_ref)T_ref/(a(T)T)]^3.

EVENT-CLOCK CONDITIONAL: if PBH source is absent and H(T)=sqrt[rho_SM(T)/(3M_Pl^2)], elapsed fixed-temperature time is proportional to integral from lnT_f to lnT_i of -[dln a/dlnT]/[T^2 sqrt(g_rho(T))] dlnT. Same source table gives ratio Delta_t_code/Delta_t_ad=1.029326177252028 from 1MeV to T_nuc; 4- and 8-point knotwise Gauss quadrature agree <5e-15. This is NOT an actual PBH-affected event-time difference nor an Xn error; LT5 ROT09's event-aligned adjoint is needed for coupled dynamics.

MATURE HOSTS: Tong, Cambridge Cosmology Ch2 https://www.damtp.cam.ac.uk/user/tong/cosmo/cosmohtml/S2.html ; Steigman 2012 neutrinos and BBN DOI 10.1155/2012/268321 (baryon-to-photon eta constant AFTER electron-positron annihilation); Rafelski et al 2025 DOI 10.1140/epjs/s11734-025-01470-w (adiabatic cooling); Entropy 26(11)947, DOI 10.3390/e26110947 (effective g_s vs g_rho and neutrino separation). None grants novelty.

SOURCE LINKS: https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl ; https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/tool_script-N_relativistic_species.jl ; https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/data/ext/N_around_m_e.csv .

STOP: source has a distinct approximate 1000-point rho->T inverse interpolation, not replayed. No Julia PBH/no-PBH full solver, no original archived event or network, no source-valid radiation/hadron injection. No real physical entropy or baryon nonconservation inferred. Source table diagnostic only; no new task assigned.