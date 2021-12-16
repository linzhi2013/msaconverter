#!/usr/bin/env python3
import sys
from Bio import AlignIO
import argparse

def get_para():
    description = 'Convert multiple-sequence-alignment into different formats. See https://biopython.org/wiki/AlignIO for format introductions. By Guanliang MENG.'

    # https://biopython.org/wiki/AlignIO
    msa_formats = ['fasta', 'clustal', 'stockholm', 'nexus', 'phylip', 
        'phylip-sequential', 'phylip-relaxed', 'mauve', 'maf']

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('-i', dest='infile', metavar='<INFILE>', 
        help='input msa file')

    parser.add_argument('-o', dest='outfile', metavar='<OUTFILE>', 
        help='output msa file')

    parser.add_argument('-p', dest='input_format', 
        choices=msa_formats, default='fasta',
        help='input msa format [%(default)s]')

    parser.add_argument('-q', dest='output_format',
        choices=msa_formats, default='phylip-relaxed',
        help='input msa format [%(default)s]')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    else:
        args = parser.parse_args()

    return args


def main():
    args = get_para()

    AlignIO.convert(args.infile, args.input_format, args.outfile, args.output_format)


if __name__ == '__main__':
    main()