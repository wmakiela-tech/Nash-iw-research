# M14 ROT020 — absolute cross-preparation triplet calibration gives a 2-tail-tone field-sign test
artifact_id: IW_M14_ROT020_SHARED_ABSOLUTE_TRIPLET_WEIGHTS_TWO_TAIL_TONE_001_20261029
date: 2026-10-29
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09 / M14
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST / REFEREE_PENDING
claim_ceiling: EXACT_CLASSICAL_CONDITIONAL_SOURCE_CLASS / NO_NOVELTY / NO_SOURCE_DEVICE_REPLAY / NO_PHYSICAL_NASH / NO_CANON / NO_EXEC_SIGN
return_id: M14-ROT020-XH5-LT7-ABSOLUTE_TRIPLET_AMPLITUDE_CALIBRATION_TWO_TAIL_TONE_001_20261029

SOURCE/PRIOR FIRST. XH-S5 ROT007 owns Schall et al Nature Communications 17 10825 (Oct22 2026), DOI 10.1038/s41467-026-78386-z, primary 14N overlapping triple-Lorentz source; Eq15 PSN LIMIT distinct from achieved technical noise. Primary does NOT authorize the hypothetical shared-absolute-weights preparation/signed-field intervention. M14 ROT019 FIRST exhibited exact positive 3- and 4-tone field aliases with independent free weights and per-preparation backgrounds. M14 ROT017-018 prior finite-shot and adaptive oracle results were for different frozen source classes. Classical Lorentz monotonicity, finite difference, Le Cam and Poisson variance math have no novelty.

FROZEN POSITIVE MODEL: for sign s=+/- and known offsets j*d, j=-1,0,1,
mu_s(x)=beta_s - sum_j w_j/((x-e-s*B-j*d)^2+v).
w_j>0 are UNKNOWN numerical values but are SHARED ABSOLUTELY, not just up to independent gains. beta_+,beta_- unknown separately but each CONSTANT across tones; ONE common e, |e|<=E, |B|<=Bmax, known v>0,d>=0. wtotal>=Wmin>0. Four tones from two preparations, xL<xR in the RIGHT TAIL with a=xL-E-Bmax-d>sqrt(v/3).

THEOREM 1 GLOBAL SIGN: Define D=[mu_-(xL)-mu_+(xL)]-[mu_-(xR)-mu_+(xR)]. Then sign(D)=sign(B), D=0 iff B=0, despite unknown e, weights and two different constant backgrounds. Exact proof: g_v(z)=2z/(z²+v)^2, h_v(z)=-g'_v(z)=2(3z²-v)/(z²+v)^3. Backgrounds cancel, and
D=integral_(e-B)^(e+B) integral_(xL)^(xR) sum_j w_j h_v(x-t-j*d) dx dt.
All integrands strictly positive in source domain; orientation determines sign.

THEOREM 2 DETERMINISTIC CALIBRATION MARGIN: h_v is unimodal for positive z, derivative h'_v(z)=24z(v-z²)/(z²+v)^4. Put b=xR+E+Bmax+d; hmin=min(h_v(a),h_v(b))>0. Then |D|>=2*|B|*(xR-xL)*Wmin*hmin=:L*|B|. Per-channel expected-mean error <=eta adds <=4eta to D. If actual w_s,j=w_j+eps_s,j, source mismatch adds <= (||eps_-||1+||eps_+||1)/v. Thus sign reliable when L|B|>4eta+(||eps_-||1+||eps_+||1)/v. Unknown independent gains are NOT a legal error in this theorem.

THEOREM 3 FINITE SHOTS AND SHARP EXPONENT: Four independent Poisson channels, n unit-exposure repeats each, beta_s<=betamax, all means positive. Contrast estimator has Var<=4betamax/n. Chebyshev threshold L*Bmin/2 for B=0 vs B>=Bmin>0 gives EACH error <=16betamax/(n*L²*Bmin²), hence O(Bmin^-2) sufficient, uniformly within this restricted class. Lower bound: freeze one legal common-weight source; any single action tone/sign shifts mean by <=Wtotal|B|*sup|K_v'|, where sup|K_v'|=9/(8sqrt(3)*v^(3/2)). If all means >=mmin, squared-root Poisson distance <=c B² with c=Wtotal²*(sup|K'|)²/(4mmin). Adaptive history-based action kernels cancel from Bhattacharyya recursion: BC_N>=exp(-N*c*B²/2); Bayes error >=[1-sqrt(1-exp(-N*c*B²))]/2. Thus Omega(Bmin^-2) necessary even for arbitrary fixed-unit-exposure adaptive actions on the frozen legal pair. Θ(Bmin^-2) is the source-class test RESOURCE EXPONENT, NOT a real physical shot estimate nor general all-parameter inverse theorem.

EXACT RATIONAL CASE: v=1/2,d=1/5,E=1/10,Bmax=1/20,xL=1,xR=2,w=(7/40,7/20,7/40),beta_-31/10,beta_+29/10. a=13/20,b=47/20; hmin=2056640000/13980103929, L=2879296000/13980103929≈.2059566949304. At e=0,B=1/20, D EXACT 3682854498032917036928/74034073127208391069455≈.0497453988747, certified margin L|B|≈.0102978347465. For a conservative <=10% Chebyshev error per class, n>=4677242 repeats EACH of 4 tones; deliberately loose, not a laboratory prescription. For the frozen adaptive lower-bound example, mmin=3/2 and c=441/1600.

NEGATIVE CONTROLS: (A) Same SHAPE only (w normalized=(1/4,1/2,1/4)) but separately UNKNOWN positive gains and backgrounds: at H0 B=0 gains .7/.7 backgrounds 3.1/2.9; H1 B=.05, sign-minus gain≈.75631313358 beta≈3.10527042772 and sign-plus gain≈.64746522323 beta≈2.89493739041, exact equality of all FOUR Poisson means at tones 1,2 with strictly positive signals globally. This is a real algebraic open alias, not shot noise; exact Fraction in frozen JSON. (B) xL=0,xR=1 inside line group yields D<0 for B>0, so tail requirement must be retained. Do not identify full B/e/weights from the four signals.

REPRO/CUSTODY: stdlib Fraction exact code performs 105 grid sign/threshold controls, the exact contrast and positive independent-gain alias, adaptive c=441/1600. Independent NumPy/SciPy directly integrates the g-derivative, verifies 1400 random legal spectra + 500 bounded calibration discrepancies and 30000 synthetic Poisson trials, with variance crosscheck. Full Polish report + two original code + two JSON + dispatch+README+manifest, Moderator-local ZIP IW_M14_ROT020_SHARED_TRIPLET_CALIBRATION_TWO_TAIL_TONES_FULL_REPRO_001_20261029.zip SHA256 1aa73d5da1c9bb7c62362bee44df28b8d86322ab60b9ce1fadd66b6fd569f46c, CRC PASS, SHA 7/7 PASS, isolated clean re-exec both JSON BYTE_IDENTICAL PASS. Full ZIP not claimed to be on GitHub.

SOURCE STOP: no Schall data download, no legal hardware signed-prep or amplitude-sharing calibration demonstrated, no real technical-noise PSD or fT result, no NASH J3/K physics, no mathematical novelty, no LT adoption/ BW ingestion/ referee authority. NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE.