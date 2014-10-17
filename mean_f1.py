#!/usr/bin/env python

import argparse
import time
import pandas
import zipfile

def parse():
    parser = argparse.ArgumentParser(description='Evaluate predictions of train data using Mean F1-Score metric.')
    parser.add_argument('-t', metavar='filename', default='data/Train.zip', help='specify Train zip file')
    parser.add_argument('pred', metavar='filename', help='specify predictions csv file')
    return parser.parse_args()

def precision(a, b):
    true_positives = len(set(a).intersection(b))
    predicted_positives = len(b)
    if predicted_positives == 0:
        return 0
    return 1.0 * true_positives / predicted_positives

def recall(a, b):
    true_positives = len(set(a).intersection(b))
    actual_positives = len(a)
    if actual_positives == 0:
        return 0
    return 1.0 * true_positives / actual_positives

def f1(a, b):
    p = precision(a, b)
    r = recall(a, b)
    if p == 0 or r == 0:
        return 0
    return 2.0 * (p * r) / (p + r)

def main():
    args = parse()

    if zipfile.is_zipfile('data/Train.zip'):
        with zipfile.ZipFile('data/Train.zip', 'r') as zf:
            train = pandas.read_csv(zf.open('Train.csv'), usecols=['Id', 'Tags'], index_col='Id')
    pred = pandas.read_csv(args.pred)

    results = pandas.merge(train, pred, how='left', on='Id', suffixes=['', '2'])
    results['Tags2'] = results['Tags2'].fillna('')
    results['F1'] = [f1(a.split(' '), b.split(' ')) for a, b in results[['Tags', 'Tags2']].values]
    mean_f1 = sum(results['F1']) / results['F1'].count()

    print 'Mean F1 Score: {0:.5f}'.format(mean_f1)

if __name__ == '__main__':
    start = time.time()
    main()
    print time.time() - start
