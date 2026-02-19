# Installation Guide

```{warning}
On Windows, QPE Toolbox is supported only through the Windows Subsystem for Linux (WSL) due to dependency constraints.
```

## Requirements
QPE Toolbox is a pure python library and will run on any system as long as its dependencies support it. In practice, this means any 64-bit macOS or Linux distribution should work. Due to [PySCF restrictions](https://pyscf.org/user/install.html), Windows is only supported through the Windows Subsystem for Linux (WSL).

## Installation

**Installing with `pip`**

```bash
pip install qpe-toolbox
```

**Installing with `conda`**

```bash
conda install qpe-toolbox
```

**Installing directly from GitHub**

```bash
git clone https://github.com/quobly-sw/qpe-toolbox
cd qpe-toolbox
pip install .
```


**Documentation toolchain**

To build the documentation locally:

```bash
pip install ".[docs]"
make -C docs html
```
