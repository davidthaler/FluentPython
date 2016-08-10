# Chain example from chapters 14 and 16
# About equivalent to itertools.chain

def chain(*iterables):
    for it in iterables:
        yield from it
