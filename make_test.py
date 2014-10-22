#!/usr/bin/env python

import argparse
import time
import pandas as pd
import numpy as np
import zipfile as zf


def parse():
    parser = argparse.ArgumentParser(description='Generate test csv from training data and output results to csv.')
    parser.add_argument('-t', metavar='path_to_file', default='data/Train.zip', help='specify Train zip file (data/filename])')
    parser.add_argument('-test', metavar='path_to_file', default='data/Test.csv', help='specify Test csv file (data/[filename])')
    return parser.parse_args()

def main():
    args = parse()

    # Load training data
    name = args.t.split('/')[1].split('.')[0]
    if zf.is_zipfile(args.t):
        with zf.ZipFile(args.t, 'r') as zipf:
            with zipf.open(name + '.csv') as f:
                train = pd.read_csv(f, usecols=['Id', 'Title', 'Tags'])

    test = train.loc[np.random.choice(train.index, 1000000, replace=False)]
    test.to_csv(args.test, columns=['Id', 'Title', 'Tags'], index=False)
    
if __name__ == '__main__':
    start = time.time()
    main()
    print 'Program runtime: {0:.3f}s'.format(time.time() - start)
