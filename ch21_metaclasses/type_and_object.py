'''
NOTE: these tests have to run under python3.
This is intended to be run as a doctest.
It demonstrates some oddities concerning `type` and `object`.

>>> s = type('foo')
>>> s
<class 'str'>
>>> type(s)
<class 'type'>
>>> type(type)
<class 'type'>

Now it gets weird...

>>> isinstance(type, object)
True
>>> issubclass(type, object)
True
>>> isinstance(object, type)
True
>>> issubclass(object, type)
False

>>> isinstance(s, type)
True
>>> issubclass(s, type)
False

`type` is both an instance of `object` and its subclass.
`object` is an instance of `type` but not a subclass of it.
`str` is also an instance of `type` but not a subclass of it.

>>> from collections import Iterable
>>> from abc import ABCMeta
>>> type(Iterable)
<class 'abc.ABCMeta'>
>>> isinstance(type(Iterable), type)
True
>>> issubclass(type(Iterable), type)
True

Every class is an instance of `type`, but only metaclasses are subclasses of it.
`collections.Iterable` is a metaclass.

>>> s.__mro__
(<class 'str'>, <class 'object'>)
>>> object.__mro__
(<class 'object'>,)
>>> type.__mro__
(<class 'type'>, <class 'object'>)
>>> Iterable.__mro__
(<class 'collections.abc.Iterable'>, <class 'object'>)
>>> Iterable.__class__.__mro__
(<class 'abc.ABCMeta'>, <class 'type'>, <class 'object'>)
'''

if __name__ == '__main__':
    import doctest
    import sys
    if sys.version_info.major != 3:
        raise Exception('These tests are written for Python 3.')
    doctest.testmod(verbose=True)