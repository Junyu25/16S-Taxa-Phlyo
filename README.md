# 16S-Taxa-Phlyo Pipeline
Use 16S Sanger sequencing to identify the taxa of culturomics
This pipeline utilize the feature of QIIME 2


![](img/16s-taxa-phylo.png)


## Quality trimming

* Isolate segment with the highest quality from the sequence, using Kadane's algorithm.
* Trim low-quality ends of the sequence.

## Merging reads
* Align the forward/reverse PCR products using the Smith-Waterman algorithm for local alignment.
* Merge the reads if the overlap is large enough.