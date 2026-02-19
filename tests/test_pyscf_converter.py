#!/usr/bin/env python3

from openfermion.transforms import jordan_wigner
from pyscf import gto, scf

from qpe_toolbox.hamiltonian.pyscf_converter import (
    do_df,
    do_sf,
    get_integrals_rhf,
    make_fermionic_hamiltonian_rhf,
)


def test_basics_H2():
    molecule = gto.M(
        atom=[("H", (0.0, 0.0, 0.0)), ("H", (0.0, 0.0, 0.735))],
        unit="A",
        basis="sto-3g",
    )
    hf = scf.RHF(molecule)
    hf.verbose = 0
    hf.kernel()
    _ncas, _nelec, ecore, hpq, hpqrs = get_integrals_rhf(hf)

    fermionic_operator = make_fermionic_hamiltonian_rhf(ecore, hpq, hpqrs)
    _qubit_operator = jordan_wigner(fermionic_operator)
    # qubit_operator.terms contains a dictionary of the Pauli terms along with its coefficients
    # the keys are the Pauli strings and the value are the coefficients
    # the pauli terms are written as a tuple
    # eg. X_4 Z_3 Y_1 is written as ((1, 'Y'), (3, 'Z'), (4, 'X'))
    # so far the output is in ascending qubit order but I don't know if that order is guaranteed

    _rank, _diff, hpqrs_sf = do_sf(hpqrs)
    fermionic_operator = make_fermionic_hamiltonian_rhf(ecore, hpq, hpqrs_sf)
    _qubit_operator = jordan_wigner(fermionic_operator)

    _neig, _rank, _df_factors, hpqrs_df, _diff = do_df(hpqrs)
    fermionic_operator = make_fermionic_hamiltonian_rhf(ecore, hpq, hpqrs_df)
    _qubit_operator = jordan_wigner(fermionic_operator)


if __name__ == "__main__":
    test_basics_H2()
