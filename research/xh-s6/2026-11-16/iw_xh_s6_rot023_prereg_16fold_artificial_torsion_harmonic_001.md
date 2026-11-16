artifact_id: IW_XH_S6_ROT023_FROZEN_16FOLD_SYNTHETIC_TORSION_YUKAWA_HARMONIC_001_20261116
date: 2026-11-16
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
status: FROZEN_BEFORE_NUMERICAL_HARMONIC_COMPUTATION
claim_ceiling: HYPOTHETICAL_POINT_RING_AND_TEST_MASS / NOT_AN_ET_AL_REAL_APPARATUS / NO_EXPERIMENTAL_ALPHA_LIMIT / NO_NASH_BRIDGE
guards: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_EXPERIMENTAL_ALPHA_LIMIT / NO_NASH_BRIDGE / NO_OWNER_TASK_CASCADE

# ROT023 frozen prospective synthetic 16-fold source-ring torque harmonic

Original science FIRST: Zheng-Jie An et al., Nature Communications published 2026-10-07, DOI https://doi.org/10.1038/s41467-026-78187-4. Verified first-party abstract reports 7.6 mg silicon objects, rotating mass modulation and 0.654–1.554 mm separations, Newtonian gravity agreement, no quantum entanglement detection. Full text, apparatus three-dimensional geometry, SI, measured torque harmonics and covariance were not retrieved. A secondary Chinese synopsis suggests a 16fold pattern, but it is NOT verified as original-source apparatus metadata. This experiment explicitly invents its whole geometry and makes no claim of actual source or torque reproduction.

BEFORE NEW TOY DATA freeze:
- One imaginary 7.6mg TEST POINT mass at horizontal radius R from torsion pivot and one invented ring of 16 POINT source masses, EACH also 7.6mg, equally spaced around same radius R and displaced axially by d, with continuous rotation phase psi. Hypothetical R in {1,2,3}mm; invented plane gaps d1=0.654mm and d2=1.554mm numeric copies of abstract endpoints, NOT verified author ring radii, wafer shape, physical source separation/center-to-center gaps or number of real masses.
- Pair point distances s_j=sqrt(d²+2R²[1-cos(psi+2pi*j/16)]). Newton+Yukawa point potential V=-Gm_t m_s sum_j [1+alpha exp(-s_j/lambda)]/s_j.
- Signed torque on test about pivot tau_z=dV/dpsi=Gm_t m_s R² sum_j sin(theta_j)/s_j³ [1+alpha(1+s_j/lambda)exp(-s_j/lambda)], theta_j=psi+2pi*j/16.
- Signed sine Fourier coefficient b16=(2/M)sum_{psi grid} tau_z sin(16psi), and b32 second harmonic. Separate Newton coefficient b_N and alpha-unit Yukawa coefficient b_Y and define toy harmonic ratio Q16(d,R,lambda)=b_Y/b_N. Two-gap normalization-independent shape C16=Q16(d1,R,lambda)-Q16(d2,R,lambda), no experimental interpretation.
- Sweep lambda={0.1,0.2,0.5,1,2,5,10}mm and numerically seek maximizing ABS(C16) in prereg domain 0.05..20mm for all R. Test that maximizer is interior and compare toy ROT021 point-force lambda*=0.519942582943222mm. Do not force a maximizer or pass if function nonunimodal/cancellation.
- Three independent phase grids M={4096,8192,16384}; verify exact Fourier 16fold phase symmetry, finite nonzero signal / cancellation stability, zero DC torque, Newton harmonic sign, +16*potential cosine Fourier coefficient relation tau=dV/dpsi, potential finite difference derivative on 12 phases, lambda->infinity Yukawa Q->1, source phase-continuum asymptotic zero torque. At least one nonzero second harmonic b32 relative b16 to distinguish waveform from pure sinusoid. Record failures if any.

This is an independent classical Newton/Yukawa TOY mathematics and algorithm audit, NOT source native An apparatus or measured signal, NOT a quantitative paper Yukawa alpha exclusion or NASH physics comparison. The original quoted 50aN is measurement uncertainty, not a residual usable to limit toy alpha. Without source geometry, measured torque channel and NASH dimensionful predeclared delta_tau, bridge remains HOLD. NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_EXPERIMENTAL_ALPHA_LIMIT / NO_NASH_BRIDGE / NO_OWNER_TASK_CASCADE.
