from dataclasses import dataclass
import math
from functools import lru_cache
from itertools import product, groupby
import time

input_file = "./day14/data.txt"

def part1(data):
    return data

def main():
    with open(input_file) as f:
        data = f.read().splitlines()

    p1 = part1(data)
    print(p1)



if __name__ == "__main__":
    main()
