import numpy as np
exec(open('/home/claude/mono/kreiss4.py').read().split('SEP = ')[0].split('def numrange_max')[0])
# czy dla G scisle kontraktujacego sup = sqrt(m) jest OSIAGANY w granicy t->0,
# czy plateauje PONIZEJ (wtedy ostra stala jest mniejsza i P1 pada merytorycznie)
def gl(G,e,d,ts,ss,gam=1.0):
    o=np.argsort(ts);ts=np.asarray(ts)[o];ss=np.asarray(ss)[o]
    L=np.eye(2);t=0.0;W=np.zeros((2,2))
    for tj,s in zip(ts,ss):
        if tj>t: L=E(G,tj-t)@L
        t=tj;u=np.exp(-gam*s);w=(1.0-u)*(L.T@e)
        W=W+np.outer(w,w);L=(np.eye(2)-(1.0-u)*np.outer(d,d))@L
    return float(max(np.linalg.eigvalsh((W+W.T)/2)))/gam**2
for nm,G in [("diag(-1,-2)",np.diag([-1.,-2.])),("[[-1,1.9],[0,-1]]",np.array([[-1.,1.9],[0.,-1.]]))]:
    print(nm)
    for m in (5,8,16):
        print(f"  m={m}  sqrt(m)={np.sqrt(m):.10f}")
        for h in (1e-1,1e-2,1e-3,1e-4,1e-5,1e-6,1e-8):
            e=np.array([1.,0.]);d=np.array([0.,1.])
            v=np.sqrt(gl(G,e,d,h*np.arange(1,m+1),np.full(m,80.0)))
            print(f"    okno h={h:<8.0e} ||c||={v:.12f}  deficyt={np.sqrt(m)-v:.3e}")
