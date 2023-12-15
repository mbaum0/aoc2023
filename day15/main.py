from dataclasses import dataclass
import math
from functools import lru_cache
from itertools import product, groupby
import time
import hashlib

input_file = "./day15/data.txt"

def part1(data):
    p1 = 0
    for d in data:
        cval = 0
        for c in d:
            cval += ord(c)
            cval *= 17
            cval %= 256
        p1 += cval
    return p1



def main():
    with open(input_file) as f:
        data = f.read()

    data = data.replace('\n', '')

    data = data.split(',')
    p1 = part1(data)
    print(p1)

if __name__ == "__main__":
    main()
