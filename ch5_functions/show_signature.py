# Based on example 5_17 FluentPython

from inspect import signature

def show_sig(f):
    '''Print out information about the signature of a function, f()'''
    sig = signature(f)
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)
