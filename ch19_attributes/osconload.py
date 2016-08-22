# Example 19-2 from Fluent Python

'''
NB: to run these tests use python -m doctest -v osconload.py

>>> feed = load()
>>> sorted(feed['Schedule'].keys())
['conferences', 'events', 'speakers', 'venues']
>>> feed['Schedule']['speakers'][-1]['name']
'Carina C. Zona'
>>> feed['Schedule']['events'][1]['name']
'Refactoring 101'
'''

import warnings
import os
import json

from urllib.request import urlopen

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'

def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())

    with open(JSON) as fp:
        return json.load(fp)

