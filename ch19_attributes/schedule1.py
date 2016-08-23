# Example 19-9 from Fluent Python

import warnings
import osconload

# NB: Python will append a '.db' to the shelf file name 
DB = 'data/schedule1'
KNOWN_KEY = 'speaker.149868'

class Record:
    def __init__(self, **kwargs):
        # This adds everything in **kwargs
        self.__dict__.update(kwargs)

# NB: this does not open the shelf file
def load_db(db):
    raw_data = osconload.load()
    warnings.warn('loading ' + DB)
    for collection, record_list in raw_data['Schedule'].items():
        record_type = collection[:-1]
        for record in record_list:
            key = '{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = Record(**record)
