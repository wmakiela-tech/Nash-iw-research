# M14 ROT014 — three versus three Lorentz lines: finite-shot singularity
artifact_id: IW_M14_ROT014_XH5_THREE_VS_THREE_POISSON_COLLISION_001_20261029
date: 2026-10-29
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_CLASSICAL_SYNTHETIC_POISSON / NO_NOVELTY / NO_DEVICE_REPLAY / NO_CANON / NO_EXEC_SIGN
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09 / M14

OTHERS FIRST: XH-S5 ROT007 owns Schall et al 2026 physical NV 14N triple-Lorentz source and shot-noise limits (DOI 10.1038/s41467-026-78386-z). M14 ROT013 first owns exact 13-tone global uniqueness for <=3 distinct positive Lorentzians and 5-tone fold, full local ZIP SHA256 0de36b1821b345ee203ce64ee9aaea6459ab26f8ce89f95030c4b723c409a458, GitHub write previously BLOCKED. Classical Le Cam/Bhattacharyya and mixture singularity theory (Heinrich-Kahn 2015 arxiv1507.04313; Ho-Nguyen SIAM 2019 doi10.1137/18M122947X) are NOT our novelty. LT6 REV028 is WORKING, no adoption.

SOURCE CONTRACT: R(x)=beta-sum_{j=1}^3 gamma_j/((x-u_j)^2+v), 3 distinct means per hypothesis, positive amplitudes, shared v>0, beta>2g/v. Frozen u,delta>0, g>0, v, beta.
A atoms (u-delta/2,g/2),(u,g),(u+delta/2,g/2).
B atoms (u-delta,g/8),(u,7g/4),(u+delta,g/8).
All signal means >=m_min=beta-2g/v>0. Exact moments about u at orders 0,1,2,3 agree: (2g,0,g delta^2/4,0). Fourth moment differs by 3g delta^4/16. The unnormalized 1-Wasserstein distance between the two spectral amplitude measures is exactly g delta/2.

THEOREM 1 UNIFORM SIGNAL DIFFERENCE: With L_v(z)=1/(z^2+v), integral L_v(z)=v^{-1/2} int_0^infty exp(-sqrt(v)t)cos(zt)dt gives sup |L_v''''|<=24/v^3. Taylor through third order and the sum of fourth absolute moments yield for every real x:
|R_A(x)-R_B(x)| <= 5g delta^4/(16v^3).
At x=u exact nonzero gap R_B(u)-R_A(u)=-3g delta^4/[4v(v+delta^2)(4v+delta^2)]. Hence observed gap Theta(delta^4) while amplitude-mixture W1 is Theta(delta). No uniform inverse Holder exponent >1/4 for this nonseparated class.

THEOREM 2 POISSON LOWER TESTING BOUND: K arbitrary distinct or repeated fixed sample tones x_i; n independent spectral repetitions; counts Poisson(n*R_A(x_i)) vs Poisson(n*R_B(x_i)), independent across tones. Affinity BC=exp[-n/2 sum_i (sqrt(R_A)-sqrt(R_B))^2]. Let D=n sum_i(square-root gap)^2. Exact optimal equal-prior Bayes error P*_e=(1-TV)/2 >=[1-sqrt(1-exp(-D))]/2. Using means>=m_min and Theorem1,
D <= n K [5g/(16v^3)]^2 delta^8/(4m_min).
If RHS<=log(4/3), then P*_e>=1/4. Thus Ω(delta^-8) repeats NECESSARY for fixed K to test this positive 3-vs-3 pair at error <25%. This is NOT a general minimax rate for unknown nuisance. SHARPNESS FOR ORACLE SIMPLE TEST ONLY: at x=u gap is Theta(delta^4), so single-tone Hellinger exponent Theta(delta^8); affinity upper Bayes error <=BC/2 implies n=O(delta^-8) sufficient for fixed hypotheses.

EXACT RATIONAL SYNTHETIC INSTANCE beta=3,g=7/20,v=1/2,u=2/5, 13 tones x=-3+i/2, i=0..12; all global means >=8/5; sup gap <=(7/8)delta^4, D<=(3185/2048)n delta^8. delta=.2 and n=72259 certify minimum Bayes error >=.25 for ANY 13 fixed tone choices; for the stated grid high-precision sharper lower bound is .4650523472056. They are theoretical bounds, NOT measured error percentages nor device photon counts.

INDEPENDENT SOURCE-TYPED EXECUTION: stdlib Fraction 6 delta exact moments, W1, positivity and gap; independent mpmath65 8 delta Poisson affinity, threshold, center exact identity, oracle upper test. Clean isolated ZIP 7/7 payload SHA256, CRC, BOTH JSON byte-identical PASS. Full Polish proof+2 code+2 JSON+README+SHA in LOCAL Moderator ZIP, sha256 b542c4d0b29c8800f4b5728d877d7879fe0ea0dbcb3caa268bb4a08ae45fd794; NOT falsely claimed GitHub-hosted.

Hard limits: real 14N splitting and device amplitudes not this arbitrary shrinking-mixture source; actual correlation, calibration, technical noise and source data untested. NO_DEVICE_REPLAY / NO_NASH_KJ3 / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_PENDING / REFEREE_PENDING / NO_NEW_TASK_CASCADE.