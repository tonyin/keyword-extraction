#!/usr/bin/env python

import string
import re
import random
import pandas as pd
import numpy as np


def get_unused_puncs(keywords):
    puncs = list(string.punctuation)
    for kw in keywords:
        for c in kw:
            if c in puncs:
                puncs.remove(c)
    return puncs

def nb_classify(test, keywords):

    # Clean titles
    unused_puncs = get_unused_puncs(keywords.keys())
    unused_puncs = re.compile('[' + ''.join(unused_puncs) + ']')
    test['Title'] = test['Title'].str.lower().replace(unused_puncs, '', regex=True).str.split(' ')
    
    # Calculate posterior probability (probability of kw in tags, given it is in title)
    for kw in keywords:
        if keywords[kw]['both'] + keywords[kw]['title'] == 0:
            keywords[kw]['p'] = 0.0
        else:
            keywords[kw]['p'] = 1.0 * keywords[kw]['both'] / (keywords[kw]['both'] + keywords[kw]['title'])

    # Generate predicted tags based on probabilities
    kws_in_title = lambda x: list(set(x).intersection(keywords.keys()))
    random_prob = lambda x: True if random.random() < x else False
    posterior_p = lambda x: filter(lambda y: random_prob(keywords[y]['p']), x)
    str_join = lambda x: ' '.join(x)

    pred = test[['Id']]
    pred['Tags'] = pd.Series(test['Title'].map(kws_in_title).map(posterior_p).map(str_join))

    return pred
