#!/usr/bin/env python

import json


def load_model(name):
    try:
        with open('classifiers/' + name + '.json', 'r') as f:
            model = json.load(f)
            print 'Using existing {0} model...'.format(name)
    except:
        model = {}
        print 'Using new {0} model...'.format(name)
    return model

def save_model(name, model):
    with open('classifiers/' + name + '.json', 'w') as f:
        json.dump(model, f)
