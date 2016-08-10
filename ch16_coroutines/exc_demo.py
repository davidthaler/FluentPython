# Example 16-8 from Fluent Python

class DemoException(Exception):
    '''Test exception'''

def demo_handler():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received {!r}'.format(x))

