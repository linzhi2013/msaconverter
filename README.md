# msaconverter

## 1 Introduction

`msaconverter` is a tool to convert a multiple sequence alignment into different format with `Biopython` (http://www.biopython.org/)

## 2 Installation

[![install with bioconda](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg?style=flat)](http://bioconda.github.io/recipes/msaconverter/README.html)

    pip install msaconverter
    # or using Bioconda
    conda install msaconverter

There will be a command `msaconverter` created under the same directory as your `pip` command.

## 3 Usage

    $ msaconverter
    usage: msaconverter.py [-h] [-i <INFILE>] [-o <OUTFILE>]
                           [-p {fasta,clustal,stockholm,nexus,phylip,phylip-sequential,phylip-relaxed,mauve,maf}]
                           [-q {fasta,clustal,stockholm,nexus,phylip,phylip-sequential,phylip-relaxed,mauve,maf}]

    Convert multiple-sequence-alignment into different formats. See
    https://biopython.org/wiki/AlignIO for format introductions. By Guanliang
    MENG.

    optional arguments:
      -h, --help            show this help message and exit
      -i <INFILE>           input msa file
      -o <OUTFILE>          output msa file
      -p {fasta,clustal,stockholm,nexus,phylip,phylip-sequential,phylip-relaxed,mauve,maf}
                            input msa format [fasta]
      -q {fasta,clustal,stockholm,nexus,phylip,phylip-sequential,phylip-relaxed,mauve,maf}
                            input msa format [phylip-relaxed]


## 4 Author
Guanliang MENG

## 5 Citation
Currently I have no plan to publish `msaconverter`, **however, if you use this program in your analysis, or you "steal" the idea/codes of this program into your script, I should be one of the co-authors in your publication!!!**

However, since `msaconverter` makes use of `Biopython`, you should cite it if you use `msaconverter` in your work:

    Peter J. A. Cock, Tiago Antao, Jeffrey T. Chang, Brad A. Chapman, Cymon J. Cox, Andrew Dalke, Iddo Friedberg, Thomas Hamelryck, Frank Kauff, Bartek Wilczynski, Michiel J. L. de Hoon: “Biopython: freely available Python tools for computational molecular biology and bioinformatics”. Bioinformatics 25 (11), 1422–1423 (2009). https://doi.org/10.1093/bioinformatics/btp163

Please go to `http://www.biopython.org/` for more details.






