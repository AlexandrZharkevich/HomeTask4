import time
from Task1 import TribonacciGenerator

if __name__ == '__main__':
    generator = TribonacciGenerator(35)
    for i in generator:
        print(i)
        time.sleep(0.25)
