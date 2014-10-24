#!/usr/bin/env python

import string
import re
import random
import pandas as pd
import numpy as np
import nltk

from features import get_unused_puncs


def decision_rule(title_kws, keywords, stopwords):

    # Get scores of each whole kw in title
    nb_scores = {}
    ti_scores = {}
    for kw in set(title_kws).intersection(keywords.keys()):
        nb_scores[kw] = keywords[kw]['p']
        ti_scores[kw] = keywords[kw]['ti']

    # Get scores for each known kw with all parts in title
    for kw in filter(lambda x: '-' in x, keywords.keys()):
        kw_new = set(kw.replace('-', ' ')).difference(stopwords)
        if kw_new.issubset(title_kws):
            nb_scores[kw] = keywords[kw]['p']
            ti_scores[kw] = keywords[kw]['ti']

    # 1. Add tag if posterior prob of tag >= not tag
    kws_to_tag = []
    for kw in sorted(nb_scores, key=nb_scores.get, reverse=True):
        if nb_scores[kw] >= 0.5:
            kws_to_tag.append(kw)
    
    # 2. Add highest scoring tf-idf kw if not already added
    for kw in sorted(ti_scores, key=ti_scores.get, reverse=True):
        if kw not in kws_to_tag:
            kws_to_tag.append(kw)
            break

    # 3. Add c# if no tags
    if len(kws_to_tag) == 0:
        kws_to_tag.append('c#')

    return kws_to_tag

def nb_classify(test, keywords):

    # Clean and tokenize titles
    unused_puncs = get_unused_puncs(keywords.keys())
    stopwords = nltk.corpus.stopwords.words('english')
    test['Title'] = test['Title'].str.lower().replace(unused_puncs, ' ').str.split(' ').map(lambda x: list(set(x).difference(stopwords)))
    
    # Generate predicted tags based on decision rule
    pred = test[['Id']]
    pred['Tags'] = pd.Series(test['Title'].map(lambda x: decision_rule(x, keywords, stopwords)).map(lambda x: ' '.join(x)))

    return pred
