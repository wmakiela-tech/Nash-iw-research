---
artifact_id: IW_REC11_ROT014_TARGET_RELATIVE_CM_GAUSSIAN_MINIMAX_AND_AXIS_SELECTION_REFEREE_001_20261111
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
created_at: 2026-11-11
source_type: M14_ROT038_HYPOTHETICAL_GAUSSIAN_POLYNOMIAL_FIELD_CM_SMOOTH_ORIENTATION_DRIFT
result_class: PASS_EXACT_ALL_SCALAR_TARGETS / PASS_3_VS_4_TARGET_SPECIFIC_GAP / NO_REAL_NV_TRANSFER
exposure: PUBLIC
claim_ceiling: NO_NOVELTY / NO_PHYSICAL_NV / NO_CANON / NO_EXEC_SIGN
bw: UNVERIFIED
---

# REC11 ROT014 — Exact global scalar-target minimax with smooth calibration drift

## Precedence and scientific question

External source priority remains Schall et al., Nature Communications 17 (2026) 10825, as located by XH-S5 ROT007; no published source supports the present synthetic signed-center, Gaussian, polynomial-time, bounded calibration model. M14 ROT037 first obtained full-vector global adaptive Gaussian minimax with polynomial nuisance; **M14 ROT038 first** proved full-vector sharp risk with a C^m derivative-bound H. AUD1 ROT036 first independently developed scalar **H=0** results for selected w and wrong-axis-pair controls. REC11 does not reassign these priorities. This new bounded theorem determines the globally optimal risk for **every** scalar linear target w·z, including H>0, under the *same frozen* M14 model and the precise 3-vs-4 tetrahedral axis selection.

Original M14 note: https://github.com/wmakiela-tech/Nash-iw-research/blob/a644b9a30dd936f12dc289f4f271566dccaf4cc6/research/m14/2026-11-11/iw_m14_rot038_smooth_calibration_derivative_floor_global_minimax_001.md
AUD1 selected-scalar H=0 priority: https://github.com/wmakiela-tech/Nash-Priv/blob/1688a2339ccac02c9300d92c4cc5350c51d67388/audits/aud1/2026-11-11/IW_AUD1_ROT036_M14_ROT037_TARGET_RELATIVE_SCALAR_GAUSSIAN_MINIMAX_AND_WRONG_AXIS_PAIR_001.md

## Exact source contract

For m=p+1>=1, time t∈[0,L], b(t)=z t^m+b_<m(t), where b_<m is an arbitrary vector polynomial of degree≤m−1. Four tetrahedral orientations are a1=(1,1,1),a2=(1,−1,−1),a3=(−1,1,−1),a4=(−1,−1,1). Available set I comprises either first three axes or all four. Independent orientation nuisances eta_i∈C^m have **only** |eta_i^(m)(t)|≤H; lower coefficients unbounded. Observations: Y_i(t)=a_i·b(t)+eta_i(t)+ independent N(0,sigma²), unit cost per elementary shot, N total. Any nonanticipating adaptive schedule and biased estimator permitted. Choice of 0 shots on an inactive arm is allowed. Target T=w·z. Define C_m=2^(2m−1)/L^m and epsilon=H/m!.

## New globally sharp source-typed theorem

Define the available-axis atomic norm:
nu_I(w)= min_{alpha: sum_i alpha_i a_i=w} sum_i |alpha_i|
       = max_{u: max_i |a_i·u|≤1} w·u.

Then, for the declared model,

**inf_{all adaptive designs and estimators} sup_{legal z,b_<m,eta} E[(T_hat−w·z)²] = nu_I(w)² [sigma² C_m²/N + epsilon²].**

For all FOUR axes, the eight signed points ±a_i are all eight vertices of cube [−1,1]³, so **nu_4(w)=||w||_infinity**. For only the first three axes A3, their coefficient representation is unique: **nu_3(w)=||A3^(−T)w||_1**, generally strictly larger. The full-vector 3-vs-4 MSE ratio 3/2 in M14 ROT037 **does not apply to arbitrary scalar targets**.

### Positive upper bound

Take Chebyshev–Lobatto nodes t_j=L(1−cos(jπ/m))/2, barycentric divided-difference weights lambda_j=1/prod_{k≠j}(t_j−t_k), for which sum|lambda_j|=C_m. Choose coefficients alpha minimizing nu_I(w), omit zero-coefficient axes, allocate continuous shots n_ij=N|alpha_i||lambda_j|/(nu_I(w) C_m). Estimate T_hat=sum_i alpha_i sum_j lambda_j Y_i(t_j).

Every lower-degree polynomial cancels. Generalized mean-value theorem gives rho_i=sum_j lambda_j eta_i(t_j)=eta_i^(m)(xi_i)/m!, hence |rho_i|≤epsilon. Worst deterministic scalar bias squared is epsilon² nu_I(w)², **attained** with eta_i(t)=epsilon sign(alpha_i) t^m. Independent Gaussian variance is EXACT sigma² C_m² nu_I(w)²/N by shot allocation. Thus the stated risk is attained in the continuous design model (and when the allocations are integers, in the discrete model).

### Matching global lower bound INCLUDING adaptivity and biased methods

Finite LP duality gives u with max_i|a_i·u|≤1 and w·u=nu_I(w). Let P_m(t)=T_m(2t/L−1)/C_m be the monic Chebyshev polynomial with |P_m|≤1/C_m, P_m−t^m degree≤m−1. Choose hidden s=±1 uniformly, independent scalar theta~N(0,tau²); define legal field and nuisances
b_(theta,s)(t)=(theta+s epsilon)u t^m;
eta_i(t)=theta (a_i·u)(P_m(t)−t^m)−s epsilon(a_i·u)t^m.

Since eta_i^(m)=−s H(a_i·u), all are legal. For ALL times and arms, the actual mean is theta (a_i·u)P_m(t), **independent of s**; the scalar target is (theta+s epsilon)nu_I(w). Even conditional on arbitrary adaptive measured times/arms, posterior theta precision is at most tau^(−2)+N/(sigma² C_m²), since |a_i·u|≤1 and |P_m(t)|≤1/C_m. The unobservable s independently contributes squared error epsilon²nu_I(w)². Let tau→infinity to obtain the matching lower bound nu_I(w)²[sigma² C_m²/N+epsilon²]. This proves globality rather than finite-grid numerical optimality.

This is classical Chebyshev extremality, LP/c-optimal design and an elementary two-world alias; no new fundamental mathematics claimed.

## Sharp axis-selection controls

- w=e1: with THREE or FOUR available tetrahedral axes, select only a1 and a2; nu=1, thus **two** correctly chosen arms attain the same globally minimal scalar risk.
- w=e1+e2: when FOUR axes available, alpha=(1/2,0,0,−1/2), nu4=1; with FIRST THREE only, unique alpha=(1,1/2,1/2), nu3=2. Thus **R3/R4=4** for this scalar target at fixed m,N,L,H,sigma, much larger than M14's full-vector ratio 3/2. The fourth axis materially helps one target while being redundant for another.
- w=(1,1,1): alpha=(1,0,0,0), nu4=1; a1 alone suffices.
- w=(1,1/2,1/5): nu4=1, nu3=13/10, hence ratio=169/100 at equal resource N, using respective optimally allocated arms.

For m=3,L=sigma²=1,H=3/5,N=144: C_m=32, epsilon=1/10; all three scalar targets e1,e1+e2,(1,1,1) with all four available have exact minimax risk **6409/900≈7.121111...**. For e1+e2 with only first three axes, exact risk **6409/225≈28.484444...**. These examples admit integer optimal allocations: for four axes e1+e2 use two arms (a1,a4), 72 shots each at four nodes in ratio 1:2:2:1; for first three use (72,36,36) total shots similarly. For any w, the 4-axis L1 optimum has at least one zero coefficient (take the median among d_i=(a_i·w)/4), so at most **three active arms** always suffice; particular targets need one or two.

## Executed independent source-typed validation

Independent Python 3 stdlib **Fraction** code (no M14 source code imported) executed:
- exact m=3 Chebyshev nodes/weights lambda=(-16/3,32/3,-32/3,16/3), moment cancellations, total abs weights C=32;
- seven full exact-integer resource/time/allocation/bias tests, including 3-vs-4 contrast and a generic target;
- **342 nonzero rational targets** w∈{−1,−2/3,−1/3,0,1/3,2/3,1}³, exact 4-axis L1=cube norm and 3-axis inequality;
- explicit paired-source all-time identity at six rational times, with legal derivative bound.
All PASS. Local complete self-contained six-member ZIP `IW_REC11_ROT014_TARGET_RELATIVE_CM_GAUSSIAN_MINIMAX_REPRO_001_20261111.zip`, SHA256 `134fafc9f17f0e56a8e6d56e76548fefd01827997604e0c1d788891d250840b8`; ZIP CRC PASS, five payload SHA256 PASS, CLEAN isolated reexecution JSON and stdout byte-identical PASS. Code SHA256 `a52baa604cbba3bf2276fd44a77c5b5a05264b7304fc3553ff519b527e0fbde0`; result JSON SHA256 `b63d956f083780eb0c722a71594fec7e514c73fa801e7a8e7f177669be9f8456`. The ZIP is LOCAL ONLY; not asserted to be hosted in GitHub.

## Scientifically binding guards

This theorem is conditional on **M14's** field polynomial degree≤m (same estimand across times), the exact listed tetrahedral axes, independent equal-cost Gaussian shot errors, and per-axis C^m drift with **only** |eta_i^(m)|≤H. It cannot be used as a physical NV sensitivity gain, nor for nonpolynomial real fields, correlated/Poisson/heteroscedastic measurement noise, actual Schall data, source-invalid signed branches, or other source geometry. Zero-shot arm omission or continuous-resource relaxation is part of the theorem; integer budgets may have rounding gaps except the demonstrated exact examples.

No owner adoption, BW source receipt, CANON, EXEC sign, physical J3/K/GW/GR/PBH or new mathematical novelty. This extends rather than refutes M14 ROT038's different vector-target statement. No automatic experimental task cascade.

RETURN_ID: IW_REC11_ROT014_TARGET_RELATIVE_CM_GAUSSIAN_MINIMAX_AND_AXIS_SELECTION_REFEREE_001_20261111
FINAL: PASS_EXACT_ALL_TARGETS_SCALAR_MINIMAX / PASS_TARGET_DEPENDENT_AXIS_GAP / HOLD_SENSOR_NATIVE_PHYSICS / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
