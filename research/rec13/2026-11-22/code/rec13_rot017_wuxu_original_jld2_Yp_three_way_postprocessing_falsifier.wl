(* IW/NASH REC13 ROT017 — independent exact author-original HDF5 source reprocessing.
   Public data: Fenyutanchan/Primordial-Black-Hole commit d395183674cace6c9906a8911bdeb7234ba4040d.
   DO NOT interpret counterfactual postprocessing or baseline anchors as physical PBH bounds. *)
ClearAll[WuxuSourceAudit];
WuxuSourceAudit[file_String] := Module[
 {sha, yy, chi, masses, beta, lnb, f, naive, globallyCentered,
  rowCentered, root, crossings, roots, describe, original, all,
  oldRooted, missingV3, obj, bdelta, anchored, typed},
 sha = Hash[ReadByteArray[file], "SHA256", "HexString"];
 If[sha =!= "51844a46ca904f57f941e0d0ebc3b5920c38bace76eea9e1d89cb5fd1f2c5786",
  Return[<|"status" -> "STOP_SHA256_MISMATCH", "actualSHA256" -> sha|>]];
 yy = Transpose @ Import[file, {"HDF5", "Data", "/Y_P_mat"}];
 chi = Transpose @ Import[file, {"HDF5", "Data", "/chi2_mat"}];
 masses = Flatten @ Import[file, {"HDF5", "Data", "/m_PBH_list [gram]"}];
 beta = Flatten @ Import[file, {"HDF5", "Data", "/β_PBH_list"}];
 If[Dimensions[yy] =!= {100, 100} || Dimensions[chi] =!= {100, 100} ||
    Length[masses] != 100 || Length[beta] != 100 ||
    Max[Abs[Flatten[chi - ((yy - .245)/.003)^2]]] > 1.*^-9 ||
    Max[Abs[{First[Log10[beta]] + 20, Last[Log10[beta]] + 17}]] > 1.*^-12,
  Return[<|"status" -> "STOP_SOURCE_AXIS_OR_CHI2_INVALID"|>]];
 lnb = Log10[beta];
 f[z_] := 2*z/(2 + z);
 naive = f[yy];
 globallyCentered = .245 + naive - f[.245];
 rowCentered = Table[.245 + f[yy[[i]]] - f[yy[[i, 1]]], {i, 100}];
 crossings[row_] := Select[Range[Length[row] - 1],
                          row[[#]] < .251 <= row[[# + 1]] &];
 root[row_] := Module[{k = crossings[row]},
  If[Length[k] != 1, Missing["no_unique_upward_crossing"],
   With[{j = First[k]}, lnb[[j]] +
     (.251 - row[[j]])*(lnb[[j + 1]] - lnb[[j]])/
       (row[[j + 1]] - row[[j]])]]];
 roots = <|"archived_code" -> (root /@ yy),
           "v3_mapping_without_baseline_recalibration" -> (root /@ naive),
           "v3_mapping_globally_anchored_0p245" -> (root /@ globallyCentered),
           "v3_mapping_anchored_per_mass_beta_min" -> (root /@ rowCentered)|>;
 original = roots["archived_code"];
 describe[name_] := Module[{rr = roots[name], common, first},
  common = Select[Range[100], NumericQ[original[[#]]] && NumericQ[rr[[#]]] &];
  first = SelectFirst[Range[100], NumericQ[rr[[#]]] &, Missing["none"]];
  <|"label" -> name, "numberOfRoots" -> Count[rr, _?NumericQ],
    "firstRootMassG" -> If[MissingQ[first], Missing["none"], masses[[first]]],
    "firstRootIndexZeroBased" -> If[MissingQ[first], Missing["none"], first - 1],
    "rootAtJ22" -> rr[[23]], "rootAtJ62" -> rr[[63]],
    "deltaJ22" -> If[NumericQ[rr[[23]]], rr[[23]] - original[[23]],
                   Missing["no_cross"]],
    "deltaJ62" -> If[NumericQ[rr[[63]]], rr[[63]] - original[[63]],
                   Missing["no_cross"]],
    "commonRootShiftRange" -> If[common === {}, Missing["none"],
       MinMax[(rr[[#]] - original[[#]]) & /@ common]],
    "uniqueUpwardCrossingPerMass" -> Max[Length[crossings[#]] & /@
                  Switch[name,
                   "archived_code", yy,
                   "v3_mapping_without_baseline_recalibration", naive,
                   "v3_mapping_globally_anchored_0p245", globallyCentered,
                   _, rowCentered]] <= 1|>];
 all = Keys[roots];
 obj = <|
  "source" -> "Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d",
  "sourceGitBlob" -> "10cc9b3f078fcadb91b5e520e75845859ca00b74",
  "sourceSHA256" -> sha, "sourceBytes" -> FileByteCount[file],
  "sourceDimensions" -> Dimensions[yy],
  "sourceChi2MaxResidual" -> Max[Abs[Flatten[chi - ((yy - .245)/.003)^2]]],
  "massRangeG" -> {First[masses], Last[masses]},
  "betaLog10Range" -> {First[lnb], Last[lnb]},
  "sourceLightMassLowBetaYcode" -> yy[[1, 1]],
  "sourceLightMassLowBetaYv3" -> naive[[1, 1]],
  "v3FromCodeY0p245" -> f[.245],
  "v3BaselineDifferenceInObservedSigma" -> (.245 - f[.245])/.003,
  "criticalRawCodeYForV3Y0p251" -> 2*.251/(2 - .251),
  "scenarios" -> (describe /@ all),
  "policy" -> "Postprocessing only; no actual physical bound, nuclear network, or baseline recalibration proved.",
  "status" -> "SOURCE_ORIGINAL_HDF5_I1_PASS_CONDITIONAL_POSTPROCESSING_ONLY_NO_CANON"
 |>;
 obj
];
If[Length[$ScriptCommandLine] >= 2,
 Print[ExportString[WuxuSourceAudit[$ScriptCommandLine[[2]]], "RawJSON"]],
 Print["Usage: wolframscript -file rec13_rot017_wuxu_source_audit.wl <author_scanning.jld2>"]];
