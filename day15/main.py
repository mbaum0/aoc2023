from dataclasses import dataclass
import math
from functools import lru_cache
from itertools import product, groupby
import time
import hashlib

input_file = "./day15/data.txt"

def part1(grid):
    return grid

def main():
    with open(input_file) as f:
        rows = f.read().splitlines()

    grid = []
    for row in rows:
        grid.append(list(row))

    p1 = part1(grid)
    print(p1)




if __name__ == "__main__":
    main()
