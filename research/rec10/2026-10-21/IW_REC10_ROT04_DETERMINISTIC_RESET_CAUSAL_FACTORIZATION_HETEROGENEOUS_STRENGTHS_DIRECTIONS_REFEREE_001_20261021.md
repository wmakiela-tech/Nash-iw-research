# REC10 ROT04 — Causal triangular factorization: heterogeneous sensing and reset directions

DATE: 2026-10-21
FROM: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10
CLASS: CLAIM-LOCAL_REFEREE / STRESS_TYPE_HARDEN / EXACT GENERALIZATION
VERDICT: PASS_WITH_STRENGTHENING for Geeky-S10 fixed-time triangular factorization; PASS_WITH_SCOPE for the separate weak-sampling storage ceiling.
AUTHORITY: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_TASK
CURRENTNESS: reviewed #iw-dispatch after REC10 ROT03, #iw-alerts (no new blocker), and GitHub commits through 2026-10-21 18:12 CEST.
REVIEWED FULL SOURCES:
- Geeky-S10 causal factorization: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s10/2026-10-21/geeky_s10_fixed_time_reset_passive_sample_triangular_equivalence_001.md (observed blob 8bc3bfeb3bfb4daeb7d52a8cfe99b9188275fe78)
- Geeky-S10 arbitrary-count weak measurements: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s10/2026-10-21/geeky_s10_int8_weak_measurement_accumulation_ceiling_001.md (blob 3a03a4f5fa192e7b5be97d79404f31334fb4ec39)
- INT8 originating finite protocol: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/int8/2026-10-21/iw_int8_weak_protocol_quotient_identification_vs_bounded_actuation_bridge_001.md (blob c0aaeadd2ee3b5faad54c27f0e297ca8a8a07937)
- LT5 scalar target amplitude-limited output feedback: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/2026-10-21/lt5_scalar_target_amplitude_limited_output_feedback_minimax_decomposition_001.md (blob aa94eea723f75d87a5f83c51c6a9779d663537c0); different controller-resource class, NOT audited as part of this claim.

## 1. Freeze the native claim

Geeky-S10 proves C_s = s (I+sH)^(-1) M for deterministic fixed sampling times, one constant sensor/reset direction e and strength s; rank(C_s)=rank(M) and ker(C_s)=ker(M) for every nonzero s. Blackwell-equivalence is only to PASSIVE MEAN with TRANSFORMED noise, not to same-noise passive sampling.

Independent source-level referee: PASS EXACT. State-recursion proof and invertibility of the unit lower-triangular factor are sound.

## 2. Independent exact extension — no common s or common direction needed

Let x'(t)=Gx(t), x0 in R^n, deterministic fixed t1<...<tm. At time j, choose a predetermined readout row e_j^T, predetermined reset direction d_j, and known real strength s_j. Define noiseless output and reset:
  b_j = s_j e_j^T x_j^-,
  x_j^+ = x_j^- - d_j b_j.
The vectors e_j,d_j need not coincide, and strengths s_j need not be equal or even nonzero. All maps remain linear and deterministic, and timing is fixed independently of x0 or any noisy outcomes.

Let D=diag(s1,...,sm), passive-sample matrix M with row M_j=e_j^T exp(G t_j), and strictly lower-triangular H defined for k<j by
  H_jk=e_j^T exp(G (t_j-t_k)) d_k,
  H_jk=0 for k>=j.

Superposition of previous state kicks gives
  x_j^-=exp(Gt_j)x0 - sum_{k<j} exp(G(t_j-t_k))d_k b_k.
Hence b=D(Mx0-Hb); equivalently
  (I+D H)b = D M x0.
Because D H is strictly lower triangular, det(I+DH)=1 and
  C=(I+D H)^(-1)D M.

Thus EXACTLY, for every finite deterministic protocol of this class:
  rank C = rank (D M);
  ker C = ker (D M).
When every s_j !=0, D is invertible, so rank C =rank M and ker C=ker M.
For s_j=0, it is NOT generally legal to replace DM by M, since the zero-strength row disappears.

This is a strengthening of the fixed-e, common-s source result, not a correction asserting its source theorem false. Mathematical host: causal linear state-space elimination / finite Volterra triangular algebra. NO novelty claim.

## 3. Separating tests and quantitative guard

Test A: n=3, m=5, G a fixed seeded real matrix; different normalized e_j and d_j, strengths (0.03,0.5,0.01,0.85,0.15), times (0.1,0.35,0.8,1.1,1.9). Independently assembled direct reset propagation for each canonical initial basis vector, and compared with exact triangular formula. Max entrywise deviation 2.220446049250313e-16. Both computed ranks =3; det(I+DH)=1.
Test B: set some s_j=0. Formula and rank(C)=rank(DM) still hold; any claim that rank must equal full passive M without all nonzero strengths is invalid. Explicit two-dimensional separator: M=I_2 and D=diag(1,0), so rank(DM)=1 despite rank M=2.

## 4. Crucial NON-TRANSFER to arbitrary-count weak-energy theorem

Geeky-S10's separate weak-measurement ceiling assumes SAME sensor/reset e, a positive semidefinite P with P e=e and G^T P+PG<=0, and b_j=s_j e^T x_j^- for all j. Its identity
  Delta V_j=s_j(2-s_j)(e^T x_j^-)²,
  b_j²=[s_j/(2-s_j)] Delta V_j
is correct; the telescoping uniform bound sum b_j² <= [epsilon/(2-epsilon)] x0^T P x0 is PASS within this precise class. Scalar G=0 sharpness witness is exact.

However triangular rank equivalence holds for many MORE deterministic protocols than the storage ceiling. Do NOT export the O(sqrt epsilon) bound to arbitrary noncollinear d_j/e_j or unverified common P.

Exact falsifier of such an export: n=2, G=0, constant e=(1,0), d=(0,1), any fixed 0<s<=epsilon, x0=(1,0). Each update x^+=x^- -s d(e^T x^-) changes only coordinate 2, leaving coordinate 1 fixed. Every record equals b_j=s, so sum_{j=1}^N b_j²=N s², unbounded as N grows. The causal rank factorization STILL holds. This failure is explained by lack of the co-axial ellipsoidal storage dissipation identity; it is not a counterexample to Geeky-S10's bounded-energy theorem.

Separate static-linear gain and hard actuator amplitude; the LT5 turn-2 minimax is a distinct resource class. The original fixed-noise Blackwell statement generalizes for all s_j !=0 to invertible readout map z=D^{-1}(I+DH)y=Mx0 + D^{-1}(I+DH)eta, provided noisy readout does NOT feed into state reset; transformed noise is not the same noise law.

## 5. Scientific disposition / reopen

GEEKY_FIXED_TIME_TRIANGULAR: PASS exact; scope may be broadened to predetermined (s_j,e_j,d_j), including arbitrary zero strengths with rank(DM) rather than rank(M).
GEEKY_WEAK_ACCUMULATION_STORAGE: PASS exact ONLY in the certified co-axial model, no extension to noncollinear resets.
INT8_WEAK_FIXED_TIME_RANK: stronger exact factorization removes reliance on small-s analytic continuation in its admissible setting.
MATHEMATICAL_NOVELTY: NO CLAIM. PHYSICAL / QUANTUM / DTC UPGRADES: BLOCKED.
SOURCE-OWNER acceptance and BW ingestion: not implied by storage. Reopen only on source correction, changed measurement-update semantics, adaptive timing, actual physical source contract, or contradictory exact test. Otherwise STOP.
