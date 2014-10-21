#!/usr/bin/env python

import argparse
import time
import pandas as pd
import zipfile as zf


def parse():
    parser = argparse.ArgumentParser(description='Evaluate predictions of train data using Mean F1-Score metric.')
    parser.add_argument('-t', metavar='filename', default='data/Train.zip', help='specify Train zip file')
    parser.add_argument('-p', metavar='filename', default='data/Pred.csv', help='specify Pred csv file')
    return parser.parse_args()

def precision(a, b):
    true_positives = len(set(a).intersection(b))
    predicted_positives = len(b)
    if predicted_positives == 0:
        return 0.0
    return 1.0 * true_positives / predicted_positives

def recall(a, b):
    true_positives = len(set(a).intersection(b))
    actual_positives = len(a)
    if actual_positives == 0:
        return 0.0
    return 1.0 * true_positives / actual_positives

def f1(a, b):
    p = precision(a, b)
    r = recall(a, b)
    if p == 0 and r == 0:
        return 0.0
    return 2.0 * (p * r) / (p + r)

def main():
    args = parse()

    # Load training and prediction files
    if zf.is_zipfile(args.t):
        with zf.ZipFile(args.t, 'r') as f:
            name = args.t.split('/')[1].split('.')[0]
            train = pd.read_csv(f.open(name + '.csv'), usecols=['Id', 'Tags'])
    pred = pd.read_csv(args.p, usecols=['Id', 'Tags'])

    # Calculate F1 scores
    results = pd.merge(train, pred, how='left', on='Id', suffixes=['', '2'])
    results['Tags2'] = results['Tags2'].fillna('')
    results['F1'] = [f1(a.split(' '), b.split(' ')) for a, b in results[['Tags', 'Tags2']].values]
    mean_f1 = sum(results['F1']) / results['F1'].count()

    print 'Mean F1 Score: {0:.5f}'.format(mean_f1)

if __name__ == '__main__':
    start = time.time()
    main()
    print 'Program runtime: {0:.3f}s'.format(time.time() - start)
