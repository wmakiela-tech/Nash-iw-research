# Mech-S9 ROT007 — independent GPT / native Julia L2.
# Uses unmodified Wu-Xu magic() definition and ORIGINAL cached g(T).
# NOT Badacz's wuxu_yp_formula_counterfactual.jl, no Badacz 53-point CSV in computation.
# NONBLIND: window selection was informed by REVIEW053; root finder/trajectories independent.
# Usage: julia --project=<MechS6_immutable_env> mech_s9_rot007_independent_L2.jl <author-dir> <out-dir>
using Printf
using SHA

length(ARGS) == 2 || error("Usage: <frozen-original-author-dir> <out-dir>")
author_dir = abspath(ARGS[1])
out_dir = abspath(ARGS[2])
mkpath(out_dir)

# The author main file would execute its unauthorised 100x100 scan after this marker.
# Extract exact original prefix, entirely unedited. Include original parameters separately.
main_bytes = read(joinpath(author_dir, "main-scan.jl"), String)
marker = "@info \"Loading `main-scan-parameters.jl`\""
occursin(marker, main_bytes) || error("FROZEN_AUTHOR_MARKER_MISSING")
occursin("2 * Xₙ_nuc / (1 - Xₙ_nuc)", main_bytes) || error("FROZEN_AUTHOR_YP_EXPRESSION_MISSING")
prefix = split(main_bytes, marker; limit=2)[1]
prefix_path = joinpath(author_dir, "_mech_s9_rot007_author_prefix_$(getpid()).jl")
write(prefix_path, prefix)
try
    cd(author_dir) do
        include(prefix_path)
        include("main-scan-parameters.jl")
    end
finally
    isfile(prefix_path) && rm(prefix_path)
end

# Different observation operator: a minimal hand-written linear interpolator in the
# native dimensionless q=Q/T coordinate, from original AUTHOR trajectory arrays.
# We do not call Badacz x_interp, xat, point, or the owner's downstream analysis.
function independent_x_at(result, temperature_mev::Float64)
    rho = result[3]
    xn = result[6]
    T = from_ρ_to_T.(rho)
    qaxis = Float64.(Q ./ T)
    perm = sortperm(qaxis)
    qaxis = qaxis[perm]
    yaxis = Float64.(xn[perm])
    qt = Float64(Q / MeV(temperature_mev))
    k = searchsortedfirst(qaxis, qt)
    k = clamp(k, 2, length(qaxis))
    x0, x1 = qaxis[k - 1], qaxis[k]
    x1 > x0 || error("q-axis non-strict at k=$k")
    return yaxis[k - 1] + (qt - x0) * (yaxis[k] - yaxis[k - 1]) / (x1 - x0)
end

const T0 = Float64(EUval(MeV, T_nuc))
const MASS_INDEX = (22, 62)
const CTX = Dict{Int,Any}()
const MEASURES = Dict{Tuple{Int,Float64},Any}()
const RAWFILE = joinpath(out_dir, "independent_L2_raw_calls.csv")
const ROOTFILE = joinpath(out_dir, "independent_L2_roots.csv")
const LOGFILE = joinpath(out_dir, "independent_L2_summary.txt")
const header = "j,log10beta,mass_g,T0_MeV,T1_MeV,X_T0,X_T1,Yc_author,calc_check,eval_kind"
open(RAWFILE, "w") do io println(io, header) end

function native_observation(j::Int, logb::Float64; kind::String="adaptive")
    key = (j, logb)
    if haskey(MEASURES, key)
        return MEASURES[key]
    end
    haskey(CTX, 22) || error("SBBN calibration not yet committed")
    m = m_PBH_f_list[j + 1]
    beta = ArbFloat(10.0^logb; bits=BITS)
    run = magic(m, beta)
    x0 = independent_x_at(run, T0)
    x1 = independent_x_at(run, CTX[22].T1)
    y0 = Float64(run[7])
    # Validate return of the unmodified original code independently.
    abs(y0 - 2*x0/(1-x0)) < 1e-8 || error("Native_Yc_vs_our_x0 disagreement j=$j lb=$logb")
    v = (j=j, lb=logb, m=Float64(m / NU.g), X0=x0, X1=x1, Yc=y0)
    MEASURES[key] = v
    open(RAWFILE, "a") do io
        @printf(io, "%d,%.17g,%.9e,%.17g,%.17g,%.16g,%.16g,%.16g,%.3e,%s\n",
            j, logb, v.m, T0, CTX[22].T1, x0, x1, y0,
            y0-2*x0/(1-x0), kind)
    end
    @printf("NATIVE_L2 j=%d log10beta=%.7f Yc=%.13f X0=%.13f X1=%.13f calls=%d\n",
        j, logb, y0, x0, x1, length(MEASURES))
    flush(stdout)
    return v
end

# Independent j22 and j62 SBBN calibrations. The physics threshold comes from
# REVIEW051, not the downstream numerical owner CSV: 2X(T1)=0.245.
for j in MASS_INDEX
    m = m_PBH_f_list[j + 1]
    run = magic(m, ArbFloat(1e-30; bits=BITS))
    X0 = independent_x_at(run, T0)
    low, high = T0, 10*T0
    2*independent_x_at(run, low) < 0.245 < 2*independent_x_at(run, high) ||
        error("SBBN_T1_NOT_BRACKETED j=$j")
    # Our operator bisection in linear T, different from Badacz geometric-T bisection.
    for _ in 1:65
        mid = (low + high)/2
        if 2*independent_x_at(run, mid) < 0.245
            low = mid
        else
            high = mid
        end
    end
    T1 = (low + high)/2
    CTX[j] = (X0=X0, T1=T1, Yc=Float64(run[7]), m=Float64(m/NU.g))
    @printf("NATIVE_L2_SBBN j=%d X0=%.15f T1=%.15f Ycode=%.15f\n",
        j,X0,T1,CTX[j].Yc)
    flush(stdout)
end

# Independent root equations. V2 shares source SBBN X0 from j22, as in prereg.
# Same author magic(), independently computed X0(T), X1(T).
response(name::String, v) =
    name == "V0" ? (v.Yc - 0.251) :
    name == "V1" ? (2*v.X1 - 0.251) :
    name == "V2" ? (2*(v.X0 - CTX[22].X0) - 0.006) :
    error("unknown root channel")

# Nonblind but independently chosen FIXED coarse beta anchors; no copied owner grid.
COARSE = Dict(
  22 => Float64[-17.40,-17.30,-17.20,-17.10,-17.00,-16.90],
  62 => Float64[-19.60,-19.50,-19.40,-19.30,-19.20,-19.10]
)

roots = Dict{Int,Dict{String,Any}}()
open(ROOTFILE, "w") do io
    println(io,"j,criterion,root_log10beta,left_log10beta,right_log10beta,lo_residual,hi_residual,half_bracket_dex,total_native_beta_calls")
    for j in MASS_INDEX
        anchors = [native_observation(j, b; kind="coarse") for b in COARSE[j]]
        found = Dict{String,Any}()
        for target in ("V0","V1","V2")
            ys = [response(target,v) for v in anchors]
            idx = findfirst(i -> ys[i] <= 0 && ys[i+1] >= 0, 1:(length(anchors)-1))
            isnothing(idx) && error("NO_BRACKET criterion=$target j=$j coarse_residuals=$ys")
            lb,rb = anchors[idx].lb, anchors[idx+1].lb
            ly,ry = ys[idx],ys[idx+1]
            # Root by NEW evaluations, NOT interpolating Badacz 53-point values.
            for _ in 1:8
                mid = (lb+rb)/2
                v = native_observation(j, mid;kind=target)
                yr = response(target,v)
                if yr < 0
                    lb, ly = mid, yr
                else
                    rb, ry = mid, yr
                end
            end
            center = (lb+rb)/2
            found[target] = (root=center, left=lb, right=rb, residual_lo=ly, residual_hi=ry)
            @printf(io,"%d,%s,%.14f,%.14f,%.14f,%.16e,%.16e,%.8f,%d\n",
                j,target,center,lb,rb,ly,ry,(rb-lb)/2,length(MEASURES))
            flush(io)
            @printf("NATIVE_L2_ROOT j=%d %s log10beta≈%.9f bracket=[%.9f,%.9f]\n",
                j,target,center,lb,rb)
            flush(stdout)
        end
        roots[j] = found
    end
end

open(LOGFILE,"w") do io
    println(io,"RUN_MECH_S9_ROT007_L2_NATIVE_ORIGINAL_AUTHOR_MAGIC")
    println(io,"FROZEN_AUTHOR_COMMIT=d395183674cace6c9906a8911bdeb7234ba4040d")
    println(io,"AUTHOR_MAIN_SOURCE_SHA256=",bytes2hex(sha256(main_bytes)))
    println(io,"JULIA_VERSION=",VERSION)
    println(io,"BITS=",BITS," native_magic_num_points=10000")
    println(io,"CALIBRATION_22_X0=",CTX[22].X0," T1=",CTX[22].T1)
    println(io,"CALIBRATION_62_X0=",CTX[62].X0," T1=",CTX[62].T1)
    println(io,"ORIGINAL_AUTHOR_FULL_SCAN_NOT_EXECUTED=true")
    println(io,"ROOT_SOLVER=independent_GPT_adaptive_8_bisection_per_criterion_coarse_nonblind")
    println(io,"L2_BETA_NATIVE_CALLS=",length(MEASURES))
    for j in MASS_INDEX
        r=roots[j]
        @printf(io,"j%d_V1_minus_V0_dex=%.12f\n",j,r["V1"].root-r["V0"].root)
        @printf(io,"j%d_V2_minus_V0_dex=%.12f\n",j,r["V2"].root-r["V0"].root)
    end
    println(io,"NO_BBN_PHYSICAL_BOUND_NO_NOVELTY_NO_CANON_NO_EXEC_SIGN")
end
println("ROT007_L2_SCIENCE_COMPLETED ", length(MEASURES)," distinct PBH magic calls + 2 SBBN controls")
