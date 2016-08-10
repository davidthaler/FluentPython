# Example 16-1 from Fluent Python
# This is about the simplest possible coroutine

def simple_coroutine():
    print('-> coroutine entered')
    x = yield
    print('-> coroutine received: ', x)
