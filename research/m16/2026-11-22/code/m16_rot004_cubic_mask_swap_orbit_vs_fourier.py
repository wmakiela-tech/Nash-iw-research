#!/usr/bin/env python3
"""M16 ROT004: cubic-mask permutation alias and four-Fourier-mode escape.

SOURCE firstness:
 M13 ROT29/ROT31 five nested RMS nonmaps;
 Geeky-S12 ROT038 rational anisotropic synthetic Gaussian site-noise B;
 Geeky-S13 ROT007/009 four hypothetical Fourier powers and cross ratio.

This script checks a DISTINCT observation interface: FIVE QUADRATIC MASKED
ENERGIES OF SYNTHETIC NOISE X_v, not original M13 tensor source RMS measurements.
Full 41^3 site-Gaussian FFT draws are actual synthetic calculations.
No observed physical instrument, no general novelty, no CANON / EXEC_SIGN.
"""
import json
import numpy as np
import mpmath as mp

N=41
SEED=74131
TRIALS=20
# (beta0,betax,betay,betaz,betaxy,betaxz,betayz,betabody)
B=np.array([1.,1/20,3/100,1/25,1/30,13/300,7/300,2/25])
B_SWAP=B[[0,2,1,3,4,6,5,7]]
assert abs(np.sum(B[1:])-0.3)<1e-14
assert abs(np.sum(B_SWAP[1:])-0.3)<1e-14

mp.mp.dps=65
cp=lambda j:mp.cos(2*mp.pi*j/N)
vx=lambda z:mp.mpf(82)/75+mp.mpf(31)*z/150
vy=lambda z:mp.mpf(17)/15+z/6
delta=mp.log(vx(cp(7))/vy(cp(7)))-mp.log(vx(cp(20))/vy(cp(20)))
assert delta>0
z=mp.exp(delta)
# Exact closed CDF of W = Logistic(0,1) + Logistic(0,1)
Fw=z*(z-1-delta)/(z-1)**2
assert Fw>mp.mpf('0.5')

k=np.arange(N)
cs=np.cos(2*np.pi*k/N)
cx,cy,cz=cs[:,None,None],cs[None,:,None],cs[None,None,:]
def spectral(b):
    return (b[0]+b[1]*cx+b[2]*cy+b[3]*cz+b[4]*cx*cy+
            b[5]*cx*cz+b[6]*cy*cz+b[7]*cx*cy*cz)
s=spectral(B)
s_swap=spectral(B_SWAP)
assert np.min(s)>0.7-1e-14 and np.min(s_swap)>0.7-1e-14
assert np.max(np.abs(s_swap-np.swapaxes(s,0,1)))<2e-15

rng=np.random.default_rng(SEED)
max_mask_abs=0.
max_logc_opposition=0.
abs_diffs=[]
for _ in range(TRIALS):
    g=rng.standard_normal((N,N,N))
    # C_B^{1/2} g via full 3D FFT of nearest-neighbor SPD covariance.
    X=np.fft.ifftn(np.fft.fftn(g)*np.sqrt(s)).real
    X_swap=np.swapaxes(X,0,1)
    m=np.array([np.mean(X[t:N-t,t:N-t,t:N-t]**2) for t in range(2,7)])
    m_swap=np.array([np.mean(X_swap[t:N-t,t:N-t,t:N-t]**2) for t in range(2,7)])
    max_mask_abs=max(max_mask_abs,float(np.max(abs(m-m_swap))))
    def log_cross(field):
        ft=np.fft.fftn(field)
        def lp(idx):return np.log(np.abs(ft[idx])**2)
        return (lp((20,0,0))+lp((0,7,0))-
                lp((0,20,0))-lp((7,0,0)))
    C=log_cross(X)
    C_swap=log_cross(X_swap)
    max_logc_opposition=max(max_logc_opposition,abs(C+C_swap))
    abs_diffs.append(abs(C-C_swap))
assert max_mask_abs < 1e-14
assert max_logc_opposition < 2e-13
assert max(abs_diffs)>0.1 # NEGATIVE CONTROL: RAW Fourier statistic not invariant.

print(json.dumps({
    "return_id":"IW_M16_ROT004_SWAP_ORBIT_CUBIC_MASK_QUADRATIC_NO_GO",
    "N":N,"N3":N**3,
    "source_B_coefficients":B.tolist(),
    "source_B_swapped_coefficients":B_SWAP.tolist(),
    "analytic_min_eigenvalue_bound":0.7,
    "actual_grid_min_eigenvalue":float(np.min(s)),
    "Delta_mp65":mp.nstr(delta,62),
    "P_correct_single_snapshot_Fourier_sign_exact":mp.nstr(Fw,50),
    "mask_experiment_theorem":"L(M_2..M_6 | B) == L(M_2..M_6 | B_swap), any n",
    "four_mode_theorem":"Z_B =_d W-Delta; Z_Bswap =_d W+Delta",
    "gaussian_noise_only_not_original_tensor_norms":True,
    "simulation_trials":TRIALS,
    "max_abs_mask_energy_difference":max_mask_abs,
    "max_abs_logC_B_plus_logC_Bswap":max_logc_opposition,
    "max_abs_distinct_fourier_logC":max(abs_diffs),
    "code_check":"PASS",
    "scientific_limits":"NO_PHYSICAL_SENSOR / NO_GENERAL_NOVELTY / NO_CANON / NO_EXEC_SIGN"
},indent=2))
