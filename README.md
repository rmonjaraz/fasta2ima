# fasta2ima
Convert a fasta alignment into IMa2/IMa3 format

## Input
- **Fasta file**
- **Populations vector** - A list of all populations in your fasta file.

Names in the Fasta file must start with the population name followed by sample name divided by an underscore " _ ". Names shoudl not be longer than 10 characters total.
    *Fasta example:*
    >Pop1_s1
    >Pop1_s2
    >Pop2_s1
    >Pop2_s2 

NOTES:
- Requires extra manipulation for inputting Pops, Tree and Number of Loci
- Poulation names vector must be provided in alphabetical order separeted by comma (",") and spelling must match alignments
- This script converts only one alignment by sorting and counting the alignment lenght, and pop sizes alphabetically
- Default values for mutation model is "I" (Infinite) and "1" (autosomal) for inheritance scalar, can be changed providing them as 2nd and 3rd arguments (always include 2nd and 3rd argument if changing any)
- For multiple fasta files can be used in a for loop and then cat output files together.

## Usage
`python fasta2ima.py [INPUT_FASTA] [POPS_VECTOR] [OPTIONAL ARGS]`

*Examples:* 

`python fasta2ima.py myFastafile.fasta Pop0,Pop1 H 0.25`

Without extra args default values is `I` and `1`

`python fasta2ima.py myFastafile.fasta Pop0,Pop1 `

## Requirements
- python 3.9.7
- Biopython 1.79

## License
The code within this repository is available under a 3-clause BSD license. See the License.txt file for more information.

## Citation
If you use this script for your own research, please provide the link to this software repository in your manuscript:
https://github.com/rmonjaraz/fasta2ima
