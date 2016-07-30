# Part of examples 6_1 and 6_2 from FluentPython, refactored.

from abc import ABC, abstractmethod

class Promotion(ABC):

    @abstractmethod
    def discount(self, order):
        '''Return discount as positive dollar amount'''

class FidelityPromo(Promotion):

    def discount(self, order):
        '''5% discount for customers with over 1000 points'''
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0

class BulkItemPromo(Promotion):

    def discount(self, order):
        '''10% discount on lineitems with 20 or more units'''
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount

class LargeOrderPromo(Promotion):

    def discount(self, order):
        '''7% discount if more than 10 distinct items purchased'''
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.07
        return 0