using Pkg

envdir = abspath(ARGS[1])
Pkg.activate(envdir)

specs = [
    PackageSpec(name="ArbNumerics", version="1.6.3"),
    PackageSpec(name="DataInterpolations", version="8.8.0"),
    PackageSpec(name="DifferentialEquations", version="7.17.0"),
    PackageSpec(name="Format", version="1.3.7"),
    PackageSpec(name="ForwardDiff", version="1.3.1"),
    PackageSpec(name="IrrationalConstants", version="0.2.6"),
    PackageSpec(name="JLD2", version="0.6.3"),
    PackageSpec(name="SpecialFunctions", version="2.6.1"),
]

for spec in specs
    Pkg.add(spec)
end

Pkg.add(PackageSpec(
    url="https://github.com/Fenyutanchan/NaturalUnits.jl.git",
    rev="4a9f007ff1df416c9fef28c4d83d8fe8846099cf",
))

Pkg.precompile()
Pkg.status()
