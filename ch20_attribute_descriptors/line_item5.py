'''
Example 20-1 from Fluent Python

1) The Quantity instances are stored (once) in the LineItem class, 
    they are not attributes of LineItem instances.
2) `Quantity.__set__` sets the value in the LineItem instance `__dict__`.
    Then the access in `LineItem.subtotal` is normal attribute access, 
    since the data is in the `__dict__` now.
3) `Quantity.__set__` accesses `instance.__dict__` to avoid infinite recursion

    >>> nutmeg = LineItem('nutmeg', 8, 13.95)
    >>> nutmeg.weight
    8
    >>> nutmeg.weight = 6
    >>> nutmeg.weight
    6
    >>> nutmeg.price
    13.95
'''

class Quantity:

    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError('value must be > 0')

class LineItem:

    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price