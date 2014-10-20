#!/usr/bin/env python

import pandas as pd
import numpy as np
import string
from common import get_kw_freqs

PROB = 0.0 # Probability threshold for accepting a keyword as a tag, given it exists in the title


def nb_train(train):

    # Get keyword frequencies
    kw_freqs = get_kw_freqs(train)

    # Make list of keywords that pass the PROB threshold for keyword acceptance
    nb_keywords = []
    for kw in kw_freqs:
        title_only = kw_freqs[kw]['title']
        both = kw_freqs[kw]['both']
        if both + title_only == 0: continue
        prob_tagged = 1.0 * both / (both + title_only)
        if prob_tagged > PROB:
            nb_keywords.append(kw)

    return nb_keywords


def naive_bayes(train, pred):
    """Add keyword to predicted tags if the keyword passes a conditional probability threshold (PROB)."""

    nb_keywords = nb_train(train)
    nb_filter = lambda x: list(set(x).intersection(nb_keywords))
    str_join = lambda x: ' '.join(x)
    pred['Tags'] = pd.Series(pred['Title'].map(nb_filter).map(str_join))

    return pred
