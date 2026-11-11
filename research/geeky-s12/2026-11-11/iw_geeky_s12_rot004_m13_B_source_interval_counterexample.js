#!/usr/bin/env node
"use strict";
/*
 * Geeky-S12 ROT004: source-locked exact-RATIONAL-INTERVAL counterexample
 * against universal nearest-delta endpoint minimization for M13 channel B.
 *
 * Node >= 18. Run:
 * node iw_geeky_s12_rot004_m13_B_source_interval_counterexample.js
 * OR supply the original bytes of M13 direct_B.json as first argument.
 *
 * The default fetches the immutable source Git *blob* by SHA and verifies
 * exact bytes. This mathematical result is on a FUNCTIONALLY MATCHED
 * auxiliary source, not the missing historic dtc0a_runtime_v0_3_1.py.
 */
const fs = require("fs");
const https = require("https");
const crypto = require("crypto");
const SOURCE_BLOB = "a6f50fbe5904e580e84c87ee87c5ad043cdec5d0";
const REMOTE = "https://api.github.com/repos/wmakiela-tech/Nash-iw-research/git/blobs/" + SOURCE_BLOB;
function get(url) {
  return new Promise((resolve,reject)=>{
    https.get(url,{headers:{"User-Agent":"Geeky-S12-source-locked-reproducer","Accept":"application/vnd.github+json"}},r=>{
      if(r.statusCode!==200){reject(new Error("HTTP "+r.statusCode));r.resume();return;}
      const chunks=[];r.on("data",b=>chunks.push(b));r.on("end",()=>resolve(Buffer.concat(chunks)));r.on("error",reject);
    }).on("error",reject);
  });
}
async function load(){
  let buf;
  if(process.argv.length>2) buf=fs.readFileSync(process.argv[2]);
  else {
    const d=JSON.parse((await get(REMOTE)).toString("utf8"));
    if(d.encoding!=="base64" || !d.content)throw Error("Unexpected GitHub blob encoding");
    buf=Buffer.from(d.content.replace(/\s/g,""),"base64");
  }
  const got=crypto.createHash("sha1").update(Buffer.from("blob "+buf.length+"\0")).update(buf).digest("hex");
  if(got!==SOURCE_BLOB)throw Error("M13 source blob identity mismatch: "+got);
  return JSON.parse(buf.toString("utf8"));
}
const abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b){const t=a%b;a=b;b=t;}return a||1n;}
function F(n,de=1n){
  n=BigInt(n);de=BigInt(de);if(de===0n)throw Error("Zero denominator");
  if(de<0n){n=-n;de=-de;}const g=gcd(n,de);return [n/g,de/g];
}
const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]);
const div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
const cmp=(a,b)=>a[0]*b[1]<b[0]*a[1]?-1:a[0]*b[1]>b[0]*a[1]?1:0;
function dec(x){
  let a=x.trim(),sign=1n;
  if(a[0]==="-"){sign=-1n;a=a.slice(1);}
  if(a[0]==="+")a=a.slice(1);
  const [m,e]=a.toLowerCase().split("e"),exp=e?Number(e):0;
  const [u,v=""]=m.split("."),raw=(u||"0")+v,p=exp-v.length;
  return p>=0?F(sign*BigInt(raw)*10n**BigInt(p)):F(sign*BigInt(raw),10n**BigInt(-p));
}
const I=(a,b=a)=>[a,b];
const iadd=(a,b)=>[add(a[0],b[0]),add(a[1],b[1])];
const isub=(a,b)=>[sub(a[0],b[1]),sub(a[1],b[0])];
function minmax(xs){
  let lo=xs[0],hi=xs[0];
  for(const x of xs){if(cmp(x,lo)<0)lo=x;if(cmp(x,hi)>0)hi=x;}
  return [lo,hi];
}
const imul=(a,b)=>minmax([mul(a[0],b[0]),mul(a[0],b[1]),mul(a[1],b[0]),mul(a[1],b[1])]);
function isquare(a){
  if(cmp(a[0],F(0))>=0)return I(mul(a[0],a[0]),mul(a[1],a[1]));
  if(cmp(a[1],F(0))<=0)return I(mul(a[1],a[1]),mul(a[0],a[0]));
  const u=mul(a[0],a[0]),v=mul(a[1],a[1]);
  return I(F(0),cmp(u,v)>0?u:v);
}
function idivpos(a,b){
  if(cmp(b[0],F(0))<=0)throw Error("Nonpositive interval denominator");
  return [div(a[0],b[1]),div(a[1],b[0])];
}
const parse=s=>dec(s.split(",")[0].slice(1));
function approx(x){
  let u=x[0].toString(),v=x[1].toString();
  return Number(u.slice(0,17))/Number(v.slice(0,17))*10**(u.length-v.length);
}
function solve(d){
  const K=[2,3,4,5,6],n=K.map(k=>BigInt((41-2*k)**3)),
    w=n.map((v,i)=>i===4?v:v-n[i+1]);
  const g=K.map(k=>d[k].map(a=>I(parse(a[0]),parse(a[1]))));
  const shell=g.map((cs,i)=>cs.map((x,j)=>{
    const t=imul(x,I(F(n[i])));
    return idivpos(i===4?t:isub(t,imul(g[i+1][j],I(F(n[i+1])))),I(F(w[i])));
  }));
  function V(x){
    return shell.map(cs=>{
      let a=cs[4];
      for(let j=3;j>=0;j--)a=iadd(imul(a,I(x)),cs[j]);
      return a;
    });
  }
  function distance2(a,b){
    const A=V(a),B=V(b);let num=I(F(0)),den=I(F(0)),project=I(F(0));
    for(let i=0;i<5;i++){
      if(cmp(A[i][0],F(0))<=0 || cmp(B[i][0],F(0))<=0)
        throw Error("Source shell energy not strictly positive at comparison point");
      den=iadd(den,imul(I(F(w[i])),isquare(B[i])));
      project=iadd(project,imul(I(F(w[i])),imul(A[i],B[i])));
      for(let j=0;j<i;j++){
        const cross=isub(imul(A[i],B[j]),imul(A[j],B[i]));
        num=iadd(num,imul(I(F(w[i]*w[j])),isquare(cross)));
      }
    }
    if(cmp(project[0],F(0))<=0)throw Error("Positive-gain optimum not certified");
    // Lagrange/wedge identity: D² = sum_(i<j) w_i w_j (a_i b_j-a_j b_i)² / sum_i w_i b_i²
    return idivpos(num,den);
  }
  const a=F(39,1000),delta=F(35,1000);
  const beta0=F(0), betaInner=F(1,1000), betaL=F(4,1000),betaR=F(74,1000);
  if(cmp(sub(a,betaInner),delta)<=0 || cmp(sub(a,betaL),delta)!==0
     || cmp(sub(betaR,a),delta)!==0)throw Error("Incorrect legal beta locations");
  const points=[
    ["zero",beta0],["interior_witness",betaInner],
    ["left_nearest",betaL],["right_nearest",betaR]
  ];
  const results=Object.fromEntries(points.map(([name,b])=>[name,distance2(a,b)]));
  const witness=results.interior_witness;
  const leftGap=sub(results.left_nearest[0],witness[1]);
  const rightGap=sub(results.right_nearest[0],witness[1]);
  const zeroGapL=sub(results.left_nearest[0],results.zero[1]);
  if(cmp(leftGap,F(0))<=0 || cmp(rightGap,F(0))<=0
     || cmp(zeroGapL,F(0))<=0)throw Error("STRICT CERTIFICATE FAIL");
  const SC=F(10n**24n);
  return {
    artifact_id:"IW_GEEKY_S12_ROT004_M13_SOURCE_B_NON_NEAREST_GLOBAL_MINIMIZER_FALSIFIER_001_20261111",
    source_blob_sha:SOURCE_BLOB,
    source_type:"M13 original outward interval direct_B.json N41 auxiliary matched generator, NOT historic runtime bytes",
    N:41,masks:K,weights:w.map(String),
    true_alpha:"39/1000",separation_delta:"7/200",
    witness_beta:"1/1000",witness_interior:true,
    nearest_allowed_beta:["1/250","37/500"],
    D2_x1e24_approx_not_proof:Object.fromEntries(Object.entries(results).map(([name,x])=>[name,approx(mul(x[0],SC))])),
    exact_upper_witness_less_than_lower_of_both_nearest:
      [cmp(witness[1],results.left_nearest[0])<0,cmp(witness[1],results.right_nearest[0])<0],
    certified_lower_gap_D2_x1e24_approx:
      [approx(mul(leftGap,SC)),approx(mul(rightGap,SC))],
    verdict:"EXACT_FRACTION_INTERVAL_COUNTEREXAMPLE_PASS"
  };
}
(async()=>{const d=await load();const result=solve(d);console.log(JSON.stringify(result,null,2));})().catch(e=>{console.error(String(e));process.exitCode=1;});
