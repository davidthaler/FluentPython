from array import array
from random import random

SIZE = 10**7
OUTFILE = 'array.dat'

# Create array w/1M random elements
a = array('d', (random() for i in range(10**7)))
print('end of a', a[-1])

# Write it out to a file
with open(OUTFILE, 'wb') as f:
    a.tofile(f)

# Create empty double array
b = array('d')

# Read data into b
with open(OUTFILE, 'rb') as f:
    b.fromfile(f, SIZE)

print('end of b', b[-1])
print('a==b?: ', a==b)