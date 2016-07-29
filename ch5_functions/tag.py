# example 5_10 from FluentPython

def tag(name, *content, cls=None, **attrs):
    """Generate HTML tags"""
    if cls is not None:
        attrs['cls'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, val)
                            for attr, val in sorted(attrs.items()))
    else:
        attr_str = ''

    if content:
        return '\n'.join('<%s%s>%s</%s>' % 
                        (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)               