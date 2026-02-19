![qpe-toolbox logo](docs/source/_static/qpe-toolbox.png)


`qpe-toolbox` is an open-source python package, which
combines quantum chemistry and tensor networks methods to compile and simulate the quantum circuits of
the quantum phase estimation (QPE) algorithm.

We articulate the toolbox on top of the tensor-network library [`quimb`](https://github.com/jcmgray/quimb) to provide: (1) classical preprocessing strategies focused
on initializing and setting up QPE circuits, (2) an internal circuit-level simulator, and (3) a list of postprocessing
functionalities for retrieving final energies.
For the preprocessing stage, the QPE Toolbox offers fermionic encodings based on [`openFermion`](https://quantumai.google/openfermion) and [`pyscf`](https://pyscf.org/).

>[!WARNING]
> **This project is "pre-alpha", and is not yet stable. The API is subject to significant changes.**


# Installation
Open a terminal and clone this repository with
```bash
git clone git@github.com:quobly-sw/qpe-toolbox.git && cd qpe-toolbox
```

Create a virtual environment with either `pip` or `uv`
```bash
# with pip
python3 -m venv --system-site-packages .venv

# with uv
uv venv
```
Activate it
```bash
source .venv/bin/activate
```
Then install the package and its dependencies
```bash
# with pip
pip install -e .

# with uv
uv pip install -e .
```

# Requirements
`numpy`, `openfermion`, `pyscf`, `quimb`, `scipy` are core dependencies. `pytest` is only used to run the test. `jupyterlab` and `jupytext` are needed to run the examples as notebooks. `kahypar` and `optuna` are `quimb` optional dependencies used to speed-up computations.
### A note on Jupytext
The examples are notebooks encoded in the `py:percent` format with a `.py` extension. In `jupyterlab` right-click and select "Open with > Notebook" or "Jupytext Notebook".
The examples folder contains a `jupytext.toml` file. It is a configuration file that associates the `.py` scripts with a twin `.ipynb` notebook (this allows you to save the notebook's outputs in your local repository).
See https://jupytext.readthedocs.io/en/latest/ for more on how Jupytext works.


# Basic workflow

To perform Quantum Phase Estimation with the toolbox, take the following steps:
1. Choose a system: spin model or molecule. The `Hamiltonian` class describes the qubit Hamiltonian.
2. Prepare a guess state with DMRG (see the `dmrg` example) or circuit optimization (see `tn_circuit_optimization` example)
3. Encode $\hat{H}$ into a unitary:
  3.1. exact time evolution or Trotterization as methods in the `Hamiltonian` class
  3.2. qubitization functions: `lcu_walk_operator`
4. Initialize circuit: `make_circ` from `circuit.initialization`
5. Run QPE: in `estimation` module
  5.1. textbook QPE: `phase_estimation`
  5.2. Robust Phase Estimation (single-ancilla): `robust_phase_estimation`

# Contents

The package is divided in four main modules:

## circuit
Initialize a circuit with a phase register and a physical register. Count gates.
Manipulate control qubits e.g. shift them to account for an auxiliary register.

## estimation
Perform QPE. Three methods are currently available:
- textbook
- robust phase estimation
- LCU "simplified": we only build explicitly the SELECT oracle and provide the
PREPARE oracle-based reflection operator as an MPO.

## hamiltonian
Define the physical model. Available are the Heisenberg spin Hamiltonian, or
any molecule loaded from pyscf.gto module using Jordan-Wigner from openfermion.
Core component here is the Hamiltonian class.
Main features:
- conversion to MPO
- Trotter time evolution as a list of gates
- simple DMRG

## tensor
MPO-MPS manipulation tools:
- kronecker product (e.g. to add auxiliary qubits)
- addition of control qubits


# Examples
Here is a list of notebooks that introduce the basics of the package. They are available in the `examples` directory as plain `.py` files using the `py:percent` format. See the [note on Jupytext](#a-note-on-jupytext) in [Requirements](#requirements) section on how to convert them and execute as notebooks.

1. [`building_circuits`](examples/building_circuits.py) explains how to create, plot, record and load quantum circuits in `quimb` and `qiskit`.

2. [`chemistry_to_qubit`](examples/chemistry_to_qubit.py) describes how to build the qubit Hamiltonian and perform the Density Matrix Renormalization Group (DMRG) algorithm for a given molecule.

3. [`textbook_qpe`](examples/textbook_qpe.py) introduces the textbook Quantum Phase Estimation algorithm assuming time evolution is implemented exactly.

4. [`trotter_decomposition`](examples/trotter_decomposition.py) introduces the Trotter-Suzuki decomposition to implement a time evolution operator $U$.

5. [`qpe_with_trotter`](examples/qpe_with_trotter.py) studies the Quantum Phase Estimation algorithm using Trotterization of the evolution operator, and provides resource estimates.

6. [`qpe_with_lcu`](examples/qpe_with_lcu.py) gives an introduction to Block Encoding via Linear Combination of Unitaries.

7. [`robust_phase_estimation`](examples/robust_phase_estimation.py) introduces the Robust Phase Estimation algorithm, based on the Hadamard test circuit.

8. [`performance_mps`](examples/performance_mps.py) compares the performance of `quimb` and `qiskit` when contracting and sampling circuits with Matrix Product States.

9. [`hyperoptimization`](examples/hyperoptimization.py) presents advanced contraction schemes provided by `quimb`.

10. [`variational_circuit_preparation`](examples/variational_circuit_preparation.py) finds an initial guess state with variational circuit optimization.

# License

Apache 2.0

# Credits

2026 Foxconn, Quobly

Authors:
- Thibaud Louvet (thibaud.louvet@quobly.io)
- Calvin Ku (calvin.ku@foxconn.com)
- Yu-Cheng Chen (kesson.yc.chen@foxconn.com)
- Carlos Ramos Marimon (carlos.marimon@quobly.io)
- Olivier Gauthé (olivier.gauthe@quobly.io)
- Tristan Meunier (tristan.meunier@quobly.io)
- Min-Hsiu Hsieh (min-hsiu.hsieh@foxconn.com)
- Benoit Vermersch (benoit.vermersch@quobly.io)
