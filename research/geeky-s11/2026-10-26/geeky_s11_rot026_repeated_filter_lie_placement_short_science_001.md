---
artifact_id: GEEKY-S11-ROT026-HEAT-LIE-PLACEMENT-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-26
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# ROT026 — exact two-band TT heat-filter / Lie noncommutation

OWN PRIOR: ROT015-017 established real raw-k B=GA, ROT021-023 fixed smooth TT memory carriers, ROT024 one-filter alpha identification limit, ROT025 repeated stable source E before transport. ROT026 examines moving that repeated E AFTER one projected source-style Lie derivative. Standard host: operator splitting commutators (Auzinger-Herfort, Opuscula Math 2014 DOI 10.7494/OpMath.2014.34.2.243). No novelty claim. Preserved unchanged auxiliary helper SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801, NOT original missing historic production DTC.

Finite even N>=12 full unmasked real TT, h=2pi/N, C=(0,cos x,0), L=full three-term centered tensor Lie, correct orthogonal B, source scalar E_alpha=I+alpha*h²*Delta2, 0<=alpha<=1/6 (stable on entire N³). For p=2,3 fixed smooth true TT input H_p=T_p*cos(px+y), T_p=.3*(e_z e_z^T - v_p v_p^T/(p²+1)), v_p=(-1,p,0). Define Y_pre=B L E_alpha^m H_p and Y_post=E_alpha^m B L H_p, m>=1. B and E commute, but B L B and E generally DO NOT.

Write d_N=sin h/h, q_j=1-4alpha*(sin²(pi*j/N)+sin²(pi/N)), and exact rational sideband coefficients c_(2,+)=71/200, c_(2,-)=31/40, c_(3,+)=261/680, c_(3,-)=141/200. Source projection and Fourier orthogonality give the EXACT finite-grid result
||Y_post-Y_pre||/||H_p|| =
d_N * sqrt( c_(p,+)^2 * (q_(p+1)^m-q_p^m)^2 + c_(p,-)^2 * (q_(p-1)^m-q_p^m)^2 ).

For alpha>0 strictly nonzero; at alpha=0 EXACTLY ZERO (no uniform all-alpha claim). Effective diffusion time u_N=alpha_N*m_N/N² controls convergence for stable alpha_N. If u_N->u>0 finite, q_j^m -> exp[-4pi²u(j²+1)] and the difference has a STRICTLY POSITIVE limit. If u_N->0 it vanishes; if u_N->infinity it vanishes because all low modes are overattenuated, NOT because operators commute. Fixed alpha>0, m=o(N²) yields Theta(m/N²), whereas m=ceil(beta*N²) yields nonzero limit. For alpha=.05, beta=.02, p2 limit=.09551467585, p3=.12102117895; for alpha=1/6, limits=.21355308588 and .18661385337. C and H_p are FIXED SMOOTH fields across N, not moving Nyquist inputs.

OBSERVABILITY: initial-carrier scalar <H_p,(Y_post-Y_pre)>/||H_p||² is identically zero, yet the fields differ. Correct sideband TT probes S_(p,s)=U_(p,s)sin((p+s)x+y) give exact signed scalar
<S_(p,s),Y_post-Y_pre>/||S_(p,s)||² = -(d_N/2)*(q_(p+s)^m-q_p^m), s=+1,-1. Signs opposite for alpha>0.

Independent EXECUTED control: 1566 Fourier/matrix TT checks over 468 parameter sets, 216 direct original SHA-pinned helper real N³ checks incl both sideband readouts, 22 Python stdlib Fraction exact rational TT coefficients: 1804/1804 PASS. Full self-contained local user-conversation ZIP includes expanded Polish proof, 3 independent scripts, 3 JSON, frozen original helper, README, SHA manifest/stdout. ZIP SHA256 70726075a1d32ef408e1175c2788f3cdb74309cd06756ca159f51c013361720b. Clean extraction CRC, SHA256 12/12, all 3 scripts rerun and 3 JSON BYTE IDENTICAL PASS. These ZIP/code files are NOT claimed publicly uploaded to GitHub.

BOUNDARY: new mathematical preparation/placement protocol only; no historic masked pure-trace h=fI K_A reproduction, J3/K or physics, BW/readback ingest, referee, or EXEC. NO_NEW_TASK.
