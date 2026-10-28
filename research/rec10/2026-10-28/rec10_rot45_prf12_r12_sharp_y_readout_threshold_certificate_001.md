---
artifact_id: IW_REC10_ROT45_PRF12_R12_Y_THRESHOLD_001_20261028
created_at: 2026-10-28
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_GLOBAL_LOCC_GAP
---

# REC10 ROT45 — independent PRF12 R12 referee, exact local YY crossover and high-q optimized tilt

**FIRST OWNERS:** PRF11 R35 original ideal Cauchy/Lévy three-probe SWAP, PRF12 R04 Helstrom and fixed X, PRF12 R08 adaptive X/Y, PRF12 R11 SEP9 frame, PRF12 R12 arbitrary-product-rank rigidity and exact 3-angle equatorial LOCC equation. REC10 ROT43/44 own earlier independent SEP9 and all-rank extension. NONBLIND science, mature Helstrom/implicit-function methods, no novelty.

**Fixed source:** ideal equal n=3, q=gamma*T/3>0, x=e^(-q), b=1-x², no memory aging/finite gate. Signed endpoint D_uv=[x^|sum(u-v)|-x^sum|u-v|]/8.

**NEW THEOREM 1: EXACT simple-YY crossover.** Alice Y, Bob Y, Charlie optimal conditional local single-qubit Helstrom. Fully achievable one-way LOCC score V_YY=b*[2+sqrt(16+x²)]/16. Original PRF R04 fixed three-local-X score V_X=b*(6+9x)/32 for x>=2/3; V_X=3b/8 for x<=2/3. For x<=2/3, V_YY>V_X for x>0. For x>2/3 difference sign equals 60−36x−77x². Unique positive zero x_c=(4sqrt(309)−18)/77. Therefore **V_YY>V_X IFF q>q_c=log[(18+4sqrt309)/60]=0.386549365097021**. This is a SHARP threshold for ONE explicit local strategy; neither all LOCC nor all local projectors.

**NEW THEOREM 2: asymptotically optimal Y-centered adaptive angle.** Alice Y, Bob conditional equatorial angle beta_s=pi/2−s theta, s=Alice outcome, Charlie conditional local Helstrom. For |theta|<=pi/2, c=cos theta, h=sin theta:
V_Y(theta)=b/16*[max(2c,sqrt((2h+xc)^2+(2+2c+xh)^2))+max(2c,sqrt((2h+xc)^2+(2−2c−xh)^2))].
Near x=0,theta=0 this reduces to b f/16, f=2cos(theta)+sqrt(8(1+cos(theta))+4x sin(theta)(1+2cos(theta))+x²). Exact f_theta(x,0)=6x/sqrt(16+x²)>0 and f_thetatheta(0,0)=−3. For x=0 the whole compact theta family has f(0,theta)=4cos(theta/2)+max(2cos theta,4|sin(theta/2)|)<6 for theta!=0, unique max at 0. By uniform convergence and implicit-function theorem global maximum in THIS ONE-PARAMETER family for x sufficiently small satisfies theta*(x)=x/2+O(x³). Exact expansion f(x,kx)=6+x²*(1/8+3k/2−3k²/2)+O(x⁴), maximum k=1/2. Hence max_theta V_Y=3b/8+b*x²/32+O(x⁴) for x->0. In particular the gain over fixed X is asymptotically b*x²/32, NOT positive constant; no unrestricted LOCC optimization.

**Independent execution:** 2400 direct 8x8 source-state partial-trace vs analytic formula max error1.6653345369377348e−16; 2000 sharp-threshold randomized tests; exact SymPy derivatives/Taylor, eight SciPy bounded local scans q=2..8, clean reproducibility PASS. Complete original Python + Polish report + JSON/log/README/SHA manifest Moderator-local ZIP IW_REC10_ROT45_PRF12_R12_SHARP_Y_READOUT_THRESHOLD_REFEREE_REPRO_20261028.zip SHA256 ec828714fb38c471731afa7302601f550aec55d0f2e2a189a5f7f0945559d4cb. ZIP CRC+SHA5/5+cleanroom JSON and stdout BYTE IDENTICAL PASS. This certificate does not claim source code remotely present. Do not import PRF12 R07's WITHDRAWN positive closure LOCC gap (R09/REC10 ROT42). No non-ideal device, physical interpretation, new mathematics priority, canon, BW ingest or EXEC. NO_NEW_TASK.
