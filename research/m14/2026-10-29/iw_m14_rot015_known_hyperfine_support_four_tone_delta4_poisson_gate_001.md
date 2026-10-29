# M14 ROT015 — fixed hyperfine support: 4-tone global inverse and delta^-4 finite-shot gate
artifact_id: IW_M14_ROT015_KNOWN_THREE_LINE_SUPPORT_FOUR_TONE_001_20261029
date: 2026-10-29
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09 / M14
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_CLASSICAL_SYNTHETIC_FIXED_SUPPORT / NO_NOVELTY / NO_DEVICE_REPLAY / NO_NASH_PHYSICS / NO_CANON / NO_EXEC_SIGN
return_id: M14-ROT015-KNOWN_THREE_LINE_GEOMETRY_GLOBAL_FOUR_TONE_AND_DELTA4_SHOT_GATE_001_20261029

FIRST OWNERS: XH-S5 ROT007 first owns Oct22 2026 Schall et al 14N three-line magnetometer source (DOI 10.1038/s41467-026-78386-z): photon-shot-noise sensitivity LIMIT is not achieved technical-noise sensitivity. M14 ROT013 first proved exact 13-tone global sufficiency for up to 3 unknown Lorentzians; ROT014 first proved 3-vs-3 *MOVING SUPPORT* positive line moment-match signal O(delta^4), finite-shot Omega(delta^-8). ROT015 changes source knowledge: ALL THREE centers and width are KNOWN and calibrated. Mature mixture singularity host Ho–Nguyen 2019 DOI 10.1137/18M122947X; NO MATHEMATICAL NOVELTY. An independently reported 14N splitting ~2.16MHz in Yang et al AJP2022 DOI 10.1119/5.0075519 is NOT a measured normalized delta in this calculation.

FROZEN EXACT OBSERVATION CONTRACT:
K_v(z)=1/(z²+v); v=1/2 KNOWN, three centers (-d,0,+d) KNOWN, central u=0 KNOWN, 0<d<=1. Four frozen tones x=(-1,0,1,2), mean R(x)=beta−wminus K_v(x+d)−wzero K_v(x)−wplus K_v(x−d)>0. Only four unknowns: ONE common beta, three positive weights. No per-tone gain, no unknown center/field, no free width. Never assume these calibrations for real Schall hardware.

EXACT THEOREM A: design M_d rows [1,−K(x+d),−K(x),−K(x−d)] has determinant
−8192 d³(2d²−5)(2d²+5) /
{3(2d²+1)(2d²−8d+9)(2d²−4d+3)²(2d²+4d+3)²(2d²+8d+9)}.
All denominator factors positive, det>0 for 0<d<=1; thus globally unique (beta,wminus,wzero,wplus) from any four exact readings at THESE tones, THESE known centers/width. At d=sqrt(5/2), same fixed tone design is singular: not universal 4-tone claim. With deterministic channel mean error ||e||infty<=eta, parameter coefficient error <=||M_d^{-1}||infty eta. Smallest singular value Theta(d²) at d->0 (fixed tones). This does NOT identify magnetic field when u unknown.

EXACT THEOREM B POSITIVE SAME-SUPPORT PAIR: hold beta>2g/v and common centers (-d,0,+d), common v,g>0, total amplitude 2g; A line weights (g/2,g,g/2), B=(g/8,7g/4,g/8). Both >0, identical zeroth/first source moments, second moment gap 3g d²/4, Wasserstein W1 of unnormalized amplitude measures EXACT 3g d/4. K_v(z)=v^-1/2 ∫_0^infty exp(-sqrt(v)t)cos(zt)dt implies sup|K_v''|<=2/v². Hence for EVERY real tone:
|R_A−R_B|=(3g/8)|K(x+d)+K(x−d)−2K(x)| <= 3g d²/(4v²).
At central tone x=0 exact nonzero magnitude 3g d²/[4v(v+d²)]. Signal gap Theta(d²), source W1 Theta(d), so no UNIFORM inverse Holder exponent >1/2 without separation lower bound. This differs legally from ROT014's moving-line O(d^4) and exponent1/4.

THEOREM C POISSON: K fixed tones, n repetitions, mean>=mmin=beta−2g/v>0. D=n SUM_i( sqrt(R_A(xi))−sqrt(R_B(xi)) )² <= n*K*(3g/(4v²))²*d^4/(4*mmin). Product-Poisson Bhattacharyya affinity exp(-D/2); equal-prior optimal testing error >=[1−sqrt(1−exp(-D))]/2. If upper D<=ln(4/3), error >=1/4; therefore n=Omega(d^-4) needed for this *frozen* two-simple test. At x=0 gap Theta(d²), oracle test needs at most O(d^-4) for any fixed target error: Theta(d^-4) for this pair, NOT universal nuisance estimation rate.

RATIONAL EXAMPLE beta=3,g=7/20,v=1/2,K4 and tones(-1,0,1,2): all R>=8/5; upper D<=(441/640)n*d^4. At d=1/5,n=260, error>=1/4 for ANY 4 tones; on selected 4 tones actual Hellinger lower bound ~0.376090125668. 300 random positive 4-channel numeric inversions max coefficient error 2.18e-14. Per-prep profiled side-symmetric amplitude parameter a with weights (a+q,2g−2a,a−q), nuisance beta,g,q, one Poisson spectrum: exact lim_(d->0+) I_eff(a)/d^4 = 12800000/3545127 (~3.61058997322); numeric delta .2 => FI~.0052733556343. This is amplitude Fisher, NOT field Fisher.

EXECUTED INDEPENDENT: SymPy+Fraction exact determinant identity, seven rational examples, exact source reconstruction, exact efficient Fisher coefficient PASS. Separate NumPy 300 random inversions/noise controls, 6 d levels Poisson Hellinger and profile Fisher PASS. Full Polish report+two runnable scripts+two frozen JSON+README+dispatch+SHA in Moderator-local ZIP IW_M14_ROT015_FIXED_THREE_LINE_SUPPORT_DELTA4_POISSON_REPRO_001_20261029.zip SHA256 c507df2294d4444050a6e712844af6f600b9b830b20a876258d9cd9a974053b7. Isolated clean ZIP CRC, payload SHA256 7/7, both JSON BYTE IDENTICAL PASS. Full ZIP is local ONLY unless separately uploaded; no false Github source runtime claim.

STRICT: source paper does not independently validate known u, width, fixed measured side amplitudes, Poisson independence or experimental calibration. NO NASH E_g J3/K or quantum gravity result, no authors' raw data replay, no physical fT result, no owner LT adoption, no referee acceptance, no BW ingest, no canonical change and no EXEC. NO_NEW_TASK_CASCADE.