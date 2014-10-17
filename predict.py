#!/usr/bin/env python

import argparse
import time
import pandas
import zipfile

from classifiers import naive_bayes

def parse():
    parser = argparse.ArgumentParser(description='Generate predictions from train data and output results to csv.')
    parser.add_argument('-t', metavar='filename', default='data/Train.zip', help='specify Train zip file (data/[filename])')
    parser.add_argument('-p', metavar='filename', default='data/Pred.csv', help='specify Pred csv file (data/[filename]')
    return parser.parse_args()

def main():
    args = parse()

    if zipfile.is_zipfile(args.t):
        with zipfile.ZipFile(args.t, 'r') as zf:
            f = args.t.split('/')[1].split('.')[0]
            train = pandas.read_csv(zf.open(f + '.csv'), usecols=['Id', 'Title', 'Tags'])
    
    pred = naive_bayes(train)
    pred.to_csv(args.p)

if __name__ == '__main__':
    start = time.time()
    main()
    print 'Program runtime: {0:.3f}s'.format(time.time() - start)
