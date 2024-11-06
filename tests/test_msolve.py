
import pytest
from pysolve.loaders import load_assembly


def test_material():
    # Load the DLL
    load_assembly("MaterialStochastic",
                  assembly_dir="/home/archer/projects/mgroup/CntConcreteBayesian.Tests/MaterialStochastic/bin/x64/Release/net8.0/linux-x64/")
    import clr
    import System

    loaded_assemblies = System.AppDomain.CurrentDomain.GetAssemblies()
    for assembly in loaded_assemblies:
        print(assembly.FullName)

    # Reload the assembly to be certain
    from MaterialStochastic.Program import Main



    assert program.Main() == 0