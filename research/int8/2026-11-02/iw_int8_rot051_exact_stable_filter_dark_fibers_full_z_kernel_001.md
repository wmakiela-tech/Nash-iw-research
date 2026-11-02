---
artifact_id: IW_INT8_ROT051_STABLE_FILTER_DARK_Z_FIBERS_001_20261102
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_SOURCE_OPERATOR_COMPATIBILITY_AND_GAUGE_TYPE_GATE_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_STABLE_E_LIN_FILTER_DARK_SECTORS_AND_FULL_HZ_KERNEL_N7_N9 / SOURCE_TYPED / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# INT8 ROT051 — exact filter-dark z-Fourier fibers and complete H(z) kernel on N=7 and N=9

Scientific date 2026-11-02. All results are for the literal auxiliary source compute_K_A_out, not the unavailable historic production masked K_A. BW ING, independent referee, source owner and Moderator EXEC PENDING.

## First ownership, mature hosts, hard source boundaries

MT13 owns original affine E_g and folded target-RAW-k alias; INT8 ROT016 owns Q Lie E P for TT input; INT8 ROT046 owns single Lie derivative versus RAW-k TT mismatch; INT8 ROT047 first commuting shears Identity unmasked KA; INT8 ROT048 first same E_lin eigenshell pair at H=I; INT8 ROT049 first f(z)I robustness and f(x) negative control; INT8 ROT050 FIRST: any symmetric H(z) has K_C=K_B=0 and the CONSTANT S KA kernel dimension3. ROT051 adds ONLY a complete all-H(z) kernel classification for N7 and N9, and identifies ALL stable second-filter spectral zeros for this shear pair at arbitrary odd N>=7. Historic h=fI masks/production K_A owned by M13/M14 and remain unavailable. Geeky even Nyquist, PRF Lie, XH York separate. No novel general mathematical theory priority: mature finite Fourier diagonalization, cyclotomic irreducibility, finite-field rank certificates and mimetic compatible discretizations. J. Hyman and M. Shashkov (1999), The Orthogonal Decomposition Theorems for Mimetic Finite Difference Methods, SIAM JNA 36(3) 788-818 DOI 10.1137/S0036142996314044 provides general background only.

Literal user-retained unchanged source deepseek_python_20260627_a87249.py SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801 imported AFTER byte verification; exact helper apply_E, projected_T and compute_K_A_out actually executed. N odd >=7, h=2pi/N, signed RAW FFT k TT, centered second order derivative and full 9-component real tensor Frobenius RMS. Inputs H(z) are arbitrary real Sym2(R3) tensor fields independent of x,y. Shears C_a=e_z sin(x+2y), C_b=e_z sin(2x-y), a=(1,2,0), b=(2,-1,0). E_lin=I+alpha*h²*Delta2 for alpha in [0,1/6], with Identity alpha0. The whole historic dtc0a_runtime_v0_3_1.py byte unavailable; no historic masked K_A or calibration executed.

## T051.1 — exact harmonic operator factorization

For each source z-Fourier sector ell (signed integer between -m and m, m=(N-1)/2), write H(z)=S_ell exp(i ell z). Original E_lin first multiplies H by scalar
  e0(ell)=1-4alpha sin²(pi ell/N).
The original first centered Lie derivative creates ONLY source Fourier modes (+/-a,ell) or (+/-b,ell). The ORIGINAL second E_lin in the nested projected_T multiplies EVERY one of these modes by the SAME
  e_shell(ell)=1-4alpha[sin²(pi/N)+sin²(2pi/N)+sin²(pi ell/N)].
Original RAW-k TT and remaining Lie terms are independent of alpha. Hence the ENTIRE REAL SOURCE OPERATOR is EXACTLY block factored:
  **K_A_out|_ell = e0(ell) * e_shell(ell) * G_ell**,
with G_ell the unchanged source operator block at alpha0 (Identity). This is an algebraic operator identity, not merely singular-value equality. All source steps preserve ell; all z harmonic blocks orthogonal in full-grid norm. The first scalar e0(ell)>=1/3 for stable alpha. By ROT050 K_C=K_B=0 for EVERY H(z) and E_lin on this equal-eigenshell pair. These are not physical gauge identities and do not apply to arbitrary H(x,y,z).

## T051.2 — ALL stable intermediate filter-dark sectors in this specified family

Cyclotomic root-of-unity identities, independently verified EXACT by reduction modulo Phi7 and Phi9:
  sin²(pi/7)+sin²(2pi/7)+sin²(3pi/7)=7/4,
  sin²(pi/9)+sin²(2pi/9)+sin²(4pi/9)=3/2.
Therefore e_shell(ell)=0 for:
  N=7, ell=+/-3, alpha=1/7 (STRICTLY inside stable [0,1/6]);
  N=9, ell=+/-4, alpha=1/6 (stable endpoint).
Each event causes complete annihilation of all SIX complex symmetric tensor polarizations at the signed ell, equivalently a TWELVE-dimensional REAL cos/sin tensor fiber. These are true spectral filter zeros, not just disappearance of a particular polarization under original RAW-k TT.

No other e_shell zeros occur for alpha in [0,1/6] and ANY odd N>=7, for this pair:
N7 ell<=2 has sine-square sum <3/2; one exact check uses sin²(3pi/7)-sin²(2pi/7)=sin(2pi/7)sin(pi/7)>(sqrt2/2)sin(pi/8)>1/4. N9 ell<=3 is strictly less than its ell4 maximum3/2. For N>=11 write x=pi/N<=pi/11 and ell<=m. Then sine-square sum <=F(x)=sin²x+sin²(2x)+cos²(x/2). For 0<x<=pi/9, derivative F'(x)=sin(2x)+2sin(4x)-sin(x)/2>0, so F(x)<F(pi/9)=3/2. Since a stable zero needs sine-square sum >=1/(4alpha)>=3/2, the list is EXHAUSTIVE for filter-factor zeros. This does NOT prove absence of geometric G_ell kernels at larger N.

Crucial direct source check: at both dark critical parameters, the FIRST ORIGINAL source projected_T(C_b,H) has nonzero full field norm, respectively about 3.450009216 (N7 ell3) and 4.443091731 (N9 ell4) on a mixed tensor. Yet applying the subsequent original E_lin to this NONZERO projected field annihilates it to floating tolerance. Thus source darkness occurs at the intermediate E, not by substituting source input0 or changing the RAW-k TT definition.

## T051.3 — exact geometry core rank for ALL ell on N7 and N9

Use t_N=2cos(2pi/N). Both irreducible minimal polynomials over Q:
 p7(t)=t³+t²-2t-1;
 p9(t)=t³-3t+1.
All centered first-derivative factors share a nonzero s1=sin(h)/h; modulo this factor s2/s1=t_N and s_ell/s1=U_(ell-1)(t_N/2), with U Chebyshev second-kind, an INTEGER polynomial in t_N. Projectors at signed integer k have rational coefficients. Hence each 36-by-6 complex Fourier coefficient matrix for G_ell (4 sidebands x full 3x3) has entries rational in t_N with invertible integer denominators.

A rank6 finite-field specialization supplies an EXACT algebraic certificate: if a rational 6x6 minor vanished at the real algebraic t_N, irreducibility forces its numerator to be divisible by p_N over Q, and then it would vanish modulo any prime p at a root r of p_N with invertible denominators. Contraposition: finding a nonzero specialized minor proves exact full rank6 over Q(t_N).

Independently written source-free SymPy/stdlib program derives ALL original Fourier-symbol TT projectors in exact Fp arithmetic, uses the integer Chebyshev recurrence, computes Gaussian elimination and then the determinant of an explicitly indexed minor, and records each witness.

N=7: prime41 root r14 of p7 mod41. For ell 1,2,3: six-by-six minors modulo41 respectively 22,9,38, ALL NONZERO: rank(G_ell)=6.
N=9: prime53 root r4 of p9 mod53. For ell 1,2,3,4: six-by-six minors modulo53 respectively 16,42,30,46, ALL NONZERO: rank(G_ell)=6.
For ell=0 rank3 is the exact symbolic constant-S result FIRST proven ROT050; the independent modular audit also returns rank3. The finite-field program exposes rows of all rank witnesses, not just a boolean. This is full proof of actual REAL rank in all nonzero z fibers for exactly N7/N9, not a floating singular-value inference.

NEGATIVE KNOWLEDGE: preliminary finite field p37,r5 for N9 ell4 gave rank5 from an accidental drop under SPECIALIZATION and was INCONCLUSIVE; this was not a counterexample to real rank6. It was replaced by certified p53,r4 with nonzero 6x6 minor46. Mathematical conclusion is from successful cert, not from preliminary failed specialization.

## T051.4 — COMPLETE real H(z) kernel on N7 and N9, stable alpha

At ell0 the real constant symmetric tensor kernel is EXACTLY the planar xy block, dimension3 (ROT050). Every nonzero signed ell carries complex rank6 of G_ell; a conjugate pair ±ell gives 12 real tensor inputs (six real polarizations times cos and sin). If e_shell(ell) !=0, it contributes ZERO to the kernel; if e_shell(ell)=0, it contributes ALL 12 real dimensions. Different ell outputs cannot cancel because z frequency is preserved.

Thus, for all stable alpha in [0,1/6]:
  N7, alpha!=1/7: real dim ker=3, rank=39 (on 6N=42 input);
  N7, alpha=1/7: real dim ker=15, rank=27;
  N9, alpha!=1/6: real dim ker=3, rank=51 (on 6N=54 input);
  N9, alpha=1/6: real dim ker=15, rank=39.
Only the original source auxiliary UNMASKED KA_out over full-grid Sym2 H(z) is classified. This is NOT a claim for arbitrary x,y-dependent tensor fields.

For N>=11, T051.2 excludes stable INTERMEDIATE FILTER spectral zeros, but T051.3 rank6 was NOT proven for these grids. Main numerical Fourier scan tested N=7,9,11,15,21,31 at alpha0, .05 and 1/6, 150 nonnegative-ell matrix cases. Nonzero ell numerically full rank except the two predicted dark factors (the actual critical alpha1/7 was tested separately); DO NOT upgrade scan to exact universal rank theorem.

## Executed source, reproducibility, provenance and STOP

ROOT A complete standalone NumPy Fourier operator + original byte-SHA-checked source: 150 exact-formula scalar factorization checks for all six singular values, 36 REAL original full-grid K_A_out source cases including BOTH dark sectors x all six independent Sym2 polarizations x cos/sin, plus ordinary off-dark nonzero controls. All source predicted ENTIRE fields agree to 1.1e-10. Also two native nonzero intermediate P_TT then E_lin->0 checks. No historic masked production operator tested.

ROOT B entirely independent SymPy/stdlib, NO NumPy/NO original helper: two exact cyclotomic identities, exact irreducibility and nine finite field rank certificates, seven full rank6 for ell>0. First unsuccessful N9 F37 specialization retained as negative knowledge; final F53 certificate PASS.

Frozen Moderator-local 8-member ZIP: iw_int8_rot051_exact_stable_filter_dark_fibers_bundle.zip SHA256 09520c69380dbb25f233379230fc420a833ccc08aeb3216b4049a2a5f5ce914d, 7 payload files and SHA256SUMS. ZIP CRC PASS, SHA256 7/7 PASS. Two fresh ZIP extractions with literal unchanged SHA-pinned original helper: both main and exact JSON BYTE IDENTICAL. Third clean extraction WITHOUT original helper: independent exact JSON BYTE IDENTICAL and all 150 mathematical main records unchanged; native source explicitly SOURCE_SKIPPED_NO_HELPER. Full Polish report, two complete runnable scripts, both frozen original JSON, README, RUNLOG and SHA sums are in the ZIP. Original helper code not redistributed.

Epistemic stop: no complete historic production dtc0a_runtime_v0_3_1.py, masked historic h=fI K_A or five mask calibration, even RAW-k Nyquist treatment, curved York, physical GR gauge, Noether, GW energy, J3/K, observations or experiments. No physical upgrade, general mathematical novelty, canon or EXEC. BW actual ingest, independent referee, original source owner adoption and Moderator approval PENDING. NO_NEW_TASK_CASCADE.
