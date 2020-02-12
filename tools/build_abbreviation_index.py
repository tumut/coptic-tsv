#!/usr/bin/env python
'''Script to make a .csv index of book names and abbreviations from an existing .tsv'''

import argparse
import pandas as pd


def group_index(filepath):
    bible = pd.read_csv(filepath, sep='\t', header=None)
    bible.columns = ['book_name', 'book_abbrev', 'book_order', 'chapter', 'verse', 'text']
    grouped = bible.groupby(['book_name', 'book_abbrev']).size().reset_index()
    grouped = grouped.drop(axis=1, columns=0)
    return grouped


def main():
    parser = argparse.ArgumentParser(
        description=__doc__)

    parser.add_argument(
        'input',
        help='filepath to the tsv')
    parser.add_argument(
        '-o',
        '--output',
        help='filepath to the output csv [default: {input}.index.csv]',
        default=None)

    args = parser.parse_args()
    tsv_filepath = args.input
    csv_filepath = args.output or f'{tsv_filepath}.index.csv'

    index = group_index(tsv_filepath)
    index.to_csv(csv_filepath, index=False)
    print(f"Saved index in '{csv_filepath}'")


if __name__ == '__main__':
    main()
