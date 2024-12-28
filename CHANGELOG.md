# Change Log

* 1.1.0 - Added BAM support

* 1.0.3 (20211008): Initial version.

* 1.0.4 (20211029): Optimize the calculation of distance of pairwise kmer frequency.

* 1.0.5 (20211105): Optimize the counting process of kmers.

* 1.0.6 (20211207): Added an option (--no_clusters) to output only sequence IDs and the corresponding cluster IDs instead of sequences.

* 1.0.7 (20220206): Minor bugs fixed.

* 1.0.8 (20220315): Minor bugs fixed.

* 1.0.9 (20220508): Fix a bug that causes abnormal coverage when the "--mapq" parameter is set to 0.

* 1.0.10 (20220514): Minor bugs fixed.

* 1.0.11 (20220518): Minor bugs fixed.

* 1.0.12 (20220708): Minor bugs fixed.

* 1.0.13 (20220712): Minor bugs fixed.

* 1.0.14 (20220914): Minor bugs fixed.

* 1.0.15 (20221103): Minor bugs fixed.

* 1.0.16 (20221117): Minor bugs fixed.

* 1.0.17 (20230418): Multiple coverage files for clustering.

* 1.0.18 (20230816): Support gz formatted assemblies.

* 1.0.19 (20240125): Clusters will not participate in the calculation of the average of kmer distance if it contains more than 50,000 sequences.

* 1.1.0 (20241207): MetaDecoder has been updated to support sorted BAM files only, discontinuing support for SAM files [Thanks for @jolespin].

* 1.1.1rc1 (20241209): Added support for PyHMMSearch and Pyrodigal.  Also provides support for precomputed gene predictions.

* 1.1.1rc2 (20241210): Added support for custom HMMs and additional parameters for PyHMMSearch

* 1.1.1rc3 (20241214): Added support for Python 3.8 for CheckM2 (In addition to Python 3.9+)

* 1.1.1rc4 (20241226): Changed numpy.float64 to float for NumPy >= 1.24

* 1.1.1rc5 (20241228): Changed output to `.metadecoder.dpgmm` and `.metadecoder.kmers` to suffix the output file in `metadecoder cluster` instead of the input fasta.  Restored `numpy.float64` and `numpy.int64`.  Instead set limit `numpy<1.24`. Also creates output directory for files if one doesn't exist.

## Pending:
* Add precomputed `PyHMMSearch` results