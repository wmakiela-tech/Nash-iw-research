// IW_MECH_S9_ROT003. Strict source-table conditional null gates, NOT author Julia/native PBH run.
// node mech_s9_rot003_neutrino_baryon_null.mjs ORIGINAL_N_around_m_e.csv
// SOURCE: Fenyutanchan/Primordial-Black-Hole, commit d395183674cace6c9906a8911bdeb7234ba4040d
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
if(!process.argv[2]) throw Error('Supply unmodified author N_around_m_e.csv');
const raw=readFileSync(process.argv[2]);
const blob=createHash('sha1').update(Buffer.from('blob '+raw.length+'\0')).update(raw).digest('hex');
const EXPECTED='93f2494f026c5d0587ea40fe08bb938dd9d01fa8';
if(blob!==EXPECTED)throw Error('Original source table git blob mismatch: '+blob);
const D=raw.toString('utf8').trim().split(/\r?\n/).map(z=>z.split(',').map(Number));
if(D.length!==1000||D.some((r,i)=>r.length!==3||r.some(x=>!Number.isFinite(x))||(i>0&&r[0]<=D[i-1][0])))throw Error('source grid contract failed');
const TT=D.map(z=>z[0]);
function state(T){
 if(T<TT[0]||T>TT.at(-1))throw Error('outside original temperature domain');
 let a=0,b=D.length-1;
 while(b-a>1){let m=(a+b)>>1;if(TT[m]<=T)a=m;else b=m;}
 const p=D[a],q=D[a+1],dl=Math.log(q[0]/p[0]),w=Math.log(T/p[0])/dl;
 const gr=p[1]+w*(q[1]-p[1]),gs=p[2]+w*(q[2]-p[2]);
 const qr=(q[1]-p[1])/(dl*gr),qs=(q[2]-p[2])/(dl*gs);
 const fcode=-4+qr/(3+qs),fadia=-3*(4+qr)/(3+qs);
 const dt_dlnT=(4+qr)/fcode;
 const entropy_drift=4*(qr-qs)/(4+qr);
 const baryon_proxy_drift=3+3*fcode/(4+qr);
 const direct_baryon_proxy_drift=3*qr*(4+qs)/((3+qs)*(4+qr));
 if(Math.abs(baryon_proxy_drift-direct_baryon_proxy_drift)>5e-14)throw Error('baryon log derivative identity');
 return {gr,gs,qr,qs,fcode,fadia,dt_dlnT,entropy_drift,baryon_proxy_drift};
}
const G2=[[-.5773502691896258,1],[.5773502691896258,1]];
const G4=[[-.8611363115940526,.3478548451374539],[-.3399810435848563,.6521451548625461],[.3399810435848563,.6521451548625461],[.8611363115940526,.3478548451374539]];
function integrate(Tini,Tend,G,key){
 let xx=[Tend,...TT.filter(t=>t>Tend&&t<Tini),Tini].map(Math.log).reverse(),ans=0;
 for(let i=0;i<xx.length-1;i++){let m=(xx[i]+xx[i+1])/2,h=(xx[i+1]-xx[i])/2;
 for(const [z,w]of G)ans+=h*w*state(Math.exp(m+h*z))[key];
 }return ans;
}
const Ti=1, Tf=.07818527068831995, gi=state(Ti).gs;
const lnAref=integrate(Ti,Tf,G4,'dt_dlnT');
const RBref=Math.exp(3*(lnAref+Math.log(Tf/Ti)));
const rows=[];
for(const T of [1,.8,.6,.5,.3,.2,.15,.1,Tf]){
 const L=integrate(Ti,T,G4,'dt_dlnT'), L2=integrate(Ti,T,G2,'dt_dlnT');
 const gs=state(T).gs;
 const L_entropy_conserving=-Math.log(T/Ti)-Math.log(gs/gi)/3;
 const RB=Math.exp(3*(L+Math.log(T/Ti)));
 const exp_neutrino_ratio=Math.exp(L-L_entropy_conserving);
 const Rentropy=Math.exp(3*(L-L_entropy_conserving));
 const Rb_adia=gi/gs;
 if(Math.abs(L2-L)>1e-9)throw Error('2/4 Gauss split-knots inconsistent at T='+T);
 if(Math.abs(RB/Rb_adia-Rentropy)>1e-10)throw Error('entropy/baryon decomposition identity at T='+T);
 rows.push({T_MeV:T,source_no_PBH_ln_a:L,comoving_entropy_proxy_ratio:Rentropy,
 source_Tnu_a_over_initial:exp_neutrino_ratio,source_fixed_eta_B_proxy_comoving_baryon_ratio:RB,
 fixed_late_eta_B_vs_conserved_baryon_density_nB_required_multiplier:RBref/RB,
 source_baryon_vs_entropy_factorization_check:RB/Rb_adia-Rentropy,
 integration_2node_4node_difference:L2-L});
}
console.log(JSON.stringify({status:'SOURCE_TABLE_SCALAR_NULL_NOT_NATIVE_JULIA_NOT_PHYSICAL_BBN',
 source_commit:'d395183674cace6c9906a8911bdeb7234ba4040d',
 table_git_blob:blob,source_rows:D.length,initial_T_MeV:Ti,late_calibration_T_MeV:Tf,
 note:'neutrino ratio is derived from manuscript Eq A1/2.7 and source thermo; baryon nB is author nB=etaB*n_gamma; no exact JCAP build identity, no 10D trajectory, no PBH contour',
 rows},null,2));
