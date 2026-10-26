---
artifact_id: IW_MT14_ROT003_FINITE_EVENT_ORDER_EXACT_AGE_LABEL_TV_001_20261026
created_at: 2026-10-26
origin_cell: IW_MT_SUCCESSOR_13 / MT14
problem_id: PRF11_R35_FIXED_PROTOCOL_MAX_SWAP_CADENCE_VISIBILITY_NO_GO
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_FINITE_EVENT_ORDER_MATHEMATICAL_LIMIT / NUMERICAL_CHECK_PASS / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_DEVICE / NO_FINITE_N_QUANTUM_SOURCE_RERUN
---

# MT14 ROT003 — finite event-order exact binary TV in the rate-floor R35 labelled-Poisson limit

**Scientific class:** source-typed exact theorem for one specified limiting binary experiment; full finite-n quantum device, adaptive comb and physics upgrade NOT claimed.

## 1. Source-first attribution and prior-art subtraction

PRF11 R35 FIRST owns the exact unequal-time-grid fixed ideal-SWAP Cauchy-A versus independent-increments-B state (35.1) and approximation toward a commuting X reference as sum_j d_j^2 tends to zero: [PRF11 R35](https://github.com/wmakiela-tech/Nash-iw-research/blob/39979379d8fd9ac3a8f42009c01b5a3baf688f87/research/prf11/2026-10-25/IW_PRF11_R35_NONUNIFORM_SWAP_TIME_GRID_RECOVERS_IDEAL_MEMORY_WITH_CRITICAL_STORAGE_RATE_001_20261025.md).

NASH 2026-10-26 rate-floor source FIRST proves strict final-POVM deficiency E2 and the sharp **total-count-only** E3 envelope: [source](https://github.com/wmakiela-tech/Nash-iw-research/blob/73c71ceac7ec4a6a60f8b3a935b466b4a75d7cdc/research/nash-independent/2026-10-26/IW_NASH_ROTATION_20261026_RATE_CAP_STRICT_VISIBILITY_DEFICIT_001.md).

MT14 ROT001 FIRST identifies two-group-vs-total-count information threshold, and [MT14 ROT002](https://github.com/wmakiela-tech/Nash-iw-research/blob/d43a02ae18a4fe6189af3a1a82ce5732ea3facb6/research/mt14/2026-10-26/iw_mt14_rot002_full_late_age_label_threshold_001.md) FIRST derives the fine-late-age threshold and an exact formula restricted to beta<=beta_2. PRF11 R34 and MT13 ROT040 own distinct equal-grid age-marked studies. This return does not reassign their results.

Mature mathematical host: likelihood ratios of Poisson point patterns and Janossy densities, Neyman–Pearson positive-part TV, Poisson approximation. See L. Leskelä, *Information divergences and likelihood ratios of Poisson processes and point patterns*, IEEE TIT 70 (2024), 9084–9101, DOI 10.1109/TIT.2024.3472448, https://arxiv.org/abs/2404.00294. No external priority or novelty claim is made; source-level novelty subtraction remains incomplete.

## 2. Precisely declared limiting binary observation

Fix a>0, beta>0, 0<c<1; h_n=ceil(sqrt(n)); legal source increments d_j=c/n+(1-c)/h_n for j<=h_n and c/n otherwise. Terminal local X measurement records (i) whether ANY early click occurred and (ii) all *late* click indices. Its R35/ROT002 limiting point-process experiment, with t=1-x in (0,1], has:

- A: early clicks zero; late PPP intensity b(t)=g*t.
- B: independent early count Pois(H), H=a(1-c)/2; late PPP intensity s(t)=g*(t+q).
- g=beta*c/2, q=a/beta, L=int_0^1 b(t)dt=g/2=beta*c/4, p=exp(-a/2).

Under zero early clicks and k late positions t_i the exact likelihood B/A equals p*PRODUCT_i(1+q/t_i). A common invertible-in-record random within-cell jitter converts discrete late indices to continuous marks before invoking *total-variation* convergence; no false bare lattice-to-continuum TV convergence is claimed. True Cauchy-A to reference TV control is source R35 (35.6–35.7), not independently rerun here.

## 3. Exact finite event-order theorem

Define D=a/2 and w=log(1+q)>0. Put

  K_star = ceil(D/w)-1,

the largest integer k>=0 with k*w<D. Under A, late configurations of order k>K_star have likelihood B/A>=p*(1+q)^k>=1; therefore their Neyman–Pearson decision is ALWAYS B, whatever their age labels. For EVERY 1<=k<=K_star, both A-favouring and B-favouring age regions have positive measure: at all t_i=1 we have p*(1+q)^k<1, while letting one t_i approach zero drives B/A to infinity. Thus each and every order k<=K_star contains genuinely decision-relevant age variation, and ALL higher orders do not, for this known binary pair only.

Equivalently, order k becomes age-dependent exactly when

  beta > beta_k(a) := a/[exp(a/(2*k))-1].

The event-order thresholds beta_k strictly increase with k. At equality, k*w=D and the would-be age-dependent region has measure ZERO; the ceiling-minus-one convention is essential.

## 4. Exact finite sum for FULL age-labelled TV

The limit total-variation distance of the *entire* age-labelled binary experiment is

  V_age = exp(-L) * SUM_(k=0..K_star) [g^k/k!] * J_k(q,p),

where J_0=1-p and, for k>=1,

  J_k(q,p)=Integral_[0,1]^k [ PRODUCT_i(t_i) - p*PRODUCT_i(t_i+q) ]_+ dt_1...dt_k.

PROOF: on zero early clicks, A's k-event Janossy density is exp(-L)*g^k*PRODUCT(t_i)/k!; B's is exp(-L)*p*g^k*PRODUCT(t_i+q)/k!. TV equals the total positive part of the signed measure A−B, since it is a binary difference of probability measures (even when B also assigns singular mass to early-click events). All terms k>K_star vanish POINTWISE by the likelihood bound. **No infinite tail truncation is needed**. The identity is mathematical, not a claim that high-dimensional quadrature is computationally cheap for large beta.

Exact one-variable elimination: writing Aprod=PRODUCT_(i<k)t_i and Bprod=p*PRODUCT_(i<k)(t_i+q),

  Integral_0^1 [Aprod*t-Bprod*(t+q)]_+ dt
  = [Aprod-(1+q)*Bprod]^2/[2*(Aprod-Bprod)]

if Aprod>(1+q)*Bprod, and zero otherwise. This reduces J_k to a (k−1)-dimensional integral.

## 5. First two event-order branches and newly closed beta=4 point

Let d=1-p, v=p*q, delta=d-v, mu=v*(1+q).

- For beta<=beta_1: K_star=0 and V_age=exp(-L)*(1-p).
- For beta_1<beta<=beta_2: J_1=(d-v)^2/(2d) and V_age=exp(-L)*[(1-p)+g*J_1].
- For beta_2<beta<=beta_3: the previous formula acquires exp(-L)*g^2*J_2/2, with
  J_2=(1/2)*Integral_(mu/delta..1) [(delta*t-mu)^2/(d*t-v)] dt.
  The lower endpoint is strictly inside (0,1), as beta>beta_2. The integral has an elementary polynomial-plus-log primitive.

For a=1, c=0.5:
- beta_1=1.5414940825368, beta_2=3.5208116641878, beta_3=5.51388246309746.
- beta=2, K_star=1: V_age=0.310460540092645 (ROT002 independently reproduced).
- beta=4, K_star=2: baseline k0=0.238651218541191; k1 contribution=0.045077123404383; k2 contribution=0.000136343642026. Thus the previously unresolved **full** V_age = **0.283864685587599**. This is an exact formula with high-precision numerical evaluation, not certified interval arithmetic.
- beta=7, K_star=3: deterministic nested numerical quadrature gives V_age ~0.26536870346; its k3 contribution ~0.00023818484. This value is a numerical estimate, NOT a new exact closed elementary expression.

## 6. Executed controls, falsifiers, and negative knowledge

An independent source-free Python reproducer evaluates J1 and J2 at 55-digit mpmath precision, compares original 2D J2 integration with reduced 1D J2 through SciPy, and uses an independent reduced 2D SciPy integral for J3. beta=4 independent original J2 dblquad=0.0004495850764 (claimed quadrature tolerance ~3e-10); reduced 1D and high-precision J2=0.000449585325464666 (difference ~2.49e-10, inside declared tolerance). beta=7 reduced 2D J3 ~0.0006396742673. Beta sweeps across thresholds and boundary handling PASS.

A Moderator-local 5-file ZIP contains **full Polish source report, standalone Python, deterministic JSON, README, SHA256SUMS**. Zip CRC, 4/4 SHA manifest, fresh-directory rerun and BYTE-IDENTICAL regenerated JSON: PASS. This repo text report is the durable source body; executable code is not claimed published on GitHub.

FALSIFIERS: (i) find any k>K_star and positive-measure positions giving A-favouring likelihood; (ii) a legal threshold equality that requires an extra k event contribution; (iii) independent Janossy signed-mass integral violating the finite-sum identity. Numerical controls do not by themselves prove the analytic result, and all threshold claims remain conditional on source-model applicability.

## 7. Owner and scope boundaries

This is a **third consecutive** bounded study of the R35 limit. It resolves the open *full-age numerical value* left by ROT002, but MT14's broad scientific architect role should not become a serial Poisson prooflet executor. Without material new owner/referee input or a genuinely new mechanism/front, STOP further automatic same-family expansions. PRF source author retains model authority; REC/SW referee and BW currentness remain separate. E2 full terminal-POVM strict deficit remains intact. No physical hardware, no arbitrary process tester, no original finite-n quantum code, no novelty, no canon, no EXEC sign, no BW ingestion asserted.

STATUS: EXACT_SOURCE_TYPED_LIMIT_IDENTITY / SELF_CONTAINED_REPRO_PASS / OWNER_REVIEW_PENDING / REFEREE_PENDING / GITHUB_PENDING_BW_INGEST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
