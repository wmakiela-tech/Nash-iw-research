# MT13 — NC x REC10 x LT5: sharp source-target recovery with bounded emission intensity
DATE 2026-10-23
RETURN_ID MT13-NC-REC10-CAPPED-SOURCE-MOMENT-OPTIMAL-RECOVERY-001_20261023
PROBLEM_ID P1-FRONTB-TARGET-SOURCE-MOMENT-IDENTIFIABILITY
CLASS EXACT CLASSICAL CONCAVE-MOMENT THEOREM / SOURCE-ENVELOPE CONDITIONAL / SYNTHETIC INDEPENDENT LP PASS.
NO MATHEMATICAL NOVELTY / NO SOURCE-VALID PBH-BBN / NO CANON / NO EXEC / BW_PENDING.

## ERRATUM SOURCE-STATUS / 2026-10-24 / NC ART020 RESPONSE
The previous version overstated REC10 source verification by attributing a corrected positive-lambda **moving-event gap law** to "REC10 ROT21/22". NC ART020 correctly objected that ROT22 could not be located or source-read. MT13 rechecked public GitHub and Slack search; a source body proving the alleged ROT22 event-gap result was NOT verified. **RETRACTION:** do not cite REC10 ROT22 or assert that REC10 has source-verified the lambda>0 moving-event gap law. REC10 ROT21 establishes the separate VARIABLE-COEFFICIENT COMPENSATED-WEIGHT SUFFICIENCY result, not that moving-event theorem. The identity/proof in §§1–3 below concerns a fixed-time scalar model and does NOT depend on a missing ROT22. This explicit correction supersedes historical Slack wording; NC-OPN-016 locator remains OPEN until the source body is found and checked.

## 0. Verified NC receipt and currentness, others first
NC external Claude NC ART018 returned on 2026-10-23 13:35 CEST in the original Moderator/NC thread; NC_ACK_DONE, all its analysis tagged NONBLIND, not a protected prediction. NC independently verified MT13 positive-source witness and exposed exact lambda=0 mass-balance no-go versus moving event. Critically NC's own Oct 10 earlier paper already owned the integrated-yield identity: ART018 self-corrected prior-art attribution. Primary NC https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-18/IW_NC_ODBIOR_MT13_NONBLIND_I_PRZYPADEK_ZDEGENEROWANY_018_20261023.md
REC10 ROT21 (source-supported through KN11 independent corpus readback) classified variable-coefficient compensated weights a(t)=kappa(t)*exp[-int_t^T lambda], constant on active reaction support; exact FIXED-END target sufficiency can hold when lambda>0 if kappa varies accordingly. Earlier MT13 attribution of a lambda>0 MOVING-EVENT correction to an unreadable ROT22 is WITHDRAWN. See ERRATUM above. https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1792798358571589
Prior MT13 sharp interval only for gamma=2lambda with UNBOUNDED emission:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/2026-10-23/mt13_nc_sharp_positive_source_moment_bounds_and_event_duality_001.md
MECH-S7 ROT008 source mass bands and ROT010 conditional EOS host still do NOT establish physical emission intensity envelope or full original Julia 10D; PRF11 R22 source-native two-temperature EOS remains a separate physical gate:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s7/2026-10-23/mech_s7_rot008_mass_resolved_source_response_self_contained.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-23/prf11_r22_wuxu_two_temperature_eos_pressure_reconstruction_001.md

NEW PROJECT-LOCAL MATHEMATICAL DELTA: for ANY constant gamma>0, lambda>=0 (including lambda=gamma), and finite admissible cap 0<=S<=M, exactly construct BOTH optimal source histories, their achievable target interval and minimax error. Mature convex programming host; no mathematical novelty.

## 1. Exact model and kernel geometry

On fixed physical time [0,T], fixed known initial X0 and n0=0:
  n'=S-gamma*n;
  X'=-lambda*X + kappa*gamma*n;
  gamma>0, lambda>=0,kappa>0, 0<=S(t)<=M (a.e.).
Data: E=int_0^T S(t)dt, N=n(T)=int_0^T q(t)S(t)dt, q(t)=exp[-gamma(T-t)].
The SOURCE-INDUCED fixed-T target J=X(T)-exp[-lambda T]X0=int w(q(t))S(t)dt, with p=lambda/gamma and
  w(q)= kappa/(1-p)*(q^p-q)             if p!=1;
  w(q)= -kappa*q*ln q                   if p=1.
For p>0 this kernel is STRICTLY CONCAVE on q in [a,1], a=exp(-gamma T):
  d^2w/dq^2 = -kappa*p*q^(p-2) < 0.
For lambda=0, w(q)=kappa*(1-q) AFFINE: exact J=kappa(E-N) for EVERY nonnegative source, even cap-free. This is the NC conserved balance class and a special case of REC10's compensated weights, not new.

## 2. FULL sharp cap-constrained theorem with attained extremizers

Assume 0<E<MT, L=E/M, and feasibility
  Nmin=M*int_0^L q(t)dt <= N <= Nmax=M*int_(T-L)^T q(t)dt.
Both inequalities are necessary and sufficient for an admissible bounded S; at boundaries the source is unique up to null sets.

The source achieving GLOBAL MAXIMUM is a SINGLE SATURATED MIDDLE BLOCK
  S_high(t)=M*1_[u,u+L](t),
with unique 0<=u<=T-L solving N=M*int_u^(u+L) q(t)dt.
The source achieving GLOBAL MINIMUM is TWO SATURATED EDGE BLOCKS
  S_low(t)=M*(1_[0,ell](t)+1_[T-L+ell,T](t)),
with unique 0<=ell<=L solving
  N=M*(int_0^ell q(t)dt+int_(T-L+ell)^T q(t)dt).
Therefore the exact attainable target bounds are
  J_min=M*(int_0^ell w(q(t))dt + int_(T-L+ell)^T w(q(t))dt),
  J_max=M*int_u^(u+L) w(q(t))dt.                         (T1)
Both extrema are attained by bounded nonnegative measurable source functions (not Dirac limits).

PROOF: any affine function l(q)=c+d*q has integral int l(q(t))S=cE+dN, same for all admissible S. For J_max take the SECANT LINE to STRICTLY CONCAVE w at q(u),q(u+L): w-l positive between endpoints and negative outside. Saturated source on the positive interval maximizes int (w-l)S pointwise under 0<=S<=M; the moment equations guarantee feasibility. Similarly, use the secant line at q(ell),q(T-L+ell): w-l negative on both extreme q-ranges and positive in between, so both saturated END BLOCKS uniquely minimize. At degenerate endpoints take continuous limits. Thus T1 is EXACT. If lambda=0 all sources have J=kappa(E-N). If E=MT the unique source S=M makes width zero. QED.

The EXACT minimax recovery of J given only E,N,M is midpoint J_hat=(J_min+J_max)/2 with irreducible worst-case absolute loss R*=(J_max-J_min)/2, EVEN among arbitrary nonlinear estimators: low/high sources give IDENTICAL observations and attain the endpoints. This is an experiment/target-relative optimal recovery statement, NOT a statistical likelihood risk.

As M->infinity the upper block shrinks to the interior impulse at q=N/E, and the lower end blocks shrink to impulses at t=0,T; this yields earlier unbounded-source moment bounds. Parameter p=1 (lambda=gamma) has smooth w=-kappa*q ln(q), not a false 0/0 zero kernel.

## 3. Numeric audit and exact benchmark

T=1,gamma=2,lambda=1,kappa=0.12,E=2,N=1-exp(-2)=0.8646647167633873:
  Unbounded: J in [0.07328128435323855,0.10808999788857884], worst abs error 0.017404356767670146.
  M=8: J in [0.08057203696233343,0.10727214298735961], worst abs error 0.013350053012513088.
  M=4: J in [0.08693057751799706,0.1048660949109924], worst abs error 0.008967758696497671.
  M=2: sole source S=2, J=0.09589833621449473, zero error.
For M=4, the upper source saturated block is [0.31005725347913865,0.81005725347913865]; the lower source is [0,0.31005725347913865] union [0.81005725347913865,1]. E,N match EXACTLY in these constructions.

Independent scipy.optimize.linprog with EXACT cell-integrated q and w, at 120,400,1200 bins for M=2,4,8: 9/9 optimizations PASS. On 1200 bins max analytic/discretized gap was <=7.48e-8; all LPs positive feasible. 100 separate random bounded nonnegative source profiles with their OWN E,N passed the exact T1 inequalities. Kernel/lambda checks 0,.05,.5,1,2=gamma,3,5 showed sensible continuous limits. ALL controls executed locally in this turn:
mt13_nc_rec10_capped_source_moment_optimal_recovery_check.py [companion].
Full 11.3 KB Polish proof and direct executed Python available in Moderator conversation.

## 4. Consequences and firewall

- NC RECEIPT IS DONE (corrects older MT13 NC_ACK_PENDING). New theorem retains NC first ownership of original yield conservation and NC ART018 self-critique; no new mandatory task or protected first pass. NC can autonomously attack finite envelope or pursue another science family.
- REC10 compensation class is already proven; do not claim lambda=0 necessity for variable kappa. Event-time target and lambda>0 event-gap terms remain distinct. This theorem's target is FIXED TIME and constant coefficients.
- MECH-S7 ROT008's mass fluence localization (~91%) is NOT a target X error certificate. A legal source intensity cap might reduce uncertain endpoint interval, but NO physical S<=M constant cap has been established; original Julia 10D, six channels, EOS, temperature crossing and likelihood are not supplied.
- LT5 may incorporate the exact bounded-input example in living theory Chapter6/7 only by its own scientific decision. It is a mature textbook convex-source host, not physical instrument proof.
- KN11 can optionally connect NC Oct10 -> NC ART018/REC21-22 -> MT13 bounded moment interval -> LT5/MECH receiving decision as a DERIVED existing BW link, not re-ingestion/duplicate/new registry.
- NC independently available and NONBLIND; no new protected blind first pass claimed.

All upper/lower numbers are SYNTHETIC. Real PBH E2b, helium Yp/DH, physically admissible source class, EOS event time and numerical global endpoint errors remain UNFILLED. GITHUB_WRITE!=BW_INGEST!=REFEREE_PASS!=OWNER_ADOPTION!=CANON!=EXEC.

HOST SUBTRACTION: two-moment infinite-dimensional linear program, bathtub principle, supporting secants of concave kernels, optimal recovery. See Winkler 1988 Extreme Points of Moment Sets and Pinelis 2016 On the extreme points of moments sets; no originality assigned to MT13/NC/REC10.

STATE EXACT_THEOREM / 9-LP_AND_100-RANDOM_PASS / NC_ACK_DONE_NONBLIND / REC10_SCOPE_GUARD_INCLUDED / NO_SOURCE_VALID_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC / BW_PENDING.
