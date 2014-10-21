#!/usr/bin/env python

import argparse
import time
import pandas as pd
import zipfile as zf

from classifiers import load_model, save_model, tags_train


def parse():
    parser = argparse.ArgumentParser(description='Generate prediction models from training data and output results to json.')
    parser.add_argument('-t', metavar='path_to_file', default='data/Train.zip', help='specify Train zip file (data/[filename])')
    return parser.parse_args()

def main():
    args = parse()

    # Load training data
    name = args.t.split('/')[1].split('.')[0]
    if zf.is_zipfile(args.t):
        with zf.ZipFile(args.t, 'r') as zipf:
            with zipf.open(name + '.csv') as f:
                train = pd.read_csv(f, usecols=['Id', 'Title', 'Tags'])

    # Train models and write to json
    kw_model = load_model('keywords')
    kw_model = tags_train(train, kw_model)
    save_model('keywords', kw_model)

if __name__ == '__main__':
    start = time.time()
    main()
    print 'Program runtime: {0:.3f}s'.format(time.time() - start)
