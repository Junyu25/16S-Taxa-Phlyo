'''
Copyright {2020} Junyu Chen

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

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