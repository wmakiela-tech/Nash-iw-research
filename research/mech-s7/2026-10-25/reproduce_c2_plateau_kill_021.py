#!/usr/bin/env python3
"""ROT021 exact pair-sum C^2 matched plateau shape nonlinear root. Conditional ODE only."""
import importlib.util,json,math,time,csv
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('c21',str(P/'reproduce_causal_kernel_021.py'))
k=importlib.util.module_from_spec(sp);sp.loader.exec_module(k)
p=k.prev;b=k.base;bridge=k.bridge;mod=k.mod
WIDTH=.15

def plateau(u,width=WIDTH):
    z=math.log(u)
    return -math.expm1(-min(100.,abs(z/width)**4))

def root_test(mp,rtol,initial_root=None):
    t0=time.time(); raw=b.load(p.PUB,p.PAP); orig=mod.contexts(b,p.PUB,p.PAP);eos=mod.eos_table()
    br=bridge.run_bridge(b,mod,raw,eos,.5,mp,rtol=rtol)
    ctx=bridge.shifted_ctx(orig,br,mp);host=mod.prepare_host(b,ctx,eos,.5,rtol=2e-10)
    frame=ctx['maps'][mp]
    y0=np.r_[float(frame.Xn.iloc[1469]),np.array([float(frame[f'n_{sp}_cm3'].iloc[1469]) for sp in b.SPECIES])/b.NSCALE]
    factors=np.ones(6) if mp=='exec' else np.array([.5,.5,.5,1,.5,.5]);Tedge=ctx['Tedge']
    def derivatives(y,T,loga):
        X=y[0];npop=y[1:]
        D,a,bb,weak=b.rates(X,T)
        return weak+np.sum(npop*b.NSCALE*b.SIGMA_V_UNIT*((1-X)*a-X*bb)),D
    def rhs(u,y,eps):
        T=host['pre_T'](u);loga=host['pre_lna'](u); dx,D=derivatives(y,T,loga)
        qq=p.source_rates(u,'public','native',WIDTH)
        if eps:
            tot=qq[4]+qq[5];lnratio=math.log(qq[4]/qq[5])+eps*plateau(u)
            r=math.exp(lnratio)
            qq[4]=tot*r/(1+r);qq[5]=tot/(1+r)
        nPBH=ctx['nedge']*math.exp(-3*loga)
        src=qq*factors*nPBH/b.HBAR_GEV_SEC/b.NSCALE
        return (-3*b.DT_EDGE*u*u)*np.r_[dx,src-D*y[1:]]
    def post(t,y):
        dx,D=derivatives(y,host['post_T'](t),host['post_lna'](t))
        return np.r_[dx,-D*y[1:]]
    X_paper=p.evolve_law(ctx,eos,host,mp,law='paper',rtol=rtol)['X_nuc']
    evals=[]
    def solve_delta(eps):
        a=solve_ivp(lambda u,y:rhs(u,y,eps),(1,b.U_CUT),y0,method='Radau',rtol=rtol,atol=rtol*1e-3,max_step=.01)
        assert a.success,a.message
        out=solve_ivp(post,(ctx['tcut'],host['Tnuc_time']),a.y[:,-1],method='Radau',rtol=rtol,atol=rtol*1e-3,max_step=2.)
        assert out.success,out.message
        delta=X_paper-float(out.y[0,-1]);evals.append({'epsilon':eps,'delta':delta,'X_public':float(out.y[0,-1])})
        print('CELL',mp,'rtol',rtol,'eps',eps,'delta',delta,'elapsed',round(time.time()-t0,1),flush=True)
        return delta
    initial=solve_delta(0.)
    if initial_root is None:
        bracket=(0.,.0004) if mp=='exec' else (-.0006,0.)
        f2=solve_delta(bracket[1] if mp=='exec' else bracket[0])
        assert initial*f2<0, 'no root bracket'
        root=brentq(solve_delta,*bracket,xtol=1e-11,rtol=1e-9)
    else:root=float(initial_root)
    froot=solve_delta(root)
    return {'map':mp,'rtol':rtol,'width':WIDTH,'X_paper':X_paper,'delta_baseline':initial,'epsilon_root':root,'delta_at_root':froot,'source_log_ratio_change_at_1e8':root*plateau(.1),'source_ratio_fractional_change_at_1e8':math.expm1(root*plateau(.1)),'evals':evals}

def main():
    rows=[]
    for mp in ('exec','sym'):
        rr=root_test(mp,3e-8)
        cc=root_test(mp,3e-9,initial_root=rr['epsilon_root'])
        rows.extend([rr,cc])
    (P/'ratio_plateau_root_021.json').write_text(json.dumps({'rows':rows,'shape':'1-exp[-(lnu/0.15)^4]; C^2 edge, exact pair sum','source':'Wu-Xu pinned','guard':'NO ORIGINAL JULIA'},indent=2))
    with (P/'ratio_plateau_roots_021.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=[k for k in rows[0] if k!='evals']);w.writeheader();w.writerows([{k:v for k,v in r.items() if k!='evals'} for r in rows])
    print('DONE')
if __name__=='__main__':main()