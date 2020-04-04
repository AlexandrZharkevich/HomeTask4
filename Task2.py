import math


class LeibnizGenerator:
    def __init__(self, expectedSum):
        self.limit = expectedSum

    def __iter__(self):
        x = 0
        sum = 0
        while sum * 100 // 1 / 100 != self.limit:
            num = math.pow(-1, x) / (2 * x + 1)
            sum += num
            x += 1
            yield num
