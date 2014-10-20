#!/usr/bin/env python

import pandas as pd
import numpy as np
import string

PROB = 0.5 # Probability threshold for accepting a keyword as a tag, given it exists in the title


def nb_train(train):

    # Create dictionary of all possible tags
    kws = np.hstack(train['Tags'])
    kws = np.unique(kws)
    counts = {}
    for kw in kws:
        counts.setdefault(kw, {})
        counts[kw].setdefault('tag', 0)
        counts[kw].setdefault('title', 0)
        counts[kw].setdefault('both', 0)

    # Find frequency of tag kw appearances
    for title_kws, tag_kws in zip(train['Title'], train['Tags']):
        for kw in set(title_kws).difference(tag_kws):
            if kw in counts:
                counts[kw]['title'] += 1
        for kw in set(title_kws).intersection(tag_kws):
            counts[kw]['both'] += 1
        for kw in set(tag_kws).difference(title_kws):
            counts[kw]['tag'] += 1
    
    # Make list of keywords that pass the PROB threshold for keyword acceptance
    nb_tags = []
    for kw in counts:
        title_only = counts[kw]['title']
        both= counts[kw]['both']
        if both + title_only == 0: continue
        prob_tagged = 1.0 * both / (both + title_only)
        if prob_tagged > PROB:
            nb_tags.append(kw)

    return nb_tags


def naive_bayes(train, pred):
    
    nb_tags = nb_train(train)
    nb_filter = lambda x: list(set(x).intersection(nb_tags))
    str_join = lambda x: ' '.join(x)
    pred['Tags'] = pd.Series(pred['Title'].map(nb_filter).map(str_join))

    return pred
