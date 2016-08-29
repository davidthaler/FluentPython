'''
Example 21-1 from Fluent Python

This class pretty much reimplements collections.namedtuple.

    >>> Dog = record_factory('Dog', 'name weight breed')
    >>> luigi = Dog('Luigi', 10, 'St Charles')
    >>> luigi
    Dog(name='Luigi', weight=10, breed='St Charles')
    >>> name, wt, breed = luigi
    >>> wt
    10
    >>> breed
    'St Charles'
'''

def record_factory(cls_name, field_names):
    try:
        # Duck typing: assume its a string
        field_names = field_names.replace(',', ' ').split()
    except AttributeError:
        # Or else a sequence
        pass
    # Or else this will raise some exception
    field_names = tuple(field_names)

    def __init__(self, *args, **kwargs):
        # get the positional args in order
        attrs = dict(zip(self.__slots__, args))
        # add the keyword args
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, value)

    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self):
        # NB: self is iterable
        values = ', '.join('{}={!r}'.format(*i) for i in zip(self.__slots__, self))
        return '{}({})'.format(self.__class__.__name__, values)

    # These will be the attributes of our new class
    cls_attrs = dict(__slots__ = field_names,
                     __init__  = __init__,
                     __iter__  = __iter__,
                     __repr__  = __repr__)

    # see help(type)
    # This is a constructor for a class
    # with name of name, superclass of object( only), 
    # and attributes of cls_attrs
    return type(cls_name, (object,), cls_attrs)           