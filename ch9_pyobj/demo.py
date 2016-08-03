# Example 9-4 from FluentPython

class Demo:

    @classmethod
    def cls_mthd(*args):
        '''
        >>> from demo import Demo
        >>> d = Demo()
        >>> d.cls_mthd()
        (<class 'demo.Demo'>,)
        >>> d.cls_mthd('foo')
        (<class 'demo.Demo'>, 'foo')
        '''
        return args

    @staticmethod
    def stat_mthd(*args):
        '''
        >>> from demo import Demo
        >>> d = Demo()
        >>> d.stat_mthd()
        ()
        >>> d.stat_mthd('foo')
        ('foo',)
        '''
        return args
