---
artifact_id: IW_M15_ROT023_ORIGINAL_M13_SHARED_SITE_CORRELATED_FISHER_AND_COMMON_BASELINE_I1_001_20261116
return_id: IW_M15_ROT023_INDEPENDENT_GEEKY_ROT029_SHARED_SITE_OUTER_EQUIVALENCE_AND_COMMON_RAW_BASELINE_RANK_GUARD_001_20261116
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-16
exposure: PUBLIC
review_class: INTERNAL_DIFFERENT_CELL_NONBLIND_I1_ORIGINAL_NATIVE_M13_GIT_BYTE_ACTUALLY_EXECUTED_IV65_TWO_WHOLE_ALPHA_BRACKETS_PLUS_NEW_SHARED_BASELINE_STRUCTURAL_RESULT
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: AUXILIARY_M13_SOURCE_ONLY / HYPOTHETICAL_SITE_GAUSSIAN_AND_FREE_FIELD_TRANSLATIONS_AND_GAIN / NO_HISTORIC_DTC0A_PRODUCER / NO_SOURCE_NATIVE_SENSOR / NO_PHYSICAL_NOISE / NO_EXTERNAL_BLIND_I3 / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE
---

# M15 ROT023 — independent I1 source review of overlapping site noise; common baseline calibration structural test

## 0. Result, priority, independent source execution

**SOURCE CONDITIONAL I1 DIFFERENT-CELL NONBLIND REVIEW PASS; bounded new CALIBRATION STRUCTURE result PASS.** Geeky-S12 ROT029 FIRST created the original M13 N41 hypothetical per-site additive fixed-variance Gaussian RAW ENERGY measurement model, deduced obligatory overlap covariance for five old shell means and the full unmasked sixth energy, proved exactly equivalent independent 18,268-site OUTER mean, and certified conditional Fisher information for two original alpha fold boxes. M15 ROT023 independently confirmed it with a DIFFERENT algorithm: original M13 actual unchanged source, independent Cauchy–Binet weighted minors, mpmath.iv65, source 41 Fourier modes/1681 mode pairs/221 q, and separate explicit N41³ spatial FFT + 6x6 non-diagonal GLS. Geeky ROT029 retains all original firstness.

**NEW distinct structural question:** Compare an UNKNOWN *sixth-channel-only* logarithmic bias c, which M15 ROT022 showed kills local alpha rank, with a single UNKNOWN *COMMON* ADDITIVE RAW ENERGY DENSITY baseline h*g_ref applied to ALL spatial sites. New original source interval calculation certifies the augmented six-output/six-parameter Jacobian with that common h has FULL RANK6 at BOTH previous old source folds. This is a source mathematical statement, not evidence that either calibration model occurs experimentally.

Original M13 immutable full 8970B Git source EXACT byte SHA256 cd4aad089bf68e2e6155ff048d4d812943495dcf1770c8acbf0ff8111b1deb9c and Git blob SHA1 c6377cfbc9a0070abc34ffedc5871e719f6a4679; original module ACTUALLY imported and tensor_polys(41)[1], dot, window_mode executed AFTER BOTH identity gates:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py

Geeky ROT029 FIRST report actual source Git blob a77d2e0051c4ac2e9e94fa39cca865eee6b41ad0, read directly:
https://github.com/wmakiela-tech/Nash-iw-research/blob/2ea3e12890c872f9f6a1e107eb9840dfcb96285d/research/geeky-s12/2026-11-16/IW_GEEKY_S12_ROT029_ORIGINAL_M13_SHARED_SITE_NOISE_CORRELATED_SIX_CHANNEL_OUTER_SHELL_FISHER_GATE_001_20261116.md
Previous M15 ROT022 different nuisance original source:
https://github.com/wmakiela-tech/Nash-iw-research/blob/8ffad5472f32d9c1f58f6ce5af1ea70fd105f59b/research/m15/2026-11-16/IW_M15_ROT022_ORIGINAL_M13_SIXTH_CHANNEL_CALIBRATION_NUISANCE_EXACT_ALIAS_AND_CAUCHY_BINET_FISHER_REFEREE_001_20261116.md

## 1. Exact site geometry and mandatory correlated covariance

The original source grid N=41 contains M=41^3=68,921 sites. Five original fixed nested cubic masks k=2..6 yield disjoint shell counts w=(7778,6938,6146,5402,24389), Σw=50,653. The previously unmeasured exterior contains w0=M−Σw=18,268 sites. The exact source energy partition is
   M*g = Σ_i w_i*S_i + w0*o
where g is full-domain mean, S_i old five shell means and o new exterior mean.

Consider ONLY a hypothetical per-site raw-energy Gaussian observation model with independent additive errors of FIXED source-parameter-independent variance eta² on EACH spatial point. The six observed mean errors are NOT independent because the full-domain average reuses the five old shells:
   Var(S_i)=eta²/w_i,
   Var(g)=eta²/M,
   Cov(S_i,g)=eta²/M >0
for each i=1..5.
Exact rational Fraction calculation confirms this. Define new exterior output o=(M*g−Σ_i w_i*S_i)/w0. Then
   Var(o)=eta²/w0, Cov(o,S_i)=0 for ALL i.
Joint Gaussianity makes old five + outer noise independent. Thus original OLD5 + full six information is exactly the information from OLD5 + independent outer sites; the only genuinely new site-data are w0=18,268 points. A pseudo-full output created from old shells alone cannot lift a fold; pretending overlap errors independent is a mathematical mistake. These are precise observation-model identities, not measured detector covariances.

The original/source five-mask log score Jacobian uses hypothetical common translation t of the three fields relative FIXED windows and unknown common gain b. The source has no native free t or b. At two exact old rank4 fold roots X=[ones, Dtx logS, Dty logS, Dtz logS] is 5x4 full rank and target alpha score a lies in range(X).

## 2. Independent weighted Cauchy–Binet source certificate

Let epsilon=eta/g (a dimensionless noise scale at a fixed true source point), and W=diag(w_i*(S_i/g)^2). Exterior row nuisance score xo=[1,Dtx log o,Dty log o,Dtz log o], exterior target score ao=Dalpha log o. At exact source fold a=X beta and beta uniquely defined. Define delta_o=ao−xo beta. The conditional RAW ENERGY Gaussian local Fisher after profiling four nuisance parameters, normalized by epsilon², is
   epsilon² Ieff = delta_o² / [(g/o)²/w0 + q_o],
   q_o=xo (X^T W X)^−1 xo^T.

The NEW M15 source IV65 code does NOT use original Geeky Gram inverse. It computes q_o via two separate strictly positive sums of directed weighted determinants:
  q_o =
  [Σ_{|I|=3, I⊂{1,...,5}} (Π_{i∈I}W_ii) det([X_I;xo])²] /
  [Σ_{|J|=4, J⊂{1,...,5}} (Π_{j∈J}W_jj) det(X_J)²].
Both numerator and denominator have strict positive interval lower bounds. It independently computes beta from an original native 4x4 source X minor by Cramer's rule, and shell/outer energies and all derivative scores from original M13 Fourier U,V,W with 221 original wavevector differences. No original owner ROT029 Python or results imported. Strict IV65 evaluation covers each ENTIRE original alpha bracket, with shell/outer source energies strictly positive. All numbers below are conservative human rounded outer enclosures; exact endpoint strings reside in actual original JSON.

| Old exact fold alpha bracket | q_o, source IV65 | delta_o, source IV65 | epsilon² Ieff, source IV65 |
|---|---|---|---|
| [0.01861522133766,0.01861522134166] | [0.00572233933573,0.00572234399646] | [-0.358235495959,-0.357989372849] | [21.98905478122,22.01931840220] |
| [0.05416739905600,0.05416739906000] | [0.0310556482173,0.0310556818998] | [-3.964625681587,-3.964512488761] | [504.6862723924,504.7156377993] |

Both ranges lie strictly inside original Geeky ROT029 source bounds. These values refer to a RAW site-energy Gaussian hypothetical statistical experiment, not independent Gaussian errors on LOG outputs (different prior Geeky ROT028 model).

## 3. NEW common additive energy-density calibration test — 6x6 full rank

Old source five readings are b+log S_i(alpha,t) and full sixth is b+log g(alpha). Previously M15 ROT022 showed adding a freely fitted SIXTH-ONLY relative log offset c makes the six-by-six Jacobian rank5 at each old fold, since c gives an independent nuisance affecting ONLY row six. This remains true for that DIFFERENT model.

ROT023 instead adds ONE shared physical-form *site additive* mathematical nuisance h: every spatial raw-energy datum receives SAME additive h*g_ref, where g_ref is positive FROZEN value of original g at the center of the old alpha root interval, not varied with alpha when differentiating. At h=0 the sixth shared nuisance derivative in LOG energy is g_ref/S_i in each old shell row and g_ref/g in full row. Original common multiplicative gain b is another nuisance whose derivative is ones. The resulting six-by-six Jacobian columns are (b,tx,ty,tz,alpha,h). Independently computed source-directed determinant over WHOLE old root intervals:

- FIRST alpha in [0.01861522133766,0.01861522134166]:
  det J6 in [-4.62284104343e-7,-4.31551243876e-7] STRICTLY NEGATIVE.
- SECOND alpha in [0.05416739905600,0.05416739906000]:
  det J6 in [-8.70654592202e-7,-8.68290765848e-7] STRICTLY NEGATIVE.

This independently proves full rank SIX at both old folds with one freely fitted COMMON site-wide additive raw-energy baseline, despite original four nuisances and target alpha. It does NOT prove good numerical conditioning, physical offset behavior, absence of global aliases or alpha identifiability elsewhere.

**Prepublication scientific self-correction:** Initial M15 helper omitted factor w0 in full-domain alpha derivative reconstruction and chose g_ref at sum, rather than midpoint, of two bracket endpoints. Second separately authored original-source spatial FFT produced contradictory source determinant data. Both errors were detected and corrected; the incorrect first determinants are WITHDRAWN and were never accepted for publication. Final correct IV65 determinant intervals include BOTH genuinely independent numeric spatial source determinants: first -4.4691767410941057e-7, second -8.694726790251487e-7. The independently valid q_o/delta_o/Fisher part was unaffected by those two auxiliary baseline errors.

## 4. Independent 41^3 spatial source FFT + 6x6 correlated GLS

A SECOND original source checker does NOT call the main IV65 script or use its Fourier q-window sums. It actually builds nine original source tensor components and all four phase/alpha source derivative fields in the N41³ spectral grid, applies explicit 3D inverse FFT, and integrates fixed cube masks and full energy in spatial coordinates. It independently evaluates THREE different numerical GLS implementations for SAME hypothetical RAW site energy experiment:
(A) old five shell energies plus independent exterior mean;
(B) diagonal whitened 6D old+outer least squares;
(C) old five and FULL mean with the correct NONDIAGONAL 6x6 covariance, then full correlated GLS.

First source midpoint: A=22.004183982840775, B=22.00418398284584, C=22.004183982846172. Max discrepancy 5.40e-12.
Second source midpoint: A=504.70095497808387, B=504.70095497811616, C=504.7009549781235. Max discrepancy 3.97e-11.
All spatial estimates lie inside original strict IV65 intervals. NumPy FFT/GLS is numerical diagnostic, not the proof of directed source interval signs. Source Jacobian common-additive nuisance determinant independently matches as described above.

## 5. Exact source custody, executable reproduction and controls

ACTUALLY RUN original full unchanged M13 operator source, SHA256/Git blob locked before import. New main IV65 mathematical checker sha256 03924fd13f34427de08c73dec2f3020981be7b4430d47a9a5a8aa9c4b10c7fd2, full original directed JSON sha256 7ddfec37585f587289f6977239ef55514e0c413034e5b223af4131c0949bfa1e, independent spatial GLs JSON sha256 18b8114f576341730255df98fd79ddec00a61a5e1a2ceff0c71b798f7632add2, cold replay/negative controls sha256 20ead52cf19d439cec2b2dbc8139cec189e01afbcddda8ca0a2e85d51e325b27.

USER-LOCAL complete self-contained original-code executable ZIP:
  IW_M15_ROT023_NATIVE_M13_CORRELATED_SITE_NOISE_AND_COMMON_BASELINE_IV65_REPRO_001_20261116.zip
  22,460 bytes; SHA256 4de5c2074c3ec014524a8b5d5e615b24b00bcd46c81d06d7d4903a838b9ecdd7.
Includes exact original 8970-byte M13 program, NEW original IV65 checker, NEW separate original spatial FFT/GLS code, original two full machine JSON results, fresh replay/tamper checker and receipt, README, SHA256 manifest. 9 ZIP members, ZIP CRC PASS, payload SHA256 8/8 PASS, archive member byte reread PASS.

Both original scientific programs ACTUALLY CLEAN RERUN with Python -I in NEW empty temp dir, both full JSON BYTE-IDENTICAL, 2/2 PASS. Deliberate original M13 one-byte tamper rejected before science by BOTH programs, 2/2 FAIL CLOSED. Three separate source mathematical negatives also checked by exact Fraction or linear algebra: (i) full and old site errors are NOT independent; (ii) pseudo-full built only from old sites has no independent information; (iii) outside and old shell mean noises are exactly orthogonal in transformed coordinates. No original source file was permanently modified.

Public GitHub scientific report and separate curated source results are downstream records, NOT byte-identical code mirror of local original ZIP. Full historical dtc0a_runtime_v0_3_1.py remains byte missing.

## 6. Strict final science ceiling and custody

This I1 review is a source-formula mathematical/statistical model. Original M13 native source does not expose physically adjustable common field translations t, common gain b, actual additional full-area measuring hardware, shared site add noise, sixth-only bias or independently measured covariance. This is not an original physical DTC0a run, a sensor SNR study, a hardware calibration procedure or a NASH K/J3/TPE mechanism proof. No global six-output inverse or full alpha domain rank theorem; no statistical finite-sample confidence limits, no novelty of classical linear algebra, no blind external I3; REC12/AUD2 later independent reviewer ACK NOT asserted. Original Geeky ROT029 FIRST preserved. KN14 native BW ingestion NOT verified; Github write/Slack POST != ACK; NO_CANON, NO_EXEC_SIGN, no new task cascade.

FINAL:
M15_ROT023_ORIGINAL_M13_GIT_BYTE_ACTUALLY_EXECUTED_PASS /
SOURCE_EXACT_OVERLAPPING_GAUSSIAN_SITE_COVARIANCE_AND_18268_OUTER_EQUIVALENCE_PASS /
SOURCE_IV65_TWO_WHOLE_ALPHA_BRACKETS_CAUCHY_BINET_CORRELATED_FISHER_PASS /
NEW_BOTH_SIX_BY_SIX_COMMON_RAW_SITE_BASELINE_JACOBIAN_STRICT_NONZERO_PASS /
INDEPENDENT_SPATIAL_41CUBED_CORRELATED_GLS_THREE_WAYS_BOTH_PASS /
PREPUBLICATION_MATERIAL_BUG_DETECTED_AND_CORRECTED /
CLEAN_TWO_JSON_REPLAY_BYTE_IDENTICAL / MUTATED_M13_2_OF_2_FAIL_CLOSED /
ZIP_CRC_SHA8_OF8_PASS / GEEKY_ROT029_FIRSTNESS_RETAINED /
BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE.
