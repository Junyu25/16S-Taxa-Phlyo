import os
import sys
from Bio import SeqIO

fasta = sys.argv[1]
mergedSeq = []

for seq in SeqIO.parse(fasta, "fasta"):
    #print(seq.description)
    if "(merged)" in seq.description:
        seq.id = seq.id.split(",")[0].replace("_F", "")
        seq.name = seq.description
        seq.description = ""
        mergedSeq.append(seq)

SeqIO.write(mergedSeq, os.path.join(os.path.split(fasta)[0], "mergedSeq_clean.fasta"), "fasta")