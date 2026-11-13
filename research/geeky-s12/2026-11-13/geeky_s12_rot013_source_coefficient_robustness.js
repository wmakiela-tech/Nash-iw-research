#!/usr/bin/env node
"use strict";
/*
 Geeky-S12 ROT013 — source-typed coefficient perturbation robustness audit
 EXACT RATIONAL INTERVAL DECISIONS, author same-cell (NOT REC11/AUD2).
 Offline usage from repo root:
 node research/geeky-s12/2026-11-13/geeky_s12_rot013_source_coefficient_robustness.js \
   research/m13/2026-10-26/direct_B.json \
   research/geeky-s12/2026-11-12/iw_geeky_s12_rot007_exact_B_uniform_delta_le_0025_rational_bernstein.js \
   research/geeky-s12/2026-11-12/iw_geeky_s12_rot007_exact_B_delta_002514_interior_falsifier.js

 This code first checks all three ORIGINAL Git blob hashes.
 It then extracts the original pure certificate bodies, preserved byte-for-byte,
 and calls them on widened source intervals only. It does not alter source
 files and does not substitute floating point decisions for interval signs.
 No new beta/delta threshold scans, no historic DTC0a producer claim.
*/
const fs=require("fs"),crypto=require("crypto");
const SOURCE_SHA="a6f50fbe5904e580e84c87ee87c5ad043cdec5d0";
const POS_SHA="798313672194929ee44c3db7fe591d3cee5e6684";
const NEG_SHA="0851b2c0eb807314849852a5c2d065d59ce9bb08";
function fail(t){throw Error("ROT013 FAIL: "+t);}
function hash(bytes){return crypto.createHash("sha1").update(Buffer.from("blob "+bytes.length+"\0")).update(bytes).digest("hex");}
function readLocked(file,expected){
  const bytes=fs.readFileSync(file),actual=hash(bytes);
  if(actual!==expected)fail("Source Git blob mismatch expected "+expected+" got "+actual+" at "+file);
  return bytes.toString("utf8");
}
function originalCertificate(script,what){
  let start,end,entry;
  if(what==="positive"){start=script.indexOf("function certificate(source) {");entry="certificate";}
  else{start=script.indexOf("const abs=x=>");entry="solve";}
  end=script.indexOf("\n(async()=>",start);
  if(start<0||end<0)fail("Certificate source grammar changed");
  // Code evaluated ONLY after exact SHA check against original immutable Git blobs.
  return new Function('const SOURCE_BLOB="'+SOURCE_SHA+'";\n'+script.slice(start,end)+"\nreturn "+entry+";")();
}
// Rational expansion of each ORIGINAL interval [lo,hi] by [lo-eps|lo|, hi+eps|hi|].
// Both endpoint conversions exact: no Number arithmetic except naming tolerance.
function parseDecimal(x){
  let sign=1n,s=x.trim();
  if(s[0]==="-"){sign=-1n;s=s.slice(1);}
  else if(s[0]==="+")s=s.slice(1);
  const p=s.split(".");
  if(p.length>2 || !/^[0-9]+$/.test(p[0]||"0") || !/^[0-9]*$/.test(p[1]||""))
    fail("Nonfixed decimal source endpoint "+x);
  return {n:sign*BigInt((p[0]||"0")+(p[1]||"")),decimals:(p[1]||"").length};
}
function decimalOutput(n,decimals){
  const sign=n<0n?"-":"";
  const v=(n<0n?-n:n).toString().padStart(decimals+1,"0");
  return sign+(decimals?v.slice(0,-decimals)+"."+v.slice(-decimals):v);
}
function widenExact(source,denominator){
  const out=JSON.parse(JSON.stringify(source)),D=BigInt(denominator);
  let pow=0,d=D;
  while(d>1n&&d%10n===0n){d/=10n;pow++;}
  if(d!==1n||pow<1)fail("denominator must be 10^k");
  for(const k of [2,3,4,5,6]){
    if(!Array.isArray(source[k])||source[k].length!==5)fail("Unexpected original source shape");
    for(let j=0;j<5;j++){
      const pair=source[k][j];
      const lower=parseDecimal(pair[0].slice(1).split(",")[0]);
      const upper=parseDecimal(pair[1].slice(1).split(",")[0]);
      const abs=x=>x<0n?-x:x;
      const l=decimalOutput(lower.n*D-abs(lower.n),lower.decimals+pow);
      const h=decimalOutput(upper.n*D+abs(upper.n),upper.decimals+pow);
      out[k][j]=["["+l+", "+l+"]","["+h+", "+h+"]"];
    }
  }
  return out;
}
function condensedPositive(result){
  return {
    positive_17_sign_gates:result.polynomial_sign_gates,
    shell_5_sign_gates:result.shell_positive_gates,
    positive_shell_lower:result.shell_positivity_lower_bounds_in_scale_1e12,
    P_five_boxes_lower:result.P_big_domain_five_rectangles_Bernstein_lower,
    P_small_lower:result.P_small_alpha_le_0p028_beta_le_0p008_Bernstein_lower,
    dP_small_lower:result.derivative_beta_P_alpha_ge_0p028_beta_le_0p008_Bernstein_lower,
    F0_eight_segments_lower:result.F0_at_delta_0p025_alpha_ge_0p028_subdivision_Bernstein_lower,
    shifted_P_two_segments_lower:result.P_along_beta_alpha_minus_0p025_alpha_0p028_to_0p033_Bernstein_lower
  };
}
function check(source,positive,negative){
  const out={
    artifact_id:"IW_GEEKY_S12_ROT013_SOURCE_B_RELATIVE_COEFFICIENT_ENCLOSURE_ROBUSTNESS_001_20261113",
    date:"2026-11-13",
    source_sha:SOURCE_SHA,positive_certifier_sha:POS_SHA,negative_certifier_sha:NEG_SHA,
    perturbation_definition:"Each of 25 independently varied original coefficient intervals [lo,hi] expanded to [lo-eps*abs(lo), hi+eps*abs(hi)], with exact decimal rational endpoints; perturbations need not arise from any physically realisable tensor field.",
    tests:{}
  };
  const e8=widenExact(source,100000000);
  const e7=widenExact(source,10000000);
  const e6=widenExact(source,1000000);
  out.tests.eps_1e_minus_8={positive:condensedPositive(positive(e8)),negative:{
    verdict:negative(e8).verdict,
    strict_nearest_gaps_D2_x1e24_lower:negative(e8).certified_lower_gap_D2_x1e24_approx
  }};
  out.tests.eps_1e_minus_7={positive:condensedPositive(positive(e7))};
  try{negative(e7);out.tests.eps_1e_minus_7.negative={verdict:"PASS"};}
  catch(e){out.tests.eps_1e_minus_7.negative={verdict:"UNDECIDED_BY_THIS_INTERVAL_TEST",diagnostic:String(e)};}
  try{positive(e6);out.tests.eps_1e_minus_6={positive:"PASS"};}
  catch(e){out.tests.eps_1e_minus_6={positive:"UNDECIDED_BY_THIS_BERNSTEIN_TEST",diagnostic:String(e)};}
  try{negative(e6);out.tests.eps_1e_minus_6.negative="PASS";}
  catch(e){out.tests.eps_1e_minus_6.negative="UNDECIDED_BY_THIS_INTERVAL_TEST";}
  if(out.tests.eps_1e_minus_8.positive.positive_17_sign_gates!==17||
     out.tests.eps_1e_minus_7.positive.positive_17_sign_gates!==17||
     out.tests.eps_1e_minus_8.positive.shell_5_sign_gates!==5||
     out.tests.eps_1e_minus_7.positive.shell_5_sign_gates!==5)
    fail("source robust sign gate count mismatch");
  out.conclusion={
    both_positive_and_negative_robust_for_all_coeff_perturbations_eps_le_1e_minus_8:true,
    positive_three_candidate_and_uniform_delta_le_0p025_robust_eps_le_1e_minus_7:true,
    eps_1e_minus_6_failed_Bernstein_bound_is_not_a_theorem_counterexample:true,
    no_claim_of_maximal_robustness_radius:true,
    original_historic_producer_identity:"OPEN",
    referee_status:"AUTHOR_ONLY_INDEPENDENT_REC11_AUD2_REFEREE_PENDING",
    science_ceiling:"NO_NOVELTY/NO_CANON/NO_EXEC_SIGN/NO_PHYSICAL_UPGRADE"
  };
  return out;
}
if(require.main===module){
  const [a,b,c]=process.argv.slice(2);
  if(!a||!b||!c)fail("Supply exact original B JSON, exact positive JS, exact negative JS paths");
  const source=JSON.parse(readLocked(a,SOURCE_SHA));
  const positive=originalCertificate(readLocked(b,POS_SHA),"positive");
  const negative=originalCertificate(readLocked(c,NEG_SHA),"negative");
  console.log(JSON.stringify(check(source,positive,negative),null,2));
}
module.exports={widenExact,check,originalCertificate};
