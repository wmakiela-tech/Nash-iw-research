#!/usr/bin/env python3
"""Mech-S7 ROT024: source-target sufficiency check with exactly pointwise pair-sum
and 0..k logarithmic comoving source moments preserved, k=2..5.
Source-pinned reduced 10-component preedge + 7D subedge/postsource only;
NO original Julia 10D execution; NO validated M<1e9g Hawking spectra.
"""
from __future__ import annotations
import argparse,csv,json,math,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp, trapezoid
from scipy.linalg import null_space
from numpy.polynomial.legendre import leggauss
import reproduce_joint_c2_ratio_020 as old

P=Path(__file__).resolve().parent
base,bridge,mod=old.base,old.bridge,old.mod
SQ=np.array([base.Q1[3],base.Q1[4]],float)
SL=np.array([base.SLOPES[3],base.SLOPES[4]],float)
EDGES=np.geomspace(.07,.92,8)
BINS=[(float(a),float(b)) for a,b in zip(EDGES[:-1],EDGES[1:])]
NL=96
NODES,WEIGHTS=leggauss(NL)
L0,L1=math.log(BINS[0][0]), math.log(BINS[-1][1])

def xs(z):return (2*z-(L1+L0))/(L1-L0)

def values(u):return SQ*u**SL

def bumpz(z,lo,hi):
    a,b=math.log(lo), math.log(hi)
    if z<=a or z>=b:return 0.
    return math.sin(math.pi*(z-a)/(b-a))**4

def support(k):
    lo,hi=BINS[k];a,b=map(math.log,(lo,hi));z=.5*(a+b)+.5*(b-a)*NODES
    w=.5*(b-a)*WEIGHTS;u=np.exp(z)
    bump=np.sin(np.pi*(z-a)/(b-a))**4
    qp,qn=SQ[0]*u**SL[0], SQ[1]*u**SL[1]
    pair=qp+qn
    return z,u,w,bump,qp,qn,pair

SUP=[support(k) for k in range(7)]
MAX_MOM=5
M=np.array([[np.sum(w*u**3*pair*B*xs(z)**j) for z,u,w,B,qp,qn,pair in SUP] for j in range(MAX_MOM+1)])
K=np.genfromtxt(P/'mass_sensitivity_kernel_021.csv',delimiter=',',names=True)
G=np.array([[np.sum(w*np.interp(z,K['logu'],K['Kln_'+mp])*pair**2/(qp*qn)*B)
               for z,u,w,B,qp,qn,pair in SUP] for mp in ('exec','sym')])


def coeffs(degree):
    A=M[:degree+1,:].copy()
    A=A/np.linalg.norm(A,axis=1)[:,None]
    N=null_space(A,rcond=1e-13)
    assert N.shape[1]==7-degree-1,N.shape
    v=N@(N.T@G[0]) # source-target-optimized null direction
    v/=max(abs(v))
    assert G[0]@v>0
    assert max(abs(A@v))<1e-12,(degree,A@v)
    return v,float(np.linalg.cond(A))

CO={k:coeffs(k)[0] for k in (2,3,4,5)}

def shape(u,k):
    z=math.log(u)
    for i,(lo,hi) in enumerate(BINS):
        if lo<u<hi:return CO[k][i]*bumpz(z,lo,hi)
    return 0.

def source(u,k,amplitude):
    values=np.array(old.source_rates(u,'public','native',.05),float)
    s=shape(u,k)
    if s:
        d=amplitude*(values[4]+values[5])*s
        values[4]+=d
        values[5]-=d
    if np.any(values[4:6]<=0):raise ValueError('negative rate')
    return values

def adjoint_prediction(k):
    return {'exec':float(G[0]@CO[k]),'sym':float(G[1]@CO[k])}

def moment_residuals(k,epsilon):
    coeff=CO[k];res=[]
    for j in range(k+1):
        # controlled moment is full ∫u³ Q_j (ln u)^j dz, but only compact perturbation contributes
        dd=sum(np.sum(w*u**3*pair*B*coeff[i]*z**j) for i,(z,u,w,B,qp,qn,pair) in enumerate(SUP))
        # independent norm for normalized ratio
        scale=sum(np.sum(w*u**3*pair*B*abs(coeff[i])*abs(z)**j) for i,(z,u,w,B,qp,qn,pair) in enumerate(SUP))
        res.append({'degree':k,'moment':j,'signed_residual':float(epsilon*dd),'relative_to_L1':float(abs(dd)/scale) if scale else 0.})
    return res

def run_map(mp,degree_amps,rtol):
    raw=base.load(old.PUB,old.PAP);ctx0=mod.contexts(base,old.PUB,old.PAP);eos=mod.eos_table()
    br=bridge.run_bridge(base,mod,raw,eos,.5,mp,conserve_from_saved=False,rtol=rtol)
    ctx=bridge.shifted_ctx(ctx0,br,mp)
    host=mod.prepare_host(base,ctx,eos,.5,rtol=2e-10)
    df=ctx['maps'][mp];X0=float(df.Xn.iloc[1469]);n0=np.array([float(df[f'n_{sp}_cm3'].iloc[1469]) for sp in base.SPECIES])/base.NSCALE
    y0=np.r_[X0,n0]
    factors=np.ones(6) if mp=='exec' else np.array([.5,.5,.5,1,.5,.5])
    def dyn(y,T):
        X=float(y[0]);n=y[1:];D,a,b,weak=base.rates(X,T,baryon_scale=1.)
        cv=np.sum(n*base.NSCALE*base.SIGMA_V_UNIT*((1-X)*a-X*b))
        return weak+cv,D
    def active(u,y,degree,epsilon):
        T=host['pre_T'](u);logA=host['pre_lna'](u);dx,D=dyn(y,T)
        nPBH=ctx['nedge']*math.exp(-3*logA)
        q=source(u,degree,epsilon)*factors*nPBH/mod.HBAR_GEV_SEC/base.NSCALE
        return -3*base.DT_EDGE*u*u*np.r_[dx,q-D*y[1:]]
    def post(t,y):
        dx,D=dyn(y,host['post_T'](t));return np.r_[dx,-D*y[1:]]
    out=[];start=time.time()
    for k,amplitudes in degree_amps.items():
        for epsilon in amplitudes:
            a=solve_ivp(lambda u,y:active(u,y,k,epsilon),(1.,base.U_CUT),y0,method='Radau',rtol=rtol,atol=rtol*1e-3,max_step=.004)
            if not a.success:raise RuntimeError(a.message)
            b=solve_ivp(post,(ctx['tcut'],host['Tnuc_time']),a.y[:,-1],method='Radau',rtol=rtol,atol=rtol*1e-3,max_step=2.)
            if not b.success:raise RuntimeError(b.message)
            r={'map':mp,'moment_degree':k,'epsilon':epsilon,'Xcut':float(a.y[0,-1]),'Xnuc':float(b.y[0,-1]),'steps_active':len(a.t),'steps_post':len(b.t),'elapsed_s':round(time.time()-start,2)}
            out.append(r);print('EXECUTED',r,flush=True)
    return out

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',default=str(P));parser.add_argument('--rtol',type=float,default=3e-9)
    parser.add_argument('--maps',default='exec,sym');parser.add_argument('--degrees',default='2,3,4,5')
    parser.add_argument('--epsilon',type=float,default=.04)
    args=parser.parse_args();dst=Path(args.out);dst.mkdir(parents=True,exist_ok=True)
    degrees=[int(x) for x in args.degrees.split(',')];maps=args.maps.split(',');amplitudes={k:[-.04,0.,.04] for k in degrees}
    # use passed amplitude, control zero only once per degree to independently check baseline invariance
    amplitudes={k:[-args.epsilon,0.,args.epsilon] for k in degrees}
    rows=[]
    for mp in maps:rows.extend(run_map(mp,amplitudes,args.rtol))
    for r in rows:
        baseline=next(b['Xnuc'] for b in rows if b['map']==r['map'] and b['moment_degree']==r['moment_degree'] and b['epsilon']==0)
        r['dXnuc']=r['Xnuc']-baseline
        r['adjoint_linear_dX']=r['epsilon']*adjoint_prediction(r['moment_degree'])[r['map']]
        r['difference_from_adjoint']=r['dXnuc']-r['adjoint_linear_dX']
        r['paper_minus_source']=0.40094496781788425-r['Xnuc'] if r['map']=='exec' else None
    adj=[{'moment_degree':k,'condition':coeffs(k)[1],'deriv_exec':float(G[0]@CO[k]),'deriv_sym':float(G[1]@CO[k]),'coefficients':CO[k].tolist(),
          'normalized_moment_residual':max(x['relative_to_L1'] for x in moment_residuals(k,args.epsilon))} for k in degrees]
    tests={'max_relative_moment_residual':max(t['normalized_moment_residual'] for t in adj),
           'pointwise_pair_sum_analytic':True,'source_support_mass_g':[BINS[0][0]*1e9,BINS[-1][1]*1e9],
           'cut_boundary_jet':'Each sin^4 supported bump has vanishing derivatives through order 3 at bin boundaries, source untouched around 1e9g',
           'condition':'Cauchy moments for LOG mass, comoving source fluence weight u^3 Q(u); k-th degree preserve first k+1 moments of each species',
           'negative_knowledge':'Not original Wu-Xu 10D, no admitted hadronic spectrum below 1e9g, no Yp or PBH bounds'}
    payload={'model':'PINNED_SOURCE_INSPIRED_CONDITIONAL_10_COMPONENT_BRIDGE_PLUS_7D',
      'author_source_commit':'d395183674cace6c9906a8911bdeb7234ba4040d',
      'method':'7 disjoint logu sin^4 bumps, linear nullspace of first k+1 species fluence log mass moments, target-informed projected ROT021 adjoint selection, verify by independent nonlinear ODE',
      'bins_mass_g':[[lo*1e9,hi*1e9] for lo,hi in BINS],'degrees':adj,'checks':tests,'rows':rows,'rtol':args.rtol}
    (dst/'high_order_moment_results_024.json').write_text(json.dumps(payload,indent=2),encoding='utf-8')
    with (dst/'high_order_moment_results_024.csv').open('w',newline='') as f:
      w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    with (dst/'high_order_moment_constraints_024.csv').open('w',newline='') as f:
      w=csv.writer(f);w.writerow(['k','j','relative_to_L1','signed_residual'])
      for k in degrees:
       for z in moment_residuals(k,args.epsilon):w.writerow([k,z['moment'],z['relative_to_L1'],z['signed_residual']])
    print('FINISHED',json.dumps({'derivatives':adj,'checks':tests},indent=2),flush=True)

if __name__=='__main__':main()