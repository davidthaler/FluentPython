# Example 14-11 from Fluent Python

class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        out = type(self.begin + self.step)(self.begin)
        idx = 0
        while self.end is None or out < self.end:
            yield out
            idx += 1
            out = self.begin + self.step * idx

