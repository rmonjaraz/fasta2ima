#!/usr/bin/env python
# coding: utf-8

"""
@author: Rodrigo Monjaraz-Ruedas (monroderik@gmail.com)

- Convert a fasta alignment into IMa2/IMa3 format

- NAMES IN THE FASTA FILE MUST START WITH THE POPULATION NAME DIVIDED BY A "_" (UNDERSCORE) FROM THE REST OF THE NAME and not be longer than 10 characters (TOTAL)
    example:
    >Pop0_s1
    >Pop0_s2
    >Pop1_s1
    >Pop1_s2 

- Requires extra manipulation for inputting Pops, Tree and Number of Loci
- Poulation names vector must be provided in alphabetical order separeted by comma (",") and spelling must match alignments
- This Script converts only one alignment by sorting and counting the alignment lenght, and pop sizes alphabetically
- Default values for mutation model is "I" (Infinite) and "1" (autosomal) for inheritance scalar, can be changed providing them as 2nd and 3rd arguments (always include 2nd and 3rd argument if changing any)
- For multiple fasta files can be used in a for loop and then cat output files together.

Usage: python fasta2ima.py [INPUT_FASTA] [POPS_VECTOR] [OPTIONAL ARGS]

Example: python fasta2ima.py myFastafile.fasta Pop0,Pop1 H 0.25

Example: python fasta2ima.py myFastafile.fasta Pop0,Pop1  # Without extra args default values is I and 1

requirements:
- python 3.9.7
- Biopython 1.79

"""


from Bio import AlignIO
from contextlib import redirect_stdout
import sys
import os


# Get Arguments
fasta_file=open(sys.argv[1])
pops_names=list(sys.argv[2].split(','))
mu_rate=sys.argv[3] if len(sys.argv) > 3 else "I"
in_schalar=sys.argv[4] if len(sys.argv) > 4 else "1"

# Set some lists and dicts
name = os.path.splitext(os.path.basename(str(sys.argv[1])))[0]
idkeep = []

# read in alignment
alignment = AlignIO.read(open(str(sys.argv[1])), "fasta")
#Sort Alignment by ID
alignment.sort()
# Get maximum length
max_len = alignment.get_alignment_length()
# Iterate over sequences for getting pop names and counting occurences of each pop
for record in alignment:
    idkeep.append(record.id.split('_')[0])
pop_sizes =[idkeep.count(i) for i in sorted(pops_names)]

# Create heading with info for the alignment
heading = name,' '.join(map(str, pop_sizes)),str(max_len),mu_rate,in_schalar


# Write out the file
with open(name + ".u", 'w') as f:
    with redirect_stdout(f):
        print(*heading)
        for record in alignment:
            print(record.id + " " + record.seq)




