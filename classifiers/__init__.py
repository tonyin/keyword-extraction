#!/usr/bin/env python

from tags import tags_train
from naive_bayes import nb_classify
import json


def load_model(name):
    try:
        with open('classifiers/' + name + '.json', 'r') as f:
            model = json.load(f)
            print 'Updating existing {0} model...'.format(name)
    except:
        model = {}
        print 'Creating new {0} model...'.format(name)
    return model

def save_model(name, model):
    with open('classifiers/' + name + '.json', 'w') as f:
        json.dump(model, f)
