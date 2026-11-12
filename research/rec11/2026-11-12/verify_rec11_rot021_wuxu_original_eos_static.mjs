// REC11 ROT021 original Wu-Xu 1000x3 degrees of freedom source recheck.
// Source: Fenyutanchan/Primordial-Black-Hole d395183, arXiv-2509.05618/data/ext/N_around_m_e.csv
// Original table Git blob SHA1: 93f2494f026c5d0587ea40fe08bb938dd9d01fa8
// Static source comparison only, NO Julia/BBN/PBH execution, NO novelty.
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';

function verifyCSV(csv){
  const rowsText=csv.trim().split(/\r?\n/).map(x=>x.split(","));
  if(rowsText.length!==1000 || rowsText.some(r=>r.length!==3))throw Error("Expected original 1000x3 rows");
  const rows=rowsText.map(r=>r.map(Number));
  if(rows.some(r=>r.some(x=>!Number.isFinite(x)||x<=0)))throw Error("Invalid source positives");
  if(rows.some((r,i)=>i>0&&r[0]<=rows[i-1][0]))throw Error("Nonascending temperatures");
  const decimal=s=>{
    const [b,ex="0"]=s.toLowerCase().split("e"),sign=b.startsWith("-")?-1n:1n;
    const p=b.replace("-","").split("."),digits=p.join("");
    let n=sign*BigInt(digits),k=(p[1]||"").length-Number(ex);
    if(k<0){n*=10n**BigInt(-k);k=0}
    return [n,10n**BigInt(k)];
  };
  const sub=(a,b)=>[a[0]*b[1]-b[0]*a[1],a[1]*b[1]];
  const mul=(a,b)=>[a[0]*b[0],a[1]*b[1]];
  let signs={positive:0,negative:0,zero:0};
  for(let i=0;i<999;i++){
    const a=rowsText[i].map(decimal),b=rowsText[i+1].map(decimal);
    const d=sub(mul(sub(b[1],a[1]),a[2]),mul(sub(b[2],a[2]),a[1]));
    signs[d[0]>0n?"positive":d[0]<0n?"negative":"zero"]++;
  }
  function at(T){
    if(T<rows[0][0]||T>rows[999][0])throw Error("temperature out of frozen table");
    let lo=0,hi=999;while(hi-lo>1){const m=(lo+hi)>>1;if(rows[m][0]<=T)lo=m;else hi=m}
    const [ta,ra,sa]=rows[lo],[tb,rb,sb]=rows[lo+1];
    const d=Math.log(tb/ta),u=Math.log(T/ta)/d,gr=ra+(rb-ra)*u,gs=sa+(sb-sa)*u;
    const qr=(rb-ra)/(d*gr),qs=(sb-sa)/(d*gs);
    const fc=-4+qr/(3+qs),fa=-3*(4+qr)/(3+qs);
    return {T,gr,gs,qr,qs,f_code:fc,f_adiab:fa,
      delta_rhs:fc-fa,j_code:(4+qr)/fc,j_adiab:-(3+qs)/3};
  }
  const n3=[[-Math.sqrt(3/5),5/9],[0,8/9],[Math.sqrt(3/5),5/9]];
  const a=Math.sqrt(5-2*Math.sqrt(10/7))/3,b=Math.sqrt(5+2*Math.sqrt(10/7))/3,s70=Math.sqrt(70);
  const n5=[[-b,(322-13*s70)/900],[-a,(322+13*s70)/900],[0,128/225],[a,(322+13*s70)/900],[b,(322-13*s70)/900]];
  function integrate(hi,lo,nodes,kind="delta"){
    const knots=[hi,...rows.filter(r=>lo<r[0]&&r[0]<hi).map(r=>r[0]).reverse(),lo];
    let acc=0;
    for(let i=0;i<knots.length-1;i++){
      const A=Math.log(knots[i]),B=Math.log(knots[i+1]),mid=(A+B)/2,half=(B-A)/2;
      for(const [x,w] of nodes){
        const z=at(Math.exp(mid+half*x));
        const value=kind==="delta"?(z.j_code-z.j_adiab):(3*z.j_code+3+z.qs);
        acc+=half*w*value;
      }
    }
    return acc;
  }
  const temperatures=[.5,.2,.1,.099689,.07818527068831995,.05,.03];
  const samples=temperatures.map(T=>{
    const g3=integrate(1,T,n3),g5=integrate(1,T,n5),entropy=integrate(1,T,n5,"entropy");
    return {T_MeV:T,delta_ln_a:g5,a_code_over_a_adiab:Math.exp(g5),
      effective_entropy_ratio:Math.exp(entropy),quadrature_delta:g5-g3,
      entropy_internal_error:entropy-3*g5};
  });
  const inv=[];
  for(let j=0;j<1000;j++){
    const logT=-2+j*8/999,T=10**logT;
    if(T>=rows[0][0]&&T<=rows[999][0])inv.push({logT,logR:Math.log10(at(T).gr*T**4)});
  }
  const errs=[];
  for(const [T] of rows){
    if(T<.03||T>1)continue;
    const q=Math.log10(at(T).gr*T**4);
    let l=0,h=inv.length-1;while(h-l>1){const m=(l+h)>>1;if(inv[m].logR<=q)l=m;else h=m}
    const w=(q-inv[l].logR)/(inv[h].logR-inv[l].logR);
    const estimated=10**(inv[l].logT+w*(inv[h].logT-inv[l].logT));
    errs.push({T,relative:estimated/T-1});
  }
  const worst=errs.reduce((a,b)=>Math.abs(b.relative)>Math.abs(a.relative)?b:a,{T:0,relative:0});
  return {source_original_1000_rows:rows.length,source_999_segment_exact_decimal_signs:signs,
    at_0p1_MeV:at(.1),integrated_1MeV_to_T:samples,
    source_rho_to_T_table_static_inverse:{original_nodes_in_0p03_to_1MeV:errs.length,
    maximum_absolute_relative:Math.abs(worst.relative),at_MeV:worst.T,
    mean_absolute_relative:errs.reduce((s,x)=>s+Math.abs(x.relative),0)/errs.length},
    guard:"SOURCE_STATIC_NUMERIC_AND_EXACT_RATIONAL_SIGN_ONLY_NO_JULIA_NO_PHYSICAL_PBH_NO_CANON"};
}

const file=process.argv[2];
if(!file)throw Error('Usage: node verify_rec11_rot021_wuxu_eos.mjs ORIGINAL_N_around_m_e.csv');
const raw=readFileSync(file);
const sha=createHash('sha1').update(Buffer.from('blob '+raw.length+'\\0'.replace('\\0','\\0'))).update(raw).digest('hex');
if(sha!=='93f2494f026c5d0587ea40fe08bb938dd9d01fa8')throw Error('FAIL original Git blob '+sha);
console.log(JSON.stringify({...verifyCSV(raw.toString('utf8')),original_git_blob:sha},null,2));
