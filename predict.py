#!/usr/bin/env python

import argparse
import time

def parse():
    parser = argparse.ArgumentParser(description='Generate predictions from train data and output results to csv.')
    parser.add_argument('-t', metavar='filename', default='data/Train.zip', help='specify Train zip file')
    parser.add_argument('-p', metavar='filename', default='data/Pred.csv', help='specify predictions csv file')
    return parser.parse_args()

def main():
    args = parse()

    if zipfile.is_zipfile(args.t):
        with zipfile.ZipFile(args.t, 'r') as zf:
            f = args.t.split('/')[1].split('.')[0]
            train = pandas.read_csv(zf.open(f + '.csv'), usecols=['Id', 'Tags'], index_col='Id')

    # do stuff
    

if __name__ == '__main__':
    start = time.time()
    main()
    print 'Program runtime: {0:.3f}s'.format(time.time() - start)
