---
artifact_id: IW_INT8_ROT033_METRIC_ORBIT_NATURAL_TT_STABILIZER_DESCENT_001_20261026
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_AFFINE_METRIC_TT_RAW_WAVEVECTOR_ALIAS_INTERFACE_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_FINITE_FLAT_INTEGER_METRIC_ORBIT_NATURALITY / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 ROT033 — source-typed metric-orbit descent of Fourier TT: stabilizer iff and alias falsifier

## Attribution; external host; no re-claim
**MT13 first** constructed source-matched affine-flat exactly transported metric-local E_g stencil and first detected naive raw-target-wavevector TT alias defect. INT8 ROT023–028 own nofold, angle, singular spectrum and one-sided repair diagnostics. INT8 ROT029–032 own the strong NO-GO for ONE SAME operator fixed independent of metric under all integral tensor pulls, followed by full spatial commutant and prime/squarefree structures. This result DOES NOT negate that no-go, but supplies its missing **metric-indexed family** distinction. M13/M14 owns original historical puretrace h=fI and masked K_A; Geeky-S11 owns original RAW-versus-matched and even-N real-cast defects; XH-S4 owns curved York; PRF11/12 other Lie-TT. No reattribution.

External MATURE foundation: G/H homogeneous spaces, stabilizer H-invariant seed data and associated bundles; see Encyclopedia of Mathematics, Homogeneous space (https://encyclopediaofmath.org/wiki/Homogeneous_space) and 2026 review Equivariant non-linear maps for neural networks on homogeneous spaces, DOI 10.1007/s44439-026-00004-z. This is group action DESCENT, NOT novel mathematical theory or physics.

## Source-typed setup and crucial composition order
Fix ODD grid N=2m+1 >=5 on G_N=(Z/NZ)^3. V_N is the REAL finite tensor Hilbert space of symmetric covariant 3x3 arrays. Source L2 metric is Euclidean, target metric is g_A=A^T A, A in SL3(Z), a spatially CONSTANT intrinsically flat positive Gram matrix. Define:
 (U_A H)(x)=A^T H(A x mod N) A .
Critically these pulls form an ANTI-REPRESENTATION:
 U_A U_B = U_(B A),  U_A^-1 = U_(A^-1).
U_A is an isometry from L2(I) to geometric L2(g_A), using N^-3 grid averages and index contractions by g_A^-1. The metric orbit is M_Z={g_A:A in SL3(Z)}; no claim about arbitrary g(x) or curved backgrounds.

Source P_I is literal odd-grid original helper apply_P_TT: on k!=0 raw signed Fourier k, symmetric rank2 transverse-traceless projector, on k0 the rank5 trace-free projector. It is an L2(I) orthogonal projector with overall rank 2N^3+3. Original E_alpha is the retained scalar-componentwise E_lin from apply_E, multiplier e(k)=1-4alpha sum_j sin²(pi k_j/N), scalar in tensor indices and hence commutes with P_I.

Retained helper file deepseek_python_20260627_a87249.py SHA256:
 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801.
Original historical full dtc0a_runtime_v0_3_1.py BYTE UNAVAILABLE, and original masked historical K_A is not re-executed.

## T033.1 — classification of ALL consistent natural operator families on integer-flat metric orbit

Let F_I be a fixed arbitrary real linear source operator and ask for an entire family F_g indexed ONLY by metric g in M_Z, satisfying the naturality law for every C in SL3(Z):
 F_(C^T g C) = U_C F_g U_C^-1.

THEOREM: A family with prescribed F_I exists iff the source operator F_I commutes with the stabilizer
 H=SO(3,Z)={O in SL3(Z):O^T O=I};
H consists of exactly 24 determinant-one signed coordinate permutations. If it exists, the family is UNIQUE GIVEN THE SEED F_I and is:
 F_(A^T A)=U_A F_I U_A^-1.                          (033.1)

Necessity: O in H preserves I, so naturality forces F_I=U_O F_I U_O^-1.

Choice independence: if A^T A=B^T B then O=B A^-1 belongs to SO3(Z), and B=O A. Since U_(OA)=U_A U_O and seed commutes U_O, transported outputs from A and B agree exactly. Sufficiency/naturality: g_(AC)=C^T g_A C and U_(AC)=U_C U_A. Uniqueness: every orbit metric g_A is reached from I. This is a concrete mature G/H stabilizer descent specialization, not a new general theorem. It does NOT assert uniqueness if F_I is left unspecified.

## T033.2 — original odd-grid source raw Fourier TT IS stabilizer-compatible

For signed coordinate permutation O, odd-grid signed Fourier representative k is mapped to an equally signed-permuted representative, with NO Nyquist ambiguity. The source rank2 TT projection at k transforms covariantly under orthogonal congruence H->O^T H O and k->O^T k. At k=0 the rank5 trace-free projector is likewise equivariant for O. Therefore [P_I,U_O]=0 for all 24 O, and the UNIQUE family continuing THIS source projector is:
 P_g=U_A P_I U_A^-1,  g=A^T A.                    (033.2)

Exact properties:
 - P_g^2=P_g; g-selfadjoint and g-orthogonal;
 - rank(P_g)=2N^3+3 on entire real symmetric tensor carrier;
 - metric trace vanishes on P_g images;
 - source-covariant filter family E_g=U_A E_alpha U_A^-1 (MT13) is well-defined and commutes with P_g;
 - composition/path law P_(C^TgC)=U_C P_g U_C^-1;
 - if B=O A with O among 24, P_(B^T B)=P_(A^T A) as literal operators on the SAME target tensor arrays.

SOURCE LIMIT: Odd N essential for asserting original helper an orthogonal projector; on EVEN grids the raw-k Nyquist real-cast effect independently identified by Geeky-S11 invalidates naive idempotence, not repaired by this theorem.

## T033.3 — near-unit gap from naive metric raw wavevector projector despite correct family existence

The correct transported family is NOT the naively recomputed target P_g^raw that treats wrapped target raw Fourier r as the unwrapped physical direction A^-T r. For input k=(m,m,0) and source genuine TT cross-polarization, shearing phi(x,y,z)=(x+y,y,z) with A=[[1,1,0],[0,1,0],[0,0,1]] gives
 ||P_g(U_A H) - U_A H||_g / ||U_A H||_g = 0,
 ||P_g^raw(U_A H) - U_A H||_g / ||U_A H||_g = N/sqrt(N^2+1).
The latter is the previous INT8 ROT023 principal-angle witness, now explicitly contrasted against the well-defined transported family; no original authorship claim for the angular mechanism.

Direct REAL source-helper FFT:
 N=5: exact-transported residual 2.54e-16, naive raw metric residual .980580675691 (formula .980580675691);
 N=9: exact-transported residual 9.45e-16, naive raw metric residual .993883734674 (formula .993883734674);
 N=15: exact-transported residual 1.41e-15, naive raw metric residual .997785157857 (formula .997785157857).
Thus RAW-TT defect is caused by the projector's target label choice and NOT impossibility of metric-indexed equivariance. It does not establish a local computational shortcut or any physical gauge claim.

## Independent fully executed falsifiers and custody

Source test (NumPy and literal unchanged preserved source helper):
 * 3 grids N5,9,15, all 24 O = 72 source stabilizer tests, worst rel residual 2.312381397670609e-16;
 * 5 explicit metrics per grid (I,S,S^2,T,S T) = 15 tests of idempotence, metric selfadjoint, tr_g=0, transported projector, source E_g intertwining and [E_g,P_g]=0 (each check passed with residual <8e-11);
 * all O on 2 nontrivial A and 3 grids = 144 representative-independence checks;
 * 6 metric path-composition checks;
 * 3 real FFT genuine source TT folded-angle checks against independent raw metric target projector;
 * unmodified apply_P_TT, apply_E imported ONLY after SHA byte check PASS.

Second separate SymPy exact-rational script, no NumPy, no helper:
 * 24 O x 5 k including zero x 3 symmetric tensor sources = 360/360 EXACT TT frame-covariance identities;
 * 24/24 exact metric g_A=g_(OA) identities;
 * 3 nonorthogonal fixed-grid A=I+N E21 (N5,9,15) source TT noncommutation counterexamples, proving no illicit claim that ALL real fiber congruences are stabilizer members.

**Rejected numerical reproducibility artifact and its repair:** raw JSON initially differed at 1e-16–1e-18 in final bit of floating self-adjointness residuals and near-unit alias ratios, despite identical PASSED unrounded assertions. The helper/source and all mathematical tolerances were unchanged; numbers are canonicalized ONLY AT SERIALIZATION to 12 decimal places, values <1e-12 stored as 0. Thus byte-level replay does not substitute for original unrounded tests. EXACT SymPy audit preserves rational arithmetic.

COMPLETE LOCAL 8-member ZIP:
 iw_int8_rot033_flat_integer_metric_orbit_natural_tt_bundle.zip
 SHA256 975e2905bd8157a0f9edfb64088761e210b2df6d5e51e2502f6e05635761d82d
 includes FULL 11KB source-faithful Polish Markdown report, standalone NumPy+retained helper reproduce script, independent rational SymPy audit, two JSON outputs, README, run log, and SHA256SUMS. ZIP CRC PASS, SHA256 6/6 PASS. CLEAN DIRECTORY 1: source helper SHA-checked, both JSON BYTE IDENTICAL. CLEAN DIRECTORY 2: helper explicitly absent, source status SKIPPED, mathematics and independent SymPy EXACT PASS. Complete scripts only in local Moderator ZIP, not falsely represented as GitHub code uploads.

## Non-maps and STOP
This concerns only FLAT, spatially constant, positive-definite integer-unimodular Euclidean metrics and original odd-grid RAW-k DTC0a conventions. No extension shown to arbitrary smoothly varying curved metrics, Lorentzian Box, York on curved spacetime, wave energy, Noether, GW polarizations, J3/K physical invariants or historical masked K_A. This is classical finite-group homogeneous-space mathematics, NO NOVELTY, NO CANON, NO EXEC, NO PHYSICAL UPGRADE; source-owner review/referee and actual BW event PENDING. No task cascade.
