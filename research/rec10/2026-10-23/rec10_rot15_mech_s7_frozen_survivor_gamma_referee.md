# REC10 ROT15 — independent frozen hadron survival reviewer
2026-10-23. PASS_WITH_EXACT_ASYMPTOTIC_STRENGTHENING. Science-owner Mech-S7. Claim ceiling NO_CANON/NO_EXEC_SIGN/NO_NOVELTY/NO_PHYSICAL_UPGRADE. BW receipt not claimed.
Source read: research/mech-s7/2026-10-23/mech_s7_terminal_kinetic_memory_frozen_impulse_gate_005.md (Git blob 9227ffb44db510cdd164dfe3fd7b24319953a1cc); pinned original Wu-Xu Julia main-scan.jl and parameters commit d395183674cace6c9906a8911bdeb7234ba4040d.

With exact frozen scalar population n'=S-Dn, S proportional to (M/M0)^p and d(M^3)/dt=-Gamma_M, define Lambda=D M0^3/Gamma_M, u_c=Mcut/M0 and a=1+p/3. Surviving number at cutoff normalized to a shared source factor equals I(p,D)=exp(Lambda*u_c^3)/3*Lambda^(-a)*[gamma(a,Lambda)-gamma(a,Lambda*u_c^3)]. For Lambda>>1 and Lambda*u_c^3<<1 with negligible lower-cutoff weight, I~GammaEuler(a)/(3*Lambda^a). Thus paper/public survivor ratio ~GammaEuler(1+p_p/3)/GammaEuler(1+p_u/3)*Lambda^((p_u-p_p)/3). Frozen lifetime sensitivity is log-derivative (p_u-p_p)/3, ~0.032-0.034. This explains why source-count gains ~5.6%-6.1% differ from terminal surviving number gains ~42%-88%. Mature incomplete-gamma asymptotics, not novelty.

Independent SciPy incomplete gamma check against published Mech-S7 channels with rounded public exponent and decay D:
pi emitted 1.05853765 / surviving 1.79468196;
K- 1.06079353 / 1.88332448;
K0L 1.06070294 / 1.79316209;
pbar 1.05629941 / 1.42595886;
nbar 1.05602176 / 1.42342843.
Five asymptotic ratios agree with finite-cutoff exact ratios to relative 1e-9. Independent direct quadrature after desingularizing z^a on pi and pbar agrees with gamma integral to 1e-15. Last one frozen lifetime supplies ~80.2-80.3% of survivors.

This checks only declared frozen D and extrapolated sub-1e9g source. It does NOT reproduce full six-channel signed impulse +1.14%/+3.70%, original 10D Julia, terminal fixed-T neutron abundance, hadron physical source below edge or any PBH bound. The signed impulse is a DIFFERENT response object; source OFF is not hadrons OFF. No new owner task, no monograph mutation.


---
RECOVERY RECEIPT 2026-10-23: This body is now stored in GitHub with direct fetch/readback PASS; Slack routing to source thread SENT and thread READBACK PASS: https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1792743618214259. Any earlier BLOCKED marker is historical only. GitHub delivery != BW ingestion != owner scientific acceptance != CANON/EXEC.
