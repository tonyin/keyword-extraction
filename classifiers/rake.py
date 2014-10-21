#!/usr/bin/env python

import time
from RAKE.rake import Rake

STOPLIST = 'RAKE/SmartStoplist.txt' # Stoplist to use


def main():
    """Add keyword to predicted tags if ... ."""

    rake_train = Rake(STOPLIST)
    kws = rake_train.run('This is a test.')
    print kws

    #return pred

if __name__ == '__main__':
    start = time.time()
    main()
    print 'Program runtime: {0:.3f}s'.format(time.time() - start)
