#!/usr/bin/env python

import string
import re
import numpy as np
import nltk


def get_unused_puncs(kws):
    puncs = list(string.punctuation)
    for kw in kws:
        for c in kw:
            if c in puncs:
                puncs.remove(c)
    puncs = re.compile('[' + ''.join(puncs) + ']')
    return puncs

# Takes too long
# def tokenize(text):
#     text = nltk.word_tokenize(unicode(text, 'utf-8'))
#     text = nltk.pos_tag(text)
#     text = filter(lambda x: x[1] == 'NN', text)
#     text = [kw[0] for kw in text]
    
#     return text

def features_train(train, keywords):

    # Clean tags and titles
    train['Tags'] = train['Tags'].str.lower().str.split(' ')
    known_kws = np.hstack(train['Tags'].values)
    known_kws = np.unique(known_kws)
    unused_puncs = get_unused_puncs(known_kws)
    stopwords = nltk.corpus.stopwords.words('english')
    train['Title'] = train['Title'].str.lower().replace(unused_puncs, ' ').str.split(' ').map(lambda x: list(set(x).difference(stopwords)))

    # Extract features
    for title_kws, tag_kws in zip(train['Title'], train['Tags']):

        # 1. Feature: existence of whole kw
        for kw in set(title_kws).difference(tag_kws):
            keywords.setdefault(kw, {})
            keywords[kw].setdefault('title', 0)
            keywords[kw]['title'] += 1
        for kw in set(title_kws).intersection(tag_kws):
            keywords.setdefault(kw, {})
            keywords[kw].setdefault('both', 0)
            keywords[kw]['both'] += 1
        for kw in set(tag_kws).difference(title_kws):
            keywords.setdefault(kw, {})
            keywords[kw].setdefault('tag', 0)
            keywords[kw]['tag'] += 1
        
        # 2. Feature: existence of all parts of known kw
        for kw in tag_kws:
            if '-' in kw:
                kw_new = kw.replace('-', ' ')
                if len(set(kw_new)) == len(set(kw_new).intersection(title_kws)):
                    keywords[kw].setdefault('both', 0)
                    keywords[kw]['both'] += 1

    # Calculate scores (posterior prob, tf-idf)
    n = len(train.index)
    for kw in keywords.keys():
        keywords[kw].setdefault('title', 0)
        keywords[kw].setdefault('both', 0)
        keywords[kw].setdefault('tag', 0)
        total_tag = keywords[kw]['both'] + keywords[kw]['tag']
        total_title = keywords[kw]['both'] + keywords[kw]['title']
        if total_tag == 0:
            del keywords[kw]
        elif total_title == 0:
            del keywords[kw]
        else:
            # Posterior probability 'p' = both / (both + title)
            keywords[kw]['p'] = 1.0 * keywords[kw]['both'] / total_title
            # tf-idf 'ti' = (both + title) * ln( n / (both + title) )
            keywords[kw]['ti'] = 1.0 * total_title * np.log(n / total_title)
            if keywords[kw]['ti'] <= 1:
                del keywords[kw]

    return keywords
