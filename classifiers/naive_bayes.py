#!/usr/bin/env python

import pandas as pd
import numpy as np
import string
import re

PRECISION = 0.2 # precision threshold for accepting a keyword to tag


def get_unused_puncs(tags):
    puncs = list(string.punctuation)
    for s in tags:
        for kw in s:
            for c in kw:
                if c in puncs:
                    puncs.remove(c)
    return puncs

def nb_classify(test, keywords):

    # Clean titles
    unused_puncs = get_unused_puncs(keywords.keys())
    test['Title'].str.lower().replace(unused_puncs, '', regex=True).str.split(' ')
    
    # Get accepted kws
    nb_keywords = []
    for kw in keywords:
        true_pos = keywords[kw]['both']
        pred_pos = keywords[kw]['both'] + keywords[kw]['title']
        actu_pos = keywords[kw]['both'] + keywords[kw]['tag']
        if pred_pos == 0: continue
        if 1.0 * true_pos / pred_pos >= PRECISION:
            nb_keywords.append(kw)

    # Apply filters
    nb_filter = lambda x: list(set(x).intersection(nb_keywords))
    str_join = lambda x: ' '.join(x)
    pred = test['Id']
    pred['Tags'] = pd.Series(test['Title'].map(nb_filter).map(str_join))

    return pred
