# Example 7-16 from FluentPython

import time
import functools
from clock import clock

@clock
def snooze(sec):
    time.sleep(sec)

@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

@clock 
def slow_fibo(n):
    if(n < 2):
        return n
    else:
        return slow_fibo(n-1) + slow_fibo(n-2)

@functools.lru_cache()
@clock
def fast_fibo(n):
    if(n < 2):
        return n
    else:
        return fast_fibo(n-1) + fast_fibo(n-2)

if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(0.123)')
    snooze(0.123)
    print('*' * 40, 'Calling factorial(10)')
    print('10! =', factorial(10))