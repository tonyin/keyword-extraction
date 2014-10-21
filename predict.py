#!/usr/bin/env python

import argparse
import time
import pandas as pd
import zipfile as zf
import string
import re

from classifiers import nb_classify


def parse():
    parser = argparse.ArgumentParser(description='Generate predictions from models for test data and output results to csv.')
    parser.add_argument('-t', metavar='path_to_file', default='data/Train.zip', help='specify Test zip file (data/[filename])')
    parser.add_argument('-p', metavar='path_to_file', default='data/Pred.csv', help='specify Pred csv file (data/[filename])')
    return parser.parse_args()

def main():
    args = parse()

    # Load test data
    name = args.t.split('/')[1].split('.')[0]
    if zf.is_zipfile(args.t):
        with zf.ZipFile(args.t, 'r') as zipf:
            with zipf.open(name + '.csv') as f:
                test = pd.read_csv(f, usecols=['Id', 'Title'])
    
    # Generate predictions and write to csv
    keywords = load_model('keywords')
    pred = nb_classify(test, keywords)
    pred.to_csv(args.p, columns=['Id', 'Tags'], index=False)

if __name__ == '__main__':
    start = time.time()
    main()
    print 'Program runtime: {0:.3f}s'.format(time.time() - start)
