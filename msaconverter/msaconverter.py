#!/usr/bin/env python3
import sys
from Bio import AlignIO
import argparse

def get_para():
    description = """
    Convert multiple-sequence-alignment into different formats. 
    See https://biopython.org/wiki/AlignIO for format introductions. 
    By Guanliang MENG.

    phylip-sequential-relaxed (for output) is a custom format by MGL, which 
    allows long sequence names but like phylip-sequential. """

    # https://biopython.org/wiki/AlignIO
    msa_formats = ['fasta', 'clustal', 'stockholm', 'nexus', 'phylip', 
        'phylip-sequential', 'phylip-relaxed', 'phylip-sequential-relaxed', 'mauve', 'maf']

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

    parser.add_argument('-t', dest='molecule_type',
        choices=["DNA", "RNA", "protein"], default="DNA",
        help='Molecule types [%(default)s]')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    else:
        args = parser.parse_args()

    return args


def get_phylip_sequential_relaxed(infile=None, input_format=None, outfile=None):
    alignment = AlignIO.read(infile, input_format)
    num_of_species = 0
    aln_len = 0

    seq_list = []
    max_seqid_len = 0
    for rec in alignment:
        num_of_species += 1
        aln_len = len(rec)
        seqid = rec.id
        seq = str(rec.seq)
        seq_list.append((seqid, seq))

        seqid_len = len(seqid)
        if seqid_len > max_seqid_len:
            max_seqid_len = seqid_len

    with open(outfile, 'w') as fhout:
        print(" {num_of_species} {aln_len}".format(num_of_species=num_of_species, aln_len=aln_len), file=fhout)
        for seqid, seq in seq_list:
            print(seqid.ljust(max_seqid_len), "  ", seq, file=fhout)


def main():
    args = get_para()

    if args.output_format != 'phylip-sequential-relaxed':
        AlignIO.convert(args.infile, args.input_format, args.outfile, args.output_format, args.molecule_type)
    else:
        get_phylip_sequential_relaxed(
            infile=args.infile, 
            input_format=args.input_format, 
            outfile=args.outfile)

if __name__ == '__main__':
    main()
