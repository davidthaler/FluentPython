# The memory test script for the Vector2d examples
# usage: python memtest.py vector2d.py
#        python memtest.py slots.py
#
# Example shows that Vector2d with __slots__ uses about 40% as much memory 
# as the one with attributes in a __dict__.

import importlib
import sys
import resource

N_VEC = 10**6

if len(sys.argv) == 2:
    mod_name = sys.argv[1].replace('.py', '')
    mod = importlib.import_module(mod_name)
else:
    print('Usage: {} <vector-module-to-test>'.format())
    sys.exit(1)

fmt = 'Vector2d type: {.__name__}.{.__name__}'
print(fmt.format(mod, mod.Vector2d))

mem_init = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print('Creating {:,} Vector2d instances'.format(N_VEC))
vectors = [mod.Vector2d(3.0, 4.0) for i in range(N_VEC)]
mem_final = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print('Inital RAM: {:14,}'.format(mem_init))
print('Final RAM: {:14,}'.format(mem_final))

