---
artifact_id: GEEKY-S11-ROT020-TWO-STEP-GUARD-H2-001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---
# Geeky-S11 ROT020 — two-step Lie and Fourier guard placement

Previously ROT015-019: scalar Nyquist guard G repairs source raw-k reality compatibility, but one smooth Lie composition has threshold H1. Distinct ROT020: two Lie steps.

With fixed smooth C=(0,cos x,0), full centered three-term tensor Lie L, one E_alpha input filter and even N divisible by 8, define D=G L² E_alpha G -(G L G)² E_alpha G=G L(I-G)L E_alpha G.

Exact genuine raw-TT high-band witness has k=(N/2-1,m,0) with m=N/4 or N/8, polarization (vvT-ez ezT)/sqrt2 where v=(-m,N/2-1,0)/sqrt((N/2-1)^2+m²). The zz component is exact scalar advection. The normalized size of the returned formerly forbidden two-step Fourier route is |e_m(alpha)|[sin(2pi m/N)/h]²/4 with e_m=1-4alpha[cos²(pi/N)+sin²(pi m/N)].

For ALL REAL alpha and s>=0, ||D||_(Hs->L2) >= 0.0004230017324024966*(16/9)^s*N^(2-s). For bounded alpha, norm <=(1+12|alpha|)[N/(2pi)+2]^2[1+(N/2-1)^2]^(-s/2). Therefore fixed-alpha sharp order Theta(N^(2-s)); critical Sobolev index s=2. Buffered support avoids the defect exactly.

Actual 219/219 independent typed numerical controls PASS, including 60 full tensor 3D FFT, 30 all-alpha two-band, 120 Hs, 4 original retained auxiliary source-function comparisons and 5 buffered tests. Local full report, standalone executed code, source helper, 219-test JSON, stdout and SHA manifest in ZIP, SHA256 b6f6a28436bf90a35fdf0df058ea98929b82d9589e60b44bab1e3b7c14147bb1. CRC, SHA 6/6, CLEAN re-execution BYTE IDENTICAL PASS.

ONLY scalar whole-mode guard; not tensor TT B composition. Original DTC production bytes unavailable. No physical NASH K/J3 or masked puretrace KA, no novelty, independent referee and BW/EXEC pending.
