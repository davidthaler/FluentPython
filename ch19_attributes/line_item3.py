# Example 19-18 from Fluent Python
# Relative to line_item2.py, this uses the 'classic style' 
# property declaration syntax instead of the @property decorator.

class LineItem:

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        '''Compute price'''
        return self.weight * self.price
    
    def get_weight(self):
        '''Basic accessor'''
        return self.__weight

    def set_weight(self, value):
        '''Basic mutator'''
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')
    
    weight = property(get_weight, set_weight)
