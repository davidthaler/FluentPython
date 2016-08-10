# Example 15-5 from Fluent Python
# The explanation is that on __enter__, everything up to the *yield* statement runs,
# then the rest of it runs on __exit__.

# Also, the try/finally block is needed to restore system state in case of
# an exception in the client's with block

import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    try:
        yield 'JABBERWOCKY'
    finally:
        sys.stdout.write = original_write

if __name__ == '__main__':
    with looking_glass() as what:
        print('Alice, Kitty and Snowdrop')
        print(what)

    print(what)
    print('Back to normal now!')