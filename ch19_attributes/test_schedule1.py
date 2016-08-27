'''
Example A-12, the test (pytest) code for example 19-9

To run:

    >>> python -m pytest

...in this directory

'''
import pytest
import shelve

import schedule1 as sched

@pytest.yield_fixture
def db():
    with shelve.open(sched.DB) as mydb:
        if sched.KNOWN_KEY not in mydb:
            sched.load_db(mydb)
        yield mydb

def test_record_class():
    rec = sched.Record(spam=99, eggs=12)
    assert rec.spam == 99
    assert rec.eggs == 12

def test_known_key(db):
    assert sched.KNOWN_KEY in db

def test_speaker_record(db):
    speaker = db['speaker.3471']
    assert speaker.name == 'Anna Martelli Ravenscroft'

def test_event_record(db):
    event = db['event.33950']
    assert event.name == 'There *Will* Be Bugs'

def test_event_venue(db):
    event = db['event.33950']
    assert event.venue_serial == 1449
