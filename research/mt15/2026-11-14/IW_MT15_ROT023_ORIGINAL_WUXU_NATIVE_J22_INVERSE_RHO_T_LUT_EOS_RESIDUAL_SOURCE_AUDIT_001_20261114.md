---
artifact_id: IW_MT15_ROT023_ORIGINAL_WUXU_NATIVE_J22_INVERSE_RHO_T_LUT_EOS_RESIDUAL_SOURCE_AUDIT_001_20261114
created_at: 2026-11-14
origin_cell: IW_MT_SUCCESSOR_14 / MT15
exposure: PUBLIC
document_type: INDEPENDENT_ORIGINAL_AUTHOR_SOURCE_INVERSE_LOOKUP_VERSUS_REAL_NATIVE_10D_POSTEV_BACKGROUND_AUDIT
status: ORIGINAL_AUTHOR_THERMO_GIT_BLOB_PASS / AUTHOR_LUT_1000_NODE_RECONSTRUCTION_PASS / ORIGINAL_NATIVE_GS_16_SAMPLE_DIAGNOSTIC_PASS / AUTHOR_SOURCE_MODEL_LUT_RESIDUAL_SEPARATED / LIMITED_OFFLINE_ZIP_REPLAY_PASS
claim_ceiling: WUXU_CODE_V2_SOURCE_MODEL_ONLY / ORIGINAL_NATIVE_ONE_J22_SAVED_TRACE / NO_ACTUAL_SOLVER_ERROR_BOUND / NO_ALTERNATE_10D_OR_PHYSICAL_ENTROPY_Yp_PBH / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# MT15 ROT023 — Source-native Wu–Xu j22 comoving entropy: can the original rho-to-T inverse lookup explain the ROT022 residual?

## 0. Priority and original custody

ORIGINAL AUTHORS FIRST: Quan-feng Wu and Xun-Jie Xu, JCAP 02 (2026) 063; unchanged original public Julia v2 repository Fenyutanchan/Primordial-Black-Hole commit d395183674cace6c9906a8911bdeb7234ba4040d. Original full thermodynamic table arXiv-2509.05618/data/ext/N_around_m_e.csv, 1000 rows (T,g_rho,g_s), exact Git SHA1 blob 93f2494f026c5d0587ea40fe08bb938dd9d01fa8; original rho/T source interpolator tool_script-N_relativistic_species.jl blob 0437c032bdc4bafca6cb634c0db4cd2c46fb7efc; main-scan.jl original full 10D Julia blob b368ba55d5a493f7bc185909730f7fe5691f10d6.

PROJECT FIRST: Mech-S9 ROT002 FIRST source EOS/adibaticity null and ROT013 FIRST genuine original-author Julia 10D j22 10000-row trace; REC11, KN13, INT9 and MT15 ROT010 independent earlier source EOS checks; MT15 ROT022 original source entropy-vs-native comparison, final corrected V003 report+machine results (V001/V002 superseded), with INT9 ROT030 first alert to V002 wrong low-T derivative handling. ROT023 is an independently bounded INVERSE LOOKUP attribution check, NOT first discovery of the thermodynamic equation inconsistency or physics novelty.

Authentic provider native Mech-S9 Actions run 43436800793, artifact 14045176436; source unchanged ZIP SHA256 71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486, 10000x19 original CSV SHA256 45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1. Native ZIP CRC PASS and original 16/16 SHA256 member manifest PASS. Source first nPBH-zero sample is index8545 (one-based). No new Julia or other physical source solver run.

## 1. Exact source code's TWO separate logarithmic tables

Original author g_rho(T),g_s(T) each interpolate linearly in lnT in ORIGINAL 1000-row thermodynamic table, with CONSTANT extrapolation outside table. Original author make_from_rho_to_T builds a SECOND approximate inverse table with 1000 geometric T nodes from 1e-5 to 1e3 GeV (0.01 to 1e6MeV), at each node computes rho=(pi^2/30)*g_rho(T)*T^4, then applies linear interpolation log10(T) against log10(rho), with LINEAR extrapolation. These are two DIFFERENT lookup tables with DIFFERENT lower cutoff temperatures: original g table Tmin about .0140029897MeV, inverse lookup Tmin=.01MeV.

Connected GitHub source was directly fetched, entire original 1000-row Git blob validated, and original inverse table values reconstructed with source recipe. Only first 340 of 1000 generated inverse knots are required by the ORIGINAL j22 postev sampled T range [.00810973699892033,1.48260941885709]MeV; this 340-node partial construction includes every relevant inverse interval, with LINEAR extrap below .01MeV. It is not a claim that the unused higher-energy nodes were physically tested.

Define q_j=dln(g_j)/dlnT and f_code(T)=dlnrho/dlna=-4+q_rho/(3+q_s), exactly the original source no-PBH equation (Mech-S9 first). Exact analytic inversion would give alpha_ideal=dlnrho/dlnT=4+q_rho. The SOURCE CODE inverse has alpha_LUT equal to the PIECEWISE secant slope dlnrho_lookup/dlnT, not generally alpha_ideal. Therefore in this source model dln a/dlnT=alpha_LUT/f_code, and the comoving equilibrium entropy proxy S_com proportional to a^3 T^3 g_s(T) obeys

    ln[S(T)/S(Tref)] =
      integral_(lnTref)^(lnT) [ 3 alpha(T)/f_code(T) + 3 + q_s(T) ] dlnT.

The source q_j has jumps at original thermo table knots; alpha_LUT has separate jumps at inverse lookup knots. Split quadrature at BOTH classes, and use source cell-local one-sided derivatives. Below the original thermo Tmin q_rho=q_s=0, whereas below inverse .01MeV the first inverse secant alpha_LUT remains active (linear extrapolation), not assumed exactly 4. This negative source check prevents repeating errors in ROT022 earlier superseded V001/V002.

## 2. Actually source computed 16 real native source rows

Start: actual native source saved row8545 Tref=1.48260941885709MeV, a_ref=185173297559521. Final: actual native row10000 T=.00810973699892033MeV, a=4.98052146203102e16. For source-computed S_com/S_ref at final:

Original native sampled S_com from original source g_s(T): **1.1682400717068826**.
Source f_code continuous with IDEAL inverse rho(T): **1.170086317111359**.
Source f_code continuous with EXACT ORIGINAL 1000-node approximate inverse recipe: **1.17008363414765**.

Mathematical relative differences:
- source LUT model effect S_LUT/S_ideal-1 = **-2.2929622e-6** = -0.00022929622 percent;
- original native-vs-source-LUT residual S_native/S_LUT-1 = **-0.0015755817678** = -0.1575582 percent;
- prior original native-vs-ideal residual S_native/S_ideal-1 = -0.0015778711173 = -0.1577871 percent.
Thus modeling the author's ORIGINAL rho-to-T inverse LUT changes the model discrepancy by about 0.145 percent OF the original discrepancy. It does NOT close the source-native ~0.158 percent residual.

At original native row9400 near 0.07868468446MeV: native S/Sref=1.14435663732 versus source-LUT predicted 1.14611615347 (relative remaining residual -0.00153520). Over these 16 source samples the absolute relative source-LUT-model shift peaks around 1.93096e-5, not a demonstrated full Julia error bound.

POINTWISE inverse negative: among 16 original sampled native temperatures the relative roundtrip difference between approximate and exact T(rho) is at most 5.51165e-6. A 30001-point logarithmic T search found a grid maximum 1.240053e-5 at T about 0.0700013MeV; explicitly NOT a global mathematical extremum or a time-integrated error bound. A small pointwise deviation alone was never used to infer the full integrated change.

Connected original source calculation split the native T range at both thermo and inverse knots; independent Gauss-Legendre8 and source-local one-sided Simpson32 computations of the source LUT prediction agreed within about 4.2e-14 in S ratio across all 16 native T values. This compares two quadratures for the SAME source model, not an ODE convergence or native solver-error measurement.

## 3. Exact reproducibility limits, negative controls, and self-contained source-limited package

CONNECTED SOURCE: complete original 1000-row author Git file was actually fetched/read within the connected GitHub environment, original Git blob authenticated, all model source values used to calculate inverse LUT and source-rate integral. Separate Python implementation was authored for independent on-machine repeat, and performs EXACT source Git blob check if given --thermo original file; alternatively --fetch-thermo downloads author public data on a networked machine. Source script mt15_rot023_original_wuxu_inverse_lookup_audit.py had successful SYNTHETIC CONSTANT EOS independent selftests. The original 1000-row dataset is NOT mounted in the local offline container, and the local source Python was NOT executed on that full original table: no false full offline original-source execution claim.

CURRENT USER CONVERSATION local ZIP: mt15_rot023_wuxu_native_inverse_LUT_source_limited_replay_20261113.zip, EXACT 724413 bytes SHA256 635aaaba126051e7e5e3a91d29292e7ad050e2984dfa8316cfbbbcb3346e1650. Includes untouched source-native Mech-S9 ZIP and its original 16/16 hashes, prior independently original-source-derived fixture of 16 values g_s(T), independent source algorithm implementation, curated connected-computation JSON, verifier, README and SHA256 manifest 6/6 PASS. ZIP CRC PASS; NEW CLEAN temporary directory extraction and Python -I mt15_rot023_verify.py PASS (16 source native sampled ratios recomputed from exact original ZIP and gs fixture, 1500 independent algebra probes, package SHA PASS). A separate original-native ZIP single byte modification is REJECTED before science by the source integrity check. LOCAL ZIP DOES NOT CONTAIN THE FULL ORIGINAL AUTHOR 1000-row THERMO CSV; it proves the LIMITED native+fixture part only. The full original-source numerical results are preserved in a separate GitHub source-typed JSON and can be reproduced on a networked source machine with verified author exact file.

## 4. Science ceiling and owner gate

This is an in-model attribution test under original author CODE v2 thermodynamics, not a physical observation of entropy production. The original code's S_com as a thermodynamic EQUILIBRIUM proxy is distinct from a physical entropy inventory of all particles and thermal sectors. An approximate inverse-LUT contribution only ~2.3e-6 is far too small, in this calculated source model, to explain an existing residual ~1.58e-3. The remaining discrepancy's precise cause is not identified: Julia solver tolerances, dense source sampling, mismatch of actual runtime source inverse versus reimplementation, original initial state, and source code parameter details remain separate and require owner convergence checks. No error bars on these unknown contributions or physical BBN-Yp/PBH beta consequences are asserted.

This one-j22 native callable input is slightly outside original paper historical scan beta maximum. Original source actual mass cutoff numerical undercut and cubic clock drift (KN14, Mech-S9, MT15 ROT020/021) remain independently OPEN. The physical hadron generator below original first M=1e9g source grid node is E4 SOURCE HOLD, code-v2 vs-paper Y mapping is unresolved. No new Julia run, no change to owner B1 protocol, no new physical prior art, no CANON/EXEC_SIGN, no BW or I3 ACK.

VERDICT: ORIGINAL_AUTHOR_INVERSE_LUT_SOURCE_REPLAY_PASS / INVERSE_LUT_ALONE_EXPLAINS_RESIDUAL_FAIL / LOCAL_SOURCE_LIMITED_NATIVE_REPLAY_PASS / TRUE_NATIVE_SOLVER_ERROR_UNDETERMINED / E4_SOURCE_HOLD / NO_PHYSICAL_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / GITHUB_PENDING_BW_INGEST / NO_NEW_TASK_CASCADE.
