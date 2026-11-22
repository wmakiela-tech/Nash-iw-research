---
artifact_id: IW_M15_ROT042_ORIGINAL_M13_EXACT_LOGGAMMA_EXPONENTIAL_BERRY_ESSEEN_SOURCE_IV110_001_20261122
return_id: IW_M15_ROT042_ORIGINAL_M13_EXACT_EXPONENTIAL_SERIES_BERRY_ESSEEN_107M_99PCT_SOURCE_001_20261122
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-22
exposure: PUBLIC
class: ORIGINAL_PUBLIC_M13_NATIVE_SOURCE_IV110_EXPONENTIAL_SERIES_LOGGAMMA_BERRY_ESSEEN_FULLSITE_SPATIAL_INDEPENDENT_CHECK
bw_state: GITHUB_PENDING_BW_INGEST
ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_SITE_SENSOR / NO_TASK_CASCADE
---

# M15 ROT042 — exact independent exponential representation of Gamma log energies; rigorously sufficient 107m Gaussian raw snapshots for >99% each-hypothesis identification

## Bounded new result

M15 ROT041 first characterized the original six-Fourier-pair source calibration maximal invariant and minimax within group-invariant tests. Its 185 million independent complete N41-cubed raw Gaussian site snapshots were a STRICT mathematical sufficient 99% count; its approximate 106–110 million count came from unrigorous numeric Gamma-CDF inversion. ROT042 independently produces a STRICT outward IV110 certificate at **107,000,000** full hypothetical independent original RAW spatial snapshots, with **P(error | EACH source Gaussian hypothesis) < 0.009784362123427** uniformly in all independently fitted admissible original C5 calibration nuisance functions. The old 185m count is lowered without any new channel, stronger nuisance constraints or physical data.

This result uses the STANDARD independent-summands Berry–Esseen inequality with safe C=0.56 and the STANDARD Euler/Weierstrass Gamma product. No general mathematical literature novelty claimed.

Original scientific firstness retained: M13 FIRST public B Fourier N41 auxiliary; Geeky-S12 ROT035 FIRST two exact rational source-legal synthetic stationary Gaussian RAW site covariance shapes A/B; Geeky-S13 ROT001 FIRST entire-field unbounded smooth axial calibration alias; M15 ROT036 FIRST six-mode FACE+C4 Peano, ROT037 FIRST C5 gap, ROT038 FIRST direct log-Gamma Chernoff, ROT040 FIRST sharp C5 weighted gap, ROT041 FIRST maximal calibration invariant and invariant minimax. Original REC13/AUD3 mathematical audits and contributions unchanged.

## Original unmodified M13 source actually executed

Original public M13 8,970-byte complete Python SHA256 cd4aad089bf68e2e6155ff048d4d812943495dcf1770c8acbf0ff8111b1deb9c and original Git blob SHA1 c6377cfbc9a0070abc34ffedc5871e719f6a4679, BOTH verified BEFORE import:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py

Two separately written actually executed ROT042 scientific programs independently call unchanged original native tensor_polys(41)[1], calc(41,alpha=1/20)[1], inner(B,B,N41,k0). Original B tensor 41 Fourier modes, original B energy has EXACTLY 221 pair differences. Six wavevectors (20,20,20),(20,20,0),(20,0,0),(7,0,0),(12,12,13),(3,13,7), including conjugates, are ALL ABSENT from native energy support. So twelve orthonormal sine/cosine source deterministic means equal zero EXACT for any alpha.

Candidate A: beta0=1, theta=(3/25,1/10,2/25); candidate B: beta0=99779719687217/10^14 and axis=316869474178226/2494492992180425, face=93110637627687/997797196872170, body=205860943554709/2494492992180425. These source-legal Gaussian site covariance shapes were first given by Geeky-S12 and are SYNTHETIC and UNMEASURED. Same deterministic original M13 field mean in A and B.

Each candidate separately fits the SAME original class of five unbounded cubic-axial+FACE logvariance calibration parameters and C5 residual functions phi_X satisfying |phi_X''''|<=16.5 and |phi_X'''''|<=50. All physical noise, calibration, SIX new Fourier probes, IID snapshots and raw-site detector capabilities remain hypothetical. Historical complete DTC0a original runtime is missing.

SHA-locked complete actual parent source JSON artifacts in the verified user-local ZIP:
M15 ROT029 exact rational source SHA 00b8c93da96c9c92901555fd4c2db0af63978ecf735df3945e9ff42d218dee90;
M15 ROT040 sharp C5 gap IV110 SHA 0d495d0d0d1c5e74eff7743717659540d849f02b9314f3512a62c6cbca7bbb9e;
M15 ROT041 maximal invariant IV110 SHA b7d673f4f3dc70832a29f10aa67bb3481932d869c6ce405e0a14bcaeb4c9443d.
Source full 16,212-byte detailed paper, the scripts, and all original result machine data reside in attached VERIFIED local ZIP.

## Core exact mathematical argument

For n IID synthetic whole site Gaussian snapshots, each zero-mean sine/cosine pair supplies a squared-energy sum S_i; after dividing by twice its calibrated Gaussian variance, X_i=S_i/(2*var_X_i) are SIX independent Gamma(n,1) variables. The exact original M13 five-dimensional calibration nullvector w annihilates all unrestricted nuisance basis terms and satisfies sum_i w_i=0. The centered random log-score is Z_n=sum_i w_i log(X_i/n), with E Z_n=0.

Euler's Gamma infinite product implies EXACT equality in law (not asymptotic):
 log X_i - digamma(n) =_d -sum_(k=n)^infinity (E_ik-1)/k,
 E_ik independent Exp(1).
Its centered log-MGF is sum_(k=n)^infinity [t/k-log(1+t/k)] = logGamma(n+t)-logGamma(n)-t digamma(n). Variance-summable infinite series converges in L2 and a.s. The MINUS SIGN is crucial.

Thus Z_n is EXACTLY the limit of a sum of INDEPENDENT, not identically distributed, centered exponential contributions. Write V=sum w_i², W3=sum |w_i|³. The exact third absolute centered Exp(1) moment is 12/e-2. Variance of Z_n=V*zeta(2,n)=V*trigamma(n), and the independent summands total third absolute moments are (12/e-2)*W3*zeta(3,n). The standard independent Berry–Esseen theorem (constant C=0.56) extends to the infinite series by its finite partial sums and L2 convergence, giving:
 sup_x |P(Z_n/sigma<=x)-Phi(x)| <= 0.56*(12/e-2)*W3*zeta(3,n)/(V*zeta(2,n))^(3/2).

Source native original-M13 recomputation via outward IV110 LU verifies V between 2.814 and 2.815 and NEW W3 strictly below 2.495 (W3≈2.494862069480037). Original ROT040 strict sharp source C5 log-variance gap G is in (0.00075774501168477565096020000637363556489237632383875,0.00075774501168477565580745002956433489354556379071167). In particular conservative g0=0.00075774<G. The midpoint classifier has BOTH source conditional signed deterministic margins >=G/2, by symmetry of per-candidate C5 nuisance sets.

For all integer n>=2, rigorous classical sum bounds:
 zeta(2,n)>=1/n; zeta(3,n)<=1/[2(n-1/2)^2].
Using safe source constants Vlo=2.814, Vup=2.815, W3up=2.495, the conditional error is bounded by
 Q(z0) + eps_BE(n),
 z0=(g0/2)*sqrt((n-1/2)/Vup),
 eps_BE=.56*(12/e-2)*W3up*n^(3/2) / (2*(n-1/2)^2*Vlo^(3/2)).
Q(z)=1-Phi(z).

To RIGOROUSLY evaluate Q, the executable does NOT trust a floating normal CDF. It evaluates the classical entire alternating expansion Phi(z)-1/2=(1/sqrt(2pi))*sum_{j=0}^infinity (-1)^j*z^(2j+1)/(2^j*j!*(2j+1)), terms j=0..60 by genuine directed IV110 arithmetic, then explicitly ADDS the magnitude of the j=61 term as a safe alternating remainder. Source IV verifies 0<z<4, so the term magnitudes are decreasing after j=8. All trigonometric source values, weights, gamma moments, zeta and normal-tail bounds are protected by interval operations. The mpmath.iv erfc routine was not used because it failed to converge in a preliminary test.

Published theorem support: I.G. Shevtsova, On the absolute constants in the Berry–Esseen inequality and its structural and nonuniform improvements (2013), independent general-case constant <=0.5583, so conservative 0.56 is safe: https://www.mathnet.ru/eng/ia252 .

### Strict source IV110 mathematical sufficient counts

| Success > for EACH Gaussian candidate | n independent whole RAW 41³-site snapshots | Strict error upper |
| --- | ---: | ---: |
| 75% | 9,000,000 | <0.249181822 |
| 90% | 33,000,000 | <0.097342859 |
| 95% | 54,000,000 | <0.048567463 |
| **99%** | **107,000,000** | **<0.009784363** |
| 99.9% | 190,000,000 | <0.000953059 |

At 107m strictly:
normal survival Q(z0)<0.009749816951976;
Berry–Esseen NONZERO CDF correction eps_BE<0.000034545171451;
total<0.009784362123427.

Explicit false source assertion demanding this SAME bound certify 99% at n106m is rejected: its bound >0.0100734. This does NOT rule out a superior test at n106m; the old ROT041 numerical least-favorable minimax risk at approximately 106–110m was never a valid strict certificate.

## Second independently authored actual original source path and falsification

The second new program ACTUALLY executes unchanged original M13 and reconstructs all nine original B tensor complex components over every one of the 41³ sites by independent inverse FFT. It calculates the original energy and source mean-free sine/cosine projections, A/B raw spatial covariances from **6 AXIAL, 12 FACE and 8 BODY** explicit original periodic signed site array rolls, and derives nuisance weights independently by 5x6 numpy SVD, not importing main interval weights.

Its independent results reproduce V≈2.8147662920276706 and W3≈2.49486206948004, matching genuine original source IV110. It verifies the EXACT centered Gamma Weierstrass representation independently by checking the Gamma log-MGF against a 33-term Hurwitz-zeta series at n7,t=.35 to <1e-42, plus polygamma(1,n)=zeta(2,n) and polygamma(2,n)=-2*zeta(3,n), including n107m. Its separate scipy.stats.norm.sf plus exact special-function Berry correction agrees with the PRIMARY interval certificates to <4e-12; this is merely numeric corroboration and is NOT the proof.

USER-LOCAL original complete standalone runnable research ZIP:
IW_M15_ROT042_ORIGINAL_M13_LOGGAMMA_EXPONENTIAL_BERRY_ESSEEN_IV110_REPRO_001_20261122.zip,
45,020 bytes, SHA256 02a488e1f77477bf5858eb19aace221562569267857a185fbd3cda0397ba5933.
14 archive members: untouched M13, three frozen source full parent JSONs, two new scientific executable Python programs and both ACTUAL complete machine result JSONs, replay and TWELVE negative executable+receipt, complete detailed 16,212B local scientific paper, README, deterministic archive builder, SHA manifest. CRC PASS; all 13 payload SHA256 PASS; exact byte reread 14/14 PASS; deterministic independent ZIP rebuild byte identical PASS. Two complete new full JSONs independently Python -I cold reproduced BYTE IDENTICAL 2/2, and after FINAL ZIP extracted fresh both full source science JSONs AGAIN BYTE IDENTICAL 2/2. Twelve actual disposable separately mutated negative controls ALL FAIL CLOSED with expected named guards: M13 tamper both programs, source parents ROT029/ROT040/ROT041 corruption, current proof JSON corruption before independent spatial, false zero-energy-mean DC mode, false W3<2.490, false zero Berry correction, false 4-term normal CDF remainder, false 99%-106m proof, false exponential third absolute moment 10/e−2. No original source mutated. Main executed IV Python SHA9198427fd9925fe0fe74fa00d10b6d10c2142530349eec4f6c64fcb407e100d1 and full IV JSON SHA02fefa288bda7eacbc8c0835283d2cdad71d23d2278179f3fdb0e2410c3cd010; independent full site source Python SHA7896b7d46dbff1a7cec72f8d178b46709cd012d30e142ee937ce9e506dcf3a9b and full spatial machine JSON SHA893e0f791cc19d177db7915b524f3210925591c2ec014092094cfb92dbb30ed9.

## Hard boundaries and review request

Original PUBLIC M13 auxiliary mathematical Fourier model only, missing complete historical DTC0a runtime. No physical full 68921-site Gaussian noise measurement, SIX actual additional original Fourier sensing pairs, known C5 calibration derivatives or 107-million independent site snapshots. No physical NASH J3/K/TPE/GW/GR signal, global alpha inverse, minimax over arbitrary noninvariant tests or general Berry–Esseen theorem novelty.

Ask REC13/AUD3 independent bounded source review: (i) exact sign in Euler exponential-series mgf, (ii) nonidentically-distributed Berry–Esseen and infinite L2 limit, (iii) exact 12/e−2 third ABSOLUTE moment, (iv) zeta2/zeta3 integral bounds, (v) strict normal-CDF alternating remainder, (vi) original parent sharp weighted C5 gap, and (vii) the precise claim of 107m SUFFICIENT, not minimal and not actual. REC13/AUD3 acceptance and outside blind I3 NOT received; KN15 native BW ING receipt unverified. GitHub or Slack transport does not equal owner ACK, CANON, EXEC_SIGN. NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE.
