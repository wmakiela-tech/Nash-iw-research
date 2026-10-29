(* MT14 ROT018: REAL ORIGINAL Wu-Xu binary from immutable author commit.
   Requires Wolfram Language and network. Not Julia 10D and not a new PBH bound. *)
url = "https://raw.githubusercontent.com/Fenyutanchan/Primordial-Black-Hole/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/data/out/scanning.jld2";
f = URLDownload[url];
If[FileByteCount[f] != 151089, Print["FAIL SOURCE SIZE"]; Abort[]];
sha = IntegerString[FileHash[f, "SHA256"], 16, 64];
If[sha != "51844a46ca904f57f941e0d0ebc3b5920c38bace76eea9e1d89cb5fd1f2c5786", Print["FAIL SOURCE HASH"]; Abort[]];
y = Import[f, {"HDF5", "Data", "/Y_P_mat"}];
c = Import[f, {"HDF5", "Data", "/chi2_mat"}];
If[Dimensions[y] != {100, 100} || Dimensions[c] != {100, 100}, Print["FAIL DATA SHAPE"]; Abort[]];
v = Flatten[y]; chi = Flatten[c]; m = 2 v/(2 + v);
err = Max[Abs[chi - ((v - .245)/.003)^2]];
conf = Counts[MapThread[List, {UnitStep[chi - 4], UnitStep[((m - .245)/.003)^2 - 4]}]];
If[err > 10^-9 || Count[v, x_ /; x > 1] != 158 ||
    Count[chi, x_ /; x > 4] != 5531 ||
    Count[m, x_ /; Abs[(x - .245)/.003] > 2] != 9487 ||
    conf != <|{0, 1} -> 4469, {1, 1} -> 5018, {1, 0} -> 513|>,
   Print["FAIL SOURCE NUMERIC CONTROL"]; Abort[]];
Print["PASS ORIGINAL AUTHOR SOURCE HDF5/JLD2; 10000/10000 chi2; source SHA256 ", sha];
Print["PASS max abs chi2 residual ", err, "; C>1: 158; original chi2>4: 5531"];
Print["NAIVE UNRECALIBRATED MASS M(X) RE-TYPING ONLY: 9487 chi2>4; 4982 changed labels."];
Print["NO PHYSICAL MODEL RE-CALIBRATION, NO JULIA10D, NO PBH BOUND."];
