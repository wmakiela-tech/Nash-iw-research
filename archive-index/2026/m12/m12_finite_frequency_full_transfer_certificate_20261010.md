# M12 — Finite-frequency to full-transfer certificate

RETURN_ID: M12-DRAFT009-FINITE-FREQUENCY-FULL-TRANSFER-CERTIFICATE-001

RESULT_CLASS: EXACT_HOST_THEOREM / INVARIANCE_RESOLUTION GATE / NO NOVELTY CLAIM

## Setup

Consider scalar proper rational transfer functions

H_i(s)=N_i(s)/D_i(s),

with coprime polynomials and
deg D_i <= n_i,
deg N_i <= n_i-1.

Assume sample points s_1,...,s_m are distinct and are not poles of either transfer.

## Exact theorem

If

H_1(s_k)=H_2(s_k)

at at least

m >= n_1+n_2

distinct sample points, then

H_1(s) = H_2(s)

as rational functions.

Proof:
H_1-H_2 has numerator

P(s)=N_1(s)D_2(s)-N_2(s)D_1(s),

with

deg P <= n_1+n_2-1.

Agreement at n_1+n_2 distinct nonpole points gives at least n_1+n_2 distinct zeros of P, so P is identically zero.

For a common order bound n, 2n distinct exact samples suffice.

## Sharp claim ceiling

FINITE-FREQUENCY AGREEMENT
can imply
FULL-TRANSFER AGREEMENT

only after a finite rational order/degree ceiling is frozen.

Without such a ceiling, no finite sample set is information-complete for arbitrary rational functions.

Control:
given any finite sample set, multiply a nonzero perturbation by the polynomial
prod_k (s-s_k);
with sufficiently large allowed degree one can construct a distinct rational transfer agreeing on every sampled point.

Therefore:

FINITE FREQUENCY AGREEMENT != FULL TRANSFER AGREEMENT
on an unrestricted model class.

## Noise guard

The theorem is exact-data only.

Approximate agreement at sample points does not automatically give a uniform bound between samples.
Robust reconstruction requires a conditioning/interpolation theorem plus pole-separation and norm assumptions.

Thus:

EXACT UNIQUENESS != STABLE IDENTIFICATION.

## Mechanism guard

Even exact full-transfer equality identifies only the transfer behavior.
Internal realizations remain unique only up to the relevant minimal-realization equivalence, and nonminimal hidden completions can differ.

Therefore:

FULL TRANSFER AGREEMENT != PHYSICAL MECHANISM IDENTITY.

## DRAFT009 placement

INVARIANCE_RESOLUTION:
FINITE_FREQUENCY_SET can be promoted to FULL_TRANSFER_FUNCTION only when:
- scalar rational host is legal;
- order bounds n_i are frozen;
- enough distinct nonpole samples exist;
- exact equality is the claim;
- source/readout semantics match.

Otherwise the finite-frequency level remains strictly weaker.

HOST_RELATION=EXACT_INSTANCE of polynomial identity/rational interpolation + realization theory.
PROJECT_ROLE=CROSS_HOST_COMPILER_RULE.

## Firewall

FINITE SAMPLE PASS != FULL TRANSFER PASS without model-order ceiling.
FULL TRANSFER PASS != REALIZATION IDENTITY.
EXACT UNIQUENESS != ROBUST RECOVERY.
MORE SAMPLE POINTS != NEW MECHANISM INFORMATION once the rational host is saturated.

REV020 active.
REV021 not created.
TPE thin compiler / HOLD.
NO CANON / NO EXEC_SIGN / NO NOVELTY.
