#!/bin/bash

echo "In: $1";
echo "Out: $2";
echo $1"/merged_seqs.fasta"
#

python ./scripts/processing-merged-seq.py -i $1 -o $2

python ./scripts/seq_quality_trimming.py -i $2"/merged_seqs.fasta"

python ./scripts/16S-Taxa-Phylo-Pipeline.py -i $2"/mergedSeq_clean.fasta" -o $2



