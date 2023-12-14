from dataclasses import dataclass
import math
from functools import lru_cache
from itertools import product, groupby
import time
import hashlib

input_file = "./day14/data.txt"


def roll_rows(grid):
    new_grid = []
    for row in grid:
        new_grid.append(roll_row(tuple(row)))
    return new_grid

@lru_cache(maxsize=None)
def roll_row(row):
    row = list(row)
    for i in range(len(row)):
        if i == 0:
            continue
        newI = i
        while(newI > 0 and row[newI] == 'O' and row[newI-1] == '.'):
            row[newI] = '.'
            row[newI-1] = 'O'
            newI -= 1
    return row


def rotate(grid, amt):
    mat = grid
    for _ in range(amt % 4):
        transposed = [list(row) for row in zip(*mat)]
        mat = [row[::-1] for row in transposed]

    return mat  
            

def roll(grid, direction='up'):
    if direction == 'up':
        grid = rotate(grid, 3)
        grid = roll_rows(grid)
        grid = rotate(grid, 1)
    elif direction == 'down':
        grid = rotate(grid, 1)
        grid = roll_rows(grid)
        grid = rotate(grid, 3)
    elif direction == 'left':
        grid = roll_rows(grid)

    elif direction == 'right':
        grid = rotate(grid, 2)
        grid = roll_rows(grid)
        grid = rotate(grid, 2)

    return grid

def print_grid(grid):
    for y in grid:
        print(''.join(y))
    print()

def sum_load(grid):
    sum = 0
    length = len(grid)
    for idy, y in enumerate(grid):
        for idx, x in enumerate(y):
            if grid[idy][idx] == 'O':
                sum +=  length - idy

    return sum

def part2(grid):
    cycles = 1000000000
    for i in range(cycles):
        grid = roll(grid, 'up')
        grid = roll(grid, 'left')
        grid = roll(grid, 'down')
        grid = roll(grid, 'right')
        if i % 100000 == 0:
            print(i)
    sum = sum_load(grid)
    return sum


def grid_to_str(grid):
    return ''.join([''.join(row) for row in grid])

@lru_cache(maxsize=None)
def get_hash(gridstr):
    return hashlib.md5(gridstr.encode()).hexdigest()

def part21(grid):
    # concated grid string
    hash_table = {}

    cycles = 1000000000
    ways = ["up", "left", "down", "right"]
    i = 0
    while i < cycles:
        for way in ways:
            h = get_hash(grid_to_str(grid) + way)
            if h in hash_table:
                i = cycles - (cycles - i) % (i - hash_table[h])
            else:
                hash_table[h] = i
            grid = roll(grid, way)
        i += 1
    sum = sum_load(grid)
    return sum

def part1(grid):
    print_grid(grid)
    grid = rotate(grid, 3)
    for idx, y in enumerate(grid):
        grid[idx] = roll_row(tuple(y))
    grid = rotate(grid, 1)
    sum = sum_load(grid)
    print_grid(grid)
    return sum

def main():
    with open(input_file) as f:
        rows = f.read().splitlines()

    grid = []
    for row in rows:
        grid.append(list(row))

    # p1 = part1(grid)
    # print(p1)
    # p2 = part2(grid)
    # print(p2)
    p21 = part21(grid)
    print(p21)



if __name__ == "__main__":
    main()
