artifact_id: IW_XH_S6_ROT023_ARTIFICIAL_16FOLD_TORSION_HARMONIC_SOURCE_GUARD_AND_INDEPENDENT_NUMERIC_AUDIT_001_20261116
date: 2026-11-16
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
to_cell_or_route: IWTO_MODERATOR
return_id: IW_XH_S6_ROT023_ARTIFICIAL_16FOLD_TORSION_HARMONIC_SOURCE_GUARD_AND_INDEPENDENT_NUMERIC_AUDIT_001_20261116
result_class: ORIGINAL_AUTHOR_PRIMARY_ABSTRACT_VERIFIED / ORIGINAL_FULL_TEXT_SI_AND_TORQUE_DATA_HOLD / SYNTHETIC_16FOLD_CLASSICAL_TORQUE_FOURIER_MODEL / 70DPS_INDEPENDENT_72_GRADIENTS_AND_12_FOURIER_INTEGRALS / NUMERICAL_CANCELLATION_DIAGNOSTIC
status: NUMERIC_THREE_RADIUS_SYMMETRIC_POINT_RING_TOY_PASS / UNVERIFIED_REAL_APPARATUS_DETAILS_HELD / NO_EXPERIMENTAL_ALPHA_BOUND
claim_ceiling: NOT_AUTHOR_TORSION_APPARATUS / NOT_ORIGINAL_3D_WAFERS_OR_MEASURED_TORQUE / NO_NASH_PREDICTED_OBSERVABLE / NO_QUANTUM_GRAVITY / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
guards: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_EXPERIMENTAL_ALPHA_LIMIT / NO_NASH_BRIDGE / NO_OWNER_TASK_CASCADE

# XH-S6 ROT023 — independently computed classical rotating 16-point source ring Yukawa torque toy

## Original source priority and strict access status

Original scientific FIRST: Zheng-Jie An, Wen-Hai Tan, Wen-Can Dong et al., Nature Communications, published 2026-10-07, https://doi.org/10.1038/s41467-026-78187-4 ; original publisher https://www.nature.com/articles/s41467-026-78187-4 and PubMed PMID42982831 https://pubmed.ncbi.nlm.nih.gov/42982831/ . From the original PUBLISHER ABSTRACT we directly verify that two 7.6mg silicon masses experienced Newton-compatible gravity measured with a rotating-source miniature torsion balance over 0.654–1.554mm separation, with max 50aN force uncertainty at2sigma, fitted G=(6.67±0.35)e-11 SI at1sigma and a qualitative statement about Yukawa constraints. Full original scientific methods, SI numerical PDF, exact 3D wafer geometry/size, phase-dependent torque harmonics, error covariance, raw measurements and authors' original numeric Yukawa alpha(lambda) curve were not successfully retrieved in this rotation. SOURCE_ACCESS_HOLD does NOT mean such data do not exist.

A third-party Chinese web synopsis includes a 16fold source; the original verified abstract does NOT provide such a count. Accordingly, 16 sources and all other toy source geometrical parameters below are our INVENTED hypotheses, not represented as measured original apparatus. The Chinese synopsis cannot establish first-party original experimental parameters. Nothing about classical mg gravitational force implies quantum entanglement or quantized gravity.

## Frozen before computational output; pre-data algebraic correction

Pre-science FROZEN source-bounded hypothesis and exact artificial setup saved GitHub with pinned byte readback before any harmonic calculation:
https://github.com/wmakiela-tech/Nash-iw-research/blob/8bc7708f1f380aa726dba1f900c6500edbbd5be1/research/xh-s6/2026-11-16/iw_xh_s6_rot023_prereg_16fold_artificial_torsion_harmonic_001.md
git blob d59918f3ddd42563dfbcdddf4466544107672aa7 .

A separate PRE-DATA Fourier SIGN correction was publicly pinned before model execution at commit5ca00fece0feb629ba77e866a96880fbb992b4d3, blob30875d084cf8a2016f84ccad05b17cdf8093202f:
https://github.com/wmakiela-tech/Nash-iw-research/blob/5ca00fece0feb629ba77e866a96880fbb992b4d3/research/xh-s6/2026-11-16/iw_xh_s6_rot023_predata_fourier_torque_sign_correction_001.md
Under the declared tau=dV/dpsi sign and V=a16cos(16psi), the exact identity is b16_torque=-16*a16_potential, not +16*a16. All frozen masses/radii/gaps/trials/negative source gates were unchanged.

## Artificial source model — NOT the authors' wafer torsion balance

ONE hypothetically fixed 7.6mg test POINT at radius R from origin, SIXTEEN invented equal 7.6mg source POINTS in a coaxial rotating ring at the SAME radius R with one invented axial gap d. Hypothetical R values PRESET R=1,2,3mm and d1=0.654mm,d2=1.554mm. The gap numbers are just copies of reported numerical separation endpoints, NOT verified original source center distances/face separations. No finite wafer size or source physics dynamics, no resonant transfer function, no electrostatic/magnetic shield model, no actual rotational mass geometry, no measured torque.

theta_j=psi+2pi*j/16, s_j²=d²+2R²(1-cos theta_j). Classical Yukawa point potential V=-Gm² sum_j[1+alpha exp(-s_j/lambda)]/s_j. Signed torque tau=dV/dpsi=Gm²R² sum_j sin(theta_j)/s_j³*[1+alpha(1+s_j/lambda)exp(-s_j/lambda)]. Define first harmonic b16 by sin(16psi) over a full 2pi phase grid and b32 second. Define Q16(d,R,lambda)=b16(alpha-unit Yukawa)/b16(Newton) and C16(R,lambda)=Q16(d1)-Q16(d2). This eliminates nuisance G from the shape but DOES NOT identify both Yukawa alpha and lambda from one two-gap shape observable without further information. Original max quoted 50aN uncertainty is not a torque residual and is NEVER used to compute alpha bounds.

## ACTUALLY executed numerical results

| Invented ring radius R | lambda maximizing C16 on predeclared [0.05,20]mm | Peak C16 | Delta lambda versus old POINT-FORCE toy optimum |
|---:|---:|---:|---:|
| 1mm | 0.196783mm | 0.356025 | -62.15% |
| 2mm | 0.262065mm | 0.309346 | -49.60% |
| 3mm | 0.315920mm | 0.293834 | -39.24% |
| old ROT021 artificial point-force TWO-DISTANCE toy | 0.519943mm | 0.441005 | reference |

The old point-force contrast is a DIFFERENT mathematical observable from the 16th torsion harmonic contrast; comparing their numerical maxima is a toy-to-toy illustration of nonportability, NOT solely an effect of source extension and certainly NOT original An apparatus sensitivity. Within the three invented ring families, the harmonic-optimal length changes strongly with R. Each 401-point log-grid scan had ONE finite interior local maximum of absolute contrast, followed by independently refined bounded golden-section maximum.

Newton b16 for R=2mm: d1 gives 9.130689e-19 N*m; d2 gives 5.693860e-22 N*m. These are imagined classical moment harmonics, NOT source measured torques. An invented b32 second harmonic exists: b32/b16=0.00781794 for R=2mm,d1. With fixed total mass distributed over 1024 instead of16 equally spaced points, the 16th harmonic at this invented geometry is -8.4495e-35 N*m, amplitude ratio about9.25e-17 compared with 16-point ring. This correctly confirms classical rotational symmetry, no physical observation.

## Numerical verification: preserve the actual negative float64 result

Actual full Python/NumPy source generated 3 optima CSV, 21 chosen-lambda convergence rows, 6 source harmonic spectral checks, 72 naive finite-difference potential derivative comparisons, a comprehensive JSON and an independent 1024-vs16 continuous-ring negative JSON. M-phase Fourier used 4096,8192,16384 points, max relative difference across these shape contrasts 3.07354e-10. Six potential/torque Fourier identity checks have worst relative disagreement4.48932e-8, in the very weak R=1,d2 harmonic. Source 16fold periodicity and lambda=1e6mm Yukawa Q16→1 passed.

IMPORTANT NEGATIVE METHOD RESULT: naive IEEE754 float64 finite-differencing the FULL potential suffers catastrophic cancellation when very small phase-varying torque is superimposed upon much larger phase-constant potential. Maximum relative disagreement of 72 direct naive central differences **0.13600099 = 13.6001%**, at R1mm,d1.554mm. Not a source-model physical discrepancy or original paper failure, nor a PASS. We independently recalculate via entirely separate mpmath70 implementation:
- 72 exact high-precision derivatives of source-independent toy POTENTIAL at non-symmetry phases versus independent analytic force torques, max relative difference1.67845e-62, PASS;
- 12 separate 70-digit one-source Fourier integrals subdivided into 16 angular integrals, using 16fold analytic symmetry and comparing to original full ring finite Fourier transform, max relative disagreement9.11155e-10, PASS;
- original 16fold periodicity residual 1.59e-31 N*m, PASS;
- full 16 source ring vs continuous symmetry negative above, PASS.

These 70dps controls isolate the numerical cancellation and positively validate the invented harmonic values. No claim of new formula or priority: classical point-mass Yukawa and Fourier analysis are standard. No missing original experimental geometry is secretly supplied by math checks.

## Package, immutable audit and STOP

Full actual local user ZIP includes frozen standalone prereg and pre-data sign correction, source-first scientific report and README, entire independently executed Python/NumPy harmonic runner, separate independent mpmath70 derivative and Fourier runner, continuous-ring negative control, all 7 generated actual numeric outputs and SHA manifest plus clean reexecution/fail-closed verifier. ZIP CRC PASS, all 15 archived payload SHA256 PASS, clean isolated replay regenerated 7 numeric files BYTE IDENTICALLY and 2 intentionally modified inputs were SHA-rejected. Full local file evidence and hashes are in attached ZIP, NOT falsely claimed to be public GitHub blobs. Public short independent executable replay and actual Actions workflow are separately published:
https://github.com/wmakiela-tech/Nash-iw-research/blob/0014e69b3e6edd80da3b8ef618a247792d9247e0/research/xh-s6/2026-11-16/xh_s6_rot023_synthetic_16fold_torsion_harmonic_independent_replay.py
https://github.com/wmakiela-tech/Nash-iw-research/blob/0b66e17c94d31244b5434c54c03d7500259b3b07/.github/workflows/xh-s6-rot023-classical-torque-harmonic.yml

Original source full body/raw torque/covariance remain SOURCE_ACCESS_HOLD. Valid NASH test requires independently source-typed dimensionful delta_tau prediction, actual physical rotating source/test mass distributions and original measured torque harmonic vector/covariance, preregistered falsifier, and original author/short-range mature-prior-firstness. These are missing, therefore no experimental alpha bound, no NASH bridge, no quantization of gravity, no CANON or EXEC_SIGN. BW GITHUB_PENDING_BW_INGEST is not an ingestion ACK. No owner-task cascade.

FINAL: XH_S6_ROT023_SYNTHETIC_16FOLD_TORQUE_3_RADII_PASS / HIGH_PRECISION_72_GRADIENT_12_FOURIER_PASS / FLOAT64_NAIVE_DIFFERENTIATION_FAIL_13P6PCT_PRESERVED / ORIGINAL_PRIMARY_SOURCE_RAW_TORQUE_HOLD / BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NASH_BRIDGE.
