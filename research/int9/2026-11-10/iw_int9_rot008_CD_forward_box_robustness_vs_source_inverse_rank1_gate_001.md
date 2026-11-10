---
artifact_id: IW_INT9_ROT008_C_D_FORWARD_ROBUSTNESS_VS_INVERSE_NONIDENTIFIABILITY_001_20261110
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_09 / INT9
created_at: 2026-11-10
exposure: PUBLIC
scientific_claim_ceiling: CONDITIONAL_MODEL_INTERNAL_FORWARD_RECTANGLE_ONLY / NO_CONFIDENCE_COVERAGE / NO_JULIA_NATIVE_REPLAY / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

> **ERRATUM / AKTUALIZACJA ŹRÓDEŁ (11 XI 2026):** Stwierdzenie w pierwotnym ROT008, że nie wykonano jeszcze natywnego, wspólnego przebiegu C×2+D×2 przy j=22, jest **NIEAKTUALNE**. Badacz wykonał taki przebieg na podstawie wcześniejszego PREREG052 i opisał w REVIEW054 już 8 XI 2026; wykonał także C+D×0. Wynik przy wspólnej bazie: Δ(CD2)=−0.1360 dex, wobec przewidywania A1 ≈−0.149 dex; kierunek CD0 wykazał niezgodność z globalnym A1. Pierwotna arytmetyka ROT008 ma nadal wyłącznie **warunkowy** status, bez certyfikacji fizycznej ani identyfikowalności C/D. Pierwszeństwo natywnego testu należy do Badacza; AUD1 ROT035 i REC11 ROT012 niezależnie sprawdziły ograniczenie A1. **Korekta i nowy matematyczny wynik:** https://github.com/wmakiela-tech/Nash-iw-research/blob/7ebb022847c506e58aaf8d14d4f64d2d4e8effe6/research/int9/2026-11-11/iw_int9_rot011_native_cd_count_proxy_sharp_shared_baseline_distance_and_rot008_erratum_001.md . Przestarzałe zapowiedzi wykonania testu w poniższym tekście zachowano jako historię stanu wiedzy w chwili sporządzenia.


# INT9 ROT008 — Identifiable combined forward target despite non-identifiable C/D source inverse

## Scientific priority and source-typed question

Wu–Xu authors FIRST own source physics; original author Julia public commit d395183674cace6c9906a8911bdeb7234ba4040d is v2 not arXiv v3. **Badacz PREREG048/REVIEW050 FIRST** obtained actual v2 model-native finite perturbations and band-resolved χ²=4 contour response:
https://github.com/wmakiela-tech/Nash-iw-research/blob/11eeb1c37c21f19b2510e3bba5ae50169cbd5d79/research/badacz/2026-11-08/IW_BADACZ_WUXU_BAND_RESOLVED_HADRON_RESPONSE_KERNEL_REVIEW_050_20261108.md
Source scientific data are in original `research/badacz/2026-11-08/data/kernel_analysis.json` blob `1df29aff025755f9042628ec85752178b991d398`, count shares `band_number_shares.json` blob `f5c15f5ef56e1e3f8593953e4a0ca56db7e33898`.
**Mech-S8 ROT012 FIRST** independently showed 4-row C,D response almost collinear and exact rank-one perturbation within every marginal *FIT SE*, including unpooled direct D2:
https://github.com/wmakiela-tech/Nash-iw-research/blob/b2ba1d79df095ec1ee19a230c30426a1796207bd/research/mech-s8/2026-11-10/IW_MECH_S8_ROT012_WUXU_E4_C_D_BAND_SOURCE_IDENTIFIABILITY_AND_ONE_SIGMA_RANK_ONE_WITNESS_001_20261110.md .
INT9 ROT006 already predicted a conditional joint C+D forward point shift using direct D2. **New bounded delta here** is robust forward interval calculus for explicit marginal FIT-SE coordinate boxes against count-only surrogate, simultaneously preserving the Mech inverse no-go. No new physical discovery or owner experimental measurement.

## Conditional source and target

For each initial mass index j and source band b in C,D, Badacz defined `s_jb=(10^(-Delta_jb)-1)/(k-1)` from independent k=2 band perturbation roots. Denote its fit-derived propagated marginal SE by u_jb. These are NOT experimental repeated measurements; u_jb is NOT a probabilistic joint confidence region nor a physical systematic bound.

Make a HYPOTHETICAL RECTANGULAR ambiguity model:
 `|c-s_jC|<=u_jC, |d-s_jD|<=u_jD`.
For the target T_j=c+d the SHARP conditional range is
 `s_jC+s_jD - (u_jC+u_jD) <= T_j <= s_jC+s_jD + (u_jC+u_jD)`.
For all legal positive 1+T, under Badacz **additional A1 hypothesis** `Y_C=Phi(beta E(k))`, E linear in band modifiers, the modeled simultaneous doubling C+D yields the conditional log10-beta root change:
 `Delta_CD=-log10(1+T_j)`.
The strict monotone mapping gives the exact box interval by applying -log10(1+x) to reversed endpoints. The alternative count-number-only target uses `Delta_num=-log10(1+s_num,C+s_num,D)`. A fit-SE coordinate box in no way licenses interpreting this as a true confidence interval. True unknown correlations would change the admissible set; new physical source error may lie outside the entire box.

For arbitrary source perturbation v=(vC,vD) the sharp *linearized* ambiguity of vC*c+vD*d is `|vC|uC+|vD|uD`. This is a TARGET-RELATIVE positive forward map; it does not make individual C,D multipliers inverse-identifiable.

## Independently rechecked source table

Source values from Badacz's source JSON; D2 is directly simulated source k=2 and Dc is pooled from direct D2/D0 as explicitly disclosed in REVIEW050. All intervals are conditional one-fit-SE-per-coordinate **deterministic boxes**:

| j | D estimator | center sC+sD | box range sC+sD | predicted Delta_CD dex box | Delta_count dex | Count outside box? |
|--:|:--|--:|:--|:--|--:|:--|
|22|direct D2|0.409240|[0.374659,0.443821]|[-0.159513,-0.138195]|-0.038720|YES|
|22|pooled Dc|0.408062|[0.378669,0.437454]|[-0.157594,-0.139460]|-0.038720|YES|
|28|direct D2|0.171042|[0.154016,0.188067]|[-0.074841,-0.062212]|-0.028863|YES|
|28|pooled Dc|0.168205|[0.153243,0.183167]|[-0.073046,-0.061921]|-0.028863|YES|
|34|direct D2|0.085883|[0.069930,0.101836]|[-0.042117,-0.029355]|-0.021517|YES|
|34|pooled Dc|0.088078|[0.074347,0.101809]|[-0.042106,-0.031145]|-0.021517|YES|
|62|direct D2|0.008471|[-0.004031,0.020973]|[-0.009014,+0.001754]|-0.005515|NO|
|62|pooled Dc|0.011272|[0.000277,0.022267]|[-0.009564,-0.000120]|-0.005515|NO|

No numerical or physical claim beyond these exact source-derived model expressions: C+D versus count-only is box-separated j=22,28,34 and not j=62. For j=62, exact Badacz D2 `s_eff=-0.0013523344406164428` is near zero relative to fit uncertainty, so do not posit positive D response.

## Why this coexists with the source inverse no-go

Independently recheck Mech ROT012 rank-one construction:
 `C'=C+(0.002,0,0,0)`, `D'=C'/5`.
Maximum source FIT-SE coordinate deviations are
 `max|C'-C|/uC=0.1034190537`,
 `max|D'-Dc|/uDc=0.9833753946`,
 `max|D'-D2|/uD2=0.7250200079`.
The columns are exactly rank one; the individual input changes `delta f_C, delta f_D` cannot be guaranteed separately recoverable from observed contours. Nonetheless this SAME rank-one witness at j22 gives a *combined forward response* `C'+D'=0.40018876845241458` and conditional modeled `Delta_CD=-0.146186589657376...` dex, far from count-only -0.03872 dex. **Inverse ambiguity ≠ loss of every target-relative forward contrast**. This is a mathematical coexistence result, not proof that the physical model has rank one.

## Earliest break, bounded falsifier and custody

The coefficient table is SOURCE-MODEL finite secants for Wu–Xu v2 code and author B_exec interpolation, NOT an exact Jacobian of true hadron physics. Source P2 at j22 FAILED prereg interval; sum-rule closes only to allowed approximate tolerance, not exact algebra. Any combined Cx2,Dx2 expectation inherits **additional A1** source-linear factorization and remains an ANALYTIC PREDICTION, not observed run.

A single explicitly owner-approved source-native simultaneous Cx2+Dx2 j22 calculation could falsify A1 at scale k=2 if compared with the precommitted -0.149 dex analytic forecast, with simulation details/tolerances/resource pilot frozen BEFORE running. This is a proposal, NOT a task assigned or an execution claim. Full physical E4 remains SOURCE_BLOCK until differential hadron/energy/charge source at masses near 1e9,3e8,1e8 g is verified; strict ODE certificate and historical JCAP Fig5 execution identity remain OPEN. Wu–Xu arXiv v3 manuscript corrections from Mech-S8/Badacz/REC11 DO NOT imply a change to the v2 native executable. No physical PBH beta or helium bound, no novelty, CANON or EXEC_SIGN.

Independent local Python3 stdlib Decimal (precision70) and distinct float log10 cross-check reproduced all 8 boxes, rank-one witness and strict JSON result. Local full self-contained report SHA256 a63d39541c78c21b90405473cdb04e8a68fe14c17edfe7963a2cf30f15f40b20, local ZIP SHA256 82a69f979c7904d6123aae8f47af129d0e839c78ab0cde199457bca34a24cf3c; ZIP CRC PASS, 4 member SHA PASS, clean replay byte-identical PASS. This public artifact is NOT the complete ZIP. Source data read-only; no BW ingestion or owner/referee ACK by this write.

FINAL: `FORWARD_CD_BOX_SEPARATION_J22_J28_J34` / `J62_NOT_SEPARATED` / `INVERSE_RANK1_NO_GUARANTEE` / `MODELED_A1_ONLY` / `PHYSICAL_SOURCE_BLOCK` / `NO_NOVELTY` / `NO_CANON` / `NO_EXEC_SIGN` / `GITHUB_PENDING_BW_INGEST`.
