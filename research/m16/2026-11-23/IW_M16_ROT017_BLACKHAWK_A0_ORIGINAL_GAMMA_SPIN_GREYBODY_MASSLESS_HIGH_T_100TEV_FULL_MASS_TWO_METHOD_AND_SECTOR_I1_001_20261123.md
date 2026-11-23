---
artifact_id: IW_M16_ROT017_BLACKHAWK_A0_ORIGINAL_GAMMA_SPIN_GREYBODY_MASSLESS_HIGH_T_100TEV_FULL_MASS_TWO_METHOD_AND_SECTOR_I1_001_20261123
date: 2026-11-23 Europe/Warsaw
cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_11 / M16
authorization: Moderator 2026-11-23: Sam prowadź prace zamiast czekać na badacza
status: FOUR_COMPLETE_A0_200_GAMMA_SOURCE_ROWS_PLUS_FITS_DIRECT_READ / TWO_MASS_INTEGRATION_ORDERS_ACTUALLY_EXECUTED / DAX_SECTOR_DIFFERENT_CELL_AGREEMENT / GLOBAL_FM_AMPLITUDE_RESIDUAL_1P177PCT_OPEN
scope: SOURCE_GAMMA_GREYBODY_RELATIVISTIC_MASSLESS_APPROXIMATION / NOT_NATIVE_BLACKHAWK_HADRON_GENERATOR / NOT_NATIVE_JULIA_BBN
ceiling: NO_ACTUAL_BBN_Y / NO_PBH_BETA_BOUND / NO_AUTHOR_ERROR_ESTABLISHED / NO_EXTERNAL_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_BW_WRITE
---

# M16 ROT017: spin-resolved BlackHawk original-family gamma tables and actual-energy primary source support beyond 100TeV

## 1. Actual originals, custody, owner FIRSTNESS

Author Wu-Xu original pinned commit d395183674cace6c9906a8911bdeb7234ba4040d: entire valid_hadrons_from_BlackHawk.ipynb has BlackHawk BBN/PYTHIA PRIMARY grid 5..100000GeV and 100 masses 1e9..4e12g, Git blob 8a10396ae771b17059808fc2b91235dd194cba8d. Original tool_script-BlackHawk_extension.jl at commit d395183 lines64-75 explicitly sets interpolation_method=0 (LINEAR), Kerr metric=0 and spin=0. Original main-scan.jl author cutoff Mstop=M0 exp(-20) for j22/j62. These are author-source facts, not model assumptions.

Author source: https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/tool_script-BlackHawk_extension.jl
Notebook: https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/valid_hadrons_from_BlackHawk.ipynb

Historical-family external BlackHawk mirror code cewasiuk/Spin-and-Charge-BH-Evolution pinned commit 0bd531eb948bd11549535a563b55f0d23671589b: src/primary.c exact gamma lookup logic using x=2 E M G, C linear or logarithmic interpolation with Kerr high/low asymptotic fits. Original author modified BlackHawk_inst.c d395183 lines309-370 supplies 15 SM primary DOF and graviton = spin0 1 Higgs, spin1/2 90, spin1 27, spin2 2. The gamma numerical tables of the RELATED HISTORICAL MIRROR are NOT directly SHA matched to official BlackHawk v2.3 release tar. Source-typed equivalence remains conditional. The full original fM file (767767 byte, 1000x51) in that mirror WAS already independently SHA identified as genuine original v2.3 input by DAX-S10 ROT007. Do not extend that identity to unverified gamma file bytes.

Mirror source: https://github.com/cewasiuk/Spin-and-Charge-BH-Evolution/tree/0bd531eb948bd11549535a563b55f0d23671589b/src/tables/gamma_tables
Mirror C consumer: https://github.com/cewasiuk/Spin-and-Charge-BH-Evolution/blob/0bd531eb948bd11549535a563b55f0d23671589b/src/primary.c
Mirror source G constant: https://github.com/cewasiuk/Spin-and-Charge-BH-Evolution/blob/0bd531eb948bd11549535a563b55f0d23671589b/src/include.h
Author original degrees: https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/external_code/BlackHawk_v2.3-hack/BlackHawk_inst.c

ACTUALLY FETCHED FOUR FULL gamma 50a×200x files and all fits files, parsed all headers and a*=0 200 grid rows, DID NOT infer input from filename. Gamma Git blobs: spin0 79b7811b3ff9342ae4b9287939d703b63aa18aaa; spin1/2 e7f2661bfe08e06a20a79e9ee9e581edbf04d04c; spin1 21c92c95324855527a55d6537651a9635f90ac06; spin2 8bd80b7ddc9fb0a4a78c6b123c15807c4d0d1267. Fit blobs: spin0 46bf24fb369a605482e9dbd0592e957e563ce93b; spin1/2 85e2e21df4aa3db6ddde54a22254b38a37ebe2ba; spin1 def5e0ed5addd8abbfec80c850bf94ab2f48ccfd; spin2 8fd7b29d7c2826c29c70b7675bb564ba3853d262.

FIRSTNESS retained: PRF13 ROT017 (2026-11-13) FIRST original j22~81.4% hadron-number subgrid and exact C-infinity nonidentifiability; M16 ROT014 independent source I1 only. Mech-S8 ROT015 (11Nov) FIRST ideal Bose/Fermi pointwise primary Emax stress, and M16 ROT016 FIRST M16 full-mass ideal thermal test. Mech-S10 ROT020 (22Nov) FIRST original source 10000 primary spectra high-energy original primary energy fraction integrated sampled mass and off-grid conditional bound. REC14 ROT009 FIRST exact j22/j62 G_PG2 mass window gap. DAX-S10 ROT007 FIRST genuine fM mirror hash; DAX-S10 ROT009 FIRST 16 original primary sector contributions and initial graviton G_DEP. BADACZ REVIEW122 FIRST original full hadron energy ledger. M16 does not claim these discoveries or external physical novelty.

## 2. Reproducible physics and exact tabular integral

For a Schwarzschild a*=0 PBH, dimensionless gamma-source x=2 E M G=E/(4pi T_H). The original BlackHawk Kerr primary.c returns d2N/(dt dE) = DOF_s gamma_s(x)/(2pi). Gamma tables at 0.01<=x<=5 already include the thermodynamic Hawking occupation factor. Do NOT multiply by another Bose/Fermi distribution. In the original author's default interpolation_method=0, gamma_s(x) is piecewise LINEAR in x, and source low-x fit x<=0.01 is 10^(a_s log10 x + b_s). Its x*gamma_s and x^2*gamma_s moments integrate ANALYTICALLY on each one of 199 segments; the low-x power segment is integrated exactly too.

The source x>=5 Kerr asymptotic uses gamma_s(x)=10^(a_s x+b_s+c_s cos(omega_s x)+d_s sin(omega_s x)). Its weighted moment beyond5 has analytic POSITIVE UPPER bound by replacing the oscillatory terms with their amplitude norm: sum_s DOF_s * 10^(b_s+sqrt(c_s^2+d_s^2)) * exp(-5 lambda_s) * (5/lambda_s+1/lambda_s^2), lambda_s= -a_s ln10 >0. Direct independently executed audit obtains sum upper bound 6.59932730105619e-24 of x*gamma energy moment versus full weighted moment 0.10596712905920753: RELATIVE < 6.227711706116824e-23. Thus truncating a*=0 integration at x=5 cannot explain any percent-scale mismatch INSIDE THESE FIT FUNCTIONS. It says nothing about whether the physical gamma files are correct.

Define w(x)=x sum_s DOF_s gamma_s(x), I=sum_s DOF_s int_0^infinity x gamma_s dx. For initial M0 and finite source stop Mstop=M0exp(-20), the high-energy primary E>100TeV fraction in the ALL-MASSLESS SOURCE GAMMA APPROXIMATION is R=(1/[(M0-Mstop)I]) integral_Mstop^M0 [integral_{cM}^infinity w(x) dx] dM, with c=Emax/(4pi T_H(1e9g)*1e9g). Independent FUBINI form uses J(u)= int_0^u x*w(x)dx + u int_u^infinity w(x)dx and R=[J(cM0)-J(cMstop)]/[(cM0-cMstop)*I]. Both original C default TABLE+LOW fit moments are exact algebra for source interpolation. Separate mass-first Simpson 500 and 2000 panels explicitly executed with independently evaluated tail from table primitives; relative Fubini vs 2000-panel <=2.0363e-10 for BOTH j22 and j62. This validates integral arithmetic, NOT the high-T massless physics approximation or historical gamma data identity.

## 3. Main NEW quantitative source-supported CONDITIONAL findings

| Source-authored object | j22 original mass 1.121174456e9g | j62 original mass 3.494213660e9g |
|---|---:|---:|
| Integrated primary E>100TeV, a*=0 tabulated gamma ALL-MASSLESS high-T approximation | **47.6679810039%** | **15.3423562565%** |
| Previous ideal massless BOSE spectral control M16 ROT016 | 36.0627130393% | 11.5953627050% |
| Of above modelled high-E emission, share produced when M<1e9g (NOT directly Wu-Xu generator mass table) | **99.56680751%** | **99.25971190%** |
| Fubini relative to independently executed 2000-panel mass Simpson | 4.32723e-11 | 2.03626e-10 |

Massless gamma source at a single instant M=1e9g has E>100TeV power tail 2.795543956%, at M=5e8g 52.939626583%, M=2.5e8g 94.899071884%, M=1e8g 99.810986914%. These single-M gamma values computed in V8 before public artifact write, actual source massless approximation. They are NOT guaranteed bounds for the full physical spin/threshold-dependent BlackHawk generator.

## 4. EXTERNAL different-cell original-primary sector I1 and unresolved amplitude

From complete original gamma rows and actual Wu-Xu source DOF: source normalized spin power shares spin0=0.0176515442764; spin1/2=0.8736802946210; spin1=0.1077577363032; grav spin2=0.00091042479930.

Translate to six original BlackHawk PRIMARY channel groups using original species DOF: QCD [6 quarks spin1/2 72 + gluons spin1 16] = 0.7628006720247; charged leptons [12 spin1/2] = 0.1164907059495; neutrinos [6 spin1/2] = 0.0582453529747; W/Z/H [9 spin1 + 1 spin0]=0.0535707897108; photons [2 spin1]=0.0079820545410; gravitons [2 spin2]=0.0009104247993. Compare to DAX-S10 ROT009 ACTUAL independently read source 100x100x16 primary spectrum at j62 published ROUND values (0.7628012, .1164909, .0582455, .0535691, .0079819, .00091136). Six normalized sector differences max absolute **1.6897108264e-6 of total power**, i.e. **0.0001689711 percentage points**. This is a substantive independent second-source test of source gamma spin+DOF READ, but NOT a proof of original official gamma-file byte identity or a new raw 100x100x16 spectrum run. DAX original FIRST maintained.

ABSOLUTE POWER MISMATCH: weighted moment I=0.10596712905920753. With actual source BlackHawk C Newton G macro from src/include.h lines20-31, G=6.708609145836679e-39 GeV^-2, reconstructed gamma high-T f(M) = 9.368419485678995e73 GeV^4 whereas actual original v2.3 a*=0 fM plateau is 9.47999e73 GeV^4. Ratio = **0.9882309459903433**, i.e. source gamma reconstruction is **1.17690540096567% lower** than the authenticated fM. This material residual is NOT fixed by the high-x>5 tail (<6.23e-23 fraction), and it prevents an EXACT-NATIVE-BLACKHAWK energy-power claim. Massless approximation (including W/Z/H modes and all source species), historical gamma-table provenance, independent production methods and source-compatible normalization require separate study. This 1.177% is not a formal error bar on the normalized high-energy fractions.

Potential G_DEP bounded observation: massless gamma model gravitational primary POWER share 0.09104248%; if gravitons are not promptly thermalized in SM plasma, a single full injected-power thermal source is structurally distinct from deposited energy. BUT this spin2 source result was already anticipated and first measured by DAX ROT009 actual initial 0.072..0.090% in finite grid and is not a newly validated full-trajectory physical deposition rate. No spontaneous assumption of 5.8% neutrino loss; free-streaming energy still gravitates.

## 5. Reproducibility and epistemic ceilings

ACTUALLY EXECUTED in connected V8: original four complete source 50x200 gamma and fit files DIRECT READ, four a0 rows and fits parsed, exact 199-segment C-linear integration, exact low-x fits, Fubini mass energy and separate 500/2000-point Simpson mass integration, full six-sector DOF crosscheck; physical source Newton G correction applied in a sequenced source+certificate repository update after actually computing G formula from src/include.h. A separate Node process has NOT been executed; independent empirical physical generator has NOT been run. Published replayable standalone JavaScript embeds ALL 200 x gamma values for a0 + fit coefficients for each of four spin channels, not falsely the other 49 Kerr parameter rows; original full source git blobs recorded and no network needed for replay.

Public pinned code (updated correct source G; final git blob c9a945466a4a6e3c7e0c15d4aef7a00c2de47c6d, 20296 chars; FULL READBACK PASS):
https://github.com/wmakiela-tech/Nash-iw-research/blob/ca3eeaf1f30becf7aa3595cbe9531e14552a6d99/research/m16/2026-11-23/code/m16_rot017_blackhawk_a0_greybody_exact_tabular_massless_reproducer.js

Final machine-source certificate after source Newton G update (Git blob 0ff4ee88be351f8f486ead094610f97cddd2060d, FULL READBACK PASS):
https://github.com/wmakiela-tech/Nash-iw-research/blob/7ee04002be7cf1eaacdb83cf7614b9869cc391b7/research/m16/2026-11-23/data/m16_rot017_blackhawk_a0_greybody_exact_tabular_certificate.json

Source earlier ROT016 ideal numerical PDF or graph not substituted; original M16 ROT016 report remains historical. No direct Gamma-family source SHA identity to official BlackHawk v2.3 tar, no full native PYTHIA hadronization below M=1e9g, no PRyMordial or Julia/BBN reexecution. The massless source gamma spectral partition is a scientific method advancement WITHIN NASH, not proven general novelty or a new physical PBH exclusion.

NEXT: to convert this from source-supported extrapolative high-T spin spectrum to full actual G_EC+(b) test, independently obtain+verify the actual Wu–Xu BlackHawk v2.3 gamma files and rerun original BBN PYTHIA generation below 1e9g with primary energy grid extended above 1e5GeV, matching old charge+binning semantics; compare all original secondary energy-resolved channels and stage-specific n/p response. Explicitly keep W/Y beta likelihood separate, preserve source firstness and require prereg+error budgets.

ROT017_END SOURCE_GAMMA_FOUR_SPIN_A0_200ROW_EXACT_INTERPOLATION_PASS / MASS_FUBINI_VS_SIMPSON_MAX2P04E_MINUS10 / SIX_PRIM_SECTOR_DAX_SOURCE_CONCORDANCE_MAX1P69E_MINUS6 / ABSOLUTE_FM_1P1769_PERCENT_OPEN / REAL_BEYOND_GRID_SECONDARY_HADRON_BBN_OPEN / NO_PHYSICAL_PBH_BOUND / NO_AUTHOR_ERROR_ESTABLISHED / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_NOT_WRITTEN.