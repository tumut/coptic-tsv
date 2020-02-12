#!/usr/bin/env python
'''Script to convert text files in the UnboundBible format into .tsv files for Bible CLIs'''

import argparse
import os
import math

from io import StringIO

import pandas as pd


def preprocess_content(filepath):
    content = ''
    with open(filepath) as f:
        for line in f.readlines():
            if line[0] == '#': continue
            content += line
    return StringIO(content)


def determine_filename(foldername):
    return foldername.split('_nt_')[-1][:3] + '.tsv'


def main():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        'input',
        help='folder where all the files can be found',
        type=str)
    parser.add_argument(
        'output_folder',
        help='name of the folder where the file will be saved',
        type=str)
    parser.add_argument(
        '-ai',
        '--abbreviation-index',
        help='path to the CSV file with book names and abbreviations [required]',
        required=True,
        type=str)
    parser.add_argument(
        '-o',
        '--output',
        help='filename of the output [default: automatically generated]',
        default=None,
        type=str)

    args = parser.parse_args()
    input_folder = args.input
    output_folder = args.output_folder
    abbrev_filepath = args.abbreviation_index

    foldername = os.path.basename(input_folder)
    print(f"Folder name: '{foldername}'")

    output_filename = args.output or determine_filename(foldername)
    print(f"Output filename: '{output_filename}'")

    index_filepath = os.path.join(input_folder, 'book_names.txt')
    content_filepath = os.path.join(input_folder, f'{foldername}_utf8.txt')
    output_filepath = os.path.join(output_folder, output_filename)

    print(f"Loading '{index_filepath}'")
    index = pd.read_csv(
        index_filepath,
        sep='\t',
        header=None,
        names=['book_index', 'book_name'])

    print(f"Loading '{content_filepath}'")
    content = pd.read_csv(
        preprocess_content(content_filepath),
        header=None,
        sep='\t',
        names=['book_index', 'chapter', 'verse', 'subverse', 'order_by', 'text'])
    content = content.drop(columns=['subverse'])

    print(f"Loading '{abbrev_filepath}'")
    abbrev = pd.read_csv(abbrev_filepath)

    print('Determining the numbering of books by order')
    numbered = content.groupby('book_index').size().reset_index().drop(axis=1, columns=0).rename_axis('book_number').reset_index()
    index = index.merge(numbered, how='left', on='book_index').dropna().astype({'book_number': int})
    index['book_number'] = index.book_number.apply(lambda x: x + 1)

    print('Joining book abbreviations onto the index')
    index = index.merge(abbrev, how='left', on='book_name')

    print('Joining book names and abbreviations onto the text')
    merged = content.merge(index, how='left', on='book_index')

    print(f"Saving '{output_filepath}'")
    merged.to_csv(output_filepath, sep='\t', header=False, index=False, columns=[
                  'book_name', 'book_abbrev', 'book_number', 'chapter', 'verse', 'text'])


if __name__ == '__main__':
    main()
