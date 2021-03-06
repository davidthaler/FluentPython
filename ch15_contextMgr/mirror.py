# Example 15-3 from Fluent Python
# The explanation here is that the string "JABBERWOCKY" is the return value
# of the __enter__ method of the context manager.

class LookingGlass:

    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please do NOT divide by zero!')
            return True

if __name__ == '__main__':
    with LookingGlass() as what:
        print('Alice, Kitty and Snowdrop')
        print(what)

    print(what)
    print('Goodbye!')