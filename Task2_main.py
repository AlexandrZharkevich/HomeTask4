import time
from Task2 import LeibnizGenerator

if __name__ == '__main__':
    generator = LeibnizGenerator(0.77)
    for i in generator:
        print(i)
        time.sleep(0.25)
