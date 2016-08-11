# Own code example of a subgenerator

import itertools

def fibgen():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

def fibstr():
    gen = fibgen()
    ct = itertools.count(1)
    yield 'Fibonacci numbers'
    while True:
        yield '%d) %d' % (next(ct), next(gen))     
