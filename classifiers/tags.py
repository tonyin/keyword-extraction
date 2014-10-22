#!/usr/bin/env python

import string
import re
import numpy as np


def get_unused_puncs(keywords):
    puncs = list(string.punctuation)
    for kw in keywords:
        for c in kw:
            if c in puncs:
                puncs.remove(c)
    return puncs

def tags_train(train, kw_model):

    # Clean tags and titles
    train['Tags'] = train['Tags'].str.lower().str.split(' ')
    unused_puncs = get_unused_puncs(train['Tags'].values)
    unused_puncs = re.compile('[' + ''.join(unused_puncs) + ']')
    train['Title'] = train['Title'].str.lower().replace(unused_puncs, '', regex=True).str.split(' ')
    
    # Get available keywords
    tags = np.hstack(train['Tags'].values)
    tags = np.unique(tags)
    for kw in tags:
        kw_model.setdefault(kw, {})
        kw_model[kw].setdefault('tag', 0)
        kw_model[kw].setdefault('title', 0)
        kw_model[kw].setdefault('both', 0)

    # Find appearances of keywords
    for title_kws, tag_kws in zip(train['Title'], train['Tags']):
        for kw in set(title_kws).difference(tag_kws):
            if kw in kw_model:
                kw_model[kw]['title'] += 1
        for kw in set(title_kws).intersection(tag_kws):
            kw_model[kw]['both'] += 1
        for kw in set(tag_kws).difference(title_kws):
            kw_model[kw]['tag'] += 1

    return kw_model
