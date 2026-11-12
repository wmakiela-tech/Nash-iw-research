---
artifact_id: IW_MT15_ROT010_WUXU_THERMO_ORIGINAL_1000ROW_INDEPENDENT_JS_WOLFRAM_NULL_REPLICATION_001_20261112
created_at: 2026-11-12
origin_cell: IW_MT_SUCCESSOR_14 / MT15
exposure: PUBLIC
document_type: INDEPENDENT_ORIGINAL_SOURCE_NUMERICAL_REPRODUCTION_AND_EXACT_SOURCE_SYMBOLIC_AUDIT
status: AUTHOR_1000x3_JS_GAUSS_2_4_8_PASS / AUTHOR_1000x3_NATIVE_WOLFRAM_SIMPSON_4_16_PASS / SYMPY_SYMBOLIC_PASS
claim_ceiling: SOURCE_V2_ZERO_PBH_THERMO_PROXY_ONLY / NO_ORIGINAL_JULIA_10D_RUN / NO_HADRON_ENERGY_OR_Yp_OR_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# MT15 ROT010 — independent source-table and symbolic controls of Mech-S9 Wu–Xu entropy, neutrino and baryon nulls

## SOURCE FIRST / priority ledger

ORIGINAL physics source: Quan-feng Wu and Xun-Jie Xu, *Primordial Black Holes Evaporating before Big Bang Nucleosynthesis*, JCAP 02 (2026) 063, DOI https://doi.org/10.1088/1475-7516/2026/02/063 , original arXiv v3 https://arxiv.org/html/2509.05618v3 Sec 2.1 Eq 2.7 and Appendix A (A.1–A.3).

ORIGINAL code: public author repository Fenyutanchan/Primordial-Black-Hole immutable code-v2 commit d395183674cace6c9906a8911bdeb7234ba4040d:
- arXiv-2509.05618/data/ext/N_around_m_e.csv — exact 1000-row x 3-column [T MeV, g_rho, g_s] array, author Git blob 93f2494f026c5d0587ea40fe08bb938dd9d01fa8;
- arXiv-2509.05618/main-scan.jl — author Git blob b368ba55d5a493f7bc185909730f7fe5691f10d6; source zero-PBH energy RHS line85 and source physical n_gamma, n_B lines64–65;
- arXiv-2509.05618/tool_script-N_relativistic_species.jl — author Git blob 0437c032bdc4bafca6cb634c0db4cd2c46fb7efc, source g_rho and g_s are LINEAR INTERPOLATIONS of their values in log T within each original 1000 table-knot cell.
The author code-v2 / article-v3 and historical FINAL JCAP Figure 5 build are NOT proven executable-identical. The original author has priority; no external article critique is communicated to authors.

PROJECT OWNER FIRST: Mech-S9 (human-activated 12 Nov 2026) ROT002 FIRST isolated the source-code zero-PBH EOS / entropy mismatch and the 1000-row 1.046638 scale-factor ratio. Mech-S9 ROT003 FIRST articulated the physical Appendix A two-temperature neutrino null and the distinct fixed-eta baryon-number null including the decomposition into 2.489421 ordinary photon-number and 1.146541 entropy-drift factors. Previous AUD1 ROT031/032 FIRST caught the unrelated helium Y_P neutron fraction-vs-ratio discrepancy, Mech-S8 ROT020 acknowledged source v2/JLD2 and held physical bounds. Native solver original Badacz, E4 physical owner Mech-S9, source custody KN13. MT15 is ONLY independently replaying and testing these already identified owner nulls and does NOT claim their firstness.

## Exact equations and independent symbolic check

Let q_rho=d ln g_rho/d ln T and q_s=d ln g_s/d ln T. For the code's zero-PBH source condition n_PBH=0 and rho_SM proportional to g_rho(T) T^4:

f_code := d ln rho/d ln a = -4 + q_rho/(3+q_s) (verified directly at original Julia line85).

Article v3 Eq2.7 says g_s(T) a^3 T^3 constant; it instead implies
f_adiab := -3(4+q_rho)/(3+q_s).

Exactly, without perturbative linearization:
f_code - f_adiab = 4(q_rho-q_s)/(3+q_s).

Define L(T)=ln(a_code(T)/a_i) by integrating the inverse-temperature source ODE:
d ln a_code/d ln T=(4+q_rho)/f_code, starting T_i=1 MeV with L(T_i)=0.
The article entropy counterpart is
L_adiab(T)=ln(T_i/T)+(1/3)ln(g_s(T_i)/g_s(T)).

For temperatures on the article Appendix A.1 first branch, T_nu proportional to g_s(T)^(1/3) T, the normalized neutrino comoving product is
R_nu(T)=a_code(T) T_nu(T)/(a_i T_nu,i)=exp[L(T)-L_adiab(T)].
Article Appendix A.3 requires this to be unity in its specified adiabatic, no-neutrino-reheating limit. This is THE SAME energy/entropy null written in a second observable interface, NOT a second independent defect.

Separate source code line65 sets n_B_code(T)=eta_B*n_gamma(T) with FIXED eta_B=6.1e-10 and n_gamma proportional T^3. In the frozen zero-PBH, net-baryon-conserving comparator the comoving physical baryon number would be constant. The code-proxy normalization therefore obeys:
R_B(T)=a_code(T)^3 n_B_code(T)/(a_i^3 n_B_code(T_i))=exp(3L(T))*(T/T_i)^3
= [g_s(T_i)/g_s(T)] * R_nu(T)^3.
Exact symbolically,
d ln(a^3 n_B_code)/d ln a
= 3 q_rho(4+q_s)/[(3+q_s)(4+q_rho)].
SymPy source-free local algebra ran on these symbolic identities and returned exact zero residuals.

The factor g_s_i/g_s_T arises from ordinary photon-number change across electron-positron entropy transfer even with a PERFECT adiabatic background. Therefore R_B being 2.854 is NOT wholly a consequence of f_code-f_adiab: factorization must NOT be collapsed.

## Independent original-data source execution

Actually fetched 1000x3 author table and exact main-scan.jl plus N interpolator source through authenticated GitHub connector. Independently coded connected JS (no borrowed Mech S9 calculation code) per-knot local q_rho(T), q_s(T), d ln a/d ln T with separate 2-node, 4-node and 8-node Gauss-Legendre integration over each original log-temperature segment.

Then a SECOND executable mathematical language was used: native Wolfram Language evaluator actually ran an independently implemented per-knot composite Simpson quadrature with 4 and 16 panels, receiving the full 1000-row original numerical source table as numeric matrix literals, without previous JS numerical results as computational input.

- Max abs difference of JS Gauss 2 vs 4 on ln a across all nine temperatures: 4.769518113789672e-13.
- Max abs difference of JS Gauss 4 vs 8: 6.661338147750939e-16.
- Max abs difference of Wolfram Simpson 4 vs 16: 3.8058445284150366e-13.
- JS baryon factorization max residual abs: 1.5543122344752192e-15.
- Wolfram final R_nu=1.046638021704486 and R_B=2.8542233308289706, agreeing with independent JS 1.0466380217044864 and 2.854223330828976 at floating precision.
These are numerical integration consistency checks, not certified enclosures of real 10D trajectories or independent experimental replication.

Source table original g_s(1 MeV)=10.560555317546175, g_rho(1 MeV)=10.55866630203338; at Tref=.07818527068831995MeV g_s=4.242172521488243 and g_rho=3.722254946361439. First Appendix A.1 branch holds at the source reference and at initial T_i=1 since g_s/10.75 < 1.

| T [MeV] | R_nu = aTnu normalized | R_B = comoving n_B_code normalized | n_B_conserved/n_B_code at T, normalized to equal at Tref |
| ---: | ---: | ---: | ---: |
| 1.000000 | 1 | 1 | 2.854223331 |
| .800000 | 1.000101306 | 1.010263060 | 2.825227848 |
| .600000 | 1.000405547 | 1.032604674 | 2.764100729 |
| .500000 | 1.000794119 | 1.055219045 | 2.704863358 |
| .300000 | 1.003893255 | 1.188486819 | 2.401560780 |
| .200000 | 1.010949156 | 1.445547051 | 1.974493552 |
| .150000 | 1.020057832 | 1.777663209 | 1.605604097 |
| .100000 | 1.037517565 | 2.466633922 | 1.157132927 |
| .0781853 | 1.046638022 | 2.854223331 | 1 |

At Tref, exactly via independently evaluated original source values:
R_B_adiab= g_s(1 MeV)/g_s(Tref) = 2.4894214613038206;
R_entropy = R_nu^3 = 1.1465408229163783;
R_B_code = 2.854223330828976.

Full source-temperatures, ln scale factor, g_s and all component factors are available as adjacent MT15 ROT010 JSON, which was published with exact GitHub body readback PASS and all three original author Git blob identities.

## What this does and does NOT establish

PASS: owner Mech-S9 ROT002 and ROT003 two mathematical source-null calculations reproduce independently to machine arithmetic. They are conditional upon reading the earlier author's Julia RHS and the later article Appendix A entropy, neutrino and conserved baryon specifications as one intended null contract. If code includes intentional nonadiabatic two-temperature physics or uses eta_B as an intentionally time-dependent proxy, that modeling interpretation must be sourced rather than silently relabeled a physical violation.

NOT DONE: actual author Julia 10D system, BlackHawk/PYTHIA spectra, Tnuc self-consistent rerun, neutron proton Yp, C1–C4 pilot science, real nuclear network, actual JCAP Figure 5 production identity, physical PBH beta contours. Original Badacz PREREG062 first native four variant S1 parser FAIL happened BEFORE magic()/ODE; independent local calculation cannot advance that. No physics change or author correction authorized.

Reproducing a source-tied scalar thermal identity by JS+Wolfram is a numerically useful audit, NOT an independent refereeing signature of physical source truth. The 1.046638 and 2.854223 factors are NOT physical measured entropy production or baryon creation; they are code–article conditional diagnostics. No new original mathematical or physics novelty, no task cascade, and no BW write claim.

END: ORIGINAL_AUTHOR_1000x3_TWO_RUNTIME_SOURCE_NULL_PASS / 9_TEMPERATURE_ROWS / SYMBOLIC_EXACT_CONSISTENCY_PASS / MECH_S9_FIRSTNESS_RETAINED / NO_JULIA / NO_PHYSICAL_BBN_PBH / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_PENDING.
