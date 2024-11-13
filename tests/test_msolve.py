
import pytest
from pysolve.loaders import load_assembly


def test_CantileverBeam2DTest():
    # Load the DLL
    load_assembly("MGroup.FEM.Structural.Tests.dll",
                  assembly_dir="/home/archer/projects/mgroup/MSolve.Tests/tests/MGroup.FEM.Structural.Tests/bin/Debug/net6.0/")

    # Reload the assembly to be certain
    from MGroup.FEM.Structural.Tests.Integration import CantileverBeam2DTest

    # need to create an instance of the test class
    # ITestOutputHelper must be removed or mocked, cause can't import in python
    test = CantileverBeam2DTest()
    test.RunTest()







