# XH-S5 ROT003 — source-native Active Fourier Spectroscopy information-gain audit
artifact_id: IW_XH_S5_ROT003_AFS_INFORMATION_GAIN_MODEL_DISCRIMINATION_001_20261026
return_id: XH-S5-ROT003-AFS_TWO_BIN_MODEL_DISCRIMINATION_AND_SOURCE_EQUATION_AUDIT_20261026
exposure: PUBLIC
claim_ceiling: EXACT_CONDITIONAL_2BIN_GAUSSIAN_MIXTURE / NO_AUTHOR_REPLICATION / NO_NOVELTY / NO_NASH_PHYSICAL / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST

SOURCE: J. Schröder et al., arXiv:2505.14364v2 (2026-09-22), https://arxiv.org/html/2505.14364 ; APS Physical Review Research accepted 2026-10-23 DOI 10.1103/shq1-j249. Author original data/code NOT retrieved. This is an independently computed SOURCE-NATIVE TWO-BIN COSINE-OPERATOR toy, not reproduction of optical/medical experiments.

Using Eq.(1) F(tau)=S1*(1+cos tau)+S2*(1+cos 2tau)+N(0,0.01), the admissible delays tauA=pi/2 and tauB=pi give rows (1,0) and (0,2). Prior models K0/K1 each with 50% mass: mean S=(1,0.35) vs (1,0.65), common covariance diag(0.02,0.000025). The source's weighted *within-model* information-gain approximation (S3.4.3 Eq.59) selects A: I_within(A)=0.549306144334 nats vs B=0.004975165427. Full Eq.58 includes model discrimination: I_model(A)=0; I_model(B)=0.689108416861; hence I_full(A)=0.549306144334 and I_full(B)=0.694083582287, reversing the acquisition choice. Analytic Fano lower I_model(B)>=0.682434323599 and independent GH/QUAD agree. Source authors recognize the omitted term and qualify the approximation when model weights concentrate: no claim that their real AFS implementation fails or that this mathematics is novel.

TWO SOURCE MATH PATCHES, arXiv v2 only: (i) Eq.17 has positive sign for Sigma_new-Sigma_old, whereas Eq.16 requires NEGATIVE; rank Eq18 unaffected. (ii) prose after Eq.60 erroneously states pointwise posterior model entropy cannot increase; only its OBSERVATION-AVERAGED value cannot. With prior K probabilities (.9,.1) a scalar observation y=1.03698661371849 yields posterior (.5,.5), Hpost=0.69314718056>Hprior=0.325082973391, though expected posterior entropy falls to 0.002310535519; MI bound Eq61 is correct.

NASH two-surface prior art: XH-S4 rotation 027A OED and 030 source identifiability, XH-S5 ROT001 Yukawa nuisance, M14/MT14 OU already have related but DIFFERENT hosts. External mature Bayesian experimental design, model discrimination, Fano. No novelty priority.

FULL LOCAL MODERATOR PACKAGE: IW_XH_S5_ROT003_AFS_IG_SOURCE_AUDIT_REPRO_20261026.zip SHA256 b9e36faf98b8feb73feaedfca8d4f7d0af75d4cec1a2c08c029de1e1e7c9f624; contains independent source-native Python, deterministic JSON, report, manifest and README. ZIP CRC+per-file SHA+clean extracted source replay JSON byte-equal PASS. Python SHA256 3f60d33bd7b12a5fcf063208feaae5092e7d30d51b8ebe1550fc89647b6094d2. Full package is NOT automatically stored on GitHub, only this locator if commit succeeds. Owner/referee/BW/EXEC acceptance NOT assumed. No new cross-cell task.