# M14 ROT009 — Log-concave extended sources retain three-distance Yukawa identifiability
artifact_id: IW_M14_ROT009_LOGCONCAVE_YUKAWA_GLOBAL_INVERSE_001_20261026
exposure: PUBLIC
claim_ceiling: EXACT_CLASSICAL_SYNTHETIC_SOURCE_TYPED / NO_NOVELTY / NO_PHYSICS / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
origin: M14 / IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09
return_id: M14-ROT009-XH5-LT-LOGCONCAVE_YUKAWA_ALL_WIDTH_GLOBAL_INVERSE_001_20261026

OTHERS FIRST: XH-S4 ROT028 first owns real Oct2026 7.6mg wafer source and point-Yukawa toy; M14 ROT006 first proves three-distance point-source injection; ROT007 first known two-slab positive-fold counterexample; ROT008 first bounded-width sufficient uniqueness condition and connected smooth folded counterexample (local archive; external write was blocked). LT6 REV024 now complete native+private GitHub readback PASS, status WORKING. Mature log-concavity/IFR host Bagnoli–Bergstrom 2005 DOI 10.1007/s00199-004-0514-4. Zou 2026 DOI 10.1007/s40505-026-00322-7 corrects a DIFFERENT composition theorem, not used here. No mathematical novelty.

SOURCE: Known D>=0 with log-concave density on convex (possibly UNBOUNDED) support; 0<r1<r2<r3; H(r,nu)=E[(1+nu(r+D))*exp(-nu(r+D))], nu=1/lambda>0. Three exact y_i=A+B*H(r_i,nu), A>0, B=A*alpha!=0 shared. This is a 1D shifted-point source average, NOT true finite-wafer 3D force or measured data.

THEOREM: Phi(nu)=(H1-H2)/(H2-H3) STRICTLY increases for EVERY nu>0 without source-width restriction. Thus three ideal readings globally identify nu,A,B,alpha,lambda.

PROOF: Let S=E exp(-nu D), kappa=E[D exp(-nu D)]/S, V=Var_tilt(D), kappa'=-V. Since -partial_r h(r+D)=nu^2*(r+D)*exp(-nu(r+D)),
H(ri)-H(rj)=nu^2*S*integral_ri^rj (t+kappa)exp(-nu t)dt.
For normalized left/right independent interval samples TL in (r1,r2), TR in (r2,r3) weighted by (t+kappa)exp(-nu t):
(d/dnu)logPhi=E(TR-TL)-V*E[(TR-TL)/((TL+kappa)(TR+kappa))]
>=E(TR-TL)*(1-V/((r1+kappa)*(r2+kappa))).
Exponential tilting preserves log-concavity. A nonnegative log-concave random variable Y obeys VarY<=(EY)^2: its survival Q(t) is log-concave by Prekopa; Q(0)=1, Q(x+y)<=Q(x)Q(y); hence EY^2/2=int_0infty int_0infty Q(x+y) dxdy <=(EY)^2. Apply to tilted D to get V<=kappa^2<(r1+kappa)(r2+kappa). Derivative strictly positive. Classical proof.

GENERAL SUFFICIENT HOST: Every known D whose tilted moments satisfy V_nu<(r1+kappa_nu)*(r2+kappa_nu) for ALL nu works; logconcavity is an independent WIDTH-FREE sufficient criterion, not necessary. Inversion: solve Phi(nu)=dy12/dy23, then B=dy12/(H1-H2), A=y1-BH1, alpha=B/A. B=0 destroys nu-identification; unknown independent gains/geometry/sensor model NOT allowed. No noisy uniform stability claim.

EXECUTED: 5 source families, 9 nu each =45 matched analytic H to independent Simpson ratio/derivative and finite-difference, all PASS. Families Uniform[0,10], Uniform[4,20] exceed ROT008 width cutoff, Gamma shape 1,2,5 have unbounded support; all log-Phi derivatives positive. Old ROT007 separated two-slab not-logconcave control retains Phi(.3)<Phi(.2)<Phi(.6). The first exploratory Simpson-only strict CV<=1 check at nu=6 failed from quadrature precision (~9e-8 numerical overshoot); replaced with exact analytical tilted uniform moments and independent Simpson tolerance, clean rerun PASS. This is a measurement of numerical quadrature error, not contradiction.

FULL local Moderator package: IW_M14_ROT009_LOGCONCAVE_SOURCE_YUKAWA_COMPLETE_REPRO_001_20261026.zip, SHA256 8c3179d8c6a9affea6576759f663a0ce924a14e43a7db40ce7cfb248e4a884e8, ZIP CRC, SHA256 5/5, clean Python re-exec BYTE_IDENTICAL JSON PASS. Contains full Polish detailed proof, runnable code, byte-frozen ROT007 helper, JSON, README, manifest. GitHub note does not claim complete ZIP uploaded. LT6 REV024 author review optional, no manuscript update.

NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICS / NO_WAFER_FIT / NO_NASH_KJ3 / BW_INGEST_UNKNOWN / REFEREE_PENDING / NO_TASK_CASCADE.