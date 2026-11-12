// Mech-S9 ROT002. Source-native STATIC entropy-null check; NOT native Julia/physical PBH.
// Node.js >=18. Usage: node mech_s9_rot002_entropy_null_source.js PATH_TO_ORIGINAL_N_around_m_e.csv
// Freeze: Fenyutanchan/Primordial-Black-Hole @ d395183674cace6c9906a8911bdeb7234ba4040d
// Original Git blob N_around_m_e.csv = 93f2494f026c5d0587ea40fe08bb938dd9d01fa8
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
const raw=readFileSync(process.argv[2]||'');
const sha=createHash('sha1').update(Buffer.from('blob '+raw.length+'\0')).update(raw).digest('hex');
if(sha!=='93f2494f026c5d0587ea40fe08bb938dd9d01fa8') throw Error('FAIL original Git blob '+sha);
const rows=raw.toString('utf8').trim().split(/\r?\n/).map(s=>s.split(',').map(Number));
if(rows.length!==1000||rows.some(x=>x.length!==3||x.some(v=>!Number.isFinite(v))))throw Error('FAIL source 1000x3 table');
if(rows.some((x,i)=>i&&x[0]<=rows[i-1][0]))throw Error('FAIL nonincreasing temperature');
const knots=rows.map(x=>x[0]);
function stat(T){
 if(T<knots[0]||T>knots.at(-1))throw Error('out-of-source-table T');
 let lo=0,hi=rows.length-1;
 while(hi-lo>1){const m=(lo+hi)>>1;if(knots[m]<=T)lo=m;else hi=m}
 const a=rows[lo],b=rows[lo+1],span=Math.log(b[0]/a[0]),w=Math.log(T/a[0])/span;
 const gr=a[1]+w*(b[1]-a[1]),gs=a[2]+w*(b[2]-a[2]);
 const qr=(b[1]-a[1])/(span*gr),qs=(b[2]-a[2])/(span*gs);
 const fcode=-4+qr/(3+qs),fadiab=-3*(4+qr)/(3+qs);
 return {qr,qs,gr,gs,fcode,fadiab,local_diff:fcode-fadiab,
  entropy_drift:4*(qr-qs)/(4+qr),
  jcode:(4+qr)/fcode,jadiab:-(3+qs)/3};
}
const G2=[[-.5773502691896258,1],[.5773502691896258,1]];
const G4=[[-.8611363115940526,.3478548451374539],[-.3399810435848563,.6521451548625461],[.3399810435848563,.6521451548625461],[.8611363115940526,.3478548451374539]];
function integrate(hi,lo,k,gl){
 const z=[lo,...knots.filter(t=>t>lo&&t<hi),hi].map(Math.log).reverse();
 let a=0;
 for(let i=0;i<z.length-1;i++){const mid=(z[i]+z[i+1])/2, half=(z[i+1]-z[i])/2;
  for(const [x,w] of gl) a+=half*w*stat(Math.exp(mid+half*x))[k];}
 return a;
}
const checks=[];
for(const T of [.5,.2,.1,.07818527068831995,.05,.03]){
 const c4=integrate(1,T,'jcode',G4),a4=integrate(1,T,'jadiab',G4),d=c4-a4;
 const d2=integrate(1,T,'jcode',G2)-integrate(1,T,'jadiab',G2);
 if(Math.abs(d2-d)>1e-8)throw Error('FAIL quadrature convergence at '+T);
 checks.push({T_end_MeV:T,...stat(T),delta_ln_a:d,scale_ratio:Math.exp(d),
  comoving_entropy_ratio:Math.exp(3*d),quadrature_difference_2v4:d2-d});
}
console.log(JSON.stringify({status:'STATIC_TABLE_AND_EXACT_ALGEBRA_ONLY_NOT_JULIA',source_git_blob:sha,
 original_rows:rows.length,comparisons:checks},null,2));