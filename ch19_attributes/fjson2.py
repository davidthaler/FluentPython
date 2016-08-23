# Example 19-7
# This uses __new__ instead of @classmethod build()

from collections import abc 

class FrozenJSON:
    '''Read-only facade for attribute-like access to a dict/JSON object.'''

    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON(self.__data[name])
    
    def __getitem__(self, key):
        return FrozenJSON(self.__data[key])
