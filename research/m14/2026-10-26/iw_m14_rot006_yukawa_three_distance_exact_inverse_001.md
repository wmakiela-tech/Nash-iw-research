# M14 ROT006 — 3-distance Yukawa exact inverse
artifact_id: IW_M14_ROT006_XH4_THREE_DISTANCE_YUKAWA_001_20261026
exposure: PUBLIC
claim_ceiling: EXACT_CLASSICAL_POINT_MODEL / NO_NOVELTY / NO_PHYSICS / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST / REFEREE_PENDING

XH-S4 ROT028 FIRST owns the October 2026 milligram-force sources and its 2-distance known-range point-mass gain-alpha toy: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s4/2026-10-26/IW_XH_S4_028_MILLIGRAM_FORCE_YUKAWA_IDENTIFIABILITY_20261026.md
The REAL measured source uses extended wafers, NOT point masses. M14 applies only the classical point-source force factor; no data reanalysis or physical claim.

Fix 0<r1<r2<r3, exactly known distances; y_i=A+B*h(r_i,nu), A>0, B=A*alpha !=0, nu=1/lambda>0, h(r,nu)=(1+nu*r)*exp(-nu*r). Then:
rho=(y1-y2)/(y2-y3)
=[int_r1^r2 t exp(-nu*t)dt]/[int_r2^r3 t exp(-nu*t)dt]=Phi(nu).
Because h_r=-nu^2*r*exp(-nu*r). Differentiate log Phi: (log Phi)'=mean_right(t)-mean_left(t)>0 since mean_left<r2<mean_right. Hence Phi is strictly increasing, nu globally UNIQUE, then B=(y1-y2)/(h1-h2), A=y1-B*h1, alpha=B/A, lambda=1/nu.

The range Phi((0,infinity))=((r2²-r1²)/(r3²-r2²),infinity); an invalid data ratio falsifies this model. With TWO distances there is a continuum of local (A,B,nu) fits; if B=0 then every y_i=A and lambda is NOT identifiable even with many distances. A fourth distance is a held-out test, not needed to fit all three parameters. Global injection does not imply uniform noisy stability when nu->0, nu->infinity or B->0.

Proof is classical exponential-weight monotonicity, NOT novel. Three distances apply only with one common gain, exact point geometry, correct normalized force, known coordinates and no extra background force; no claim for lab wafer geometry, E_g, K_A or J3/K.

See companion source-typed numeric controls and full Moderator-local standalone report. LT REV023 Chapters 2/7 may optionally incorporate the observation contract; no author uptake assumed. NO_EXEC_SIGN / NO_CANON / NO_NEW_TASK_CASCADE.
