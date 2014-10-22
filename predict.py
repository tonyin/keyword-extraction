#!/usr/bin/env python

import argparse
import time
import string
import re
import pandas as pd

from classifiers import load_model
from classifiers.naive_bayes import nb_classify


def parse():
    parser = argparse.ArgumentParser(description='Generate predictions from models for test data and output results to csv.')
    parser.add_argument('-test', metavar='path_to_file', default='data/Test.csv', help='specify Test csv file')
    parser.add_argument('-p', metavar='path_to_file', default='data/Pred.csv', help='specify Pred csv file')
    return parser.parse_args()

def main():
    args = parse()

    # Load test data
    test = pd.read_csv(args.test, usecols=['Id', 'Title'])
    
    # Generate predictions and write to csv
    keywords = load_model('keywords')
    pred = nb_classify(test, keywords)
    pred.to_csv(args.p, columns=['Id', 'Tags'], index=False)

if __name__ == '__main__':
    start = time.time()
    main()
    print 'Program runtime: {0:.3f}s'.format(time.time() - start)
