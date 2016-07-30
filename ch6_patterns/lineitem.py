# Part of examples 6_1 and 6_2 from FluentPython, refactored.

class LineItem(object):

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity
