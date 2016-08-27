'''
Example A-13, schedule2.py from chapter 19 of Fluent Python

Doctest:

# Set-up

    >>> import shelve
    >>> db = shelve.open(DB)
    >>> if KNOWN_KEY not in db: load_db(db)

# Demo

    >>> DBRecord.set_db(db)
    >>> event = DBRecord.fetch('event.33950')
    >>> event
    <Event 'There *Will* Be Bugs'>
    >>> event.venue
    <DBRecord serial='venue.1449'>
    >>> event.venue.name
    'Portland 251'

# Tear-down

    >>> db.close()
'''

import warnings
import inspect
import osconload
import pdb

DB = 'data/schedule2'
KNOWN_KEY = 'conference.115'

class Record:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __eq__(self, other):
        if isinstance(other, Record):
            return self.__dict__ == other.__dict__
        else:
            return NotImplemented

class MissingDatabaseError(RuntimeError):
    '''Raised when database is not set'''

class DBRecord(Record):
    
    __db = None

    @staticmethod
    def set_db(db):
        DBRecord.__db = db

    @staticmethod
    def get_db():
        return DBRecord.__db

    @classmethod
    def fetch(cls, id):
        db = cls.get_db()
        try:
            return db[id]
        except TypeError:
            if db is None:
                msg = 'DB does not exist, call {}.set_db(db)'
                raise MissingDatabaseError(msg.format(cls.__name__))
            else:
                raise

    def __repr__(self):
        if hasattr(self, 'serial'):
            cls_name = self.__class__.__name__
            return '<{} serial={!r}>'.format(cls_name, self.serial)
        else:
            return super().__repr__()

class Event(DBRecord):

    @property
    def venue(self):
        key = 'venue.{}'.format(self.venue_serial)
        return self.__class__.fetch(key)

    @property
    def speakers(self):
        if not hasattr(self, '_speaker_objs'):
            spkr_serials = self.__dict__['speakers']
            fetch = self.__class__.fetch
            self._speaker_objs = [fetch('speaker.{}'.format(key)) 
                                    for key in spkr_serials]
        return self._speaker_objs

    def __repr__(self):
        if hasattr(self, 'name'):
            cls_name = self.__class__.__name__
            return '<{} {!r}>'.format(cls_name, self.name)
        else:
            return super().__repr__()

def load_db(db):
    raw_data = osconload.load()
    warnings.warn('loading' + DB)
    for collection, record_list in raw_data['Schedule'].items():
        record_type = collection[:-1]
        cls_name = record_type.capitalize()
        cls = globals().get(cls_name, DBRecord)
        #pdb.set_trace()
        if inspect.isclass(cls) and issubclass(cls, DBRecord):
            factory = cls
        else:
            factory = DBRecord
        for record in record_list:
            key = '{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = factory(**record)


