---
artifact_id: GEEKY-S11-ROT018-GUARD-LIE-NONCLOSURE-001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---
# ROT018 — source-helper mathematical composition counterexample

For the even-grid Fourier whole-mode Nyquist guard G of ROT016–017, the exact scalar norm of the commutator with smooth multiplication by cos(x) is 1/sqrt(2) for every even N>=6.

With the fixed smooth Lie generator C=(cos x,0,0), raw-k TT input carrier k=(N/2-1,1,0) and the standard source scalar filter E_alpha, the exact normalized discarded Nyquist-sideband amplitude is

R_bad=abs(1-4alpha)*sin(2pi/N)/(4pi/N)*sqrt(1+3t+t*t), t=1/((N/2-1)^2+1).

At fixed alpha=.05 this converges to .4. The strict repaired TT residual stays >=R_bad, whereas the original raw-k realcast source formal residual on the same input vanishes O(1/N). Original A is not idempotent and its residual is not a true TT leakage. At alpha=.25 this carrier is killed; NO all-alpha uniform claim.

Executed: 56 full 3D FFT tensor Lie/filter tests, 7 scalar guard fibre controls, 6 unchanged source-helper comparisons; PASS. Full report, standalone code, JSON and original SHA-pinned helper reside in local ZIP SHA256 1720f537b871d547767ff0a18bb0ef98e8fea794e7420273084d5e94bd3e53bb; clean unzip, 5/5 content digests, byte-identical rerun.

No historical production runner, physical NASH K/J3 or canon claim; referee and BW pending.
