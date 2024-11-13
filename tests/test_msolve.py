
import pytest
from pysolve.loaders import load_assembly

load_assembly(
    "MGroup.Constitutive.Structural",
    "MGroup.NumericalAnalyzers",
    "MGroup.Solvers",
    "MGroup.FEM.Structural.Tests",
    assembly_dir="/home/archer/projects/MSolve.Tests/tests/MGroup.FEM.Structural.Tests/bin/Debug/net6.0")

# Import the required .NET classes
from MGroup.Constitutive.Structural import StructuralDof, ProblemStructural
from MGroup.NumericalAnalyzers import LinearAnalyzer, StaticAnalyzer
from MGroup.Solvers.Direct import SkylineSolver
from MGroup.FEM.Structural.Tests.ExampleModels import CantileverBeam2DExample


def test_CantileverBeam2DTest():

    # Create the model using the ExampleModel class
    model = CantileverBeam2DExample.CreateModel()

    # Solve the model and compute displacement
    computed_displacement = solve_model(model)

    # Compare the computed and expected displacements
    expected_displacement = CantileverBeam2DExample.expected_solution_node2_TranslationY
    assert abs(computed_displacement - expected_displacement) < 1e-6, \
        f"Test failed: Expected {expected_displacement}, but got {computed_displacement}"



def solve_model(model) -> float:
    # Set up solver factory and create solver
    solver_factory = SkylineSolver.Factory()
    algebraic_model = solver_factory.BuildAlgebraicModel(model)
    solver = solver_factory.BuildSolver(algebraic_model)
    problem = ProblemStructural(model, algebraic_model)

    # Set up analyzers
    linear_analyzer = LinearAnalyzer(algebraic_model, solver, problem)
    static_analyzer = StaticAnalyzer(algebraic_model, problem, linear_analyzer)

    # Run analysis
    static_analyzer.Initialize()
    static_analyzer.Solve()

    # Extract displacement from the solution
    computed_displacement = algebraic_model.ExtractSingleValue(
        solver.LinearSystem.Solution,
        model.NodesDictionary[2],
        StructuralDof.TranslationY
    )
    return computed_displacement
