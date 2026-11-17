#!/usr/bin/env python3
"""PRF14 ROT004: exact rational clock-and-KL no-go on R34 reference contract.

The checked statement is conditional on single-instrument sequential reference
readouts of duration >= 0.1 gamma-time and instantaneous conditional Bernoulli
probabilities at their timestamp; this is not a physical detector measurement.
"""
from fractions import Fraction as Q
from decimal import Decimal, localcontext

q = Q(247, 4600)                            # PRF12 R34 nominal p1*
delta = Q(9398133420642572, 10**18)        # R34 Eq. 34.7 displayed tolerance
L = Q(1, 500)                              # hypothetical drift cap 0.002
tau = Q(1, 10)                             # sequential reference read time 0.1
alpha = beta = Q(1, 20)                    # error constraints 0.05 each

# A tent alternative p1(t)=q+[2delta-L*|t-center|]_+ has height 2delta
# and support width 4delta/L, with p0(t)=99/100 unchanged.
width = 4*delta/L
clock_slots = width/tau
n_max = clock_slots.numerator//clock_slots.denominator + 1
center = Q(50, 1)
left = center-2*delta/L
right = center+2*delta/L

def alt_p1(t):
    return q + max(Q(0, 1), 2*delta-L*abs(t-center))

assert alt_p1(left) == alt_p1(right) == q
assert alt_p1(center) == q + 2*delta
assert q+2*delta < Q(1, 2) < Q(99, 100)
assert left > 0 and right < 100
assert alt_p1(center-Q(1)) == q+2*delta-L
assert alt_p1(center+Q(1)) == q+2*delta-L

# Per-observation KL (stable Bern(q) || bumped Bern(q+x)) <= chi-squared
# <= 4delta^2/[q(1-q)] for any x in [0, 2delta], since bumped v<1/2.
per_ref_KL_upper = 4*delta**2/(q*(1-q))
transcript_KL_upper = n_max*per_ref_KL_upper

# Data-processing KL >= binary kl(P0(CERTIFY),P1(CERTIFY)).
# Pinsker with natural logs yields >= 2*(1-alpha-beta)^2 exactly.
required_KL_lower_Pinsker = 2*(1-alpha-beta)**2
assert transcript_KL_upper < required_KL_lower_Pinsker

# Necessary number of *informative* clock-spaced readouts using Pinsker.
needed_fraction = required_KL_lower_Pinsker/per_ref_KL_upper
n_needed = -(-needed_fraction.numerator//needed_fraction.denominator)
assert n_needed == 233 and n_max == 188 and n_needed > n_max

# Non-fatal native R34 negative control: L=1e-4 is NOT ruled out by this gate.
L_small = Q(1, 10000)
slots_small = (4*delta/L_small)/tau
cap_small = slots_small.numerator//slots_small.denominator+1
assert cap_small*per_ref_KL_upper > required_KL_lower_Pinsker

# The exact kl(.95||.05) threshold is larger; this is DIAGNOSTIC ONLY.
with localcontext() as ctx:
    ctx.prec = 70
    full_binary_kl = Decimal(9)/Decimal(10)*Decimal(19).ln()
    def dec(v):
        return Decimal(v.numerator)/Decimal(v.denominator)
    print('p1* =', dec(q))
    print('delta* =', dec(delta))
    print('L =', dec(L), '; minimum inter-reference spacing =', dec(tau))
    print('tent support width =', dec(width))
    print('maximum informative sequential reference reads =', n_max)
    print('per-observation KL upper =', dec(per_ref_KL_upper))
    print('whole-transcript KL upper =', dec(transcript_KL_upper))
    print('Pinsker rational necessary transcript KL >=', dec(required_KL_lower_Pinsker))
    print('Pinsker necessary informative reads >=', n_needed)
    print('exact binary KL(.95||.05) =', full_binary_kl)
    print('exact-binary-KL necessary count (diagnostic) =', full_binary_kl/dec(per_ref_KL_upper))
    print('negative control L=1e-4, max reads =', cap_small,
          ': THIS gate does not rule it out')
    print('PASS: exact rational sequential-clock information impossibility for L=0.002')
