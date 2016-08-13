# Example 9-7 or 9-9 from FluentPython

import math

class Vector2d:
    
    typecode = 'd'

    __slots__ = ('__x', '__y')

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __str__(self):
        return str(tuple(self))

    def __repr__(self):
        cls = type(self).__name__
        return '{}({!r}, {!r})'.format(cls, *self)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __abs__(self):
        return math.hypot(*self)

    