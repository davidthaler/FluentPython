# Example 7_9 of FluentPython

def make_averager():
    data = []

    def avg(val):
        data.append(val)
        return sum(data) / len(data)

    return avg