#!/usr/bin/env python

import argparse
import time
import pandas as pd


def parse():
    parser = argparse.ArgumentParser(description='Evaluate predictions of test data using Mean F1-Score metric.')
    parser.add_argument('-test', metavar='filename', default='data/Test.csv', help='specify Test csv file')
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

    # Load test and prediction files
    test = pd.read_csv(args.test, usecols=['Id', 'Tags'])
    pred = pd.read_csv(args.p, usecols=['Id', 'Tags'])

    # Calculate F1 scores
    results = pd.merge(test, pred, how='left', on='Id', suffixes=['', '2'])
    results['Tags2'] = results['Tags2'].fillna('')
    results['p'] = [precision(a.split(' '), b.split(' ')) for a, b in results[['Tags', 'Tags2']].values]
    results['r'] = [recall(a.split(' '), b.split(' ')) for a, b in results[['Tags', 'Tags2']].values]
    results['F1'] = [f1(a.split(' '), b.split(' ')) for a, b in results[['Tags', 'Tags2']].values]

    print 'Mean Precision: {0:.5f}'.format(sum(results['p']) / results['p'].count())
    print 'Mean Recall: {0:.5f}'.format(sum(results['r']) / results['r'].count())
    print 'Mean F1 Score: {0:.5f}'.format(sum(results['F1']) / results['F1'].count())

if __name__ == '__main__':
    start = time.time()
    main()
    print 'Program runtime: {0:.3f}s'.format(time.time() - start)
