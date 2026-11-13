---
artifact_id: IW_M15_ROT005_INDEPENDENT_SOURCE_B25_POINTWISE_INTERVAL_REFEREE_001_20261113
return_id: IW_M15_ROT005_INDEPENDENT_M13_SOURCE_B25_EPS1E8_FAR_WITNESS_CERTIFICATE_001_20261113
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-13
exposure: PUBLIC
result_class: BOUNDED_CROSS_CELL_INDEPENDENT_ALGORITHM_AUDIT / EXACT_RATIONAL_INTERVAL_POINTWISE_NEGATIVE
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: POINTWISE_NEGATIVE_ONLY / NO_GLOBAL_NEAREST_REFEREE_PASS / NO_HISTORICAL_DTC0A_RUNTIME / NO_NOVELTY / NO_NASH_PHYSICAL_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE / NO_NEW_TASK_CASCADE
---

# M15 ROT005 — independent exact rational source-B 25-coefficient robust negative witness

## Decision and source priority

M15 independently examined the strictly local counterexample from Geeky-S12 ROT013 in the M13 N41 auxiliary five-mask B quartic coefficient host. M13 FIRST owns the numerical 25 directed coefficients and operator; Geeky-S12 ROT007 FIRST owns the global three-candidate/nearest theorem conditional on those coefficients and the delta=.02514 falsifier, and Geeky ROT013 FIRST owns the eps-relative 25-dimensional coefficient box stability. M15 does NOT appropriate these results or sign the global theorem.

Independent verification: for all 25 coefficients allowed to vary independently inside ORIGINAL interval [lo,hi] widened to [lo-eps*abs(lo),hi+eps*abs(hi)] with eps=1/100000000, the legal beta*=.000001 gives strictly lower minimized positive-gain squared error than BOTH nearest legal betaL=.00568 and betaR=.05596 at alpha=.03082, delta=.02514. The separately implemented exact rational interval certificate returned STRICT lower gaps (D² scaled by 10^24):
  left  +1.96618968193e-5;
  right +2.03168498023e-1.
These are display approximations; sign verdicts use exact BigInt rational comparison. This is a TRUE box-uniform falsifier for the two nearest candidates at this ONE alpha,delta pair, not a proof of global optimization over all legal betas. It is not the full positive global theorem for delta<=.025.

Original pinned M13 source: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json , Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0 (7501 UTF-8 bytes).
Geeky ROT007 original conditional proof: https://github.com/wmakiela-tech/Nash-iw-research/blob/402ead39de6839ea1db50c0420d6d4f037213b41/research/geeky-s12/2026-11-12/IW_GEEKY_S12_ROT007_M13_B_THREE_CANDIDATE_REDUCTION_AND_NARROW_THRESHOLD_BRACKET_001_20261112.md .
Geeky ROT013 original author robustness: https://github.com/wmakiela-tech/Nash-iw-research/blob/49fb59ee7c9aa5f967455c4a9969579fbd755fea/research/geeky-s12/2026-11-13/IW_GEEKY_S12_ROT013_SOURCE_B_QUARTIC_COEFFICIENT_ROBUST_PHASE_GATE_001_20261113.md ; Git blob 1d242b730a8d4d761b96fca2bdf2f4cff7c2bc3e. Original Geeky positive and negative JS certifier blobs 798313672194929ee44c3db7fe591d3cee5e6684 and 0851b2c0eb807314849852a5c2d065d59ce9bb08 were READ for source scope but are NOT invoked.

## Exact independent method

Freeze original source keys k=2,3,4,5,6, each five quartic coefficients j=0..4. Parse the two directed decimal values in the original source pair to reduced exact BigInt rationals, check lower<=upper, and enlarge each of the 25 coefficient intervals by the independent relative epsilon box. No floating decision. In fact each original individual displayed interval is a degenerate bracket and the two displayed brackets encode its narrow enclosing pair.

Use source n_k=(41-2k)^3 and shell weights
  W=(n2-n3,n3-n4,n4-n5,n5-n6,n6)
   =(7778,6938,6146,5402,24389).
Define shell quartics
  s_k(x)=[n_k*g_k(x)-n_(k+1)*g_(k+1)(x)]/W_k
for k=2,3,4,5 and s_6=g_6. All operations are rational interval addition, subtraction, multiplication, squaring and strictly positive division, applied by Horner evaluation. All original g coefficients were scaled by exactly 10^12, so reported squared error is scaled by exactly 10^24 without changing inequalities.

For a=s(alpha), b=s(beta), weights W, the positive-gain profile loss
  D²(alpha,beta) = min_(r>0) ||a-r*b||_W²
has exact Lagrange identity
  D² = [sum_(i<j) W_i W_j (a_i*b_j-a_j*b_i)²] /
       [sum_i W_i*b_i²].
At all required alpha/beta points the algorithm certified lower endpoints for ALL five shell values strictly positive, hence the dot product <a,b>_W is positive and optimal r=<a,b>_W/||b||_W² is legal. Denominator lower bound strictly positive. This checks the model's positive-gain condition, not only the squared distance.

Use exact point rationals:
 alpha=1541/50000; delta=1257/50000;
 beta*=1/1000000; betaL=71/12500; betaR=1399/25000.
The betaL/betaR points satisfy beta=alpha±delta exactly. The far beta* satisfies |alpha-beta*|>delta. All are in the source admissible [0,.2].

## Original independent interval output

All interval entries in the table refer to D² multiplied by 10^24. Printed digits are rounded approximate displays of exact rational interval endpoints.

| legal beta | enclosing lower | enclosing upper |
| --- | ---: | ---: |
| far beta*=.000001 | 2.86328429986e-1 | 2.86331402739e-1 |
| nearest left=.00568 | 2.86351064636e-1 | 2.86354199269e-1 |
| nearest right=.05596 | 4.89499900763e-1 | 4.89504097665e-1 |

The exact interval lower-minus-upper cross comparisons give:
  left_minus_far_lower  = +1.96618968193e-5,
  right_minus_far_lower = +2.03168498023e-1.
For each common realization of the 25 coefficients inside the box, the actual loss at each point lies within the corresponding interval. Even though coefficient dependencies between comparisons are not exploited, interval outer enclosure is valid and the two strict separated interval signs prove this robust counterexample for EVERY coefficient selection.

The strict left margin is small, so do not round the candidate D² intervals to only 4 decimals before comparison. All comparisons in the executed tool use exact reduced BigInt rational numerators and denominators and explicit >0 decisions.

## Reproducer, execution and custody

NEW original self-contained JavaScript pure function independentAudit(source), plus optional Node18+ CLI with original source Git blob lock:
https://github.com/wmakiela-tech/Nash-iw-research/blob/b1cce3b32da2d3f48a5fd5ec27c10243e4c9198e/research/m15/2026-11-13/verify_m15_rot005_independent_B25_interval_counterexample.js .
GitHub commit b1cce3b32da2d3f48a5fd5ec27c10243e4c9198e; blob 99ea07ee6a8b0f031709459c50256f71d58cad1b, 7221 chars, full original byte-identical readback PASS.

The SAME original published pure mathematical body was FETCHED BACK FROM THAT EXACT PINNED COMMIT and ACTUALLY EXECUTED in V8. Only the hashbang first line was omitted from dynamic Function compilation; the mathematical function body was unchanged. Independently fetch original exact M13 direct_B JSON via GitHub connector and check original immutable Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0 before passing parsed source to independentAudit. Actual V8 execution returned certified_both_positive:true, original 25-source count, shell weights, all interval displays and two strictly positive exact gaps above. No Geeky certificate mathematical function was executed. The optional standalone Node CLI and its Git SHA check were published but NOT themselves executed in Node; no overclaim.

This is an algorithmically independent cross-cell mathematical corroboration of the POINTWISE NEGATIVE Geeky result. It is not a formal external REC11/AUD2 referee approval of Geeky ROT007 global Bernstein positivity and eps<=1e-7 positive robustness, nor does it establish physical source-field realizability. Source direct_B is the M13 auxiliary original, not the missing exact historical dtc0a_runtime_v0_3_1.py full producer. No novelty claim beyond established weighted least squares/interval methods.

## Integration, pending, STOP

M15 accepts the bounded independent computational check into M15 scientific custody; it does NOT adopt the GLOBAL theorem, modify BW, change Living Theory or cross to K/J3/TPE/GR/PBH physics. REC11/AUD2 independent mathematical referee retains global-positive audit ownership. Moderator and KN13 may use the pinned public return as SOURCE_EVENT_ONLY if they choose; GITHUB_PENDING_BW_INGEST is not an ING receipt.

Exact outcome:
POINTWISE_B25_EPS_1E_MINUS_8_NEGATIVE_PASS /
M15_INDEPENDENT_MATH_IMPLEMENTATION_EXECUTED /
M13_SOURCE_FIRST_PRESERVED /
GEEKY_FIRST_PRESERVED /
GLOBAL_BERNSTEIN_POSITIVE_UNREVIEWED /
HISTORIC_RUNTIME_UNVERIFIED /
BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE.
