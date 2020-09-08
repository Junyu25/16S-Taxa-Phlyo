import os
import argparse

from qiime2 import Artifact
from qiime2.plugins.phylogeny.pipelines import align_to_tree_mafft_fasttree
from qiime2.plugins.feature_classifier.methods import classify_consensus_vsearch


parser = argparse.ArgumentParser(description='Run Diamond')
parser.add_argument('-i', '--input', dest='fileDir', type=str, required=True,
                    help="the path of the reads")
parser.add_argument('-o', '--output', dest='OpDir', type=str, required=True,
                    help="the output path of reads")
parser.add_argument('-r', '--ref_reads', dest='reference_reads', type=str,  required=False, default="/mnt/d/Lab/TaxaIdentification/classifier/silva-138-99-seqs.qza",
                    help="the reference_reads path")
parser.add_argument('-t', '--ref_taxa', dest='reference_taxonomy', type=str,  required=False, default="/mnt/d/Lab/TaxaIdentification/classifier/silva-138-99-tax.qza",
                    help="the reference_taxonomy path")

args = parser.parse_args()

inputDir = os.path.abspath(args.fileDir)
outputDir = os.path.abspath(args.OpDir)
ref_reads = os.path.abspath(args.reference_reads)
ref_taxa = os.path.abspath(args.reference_taxonomy)


artifact = Artifact.import_data('FeatureData[Sequence]',
                                inputDir
                                )

reference_reads =  Artifact.load(ref_reads)
reference_taxonomy = Artifact.load(ref_taxa)

taxonomy = classify_consensus_vsearch(artifact, 
                           reference_reads,
                           reference_taxonomy,
                           threads = 8)


mafft_alignment = align_to_tree_mafft_fasttree(artifact, 8)

Artifact.export_data(taxonomy.classification, outputDir)
Artifact.export_data(mafft_alignment.tree, outputDir)