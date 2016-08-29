'''
Example 20-8 from Fluent Python
This example illustrates some trickiness surrounding descriptor 
classes shadowing (or not) instance attributes.

Overriding descriptor class:

    >>> o = Managed()
    >>> o.over
    ->Overriding.__get__(<Overriding object>, <Managed object>, <class Managed>)
    >>> Managed.over
    ->Overriding.__get__(<Overriding object>, None, <class Managed>)
    >>> o.over = 7
    ->Overriding.__set__(<Overriding object>, <Managed object>, 7)
    >>> o.over
    ->Overriding.__get__(<Overriding object>, <Managed object>, <class Managed>)
    >>> o.__dict__['over'] = 8
    >>> vars(o)
    {'over': 8}
    >>> o.over
    ->Overriding.__get__(<Overriding object>, <Managed object>, <class Managed>)

Overriding, but w/o `__get__`:

    >>> type(o.noget)
    <class 'descriptors.NoGet'>
    >>> type(Managed.noget)
    <class 'descriptors.NoGet'>
    >>> o.noget = 7
    ->NoGet.__set__(<NoGet object>, <Managed object>, 7)
    >>> o.__dict__['noget'] = 8
    >>> o.noget
    8
    >>> o.noget = 7
    ->NoGet.__set__(<NoGet object>, <Managed object>, 7)
    >>> o.noget
    8

Non-overriding Descriptor Class:

    >>> o = Managed()
    >>> o.non
    ->Nonoverriding.__get__(<Nonoverriding object>, <Managed object>, <class Managed>)
    >>> o.non = 7
    >>> o.non
    7
    >>> Managed.non
    ->Nonoverriding.__get__(<Nonoverriding object>, None, <class Managed>)
    >>> vars(o)
    {'non': 7}
    >>> del o.non
    >>> o.non
    ->Nonoverriding.__get__(<Nonoverriding object>, <Managed object>, <class Managed>)
'''

# Helper classes
def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]

def display(obj):
    cls = type(obj)
    if cls is type:
        return '<class {}>'.format(obj.__name__)
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return '<{} object>'.format(cls_name(obj))

def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print('->{}.__{}__({})'.format(cls_name(args[0]), name, pseudo_args))

# Demo classes

class Overriding:
    '''overriding descriptor class'''

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class NoGet:
    '''TODO: explain this'''

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class Nonoverriding:
    '''TODO: explain this'''
    
    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)


class Managed:
    over = Overriding()
    noget = NoGet()
    non = Nonoverriding()

    def spam(self):
        print('-> Managed.spam({})'.format(display(self)))

