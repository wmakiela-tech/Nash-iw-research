#!/usr/bin/env node
"use strict";
/* M15 ROT006: independently authored source-B 25-coefficient exact-rational
   5 shell + 17 Bernstein certificate. No Geeky ROT007/013 code imports/calls.
   Run node this_file.js path/to/direct_B.json (Node 18+ stdlib).
   Original M13 source Git blob is verified fail-closed.
*/
function independentCertificate(src) {
 const abs=n=>n<0n?-n:n;
 function gcd(a,b){a=abs(a);b=abs(b);while(b){let t=a%b;a=b;b=t;}return a||1n;}
 function F(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("DIV_ZERO");if(b<0n){a=-a;b=-b;}let g=gcd(a,b);return [a/g,b/g];}
 const zero=F(0),one=F(1);
 const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
 const sub=(a,b)=>add(a,[-b[0],b[1]]);
 const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]);
 const div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
 const cmp=(a,b)=>{let v=a[0]*b[1]-b[0]*a[1];return v<0n?-1:v>0n?1:0;};
 function parse(s) {s=s.trim();let sg=1n;if(s.startsWith("-")){sg=-1n;s=s.slice(1);}else if(s.startsWith("+"))s=s.slice(1);let [base,expo="0"]=s.toLowerCase().split("e"),[u,v=""]=base.split("."),p=Number(expo)-v.length;let n=sg*BigInt((u||"0")+v);return p>=0?F(n*10n**BigInt(p)):F(n,10n**BigInt(-p));}
 function originalBound(s) {if(!s.startsWith("[")||!s.includes(","))throw Error("B bracket");return parse(s.slice(1,s.indexOf(",")));}
 const magnitude=x=>[abs(x[0]),x[1]];
 function I(a,b=a){if(cmp(a,b)>0)throw Error("BAD_INTERVAL");return[a,b];}
 const iz=()=>I(zero);
 const iadd=(a,b)=>I(add(a[0],b[0]),add(a[1],b[1]));
 const isub=(a,b)=>I(sub(a[0],b[1]),sub(a[1],b[0]));
 function imul(a,b){let xs=[mul(a[0],b[0]),mul(a[0],b[1]),mul(a[1],b[0]),mul(a[1],b[1])].sort(cmp);return I(xs[0],xs[3]);}
 const iscale=(a,r)=>imul(a,I(r));
 const isquare=a=>{if(cmp(a[0],zero)>=0)return I(mul(a[0],a[0]),mul(a[1],a[1]));if(cmp(a[1],zero)<=0)return I(mul(a[1],a[1]),mul(a[0],a[0]));let u=mul(a[0],a[0]),v=mul(a[1],a[1]);return I(zero,cmp(u,v)>0?u:v);};
 const iposdiv=(a,b)=>{if(cmp(b[0],zero)<=0)throw Error("DENOM_NONPOS");return I(div(a[0],b[1]),div(a[1],b[0]));};
 const Q=(a,b=1)=>F(BigInt(a),BigInt(b));
 function choose(n,k){if(k<0||k>n)return 0n;let r=1n;for(let j=1;j<=k;j++)r=r*BigInt(n-j+1)/BigInt(j);return r;}
 function pow(v,n){let r=one;for(let i=0;i<n;i++)r=mul(r,v);return r;}
 function pplus(a,b){let o=Array.from({length:Math.max(a.length,b.length)},iz);for(let k=0;k<o.length;k++)o[k]=iadd(a[k]||iz(),b[k]||iz());return o;}
 function pminus(a,b){let o=Array.from({length:Math.max(a.length,b.length)},iz);for(let k=0;k<o.length;k++)o[k]=isub(a[k]||iz(),b[k]||iz());return o;}
 const pscale=(a,r)=>a.map(v=>iscale(v,r));
 const pmulI=(a,b)=>a.map(v=>imul(v,b));
 function pmul(a,b){let o=Array.from({length:a.length+b.length-1},iz);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)o[i+j]=iadd(o[i+j],imul(a[i],b[j]));return o;}
 function shifted(a,h){let o=Array.from({length:a.length},iz);for(let j=0;j<a.length;j++)for(let k=0;k<=j;k++)o[k]=iadd(o[k],iscale(a[j],mul(Q(choose(j,k)),pow(h,j-k))));return o;}
 function bern(a,left,right){
   let n=a.length-1,step=sub(right,left),mon=Array.from({length:n+1},iz);
   for(let j=0;j<=n;j++)for(let k=0;k<=j;k++)
     mon[k]=iadd(mon[k],iscale(a[j],mul(Q(choose(j,k)),mul(pow(left,j-k),pow(step,k)))));
   let o=Array.from({length:n+1},iz);
   for(let k=0;k<=n;k++)for(let j=0;j<=k;j++)
     o[k]=iadd(o[k],iscale(mon[j],div(Q(choose(k,j)),Q(choose(n,j)))));
   return o;
 }
 function bmin(a,left,right){let lo=null;for(const x of bern(a,left,right)){if(lo===null||cmp(x[0],lo)<0)lo=x[0];}return lo;}
 function bmin2(P,alo,ahi,blo,bhi){
  const nr=P.length,nc=P[0].length;
  let half=Array.from({length:nr},()=>Array.from({length:nc},iz));
  for(let j=0;j<nc;j++){let x=bern(P.map(row=>row[j]),alo,ahi);for(let i=0;i<nr;i++)half[i][j]=x[i];}
  let lo=null;for(const row of half)for(const x of bern(row,blo,bhi)){if(lo===null||cmp(x[0],lo)<0)lo=x[0];}return lo;
 }
 const zeros=(m,n)=>Array.from({length:m},()=>Array.from({length:n},iz));
 function diagonal(M,shift) { // beta=alpha+shift, returns 1D polynomial
   let out=Array.from({length:M.length+M[0].length-1},iz);
   for(let i=0;i<M.length;i++)for(let j=0;j<M[i].length;j++)for(let h=0;h<=j;h++)
     out[i+h]=iadd(out[i+h],iscale(M[i][j],mul(Q(choose(j,h)),pow(shift,j-h))));
   return out;
 }
 const K=[2,3,4,5,6],ns=K.map(k=>BigInt((41-2*k)**3)),ws=ns.map((n,i)=>i<4?n-ns[i+1]:n);
 const eps=Q(1n,10000000n),scale=F(1000000000000n);
 const G=K.map(k=>{
  if(!Array.isArray(src[k])||src[k].length!==5)throw Error("M13_SOURCE_SHAPE");
  return src[k].map(pair=>{
   let lo=originalBound(pair[0]),hi=originalBound(pair[1]);if(cmp(lo,hi)>0)throw Error("SOURCE_ORDER");
   return imul(I(sub(lo,mul(eps,magnitude(lo))),add(hi,mul(eps,magnitude(hi)))),I(scale));
  });
 });
 const S=G.map((row,i)=>row.map((v,j)=>iposdiv(i===4?iscale(v,F(ns[i])):isub(iscale(v,F(ns[i])),iscale(G[i+1][j],F(ns[i+1]))),I(F(ws[i])))));
 const left=F(0),right=F(1n,5n),acut=F(7n,250n),bcut=F(1n,125n),D=F(1n,40n);
 const shell=S.map(c=>bmin(c,left,right));
 if(shell.some(x=>cmp(x,left)<=0))throw Error("SHELL_SIGN_FAIL");
 // Construct wedge quotient Qij=(si(a)sj(b)-sj(a)si(b))/(a-b)
 // directly as finite antisymmetric monomial sum, without numeric division.
 const polys=[],P=zeros(4,10);
 for(let i=0;i<5;i++)for(let j=i+1;j<5;j++){
   let W=zeros(4,4);
   for(let m=1;m<=4;m++)for(let n=0;n<m;n++){
     let c=isub(imul(S[i][m],S[j][n]),imul(S[i][n],S[j][m]));
     for(let t=0;t<m-n;t++)W[m-1-t][n+t]=iadd(W[m-1-t][n+t],c);
   }
   // independent direct monomial coefficient of R=si'(b)sj(b)-si(b)sj'(b)
   let R=Array.from({length:7},iz);
   for(let m=0;m<=4;m++)for(let n=0;n<=4;n++)if(m!==n){
     R[m+n-1]=iadd(R[m+n-1],iscale(imul(S[i][m],S[j][n]),F(m-n)));
   }
   for(let a=0;a<4;a++)for(let b=0;b<4;b++)for(let c=0;c<7;c++){
     P[a][b+c]=iadd(P[a][b+c],iscale(imul(W[a][b],R[c]),F(2n*ws[i]*ws[j])));
   }
   polys.push({i,j,W});
 }
 const rect=[
   [F(0),F(1n,10n),bcut,F(1n,50n)],
   [F(0),F(1n,10n),F(1n,50n),F(21n,200n)],
   [F(0),F(1n,10n),F(21n,200n),right],
   [F(1n,10n),right,bcut,F(1n,50n)],
   [F(1n,10n),right,F(1n,50n),right]
 ];
 const pbig=rect.map(t=>bmin2(P,...t));
 const psmall=bmin2(P,left,acut,left,bcut);
 const pbeta=P.map(row=>row.slice(1).map((v,j)=>iscale(v,F(j+1))));
 const pderiv=bmin2(pbeta,acut,right,left,bcut);
 const negativeD=F(-D[0],D[1]);
 const linepoly=diagonal(P,negativeD);
 const lines=[[acut,F(3n,100n)],[F(3n,100n),F(33n,1000n)]].map(t=>bmin(linepoly,...t));
 // Independent polynomial construction of F0:
 // N(a,0)=sum Wij (si(a)sj(0)-sj(a)si(0))^2.
 // N(a,a-D)=D^2 sum Wij Qij(a,a-D)^2.
 let n0=[iz()],nNear=[iz()];
 for(const {i,j,W} of polys){
   const A=pmulI(S[i],S[j][0]),B=pmulI(S[j],S[i][0]);
   const v=pminus(A,B);v[0]=iz(); // formal zero antisymmetry
   n0=pplus(n0,pscale(pmul(v,v),F(ws[i]*ws[j])));
   const qline=diagonal(W,negativeD);
   nNear=pplus(nNear,pscale(pmul(qline,qline),mul(mul(D,D),F(ws[i]*ws[j]))));
 }
 const q0=S.reduce((acc,row,i)=>iadd(acc,iscale(isquare(row[0]),F(ws[i]))),iz());
 let qnear=[iz()];
 for(let i=0;i<5;i++){
   const polynomial=shifted(S[i],negativeD);
   qnear=pplus(qnear,pscale(pmul(polynomial,polynomial),F(ws[i])));
 }
 const Fzero=pminus(pmul(n0,qnear),pmulI(nNear,q0));
 const spans=[
   [F(7n,250n),F(3n,100n)],
   [F(3n,100n),F(4n,125n)],
   [F(4n,125n),F(33n,1000n)],
   [F(33n,1000n),F(7n,200n)],
   [F(7n,200n),F(1n,25n)],
   [F(1n,25n),F(1n,20n)],
   [F(1n,20n),F(1n,10n)],
   [F(1n,10n),F(1n,5n)]
 ];
 const f0=spans.map(t=>bmin(Fzero,...t));
 const all=[...pbig,psmall,pderiv,...f0,...lines];
 if(all.length!==17||shell.length!==5)throw Error("BAD_17_5_COUNT");
 const signs=all.map((v,i)=>({i,positive:cmp(v,left)>0}));
 const failed=signs.filter(v=>!v.positive);
 function sci(v){
  if(v[0]===0n)return "0";let a=abs(v[0]).toString(),b=v[1].toString(),na=a.slice(0,15),nb=b.slice(0,15);
  let m=Number(na)/10**(na.length-1)/(Number(nb)/10**(nb.length-1)),e=a.length-b.length;
  if(m>=10){m/=10;e++}if(m<1){m*=10;e--}return(v[0]<0n?"-":"")+m.toPrecision(12)+"e"+(e>=0?"+":"")+e;
 }
 return {
  artifact_id:"IW_M15_ROT006_INDEPENDENT_FULL_M13_B25_17_BERNSTEIN_SOURCE_AUDIT_001_20261113",
  original_blob:"a6f50fbe5904e580e84c87ee87c5ad043cdec5d0",
  method:"Independent rational interval polynomial assembly; exact formal antisymmetry quotient; tensor Bernstein on source widened by 1e-7",
  source_coefficients:25,epsilon:"1/10000000",source_scale:"1e12",
  shell_lower:shell.map(sci),
  five_P_rectangles:pbig.map(sci),small_P:sci(psmall),small_P_beta:sci(pderiv),
  F0_eight_segments:f0.map(sci),P_shifted_two_segments:lines.map(sci),
  strictly_positive_polynomial_gates:17-failed.length,
  strictly_positive_shell_gates:shell.filter(v=>cmp(v,left)>0).length,
  all_gates_pass:failed.length===0,
  failed_gates:failed,
  ceiling:"I1_NONBLIND_INDEPENDENT_17_SOURCE_MATH_GATES_ONLY_NO_HISTORICAL_RUNTIME_NO_PHYSICS_NO_CANON_NO_EXEC"
 };
}
if(typeof module!=="undefined"&&require.main===module) {
 const fs=require("fs"),crypto=require("crypto"),path=require("path");
 const filename=process.argv[2];if(!filename)throw Error("Pass original M13 direct_B.json");
 const bytes=fs.readFileSync(filename);
 const blob=crypto.createHash("sha1").update(Buffer.from("blob "+bytes.length+"\0")).update(bytes).digest("hex");
 if(blob!=="a6f50fbe5904e580e84c87ee87c5ad043cdec5d0")throw Error("SOURCE_GIT_BLOB_MISMATCH");
 const out=independentCertificate(JSON.parse(bytes.toString("utf8")));
 fs.writeFileSync(path.join(path.dirname(__filename),"m15_rot006_exact_17_gates.json"),JSON.stringify(out,null,2)+"\n");
 process.stdout.write(JSON.stringify(out,null,2)+"\n");
 if(!out.all_gates_pass)process.exitCode=1;
}
