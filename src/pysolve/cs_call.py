from typing import Optional
from pathlib import Path
import subprocess
from logging import getLogger

logger = getLogger(__name__)



from pythonnet import load
# Load and set the coreclr (the .NET Core runtime)
load("coreclr")
import clr


def build_assembly(
        csproj_path: str,
        build_dir: str,
) -> None:
    """
    Builds a C# project and dynamically loads the required assemblies into Python using pythonnet.

    Args:
        csproj_path (str): Path to the .csproj file.
        build_dir (str): Directory where the project will be built.
        modules_to_import (Dict[str, List[str]]): Dictionary where keys are assembly names, and values are lists of modules to import.
        force_rebuild (bool): If True, rebuilds the project even if already built.

    Raises:
        FileNotFoundError: If the .csproj file is not found.
        RuntimeError: If the build process fails.
    """
    # Ensure the .csproj file exists
    csproj_path = Path(csproj_path)
    if not csproj_path.exists():
        raise FileNotFoundError(f".csproj file not found at {csproj_path}")

    # Ensure the build directory exists
    build_dir_path = Path(build_dir)
    build_dir_path.mkdir(parents=True, exist_ok=True)

    # Check if the project is already built

    try:
        logger.info("Building the project.")
        subprocess.run(
            ["dotnet", "build", csproj_path, "-o", build_dir],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        logger.info("Project built successfully.")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(
            f"Build failed with error:\n{e.stderr.decode('utf-8')}"
        )

