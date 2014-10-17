#!/usr/bin/env python

import pandas
import zipfile

def naive_bayes(train):
    pred = pandas.DataFrame(data=train['Id'])
    pred['Tags'] = ''

    return pred
