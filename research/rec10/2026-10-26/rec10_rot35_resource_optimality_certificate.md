---
artifact_id: IW_REC10_ROT35_PRF11_R35_SHARP_MESH_AGE_TRADEOFF_REFEREE_20261026
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# REC10 ROT35: sharp nonuniform SWAP timing/resource referee (PRF11 R35)

DATE 2026-10-26. Source PRF11 R35, original report blob 3d8dda56a401c5fce1d1ab9f0f280c4127a6caf0. NONBLIND and SOURCE_TYPED.

For any strictly positive normalized SWAP durations d_j>0, sum d=1, set E=sum d_j^2 and A=(1/n)sum(j-1)d_j (the exact R35 normalized mesh and average stored age). The source R35 theorem: E->0 and A->0 imply fixed-controller terminal quantum Helstrom trace distance tends to ideal 2(1-exp(-gamma T/2)) when kappa_n T=beta/n. PRF11 retains full ownership.

NEW REC10 exact finite-size resource inequality: E*(n*A+1/2)>=4/9. Proof: embed f(x)=d_j on [j-1,j), so int f=1, int f^2=E, mu=int x f=nA+1/2. For any R>0, 1<=mu/R+sqrt(E*R/3) via 1<=x/R+(1-x/R)_+ and Cauchy-Schwarz. Set R=3mu to conclude sqrt(E mu)>=2/3. Sharp continuum extremizer triangular density f(x)=2(1-x/R)_+/R.

NEW exact finite-n optimum of F=E+A for n>=4: choose unique integer m with m(m-1)<4n<=m(m+1). On closed simplex d>=0, unique minimizer d_j=1/m+(m+1-2j)/(4n) for j<=m, zero otherwise. Proof: KKT stationarity 2d_j+(j-1)/n constant for positive entries; dual KKT for remaining; strict convexity ensures uniqueness. Exact infimum on STRICT partitions d>0 is
F_n*=1/m+(m-1)/(2n)-m(m^2-1)/(48n^2),
approached by positive d^(eta)=(1-eta)d*+eta/n. As n grows m~2 sqrt n, E~A~2/(3 sqrt n), F_n*=4/(3 sqrt n)+O(1/n). Strict positivity must NOT be conflated with exact boundary minimizer.

PRF11's original two-tier grid m=ceil(sqrt n), delta=n^-1/2 has F~2/sqrt n, or ratio 3/2 vs F_n*; source R35 asserts sufficiency, not minimum. n4096: source F=.030643523685515872, exact inf=.020711421966552734, positive eta=1/n schedule F=.020825982700131362. Necessary max ideal SWAP cadence 1/min Delta >= (n-1)/(2*T*A), since A>=d_min*(n-1)/2. None of these inequalities minimizes actual quantum Helstrom error or validates hardware.

Independently executed exact Fraction KKT on 9 n, 1000 random simplex trials, 54 independent full 2^n x 2^n source quantum rho_A/rho_B checks n2..7, max residual 4.44e-16. Clean locally extracted ZIP CRC+SHA and byte-identical standalone JSON/stdout regeneration PASS. Local Moderator bundle: IW_REC10_ROT35_PRF11_R35_SHARP_MESH_AGE_TRADEOFF_REPRO_20261026.zip, SHA256 03740e654e64f2ae3c57a269a3057202020290534d2ab71372483ce487349dd3. Complete Polish report and standalone code stored there. This GitHub certificate, if committed, is concise public derivation rather than exact-byte copy of local report.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_OWNER_ADOPTION / NO_NEW_TASK.
