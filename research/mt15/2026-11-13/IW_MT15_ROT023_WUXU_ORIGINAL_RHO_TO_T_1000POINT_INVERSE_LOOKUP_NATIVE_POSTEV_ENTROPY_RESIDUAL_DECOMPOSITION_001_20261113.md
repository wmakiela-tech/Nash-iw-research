---
artifact_id: IW_MT15_ROT023_WUXU_ORIGINAL_RHO_TO_T_1000POINT_INVERSE_LOOKUP_NATIVE_POSTEV_ENTROPY_RESIDUAL_DECOMPOSITION_001_20261113
date: 2026-11-13
origin_cell: IW_MT_SUCCESSOR_14 / MT15
exposure: PUBLIC
type: INDEPENDENT_ORIGINAL_AUTHOR_SOURCE_INVERSE_LOOKUP_RECONSTRUCTION_AND_ACTUAL_NATIVE_10D_POSTEV_COMPARISON
status: ORIGINAL_THERMO_1000ROW_GIT_BLOB_PASS / ORIGINAL_SOURCE_INVERSE_LOOKUP_PREFIX_RECONSTRUCTION_PASS / GAUSS8_SIMPSON32_PASS / 16_ACTUAL_NATIVE_ROWS_PASS / SOURCE_LIMITED_CLEAN_REPLAY_PASS
claim_ceiling: SOURCE_AUTHOR_CODE_V2_ONLY / NO_ACTUAL_JULIA_SOLVER_ERROR_BOUND / NO_PHYSICAL_Yp_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# MT15 ROT023 — Original Wu–Xu rho-to-T inverse lookup explains little of the actual native j22 postevaporation entropy residual

## 1. Original source and scientific firstness

ORIGINAL author source: Quan-feng Wu and Xun-Jie Xu, JCAP 02 (2026) 063, original author public repository Fenyutanchan/Primordial-Black-Hole frozen at commit d395183674cace6c9906a8911bdeb7234ba4040d. Original full source 1000×3 table arXiv-2509.05618/data/ext/N_around_m_e.csv Git SHA1 blob 93f2494f026c5d0587ea40fe08bb938dd9d01fa8; directly fetched, read and SHA-locked in the connected original GitHub computation. Original code tool_script-N_relativistic_species.jl Git blob 0437c032bdc4bafca6cb634c0db4cd2c46fb7efc provides both original forward logarithmic-temperature linear g_rho,g_s interpolants and a separate function make_from_rho_to_T(), which tabulates 1000 geometric T knots from 1e-5 to 1e3 GeV, evaluates rho=(pi²/30)g_rho(T) T⁴, then linearly interpolates log10 T against log10 rho; the inverse extrapolates linearly. Original main-scan.jl blob b368ba55d5a493f7bc185909730f7fe5691f10d6 lines62/77–85 evaluates that inverse and the source no-PBH equation.

FIRSTNESS: Mech-S9 ROT002 FIRST established this original code-v2 entropy/adabatic EoS null, Mech-S9 ROT003 separate baryon/photon source null, REC11 ROT021 and KN13 ROT017/018 independent checks, MT15 ROT010 direct 1000-row independent source null. Mech-S9 ROT013 FIRST actually ran original 10D one-j22 Julia 10000-sample native source. MT15 ROT022 first within this MT15 line paired that actual native source trajectory with the continuous source EoS integral and corrected its V002 low-T quadrature test in V003. INT9 ROT030 FIRST independently alerted about the V002 source-knot bug before V003 owner confirmation. ROT023 is a distinct direct SOURCE 1000-node INVERSE-LOOKUP test, not discovery of the existing nonadiabatic source equation or original physics. All prior owners and author firstness preserved.

NATIVE original source used: Mech-S9 GitHub Actions run 43436800793 artifact 14045176436, UNMODIFIED ZIP SHA256 71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486 (713794 bytes), original 10000×19 CSV SHA256 45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1. ZIP CRC and original 16/16 SHA256 provider manifest PASS. Source first zero PBH sample 8545 Tref=1.48260941885709 MeV, last native sample10000 T=.00810973699892033 MeV. No new Julia execution.

## 2. Exact code-typed mathematical distinction

For nPBH=0, original author code has

    d ln rho_SM/d ln a = f(T) = -4 + q_rho(T)/(3+q_s(T))

with q_rho=d ln g_rho/d lnT and q_s=d ln g_s/d lnT. The ideal analytical inverse of rho(T)=C g_rho(T)T⁴ would give alpha_ideal=d ln rho/dlnT=4+q_rho. But the ORIGINAL code uses its separate log-rho/log-T piecewise-linear inverse lookup. On inverse knot cell j, the exact slope of the reciprocal lookup law is the constant chord

    alpha_LUT,j=(ln rho_(j+1)-ln rho_j)/(ln T_(j+1)-ln T_j),

not the derivative 4+q_rho(T). Therefore the code-specific continuous postev model in terms of its returned inverse temperature obeys

    d ln a/d lnT = alpha_LUT,j/f(T).

For Scom proportional a³T³g_s(T), the exact source-typed integral with either alpha is

    ln(Scom(T)/Scom(Tref)) =
       3 integral_from_lnTref_to_lnT alpha(T)/f(T) dlnT
       + 3 ln(T/Tref) + ln[g_s(T)/g_s(Tref)].

This independently checks whether replacing the actual inverse LUT by an ideal inverse caused ROT022's 0.1578% native-versus-code-continuum discrepancy. These are standard change-of-variables and piecewise-linear-source statements, not new mathematics or physical cosmology.

## 3. Exact scope and numerical controls

The author global inverse has 1000 geometric knots spanning 0.01 MeV to 1e6 MeV. All actual postev native temperatures are within [.008109737,1.482609419]MeV, so the FIRST 340/1000 original geometric inverse knots are a mathematically sufficient EXACT PREFIX; its last knot lies well above 1.48MeV and below 10MeV. Source high-T PDG tables and other 660 inverse knots need not be claimed loaded for this particular small-T calculation. The 340 inverse knots were recreated from original author source 1000-row g_rho data, not generated as a new narrowly rescaled 340-knot proxy.

Original table g(T) is linear in lnT within each cell, g-derivatives jump at original source knots, and the inverse LUT derivative jumps at a DIFFERENT knot set. Every source integral was segmented at BOTH original full 1000-row thermodynamic knots AND necessary inverse-LUT knots; coefficients on each segment use source-cell-consistent one-sided values. Original forward thermal table has constant extrapolation below first T node .01400298972685787MeV. Original inverse grid begins .01MeV and its extrapolation has alpha=4 there, so at very low T q_rho=q_s=0, f=-4, and dln(aTg_s^(1/3))/dlnT=0. This reproduces the source low-temperature plateau and explicitly avoids the corrected V002 mis-handling reported earlier.

Actually executed original connected-source V8 analysis used TWO independently rearranged quadratures: direct full Scom log-integrand and independent analytic extraction of endpoint 3ln(T/Tref)+ln(gs/gsref), with Gauss–Legendre8 and cell-local Simpson32 for the remaining alpha/f. Across all 16 source native temperatures the independent Gaussian8/Simpson32 result difference in Scom ratio is at most 4.1744385725905886e-14. This is strong binary64 quadrature consistency, NOT a formally outward-rounded or author-Julia error certificate.

Pointwise original inverse-LUT roundtrip T_LUT[rho_author(T)]/T−1:
- maximum abs at 16 actual native selected T values: 5.511654764811524e-6;
- separate 30001 log-temperature scan within the source native T range: largest sampled magnitude approximately 1.2400532266587666e-5, at T=.07000128953303338MeV.
The latter is a FINITE GRID diagnostic, not a certified global continuous supremum.

## 4. Actual original source numerical result

At last original native source sample10000, relative to first native no-PBH sample8545:

| Source-defined evaluation | Scom(final)/Scom(first) | total rise |
| --- | ---: | ---: |
| Actual ORIGINAL j22 native Julia 10D a,T with authentic author g_s | 1.1682400717068826 | +16.82400717% |
| Author continuous no-PBH code source with IDEAL rho/T inverse (MT15 ROT022 V003) | 1.170086317111359 | +17.00863171% |
| Author continuous no-PBH code source with ACTUAL 1000-knot inverse-LUT prescription | 1.1700836341476482 | +17.00836341% |

Exact reported original-source inverse-LUT-only relative effect at endpoint:
S_LUT/S_ideal - 1 = -2.292962212546712e-6 = -0.000229296%.

Actual saved native source vs code-LUT prediction:
S_native/S_LUT - 1 = -0.0015755817678011486 = -0.157558177%.

Thus **under the specified original source continuous equation with the original source 1000-knot inverse** the inverse LUT ALONE cannot reconcile the saved native entropy and source equation, because the remaining endpoint discrepancy is ~687 times the endpoint LUT-only relative adjustment. This 687 ratio compares model relative changes, NOT two realized solver errors and NOT source physical uncertainties. The inverse LUT's effect is not identically tiny at every temperature: among the 16 source rows its largest model relative effect is approximately 1.930962454455e-5 at row9500 T=.05520747218MeV. No uniform global-in-time bound follows from the endpoint alone.

For the actual original native row9400 T=.0786846844615MeV, source LUT EoS predicts S ratio1.1461161534722 while native S=1.1443566373174, relative residual -0.00153520. This is not an original exact T0 Q/T event readout. Late original native 123-row aT plateau previously checked by ROT022 remains compatible with source constant-g extension.

## 5. Scientific limitations and reproducibility separation

The residual IS NOT a certified original 10D solver error. The full native code evolves log rho, log PBH mass, H and coupled hadrons, uses its own numerical integration and dense source output sampling, and the measured source Q/T readout is a separate operator. Adaptive solver options and local-to-global error were NOT independently extracted or converged. The discrepancy can reflect solver/dense-output and other implementation details; this model comparison cannot assign cause. Separate source native mass cutoff invariant FAIL from MT15 ROT020, KN14/REC11/LT8 cubic clock audits and MT15 ROT021 nominal default tolerance gate remain corroborating motivation for a future *owner-authorized* solver convergence audit, NOT a proof of this entropy residual's origin.

Two distinct execution surfaces are declared without conflation:
1. **ACTUAL ORIGINAL AUTHOR 1000-row numerical science:** source file was actually fetched and SHA checked in connected GitHub V8; all 16 original source temperatures, lookup knots and independent quadratures executed there.
2. **CURRENT-CONVERSATION LOCAL SCRIPT AND ZIP:** local standalone stdlib Python script mt15_rot023_original_wuxu_inverse_lookup_audit.py SHA256 ba9849cff9a8df68851e19195561d01b886740c1bcbd8c503b2a3c56a9621b93 supports --thermo exact original file or --fetch-thermo when user has Internet, verifies original Git blob, and reruns the source and native analysis. It was ACTUALLY locally executed in --selftest SYNTHETIC constant-g source mode PASS but NOT full original source 1000-row mode (the full author table is not mounted and local Internet blocked). Source-limited user ZIP mt15_rot023_wuxu_native_inverse_LUT_source_limited_replay_20261113.zip 724413 bytes SHA256 635aaaba126051e7e5e3a91d29292e7ad050e2984dfa8316cfbbbcb3346e1650 includes ORIGINAL untouched native Mech-S9 ZIP, previously authenticated 16-g_s source fixture, new script, curated derived source results, verifier, README and 6-file SHA manifest. ZIP CRC PASS, original native 16/16 SHA PASS, six outer payload SHA PASS. NEW CLEAN temp extraction and python -I verification re-read original native 16 selected rows, recovered native S ratios, checked 1500 synthetic independent algebra controls, verified constant-EOS source script, and rejected mutated native original ZIP; all PASS. It does NOT constitute an offline full 1000-row thermodynamic table rerun, which requires network-enabled original-source fetch or supplied authentic file.

No new original Julia run authorized or performed, no corrected physical Yp, no paper-v2 versus code-v3 emission generator resolution, no PBH beta/mass bound, no new novelty, no CANON/EXEC_SIGN or BW writeback claimed. Mech-S9 and Badacz remain B1 source owner. Source EOS mechanism firstness retained.

VERDICT: ORIGINAL_SOURCE_1000NODE_INVERSE_LUT_RECONSTRUCTION_PASS / ACTUAL_NATIVE_J22_SCOM_RESIDUAL_PERSISTS_0p157558_PERCENT / INVERSE_LUT_ONLY_INSUFFICIENT_IN_SOURCE_MODEL / NO_ACTUAL_SOLVER_ERROR_CERT / E4_SOURCE_HOLD / NO_PHYSICAL_BBN_PBH / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / GITHUB_PENDING_BW_INGEST / NO_NEW_TASK_CASCADE.
