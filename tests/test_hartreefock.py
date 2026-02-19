#!/usr/bin/env python3

import numpy as np
import quimb.tensor as qtn
import scipy
from pyscf import gto, scf

from qpe_toolbox.hamiltonian import chemistry_hamiltonian

basis = "sto-3g"


def check_hf(mol, hf_mode, str_HF):
    # In the orbital_major convention (see pyscf_converter)
    #   qubit [0, norb) will be for the spin up
    #   qubit [norb, 2*norb) will be for the spin down
    # The Hartree-Fock state corresponds to one electron occupying the lowest orbs
    # for spin-up and spin down
    H = chemistry_hamiltonian(
        mol, hf_mode=hf_mode, encoding="original", do_fci=True, do_ccsd=False
    )

    H_mpo = H.to_mpo()
    psi_HF = qtn.MPS_computational_state(str_HF)
    E_HF = psi_HF.overlap(H_mpo.apply(psi_HF)) + H.e_const
    assert np.isclose(E_HF, H.e_hf, rtol=0, atol=1e-10)
    return H, psi_HF


def test_hartree_fock_H2():
    mol = gto.M(
        atom=[("H", (0.0, 0.0, 0.0)), ("H", (0.0, 0.0, 0.7414))],
        basis=basis,
        spin=0,
        verbose=0,
    )
    hf_mode = "rhf"
    mf = scf.RHF(mol)
    mf.verbose = 0
    mf.kernel()
    str_HF = ""
    for b in mf.mo_occ:
        if int(b):
            str_HF += "1"
        else:
            str_HF += "0"
    str_HF = str_HF * 2

    H, psi_HF = check_hf(mol, hf_mode, str_HF)
    H_sp = H.to_builder().build_sparse_matrix()
    eigvals, eigvecs = scipy.sparse.linalg.eigsh(H_sp, k=1, which="SA")
    E_ed = eigvals[0] + H.e_const
    assert abs(E_ed - H.e_fci) < 1e-10

    psi_ed = eigvecs[:, 0]
    overlap = abs(np.vdot(psi_HF.to_dense(), psi_ed)) ** 2
    assert abs(overlap - 0.9872699848699622) < 1e-12


def test_hartree_fock_ionizedH2():
    mol = gto.M(
        atom=[("H", (0.0, 0.0, 0.0)), ("H", (0.0, 0.0, 0.7414))],
        basis=basis,
        charge=1,
        spin=1,
        verbose=0,
    )
    hf_mode = "uhf"
    mf = scf.UHF(mol)
    mf.verbose = 0
    mf.kernel()
    str_HF = ""
    for b in np.ravel(mf.mo_occ):
        str_HF += str(int(b))
    check_hf(mol, hf_mode, str_HF)


if __name__ == "__main__":
    test_hartree_fock_H2()
    test_hartree_fock_ionizedH2()
