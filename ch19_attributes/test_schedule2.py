'''
Example A-14, pytest code for example A-13, schedule2.py, 
from chapter 19 of Fluent Python.

Note the exception handling syntax in `test_missing_db_exception()`.
'''

import pytest
import shelve

import schedule2 as sched

@pytest.yield_fixture
def db():
    with shelve.open(sched.DB) as mydb:
        sched.load_db(mydb)
        yield mydb

def test_record():
    rec = sched.Record(spam=99, eggs=12)
    assert rec.spam == 99
    assert rec.eggs == 12

def test_record_repr():
    rec = sched.DBRecord(spam=99, eggs=12)
    assert 'DBRecord object at 0x' in repr(rec)
    rec2 = sched.DBRecord(serial=13)
    assert repr(rec2) == '<DBRecord serial=13>'

def test_known_key(db):
    assert sched.KNOWN_KEY in db

def test_speaker(db):
    speaker = db['speaker.3471']
    assert speaker.name ==  'Anna Martelli Ravenscroft'

def test_missing_db_exception():
    with pytest.raises(sched.MissingDatabaseError):
        sched.DBRecord.fetch('venue.1585')

def test_dbrecord(db):
    sched.DBRecord.set_db(db)
    venue = sched.DBRecord.fetch('venue.1585')
    assert venue.name == 'Exhibit Hall B'

def test_event_record(db):
    event = db['event.33950']
    assert repr(event) == "<Event 'There *Will* Be Bugs'>"

def test_event_venue(db):
    sched.Event.set_db(db)
    event = db['event.33950']
    assert event.venue_serial == 1449
    assert event.venue == db['venue.1449']
    assert event.venue.name == 'Portland 251'

def test_event_speakers(db):
    sched.Event.set_db(db)
    event = db['event.33950']
    assert len(event.speakers) == 2
    aa = [db['speaker.3471'], db['speaker.5199']]
    assert event.speakers == aa
