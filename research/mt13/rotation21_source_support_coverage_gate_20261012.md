# MT13 Rotation 21 — Front B three-domain support admission

2026-10-12. Temporary LT coverage. NONCANON, NO EXEC, no physical BBN bound.

Source-native basis: MECH-S6 https://docs.google.com/document/d/1DVxm-RWjZ7nyjZHCR_32KHONQKSX6Qdc5YfiycAz8JI/edit and XH-S3 https://docs.google.com/document/d/1_cw8TQ1QqHUiztoQgm2DrwDLCaHzmHXBBjm5A7b2NbA/edit . They recover Wu-Xu v2 generator, with source table PBH masses 1e9 to 4e12 g, BlackHawk v2.3 instantaneous spectra and BBN-PYTHIA hadronization with primary energy ceiling 1e5 GeV. Source regeneration below 1e9 g is software-addressable but not automatically source-valid.

THREE SUPPORT GATES: mass-grid validity, primary Hawking spectral energy support, and hadronization/secondary-species energy support. E2a executor rerun does not imply E2b source-supported regeneration.

EXACT SCALING: T_BH proportional to M^-1, so for fixed Emax, chi(M)=Emax/T_BH(M)=chi_e M/M_e. To preserve chi_e at M<M_e, Emax_required(M)=Emax_e M_e/M. For Emax_e=1e5 GeV and M_e=1e9 g: 6e8 g -> 1.667e5 GeV; 3e8 g -> 3.333e5 GeV; 1e8 g -> 1e6 GeV. These exceed existing 1e5 GeV hadronization-table support; raising the run Emax alone does not repair physical coverage.

INDEPENDENT DERIVATION: Let H_M(E)>=0 denote primary spectral number density and f_h(E)>=0 the expected species-h secondary yield per primary. The full source is q_h(M)=integral_0^infty H_M(E) f_h(E)dE. The truncated executor-supported part is q_h^<=integral_0^Emax H_M(E)f_h(E)dE. The missing source is exactly integral_Emax^infty H_M(E)f_h(E)dE. A bound on the missing primary NUMBER fraction, integral_tail H / integral_all H, is not a bound on the missing hadron-source fraction unless a quantitative bound on f_h in the tail is supplied. For example, f_h(E)=K on the tail and 1 below yields arbitrarily large missing hadron fraction as K grows, despite fixed small primary tail fraction. This is a mature positive-integral counterexample, not a claim about actual QCD species yields. A source certificate requires a species-specific tail bound or physically supported high-energy fragmentation.

H8R-C remains SOURCE_INTERFACE_UNRESOLVED, following Rec9/NC correction and INT7 linear-consistency gate. LT4 packet 003 is current planned succession, not activated. DRAFT018 active with overlays. P2 retained/P3 fallback; TPE HOLD; REV021 not created.
