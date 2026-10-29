---
artifact_id: IW_REC10_ROT50_PRF12_R18_IDEAL_AXIS_NONUNIFORM_001_20261029
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10
created_at: 2026-10-29
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# REC10 ROT50 — independent PRF12 R18 referee, ideal memory-and-axis countersequence

PRF12 R18 FIRST owns full active three-qubit source-A vs Lindblad source-B SWAP dynamics and a nonuniform frozen-xi sign-reversal countersequence with kappa=.3 and axis error=.02 (source Git blob e71c917b526a2b99426198a8c68192e8489ea118). PRF12 R17 FIRST owns B-Duhamel bound |pBactive−pBref|<=gamma*tau; PRF12 R16 owns randomized X/Y three-sign agreement. REC10 ROT49 prior sector operator E=3P/4+K/4. REC10 ROT50 NONBLIND independently strengthens the R18 counterexample to **zero memory aging kappa=0 and perfect orthogonal axes epsilon=0**.

Set gamma=Tfree=1, Delta=1/3, Hfree=xi*Zsensor/2 and each active Hj=(pi/(2tau))*SWAP_(sensor,Mj)+(xi/2)*Zsensor, j=1,2. Input |+++>; total physical clock=1+2tau. Take for ANY positive integer n: xi_n=6pi*n, tau_n=4/(6pi*n). Each free gate exp(-i xi_n Delta Z/2)=(-1)^n I, while each pulse has fixed xi_n*tau_n=4. Thus the conditional A final state is, up to scalar phase, psi*=exp(-i[(pi/2)SWAP2+2Zs])exp(-i[(pi/2)SWAP1+2Zs])|+++>, independent of n. The source observable E=(3/4)P+(1/4)K obeys pA=1/16+(3/4)(|<W|psi*>|²+|<Wbar|psi*>|²).

Exact solved pulse blocks: on |01>,|10> U=cos(Omega)I−i sin(Omega)[pi*sigmaX+4*sigmaZ]/sqrt(pi²+16), Omega=sqrt(pi²+16)/2; equal local pair bits contribute exp(-i(pi±4)/2). Independent mpmath.iv at 65 decimal digits gives outward pA in [0.4168697067694650051808867732316454383229552786783937059071186149238683,0.4168697067694650051808867732316454383229552786783937059071186149642245]. Ideal B reference pBref=(2+3exp(-2/3))/8=0.442531419637222010...; difference pBref−pA belongs to [0.02566171286775700489610813656582773994943452893187183721244992648090444,0.02566171286775700489610813656582773994943452893187183721244992652244755].

By PRF12 R17 Duhamel |pBactive−pBref|<=gamma*tau_n=4/(6pi*n). For ALL n>=9, pBactive−pA >= (pBref−pA)−4/(6pi*n) >=0.0020832027800688070...>0, certified using outward interval pi. Thus arbitrarily SHORT nonzero source-active SWAP durations are NOT uniformly reset-phase-robust EVEN with kappa=epsilon=0. One may round n≈4/(6pi*tau) with xi=6pi*n to obtain this also for ALL sufficiently short tau via pulse-area continuity; a Cauchy tail adversarial xi diverges. This does NOT overturn PRF12 R18's POSITIVE CAUCHY-AVERAGED contrast.

Independent NumPy+SciPy full A 8x8 expm vs separately coded exact interval pulse blocks: 10 n tests max A discrepancy1.55e-14. Full B 64x64 Lindblad expm (not static drawn pulse phase): n=9 pB=.436589633217, n=100 pB=.441987576495. The B source bound holds at all tested n. Original R18 noisy kappa=.3 eps=.02 n100 conditional pA=.377688705429, consistent with its limiting .377756095417. Original full R18 Cauchy 2000-bin table NOT independently reproduced.

Full Polish scientific report, independent executable Python, JSON/log, README and SHA256 manifest in Moderator-local ZIP IW_REC10_ROT50_PRF12_R18_IDEAL_RESOURCES_NONUNIFORM_COUNTERSEQUENCE_REPRO_20261029.zip SHA256 2515fa64c0bc548dc48f7a61cc5b4166f96c413f86c8deb1ce457e3f4139978e. CRC, five member SHA and fresh extracted byte-identical JSON/stdout PASS. This concise certificate does NOT claim uploading executable ZIP to GitHub. No physical device, measured Cauchy frequency, finite source-active hardware, global LOCC, BW ingestion, novelty, canon or EXEC. NO_NEW_TASK.
