import numpy as np
import json
from pathlib import Path

def deriv(A, axis, h): return (np.roll(A,-1,axis=axis)-np.roll(A,1,axis=axis))/(2*h)
def E(A, alpha,h):
    lap = sum(np.roll(A,-1,axis=j)-2*A+np.roll(A,1,axis=j) for j in range(3))
    return A+alpha*lap

def lie(C,H,h):
    Z=np.zeros_like(H)
    D_C=np.stack([deriv(C,ax,h) for ax in range(3)],axis=-2) # shape grid,3 deriv_i,3 C^j
    for j in range(3): Z+=C[...,j,None,None]*deriv(H,j,h)
    Z+=np.einsum('...mj,...im->...ij',H,D_C)
    Z+=np.einsum('...im,...jm->...ij',H,D_C)
    return Z

def P_tt(H,h):
    N=H.shape[0]
    m=np.fft.fftfreq(N,d=h)*2*np.pi
    k=np.stack(np.meshgrid(m,m,m,indexing='ij'),axis=-1)
    k2=np.sum(k*k,axis=-1)
    inv=np.divide(1.,k2,out=np.zeros_like(k2),where=k2>0)
    P=np.eye(3)-k[..., :,None]*k[...,None,:]*inv[...,None,None]
    Hhat=np.fft.fftn(H,axes=(0,1,2))
    B=np.einsum('...im,...mn,...nj->...ij',P,Hhat,P)
    t=np.einsum('...ij,...ji->...',P,Hhat)
    B-=0.5*P*t[...,None,None]
    B[k2==0]=0
    return np.fft.ifftn(B,axes=(0,1,2)).real

def fields(N):
    h=2*np.pi/N
    X,Y,Z=np.meshgrid(np.arange(N)*h,np.arange(N)*h,np.arange(N)*h,indexing='ij')
    C=np.stack([.15*np.sin(X)+.10*np.cos(Y),.08*np.cos(Z),.06*np.sin(X+Z)],axis=-1)
    return h,(X,Y,Z),C

def pols():
    out=[]
    for axis in range(3):
        oth=[j for j in range(3) if j!=axis]
        a,b=oth
        diag=np.zeros((3,3)); diag[a,a]=1/np.sqrt(3);diag[b,b]=-1/np.sqrt(3)
        shear=np.zeros((3,3)); shear[a,b]=shear[b,a]=1/np.sqrt(2)
        out.extend([(axis,'diag',diag),(axis,'shear',shear)])
    return out

def run(N,alpha,const=False):
    h,coords,C=fields(N)
    if const: C[:]=[.07,.03,-.02]
    DC=np.stack([deriv(C,j,h) for j in range(3)],axis=-2)
    S=(DC+np.swapaxes(DC,-1,-2))/2
    S0=S-np.trace(S,axis1=-2,axis2=-1)[...,None,None]*np.eye(3)/3
    strain_norm2=np.mean(np.sum(S0*S0,axis=(-2,-1)))
    e=1-4*alpha*np.sin(h/2)**2
    trace_sum=0.; leakage_sum=0.;input_sum=0.;max_tt_err=0.;max_trace_err=0.
    for axis,name,M in pols():
        for phase in ('cos','sin'):
            f=np.cos(coords[axis]) if phase=='cos' else np.sin(coords[axis])
            H=f[...,None,None]*M
            max_tt_err=max(max_tt_err,float(np.sqrt(np.mean(np.sum((P_tt(H,h)-H)**2,axis=(-2,-1))))))
            O=lie(C,E(H,alpha,h),h)
            tr=np.trace(O,axis1=-2,axis2=-1)
            predicted=2*e*f*np.einsum('ij,...ij->...',M,S0)
            max_trace_err=max(max_trace_err,float(np.max(np.abs(tr-predicted))))
            trace_sum+=np.mean(tr**2)
            Q=O-P_tt(O,h)
            leakage_sum+=np.mean(np.sum(Q**2,axis=(-2,-1)))
            input_sum+=np.mean(np.sum(H**2,axis=(-2,-1)))
    rhs=4*e*e*strain_norm2
    return {'N':N,'alpha':alpha,'constant_C':const,'e1':e,'trace_probe_sum':trace_sum,'exact_rhs':rhs,
     'abs_error':abs(trace_sum-rhs),'relative_error':(abs(trace_sum-rhs)/rhs if rhs>1.e-25 else None),
     'strain_dev_rms':np.sqrt(strain_norm2),'leakage_probe_sum':leakage_sum,
     'leakage_bound_rhs':rhs/3,'input_probe_sum':input_sum,
     'operator_bound':2*abs(e)*np.sqrt(strain_norm2)/np.sqrt(15),
     'observed_probe_ratio':np.sqrt(leakage_sum/input_sum),
     'max_tt_input_err_rms':max_tt_err,'max_trace_formula_point_error':max_trace_err,
     'lower_bound_check': bool(leakage_sum>=rhs/3-2e-14)}

if __name__=='__main__':
 rows=[run(N,a) for N in (7,9,17,31) for a in (0.,.05,.2)]
 rows.append(run(9,.05,True))
 summary={'result_id':'GEEKY-S11-ROT002-SIX-POLARIZATION-TT-TRACE-FRAME-RIGIDITY',
          'max_trace_frame_abs_error':max(x['abs_error'] for x in rows),
          'max_trace_formula_point_error':max(x['max_trace_formula_point_error'] for x in rows),
          'max_tt_input_err_rms':max(x['max_tt_input_err_rms'] for x in rows),
          'all_lower_bounds_pass':all(x['lower_bound_check'] for x in rows),
          'rows':rows}
 p=Path('/mnt/data/geeky_s11_rot002_results.json');p.write_text(json.dumps(summary,indent=2)+'\n')
 print(json.dumps({k:v for k,v in summary.items() if k!='rows'},indent=2));
 for r in rows: print('N',r['N'],'alpha',r['alpha'],'constant',r['constant_C'],'frame err',r['abs_error'],'norm bound',r['operator_bound'],'observed',r['observed_probe_ratio'],'Ptt err',r['max_tt_input_err_rms'])
