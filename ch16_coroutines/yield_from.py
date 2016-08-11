# Example 16-7 from Fluent Python

from collections import namedtuple

Result = namedtuple('Result', 'count average')

DATA = {
    'girls:kg': [40.9, 38.5, 44.3, 42.2, 45.2],
    'girls:m' : [1.6, 1.51, 1.4, 1.3, 1.41],
    'boys:kg' : [39.0, 40.8, 43.2, 40.8, 43.1],
    'boys:m'  : [1.38, 1.5, 1.32, 1.25, 1.37],
}

# subgenerator
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)

def grouper(results, key):
    while True:
        results[key] = yield from averager()

def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)        # Needed to terminate the subgenerator

    #print(results)            # for debug
    report(results)

def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(':')
        print('{:2} {:5} averaging {:.2f}{}'.format(
            result.count, group, result.average, unit))

if __name__ == '__main__':
    main(DATA)