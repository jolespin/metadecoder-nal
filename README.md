# MetaDecoder

An algorithm for clustering metagenomic sequences [Modified by [Josh L. Espinoza](https://github.com/jolespin) for [Pyrodigal]((https://github.com/althonos/pyrodigal)) and [PyHMMSearch]((https://github.com/jolespin/pyhmmsearch)) support]

Cite [MetaDecoder](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-022-01237-8):

Liu, CC., Dong, SS., Chen, JB. et al. MetaDecoder: a novel method for clustering metagenomic contigs. Microbiome 10, 46 (2022). [https://doi.org/10.1186/s40168-022-01237-8](https://doi.org/10.1186/s40168-022-01237-8)

## Dependencies

* [python](https://www.python.org/)
* [numpy](https://pypi.org/project/numpy/)
* [scipy](https://pypi.org/project/scipy/)
* [scikit-learn](https://pypi.org/project/scikit-learn/)
* [threadpoolctl](https://pypi.org/project/threadpoolctl/)
* [pyrodigal](https://github.com/althonos/pyrodigal)
* [pyhmmsearch](https://github.com/jolespin/pyhmmsearch)

## Installation

### Download and install MetaDecoder-NAL

```bash
pip install -U https://github.com/jolespin/metadecoder-nal/releases/download/1.1.1rc4/metadecoder-1.1.1rc4.tar.gz
```

The NewAtlantis Labs fork of MetaDecoder uses **Pyrodigal** and **PyHMMSearch** for predicting protein coding genes (if not proteins are provided) and mapping single-copy marker genes to contigs, respectively.

MetaDecoder has included the compiled FragGeneScan (version 1.31) and Hmmer (version 3.2.1).

### The GPU version of MetaDecoder

MetaDecoder can be accelerated using the GPU on the basis of **CUDA** and **[CuPy](https://cupy.dev/)**.

To use the GPU version of Metadecoder, you need to have a compatible driver installed for your GPU (**CUDA**), and then install CuPy using pip3:

```shell
# You may need to install and upgrade setuptools and wheel using pip3 before. #
pip3 install --upgrade setuptools wheel
# Please note that XXX is the CUDA version. e.g. cupy-cuda101 means CuPy with CUDA 10.1. #
pip3 install cupy-cudaXXX
```

Please be careful not to install multiple CuPy packages at the same time.

MetaDecoder will automatically enable GPU if it is available.

And moreover, CuPy can use additional CUDA library (**cuTENSOR**) to accelerate tensor operations: **UNTESTED**

```shell
# Please note that XXX is the CUDA version. #
python3 -m cupyx.tools.install_library --cuda XXX --library cutensor
# Setting the environment variable to activate some CUDA features in CuPy. #
echo 'export CUPY_ACCELERATORS="cutensor"' >> ~/.bashrc
```

## Usage

### Preparations

**Before running MetaDecoder, you may need to prepare some files by yourself.**

* A FASTA formatted assembly file: **ASSEMBLY.FASTA**

* Some sorted BAM formatted read files with the **SAME HEADER**: **SAMPLE1.BAM**, **SAMPLE2.BAM** ...

### Run MetaDecoder

#### Obtain the coverages of contigs

Input: **SAMPLE1.BAM**, **SAMPLE2.BAM**, **...**

Output: **METADECODER.COVERAGE**

```shell
metadecoder coverage -b SAMPLE1.BAM ... SAMPLE2.BAM  -o METADECODER.COVERAGE
```


#### Map single-copy marker genes to the assembly

Input: **ASSEMBLY.FASTA**

Output: **METADECODER.SEED**

```shell
metadecoder seed --threads 4 -f ASSEMBLY.FASTA -o METADECODER.SEED
```

#### Run MetaDecoder algorithm to cluster contigs

Input: **ASSEMBLY.FASTA**, **METADECODER.COVERAGE**, **METADECODER.SEED**

Output: **METADECODER.1.FASTA**, **METADECODER.2.FASTA**, ...

```shell
metadecoder cluster -f ASSEMBLY.FASTA -c METADECODER.COVERAGE -s METADECODER.SEED -o METADECODER
```

Since v1.0.17, MetaDecoder can load multiple coverage files for clustering.

```shell
metadecoder cluster -f ASSEMBLY.FASTA -c *.METADECODER.COVERAGE -s METADECODER.SEED -o METADECODER
```

## References

* Mina Rho, Haixu Tang, and Yuzhen Ye. FragGeneScan: Predicting Genes in Short and Error-prone Reads. Nucl. Acids Res., 2010 doi: 10.1093/nar/gkq747.

* nhmmer: DNA Homology Search With Profile HMMs. T. J. Wheeler, S. R. Eddy. Bioinformatics, 29:2487-2489, 2013.
