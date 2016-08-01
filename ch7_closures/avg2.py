# Example 7_14 of FluentPython

def make_averager():
    count = 0
    total = 0

    def avg(x):
        nonlocal count
        nonlocal total
        count += 1
        total += x
        return total / count

    return avg
