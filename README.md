# msaconverter
THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.

**WHEN YOU ADAPT (PART OF) THE SOFTWARE FOR YOUR USE CASES, THE AUTHOR AND
THE SOFTWARE MUST BE EXPLICITLY CREDITED IN YOUR PUBLICATIONS AND SOFTWARE,
AND YOU SHOULD ASK THE USERS OF YOUR SOFTWARE TO CITE THE SOFTWARE IN
THEIR PUBLICATIONS. IN A WORD, 请讲武德.**

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
                       [-q {fasta,clustal,stockholm,nexus,phylip,phylip-sequential,phylip-relaxed,phylip-sequential-relaxed,mauve,maf}]
                       [-t {DNA,RNA,protein}]

    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
    REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
    AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
    INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
    LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
    OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
    PERFORMANCE OF THIS SOFTWARE.

    **WHEN YOU ADAPT (PART OF) THE SOFTWARE FOR YOUR USE CASES, THE AUTHOR AND
    THE SOFTWARE MUST BE EXPLICITLY CREDITED IN YOUR PUBLICATIONS AND SOFTWARE,
    AND YOU SHOULD ASK THE USERS OF YOUR SOFTWARE TO CITE THE SOFTWARE IN
    THEIR PUBLICATIONS. IN A WORD, 请讲武德.**

    Convert multiple-sequence-alignment into different formats.
    See https://biopython.org/wiki/AlignIO for format introductions.

    V0.0.3:
    phylip-sequential-relaxed (for output) is a custom format by MGL, which
    allows long sequence names but like phylip-sequential.

    By Guanliang MENG, available from https://github.com/linzhi2013/msaconverter.

    optional arguments:
      -h, --help            show this help message and exit
      -i <INFILE>           input msa file
      -o <OUTFILE>          output msa file
      -p {fasta,clustal,stockholm,nexus,phylip,phylip-sequential,phylip-relaxed,mauve,maf}
                            input msa format [fasta]
      -q {fasta,clustal,stockholm,nexus,phylip,phylip-sequential,phylip-relaxed,phylip-sequential-relaxed,mauve,maf}
                            input msa format [phylip-relaxed]
      -t {DNA,RNA,protein}  Molecule types [DNA]


## 4 Author
Guanliang MENG

## 5 Citation

Since `msaconverter` makes use of `Biopython`, you should cite it if you use `msaconverter` in your work:

    Peter J. A. Cock, Tiago Antao, Jeffrey T. Chang, Brad A. Chapman, Cymon J. Cox, Andrew Dalke, Iddo Friedberg, Thomas Hamelryck, Frank Kauff, Bartek Wilczynski, Michiel J. L. de Hoon: “Biopython: freely available Python tools for computational molecular biology and bioinformatics”. Bioinformatics 25 (11), 1422–1423 (2009). https://doi.org/10.1093/bioinformatics/btp163

Please go to `http://www.biopython.org/` for more details.






