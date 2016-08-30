'''
Copied from example 20-6 from Fluent Python/ ch20_... line_item6.
It is restructured to move the descriptor class into model,
and the class decorator is added there.

These tests are called in a '__main__' block, 
so they will run with `python line_item.py`.

    >>> nutmeg = LineItem('Moluccan nutmeg', 2, 4.5)
    >>> nutmeg.weight
    2
    >>> nutmeg.price
    4.5
    >>> nutmeg.subtotal()
    9.0
    >>> nutmeg.description
    'Moluccan nutmeg'
    >>> LineItem.description.storage_name
    '_NonBlank#description'
    >>> LineItem.weight.storage_name
    '_Quantity#weight'
    >>> LineItem.price.storage_name
    '_Quantity#price'
    >>> getattr(nutmeg, '_NonBlank#description')
    'Moluccan nutmeg'
    >>> type(nutmeg).description.storage_name
    '_NonBlank#description'
'''
import model

@model.entity
class LineItem:
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
