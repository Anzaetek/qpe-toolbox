#!/usr/bin/env python3

import numpy as np
import quimb.tensor as qtn

from qpe_toolbox.tensor import kron_mpos, kron_mps

# define


def test_kronmps():
    mps1 = qtn.MPS_computational_state("1011")
    mps2 = qtn.MPS_computational_state("001")

    mps_ref = qtn.MPS_computational_state("1011001")
    res = kron_mps(mps1, mps2)
    assert abs(1 - res.overlap(mps_ref)) < 1e-10

    mps1 = qtn.MPS_computational_state("1")
    mps2 = qtn.MPS_computational_state("001")

    mps_ref = qtn.MPS_computational_state("1001")
    res = kron_mps(mps1, mps2)
    assert abs(1 - res.overlap(mps_ref)) < 1e-10

    mps_ref = qtn.MPS_computational_state("0011")
    res = kron_mps(mps2, mps1)
    assert abs(1 - res.overlap(mps_ref)) < 1e-10


def test_kronmpos():
    Id1 = qtn.MatrixProductOperator([np.eye(2)])
    Id2 = qtn.MPO_identity(2)
    Id3 = qtn.MPO_identity(3)

    myId3 = kron_mpos(Id2, Id1)
    assert abs((myId3 - Id3).norm()) < 1e-10

    myId3_bis = kron_mpos(Id1, Id2)
    assert abs((myId3_bis - Id3).norm()) < 1e-10


# run
if __name__ == "__main__":
    test_kronmps()
    test_kronmpos()
