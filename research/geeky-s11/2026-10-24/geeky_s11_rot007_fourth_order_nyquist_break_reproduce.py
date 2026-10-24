#!/usr/bin/env python3
"""Geeky-S11 ROT007 -- independent finite-grid Fourier/FFT test of 2nd vs 4th order TT checkerboard shift.
All-alpha robustness: two Fourier witnesses with distinct E_alpha zeros, N divisible by 8. NumPy only.
"""
import json, numpy as np

def centered_derivative(a,axis,order,h):
    if order==2:
        return (np.roll(a,-1,axis=axis)-np.roll(a,1,axis=axis))/(2*h)
    if order==4:
        return (-np.roll(a,-2,axis=axis)+8*np.roll(a,-1,axis=axis)-8*np.roll(a,1,axis=axis)+np.roll(a,2,axis=axis))/(12*h)
    raise ValueError(order)

def project_tt(F,order,N):
    h=2*np.pi/N
    k=np.rint(np.fft.fftfreq(N)*N).astype(int)
    t=2*np.pi*k/N
    sym=np.sin(t)/h
    if order==4:sym*= (4-np.cos(t))/3
    sym[(k==0)|(np.abs(k)==N//2)]=0.
    dx,dy,dz=np.meshgrid(sym,sym,sym,indexing='ij')
    d=np.stack((dx,dy,dz),axis=-1)
    norm2=np.sum(d*d,axis=-1)
    pi=np.broadcast_to(np.eye(3),(N,N,N,3,3)).copy()
    pi-=np.einsum('...i,...j->...ij',d,d)/np.where(norm2==0,1.,norm2)[...,None,None]
    pi[norm2==0]=0.
    FF=np.fft.fftn(F,axes=(0,1,2))
    proj=np.einsum('...ik,...kl,...lj->...ij',pi,FF,pi,optimize=True)
    tr=np.einsum('...ij,...ji->...',pi,FF,optimize=True)
    proj-=.5*pi*tr[...,None,None]
    res=np.fft.ifftn(proj,axes=(0,1,2))
    return res.real,float(np.max(np.abs(res.imag)))

def norm(F):return float(np.sqrt(np.mean(np.sum(F*F,axis=(-2,-1)))))

def symbol(theta,order,h):
    s=np.sin(theta)/h
    return s if order==2 else s*(4-np.cos(theta))/3

def analytic(N,alpha,carrier,order):
    h=2*np.pi/N
    tx=np.pi/4
    ty=np.pi/2 if carrier=='A' else 3*np.pi/4
    ax=symbol(tx,order,h);ay=symbol(ty,order,h)
    bx=symbol(tx+np.pi,order,h);by=symbol(ty+np.pi,order,h)
    delta=abs(ax*by-ay*bx)/(np.hypot(ax,ay)*np.hypot(bx,by))
    rho=delta*np.sqrt(4-delta*delta)/2
    filt=1.-4*alpha*(np.sin(tx/2)**2+np.sin(ty/2)**2)
    return abs(ax*filt)*rho,float(delta),float(rho),float(filt)

def run():
    rt2=np.sqrt(2.)
    rA=16*np.sqrt(9217.)/9281
    rB=8*np.sqrt(2114.)/1089
    A=(4*rt2-1)*rA/(12*np.pi)
    B=(4*rt2-1)*rB/(12*np.pi)
    p=4-rt2
    alpha_star=(A+B)/(p*A+4*B)
    min_gain=A*B*rt2/(p*A+4*B)
    alphas=(0.,.05,.2,.25,1./p,alpha_star)
    rows=[]
    for N in (8,16,24,32):
        h=2*np.pi/N
        xx,yy,zz=np.meshgrid(np.arange(N)*h,np.arange(N)*h,np.arange(N)*h,indexing='ij')
        chi=(-1.)**(np.arange(N)[:,None,None]+np.arange(N)[None,:,None]+np.arange(N)[None,None,:])
        for order in (2,4):
            for alpha in alphas:
                for carrier,ky in (('A',N//4),('B',3*N//8)):
                    kx=N//8
                    ax=symbol(np.pi/4,order,h)
                    ay=symbol(2*np.pi*ky/N,order,h)
                    v=np.array([ay,-ax,0.])/np.hypot(ax,ay)
                    w=np.array([0.,0.,1.])
                    T=np.outer(v,v)-np.outer(w,w)
                    H=np.cos(kx*xx+ky*yy)[...,None,None]*T
                    EH=H+alpha*sum(np.roll(H,-1,axis=j)-2*H+np.roll(H,1,axis=j) for j in range(3))
                    LH=chi[...,None,None]*centered_derivative(EH,0,order,h)
                    PH,imH=project_tt(H,order,N)
                    PL,imL=project_tt(LH,order,N)
                    actual=norm(LH-PL)/norm(H)
                    tt_error=norm(PH-H)/norm(H)
                    pred,delta,rho,filt=analytic(N,alpha,carrier,order)
                    assert abs(actual-pred)<3.e-12,(N,order,alpha,carrier,actual,pred)
                    assert tt_error<3.e-13,(N,order,alpha,carrier,tt_error)
                    rows.append(dict(N=N,order=order,alpha=alpha,carrier=carrier,leak=actual,predicted=pred,error=abs(actual-pred),TT_error=tt_error,filter=filt,sin_angle=delta,projector_imag_max=max(imH,imL)))
    # Uniform alpha bound proven analytically as minimax over two exact carriers.
    for N in (8,16,24,32):
        for alpha in alphas:
            seq=[r['leak'] for r in rows if r['N']==N and r['order']==4 and r['alpha']==alpha]
            assert max(seq)+1e-12>=N*min_gain,(N,alpha,seq,N*min_gain)
    summary=dict(artifact_id='GEEKY-S11-ROT007-FOURTH-ORDER-SCHEME-DEPENDENT-CHECKERBOARD-TT-NONGO',status='PASS',cases=len(rows),N=[8,16,24,32],alpha_values=list(alphas),minimax_alpha=alpha_star,all_alpha_uniform_gain_per_N=min_gain,carrier_A_gain_per_N=A,carrier_B_gain_per_N=B,max_formula_gap=max(row['error'] for row in rows),max_tt_input_error=max(row['TT_error'] for row in rows),max_order2_leak=max(row['leak'] for row in rows if row['order']==2),rows=rows)
    dst='/mnt/data/geeky_s11_rot007_fourth_order_nyquist_results.json'
    with open(dst,'w') as f:json.dump(summary,f,indent=2,ensure_ascii=False)
    print('PASS',json.dumps({k:v for k,v in summary.items() if k!='rows'},indent=2))
    for N in summary['N']:
        aa=[r for r in rows if r['N']==N and r['alpha']==.05]
        print('N',N,'alpha .05',[(r['order'],r['carrier'],round(r['leak'],9)) for r in aa])
    return summary
if __name__=='__main__':run()
