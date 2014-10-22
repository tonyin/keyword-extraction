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

def decision_rule(title, model):

    # Get scores of each kw found in title
    kw_scores = {}
    for kw in list(set(title).intersection(model.keys())):
        kw_scores[kw] = model[kw]['p']

    # Sort found kws by score and probabilistically decide whether to tag
    kws_sorted = []
    kws_to_tag = []
    for kw in sorted(kw_scores, key=kw_scores.get, reverse=True):
        kws_sorted.append(kw)
        random_prob = lambda x: True if random.random() < x else False
        if random_prob(kw_scores[kw]):
            kws_to_tag.append(kw)
    
    # Heuristic: Add highest scoring kw if nothing was tagged, since tags >= 1
    if len(kws_to_tag) == 0 and len(kws_sorted) != 0:
        kws_to_tag.append(kws_sorted[0])

    return kws_to_tag

def nb_classify(test, keywords):

    # Clean titles
    unused_puncs = get_unused_puncs(keywords.keys())
    unused_puncs = re.compile('[' + ''.join(unused_puncs) + ']')
    test['Title'] = test['Title'].str.lower().replace(unused_puncs, '', regex=True).str.split(' ')
    
    # Calculate score: posterior probability (probability of kw in tags, given it is in title)
    for kw in keywords:
        if keywords[kw]['both'] + keywords[kw]['title'] == 0:
            keywords[kw]['p'] = 0.0
        else:
            keywords[kw]['p'] = 1.0 * keywords[kw]['both'] / (keywords[kw]['both'] + keywords[kw]['title'])

    # Generate predicted tags based on probabilities
    pred = test[['Id']]
    pred['Tags'] = pd.Series(test['Title'].head(10000).map(lambda x: decision_rule(x, kw_model)).map(lambda x: ' '.join(x)))

    return pred
