'''
Example 20-14 from Fluent Python

    >>> w = Text('forward')
    >>> w 
    Text('forward')
    >>> w.reverse()
    Text('drawrof')
    >>> w.reverse
    <bound method Text.reverse of Text('forward')>
    >>> type(w.reverse)
    <class 'method'>
    >>> Text.reverse(Text('backward'))
    Text('drawkcab')
    >>> type(Text.reverse)
    <class 'function'>
    >>> w.reverse.__func__ is Text.reverse
    True
'''

import collections

class Text(collections.UserString):

    def __repr__(self):
        return 'Text({!r})'.format(self.data)

    def reverse(self):
        return self[::-1]