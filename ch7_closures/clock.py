# Example 7-15 from FluentPython

import time

def clock(func):

    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        et = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8f] %s(%s) -> %r' % (et, name, arg_str, result))
        return result

    return clocked