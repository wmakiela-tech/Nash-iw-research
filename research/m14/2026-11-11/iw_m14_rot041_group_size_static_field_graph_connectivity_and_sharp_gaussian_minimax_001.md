# IW/NASH M14 ROT041 — group-size Gaussian minimax and connected co-time graph for a static vector field

artifact_id: IW_M14_ROT041_COMMON_DRIFT_GROUP_SIZE_GLOBAL_MINIMAX_AND_GRAPH_GATE_001_20261111
return_id: M14-ROT041-SHARP_PAIR_TRIPLE_QUAD_GROUP_GAUSSIAN_MINIMAX_AND_GRAPH_IDENTIFIABILITY_001_20261111
date: 2026-11-11
origin: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09 / M14
exposure: PUBLIC
ceiling: EXACT_CLASSICAL_FINITE_CALENDAR_STATIC_FIELD_GAUSSIAN_MINIMAX / NO_NOVELTY / NO_NATIVE_NV_REPLAY / NO_NASH_PHYSICS / NO_CANON / NO_EXEC_SIGN / BW_PENDING / REFEREE_PENDING

## Source first and scientific precedence

External source FIRST owned by XH-S5 ROT007: Florian Schall, Lukas Lindner, Yves Rottstaedt et al., "Laser-enhanced quantum sensing boosts sensitivity and dynamic range," Nature Communications 17 (2026), 10825, published 2026-10-22; https://doi.org/10.1038/s41467-026-78386-z . The reported 127 fT/sqrtHz is the author's photon-shot-noise sensitivity *limit*, NOT an achieved sensitivity including technical noise. Four NV orientations are discussed, but real native simultaneous grouping, common calibration drift, Gaussian centered branch estimates, equal readout costs, or static-field multi-session experiments have NOT been validated by that publication. No source-native sensor raw data replay. Mathematics wholly classical, source-typed and synthetic.

OWN PRIOR FIRST: M14 ROT031 tetrahedral axes/common-mode geometry; ROT034–038 temporal quotient/Chebyshev/regularity and conditional minimax; ROT039 exact four-axis common rejection with SAME physical timestamp; ROT040 FIRST finite co-time contrast rank and minimum number of session groups for polynomial vector fields, plus a SEPARATE sequential Lipschitz fixed-slot penalty. ROT041 addresses a new optimization: best possible information/risk when the hardware allows only r=2,3,4 axes to be read simultaneously and the field is CONSTANT across sessions. No claim of mathematical novelty or a new physical sensor capability.

## Frozen contract

Known tetrahedron a0=(1,1,1), a1=(1,-1,-1), a2=(-1,1,-1), a3=(-1,-1,1), with A^TA=4I3, A^T 1_4=0, ai·aj=-1 (i≠j), ||ai||²=3.

CONSTANT b(t)=z∈R3 across all sessions. Finite calendar t_k chosen *before observing data*, with at most r distinct axes S_k read at exactly the same physical timestamp per session, r∈{2,3,4}. One arbitrary common scalar nuisance h(t_k) per session, where h∈C∞ but has UNBOUNDED amplitude and derivatives. Its values at distinct finite times are freely independent: any such values interpolate a smooth polynomial h. Each unit-cost raw observation Y_{k,i,l}=ai·z+h(t_k)+ξ_{k,i,l}, independent ξ~Normal(0,sigma²), total number of observations N. The total number of replications in predeclared allowed sessions may be chosen adaptively based on earlier readings, but the theorem does NOT cover creation of arbitrary NEW timestamps after reading data. All possibly BIASED estimators allowed. Fractional resources are a continuous relaxation; exact integer attained at divisible budgets.

## R41.1 — EXACT effective Fisher and co-time graph gate

Let n_ki>0 be counts for i∈S_k, n_k=sum_i n_ki. Profiling each arbitrary h_k from the COMPLETE raw Gaussian design gives:

I_z = sigma^-2 sum_k [ sum_i n_ki ai ai^T - (sum_i n_ki ai)(sum_j n_kj aj)^T / n_k ]
    = sigma^-2 sum_k sum_{i<j in S_k} (n_ki*n_kj/n_k) (ai-aj)(ai-aj)^T.

The union co-time graph G has four axis vertices and connects i,j when they are observed at the SAME timestamp. Then I_z is full rank iff G is connected: v^T I_z v is a positive sum of ((ai-aj)·v)^2; v→(ai·v)_i identifies R3 with the four-component zero-sum space, so a kernel exists exactly when the graph is disconnected. Any distinct disconnected-component constants can be offset with legal h_k values and interpolated by one smooth common h; z aliases can have arbitrary magnitude and global minimax risk is infinite. All 2^6=64 simple 4-vertex graphs exact checked: 38 connected rank3, 26 disconnected rank<3. A connected spanning tree identifies z, but need not be an optimal statistical design. Four axes measured ONLY at four different times, with one at each, produce no co-time edges and NO finite identification.

## R41.2 — GLOBAL SHARP TOTAL VECTOR Gaussian risk

Tetrahedron Gram identity yields ||sum_i n_ki ai||²=4 sum_i n_ki²-n_k², hence
sigma² tr I_k = 4*(n_k - sum_i n_ki²/n_k) <= 4*n_k*(1-1/|S_k|) <= 4*n_k*(r-1)/r.
Thus tr I_z <=4*N*(r-1)/(r*sigma²). The trace inverse inequality tr I_z^-1 >=9/tr I_z implies candidate total-vector MSE lower bound 9*r*sigma²/[4*(r-1)*N], and singular designs have infinite minimax risk.

**BIASED/ADAPTIVE MINIMAX LOWER, not merely a Cramer-Rao claim:** take independent proper Gaussian priors z~N(0,tau_z² I3), h_k~N(0,tau_h²) for any fixed finite calendar. They are legal: interpolate h_k at calendar times by a smooth polynomial. For each realized history of a nonanticipating replication-allocation policy the conditional posterior is Gaussian; its 3x3 precision Q equals tau_z^-2 I plus the raw Schur terms with denominator (n_k+sigma²/tau_h²). Every realized path obeys tr Q <=3/tau_z² + 4N(r-1)/(r*sigma²)+3N/tau_h² (at most N nonempty sessions for an integer N-shot budget). Consequently posterior MSE for ANY estimator >=tr Q^-1>=9/tr Q; let tau_z,tau_h→infinity. Hence this is a GLOBAL minimax lower bound over all predetermined finite session calendars, all group choices of at most r, all allocations including data-adaptive replications among such predeclared groups, and all biased estimators. Not a theorem for arbitrary new adaptive timestamps or nonconstant fields.

## R41.3 — Exact attainment with all r-subsets

Use all binom(4,r) equally distinct predeclared session groups of size exactly r, each a different time, and give each axis in each group n_ki=N/[r*binom(4,r)] independent samples. By tetrahedral symmetry the full-nuisance profiled FI is isotropic:
I_r*=4*(r-1)*N/(3*r*sigma²) I3.
Full-nuisance Gaussian GLS is unbiased uniformly over arbitrary h(t_k), achieves
Cov(z_hat)=3*r*sigma²/[4*(r-1)*N] I3;
therefore the exact global minimax is
**R_r*=9*r*sigma²/[4*(r-1)*N]**, in continuous exposure relaxation and at divisible integer budgets. Demonstrated explicit designs; no assertion that these exact session counts are NECESSARY to attain the same optimum.

| simultaneous axes max r | attaining sessions | sharp total risk | increase vs full 4 |
| --- | --- | --- | --- |
| 4 | 1 four-axis group | 3*sigma²/N | baseline |
| 3 | all four different 3-axis groups | 27*sigma²/(8N) | +12.5% |
| 2 | all six different pair groups | 9*sigma²/(2N) | +50% |

At N=240 sigma²=1 exact FI/cov:
r4: I=240 I3, Cov=I3/240, risk 1/80=.0125;
r3: I=(640/3)I3, Cov=(3/640)I3, risk 9/640=.0140625;
r2: I=160 I3, Cov=I3/160, risk 3/160=.01875.

NEGATIVE: only THREE connected pair sessions (N=240 divided equally among 6 raw axis-channel slots) are identifiable but less efficient: star edges (01,02,03) risk 9/320=.028125; path (01,12,23) risk 1/32=.03125; complete six-pair design 3/160=.01875. The minimal 3-session identification from ROT040 does not imply optimal variance. A counterfactual with pair observations from different timestamps treated as same-time would be invalid.

## Independent validation / errors caught

Moderator LOCAL ZIP includes original full Polish scientific report (~15K bytes), three scientific scripts, two JSON, README, dispatch and SHA256 manifest, not presumed uploaded to GitHub. SymPy/Fraction EXACT **257** checks incl all 64 graphs, pair identity and full raw Schur, r2/3/4 isotropic FI and strict tree controls. Independently written raw whole-design regression with a separate nuisance column per session (NumPy), mpmath **85 digits**, **5286** validations across **1758** randomized nonsingular designs and **390000** synthetic Monte Carlo trials. MC deviations from exact risks: r2 0.576%, r3 0.029%, r4 0.248%; these checks are NOT a proof of global optimality. A material numerical bug was discovered and repaired: float64 matrix inversion can spuriously return finite inverse for effectively singular co-time graph, so a singular-value rank gate precedes inversion. Pure stdlib exact Fraction source also provided.

Local ZIP name IW_M14_ROT041_GROUP_SIZE_TETRAHEDRAL_GAUSSIAN_MINIMAX_FULL_REPRO_001_20261111.zip, size 18,785 bytes, SHA256 **d6c83f3368d065edbf6e0ef64ee6f37c993a8d8ffb087690401a26cc6466970a**. ZIP CRC PASS, payload SHA256 8/8 PASS; two independently clean extracted JSON reruns BYTE IDENTICAL, public stdlib source clean replay PASS.

STRICT STOP: no original time-resolved NV center/branch data, measured h law, native optical Poisson statistics, true hardware simultaneous groups, unequal per-axis costs, sensor sigma/gamma/fT, nonconstant field, arbitrary adaptively selected new timestamps, novelty, NASH J3K GR/GW/PBH physical claim, independently returned REC11/AUD1 verdict, BW ingest or LT canon. NO_NOVELTY / NO_NASH_PHYSICS / NO_CANON / NO_EXEC_SIGN / BW_PENDING / REFEREE_PENDING / NO_NEW_TASK_CASCADE. POSTED != ACK.