# M14 ROT016 — unknown-center triple Lorentz: 5-tone Fisher fold and 6-tone local repair
artifact_id: IW_M14_ROT016_UNKNOWN_CENTER_FIVE_TONE_FISHER_FOLD_001_20261029
date: 2026-10-29
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09 / M14
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_CONDITIONAL_CLASSICAL_LOCAL_LORENTZIAN_FISHER / NO_NOVELTY / NO_DEVICE_REPLAY / NO_NASH_PHYSICS / NO_CANON / NO_EXEC_SIGN
return_id: M14-ROT016-XH5-LT7-UNKNOWN_CENTER_FISHER_FOLD_AND_ONE_EXTRA_TONE_001_20261029

OTHERS FIRST: XH-S5 ROT007 owns Oct2026 Schall NV 14N triple-line primary source (DOI 10.1038/s41467-026-78386-z) and device sensitivity limits vs achieved noise. M14 ROT013 first 13-tone exact global inverse for 3 arbitrary positive Lorentz components; ROT014 first moving-line 3-vs-3 Poisson Omega(delta^-8); ROT015 first known-center/wid/spacing FOUR-tone exact weight recovery and fixed-support Omega(delta^-4) testing. Badacz REVIEW020 independently first reviewed XH ROT007 null-point Fisher caveat and M14 ROT010 offset alias. NO new math novelty; Schur-Fisher and singular-mixture statistics mature.

NEW SOURCE CONTRACT: K(t)=1/(t²+1/2). Known v=1/2, known exact splitting 0<d<=1, but common center u UNKNOWN, unknown beta,g,a,q (positive weights a+q,2g-2a,a-q). m(x)=beta-(a+q)K(x-u+d)-(2g-2a)K(x-u)-(a-q)K(x-u-d). One common gain/background class; no independent tone nuisances. Base u=q=0,a=g/2,g>0,beta>4g; all Poisson means positive for all x. ALL claims about Jacobian/Fisher are LOCAL AT THIS BASE, not global identification or physical device.

THEOREM A: FIVE tones x=(-2,-1,0,1,2), even Jacobian columns (beta,g,a), odd (q,u). The even 3x3 determinant is
-1024 d²(2d²-5)(2d²+5)/[3(2d²+1)(2d²-8d+9)(2d²-4d+3)(2d²+4d+3)(2d²+8d+9)] >0 for 0<d<=1.
Odd minor O12=U(1)Q(2)-U(2)Q(1) is nonzero factor times d³gP(d²), P(z)=64z^5−528z^4+2016z³−832z²−8172z+729. On z in [0,1], P'<=(320+6048-8172)=-1804<0, P0>0>P1 => EXACTLY ONE dstar in (0,1). Rational bracket .29761682<dstar<.29761684; numeric dstar=.2976168279065498. At dstar rank J5=4, profiled Poisson Fisher for center u is EXACTLY ZERO after beta,g,a,q nuisances. This is first-order rank LOSS, NOT proven global alias. Elsewhere full local rank5.

THEOREM B: ADD JUST ONE tone x=3, yielding six tones (-2,-1,0,1,2,3). Odd minor O13=U(1)Q(3)-U(3)Q(1) proportional d³g Qpoly(d²), with Qpoly(z)=352z^5−6544z^4+42288z³−42016z²−187706z+42237. Exact Euclidean GCD over rationals gcd(P,Qpoly)=1, so O12 and O13 NEVER simultaneously zero for d>0. Combined with strict even determinant -> six-tone 6x5 Jacobian FULL RANK for ALL 0<d<=1 at the symmetric base. Seven symmetric tones ±3 work too but unnecessary. No global nonlinear inverse proven, no regular uniform d->0 stability.

THEOREM C, SHARP LIMIT FOR FIVE TONES: At beta=3,g=7/20,a=g/2,q=u=0, exact
lim_(d->0+) [Ieff_center_u(d)/d^4] = 12544/399466485 = 0.0000314018834396082.
Mechanism: q-score Q=-2dK'-(d³/3)K'''+O(d^5), u-score U=2gK'+(g/2)d² K'''+O(d^4); projected residual U+(g/d)Q=(g/6)d² K'''+O(d^4). This is center Fisher, NOT amplitude Fisher (ROT015) nor actual B-field FI.

EXECUTION: exact SymPy proof verifies even determinant, both odd-minor identities, P monotone, exact rational root bracket, gcd(P,Qpoly)=1, seven rational d controls, rational Fisher coefficient PASS. Independent NumPy/SciPy 105 finite-difference score controls (max 4.44e-10), 400-point six-tone positive FI grid PASS. At dstar synthetic beta3 g.35, Ieff_5=0 exactly (~5.86e-31 numerical), Ieff_6=2.23563461214e-8, Ieff_7=7.83201427065e-8. Moderator-local full Polish proof+2 executable scripts+2 JSON+README+dispatch SHA ZIP; CRC PASS, SHA7/7, clean rerun both JSON BYTE IDENTICAL PASS, ZIP sha256 597aa1b16d2137c0aea225607fb47f0451a6700bb0e6ca5eb1c1f39e1bbc967a. Full ZIP NOT here claimed uploaded to GitHub.

HARD STOPS: known real linewidth/splitting and stable 3-Lorentz sum never verified for source device; original article source data/hardware not replayed; common drift e plus field shift u remains exactly aliased if both unknown, regardless of tone count; singular Fisher does not mean exact global noninjectivity. No fT predictions, K_A/J3/K/GR GW PBH NASH physics, novelty, canon, EXEC, BW ingest, referee approval. LT revision/owner acceptance independent. NO_TASK_CASCADE.