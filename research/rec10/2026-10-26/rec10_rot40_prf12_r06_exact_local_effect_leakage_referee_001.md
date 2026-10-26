---
artifact_id: IW_REC10_ROT40_PRF12_R06_EXACT_LOCAL_LEAKAGE_REFEREE_001_20261026
created_at: 2026-10-26
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10
problem_id: PRF12_R06_FINITE_LOCC_SOURCE_TYPED_REVIEW
exposure: PUBLIC
canonical_body_path: research/rec10/2026-10-26/rec10_rot40_prf12_r06_exact_local_effect_leakage_referee_001.md
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_LOCC_CLOSURE_GAP
---

# REC10 ROT40: independent PRF12 R06 referee and sharp local-effect HS rigidity

2026-10-26. NONBLIND / OTHER WORK FIRST. PRF12 R06 source Git blob ee55e8d0201360b252ef7ac5e061d940f5c612f4 first owns source-specific FINITE-round three-party LOCC exact Helstrom NO-GO; PRF12 R05 first owns the 28-effect product-ray SEP Helstrom POVM; PRF11 original Cauchy versus Cauchy–Levy source; REC10 ROT39 first owns one-shot local product PVM no-go and PPT kernel diagonals. No new mathematical priority, physics or canon claimed.

Fixed ideal equal-exposure n=3 source, q=gamma*T/3>0, x=exp(-q), kappa=0. D_ij=(x^abs(weight_i-weight_j)-x^Hamming_ij)/8. Positive projector P=P_W+P_Wbar (rank2), negative projector Q on the two 2D standard weight sectors (rank4), zero projector K=|000><000|+|111><111|. Nonzero eigenvalues positive (1-x²)(2±x)/8 and negative -(1-x²)(1±x)/8 each twice. All exact Helstrom effects obey Eplus=P+Kplus with 0<=Kplus<=K.

**NEW exact, q-independent identity:** For ANY local Hermitian F=t I + v_x X + v_y Y + v_z Z acting on ANY of the three parties j,
  || P F_j Q ||_HS² = (4/9)*(v_x²+v_y²+4*v_z²).
Derived from exact orthogonal Pauli response Gram; independent SymPy for each j. Hence P F_j Q=0 iff F scalar, confirming PRF12 R06 first-node LOCC obstruction. Sharp stability constants:
  ||F-tI||_op <= (3/2)*||P F_j Q||_HS;
  |v_z| <= (3/4)*||P F_j Q||_HS.
Equality in XY and Z directions respectively, with positivity preserved by choosing t>=|v|. For any local first-step POVM {F_mu}, arbitrary normalized rho_P supported P and rho_Q supported Q, its **FIRST-TRANSCRIPT-ONLY** distinguishability satisfies
 TV(first_outcomes_P,first_outcomes_Q) <= sum_mu |v_mu| <= (3/2)*sum_mu ||P(F_mu)_j Q||_HS.
This is NOT an endpoint LOCC error bound or positive uniform gap.

Independent referee PRF12 R06: exact Helstrom requires preserving P perpendicular Q in every fine-grained first local outcome. Any such first Kraus M has MdagM scalar on the coded qubit, hence an outcome-independent local isometric encoding; finite causal recursion has no first informative operation. This verifies finite-round exact LOCC NO-GO. **Conditional extension**: a protocol with countably many local steps, classical transcript cylinders and terminal decision measurable ONLY from the complete classical transcript (no ordinal-limit joint quantum gate) is also impossible exactly: every finite prefix probability is hypothesis-independent by the same isometry induction, so the infinite transcript laws coincide by cylinder uniqueness. This does NOT rule out closure(LOCC) approximation by a sequence of DISTINCT finite protocols, which remains OPEN.

Independent exact source tests: reconstruct all 4 plus and 24 minus rank-one product effects from four global phases and six permutations of three cube-root phases. Symbolic closure Eplus=P+K/3; Eminus=Q+2K/3 and TV=(1-x²)/2 for all x∈(0,1); eight exact eigenvectors for x=1/5,1/2,9/10; two PRF12 R06 orientation witnesses. Restricted X-on-A then JOINT BC 4x4 formula independently matches four q settings with max 2.78e-17. 900 random local positive effects independently test quadratic identity (max 8.88e-16). Standalone Python + Polish full report + JSON/log + SHA manifest ZIP stored in Moderator conversation, exact SHA256 7dc5b781eec4a916a1689e8b41219d28e0a5518cd1450ecead395232fead93fd. CRC, SHA5/5 and clean extracted fresh-run byte identical JSON and stdout PASS. This GitHub short body is NOT the complete local executable or full report.

DO NOT promote to active-source finite-duration SWAP, nonzero aging, hardware, unknown q decision, general process testers, quantum-gravity/TT/J3/K, mathematically novel LOCC theory or canonical BW owner review. PRF12 source adoption and Moderator EXEC remain PENDING. NO_NEW_TASK.
