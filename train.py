#!/usr/bin/env python

import argparse
import time
import pandas as pd

from classifiers import load_model, save_model
from classifiers.features import features_train


def parse():
    parser = argparse.ArgumentParser(description='Generate prediction models from training data and output results to json.')
    parser.add_argument('-t', metavar='path_to_file', default='data/Train.csv', help='specify Train csv file')
    return parser.parse_args()

def main():
    args = parse()

    # Load training data
    train = pd.read_csv(args.t, usecols=['Id', 'Title', 'Tags'])

    # Train models and write to json
    keywords = load_model('keywords')
    keywords = features_train(train, keywords)
    save_model('keywords', keywords)

if __name__ == '__main__':
    start = time.time()
    main()
    print 'Program runtime: {0:.3f}s'.format(time.time() - start)
