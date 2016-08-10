# Example 16-3 from Fluent Python
# See also: the running average codes from chapter 7

def averager():
    total = 0.0
    count = 0
    avg = None
    while True:
        term = yield avg
        total += term
        count += 1
        avg = total / count

