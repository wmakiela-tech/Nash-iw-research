# MT13 Rotation 18 — Subfloor source-injection asymptotic mismatch
2026-10-11 | MT13 temporary Living Theory coverage | NONCANON / NO EXEC / NO NOVELTY.

Source: MECH-S6 Wu-Xu floor semantics https://docs.google.com/document/d/1as07oJ9r4z0i-TmYPPFAAjEq_PhiUHJ2i7bEWHhpYRc/edit ; LT3 DRAFT018 https://docs.google.com/document/d/1KorpE8IGJlPlDTkBcTs1WvMeepgff7Ga3qcpZP-wKuY/edit .

EXACT COUNTEREXAMPLE. For constants S>0, D>0, epsilon>0 and 0<n0<epsilon, the intended equation n_phys'=S-D*n_phys has solution n_phys(t)=S/D+(n0-S/D)exp(-Dt), hence tends to positive S/D. The log-floor executor evolves n_exec'=min(1,n_exec/epsilon)*S-D*n_exec. If 0<S<D*epsilon, its subfloor solution is n_exec(t)=n0 exp((S/epsilon-D)t), remains below epsilon, and tends to zero. Thus absolute asymptotic discrepancy tends to S/D and relative population error tends to 100 percent. The instantaneous DE population is S/D, unique, positive, and subfloor; the executor misses it asymptotically. This is an exact scalar constant-coefficient model result, not a claim about actual Wu-Xu parameter values.

THRESHOLD TRICHOTOMY: S<D epsilon => subfloor exponential decay to zero, though physical fixed point positive; S=D epsilon => every subfloor population is stationary under executor while physical equation drives toward epsilon; S>D epsilon => executor grows exponentially while subfloor and eventually exits the floor after log(epsilon/n0)/(S/epsilon-D). At threshold S=D epsilon, the executor has a continuum of subfloor stationary states; intended equation has unique equilibrium epsilon. For S>D epsilon, eventual floor exit does not guarantee small transient error.

FINITE-HORIZON WARNING: Asymptotic statements are not PBH/BBN time-window claims. Physical sources switch off; when S=0 both executor and intended have identical depletion law (though accumulated differences may remain). Actual floor activation and density units must be measured. In coupled multispecies evolution, rates and backgrounds differ, and the scalar comparison is only a local frozen-contract falsifier.

TYPED THREE-OBJECT SEPARATION: intended physical ODE vs actual floor executor vs DE algebraic closure. Frozen-root uniqueness and Picard convergence claims concern different mathematical objects. Source-native validation must log floor activation and injection residual deltaS=(1-min(1,n_exec/epsilon))*S before interpreting any DE-vs-full comparison. The scalar asymptotic failure is mature ODE analysis and cannot be promoted to new physical law.

PLACEMENT: DRAFT018 retained, P2/REV020_PLUS_COMPILER unchanged, P3 HOST_ATLAS_ONLY fallback, TPE HOLD. No PBH_B2 transfer, no Yp/DH endpoint bound, no canon.
