(* IW/NASH REC13 ROT018 — original Wu–Xu JLD2, two-sided chi-square
   source-typed falsifier for naive v3 helium postprocessing.
   EXECUTION: wolframscript -file rec13_rot018_wuxu_twosided_yp_guard.wl \
     current_scanning.jld2 v1_scanning.jld2
   Both source files must come from Fenyutanchan/Primordial-Black-Hole
   @d395183674cace6c9906a8911bdeb7234ba4040d.
   Does NOT compute physical PBH bounds; no SBBN calibration or new solver. *)

ClearAll[rec13SourceAudit];
rec13SourceAudit[file_String, archive_String] := Module[
 {digests, expected, y, c, mass, beta, alpha, v3, lo=.239, hi=.251,
  sourceRoot, acceptable, branch, describe, res},
 digests=<|"latest"->"51844a46ca904f57f941e0d0ebc3b5920c38bace76eea9e1d89cb5fd1f2c5786",
 "v1"->"7f8ebe6c6c7b380f20c725908d900c5508bb4f16519a7f17e10955a55e78ecf1"|>;
 expected=Lookup[digests,archive,Missing["unknown_archive"]];
 If[MissingQ[expected],Return[<|"status"->"FAIL_ARCHIVE_NAME"|>]];
 If[Hash[ReadByteArray[file],"SHA256","HexString"] =!= expected,
  Return[<|"status"->"FAIL_SOURCE_SHA256"|>]];
 y=Transpose@Import[file,{"HDF5","Data","/Y_P_mat"}];
 c=Transpose@Import[file,{"HDF5","Data","/chi2_mat"}];
 mass=Flatten@Import[file,{"HDF5","Data","/m_PBH_list [gram]"}];
 beta=Flatten@Import[file,{"HDF5","Data","/β_PBH_list"}];
 If[Dimensions[y] =!= {100,100} || Dimensions[c] =!= {100,100}
    || Length[mass] != 100 || Length[beta] != 100 ||
    Max[Abs[Flatten[c-((y-.245)/.003)^2]]] > 1.*^-9 ||
    Max[Abs[Log10[beta[[{1,100}]]]-{-20,-17}]] > 1.*^-11,
   Return[<|"status"->"FAIL_SOURCE_CHI2_OR_AXIS"|>]];
 alpha=Log10[beta];
 v3=2*y/(2+y);
 acceptable[u_]:=Boole[lo<=u<=hi];
 branch[row_,level_]:=Module[{idx},
    idx=Select[Range[99],row[[#]]<level<=row[[#+1]]&];
    If[Length[idx]!=1,Missing["no_unique_cross"],
     With[{j=First[idx]},alpha[[j]]+(level-row[[j]])*
       (alpha[[j+1]]-alpha[[j]])/(row[[j+1]]-row[[j]])]]];
 describe[tag_,q_]:=Module[{flags,lowY,lowChi,upper,lower,allowedRows},
  flags=Map[acceptable,q,{2}];lowY=q[[All,1]];
  lowChi=((lowY-.245)/.003)^2;
  upper=branch[#,hi]&/@q;lower=branch[#,lo]&/@q;
  allowedRows=Total[flags,{2}];
  <|"scenario"->tag,"nMass"->Length[mass],
   "lowestBetaMassesAccepted"->Count[lowY,_?(lo<=#<=hi&)],
   "lowestBetaMassesBelowLower"->Count[lowY,_?(#<lo&)],
   "lowestBetaMassesAboveUpper"->Count[lowY,_?(#>hi&)],
   "sourceCellsAllowed"->Total[Flatten[flags]],
   "sourceCellsBelowLower"->Count[Flatten[q],_?(#<lo&)],
   "sourceCellsAboveUpper"->Count[Flatten[q],_?(#>hi&)],
   "massRowsAnyAllowedCell"->Count[allowedRows,_?(#>0&)],
   "massRowsNeverAllowed"->Count[allowedRows,0],
   "lowerCrossingMasses"->Count[lower,_?NumericQ],
   "upperCrossingMasses"->Count[upper,_?NumericQ],
   "twoBoundedAllowedIntervalMasses"->Count[MapThread[
      NumericQ[#1]&&NumericQ[#2]&, {lower,upper}],True],
   "lowestBetaChi2MinMax"->MinMax[lowChi],
   "j22"-><|"massG"->mass[[23]],"Y_at_low_beta"->lowY[[23]],
     "chi2_at_low_beta"->lowChi[[23]],
     "lowerCrossLog10Beta"->lower[[23]],"upperCrossLog10Beta"->upper[[23]],
     "allowedGridCells"->allowedRows[[23]]|>,
   "j62"-><|"massG"->mass[[63]],"Y_at_low_beta"->lowY[[63]],
     "chi2_at_low_beta"->lowChi[[63]],
     "lowerCrossLog10Beta"->lower[[63]],"upperCrossLog10Beta"->upper[[63]],
     "allowedGridCells"->allowedRows[[63]]|>
   |>];
 res=<|"status"->"SOURCE_SHA256_CHI2_I1_PASS_TWO_SIDED_CONTRACT_ONLY",
   "archive"->archive,
   "originalAuthorSHA256"->expected,
   "originalMassRangeG"->{First[mass],Last[mass]},
   "originalBetaLogRange"->alpha[[{1,100}]],
   "sourceChi2MaxDeviation"->Max[Abs[Flatten[c-((y-.245)/.003)^2]]],
   "acceptedYinterval2sigma"->{lo,hi},
   "sourceAsStored"->describe["source_stored_Ycode",y],
   "naiveV3"->describe["naive_v3_Y_2Ycode_over_2plusYcode",v3],
   "noPhysicsClaims"->{"No baseline recalibration","No physical corrected beta",
      "No independent producer authentication of published Fig5",
      "No comparison of nuclear BBN-simple solver outputs",
      "No novelty, no CANON, no EXEC_SIGN"}|>;
 res
];
If[Length[$ScriptCommandLine]>=3,
 Print[ExportString[
   {rec13SourceAudit[$ScriptCommandLine[[2]],"latest"],
    rec13SourceAudit[$ScriptCommandLine[[3]],"v1"]},"RawJSON"]],
 Print["Usage: wolframscript -file rec13_rot018_wuxu_twosided_yp_guard.wl current_scanning.jld2 v1_scanning.jld2"]];
