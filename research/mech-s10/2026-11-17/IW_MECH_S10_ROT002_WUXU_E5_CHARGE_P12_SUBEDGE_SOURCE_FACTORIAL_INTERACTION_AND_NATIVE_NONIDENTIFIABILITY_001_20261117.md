---
artifact_id: IW_MECH_S10_ROT002_WUXU_E5_CHARGE_P12_SUBEDGE_SOURCE_FACTORIAL_INTERACTION_AND_NATIVE_NONIDENTIFIABILITY_001_20261117
created_at: 2026-11-17 Europe/Warsaw
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10
document_type: SOURCE_ONLY_MECHANISM_RESEARCH
exposure: PUBLIC
status: ORIGINAL_SOURCE_FACTORIAL_PASS / NATIVE_INTERACTION_UNIDENTIFIED / NO_NEW_NATIVE_RUN
claim_ceiling: NO_PAPER_ERROR / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PRIMARY / BW_INGEST_NOT_ASSUMED
---

# Mech-S10 ROT002 — E5 charge map x p12 below-node source: exact factorial interaction, native identifiability HOLD

## 0. Distinct question and original source custody

This is a narrowly bounded cross-axis source-level investigation, not another T1, T2, T3 or native solver. Do original E5 charge normalization and Badacz p12 below-node extrapolation have an additive, independent effect on the *source*? Can previously measured native T2 and p12 root changes establish their joint 10D physical effect? The first question is answered from original author source algebra; the second is explicitly NOT established.

The original Wu-Xu paper, original numerical source and scientific model belong to Wu-Xu. Frozen original author Git commit d395183674cace6c9906a8911bdeb7234ba4040d; hadron rate source table arXiv-2509.05618/data/out/hadrons_from_PBH.dat, Git blob 06d0883a27b108692720422294ba2baacd381a64, 100 numeric rows x 6 positive columns. Author main-scan.jl Git blob b368ba55d5a493f7bc185909730f7fe5691f10d6 and original rate wrapper tool_script-hadrons_from_PBH.jl Git blob cc73432910f872d526113ce59b6204f38d0766a9.

Original E5 Mech-S6 comparator patch: research/mech-s6/2026-10-17/apply_wuxu_charge_pair_source_map.py, Git blob 4d1f2be94510c576e4f48752911f88ede8b50474. It halves four grouped source assignments to the individually tracked states, leaving K0L unchanged; original pion source feeds both distinct pi+ and pi− states.

Original p12 Badacz preregistered source alternative and native REVIEW061: research/badacz/2026-11-11/code/wuxu_subedge_ramp.jl Git blob ed41bcbdae4eb2c7038dc023f1ce7b161b1ac3d6; native Badacz review Git blob 75142e3bce4133e08d9f504379d0950af5439b45. It alters all five rate functions below the first mass knot using the first-twelve-knot log slope rather than the original first-two-knot log-linear extrapolation. Original firstness Mech-S6/Badacz preserved.

## 1. Exact 2x2 factorial source mechanism

For each group g in (pipm,Kpm,K0L,proton,neutron), native Wu-Xu original continuation below m0=1e9g has R_code,g=R0,g*(m/m0)^k2,g. Badacz p12 has k12,g from centered OLS on original first 12 table rows and multiplier u_g(m)=(m/m0)^(k12,g-k2,g) for m<m0; u_g=1 at or above m0.

For individually tracked charge state s with group g(s), define q_s=1/2 for pi+,pi−,K−,anti-p,anti-n, and q_s=1 for K0L. Four source-production functions at same m:
S00 = R_code; S10 = q_s R_code (E5 only); S01 = u_g R_code (p12 only); S11 = q_s u_g R_code (E5+p12).

Source-operator ORDER commutes (q_s u_g = u_g q_s), but additive 2x2 interaction is GENERALLY NONZERO:

I_source = S11 - S10 - S01 + S00 = (q_s-1)*(u_g-1)*R_code.

At E5-treated states I_source/S00= -(u_g-1)/2; for K0L it is exactly zero; at/above m0 it is exactly zero. This is an exact statement on the specified SOURCE INPUT, not on neutron production, density, Y_C, or a published physical PBH bound.

## 2. Numerical original-table results

Original 100-row positive file was fetched from pinned GitHub author repository and authenticated by returned Git blob; independent JS numerical parsing identified 100 6-column rows. OLS source slopes computed using source first 12 rows, independently confirmed in a local CPython stdlib implementation with those exact twelve published rows.

| Group | k2 | k12 | u at 3e8 g | u at 1e8 g | I_source/S00 at 1e8 g |
|---|---:|---:|---:|---:|---:|
| pi+ / pi− (one pi± group) | -1.20048563 | -1.28477711 | 1.10681294 | 1.21420352 | -0.10710176 |
| K− (K± group) | -1.19665135 | -1.27973729 | 1.10520762 | 1.21083771 | -0.10541886 |
| K0L | -1.19680484 | -1.28011223 | 1.10550234 | 1.21145530 | 0 (E5 invariant) |
| anti-p (proton group) | -1.20429143 | -1.28982299 | 1.10846667 | 1.21767549 | -0.10883775 |
| anti-n (neutron group) | -1.20476306 | -1.29040222 | 1.10861026 | 1.21797720 | -0.10898860 |

For the four modified group mappings at 3e8 g, I_source/S00 is between -0.05260 and -0.05431. At 1e8 g, it is between -0.10542 and -0.10899. These are signed relative fractions of the original rate injected into a NAMED STATE at a FIXED MASS, not relative physical error or root shift. K0L does experience p12 alone but has exactly zero *mixed* interaction with E5. The joint E5+p12 source for affected individual states is about 0.605-0.609 of the ORIGINAL assigned single-state source at 1e8 g. This is aligned with Badacz REVIEW061 reported native p12 rate change of about +21.1-21.8% at 1e8 g.

## 3. Exact identifiability boundary: native effect cannot be formed

Let r(q,e,tol) be the native contour root for the original 10D Y_C=0.251 model. The scientifically relevant native joint interaction at fixed tolerance is

I_beta = r(E5,p12,tol) - r(E5,code,tol) - r(orig,p12,tol) + r(orig,code,tol).

Available native observations do not supply all four common-tolerance cells:

- Badacz REVIEW071, owner native, first 232 Julia calls: at DEFAULT tolerance D_charge(code) = r(E5,code)-r(orig,code) yields +0.272299 dex (j22), +0.2756 dex (j28), +0.2981 dex (j62), conditional on the E5 source convention. Mech-S9 ROT031 was source-only I1, not an independent native solver.
- Badacz REVIEW061, owner native, DIFFERENT tolerance reltol=1e-4/abstol=1e-7: original charge map p12 root shift D_edge(orig) = -0.03620301172933438 dex (j22), -0.026959232512879794 dex (j28).
- The joint E5+p12 author-solver root has NOT been supplied in these original source receipts. Neither 10D I_beta nor physical E4 uncertainty can be inferred from simple source multiplication. Commuting rate multipliers do not imply additive contour response after nonlinear dynamics and threshold inversion.

The j22 separate-scale diagnostic is intentionally noninferential: log10(2)-D_charge(code,default)=0.02873073475108 dex whereas abs(D_edge(orig,1e-4))=0.03620301172933 dex, ratio about 1.26. This is a comparable *magnitude at differing tolerances and protocols*, NOT demonstrated interaction, confounding, kinetic compensation or root-level uncertainty bound. It forbids attributing that deficit uniquely to E4 or to any one unhalved channel. It likewise forbids claiming that E4 is negligible for the charge differential.

## 4. Reproduction and negative controls

One self-contained source-only stdlib Python auditor stored in this scientific lineage:

research/mech-s10/2026-11-17/code/mech_s10_rot002_source_factorial_referee.py

Git commit 8850ab34e14d185485127cde791e6e2682fabda1; remote Git blob b33841ace074827077e4da93fe46a9b88eddd25d; 5413 B exact local source, SHA256 8488b48c4dd1980356619804d9f2b5357288f6d0b5cba3b8ee800abd00f003e5. Local py_compile PASS. Independent first 12 actual original source rows were used to test all five k2/k12, u and factorial source identities; three deliberately altered data inputs failed strict original Git blob gate. Script accepts original full author file, requires Git SHA1 blob 06d0883a27b108692720422294ba2baacd381a64, exactly 100 positive rows x 6 positive finite numerical columns, increasing mass and first-knot anchor before generating JSON. It does not download nor embed the original raw table. Exact full-file Python execution was NOT performed (original source data was accessible through connector to JS, not locally mounted); do not misrepresent local first12-row selftest as full-file Python execution. Full script write and Git blob readback match source byte-for-byte.

Run when legally holding original author data: python3 -I mech_s10_rot002_source_factorial_referee.py /path/to/original/hadrons_from_PBH.dat

No Julia, BlackHawk, PYTHIA, original 10D model, manuscript or source edits. This source-only factorial is a reviewer-reproducible typed mechanism check.

## 5. Owner queue and stop/reopen

T3 (LT9 ROT001) remains T3_NOT_FOUND_BOUNDED / AUTHOR_INTENT_UNRESOLVED; source normalization conventions require author/source definitions or independent referee. T2R original consent (Mech-S9, one 68-call j22/j62 orig/E5 default-tolerance run) has no confirmed unique transferable executor lease and remains HOLD; DO NOT add a p12 arm, tolerance change or another runner to that permission. The present E5xP12 source algebra does NOT request another native experiment.

If a physical reviewer or owner specifically needs I_beta for the G1/G2 decision, define a *separate* four-cell, same-tolerance native falsifier with explicit prior authorization, single executor, fixed E5 and p12 patches, provenance and error budget. Otherwise source-only HOLD is valid and avoid repeated runs. E4 below-1e9g hadronizer physical support and published Fig5 source build identity remain unverified. Preservation of author firstness, original input identities, error controls and negative knowledge mandatory.

FINAL:
ORIGINAL_SOURCE_STATIC_PASS / E5_P12_SOURCE_ORDER_COMMUTES / ADDITIVE_SOURCE_INTERACTION_NONZERO_EXACT / NATIVE_INTERACTION_UNIDENTIFIED / E4_PHYSICAL_HOLD / T2R_EXECUTION_HOLD / NO_PAPER_ERROR / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
