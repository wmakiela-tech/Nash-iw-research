---
artifact_id: GEEKY-S11-ROT013-RAW-VS-MATCHED-TT-SOURCE-INTERFACE-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-25
status: SOURCE_HELPER_REPLAY_AND_NUMPY_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# ROT013 — source raw-wavevector TT versus matched-symbol TT: exact source-mode guard

OTHERS FIRST: Geeky-S11 ROT004–012 own matched-centered-symbol TT finite-grid classification; INT8 ROT012 owns mature TT principal-angle formula and INT8 ROT023/MT13 affine alias; PRF11 R25–R27 own raw-k source Lie commutator Sobolev discretization, distinct from isolated projector comparison. M13 owns h=fI masked K_A. No mathematical novelty claimed.

SOURCE-TYPED: unchanged retained helper `deepseek_python_20260627_a87249.py`, SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`, defines P_raw(0)F=F-tr(F)I/3 (rank5). Prior Geeky P_delta(0)=0 (rank0). Hence on full grid for every odd N and every s>=0, ||P_raw-P_delta||_(H^s -> L²)=1 EXACTLY, witnessed by constant traceless tensors. Original E_alpha(0)=1, so no scalar-alpha source filter can remove it. Conventions must be harmonized or inputs restricted to mean zero before comparing convergence.

At nonzero k, define n=k/|k|, d=delta(k)/|delta(k)| with delta_i=sin(2pi k_i/N)/h. Their symmetric rank2 TT polarization overlap singular values are (1+c²)/2 and c, c=|n.d|. Thus EXACT ||P_raw(k)-P_delta(k)||=sqrt(1-c²)=sin(theta); the raw-TT cross polarization [v otimes e_z+e_z otimes v]/sqrt2 at k=(m,j,0) saturates the leakage Q_delta P_raw.

LOW BAND fixed k=(1,2,0): sin(theta)=2(1-cos h)/(sqrt5 sqrt(1+4cos²h))=h²/5+O(h^4). HIGH BAND m=(N-1)/2, j=round(sqrt N/2): cos(theta)=2/sqrt N+o(N^-1/2), sin(theta)=1-2/N+o(N^-1). Source raw-TT tensor loses 93.1357589% L² norm at N31, 94.9321741% at N41, 99.6071203% at N511 when projected with matched P_delta. These are moving frequency witnesses, not fixed smooth fields. For E_alpha=.05, high-band retained multiplier tends .8.

EXACT SOBOLEV CONTRAST ON MEAN-ZERO INPUTS: ||P_raw-P_delta||_(H^s_0->L²) = max_(k ne 0) sin(theta(k))/(1+|k|²)^(s/2) = Theta(N^-min(s,2)), s>=0. Upper: angular discrepancy <=C min(1,|k|²/N²), using sine Taylor on low band and trivial bound on high band. Lower: k=(floor(N/8),floor(N/4),0) for 0<=s<=2; fixed k=(1,2,0) for s>=2. At s=0 stronger limit operator norm ->1. No physical or original masked h=fI inference.

INDEPENDENT EXECUTION: 70 typed rows, 14 explicit high-band wavevectors, six fixed low-band, four direct full real FFT genuine raw-TT witness comparisons, four raw-vs-matched zero-mode tests, 36 all-wavevector exact Sobolev multiplier censuses and six unchanged-helper source checks (including source k0). Maximum difference versus exact symbol/projection formula 4.121e-15; maximum independent original helper mismatch 2.316e-16. Local ZIP full 11.4k report, standalone code, 70-row JSON, README, exact unchanged helper; clean extraction CRC PASS, SHA256 5/5 PASS, identical JSON after fresh standalone execution. ZIP SHA256 `3a9ef3f237383767d0aad5297bc008047aa53667a6eea4d2cfa2bf4c1c3ff2b3`.

SOURCE CUSTODY: only helper replay, historical production runner byte unavailable. Distinct odd-N projector operators, NO original even-N raw-k validation repair, no curved York, J3/K, GR/GW, physical K_A, canon, EXEC, independent referee or BW ingest. NO_NEW_TASK.
