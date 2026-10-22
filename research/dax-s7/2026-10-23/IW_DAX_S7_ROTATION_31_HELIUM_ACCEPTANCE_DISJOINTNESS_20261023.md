# DAX-S7 rotation 31 — helium acceptance disjointness

Public Wu-Xu main-scan.jl uses Y_code=2X_n/(1-X_n) and chi2=((Y_code-0.245)/0.003)^2. Under the standard He-4 mass fraction approximation Y_std=2X_n, the acceptance intervals in X_n differ. For k sigma, code X_n in [(mu-k*sigma)/(2+mu-k*sigma),(mu+k*sigma)/(2+mu+k*sigma)], standard X_n in [(mu-k*sigma)/2,(mu+k*sigma)/2], mu=0.245 sigma=0.003.

1sigma: code [0.107939339875,0.110320284698] versus standard [0.121,0.124]. 3sigma: code [0.105545617174,0.112688553682] versus standard [0.118,0.127]. Thus even 3sigma X_n acceptance intervals are disjoint. This is exact algebra conditional on standard Yp convention, not a demonstrated change in PBH physical bounds or published paper results. To test actual parameter contours, load Yp_mat from scanning.jld2 and remap Y_std=2Y_code/(2+Y_code), chi2_std=((Y_std-0.245)/0.003)^2; chi2 alone loses deviation sign. NO_CANON / NO_EXEC_SIGN / NO_NOVELTY.
