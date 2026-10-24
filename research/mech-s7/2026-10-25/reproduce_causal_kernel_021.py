#!/usr/bin/env python3
"""MECH-S7 ROT021: conditional source-pinned fixed-pair-sum linear response kernel.
Differentiates ODE exactly wrt pointwise pbar/nbar source redistribution,
uses backwards adjoint on forward 7D source-on and postsource traces.
Independent finite-difference 7D ODE reruns for compact mass windows.
Not original Julia Wu-Xu 10D; not a physical PBH/BBN result.
"""
import math,csv,json,time,hashlib,importlib.util,sys
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp, trapezoid
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('prev020',str(ROOT/'reproduce_joint_c2_ratio_020.py'))
prev=importlib.util.module_from_spec(spec);spec.loader.exec_module(prev)
base=prev.base;bridge=prev.bridge;mod=prev.mod
Gamma=base.GAMMA
# intervals in M/1e9g, lower -> upper. C^2 support bump = sin^4.
EDGES=np.array([base.U_CUT,1e-6,1e-5,1e-4,1e-3,.01,.05,.1,.2,.35,.5,.75,1.0])
# restrict compact windows, normalize to unit peak log-ratio perturbation; masks independent.
def bumps_logu(logu):
    z=np.asarray(logu)
    out=np.zeros((len(EDGES)-1,)+z.shape)
    for i,(lo,hi) in enumerate(zip(EDGES[:-1],EDGES[1:])):
        al,ah=math.log(lo),math.log(hi)
        t=(z-al)/(ah-al)
        flag=(t>0)&(t<1)
        out[i]=np.where(flag,np.sin(np.pi*np.clip(t,0,1))**4,0.)
    return out

def full_jacobian(X,T,n,conserve,Tedge,logA):
    scale=(Tedge/T)**3*math.exp(-3*logA) if conserve else 1.
    D,a,b,weak=base.rates(X,T,baryon_scale=scale)
    x=base.Q_MEV/T
    g=(255/base.TAU_N)*(12+6*x+x*x)/x**5
    C=base.NSCALE*base.SIGMA_V_UNIT
    nb=scale*base.ETA_B*(2*base.ZETA3/math.pi**2)*(T/base.HBARC_MEV_CM)**3
    fC=np.array([base.coulomb(T,139.57039),base.coulomb(T,493.677)])
    dD=np.array([-a[0], b[1], 60-45.5*fC[1], 0, -9, +9])*nb*base.SIGMA_V_UNIT
    J=np.zeros((7,7))
    J[0,0]=-g*(1+math.exp(-x))-1/base.TAU_N-C*np.dot(n,a+b)
    J[0,1:]=C*((1-X)*a-X*b)
    J[1:,0]=-dD*n
    J[1:,1:]=-np.diag(D)
    return J

def run_model(mp='exec',chi=.5,conserve=False,rtol=3e-8,do_finite=True):
    start=time.time()
    orig=mod.contexts(base,prev.PUB,prev.PAP)
    raw=base.load(prev.PUB,prev.PAP)
    eos=mod.eos_table()
    br=bridge.run_bridge(base,mod,raw,eos,chi,mp,conserve_from_saved=conserve,rtol=rtol)
    ctx=bridge.shifted_ctx(orig,br,mp)
    host=mod.prepare_host(base,ctx,eos,chi,rtol=2e-10)
    factors=np.ones(6) if mp=='exec' else np.array([.5,.5,.5,1,.5,.5])
    Tedge=ctx['Tedge']
    df=ctx['maps'][mp]
    X0=float(df.Xn.iloc[1469]);npop=np.array([float(df[f'n_{sp}_cm3'].iloc[1469]) for sp in base.SPECIES])/base.NSCALE
    y0=np.r_[X0,npop]
    def deriv(y,T,logA):
        X=float(y[0]);n=y[1:]
        scale=(Tedge/T)**3*math.exp(-3*logA) if conserve else 1.
        D,aa,bb,weak=base.rates(X,T,baryon_scale=scale)
        conv=np.sum(n*base.NSCALE*base.SIGMA_V_UNIT*((1-X)*aa-X*bb))
        return weak+conv,D
    def fw_active(u,y,amp=0.,window=None,kind=None,lmbd=.05):
        T=host['pre_T'](u);logA=host['pre_lna'](u)
        dx,D=deriv(y,T,logA)
        nPBH=ctx['nedge']*math.exp(-3*logA)
        q=prev.source_rates(u,'public','native',lmbd)
        if kind=='sumflat':
            q=prev.source_rates(u,'public','sumflat',lmbd)
        if window is not None and amp!=0.:
            phi=float(bumps_logu(np.array([math.log(u)]))[window,0])
            qtot=q[4]+q[5];z=math.log(q[4]/q[5])+amp*phi
            # exp z underflow protected, but |z| small here
            R=math.exp(z);q[4]=qtot*R/(1+R);q[5]=qtot/(1+R)
        src=q*factors*nPBH/base.HBAR_GEV_SEC/base.NSCALE
        return (-3*base.DT_EDGE*u*u)*np.r_[dx,src-D*y[1:]]
    a=solve_ivp(lambda u,y:fw_active(u,y), (1.,base.U_CUT),y0,method='Radau',rtol=rtol,atol=rtol*1e-3,max_step=.01,dense_output=True)
    assert a.success,a.message
    def fw_post(t,y):
        T=host['post_T'](t);logA=host['post_lna'](t)
        dx,D=deriv(y,T,logA)
        return np.r_[dx,-D*y[1:]]
    b=solve_ivp(fw_post,(ctx['tcut'],host['Tnuc_time']),a.y[:,-1],method='Radau',rtol=rtol,atol=rtol*1e-3,max_step=2.,dense_output=True)
    assert b.success,b.message
    target=float(b.y[0,-1])
    # ADJOINT λ_t = -J(t)^T λ for postsource, backwards tnuc -> tcut
    def adj_post(t,lam):
        T=host['post_T'](t); logA=host['post_lna'](t)
        yy=b.sol(t);J=full_jacobian(yy[0],T,yy[1:],conserve,Tedge,logA)
        return -J.T@lam
    ap=solve_ivp(adj_post,(host['Tnuc_time'],ctx['tcut']),np.r_[1.,np.zeros(6)],method='Radau',rtol=3e-9,atol=1e-12,max_step=2.,dense_output=True)
    assert ap.success,ap.message
    def adj_pre(u,lam):
        T=host['pre_T'](u);logA=host['pre_lna'](u)
        yy=a.sol(u);J=full_jacobian(yy[0],T,yy[1:],conserve,Tedge,logA)
        return -(-3*base.DT_EDGE*u*u)*J.T@lam
    aa=solve_ivp(adj_pre,(base.U_CUT,1.),ap.y[:,-1],method='Radau',rtol=3e-9,atol=1e-12,max_step=.01,dense_output=True)
    assert aa.success,aa.message
    z=np.linspace(math.log(base.U_CUT),0,5201)
    us=np.exp(z)
    jac=aa.sol(us) # λ_i
    nPBH=np.array([ctx['nedge']*math.exp(-3*host['pre_lna'](float(u))) for u in us])
    qp=base.Q1[3]*us**base.SLOPES[3];qn=base.Q1[4]*us**base.SLOPES[4]
    derivQ=qp*qn/(qp+qn)
    weight=3*base.DT_EDGE*us**3*derivQ*nPBH/base.HBAR_GEV_SEC/base.NSCALE*(factors[4]*jac[5]-factors[5]*jac[6]);# per d(ln mass)
    phi=bumps_logu(z)
    responses=[float(trapezoid(weight*phi[i],z)) for i in range(len(EDGES)-1)]
    source_shape=np.array([prev.log_shape(float(u),'sumflat',.05) for u in us])
    predicted=float(trapezoid(weight*source_shape,z))
    actual_flat=prev.evolve_law(ctx,eos,host,mp,law='public',kind='sumflat',lmbd=.05,rtol=rtol,conserve=conserve)['X_nuc']-target
    # geometry robustness data
    result={'map':mp,'chi':chi,'baryon':'comoving' if conserve else 'eta','rtol':rtol,'X_native':target,'X_flat':target+actual_flat,'actual_Xflat_minus_Xnative':actual_flat,'linear_prediction_Xflat_minus_Xnative':predicted,'linear_diff':predicted-actual_flat,'adjoint_cut':list(ap.y[:,-1]),'adjoint_edge':list(aa.y[:,-1]),'active_steps':len(a.t),'post_steps':len(b.t),'adjoint_active_steps':len(aa.t),'adjoint_post_steps':len(ap.t),'elapsed_s':time.time()-start,'shell_responses':responses}
    fd=[]
    if do_finite:
        for i in [5,7,9,10]:
            eps=2e-4
            vp=[]
            for sign in [1,-1]:
                ac=solve_ivp(lambda u,y:fw_active(u,y,amp=sign*eps,window=i), (1.,base.U_CUT),y0,method='Radau',rtol=rtol,atol=rtol*1e-3,max_step=.01)
                assert ac.success,ac.message
                pc=solve_ivp(fw_post,(ctx['tcut'],host['Tnuc_time']),ac.y[:,-1],method='Radau',rtol=rtol,atol=rtol*1e-3,max_step=2.)
                assert pc.success,pc.message
                vp.append(float(pc.y[0,-1]))
            grad=(vp[0]-vp[1])/(2*eps)
            fd.append({'index':i,'mass_low_g':float(EDGES[i]*1e9),'mass_high_g':float(EDGES[i+1]*1e9),'predicted_adjoint':responses[i],'finite_diff_centered':grad,'fd_vs_adjoint':grad-responses[i],'X_plus':vp[0],'X_minus':vp[1]})
    result['finite_difference']=fd
    print('RESULT',mp, 'X',target,'d_flat',actual_flat,'pred',predicted,'adj_shells',responses,'fd',fd,'elapsed',round(time.time()-start,1),flush=True)
    return result,{'logu':z,'mass_g':us*1e9,'kernel':weight,'shape':source_shape,'source_center_p':qp,'source_center_n':qn,'local_density_flat':weight*source_shape},phi

def main():
    out=ROOT
    cases=[];kernels={}
    for mp in ('exec','sym'):
        r,k,phi=run_model(mp,do_finite=True)
        cases.append(r);kernels[mp]=k
    (out/'causal_kernel_021.json').write_text(json.dumps({'cases':cases,'edges_u':EDGES.tolist(),'source_commit':base.UPSTREAM,'source_table_sha':'06d0883a27b108692720422294ba2baacd381a64','guard':'CONDITIONAL_7D_NOT_ORIGINAL_JULIA'},indent=2))
    with (out/'mass_sensitivity_kernel_021.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['mass_g','u','logu','Kln_exec','Kln_sym','source_shape','effect_density_exec','effect_density_sym'])
        for j in range(len(kernels['exec']['logu'])):
            w.writerow([kernels['exec']['mass_g'][j],kernels['exec']['mass_g'][j]/1e9,kernels['exec']['logu'][j],kernels['exec']['kernel'][j],kernels['sym']['kernel'][j],kernels['exec']['shape'][j],kernels['exec']['local_density_flat'][j],kernels['sym']['local_density_flat'][j]])
    with (out/'mass_shell_adjoint_fd_021.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['map','bin','mass_low_g','mass_high_g','adjoint_gradient','finite_difference','difference'])
        for r in cases:
            for i,val in enumerate(r['shell_responses']):
                fd=next((x for x in r['finite_difference'] if x['index']==i),None)
                w.writerow([r['map'],i,EDGES[i]*1e9,EDGES[i+1]*1e9,val,'' if fd is None else fd['finite_diff_centered'],'' if fd is None else fd['fd_vs_adjoint']])
    print('COMPLETE',flush=True)
if __name__=='__main__': main()