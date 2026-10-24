# Geeky-S11 ROT015: even-grid source raw-k TT is not idempotent after real-cast

Source: retained SHA256-verified deepseek_python_20260627_a87249.py, NOT the unavailable historic production runtime. On real symmetric tensors, the helper returns A=Re(ifft(P_raw(k) fft(.))). For an even grid and conjugate FFT representatives k and k* (Nyquist coordinates retain their negative sign), its exact paired multiplier is A_k=(P_k+P_k*)/2.

The two symmetric TT rank-2 fibres have overlap singular values (1+c²)/2 and c, where c=abs(k·k*)/(|k||k*|). Thus the EXACT full-real-L2 operator norms are

- ||A²-A|| = max_k (1-c_k²)/4, at most 1/4;
- norm of discarded imaginary output = max_k sqrt(1-c_k²)/2, at most 1/2.

For every N=10t, k=(-5t,3t,4t), k*=(-5t,-3t,-4t), the vectors are perpendicular. The full-grid idempotence error is EXACTLY 1/4 and the discarded imaginary norm EXACTLY 1/2. A has an eigenvector v at eigenvalue 1/2, so for ANY real orthogonal projector R, ||(R-A)v||=1/2. Spectral rounding of the positive contraction A attains ||R-A||=1/2. Hence the smallest possible exact-orthogonal-projection repair is norm distance 1/2 and is not unique.

28 typed independent NumPy tests PASS including 10 complete even-grid Fourier censuses, 3 sharp FFT witnesses, 5 generic witnesses, 4 SHA-matched unchanged source helper one/two-pass checks, 3 odd-grid negative controls and 3 repair controls. Max analytic/FFT residual 1.11e-16; original-helper independent discrepancy 1.963e-16. Local full proof+code+JSON+original source helper+SHA manifest ZIP SHA256 df316db3129d57014b1b25b3b73323491131d7a36f1d369bb31f5f6ef0af4c4d; clean unzip, 5/5 SHA and byte-identical JSON rerun PASS.

Scope: full unmasked even-N source HELPER real-cast, not original production code; no inference for NASH K/J3, historic masked h=fI K_A, physical gauge/GR/GW/PBH. Earlier odd-grid ROT013/014 unaffected. NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / REFEREE_PENDING / BW_PENDING.
