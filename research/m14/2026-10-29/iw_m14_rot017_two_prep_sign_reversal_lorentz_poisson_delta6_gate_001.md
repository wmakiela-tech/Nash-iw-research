# M14 ROT017 — known three-line spacing, opposite field response, common drift: finite-shot delta^-6 barrier
artifact_id: IW_M14_ROT017_XH5_TWO_PREP_SIGN_REVERSAL_THREE_LINE_SHOT_GATE_001_20261029
date: 2026-10-29
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09 / M14
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_CLASSICAL_SYNTHETIC_LORENTZIAN_POISSON / NO_NOVELTY / NO_SOURCE_DEVICE_REPLAY / NO_NASH_PHYSICS / NO_CANON / NO_EXEC_SIGN
return_id: M14-ROT017-XH5-AUD1-LT-THREE_VS_THREE_SIGN_REVERSAL_DELTA6_SHOT_LIMIT_001_20261029

## Source ownership and model
XH-S5 ROT007 FIRST owns the Oct22 2026 Schall/Lindner/Rottstaedt NV 14N triple-hyperfine physical source, DOI 10.1038/s41467-026-78386-z. Authors' 127 fT/sqrtHz PSN sensitivity LIMIT is not actual measured technical-noise performance. M14 ROT010 FIRST hypothetical sign reversal; ROT013 13-tone exact global 3-Lorentz inverse; ROT014 moving unknown 3-vs-3 support Omega(d^-8) shot gate; ROT015 known-center/fixed-support amplitude Omega(d^-4) gate; ROT016 five-tone local Fisher zero at dstar and six-tone local repair for unknown center. Classical moments, Le Cam Hellinger and Fisher are mature prior math. NO NOVELTY.

FROZEN SOURCE-TYPED SYNTHETIC OBSERVATION: known d>0 and v>0, three Lorentz centers in each of two preparations u_s-d,u_s,u_s+d, u_s=e+s*B, s=+/-; common unknown drift e and unknown field B. Each preparation has its OWN three unknown positive weights and shared-per-triple beta_s>0 (no tone-specific gain). Independent Poisson count channels. Six frozen tones (-2,-1,0,1,2,3) in EACH preparation, total 12 per spectrum. Hypothetical sign reversal is NOT real-source experimental proof.

## Exact positive two-point witness
Fix beta3, g7/20, v1/2; all Poisson means >= beta-2g/v=8/5.
H0: e=0,B=0; both preparations 3 line atoms (-d,g/2),(0,g),(d,g/2).
H1: e=0,B=d/4:
plus centers (-3d/4,d/4,5d/4) weights g*(13/16,7/8,5/16);
minus centers (-5d/4,-d/4,3d/4) weights g*(5/16,7/8,13/16).
Weights are strictly positive, three centers distinct, each hypothesis uses the SAME d,v, each preparation obeys sign reversal with ONE common e. H0 and H1 differ in B by d/4, not an instrumental drift.

EXACT MOMENT FIBRE: Within EACH sign preparation moments about 0 match for orders k=0,1,2: M0=2g,M1=0,M2=g*d^2. Third moment difference H1-H0=sign*(9g/32)*d^3. Unnormalized source W1 distance exactly 3g*d/4 per preparation (1D CDF integration).

GLOBAL SIGNAL BOUND: K_v(t)=1/(t^2+v) has |K_v'''(t)|<=6/v^(5/2) via exponential Laplace cosine integral. Taylor to degree2 and matched moments show for ANY real tone x:
|mu_H1,s(x)-mu_H0,s(x)| <=(1007/512)*g*d^3/v^(5/2).
At x=1 for plus sign, the EXACT RATIONAL asymptotic limit [mu_H1,+ (1)-mu_H0,+ (1)]/d^3 -> -g/9, and minus sign has opposite sign. Thus the delta^3 signal order is sharp for this frozen pair, despite exact structural global identification for any fixed d.

FINITE-SHOT BARRIER: n independent repetitions, K tones PER sign (2K total), product-Poisson means n*mu_i, D=n*sum_i(sqrt(mu1_i)-sqrt(mu0_i))^2, Bhattacharyya affinity BC=exp(-D/2). Minimum equal-prior Bayes error obeys Pe* >= [1-sqrt(1-exp(-D))]/2. Since mu>=mmin and |sqrt(a)-sqrt(b)|^2<=|a-b|^2/(4*mmin):
D <= n*K*(1007/512)^2*g^2/(2*mmin*v^5)*d^6.
For frozen g7/20,beta3,v1/2,K6, this is the EXACT RATIONAL constant C=149065203/5242880 (~28.4319311). If n*C*d^6 <= ln(4/3), Pe*>=1/4. Examples d=.2,n<=158; d=.1,n<=10118; d=.05,n<=647569. Strongly conservative guaranteed numbers. For the fixed 12-tone design the EXACT small-d coefficient of D/(n*d^6) is 11515665443451841/18782029547400522240 (~0.00061312146349198), independently checked at high precision. One-tone x=1 achieves nonzero cubic gap; for KNOWN oracle pair n=O(d^-6) also suffices to fix testing error. Therefore Theta(d^-6) is SHARP for THIS two-simple-hypothesis decision, not for all unknown nuisance or actual sensor performance.

FISHER CROSSCHECK: Let kappa_s be nuisance-profiled single-preparation local center Fisher. The two score directions e and B after profiling independent per-prep beta,g,a,q have Fisher [[kappa_++kappa_-,kappa_+-kappa_-],[kappa_+-kappa_-,kappa_++kappa_-]], so profiling common e yields I_B=4kappa_+kappa_-/(kappa_++kappa_-) (zero when either kappa=0). For symmetric prep kappa_+=kappa_-=kappa, I_B=2kappa with TWO full preps. At ROT016 five-tone dstar=.29761682790655 kappa=0 in both, so sign reversal DOES NOT repair local Fisher singularity with independent nuisance weights. At SIX tones per prep exact ROT016 local rank repair applies for all 0<d<=1 at symmetric base: 12x10 Jacobian full rank. For dstar, synthetic I_B=4.47126922428e-8. This is NOT physical field sensitivity, finite-sample inverse stability or global identifiability.

EXECUTED TWO INDEPENDENT CONTROLS: Fraction+SymPy 12 signed exact source pairs, moments/W1, positive means, cubic x1 coefficient -g/9 and EXACT rational asymptotic full-Poisson coefficient PASS. Independent mpmath 70-digit 5 d values and NumPy/SciPy two-prep 12x10 Fisher at 5 d values PASS. Clean ZIP extraction ZIP CRC PASS, SHA256 7/7, both programs JSON BYTE_IDENTICAL PASS. LOCAL full Polish report, 2 scripts, 2 JSON, README, cross-cell dispatch, manifest in IW_M14_ROT017_SIGN_REVERSAL_POISSON_FULL_REPRO_001_20261029.zip SHA256 be40420af8356bcc04703dee115b92ce14b8e4517eddc0f08ce1bc263007cc69; ZIP itself not GitHub-hosted. First independent execution had numpy.int64 JSON serialization-only error; fixed by int conversion, rerun PASS.

SOURCE/CLAIM STOP: Original Schall source discusses sum of 3 overlapping 14N lines and uses PSN fit limits not attained technical noise. NO original source data/hardware fit, no verified independent sign-preparation switching, no actual normalized d or Poisson photodetection, unknown real calibration. NO NASH E_g/J3K physics, NO MATHEMATICAL NOVELTY, NO CANON, NO EXEC_SIGN, BW_INGEST_UNVERIFIED, LT OWNER REVIEW_PENDING, REC/AUD1 REFEREE_PENDING, NO_TASK_CASCADE.