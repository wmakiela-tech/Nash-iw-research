---
artifact_id: IW_INT8_ROT041_EXACT_FULL_AND_MEANZERO_TT_SHEAR_NORM_001_20261028
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_FLAT_AFFINE_METRIC_NUMERICAL_COORDINATE_VS_GEOMETRIC_NORM_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_SOURCE_TYPED_WHOLE_FOURIER_TT_NORM / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 ROT041 — EXACT full and mean-zero norm of natural TT under any integer xy shear

2026-10-28. MATHEMATICAL SOURCE-TYPED result, not historical production masked K_A. BW ING / external referee / owner uptake / Moderator EXEC all PENDING.

## Owners, source, mature external host

MT13 FIRST established exactly transported affine E_g and first raw target-k TT alias. INT8 ROT033 FIRST supplied stabilizer descent for the metric-indexed source family. ROT034–039 FIRST own separate support/locality results. INT8 ROT040 FIRST proved the constant-tensor metric-tracefree projector fixed-coordinate norm (t^4+4t²+3)/3, yielding ONLY a lower bound on the entire P_g. This ROT041 computes the WHOLE exact norm. M14/M13 historical h=fI masked K_A, Geeky even-grid RAW real-cast, XH curved York and PRF distinct Lie/TT remain separate.

External mature mathematical HOST: Wielandt inequalities for angles between images of orthogonal subspaces. Minghua Lin and Gord Sinnamon, The generalized Wielandt inequality in inner product spaces, Eurasian Mathematical Journal 3(1), 72–85 (2012), https://www.mathnet.ru/php/archive.phtml?jrnid=emj&option_lang=eng&paperid=75&wshow=paper ; Karl Gustafson, The geometrical meaning of the Kantorovich–Wielandt inequalities, Linear Algebra and Its Applications 296 (1999), 143–151, DOI 10.1016/S0024-3795(99)00106-8. No mathematical or physical NOVELTY claim.

## Source-defined exact carrier

Odd N>=3, 3-torus (Z/N)^3, ALL real symmetric covariant rank2 tensor fields, flat Frobenius L2. Distinct MEANZERO carrier removes ONLY Fourier k=0. The unchanged retained auxiliary DTC0a source apply_P_TT has signed RAW-k nonzero Fourier projection P_kH=Q_k H Q_k−(tr Q_kH)Q_k/2, Q_k=I−kk^T/|k|². Its nonzero modes are real 6D Frobenius orthogonal rank2 projectors; original k0 is rank5 tracefree, but is NOT needed for the new sharp norm.

Literal original unchanged auxiliary helper SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. Historical entire production dtc0a_runtime_v0_3_1.py BYTE UNAVAILABLE.

For integer t, A_t=[[1,t,0],[0,1,0],[0,0,1]], g_t=A_t^T A_t. Tensor-and-node pull U_A H(x)=A^T H(Ax mod N)A; natural family P_g=U_A P_I U_A^-1. The geometric tensor L2(g) differs from fixed-coordinate Frobenius L2.

## EXACT THEOREM T041.1 — FULL and MEANZERO norms coincide, known exactly

For EVERY odd N>=3 and EVERY integer t, including t NOT divisible by N:
   ||P_(g_t)||_(FULL fixed-Frobenius L2)
   = ||P_(g_t)||_(MEANZERO fixed-Frobenius L2)
   = (t^4+4t²+2)/2.                                     (T041.1)

Meanwhile for both source carriers,
   ||P_(g_t)||_(geometric L2(g_t))=1.                    (T041.2)

GLOBAL UPPER PROOF: For invertible L on a Hilbert space with condition κ(L)=||L|| ||L^-1||, and any orthogonal idempotent P, the classical Wielandt smallest-angle bound gives
   ||L P L^-1|| <= (κ(L)+κ(L)^-1)/2.                     (W041)
Indeed transformed orthogonal subspaces have cosine of their minimum angle at most (κ²−1)/(κ²+1); the norm of the oblique projection is reciprocal of sine of that angle. On Sym²(R³), congruence C_A:H↦A^T H A has singular values products σ_i(A)σ_j(A); thus κ(C_A)=κ(A)^2. Spatial node permutations add no L2 condition factor. The bound controls ALL Fourier modes, including wrapped target mode labels, and holds for the original whole operator.

For A_t, A_t A_t^T has eigenvalues λ+,1,λ−, λ+λ−=1 and λ++λ−=t²+2. Therefore κ(A_t)^2=λ+/λ−=λ+², yielding
  (κ(A_t)^2+κ(A_t)^−2)/2
  =(λ+²+λ−²)/2=((t²+2)²−2)/2=(t^4+4t²+2)/2.

EXACT LOWER AND ATTAINMENT: k=(0,0,1) is a LEGAL NONZERO source Fourier vector for every odd N and is fixed by xy shear. Represent tensor congruence by real 6x6 Frobenius-orthonormal C_t, and source TT at k=e3 by rank2 P_e3. Exact independent SymPy shows F_t=C_t P_e3 C_t^-1 has
  eigenvalues(F_t^T F_t)
  = {[(t^4+4t²+2)/2]^2, 1, 0,0,0,0}.
At t=0 two positive eigenvalues coincide at 1 (multiplicity2). The largest singular value equals the GLOBAL upper bound, attained by a REAL cosine field on k=e3 with a right singular input tensor. That field has EXACTLY zero spatial mean. Thus T041.1 holds in BOTH full and MEANZERO carriers. No nonzero-frequency candidate can exceed it by the global bound.

## EXACT correction/completion of INT8 ROT040

The ROT040 constant-mode norm and new full TT norm are distinct:
  ||Q_(g_t)||_F=(t^4+4t²+3)/3,
  ||P_(g_t)||_F=(t^4+4t²+2)/2.
Their ratio is
  (3/2)*(t^4+4t²+2)/(t^4+4t²+3) -> 3/2 for |t|->infinity.

| t | k0 Q_g (ROT040) | FULL/MEANZERO P_g EXACT (ROT041) | L2(g) P_g |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 |
| 1 | 8/3 | 7/2 | 1 |
| 3 | 40 | 119/2 | 1 |
| 5 | 728/3 | 727/2 | 1 |
| 10 | 10403/3 | 5201 | 1 |
| 20 | 161603/3 | 80801 | 1 |
| 31 | 927368/3 | 927367/2 | 1 |

The new amplification is NOT caused by k0, as the extremizing wavevector is e3. It persists when t is a multiple of N and the spatial nodes do NOT move at all under the shear modulo N. Fixed-component conditioning does not imply a geometric naturality defect. On the source scalar E_lin side, ROT040 already showed fixed scalar E_lin stays unchanged for congruence-kernel shears; that is a separate operator, not an assertion of production stability.

## Independently EXECUTED verification

ROUTE A, full all-mode NUMPY: N=3,5,7,9,15 crossed with t=0,1,3,5,10; 25 COMPLETE enumerations of all nonzero signed raw Fourier modes, total 22,970 independent 6x6 block SVDs. Every observed maximal singular value agrees with theorem; ZERO upper-bound violations; axial e3 attains the same norm; its second singular is1; tests run on unrounded arrays.

SOURCE DIRECT: user-retained unchanged auxiliary apply_P_TT invoked AFTER SHA256 validation on TEN real cosine fields whose mean is zero, (N,t)=(3,0),(3,1),(3,3),(5,1),(5,5),(5,10),(7,0),(7,7),(9,1),(9,9). Use the 6D right singular maximizing tensor, transport it BACK to source, apply LITERAL helper, transport its output, and compare to separate six-dimensional formula and exact amplification, threshold 3e−9 on original floating arrays. Every case PASS. No original masked historic K_A or full production runtime was run.

ROUTE B, completely separate symbolic exact SymPy with NO NumPy and NO helper: full 6x6 congruence C_t, P_e3, symbolic F_t²=F_t, eigenvalues(F_t^T F_t) exactly as stated, source k0 metric-tracefree comparison, ten exact rational t=0,1,2,3,5,7,10,20,31,62: trace, trace-square and idempotence exact checks PASS.

NEGATIVE KNOWLEDGE: first SymPy test compared an expanded polynomial with factored version via raw equality and failed despite actual identity. After replacing by symbolic simplification, t=0 degenerate singular-value multiplicity needed a distinct test; fixed then fully rerun PASS. No mathematical counterexample was concealed or falsely declared passing.

REPRO: complete 8-member Moderator-local ZIP iw_int8_rot041_exact_full_mean_zero_tt_norm_repro_bundle.zip; SHA256 6ef4eec8b4715555433507aee2a1ddc6d8bc317333f3c342fa562a5ae1cf4254. Complete longer Polish mathematical report SHA256 9525d542d1a0b2864d1cf12a191a89122ef90a721e019caa50c25cfd42b9d5cb; TWO independent standalone Python, TWO JSON, README, RUNLOG, SHA256SUMS. ZIP CRC PASS / member SHA256 7/7 PASS. Clean extract A with original unchanged SHA-verified helper reproduced BOTH JSON BYTE IDENTICAL; clean extract B without helper reproduced EXACT SymPy JSON byte-identical and all math fields identical, original source status SOURCE_SKIPPED_NO_HELPER. No original helper redistribution. The ZIP is a Moderator conversation artifact; individual runnable code only claimed there unless separately uploaded.

## Strict stop

Only odd raw-k auxiliary source, flat g_t constant integer xy shear, fixed Frobenius versus correct geometric L2, full real symmetric tensor carrier and meanzero version. NO even-grid Nyquist cast, NO historical masked K_A/h=fI, NO full historical production runtime, NO arbitrary curved York, GR gauge, Noether, physical J3/K, GW energy, physical experiments, mathematical novelty, canon, EXEC. BW/referee/owner/Moderator adoption pending; no task cascade.
