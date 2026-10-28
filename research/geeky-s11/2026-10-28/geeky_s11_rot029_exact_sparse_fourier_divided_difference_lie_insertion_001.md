---
artifact_id: GEEKY-S11-ROT029-EXACT-SPARSE-SPECTRAL-DIVIDED-DIFFERENCE-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-28
problem_id: P3_DTC0A_FINITE_SUPPORT_EXACT_UNIFORM_LIE_INSERTION_FOURIER_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
class: EXACT_ALL_M_FINITE_FOURIER_SUPPORT_FRECHET_DIVIDED_DIFFERENCE
status: PROOF_PLUS_4019_EXECUTED_TYPED_CONTROLS_PASS / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# ROT029: Exact Fourier divided-difference shortcut for ALL uniformly inserted TT Lie positions

## Ownership, classical theory, and source typing

Geeky ROT015–017 FIRST proved even-grid realcast raw-k TT source pathology and constructed compatible real orthogonal projector B=GA. ROT021–023 established fixed-smooth TT memory observables; ROT024–025 single/repeated E alpha identification; ROT026 Lie vs repeated-filter placement noncommutation; ROT027 FIRST exact m+1-position uniform Lie placement mean U_m; ROT028 FIRST positive integer 3/5-node moment quadrature and sixth-order scalar low-band error. ROT029 studies a DIFFERENT algorithm for evaluating the EXACT U_m in a finite-Fourier-support generator host; it does NOT claim new mathematics or reassign previous work. Classical host: first divided differences and the polynomial Fréchet derivative (Daleckii–Krein, see J. A. Tropp, Matrix Analysis, Sec 14.3, https://www.tropp.caltech.edu/notes/Tro22-Matrix-Analysis-LN.pdf; N. J. Higham, Functions of Matrices, SIAM 2008). M14 historical source puretrace h=fI/masked K_A, PRF12 quantum process memory, INT8 metric TT are separate.

Source used: UNCHANGED retained auxiliary deepseek_python_20260627_a87249.py SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. Historic original production dtc0a_runtime_v0_3_1.py bytes are UNAVAILABLE. Full flat periodic real symmetric tensor N³, even N, h=2pi/N, FULL unmasked Frobenius L², source centered second-order stencil and THREE-TERM covariant tensor Lie L_C. The source auxiliary realcast A is NOT a true projector on even grids; we use strict B=GA from ROT017. E_alpha=I+alpha h² Delta2 has exact symbol e(k)=1-4alpha*sum_j sin²(pi k_j/N) and commutes with B. For 0<=alpha<=1/6 it is a contraction on full N³ but can have NEGATIVE eigenvalues if alpha>1/12.

## Exact theorem — all m, all alpha, all real symmetric input H

Fix any C with finite discrete Fourier support S and normalized Fourier coefficients c^r(s), independently of m. Write d_i(k)=sin(h k_i)/h. For a symmetric complex tensor Fourier fibre V at input wavevector k, define the EXACT source Lie transition M_s(k):
 [M_s(k)V]_(ij)
 = i*(sum_r c^r(s)d_r(k))*V_(ij)
 + i*d_i(s)*sum_r c^r(s)V_(rj)
 + i*d_j(s)*sum_r c^r(s)V_(ir).
All three terms and the actual CENTRAL derivative on C are required.

Write T=B L_C B and the ROT027 exact uniform insertion mean:
 U_m=(1/(m+1))*sum_(ell=0)^m E^(m-ell) T E^ell, for integer m>=0.
Then for every output mode k' on the signed periodic FFT grid, EXACTLY:
 (U_m H)^hat(k')
 = B_(k') * sum_(s in S) u_m(e(k'),e(k'-s)) *
      M_s(k'-s)[B_(k'-s)*Hhat(k'-s)],
where
 u_m(a,b)=(a^(m+1)-b^(m+1))/((m+1)*(a-b)) if a!=b,
 u_m(a,a)=a^m.
The formula is EXACT even at zero and mixed-sign a,b, source Nyquist modes (correct B!), m odd/even, any real alpha; no root or fractional E power is taken. Proof: for each source-target pair, every E^(m-ell) T E^ell contributes identical projected M_s and scalar e(k')^(m-ell)e(k)^ell; geometrical series yields u_m. This is precisely U_m=[D(X->X^(m+1))_(X=E)[T]]/(m+1), a classical polynomial Frechet derivative.

## Uniform stability and numerical pitfall

For all |a|,|b|<=1, |u_m(a,b)| <= average_(ell) |a|^(m-ell)|b|^ell <=1. Thus for SOURCE-LEGAL 0<=alpha<=1/6, ||U_m||_(L2->L2)<=||T|| independently of m. However ||T|| can depend on N due to Lie differentiation; this is NOT an N-uniform first-order-operator bound.

Naively evaluating (a^(m+1)-b^(m+1))/(a-b) loses floating-point precision when a≈b; the provided runnable algorithm handles a=b, zero, same-sign near-equality using log1p/expm1, and opposite signs/parity separately. It works with negative full-grid E eigenvalues and m up to 50001 in executed stress. It is ALGEBRAICALLY exact, not machine bit-exact; FFT and floating-point rounding remain.

## Cost — precise conditional improvement over ROT028

If |S|=O(1) as N increases, a direct Fourier implementation requires O(N³ log N) FFT plus O(|S|N³) tensor transitions and scalar u_m evaluations, with no loop over m and no m+1 or five Lie black-box calls. Power evaluations still have arithmetic/bit costs related to m; do not claim literal O(1) bit complexity. This is a specialized SPECTRAL implementation, not equivalent to one generic black-box Lie call. If |S| grows to N³, the straightforward loop can require O(N^6) work and may be WORSE than ROT028. No universal runtime claim; no extrapolation to moving metrics, arbitrary broadband generator or historical h=fI K_A.

## Executed independent falsifiers and clean custody

(A) Original from-scratch NumPy real 3D FFT compatible B + exact Fourier transition, compared to explicit m+1-sum. N8/12/16/24, alpha0/.05/1/12/1/6, random/near-Nyquist/smooth H, m0/1/2/3/5/8/12, plus longer m~0.02 N². 796/796 checks PASS; maximum normalized difference 4.18434e-16, discarded imaginary <=1.25820e-15.

(B) LITERAL original frozen source 3D apply_P_TT, full three-term lie_derivative_tensor and apply_E, with correct separate G mask, all m+1 positions N8/12/16 for random and near-Nyquist H. 90/90 checks PASS, max relative difference 1.55253e-15.

(C) MORE GENERAL C with THREE nonzero VECTOR COMPONENTS and EIGHT nonzero Fourier modes: C^x=0.15sin y, C^y=cos x+0.2sin 2x, C^z=0.1cos z. A separate spectral implementation checks every M_s against full original source 3D real Lie and B. 30/30 checks PASS, max relative gap 1.44878e-15. Preliminary expected support count 6 was corrected to the actual 8 (±x, ±2x, ±y, ±z); no failed result was hidden or counted.

(D) Independent exact stdlib Fraction checks of 81 signed/zero (a,b) pairs x 13 m values and 2x2 polynomial Frechet derivative, together with 95-digit Decimal stress at m up to 50001, including opposite-sign near cancellation. 3103/3103 PASS, maximum float absolute fraction error 2.22e-16, worst high-precision float-relative gap 1.264e-14 relative to SAME binary-float inputs. Rational polynomial arithmetic is not an exact-trigonometric spectral certificate.

TOTAL 4019/4019 TYPED EXECUTED PASS. One Moderator-local user-conversation ZIP includes full expanded 11KB Polish report, FOUR original executable source files, FOUR output JSON, four stdout logs, unchanged original frozen helper, README and SHA manifest. ZIP SHA256 16939882e703735617a4b7e964ad837f5773f8e40b13843c95fca0e84aad8c92. Clean extracted ZIP CRC PASS, 15/15 content SHA256 PASS, all FOUR scripts rerun and FOUR JSON BYTE IDENTICAL PASS. ZIP/code not claimed separately published to GitHub.

## Firewall

Source auxiliary flat full unmasked mathematical result ONLY, no original production DTC, original h=fI or masked K_A, no NASH J3/K, GR/GW/PBH/BBN physics, no independent referee, BW ingestion, scientific-owner adoption, canon or EXEC. No novel theorem priority. NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
