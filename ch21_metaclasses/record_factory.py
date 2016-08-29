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
    >>> luigi.__slots__
    ('name', 'weight', 'breed')
    >>> luigi.weight
    10
    >>> Dog.weight
    <member 'weight' of 'Dog' objects>
    >>> luigi.__class__
    <class 'record_factory.Dog'>
    >>> Dog.__class__
    <class 'type'>
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
    # type (that is class) is a type and this is its constructor
    # It is a constructor for a class
    # with name of cls_name, superclass of object(only), 
    # and attributes of cls_attrs
    return type(cls_name, (object,), cls_attrs)

'''
* This is the key *
These are equivalent:

class MyClass(MySuper, MyMixin):
    x = 42

    def x2(self):
        return self.x * 2

MyClass = type('MyClass', (MySuper, MyMixin), 
                {'x': 42, 'x2': lambda self: self.x * 2})
'''
