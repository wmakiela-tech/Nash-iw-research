---
artifact_id: IW_MT14_ROT009_FRONTB_BORSUK_ULAM_EXACT_NONLINEAR_SOURCE_ALIAS_001_20261027
created_at: 2026-10-27
origin_cell: IW_MT_SUCCESSOR_13 / MT14
problem_id: P1_FRONTB_FINITE_NONLINEAR_TARGETS_VS_POSITIVE_CONSERVATIVE_SOURCE_IDENTIFIABILITY
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: CONDITIONAL_EXACT_TOPOLOGICAL_TWO_SOURCE_NONLINEAR_ALIAS / SYNTHETIC_INDEPENDENT_CONTROLS_PASS / OWNER_REVIEW_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_Yp_DH_PBH / NO_SOURCE_NATIVE_ODE_REPLAY / NO_CONTINUITY_VALIDATED
---

# MT14 ROT009 — Source-positive eleven-bin family: exact nonlinear aliases for six measured targets

**First source owners, strict subtraction:** Wu and Xu, *Primordial black holes evaporating before big bang nucleosynthesis*, JCAP 02 (2026) 063 (arXiv:2509.05618; doi:10.1088/1475-7516/2026/02/063) original PBH calculation and Fenyutanchan upstream GitHub commit d395183674cace6c9906a8911bdeb7234ba4040d. **Mech-S7 ROT030 FIRST** created eleven disjoint C^3 sin^4 bins on M/1e9g in [.07,.92], pointwise antinucleon pair-sum conserving source shift, 3 source log-moments, six nominal Xnuc targets (chi_EM=.25,.5,.75 x Bexec/Bsym), 11-9 >=2 linear-null dimension and full conditional 7D ODE finite-amplitude checks. Their *particular* first-order-null direction had NONZERO mostly even/quadratic full target responses, and this does not conflict with MT14's existential theorem. Original full owner report, including code: https://github.com/wmakiela-tech/Nash-iw-research/blob/e415aeeb0c053e677d823124754ddcc76d2f3005/research/mech-s7/2026-10-26/mech_s7_rot030_basis_enlargement_finite_observation_nullspace_nonlinear_gate_001.md .

**EXTERNAL MATURE THEOREM FIRST:** Borsuk–Ulam: every continuous map S^d -> R^p with d>=p maps at least one antipodal pair to the same value, e.g. published university algebraic topology proof https://strickland1.org/courses/MAS61015/notes_html/S24.html corollary 24.6. Hence this is NOT claimed mathematically novel, not a verified new physical model, not an original Wu–Xu code replay.

## Frozen admissible source and exact theorem

Let phi_i, i=1..11, be the original eleven smooth nonnegative mutually disjoint sin^4(log-mass) source bumps strictly below the source tabulated boundary M=1e9g, with 0<=phi_i<=1. Let base source channels q_p(z), q_n(z) be *strictly positive continuous functions on the compact union of supports* (this is the conditional extrapolated Mech source model, NOT source-valid Hawking particle spectroscopy). For any c in R^11 define h_c(z)=sum_i c_i phi_i(z), and perturbed source species

  q_p^c=q_p+(q_p+q_n)h_c,  q_n^c=q_n-(q_p+q_n)h_c.

Their pair sum is EXACTLY equal to q_p+q_n pointwise, for every c. For positive source safety define

  mu = min_support min(q_p/(q_p+q_n),q_n/(q_p+q_n)) > 0.

All coefficient vectors with ||c||_2 < mu give strictly positive perturbed q_p^c,q_n^c, and the opposite -c is equally admissible, without touching source table-edge jets.

Mech's first three *independent per-species* comoving log-mass moments in this +/- redistribution are equivalent to THREE linear equations M c=0, where

 M_{j,i} = integral_{I_i} exp(3z) [q_p(z)+q_n(z)] phi_i(z) z^j dz,
 j=0,1,2; i=1..11.

Since source weight is strictly positive and bins ordered/disjoint, ANY three ordered columns form a positive determinant (multilinear integral of 3x3 Vandermonde in z with z1<z2<z3). Thus rank(M)=3 exactly, V=ker(M) has dim(V)=8, its radius-r sphere is S^7, and BOTH c and -c satisfy the exact moment conservation equations. Separate pbar and nbar moments give the same +/- constraints, not SIX independent constraints.

Define Y(c)=(Y_.25,exec, Y_.25,sym, Y_.5,exec, Y_.5,sym, Y_.75,exec, Y_.75,sym) in R^6 as the **FULL nonlinear** source-to-final-Xnuc target outputs, not linearized adjoints, within the precise Mech 7D conditional bridge model. Assume on a sufficiently small coefficient ball that all six ODE IVPs possess unique trajectories, source/target map depends continuously on coefficients and final event readout is continuously defined. A local-Lipschitz vector field in a common compact domain and transverse unique Tnuc event are sufficient; Mech's discrete Radau tests did not independently certify this event-continuity hypothesis or the original Julia10D. Mark it CONDITIONAL.

**T009 (exact antipodal nonlinear data collision).** For EACH radius 0<r<r0=min(mu,r_ODE) there exists c∈V with ||c||_2=r such that simultaneously

  Y(c)=Y(-c) exactly as ALL SIX finite-amplitude NONLINEAR targets;
  M c=M(-c)=0 (all three moments of EACH shifted species equal base);
  q_p^c+q_n^c=q_p^-c+q_n^-c=q_p+q_n pointwise;
  both source species strictly positive for c and -c;
  ||c-(-c)||_2=2r > 0.

**Proof:** V is R^8; its radius-r sphere is S^7. Restriction of continuous Y to sphere gives S^7→R^6, thus by Borsuk–Ulam SOME antipodes have identical six nonlinear outputs. Moment conservation is automatic in V, source positivity from ||h_c||∞<=||c||∞<=r<mu. Disjoint bump supports guarantee the two source functions are genuinely different. QED. No source-dependent derivatives, ill-conditioned rank-9 estimates, small-perturbation Taylor truncation or special nonlinear ODE numerical result is used in the existence proof.

This does NOT say Y(c)=Y(0), that Mech's particular SVD-null vector c0 has identical finite responses, that all null vectors have zero nonlinear remainder, or that ANY heldout seventh/eighth target must differ between these sources.

**Design resource corollary.** With n=11 independent source coefficients and m=3 independent linear moment constraints, d=n-m=8. For ANY p<=d-1=7 continuous scalar final readouts, Borsuk–Ulam produces a positive admissible opposite-source pair with identical full p-vector for each sufficiently small radius. Therefore adding only ONE readout to the original six does not make the source-to-observations map injective in any open neighborhood. To *possibly* obtain local injectivity, p>=8 target coordinates are NECESSARY but NOT SUFFICIENT: full nonlinear inverse regularity, actual Jacobian rank, stable signal-to-noise, and physical source law remain separate gates. Mech's additional chi=0/1 heldout readouts could remove this particular topological obstruction, but they have NOT been shown to achieve injectivity.

**Conditional loss consequence**: for any observation likelihood depending on c solely through the above common Y(c) and with IDENTICAL noise law at a fixed Y, the two selected hypotheses c,-c generate identical data distributions; any estimator of full coefficient vector c suffers worst-case Euclidean error >=r on this source pair and squared error >=r^2 (two-point metric triangle/Jensen). This is NOT a target Xn physical uncertainty interval, no guarantee of different extra heldout Xn targets, and does not cover heteroscedastic source-dependent noise.

## Actually run independent controls (not original Mech kinetics)

The separate full Polish report and self-contained Moderator-local ZIP have two INDEPENDENT examples:
1. NumPy/SciPy exact eleven bin locations [.07,.92] and actual sin^4 shape, *synthetic* positive source weight W(z)=exp(3z)(exp(.5z)+.75exp(-.2z)), NOT Mech native q_p/q_n. Gauss-Legendre160 vs independent QUAD moment discrepancy 2.91e-16. Numerical moment rank3/ker8, positive 3-column determinant. A smooth *synthetic* six-output map with nonlinear even quadratic and odd cubic+sin terms yields an approximate antipodal witness ||c||2=.1, source moment errors <5e-19 and six nonlinear target differences <1.10e-15. This is numerical **illustration** only and not proof of exact original ODE equality.
2. Independent Python STANDARD LIBRARY Fraction, no imports of first code, gives explicit 11-bin signed finite-difference coefficients (-1)^i*choose(9,i)/100000 on i=0..9, c10=0. First 3 polynomial moments and SIX first-order target terms vanish EXACTLY; six quadratic even target values are nonzero and identical for ±c; source pair-sum and .5/.5 partition positivity hold EXACTLY. It is a distinct mathematical toy, not author 7D trajectory.
Self-contained report, both programs, results JSON, README and 6-file SHA256 manifest; ZIP SHA256 86223b3eac6d7b0a48eaa7504f70d3aaf70403e1e01c94d368ffe9c3a0176713. ZIP CRC pass, checksum 6/6 pass; clean isolated extraction, delete BOTH recorded JSONs, rerun two independent programs and regenerate byte-identical JSON pass. Full original Mech 7D or original Julia 10D was NOT run in MT14 ROT009.

## Scientific decision and stop

Mech ROT030's observation **"particular first-order-null direction did not preserve full nonlinear targets"** stays TRUE. Nevertheless, its six continuous nonlinear nominal outputs cannot ever globally identify all eight free source degrees on the declared positive eleven-bump model: an EXACT finite-nonlinear alias pair exists topologically for each small amplitude. This is stronger and logically different from first-order nullity and clarifies why selecting one SVD-null direction cannot settle source identifiability. To challenge the theorem in the specific ODE, examine its exact six-map CONTINUITY/event-time admissibility, input positivity or source dimension; no further quadratic-only prooflet needed. One optional original-owner Mech-S7 and independent REC/LT review, no forced task cascade. No genuine sub-1e9g Hadron rates, no 10D original source, no PBH/BBN bound, no novelty/canon/EXEC, no BW ingestion inferred.

STATUS: CONDITIONAL_EXACT_BORSUK_ULAM_FULL_NONLINEAR_ALIAS / TWO_SYNTHETIC_INDEPENDENT_TESTS_PASS / ORIGINAL_ODE_NOT_RERUN / OWNER_REVIEW_PENDING / GITHUB_PENDING_BW_INGEST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
