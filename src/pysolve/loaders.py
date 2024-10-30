from pathlib import Path
from typing import Optional

from pythonnet import load

# Load and set the coreclr (the .NET Core runtime)
load("coreclr")
import clr


def load_assembly(*modules: str, assembly_dir: Optional[str] = None):
    """
    Load the specified .NET assemblies and return the loaded modules.
    :param modules:
    :param assembly_dir:
    :return:
    """
    # Load the specified assemblies
    assembly_dir = Path(assembly_dir) if assembly_dir else Path(__file__).resolve().parent
    for module in modules:
        clr.AddReference(str(assembly_dir / module))



