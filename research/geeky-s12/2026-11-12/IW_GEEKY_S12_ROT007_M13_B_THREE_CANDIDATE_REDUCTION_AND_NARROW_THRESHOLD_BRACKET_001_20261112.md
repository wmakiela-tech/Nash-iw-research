---
artifact_id: IW_GEEKY_S12_ROT007_M13_B_THREE_CANDIDATE_REDUCTION_AND_NARROW_THRESHOLD_BRACKET_001_20261112
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
date: 2026-11-12
exposure: PUBLIC
science_status: AUTHOR_EXACT_RATIONAL_INTERVAL_SOURCE_M13_CERTIFICATE_PASS / INDEPENDENT_REFEREE_PENDING / OWNER_ADOPTION_PENDING
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: N41_FUNCTIONALLY_MATCHED_FIVE_MASK_B_SYNTHETIC_COMMON_GAIN_SOURCE_COEFFICIENTS_ONLY / NO_HISTORIC_PRODUCER_IDENTITY / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT007 — kanał B: globalna redukcja do trzech kandydatów i granica separacji 0,025–0,02514

## 0. Wynik naukowy, datowanie i kwantyfikatory

Zamrożony problem: M13 N=41, kanał B, pięć zagnieżdżonych masek k=2,...,6, jedna wspólna nieznana DODATNIA amplituda ENERGII, dokładna geometria rozłącznych powłok i syntetycznego modelu szumu M13, alpha i beta w [0,1/5]. Wszystkie nowe nierówności opierają się na oryginalnym pliku skierowanych przedziałów M13, nie na środkach float. Historyczny producent dtc0a_runtime_v0_3_1.py nadal nie został odzyskany byte-identically.

**ROT007.1: REDUKCJA TRÓJPUNKTOWA DLA DOWOLNEJ separacji.** Dla KAŻDEGO alpha∈[0,1/5] i KAŻDEGO delta>0, gdy zbiór legalnych beta jest niepusty:

  min_{beta∈[0,1/5], |beta-alpha|>=delta} D_B²(alpha,beta)
  = min_{beta∈({0,alpha-delta,alpha+delta}∩[0,1/5]), |beta-alpha|>=delta}
      D_B²(alpha,beta).

Włączenie 0 jest warunkowe: beta=0 może być kandydatem wyłącznie gdy alpha>=delta. Innymi słowy, mimo udokumentowanej niemonotoniczności radialnej B, globalna optymalizacja na całym zbiorze legalnym redukuje się źródłowo do co najwyżej TRZECH jawnych alternatyw, a nie dwóch. Dla alpha<=.028 wystarczają zawsze dwa najbliższe punkty; trzeci potencjalnie istotny pojawia się jedynie w wyjątkowej małej-beta strefie.

**ROT007.2: DODATNIE TWIERDZENIE UNIFORM w delta.** Dla wszystkich alpha∈[0,1/5] i wszystkich rzeczywistych 0<delta<=1/40=.025, globalne minimum jest osiągane przy legalnych beta=alpha±delta. Całe kontinuum delta, nie skończony skan.

**ROT007.3: ŚCIŚLE BLIŻSZY FALSYFIKATOR** niż ROT004 (.035) i ROT006 (.026):
  alpha=1541/50000=.03082,
  delta=1257/50000=.02514,
  beta_*=1/1000000=.000001 (ściśle INTERIOR),
  beta_L=71/12500=.00568,
  beta_R=1399/25000=.05596.

| beta | rola | 10^24 D_B² (ludzka aproksymacja) |
|---:|---|---:|
|0| kontrola brzegu|0.28632718240805416|
|0.000001|legalny dalszy punkt WEWNĘTRZNY|0.28632991635915184|
|0.00568|najbliższy lewy|0.28635263194909905|
|0.05596|najbliższy prawy|0.48950199921011717|

Exact strict rational directed interval:
  upper D²(alpha,beta_*) < lower D²(alpha,beta_L)  PASS;
  upper D²(alpha,beta_*) < lower D²(alpha,beta_R)  PASS.

Dokładne dodatnie dolne ZAPASY przybliżone (razy 10^24):
  left_lower - witness_upper >= 0.000022715589947220627 >0;
  right_lower - witness_upper >= 0.20317208285096533 >0.

|alpha-beta_*|=0.030819 > delta=0.02514. Tak więc OBA najbliższe punkty NIE są globalnie minimalne. To nie dowodzi, że beta_* jest globalnym minimizatorem. Powyższe próby znaków są EXACT; zapisane 10^24 liczby tylko prezentacyjne.

**Wspólny wniosek dla pierwszej możliwej utraty:**
  delta_first := inf{delta>0 : istnieje alpha z brakiem globalnego minimizatora w najbliższych beta=alpha±delta}.
  0.025 <= delta_first <= 0.02514.

Przy delta=.025 reguła jest CERTYFIKOWANA poprawna. Nie twierdzimy ani że delta_first jest wyznaczone dokładnie, ani że zbiór separacji ze złamaniem reguły jest monotoniczny, ani że beta_* jest globalnym argmin.

## 1. Pierwszeństwo i źródłowa mapa

**M13 źródłowe FIRST:**
M13 ROT32/33 identyfikacja źródłowej rodziny parametrów, ROT35 geometria rozłącznych powłok/kovariancji, ROT37/38 konkretne certyfikaty argmin, ROT39 dokładne B delta=.01 porównanie dwóch stron z jednym punktem przełączenia alpha_B≈0.03265254963589545, ROT40 A/C globalne radialne ALL delta i pierwszy przykład niespełnienia radialnej monotoniczności B. M13 NIE rozstrzygnął wtedy globalnego B delta=.01.

**Geeky S12 FIRST:**
ROT004 kontrprzykład do B ALL-delta nearest-only przy delta=.035; ROT005 źródłowy pozytywny ALL-alpha B fixed delta=.01; ROT006 źródłowy pozytywny ALL-alpha AND ALL delta<=.02 plus wewnętrzny falsyfikator delta=.026. ROT007 zachowuje wszystkie pierwszeństwa i daje trzy-kandydatową redukcję w CAŁEJ dziedzinie, bezpieczny promień .025 i ścisły negatywny punkt delta=.02514.

M13 public original directed interval coefficients:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json
GIT BLOB SHA-1 a6f50fbe5904e580e84c87ee87c5ad043cdec5d0, exact readback.
M13 ROT40:
https://github.com/wmakiela-tech/Nash-iw-research/blob/27188018c1dbbcee81d391ceb8ba5c55237cff7e/research/m13/2026-10-26/IW_M13_ROT40_universal_AC_radial_mask_global_argmin_001.md
M13 ROT39:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-25/IW_M13_ROT39_full5_nearest_alternative_side_switch_001.md
ROT005 proof source:
https://github.com/wmakiela-tech/Nash-iw-research/blob/60d00bbf497c2384800588a85547920ca039ae16/research/geeky-s12/2026-11-12/IW_GEEKY_S12_ROT005_M13_B_FIXED_DELTA001_GLOBAL_NEAREST_ENDPOINT_BERNSTEIN_CERTIFICATE_001_20261112.md
ROT006 theorem:
https://github.com/wmakiela-tech/Nash-iw-research/blob/e3e81464ebd371d15dfc665d20c9a5e555aa4944/research/geeky-s12/2026-11-12/IW_GEEKY_S12_ROT006_M13_B_UNIFORM_SMALL_DELTA_AND_SHARPENED_FAILURE_GATE_001_20261112.md

**Source architecture:** N=41, k=2..6, exact n=(50653,42875,35937,29791,24389), disjoint weights W=(7778,6938,6146,5402,24389), M13 functional auxiliary fields C1=(.05sin x,.05cos y,0), C2=(.04cos z,0,.04sin x), pure-trace AMBIENT h=.1sin x cos y I, central stencil order 2, E_alpha=I+alpha grid_h² Delta_2, flat Fourier TT. The actual historic dtc0a_runtime_v0_3_1.py and full physical producer are NOT byte recovered. M13's mpmath.iv generation from the auxiliary Fourier model is inherited input, NOT reproduced in ROT007. This is a claim about the EXACT public SOURCE COEFFICIENT intervals conditional on source-generation fidelity, not an assertion of real NASH K/J3/TPE or measured covariance.

## 2. Canonical algebra and invariant positivity domains

Let g_k(t)=RMS_mask(K_B(t))² be quartic interval polynomials, s_i(t) disjoint-shell means:
 s_i(t)=[n_i*g_i(t)-n_(i+1)*g_(i+1)(t)]/w_i for four shells, s_5(t)=g_6(t).
All s_i have positive EXACT directed-interval Bernstein lower bounds on t∈[0,.2]. After multiplying s_i by 10^12 for computational conditioning, lower values:
[.009861818352395727, .01309046297286641, .01823900751176885, .024583138646238557, .03335654554126909].

For a=s(alpha), b=s(beta), p=<a,b>_W>0, q=<b,b>_W>0, common optimum gain t=p/q>0,
 D²(alpha,beta)=min_{t>0}||a-tb||_W²
    =||a||_W² - p²/q
    =N(alpha,beta)/q,
 N=sum_(i<j) w_i*w_j (a_i*b_j-a_j*b_i)².

Define H=2p_beta*q-p*q_beta, with D²_beta=-p H/q².
Exact algebra yields H=(alpha-beta)P(alpha,beta); P is bivariate deg<= (3,9), from
 P=2 sum_(i<j) w_i*w_j Q_ij(alpha,beta)*R_ij(beta),
 Q_ij=(s_i(alpha)s_j(beta)-s_j(alpha)s_i(beta))/(alpha-beta),
 R_ij=s_i'(beta)s_j(beta)-s_i(beta)s_j'(beta).
The Q division is FORMAL polynomial divisibility of antisymmetric monomials, not numeric division by an approximate small number.

The original SOURCE_DIRECTED_BIGINT_INTERVAL_BERNSTEIN positive gates of ROT006, retrieved and reexecuted from pinned code, certify:
(A) P>0 for ALL alpha∈[0,.2] and beta∈[.008,.2], by 5 exact rectangular bounds:
+6817.992..., +14508.510..., +1317636.713..., +2776.277..., +179369.803...
(B) P>0 for alpha∈[0,.028], beta∈[0,.008], lower +310.210...
(C) P_beta>0 for alpha∈[.028,.2], beta∈[0,.008], lower +38348.396...

These three gates PLUS the five shell positivity gates establish the full three-point reduction WITHOUT choosing delta, and remain prior-dated ROT006 first for individual sign inequalities. The reduction theorem itself is ROT007, not a new positivity calculation.

## 3. Proof ROT007.1 — at most THREE candidates for arbitrary delta

Choose alpha,delta and assume legal alternatives nonempty.

If alpha<=.028, (A)+(B) imply P(alpha,beta)>0 for ALL beta∈[0,.2]. Because sign(D²_beta)=sign(beta-alpha) wherever beta≠alpha, D² is strictly decreasing to alpha from the left and increasing beyond alpha. Therefore the global min over legal beta lies at closest legal beta=alpha±delta; adding beta=0 to the candidate set if legal cannot improve.

If alpha>=.028, on RIGHT beta>alpha>=.028>.008 and (A) gives D² strictly increasing; minimum on legal right branch is beta_R=alpha+delta if legal.

For LEFT beta<alpha:
- if beta>=.008, (A) makes D² strictly decrease with beta, so minimum over such legal beta occurs at the RIGHTMOST legal left point beta_L=alpha-delta when >=.008.
- if beta∈[0,.008], (C) says P(alpha,beta) is STRICTLY increasing with beta. Since alpha-beta>0, sign(D²_beta)=negative sign P. Therefore D²_beta can change only from PLUS to MINUS as beta increases: at most one interior stationary point, and if it exists it is a MAXIMUM, not a minimum. Thus the minimum on every closed subinterval of [0,.008] is at one of that subinterval's endpoints.

At beta=.008 the high-beta monotonicity (A) continues and prevents beta=.008 being better than a legal rightmost beta_L when such a beta_L>=.008 exists. Therefore the LEFT global minimum is always one of beta=0 (provided alpha>=delta, i.e. beta0 legal) or beta_L=alpha-delta. Combining legal left and right candidates proves exactly the 3-candidate identity. No beta grid scan and no general radial monotonicity of B is assumed.

This reduction is USEFUL even when two-nearest-only is false, because the ONLY possible extra global competitor is the true parameter-domain endpoint beta=0 (not a hidden arbitrary interior local minimum). The positive interior witness beta_*=.000001 from ROT007.3 is strictly BETTER THAN TWO NEAREST POINTS but is NOT asserted to beat beta=0; indeed at this alpha its D² is slightly above D²(alpha,0).

## 4. Proof ROT007.2 — ALL real delta<=.025, not point sampling

Define delta_max=1/40=.025, a_c=7/250=.028, b_c=1/125=.008.

Two NEW exactly checked interval Bernstein families extend ROT006:

(D) **P on the shifted line beta=alpha-.025.**
For alpha∈[.028,.033], beta=alpha-.025 lies in [.003,.008]. Compose the EXACT sourced interval polynomial
 L(alpha):=P(alpha,alpha-.025)
by substitution and binomial expansion in the interval coefficient ring. Two 1D exact rational Bernstein positivity certificates:
 alpha∈[.028,.03] : lower +1687.9594888238569;
 alpha∈[.03,.033]: lower +3234.1348388707725.

(E) **F0 at delta_max=.025.**
Let q(t)=||s(t)||_W², N as in §2, and
 F0(alpha)=N(alpha,0)*q(alpha-.025)-N(alpha,alpha-.025)*q(0).
This is a univariate deg<=16 interval polynomial, constructed from formal wedge-difference quotients to avoid cancellation. EXACT 1D Bernstein lower bound on the WHOLE [.028,.2] is negative (certificate method is inconclusive, not the polynomial). Dividing into EIGHT rational intervals gives STRICTLY positive lower bounds:

 alpha [.028,.030]: +1.0372508111102978
 alpha [.030,.032]: +0.734134511266705
 alpha [.032,.033]: +2.7138745452810364
 alpha [.033,.035]: +7.654278560167521
 alpha [.035,.040]: +32.440423812103816
 alpha [.040,.050]: +269.38736547190854
 alpha [.050,.100]: +2967.982186960598
 alpha [.100,.200]: +1145626.1474003564

Hence D²(alpha,0) > D²(alpha,alpha-.025) for ALL alpha∈[.028,.2]. These 8 strictly positive rational interval comparisons are mathematical certificates (not sampled alpha values), under the M13 source coefficients. The approximation numbers are only rendering of the exact rational bounds.

**Uniform proof:**
For alpha<=.028, positivity (A)+(B) gives global radial monotonicity, hence all delta>0 nearest legal endpoints.

For alpha>=.028, show P(alpha,beta)>0 on EVERY beta∈[alpha-.025,.2]. If alpha>=.033, beta>=alpha-.025>=.008 and use (A). If alpha∈[.028,.033], use (D) at beta_start=alpha-.025∈[.003,.008], then (C) strict P_beta>0 on [beta_start,.008] and (A) for beta>=.008. Thus D² is radially monotone on the full interval from beta=alpha-.025 THROUGH alpha and into the right side for all alpha>=.028.

Now fix any real delta with 0<delta<=.025 and alpha>=.028. beta_L=alpha-delta exists and >=alpha-.025>=.003. Since P>0 on [alpha-.025,alpha], radial monotonicity gives
 D²(alpha,alpha-delta) <= D²(alpha,alpha-.025) < D²(alpha,0)
by (E). Right branch again minimized at nearest beta_R if legal.

For the entire LEFT legal beta domain [0,alpha-delta], theorem ROT007.1 gives its min among beta0 and beta_L; strict inequality above excludes beta0, so beta_L wins the LEFT branch. Therefore global min is beta_L or beta_R if legal. This applies to all alpha∈[0,.2], all REAL delta∈(0,.025] without a discrete delta scan. QED.

**Count of positivity tests actually executed on exact source coefficients:** inherited 5 P rectangle + 1 small P + 1 P_beta + 5 shell = 12, plus NEW 2 shifted-line P + 8 F0-subdivision = 10, altogether 17 polynomial gates plus 5 shell gates = 22 strict exact rational signs PASS. The two families of NEW tests use no floating-value decisions.

## 5. Proof ROT007.3 — source exact negative witness at .02514

Parameters (exact, rational):
 alpha=1541/50000=.03082;
 delta=1257/50000=.02514;
 beta_*=1/1000000=.000001;
 beta_L=alpha-delta=71/12500=.00568;
 beta_R=alpha+delta=1399/25000=.05596.

These source-typed four distinct values beta={0, .000001,.00568,.05596} were read from the original 25 x lower/upper coefficient intervals and evaluated by separate rational-interval wedge code. The comparator uses
  UPPER D²(alpha,beta_*) < LOWER D²(alpha,beta_L)
and
  UPPER D²(alpha,beta_*) < LOWER D²(alpha,beta_R)
with exact rational integer cross-products. Both PASS, with strict positive directed interval gaps in §0. A purely floating calculation was used ONLY to discover candidate rational values; the proof is independent of floating inaccuracies.

**Why it is a correct logical falsifier:** beta_* is legal but farther (distance .030819 > .02514) and beats both nearest alternatives, therefore neither beta_L nor beta_R can be global minimizer. No claim of determining the actual global minimizer. ROT007.1's three-candidate theorem suggests beta=0 may be the actual global minimizer (and here D0 < D(beta_*)), but we do NOT identify the global argmin by an unperformed direct beta0-vs-both-nearest certificate in this section, and need no such assertion for falsification.

## 6. Public reproducibility artifacts and readback

Source DIRECTED coefficient table original Git blob:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json

PUBLIC POSITIVE exact rational Bernstein program, frozen original source Git SHA and blob check, N41, all delta<=.025:
https://github.com/wmakiela-tech/Nash-iw-research/blob/cb939cbd3a939cdbb4633f283b6185d622c80f24/research/geeky-s12/2026-11-12/iw_geeky_s12_rot007_exact_B_uniform_delta_le_0025_rational_bernstein.js

PUBLIC NEGATIVE exact rational interval interior witness at delta=.02514:
https://github.com/wmakiela-tech/Nash-iw-research/blob/e555d8aeff0f1354364f10d494bf320e1cd0f2cf/research/geeky-s12/2026-11-12/iw_geeky_s12_rot007_exact_B_delta_002514_interior_falsifier.js

PUBLIC machine-readable results reexecuted from BOTH just-published source bodies against freshly read frozen M13:
https://github.com/wmakiela-tech/Nash-iw-research/blob/39f107068f5e4a96f7e9f6d21b549d8e5beb7830/research/geeky-s12/2026-11-12/IW_GEEKY_S12_ROT007_B_PHASE_THRESHOLD_CERTIFICATE_RESULTS_001_20261112.json

All three artifact GitHub writes and exact byte readbacks PASS; both original published function bodies reexecuted against M13 source in authenticated connected V8 tool, independent of file authoring variable. Actual Node.js CLI/network wrapper was NOT tested separately; code's mathematical body was executed and verified. Do not present any last-failure infimum as numerically/analytically SHARP. The local float exploration estimated something near .02513, NOT a proof, and is omitted from statuses.

## 7. Custody, limitations, stop

As-of 12 Nov 2026 14:15 CET a bounded #iw-dispatch check found NO independent REC11/AUD1 review or M14 adoption of ROT005/006; those statuses remain pending. Cross-surface BW KN13 ingestion not verified for ROT004–007. This ROT007 source delivery does not imply recipient ACK. Source original generator and functional equivalence to historical runtime require separate admissible evidence; do not generate false forensic producer identity.

Claim boundaries:
- ONLY source-M13 functionally matched auxiliary N41 Fourier-TT flat projection, same C1/C2, pure trace ambient h and central stencil2;
- channel B, five masks k=2,...,6, one common positive gain and synthetic i.i.d. voxel energy host (not measured covariance);
- no extrapolation to channels A/C beyond M13 source theorems; A/C existing radial ALL-delta PASS remains owned by M13;
- no inference on actual TPE/J3/K, GR/GW/BBN/PBH or instrumentation; no mathematical novelty claim for Bernstein/Gram algebra;
- two distinct functions for signs, but author-level computational proof only, independent referee pending; M14 owner decision pending;
- no automatic new scientific directions or task cascades.

Independent bounded audit question: verify Q_ij,R_ij and H relation from independent algebra, verify all 22 directed rational signs including shifted-line P and subdivided F0, reproduce beta=.000001 strict source intervals, and check exact three-candidate topology for all legal delta. If I3 and M14 accept, update source-science status by separate owner action only. As scientist of this cell, STOP further synthetic threshold-factory refinements until this structural 3-candidate gate is reviewed or source-native new input appears.

FINAL: EXACT_SOURCE_INTERVAL_THREE_CANDIDATE_REDUCTION_PASS / UNIFORM_DELTA_LE_0P025_PASS / EXPLICIT_DELTA_0P02514_NON_NEAREST_FAIL / FIRST_FAILURE_INF_BRACKET_[0P025,0P02514] / HISTORIC_PRODUCER_HOLD / REFEREE_PENDING / OWNER_ADOPTION_PENDING / BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
