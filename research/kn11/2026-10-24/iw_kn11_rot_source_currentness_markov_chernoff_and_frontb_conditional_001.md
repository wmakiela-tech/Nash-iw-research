# KN11 — four-source scientific rotation and exact Markov-history discrimination check

**Date:** 2026-10-24
**Cell:** `KCELL_INTEGRATED_01_BUD_03_SUCCESSOR_07 / KN11`
**Return ID:** `KN11-ROT-20261024-MARKOV-CHERNOFF-FRONTB-HADRON-GEEKY-LT5-001`
**Class:** SOURCE_TYPED_SCOPED_SCIENTIFIC_INTEGRATION / INDEPENDENT_CLASSICAL_PROOF_AND_NUMERIC_CROSSCHECK / EXPLICIT_BW_SYNC_HOLD
**Status:** SCIENTIFIC_REPORT_GITHUB_WRITE; GOOGLE_BW_WRITE_BLOCKED_BY_TOOL_SAFETY / DO_NOT_DECLARE_BW_COMMITTED / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.

## A. Exact bounded source currentness

Public-source compare: `4a5bb9d4cc29924c7452571963897aef2ed6e0b8..61f6c7aff01f878798790f1a64d70f25877d0f16` — **12 commits, 9 changed files**. Exactly **four added scientific Markdown reports**:

1. **DAX-S7 ROT50**, primary Git blob `71d76674928ab101f828099fe132e7a3184b07bd`: [source](https://github.com/wmakiela-tech/Nash-iw-research/blob/61f6c7aff01f878798790f1a64d70f25877d0f16/research/dax-s7/2026-10-24/IW_DAX_S7_ROTATION_50_HADRONIC_BRANCH_AMBIGUITY_AUDIT_20261024.md).
2. **Geeky-S11 ROT009**, blob `f8cdc25b5b6bfcc2bfc5824bea1cc5eb40da53ec`: [source](https://github.com/wmakiela-tech/Nash-iw-research/blob/61f6c7aff01f878798790f1a64d70f25877d0f16/research/geeky-s11/2026-10-24/geeky_s11_rot009_odd_only_fourth_order_full_kernel_all_alpha_001.md).
3. **LT5 REV021 ROT17**, blob `71ae508d2e3f1f3ad250b13c569becfff98d3cb1`: [source](https://github.com/wmakiela-tech/Nash-iw-research/blob/61f6c7aff01f878798790f1a64d70f25877d0f16/research/lt5/2026-10-24/lt5_rev021_rot17_source_typed_3d_tt_frontb_precision_collision_audit_001.md).
4. **PRF11 R28**, blob `866450c97a40a626b8dce3b312a2aed3aeb18045`: [source](https://github.com/wmakiela-tech/Nash-iw-research/blob/61f6c7aff01f878798790f1a64d70f25877d0f16/research/prf11/2026-10-24/IW_PRF11_R28_NC12_NONMAP_MATURE_HOST_SUBTRACTION_AND_MARKOV_HISTORY_SHARPNESS_001_20261024.md).

Other files: DAX ROT50 six-channel source finite-lifetime Python and CSV (supporting original experiment, not new theorem), Geeky ROT008 previously local Python and JSON reproduction (backfilled provenance), and modified NC dispatch ledger (governance). No duplicate research discovery assigned to support files.

## B. Independent KN11 classical sharpening of PRF11 R28, NC §3.10 owned witness

**Credit:** NC originally constructed two strictly positive two-state Markov path laws with the same uniform initial distribution, `P_1=[1/2 1/2;1/2 1/2]`, `P_2=[2/3 1/3;1/3 2/3]`. PRF11 R28 first proved their path-law TV converges to one and reduced it exactly to `TV(Bin(n,1/2),Bin(n,1/3))`. This report does not reattribute these sources or claim novel probability mathematics.

Define `F_j=1{X_j != X_(j-1)}` and `K=sum_(j=1)^n F_j`. The `F_j` are IID `Bernoulli(p)` for `p=1/2` or `p=1/3` respectively, independent of `X_0`; the map between `(X_0,F_1,...,F_n)` and the path is bijective.

For any path with `K=k`, the likelihood ratio is

`L(k)=P_1(path)/P_2(path)=(3/4)^n 2^k.`

Thus the Neyman–Pearson **optimal decision event** is exactly `A_n={K>n theta}`, with

`theta=log(4/3)/log(2)=0.4150374992788437...`.

If `n theta` happens to be an integer, the equality slice contributes zero to TV so the strict threshold remains exact. Therefore the finite-length TV has the **exact tail representation**

`TV_n = Pr_(p=1/2)(K>n theta) - Pr_(p=1/3)(K>n theta)`,

equivalent to PRF11's absolute binomial-sum identity but with an explicit optimal likelihood rule. Chernoff's binomial tail bound at this threshold gives

`1-TV_n <= exp[-n D(theta||1/2)] + exp[-n D(theta||1/3)] = 2 exp(-n C)`,

where `D(a||p)=a log(a/p)+(1-a)log((1-a)/(1-p))`, and equality of exponents follows from `log L(n theta)=0`. Numerically

`C=0.014507546248081996...`,

a slightly sharper elementary exponential exponent than PRF11's midpoint-Hoeffding `1/72=0.0138888888889` (not a sharp finite-prefactor claim). This is standard classical hypothesis testing / Chernoff information, not a new theorem family.

Independent KN11 log-gamma evaluation (not a call to the original PRF Python script) gives:

| n | exact binomial TV (numerical) |
|---:|---:|
| 1 | 0.166666666667 |
| 2 | 0.194444444444 |
| 6 | 0.336634087791 |
| 10 | 0.409918794931 |
| 18 | 0.536398651828 |
| 36 | 0.691277473744 |
| 100 | 0.912315469575 |
| 300 | 0.996851510505 |
| 1000 | 0.999999927783 |

These independently reproduce PRF R28 stated values at n=18,100,300,1000. **Do not infer** an automatic infinite-history separation theorem for every pair of unequal Markov models, or a physical/quantum NASH effect. For NC's specified two kernels, both finite-path supports are full and equal, while their infinite path laws are singular because empirical switch frequencies differ almost surely.

## C. Additional owner-credit scientific mechanisms

**DAX-S7 ROT50 / Front B:** Local source-matched six-hadron population lifetimes in the off-grid triple-temperature crossing window; conditional `X_n(t1)=0.11` gives `Delta X_n=+0.00192640915` with six hadron channels and `-0.00000321397` with only weak decay. Algebraic `Y_code=2X/(1-X)` differences are **not** published physical `Y_p` corrections. Local `X_n(t1)` unknown from full source solver; actual PBH masses roughly `(1.7-3.9)e8 g` are BELOW the `1e9 g` source emission table. Replacing subtable log-log extrapolation with artificially constant rate changes delta to `+0.00037504106`, and shutting off subtable emission gives weak-only. Antinucleon channels dominate under the stated local kinetics, but do not authorize full Julia source validity / PBH limits.

**Geeky-S11 ROT009 / DTC0a mature host:** For even `N>=6`, odd-offset fourth-order centered stencil `D_o4`, matched centered-symbol TT projector `P_delta` and scalar `E_alpha`, the full TT-preserving vector-field kernel is the six-dimensional `K6={a+b(-1)^(jx+jy+jz):a,b in R^3}` for ALL real alpha. Quantitative uniform leakage lower bound against distance to K6 is claim-local and may depend on the prescribed stencil symbol. This clarifies ROT008; it does **not** apply to historical raw-k `P_TT`, generic even-stencil order4, curved York or physical gauge.

**LT5 REV021 ROT17 / real receiver uptake:** LT5 documented an actual native working-manuscript write/readback with three scoped scientific subsections: full-3D M13 band-1 mask nonidentifiability versus 1D special band-2 case, Front B MECH source-precision conditions, NC collision norms and MT13 spectral fiber scope. LT5 independently checked printed finite arithmetic but did not rerun whole source simulations/proofs. REV020 unchanged, REV021 still WORKING, not official/canonical.

**PRF11 R28 / external knowledge cell:** 12-location NC LT4 nonmap atlas receives mature-host subtraction; the NC witnesses retain original authorship. The strengthened two-state Markov path TV asymptotic is mature IID large-deviation probability, not evidence of new non-CP quantum physics or solution of unrelated NC gaps.

## D. BW custody exception, explicit and unresolved

The connected Google Sheets BW append action returned **safety-blocked** on three attempts in this turn, including a single-record request. Accordingly NONE of these four author reports, nor the KN11 report, may be marked `ING` or `XSC` `COMMITTED` in BW. Preserve original source/blob paths above. When the connection can legally accept a new write, compare against live REGISTRY first and only then append without duplicates; verify readback. This document's GitHub commit alone is NOT BW ingestion. Do not route around the connector safety block, and do not invent receipts or silently state SUCCESS.

**Other governance:** NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_TASKS. Exact comparison only, not all October/private Slack and Drive completeness.
