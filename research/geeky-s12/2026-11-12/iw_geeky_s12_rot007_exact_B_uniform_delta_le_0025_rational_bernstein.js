#!/usr/bin/env node
"use strict";
/*
  IW Geeky-S12 ROT007 — 0 < delta <= 0.025 source-interval Bernstein certificate for
  N41 B, 5 masks, one positive gain, ALL 0 < delta <= 1/40.
  Runtime: Node >=18, stdlib only.
  Use: node <script> [exact M13 direct_B.json file]
  Without argument fetches the IMMUTABLE Git blob from the public GitHub API.
  Authors' historic dtc0a runtime NOT identified or executed here.
*/
const fs=require("fs"),crypto=require("crypto"),https=require("https");
const SOURCE_BLOB="a6f50fbe5904e580e84c87ee87c5ad043cdec5d0";
async function loadSource(){
  let bytes;
  if(process.argv[2]) bytes=fs.readFileSync(process.argv[2]);
  else {
    const url="https://api.github.com/repos/wmakiela-tech/Nash-iw-research/git/blobs/"+SOURCE_BLOB;
    const raw=await new Promise((resolve,reject)=>{
      https.get(url,{headers:{"Accept":"application/vnd.github+json","User-Agent":"Geeky-S12-ROT007-Bernstein-cert"}},r=>{
        if(r.statusCode!==200){reject(new Error("GitHub HTTP "+r.statusCode));r.resume();return;}
        const c=[];r.on("data",x=>c.push(x));r.on("end",()=>resolve(Buffer.concat(c)));r.on("error",reject);
      }).on("error",reject);
    });
    const b=JSON.parse(raw.toString("utf8"));
    if(b.encoding!=="base64"||!b.content)throw new Error("GitHub blob encoding fail");
    bytes=Buffer.from(b.content.replace(/\s/g,""),"base64");
  }
  const actual=crypto.createHash("sha1").update(Buffer.from("blob "+bytes.length+"\0")).update(bytes).digest("hex");
  if(actual!==SOURCE_BLOB)throw new Error("FROZEN SOURCE BLOB ID MISMATCH "+actual);
  return JSON.parse(bytes.toString("utf8"));
}
function certificate(source) {
 function fail(t){throw new Error("ROT007 CERTIFICATE FAIL: "+t);}
 const Z=[0n,1n],O=[1n,1n],abs=x=>x<0n?-x:x;
 function gcd(a,b){a=abs(a);b=abs(b);while(b){const r=a%b;a=b;b=r;}return a||1n;}
 function F(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)fail("zero denominator");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return [a/g,b/g];}
 const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
 const neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b));
 const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
 const cmp=(a,b)=>{const d=a[0]*b[1]-b[0]*a[1];return d<0n?-1:d>0n?1:0;};
 function decimal(s){
   s=s.trim();let sign=1n;
   if(s[0]==="-"){sign=-1n;s=s.slice(1);}else if(s[0]==="+")s=s.slice(1);
   const [m,e="0"]=s.toLowerCase().split("e"),[u,v=""]=m.split(".");
   const p=Number(e)-v.length,n=sign*BigInt((u||"0")+v);
   return p>=0?F(n*10n**BigInt(p)):F(n,10n**BigInt(-p));
 }
 const I=(a,b=a)=>[a,b],zero=()=>I(Z),one=()=>I(O);
 const ia=(a,b)=>I(add(a[0],b[0]),add(a[1],b[1]));
 const is=(a,b)=>I(sub(a[0],b[1]),sub(a[1],b[0]));
 function im(a,b){const vals=[mul(a[0],b[0]),mul(a[0],b[1]),mul(a[1],b[0]),mul(a[1],b[1])].sort(cmp);return I(vals[0],vals[3]);}
 function sq(a){
   if(cmp(a[0],Z)>=0)return I(mul(a[0],a[0]),mul(a[1],a[1]));
   if(cmp(a[1],Z)<=0)return I(mul(a[1],a[1]),mul(a[0],a[0]));
   const x=mul(a[0],a[0]),y=mul(a[1],a[1]);return I(Z,cmp(x,y)>0?x:y);
 }
 const scale=(a,k)=>im(a,I(k));
 function idiv(a,b){if(cmp(b[0],Z)<=0)fail("nonpositive interval denominator");return I(div(a[0],b[1]),div(a[1],b[0]));}
 function pow(x,n){let r=O;for(let j=0;j<n;j++)r=mul(r,x);return r;}
 function choose(n,k){if(k<0||k>n)return 0n;let z=1n;for(let j=1;j<=k;j++)z=z*BigInt(n-j+1)/BigInt(j);return z;}
 const arr=n=>Array.from({length:n},zero);
 const pa=(a,b)=>Array.from({length:Math.max(a.length,b.length)},(_,i)=>ia(a[i]||zero(),b[i]||zero()));
 const ps=(a,b)=>Array.from({length:Math.max(a.length,b.length)},(_,i)=>is(a[i]||zero(),b[i]||zero()));
 function pm(a,b){let r=arr(a.length+b.length-1);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)r[i+j]=ia(r[i+j],im(a[i],b[j]));return r;}
 const pc=(a,k)=>a.map(v=>scale(v,k));
 function pshift(a,h){
   let r=arr(a.length);
   for(let j=0;j<a.length;j++)for(let i=0;i<=j;i++)
     r[i]=ia(r[i],scale(a[j],mul(F(choose(j,i)),pow(h,j-i))));
   return r;
 }
 function bern(c,a,b){
   const n=c.length-1,mon=arr(n+1),dx=sub(b,a);
   for(let j=0;j<=n;j++)for(let i=0;i<=j;i++)
     mon[i]=ia(mon[i],scale(c[j],mul(F(choose(j,i)),mul(pow(a,j-i),pow(dx,i)))));
   const B=arr(n+1);
   for(let i=0;i<=n;i++)for(let j=0;j<=i;j++)
     B[i]=ia(B[i],scale(mon[j],div(F(choose(i,j)),F(choose(n,j)))));
   return B;
 }
 function min1(c,a,b){let lo=null;for(const x of bern(c,a,b))if(lo===null||cmp(x[0],lo)<0)lo=x[0];return lo;}
 function min2(c,a,b,d,e){
   const r=c.length,s=c[0].length,B=Array.from({length:r},()=>arr(s));
   for(let j=0;j<s;j++){let col=bern(c.map(z=>z[j]),a,b);for(let i=0;i<r;i++)B[i][j]=col[i];}
   let lo=null;for(let i=0;i<r;i++)for(const x of bern(B[i],d,e))if(lo===null||cmp(x[0],lo)<0)lo=x[0];return lo;
 }
 function approx(f){
   if(f[0]===0n)return 0;const sign=f[0]<0n?-1:1;
   const nu=abs(f[0]).toString(),de=f[1].toString(),a=nu.slice(0,16),b=de.slice(0,16);
   return sign*(Number(a)/10**(a.length-1))/(Number(b)/10**(b.length-1))*10**(nu.length-de.length);
 }
 function endpoint(s){
   if(!s.startsWith("[")||!s.endsWith("]"))fail("directed decimal syntax");
   return decimal(s.slice(1,-1).split(",")[0]);
 }
 const K=[2,3,4,5,6],N=K.map(k=>BigInt((41-2*k)**3)),
   W=N.map((v,i)=>i<4?v-N[i+1]:v),inputScale=F(10n**12n);
 const a0=F(0),aMax=F(1,5),edge=F(1,125),deltaMax=F(1,40),cut=F(7,250);
 const G=K.map(k=>source[k].map(pair=>{
   const x=mul(endpoint(pair[0]),inputScale),y=mul(endpoint(pair[1]),inputScale);
   if(cmp(x,y)>0)fail("inverted original interval");
   return I(x,y);
 }));
 const C=G.map((row,i)=>row.map((v,j)=>idiv(
   is(scale(v,F(N[i])),i<4?scale(G[i+1][j],F(N[i+1])):zero()),I(F(W[i]))
 )));
 const shellMin=C.map(c=>min1(c,a0,aMax));
 shellMin.forEach((x,i)=>{if(cmp(x,Z)<=0)fail("shell not positive k="+K[i]);});
 const P=Array.from({length:4},()=>arr(10)),Qpairs=[];
 for(let i=0;i<5;i++)for(let j=i+1;j<5;j++){
   const Q=Array.from({length:4},()=>arr(4)),R=arr(7);
   for(let m=1;m<=4;m++)for(let n=0;n<m;n++){
     const d=is(im(C[i][m],C[j][n]),im(C[j][m],C[i][n]));
     for(let t=0;t<m-n;t++)Q[m-1-t][n+t]=ia(Q[m-1-t][n+t],d);
   }
   for(let m=0;m<=4;m++)for(let n=0;n<=4;n++)if(m!==n)
     R[m+n-1]=ia(R[m+n-1],scale(im(C[i][m],C[j][n]),F(m-n)));
   for(let m=0;m<4;m++)for(let n=0;n<4;n++)for(let t=0;t<7;t++)
     P[m][n+t]=ia(P[m][n+t],scale(im(Q[m][n],R[t]),F(2n*W[i]*W[j])));
   Qpairs.push({i,j,Q});
 }
 // H=(alpha-beta)P, H=2(p_beta q)-p(q_beta).
 // The following THREE boxes exactly tile [0,0.2]x[0.01,0.2].
 const certifiedBox=[
   [F(0),F(1,10),F(1,125),F(1,50)],
   [F(0),F(1,10),F(1,50),F(21,200)],
   [F(0),F(1,10),F(21,200),F(1,5)],
   [F(1,10),F(1,5),F(1,125),F(1,50)],
   [F(1,10),F(1,5),F(1,50),F(1,5)]
 ];
 const pBig=certifiedBox.map(z=>min2(P,...z));
 const pSmall=min2(P,F(0),cut,F(0),edge);
 const dP=P.map(row=>Array.from({length:9},(_,j)=>scale(row[j+1],F(j+1))));
 const dpSmall=min2(dP,cut,aMax,F(0),edge);
 // F0(alpha)=N(alpha,0)*q(alpha-deltaMax)-N(alpha,alpha-deltaMax)*q(0).
 // N(alpha,beta)=sum_(i<j) w_i w_j (s_i(alpha)s_j(beta)-s_j(alpha)s_i(beta))^2.
 const Cshift=C.map(c=>pshift(c,neg(deltaMax)));
 const q0=C.reduce((r,c,i)=>ia(r,scale(sq(c[0]),F(W[i]))),zero());
 const qNear=Cshift.reduce((r,c,i)=>pa(r,pc(pm(c,c),F(W[i]))),[zero()]);
 let N0=[zero()],Nnear=[zero()];
 for(const {i,j,Q} of Qpairs){
   const A0=ps(C[i].map(x=>im(x,C[j][0])),C[j].map(x=>im(x,C[i][0])));
   A0[0]=zero(); // exact symbolic cancellation c_i0*c_j0-c_j0*c_i0
   N0=pa(N0,pc(pm(A0,A0),F(W[i]*W[j])));
   let Qnear=[zero()];
   for(let m=0;m<4;m++)for(let n=0;n<4;n++){
     const mon=Array.from({length:n+1},(_,k)=>k===n?one():zero());
     const term=Array.from({length:m},zero).concat(pshift(mon,neg(deltaMax)));
     Qnear=pa(Qnear,term.map(x=>im(x,Q[m][n])));
   }
   Nnear=pa(Nnear,pc(pm(Qnear,Qnear),mul(mul(deltaMax,deltaMax),F(W[i]*W[j]))));
 }
 const F0=ps(pm(N0,qNear),Nnear.map(x=>im(x,q0)));
 // ROT007: full-interval Bernstein for F0 at deltaMax=0.025 is negative
 // (the Bernstein bound, NOT the polynomial). Subdivide into eight rational
 // intervals with individually STRICT positive exact directed interval bounds.
 const f0Segments=[
   [F(7,250),F(3,100)],
   [F(3,100),F(4,125)],
   [F(4,125),F(33,1000)],
   [F(33,1000),F(7,200)],
   [F(7,200),F(1,25)],
   [F(1,25),F(1,20)],
   [F(1,20),F(1,10)],
   [F(1,10),F(1,5)]
 ];
 const f0Bounds=f0Segments.map(([l,h])=>min1(F0,l,h));
 // ROT007: exact 1D polynomial along the slanted boundary beta=alpha-0.025.
 // P is a bivariate polynomial, constructed above by exact interval algebra.
 // alpha in [0.028,0.033] gives beta=alpha-0.025 in [0.003,0.008].
 let Pline=[zero()];
 for(let i=0;i<P.length;i++)for(let j=0;j<P[i].length;j++){
   const mon=Array.from({length:j+1},(_,k)=>k===j?one():zero());
   const term=Array.from({length:i},zero).concat(pshift(mon,neg(deltaMax)));
   Pline=pa(Pline,term.map(x=>im(x,P[i][j])));
 }
 const pLineSegments=[[F(7,250),F(3,100)],[F(3,100),F(33,1000)]];
 const pLineBounds=pLineSegments.map(([l,h])=>min1(Pline,l,h));

   // Exactly 5 + 1 + 1 + 8 + 2 = 17 polynomial Bernstein positivity tests.
  // Plus 5 separate positive-shell energy tests. Literal strict exact
  // rational comparisons; reported Number values are for display ONLY.
const all=[...pBig,pSmall,dpSmall,...f0Bounds,...pLineBounds];
 all.forEach((z,i)=>{if(cmp(z,Z)<=0)fail("Bernstein certificate #"+i+" lower <=0, approximately "+approx(z));});
 return {
  artifact_id:"IW_GEEKY_S12_ROT007_M13_B_ALL_SMALL_DELTA_UP_TO_0025_GLOBAL_NEAREST_ENDPOINT_CERTIFICATE_001_20261112",
  immutable_M13_B_blob:SOURCE_BLOB,
  exact_source_interval_calculation:true,
  n:41,masks:K,weights:W.map(String),polynomial_sign_gates:all.length,shell_positive_gates:shellMin.length,delta_uniform_range:"0 < delta <= 1/40",critical_alpha_cut:"7/250",exceptional_beta_cut:"1/125",critical_alpha_line_upper:"33/1000",
  shell_positivity_lower_bounds_in_scale_1e12:shellMin.map(approx),
  P_big_domain_five_rectangles_Bernstein_lower:pBig.map(approx),
  P_small_alpha_le_0p028_beta_le_0p008_Bernstein_lower:approx(pSmall),
  derivative_beta_P_alpha_ge_0p028_beta_le_0p008_Bernstein_lower:approx(dpSmall),
  F0_at_delta_0p025_alpha_ge_0p028_subdivision_Bernstein_lower:f0Bounds.map(approx),
  P_along_beta_alpha_minus_0p025_alpha_0p028_to_0p033_Bernstein_lower:pLineBounds.map(approx),
  sign_decisions:"ALL 17 EXACT RATIONAL INTERVAL BERNSTEIN GATES PASS",
  conclusion:"For every alpha in [0,0.2] and EVERY real delta with 0 < delta <= 0.025, the global D_B² minimizer over beta in [0,0.2] with |beta-alpha| >= delta is among the closest legal endpoints alpha-delta and alpha+delta.",
  limits:"Functionally matched M13 auxiliary coefficients ONLY, not byte-identical historic producer, not physical K/J3/TPE, no scientific canon or EXEC."
 };
}
(async()=>{
  const result=certificate(await loadSource());
  console.log(JSON.stringify(result,null,2));
})().catch(e=>{console.error(e.stack||String(e));process.exitCode=1;});
