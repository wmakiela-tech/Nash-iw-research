# PREREG_090: BlackHawk instantaneous PRIMARY spectra on the authors' 100-mass grid (input for folding modern multiplicities).
# Derived from gen_hadron_table_085.jl for the Wu-Xu code (arXiv:2509.05618, repo d395183).
# Reproduces the authors' notebook valid_hadrons_from_BlackHawk.ipynb cells 12-13 (mass grid, BlackHawk_inst call,
# trapezoid in log E over the secondary-energy grid, output format), with the hadronization generator and the
# primary-energy window as arguments. Uses the authors' own tool scripts (read-only include) and a BlackHawk v2.3
# build (tarball SHA256 dd148349...a7 = authors' Artifacts.toml) with the authors' exit-code hack overlaid.
#
# Usage: julia primary_spectra_090.jl <wuxu_src> <blackhawk_dir> <out_file> <hadronization_choice> <Emin_GeV> <Emax_GeV> <E_number> <tag>
# Output: tab-separated, one row per (mass row k, energy): k, m_PBH[g], energy[GeV], primary columns as written by BlackHawk;
# also the five secondary totals per mass (same trapezoid as the authors) for the folding gate.
#   hadronization_choice: 0 = PYTHIA (BBN epoch, authors' choice), 1 = HERWIG (BBN epoch)
# Output columns (authors' header and units): m_PBH [GeV], dN/dt for pi+-, K+-, K0L, p, n [GeV].
# Exits nonzero on any BlackHawk failure or non-finite/negative yield.

const SRC = ARGS[1]
const BlackHawk_directory = ARGS[2]
const BlackHawk_results_directory = joinpath(BlackHawk_directory, "results")
const OUT = ARGS[3]
const HCHOICE = parse(Int, ARGS[4])
const EMIN = parse(Float64, ARGS[5])
const EMAX = parse(Float64, ARGS[6])
const ENUM = parse(Int, ARGS[7])
const TAG = ARGS[8]

using DelimitedFiles
using Statistics
include(joinpath(SRC, "tool_script-parameters.jl"))        # defines EU = GeV, NU = NaturalUnit(EU)
include(joinpath(SRC, "tool_script-geomspace.jl"))
include(joinpath(SRC, "tool_script-BlackHawk_extension.jl"))

@assert HCHOICE in (0, 1)

m_PBH_list = geomspace(1e9, 4e12, 100) .* NU.g
species = ["pipm", "Kpm", "K0L", "proton", "neutron"]
Y = zeros(Float64, length(m_PBH_list), length(species))
trap(E, f) = begin
    integrand = E .* f
    h = mean(log.(E[begin+1:end]) .- log.(E[begin:end-1]))
    (h / 2) * (2 * sum(integrand) - (first(integrand) + last(integrand)))
end
@assert !isfile(OUT) "REFUSE_OVERWRITE"
io = open(OUT, "w")
hdr = nothing
for (ii, m_PBH) in enumerate(m_PBH_list)
    params = BlackHawkParameters()
    name = "iw090_$(TAG)_$(lpad(ii, 3, '0'))"
    rdir = joinpath(BlackHawk_results_directory, name)
    rm(rdir; force=true, recursive=true)
    set_BlackHawk_name!(params, name)
    set_BlackHawk_mass!(params, m_PBH; NU=NU)
    set_BlackHawk_energy_spectrum!(params, GeV(EMIN), GeV(EMAX), ENUM)
    close_BlackHawk_dark_matter!(params)
    params.hadronization_choice = HCHOICE
    run_BlackHawk_inst(params)
    pri, sec = read_BlackHawk_instantaneous_spectra(rdir)
    keys_p = sort(collect(keys(pri)))
    global hdr
    if hdr === nothing
        hdr = keys_p
        write(io, "k\tm_g\t" * join(keys_p, "\t") * "\n")
    end
    @assert keys_p == hdr
    for j in 1:length(pri["energy"])
        write(io, string(ii - 1, "\t", Float64(m_PBH / NU.g), "\t", join([repr(pri[c][j]) for c in keys_p], "\t"), "\n"))
    end
    for (k, s) in enumerate(species)
        Y[ii, k] = trap(sec["energy"], sec[s])
    end
    rm(rdir; force=true, recursive=true)
end
close(io)
open(OUT * ".secondary_totals.tsv", "w") do f
    write(f, "k\tm_g\t" * join(species, "\t") * "\n")
    for ii in 1:length(m_PBH_list)
        write(f, string(ii - 1, "\t", Float64(m_PBH_list[ii] / NU.g), "\t", join([repr(Y[ii, k]) for k in 1:5], "\t"), "\n"))
    end
end
println("IW090_PRIMARY_DONE rows=$(length(m_PBH_list)) columns=$(hdr)")
