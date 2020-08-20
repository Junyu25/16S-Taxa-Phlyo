from qiime2 import Artifact
from qiime2.plugins.phylogeny.pipelines import align_to_tree_mafft_fasttree

artifact = Artifact.import_data('FeatureData[Sequence]',
                                '/mnt/d/Lab/TaxaIdentification/16S-out-1.fasta'
                                )

mafft_alignment = align_to_tree_mafft_fasttree(artifact, 4)