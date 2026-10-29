---
artifact_id: IW_INT8_ROT047_INSERTED_RAW_TT_COMMUTATOR_NONCLOSURE_001_20261029
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_SOURCE_OPERATOR_COMPATIBILITY_AND_GAUGE_TYPE_GATE_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_SOURCE_AUXILIARY_UNMASKED_K_A_OUT_PROJECTED_COMMUTATOR_COUNTEREXAMPLE / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 ROT047 — source-native inserted RAW-k TT projection separates commuting z-shear operators

Date 2026-10-29. Science-first SOURCE-TYPED exact theorem, checked both on literal user auxiliary DTC0a and an independent source-free SymPy audit. No historic production masked K_A or physical claims.

## Others FIRST / external host
MT13 first identified incorrect raw target-k alias and correct affine E_g transport. INT8 ROT016 already FIRST found Q Lie_C E P leakage with TT input, INT8 ROT046 already FIRST established P_raw Lie_C I is NONZERO for one centered Lie derivative on constant puretrace I. THIS rotation establishes a NEW bounded TWO-generator source auxiliary compute_K_A_out full-grid consequence and a strict contrast to the SAME input's compute_K_C / compute_K_B. M13/M14 own original masked historic h=fI K_A and 5-mask calibration, Geeky-S11 even-RAW and source Lie distinct, PRF/XH separate theory. Mature compatible discrete complex host: J. Hyman and M. Shashkov, The Orthogonal Decomposition Theorems for Mimetic Finite Difference Methods, SIAM JNA 36 (1999) 788-818, DOI 10.1137/S0036142996314044. No novelty claim.

## EXACT SOURCE and carrier
Literal unchanged user helper deepseek_python_20260627_a87249.py, SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. Its functions lie_bracket, derivative, lie_derivative_tensor, apply_P_TT, projected_T, compute_K_C, compute_K_B, compute_K_A_out were actually inspected and executed. Distinguish this helper from byte-unavailable original HISTORIC production dtc0a_runtime_v0_3_1.py. No full masked source K_A reconstruction or historic mask RMS: all results below are full-grid tensor Frobenius RMS and odd N.

Fix ODD N>=7, spatial h=2pi/N, coordinates x=h*jx, y=h*jy. Real symmetric 3x3 covariant fields. Source derivative stencil is centered order2 with Fourier symbol s_N(k)_j=sin(h*k_j)/h; TT projector uses ORIGINAL raw signed integer FFT k, NOT matched s. Choose
  C1=e_z sin(x+2y),
  C2=e_z sin(x+y),
  H=I3 (constant puretrace),
  E_mode=Identity (exact theorem).
All fields are independent of z.

## EXACT T047.1 — nonprojected commutator zero, inserted-projector auxiliary commutator nonzero

The source discrete bracket is EXACT zero because C1 and C2 have only a z-component independent of z. For any z-independent H, the Lie action of such C=e_z f(x,y) is L_C H=H_{zj} partial_i f+H_{iz} partial_j f, with no convective z derivative. On H=I:
  L_C1 L_C2 I = sym(grad_d f1, grad_d f2) = L_C2 L_C1 I.
Thus source
  lie_bracket(C1,C2)=0,
  compute_K_C(C1,C2,I,Identity)=0,
  compute_K_B(C1,C2,I,Identity)=P_raw K_C=0
EXACT, not merely floating tolerances.

Define the auxiliary source
  K_A_out=P_raw L_C1 P_raw L_C2 I - P_raw L_C2 P_raw L_C1 I - P_raw L_[C1,C2] I.
The s(k2) vector is parallel to source k2=(1,1,0), so P_raw L_C2 I=0. But s(k1) not parallel to k1=(1,2,0), hence
  K_A_out= -P_raw L_C2 P_raw L_C1 I !=0.

Let s1=sin(h)/h, s2=sin(2h)/h, d=2*s1-s2. Let wp=(3,-2,0)/sqrt(13), wm=(1,0,0), ez=(0,0,1). EXACT whole-field identity at ALL nodes:
  K_A_out(x,y)
   =-[4*s1*d/65]*cos(2x+3y)*(wp outer wp -ez outer ez)
    -[s1*d/5]*cos(y)*(wm outer wm-ez outer ez).
Proof: raw-k1 transverse derivative vector r=d*(2,-1,0)/5. The second Lie produces sym(r,s1*(1,1,0))*cos(x+2y)*cos(x+y). Two Fourier sidebands are k+= (2,3,0), k-= (0,1,0), legal unwrapped raw signed vectors exactly when odd N>=7. TT_{k+} of sym(r,s1(1,1,0)) has coefficient 8*s1*d/65 times (wp outer wp-ez outer ez). TT_{k-} coefficient 2*s1*d/5 times (wm outer wm-ez outer ez). Cosine product splits these with factor 1/2 and the source commutator order yields the minus sign.

Two cosine modes are orthogonal in the full periodic grid L2. Each displayed TT polarization has squared 3x3 Frobenius norm 2 and each cosine spatial mean-square 1/2. Therefore exactly
  ||K_A_out||_full-grid-Frobenius-RMS = abs(s1*d)*sqrt(185)/65 >0.
Since d=2*sin(h)*(1-cos(h))/h~h² and s1→1,
  lim_(N odd→infty) N²||K_A_out||_RMS=4*pi²*sqrt(185)/65≈8.260992811957.
This is a SPECIFIC TWO-FIXED-SMOOTH-MODE result, not a universal operator bound or physics claim.

Numeric source checks:
 N7 0.119547885622938
 N9 0.083003449970277
 N11 0.059518210910559
 N15 0.034114554224514
 N21 0.018044843425072
 N31 0.008450188701759

## Independent tests and negative knowledge
ROOT A: complete standalone NumPy+SHA-pinned literal original helper, six actual full-grid cases N=7,9,11,15,21,31 with E_mode=Identity: bracket, compute_K_C, compute_K_B EXACT zero, compute_K_A_out FULL field agrees with exact two-sideband expression to <2e-11 (actually around 1e-15), projected_T second input zero, antisymmetry and source operator ordering PASS. THREE additional source E_lin alpha=.05 checks N7,9,15: bracket0 but K_C/K_B/K_A generally NONZERO, so do NOT attribute all E_lin residual to TT insertion. THREE further source zero pairs (C1/C2 with modes (1,2)/(2,1) or axis modes) PASS. 12 analytic N values to 1025; full N³ fields allocated only up to 41, N>41 pure SCALAR analytical calculation, never claimed full source run.

ROOT B: completely independently written SymPy/stdlib, NO NumPy, no original helper, exact 3x3 TT_k symbolic reduction on k1, k2 and sidebands, exact RMS coefficient identity; 169 rational gradient symbol cases PASS.

An EXPLORATORY FAIL correctly retained: initial main script erroneously allocated a HUGE full 3D N=1025 tensor, process OOM-KILLED. That failed test was not marked PASS. Corrected algorithm uses scalar-only for high N, reran all science and native source PASS.

Complete FULL Moderator conversation ZIP iw_int8_rot047_projected_commuting_shears_exact_source_KA_bundle.zip SHA256 cb59225ca96ea78352f215d559671f1720ef51636f68310c90036b0f2c6d057c, 8 members (longer Polish report, both complete independent runnable Python, both frozen JSON, README, RUNLOG, SHA256SUMS). ZIP CRC PASS; SHA256 7/7 payload PASS. CLEAN A and B with unchanged SHA-verified original helper: both JSON BYTE IDENTICAL. CLEAN C without original helper: exact JSON byte-identical and mathematical main identical, original source SOURCE_SKIPPED_NO_HELPER. User's original helper NOT redistributed. Complete Python/JSON in ZIP are source of record; this public report alone does not prove GitHub separately contains all runnable files.

## STOP
This case ACTUALLY executes auxiliary source compute_K_A_out unmasked, unlike ROT046's single projected_T. It DOES NOT reproduce historical production masked K_A, full historical h=fI protocols, five-mask RMS, DTC0a physical claims, J3/K, physical GR gauge/Noether/GW, even Nyquist real-casting, curved York, independent referee, owner uptake, actual BW ingest or EXEC. Altering RAW-k projector to a mimetic s_N(k) projector changes the source object and requires owner approval. No math novelty/physics upgrade. NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_TASK_CASCADE.
