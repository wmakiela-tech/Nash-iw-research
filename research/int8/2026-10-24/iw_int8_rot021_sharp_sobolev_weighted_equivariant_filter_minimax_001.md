---
artifact_id: IW_INT8_ROT021_SHARP_SOBOLEV_WEIGHTED_EQUIVARIANT_FILTER_MINIMAX_001_20261024
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_METRIC_NATURALITY_FILTER_OPERATOR_HOST_001
exposure: PUBLIC
status: EXACT_THEOREM_AND_NUMPY_PLUS_LITERAL_HELPER_CHECK_PASS
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# INT8 ROT021 — exact attained Sobolev-weighted minimax and sharp rate

## Source-first scientific subtraction
INT8 ROT018–019: classified fixed-kernel componentwise scalar convolutions commuting with ALL integral SL(3,Z) shears, including composite N. ROT020: sharp NONVANISHING L2->L2 full-band optimum. Current Q: precise and attainable Sobolev-regularity-weighted minimum. PRF11 R24–25 concerned a DIFFERENT host: Lie/TT commutator DISCRETIZATION accuracy/aliasing, not source E-to-equivariant-filter approximation. Geeky-S11 owns TT leakage/rigidity; M13 owns source-family h=fI KA asymptotics/masks; XH-S4 owns geometric moving York and curved E-host. No novelty or physical upgrade claimed.

## Exact carrier
Odd N>=5, signed Fourier band B_N={-(N-1)/2,...,(N-1)/2}^3. Symmetric covariant tensor fields H on (Z/NZ)^3 with declared flat-coordinate Fourier norm
  ||H||_(H_N^s)^2 = sum_(k in B_N)(1+|k|^2)^s ||Hhat(k)||_F^2.
It is NOT shear-invariant geometric Sobolev norm. No physical mask or metric g.
Original retained source helper SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801: E_alpha=I+alpha h² Delta_centered, h=2pi/N; multiplier
  e(k)=1-4alpha sum_(i=1 to 3) sin²(pi k_i/N).
C_N = all REAL componentwise scalar translation-invariant convolutions with SAME fixed unchanged kernel commuting with every integer SL3(Z) tensor pullback A^T H(Ax) A. By ROT019, Fourier multipliers t(k) constant on each gcd-frequency orbit O_d={k:gcd(k1,k2,k3,N)=d}, d|N.

## Theorem 021.1: EXACT ATTAINED WEIGHTED MINIMAX for all real s>=0
Let rho_s(k)=(1+|k|²)^(s/2). Then
  R_(N,s,alpha):=inf_(T in C_N) ||E_alpha-T||_(H_N^s->L2)
    =max_(d|N) max_(k,l in O_d) |e(k)-e(l)|/[rho_s(k)+rho_s(l)].   (T1)
PROOF: For any orbit O_d, a candidate scalar multiplier t_d has error ≤R iff it belongs to every real interval [e(k)-R*rho_s(k), e(k)+R*rho_s(k)]. A finite family of real intervals has common intersection iff every pair intersects, equivalent exactly to the pair inequality in (T1). Choose t_d from the intersection separately on each orbit. It is real/even and produces a real shear-equivariant convolution, attaining the global minimum. Parseval gives the induced weighted operator norm as maximum of |e-t|/rho. QED.
For s=0 this reduces EXACTLY to ROT020:
  R_N,0=2|alpha|[3cos²(pi/(2N))-sin²(pi/N)] ->6|alpha|.

## Theorem 021.2: SHARP RATE across ALL odd N, composite included
For fixed alpha !=0 and any fixed s>0,
  R_N,s=Theta_(alpha,s)(N^(-min(s,2))).                                (T2)
UPPER: identity I is admissible and |sin u|<=|u| implies
  R<=4|alpha|pi²/N² max_k |k|²/(1+|k|²)^(s/2).
Since |k|<=sqrt(3)N/2, this is O(N^-s) for 0<s<2 and O(N^-2) for s>=2.
LOWER 0<s<=2: primitive gcd-frequency orbit contains k_low=(1,0,0), k_high=(m,m,m) m=(N-1)/2 and gcd(m,N)=1. By (T1),
 R>=4|alpha|[3cos²(pi/(2N))-sin²(pi/N)]/[2^(s/2)+(1+3m²)^(s/2)]=Omega(N^-s).
LOWER s>=2: SAME primitive orbit includes k1=(1,0,0), k2=(1,1,0); their e gap=4|alpha|sin²(pi/N), so
 R>=4|alpha|sin²(pi/N)/[2^(s/2)+3^(s/2)]=Omega(N^-2).
Combine, proving T2. This is NOT a claim original E commutes with every shear, and is NOT PRF11's s>1 Lie commutator threshold.

## Executed numeric exact-orbit minimax, alpha=.05
|N|s0|s0.5|s1|s2|s3|
|--:|--:|--:|--:|--:|--:|
|31|.298206895571|.095525379376|.023650434655|.001789468988|.000475496458|
|33|.298417223249|.092919328307|.022293961594|.001591997396|.000420182153|
|35|.298592623529|.091024346809|.021112607977|.001425910897|.000373959969|
|37|.298740418799|.088994115637|.020057535069|.001286656077|.000334946344|
|39|.298866109352|.086993977013|.019055640002|.001165227182|.000301720183|
|41|.298973891367|.085307150885|.018194326764|.001059891850|.000273193317|
|63|.299565076951|.071307610289|.012074603377|.000464926438|.000116284374|

Independent NUMERICAL verification: interval intersection bisection, constructed orbit-wise multiplier, direct weighted sup and active-pair equality ALL PASS on N=7,9,15,31,33,35,37,39,41,63 and s=0,.5,1,2,3 (50 cases). SECOND independent exhaustive pair enumeration for all mod pairs N7/9/15 × five s PASS (<3e-13, 15 cases). At N31 s0 active high mode (15,15,15); s3 active high (1,1,2): do NOT extrapolate only from Nyquist high mode.
Unmodified retained helper apply_E AND apply_P_TT literally executed on 3 genuinely TT Fourier tensors at each N=31,33,35,39,41, Fourier k=(1,0,0),(1,1,0),(m,m,m), alpha=.05. P_TT input mismatch <=1.1e-14 Frobenius RMS; E Fourier-symbol residual <=4.3e-15. These are synthetic source-carrier tests, NOT historical puretrace input.

## Repro/custody/STOP
Full separate local report, complete independent NumPy script, independent all-pair script, JSON rows, README and SHA256 manifest are attached in Moderator conversation as a single ZIP:
 iw_int8_rot021_sobolev_weighted_minimax_bundle.zip
ZIP SHA256 dbf4a4cc5cac484612ffa95be983b019a226aa0f8cde9685552981493719a91a.
Clean unzip/CRC PASS; manifest 5/5 PASS; independent execution in two CLEAN directories with source helper SKIPPED vs byte SHA-checked source helper PRESENT: theorem 50/50, brute 15/15, native source gate only when present PASS. GitHub code upload NOT claimed.
Historical original dtc0a_runtime_v0_3_1.py bytes still unavailable (declared SHA256 2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084). No historical KA, J3/K invariant, physical GR/NCDG or generalized tensor operator consequence.
Metric-natural covariant FAMILY E_(phi*g)U=U E_g is NOT excluded; this theorem only treats a SINGLE unchanged componentwise convolution. Owner, independent referee, BW and EXEC PENDING. NO_NEW_TASK / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
