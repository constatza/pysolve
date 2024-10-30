# test hello world csharp program with pytest

import pytest
from pysolve.loaders import load_assembly


def test_hello():
    # Load the DLL
    load_assembly("Test", assembly_dir="./lib/HelloWorldFromCS")

    from Test import Program

    program = Program()
    assert program.Main() == 0
