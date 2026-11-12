#!/usr/bin/env node
"use strict";
/*
 * Geeky-S12 ROT008: independent N41 Fourier source coefficient control.
 * Implements explicit complex arithmetic and DIRECT finite mask sums;
 * it does NOT import or use the M13 mpmath interval/window_mode code.
 * Original M13 source FIRST; this is an independent FLOAT64 cross-runtime
 * functional-alignment check, NOT directed interval proof or historical
 * dtc0a_runtime_v0_3_1.py byte identity.
 *
 * node iw_geeky_s12_rot008_independent_complex_fourier_mask_25_coeff_reproducer.js
 * node iw_geeky_s12_rot008_independent_complex_fourier_mask_25_coeff_reproducer.js /path/to/original/direct_B.json
 */
const fs=require("fs"),crypto=require("crypto"),https=require("https");
const ORIGINAL_M13_GIT_BLOB="a6f50fbe5904e580e84c87ee87c5ad043cdec5d0";
async function load(){
 let bytes;
 if(process.argv[2])bytes=fs.readFileSync(process.argv[2]);
 else {
  let raw=await new Promise((resolve,reject)=>{
   https.get("https://api.github.com/repos/wmakiela-tech/Nash-iw-research/git/blobs/"+ORIGINAL_M13_GIT_BLOB,
   {headers:{"Accept":"application/vnd.github+json","User-Agent":"Geeky-S12-ROT008-source-crosscontrol"}},r=>{
    if(r.statusCode!==200){r.resume();reject(new Error("GitHub HTTP "+r.statusCode));return;}
    const v=[];r.on("data",b=>v.push(b));r.on("end",()=>resolve(Buffer.concat(v)));r.on("error",reject);
   }).on("error",reject);
  });
  const j=JSON.parse(raw.toString("utf8"));
  if(j.encoding!=="base64"||!j.content)throw Error("Unrecognized Git blob response");
  bytes=Buffer.from(j.content.replace(/\s/g,""),"base64");
 }
 const gitSHA=crypto.createHash("sha1").update(Buffer.from("blob "+bytes.length+"\0")).update(bytes).digest("hex");
 if(gitSHA!==ORIGINAL_M13_GIT_BLOB)throw Error("ORIGINAL_SOURCE_BLOB_MISMATCH "+gitSHA);
 return JSON.parse(bytes.toString("utf8"));
}
function verify(source,options={}){
 const N=41,dx=2*Math.PI/N,Z=[0,0];
 const cadd=(a,b)=>[a[0]+b[0],a[1]+b[1]],
       csub=(a,b)=>[a[0]-b[0],a[1]-b[1]],
       cmul=(a,b)=>[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]],
       csc=(a,r)=>[r*a[0],r*a[1]],
       conj=a=>[a[0],-a[1]];
 const vec0=()=>Array.from({length:3},()=>[0,0]);
 const mat0=()=>Array.from({length:3},vec0);
 const kvec=m=>m.join(","),unkey=k=>k.split(",").map(Number);
 const vadd=(a,b)=>a.map((x,i)=>cadd(x,b[i]));
 const madd=(a,b)=>a.map((r,i)=>r.map((x,j)=>cadd(x,b[i][j])));
 const msub=(a,b)=>a.map((r,i)=>r.map((x,j)=>csub(x,b[i][j])));
 const msc=(a,s)=>a.map(r=>r.map(x=>csc(x,s)));
 const put=(m,k,value,plus)=>m.set(k,m.has(k)?plus(m.get(k),value):value);
 const C1=new Map(),C2=new Map(),h=new Map();
 for(const sign of [-1,1]){
  let a=vec0(),b=vec0();a[0]=[0,-sign/40*(1+(options.perturbC1||0))];b[2]=[0,-sign/50];
  C1.set(kvec([sign,0,0]),a);C2.set(kvec([sign,0,0]),b);
  a=vec0();a[1]=[1/40,0];C1.set(kvec([0,sign,0]),a);
  b=vec0();b[0]=[1/50,0];C2.set(kvec([0,0,sign]),b);
  for(const t of [-1,1]){
   const H=mat0();for(let j=0;j<3;j++)H[j][j]=[0,-sign/40];
   h.set(kvec([sign,t,0]),H);
  }
 }
 const deriv=m=>m.map(t=>[0,Math.sin(t*dx)/dx]);
 const filterMultiplier=(m,a)=>1+2*a*m.reduce((u,t)=>u+Math.cos(t*dx)-1,0);
 function bracket(A,B){
  const out=new Map();
  for(const [pk,c] of A)for(const [qk,d] of B){
   const p=unkey(pk),q=unkey(qk),dp=deriv(p),dq=deriv(q),v=vec0();
   for(let i=0;i<3;i++)for(let j=0;j<3;j++)
     v[i]=cadd(v[i],csub(cmul(cmul(c[j],dq[j]),d[i]),cmul(cmul(d[j],dp[j]),c[i])));
   put(out,kvec(p.map((x,i)=>x+q[i])),v,vadd);
  }
  return out;
 }
 function lie(C,H){
  const out=new Map();
  for(const [pk,c] of C)for(const [qk,M] of H){
   const p=unkey(pk),q=unkey(qk),dp=deriv(p),dq=deriv(q);
   let adv=Z;for(let j=0;j<3;j++)adv=cadd(adv,cmul(c[j],dq[j]));
   const v=mat0();
   for(let i=0;i<3;i++)for(let j=0;j<3;j++){
    let u=cmul(adv,M[i][j]);
    for(let t=0;t<3;t++)
      u=cadd(u,cadd(cmul(cmul(M[t][j],dp[i]),c[t]),cmul(cmul(M[i][t],dp[j]),c[t])));
    v[i][j]=u;
   }
   put(out,kvec(p.map((x,i)=>x+q[i])),v,madd);
  }
  return out;
 }
 function filtered(H,a){
  const out=new Map();
  for(const [k,m] of H)out.set(k,msc(m,filterMultiplier(unkey(k),a)));
  return out;
 }
 function difference(A,B){
  const out=new Map(A);
  for(const [k,m] of B)put(out,k,msc(m,-1),madd);
  return out;
 }
 function mmul(A,B){
  const out=mat0();
  for(let i=0;i<3;i++)for(let j=0;j<3;j++)for(let k=0;k<3;k++)
    out[i][j]=cadd(out[i][j],cmul(A[i][k],B[k][j]));
  return out;
 }
 function trace(A){let r=Z;for(let i=0;i<3;i++)r=cadd(r,A[i][i]);return r;}
 function TT(H){
  const out=new Map();
  for(const [mk,M] of H){
   const m=unkey(mk),m2=m.reduce((v,x)=>v+x*x,0),R=mat0();
   if(m2===0){
    const t=csc(trace(M),1/3);
    for(let i=0;i<3;i++)for(let j=0;j<3;j++)R[i][j]=csub(M[i][j],i===j?t:Z);
   }else{
    const P=mat0();
    for(let i=0;i<3;i++)for(let j=0;j<3;j++)
      P[i][j]=[(i===j?1:0)-m[i]*m[j]/m2,0];
    const PM=mmul(P,M),PMP=mmul(PM,P),t=csc(trace(PM),.5);
    for(let i=0;i<3;i++)for(let j=0;j<3;j++)
      R[i][j]=csub(PMP[i][j],cmul(t,P[i][j]));
   }
   const S=mat0();
   for(let i=0;i<3;i++)for(let j=0;j<3;j++)
     S[i][j]=csc(cadd(R[i][j],R[j][i]),.5);
   out.set(mk,S);
  }
  return out;
 }
 const comm=bracket(C1,C2);
 function K_B(a){
  const c12=lie(C1,filtered(lie(C2,filtered(h,a)),a));
  const c21=lie(C2,filtered(lie(C1,filtered(h,a)),a));
  const cb=lie(comm,filtered(h,a));
  return TT(difference(difference(c12,c21),cb));
 }
 const K0=K_B(0),Kplus=K_B(1),Kminus=K_B(-1);
 const modes=new Set([...K0.keys(),...Kplus.keys(),...Kminus.keys()]);
 const U=new Map(),V=new Map(),W=new Map();
 for(const k of modes){
  const a=K0.get(k)||mat0(),b=Kplus.get(k)||mat0(),c=Kminus.get(k)||mat0();
  U.set(k,a);V.set(k,msc(msub(b,c),.5));W.set(k,msub(msc(madd(b,c),.5),a));
 }
 // EXACT MASK DEFINITION for finite lattice [k,N-k)^3:
 // the following evaluates all finite-lattice Fourier averages by an
 // ordinary real/complex direct sum, independent of M13's complement formula.
 const cache=new Map();
 function win(q,k){
  const id=q+","+k;if(cache.has(id))return cache.get(id);
  const M=N-2*k;let out=Z;
  for(let i=k;i<N-k;i++)out=cadd(out,[Math.cos(q*i*dx)/M,Math.sin(q*i*dx)/M]);
  cache.set(id,out);return out;
 }
 function inner(A,B,k){
  let r=Z;
  for(const [pk,X] of A)for(const [qk,Y] of B){
   const p=unkey(pk),q=unkey(qk);let factor=[1,0],dot=Z;
   for(let j=0;j<3;j++)factor=cmul(factor,win(p[j]-q[j],k+(options.maskOffset||0)));
   for(let i=0;i<3;i++)for(let j=0;j<3;j++)dot=cadd(dot,cmul(X[i][j],conj(Y[i][j])));
   r=cadd(r,cmul(dot,factor));
  }
  return r[0]/6;
 }
 let results=[],maxRel=0,maxAbs=0;
 for(let k=2;k<=6;k++){
  const coeff=[
   inner(U,U,k),2*inner(U,V,k),
   inner(V,V,k)+2*inner(U,W,k),
   2*inner(V,W,k),inner(W,W,k)
  ];
  for(let j=0;j<5;j++){
   const bounds=source[String(k)][j];
   const sourceLo=Number(bounds[0].slice(1).split(",")[0]);
   const sourceHi=Number(bounds[1].slice(1).split(",")[0]);
   const sourceMid=(sourceLo+sourceHi)/2;
   const num=coeff[j],relative=Math.abs(num-sourceMid)/Math.abs(sourceMid);
   if(!Number.isFinite(relative))throw Error("Nonfinite coefficient or source coefficient zero at "+k+","+j);
   results.push({mask:k,power:j,value_float64:num,source_mid_float64:sourceMid,relative_error:relative});
   maxRel=Math.max(maxRel,relative);maxAbs=Math.max(maxAbs,Math.abs(num-sourceMid));
  }
 }
 return {
  artifact_id:"IW_GEEKY_S12_ROT008_M13_INDEPENDENT_SOURCE_B_FOURIER_MASK_25_COEFFICIENT_REPLAY_001_20261112",
  N,masks:[2,3,4,5,6],channel:"B",quartic_coefficients_checked:results.length,
  independent_method:"Float64 complex sparse Fourier Lie/filter/TT + direct finite position sums for masked modal inner products",
  input_M13_source_blob:ORIGINAL_M13_GIT_BLOB,
  mode_count:U.size,
  max_relative_error_float64:maxRel,max_absolute_error_float64:maxAbs,
  relative_tolerance_predeclared:1e-10,
  within_tolerance:maxRel<1e-10,
  results,
  source_scope:"FUNCTIONALLY_MATCHED_AUXILIARY_N41_NOT_HISTORIC_PRODUCER",
  mathematical_status:"INDEPENDENT_FLOAT64_CROSS_IMPLEMENTATION_SANITY_CHECK_NOT_INTERVAL_PROOF"
 };
}
(async()=>{
 const data=await load(),good=verify(data);
 if(!good.within_tolerance)throw Error("INDEPENDENT SOURCE ALIGNMENT FAIL "+good.max_relative_error_float64);
 const badMask=verify(data,{maskOffset:1}),badField=verify(data,{perturbC1:.01});
 if(badMask.max_relative_error_float64<1e-5||badField.max_relative_error_float64<1e-5)
   throw Error("NEGATIVE SOURCE_SENSITIVITY_CONTROLS FAILED");
 const output={...good,negative_controls:{
   swapped_mask_by_one:{max_relative_error_float64:badMask.max_relative_error_float64,detected:true},
   perturb_C1_xsin_1percent:{max_relative_error_float64:badField.max_relative_error_float64,detected:true}
 }};
 console.log(JSON.stringify(output,null,2));
})().catch(e=>{console.error(e.stack||String(e));process.exitCode=1;});
