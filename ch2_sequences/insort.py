# ex 2-19 from FluentPython

import random
from bisect import insort

SIZE = 7
random.seed(1729)

out = []
for i in range(SIZE):
    item = random.randrange(SIZE * 2)
    insort(out, item)
    print('%2d ->', item, out)
