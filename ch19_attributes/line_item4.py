'''
Example 19-23 and 19-24 of Fluent Python.

# TODO: find out how to check an exception in a doctest.

This one is tricky...
1) `get/set_qty` are closures: `storage_name` is set in their defining scope
2) `instance` is the `self` argument from a normal property definition
    It refers to the instance that has this `quantity` as a property
3) `instance.__dict__` access avoids the inifinite recursion 
    that would occur if we called the property

    >>> nutmeg = LineItem('nutmeg', 8, 13.95)
    >>> nutmeg.weight
    8
    >>> nutmeg.weight = 6
    >>> nutmeg.weight
    6
    >>> nutmeg.price
    13.95
'''

def quantity(storage_name):
    '''A property factory.'''
    def get_qty(instance):
        return instance.__dict__[storage_name]

    def set_qty(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise ValueError('value must be > 0')

    return property(get_qty, set_qty)

class LineItem:

    weight = quantity('weight')
    price = quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight                        # set through property
        self.price = price                          # ditto

    def subtotal(self):
        return self.weight * self.price             # get through property
