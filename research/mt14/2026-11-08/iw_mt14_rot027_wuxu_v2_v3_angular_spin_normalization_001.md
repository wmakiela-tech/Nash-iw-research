---
artifact_id: IW_MT14_ROT027_WUXU_V2_V3_ANGULAR_SPIN_NORMALIZATION_001_20261108
created_at: 2026-11-08
origin_cell: IW_MT_SUCCESSOR_13 / MT14
exposure: PUBLIC_SAFE
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: MANUSCRIPT_SOURCE_MATH / NO_TEX_PDF_SOURCE_CERT / NO_JULIA10D / NO_PHYSICAL_FIG5_BETA / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# MT14 ROT027 — Wu–Xu arXiv v2 versus v3: two different formula failures and the same integrated neutron rate

SOURCE FIRST Wu–Xu [arXiv v2](https://arxiv.org/html/2509.05618v2) (December 30 2025) and [arXiv v3](https://arxiv.org/html/2509.05618v3) (May 6 2026); standard V−A and neutron decay physics. Mech-S8 ROT008 (Nov 5) FIRST explicit v3 B.6 vs B.9 falsifier, AUD1 ROT029 (Nov 6) FIRST independent primary HTML algebra audit, Badacz REVIEW049 (Nov 8) FIRST independent gamma-trace orientation: v3 B.6 wrong MASS SIGN and printed spin prefactor missing factor32. Neither MT14 priority nor a new physics claim. Original public Wu–Xu GitHub source at d395183674cace6c9906a8911bdeb7234ba4040d is a v2 source snapshot, not v3; original JCAP Fig5 producer unverified.

## DISTINCT mathematical delta this rotation

The original arXiv v2 Appendix B.6 literally states the all-four-spin averaged expression

    (32/16) GF² (gV²+3gA²) mp² (pe·pnu).

In the same outgoing four-momentum convention as arXiv v3 B.8, define E=Ee Enu and D=(pe_3vector·pnu_3vector), so pe·pnu=E−D. A direct leading nucleon-rest reduction of Lagrangian B.5 with 2×2 Pauli nucleon spins and the symmetric left-chiral leptonic tensor gives the **correct** spin sum

    SUM_spins |M|² = 32 GF² mp² [(gV²+3gA²) E + (gV²−gA²) D].

Spin-average over all four doublets/16 = 2 GF² mp² times the bracket. At this level v2 B.6 has the CORRECT prefactor 32/16, but the WRONG differential angular structure:

    Fv2=(gV²+3gA²)(E−D)
    Fcorrect=(gV²+3gA²)E+(gV²−gA²)D
    Fv2−Fcorrect=−2(gV²+gA²)D.

For D=|pe||pnu|cos(theta), integration over the COMPLETE cos(theta) range −1 to 1 makes this difference EXACTLY ZERO. So v2 can give the CORRECT total neutron decay rate despite a WRONG differential beta−antineutrino angular dependence. Do not extend this full-angle cancellation to detectors with angular cuts or to a differential observable.

At gV=1, gA=13/10, E=1, D=1/2:
Fcorrect=229/40=5.725; Fv2=607/200=3.035; difference −269/100. The v2 literal angular coefficient would be a=−1, compared with standard a=(gV²−gA²)/(gV²+3gA²)=−69/607=−0.1136738 at gA=1.3. The physically observed aSPECT reanalysis (Phys Rev Lett 132 (2024) 102501 DOI 10.1103/PhysRevLett.132.102501) gives a=−0.10402(82), strongly rejecting a=−1. No claims about the precision agreement of one arbitrary gA input with that data or effects of radiative corrections.

## arXiv v3: bracket and coefficient require separate verdicts

The printed v3 B.6 includes the plus sign at the mixed mass bilinear proportional to (gV²−gA²)mn mp(pe·pnu), whereas the original V−A trace requires a MINUS sign; this orientation is Badacz FIRST. Printed v3 B.9 contains the **CORRECT BRACKET** (gV²+3gA²)E+(gV²−gA²)D, but its overall prefactor GF²/16 is WRONG by a factor 32; actual all-four-spin average is 2GF². Calling the entire printed B.9 "correct" is inaccurate without the prefactor qualification. The v3 B.11 next step uses the correct GF² normalization and yields the expected integrated rate.

Independent MT14 calculations actually executed:
(1) exact two-component Pauli spin traces: Tr(I)=2, Tr(sig_i sig_j)=2 delta_ij, Tr(sig_i)=0. Symmetric V−A leptonic tensor gives L00=8(E+D), SUM Lii=8(3E−D). These independently derive correct bracket and coefficient 32.
(2) independent exact 4×4 Dirac traces in a CHIRAL gamma basis, not Badacz's basis or code. Three on-shell momentum witnesses, including one with EXACT four-momentum conservation pn=(39/2,0,0,0), pp=(19/2,−3,−3,−4), pe=(5,3,0,0), pnu=(5,0,3,4). Actual spin sum/GF²=5168046/5, exactly equal to 32 F_minus; wrong sign residual 161460. Unit-test masses are algebraic, not physical neutron/proton electron masses; this is a tensor identity, not physical event simulation.
(3) independent SciPy and 60-digit mpmath integrations of phase-space lambda0: 1.63609795600872932489..., difference 8.88e−16. With gp gnu ge=8, GA=1.3, GF=1.1663787e−5 GeV−2, hbar=6.582119569e−25 GeV*s, Eq. B.11 gives tau_approx=867.09800885 s. Literally using printed v3 B.9 without 32x compensation would yield 27747.13628 s, which is not the paper result. The preserved v2 source main-scan.jl blob b368ba55d5a493f7bc185909730f7fe5691f10d6 line71 uses (255/tau_n)*(12+6x+x²)/x⁵ with neutron decay separate, not a runtime evaluation of v3 B.6.

## What can and cannot be concluded

MATHEMATICAL STATUS: v2 differential-angular law FAIL; v2 integrated full-angle law PASS; v3 printed B.6 mass-sign FAIL; v3 B.9 BRACKET PASS but prefactor FAIL by 32; v3 B.11 total decay-rate normalization PASS. Source HTML arXiv v2 and v3 verified directly; TeX and PDF source typography unverified. Original JCAP print, v3 producing code, original Fig5 provenance and any physical E4/Yp/BBN/beta consequences remain **UNDETERMINED**. No revised observational PBH limit or new physics inferred. No source-author contact, no owner substitution, no external audit cascade.

Repro Moderator-local complete Polish ZIP MT14_ROT027_WuXu_v2_v3_Angular_Spin_Normalization_Math_Audit_20261108.zip SHA256 5f4631b0a78219da709dcda575be989e51ff5f568904ac09865e974097e82d7f, contains complete 11KB Polish proof, THREE independent Python checkers, three actual JSON results, README, 8-entry SHA256SUMS. ZIP CRC PASS, payload 8/8 SHA PASS, clean separate Python reruns 3/3 byte identical PASS. No code or raw sources from Badacz are copied. No native Julia or physical source re-execution.

REVIEW ROUTE: Mech-S8 owner for Wu–Xu, REC11 and AUD1 independently, Badacz attribution FIRST, KN13 BW custody, Moderator EXEC. MT15 NOT ACTIVATED.

STATUS: SOURCE_V2_V3_MATH_TYPED / V2_ANGULAR_DIFFERENCE_FULL_ANGLE_ZERO / V3_B6_SIGN_RECONFIRMED / V3_B9_COEFFICIENT_FACTOR32_RECONFIRMED / B11_RATE_PASS / PHYSICAL_FIG5_HOLD / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
