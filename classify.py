#!/usr/bin/env python

import argparse
import time
import pandas as pd
import zipfile as zf
import string

from classifiers import naive_bayes

def parse():
    parser = argparse.ArgumentParser(description='Generate predictions from train data and output results to csv.')
    parser.add_argument('-t', metavar='path_to_file', default='data/Train.zip', help='specify Train zip file (data/[filename])')
    parser.add_argument('-p', metavar='path_to_file', default='data/Pred.csv', help='specify Pred csv file (data/[filename])')
    return parser.parse_args()

def main():
    args = parse()

    # Load training data
    if zf.is_zipfile(args.t):
        with zf.ZipFile(args.t, 'r') as f:
            name = args.t.split('/')[1].split('.')[0]
            train = pd.read_csv(f.open(name + '.csv'), usecols=['Id', 'Title', 'Tags'])

    # Clean tags
    train['Tags'] = train['Tags'].str.lower().str.split(' ')

    # Get list of unused punctuation and clean titles
    puncs = list(string.punctuation)
    for s in train['Tags'].values:
        for kw in s:
            for c in kw:
                if c in puncs:
                    puncs.remove(c)
    puncs = ''.join(puncs)
    train['Title'] = train['Title'].str.lower().str.replace('[' + puncs + ']', '').str.split(' ')
    
    # Apply classifier(s)
    pred = train[['Id', 'Title']]
    pred = naive_bayes(train, pred)
    
    pred.to_csv(args.p, columns=['Id', 'Tags'], index=False)

if __name__ == '__main__':
    start = time.time()
    main()
    print 'Program runtime: {0:.3f}s'.format(time.time() - start)
