class TribonacciGenerator:
    def __init__(self, size):
        self.x = size

    def __iter__(self):
        a, b, c = 0, 0, 0
        sum = 0
        for i in range(self.x):
            if c == 0:
                sum = 1
            else:
                sum = a + b + c
            a, b, c = b, c, sum
            yield sum
