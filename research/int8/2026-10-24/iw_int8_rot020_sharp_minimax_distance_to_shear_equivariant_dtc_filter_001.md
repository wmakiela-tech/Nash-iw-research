---
artifact_id: IW_INT8_ROT020_SHARP_MINIMAX_DISTANCE_TO_SHEAR_EQUIVARIANT_DTC_FILTER_001_20261024
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_METRIC_NATURALITY_FILTER_OPERATOR_HOST_001
evidence: EXACT_OPERATOR_NORM_MINIMAX / SOURCE_HELPER_DIRECT_EXEC / CLEAN_REPRODUCTION_PASS
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
exposure: PUBLIC
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 ROT020 — sharp optimal full-band distance from source E_lin to universal fixed shear-equivariant convolution

## Currentness, authorship and host
Currentness via IW Slack #iw-dispatch, 2026-10-24. INT8 ROT018 (prime) and ROT019 (all odd N, including DTC composites N33,35,39) already classify fixed componentwise scalar convolutions commuting with all determinant-one lattice shears: spatial kernels are constant on gcd-coordinate ideal orbits, dual Fourier multipliers likewise constant on gcd-frequency orbits. ROT019 also proved sharp finite locality threshold. NEW question is optimal L2 operator-norm approximation of the original E_lin by ANY such universal fixed-kernel convolution, INCLUDING nonlocal ones. This is a mature finite Fourier group-commutant/Chebyshev minimax specialization, NO novelty.

XH-S4 ROT020–024 owns metric York geometry and E-filter naturality concerns; M13 ROT023–028 owns historic pure-trace DTC source-family K_A and masks; Geeky-S11 owns TT rigidity/smooth leakage; PRF11 R24–25 owns commutator/stencil Sobolev errors. Our result neither replaces nor advances their physical-status claims.

## Exact operator setup
N>=5 any ODD number, including COMPOSITE N. G=(Z/NZ)^3; full periodic Hilbert space of symmetric covariant tensor arrays with normalized Frobenius L2 (NO interior mask). Original retained source helper deepseek_python_20260627_a87249.py SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801 defines
E_alpha = I + alpha sum_{j=1}^3 (tau_ej + tau_-ej - 2I),
whose exact Fourier multiplier is e(k)=1-4alpha sum_j sin^2(pi k_j/N).
C_N = all REAL componentwise SCALAR translation-invariant convolutions T_c commuting with U_A H(x)=A^T H(Ax) A for EVERY integer A in SL(3,Z), WITHOUT changing the kernel with A.

## Theorem — sharp attained L2 operator distance
For any real alpha,
  inf_{T in C_N} ||E_alpha-T||_(full L2->L2)
    = 2 |alpha| [3 cos^2(pi/(2N)) - sin^2(pi/N)].    (*)

Proof: Let m=(N-1)/2. Frequencies k_low=(1,0,0) and k_high=(m,m,m) have the SAME primitive gcd orbit because gcd(m,N)=1 for odd N. The source multipliers there are
  e_low=1-4alpha sin^2(pi/N),
  e_high=1-12alpha cos^2(pi/(2N)).
These are extrema over all NONZERO Fourier frequencies (order reversed for alpha<0). Every T in C_N has the SAME scalar multiplier t at k_low and k_high, so max(|e_low-t|,|e_high-t|) >= |e_low-e_high|/2, and Fourier Parseval identifies this with a lower bound on the full L2 operator norm. For the converse: on EACH gcd-frequency orbit choose its independent multiplier t_star as the midpoint of the minimum and maximum source e(k) on that orbit; set t_star(0)=e(0)=1. This is a real even orbit-invariant multiplier, hence inverse-FFT a real convolution in C_N. Each orbit error is half its own range, and the primitive orbit includes BOTH global nonzero extrema, so its half-range is the largest. The lower bound is ATTAINED, proving (*), even with arbitrary nonlocal gcd-subgroup filters. For fixed alpha and Nodd->infinity the exact distance tends to 6|alpha|.

Extra exact calibration cost: if T is constrained to reproduce E_alpha on ONE low fundamental frequency k_low, its primitive orbit multiplier must equal e_low; hence the attainable minimum operator distance DOUBLES to
  4 |alpha| [3cos^2(pi/(2N))-sin^2(pi/N)].
This does NOT claim simultaneous exact matching of ALL low Fourier modes is possible.

For alpha=.05 exact distances:
N31 .29820689557141; N33 .29841722324910; N35 .29859262352922;
N37 .29874041879876; N39 .29886610935203; N41 .29897389136658.
Limit .30000000000000. With N31 low-mode calibration lower limit .59641379114282.

## Executed independently, source native check and qualified interpretation
Stand-alone NumPy verification independently builds all gcd orbit minima/maxima and attainer t_star for N=7,9,15,31,33,35,37,39,41; checks that all 9 reconstructed full spectral operator norms equal (*) within 6e-15 and attainer is constant under integer elementary shears. It then SHA256-verifies and calls actual unmodified user helper apply_E on two genuine flat Fourier TT tensors with modes (1,0,0) and (m,m,m), at N31,33,35,39,41: recovered eigenvalues agree with exact source symbols and max Frobenius RMS residual <=4.3e-15. Important: those synthetic TT carriers probe E alone and are NOT the historic input h=fI.

Full local self-contained report SHA256 6568835757a176db71fb4eaa8078476b06033c63861e54bc481a107bd43fbbcf;
executed standalone Python SHA256 be8d9ddc3a1d74d6c4860dcbad5bb9af91d35467b451e1ab936af4e9f8a84e05;
numeric JSON SHA256 b0c759d3b52b4721865db4ca0e13400ecb627acf4ce24a1a66c800453adf561c.
ZIP checked CRC, SHA256 manifest 4/4 and TWO clean-directory runs (with and without source helper) PASS. Exact file is attached in Moderator INT8 session; GitHub publication of separate Python code is NOT claimed.

ESSENTIAL STOP: full-band L2 norm gap ~.3 is NOT 30% of DTC historical KA/KB or any physical observable. For FIXED Fourier bandwidth K, admissible identity approximation satisfies ||E_alpha-I||_(V_K->L2) <=12|alpha|sin^2(pi K/N)=O(K^2/N^2). Also, the universal SAME KERNEL requirement differs from the GEOMETRICALLY NATURAL FAMILY E_(phi*g) U_phi = U_phi E_g; the latter is NOT excluded. Nor do we claim anything for all tensor-coupled operators, curved geometry, Lorentzian Box, J3/K, covariance of full NASH, or the byte-unavailable historic production dtc0a_runtime_v0_3_1.py. Scientific owner, independent referee and BW ingestion are PENDING. No new task cascade.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.


## Source-custody correction (2026-10-24, INT8 ROT023)
Earlier report text transposed two adjacent hexadecimal characters at positions 33–34 (one-based) of the retained helper SHA256, writing `...f9dcb9...` instead of the independently rehashed actual `...f9cdb9...`. This is a provenance transcription error, **not** a changed script byte or a mathematical/numeric correction. The executable reproducer code used the correct digest where checked. The original commit/blob remains an immutable historical receipt; this correction creates a new version. Direct source path: `deepseek_python_20260627_a87249.py`.
