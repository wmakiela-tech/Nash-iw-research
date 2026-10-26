---
artifact_id: IW_LT6_ROT003_VARIABLE_OPERATOR_TARGET_TRANSFER_CERTIFICATE_001_20261026
created_at: 2026-10-26
origin_cell: IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_04 / LT6
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_MATURE_LP_HOST / SOURCE_TYPED_CERTIFICATE / LOCAL_REPRO_PASS / REFEREE_PENDING
claim_ceiling: NO_MATHEMATICAL_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_PBH_BBN / NO_ORIGINAL_JULIA_10D
---

# LT6 ROT003 — verified bounded certificate for background-dependent observations and target

Source-typed finite-dimensional problem: c in [-1,1]^d, |A_theta c|<=delta, target gradient g_theta and error R_theta=max |g_theta.c|. This is *not* a law of physics.

Assume rowwise l1 change ||(A_theta-A0)_j||1<=eta_j and gradient change ||g_theta-g0||1<=rho. Set B(g;A,d)=max_{|c|<=1,|Ac|<=d}|g.c|; the exact mature LP dual is min_lambda (||g-A^T lambda||1+sum_j d_j|lambda_j|).

- Upper: R_theta <= B(g0;A0,delta+eta)+rho.
- Lower, only if delta>=eta componentwise: R_theta >= max(0,B(g0;A0,delta-eta)-rho).

Proof: apply rowwise Holder inequality and set inclusion K_theta(delta) subset K0(delta+eta); for lower, use reverse inclusion K0(delta-eta) subset K_theta(delta), then bound target gradient difference by rho.

With parameter theta in a compact interval, **proved** rowwise and target Lipschitz constants L_A,L_g, and a finite theta-grid with cover radius h, the entire background worst-case risk is between max_i B(g_i;A_i,delta) and max_i[B(g_i;A_i,delta+hL_A)+h L_g]. A grid without a source-valid Lipschitz/interval certificate has no global upper-bound status.

Sharp negative guard: A0=[0,epsilon], A1=[0,0], g=[0,1], delta=0. The operator perturbation can be arbitrarily small while the exact target radius jumps from 0 to 1 as the measurement loses rank. Even nominal A0 with delta=epsilon yields radius 1. This is ordinary identifiability/conditioning mathematics, not a new theorem.

Executed independent Python primal/dual controls PASS. Seven-coordinate **synthetic** background family A_theta=A0+theta E, g_theta=g0+theta v, ||E_j||1=.005,||v||1=.02, delta_j=.01 and six nodes cover [0,1] with h=.1. Formula's global risk bracket evaluated by floating-point LP: [0.0545782160631, 0.0578728703144]. Inequality is exact under its hypotheses; displayed decimal endpoints are numerical LP evaluations, not independent interval-arithmetic proof.

First sources: [Mech-S7 ROT026](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s7/2026-10-26/mech_s7_rot026_joint_target_matched_source_moments_heldout_thermal_transfer_001.md), [MT14 ROT004](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt14/2026-10-26/iw_mt14_rot004_frontb_seven_bin_moment_rank_and_exact_target_dual_001.md), LT6 ROT002. Mature external hosts: Ettehad–Foucart, DOI 10.1137/20M1328476; Attia–Leyffer–Munson, DOI 10.1137/24M1667543; Chowdhary–Attia–Alexanderian, DOI 10.1137/24M1693921. No first-priority or physical claim.

[Private LT6 ROT003 folder](https://github.com/wmakiela-tech/Nash-Priv/tree/main/living-theory/2026-10-26/ROT003) contains a readback-verified science locator and independent [Python reproducer](https://github.com/wmakiela-tech/Nash-Priv/blob/main/living-theory/2026-10-26/ROT003/verify_rot003.py). Full proof, validation JSON, SHA and ready-for-insertion REV024 text were delivered to Moderator as a local ZIP. Native REV024 Google Docs edit was blocked; the last fully integrated monograph is REV023.

**Status:** SOURCE_TYPED_MATH / REPRO_PASS / EDITORIAL_INTEGRATION_PENDING / BW_INGEST_PENDING / NO_CANON / NO_EXEC / NO_NOVELTY / NO_PBH_BBN_PHYSICS.
