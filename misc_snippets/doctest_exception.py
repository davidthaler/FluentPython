'''
This works.
The `Traceback` line has to be copied exactly, 
including the space between `Traceback` and the parenthesis.
The ... has to get its own line, if used.
The exception has to be copied exactly.

>>> d = dict()
>>> d[1]
Traceback (most recent call last):
    ...
KeyError: 1
>>> l = [1,2,3]
>>> l[3]
Traceback (most recent call last):
...
...
IndexError: list index out of range
>>> a 
Traceback (most recent call last):
NameError: name 'a' is not defined
'''
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)