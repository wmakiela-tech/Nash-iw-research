---
artifact_id: IW_BADACZ_B1_RESULT_BRIEF_STD_A_V5_143_20261127
supersedes: IW_BADACZ_B1_RESULT_BRIEF_STD_A_V4_141_20261126
referee: REC15 ROT011 (H1 bounded PASS; H2 primary 3/3 PASS, secondary 2/3); REC15 ROT012 (v2 repairs confirmed); REC15 ROT015 (v3 bounded PASS, repairs in v4); REC15 ROT019 (v4 bounded PASS, remaining wording repairs applied in v5)
exposure: PUBLIC
origin_cell: BADACZ (Claude thread), B1 owner
created_at: 2026-11-27
document_type: RESULT_BRIEF_DRAFT v5 (B1 deliverable for 13 XII, 30-day protocol §B/§F)
decision_basis: Moderator 25 XI 14:57 (verbatim): „tak przyjmuję” — answer to: STD_A as the main B1 brief (shift and mechanism in the code model, no absolute thresholds), Q-B as a conditional section
language_note: English for preprint readiness; project working notes remain Polish
claim_ceiling: B1-SOURCE-VALIDATED-MATURE-APPLICATION candidate (proposed) / MODEL_CONDITIONAL / NO_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
open_gates: STOP A (HOLD; PREREG_129 non-admissible, REVIEW_132), STOP B (Y_P map), G_DEP; Q-B T3 semantics; referee of this brief outside the Claude family
sync_state: GITHUB_PENDING_BW_INGEST
---

# Clock–spectrum normalization in the public Wu–Xu PBH–BBN code: a similarity map of the threshold curve

*Draft v5. Every number below is a model-level result for the public code at commit d395183. None of them is a physical bound on primordial black holes.*

## Summary

*Scope note.* The protocol's original B1 question (regime distinction or a tighter reduction-error bound for the hadron history) is not answered here. This brief answers a narrower question accepted by the Moderator (25 XI). Novelty has not been demonstrated; that is not a demonstration that no novelty exists. Native six-hadron histories exist only at one frozen j22 point (Mech-S9 ROT013, 13 XI), which does not address the original question (Mech-S11 ROT031).

Wu & Xu (arXiv:2509.05618v3; JCAP 02 (2026) 063) derive BBN constraints on PBHs evaporating before nucleosynthesis and publish their code.
- **The mismatch.** The code evolves PBH mass with the geometric-optics loss rate of their Eq. 2.10. Its hadron injection rates, however, come from BlackHawk v2.3, whose spectra include greybody factors (Eq. 4.3, Fig. 2).
- **Size of the mismatch.** The two normalizations differ by a constant factor R = f_BH/f_code = 0.5817518 over 1 g – 1e10 g. The ideal coefficient-clock lifetime ratio is 1/R = 1.719; native lifetime ratios in the replicated runs are 1.718–1.725 (Mech-S11 ROT009). That factor is the known geometric-optics overestimate of the mass-loss rate (Baldes et al. 2020, App. A, quote a factor of about 2).
- **Measured shift.** Rescaling the code's mass-loss rate by R, with everything else unchanged, shifts the code's β threshold at the Y_code = 0.251 contour by Δ = −1.384 dex at M = 1.121e9 g and −0.244 dex at 3.494e9 g. It also creates threshold roots at 9.45e8–1.08e9 g, where the unmodified code has none in the sampled range.
- **Verification.** An independent native execution by a different model family reproduced all 56 parsed Y_code values and the corresponding shifts exactly (equal parsed binary64 values, not bytewise file identity); bounded referees passed it.
- **Mechanism.** The shift is a similarity map: log β_std(M) ≈ log β_base(M·R^(−1/3)) + c·log R. Here c ≈ 0.90–0.95 is approximately predicted from the code's own hadron-source table. Three precommitted, nonblind point predictions at new masses passed, and two of three final root brackets were fully contained. The map is conditional on an idealized clock and approximate source scaling; it is not an exact symmetry of the full network.
- **Status.** We claim the shift and its mechanism within the code. We claim no corrected physical bound: three open gates control the absolute thresholds.

## 1. Source and question
- Source: `fenyutanchan/primordial-black-hole` @ d395183, `arXiv-2509.05618/main-scan.jl` (blob b368ba55). Mass loss at line 80: `d_m_PBH_dt = -N_PBH * m_Pl^4 / m_PBH^2`, with N_BH = (27/4)·N_ρ(T_BH)/(30720π), the geometric-optics coefficient of Eq. 2.10.
- Hadron rates: table `hadrons_from_PBH.dat` (blob 06d0883a), 100 masses from 1e9 g upward, built from BlackHawk v2.3 PYTHIA BBN tables. Below 1e9 g the code extrapolates log-linearly from the first two rows (slope ≈ −1.20). The paper text instead prescribes an analytic T^1.3 law calibrated at 1e9 g.
- Question: by how much does the code's threshold curve move if the PBH clock is made consistent with the greybody-normalized spectra that set the hadron injection?

## 2. The normalization factor
- R = f_BH(M)/f_code(M) = 0.5817518, constant over 1 g – 1e10 g. Here f_BH is the BlackHawk v2.3 `fM.txt` mass-loss function; its SHA was matched independently by DAX ROT007, the code clock by M16 ROT011, and the operand N_BH (not n_PBH) by REC14 ROT014.
- BlackHawk's emitted spectra integrate to f_BH within about 1% inside the tabulated window (G_EC+(b), Badacz REVIEW_122; independent raw-table energy I1 by DAX-S10 ROT011, 140/140).
- Mature host: Page 1976; MacGibbon & Webber 1990; MacGibbon 1991; Cheek et al. 2022; Baldes et al. 2020, App. A (e_T = 7.6e−3 in geometric optics vs ẽ_T = 4.3e−3 with greybody factors). The factor itself is not new.

## 3. Measured shift (native, model-level)
Setup: the code's own solver and target Y_code = 0.251, with line 80 multiplied by R (operand STD_A). Grid log β ∈ {−21, …, −16}, bracket and bisection (PREREG_123).

| M [g] | base root | std root | Δ [dex] |
|---|---|---|---|
| 9.454e8 (j16) | none in [−21, −16] | −17.581 | — |
| 1.121e9 (j22) | −17.225 | −18.609 | −1.384 |
| 3.494e9 (j62) | −19.389 | −19.633 | −0.244 |

- **Robustness to the sub-1e9 g source continuation** (PREREG_125/REVIEW_126): with q_h ∝ M^s, s ∈ {−1.0, −1.3, −1.5}, Δ(j22) ranges over −1.430…−1.340 and Δ(j62) over −0.252…−0.239. The code's s = −1.20 lies inside.
- **Independent execution:** Mech-S11 ROT009 (different model family, native Julia, 56/56 calls, 5/5 gates) gives identical Δ to all digits. This verifies execution, not independent physics.
- **Null for H1 (declared before replication):** a different-family native replication differing by more than 0.03 dex at j16, j22 or j62. Not observed.
- **Bounded referee:** AUD4 ROT007 PASS, with interpolation-free brackets Δ(j22) ∈ [−1.4375, −1.3125] and Δ(j62) ∈ [−0.3125, −0.1875].
- Numerical root noise is 0.001–0.021 dex.

## 4. Mechanism: a similarity map
- **Relabeling.** If the loss rate is scaled by R, a PBH of mass M has the same lifetime and fractional mass history as an unmodified PBH of mass M′ = M·R^(−1/3).
- **Injection equivalence.** With β defined at formation (n_PBH/s ∝ β M^(−3/2)) and q_h ∝ M^(−a), equal hadron injection requires β_std = β_base·R^c with c = 1/2 + a/3.
- **Source-table value of c.** REC14 ROT016 evaluates the exact source-table expression and finds c_eff = 0.900–0.938 at the masses below. A continuous log-mass minimax over the source table gives a conditional common c ≈ 0.920 (first: M17 ROT002); an independent replay and extension across the three relabeled mass pairs and all five hadron channels finds maximum component discrepancy ≈ 0.005 dex (REC15 ROT014; binary64, not an interval certificate).
- **Null for H2 (frozen in DRAFT_127 §3):** two or more of the three point predictions outside their intervals. Not observed (0/3 outside).
- **Prospective test** (PREREG §3 of DRAFT_127, frozen before execution; nonblind; executed by Mech-S11 ROT012):

| M [g] | predicted interval | native std root | implied c |
|---|---|---|---|
| 1.474765e9 | [−19.274, −19.190] | −19.2219 | 0.907 |
| 2.133869e9 | [−19.566, −19.482] | −19.5222 | 0.943 |
| 6.464011e9 | [−19.632, −19.549] | −19.5870 | 0.936 |

- **Reading.** All three point predictions pass; two of three final brackets are fully contained in the predicted intervals. The implied c agree with the source-derived band within root noise; no single exact c fits all points (posthoc PCHIP fit gives c ≈ 0.905 at j22 and 1.027 at j62, REC14 ROT016). The large Δ at the left wall follows from the mass relabeling M′ = 1.198·M (equivalently, base mass reduced by 16.5%) acting on a steep wall, plus the factor R^c in β.
- **Figure 1** (`2026-11-25/data/fig_brief_137.png`, script `2026-11-25/code/figure_brief_137.py`, existing data only). Illustrative posthoc map using older base nodes from REVIEW_071 (a separate study, root method M_D; e.g. j22 −17.2212 vs the matched REVIEW_124 control −17.2251). STD_A roots are from REVIEW_124 and Mech-S11 ROT012. The PCHIP curve is a visualization, not a confidence band or a solver prediction. The narrow c-band [0.900, 0.938] is not the frozen prediction interval; one prospective root (2.13e9 g) lies 0.0013 dex outside the narrow band while inside its frozen interval. Shading denotes initial mass < 1e9 g only: every initial mass passes below 1e9 g during evaporation, so shading does not mark source support along the trajectory.
- **Cross-instrument check.** The independent linear-response instrument M16 ROT028 reproduces the scale of the continuation effect (−0.038 / −0.003 dex vs −0.039 / −0.003 dex natively).

## 5. What is not claimed (open gates)
- **STOP A, source below 1e9 g.** At j22, 81% of hadrons and about 99.998% of the frozen-background neutron response come from the extrapolated region (M16 ROT025). The shift Δ is insensitive to the continuation shape (§3), but absolute thresholds are not.
  - A preregistered attempt to replace the extrapolation with the authors' own PYTHIA generator scripts, extended to 2e6 GeV (PREREG_129/A1) and executed with the PYTHIA 8.318.3 Python binding rather than the authors' literal PYTHIA8.jl environment, was non-admissible. The per-event energy gate failed in 11/24 cells (2726/48000 events; maximum relative residual 4.15e−5; Mech-S11 ROT019, full independent replay PRF15 ROT013). The generator itself reported energy–momentum warnings and hadronization retries at PeV energies (REVIEW_132). A separate diagnostic found the recorded mismatch already present before hadronization (Mech-S11 ROT021/022/026), without identifying a causal subroutine.
  - Endpoint secants of the charged-pion multiplicity over 1e5–2e6 GeV are descriptive only: 0.285 ± 0.005 (u) and 0.288 ± 0.003 (g). They are close to the paper's T^1.3 prescription and above the code's effective 0.20.
  - Outside B1 (REVIEW_135; raw cross-family I1 by AUD4 ROT019, SCOPE13 ROT019 and Geeky-S14 ROT016): deficit and surplus failure events both carry 10–26% fewer, harder pions, and the surplus–deficit difference is not significant. This is compatible with failures tracking event topology. It does not establish equality: the 95% intervals for the surplus–deficit difference are wide, and a sign-independent, common-mode count error is not excluded. Accepted-event means are recorded generator output, not certified physical yields. A stage observer finds that 72/75 four-vector L1 failures (38/41 energy-only failures) are already present at the post-parton snapshot, before hadronization (Mech-S11 ROT026; I1 AUD4 ROT022). This localizes a snapshot, not a proven onset or a magnitude attribution: whether the residual first arises inside the parton level is not resolved, and later stages change magnitudes in both directions (Mech-S11 ROT027). None of this reopens STOP A.
  - STOP A therefore stays on HOLD.
- **STOP B, Y_P map.** Three helium readouts exist across the source versions: 2X/(1−2X) in JCAP/v1/v2, 2X/(1−X) in the public code, 2X in arXiv v3. Under the v3 map the first bracketed std wall node is 1.059e9 g, not 9.45e8 g (REC14 ROT015). No statement about the 1e9 g headline threshold is made.
- **G_DEP and network.** Energy deposition and a full-network transfer of the shift have not been certified.
- **Firstness.** Direction: EKS1 (DIR-010). Native measurements: Badacz REVIEW_120–126. Replication: Mech-S10/S11. Referees: REC14, AUD4.

## 6. Conditional section: charge-state normalization (Q-B)
- **Finding.** The code injects each BlackHawk group rate (π±, K±, p/p̄, n/n̄ summed over charge states) into every charge state separately (T1-GROUPED, Mech-S9).
- **Size.** Per-state normalization shifts the code's threshold by +0.272…+0.301 dex at six masses (REVIEW_071). A native replication by a different family matched it (Mech-S10 T2R, 68/68 bitwise). The shift survives network transfer at +0.26…+0.30 (REVIEW_084).
- **Open.** Whether the group convention was intended together with group-averaged rates is SEMANTICS_OPEN (T3). Mature host: per-state yields in Reno & Seckel 1988 and Bianco et al. 2026. The effect has the opposite sign to STD_A at j62, so the two must not be added.
- **Status.** Reproducibility finding, conditional on semantics.

## 7. Reproducibility
- Badacz public artifacts: research/badacz/2026-11-23 (PREREG_123/REVIEW_124, PREREG_125/REVIEW_126, MANIFEST_SHA256_116) and 2026-11-25 (128–137) and 2026-11-26 (138–142), 2026-11-27 (143–144). Raw evidence custody: Mech-S11 ROT029 STD_A capsule; KN18 ROT006/007 private archive of the j22 six-history and the ten STOP A raw ZIPs (Actions artifacts expire 2027-02-23).
- Mech-S11 public artifacts: research/mech-s11/2026-11-25, with GitHub Actions runs 45616230955 and 45620537732.
- Private referee and instrument reports (REC14, AUD4, M16, DAX, LT11) are cited by ID only.

## References
- Q.-f. Wu, X.-J. Xu, arXiv:2509.05618v3; JCAP 02 (2026) 063.
- D. N. Page, PRD 13 (1976) 198.
- J. H. MacGibbon, B. R. Webber, PRD 41 (1990) 3052.
- J. H. MacGibbon, PRD 44 (1991) 376.
- I. Baldes et al., JCAP 08 (2020) 045, arXiv:2004.14773.
- A. Cheek et al., PRD 105 (2022) 015022, arXiv:2107.00013.
- A. Arbey, J. Auffinger, EPJC 79 (2019) 693; EPJC 81 (2021) 910.
- M. H. Reno, D. Seckel, PRD 37 (1988) 3441.
- Bianco et al., arXiv:2605.26824.
- A. Boccia, F. Iocco, L. Visinelli, PRD 111 (2025) 063508, arXiv:2405.18493. An independent BBN treatment with a greybody clock but no nonthermal hadronic effects (XH-S9 ROT011).
- C. Keith, D. Hooper, N. Blinov, S. D. McDermott, PRD 102 (2020) 103512, arXiv:2006.03608.
- K. Kohri, J. Yokoyama, PRD 61 (2000) 023501, astro-ph/9908160.

## Next steps
1. Done: REC15 ROT011 (v1), ROT012 (v2), ROT015 (v3), ROT019 (v4); v5 applies the v4 wording repairs.
2. Fix the Badacz artifact locators to commits in §7.
3. B1 rows of the §F decision artifact: IW_BADACZ_B1_SECTION_F_ROWS_V3_144_20261127.
4. Not planned for B1: any further generator run (REVIEW_132 §3).

NO_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
