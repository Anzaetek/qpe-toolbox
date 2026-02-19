#!/usr/bin/env python3

import pkgutil

import qpe_toolbox


def test_has_version():
    assert hasattr(qpe_toolbox, "__version__")
    assert type(qpe_toolbox.__version__) is str


def test_package_contains_submodules():
    submodules = {m.name for m in pkgutil.iter_modules(qpe_toolbox.__path__)}
    assert "circuit" in submodules
    assert "estimation" in submodules
    assert "hamiltonian" in submodules
    assert "tensor" in submodules


if __name__ == "__main__":
    test_has_version()
    test_package_contains_submodules()
