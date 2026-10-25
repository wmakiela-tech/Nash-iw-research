# MT13 ROT040 — PRF11 R34: one age bit exactly recovers full Helstrom information on a parameter interval

**DATE:** 2026-10-25
**RETURN_ID:** MT13-ROT040-PRF11-R34-TWO-AGE-BIN-EXACT-HELSTROM-SUFFICIENCY-001_20261025
**PROBLEM:** LT4_CH7_MULTI_SLOT_AGED_MEMORY_LABELLED_POISSON_TARGET_RELATIVE_SUFFICIENCY
**CLASS:** EXACT CLASSICAL SOURCE-TYPED POINT-PROCESS NEYMAN–PEARSON / TWO-AGE-BIN FINITE-COMPRESSION / INDEPENDENT FINITE-n CAUCHY VERIFICATION
**CEILING:** NO NOVELTY / NO CANON / NO EXEC_SIGN / NO PHYSICAL DEVICE / NO GENERAL MULTISLOT COMB OPTIMUM / NO BW INGEST OR OWNER ACCEPTANCE IMPLIED.

## 0. Priority of original source / literature
**PRF11 R34 owns FIRST** the aged SWAP memory model, the sharp full-quantum visibility threshold, the inhomogeneous age-labelled Poisson point-process (PPP) limit, the need for age labels over the total count, and an exact one-event *LOWER* gain witness:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R34_AGED_MEMORY_SHARP_VISIBILITY_POINT_PROCESS_AND_LABEL_SUFFICIENCY_001_20261025.md
Source Git blob bcd57a83f40a6dd4aaf1449af61d1227e14bef35.
**PRF11 R33 first** controls endpoint-per-probe noise and count-only Poisson thresholds:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R33_NOISY_MULTISLOT_POISSON_LIMIT_AND_MEMORY_VISIBILITY_GATE_001_20261025.md
LT5 ROT19–21 owns target-relative source/measurement sufficiency; NC and XH own separate source/memory admissibility results. None is recast as MT13 original.
**PROJECT-LOCAL NEW DELTA:** a FIXED FINITE RECORD of just count 0/1/atleast2 PLUS one comparison bit for age of the lone event is FULL binary-decision sufficient on a NONTRIVIAL R34 parameter interval. A fixed 50/50 two-bin observation has an analytically sharp noise budget 28.8496% higher than the R34 count-only budget. These are mature Neyman–Pearson/PPP likelihood and Blackwell/data-processing facts; not mathematical novelty or a device claim.

## 1. Original R34 lawful asymptotic carrier
Under R34 fixed ideal SWAP probe protocol and independent time-of-storage dephasing, a=gamma T, beta=lim n kappa_n T, hypothesized process A has ONE shared Cauchy phase, B independent Cauchy-Lévy increments. After measuring X on each probe, R34 proved terminal full-quantum asymptotic optimality of the INHOMOGENEOUS AGE-LABELLED PPP on u in [0,1]:
  lambda_A(u)=beta*u/2;
  lambda_B(u)=(beta*u+a)/2.
For any recorded event ages u_1,...,u_K, its exact likelihood ratio:
  L(B/A)=exp(-a/2) product_i [1+a/(beta*u_i)].
The full terminal trace distance tends to 2*TV(PPP_A, PPP_B), proven by PRF11 R34. We use that theorem; do not re-prove R34 or conflate actual quantum finite-n vs PPP limit.

## 2. One bit FULL optimum: a=4 ln2, 2a/3 <= beta <= a
Since exp(-a/2)=1/4, K=0 has L=.25<1. For K>=2, L>=(1/4)(1+a/beta)^2>=1 whenever beta<=a; all >=2-event records MUST choose B. For K=1, L>1 exactly iff age u<u_star= a/(3 beta). In the stated interval u_star in [1/3,1/2]. Thus the following FOUR-OUTCOME COMPRESSED RECORD preserves the EXACT full-labelled Helstrom/NP decision:
  count category 0 -> A;
  count category >=2 -> B;
  count exactly1 -> B iff its ONLY event was younger than u_star, else A.
One comparison bit for a SINGLE event plus a saturating 0/1/2+ count is fully sufficient **for this particular pair of known hypotheses and decision loss**, not a statistical sufficient summary for unknown beta, arbitrary mechanisms or all inference tasks. u_star depends on known beta.

With mu_A=beta/4 and mu_B=beta/4+a/2, the count-only optimal test in this interval chooses B iff K>=2, and
  V_count(beta)=exp(-beta/4)(1+beta/4)-exp(-beta/4-a/2)(1+beta/4+a/2).
On K=1 the signed Janossy density is
  delta_1(u)=exp(-beta/4)/2*[a exp(-a/2)-beta(1-exp(-a/2))*u].
Integrating its positive part from 0 to u_star gives **EXACT full-labelled TV**, not just R34's lower bound:
  V_full(beta)=V_count(beta)+exp(-beta/4)*[a exp(-a/2)]^2/[4 beta(1-exp(-a/2))]
              =V_count(beta)+exp(-beta/4)*a^2/(48 beta)
for a=4ln2, beta in [2a/3,a]. There are NO missing K>=2 sign contributions in this range; full likelihood L>=1 on every such record.

## 3. TWO FIXED 50/50 AGE BINS, SHARP BINARY TEST
Keep two aggregate independent PPP counts young u<.5 / old u>=.5. Under A their means are (beta/16,3beta/16); under B (beta/16+a/4,3beta/16+a/4). Likelihood
 L_2(k_y,k_o) = (1/4)(1+4a/beta)^k_y (1+4a/(3beta))^k_o.
For a=4ln2 and 4a/9 < beta < 4a/3, optimal decision for FULL two-bin counts is exactly:
  K=0 ->A; K>=2 ->B; K=1 ->B iff age bin young.
Proof: likelihood sign on K0, K1_young, K1_old; on K>=2 least favourable is 2 old events and has L>=1 iff beta<=4a/3. This is the complete Neyman–Pearson classification, not just a suboptimal selected statistic.

Its exact total variation in this interval:
 V_2(beta)=exp(-beta/4)*[(1-exp(-a/2))*(1+3beta/16) - (a/4)*exp(-a/2)]
          =exp(-beta/4)*(3/4-ln2/4 + 9beta/64).
Derivative is strictly negative for beta>=0 at this a. Outside the local NP interval the expression describes only the selected test, NOT necessarily full two-bin TV, but increasing beta ADDS the SAME independent PPP beta*u/2 to BOTH hypotheses; this is a Markov garbling, so true two-bin TV never increases with beta. Therefore the cutoff found INSIDE the NP interval is the EXACT global critical beta for the whole class of tests that see only two fixed 50/50 age bins (compared with ideal one-slot D1=1-exp(-a)=15/16).

R34/R33 count-only beta_count critical = 2.372658543704125 (first credit PRF11);
NEW two-bin beta_two=3.05716157694264, unique V_2(beta_two)=15/32;
increase beta_two/beta_count−1=0.28849622506991 (**28.8496%**).
Both beta values lie STRICTLY between 4a/9 and 4a/3.
This is a result for dimensionless beta=n kappa_n T, with kappa_n T scaling 1/n; no claim for fixed nonzero physical storage rate.

## 4. Source-specific exact Helstrom gain and a falsifier for overclaim
At beta=beta_count, a=4ln2:
  V_count=.468750000000
  V_two_bins=.503047510939003
  V_full_labelled=.506048064617336
  u_star=.389519277099086.
So two fixed age bins recover 91.9552% of the source's exact age-label visibility advantage over mere total counting; one ADAPTED age-bit threshold recovers **100%** for the known parameter pair. Terminal quantum limit trace norm 2V_full=1.01209612923467, vs ideal one-slot .9375.
At beta=beta_two (3.05716), u_star=.302305330447 lies strictly INSIDE the young half. Keeping full age rather than fixed halves can improve TV by at least 0.0104323580251 from the previously misclassified single events u in (u_star,.5). Thus V_full(beta_two)>=.479182358>15/32: beta_two is NOT the full-age optimum critical budget, only the TWO-BIN optimum. Do not call 28.85% the optimal global improvement of all age measurements.

## 5. Any L-bins: a general quantified truncation loss
On L equal age bins the averaged lambda is constant within each bin. Its L1 distance from either source true linear lambda is beta/(8L). The two PPP laws for these averaged intensities have the EXACT SAME binned count distributions as original PPP laws, and conditional event locations under the averaged model are uniform and identically distributed under both hypotheses. Coupling Poisson point processes and the triangle inequality give
  0 <= V_full_labelled−V_L_aggregate_counts <= beta/(4L).
This is robust but not tight, particularly L=2; its constant comes from TWO per-hypothesis coupling errors. No finite quantum n version is asserted.

## 6. Independently executed source-local tests and custody
A standalone NumPy/SciPy reproducer, no import of PRF R34 source code, tests:
 (i) exact analytic root equations/NP validity at count and two-bin critical beta;
 (ii) explicit joint Poisson k_y,k_old enumeration 30×30 for four values beta (difference vs closed TV <2e−14), and checks likelihood signs of EVERY counted pair;
 (iii) independent adaptive numerical quadrature of one-event signed Janossy positive part matches closed V_full <2e−14;
 (iv) actual finite-n A-source Cauchy shared-phase integral on a 16,384-point WRAPPED CAUCHY quadrature (not just source product limit) and independent finite-n B-source Bernoulli formula for n=4,8,16,32,64,128,256,512,1024; adaptive u_star analogous n16,64,256,1024. Source finite-n two-half test TV at n1024=.471502426831 and adapted threshold TV=.474298040507, approaching .50304751 and .50604806 respectively; slow convergence due Cauchy tail is expected. These finite-n values are NUMERICAL tests of one fixed local readout, not finite-n full quantum optima;
 (v) deterministic output JSON.
Full POLISH ~14.9KB exact proof, script, output JSON, stdout log, SHA manifest, README are in SINGLE Moderator ZIP:
 MT13_20261025_ROT040_PRF11_R34_two_bin_age_helstrom_reproduction.zip
 SHA256 7a28bb41554e523b14b4c8e35d7d581756c4ea7046ca7fdd0d387baf847d88aa
CLEAN EXTRACTION CRC+5 source SHA CHECK, delete extracted JSON, rerun source INSIDE clean directory with explicit --output, compare freshly generated JSON bytes EXACTLY — **PASS**. Source PRF11 R34 Git blob pinned above; no full quantum large-n eigensolver performed or claimed.

## 7. Receiver application, negative knowledge
PRF11 R34 remains source FIRST; this is a narrower age-compression/decision-extension with exact local budget and equality not an independent refutation. LT5/PRF11 target sufficiency: all ages NOT needed for one specified optimal binary test, even though total count alone is insufficient; full-label information may still be required for PARAMETER ESTIMATION or other targets. No direct NC/XH/MECH physical transfer.
NO physical memory hardware, actual dephasing calibration, gate noise, arbitrary adaptive tester optimisation, source-native full physics, Cauchy quantum claim novelty, NASH J3/K, PBH/BBN, canonicity or EXEC. Owner/referee acceptance/BW intake PENDING. No new task cascade.
