
from pysolve.cs_call import build_assembly
from pysolve.loaders import load_assembly

# Example usage
def test_build():
    # Path to the .csproj file
    csproj_file = "/home/archer/projects/MSolve.Tests/tests/MGroup.FEM.Structural.Tests/MGroup.FEM.Structural.Tests.csproj"

    # Build output directory
    build_directory = "./bin/"


    # Build and load assemblies
    build_assembly(csproj_file, build_directory)
    load_assembly(
        "MGroup.Constitutive.Structural",
        "MGroup.NumericalAnalyzers",
        "MGroup.Solvers",
        "MGroup.FEM.Structural.Tests",
        assembly_dir=build_directory)

    from MGroup.Constitutive.Structural import StructuralDof, ProblemStructural
    from MGroup.NumericalAnalyzers import LinearAnalyzer, StaticAnalyzer
    from MGroup.Solvers.Direct import SkylineSolver
    from MGroup.FEM.Structural.Tests.ExampleModels import CantileverBeam2DExample
